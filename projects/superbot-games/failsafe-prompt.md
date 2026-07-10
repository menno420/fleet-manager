# superbot-games — failsafe cron text (Q-0265)

> Part 4 of the superbot-games Project package. **Routine name:**
> `superbot-games failsafe wake` · **cadence:** `0 */2 * * *` (even hours :00 —
> the core/lane stagger: lanes `0 */2`, manager `30 */2`; gen-3 deployment
> standard §2) · fires into the persistent merged-lane coordinator session.
>
> **NOT ARMED (2026-07-10).** The repo is CLOCKLESS: no routine exists anywhere
> for it; inbox ORDER 002 (self-arm, status:new) is UNEXECUTED — arming this
> failsafe + the pacemaker chain IS that order's Q-0265-shaped execution
> (adaptation flagged in the coordinator prompt: the order's literal spec was
> a pre-Q-0265 hourly standing wake). Known wall, on record verbatim from the
> mining gen-1 close-out (superbot-games `control/status-mining.md` @
> `4493292`): routine "NOT ARMED — no scheduler tool available this session
> ('No such tool available: mcp__claude-code-remote__send_later')". Scheduler
> tool availability is SEAT-DEPENDENT (websites/trading/kit/fleet-manager and
> the Builder seat all armed successfully the same day) — re-probe on every
> session; if the tools are absent on the arming seat, record the verbatim
> denial in status + a ⚑ owner fallback, per ORDER 002's required-record rule.
>
> Template provenance: part-4 brief §2b failsafe template (superbot
> `docs/planning/round3-dispatch-part4-brief-2026-07-10.md` @ `53fb5ef`),
> adapted for the merged games-plugins lane.

## The prompt (create_trigger `prompt` field, verbatim)

```
FAILSAFE WAKE (superbot-games, Q-0265): if your send_later/one-shot
continuation chain is alive, verify that in one line and end. If it stalled,
resume the work loop (sync menno420/superbot-games to origin/main HEAD →
control/inbox.md at HEAD → slice after slice, each its own merged-on-green PR
— mining and exploration plugin increments per your standing brief; the gate
is untrustworthy until ORDER 001's collect-ALL-suites fix is merged, so
verify with a full local collection) and re-arm the chain (~15 min) before
ending. Overwrite control/status.md as the deliberate last step.
```

## create_trigger args (recipe)

- `name`: `superbot-games failsafe wake`
- `cron_expression`: `0 */2 * * *`
- target: the persistent coordinator session — default self-bind when armed
  from that session; do NOT set `create_new_session_on_fire`
- `prompt`: the fenced block above, verbatim

## Arming record (ORDER 002 requirement — do not skip)

Write in `control/status.md`: the EXACT `create_trigger` call (tool name +
arguments) and its outcome VERBATIM; verify presence via `list_triggers` (the
registry is the proof — never wait for the first fire); on tool absence, the
verbatim denial text + ⚑ owner fallback. Drop the `ORDER 001 …gate…` clause
from the prompt at the first re-arm after the CI fix merges.
