<!-- v1 · 2026-07-10 · fleet-manager projects registry -->
# pokemon-mod-lab — failsafe cron text (Q-0265) — NOT ARMED

> Part 4 of the pokemon-mod-lab Project package. **Routine name:**
> `pokemon-mod-lab failsafe wake` · **cadence:** `0 */2 * * *` (even hours
> :00 — the fleet stagger: lanes `0 */2`, manager `30 */2`; gen-3 deployment
> standard §2) · fires into the persistent coordinator session.
>
> **Cadence provenance — supersession note:** the in-repo ask on record is
> inbox **ORDER 002** ("SELF-ARM YOUR WAKE ROUTINE… cadence hourly, prompt:
> 'Read control/inbox.md at HEAD and run the standing ritual from your
> instructions.'" — `control/inbox.md` @ `a76ada7`, status `new`, never
> executed: status.md orders line shows only ORDER 001 done). That hourly
> Class-A discrete-wake ask is the **pre-Q-0265 model** and is SUPERSEDED by
> this file: under Q-0265 the send_later ~15-min chain is the pacemaker and
> the cron is a dead-man failsafe only, so the gen-3 standard cadence
> **`0 */2 * * *`** is prescribed here, not hourly. Arming this failsafe and
> recording the create_trigger call verbatim in `control/status.md`
> satisfies ORDER 002's done-when (mechanism documented) with the
> supersession noted — see coordinator-prompt.md step 3.
>
> **Deployed-state (2026-07-10): NOT ARMED.** No trigger is recorded
> anywhere in the repo (`control/status.md` @ `a76ada7` has no routine
> line; ORDER 002 unexecuted). The lane advanced overnight on
> manager/owner-driven sessions only and is currently LIVE-PARKED.
>
> Template provenance: the Q-0265 §2b failsafe template (superbot
> `docs/planning/round3-dispatch-part4-brief-2026-07-10.md`), as deployed
> verbatim on idea-engine (`trig_0178q9Je2xRFJgthwamrg9Br`) and
> superbot-next — adapted for this seat with the R22 visibility guard and
> the private-rail work loop.

## The prompt (create_trigger `prompt` field, verbatim)

```
FAILSAFE WAKE (pokemon-mod-lab, Q-0265): if your send_later continuation
chain is alive, verify that in one line and end. If it stalled, resume the
work loop (sync menno420/pokemon-mod-lab to origin/main HEAD →
control/inbox.md at HEAD → R22: verify visibility==private via API and
carry the verified line into status → next Emerald QoL+ increment,
increment after increment, each headless-proven and merged on green;
PRIVATE hard rail above all) and re-arm the chain (~15 min) before ending.
Overwrite control/status.md as the deliberate last step.
```

## create_trigger args (recipe)

- `name`: `pokemon-mod-lab failsafe wake`
- `cron_expression`: `0 */2 * * *`
- target: the persistent coordinator session — default self-bind; do NOT set
  `create_new_session_on_fire`
- `prompt`: the fenced block above, verbatim
- After creating: verify via `list_triggers` (the registry is the proof —
  never wait for the first fire) and record the call verbatim in
  `control/status.md` (the idea-engine status line is the format exemplar).
- Seat-dependent tool wall: if `create_trigger`/`send_later` are absent on
  this seat (the sim-lab precedent — "tool not present in session toolset"),
  record the exact refusal in status + ⚑ an owner fallback ask, per ORDER
  002's failure branch.
