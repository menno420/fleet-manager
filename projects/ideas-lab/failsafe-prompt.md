<!-- v1 · 2026-07-11 · fleet-manager projects registry -->
# Ideas Lab — failsafe cron text (Q-0265)

> Part 4 of the Ideas Lab Project package. **Routine name:**
> `ideas-lab failsafe wake` · **cadence:** `0 */2 * * *` (even hours :00 —
> the gen-3 lane stagger; the old idea-engine/sim-lab even/odd cadence
> pairing is RETIRED with the merge) · fires into the persistent coordinator
> session (default self-bind). **Provenance:** v1 · 2026-07-11, owner
> restructure directive 2026-07-11 — replaces the slice-1 v0 placeholder;
> authored from the source failsafes (idea-engine v2 · sim-lab v2 @
> `1dea86d`). Per registry doctrine the trigger prompt block below is
> deliberately NOT version-stamped in-band (byte-checkable against
> `list_triggers`).
>
> **Deployed state (2026-07-11): NOT ARMED for this seat.** Two OLD seat
> failsafes are still armed against the retired seats (last committed
> registry state — re-verify via `list_triggers` before acting):
> - idea-engine: `trig_0178q9Je2xRFJgthwamrg9Br` (`0 */2 * * *`, even)
> - sim-lab: `trig_01SHfnLv6EqZesr4tC3T9kUU` (`0 1-23/2 * * *`, odd)
>
> **Cutover recipe (rides the merged seat's boot — coordinator-prompt.md
> BOOT step 2, rebind-then-delete):** create THIS trigger first, verify via
> `list_triggers` (the registry is the proof — never wait for the first
> fire), THEN delete both old triggers and verify them absent. Record every
> call + outcome verbatim in the idea-engine heartbeat. If the seat's
> surface walls the calls: record the verbatim denial and hand the owner
> this block (name + cadence + prompt) via the owner-queue.

## The prompt (create_trigger `prompt` field, verbatim)

```
FAILSAFE WAKE (ideas-lab, Q-0265): if your send_later continuation chain
is alive, verify that in one line and end. If it stalled, resume the work
loop: sync menno420/idea-engine + sim-lab to origin/main HEAD → read each
control/inbox.md at HEAD → generate → verify → verdict, slice after slice,
each its own PR (the loop is internal to this seat — never wait on another
Project; the verifier stays skeptical of the generator; WIP cap ≤3;
build-worthy verdicts go to the manager, never dispatched here) — and
re-arm the chain (~15 min) before ending. Overwrite idea-engine
control/status.md as the deliberate last step.
```

## create_trigger args (recipe)

- `name`: `ideas-lab failsafe wake`
- `cron_expression`: `0 */2 * * *`
- target: this (persistent coordinator) session — default self-bind; do NOT
  set `create_new_session_on_fire`
- `prompt`: the fenced block above, verbatim
- After creating: verify via `list_triggers`, then retire the two old-seat
  triggers (delete + verify absent) and record all calls verbatim in the
  heartbeat.
