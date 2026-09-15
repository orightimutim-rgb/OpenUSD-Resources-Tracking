# Interaction Trigger Policy

Purpose: decide automatically, for each meaningful conversation turn, whether the interaction-learning layer should be retrieved, reused, updated, or left unchanged.

This policy is a routing layer. It does **not** create a new Interaction record for every message.

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
  - update/version the closest existing Interaction instead of creating a duplicate

- `CREATE_NEW`
  - a genuinely new reusable interaction pattern appears
  - the pattern is likely to recur
  - the decision logic is materially different from existing rules

- `REVIEW_CONFLICT`
  - current user feedback conflicts with an active interaction rule
  - preserve both contexts
  - do not silently overwrite
  - create a versioned review item

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

## Required decision sequence

`incoming user message`
→ `trigger classification`
→ if triggered: `retrieve similar interaction rules`
→ inspect relevant knowledge layers
→ form current judgment
→ respond / act
→ inspect user feedback
→ decide `NO WRITE / UPDATE / CREATE / REVIEW`
→ synchronize external stores when applicable

## Similarity-first rule

Before creating a new Interaction:

1. search by problem-detection pattern
2. search by user prompt pattern
3. search by reusable rule
4. search by response strategy
5. compare decision basis and outcome

If an existing Interaction substantially covers the case, prefer update/versioning over creation.

## Synchronization transparency

Every external mutation must still distinguish:
- actually executed
- planned only
- not yet written externally
- waiting for authorization
- waiting for verification

## GitHub-side / Cursor maintenance events

The same Trigger Router applies to meaningful GitHub-side maintenance batches, not only chat turns.

A repository event, CI run, status comment, formatting-only change, or changelog-only note is not by itself an Interaction write. Classify the batch first. Retrieve similar existing rules before any Interaction write. Prefer `UPDATE_EXISTING` over `CREATE_NEW`.

High-impact changes to these trigger heuristics require an `APPROVAL REQUIRED` comment on GitHub Issue #1 before this policy is rewritten.

## Retrieval catalog

Human-readable rules live in `knowledge/interaction-learning.md`.

The machine-readable retrieval catalog is `knowledge/interaction-index.json`. Before an Interaction write, search that catalog (or an equivalent similarity search over the markdown rules) by:

1. problem-detection pattern
2. user prompt pattern
3. reusable rule
4. response strategy
5. decision basis and outcome

GitHub-side helper:

```text
python3 scripts/interaction_trigger.py decide --event "<maintenance-event-summary>"
```

The helper suggests a routing outcome. It does not write Interaction records.

## Scope boundary

This policy stores concise, reviewable decision summaries and criteria. It does not store hidden chain-of-thought and does not claim to modify model weights.
