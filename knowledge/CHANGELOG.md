# Knowledge Mirror Changelog

## 2026-09-15 — Add INT-0008 context escape and dual-source retrieval

Designated Cursor Agent ID: `bc-01a0a3a4-ff95-7e51-bfd5-9a61684aa081`

Trigger classification for this batch: `CREATE_NEW` (INT-0008).

Retrieved before writing:
- INT-0007 remains adjacent forward-scan / compact batch inside a cluster; it is not loop escape.
- INT-0006 remains ordinary-language structural triggers; those stay valid for dual-source retrieval.
- INT-0005 remains retrieve-broadly / write-conservatively; retrieval still does not persist.
- INT-0004: judgment-layer retrieval.

What changed:
- Added INT-0008: structure-first retrieval strategy, symmetric INTERNAL/EXTERNAL retrieval, and context escape from conversational recursion.
- Appended additive version notes to INT-0006 and INT-0007 without replacing prior rule text.
- Bound agent/policy/Cursor rules so inefficient local loops escape via retrieval instead of another mirror-turn.
- Added retrieval catalog `knowledge/interaction-index.json` covering INT-0001–INT-0008.
- Added read-only helper `scripts/interaction_trigger.py` (`retrieve` / `classify` / `decide` / `write-gate` / `context-escape` never persist or rewrite history).

What did not change:
- No claim verification status.
- ISSUE-0001–ISSUE-0010 remain unresolved.
- Canonical Stage 0 outcomes were not rewritten.
- No Airtable write was executed from this GitHub-side batch.
- Historical INT-0001–INT-0007 rule text was not replaced.
- Open PR #2's drafted INT-0005 numbering collision remains `APPROVAL REQUIRED`.

Unresolved / approval-gated:
- Open PR #2 drafts a different INT-0005 (approval protocol) while `main` already uses INT-0005 for retrieval/write gating.
- Open PRs #3–#5 operationalize earlier INT layers and overlap helper/catalog files; treat as a rebase cluster, not a silent close.
- INT-0006 / INT-0007 / INT-0008 remain related distinct layers, not a merge.
