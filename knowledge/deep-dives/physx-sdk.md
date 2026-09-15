# PhysX SDK — directory summary

GitHub node: `GH-DD-PHYSX`
Source URL: https://developer.nvidia.com/physx-sdk
HTTP check 2026-09-15: reachable
Status: WORKING directory summary of an **already represented** source/architecture node
Learned/read: YES for the official product page and the ChatGPT-side structural representation already in `knowledge/chat-sync-2026-09-15.md`. This file does **not** create a duplicate source.

Category: Vendor Product Mapping source that supports ARCH-0005. Not an industry-wide physics-engine standard.

## Why this is not a new source

INT-0001 already recorded that PhysX existed as a source; the earlier gap was architectural prominence (ARCH-0005), not a missing URL. ChatGPT-side retrieval for this continuation confirmed PhysX has already been deeply researched and structurally represented, including:

- Omniverse primary physics engine relationship
- Isaac Sim / Isaac Lab relationship
- Newton relation marker (distinct engine, not a PhysX alias)

## Live-page facts retrieved 2026-09-15

From https://developer.nvidia.com/physx-sdk (vendor page; WORKING, not promoted to VERIFIED industry definition):

- NVIDIA PhysX is described as an open-source multi-physics SDK for scalable simulation, including robotics and autonomous-vehicle applications.
- The page states PhysX is the **primary physics engine of NVIDIA Omniverse**, a platform of APIs/SDKs for 3D and industrial digitalization workflows based on OpenUSD.
- NVIDIA Isaac Sim and Isaac Lab are described as robotics reference applications built on Omniverse.
- Related official links on the same page:
  - Omniverse: https://developer.nvidia.com/omniverse
  - GitHub source: https://github.com/NVIDIA-Omniverse/PhysX
  - Omniverse physics documentation: https://docs.omniverse.nvidia.com/extensions/latest/ext_physics.html#overview
- Feature groups named on the page include rigid body dynamics, scene queries, joints, reduced-coordinate articulations, vehicle dynamics, character controllers, FEM soft bodies, SDF colliders, position-based dynamics, custom geometry, Blast fracture/destruction, and Flow smoke/fire.
- The page also names a GPU API path supporting end-to-end reinforcement learning via Isaac Lab.

## Newton relation marker (keep distinct)

The same PhysX page includes a separate block for **Newton**, described there as a next-generation open-source, GPU-accelerated physics engine, co-developed by Google DeepMind and Disney Research, managed by the Linux Foundation, built on NVIDIA Warp and OpenUSD, and compatible with learning frameworks such as MuJoCo Playground or Isaac Lab. Starter link named on the page: https://developer.nvidia.com/newton-physics

Do not merge Newton into the PhysX source node. Do not treat the marketing adjacency as proof that PhysX has been replaced.

## Structural links

- ARCH-0003 — Omniverse / OpenUSD / PhysX / Isaac Sim / Isaac Lab product mapping
- ARCH-0005 — PhysX SDK as a core physics-based-simulation reference node
- ARCH-0001 / ARCH-0004 — Physical AI definition and vendor reference stack (PhysX is a physics-simulation component, not the whole stack)
- Sibling research nodes: [autonomous-vehicle-simulation.md](autonomous-vehicle-simulation.md), [smart-cities-and-spaces.md](smart-cities-and-spaces.md)
- Hub: [omniverse-research-index.md](../omniverse-research-index.md)

PhysX Vehicle Dynamics on this SDK page is a physics feature. It is **not** the same node as the Autonomous Vehicle Simulation landing page.

## What remains open

- Dedicated ARCH-0005 file is still not present on `main` (`APPROVAL REQUIRED` to extract full Architecture Reference files).
- Airtable `SRC-*` binding for this URL is unverified.
- Feature-level deep dives (FEM, PBD, Flow, Blast, GPU API) are named, not expanded in this file.
