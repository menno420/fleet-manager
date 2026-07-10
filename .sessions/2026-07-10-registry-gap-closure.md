# 2026-07-10 — prompt-registry gap closure (v-stamps · one-writer · trigger snapshot)

> **Status:** `in-progress`

📊 Model: fable family (gap-closure worker, coordinator-dispatched) · start 2026-07-10T22:05Z (`date -u`)

## Declared at open (born-red)

Gap-closure worker for the prompt-registry ingest dispatch — verification of the
projects/ registry (PR #39 @ 3d105d9) against the original dispatch found four
gaps; this PR closes the three fleet-manager-side ones (the fourth is a
docs-only superbot PR landing in parallel):

1. **GAP 1 — version-stamp headers**: every prompt-bearing registry file
   (`projects/*/instructions.md`, `coordinator-prompt.md`, `failsafe-prompt.md`
   — 39 files) gets a first-line `<!-- v1 · 2026-07-10 · fleet-manager projects
   registry -->` header, plus a plain-text `v1 · 2026-07-10 · <seat> <part>`
   first line INSIDE each console-pasted block (so the stamp survives the paste
   and a seat can be asked to QUOTE it for drift detection). Governing rule
   added to `projects/README.md`.
2. **GAP 2 — one-writer + intake rule** in `projects/README.md`: manager is the
   registry's sole writer; lanes propose via heartbeat ⚑ flags / INTAKE notes.
3. **GAP 3 — verbatim trigger-prompt extraction**: full `list_triggers` sweep
   (113 triggers, both pages) → reconcile every enabled fleet-seat trigger's
   STORED prompt against the registry's claims; replace substrate-kit's
   [RECONSTRUCTED] text with the verbatim stored prompt; fix the
   fm/product-forge/trading/websites/sim-lab deployed-state mismatches with
   provenance; commit the fleet's first full trigger snapshot at
   `projects/_inventory/trigger-registry-2026-07-10.md`.
4. **Heartbeat**: explicit PROMPT-REGISTRY location line in `control/status.md`.

Landing: born-red card holds the gate red; content commits next; gate run
before the flip; flip last; REST squash on green substrate-gate.

## Done (close-out)

_(pending — filled at flip)_
