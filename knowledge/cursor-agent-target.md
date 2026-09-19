# Cursor Agent Synchronization Target

Primary Cursor Agent ID: `bc-01a0a3a4-ff95-7e51-bfd5-9a61684aa081`

Primary Cursor Agent URL:
`https://cursor.com/agents/bc-01a0a3a4-ff95-7e51-bfd5-9a61684aa081`

## Purpose

This file is the canonical GitHub-side pointer for Cursor-oriented work in this repository.

All routine GitHub maintenance handoffs should reference this Agent ID and URL, including:
- source/index cleanup
- architecture-reference maintenance
- Interaction Learning consistency checks
- duplicate detection
- stale-link checks
- terminology consistency
- issue triage
- changelog generation
- pull-request preparation for public-safe repository maintenance
- vendor portal tree maps (Omniverse Developer: `knowledge/omniverse-developer-portal-tree.md`)

## Owner communication

Preferred channel: GitHub Issue #1 and related pull requests.

Approval and notification protocol: `knowledge/cursor-approval-protocol.md`

The designated Agent ID above is the GitHub-side target identity. A later Cursor run may have a different execution URL; do not treat a one-off run URL as a replacement for this target unless the owner updates it.

## Current execution boundary

The repository can store and propagate the Cursor Agent target, but GitHub alone does not prove that the external Cursor Agent has opened, accepted, or executed the task. Treat Cursor execution as confirmed only when explicit Cursor/GitHub output appears.

## Related files

- `AGENTS.md`
- `.cursor/rules/github-sync-maintenance.mdc`
- `knowledge/sync-policy.md`
- `knowledge/interaction-learning.md`
- `knowledge/cursor-approval-protocol.md`
- `knowledge/omniverse-developer-portal-tree.md`
- GitHub Issue #1
