---
updated: 2026-07-16T15:03:57Z
kit_version: 1.17.0
seat: fleet-manager (manager)
wake: wake-0716-pm oversight sweep (PR #262)
---

# Fleet Manager — status

Neutral heartbeat. Facts + pointers only. Orders live in `control/inbox.md`; asks in `docs/owner-queue.md`; sweep detail in `docs/fleet-triage.md`.

## Routine state
- FM failsafe cron `30 */2 * * *` — coordinator session `cse_01WwuStAe6JuMatMRdiA8Zsi` is verifying/re-arming it separately this turn. (I6 snapshot was 8.1h stale at the 06:47Z export; not re-captured here.)
- Roster: Gen #70, generated 2026-07-16T14:35Z (0.3h — fresh). roster-regen.yml healthy (Gen #66→#70 landed 03:49→14:35Z).
- Trigger health (last export 06:47Z): I6 SNAPSHOT-FRESH FAIL + I8 DUPLICATE-CRON WARN ×4 (superbot-2.0/superbot-world/venture-lab/websites old failsafe crons still enabled) — cutover-seat disposition, coordinator lane.

## PRs
- **#262 (this session)** — wake-0716-pm oversight sweep; born-red (in-progress card holds substrate-gate), flips `complete` last → merge-on-green.yml lands it. No blocker.
- fleet-manager open PRs otherwise: **none**. Night PRs #253–#256 + Gen-roster #257–#261 all terminal on main.

## Fleet (sweep ~15:00Z — detail in docs/fleet-triage.md)
- FRESH today: idea-engine, trading-strategy, substrate-kit, websites, sim-lab.
- Wake candidates (~12–14h, active): superbot-next, gba-homebrew, superbot-mineverse, venture-lab.
- STALE by design: superbot-games, superbot-idle (FROZEN); product-forge (archived, owner OA-003).
- DARK: superbot-plugin-hello (scaffold), pokemon-mod-lab (private, skip).

## Open work / blockers
- ORDER 047 & 048 (P0, `new`): lane fan-out leg unfinished — 0 lane inboxes cite them. Cross-repo lane-inbox writes classifier-walled on relayed authority → owner-live venue. Several coordinator-project sessions parked on the same permission-classifier walls this turn (denial detail in PR #262 body).
- ORDER 049: absent at HEAD — prior coordinator session classifier-blocked before landing; text unrecoverable from tree. Flagged to coordinator.
- owner-queue: PR #227 "click merge" item closed this sweep (merged 2026-07-15T22:47:58Z). ~57 items remain; 8 seats carry owner-ask blocks → candidate consolidated owner pass.

## Baton — next 2 tasks
1. Recover ORDER 049 text + land ORDER 047/048 lane fan-out via owner-live venue (classifier wall).
2. Next R26 trigger-health sweep on a fresh export (clears I6); I8 duplicate-cron disposition — keep-NEWEST per cutover intent, verify keeper before deleting.
