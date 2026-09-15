#!/usr/bin/env python3
"""Interaction Learning retrieval trigger helper.

Canonical spec: knowledge/interaction-trigger-policy.md

This script suggests a routing outcome. It does not write Interaction records
and does not replace the canonical policy.

Commands:
  retrieve  --query TEXT
  classify  --event TEXT
  decide    --event TEXT
  self-test
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "knowledge" / "interaction-index.json"
RULES_PATH = ROOT / "knowledge" / "interaction-learning.md"

ACTIONS = (
    "NO_INTERACTION_ACTION",
    "RETRIEVE_ONLY",
    "UPDATE_EXISTING",
    "CREATE_NEW",
    "REVIEW_CONFLICT",
)

TOKEN_RE = re.compile(r"[a-z0-9]+")
INT_HEADING_RE = re.compile(r"^## (INT-\d{4}) — ", re.MULTILINE)

# Cue lists operationalize the published trigger policy. Changing them in a
# way that rewrites Stage 0 outcomes is a high-impact heuristic change.
NO_WRITE_CUES = (
    "formatting",
    "whitespace",
    "typo",
    "changelog only",
    "status comment",
    "notification",
    "no new pattern",
    "ordinary factual",
)
RETRIEVE_CUES = (
    "missing",
    "duplicate",
    "inconsistent",
    "stale",
    "wrongly classified",
    "synchron",
    "architecture",
    "retrieve",
    "existing rule",
    "already covered",
    "maintenance",
    "index",
    "workflow",
)
UPDATE_CUES = (
    "version",
    "update existing",
    "refine",
    "narrow",
    "strengthen",
    "correct an existing",
    "same problem type",
    "near-duplicate",
    "operationalize",
)
CREATE_CUES = (
    "genuinely new",
    "new reusable",
    "new decision",
    "materially different",
    "no matching int",
)
CONFLICT_CUES = (
    "conflicts with",
    "contradicts",
    "overwrite",
    "numbering collision",
    "disputed",
    "verification status",
)


def tokenize(text: str) -> set[str]:
    return {token for token in TOKEN_RE.findall(text.lower()) if len(token) > 1}


def load_index() -> dict:
    if not INDEX_PATH.exists():
        raise SystemExit(f"missing retrieval catalog: {INDEX_PATH}")
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))


def markdown_int_ids() -> list[str]:
    if not RULES_PATH.exists():
        return []
    return INT_HEADING_RE.findall(RULES_PATH.read_text(encoding="utf-8"))


def rule_blob(rule: dict) -> str:
    parts = [
        rule.get("id", ""),
        rule.get("title", ""),
        " ".join(rule.get("problem_types", [])),
        " ".join(rule.get("prompt_patterns", [])),
        " ".join(rule.get("tags", [])),
        rule.get("reusable_rule", ""),
        rule.get("response_strategy", ""),
    ]
    return " ".join(parts)


def score(query: str, rule: dict) -> float:
    query_tokens = tokenize(query)
    rule_tokens = tokenize(rule_blob(rule))
    if not query_tokens or not rule_tokens:
        return 0.0
    overlap = query_tokens & rule_tokens
    # Jaccard keeps short maintenance queries from matching everything.
    return len(overlap) / len(query_tokens | rule_tokens)


def retrieve(query: str, limit: int = 5) -> list[dict]:
    catalog = load_index()
    ranked = []
    for rule in catalog.get("rules", []):
        ranked.append(
            {
                "id": rule["id"],
                "title": rule["title"],
                "status": rule.get("status"),
                "default_trigger_action": rule.get("default_trigger_action"),
                "score": round(score(query, rule), 4),
                "related_rules": rule.get("related_rules", []),
            }
        )
    ranked.sort(key=lambda item: item["score"], reverse=True)
    return [item for item in ranked if item["score"] > 0][:limit]


def contains_cue(text: str, cues: tuple[str, ...]) -> bool:
    lowered = text.lower()
    return any(cue in lowered for cue in cues)


def classify(event: str, matches: list[dict] | None = None) -> dict:
    """Suggest a Stage 0 outcome from the published policy, plus retrieval scores."""
    matches = matches if matches is not None else retrieve(event)
    best = matches[0] if matches else None
    best_score = best["score"] if best else 0.0
    second_score = matches[1]["score"] if len(matches) > 1 else 0.0

    if contains_cue(event, CONFLICT_CUES):
        action = "REVIEW_CONFLICT"
        reason = "Event language indicates a conflict with an existing rule or claim."
    elif contains_cue(event, CREATE_CUES) and best_score < 0.22:
        action = "CREATE_NEW"
        reason = "Event claims a new reusable pattern and retrieval overlap is low."
    elif contains_cue(event, UPDATE_CUES) and best_score >= 0.08:
        action = "UPDATE_EXISTING"
        reason = "Event strengthens or versions a close existing rule."
    elif best_score >= 0.08 or contains_cue(event, RETRIEVE_CUES):
        action = "RETRIEVE_ONLY"
        reason = "Existing Interaction rules can materially affect the response; write gate not clearly satisfied."
    elif contains_cue(event, NO_WRITE_CUES) or best_score == 0.0:
        action = "NO_INTERACTION_ACTION"
        reason = "No recurring workflow pattern or retrieval hit requiring Interaction work."
    else:
        action = "RETRIEVE_ONLY"
        reason = "Default to retrieval without writing."

    # Near-ties between two ACTIVE rules with conflict language stay REVIEW_CONFLICT.
    if (
        action != "REVIEW_CONFLICT"
        and best
        and second_score > 0
        and abs(best_score - second_score) < 0.01
        and contains_cue(event, CONFLICT_CUES)
    ):
        action = "REVIEW_CONFLICT"
        reason = "Two close matches plus conflict language; do not overwrite."

    return {
        "action": action,
        "reason": reason,
        "best_match": best,
        "matches": matches,
        "write_gate": action in {"UPDATE_EXISTING", "CREATE_NEW", "REVIEW_CONFLICT"},
    }


def emit(payload: dict) -> None:
    json.dump(payload, sys.stdout, indent=2, ensure_ascii=True)
    sys.stdout.write("\n")


def cmd_self_test() -> int:
    catalog = load_index()
    indexed_ids = [rule["id"] for rule in catalog.get("rules", [])]
    markdown_ids = markdown_int_ids()
    missing = [rule_id for rule_id in markdown_ids if rule_id not in indexed_ids]
    extra = [rule_id for rule_id in indexed_ids if rule_id not in markdown_ids]
    failures = []
    if missing:
        failures.append(f"index missing markdown rules: {missing}")
    if extra:
        failures.append(f"index has rules absent from markdown: {extra}")

    cases = [
        (
            "PhysX exists as a source but the architecture-reference layer has no node",
            "INT-0001",
            {"RETRIEVE_ONLY", "UPDATE_EXISTING"},
        ),
        (
            "Completion language implied Airtable persistence without tool execution",
            "INT-0002",
            {"RETRIEVE_ONLY", "UPDATE_EXISTING"},
        ),
        (
            "User forgot the record number and reposted overlapping content",
            "INT-0003",
            {"RETRIEVE_ONLY", "UPDATE_EXISTING"},
        ),
        (
            "Ordinary factual question about OpenUSD file extensions, no new pattern",
            None,
            {"NO_INTERACTION_ACTION"},
        ),
        (
            "Implement automatic retrieval trigger; do not create an interaction for every event; classify first and retrieve similar existing rules",
            "INT-0005",
            {"RETRIEVE_ONLY", "UPDATE_EXISTING"},
        ),
        (
            "Current user feedback conflicts with an active interaction rule and would overwrite INT-0001",
            "INT-0001",
            {"REVIEW_CONFLICT"},
        ),
    ]

    for event, expected_id, allowed_actions in cases:
        decision = classify(event)
        if decision["action"] not in allowed_actions:
            failures.append(
                f"{event!r}: action {decision['action']} not in {sorted(allowed_actions)}"
            )
        if expected_id:
            match_ids = [item["id"] for item in decision["matches"][:3]]
            if expected_id not in match_ids:
                failures.append(f"{event!r}: expected {expected_id} in {match_ids}")

    if failures:
        emit({"ok": False, "failures": failures})
        return 1
    emit(
        {
            "ok": True,
            "indexed_ids": indexed_ids,
            "markdown_ids": markdown_ids,
            "tested_cases": len(cases),
        }
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    retrieve_cmd = sub.add_parser("retrieve", help="Rank similar INT rules")
    retrieve_cmd.add_argument("--query", required=True)
    retrieve_cmd.add_argument("--limit", type=int, default=5)

    classify_cmd = sub.add_parser("classify", help="Suggest a Stage 0 outcome")
    classify_cmd.add_argument("--event", required=True)

    decide_cmd = sub.add_parser("decide", help="Retrieve then classify")
    decide_cmd.add_argument("--event", required=True)

    sub.add_parser("self-test", help="Check catalog completeness and routing examples")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "retrieve":
        emit({"query": args.query, "matches": retrieve(args.query, limit=args.limit)})
        return 0
    if args.command == "classify":
        emit(classify(args.event))
        return 0
    if args.command == "decide":
        emit(classify(args.event))
        return 0
    if args.command == "self-test":
        return cmd_self_test()
    parser.error("unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
