<!-- v2 · 2026-07-12 · fleet-manager projects registry -->
# Game Lab — Project package meta

> **Status:** `standing seat — v2 restamp 2026-07-12` (v1: owner fleet
> restructure 2026-07-11, slice 1). The sibling package files
> (`instructions.md` / `coordinator-prompt.md` / `failsafe-prompt.md`) are
> GENERATED COPIES serving **prompts v3.3** (generated from `docs/prompts/v3`
> @ `48650f8`; v3.3 generation on main @ `98d0f68`) — the slice-1/slice-2 v1
> bodies this meta previously described are superseded. Deployment + trigger
> cutover still ride the owner sitting (owner-queue C#34–C#36: rename / paste
> / cutover; rebind-then-delete recipe in `failsafe-prompt.md`).

- **Seat:** Game Lab (standing Project).
- **Writable repos:** menno420/gba-homebrew (Track B, PUBLIC) + menno420/pokemon-mod-lab (Track A, PRIVATE).
- **Folds (sources):** gba-homebrew (v2) + pokemon-mod-lab (v2) — full prior packages live in git history:
  `projects/gba-homebrew/` · `projects/pokemon-mod-lab/` (last full state @ `1dea86d`).
- **Seat notes:** Standalone — NO SuperBot connection. Strict public/private track isolation is the seat's hard rail. The retired superbot-retro seat's armed triggers (failsafe trig_01Y99uDKNtKTz2EtRYPWZkGY + hourly child wakes trig_0137SkvhXEJvwepX8aVNkcSn / trig_01BTJjkMVMKtWPjuYe7643Hi — last committed registry state) drove these repos: the rebind-then-delete cutover recipe is in this package's `failsafe-prompt.md` v1 (slice 2) and executes at the merged seat's boot.
- **Deployed state (as of 2026-07-12 — verify at HEAD):** Custom-Instructions
  paste unreceipted (owner-queue C#34–C#36 open at this repo's HEAD). No
  failsafe named for this seat in the committed registry snapshot
  (`telemetry/triggers-snapshot.json`, exported 2026-07-12); the retired
  superbot-retro triggers named in the caution above are likewise absent from
  that snapshot. Trigger cutover rides C#36.
