<!-- v1 · 2026-07-10 · fleet-manager projects registry -->
# trading-strategy — failsafe cron text (Q-0265)

> Part 4 of the trading-strategy Project package. **Routine name:**
> `trading-strategy failsafe wake` · **recommended cadence:** `0 */2 * * *`
> (even hours :00 — the core-seat stagger: lanes `0 */2`, manager `30 */2`;
> gen-3 deployment standard §2) · fires into the persistent coordinator
> session.
>
> **Deployed-state note (2026-07-10):** the trigger currently live is
> `trig_01Mvn5xRmqGmZJNRHgjqyLpN`, cron `0 */4 * * *`, armed at the ORDER 006
> boot and carried unchanged through the ORDER 007/008 close-outs
> (trading `control/status.md` ROUTINE STATE @ `ffdd6f6`; fires confirmed
> 04:08Z/08:00Z/12:00Z 2026-07-10). It is **stale on two axes**: (1) it is
> session-bound to the OLD coordinator chat (the gen-2 ORDER-006 seat), not
> to whatever fresh seat this package boots; (2) its prompt is the old
> pre-Q-0265 delegating ritual — verbatim per ORDER 006: 'Read
> control/inbox.md at HEAD and run the standing ritual from your
> instructions.' Under Q-0265 the cron is a dead-man FAILSAFE only; the
> send_later ~15-min chain is the pacemaker.
>
> **Cutover recipe (F-1 — re-arm THEN delete; never a clockless window):**
> the fresh seat, on its first capable turn: (1) `create_trigger` with the
> name/cron/prompt below, default self-bind into ITS OWN persistent session
> (do NOT set `create_new_session_on_fire`); (2) verify the new trigger via
> `list_triggers` — the registry is the proof, never wait for the first
> fire; (3) only then `delete_trigger` the old
> `trig_01Mvn5xRmqGmZJNRHgjqyLpN`; (4) record both calls verbatim in
> `control/status.md` § routine state.
>
> Template provenance: part-4 brief §2b failsafe template (superbot
> `docs/planning/round3-dispatch-part4-brief-2026-07-10.md`), adapted for
> the trading seat's post-P5 rails.

## Deployed prompt — VERBATIM-FROM-REGISTRY (extracted 2026-07-10 ~22:05Z via `list_triggers`)

**Deployed-state update (gap-closure pass):** the cutover HAPPENED after this
package's build snapshot — the old `trig_01Mvn5xRmqGmZJNRHgjqyLpN` (`0 */4`,
gen-2 delegating ritual) is GONE from the registry, and the live trigger is
now **`trig_01YBaVeKAW2fSD83S9F37s2d` "trading-strategy failsafe wake"**,
cron `0 */2 * * *`, created 2026-07-10T21:03:05Z, bound to coordinator
session `session_01NwvvbgUVSdQvY8eYwtuEoo` (matches the fm roster's 21:03Z
re-arm record). Its stored prompt, byte-exact, single line as stored (315
chars) — a SHORTENED seat-authored variant, not the fuller canonical block
below (the canonical text keeps the holdout-SPENT / dedicated-session /
PARKED-GREEN rails in-band; the deployed variant compresses them to "grade
due ledger windows before new research"):

```
FAILSAFE WAKE (trading-strategy, Q-0265): if your send_later continuation chain is alive, verify that in one line and end. If it stalled, resume the work loop (sync HEAD -> inbox -> slice after slice, each merged-on-green — grade due ledger windows before new research) and re-arm the chain (~15 min) before ending.
```

## The prompt (create_trigger `prompt` field, verbatim) — canonical re-arm text

```
FAILSAFE WAKE (trading-strategy, Q-0265): if your send_later continuation
chain is alive, verify that in one line and end. If it stalled, resume
the work loop (sync menno420/trading-strategy to origin/main HEAD →
control/inbox.md at HEAD → slice after slice, each its own
merged-on-green PR per the landing path — new orders, then hygiene, then
backlog per your standing brief). Rails: the holdout is SPENT and stays
spent (protocol §6 — no re-runs, no new windows, ever); a holdout-class
order goes to a DEDICATED fresh session you spawn, never this seat
(protocol §7); PARKED GREEN is legitimate only with an empty inbox AND
the manager flagged. Re-arm the chain (~15 min) before ending; overwrite
control/status.md as the deliberate last step.
```

## create_trigger args (recipe)

- `name`: `trading-strategy failsafe wake`
- `cron_expression`: `0 */2 * * *` (recommended; supersedes the deployed
  `0 */4 * * *` — align with the core-seat stagger)
- target: the fresh persistent coordinator session — default self-bind; do
  NOT set `create_new_session_on_fire`
- `prompt`: the fenced block above, verbatim
