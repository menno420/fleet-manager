<!-- v2 · 2026-07-12 · fleet-manager projects registry -->
# Ideas Lab — Project package meta

> **Status:** `standing seat — v2 restamp 2026-07-12` (v1: owner fleet
> restructure 2026-07-11, slice 1). The sibling package files
> (`instructions.md` / `coordinator-prompt.md` / `failsafe-prompt.md`) are
> GENERATED COPIES serving **prompts v3.3** (generated from `docs/prompts/v3`
> @ `48650f8`; v3.3 generation on main @ `98d0f68`) — the slice-1/slice-2 v1
> bodies this meta previously described are superseded. Custom-Instructions
> deployment still rides the owner sitting (owner-queue C#34–C#36).

- **Seat:** Ideas Lab (standing Project).
- **Writable repos:** menno420/idea-engine (generate) + menno420/sim-lab (verify).
- **Folds (sources):** idea-engine (v2) + sim-lab (v2) — full prior packages live in git history:
  `projects/idea-engine/` · `projects/sim-lab/` (last full state @ `1dea86d`).
- **Seat notes:** The generate→verify loop is INTERNAL to this seat — the old outbox→intake cross-project wait and the even/odd cadence pairing are retired. Old seats' armed failsafes (idea-engine trig_0178q9Je2xRFJgthwamrg9Br, sim-lab trig_01SHfnLv6EqZesr4tC3T9kUU — last committed registry state) still target the OLD seats: the rebind-then-delete cutover recipe is in this package's `failsafe-prompt.md` v1 (slice 2) and executes at the merged seat's boot.
- **Deployed state (as of 2026-07-12 — verify at HEAD):** Custom-Instructions
  paste unreceipted (owner-queue C#34–C#36 open at this repo's HEAD). Seat
  failsafe ARMED: `trig_01T83UuVthszGBcENYwrTrm7` "Ideas Lab failsafe wake",
  cron `0 */2 * * *`, enabled, created 2026-07-11T23:55:17Z
  (`telemetry/triggers-snapshot.json`, exported 2026-07-12). The old
  idea-engine / sim-lab failsafes named in the caution above are absent from
  that snapshot.
