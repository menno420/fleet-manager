# fleet-manager — failsafe cron (dead-man wake)

> **Status: DEPLOYED + VERIFIED** — trigger `trig_014odnv5h1tkJAFRhix3tGLq`,
> created 2026-07-10T20:26:23Z, bound to the coordinator session
> `session_01V66KdPhtbR1AThhK77kDqr`; verified live (present + `enabled: true`)
> in the full 88-record `list_triggers` output at ~20:47Z, `next_run_at`
> 2026-07-10T22:34:20Z. The prior standing wake
> `trig_01QBrp5MjZL3F9mv6KsTXTzN` ("fleet-manager 2-hourly standing wake") was
> deleted and verified gone in the same listing. Record: fm `control/status.md`
> re-arm record + `control/inbox.md` ORDER 011 ✅ DONE block (Q-0265 cutover,
> landed via fleet-manager PR #37, branch `claude/order-003-007-review-queue`;
> origin/main was still @702ba89 "in-progress" at build time — the DONE record
> is the newer state).

## Trigger fields

- **name:** `fleet-manager failsafe wake`
- **cron:** `30 */2 * * *` — the manager's :30 offset per the gen-3 standard
  (lanes fire even hours `0 */2`; the manager fires at :30 so it reads lane
  heartbeats written at the top of the hour)
- **binding:** persistent — fires into the live coordinator chat (not
  fresh-session-per-fire)

## Prompt text (deployed)

```
FAILSAFE WAKE (fleet-manager, Q-0265): if your send_later continuation chain is
alive, verify that in one line and end. If it stalled, resume the work loop
(sync HEAD → inbox → slice after slice, each merged-on-green) and re-arm the
chain (~15 min) before ending.
```

**Provenance of the text:** this is the Q-0265 failsafe template (superbot
`docs/planning/round3-dispatch-part4-brief-2026-07-10.md` §2b, step 3)
instantiated with `<seat>` = fleet-manager — the exact pattern ORDER 011's `do:`
ordered deployed ("fleet-manager failsafe wake", same 30 */2 cadence, chain-alive
→ one-line verify + end / chain-stalled → resume + re-arm). Honesty note: the
in-repo re-arm record (status.md) commits the trigger **id, name, cron, creation
time, session binding, and the pattern in summary form** verbatim; the full
prompt string above is the §2b template the cutover executed, not a
character-for-character quote lifted from status.md — a future verifier can
confirm the stored prompt via `list_triggers` (it returns the prompt field).

## Role in the operating model (Q-0265)

The cron is the **dead-man failsafe only**. The pacemaker is the **~15-minute
`send_later` continuation chain** ("continue the work loop: sync HEAD → inbox →
next slice → re-arm"), re-armed before ending every turn — first chain fire
2026-07-10T20:43Z executed the ORDER 003/007 slice (PR #37). If the failsafe
ever has to fire the loop back to life, the coordinator resumes and re-arms the
chain, then records the event on its heartbeat.

## Re-arm recipe (proven cutover, F-1)

Rebind-then-delete: `create_trigger` the new failsafe first (name/cron/prompt
above, `persistent_session_id` = the coordinator session), verify via
`list_triggers` (never wait for the first fire — completed runs are not
inspectable owner-side), then `delete_trigger` the old id and verify it is
absent. Record both calls + outcomes verbatim in `control/status.md`
(`docs/prompts/init-prompt-universal.md` § Current text holds the fleet recipe).
