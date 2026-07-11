<!-- v1 · 2026-07-11 · fleet-manager projects registry -->
# Game Lab — Project package meta

> **Status:** `new seat — v1, owner fleet restructure 2026-07-11 (slice 1)`.
> Created by the restructure to the 8 standing Projects. Nothing of this
> package is deployed yet: `instructions.md` v1 is authored (never pasted);
> `coordinator-prompt.md` / `failsafe-prompt.md` carry REAL v1 bodies since
> slice 2 (prompt re-sync, 2026-07-11) — never pasted/armed; deployment +
> trigger cutover ride the merged seat's boot (rebind-then-delete recipe in
> `failsafe-prompt.md`).

- **Seat:** Game Lab (standing Project).
- **Writable repos:** menno420/gba-homebrew (Track B, PUBLIC) + menno420/pokemon-mod-lab (Track A, PRIVATE).
- **Folds (sources):** gba-homebrew (v2) + pokemon-mod-lab (v2) — full prior packages live in git history:
  `projects/gba-homebrew/` · `projects/pokemon-mod-lab/` (last full state @ `1dea86d`).
- **Seat notes:** Standalone — NO SuperBot connection. Strict public/private track isolation is the seat's hard rail. The retired superbot-retro seat's armed triggers (failsafe trig_01Y99uDKNtKTz2EtRYPWZkGY + hourly child wakes trig_0137SkvhXEJvwepX8aVNkcSn / trig_01BTJjkMVMKtWPjuYe7643Hi — last committed registry state) drove these repos: the rebind-then-delete cutover recipe is in this package's `failsafe-prompt.md` v1 (slice 2) and executes at the merged seat's boot.
- **Deployed state:** instructions never pasted; prompts authored (v1,
  slice 2) but never pasted; no trigger armed FOR THIS SEAT yet (boot/slice 3).
