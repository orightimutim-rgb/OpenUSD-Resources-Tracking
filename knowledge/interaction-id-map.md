# Interaction ID map — GitHub-side numbering

Designated Cursor Agent ID: `bc-01a0a3a4-ff95-7e51-bfd5-9a61684aa081`

Purpose: re-evaluate open PRs against owner-approved numbering. This is a retrieval/index file, not a second Interaction store. Updating this map does not create an Interaction record.

Owner decision (2026-09-19, PR #2):
- Keep `main` `INT-0005` for retrieval/write gating.
- PR #2 approval/notification protocol is `INT-0010`.
- History: originally drafted as INT-0005 in PR #2; renumbered by owner approval.

Owner writing authorization (2026-09-19, PR #2; no new INT ID):
- INT-0005 = action/write gate.
- INT-0010 = approval handoff when INT-0005 requires owner authorization.
- Routine, reversible GitHub-side writes inside the established maintenance scope may proceed without per-write approval.
- Approval is scoped to the gated action or an explicitly defined batch, not blanket future authorization.
- Pause only the dependent gated action; continue safe independent work.
- Protocol-derived problems (stale metadata, duplicated approval questions, dependency conflicts, repeated manual burden) return to the INT-0005/INT-0010 routing layer rather than to whoever appears more available.
- This map does not copy PR #2's protocol file bodies.

## Canonical IDs on current `main`

| ID | Title | Status |
| --- | --- | --- |
| INT-0001 | Detecting a missing architecture node | ACTIVE_RULE |
| INT-0002 | Synchronization transparency | ACTIVE_RULE |
| INT-0003 | Duplicate detection when record number is forgotten | ACTIVE_RULE |
| INT-0004 | Assistant judgment as retrievable interaction data | ACTIVE_RULE |
| INT-0005 | Automatic interaction retrieval and write gating | ACTIVE_RULE |
| INT-0006 | Structure-first user reasoning signal | ACTIVE_RULE |
| INT-0007 | Proactive synthesis instead of toothpaste-style interaction | ACTIVE_RULE |

## Reserved / draft IDs (not on `main`)

| ID | Intended rule | Source | Numbering status |
| --- | --- | --- | --- |
| INT-0008 | Context-escape / dual-source retrieval | PR #6 and PR #7 | `REVIEW_CONFLICT` — both drafts use INT-0008; near-duplicate; do not silently pick a winner |
| INT-0009 | Active agency / control loop | PR #8 | Unique vs INT-0010; still pending merge |
| INT-0010 | Owner approval and GitHub notification protocol | PR #2 | `OWNER_APPROVED` numbering and writing-handoff role; rebased onto current `main`. Pending merge. |

## Open PR re-evaluation (PRs #3–#9)

| PR | What it adds | Numbering vs owner decision | Merge guidance |
| --- | --- | --- | --- |
| #3 | Older retrieval-trigger operationalization (catalog/helper) | Uses INT-0005 correctly as retrieval/write gating, but predates INT-0006/INT-0007 | Superseded by PR #4 / PR #5. Do not merge as-is. |
| #4 | Retrieve-vs-write + INT-0006 operationalization + this ID map | INT-0005 kept; INT-0010 reserved | Keep as the numbering/re-evaluation PR. Overlaps PR #5 on catalog/helper. |
| #5 | INT-0007 operationalization (forward-scan/consolidation helper) | INT-0005 collision wording annotated as resolved to INT-0010 | Catalog/helper is the later operationalization of INT-0005–0007. Overlaps PRs #3/#4 tooling. |
| #6 | Draft INT-0008 structure-first retrieval and context escape | Collides with PR #7 on INT-0008 | `APPROVAL REQUIRED` before merge. Prefer one canonical INT-0008; version the other additively. |
| #7 | Draft INT-0008 context-escape retrieval, not next-prompt prediction | Collides with PR #6 on INT-0008 | Same `APPROVAL REQUIRED` as PR #6. Also adds Omniverse continuation files. |
| #8 | Draft INT-0009 active agency / control loop | Does not collide with INT-0010 | Safe numbering. Do not silently reassign PR #6/#7 INT-0008. |
| #9 | Omniverse Developer portal knowledge tree | No new INT ID | Independent of the INT-0005/INT-0010 collision. Rebase onto current `main` before merge. |

## Merge risks (do not ignore)

- PR #2 rebase (2026-09-19): `knowledge/interaction-learning.md` now keeps INT-0005–INT-0007 and appends INT-0010. The earlier drop-on-merge risk is resolved. A parallel stack review lives on PR #2 as `knowledge/pr-stack-review-2026-09-19.md`; this map is not a second Interaction rule.
- PR #3, PR #4, and PR #5 overlap on `knowledge/interaction-index.json` and `scripts/interaction_trigger.py`. Merge at most one catalog/helper lineage. Choosing a survivor is owner-gated; this batch does not close any of those PRs.
- PR #6 and PR #7 are a numbering collision and a near-duplicate rule. That is `APPROVAL REQUIRED`, not a silent ID reassignment.

## What this batch does not do

- Does not create a new Interaction ID.
- Does not copy INT-0008 / INT-0009 / INT-0010 rule bodies onto `main`.
- Does not close PRs #3–#9.
- Does not change claim verification status or ISSUE-0001–ISSUE-0010.
