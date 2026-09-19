# Knowledge Mirror Changelog

## 2026-09-15 — Cursor approval protocol and index normalization

Designated Cursor Agent ID: `bc-01a0a3a4-ff95-7e51-bfd5-9a61684aa081`

What changed:

- Recorded the owner’s GitHub Issue #1 approval/notification protocol as `knowledge/cursor-approval-protocol.md` and INT-0010.
- Numbering history: this rule was originally drafted as INT-0005 in PR #2; on 2026-09-19 the owner approved renumbering it to INT-0010 because main already uses INT-0005 for retrieval/write gating. No rule content was discarded.
- Added non-destructive GitHub-side indexes for sources, architecture references, and unresolved issues.
- Recorded a terminology consistency check for Simulator / Emulator / Digital Twin / HIL / Omniverse / OpenUSD / Physical AI / PhysX.
- Checked candidate source URLs and logged stale or ambiguous links without rewriting claims.
- Bound AGENTS.md, the Cursor maintenance rule, and the agent-target file to Issue #1 as the owner communication channel.

What did not change:

- No claim verification status.
- No disputed snapshot issue was resolved.
- No dedicated ARCH-0001–ARCH-0005 files were created.
- No Airtable `SRC-*` IDs were invented or remapped.

Unresolved:

- ISSUE-0001–ISSUE-0010 remain open.
- ISSUE-GH-001–ISSUE-GH-006 are new review items.
- ISSUE-GH-007: PRs #6 and #7 both draft INT-0008; owner choice required before merge.

## 2026-09-19 — Rebase onto main after INT-0010 approval

What changed:

- Rebased this branch onto current `main` so INT-0005/INT-0006/INT-0007 remain in place and the approval protocol stays INT-0010.
- Added `knowledge/pr-stack-review-2026-09-19.md` for PRs #3–#9. No overlapping PR was merged.

What was not changed:

- INT-0008 was not assigned; PRs #6 and #7 still collide.
- PRs #3–#9 were not rebased or closed from this branch.

## 2026-09-19 — Dynamic context principle (owner-authored)

What changed:

- Owner added `knowledge/dynamic-context-principle.md` and placed it in the Cursor reading order. No new INT ID.
- Linked the principle from the approval protocol and maintenance rule so agents retrieve it before creating structure.

What was not changed:

- INT-0008 overlap between PRs #6 and #7 remains an owner choice.
- ARCH-0001–ARCH-0005 extraction remains approval-gated.
- Metadata-only cleanup on PRs #3/#5/#6/#7/#8 marked the INT-0005 collision as resolved; those PRs were not rebased or merged.

## 2026-09-19 — Cursor writing authorization (owner-authored)

What changed:

- Owner bound INT-0005 as the action/write gate and INT-0010 as the scoped approval handoff.
- Routine reversible GitHub-side writes inside maintenance scope may proceed without per-write approval.
- Protocol-derived problems (stale metadata, duplicate gates, dependency conflicts) stay on the protocol/routing layer.

What was not changed:

- No merge, PR close, ARCH extraction, verification-status change, or INT-0008 resolution.
