# Repository Agent Instructions

This repository is the public, versioned mirror of a structured research workflow spanning ChatGPT, Airtable, GitHub, and Cursor.

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
2. `knowledge/interaction-learning.md`
3. `knowledge/chat-sync-2026-09-15.md`
4. architecture-reference files or source indexes present in the repository

## Synchronization principles

- Airtable is the structured working database.
- GitHub is the public versioned mirror.
- Cursor maintains GitHub-side consistency and automation-friendly structure.
- Do not expose personal identifiers, private case details, account information, raw emotional passages, or unsupported allegations.
- Preserve version history instead of overwriting conflicting knowledge without explanation.
- `Official Definition`, `Vendor Product Mapping`, and `Vendor Standard / Implementation Framework` are distinct categories.
- A vendor definition is not automatically an industry-wide definition or formal standard.

## Interaction-learning rule

When a recurring repository problem appears, record the reusable maintenance rule, not only the fix. Track:
- detected pattern
- evidence
- action
- unresolved uncertainty
- next-time handling

Do not attempt to reproduce hidden chain-of-thought. Store only concise, reviewable reasoning summaries and decision criteria.

## Working style

Prefer small, reviewable commits. Avoid destructive rewrites. For uncertain changes, open or update an issue rather than silently changing canonical knowledge.
