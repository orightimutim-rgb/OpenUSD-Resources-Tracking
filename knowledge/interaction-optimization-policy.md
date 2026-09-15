# Interaction Optimization Policy

Purpose: reduce serial, toothpaste-style back-and-forth by proactively synthesizing structural consequences while keeping Interaction Learning selective, additive, and reviewable.

## 1. Three-layer interaction optimization

### A. Immediate layer — proactive forward scan
For each meaningful structural issue:
1. identify the current issue
2. inspect adjacent dependencies and likely downstream gaps
3. retrieve related Interaction rules
4. return a compact combined recommendation
5. separate confident actions from review candidates

Goal: solve a cluster, not one isolated symptom.

### B. Batch layer — session synthesis
When several related corrections occur in the same conversation/session:
- group them by structure, not by message order
- detect whether they belong to one higher-level rule
- prefer updating/versioning one Interaction over creating many micro-records
- summarize remaining unresolved structural questions before the session drifts into repetitive turns

### C. Periodic layer — consolidation maintenance
Because the database preserves history and versions rather than overwriting, schedule periodic review of accumulated Interaction records.

Consolidation tasks:
- near-duplicate detection
- superseded-rule detection
- conflict-cluster review
- stale response-strategy detection
- merge candidates into higher-level abstractions
- preserve provenance and old versions
- never delete historical logic merely because a newer abstraction exists

## 2. Retrieval and write discipline

Retrieval is frequent and cheap conceptually; writing is selective.

`RETRIEVE → JUDGE → ACT → FEEDBACK → WRITE GATE`

Possible write outcomes:
- NO WRITE
- UPDATE EXISTING VERSION
- CREATE NEW RULE
- REVIEW CONFLICT

## 3. Proactive response contract

When a user surfaces one structural problem, do not answer only that point if adjacent consequences are reasonably inferable.

Return, when relevant:
- what the user found
- what else this structurally implies
- which existing rule already covers part of it
- what should be changed together
- what should not change
- what requires later consolidation or scheduled review

## 4. Efficiency objective

The optimization target is fewer serial turns, not fewer thoughts.

A useful response should compress multiple likely next questions into one coherent structural answer without overwhelming the user or pretending certainty where it does not exist.

## 5. Context escape — retrieval is not next-question forecasting

INT-0007's forward-scan remains valid for adjacent workflow gaps inside a cluster. It does not mean the user is a sequence of upcoming prompts.

When the current conversation becomes locally repetitive or inefficient:
- stop extending the mirror loop
- retrieve symmetrically from INTERNAL sources (Interaction Learning, Records, Sources, Issues, Architecture References, repository files/history) and EXTERNAL sources (official docs, linked pages, authoritative references)
- return with a consolidated structural answer

Retrieval is the primary escape from conversational recursion. Proactive retrieval is not equivalent to guessing the user's next question. Ordinary-language structural observations remain valid escape triggers.

This section implements INT-0008. It does not replace sections 1–4 and does not rewrite INT-0007.

## 6. Scheduled maintenance principle

Periodic consolidation is needed because additive/versioned storage accumulates history.

Scheduling cadence should be based on actual interaction volume:
- low volume: monthly
- medium volume: weekly
- high-change periods: more frequent review may be appropriate

A scheduled task should not silently rewrite rules. It should produce a consolidation report and proposed merges/updates for review unless prior policy explicitly authorizes automatic low-risk maintenance.
