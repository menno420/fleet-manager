<!-- v1 · 2026-07-11 · fleet-manager projects registry -->
# superbot-retro — failsafe wake trigger — DEPLOYED + REGISTRY-VERIFIED

> Part 4 of the superbot-retro package. **Status: ARMED + LIVE** — armed
> 2026-07-11T01:16:16Z, bound to the retro coordinator session. This file is
> the registry's byte-checkable record of the STORED prompt — per registry
> doctrine, failsafe prompts carry NO in-band version stamp so the block
> below can be byte-matched against `list_triggers` output directly.

## Deployed trigger (registry metadata, `list_triggers` 2026-07-11T13:17:24Z)

- **trigger id:** `trig_01Y99uDKNtKTz2EtRYPWZkGY`
- **name:** `superbot-retro failsafe wake`
- **cron_expression:** `50 */2 * * *` (even hours :50 — lane stagger;
  mineverse runs `20 */2`, manager `30 */2`, games `15 */2`, idle `45 */2`)
- **enabled:** true
- **persistent_session_id:** `session_01BqCRbGYGeo97sFxMJHzu1e` (the retro
  coordinator session; persist_session true)
- **created (armed):** 2026-07-11T01:16:16.782484Z · created_via `meta_mcp` ·
  never updated since creation
- **last_fired_at:** 2026-07-11T12:50:20.323986Z · next_run_at
  2026-07-11T14:50:00Z at extraction
- **environment_id:** `env_014P62UXP7cuK1bPPWWzg521` (shared with both
  hourly child-lane wakes — see `triggers.md`)

## The stored prompt text

VERBATIM-FROM-REGISTRY · extracted 2026-07-11T13:17:24Z

```
FAILSAFE WAKE (retro-games, Q-0265): if your send_later continuation chain is alive, verify that in one line and end. If it stalled, resume the work loop (sync both repos' HEAD -> inboxes -> slice after slice, each merged-on-green) and re-arm the chain (~15 min) before ending.
```

## Notes

- Byte-identical to the founding package's §2 step-3 "prompt EXACTLY" block
  (superbot PR #1972 @ `10a7486`,
  `docs/planning/round3-founding-package-games-retro-2026-07-11.md`) — the
  seat armed exactly what its founding brief specified; note the two-repo
  phrasing ("sync both repos' HEAD -> inboxes"), unique among fleet
  failsafes. Cron is the dead-man failsafe (Q-0265). Registry negative
  finding: NO "superbot-retro chain link" one-shots appear in the
  549-record sweep — the observable drumbeat is the pair of hourly
  child-lane wakes (`triggers.md`), not a recorded send_later chain.
