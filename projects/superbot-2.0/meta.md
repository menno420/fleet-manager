<!-- v3.7 · 2026-07-18 · fleet-manager projects registry -->
# SuperBot 2.0 — Project package meta

> **Status:** `new seat — v1, owner fleet restructure 2026-07-11 (slice 1)`.
> Created by the restructure to the 8 standing Projects. Nothing of this
> package is deployed yet: `instructions.md` v1 is authored (never pasted);
> `coordinator-prompt.md` / `failsafe-prompt.md` carry REAL v1 bodies since
> slice 2 (prompt re-sync, 2026-07-11) — never pasted/armed; deployment +
> trigger cutover ride the merged seat's boot (rebind-then-delete recipe in
> `failsafe-prompt.md`).

- **Seat:** SuperBot 2.0 (standing Project).
- **Writable repos:** menno420/superbot (LIVE production bot — hub) + menno420/superbot-next (rebuild).
- **Folds (sources):** superbot (v2) + superbot-next (v2) — full prior packages live in git history:
  `projects/superbot/` · `projects/superbot-next/` (last full state @ `1dea86d`).
- **Seat notes:** superbot stays the ORACLE for the port; merging superbot = deploying (Q-0193); superbot-next carries the never-wait rebuild doctrine (Q-0241).
- **Deployed state:** instructions never pasted; prompts authored (v1,
  slice 2) but never pasted; no trigger armed FOR THIS SEAT yet (boot/slice 3).

## Deployed-state per part (2026-07-18)

| Part | State |
|---|---|
| `instructions.md` (Custom Instructions) | v3.7 · 2026-07-18 · registry-current; never console-pasted — the registry copy is the deployed artifact |
| `coordinator-prompt.md` (coordinator / wake prompt) | v3.7 · 2026-07-18 · registry-current; never console-pasted |
| `failsafe-prompt.md` | v3.7 · 2026-07-18 · registry-current; failsafe byte-state verified via the triggers snapshot, not this table |
