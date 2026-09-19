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
- pull-request preparation for non-sensitive repository maintenance

### Cursor should not decide alone
- whether an unverified claim becomes a verified fact
- whether user reaction or private context should be published
- whether a disputed issue is resolved
- whether a vendor definition should be treated as an industry-wide standard
- whether a private or identifying detail may enter the public repository

Escalate these as a review item instead of silently deciding.

## Owner communication and approval

Preferred owner↔Cursor channel: GitHub Issue #1 and related pull requests.

Full protocol: `knowledge/cursor-approval-protocol.md`

Approval-gated actions require a GitHub comment beginning with `APPROVAL REQUIRED` and explicit owner approval before execution:
- destructive changes
- verification-status changes
- disputed-issue resolution
- canonical-architecture changes
- publication of sensitive/contextual material
- broad refactors

Routine reversible GitHub-side maintenance may proceed without approval when it stays within this file, `.cursor/rules/github-sync-maintenance.mdc`, and `knowledge/sync-policy.md`.

After each meaningful maintenance batch, post a concise status comment on Issue #1 or the corresponding pull request.

## Required knowledge order before editing

Read these first when relevant:
1. `knowledge/sync-policy.md`
2. `knowledge/interaction-learning.md`
3. `knowledge/interaction-trigger-policy.md`
4. `knowledge/cursor-approval-protocol.md`
5. `knowledge/chat-sync-2026-09-15.md`
6. architecture-reference files or source indexes present in the repository (`knowledge/architecture-index.md`, `knowledge/source-index.md`, `knowledge/issue-index.md`)

## Synchronization principles

- Airtable is the structured working database.
- GitHub is the public versioned mirror.
- Cursor maintains GitHub-side consistency and automation-friendly structure.
- The designated Cursor Agent above is the preferred GitHub-side execution target.
- Do not expose personal identifiers, private case details, account information, raw emotional passages, or unsupported allegations.
- Preserve version history instead of overwriting conflicting knowledge without explanation.
- `Official Definition`, `Vendor Product Mapping`, and `Vendor Standard / Implementation Framework` are distinct categories.
- A vendor definition is not automatically an industry-wide definition or formal standard.
- A vendor developer portal that already exists as a source is an entry node, not a completed landing-page summary. Retrieve its first-level tree (`knowledge/omniverse-developer-portal-tree.md` for NVIDIA Omniverse Developer) and do not create a new Interaction record for each continuing correction.

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
