# Dynamic Context Principle

Status: WORKING PRINCIPLE

Purpose: define what "dynamic" means for this repository so Cursor and other agents can continue making useful progress when context is incomplete, changing, or expressed without technical vocabulary.

## Core definition

Dynamic does not mean "constantly create new records, rules, or structures."

Dynamic means:
- existing information can be re-found when the situation changes
- existing relationships can be re-evaluated and reconnected
- missing context can be detected without requiring the user to know the technical name of the gap
- the system can choose a reasonable next investigative or organizational step instead of stopping only because the current state is incomplete
- the quality of judgment should remain stable across changing inputs, uncertainty, and partial knowledge
- new information should first be tested against existing context before a new rule or structure is created

Unknown does not equal stop.

## Active behavior under uncertainty

When context is incomplete, prefer:

1. retrieve relevant existing context
2. inspect relationships, dependencies, boundaries, and prior decisions
3. identify what is missing or ambiguous
4. choose the smallest useful next step that is allowed
5. preserve uncertainty explicitly
6. escalate only when the next action crosses an approval, verification, privacy, or canonical-change boundary

The system should not require the user to already know the correct database, schema, coding, or retrieval terminology before useful work can continue.

## "Proactive" meaning

Proactive does not mean unrestricted autonomous writing.

Proactive means the system may independently:
- notice structural signals
- retrieve relevant context
- compare alternatives
- detect duplication or gaps
- trace dependencies
- prepare a candidate change
- recommend the next step
- continue investigation within allowed boundaries

State-changing actions remain subject to the applicable write and approval gates.

## Context-thread model

Treat new information as a thread to be connected, not as proof that a new concept must be created.

For each new signal:

`new signal`
→ `retrieve related context`
→ `trace existing relationships`
→ `identify missing connection / conflict / boundary`
→ `reuse or update existing structure when possible`
→ `create new structure only when materially distinct`

This repository should therefore prefer continuity, provenance, and reconnection over unnecessary novelty.

## Interaction with existing rules

This principle is an upper-level operating rule and does not replace existing Interaction IDs.

- INT-0005 governs retrieval/write routing and write gating.
- INT-0006 recognizes structure-first user signals without requiring technical vocabulary.
- INT-0007 performs proactive forward-scan and consolidation.
- Proposed INT-0008 work concerns context escape / broader retrieval when the current loop is insufficient.
- Proposed INT-0009 work concerns active action-path selection above prediction.
- INT-0010 governs owner approval and notification protocol.

Do not create a new INT merely because this principle is expressed with different wording. First determine whether the behavior is already covered by an existing active or proposed rule.

## Cursor execution rule

Before creating a new Interaction rule, policy, index entry, or architecture node because of a newly observed concept:

1. search existing repository knowledge for the same underlying capability
2. compare behavior, not wording
3. classify the finding as:
   - existing rule already covers it
   - existing rule needs additive/versioned refinement
   - unresolved conflict
   - genuinely distinct capability
4. prefer linkage or refinement over duplication
5. preserve provenance when meaning changes
6. use the applicable approval gate before any gated write or canonical restructuring

## Quality objective

The objective of a dynamic system is not maximum activity.

The objective is:
- remain useful when information is incomplete
- avoid repeated rediscovery of the same context
- avoid forcing the user to supply missing technical vocabulary
- preserve stable decision quality while the environment changes
- keep enough initiative to move toward the next useful state without bypassing owner-controlled gates
