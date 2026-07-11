<!-- v2 · 2026-07-11 · fleet-manager projects registry -->
# superbot-games — failsafe wake trigger (Seat A) — DEPLOYED + REGISTRY-VERIFIED

> Part 4 of the superbot-games package. **Status: ARMED + LIVE** — the seat
> SELF-BOOTED and armed this trigger itself 2026-07-10T23:47:02Z (v1's "NOT
> ARMED / repo CLOCKLESS" state is history; ORDER 002's substance executed
> seat-side in the Q-0265 shape). This file is the registry's byte-checkable
> record of the STORED prompt — per registry doctrine, failsafe prompts carry
> NO in-band version stamp so the block below can be byte-matched against
> `list_triggers` output directly.

## Deployed trigger (registry metadata, `list_triggers` 2026-07-11T01:26:43Z)

- **trigger id:** `trig_019ZgWyL78Rx1sr6LhvL8NE3`
- **name:** `superbot-games failsafe wake`
- **cron_expression:** `15 */2 * * *` (even hours :15 — lane stagger; Seat B
  runs `45 */2`, manager `30 */2`)
- **enabled:** true
- **persistent_session_id:** `session_01TZcMwFdE7zvViW9HgH7fqZ` (the Seat A
  coordinator session)
- **created (armed):** 2026-07-10T23:47:02Z · created_via `meta_mcp`
- **last_fired_at:** 2026-07-11T00:15:39Z · next_run_at 2026-07-11T02:15:00Z
  at extraction
- **prompt length:** 266 chars

## The stored prompt text

VERBATIM-FROM-REGISTRY · extracted 2026-07-11T01:26:43Z

```
FAILSAFE WAKE (superbot-games, Q-0265): if your send_later continuation chain is alive, verify that in one line and end. If it stalled, resume the work loop (sync HEAD -> inbox -> slice after slice, each merged-on-green) and re-arm the chain (~15 min) before ending.
```

## Notes

- This is the generic §2b-template failsafe shape (superbot
  `docs/planning/round3-dispatch-part4-brief-2026-07-10.md`), seat-armed — it
  SUPERSEDES v1's longer draft text (which carried an ORDER-001 "gate is
  untrustworthy" clause; that order merged via superbot-games PR #24, merge
  SHA `7d4c347`, so the clause is obsolete anyway). Regenerate-don't-fork:
  the deployed text above is canonical; v1's draft was never armed.
- The cron is the dead-man failsafe only; the pacemaker is the seat's
  one-shot/send_later continuation chain (Q-0265).
