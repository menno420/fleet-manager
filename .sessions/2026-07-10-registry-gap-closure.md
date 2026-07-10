# 2026-07-10 — prompt-registry gap closure (v-stamps · one-writer · trigger snapshot)

> **Status:** `complete`

📊 Model: fable family (gap-closure worker, coordinator-dispatched) · start 2026-07-10T22:00Z · end 2026-07-10T22:10Z (`date -u`)

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

- **GAP 1** — all 39 prompt-bearing files stamped: file-header HTML comment + in-paste
  plain-text `v1 · 2026-07-10 · <seat> <part>` line (failsafe files header-only by design —
  in-band stamps would break byte-matching against the stored trigger text). Governing
  rules shipped as projects/README.md Doctrine items 2 (ONE WRITER + INTAKE) and 3
  (VERSION-STAMP + EDIT-REGISTRY-FIRST + quote-the-header drift detection).
- **GAP 3** — full `list_triggers` sweep (114 triggers, 2 pages). Byte-verdicts:
  Builder + idea-engine EXACT; sim-lab content-match (wrap-only) and ARMED seat-side
  20:54Z (OA-003 closed — file + matrix + paste-wave updated); fm MISMATCH (deployed is
  the richer manager text, 497 chars — verbatim committed); product-forge MISMATCH
  (deployed = generic §2b template, not the canonical long form — verbatim committed);
  trading cutover CONFIRMED (new `trig_01YBaVeKAW…` @ `0 */2`, shortened prompt verbatim
  committed, old id gone); substrate-kit [RECONSTRUCTED] resolved verbatim; websites
  v1-era prompt CONFIRMED deployed (v2 re-paste still owed — paste-wave updated).
  Snapshot: `projects/_inventory/trigger-registry-2026-07-10.md`.
- **GAP 4** — superbot PR #1967 (docs-only, auto-merge armed per Q-0127): superseded
  banners on the 5 founding packages + runbook §2 manager package.
- Heartbeat carries the explicit PROMPT-REGISTRY location line.
- ⚑ Self-initiated: matrix/paste-wave deployed-state fixes (drift visible in the same
  registry read — fix-on-sight); worktree isolation after a mid-flight branch switch by a
  parallel worker in the shared checkout (process note for the coordinator: shared-checkout
  workers should always work from `git worktree` copies).

## Session enders

- 💡 **Session idea:** add a manager-runnable **registry drift checker**
  (`tools/check_prompt_registry.py`): re-run `list_triggers`, byte-compare every enabled
  fleet-seat stored prompt against the seat's `failsafe-prompt.md` deployed-state block and
  the `_inventory/` snapshot, and fail loud on any new mismatch — turning this pass's
  one-off byte-verification into a repeatable sweep step (enforce, don't exhort; the
  registry read is cheap and the mismatch class is now proven real: 4 of 8 wakes had
  drifted from their committed claims).
- ⟲ **Previous-session review:** the package-centralization assembly (PR #39) landed an
  impressively complete 18-dir registry in one pass, and its honesty notes ([RECONSTRUCTED],
  "text-equality unverified") are exactly what made this gap-closure mechanical — but it
  stopped one step short of running `list_triggers` itself, leaving 4 verifiable claims
  unverified for a follow-up PR. **Workflow improvement:** when a registry claim is
  checkable by a single tool call available in-session, verify it in the same PR that
  commits the claim — an honesty note should be the fallback, not the default.
