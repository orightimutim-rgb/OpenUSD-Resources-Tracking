# PR stack review — 2026-09-19

Status: WORKING review after owner approval on PR #2. No overlapping PR is merged by this batch.

Owner decision recorded on PR #2:

- Keep `main` `INT-0005` for retrieval/write gating.
- Renumber PR #2 approval/notification protocol to `INT-0010`.
- Re-evaluate PRs #3–#9 against that numbering before merging overlapping work.
- The INT-0005 numbering collision is **resolved**. Metadata-only cleanup of stale “collision remains / PR #2 should rebase” wording was applied on PRs #3/#5/#6/#7/#8.
- `knowledge/dynamic-context-principle.md` is an upper-level operating principle, not a new INT ID.

## Canonical INT IDs after this PR

| ID | Title | Canonical location |
| --- | --- | --- |
| INT-0005 | Automatic interaction retrieval and write gating | `main` |
| INT-0006 | Structure-first user reasoning signal | `main` |
| INT-0007 | Proactive synthesis instead of toothpaste-style interaction | `main` |
| INT-0008 | Context-escape / dual-source retrieval | **not on `main`**; claimed by both PR #6 and PR #7 |
| INT-0009 | Active agency / control loop above prediction | PR #8 only |
| INT-0010 | Owner approval and GitHub notification protocol | this PR (#2) |

## PR #2 action taken

Rebased onto current `main` so INT-0010 is appended after INT-0005–INT-0007. Merging this PR no longer deletes the `main` retrieval/write-gating rule.

## PRs #3–#9

| PR | Branch base vs `main` | INT claim | Unique remaining work | Overlap | Recommended next step |
| --- | --- | --- | --- | --- | --- |
| #3 | behind (`c46adce`) | operationalize INT-0005; no new ID | `scripts/interaction_trigger.py`, `knowledge/interaction-index.json`, schema, trigger Cursor rule | policies already on `main`; file overlap with #4/#5 | rebase onto `main`+PR #2; do not create a new INT; treat as tooling for INT-0005 |
| #4 | behind (`ca29eb3`) | INT-0006 alignment | later trigger script/catalog than #3 | superset overlap with #3; policies on `main` | rebase after #3 decision; keep INT-0006 ID |
| #5 | current `main` | operationalize INT-0007 | largest trigger script, consolidation review | overlaps #3/#4 tooling | prefer as the surviving trigger-tooling PR if #3/#4 are not merged first |
| #6 | current `main` | **CREATE INT-0008** | context-escape retrieval + dual-source trigger updates | **INT-0008 collision with #7** | owner chooses one INT-0008 text; do not merge both as-is |
| #7 | current `main` | **CREATE INT-0008** (near-duplicate of #6) | Omniverse continuation/deep-dive nodes (PhysX, AV sim, Smart Cities, YouTube) | INT-0008 text overlaps #6; deep-dives are unique | keep unique deep-dives; do not also land a second INT-0008 |
| #8 | current `main` | CREATE INT-0009 | control-loop policy and Cursor rule | small policy-file overlap | rebase after INT-0008 resolution; ID INT-0009 is free |
| #9 | current `main` | no new INT; binds to INT-0001/0005/0006/0007 | Omniverse Developer portal tree | low INT overlap | independent content PR; still rebase after #2 so changelog/indexes compose |

## Merge order (recommended, not executed)

1. Merge PR #2 (INT-0010 + indexes) now that it is rebased onto `main`.
2. Choose one trigger-tooling survivor among #3/#4/#5 (likely #5 if the others are closed as superseded).
3. Resolve INT-0008: merge #6 **or** keep #6’s rule text and take #7’s deep-dives in a follow-up. Do not merge both INT-0008 sections.
4. Merge #8 (INT-0009) after INT-0008 exists or with an explicit note that INT-0008 is still pending.
5. Merge #9 as content, not as a new Interaction ID.

## What this review does not do

- It does not merge, close, or rewrite PRs #3–#9.
- It does not choose a winner between the two INT-0008 drafts.
- It does not change claim verification status.
