# Omniverse Developer portal — knowledge tree

Status: WORKING GitHub-side directory/relationship map.
GitHub node: `GH-OV-DEV-PORTAL-TREE`
Root URL: https://developer.nvidia.com/omniverse
Retrieved: 2026-09-15 (live page + learning-library JSON)
Learned/read of root: **Partial** — entry node captured; linked branches are not fully read.

Designated Cursor Agent ID: `bc-01a0a3a4-ff95-7e51-bfd5-9a61684aa081`

This file is the retrievable map for later turns. Machine-readable companion: [`omniverse-developer-portal-tree.json`](omniverse-developer-portal-tree.json).

## Classification (INT-0001)

| Question | Answer |
| --- | --- |
| Is the root a new source? | No. `NVIDIA Omniverse Developer` is already in `knowledge/chat-sync-2026-09-15.md` section 10 and in unmerged PR #2 `knowledge/source-index.md`. |
| What was missing? | Relationship / tree structure. The page was treated as a landing-page summary instead of a **root knowledge portal**. |
| New Interaction record? | No. Merged into the continuing correction stream (INT-0001 / INT-0005 / INT-0006 / INT-0007). |
| New `SRC-*` IDs? | No. Airtable was not writable in this environment (MCP unauthenticated; no `AIRTABLE_TOKEN`). |
| Root fully learned? | **No.** First-level destinations remain unread unless an existing node already covers them. |

Read-status vocabulary used here:

- **Read**: destination content independently retrieved and captured.
- **Partial**: node exists in inventory and/or the root card was captured, but the destination was not deeply read.
- **Pending**: destination not retrieved; listed so later turns can auto-retrieve the URL.

Vendor card wording on the root page is **WORKING vendor product mapping**, not an Official Definition and not an industry-wide standard.

## Root = entry node, not completion

```text
https://developer.nvidia.com/omniverse          ROOT (Partial)
├── Quick links / docs & community              Pending
├── Omniverse AI Agent Skills                   Pending (6 skills)
├── Omniverse Tools for Agents                  Pending
│   ├── ovphysx / ovrtx / ovstage / ovstorage / ovstream / ovui
│   ├── SimReady Foundation / simready-validate
│   └── USD tools (agents, search, convert, exchange, optimize, validation, OpenUSD)
├── Simulation Libraries for Physical AI        mixed (PhysX Partial; others Pending)
├── Blueprints and Agent Workflows              Pending
└── Learning Resources                          Partial catalog (57 items listed; none marked learned)
```

Live page title retrieved this pass: **NVIDIA Omniverse Libraries**. Vendor description: tools/libraries for developers and AI agents to build simulation-ready worlds for physical AI. That wording is not promoted to a verified industry definition.

## Inventory comparison before creating nodes

Compared against:

- GitHub `knowledge/chat-sync-2026-09-15.md` section 10 (canonical named source set on `main`)
- Unmerged PR #2 `knowledge/source-index.md` / `knowledge/architecture-index.md`
- Unmerged PR #7 `knowledge/omniverse-research-index.md` (PhysX / AV Simulation / Smart Cities / YouTube stubs)
- Airtable: **not queried** this pass (no authenticated Airtable access). Do not invent `SRC-*` bindings.

