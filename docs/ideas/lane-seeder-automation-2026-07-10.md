---
state: captured
origin: lab
shipped_pr: null
shipped_repo: null
merged_date: null
outcome: open
---

# Lane-seeder automation — one dispatched run lands the full §1 seed state

> **Status:** `ideas`

**Idea:** build a "seed-lane" order pack or substrate-kit verb: given an
empty (or gen-1) repo + a lane mission text, one manager-dispatched run lands
the complete blueprint §1 seed state in one PR — conventions file generated
from the blueprint with the R21 landing path baked in, PLATFORM-LIMITS
pre-filled from the fleet-wide **union** of verbatim wall texts (fable5's
file format is the best template), archetype setup script, control/ files +
capability manifest, claims/ dir, born-red card template. Owner clicks
shrink to the blueprint §3 UI-only items (repo create, Project, environment,
routine).
**Why worth having:** 9 gen-1 lanes just committed wind-down packages and
each needs the full seed state, plus venture-lab, game-lab's two repos, and
every future lane. Tonight venture-lab was seeded by hand; doing this 10+
more times manually is exactly the rediscovery tax gen-2 exists to kill, and
each hand-seeding risks divergence — the corpus shows three codetool arms
independently wrote three different walls-doc formats for the same walls.
Agents can populate an empty owner-created repo via the Contents API
(playbook R13 proves the bootstrap path), so everything except the true UI
walls is automatable.
**Unblocks:** the entire gen-1→gen-2 relaunch wave at near-zero marginal
cost; guarantees every lane is born from the same tested seed instead of a
hand copy.
**Provenance:** Fable-5 fleet review finding F11 (verified: no seeding
automation exists in fleet-manager or substrate-kit ideas/backlogs; the
kit's adopt/render templates already cover part of the surface, so this is
an extension of existing machinery). Synthesis:
[`../findings/fable5-review-2026-07-09.md`](../findings/fable5-review-2026-07-09.md).
**Status:** captured (not approved). Kit-side counterpart belongs in
substrate-kit's backlog (kit-lab never writes consumer repos — KF-2).
