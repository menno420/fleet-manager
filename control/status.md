---
updated: 2026-07-17T07:53Z
kit_version: 1.17.0
seat: fleet-manager (manager)
wake: owner-actions-0717 — built docs/owner-actions-2026-07-17.md, a live-verified fleet-wide owner-action overview (2 merges / 12 flips / 5 decisions / 6 veto menus ~266 proposals); PR #279.
---

# Fleet Manager — status

Neutral heartbeat. Facts + pointers only. Orders live in `control/inbox.md`; asks in `docs/owner-queue.md`; sweep detail in `docs/fleet-triage.md`.

## Routine state
- Overnight run recorded: `docs/fleet-triage.md` → **`## 2026-07-17 · overnight run analysis`** (run split + two stall-class incidents: decision-freeze, draft-parking; PR-cited).
- Trigger snapshot: last full export **captured_at 2026-07-17T00:34:34Z** (22 pages / 2166 records / 20 enabled). `check_trigger_health.py` last verdict **PASS — 8/9 green, 1 WARN** (exit 0); I6 SNAPSHOT-FRESH aging vs 4h bar — refresh `list_triggers` before acting.
- FM failsafe cron `30 */2 * * *` — `trig_01An9YmU3KC1kLhB5c9cv4Ax` ("Fleet Manager failsafe wake", enabled, coordinator-bound). I4 MANAGER-FAILSAFE PASS.
- Roster: Gen #76 (roster-regen.yml, PR #276). I5 ROSTER-FRESH — verify age at wake.
- I8 DUPLICATE-CRON **WARN ×4** — sibling-seat failsafe pairs (SuperBot 2.0, SuperBot World, Venture Lab, Websites) persist post-cutover; report-only, no ids touched (keep-OLDEST is a sibling-lane / orphan-sweep call, not this seat's to action).

## PRs
- **#277 (this session)** — record 2026-07-17 overnight run incidents in fleet-triage — landing on green; born-red card holds substrate-gate until flipped `complete`, then merge-on-green.yml lands it.
- Merged today on main: #271 (EAP project-recreation runbook), #272 (roster-regen Gen #74), #273 (overnight plan-menu — 25-proposal fleet-manager seat menu), #274 (roster-regen Gen #75), #275 (night trigger-telemetry refresh), #276 (roster-regen Gen #76).
- fleet-manager open PRs otherwise: none.

## Fleet (last sweep ~15:00Z + overnight analysis 2026-07-17 — detail in docs/fleet-triage.md)
- Overnight producers (merged output): 10 seats; idea-engine ↔ sim-lab ran the proposal/verdict pipeline to V104 (last landing 06:20Z).
- INCIDENT decision-freeze: superbot-next seat idled after ~23:00Z (froze on #499/#500 consent instead of parking those PRs; resumed AM after owner contact).
- INCIDENT draft-parking: gba-homebrew (10 unmerged drafts) + pokemon-mod-lab (2 parked) — night output exists, none landed.
- Quiet: superbot-mineverse (no wake since ORDER 010, 2026-07-16); product-forge (frozen by design).
- STALE by design: superbot-games, superbot-idle (FROZEN); product-forge (archived, owner OA-003).

## Open work / blockers
- ORDER 047 & 048 (P0, `new`): lane fan-out leg unfinished — 0 lane inboxes cite them. Cross-repo lane-inbox writes classifier-walled on relayed authority → owner-live venue unlock needed.
- ORDER 049: absent at HEAD — prior coordinator session classifier-blocked before landing; text unrecoverable from tree. Awaits owner paste in coordinator chat.
- PR-landing audit (2026-07-16, `docs/pr-landing-audit-2026-07-16.md`) owner-only landings recorded in `docs/owner-queue.md`: websites #359 (OQ-WEBSITES-359-MANUAL-MERGE), pokemon-mod-lab #87 (OQ-POKEMON-87-CONFLICT-DISPOSITION), ready-flip trio #153/#145/#149 (OQ-READY-FLIP-TRIO-0716).
- E#68 (OQ-THIN-LANE-DISPATCH-2026-07-16): owner live-authorized the batch; superbot-mineverse ORDER 010 landed (PR #118); remaining lanes re-blocked by classifier, dispatch session parked on a pending permission prompt.
- I8 DUPLICATE-CRON ×4: keep-OLDEST disposition per cutover intent is a sibling-lane call (verify each live before deleting the newer id); NOT actioned this wake.
- EAP wind-down: ends 2026-07-21 17:00 PT; recreation plan in docs/project-recreation-runbook.md; seat state is repo-resident so nothing is lost.

## Baton — next 2 tasks
1. Owner executes docs/owner-actions-2026-07-17.md via a hub session (start with gba #153 flip).
2. EAP project recreation + orphan-trigger sweep (per `docs/project-recreation-runbook.md` §2/§5; cutover 2026-07-21 17:00 PT) — match the fresh snapshot against the failsafe-id table, delete only ids attributed to stopped seats; collapse the 4 I8 dup pairs (keep-OLDEST) after verifying each live; verify each recreated seat's v3.7 prompt paste + failsafe cutover.
