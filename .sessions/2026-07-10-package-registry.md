# 2026-07-10 — package-centralization assembly (projects/ registry)

> **Status:** `in-progress`

📊 Model: fable family (assembly worker, coordinator-dispatched) · start 2026-07-10T21:30Z (`date -u`)

## Declared at open (born-red)

Assembly worker for the coordinator's package-centralization dispatch (Phase C
— the deliverable). About to land, in this PR:

1. **`projects/<name>/`** — every package dir from the three-builder sweep
   committed verbatim (13 full seat packages: fleet-manager · substrate-kit ·
   superbot-next · idea-engine · product-forge · sim-lab · websites ·
   trading-strategy · venture-lab · superbot-games · pokemon-mod-lab ·
   gba-homebrew · superbot; 5 archive/pre-birth metas: codetool-lab-fable5 /
   -opus4.8 / -sonnet5 · mobile-lab · games-program). Content is
   builder-verified; assembler spot-fixes mechanical issues only.
2. **`projects/README.md`** — the registry index: what this is (source of
   truth for per-Project console pastes; regenerate-don't-fork), the
   per-Project MATRIX (seat status · cadence · per-part deployed-state · key
   flag), the paste-wave section (which packages need owner pastes NOW vs
   ride a seat's own boot), provenance.
3. **`docs/owner-queue.md`** — ONE consolidated "Project package paste wave"
   active item (click-level subitems: kit §2b + OA8 · forge §2b · sim-lab
   failsafe arm via Routines screen · websites v2 re-paste + optional cadence
   retune · trading re-paste · superbot optional); FIX the Parked mislabel
   (opus4.8's releases are LIVE — the un-released tags are fable5/envdrift's);
   ADD the trading-strategy PR #37 owner merge click.
4. **`control/status.md`** — heartbeat as last content step (package-
   centralization record + notable builder findings).
5. **This card**, flipped `complete` as the deliberate last commit.

Landing: born-red card holds the gate red; work commits next; gate run
(`python3 bootstrap.py check --strict`) before the flip; flip last; REST
squash-merge on the branch's substrate-gate run going green. Sequencing note:
PR #38 (chain slice: roster v1 + model matrix) is open in parallel — this
branch update-branches/rebases over it before merging if it lands first.
