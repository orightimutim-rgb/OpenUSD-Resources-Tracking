# Interaction Trigger Policy

Purpose: decide automatically, for each meaningful conversation turn, whether the interaction-learning layer should be retrieved, reused, updated, or left unchanged.

This policy is a routing layer. It does **not** create a new Interaction record for every message.

## Core distinction — retrieval is not writing

Automatic retrieval and Interaction persistence are separate operations.

- Retrieval may run frequently whenever prior interaction logic could materially change the response.
- Retrieval alone must not create a new Interaction record.
- A write occurs only after the Interaction Write Gate is satisfied.
- Therefore, "retrieve often, write conservatively" means broad lookup with sparse persistence.

When a write is justified, preserve history through versioning or additive event records rather than destructive overwrite. Earlier judgments, corrections, and rule states should remain traceable.

## Stage 0 — Trigger Router

For each user message, classify the turn before creating or editing Interaction Learning data.

Possible outcomes:

- `NO_INTERACTION_ACTION`
  - ordinary factual question
  - no recurring workflow pattern
  - no correction of assistant behavior
  - no new decision method
  - no synchronization or retrieval issue

- `RETRIEVE_ONLY`
  - current turn resembles a known workflow pattern
  - prior interaction rules may materially affect how the assistant should respond
  - retrieve similar Interaction Learning rules before deciding
  - do not write a new Interaction unless the current case changes the rule

- `UPDATE_EXISTING`
  - user feedback modifies, narrows, corrects, or strengthens an existing reusable interaction rule
  - version the closest existing Interaction instead of replacing its historical context

- `CREATE_NEW`
  - a genuinely new reusable interaction pattern appears
  - the pattern is likely to recur
  - the decision logic is materially different from existing rules

- `REVIEW_CONFLICT`
  - current user feedback conflicts with an active interaction rule
  - preserve both contexts
  - do not silently overwrite
  - create a versioned review item

## Structure-first signal rule

The user's messages should be interpreted by structural meaning rather than by technical vocabulary.

The user may not use database, programming, encoding, or data-model terminology. Natural-language observations still count as strong retrieval triggers when they identify structural properties such as:

- missing or extra parts
- hierarchy or layer relationships
- ordering or sequence
- correspondence or mismatch
- duplication
- dependency
- cause/effect or handoff structure
- synchronization gaps
- classification boundaries
- whether two things should remain distinct or be linked

Do not require the user to translate these observations into technical terms before the system recognizes them.

## Automatic retrieval triggers

Retrieve Interaction Learning before responding when one or more of these are present:

1. user says or implies something is missing, duplicated, inconsistent, stale, wrongly classified, or incompletely synchronized
2. user corrects the assistant's workflow, judgment, sequencing, or execution behavior
3. user refers to how a similar problem was handled before
4. the task modifies Airtable, GitHub, Cursor, automation, synchronization, indexing, database structure, or long-running research workflow
5. the assistant is about to claim something was completed, persisted, synchronized, verified, or resolved
6. the user asks to continue, resume, reuse, compare, align, remember, or follow an established project method
7. a new source appears structurally important and may require source / relationship / architecture-node classification
8. there is a risk of creating duplicate Records / Sources / Architecture References / Interaction records
9. the user identifies a structural relationship in plain language even without technical terminology
10. the current conversation is locally repetitive, circling, or only extending the current mirror loop (context escape; INT-0008)
11. a structural question requires INTERNAL and EXTERNAL sources together, not chat continuation alone

## Interaction write gate

After retrieval, do **not** write by default.

Write only if at least one of these is true:

- a new reusable decision rule was discovered
- an existing rule needs correction or stronger scope
- the user's validation changes the assistant's future response strategy
- a repeated failure pattern is identified
- a new synchronization checkpoint becomes necessary
- an old rule is now obsolete, conflicting, or requires versioning

Otherwise keep the interaction database unchanged.

## Persistence model — additive and versioned

When writing Interaction Learning data:

- do not erase prior rule states merely because a newer judgment exists
- preserve the previous version or event context
- add the new correction, refinement, or state transition
- maintain a current active rule pointer/status if useful, while retaining earlier versions for provenance
- use conflict/review records when two judgments cannot yet be reconciled

This is intended to produce layered learning history, not a flat chat log and not destructive replacement.

## Required decision sequence

`incoming user message`
→ `trigger classification`
→ if triggered: `retrieve similar interaction rules`
→ if the local conversation is repetitive or inefficient: `context escape` (stop extending the mirror loop; retrieve INTERNAL and EXTERNAL sources; return a consolidated structural answer)
→ inspect relevant knowledge layers
→ form current judgment
→ respond / act
→ inspect user feedback
→ decide `NO WRITE / UPDATE-VERSION / CREATE / REVIEW`
→ synchronize external stores when applicable

Context escape and retrieval do not create Interaction records. Extending a locally inefficient loop is not an acceptable substitute for retrieval.

## Symmetric retrieval scope

Automatic retrieval applies to INTERNAL and EXTERNAL sources on the same trigger. Do not retrieve only from the chat transcript or only from Interaction Learning.

INTERNAL sources:
- Interaction Learning rules and catalogs
- Records
- Sources
- Issues
- Architecture References
- repository files and history

EXTERNAL sources:
- official documentation
- linked pages already in the source set
- other authoritative references implicated by the current structure

Ordinary-language structural observations are valid triggers for this dual-source retrieval even when the user does not use technical vocabulary.

## Context escape from conversational recursion

Do not model the user only as a sequence of prompts. Treat their behavior as a structure-first retrieval strategy: they inspect structure, detect local inefficiency, and jump out of the current loop.

Trigger a context escape when one or more of these are present:
- the conversation is repeating the same structural question with only incremental wording changes
- replies are mirroring the current thread instead of searching the relevant knowledge space
- the user indicates that continuing in-loop is inefficient, incomplete, or the wrong layer
- a needed answer lives in an internal catalog or an external official/linked source rather than in further chat continuation

When context escape triggers:
1. stop extending the current mirror loop
2. retrieve INTERNAL and EXTERNAL sources together
3. return one consolidated structural answer
4. do not treat that retrieval as forecasting the user's next question

Context escape is the primary mechanism for leaving conversational recursion. It is not a new Stage 0 outcome and does not persist a record by itself.

## User-model boundary

Proactive retrieval is lookup across the relevant knowledge space. It is not:
- predicting the next prompt
- continuing a serial Q&A chain one step ahead
- a substitute for INT-0007's adjacent forward-scan when the cluster is still in-scope and efficient

If forward-scan and context escape both appear applicable, prefer escape-and-retrieve over another in-loop adjacent guess.

## Similarity-first rule

Before creating a new Interaction:

1. search by problem-detection pattern
2. search by user prompt pattern
3. search by reusable rule
4. search by response strategy
5. compare decision basis and outcome

If an existing Interaction substantially covers the case, prefer versioning that existing Interaction over creating a near-duplicate.

## Synchronization transparency

Every external mutation must still distinguish:
- actually executed
- planned only
- not yet written externally
- waiting for authorization
- waiting for verification

## Scope boundary

This policy stores concise, reviewable decision summaries and criteria. It does not store hidden chain-of-thought and does not claim to modify model weights.
