# Knowledge Mirror Changelog

## 2026-09-15 — Align GitHub-side Interaction retrieval with retrieve-vs-write and INT-0006

Designated Cursor Agent ID: `bc-01a0a3a4-ff95-7e51-bfd5-9a61684aa081`

Trigger classification for this batch: `UPDATE_EXISTING` (INT-0005 and INT-0006).

Retrieved before writing:
- INT-0005 already separates retrieval from persistence; this batch does not create a new Interaction ID.
- INT-0006 already is the structure-first rule; catalog/helper now retrieve from ordinary-language structural observations.
- INT-0004 remains the judgment-layer rule.
- INT-0002 / INT-0003: persistence transparency and semantic de-duplication.

What changed:
- Bound `AGENTS.md`, `knowledge/sync-policy.md`, and Cursor rules so retrieval cannot create Interaction records.
- Added retrieval catalog `knowledge/interaction-index.json` covering INT-0001–INT-0006.
- Added read-only helper `scripts/interaction_trigger.py` with structure-first retrieval cues.
- Added always-on Cursor rule `.cursor/rules/interaction-trigger.mdc`.
- Appended GitHub-side version notes to INT-0005 and INT-0006 without replacing prior rule text.

What did not change:
- No claim verification status.
- ISSUE-0001–ISSUE-0010 remain unresolved.
- Canonical Stage 0 outcomes were not rewritten.
- No Airtable write was executed from this GitHub-side batch.
- Open PR #2's drafted INT-0005 (owner approval protocol) was not reassigned or overwritten.

Unresolved / approval-gated:
- Open PR #2 drafts a different INT-0005 (approval protocol) while `main` already uses INT-0005 for the retrieval-trigger rule. Numbering collision remains `APPROVAL REQUIRED`; not silently merged.
