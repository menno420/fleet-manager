---
updated: 2026-07-16T21:56:32Z
kit_version: 1.17.0
seat: fleet-manager (manager)
wake: overnight-plan-menu-0716 — shipped docs/planning/overnight-menu-2026-07-17.md (25-proposal veto-ready seat menu); PART-1 records sweep
---

# Fleet Manager — status

Neutral heartbeat. Facts + pointers only. Orders live in `control/inbox.md`; asks in `docs/owner-queue.md`; sweep detail in `docs/fleet-triage.md`.

## Routine state
- FM failsafe cron `30 */2 * * *` — replacement `trig_01An9YmU3KC1kLhB5c9cv4Ax` PRESENT ("Fleet Manager failsafe wake", enabled, bound to coordinator session `session_01WwuStAe6JuMatMRdiA8Zsi`), next fire **2026-07-16T16:33Z**. Old `trig_01UNjDKaaiGuUTvyfQGLKLrn` ABSENT (deleted). I4 MANAGER-FAILSAFE PASS.
- Roster: Gen #74 at HEAD (roster-regen.yml #272). I5 ROSTER-FRESH PASS.
- Trigger health: last fresh export **captured_at 2026-07-16T15:26:43Z** (21 pages / 2033 records / 19 enabled), `check_trigger_health.py` **PASS — 8/9 green, 1 WARN**; I6 snapshot ~6.3h stale (coordinator-bound refresh). I8 DUPLICATE-CRON **WARN ×4** persists on sibling seats post-cutover (report-only, no ids touched).

## PRs
- **#273 (this session)** — overnight plan-menu (menu + current-state link + late-evening triage sweep) — landing tonight on green; born-red card holds substrate-gate until flipped `complete`, then merge-on-green.yml lands it.
- Merged today on main: **#262** (wake-0716-pm sweep), **#263** (fix227prov follow-up), **#264** (R26 trigger-snapshot refresh), **#265** (fleet-wide PR-landing audit → `docs/pr-landing-audit-2026-07-16.md`), **#266** (stale-claim sweep from #262/#263 lane), **#268** (PR-landing-audit owner actions + item-68 progress note). Automated roster regen **#272** merged (Gen #74, HEAD).
- fleet-manager open PRs otherwise: none.

## Fleet (last sweep ~15:00Z — detail in docs/fleet-triage.md; PR-landing detail in docs/pr-landing-audit-2026-07-16.md; not re-run this wake)
- FRESH: idea-engine, trading-strategy, substrate-kit, websites, sim-lab.
- Wake candidates (~12–14h, active): superbot-next, gba-homebrew, superbot-mineverse, venture-lab.
- STALE by design: superbot-games, superbot-idle (FROZEN); product-forge (archived, owner OA-003).
- DARK: superbot-plugin-hello (scaffold), pokemon-mod-lab (private, skip).

## Open work / blockers
- ORDER 047 & 048 (P0, `new`): lane fan-out leg unfinished — 0 lane inboxes cite them. Cross-repo lane-inbox writes classifier-walled on relayed authority → owner-live venue unlock needed.
- ORDER 049: absent at HEAD — prior coordinator session classifier-blocked before landing; text unrecoverable from tree. Awaits owner paste in coordinator chat.
- PR-landing audit (2026-07-16, `docs/pr-landing-audit-2026-07-16.md`) surfaced owner-only landings now recorded in `docs/owner-queue.md`: websites #359 (OQ-WEBSITES-359-MANUAL-MERGE), pokemon-mod-lab #87 (OQ-POKEMON-87-CONFLICT-DISPOSITION), ready-flip trio #153/#145/#149 (OQ-READY-FLIP-TRIO-0716).
- E#68 (OQ-THIN-LANE-DISPATCH-2026-07-16): owner live-authorized the batch; superbot-mineverse ORDER 010 landed (PR #118); remaining lanes re-blocked by classifier, dispatch session parked on a pending permission prompt (progress note in owner-queue).
- I8 DUPLICATE-CRON ×4: keep-OLDEST disposition per cutover intent is a sibling-lane call (verify each live before deleting the newer id); NOT actioned this wake.
- EAP wind-down: ends 2026-07-21 17:00 PT; recreation plan documented in docs/project-recreation-runbook.md; recreation executes control-plane-side (owner + coordinators), seat state is repo-resident so nothing is lost.

## Baton — next 2 tasks
1. Owner veto pass on the overnight menu — `docs/planning/overnight-menu-2026-07-17.md` (25 proposals; recommended first-build set S3/S5/S9).
2. EAP project recreation + orphan-trigger sweep tomorrow (per `docs/project-recreation-runbook.md` §2; cutover 2026-07-21 17:00 PT) — match live `list_triggers` against the failsafe-id table, delete only ids attributed to stopped seats; verify each recreated seat's v3.7 prompt paste + failsafe cutover.
