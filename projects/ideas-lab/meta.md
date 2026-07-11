<!-- v1 · 2026-07-11 · fleet-manager projects registry -->
# Ideas Lab — Project package meta

> **Status:** `new seat — v1, owner fleet restructure 2026-07-11 (slice 1)`.
> Created by the restructure to the 8 standing Projects. Nothing of this
> package is deployed yet: `instructions.md` v1 is authored (never pasted);
> `coordinator-prompt.md` / `failsafe-prompt.md` carry REAL v1 bodies since
> slice 2 (prompt re-sync, 2026-07-11) — never pasted/armed; deployment +
> trigger cutover ride the merged seat's boot (rebind-then-delete recipe in
> `failsafe-prompt.md`).

- **Seat:** Ideas Lab (standing Project).
- **Writable repos:** menno420/idea-engine (generate) + menno420/sim-lab (verify).
- **Folds (sources):** idea-engine (v2) + sim-lab (v2) — full prior packages live in git history:
  `projects/idea-engine/` · `projects/sim-lab/` (last full state @ `1dea86d`).
- **Seat notes:** The generate→verify loop is INTERNAL to this seat — the old outbox→intake cross-project wait and the even/odd cadence pairing are retired. Old seats' armed failsafes (idea-engine trig_0178q9Je2xRFJgthwamrg9Br, sim-lab trig_01SHfnLv6EqZesr4tC3T9kUU — last committed registry state) still target the OLD seats: the rebind-then-delete cutover recipe is in this package's `failsafe-prompt.md` v1 (slice 2) and executes at the merged seat's boot.
- **Deployed state:** instructions never pasted; prompts authored (v1,
  slice 2) but never pasted; no trigger armed FOR THIS SEAT yet (boot/slice 3).
