# Knowledge Mirror Changelog

## 2026-09-19 — PR #2 rebase resolved the INT-0005–INT-0007 drop risk

Trigger classification: `UPDATE_EXISTING` (INT-0005 / INT-0010 map only). No new Interaction ID.

What changed:
- PR #2 was rebased onto current `main` and now keeps INT-0005–INT-0007 with INT-0010 appended.
- `knowledge/interaction-id-map.md` no longer treats PR #2 as a drop-on-merge risk.

What did not change:
- INT-0008 collision (PRs #6/#7) remains `APPROVAL REQUIRED`.
- PRs #3/#4/#5 catalog overlap is still owner-gated; none were closed.

## 2026-09-19 — Re-evaluate PRs #3–#9 after INT-0010 owner approval

Designated Cursor Agent ID: `bc-01a0a3a4-ff95-7e51-bfd5-9a61684aa081`

Trigger classification for this batch: `UPDATE_EXISTING` (INT-0005 numbering), with retrieval of INT-0003 / INT-0007.

Retrieved before writing:
- Owner approval on PR #2 keeps `main` INT-0005 for retrieval/write gating and assigns INT-0010 to the approval protocol.
- INT-0003: do not create a near-duplicate Interaction ID for this numbering event.
- INT-0007: adjacent merge risk is that PR #2 still omits INT-0005–INT-0007 unless rebased.

What changed:
- Merged current `main` (INT-0007 + optimization policy) into this branch without replacing INT-0005/INT-0006 notes.
- Added `knowledge/interaction-id-map.md` for PRs #3–#9.
- Catalog now indexes INT-0001–INT-0007 and reserves INT-0008 / INT-0009 / INT-0010 without copying unmerged rule bodies.

What did not change:
- No new Interaction ID.
- ISSUE-0001–ISSUE-0010 remain unresolved.
- PRs #3–#9 were not closed or rewritten.
- Claim verification status was not changed.
- No Airtable write.

Unresolved / approval-gated:
- PRs #6 and #7 both draft INT-0008 (near-duplicate context-escape). `APPROVAL REQUIRED` before assigning a canonical ID.
- PR #2 rebase onto current `main` later resolved the INT-0005–INT-0007 drop risk (see the 2026-09-19 follow-up entry).

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
