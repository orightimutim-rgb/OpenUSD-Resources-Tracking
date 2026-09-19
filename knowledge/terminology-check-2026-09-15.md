# Terminology Consistency Check — 2026-09-15

Scope: cross-file wording for Simulator, Emulator, Digital Twin, HIL, Omniverse, OpenUSD, Physical AI, and PhysX.

Method: compare `knowledge/chat-sync-2026-09-15.md`, `knowledge/sync-policy.md`, `knowledge/interaction-learning.md`, `knowledge/architecture-index.md`, and `knowledge/source-index.md`. No claim verification status was changed.

| Term | Current GitHub treatment | Consistency finding |
| --- | --- | --- |
| Simulator | Working interpretation: modeled behavior / system state / physical rules. Snapshot warns that “surface behavior” is too broad as a universal definition. | Consistent. ISSUE-0002 and ISSUE-0003 remain open. |
| Emulator | Working interpretation: compatibility with another execution environment. Kept distinct from HIL and from game-console SDK/devkit/hardware setups. | Consistent. ISSUE-0007 and ISSUE-0010 remain open. |
| Digital Twin | Broader mapping layer; NVIDIA glossary is a vendor official definition source, not an industry-wide definition. | Consistent. Not collapsed into simulator or HIL. |
| HIL | Separate from emulation. Working model lists simulated plant, real/representative controller, interface, real-time closed loop. | Consistent. MIL/SIL/PIL/HIL still marked as needing separate verification. |
| Omniverse | Vendor product / library platform in ARCH-0003. | Consistent. Not treated as OpenUSD itself. |
| OpenUSD | Common scene/data framework; NVIDIA developer page is vendor mapping, not the OpenUSD standard body. | Consistent. Official openusd.org is noted as related but was not in the original 16-name snapshot, so it is not added as a canonical SRC. |
| Physical AI | NVIDIA official definition (ARCH-0001). Vendor definition ≠ industry-wide definition. | Consistent. Glossary URL now redirects to generative-physical-ai. |
| PhysX | Source page plus ARCH-0005 architecture node. Not duplicated as a second source. | Consistent with INT-0001. |

No terminology rewrite was applied. Conflicts already recorded in ISSUE-0002 and ISSUE-0003 were left unresolved.
