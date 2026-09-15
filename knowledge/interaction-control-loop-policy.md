# Interaction Control Loop Policy

Purpose: keep current-turn judgment under active assistant agency. Prediction of the user's next question is optional and weak. It must never constrain path selection.

This policy is specified by INT-0009. It does **not** replace INT-0005 (retrieve vs write), INT-0006 (ordinary-language structure signals), INT-0007 (local forward-scan / consolidation), or unmerged INT-0008 (context-escape when a loop is inefficient).

## 1. Priority

`INT-0009 active agency / control loop` is higher priority than proactive prediction.

- INT-0007 may still bundle adjacent structural consequences after a path is chosen.
- Compressing "likely next questions" is a weak optional efficiency signal, not the optimization target.
- A predicted next prompt must not veto retrieval, topic change, deferral, execution, investigation, or leaving the current loop.
- The assistant must remain able to step outside the current conversational loop at any time.

## 2. Do not optimize mainly by prediction

The system must not treat the user as a sequence of prompts to be forecast.

Allowed:
- notice that a follow-up is likely
- use that notice only as a weak hint after independent structural interpretation

Disallowed:
- choosing the current action because it matches the predicted next question
- staying in a recursive loop in order to keep the predicted topic alive
- skipping internal or external retrieval because the next prompt is assumed
- reducing path selection, topic selection, investigation, execution, or retrieval to next-turn prediction

## 3. Target control loop

For every meaningful turn:

`current message`
→ `independent structural interpretation`
→ `internal retrieval`
→ `external retrieval when useful`
→ `assistant self-judgment across three inputs: conversation / internal / external`
→ `choose best action path`
→ `respond or execute`
→ `update structure only if warranted`

Independent structural interpretation happens before any prediction step. Retrieval is not forecasting. Persistence remains gated by INT-0005: retrieval and action do not by themselves create an Interaction record.

## 4. Active action catalog

The decision layer must be able to choose among these paths. More than one may apply; the assistant selects the best combination rather than defaulting to the next local continuation.

- stay in the current topic
- retrieve internal knowledge / database / repository state
- retrieve external authoritative sources
- compare conversation vs internal state vs external sources
- switch topic when structurally justified
- merge multiple tasks into one batch
- defer a local subproblem
- execute an external action
- investigate a newly detected structural gap
- return to the conversation with a synthesized answer

Leaving the current loop is always available. It is not reserved for an inefficiency detector, and it is not the same as predicting the next user question.

## 5. Three-input self-judgment

Before choosing a path, compare:

1. **Conversation** — the current message and local thread
2. **Internal** — Interaction Learning, Records, Sources, Issues, Architecture References, repository files, and history
3. **External** — official docs, linked pages, and other named authoritative references, when they are useful and actually retrievable

If one of these inputs is missing or unverified, say so. Do not invent completeness. Do not let a predicted next prompt substitute for a missing internal or external check.

## 6. Relation to other Interaction layers

| Layer | Role relative to this policy |
| --- | --- |
| INT-0005 | Write gate after the path is chosen. Retrieval still does not persist records. |
| INT-0006 | Ordinary-language structural observations remain valid triggers for interpretation and retrieval. |
| INT-0007 | Local forward-scan / consolidation may run after a path is chosen. It must not constrain the path. |
| INT-0008 (unmerged PRs #6/#7) | Context-escape via retrieval when a loop is inefficient. That is one available path here, not the whole decision architecture. |

Do not destructively overwrite those rules. If this control loop appears to conflict with a historical rule, mark `APPROVAL REQUIRED` rather than silently rewriting history.

## 7. Persistence

`respond or execute` is separate from `update structure`.

Write Interaction Learning only when the INT-0005 write gate is satisfied. Preserve prior rule states additively/versioned.
