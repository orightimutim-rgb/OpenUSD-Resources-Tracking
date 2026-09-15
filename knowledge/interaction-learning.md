# Interaction Learning — Public De-identified Mirror

This file mirrors reusable interaction logic from the Airtable `Interaction Learning` table. It stores shareable decision summaries and user-validation patterns, not hidden chain-of-thought.

## INT-0001 — Detecting a missing architecture node

Problem detection logic:
- The user noticed that the NVIDIA Physical AI landing page linked directly to PhysX SDK, but the architecture-reference layer had not given PhysX its own node.

Reusable rule:
- When the user asks whether something is missing, first search Records, Sources, and Architecture References.
- Distinguish among: missing source, missing relationship, missing architecture node, or already-existing content.
- Apply the smallest necessary update instead of duplicating records.

Assistant judgment summary:
- PhysX was not absent from all data; it already existed as a source. The gap was architectural prominence, so the correct action was to add an Architecture Reference, not duplicate the Source.

User validation:
- The user emphasized that the reasoning process used to detect and correct the omission must itself become reusable data.

Status: ACTIVE_RULE

## INT-0002 — Synchronization transparency

Problem detection logic:
- The user noticed that formatting and completion language could imply external persistence even when work only existed in chat.

Reusable rule:
- Every database, automation, or long-running workflow must clearly distinguish:
  - actually executed externally
  - only planned/organized in chat
  - not yet written externally
  - waiting for authorization

Assistant judgment summary:
- This is an execution-transparency problem, not merely a wording problem.

Status: ACTIVE_RULE

## INT-0003 — Duplicate detection when record number is forgotten

Problem detection logic:
- The user reposted prior content while unsure of its record number.

Reusable rule:
- Compare core propositions, examples, and knowledge nodes before creating a new record.
- If highly overlapping, preserve the canonical record and create a duplicate relationship instead of incrementing a new REC number.

Status: ACTIVE_RULE

## INT-0004 — Assistant judgment as retrievable interaction data

Problem detection logic:
- Event logs alone are not enough to produce stable interaction behavior.

Required retrievable layers:
1. conversation structure and context relationships
2. assistant judgment summary and decision basis
3. uncertainty / risk
4. response strategy
5. sync checkpoints
6. user feedback and correction
7. reusable rule and version

Assistant judgment summary:
- Stable collaboration requires preserving not only what happened, but also the shareable reasoning structure that determined the response and action.

Important boundary:
- These notes are public, de-identified judgment summaries. They are not hidden chain-of-thought and do not claim to modify model weights.

Response strategy:
- For important research/database/sync work, retrieve similar interaction rules before deciding what to do.
- If a new case conflicts with an older rule, create a versioned rule rather than silently overwriting history.

Sync checkpoint:
- Airtable is the structured working store.
- GitHub is the public versioned mirror.
- In-conversation synchronization is active; unattended background monitoring is not.

Status: ACTIVE_RULE

## INT-0005 — Automatic interaction retrieval and write gating

Problem detection logic:
- The user identified that having an Interaction Learning table is not enough if retrieval depends on the assistant manually remembering to query it.
- The system needs a pre-response trigger that decides whether to retrieve, reuse, update, create, or leave Interaction Learning unchanged.

User requirement:
- Do not create an Interaction record for every message.
- Automatically determine, from the current turn and conversation structure, whether an existing Interaction should be retrieved, updated, edited, versioned, or whether no write is needed.

Assistant judgment summary:
- The missing component is a routing layer, not another storage layer.
- Interaction Learning should be downstream of a trigger classifier.
- Retrieval should be broad enough to catch recurring workflow patterns, while writing should be gated to prevent chat-log inflation.

Reusable rule:
- Run the Trigger Router first.
- Possible outcomes: NO_INTERACTION_ACTION / RETRIEVE_ONLY / UPDATE_EXISTING / CREATE_NEW / REVIEW_CONFLICT.
- Prefer retrieval without writing when the current case is already covered.
- Prefer updating/versioning an existing Interaction over creating a near-duplicate.
- Create a new Interaction only when a genuinely new reusable decision pattern appears.

Response strategy:
- For each meaningful turn, classify whether prior interaction logic can materially change the response.
- If yes, retrieve similar interaction rules before acting.
- After the action and user feedback, decide whether the interaction database should remain unchanged, update an existing rule, create a new rule, or open a conflict review.

Implementation reference:
- See `knowledge/interaction-trigger-policy.md`.

Status: ACTIVE_RULE

## INT-0006 — Structure-first user reasoning signal