| First-level node | Published URL | Inventory match | Read status | Action this batch |
| --- | --- | --- | --- | --- |
| Omniverse Developer (root) | https://developer.nvidia.com/omniverse | Existing named source | Partial | Directory/tree only. Do not duplicate the source. |
| OpenUSD | https://developer.nvidia.com/openusd | Existing named source (`NVIDIA OpenUSD for Developers`) | Partial | Link only. |
| PhysX | https://github.com/NVIDIA-Omniverse/PhysX and https://developer.nvidia.com/physx-sdk | Existing named source + ARCH-0005 | Partial | Link only. Unmerged PR #7 has a directory summary; do not recreate it. |
| Isaac Sim / Isaac Lab | appear in learning-library cards, not as first-level tool cards | Existing named sources | Partial | Keep as product-mapping sources; do not collapse into this portal. |
| Newton Physics | https://developer.nvidia.com/newton-physics | Related marker in PhysX notes; not a standalone section-10 source | Pending | Missing source + missing relationship. No `SRC-*` invented. |
| NuRec | https://docs.nvidia.com/nurec/index.html | Not in section 10; PR #7 flagged dedicated ARCH as review | Pending | Missing source. Keep distinct from PhysX and from the AV Simulation landing page. |
| PhysicsNeMo | https://developer.nvidia.com/physicsnemo | Not in section 10 | Pending | Missing source. |
| NVIDIA Warp | card on root; **Learn More currently points at Newton** | Not in section 10 | Pending | Missing source. **Do not merge Warp into Newton.** See open defects. |
| Agent Skills catalog | https://github.com/NVIDIA/skills | Not in section 10 | Pending | Missing source (skill catalog). |
| ovphysx | https://github.com/NVIDIA-Omniverse/PhysX/tree/main/ovphysx | Related to PhysX repo; not a separate named source | Pending | Missing relationship under existing PhysX source. Do not create a second PhysX source. |
| ovrtx / ovstage / ovstorage / ovstream / ovui | GitHub repos listed below | Not in section 10 | Pending | Missing sources. Keep as separate tool nodes under the portal tree. |
| SimReady Foundation | https://github.com/nvidia/simready-foundation | Not in section 10 | Pending | Missing source. Keep distinct from OpenUSD. |
| USD tool repos | GitHub repos listed below | OpenUSD source exists; tool repos do not | Pending | Missing relationships under OpenUSD / new tool sources. Do not duplicate OpenUSD. |
| Blueprints | build.nvidia.com / docs URLs below | Not in section 10 | Pending | Missing sources. Smart Cities **blueprint** ≠ Smart Cities **landing page** (PR #7). |
| Docs | https://docs.omniverse.nvidia.com/ | Not a named section-10 source | Pending | Missing source (docs hub). |
| GitHub org | https://github.com/NVIDIA-Omniverse | Not a named section-10 source | Pending | Missing source (org hub). |
| Community | https://developer.nvidia.com/omniverse/community | Not in section 10 | Pending | Missing source. |
| Physical AI learning path | https://docs.nvidia.com/learning/physical-ai/ | Not in section 10 | Pending | Missing source. |
| Omniverse Labs | https://nvidia-omniverse.github.io/omniverse-labs/ | Not in section 10 | Pending | Missing source. |
| Omniverse commercial page | https://www.nvidia.com/en-us/omniverse/ | Existing named source (`NVIDIA Omniverse official page`) | Partial | Keep distinct from this developer portal. |

## First-level sections captured from the root page

### 1. Quick links / docs and community

| Node | URL | Read status |
| --- | --- | --- |
| Learning Library (on-page) | https://developer.nvidia.com/omniverse#library | Partial (catalog JSON retrieved) |
| Choose a Library | https://developer.nvidia.com/omniverse#build-with-libraries | Partial (same page) |
| Use Agent Skills | https://developer.nvidia.com/omniverse#agents-skills | Partial (same page) |
| Start With a Blueprint | https://developer.nvidia.com/omniverse#blueprints | Partial (same page) |
| Follow a Learning Path | https://docs.nvidia.com/learning/physical-ai/ | Pending |
| GitHub | https://github.com/NVIDIA-Omniverse | Pending |
| Docs | https://docs.omniverse.nvidia.com/ | Pending |
| Community | https://developer.nvidia.com/omniverse/community | Pending |
| Omniverse Labs | https://nvidia-omniverse.github.io/omniverse-labs/ | Pending |

### 2. Omniverse AI Agent Skills

Skill catalog: https://github.com/NVIDIA/skills (Pending). Root-page cards (destinations unread):

| Skill | URL | Best-for (vendor card; WORKING) |
| --- | --- | --- |
| CAD to SimReady | https://github.com/NVIDIA/skills/tree/main/skills/omniverse-cad-to-simready | CAD/source assets → reviewable USD |
| Defect Image Generation | https://github.com/NVIDIA/skills/tree/main/skills/physical-ai-defect-image-generation | AOI inspection data |
| Neural Reconstruction | https://github.com/NVIDIA/skills/tree/main/skills/physical-ai-neural-reconstruction | camera/lidar/radar/stereo reconstruction for AV/robotics |
| Realtime Viewer | https://github.com/NVIDIA/skills/tree/main/skills/omniverse-realtime-viewer | OpenUSD viewers without modifying source USD |
| Video Data Augmentation | https://github.com/NVIDIA/skills/tree/main/skills/physical-ai-video-data-augmentation | enrich/label video datasets |
| USD Performance Tuning | https://github.com/NVIDIA/skills/tree/main/skills/omniverse-usd-performance-tuning | large USD scene performance |

Neural Reconstruction is related to NuRec and to unmerged PR #7 AV Simulation / YouTube nodes. Keep those **separate**.

### 3. Omniverse Tools for Agents

| Tool | Published Get Started URL | Read status | Notes |
| --- | --- | --- | --- |
| ovphysx | https://github.com/NVIDIA-Omniverse/PhysX/tree/main/ovphysx | Pending | USD-native physics library card; sits under existing PhysX source, not a second PhysX. |
| ovrtx | https://github.com/nvidia-omniverse/ovrtx | Pending | RTX rendering / sensor simulation. Related to RTX working notes; not a duplicate of PhysX. |
| ovstage | http://github.com/nvidia-omniverse/ovstage | Pending | Published as `http://`. HTTPS candidate unverified this pass. |
| ovstorage | https://github.com/NVIDIA-Omniverse/ovstorage | Pending | Cloud-native OpenUSD asset APIs. |
| ovstream | https://github.com/nvidia-omniverse/ovstream | Pending | GPU data streaming. |
| ovui | http://github.com/NVIDIA-omniverse/ovui | Pending | Published as `http://`. HTTPS candidate unverified this pass. |
| SimReady Foundation | https://github.com/nvidia/simready-foundation | Pending | Framework/pipeline for simulation-ready assets. |
| simready-validate | https://github.com/NVIDIA/simready-foundation | Pending | Same repo as SimReady Foundation on the live page. Do not split into two sources until compared. |
| usd-agents | https://github.com/NVIDIA-Omniverse/content-agents | Pending | |
| usd-search | https://github.com/NVIDIA-Omniverse/usd-search | Pending | |
| usd-convert-asset | https://github.com/NVIDIA-Omniverse/usd-convert-asset | Pending | |
| usd-convert-gsplat | https://github.com/NVIDIA-Omniverse/usd-convert-gsplat | Pending | Keep distinct from NuRec. |
| mujoco-usd-converter | https://github.com/newton-physics/mujoco-usd-converter | Pending | Newton-adjacent converter; not a PhysX alias. |
| urdf-usd-converter | https://github.com/newton-physics/urdf-usd-converter | Pending | Newton-adjacent converter. |
| usd-exchange | https://github.com/NVIDIA-Omniverse/usd-exchange | Pending | |
| usd-optimize | https://github.com/NVIDIA-Omniverse/usd-optimize | Pending | |
| usd-validation-nvidia | https://github.com/NVIDIA-Omniverse/usd-validation-nvidia | Pending | |
| OpenUSD | https://developer.nvidia.com/openusd | Partial | Existing source. |

### 4. Simulation Libraries for Physical AI

| Library | Published URL | Inventory | Read status |
| --- | --- | --- | --- |
| Newton Physics | https://developer.nvidia.com/newton-physics | missing standalone source; PhysX page already names Newton as a distinct engine | Pending |
| NuRec | https://docs.nvidia.com/nurec/index.html | missing source; Hugging Face dataset named on the card is not retrieved | Pending |
| PhysX | https://github.com/NVIDIA-Omniverse/PhysX | existing source + ARCH-0005 | Partial |
| PhysicsNeMo | https://developer.nvidia.com/physicsnemo | missing source | Pending |
| NVIDIA Warp | https://developer.nvidia.com/newton-physics | **same URL as Newton on the live page** | Pending |
| Omniverse Labs | https://nvidia-omniverse.github.io/omniverse-labs/ | missing source | Pending |

Keep PhysX ≠ Newton ≠ Warp ≠ PhysicsNeMo ≠ NuRec.

### 5. Blueprints and agent workflows

| Blueprint | Published URL | Read status | Keep distinct from |
| --- | --- | --- | --- |
| DSX Gigawatt-Scale AI Factories | https://build.nvidia.com/nvidia/omniverse-dsx-blueprint-for-ai-factories | Pending | |
| GR00T-Mimic Synthetic Robot Manipulation | https://build.nvidia.com/nvidia/isaac-gr00t-synthetic-manipulation | Pending | Isaac Sim/Lab sources |
| Mega Multi-Robot Industrial Fleets | https://build.nvidia.com/nvidia/mega-multi-robot-fleets-for-industrial-automation | Pending | |
| Agent Skills for Synthetic Data Generation | https://brev.nvidia.com/physical-ai | Pending | Agent Skills catalog; Synthetic Data glossary |
| Digital Twin for Interactive Fluid Simulation | root-page hash only (`#`); learning JSON candidate https://build.nvidia.com/nvidia/digital-twins-for-fluid-simulation | Pending | Do not silently replace the hash with the JSON URL as canonical |
| Digital Twins for Smart Cities | https://docs.nvidia.com/vss/3.1.0/smartcity-docs/smartcity-toc.html | Pending | Unmerged PR #7 Smart Cities **landing page** `https://www.nvidia.com/en-us/industries/smart-cities-and-spaces/` |

### 6. Learning Resources

The root page exposes a filterable library (page text: 57 results). Catalog JSON retrieved from https://developer.nvidia.com/search-data/omniverse.json. Item titles and URLs are stored in the companion JSON for later auto-retrieval.

**None of the 57 items is marked learned/read.** Catalog listing ≠ content retrieval.

Featured cards visible on the root this pass (still Pending as documents):

- Build and Orchestrate End-to-End SDG Workflows with NVIDIA Isaac Sim and NVIDIA OSMO
- Synthetic Manipulation Motion Generation for Robotics
- Developers Build Fast and Reliable Robot Simulations with NVIDIA Omniverse Libraries
- Research Advances in AI-Assisted Material Generation for Physical AI
- Neural Reconstruction for Robotics and Autonomous Vehicles
- Test Multi-Robot Fleets for Industrial Automation
- How to Instantly Render Real-World Scenes in Interactive Simulation

## Structural links (do not collapse)

```text
Physical world / planned system
→ sensed or authored data
→ Digital Twin / OpenUSD scene (usd-* tools, SimReady, OpenUSD)
→ physics simulation (PhysX / ovphysx; Newton relation; Warp/PhysicsNeMo pending)
→ sensor simulation / synthetic data (ovrtx, NuRec, Agent Skills, blueprints)
→ world model / policy learning (Isaac Lab existing source; GR00T blueprint pending)
→ validation (simready-validate, usd-validation-nvidia)
→ review / deployment
```

Named architecture IDs (files still not extracted on `main`; `APPROVAL REQUIRED` to materialize ARCH records):

- ARCH-0001 Physical AI official definition — portal is a vendor product mapping hub, not that definition
- ARCH-0003 Omniverse / OpenUSD / PhysX / Isaac Sim / Isaac Lab product mapping — this tree **expands** that mapping; it does not replace it
- ARCH-0004 NVIDIA Physical AI reference stack — working workflow; this tree is evidence of current vendor library layout
- ARCH-0005 PhysX SDK — existing physics node; ovphysx is a relationship under it

Unmerged sibling research (PR #7) remains separate:

- PhysX directory summary
- Autonomous Vehicle Simulation landing page
- Smart Cities and Spaces landing page
- YouTube `XeHtw36h-eI` source stub (not learned)

## Open defects / review items

Do not silently resolve:

1. **Warp Learn More URL** currently equals the Newton URL. Treat as a possible page defect or alias. Do not merge Warp into Newton.
2. **Fluid Simulation blueprint** on the portal is a same-page hash; the learning JSON has a different candidate URL.
3. **simready-validate** and **SimReady Foundation** share a GitHub repo on the live page.
4. **ovstage** / **ovui** published as `http://` GitHub links.
5. Whether ov* libraries, Agent Skills, Newton, NuRec, PhysicsNeMo, Warp, or blueprints need dedicated ARCH nodes remains `APPROVAL REQUIRED`.
6. Airtable `SRC-*` binding is unverified. GitHub/Airtable count mismatch (`ISSUE-GH-001` on unmerged PR #2) is unchanged.
7. Dedicated ARCH-0001–ARCH-0005 files are still absent on `main` (`ISSUE-GH-002` / `APPROVAL REQUIRED`).

## What this batch does not do

- No Airtable write.
- No new Interaction ID.
- No new `SRC-*` IDs.
- No claim that the root page is fully learned.
- No promotion of NVIDIA portal wording to an industry-wide definition.
- No silent merge of Newton/Warp/PhysX, NuRec/AV Simulation, or Smart Cities blueprint/landing page.
- ISSUE-0001–ISSUE-0010 unchanged.
