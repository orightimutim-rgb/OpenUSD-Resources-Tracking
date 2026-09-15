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
- Related later layer: INT-0008 (context-escape retrieval). INT-0005 remains the routing / write-gate rule and is not replaced.

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
- Related later layer: INT-0008 (context-escape retrieval). INT-0006 remains the ordinary-language structural-signal rule and is not replaced.

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
- Related later layer: INT-0008 (context-escape retrieval). INT-0007 remains the local forward-scan / consolidation rule and is not replaced by INT-0008.

Status: ACTIVE_RULE

## INT-0008 — Context-escape retrieval, not next-prompt prediction

Problem detection logic:
- The user distinguished STRUCTURE from linear dialogue flow.
- They do not merely follow the conversation forward. They inspect the current loop, recognize when it is becoming inefficient or recursive, and jump OUT of that loop to retrieve information from both internal and external sources.
- Modeling the user only as a sequence of prompts therefore misses the actual strategy.

User requirement:
- Automatic retrieval must apply symmetrically to INTERNAL sources (Interaction Learning, Records, Sources, Issues, Architecture References, repository files/history) and EXTERNAL sources (official docs, linked pages, authoritative references).
- When the current conversation becomes locally repetitive or inefficient, trigger a context escape: stop extending the mirror loop, search the relevant internal/external knowledge space, then return with a consolidated structural answer.
- Retrieval is the primary escape mechanism from conversational recursion.
- User natural-language structural observations remain valid retrieval triggers even without technical vocabulary.
- Do not interpret proactive retrieval as merely forecasting the user's next question.

Assistant judgment summary:
- INT-0006 covers detecting structural meaning in ordinary language.
- INT-0007 covers bundling adjacent consequences after a structural issue is found.
- This rule is a different layer: when the local conversational loop itself is the problem, leave it via retrieval rather than extending it with another predicted prompt.

Reusable rule:
- Treat the user as a structure-first retrieval actor, not as a linear prompt sequence.
- If the turn is becoming recursive, inefficient, or mirror-like, stop generating the next local continuation.
- Retrieve internally and externally in the same pass.
- Return one consolidated structural answer: what was found, what remains distinct, what is still unverified, and what should not be invented.
- Retrieval still does not create an Interaction record. Persistence remains gated by INT-0005.

Persistence rule:
- Preserve INT-0005 / INT-0006 / INT-0007 as historical and still-active related layers.
- Do not destructively overwrite those rules with this correction.

Uncertainty / risk:
- Leaving a loop too early can skip needed clarification.
- Treating a marketing landing page as a complete deep-dive can overstate verification.
- Next-time handling: escape when the same structural question is being re-asked or locally restated; stay in the loop when a genuine missing fact must come from the user.

Status: ACTIVE_RULE
