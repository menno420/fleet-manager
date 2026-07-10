<!-- v1 · 2026-07-10 · fleet-manager projects registry -->
# venture-lab — failsafe cron text (Q-0265)

> Part 4 of the venture-lab Project package. **Routine name:**
> `venture-lab failsafe wake` · **cadence:** `0 */2 * * *` (even hours :00 —
> the gen-3 standard's lane stagger: lanes `0 */2`, manager `30 */2`) · fires
> into the persistent coordinator session (default self-bind).
>
> **Deployed-state note (2026-07-10): NOT ARMED — nothing to replace.** The
> lane is CLOCKLESS: `list_triggers` shows no venture-lab trigger
> (fleet-manager `docs/launch-readiness-2026-07-10.md` "Gap found live"), and
> inbox ORDER 002 (self-arm an hourly standing wake) sits UNEXECUTED at
> `control/inbox.md` @ `f999ddf` with no routine record anywhere in
> `control/status.md`. **Arming rides the fresh boot**: the coordinator
> prompt (part 2) has the seat self-arm this text as its dead-man failsafe —
> ORDER 002's hourly standing-wake wording is superseded by Q-0265 (the
> send_later ~15-min chain is the pacemaker; cron is the failsafe only) —
> and record the create_trigger call + list_triggers confirmation VERBATIM in
> `control/status.md` per ORDER 002's done-when (or the exact refusal text +
> ⚑ owner fallback if the surface denies it).
>
> Template provenance: part-4 brief §2b failsafe template (superbot
> `docs/planning/round3-dispatch-part4-brief-2026-07-10.md`), adapted for the
> venture-lab seat.

## The prompt (create_trigger `prompt` field, verbatim)

```
FAILSAFE WAKE (venture-lab, Q-0265): if your send_later continuation chain
is alive, verify that in one line and end. If it stalled, resume the work
loop (sync menno420/venture-lab to origin/main HEAD → control/inbox.md at
HEAD → slice after slice, each its own merged-on-green PR — revenue work
under the Q-0259.4 profitability mandate and money protocol; ⚑B/⚑D stay
FROZEN until ORDER 003's real-Stripe-path fix is merged with green
real-path tests; no spend/accounts/publishing without an owner click) and
re-arm the chain (~15 min) before ending. Overwrite control/status.md as
the deliberate last step.
```

## create_trigger args (recipe)

- `name`: `venture-lab failsafe wake`
- `cron_expression`: `0 */2 * * *`
- target: this (persistent coordinator) session — default self-bind; do NOT
  set `create_new_session_on_fire`
- `prompt`: the fenced block above, verbatim
- After creating: verify via `list_triggers` (the registry is the proof —
  never wait for the first fire) and record the call + confirmation verbatim
  in `control/status.md` (ORDER 002 done-when).
