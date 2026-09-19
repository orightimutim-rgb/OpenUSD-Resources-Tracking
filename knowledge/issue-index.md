# Issue Index

Status: WORKING public mirror of unresolved items. None of these issues are marked resolved.

IDs `ISSUE-0001`–`ISSUE-0010` appear in `knowledge/sync-state.json`. Titles below follow the order of `knowledge/chat-sync-2026-09-15.md` section 9. That order-to-ID mapping is inferred, not independently confirmed from Airtable. Tracked as `ISSUE-GH-003`.

## Snapshot issues (unresolved)

| Inferred ID | Statement from chat-sync | Notes |
| --- | --- | --- |
| ISSUE-0001 | DJI Flight Simulator is historical / discontinued and should not be presented as a current actively maintained recommendation. | Candidate product URL returned 404 on 2026-09-15. Do not substitute other DJI simulator-branded apps. |
| ISSUE-0002 | Some Simulator / Emulator summaries conflict with cited source wording. | No wording was rewritten in this batch. |
| ISSUE-0003 | Simulator / Emulator “surface vs internal structure” is too broad as a universal definition. | Chat-sync already labels this an overgeneralization. Status unchanged. |
| ISSUE-0004 | Historical claims about early simulation / emulation origins require stronger sources. | No historical origin claims were added. |
| ISSUE-0005 | Technical-history claims must be separated from social or institutional interpretation. | No such claims were published. |
| ISSUE-0006 | Unverified claims about platforms or institutions must remain unverified unless independently supported. | Status unchanged. |
| ISSUE-0007 | HIL and Emulator should not be collapsed into one concept. | Cross-file check: chat-sync and this index still keep them separate. |
| ISSUE-0008 | Claims about virtual signals damaging real chips require technical verification. | Left open. |
| ISSUE-0009 | SpaceX / Boeing / NVIDIA Omniverse usage claims should be independently verified. | Left open. No such claims were added. |
| ISSUE-0010 | Game-console development should distinguish emulator, SDK, devkit, and hardware test environments. | Left open. |

## GitHub-side maintenance issues (new, review-only)

These are repository-structure findings. They do not resolve or replace the snapshot issues above.

| ID | Classification | Finding | Recommended next step |
| --- | --- | --- | --- |
| ISSUE-GH-001 | synchronization mismatch | `sync-state.json` lists 10 `SRC-*` IDs; chat-sync names 16 sources; no title-to-ID map exists on GitHub. | Owner/Airtable confirmation of the source map. |
| ISSUE-GH-002 | existing source but missing architecture node files | ARCH-0001–ARCH-0005 are named in chat-sync; dedicated Architecture Reference files are absent. | Owner approval before extracting full canonical ARCH files. |
| ISSUE-GH-003 | synchronization mismatch | ISSUE-0001–ISSUE-0010 IDs are listed, but GitHub has no explicit ID-to-title map. | Confirm order-based mapping against Airtable. |
| ISSUE-GH-004 | stale source | NVIDIA Design & Simulation candidate URL returned 404. | Confirm replacement URL or mark the source historical. |
| ISSUE-GH-005 | stale source | NVIDIA Synthetic Data glossary URL as named in the snapshot returned 404; a nearby “synthetic data generation” glossary is live. | Confirm whether the nearby page is the same source. |
| ISSUE-GH-006 | missing relationship / duplicate-risk | README still describes a full OpenUSD resource-tracking corpus, while GitHub currently contains the knowledge-mirror subset only. | Decide whether README should describe the current mirror scope. |
| ISSUE-GH-007 | duplicate | PRs #6 and #7 both create INT-0008 with near-duplicate context-escape rules. | Owner chooses one INT-0008 text; keep #7 deep-dives separately. See `knowledge/pr-stack-review-2026-09-19.md`. |
| ISSUE-GH-008 | stale source / vendor page defect | On the live Omniverse Developer portal, NVIDIA Warp “Learn More” currently points at the Newton URL. | Do not merge Warp into Newton. Confirm whether the live card is a page defect or an alias. |

## Explicitly not resolved

No disputed issue from the snapshot list was closed. No WORKING claim was promoted to VERIFIED.
