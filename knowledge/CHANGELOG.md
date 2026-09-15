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

## 2026-09-15 — Omniverse Developer portal as knowledge tree (PR #9)

What changed:

- Classified as `UPDATE_EXISTING` on INT-0001 / INT-0005 / INT-0006 / INT-0007. No new Interaction ID.
- Added `knowledge/omniverse-developer-portal-tree.md` and `.json` so later turns can retrieve first-level Omniverse Developer links without re-feeding the root URL.
- Root https://developer.nvidia.com/omniverse is an **entry node** (`Partial`). Linked Agent Skills, ov* tools, SimReady/USD tools, simulation libraries, blueprints, and the 57-item learning catalog remain unread unless already covered by an existing source.
- No `SRC-*` IDs invented. Airtable was not written. ISSUE-0001–ISSUE-0010 unchanged.

## 2026-09-19 — Compose portal tree with PR #2 indexes

What changed:

- Rebased PR #9 onto PR #2 so this changelog and the source/architecture indexes compose.
- Keep `main` INT-0005 (retrieval/write gating). Approval protocol remains INT-0010 on PR #2. This PR still creates no Interaction ID.

What was not changed:

- No Airtable write.
- ARCH-0001–ARCH-0005 files were not extracted.
- INT-0008 collision on PRs #6/#7 was not resolved from this branch.
