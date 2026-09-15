# Conversation ↔ Airtable ↔ GitHub Sync Policy

Status: ACTIVE for in-conversation synchronization.

Purpose: keep the public GitHub knowledge layer aligned with the structured Airtable knowledge database and the current research conversation, without exposing personal or sensitive material.

## What is synchronized

- verified technical facts
- working definitions clearly marked as provisional when needed
- official and high-quality source links
- knowledge relationships
- issue / conflict metadata
- Architecture References: official definitions, vendor product mapping, vendor implementation frameworks
- Interaction Learning: de-identified problem-detection logic, prompt patterns, assistant judgment summaries, decision bases, user validation, reusable rules, response strategies, uncertainty/risk, sync checkpoints
- versioned summaries of simulation, emulation, digital twin, HIL, OpenUSD, Omniverse, PhysX, Physical AI, world models, synthetic data, Isaac Sim, and Isaac Lab research

## What is not synchronized raw

- personal identifiers
- private case details
- unverified allegations about identifiable people or organizations
- raw emotional passages
- account information or private system data
- hidden model chain-of-thought

These may be represented only as de-identified abstract layers when relevant to response-system research. Assistant reasoning stored here must be a shareable judgment summary, not hidden internal reasoning.

## Synchronization states

- `VERIFIED`: supported by an appropriate source.
- `WORKING`: useful working model, still domain-dependent.
- `ISSUE`: conflict, overgeneralization, stale source, unsupported claim, or missing verification.
- `HISTORICAL`: retained for provenance but not treated as current guidance.
- `ACTIVE_RULE`: reusable interaction or synchronization rule currently applied.

## Active update workflow

1. ingest new conversation material
2. retrieve similar Interaction Learning records first when relevant
3. de-duplicate against Records / Sources / Architecture References
4. extract technical claims and sources
5. classify FACT / USER_REACTION / AI_RESPONSE_SCRIPT / ISSUE where applicable
6. record assistant structure notes, judgment summary, uncertainty/risk, response strategy, and sync checkpoints for important interactions
7. verify where possible
8. update Airtable structured database
9. write the de-identified GitHub snapshot or patch in the same conversation workflow
10. preserve unresolved issues for later review
11. never silently convert a working claim into a verified fact
12. explicitly state what was actually synchronized and what was not

## Interaction-learning rule

For recurring problem types such as missing sources, architecture gaps, duplicate records, synchronization ambiguity, vendor mapping, and issue handling:
- search the interaction-learning layer first
- reuse prior decision rules when still applicable
- create a new version when the new case conflicts with an older rule
- retain the user's validation/correction as part of the rule history

Automatic retrieval is not next-prompt prediction. When a maintenance turn becomes recursive or locally inefficient, leave the conversational loop and retrieve INTERNAL sources and EXTERNAL authoritative sources in the same pass, then return a consolidated structural answer. Retrieval still does not create an Interaction record.

## Conflict handling

When two records disagree:
- preserve both source contexts
- create an issue marker
- do not overwrite the earlier record
- resolve only after source comparison
- record the resolution rationale in a later version

## Public-repository rule

This repository is public. Every write must be safe for public disclosure and de-identified by default.

## Automation boundary

This policy is active whenever the assistant is handling this knowledge project in the conversation and can call the connected tools. It does not mean ChatGPT can monitor every future chat while inactive or push changes in the background without an event source. Full unattended synchronization requires a separate webhook/API/n8n-style trigger pipeline.
