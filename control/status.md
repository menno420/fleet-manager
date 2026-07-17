---
updated: 2026-07-17T00:42:26Z
kit_version: 1.17.0
seat: fleet-manager (manager)
wake: night-snapshot-0717 — R26 trigger-telemetry refresh: fresh full list_triggers export + trigger-health verdicts (8/9 green, I8 WARN×4)
---

# Fleet Manager — status

Neutral heartbeat. Facts + pointers only. Orders live in `control/inbox.md`; asks in `docs/owner-queue.md`; sweep detail in `docs/fleet-triage.md`.

## Routine state
- Trigger snapshot: fresh full export **captured_at 2026-07-17T00:34:34Z** (22 pages / 2166 records / 20 enabled; +133 new / -0 gone vs prior 2026-07-16T15:26:43Z). `check_trigger_health.py` **PASS — 8/9 green, 1 WARN** (exit 0). I6 SNAPSHOT-FRESH now PASS (0.0h; cleared prior ~6.3h WARN).
- FM failsafe cron `30 */2 * * *` — `trig_01An9YmU3KC1kLhB5c9cv4Ax` ("Fleet Manager failsafe wake", enabled, coordinator-bound), next fire **2026-07-17T00:36:53Z**. I4 MANAGER-FAILSAFE PASS.
- Roster: Gen #75 (roster-regen.yml, PR #274), 1.1h old. I5 ROSTER-FRESH PASS.
- I8 DUPLICATE-CRON **WARN ×4** — sibling-seat failsafe pairs (SuperBot 2.0, SuperBot World, Venture Lab, Websites) persist post-cutover; report-only, no ids touched (keep-OLDEST is a sibling-lane / orphan-sweep call, not this seat's to action).

## PRs
- **#275 (this session)** — night trigger-telemetry refresh (snapshot + verdicts) — landing tonight on green; born-red card holds substrate-gate until flipped `complete`, then merge-on-green.yml lands it.
- Merged today on main: #271 (EAP project-recreation runbook), #272 (roster-regen Gen #74), #273 (overnight plan-menu — 25-proposal fleet-manager seat menu), #274 (roster-regen Gen #75).
- fleet-manager open PRs otherwise: none.

## Fleet (last sweep ~15:00Z — detail in docs/fleet-triage.md; PR-landing detail in docs/pr-landing-audit-2026-07-16.md; not re-run this wake)
- FRESH: idea-engine, trading-strategy, substrate-kit, websites, sim-lab.
- Wake candidates (~12–14h, active): superbot-next, gba-homebrew, superbot-mineverse, venture-lab.
- STALE by design: superbot-games, superbot-idle (FROZEN); product-forge (archived, owner OA-003).
- DARK: superbot-plugin-hello (scaffold), pokemon-mod-lab (private, skip).

## Open work / blockers
- ORDER 047 & 048 (P0, `new`): lane fan-out leg unfinished — 0 lane inboxes cite them. Cross-repo lane-inbox writes classifier-walled on relayed authority → owner-live venue unlock needed.
- ORDER 049: absent at HEAD — prior coordinator session classifier-blocked before landing; text unrecoverable from tree. Awaits owner paste in coordinator chat.
- PR-landing audit (2026-07-16, `docs/pr-landing-audit-2026-07-16.md`) owner-only landings recorded in `docs/owner-queue.md`: websites #359 (OQ-WEBSITES-359-MANUAL-MERGE), pokemon-mod-lab #87 (OQ-POKEMON-87-CONFLICT-DISPOSITION), ready-flip trio #153/#145/#149 (OQ-READY-FLIP-TRIO-0716).
- E#68 (OQ-THIN-LANE-DISPATCH-2026-07-16): owner live-authorized the batch; superbot-mineverse ORDER 010 landed (PR #118); remaining lanes re-blocked by classifier, dispatch session parked on a pending permission prompt.
- I8 DUPLICATE-CRON ×4: keep-OLDEST disposition per cutover intent is a sibling-lane call (verify each live before deleting the newer id); NOT actioned this wake.
- EAP wind-down: ends 2026-07-21 17:00 PT; recreation plan in docs/project-recreation-runbook.md; seat state is repo-resident so nothing is lost.

## Baton — next 2 tasks
1. Owner veto pass on the overnight menu — `docs/planning/overnight-menu-2026-07-17.md` (25 proposals; recommended first-build set S3/S5/S9).
2. EAP project recreation + orphan-trigger sweep (per `docs/project-recreation-runbook.md` §2/§5; cutover 2026-07-21 17:00 PT) — match this fresh 2026-07-17T00:34:34Z snapshot against the failsafe-id table, delete only ids attributed to stopped seats; collapse the 4 I8 dup pairs (keep-OLDEST) after verifying each live; verify each recreated seat's v3.7 prompt paste + failsafe cutover.
