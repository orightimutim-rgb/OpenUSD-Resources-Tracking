# Conversation ↔ GitHub Sync Policy

Purpose: keep the public GitHub knowledge layer aligned with the current structured research conversation without exposing personal or sensitive material.

## What is synchronized

- verified technical facts
- working definitions clearly marked as provisional when needed
- official and high-quality source links
- knowledge relationships
- issue / conflict metadata
- versioned summaries of simulation, emulation, digital twin, HIL, OpenUSD, Omniverse, and Physical AI research

## What is not synchronized raw

- personal identifiers
- private case details
- unverified allegations about identifiable people or organizations
- raw emotional passages
- account information or private system data

These may be represented only as de-identified abstract layers when relevant to response-system research.

## Synchronization states

- `VERIFIED`: supported by an appropriate source.
- `WORKING`: useful working model, still domain-dependent.
- `ISSUE`: conflict, overgeneralization, stale source, unsupported claim, or missing verification.
- `HISTORICAL`: retained for provenance but not treated as current guidance.

## Update workflow

1. ingest new conversation material
2. de-duplicate against current records
3. extract technical claims and sources
4. classify FACT / USER_REACTION / AI_RESPONSE_SCRIPT / ISSUE
5. verify where possible
6. update the structured external database
7. write a de-identified GitHub snapshot or patch
8. preserve unresolved issues for later review
9. never silently convert a working claim into a verified fact

## Conflict handling

When two records disagree:
- preserve both source contexts
- create an issue marker
- do not overwrite the earlier record
- resolve only after source comparison
- record the resolution rationale in a later version

## Public-repository rule

This repository is public. Every write must be safe for public disclosure and de-identified by default.
