# Cursor Agent Approval and Notification Protocol

Status: ACTIVE_RULE

Designated Cursor Agent ID: `bc-01a0a3a4-ff95-7e51-bfd5-9a61684aa081`

Designated Cursor Agent URL:
`https://cursor.com/agents/bc-01a0a3a4-ff95-7e51-bfd5-9a61684aa081`

Owner communication channel:
- GitHub Issue #1
- related pull requests

This protocol was recorded from the repository owner’s instruction on GitHub Issue #1. It does not change claim verification status and does not replace `knowledge/sync-policy.md`.

## When approval is required

Before making any change that is destructive, changes verification status, resolves a disputed issue, changes canonical architecture, publishes sensitive/contextual material, or performs a broad refactor, post a GitHub comment beginning with:

`APPROVAL REQUIRED`

Then include:

- proposed action
- files/records affected
- reason
- risk / uncertainty
- exact change intended

Do not execute that approval-gated action until the repository owner explicitly approves it.

## When approval is not required

Routine, reversible GitHub-side maintenance may proceed without approval when it stays within `AGENTS.md`, `.cursor/rules/github-sync-maintenance.mdc`, and `knowledge/sync-policy.md`, for example:

- Markdown cleanup
- index normalization
- duplicate detection
- broken-link detection
- non-destructive source indexing
- opening review issues
- small consistency fixes that do not alter claim verification status

## Notification behavior

After each meaningful maintenance batch, post a concise status comment on GitHub Issue #1 or the corresponding pull request with:

- what changed
- what was not changed
- any unresolved issue
- whether owner action is required

If owner approval is needed, leave the request open and wait for an explicit approval comment.

## Related files

- `AGENTS.md`
- `.cursor/rules/github-sync-maintenance.mdc`
- `knowledge/sync-policy.md`
- `knowledge/interaction-learning.md` (INT-0005)
- `knowledge/cursor-agent-target.md`
