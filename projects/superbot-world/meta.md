<!-- v2 · 2026-07-12 · fleet-manager projects registry -->
# SuperBot World — Project package meta

> **Status:** `standing seat — v2 restamp 2026-07-12` (v1: owner fleet
> restructure 2026-07-11, slice 1). The sibling package files
> (`instructions.md` / `coordinator-prompt.md` / `failsafe-prompt.md`) are
> GENERATED COPIES serving **prompts v3.3** (generated from `docs/prompts/v3`
> @ `48650f8`; v3.3 generation on main @ `98d0f68`) — the slice-1/slice-2 v1
> bodies this meta previously described are superseded. Custom-Instructions
> deployment still rides the owner sitting (owner-queue C#34–C#36).

- **Seat:** SuperBot World (standing Project).
- **Writable repos:** menno420/superbot-mineverse (FLAGSHIP) + menno420/superbot-games + menno420/superbot-idle.
- **Folds (sources):** superbot-games (v3) + superbot-idle (v2) + superbot-mineverse (v2) — full prior packages live in git history:
  `projects/superbot-games/` · `projects/superbot-idle/` · `projects/superbot-mineverse/` (last full state @ `1dea86d`).
- **Seat notes:** Flagship = mineverse; the OAuth login-CSRF fix lands BEFORE any secrets work. Old seats' armed failsafe triggers (games trig_019ZgWyL78Rx1sr6LhvL8NE3, idle trig_01TWKGFW8RUsMvxUMt2ndzqA, mineverse trig_01K8xmAKYS5S2HLy1HPANM7j — last committed registry state) still target the OLD seats: the rebind-then-delete cutover recipe is in this package's `failsafe-prompt.md` v1 (slice 2) and executes at the merged seat's boot.
- **Deployed state (as of 2026-07-12 — verify at HEAD):** Custom-Instructions
  paste unreceipted (owner-queue C#34–C#36 open at this repo's HEAD). Seat
  failsafe ARMED: `trig_01KQbKNiSVfZRWutKEWFx2q2` "SuperBot World failsafe
  wake", cron `0 */2 * * *`, enabled, created 2026-07-11T23:12:36Z
  (`telemetry/triggers-snapshot.json`, exported 2026-07-12). The old games /
  idle / mineverse failsafes named in the caution above are absent from that
  snapshot.
