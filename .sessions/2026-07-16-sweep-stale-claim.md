# 2026-07-16 — sweep-stale-claim (terminal-lane stale-claim housekeeping)

> **Status:** `complete`
> **Branch:** claude/sweep-stale-claim-0716pm

Swept the terminal-lane stale claim `control/claims/claude-wake-0716-pm-sweep.md` — its lane (PRs #262/#263) is merged/terminal, so the claim was dead by doctrine and only tripped the bootstrap advisory. Under fm ORDER 048 (decide/build/land-on-green; landing via merge-on-green.yml — this session does NOT self-arm or self-merge).

## What happened

- **Verified terminal:** live GitHub `get_pull_request` confirmed **#262 merged** 2026-07-16T15:07:03Z and **#263 merged** 2026-07-16T15:14:48Z (both `state: closed`, `merged: true`, merged by `github-actions[bot]`). The claim referenced the `claude/wake-0716-pm-sweep` branch = #262's lane; #263 was its same-wake follow-up. Neither PR open → safe to sweep.
- **Removed** `control/claims/claude-wake-0716-pm-sweep.md` (`git rm`). It was the only claim file besides the README, so `control/claims/` now holds just the doctrine README.
- **Verified green:** `python3 bootstrap.py check --strict` after the deletion.

## Enders

- **💡 Session idea:** give the claims checker a `claims-terminal-lane` signal — resolve each claim's backticked branch/scope token to its PR state at live GitHub and flag (or auto-prune) a claim whose lane PRs are all merged/closed, rather than waiting for the 72h `claims-stale` age horizon. A claim goes dead the instant its lane lands, not 72h later; keying on PR-terminal state kills the whiteboard note at exactly the right moment and removes the recurring "manual sweep of an obviously-dead claim" wake (this one). (Dedup-grepped `docs/ideas/` for claim/stale/sweep/terminal/expire — novel; complements the existing age-based `claims-stale` rather than duplicating it.)
- **📊 Model:** Claude Opus 4.x family · low · mechanical refactor
- **⟲ Previous-session review:** the trigger-snapshot-pm wake (PR #264) closed the I6 SNAPSHOT-FRESH FAIL cleanly and left an honest baton — it correctly refused to touch sibling-seat triggers for the I8 DUPLICATE-CRON warnings, flagging disposition as a sibling-lane call rather than acting outside its scope. Good scope discipline. What it surfaces for the system: its own ender named I6 staleness as a *predictable* recurring FAIL that rides whichever wake happens to notice — the same "obviously-dead thing waits for a manual wake to notice it" pattern this stale-claim sweep is an instance of. Both point at the same workflow improvement: cheap, targeted watchdog checks that catch predictable decay at its source (the `claims-terminal-lane` idea above) beat scheduling a human/agent wake to eyeball it.
