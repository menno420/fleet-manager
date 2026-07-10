# gba-homebrew — failsafe cron text (Q-0265)

> Part 4 of the gba-homebrew Project package. **Routine name:**
> `gba-homebrew failsafe wake` · **cadence:** `0 */2 * * *` (even hours :00 —
> the fleet stagger: lanes `0 */2`, manager `30 */2`, sim-lab odd hours;
> gen-3 deployment standard §2) · fires into the persistent coordinator
> session (self-bind).
>
> **NOT ARMED (2026-07-10):** no routine exists for this lane — nothing to
> delete. The in-repo predecessor text is `control/inbox.md` **ORDER 002**
> (status: new, **UNEXECUTED** — the status orders line @ `bc73da7` records
> "acked=001 done=001 · no new orders at HEAD (inbox re-read 07:14Z)"; ORDER
> 002 landed after that re-read, the lane has never seen it), which instructs
> a self-armed **hourly** standing wake ("Read control/inbox.md at HEAD and
> run the standing ritual from your instructions"). **That hourly text is
> SUPERSEDED by this file, with provenance:** Q-0265 (owner directive,
> 2026-07-10) demotes the cron to a dead-man failsafe — the send_later
> ~15-min chain is the pacemaker — and the gen-3 deployment standard sets
> lane cadence `0 */2`, not hourly. The coordinator executes ORDER 002's
> *intent* (self-arm + document the mechanism) at first boot by arming THIS
> text instead, and records in `control/status.md` verbatim: the full
> `create_trigger` args + trigger id + `list_triggers` verification (the
> registry is the proof — never wait for the first fire) + one line naming
> the supersession (ORDER 002 hourly → Q-0265 failsafe). That satisfies
> ORDER 002's done-when; if the trigger tools are absent on the seat (the
> sim-lab precedent), record the exact refusal text + a ⚑ owner fallback
> ask, per the order's own failure branch.
>
> Template provenance: idea-engine's deployed failsafe (the Q-0265 reference
> implementation, committed verbatim in its control/status.md routine line),
> adapted for this lane.

## The prompt (create_trigger `prompt` field, verbatim)

```
FAILSAFE WAKE (gba-homebrew, Q-0265): if your send_later continuation chain
is alive, verify that in one line and end. If it stalled, resume the work
loop (sync menno420/gba-homebrew to origin/main HEAD → control/inbox.md at
HEAD → slice after slice, each its own merged-on-green PR — concept-pick
signal first, then review-queue drain / test coverage / the flagged
vertical slice, per your standing brief; original code + Butano only, NEVER
Track A material) and re-arm the chain (~15 min) before ending. Overwrite
control/status.md as the deliberate last step.
```

## create_trigger args (recipe)

- `name`: `gba-homebrew failsafe wake`
- `cron_expression`: `0 */2 * * *`
- target: this (persistent coordinator) session — default self-bind; do NOT
  set `create_new_session_on_fire`
- `prompt`: the fenced block above, verbatim
