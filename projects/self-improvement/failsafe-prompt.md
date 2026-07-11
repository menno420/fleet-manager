<!-- v1 · 2026-07-11 · fleet-manager projects registry -->
# Self Improvement — failsafe cron text (Q-0265)

> Part 4 of the Self Improvement Project package. **Routine name:**
> `self-improvement failsafe wake` · **cadence:** `0 */2 * * *` (even hours
> :00 — the substrate-kit seat's existing slot in the gen-3 lane stagger;
> manager reads at :30) · fires into the persistent coordinator session
> (default self-bind). **Provenance:** v1 · 2026-07-11, owner restructure
> directive 2026-07-11 — replaces the slice-1 v0 placeholder; the seat is a
> rename of the substrate-kit seat (source package @ `1dea86d`), whose
> Q-0265 failsafe re-arm was ALREADY due (the old pre-Q-0265 standing wake
> is still what's armed). Per registry doctrine the trigger prompt block
> below is deliberately NOT version-stamped in-band (byte-checkable against
> `list_triggers`).
>
> **Deployed state (2026-07-11): NOT ARMED as a failsafe.** Still armed
> (last committed registry state — re-verify via `list_triggers` before
> acting): `trig_016EfUawz6KxEYqUM6f1BqDw` — "substrate-kit 2-hourly
> standing wake" (the OLD pre-Q-0265 standing wake, not a dead-man
> failsafe).
>
> **Cutover recipe (rides the seat's next boot — coordinator-prompt.md BOOT
> step 2, rebind-then-delete):** create THIS trigger first, verify via
> `list_triggers` (the registry is the proof — never wait for the first
> fire), THEN delete the old standing wake and verify it absent. Record
> every call + outcome verbatim in `control/status.md`. If the seat's
> surface walls the calls: record the verbatim denial and hand the owner
> this block (name + cadence + prompt) via the owner-queue.

## The prompt (create_trigger `prompt` field, verbatim)

```
FAILSAFE WAKE (self-improvement, Q-0265): if your send_later continuation
chain is alive, verify that in one line and end. If it stalled, resume the
work loop: sync menno420/substrate-kit to origin/main HEAD →
control/inbox.md at HEAD → slice after slice, each its own PR on the full
quality bar (pytest + check --strict + dist byte-pin + ruff) — kit
development and fleet distribution only; never a lane's domain work
(Q-0261.3) — and re-arm the chain (~15 min) before ending. Overwrite
control/status.md as the deliberate last step.
```

## create_trigger args (recipe)

- `name`: `self-improvement failsafe wake`
- `cron_expression`: `0 */2 * * *`
- target: this (persistent coordinator) session — default self-bind; do NOT
  set `create_new_session_on_fire`
- `prompt`: the fenced block above, verbatim
- After creating: verify via `list_triggers`, then retire the old standing
  wake `trig_016EfUawz6KxEYqUM6f1BqDw` (delete + verify absent) and record
  all calls verbatim in the heartbeat.