Problem detection logic:
- The user clarified that their judgments come from seeing the structure of the situation, not from formal training in databases, programming, encoding, or data logic.
- Their natural-language responses frequently identify hierarchy, missing parts, misalignment, ordering, duplication, dependency, or classification boundaries before technical labels are known.

User requirement:
- The system must understand and learn from structural observations expressed in ordinary language.
- The user should not need to know or supply technical terminology for a structural signal to trigger retrieval or review.

Assistant judgment summary:
- The user's wording is best treated as a structure-first signal source rather than as a technical-specification interface.
- The assistant/database layer should translate natural-language structural observations into technical retrieval categories internally.

Reusable rule:
- Detect structural meaning before looking for technical vocabulary.
- Treat statements about missing pieces, layers, ordering, links, duplication, handoffs, boundaries, dependencies, or synchronization as strong interaction-retrieval signals.
- Do not ask the user to convert such observations into code, schema, database, or data-model terminology unless implementation details are genuinely needed.

Persistence rule:
- Retrieval itself does not create a record.
- When the user's structural judgment creates or changes a reusable rule, persist it additively/versioned so earlier rule states remain traceable.

Status: ACTIVE_RULE

## INT-0007 — Proactive synthesis instead of toothpaste-style interaction

Problem detection logic:
- The user identified a costly interaction pattern: the assistant proposes one point, the user detects one downstream structural issue, the assistant proposes another fix, and the cycle repeats many times.
- The problem is not lack of answers; it is insufficient proactive synthesis across the full conversation structure.

Assistant judgment summary:
- The interaction system should not wait for the user to discover every adjacent structural consequence one by one.
- After detecting a meaningful structural issue, the assistant should scan the surrounding workflow for likely adjacent gaps, dependencies, maintenance needs, and second-order effects before replying.

Reusable rule:
- When a structural correction is detected, perform a local forward-scan before responding.
- Return: current issue, likely adjacent issues, recommended combined change, what should remain unchanged, and any maintenance implication.
- Prefer one compact batch decision over multiple serial micro-decisions when confidence is sufficient.
- Do not over-automate uncertain changes; bundle them as review candidates instead.

Maintenance implication:
- Because Interaction Learning is additive/versioned rather than overwrite-based, it requires periodic consolidation.
- Consolidation should detect near-duplicates, superseded rules, conflict clusters, stale response strategies, and rules that can be merged into a higher-level abstraction while preserving provenance.

Status: ACTIVE_RULE

## INT-0010 — Owner approval and GitHub notification protocol

Version history:
- Originally drafted in PR #2 as `INT-0005`.
- Owner approved renumbering to `INT-0010` on 2026-09-19 because `main` already uses `INT-0005` for retrieval/write gating.
- Rule content and intent are preserved; this renumbering resolves identifier collision without overwriting either history.

Problem detection logic:
- The repository owner designated GitHub Issue #1 and related pull requests as the communication channel with the Cursor Agent.
- Routine GitHub-side maintenance can proceed, but several action types can silently overstep conversational judgment that ChatGPT / the owner still owns.

Reusable rule:
- Use GitHub Issue #1 and related pull requests as the owner↔Cursor communication bridge.
- Before a destructive change, verification-status change, disputed-issue resolution, canonical-architecture change, publication of sensitive/contextual material, or broad refactor, post a GitHub comment beginning with `APPROVAL REQUIRED` and wait for explicit owner approval.
- Routine reversible maintenance may proceed without approval when it stays within `AGENTS.md`, `.cursor/rules/github-sync-maintenance.mdc`, and `knowledge/sync-policy.md`.
- After each meaningful maintenance batch, post a concise status comment covering what changed, what was not changed, any unresolved issue, and whether owner action is required.

Assistant judgment summary:
- This is an execution-boundary rule, not a technical-claim rule. Recording the protocol on GitHub is itself routine, reversible documentation.

Uncertainty / risk:
- “Canonical architecture” includes extracting ARCH records into new standalone files. Indexing existing names is allowed; materializing full architecture files is approval-gated.

Response strategy:
- Default to the smallest reversible GitHub-side edit.
- Escalate with `APPROVAL REQUIRED` rather than guessing at verification, privacy, or architecture-file extraction.

Sync checkpoint:
- Protocol file: `knowledge/cursor-approval-protocol.md`
- Communication channel: GitHub Issue #1 and related pull requests
- Designated Cursor Agent ID: `bc-01a0a3a4-ff95-7e51-bfd5-9a61684aa081`

Status: ACTIVE_RULE
