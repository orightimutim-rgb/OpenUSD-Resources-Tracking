# Repository Agent Instructions

This repository is the public, versioned mirror of a structured research workflow spanning ChatGPT, Airtable, GitHub, and Cursor.

## Designated Cursor Agent

Primary Cursor Agent ID: `bc-01a0a3a4-ff95-7e51-bfd5-9a61684aa081`

Primary Cursor Agent URL:
`https://cursor.com/agents/bc-01a0a3a4-ff95-7e51-bfd5-9a61684aa081`

GitHub-side maintenance tasks intended for Cursor should target this agent identity when possible. If automation cannot address the Cursor Agent URL directly, preserve this ID and URL in handoff issues, task files, and synchronization metadata so all agents refer to the same target.

## Primary role for Cursor

Cursor should take over GitHub-side maintenance that does not require conversational judgment from ChatGPT.

### Cursor owns
- repository organization and file hygiene
- de-duplication of technical notes
- broken-link checks
- source-index maintenance
- architecture-reference maintenance
- issue/alert index maintenance
- cross-file consistency checks
- Markdown cleanup and table normalization
- changelog generation
- detection of stale or conflicting statements
- dual-source retrieval (internal catalogs and external official/linked sources)
- context escape when a maintenance loop is locally repetitive
- pull-request preparation for non-sensitive repository maintenance

### Cursor should not decide alone
- whether an unverified claim becomes a verified fact
- whether user reaction or private context should be published
- whether a disputed issue is resolved
- whether a vendor definition should be treated as an industry-wide standard
- whether a private or identifying detail may enter the public repository

Escalate these as a review item instead of silently deciding.

## Required knowledge order before editing

Read these first when relevant:
1. `knowledge/sync-policy.md`
2. `knowledge/interaction-trigger-policy.md`
3. `knowledge/interaction-optimization-policy.md`
4. `knowledge/interaction-learning.md`
5. `knowledge/chat-sync-2026-09-15.md`
6. architecture-reference files or source indexes present in the repository

## Synchronization principles

- Airtable is the structured working database.
- GitHub is the public versioned mirror.
- Cursor maintains GitHub-side consistency and automation-friendly structure.
- The designated Cursor Agent above is the preferred GitHub-side execution target.
- Do not expose personal identifiers, private case details, account information, raw emotional passages, or unsupported allegations.
- Preserve version history instead of overwriting conflicting knowledge without explanation.
- `Official Definition`, `Vendor Product Mapping`, and `Vendor Standard / Implementation Framework` are distinct categories.
- A vendor definition is not automatically an industry-wide definition or formal standard.

## Interaction-learning rule

Canonical routing spec: `knowledge/interaction-trigger-policy.md`.
Canonical optimization spec: `knowledge/interaction-optimization-policy.md`.

For each meaningful maintenance event, classify first:
- `NO_INTERACTION_ACTION`
- `RETRIEVE_ONLY`
- `UPDATE_EXISTING`
- `CREATE_NEW`
- `REVIEW_CONFLICT`

Retrieve similar Interaction rules before deciding to write. Automatic retrieval must not create Interaction records. Prefer update/versioning over near-duplicates. When a write is justified, preserve history additively/versioned rather than overwriting prior rule states.

Do not model the user only as a sequence of prompts. Treat their behavior as a structure-first retrieval strategy. Interpret ordinary-language observations structurally even when no technical terminology is used.

Automatic retrieval applies symmetrically to INTERNAL sources (Interaction Learning, Records, Sources, Issues, Architecture References, repository files/history) and EXTERNAL sources (official docs, linked pages, authoritative references).

When the current loop is locally repetitive or inefficient, trigger a context escape: stop extending the mirror loop, search the relevant internal/external knowledge space, then return with a consolidated structural answer. Retrieval is the primary escape from conversational recursion. Do not interpret that retrieval as merely forecasting the next question.

When a recurring repository problem appears and the write gate is satisfied, record the reusable maintenance rule, not only the fix. Track:
- detected pattern
- evidence
- action
- unresolved uncertainty
- next-time handling

Do not attempt to reproduce hidden chain-of-thought. Store only concise, reviewable reasoning summaries and decision criteria. Flag conflicts as `APPROVAL REQUIRED` rather than silently rewriting history.

## Working style

Prefer small, reviewable commits. Avoid destructive rewrites. For uncertain changes, open or update an issue rather than silently changing canonical knowledge.
