# Knowledge Mirror Changelog

## 2026-09-15 — INT-0009 active agency / control loop

Designated Cursor Agent ID: `bc-01a0a3a4-ff95-7e51-bfd5-9a61684aa081`

Trigger classification for this batch: `CREATE_NEW` (INT-0009).

Retrieved before writing:
- INT-0007: local forward-scan / consolidation; compresses adjacent work, not the full decision architecture
- INT-0005: routing / write gate; retrieval still does not persist records
- INT-0006: ordinary-language structural signals
- INT-0004: shareable judgment layer
- Unmerged INT-0008 on PRs #6/#7: context-escape via retrieval when a loop is inefficient; related path, not this control loop

Why not UPDATE_EXISTING on INT-0007 or INT-0008:
- INT-0007 remains local bundling after a structural issue is found.
- INT-0008 (unmerged) remains escape-when-inefficient via retrieval.
- This correction is the always-on decision layer: active path catalog, three-input self-judgment, and prediction as a weak optional signal that must never constrain current-turn judgment.

Forward-scan bundled:
- INT-0009 rule plus additive version note on INT-0007
- control-loop policy and always-on Cursor rule
- agent / sync / trigger / optimization bindings
- chat-sync representative-rule list through INT-0009
- changelog

What changed:
- Added INT-0009. Appended a version note to INT-0007 without replacing its rule text.
- Bound the control loop as higher priority than proactive prediction in `AGENTS.md`, `knowledge/sync-policy.md`, `knowledge/interaction-trigger-policy.md`, `knowledge/interaction-optimization-policy.md`, and Cursor rules.
- Added `knowledge/interaction-control-loop-policy.md` and `.cursor/rules/interaction-control-loop.mdc`.

What did not change:
- No claim promoted from WORKING to VERIFIED.
- ISSUE-0001–ISSUE-0010 remain unresolved.
- Canonical INT-0005 Stage 0 outcome names were not rewritten.
- No Airtable write was executed.
- Historical INT-0001–INT-0007 rule text was not destructively overwritten.
- Unmerged PRs #2–#7 were not silently merged, closed, or reassigned.

Unresolved / approval-gated:
- INT-0005 numbering collision with PR #2 is resolved (2026-09-19): approval protocol is INT-0010.
- Unmerged PRs #6/#7 already draft INT-0008 (context-escape). This branch uses INT-0009 rather than colliding with that ID. Rebase should keep INT-0008 and INT-0009 distinct related layers.
