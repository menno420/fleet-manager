<!-- v1 · 2026-07-10 · fleet-manager projects registry -->
# Builder failsafe wake — DEPLOYED + VERIFIED (this seat is the reference)

> **Status:** DEPLOYED + VERIFIED. This is the canonical deployed failsafe of the
> fleet — the Q-0265 cutover was executed live on this seat and recorded VERBATIM
> in superbot-next `control/status.md` (ORDER 008 record, origin/main @
> `9757755c61034edad4b5dee5ab715783da18f1a6`). Other seats' failsafe texts derive
> from the generic §2b template (superbot
> `docs/planning/round3-dispatch-part4-brief-2026-07-10.md`); this one is the
> committed, registry-verified instance.

**Trigger:** `trig_01L5JBefGSCM1fUdwm4SRQnY` · name `Builder failsafe wake` ·
**cadence `0 */2 * * *`** (2-hourly, even hours :00 — lane stagger; the manager
runs `30 */2`) · fires into persistent session
`session_01HRfuSKiQSnGHXKne3yzadg` · created 2026-07-10, enabled, first
`next_run_at 2026-07-10T20:05:55Z`, **verified via `list_triggers`** (never
wait for a fire as proof — runs are not inspectable owner-side).

## The deployed prompt text (verbatim, from control/status.md)

**Byte-verified against the live registry** (gap-closure pass, `list_triggers`
2026-07-10 ~22:05Z): the stored prompt of `trig_01L5JBefGSCM1fUdwm4SRQnY`
matches the block below byte-for-byte (257 chars).

```
FAILSAFE WAKE (Builder, Q-0265): if your send_later continuation chain is alive, verify that in one line and end. If it stalled, resume the work loop (sync HEAD → inbox → slice after slice, each merged-on-green) and re-arm the chain (~15 min) before ending.
```

## Cutover record (verbatim-in-substance, control/status.md ORDER 008 record)

- **DELETED:** `delete_trigger {"trigger_id":"trig_01VYZQ7GHxYq3ecSw8UNZek8"}` →
  "deleted trigger trig_01VYZQ7GHxYq3ecSw8UNZek8" (old builder-wake cron,
  verified absent from list_triggers).
- **CREATED failsafe:** `create_trigger {"name":"Builder failsafe wake",
  "cron_expression":"0 */2 * * *",
  "persistent_session_id":"session_01HRfuSKiQSnGHXKne3yzadg",
  "prompt":"FAILSAFE WAKE (Builder, Q-0265): …"}` → SUCCESS,
  `trig_01L5JBefGSCM1fUdwm4SRQnY`, enabled, verified via list_triggers.
- **CHAIN MECHANISM (the pacemaker the failsafe backs):** `send_later` cannot
  target another session (schema: message/at/delay_minutes only, fires into the
  calling session), so the continuation chain runs on **one-shot
  `create_trigger` calls into the coordinator session** — first link
  `trig_01KedTiCKYMbB3oaNZL5rHmf` ("Builder continuation chain (one-shot)",
  run_once_at 2026-07-10T20:03:00Z); the coordinator re-arms a fresh one-shot
  each turn (a one-shot self-disables after firing,
  ended_reason=run_once_fired). The failsafe cron catches any stalled chain.
