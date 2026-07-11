<!-- v1 · 2026-07-11 · fleet-manager projects registry -->
# superbot-idle — failsafe wake trigger (Seat B) — DEPLOYED + REGISTRY-VERIFIED

> Part 4 of the superbot-idle package. **Status: ARMED + LIVE** — the seat
> SELF-ARMED this trigger during its own boot (recorded in the seat's
> `control/status.md` § ROUTINE RECORD: "cron trigger created via
> mcp__claude-code-remote__create_trigger … VERIFIED via list_triggers").
> This file is the registry's byte-checkable record of the STORED prompt —
> per registry doctrine, failsafe prompts carry NO in-band version stamp so
> the block below can be byte-matched against `list_triggers` output directly.

## Deployed trigger (registry metadata, `list_triggers` 2026-07-11T01:26:43Z)

- **trigger id:** `trig_01TWKGFW8RUsMvxUMt2ndzqA`
- **name:** `superbot-idle failsafe wake`
- **cron_expression:** `45 */2 * * *` (even hours :45 — lane stagger; Seat A
  runs `15 */2`, manager `30 */2`)
- **enabled:** true
- **persistent_session_id:** `session_01BRmUrjckzMsewsXzpc3wwW` (the Seat B
  coordinator session)
- **created (armed):** 2026-07-10T23:44:45Z · created_via `meta_mcp`
- **last_fired_at:** 2026-07-11T00:45:28Z · next_run_at 2026-07-11T02:45:00Z
  at extraction
- **prompt length:** 265 chars

## The stored prompt text

VERBATIM-FROM-REGISTRY · extracted 2026-07-11T01:26:43Z

```
FAILSAFE WAKE (superbot-idle, Q-0265): if your send_later continuation chain is alive, verify that in one line and end. If it stalled, resume the work loop (sync HEAD -> inbox -> slice after slice, each merged-on-green) and re-arm the chain (~15 min) before ending.
```

## Notes

- Generic §2b-template failsafe shape (superbot
  `docs/planning/round3-dispatch-part4-brief-2026-07-10.md`), seat-armed at
  boot. The cron is the dead-man failsafe only; the pacemaker is the seat's
  send_later/one-shot continuation chain (Q-0265) — the seat's status records
  chain links firing + re-arming on schedule ("Both ARMED-AND-VERIFIED").
