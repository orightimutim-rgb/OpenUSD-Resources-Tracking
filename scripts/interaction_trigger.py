#!/usr/bin/env python3
"""Interaction Learning retrieval, forward-scan, and consolidation helper.

Canonical specs:
  knowledge/interaction-trigger-policy.md
  knowledge/interaction-optimization-policy.md

This script suggests routing and review outputs. It never writes Interaction
records and never rewrites historical rules. Retrieval, forward-scan, and
consolidation are separate from persistence.

Commands:
  retrieve      --query TEXT
  classify      --event TEXT
  decide        --event TEXT
  write-gate    --event TEXT
  forward-scan  --event TEXT
  consolidate
  self-test
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "knowledge" / "interaction-index.json"
RULES_PATH = ROOT / "knowledge" / "interaction-learning.md"
CHAT_SYNC_PATH = ROOT / "knowledge" / "chat-sync-2026-09-15.md"
AGENTS_PATH = ROOT / "AGENTS.md"
OPT_POLICY_PATH = ROOT / "knowledge" / "interaction-optimization-policy.md"
TRIGGER_POLICY_PATH = ROOT / "knowledge" / "interaction-trigger-policy.md"
MAINT_RULE_PATH = ROOT / ".cursor" / "rules" / "github-sync-maintenance.mdc"

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
INT_MENTION_RE = re.compile(r"INT-\d{4}")

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
    "keep github-side maintenance aligned",
    "write conservatively",
    "must not automatically create",
    "forward scan",
    "forward-scan",
    "compact batch",
    "periodic consolidation",
    "toothpaste",
    "serial micro",
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

# Ordinary-language structural observations from INT-0006 / trigger policy.
# These are retrieval signals, not automatic persist signals.
STRUCTURAL_CUES = (
    "piece seems missing",
    "a piece is missing",
    "something is missing",
    "missing piece",
    "extra part",
    "belongs under",
    "wrong layer",
    "out of order",
    "order feels wrong",
    "the order is wrong",
    "should come first",
    "not connected",
    "should be linked",
    "should stay separate",
    "should remain distinct",
    "handoff",
    "boundary is unclear",
    "the boundary",
    "depends on",
    "these two things",
    "not the same thing",
    "mixed together",
    "out of sync",
    "not in sync",
    "not lined up",
    "gap between",
    "hierarchy",
    "i don't know the database",
    "don't know the schema",
    "without technical",
    "ordinary language",
    "one piece at a time",
    "catch the next missing",
    "next missing piece",
)

# INT-0007 synthesis signals. Retrieval/review, not automatic persist.
SYNTHESIS_CUES = (
    "toothpaste",
    "serial micro",
    "one piece at a time",
    "forward scan",
    "forward-scan",
    "compact batch",
    "combined recommendation",
    "periodic consolidation",
    "silently rewrite historical",
    "adjacent dependencies",
    "downstream gaps",
    "merge candidates",
    "review candidates",
)

MAINTENANCE_SURFACES = (
    "knowledge/interaction-learning.md",
    "knowledge/interaction-index.json",
    "knowledge/interaction-trigger-policy.md",
    "knowledge/interaction-optimization-policy.md",
    "knowledge/chat-sync-2026-09-15.md",
    "knowledge/sync-policy.md",
    "knowledge/sync-state.json",
    "AGENTS.md",
    ".cursor/rules/github-sync-maintenance.mdc",
    ".cursor/rules/interaction-trigger.mdc",
)

# Known GitHub-side review items. Listed for consolidation reports only;
# this helper does not resolve them.
KNOWN_REVIEW_CANDIDATES = (
    {
        "id": "REV-INT-0005-NUMBERING",
        "status": "APPROVAL_REQUIRED",
        "cluster": ["INT-0005"],
        "summary": (
            "Open PR #2 drafts INT-0005 as the owner approval/notification protocol, "
            "while main already uses INT-0005 for retrieval/write gating."
        ),
        "recommended_handling": (
            "Do not silently re-number or overwrite either rule. Rebase PR #2 onto "
            "an unused INT ID only after explicit owner approval."
        ),
    },
    {
        "id": "REV-INT-0004-0005-0007-CLUSTER",
        "status": "REVIEW_CANDIDATE",
        "cluster": ["INT-0004", "INT-0005", "INT-0006", "INT-0007"],
        "summary": (
            "Retrieval (INT-0004), routing/write-gating (INT-0005), structure-first "
            "signals (INT-0006), and proactive synthesis/consolidation (INT-0007) "
            "are related layers, not one rule."
        ),
        "recommended_handling": (
            "Keep the four rules distinct. Do not merge them into a single INT. "
            "Related-rule links are sufficient."
        ),
    },
    {
        "id": "REV-OPEN-OPERATIONALIZATION-PRS",
        "status": "REVIEW_CANDIDATE",
        "cluster": ["INT-0005", "INT-0006", "INT-0007"],
        "summary": (
            "Open PRs #3 and #4 operationalize earlier Interaction trigger work on "
            "older bases. This branch rebases that operationalization onto current "
            "main, including INT-0007."
        ),
        "recommended_handling": (
            "Do not silently close or rewrite those PRs. Treat overlapping helper/"
            "catalog files as a rebase cluster for owner review."
        ),
    },
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
        " ".join(rule.get("structural_signals", [])),
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
    return len(overlap) / len(query_tokens | rule_tokens)


def contains_cue(text: str, cues: tuple[str, ...]) -> bool:
    lowered = text.lower()
    return any(cue in lowered for cue in cues)


def catalog_rules() -> list[dict]:
    return list(load_index().get("rules", []))


def rule_by_id() -> dict[str, dict]:
    return {rule["id"]: rule for rule in catalog_rules()}


def retrieve(query: str, limit: int = 5) -> list[dict]:
    ranked = []
    for rule in catalog_rules():
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
    if contains_cue(query, STRUCTURAL_CUES):
        for item in ranked:
            if item["id"] == "INT-0006" and item["score"] < 0.12:
                item["score"] = 0.12
    if contains_cue(query, SYNTHESIS_CUES):
        for item in ranked:
            if item["id"] == "INT-0007" and item["score"] < 0.14:
                item["score"] = 0.14
    ranked.sort(key=lambda item: item["score"], reverse=True)
    return [item for item in ranked if item["score"] > 0][:limit]


def persist_block(action: str) -> dict:
    """Retrieval helpers never persist. write_gate is a suggestion only."""
    suggested_mode = {
        "NO_INTERACTION_ACTION": "none",
        "RETRIEVE_ONLY": "none",
        "UPDATE_EXISTING": "version_existing",
        "CREATE_NEW": "create_new",
        "REVIEW_CONFLICT": "review_conflict",
    }[action]
    return {
        "executed": False,
        "creates_record": False,
        "rewrites_history": False,
        "write_gate_satisfied": action in WRITE_ACTIONS,
        "suggested_mode": suggested_mode,
        "history_policy": "additive_versioned",
        "note": (
            "This helper never writes Interaction records and never rewrites "
            "historical rules. Persistence is a later gated step."
        ),
    }


def classify(event: str, matches: list[dict] | None = None) -> dict:
    """Suggest a Stage 0 outcome from the published policy, plus retrieval scores."""
    matches = matches if matches is not None else retrieve(event)
    best = matches[0] if matches else None
    best_score = best["score"] if best else 0.0
    second_score = matches[1]["score"] if len(matches) > 1 else 0.0
    structural = contains_cue(event, STRUCTURAL_CUES)
    synthesis = contains_cue(event, SYNTHESIS_CUES)

    if contains_cue(event, CONFLICT_CUES):
        action = "REVIEW_CONFLICT"
        reason = "Event language indicates a conflict with an existing rule or claim."
    elif contains_cue(event, CREATE_CUES) and best_score < 0.22:
        action = "CREATE_NEW"
        reason = "Event claims a new reusable pattern and retrieval overlap is low."
    elif contains_cue(event, UPDATE_CUES) and best_score >= 0.08:
        action = "UPDATE_EXISTING"
        reason = "Event strengthens or versions a close existing rule."
    elif best_score >= 0.08 or contains_cue(event, RETRIEVE_CUES) or structural or synthesis:
        action = "RETRIEVE_ONLY"
        reason = (
            "Existing Interaction rules or a structure-first/synthesis signal can "
            "materially affect the response; write gate not clearly satisfied."
        )
    elif contains_cue(event, NO_WRITE_CUES) or best_score == 0.0:
        action = "NO_INTERACTION_ACTION"
        reason = "No recurring workflow pattern or retrieval hit requiring Interaction work."
    else:
        action = "RETRIEVE_ONLY"
        reason = "Default to retrieval without writing."

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
        "structure_first_signal": structural,
        "synthesis_signal": synthesis,
        "retrieval": {
            "executed": True,
            "creates_record": False,
        },
        "persistence": persist_block(action),
    }


def mentioned_int_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return set(INT_MENTION_RE.findall(path.read_text(encoding="utf-8")))


def file_exists_notes() -> list[dict]:
    notes = []
    for relative in MAINTENANCE_SURFACES:
        path = ROOT / relative
        notes.append({"path": relative, "present": path.exists()})
    return notes


def adjacent_from_matches(matches: list[dict]) -> list[dict]:
    catalog = rule_by_id()
    seen: dict[str, dict] = {}
    for match in matches:
        for related_id in match.get("related_rules", []):
            if related_id == match["id"] or related_id in {item["id"] for item in matches}:
                continue
            rule = catalog.get(related_id)
            if not rule:
                seen[related_id] = {
                    "id": related_id,
                    "title": None,
                    "via": match["id"],
                    "gap": "related_rule_missing_from_catalog",
                }
                continue
            seen.setdefault(
                related_id,
                {
                    "id": related_id,
                    "title": rule.get("title"),
                    "via": match["id"],
                    "status": rule.get("status"),
                    "reusable_rule": rule.get("reusable_rule"),
                },
            )
    return list(seen.values())


def downstream_gaps(matches: list[dict]) -> list[dict]:
    markdown_ids = markdown_int_ids()
    indexed_ids = [rule["id"] for rule in catalog_rules()]
    chat_ids = mentioned_int_ids(CHAT_SYNC_PATH)
    agents_ids = mentioned_int_ids(AGENTS_PATH)
    gaps = []

    missing_from_index = [rule_id for rule_id in markdown_ids if rule_id not in indexed_ids]
    if missing_from_index:
        gaps.append(
            {
                "surface": "knowledge/interaction-index.json",
                "gap": "catalog missing markdown Interaction IDs",
                "ids": missing_from_index,
            }
        )

    extra_in_index = [rule_id for rule_id in indexed_ids if rule_id not in markdown_ids]
    if extra_in_index:
        gaps.append(
            {
                "surface": "knowledge/interaction-index.json",
                "gap": "catalog has IDs absent from markdown",
                "ids": extra_in_index,
            }
        )

    if CHAT_SYNC_PATH.exists():
        missing_chat = [rule_id for rule_id in markdown_ids if rule_id not in chat_ids]
        if missing_chat:
            gaps.append(
                {
                    "surface": "knowledge/chat-sync-2026-09-15.md",
                    "gap": "representative Interaction list is behind markdown rules",
                    "ids": missing_chat,
                }
            )

    if not OPT_POLICY_PATH.exists():
        gaps.append(
            {
                "surface": "knowledge/interaction-optimization-policy.md",
                "gap": "optimization policy file missing",
                "ids": ["INT-0007"],
            }
        )

    if AGENTS_PATH.exists() and "INT-0007" in markdown_ids and "forward" not in AGENTS_PATH.read_text(encoding="utf-8").lower():
        gaps.append(
            {
                "surface": "AGENTS.md",
                "gap": "agent instructions do not yet bind local forward-scan / consolidation",
                "ids": ["INT-0007"],
            }
        )

    if MAINT_RULE_PATH.exists():
        maint_text = MAINT_RULE_PATH.read_text(encoding="utf-8").lower()
        if "forward" not in maint_text or "consolidat" not in maint_text:
            gaps.append(
                {
                    "surface": ".cursor/rules/github-sync-maintenance.mdc",
                    "gap": "maintenance rule does not yet bind forward-scan / consolidation",
                    "ids": ["INT-0007"],
                }
            )

    if agents_ids and "INT-0007" in markdown_ids and "optimization" not in AGENTS_PATH.read_text(encoding="utf-8").lower():
        gaps.append(
            {
                "surface": "AGENTS.md",
                "gap": "optimization policy is not in the required knowledge order",
                "ids": ["INT-0007"],
            }
        )

    match_ids = [item["id"] for item in matches]
    if "INT-0007" in match_ids and TRIGGER_POLICY_PATH.exists():
        trigger_text = TRIGGER_POLICY_PATH.read_text(encoding="utf-8").lower()
        if "forward-scan" not in trigger_text and "forward scan" not in trigger_text:
            gaps.append(
                {
                    "surface": "knowledge/interaction-trigger-policy.md",
                    "gap": "decision sequence does not yet name the local forward-scan step",
                    "ids": ["INT-0007"],
                }
            )

    return gaps


def compact_recommendation(event: str, decision: dict, adjacent: list[dict], gaps: list[dict]) -> dict:
    best = decision.get("best_match") or {}
    confident = []
    review = []

    if decision["action"] in {"RETRIEVE_ONLY", "UPDATE_EXISTING"} and best.get("id"):
        confident.append(
            f"Reuse {best['id']} ({best.get('title')}); do not create a new Interaction ID."
        )
    if decision["action"] == "UPDATE_EXISTING":
        confident.append(
            "Append a GitHub-side version note and bind existing policy files; do not replace prior rule text."
        )
    if gaps:
        confident.append(
            "Update the listed adjacent maintenance surfaces in one batch rather than serial follow-up turns."
        )
    if adjacent:
        confident.append(
            "Retrieve related rules "
            + ", ".join(item["id"] for item in adjacent)
            + " as context; keep them distinct."
        )

    for candidate in KNOWN_REVIEW_CANDIDATES:
        review.append(
            {
                "id": candidate["id"],
                "status": candidate["status"],
                "summary": candidate["summary"],
            }
        )
    if decision["action"] == "REVIEW_CONFLICT":
        review.append(
            {
                "id": "REV-CURRENT-EVENT",
                "status": "APPROVAL_REQUIRED",
                "summary": decision["reason"],
            }
        )

    return {
        "current_issue": event,
        "recommended_combined_change": confident,
        "leave_unchanged": [
            "Canonical Stage 0 outcomes",
            "ISSUE-0001 through ISSUE-0010 verification status",
            "Historical Interaction rule text (append only)",
            "Airtable records (no GitHub-side Airtable write in this helper)",
        ],
        "review_candidates": review,
        "maintenance_implication": (
            "Additive/versioned Interaction storage requires periodic consolidation "
            "reports; do not silently merge or delete historical rules."
        ),
    }


def forward_scan(event: str) -> dict:
    decision = classify(event)
    adjacent = adjacent_from_matches(decision["matches"])
    gaps = downstream_gaps(decision["matches"])
    recommendation = compact_recommendation(event, decision, adjacent, gaps)
    return {
        "action": decision["action"],
        "reason": decision["reason"],
        "best_match": decision["best_match"],
        "retrieved_rules": decision["matches"],
        "adjacent_dependencies": adjacent,
        "likely_downstream_gaps": gaps,
        "maintenance_surfaces": file_exists_notes(),
        "compact_recommendation": recommendation,
        "structure_first_signal": decision["structure_first_signal"],
        "synthesis_signal": decision["synthesis_signal"],
        "retrieval": {"executed": True, "creates_record": False},
        "persistence": persist_block(decision["action"]),
    }


def pairwise_overlap() -> list[dict]:
    rules = catalog_rules()
    pairs = []
    for index, left in enumerate(rules):
        left_tokens = tokenize(rule_blob(left))
        for right in rules[index + 1 :]:
            right_tokens = tokenize(rule_blob(right))
            if not left_tokens or not right_tokens:
                continue
            overlap = left_tokens & right_tokens
            jaccard = len(overlap) / len(left_tokens | right_tokens)
            pairs.append(
                {
                    "left": left["id"],
                    "right": right["id"],
                    "score": round(jaccard, 4),
                    "shared_tags": sorted(set(left.get("tags", [])) & set(right.get("tags", []))),
                }
            )
    pairs.sort(key=lambda item: item["score"], reverse=True)
    return pairs


def related_clusters() -> list[dict]:
    graph: dict[str, set[str]] = defaultdict(set)
    titles = {}
    for rule in catalog_rules():
        titles[rule["id"]] = rule.get("title")
        for related in rule.get("related_rules", []):
            graph[rule["id"]].add(related)
            graph[related].add(rule["id"])
    seen: set[str] = set()
    clusters = []
    for start in sorted(graph):
        if start in seen:
            continue
        stack = [start]
        component: set[str] = set()
        while stack:
            node = stack.pop()
            if node in component:
                continue
            component.add(node)
            seen.add(node)
            stack.extend(graph[node] - component)
        if len(component) > 1:
            clusters.append(
                {
                    "ids": sorted(component),
                    "titles": {rule_id: titles.get(rule_id) for rule_id in sorted(component)},
                    "handling": "Related cluster. Keep distinct unless owner approves a merge.",
                }
            )
    return clusters


def stale_response_strategies() -> list[dict]:
    stale = []
    for rule in catalog_rules():
        strategy = (rule.get("response_strategy") or "").strip()
        if not strategy:
            stale.append(
                {
                    "id": rule["id"],
                    "reason": "response_strategy is empty in the retrieval catalog",
                }
            )
    return stale


def superseded_candidates() -> list[dict]:
    superseded = []
    for rule in catalog_rules():
        if rule.get("status") == "HISTORICAL":
            superseded.append(
                {
                    "id": rule["id"],
                    "reason": "status is HISTORICAL; retain for provenance, do not delete",
                }
            )
    return superseded


def consolidate() -> dict:
    pairs = pairwise_overlap()
    near_duplicates = [pair for pair in pairs if pair["score"] >= 0.35]
    merge_candidates = [pair for pair in pairs if 0.22 <= pair["score"] < 0.35]
    return {
        "cadence_hint": (
            "High-change period on 2026-09-15: more frequent review is appropriate. "
            "Otherwise use monthly (low volume) or weekly (medium volume)."
        ),
        "near_duplicates": near_duplicates,
        "merge_candidates": merge_candidates,
        "related_clusters": related_clusters(),
        "superseded_candidates": superseded_candidates(),
        "stale_response_strategies": stale_response_strategies(),
        "conflict_clusters": list(KNOWN_REVIEW_CANDIDATES),
        "auto_applied": [],
        "review_required": True,
        "history_policy": "additive_versioned",
        "rewrites_history": False,
        "retrieval": {"executed": True, "creates_record": False},
        "persistence": {
            "executed": False,
            "creates_record": False,
            "rewrites_history": False,
            "note": "consolidate emits a review report only; it does not merge or delete rules.",
        },
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
    if catalog.get("retrieval_does_not_persist") is not True:
        failures.append("catalog must declare retrieval_does_not_persist=true")
    if catalog.get("consolidation_does_not_rewrite") is not True:
        failures.append("catalog must declare consolidation_does_not_rewrite=true")

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
        (
            "A piece seems missing and the order feels wrong. These two things should stay separate, but I don't know the database terms.",
            "INT-0006",
            {"RETRIEVE_ONLY", "UPDATE_EXISTING"},
        ),
        (
            "Automatic retrieval must not automatically create Interaction records. Retrieve broadly, write conservatively. Keep GitHub-side maintenance aligned.",
            "INT-0005",
            {"UPDATE_EXISTING", "RETRIEVE_ONLY"},
        ),
        (
            "Flag any conflict as APPROVAL REQUIRED rather than silently rewriting history. Keep GitHub-side maintenance aligned with retrieve broadly, write conservatively.",
            "INT-0005",
            {"UPDATE_EXISTING", "RETRIEVE_ONLY"},
        ),
        (
            "Stop toothpaste-style serial micro-decisions. When one structural issue is detected, perform a local forward scan and prefer one compact batch recommendation. Keep GitHub-side maintenance aligned.",
            "INT-0007",
            {"UPDATE_EXISTING", "RETRIEVE_ONLY"},
        ),
        (
            "Add periodic consolidation as a maintenance responsibility. Consolidation should detect near-duplicates and merge candidates while preserving provenance. Do not silently rewrite historical rules.",
            "INT-0007",
            {"UPDATE_EXISTING", "RETRIEVE_ONLY"},
        ),
        (
            "You keep going one piece at a time and I have to catch the next missing piece.",
            "INT-0007",
            {"RETRIEVE_ONLY", "UPDATE_EXISTING"},
        ),
    ]

    for event, expected_id, allowed_actions in cases:
        decision = classify(event)
        if decision["action"] not in allowed_actions:
            failures.append(
                f"{event!r}: action {decision['action']} not in {sorted(allowed_actions)}"
            )
        if decision["retrieval"]["creates_record"] or decision["persistence"]["executed"]:
            failures.append(f"{event!r}: retrieval/classify must not persist")
        if decision["persistence"].get("rewrites_history"):
            failures.append(f"{event!r}: helper must not rewrite history")
        if expected_id:
            match_ids = [item["id"] for item in decision["matches"][:3]]
            if expected_id not in match_ids:
                failures.append(f"{event!r}: expected {expected_id} in {match_ids}")

    scan = forward_scan(
        "Stop toothpaste-style serial micro-decisions. Perform a local forward scan "
        "and add periodic consolidation. Do not silently rewrite historical rules. "
        "Keep GitHub-side maintenance aligned."
    )
    if scan["persistence"]["executed"] or scan["persistence"]["rewrites_history"]:
        failures.append("forward-scan must not persist or rewrite history")
    scan_ids = [item["id"] for item in scan["retrieved_rules"][:3]]
    if "INT-0007" not in scan_ids:
        failures.append(f"forward-scan expected INT-0007 in {scan_ids}")
    if "compact_recommendation" not in scan:
        failures.append("forward-scan must return a compact recommendation")

    report = consolidate()
    if report["auto_applied"] or report["persistence"]["executed"] or report["rewrites_history"]:
        failures.append("consolidate must not auto-apply, persist, or rewrite history")
    if report["review_required"] is not True:
        failures.append("consolidate must require review")

    if failures:
        emit({"ok": False, "failures": failures})
        return 1
    emit(
        {
            "ok": True,
            "indexed_ids": indexed_ids,
            "markdown_ids": markdown_ids,
            "tested_cases": len(cases),
            "retrieval_does_not_persist": True,
            "forward_scan_does_not_persist": True,
            "consolidation_does_not_rewrite": True,
        }
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    retrieve_cmd = sub.add_parser("retrieve", help="Rank similar INT rules (read-only)")
    retrieve_cmd.add_argument("--query", required=True)
    retrieve_cmd.add_argument("--limit", type=int, default=5)

    classify_cmd = sub.add_parser("classify", help="Suggest a Stage 0 outcome (read-only)")
    classify_cmd.add_argument("--event", required=True)

    decide_cmd = sub.add_parser("decide", help="Retrieve then classify (read-only)")
    decide_cmd.add_argument("--event", required=True)

    gate_cmd = sub.add_parser(
        "write-gate",
        help="Report whether a later persist step would be justified (still does not write)",
    )
    gate_cmd.add_argument("--event", required=True)

    scan_cmd = sub.add_parser(
        "forward-scan",
        help="Retrieve related rules and adjacent gaps as one compact batch (read-only)",
    )
    scan_cmd.add_argument("--event", required=True)

    sub.add_parser(
        "consolidate",
        help="Emit a consolidation review report without rewriting historical rules",
    )
    sub.add_parser("self-test", help="Check catalog completeness and routing examples")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "retrieve":
        emit(
            {
                "query": args.query,
                "matches": retrieve(args.query, limit=args.limit),
                "retrieval": {"executed": True, "creates_record": False},
                "persistence": {
                    "executed": False,
                    "creates_record": False,
                    "rewrites_history": False,
                    "note": "retrieve is read-only",
                },
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
        decision = classify(args.event)
        emit(
            {
                "action": decision["action"],
                "write_gate_satisfied": decision["persistence"]["write_gate_satisfied"],
                "suggested_mode": decision["persistence"]["suggested_mode"],
                "history_policy": "additive_versioned",
                "persistence": decision["persistence"],
                "best_match": decision["best_match"],
            }
        )
        return 0
    if args.command == "forward-scan":
        emit(forward_scan(args.event))
        return 0
    if args.command == "consolidate":
        emit(consolidate())
        return 0
    if args.command == "self-test":
        return cmd_self_test()
    parser.error("unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
