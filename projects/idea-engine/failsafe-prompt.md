# idea-engine — failsafe routine (DEPLOYED + VERIFIED)

> Package part 4 of 4 · seat: **Idea Engine** (core seat 4, LIVE).
> **Status: DEPLOYED + VERIFIED** — this is the fleet's only committed-verbatim deployed
> failsafe besides superbot-next's: the text below is transcribed VERBATIM from the seat's
> own committed heartbeat, idea-engine `control/status.md` @ c8651f7 (routine line), which
> records the full Q-0265 cutover including both trigger calls and the registry
> verification. Do NOT rewrite this text when assembling — it is the deployed artifact.

## Deployed trigger

- **Name:** `idea-engine failsafe wake`
- **Trigger id:** `trig_0178q9Je2xRFJgthwamrg9Br` — enabled
- **Cadence:** `0 */2 * * *` (even hours :00, 2-hourly — the pipeline stagger: engine even
  → sim-lab odd `0 1-23/2 * * *` → manager `30 */2 * * *`)
- **Binding:** persistent_session_id `session_01TwoaFmWeB8pYbHMyFYgjqJ` (coordinator
  self-bind)
- **Verified:** via `list_triggers` at cutover (old id `trig_01KBoHPaquSCDHysip67PQBh`:
  0 occurrences); first `next_run_at` recorded as `2026-07-10T20:00:30Z`
- **Cutover record (verbatim status line):** old wake DELETED —
  `delete_trigger {"trigger_id":"trig_01KBoHPaquSCDHysip67PQBh"}` →
  `"deleted trigger trig_01KBoHPaquSCDHysip67PQBh"` — then the new failsafe CREATED.

## The full deployed `create_trigger` call (verbatim)

```json
create_trigger {"name":"idea-engine failsafe wake","cron_expression":"0 */2 * * *","prompt":"FAILSAFE WAKE (idea-engine, Q-0265): if your send_later continuation chain is alive, verify that in one line and end. If it stalled, resume the work loop (sync HEAD → inbox → slice after slice, each merged-on-green) and re-arm the chain (~15 min) before ending."}
```

## The failsafe prompt text (verbatim, standalone)

```
FAILSAFE WAKE (idea-engine, Q-0265): if your send_later continuation chain is alive, verify that in one line and end. If it stalled, resume the work loop (sync HEAD → inbox → slice after slice, each merged-on-green) and re-arm the chain (~15 min) before ending.
```

## Notes for the assembler

- This is the **Q-0265 reference implementation** — the status routine line that records
  it is the template the fleet package generalizes for other seats (per-seat prompt:
  substitute the seat name; keep the seat's own stagger slot).
- The failsafe is NOT the pacemaker: the coordinator's `send_later` continuation chain
  (~15 min, "continue the work loop") drives the seat; the cron only detects a stalled
  chain (dead-man switch). Both were live ("Continuation chain armed and alive") at
  status @ c8651f7.
- The cadence is one half of an **inter-Project pair** (engine even-hour output ↔ sim-lab
  odd-hour pull, manager :30 sweep). Centralize/change it only as a pair.
