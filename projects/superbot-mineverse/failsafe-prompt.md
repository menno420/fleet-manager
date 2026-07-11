<!-- v1 · 2026-07-11 · fleet-manager projects registry -->
# superbot-mineverse — failsafe wake trigger — DEPLOYED + REGISTRY-VERIFIED

> Part 4 of the superbot-mineverse package. **Status: ARMED + LIVE** — the
> seat SELF-ARMED this trigger during its own boot (recorded in the seat's
> `control/status.md` § "Routine + chain (verbatim record)": failsafe
> `trig_01K8xmAKYS5S2HLy1HPANM7j` cron `20 */2 * * *`, unchanged since boot).
> This file is the registry's byte-checkable record of the STORED prompt —
> per registry doctrine, failsafe prompts carry NO in-band version stamp so
> the block below can be byte-matched against `list_triggers` output directly.

## Deployed trigger (registry metadata, `list_triggers` 2026-07-11T13:17:24Z)

- **trigger id:** `trig_01K8xmAKYS5S2HLy1HPANM7j`
- **name:** `superbot-mineverse failsafe wake`
- **cron_expression:** `20 */2 * * *` (even hours :20 — lane stagger; retro
  runs `50 */2`, manager `30 */2`, games `15 */2`, idle `45 */2`)
- **enabled:** true
- **persistent_session_id:** `session_017yrng4qx2LcLNqKb5AGoe8` (the
  mineverse coordinator session; persist_session true)
- **created (armed):** 2026-07-11T01:30:43.107380Z · created_via `meta_mcp` ·
  never updated since creation
- **last_fired_at:** 2026-07-11T12:20:34.711523Z · next_run_at
  2026-07-11T14:20:00Z at extraction
- **environment_id:** `env_01R7HZmxtsoGMKH4ncTJCWyk`

## The stored prompt text

VERBATIM-FROM-REGISTRY · extracted 2026-07-11T13:17:24Z

```
FAILSAFE WAKE (mining-browsergame, Q-0265): if your send_later continuation chain is alive, verify that in one line and end. If it stalled, resume the work loop (sync HEAD -> inbox -> slice after slice, each merged-on-green) and re-arm the chain (~15 min) before ending.
```

## Notes

- Byte-identical to the founding package's §2 step-3 "prompt EXACTLY" block
  (superbot PR #1972 @ `10a7486`,
  `docs/planning/round3-founding-package-mining-web-2026-07-11.md`) — the
  seat armed exactly what its founding brief specified. Generic §2b-template
  failsafe shape; the cron is the dead-man failsafe only, the pacemaker is
  the seat's send_later/one-shot continuation chain (Q-0265) — the registry
  shows 20 spent "superbot-mineverse chain link" one-shots (01:32Z–12:23Z),
  proving the chain fires and re-arms.
