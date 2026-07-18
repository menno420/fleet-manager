<!-- v3.7 · 2026-07-18 · fleet-manager projects registry -->
# SuperBot World — Project package meta

> **Status:** `new seat — v1, owner fleet restructure 2026-07-11 (slice 1)`.
> Created by the restructure to the 8 standing Projects. Nothing of this
> package is deployed yet: `instructions.md` v1 is authored (never pasted);
> `coordinator-prompt.md` / `failsafe-prompt.md` carry REAL v1 bodies since
> slice 2 (prompt re-sync, 2026-07-11) — never pasted/armed; deployment +
> trigger cutover ride the merged seat's boot (rebind-then-delete recipe in
> `failsafe-prompt.md`).

- **Seat:** SuperBot World (standing Project).
- **Writable repos:** menno420/superbot-mineverse (FLAGSHIP) + menno420/superbot-games + menno420/superbot-idle.
- **Folds (sources):** superbot-games (v3) + superbot-idle (v2) + superbot-mineverse (v2) — full prior packages live in git history:
  `projects/superbot-games/` · `projects/superbot-idle/` · `projects/superbot-mineverse/` (last full state @ `1dea86d`).
- **Seat notes:** Flagship = mineverse; the OAuth login-CSRF fix lands BEFORE any secrets work. Old seats' armed failsafe triggers (games trig_019ZgWyL78Rx1sr6LhvL8NE3, idle trig_01TWKGFW8RUsMvxUMt2ndzqA, mineverse trig_01K8xmAKYS5S2HLy1HPANM7j — last committed registry state) still target the OLD seats: the rebind-then-delete cutover recipe is in this package's `failsafe-prompt.md` v1 (slice 2) and executes at the merged seat's boot.
- **Deployed state:** instructions never pasted; prompts authored (v1,
  slice 2) but never pasted; no trigger armed FOR THIS SEAT yet (boot/slice 3).

## Deployed-state per part (2026-07-18)

| Part | State |
|---|---|
| `instructions.md` (Custom Instructions) | v3.7 · 2026-07-18 · registry-current; never console-pasted — the registry copy is the deployed artifact |
| `coordinator-prompt.md` (coordinator / wake prompt) | v3.7 · 2026-07-18 · registry-current; never console-pasted |
| `failsafe-prompt.md` | v3.7 · 2026-07-18 · registry-current; failsafe byte-state verified via the triggers snapshot, not this table |
