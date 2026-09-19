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


## Authorization model for Cursor writing

Cursor is authorized to perform routine, reversible GitHub-side writing inside the repository maintenance scope when the action does not cross an INT-0005 gate.

INT-0005 is the action/write gate. It determines whether a proposed repository action may proceed automatically, may proceed as routine reversible maintenance, or must be escalated.

When INT-0005 determines that owner authorization is required, INT-0010 is the handoff protocol. Cursor must create an `APPROVAL REQUIRED` request with the action, affected files/records, reason, risk/uncertainty, and exact intended change, then stop only that gated action until explicit owner approval is recorded.

Owner approval applies to the proposed gated action or clearly defined batch. It does not convert Cursor into an unrestricted writer and does not remove later gates for materially different actions.

## Protocol-responsibility rule

Problems produced by the protocol must return to the protocol.

If gating, approval, routing, dependency ordering, stale metadata, conflicting instructions, or a waiting state creates follow-on work, the default response is to classify and repair the process path rather than assigning the burden to whichever person or agent appears more available.

Do not use workload, persistence, familiarity with technical language, or willingness to absorb extra steps as a substitute for protocol logic.

Examples:
- stale approval metadata → repair/update the approval metadata
- two rules compete for the same identifier → open/maintain a conflict decision path
- an approval blocks dependent work → continue allowed independent work and record the dependency
- an action is ambiguous under INT-0005 → classify the ambiguity and escalate only the gated boundary
- repeated owner questions are caused by missing routing logic → improve the routing/protocol rather than treating repeated manual confirmation as the permanent solution

The objective is to keep responsibility attached to the rule that generated the dependency or uncertainty.

## Minimum-interruption principle

Approval should stop the smallest necessary action, not the whole workflow.

Cursor may continue independent, reversible, non-sensitive work that does not depend on the blocked decision. It should preserve a clear dependency marker so the blocked branch can resume after approval.

Do not turn an unresolved gate into global inactivity when safe parallel work exists.

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
- `knowledge/interaction-learning.md` (INT-0010; originally drafted as INT-0005 in PR #2, renumbered by owner approval to resolve the collision with main)
- `knowledge/dynamic-context-principle.md` (upper-level operating principle; not a new INT ID)
- `knowledge/cursor-agent-target.md`
