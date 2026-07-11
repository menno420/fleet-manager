<!-- v1 · 2026-07-11 · fleet-manager projects registry -->
# SuperBot World — failsafe cron text (Q-0265)

> Part 4 of the SuperBot World Project package. **Routine name:**
> `superbot-world failsafe wake` · **cadence:** `20 */2 * * *` (even hours
> :20 — inherits the flagship mineverse slot in the gen-3 lane stagger;
> manager reads at :30) · fires into the persistent coordinator session
> (default self-bind). **Provenance:** v1 · 2026-07-11, owner restructure
> directive 2026-07-11 — replaces the slice-1 v0 placeholder; authored from
> the three source failsafes (superbot-games v3 · superbot-idle v2 ·
> superbot-mineverse v2 @ `1dea86d`). Per registry doctrine the trigger
> prompt block below is deliberately NOT version-stamped in-band
> (byte-checkable against `list_triggers`).
>
> **Deployed state (2026-07-11): NOT ARMED for this seat.** Three OLD seat
> failsafes are still armed against the retired seats (last committed
> registry state — re-verify via `list_triggers` before acting):
> - superbot-games: `trig_019ZgWyL78Rx1sr6LhvL8NE3` (`15 */2 * * *`)
> - superbot-idle: `trig_01TWKGFW8RUsMvxUMt2ndzqA` (`45 */2 * * *`)
> - superbot-mineverse: `trig_01K8xmAKYS5S2HLy1HPANM7j` (`20 */2 * * *`)
>
> **Cutover recipe (rides the merged seat's boot — coordinator-prompt.md
> BOOT step 2, rebind-then-delete):** create THIS trigger first, verify via
> `list_triggers` (the registry is the proof — never wait for the first
> fire), THEN delete the three old triggers and verify them absent. Record
> every call + outcome verbatim in the flagship heartbeat. If the seat's
> surface walls the calls: record the verbatim denial and hand the owner
> this block (name + cadence + prompt) via the owner-queue.

## The prompt (create_trigger `prompt` field, verbatim)

```
FAILSAFE WAKE (superbot-world, Q-0265): if your send_later continuation
chain is alive, verify that in one line and end. If it stalled, resume the
work loop: sync menno420/superbot-mineverse + superbot-games +
superbot-idle to origin/main HEAD → read each control/inbox.md at HEAD →
slice after slice, each its own PR (mineverse flagship first — the OAuth
login-CSRF fix before any secrets work; web app never touches the bot
Postgres or token; idle/games sequenced behind the flagship; no
pay-to-win) — and re-arm the chain (~15 min) before ending. Overwrite the
flagship control/status.md as the deliberate last step.
```

## create_trigger args (recipe)

- `name`: `superbot-world failsafe wake`
- `cron_expression`: `20 */2 * * *`
- target: this (persistent coordinator) session — default self-bind; do NOT
  set `create_new_session_on_fire`
- `prompt`: the fenced block above, verbatim
- After creating: verify via `list_triggers`, then retire the three old-seat
  triggers (delete + verify absent) and record all calls verbatim in the
  heartbeat.
