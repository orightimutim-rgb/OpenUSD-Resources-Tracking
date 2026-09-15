# Autonomous Vehicle Simulation — directory summary

GitHub node: `GH-DD-AV-SIM`
Source URL: https://www.nvidia.com/en-us/solutions/autonomous-vehicles/simulation/
HTTP check 2026-09-15: reachable
Status: WORKING incomplete standalone directory summary. **Not** previously represented as a complete deep dive in the mirrored knowledge state.
Learned/read: PARTIAL. Official landing-page body was retrieved on 2026-09-15. This is not a complete research deep dive and is not VERIFIED as an industry standard.

Category: Vendor Product Mapping / vendor solution page. Related to Physical AI, world models, synthetic data, and simulation-validation. Not an Official Definition of “simulation,” and not a cross-vendor AV-validation standard.

## Why this is a new GitHub-side node

`knowledge/chat-sync-2026-09-15.md` already lists NVIDIA PhysX SDK, Omniverse, Isaac Sim/Lab, and Physical AI/World Model glossary pages. It did **not** list this Autonomous Vehicle Simulation landing page as its own source or directory-summary. Creating a relationship from PhysX or Omniverse is not enough; this page is a separate application-domain node.

Do not duplicate:

- PhysX SDK (physics engine)
- Isaac Sim (robotics simulation product)
- YouTube `XeHtw36h-eI` (unverified clip about Omniverse Cloud APIs / sensor simulation)

## Live-page facts retrieved 2026-09-15

Page title: “Simulation for Robotaxis and Autonomous Vehicles”.
H1: “Simulation and Validation for Robotaxis and Autonomous Vehicles”.

Vendor wording on the page (WORKING; do not promote to industry-wide definition):

- NVIDIA presents an “open simulation foundation” that combines reasoning models, 3D neural reconstruction, world foundation models (WFMs), high-fidelity sensor simulation, and closed-loop evaluation.
- Stated purpose: expand scenario coverage, strengthen safety validation, and advance robotaxi / AV development. Physical test drives are described as unable to cover every edge case.
- Named vendor tools on this page (product mapping, not new ARCH IDs):
  - NVIDIA Alpamayo — open VLA models, simulation frameworks, and datasets; closed-loop evaluation with AlpaSim; AlpaGym named for closed-loop RL
  - NVIDIA Omniverse NuRec — 3D Gaussian-based neural reconstruction from real-world / recorded sensor data
  - NVIDIA Cosmos — world foundation models for scenario generation, including Cosmos Transfer and Cosmos-Dreams as named on the page
- Use-case headings retrieved: Neural Reconstruction, World Generation, Scenario Variation, Closed-Loop Simulation.

## Structural links

Working pipeline placement: sensor simulation / synthetic data / validation — downstream of Digital Twin / OpenUSD scene representation and alongside, not identical to, PhysX physics simulation.

| Link target | Relationship |
| --- | --- |
| ARCH-0001 Physical AI | vendor application of Physical AI to AV development |
| ARCH-0002 World Model / WFM | Cosmos WFMs named on this page; keep definition vs product mapping separate |
| ARCH-0003 / ARCH-0004 | Omniverse / simulation-validation vendor mapping and reference stack |
| [physx-sdk.md](physx-sdk.md) | related physics backend; not a duplicate of this AV landing page |
| [smart-cities-and-spaces.md](smart-cities-and-spaces.md) | sibling domain page; also uses Omniverse / Cosmos / digital twins |
| [youtube-xehtw36h-ei.md](youtube-xehtw36h-ei.md) | related sensor-simulation illustration; not a substitute for this source |
| Hub | [omniverse-research-index.md](../omniverse-research-index.md) |

## Completeness gap

This file is a heading-and-body directory summary of one marketing/solution page. It is **not** yet a complete standalone deep dive of the AV simulation stack (NuRec APIs, Alpamayo models, Cosmos post-training, closed-loop metrics, safety claims). Sub-product pages were not retrieved in this pass.

Review candidate (`APPROVAL REQUIRED` before creating new ARCH IDs): whether Alpamayo, NuRec, and Cosmos need their own Architecture Reference nodes versus remaining product-mapping bullets under ARCH-0003/0004.
