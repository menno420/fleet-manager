<!-- v2 · 2026-07-11 · fleet-manager projects registry -->
# fleet-manager — failsafe cron (dead-man wake)

> **Status: DEPLOYED + VERIFIED** — trigger `trig_01F9UdoUtLy8oknBPBkHLshS`,
> created 2026-07-11T01:04:10Z, bound to the successor coordinator session
> `session_012o8pySy5K3AV6JWoPKryZL`; verified live (present + enabled) via
> `list_triggers` ~01:05Z, `next_run_at` 2026-07-11T02:33:34Z. The prior
> failsafe `trig_014odnv5h1tkJAFRhix3tGLq` (bound to the archived predecessor
> coordinator session `session_01V66KdPhtbR1AThhK77kDqr`) was deleted and
> verified-absent 2026-07-11 (F-1 rebind-then-delete cutover after the
> predecessor chat archive — new trigger created + verified FIRST, old id
> deleted second). The stored prompt of the new trigger was verified byte-exact
> against § "Prompt text (deployed)" below (497 chars) — the deployed text is
> UNCHANGED by the cutover. Record: fm `control/status.md` § "Successor seat
> LIVE — F-1 cutover complete" (fleet-manager PR #57).

## Trigger fields

- **name:** `fleet-manager failsafe wake`
- **cron:** `30 */2 * * *` — the manager's :30 offset per the gen-3 standard
  (lanes fire even hours `0 */2`; the manager fires at :30 so it reads lane
  heartbeats written at the top of the hour)
- **binding:** persistent — fires into the live coordinator chat (not
  fresh-session-per-fire)

## Prompt text (deployed) — VERBATIM-FROM-REGISTRY (extracted 2026-07-10 ~22:05Z via `list_triggers`)

The stored `prompt` field of `trig_014odnv5h1tkJAFRhix3tGLq`, byte-exact,
single line as stored (497 chars):

```
FAILSAFE WAKE (fleet manager, Q-0265): if your send_later continuation chain is alive, verify that in one line and end. If it stalled, resume the work loop — sync menno420/fleet-manager to origin/main HEAD, read control/inbox.md at HEAD, then slice after slice (staleness sweep → route/advance ORDERs → owner-queue + safe-to-delete → doctrine ORDERs), each shipped as its own merged-on-green PR — and re-arm the chain (~15 min) before ending. Heartbeat control/status.md as each batch's last step.
```

**Provenance of the text:** extracted verbatim from the live trigger registry
by the 2026-07-10 gap-closure pass (this replaces the earlier honesty-noted
template reconstruction, which differed from the deployed text: the stored
prompt says "fleet manager" — space, not hyphen — and carries the manager's
own richer work loop: staleness sweep → route/advance ORDERs → owner-queue +
safe-to-delete → doctrine ORDERs, plus the heartbeat-as-last-step clause;
the old generic §2b template quote is superseded by the block above). A
future verifier re-confirms via `list_triggers` — the registry returns the
stored prompt; see `../_inventory/trigger-registry-2026-07-10.md`.

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
