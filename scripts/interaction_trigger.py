#!/usr/bin/env python3
"""Interaction Learning retrieval and context-escape helper.

Canonical specs:
  knowledge/interaction-trigger-policy.md
  knowledge/interaction-optimization-policy.md

This script suggests routing. It never writes Interaction records and never
rewrites historical rules. Retrieval and context-escape are not persistence.

Commands:
  retrieve         --query TEXT
  classify         --event TEXT
  decide           --event TEXT
  write-gate       --event TEXT
  context-escape   --event TEXT
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

WRITE_ACTIONS = {"UPDATE_EXISTING", "CREATE_NEW", "REVIEW_CONFLICT"}

TOKEN_RE = re.compile(r"[a-z0-9]+")
INT_HEADING_RE = re.compile(r"^## (INT-\d{4}) — ", re.MULTILINE)

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
    "official",
    "linked page",
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
    "keep github-side maintenance aligned",
    "write conservatively",
    "must not automatically create",
)
CREATE_CUES = (
    "genuinely new",
    "new reusable",
    "new decision",
    "materially different",
    "no matching int",
    "context escape",
    "jump out of the loop",
    "jump out of that loop",
    "not merely follow the conversation",
    "sequence of prompts",
    "conversational recursion",
    "internal and external",
    "not forecasting the next question",
    "do not interpret proactive retrieval as merely forecasting",
)
CONFLICT_CUES = (
    "conflicts with",
    "contradicts",
    "overwrite",
    "numbering collision",
    "disputed",
    "verification status",
)
STRUCTURAL_CUES = (
    "piece seems missing",
    "something is missing",
    "missing piece",
    "belongs under",
    "wrong layer",
    "out of order",
    "order feels wrong",
    "should stay separate",
    "should remain distinct",
    "handoff",
    "boundary is unclear",
    "depends on",
    "out of sync",
    "hierarchy",
    "i don't know the database",
    "without technical",
    "ordinary language",
)
ESCAPE_CUES = (
    "context escape",
    "jump out",
    "leave the loop",
    "out of the loop",
    "going in circles",
    "repeating the same",
    "locally repetitive",
    "inefficient",
    "stop extending",
    "mirror loop",
    "conversational recursion",
    "sequence of prompts",
    "not forecasting",
    "next question",
    "internal and external",
    "both internal and external",
    "official docs",
    "search elsewhere",
    "look it up",
)
SYNTHESIS_CUES = (
    "toothpaste",
    "serial micro",
    "forward scan",
    "forward-scan",
    "compact batch",
    "periodic consolidation",
    "adjacent dependencies",
)

INTERNAL_TARGETS = (
    {
        "layer": "Interaction Learning",
        "paths": [
            "knowledge/interaction-learning.md",
            "knowledge/interaction-index.json",
            "knowledge/interaction-trigger-policy.md",
            "knowledge/interaction-optimization-policy.md",
        ],
    },
    {
        "layer": "Records / Sources / Issues",
        "paths": [
            "knowledge/chat-sync-2026-09-15.md",
            "knowledge/sync-state.json",
            "knowledge/issue-index.md",
            "knowledge/source-index.md",
        ],
    },
    {
        "layer": "Architecture References",
        "paths": [
            "knowledge/architecture-index.md",
            "knowledge/chat-sync-2026-09-15.md",
        ],
    },
    {
        "layer": "repository files/history",
        "paths": ["AGENTS.md", ".cursor/rules/", "git history"],
    },
)

EXTERNAL_TARGETS = (
    {
        "layer": "official documentation",
        "examples": [
            "NVIDIA Physical AI glossary",
            "NVIDIA OpenUSD for Developers",
            "NVIDIA PhysX SDK",
            "other official pages already in the source set",
        ],
    },
    {
        "layer": "linked pages",
        "examples": ["pages linked from official architecture or glossary nodes"],
    },
    {
        "layer": "authoritative references",
        "examples": ["cited dictionaries, standards bodies, vendor docs already indexed"],
    },
)


def tokenize(text: str) -> set[str]:
    return set(TOKEN_RE.findall(text.lower()))


def load_index() -> dict:
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))


def markdown_int_ids() -> list[str]:
    return INT_HEADING_RE.findall(RULES_PATH.read_text(encoding="utf-8"))


def rule_blob(rule: dict) -> str:
    parts = [
        rule.get("id", ""),
        rule.get("title", ""),
        rule.get("reusable_rule", ""),
        rule.get("response_strategy", ""),
        " ".join(rule.get("problem_types", [])),
        " ".join(rule.get("prompt_patterns", [])),
        " ".join(rule.get("structural_signals", [])),
        " ".join(rule.get("tags", [])),
    ]
    return " ".join(parts).lower()


def score(query: str, rule: dict) -> float:
    q = tokenize(query)
    r = tokenize(rule_blob(rule))
    if not q or not r:
        return 0.0
    overlap = q & r
    return len(overlap) / max(1, len(q))


def contains_cue(text: str, cues: tuple[str, ...]) -> bool:
    lowered = text.lower()
    return any(cue in lowered for cue in cues)


def catalog_rules() -> list[dict]:
    return list(load_index().get("rules", []))


def retrieve(query: str, limit: int = 5) -> list[dict]:
    ranked = []
    for rule in catalog_rules():
        ranked.append(
            {
                "id": rule["id"],
                "title": rule["title"],
                "score": round(score(query, rule), 4),
                "default_trigger_action": rule.get("default_trigger_action"),
                "related_rules": rule.get("related_rules", []),
            }
        )
    ranked.sort(key=lambda item: (-item["score"], item["id"]))
    return [item for item in ranked if item["score"] > 0][:limit]


def persist_block(action: str) -> dict:
    return {
        "executed": False,
        "creates_record": False,
        "rewrites_history": False,
        "persist": False,
        "write_action": action if action in WRITE_ACTIONS else "NO_WRITE",
        "note": "Helper output is routing evidence only. It does not persist Interaction records.",
    }


def classify(event: str, matches: list[dict] | None = None) -> dict:
    matches = matches if matches is not None else retrieve(event)
    top = matches[0] if matches else None
    catalog_ids = {rule["id"] for rule in catalog_rules()}
    reasons = []

    if contains_cue(event, CONFLICT_CUES):
        action = "REVIEW_CONFLICT"
        reasons.append("conflict or overwrite cue")
    elif contains_cue(event, CREATE_CUES) and (
        not top or top["id"] not in catalog_ids or top["score"] < 0.12
    ):
        action = "CREATE_NEW"
        reasons.append("new reusable pattern cue without a strong catalog match")
    elif contains_cue(event, CREATE_CUES) and top and top["id"] == "INT-0008":
        # INT-0008 already exists: later identical events version rather than mint.
        action = "UPDATE_EXISTING"
        reasons.append("context-escape pattern matches existing INT-0008")
    elif contains_cue(event, CREATE_CUES) and "INT-0008" not in catalog_ids:
        action = "CREATE_NEW"
        reasons.append("context-escape / dual-source pattern with no INT-0008 yet")
    elif contains_cue(event, UPDATE_CUES) and top:
        action = "UPDATE_EXISTING"
        reasons.append("correction/versioning cue against an existing rule")
    elif contains_cue(event, STRUCTURAL_CUES) or contains_cue(event, ESCAPE_CUES) or contains_cue(
        event, RETRIEVE_CUES
    ) or contains_cue(event, SYNTHESIS_CUES):
        action = "RETRIEVE_ONLY"
        reasons.append("structural, escape, synthesis, or retrieval cue")
    elif contains_cue(event, NO_WRITE_CUES) or not matches:
        action = "NO_INTERACTION_ACTION"
        reasons.append("no reusable interaction pattern detected")
    else:
        action = "RETRIEVE_ONLY"
        reasons.append("prior interaction logic may materially change the response")

    return {
        "action": action,
        "best_match": top,
        "matches": matches,
        "reasons": reasons,
        "structural_signal": contains_cue(event, STRUCTURAL_CUES),
        "context_escape_signal": contains_cue(event, ESCAPE_CUES),
        "dual_source_required": contains_cue(event, ESCAPE_CUES)
        or "internal" in event.lower()
        or "external" in event.lower(),
        "not_next_question_forecast": "forecast" in event.lower()
        or "next question" in event.lower()
        or contains_cue(event, ESCAPE_CUES),
        **persist_block(action),
    }


def write_gate(event: str) -> dict:
    decision = classify(event)
    allowed = decision["action"] in WRITE_ACTIONS
    return {
        "allowed": allowed,
        "action": decision["action"] if allowed else "NO_WRITE",
        "reason": (
            "Write gate satisfied only for UPDATE_EXISTING / CREATE_NEW / REVIEW_CONFLICT."
            if allowed
            else "Retrieval is not a write. Leave Interaction Learning unchanged."
        ),
        **persist_block(decision["action"] if allowed else "NO_INTERACTION_ACTION"),
        "classification": decision,
    }


def context_escape(event: str) -> dict:
    decision = classify(event)
    triggered = bool(
        decision["context_escape_signal"]
        or decision["structural_signal"]
        or decision["action"] != "NO_INTERACTION_ACTION"
    )
    return {
        "triggered": triggered,
        "stop_extending_loop": triggered,
        "not_next_question_forecast": True,
        "user_model": "structure-first retrieval strategy, not a sequence of prompts",
        "internal": list(INTERNAL_TARGETS),
        "external": list(EXTERNAL_TARGETS),
        "retrieved_rules": decision["matches"],
        "consolidated_answer_contract": [
            "stop extending the current mirror loop",
            "retrieve INTERNAL and EXTERNAL sources together",
            "return one structural answer",
            "do not treat retrieval as forecasting the next user question",
            "do not persist a record because retrieval ran",
        ],
        "prefer_over_in_loop_forward_scan": triggered,
        **persist_block("NO_INTERACTION_ACTION"),
        "classification": {
            "action": decision["action"],
            "best_match": decision["best_match"],
            "reasons": decision["reasons"],
        },
    }


def emit(payload: dict) -> None:
    json.dump(payload, sys.stdout, indent=2, ensure_ascii=True)
    sys.stdout.write("\n")


def cmd_self_test() -> int:
    failures: list[str] = []
    index = load_index()
    catalog_ids = [rule["id"] for rule in index.get("rules", [])]
    md_ids = markdown_int_ids()

    if catalog_ids != md_ids:
        failures.append(f"catalog/markdown INT mismatch: {catalog_ids} vs {md_ids}")
    if "INT-0008" not in catalog_ids:
        failures.append("catalog missing INT-0008")
    if index.get("retrieval_does_not_persist") is not True:
        failures.append("catalog must declare retrieval_does_not_persist")
    if index.get("context_escape_does_not_persist") is not True:
        failures.append("catalog must declare context_escape_does_not_persist")

    scope = index.get("retrieval_scope", {})
    if "Interaction Learning" not in scope.get("internal", []):
        failures.append("internal retrieval scope missing Interaction Learning")
    if "official documentation" not in scope.get("external", []):
        failures.append("external retrieval scope missing official documentation")

    no_action = classify("Fix a typo in changelog whitespace only. No new pattern.")
    if no_action["action"] != "NO_INTERACTION_ACTION" or no_action["creates_record"]:
        failures.append(f"typo event should be NO_INTERACTION_ACTION, got {no_action['action']}")

    retrieve_only = classify(
        "A piece seems missing and the order feels wrong, but I don't know the database terms."
    )
    if retrieve_only["action"] != "RETRIEVE_ONLY" or retrieve_only["creates_record"]:
        failures.append(f"structural NL event should be RETRIEVE_ONLY, got {retrieve_only['action']}")

    toothpaste = classify(
        "Stop toothpaste-style serial micro-decisions. Perform a local forward scan "
        "and prefer one compact batch recommendation."
    )
    if toothpaste["best_match"] and toothpaste["best_match"]["id"] not in {"INT-0007", "INT-0006"}:
        failures.append(f"toothpaste event expected INT-0007, got {toothpaste['best_match']}")

    escape_event = (
        "The user does not merely follow the conversation forward. They jump OUT of "
        "the loop to retrieve from both internal and external sources. Trigger a "
        "context escape. Retrieval is not forecasting the next question. Do not "
        "model the user only as a sequence of prompts."
    )
    escape = classify(escape_event)
    if not escape["best_match"] or escape["best_match"]["id"] != "INT-0008":
        failures.append(f"context-escape event expected INT-0008, got {escape['best_match']}")
    if escape["action"] not in {"UPDATE_EXISTING", "CREATE_NEW", "RETRIEVE_ONLY"}:
        failures.append(f"context-escape event unexpected action {escape['action']}")
    if escape["creates_record"] or escape["rewrites_history"]:
        failures.append("classify must not persist or rewrite history")

    plan = context_escape(escape_event)
    if not plan["triggered"] or not plan["stop_extending_loop"]:
        failures.append("context-escape must stop extending the loop")
    if plan["creates_record"] or plan["persist"] or plan["rewrites_history"]:
        failures.append("context-escape must not persist or rewrite history")
    if not plan["internal"] or not plan["external"]:
        failures.append("context-escape must return internal and external targets")
    if not plan["not_next_question_forecast"]:
        failures.append("context-escape must reject next-question forecasting")

    gate = write_gate("ordinary factual question about a definition, no new pattern")
    if gate["allowed"] or gate["creates_record"]:
        failures.append("write-gate must block ordinary factual events")

    if failures:
        emit({"ok": False, "failures": failures})
        return 1
    emit(
        {
            "ok": True,
            "cases": 8,
            "catalog": catalog_ids,
            "retrieval_does_not_persist": True,
            "context_escape_does_not_persist": True,
        }
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("retrieve", "classify", "decide", "write-gate", "context-escape"):
        item = sub.add_parser(name)
        if name == "retrieve":
            item.add_argument("--query", required=True)
            item.add_argument("--limit", type=int, default=5)
        else:
            item.add_argument("--event", required=True)
    sub.add_parser("self-test")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "retrieve":
        emit(
            {
                "matches": retrieve(args.query, args.limit),
                "internal": list(INTERNAL_TARGETS),
                "external": list(EXTERNAL_TARGETS),
                **persist_block("NO_INTERACTION_ACTION"),
            }
        )
        return 0
    if args.command == "classify":
        emit(classify(args.event))
        return 0
    if args.command == "decide":
        emit(classify(args.event))
        return 0
    if args.command == "write-gate":
        emit(write_gate(args.event))
        return 0
    if args.command == "context-escape":
        emit(context_escape(args.event))
        return 0
    if args.command == "self-test":
        return cmd_self_test()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
