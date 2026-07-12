<!-- v1 · 2026-07-11 · fleet-manager projects registry -->
# SuperBot 2.0 — failsafe cron text (Q-0265)

> Part 4 of the SuperBot 2.0 Project package. **Routine name:**
> `superbot-2.0 failsafe wake` · **cadence:** `0 */2 * * *` (even hours :00
> — inherits the superbot-next Builder slot in the gen-3 lane stagger;
> manager reads at :30) · fires into the persistent coordinator session
> (default self-bind). **Provenance:** v1 · 2026-07-11, owner restructure
> directive 2026-07-11 — replaces the slice-1 v0 placeholder; authored from
> the superbot-next Builder failsafe (fleet reference instance, package @
> `1dea86d`); superbot contributes no failsafe (it was NO SEAT by design,
> Q-0264). Per registry doctrine the trigger prompt block below is
> deliberately NOT version-stamped in-band (byte-checkable against
> `list_triggers`).
>
> **Deployed state (2026-07-11): NOT ARMED for this seat.** Still armed
> (last committed registry state — re-verify via `list_triggers` before
> acting): `trig_01L5JBefGSCM1fUdwm4SRQnY` — "Builder failsafe wake"
> (targets the retired superbot-next seat). Superbot's own hub triggers
> (docs-reconciliation, dispatch — poke-only/issue-based) are hub machinery,
> NOT part of this cutover: leave them alone.
>
> **Cutover recipe (rides the merged seat's boot — coordinator-prompt.md
> BOOT step 2, rebind-then-delete):** create THIS trigger first, verify via
> `list_triggers` (the registry is the proof — never wait for the first
> fire), THEN delete the old Builder failsafe and verify it absent. Record
> every call + outcome verbatim in the superbot-next heartbeat. If the
> seat's surface walls the calls: record the verbatim denial and hand the
> owner this block (name + cadence + prompt) via the owner-queue.

## The prompt (create_trigger `prompt` field, verbatim)

```
FAILSAFE WAKE (superbot-2.0, Q-0265): if your send_later continuation
chain is alive, verify that in one line and end. If it stalled, resume the
work loop: sync menno420/superbot-next + superbot to origin/main HEAD →
read the superbot-next control/inbox.md at HEAD → slice after slice, each
its own PR (rebuild first — port band by band, parity pins the ORACLE,
never-wait Q-0241, the report job is red by design; superbot itself is
production-critical-only: merging IS deploying, Q-0213 brake stands) — and
re-arm the chain (~15 min) before ending. Overwrite superbot-next
control/status.md as the deliberate last step.
```

## create_trigger args (recipe)

- `name`: `superbot-2.0 failsafe wake`
- `cron_expression`: `0 */2 * * *`
- target: this (persistent coordinator) session — default self-bind; do NOT
  set `create_new_session_on_fire`
- `prompt`: the fenced block above, verbatim
- After creating: verify via `list_triggers`, then retire the old Builder
  failsafe `trig_01L5JBefGSCM1fUdwm4SRQnY` (delete + verify absent) and
  record all calls verbatim in the heartbeat. Superbot hub triggers stay.
