<!-- v2 · 2026-07-11 · fleet-manager projects registry -->
# Venture Lab — failsafe cron text (Q-0265)

> Part 4 of the Venture Lab Project package. **Routine name:**
> `venture-lab failsafe wake` · **cadence:** `0 */2 * * *` (even hours :00 —
> the gen-3 lane stagger; manager reads at :30) · fires into the persistent
> coordinator session (default self-bind). **Provenance:** v2 · 2026-07-11,
> owner restructure directive 2026-07-11 — re-synced to `instructions.md` v3
> (venture-lab + trading-strategy, ONE seat); supersedes v1 · 2026-07-10,
> whose prompt hardcoded the ORDER 003 freeze state (v1 in git history). Per
> registry doctrine the trigger prompt block below is deliberately NOT
> version-stamped in-band (byte-checkable against `list_triggers`).
>
> **Deployed state (2026-07-11): NOT ARMED for this seat.** venture-lab
> itself was CLOCKLESS; in the merged seat's scope one old trigger is armed
> (last committed registry state — re-verify via `list_triggers` before
> acting): `trig_01YBaVeKAW2fSD83S9F37s2d` — "trading-strategy failsafe
> wake" (`0 */2 * * *`, re-armed seat-side 2026-07-10T21:03Z; the
> trading-strategy program is COMPLETE ON MAIN and the annex is
> research-only — it wakes with this seat now, not on its own clock).
>
> **Cutover recipe (rides the merged seat's boot — coordinator-prompt.md
> BOOT step 2, rebind-then-delete):** create THIS trigger first, verify via
> `list_triggers` (the registry is the proof — never wait for the first
> fire), THEN delete the old trading-strategy failsafe and verify it absent.
> Record every call + outcome verbatim in `control/status.md`. If the
> seat's surface walls the calls: record the verbatim denial and hand the
> owner this block (name + cadence + prompt) via the owner-queue.

## The prompt (create_trigger `prompt` field, verbatim)

```
FAILSAFE WAKE (venture-lab, Q-0265): if your send_later continuation chain
is alive, verify that in one line and end. If it stalled, resume the work
loop: sync menno420/venture-lab + trading-strategy to origin/main HEAD →
read each control/inbox.md at HEAD → slice after slice, each its own PR —
revenue work under the Q-0259.4 profitability mandate and money protocol
(no spend/accounts/publishing/payment flows without an owner click; no
secret values); trading-strategy stays RESEARCH-ONLY, holdout spent — no
live trading, ever — and re-arm the chain (~15 min) before ending.
Overwrite venture-lab control/status.md as the deliberate last step.
```

## create_trigger args (recipe)

- `name`: `venture-lab failsafe wake`
- `cron_expression`: `0 */2 * * *`
- target: this (persistent coordinator) session — default self-bind; do NOT
  set `create_new_session_on_fire`
- `prompt`: the fenced block above, verbatim
- After creating: verify via `list_triggers`, then retire the old
  trading-strategy failsafe `trig_01YBaVeKAW2fSD83S9F37s2d` (delete +
  verify absent) and record all calls verbatim in the heartbeat.
