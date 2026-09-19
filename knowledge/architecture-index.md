# Architecture Reference Index

Status: WORKING index of architecture nodes already named in `knowledge/chat-sync-2026-09-15.md`. Dedicated per-node files are not present in this repository yet.

This is an index, not a new canonical architecture. No verification status is changed. Extracting full Architecture Reference records into standalone files would change canonical architecture presentation and requires owner approval under `knowledge/cursor-approval-protocol.md`.

## Required category separation

Keep these distinct:

| Category | Meaning | Must not be treated as |
| --- | --- | --- |
| Official Definition | A named party’s own definition | a universal industry definition |
| Vendor Product Mapping | How a vendor maps products/tools onto a concept | the technology itself |
| Vendor Standard / Implementation Framework | A vendor’s implementation stack or recommended workflow | a formal cross-vendor standard |

## Nodes named in the chat snapshot

| ID | Title | Category in snapshot | GitHub file status |
| --- | --- | --- | --- |
| ARCH-0001 | Physical AI official definition | Official Definition | named in chat-sync only |
| ARCH-0002 | World Model / WFM official definition | Official Definition | named in chat-sync only |
| ARCH-0003 | Omniverse / OpenUSD / PhysX / Isaac Sim / Isaac Lab product mapping | Vendor Product Mapping | named in chat-sync only |
| ARCH-0004 | NVIDIA Physical AI reference stack | Vendor Standard / Implementation Framework | named in chat-sync only |
| ARCH-0005 | PhysX SDK as a core physics-based-simulation reference node | architecture node; snapshot places PhysX as a core physics-simulation reference | named in chat-sync only |

Current NVIDIA source pages that support these nodes, without promoting them to industry-wide definitions:

- ARCH-0001 — https://www.nvidia.com/en-us/glossary/generative-physical-ai/
- ARCH-0002 — https://www.nvidia.com/en-us/glossary/world-models/
- ARCH-0003 / ARCH-0005 — https://developer.nvidia.com/omniverse, https://developer.nvidia.com/openusd, https://developer.nvidia.com/physx-sdk, https://developer.nvidia.com/isaac/sim, https://developer.nvidia.com/isaac/lab
- ARCH-0004 — described in chat-sync as a working NVIDIA Physical AI reference workflow, not as a formal standard

The Omniverse Developer URL is a vendor **product-mapping hub** (entry node). Its first-level tree is `knowledge/omniverse-developer-portal-tree.md`. That tree expands ARCH-0003 evidence; it is not a new Architecture Reference and does not extract ARCH-0001–ARCH-0005 files. ovphysx is a missing relationship under existing ARCH-0005/PhysX, not a second PhysX source.

## INT-0001 reminder

PhysX already exists as a source. ARCH-0005 exists because the NVIDIA Physical AI glossary points from physics-based simulations to the PhysX SDK. The correct GitHub-side action for a missing node is an Architecture Reference, not a duplicate Source.

## Missing-file finding

Classification: existing source/snapshot content, missing dedicated architecture-reference files.

Tracked as `ISSUE-GH-002`. Do not silently materialize full ARCH records in this batch.
