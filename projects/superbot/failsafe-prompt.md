<!-- v1 · 2026-07-10 · fleet-manager projects registry -->
# superbot — failsafe / wake text: NONE by design

**NO standing wake by design (Q-0264, 2026-07-10):** Q-0264 superseded the
hub-seat idea — the Q-0262.8 pick of superbot as a hub-executor seat was ⚑
flagged most-vetoable and the veto arrived (Q-0264 item 2/5) — so there is no
persistent superbot coordinator session for a cron to fire into, and no
send_later pacemaker chain to back up. The self-firing reconciliation loop
already covers the repo's only recurring duty: the ROUTINE_PAT issue-based
Q-0107 machinery (`scripts/check_reconciliation_due.py` +
`.github/workflows/reconciliation-trigger.yml` open a `reconcile` issue at
every 30-PR band boundary, which fires the "superbot docs reconciliation"
routine; confirmed live — the band-#1950 pass ran off issue #1951, per
`docs/current-state.md` "Last updated"). Everything else is owner-started
sessions (part 2 of this package) plus the games program / Idea Engine
harvesting per Q-0264. **If the owner ever seats a hub Project,** do not
resurrect the vetoed design ad hoc — start from the gen-3 deployment
standard's born-continuous template (superbot
`docs/planning/gen3-deployment-standard-2026-07-10.md` §2, Q-0265 operating
model: send_later pacemaker + a `"<seat> failsafe wake"` dead-man cron on the
core-seat stagger) and write the seat's package into this folder then.
