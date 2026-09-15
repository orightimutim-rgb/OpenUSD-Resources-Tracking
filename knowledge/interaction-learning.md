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

Retrieval tags: missing, architecture-node, source, relationship, physx, smallest-edit, duplicate-avoidance

Default trigger action: RETRIEVE_ONLY

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

Retrieval tags: synchronization, transparency, persistence-language, authorization, completed-claim

Default trigger action: RETRIEVE_ONLY

Status: ACTIVE_RULE

## INT-0003 — Duplicate detection when record number is forgotten

Problem detection logic:
- The user reposted prior content while unsure of its record number.

Reusable rule:
- Compare core propositions, examples, and knowledge nodes before creating a new record.
- If highly overlapping, preserve the canonical record and create a duplicate relationship instead of incrementing a new REC number.

Retrieval tags: duplicate, forgotten-id, semantic-overlap, record-number

Default trigger action: RETRIEVE_ONLY

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

Retrieval tags: judgment-summary, retrieval, versioning, response-strategy, sync-checkpoint

Default trigger action: RETRIEVE_ONLY

Related operational rule: INT-0005 / `knowledge/interaction-trigger-policy.md`

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
- Canonical routing spec: `knowledge/interaction-trigger-policy.md`
- Retrieval catalog: `knowledge/interaction-index.json`
- GitHub-side helper: `scripts/interaction_trigger.py`

Version note (2026-09-15 GitHub operationalization):
- Cursor GitHub-side maintenance uses the same Trigger Router as conversation turns.
- Retrieve similar existing rules before deciding to write.
- High-impact changes to trigger heuristics require `APPROVAL REQUIRED` on GitHub Issue #1.
- This batch does not create a new Interaction ID; INT-0005 already covers the routing layer.

Uncertainty / risk:
- Open pull request #2 drafts a different rule also numbered INT-0005 (owner approval/notification protocol). That is a numbering collision, not a merge of the two rules. INT-0005 on `main` remains the retrieval-trigger rule. PR #2 should rebase and assign a new ID to the approval-protocol rule.
- Token-overlap retrieval in `scripts/interaction_trigger.py` is an implementation aid, not a replacement for the canonical policy. A different similarity heuristic would be a high-impact policy change and needs owner approval.

Retrieval tags: trigger-router, retrieve-before-write, write-gate, no-log-every-event, classification

Default trigger action: RETRIEVE_ONLY

Status: ACTIVE_RULE
