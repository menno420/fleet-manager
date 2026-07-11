<!-- v1 · 2026-07-11 · fleet-manager projects registry -->
# superbot-retro — hourly child-lane wake triggers — DEPLOYED + REGISTRY-VERIFIED

> Companion to Part 4 of the superbot-retro package: the TWO hourly
> fresh-session wakes the repo-less seat drives its child lanes with (both
> named "(ORDER 002)"; created ~20 min after the seat's failsafe, in the same
> environment `env_014P62UXP7cuK1bPPWWzg521`). Unlike the failsafe these are
> NOT session-bound — each fire creates a fresh session against the listed
> sources. Per registry doctrine the stored prompts carry NO in-band stamp so
> each block below byte-matches `list_triggers` output directly.
>
> **Registry-truth delta:** the 2026-07-10 gba/pokemon packages recorded
> "`0 */2` spec'd — NOT armed" and their inbox ORDER 002s as unexecuted /
> superseded. Since 2026-07-11T01:36Z that is stale — these hourly wakes ARE
> armed and firing (last_fired values below). Regenerating those two
> packages is the flagged follow-up in `meta.md`.

## 1. gba-homebrew hourly wake (registry metadata, `list_triggers` 2026-07-11T13:17:24Z)

- **trigger id:** `trig_0137SkvhXEJvwepX8aVNkcSn`
- **name:** `gba-homebrew hourly wake (ORDER 002)`
- **cron_expression:** `0 * * * *`
- **enabled:** true
- **session binding:** none — fresh-session-per-fire (no
  persist_session/persistent_session_id stored)
- **created:** 2026-07-11T01:36:30.814268Z · updated
  2026-07-11T11:03:12.446610Z · created_via `meta_mcp`
- **last_fired_at:** 2026-07-11T13:02:08.142904Z · next_run_at
  2026-07-11T14:01:40Z at extraction
- **environment_id:** `env_014P62UXP7cuK1bPPWWzg521`
- **sources:** `https://github.com/menno420/pokemon-mod-lab`,
  `https://github.com/menno420/gba-homebrew` (BOTH repos — the wake's
  sessions can read/write either; the stored record is the evidence the
  seat's environment attaches both)
- **outcomes (branches):** `claude/happy-gauss` (pokemon-mod-lab),
  `claude/gracious-feynman` (gba-homebrew)
- **notifications:** push/email/slack all false ·
  **autofix_on_pr_create:** false

### Stored prompt text — VERBATIM-FROM-REGISTRY · extracted 2026-07-11T13:17:24Z

```
Read control/inbox.md at HEAD and run the standing ritual from your instructions.
```

## 2. pokemon-mod-lab hourly wake (registry metadata, `list_triggers` 2026-07-11T13:17:24Z)

- **trigger id:** `trig_01BTJjkMVMKtWPjuYe7643Hi`
- **name:** `pokemon-mod-lab hourly wake (ORDER 002)`
- **cron_expression:** `30 * * * *`
- **enabled:** true
- **session binding:** none — fresh-session-per-fire (no
  persist_session/persistent_session_id stored)
- **created:** 2026-07-11T01:37:07.905207Z · updated
  2026-07-11T10:51:08.321534Z · created_via `meta_mcp`
- **last_fired_at:** 2026-07-11T12:36:31.364929Z · next_run_at
  2026-07-11T13:36:06Z at extraction
- **environment_id:** `env_014P62UXP7cuK1bPPWWzg521`
- **sources:** `https://github.com/menno420/pokemon-mod-lab`
- **outcomes (branches):** `claude/eloquent-newton` (pokemon-mod-lab)
- **notifications:** push/email/slack all false ·
  **autofix_on_pr_create:** false

### Stored prompt text — VERBATIM-FROM-REGISTRY · extracted 2026-07-11T13:17:24Z

```
Track A (menno420/pokemon-mod-lab): Read control/inbox.md at HEAD and run the standing ritual from your instructions.
```

## Notes

- The "(ORDER 002)" names echo each repo's inbox ORDER 002 (self-arm hourly
  wake), which the 2026-07-10 packages recorded as unexecuted — the deployed
  crons (`0 * * * *` / `30 * * * *`, hourly) also differ from those
  packages' spec'd `0 */2` cadence. The registry records what RUNS; the
  reconciliation belongs to the gba/pokemon package regeneration follow-up.
- The pokemon prompt's "Track A" prefix is part of the stored text —
  reproduced byte-true above.
