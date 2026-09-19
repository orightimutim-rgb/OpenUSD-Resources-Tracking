# Source Index

Status: WORKING inventory derived from `knowledge/chat-sync-2026-09-15.md` section 10 and live URL checks on 2026-09-15.

Purpose: normalize the GitHub-side source inventory without assigning unverified Airtable `SRC-*` IDs and without changing claim verification status.

`knowledge/sync-state.json` lists `SRC-0001` through `SRC-0010`, but this repository does not yet contain a title-to-ID map. Those ten IDs are therefore not attached to rows below. The chat snapshot lists sixteen named sources. That count mismatch is tracked as `ISSUE-GH-001` in `knowledge/issue-index.md`.

Category reminder:

- official dictionary or product pages are sources, not architecture nodes
- NVIDIA glossary/product pages remain vendor sources unless an Architecture Reference exists
- a vendor source is not automatically an industry-wide definition

## Inventory

| Snapshot name | Candidate URL | HTTP check 2026-09-15 | Notes |
| --- | --- | --- | --- |
| Cambridge Dictionary — simulator definition | https://dictionary.cambridge.org/dictionary/english/simulator | 200 | Candidate official dictionary page. Exact Airtable binding unverified. |
| iT 邦幫忙 — Simulator / Emulator comparison | https://ithelp.ithome.com.tw/articles/10299630 | 403 | Candidate article title: “The Hardware Platform of System Software – Simulator/Emulator”. A second comparison-like article exists at https://ithelp.ithome.com.tw/articles/10319697 (also 403). Exact canonical article is unverified. 403 may be bot filtering rather than a dead page. |
| Microsoft Flight Simulator official page | https://www.flightsimulator.com/ | 200 | Candidate official product page. |
| DJI Flight Simulator historical product / end-of-support information | https://www.dji.com/downloads/products/dji-flight-simulator | 404 | Snapshot already treats this product as historical. Do not substitute DJI Virtual Flight or DJI Simulator without owner/Airtable confirmation; those are different product names. |
| Simulator.io | https://simulator.io/ | 200 | Product homepage reachable. |
| NVIDIA Omniverse official page | https://www.nvidia.com/en-us/omniverse/ | 200 | Vendor product page. |
| NVIDIA Omniverse Developer | https://developer.nvidia.com/omniverse | 200 | Vendor developer page. |
| NVIDIA OpenUSD for Developers | https://developer.nvidia.com/openusd | 200 | `https://developer.nvidia.com/usd` redirected here. |
| NVIDIA PhysX SDK | https://developer.nvidia.com/physx-sdk | 200 | Also related: https://github.com/NVIDIA-Omniverse/PhysX (200). Source vs ARCH-0005 distinction remains: source page ≠ architecture node. |
| NVIDIA Design & Simulation | previously expected: https://www.nvidia.com/en-us/omniverse/solutions/design-and-simulation/ | 404 | Stale candidate URL. No equivalent replacement was confirmed in this pass. Leave mapped to the snapshot name only. |
| NVIDIA Physical AI glossary | https://www.nvidia.com/en-us/glossary/generative-physical-ai/ | 200 | `https://www.nvidia.com/en-us/glossary/physical-ai/` redirected here. Treat as vendor official definition source for ARCH-0001, not as an industry-wide definition. |
| NVIDIA World Models glossary | https://www.nvidia.com/en-us/glossary/world-models/ | 200 | Vendor official definition source for ARCH-0002. |
| NVIDIA Digital Twin glossary | https://www.nvidia.com/en-us/glossary/digital-twin/ | 200 | Vendor official definition source. Digital Twin remains broader than HIL. |
| NVIDIA Synthetic Data glossary | previously expected: https://www.nvidia.com/en-us/glossary/synthetic-data/ | 404 | Nearby live page: https://www.nvidia.com/en-us/glossary/synthetic-data-generation/ (200). Equivalence of the two glossary titles is unverified; do not silently replace the snapshot name. |
| NVIDIA Isaac Lab | https://developer.nvidia.com/isaac/lab | 200 | `https://developer.nvidia.com/isaac-lab` redirected here. Vendor product mapping. |
| NVIDIA Isaac Sim | https://developer.nvidia.com/isaac/sim | 200 | `https://developer.nvidia.com/isaac-sim` redirected here. Vendor product mapping. |

## Link-check summary

Reachable in this pass: Cambridge simulator, Microsoft Flight Simulator, Simulator.io, Omniverse official, Omniverse developer, OpenUSD developer, PhysX SDK, Physical AI glossary (redirected), World Models glossary, Digital Twin glossary, Isaac Lab, Isaac Sim.

Broken or stale candidate URLs:

1. DJI Flight Simulator product download page — 404
2. NVIDIA Design & Simulation solutions URL — 404
3. NVIDIA Synthetic Data glossary URL as named in the snapshot — 404

Checker-limited:

- iT 邦幫忙 candidate articles returned 403 to this environment

## What this index does not do

- It does not mark any source VERIFIED in Airtable.
- It does not invent `SRC-0011`–`SRC-0016`.
- It does not collapse DJI Flight Simulator, DJI Virtual Flight, and DJI Simulator.
- It does not treat NVIDIA glossary wording as a universal industry definition.
