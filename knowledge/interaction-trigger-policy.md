# Interaction Trigger Policy

Purpose: decide automatically, for each meaningful conversation turn, whether the interaction-learning layer should be retrieved, reused, updated, or left unchanged.

This policy is a routing layer. It does **not** create a new Interaction record for every message.

## Control loop — higher priority than prediction

Path selection is specified by INT-0009 / `knowledge/interaction-control-loop-policy.md`. Stage 0 below gates Interaction writes. It does not replace the control loop and must not be reduced to next-question prediction.

For every meaningful turn, interpret the current message structurally, retrieve internal state, retrieve external sources when useful, then judge across conversation / internal / external before choosing an action path. Prediction of the next user question is a weak optional signal and must never constrain that choice. The assistant may leave the current loop at any time.

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
→ `independent structural interpretation` (INT-0009; not next-question prediction)
→ `internal retrieval`
→ `external retrieval when useful`
→ `self-judgment across conversation / internal / external`
→ `choose action path` (stay / retrieve / compare / switch / merge / defer / execute / investigate / synthesize)
→ `trigger classification` (INT-0005 write routing)
→ if triggered: `retrieve similar interaction rules`
→ inspect relevant knowledge layers
→ form current judgment
→ respond / act
→ inspect user feedback
→ decide `NO WRITE / UPDATE-VERSION / CREATE / REVIEW`
→ synchronize external stores when applicable

A predicted next prompt must not skip, reorder, or veto the interpretation, retrieval, or path-choice steps.

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
