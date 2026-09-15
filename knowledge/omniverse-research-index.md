# Omniverse / Physical AI research structure

Status: WORKING GitHub-side hub for Issue #1 Omniverse continuation. This is not an Airtable source map and does not invent `SRC-*` IDs.

Designated Cursor Agent ID: `bc-01a0a3a4-ff95-7e51-bfd5-9a61684aa081`

Purpose: keep the four named NVIDIA/user links as **separate source/deep-dive nodes**, link them to existing Omniverse / Physical AI / Digital Twin / simulation-validation structure, and avoid duplicate sources.

## Classification used in this batch

| Named link | GitHub node | Problem class | Action |
| --- | --- | --- | --- |
| PhysX SDK | [physx-sdk.md](deep-dives/physx-sdk.md) | existing source; architecture node already named as ARCH-0005 | Directory-summary only. Do not create a second PhysX source. |
| Autonomous Vehicle Simulation | [autonomous-vehicle-simulation.md](deep-dives/autonomous-vehicle-simulation.md) | missing source and missing standalone deep-dive | New source + incomplete directory-summary. |
| Smart Cities and Spaces | [smart-cities-and-spaces.md](deep-dives/smart-cities-and-spaces.md) | missing source and missing standalone deep-dive | New source + incomplete directory-summary. |
| YouTube `XeHtw36h-eI` | [youtube-xehtw36h-ei.md](deep-dives/youtube-xehtw36h-ei.md) | missing source; content not independently verified | Source stub only. Not marked learned/read. |

## Keep these distinct

- PhysX SDK ≠ Newton (Newton is a related next-generation physics engine marker, not a PhysX alias).
- Autonomous Vehicle Simulation landing page ≠ PhysX Vehicle Dynamics feature ≠ the YouTube sensor-simulation clip.
- Smart Cities and Spaces landing page ≠ Digital Twin glossary definition ≠ Omniverse product page.
- Official Definition / Vendor Product Mapping / Vendor Standard or Implementation Framework remain separate. These four nodes are vendor sources or working directory summaries, not industry-wide standards.
- Dedicated ARCH-0001–ARCH-0005 files are still absent on `main`. Extracting them remains `APPROVAL REQUIRED` (see unmerged PR #2 / ISSUE-GH-002). This hub **links** to the named architecture IDs; it does not materialize full ARCH records.

## Structural links

```text
Physical world / planned system
→ sensed or authored data
→ Digital Twin / OpenUSD scene
→ physics simulation (PhysX; Newton relation marker)
→ sensor simulation / synthetic data
→ world model / policy learning
→ validation
→ review / deployment
```

Node placement in that working pipeline:

| Node | Pipeline role | Named architecture links |
| --- | --- | --- |
| PhysX SDK | physics simulation | ARCH-0003, ARCH-0005; also Isaac Sim/Lab product mapping |
| Autonomous Vehicle Simulation | sensor simulation, synthetic data, closed-loop validation | ARCH-0001 Physical AI; ARCH-0002 World Model; ARCH-0003/0004 vendor mapping/stack |
| Smart Cities and Spaces | digital-twin / Physical AI application domain | ARCH-0001; Digital Twin working layer; Omniverse vendor mapping |
| YouTube `XeHtw36h-eI` | unverified AV sensor-simulation illustration | related to AV Simulation + Omniverse; not a substitute for either source |

## Retrieval executed 2026-09-15

Internal: `knowledge/chat-sync-2026-09-15.md`, INT-0001–INT-0008, unmerged PR #2 source/architecture indexes (not copied wholesale).

External: live fetches of the four named URLs. PhysX body text was retrieved. AV Simulation body text was retrieved from the official page. Smart Cities body text was retrieved. YouTube title/description/transcript were retrieved but claims are **not verified** and the video is **not marked learned**.

## What this hub does not do

- No Airtable write.
- No `SRC-0011+` IDs.
- No collapse of these four nodes into one Omniverse page.
- No promotion of NVIDIA landing-page wording to industry-wide definition.
- No silent resolution of ISSUE-0001–ISSUE-0010.
