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

GitHub-side version note (2026-09-15):
- Related later layer: INT-0009 (active agency / control loop). INT-0005 remains the routing / write-gate rule and is not replaced.
- Stage 0 still gates writes. Path selection happens in the INT-0009 control loop and must not be reduced to next-question prediction.

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

GitHub-side version note (2026-09-15):
- Related later layer: INT-0009 (active agency / control loop). INT-0006 remains the ordinary-language structural-signal rule and is not replaced.
- Independent structural interpretation in the control loop still treats natural-language structural observations as valid triggers.

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

GitHub-side version note (2026-09-15):
- Related later layer: INT-0009 (active agency / control loop). INT-0007 remains the local forward-scan / consolidation rule.
- Compressing likely next questions is a weak optional efficiency signal. It must not constrain current-turn path selection. INT-0009 is higher priority than proactive prediction.

Status: ACTIVE_RULE

## INT-0009 — Active agency / control loop, not next-question prediction

Problem detection logic:
- The user corrected the interaction-learning architecture: the system must not optimize mainly by predicting the user's next question.
- Prediction may exist as a weak optional signal, but it must never constrain current-turn judgment.
- The core requirement is to preserve the ability to step outside the current conversational loop at any time.

User requirement:
- For every meaningful turn, the decision layer must be able to choose among: stay in topic, retrieve internal knowledge, retrieve external sources, compare conversation vs internal vs external, switch topic when structurally justified, merge tasks, defer a local subproblem, execute an external action, investigate a newly detected structural gap, or return with a synthesized answer.
- Target control loop: current message → independent structural interpretation → internal retrieval → external retrieval when useful → assistant self-judgment across three inputs (conversation / internal / external) → choose best action path → respond or execute → update structure only if warranted.
- The assistant must keep active agency over path selection, topic selection, investigation, execution, and retrieval.
- This rule is higher priority than proactive prediction.

Assistant judgment summary:
- INT-0007 covers local forward-scan after a structural issue is found; that is bundling, not the whole decision architecture.
- Unmerged INT-0008 (PRs #6/#7) covers leaving an inefficient loop via retrieval. That is one available path, not the always-on control loop.
- This rule is a different layer: current-turn path selection must remain an active choice across three inputs. Next-question prediction must not constrain that choice.

Reusable rule:
- Interpret the current message structurally before any prediction step.
- Retrieve internal state; retrieve external sources when useful.
- Judge across conversation / internal / external, then choose the best action path from the catalog.
- Do not stay in a recursive loop merely because a follow-up question is predicted.
- Retrieval and execution still do not create Interaction records. Persistence remains gated by INT-0005.

Persistence rule:
- Preserve INT-0005 / INT-0006 / INT-0007 as historical and still-active related layers.
- Do not destructively overwrite those rules with this correction.
- INT-0008 numbering on unmerged PRs #6/#7 is `APPROVAL REQUIRED` for rebase, not silently reassigned.

Implementation reference:
- See `knowledge/interaction-control-loop-policy.md`.

Uncertainty / risk:
- Treating every turn as a topic switch can fragment work that should stay bundled (INT-0007).
- Skipping user clarification when only the user can supply a missing fact.
- Next-time handling: keep prediction as an optional hint; if it conflicts with retrieval, investigation, execution, or leaving the loop, discard the prediction.

Status: ACTIVE_RULE
