# 2026-07-12 — ORDER 020: per-wake trigger-health check

> **Status:** `complete`

📊 Model: fable-5 · start 2026-07-12 ·
lane worker (ORDER 020, dispatched by the coordinator)

## Declared at open (born-red)

Build the per-wake trigger-health check per ORDER 020 (canonical spec: superbot
`docs/owner/trigger-health-order-2026-07-12.md`): `scripts/check_trigger_health.py`
(WEDGED-cron / DROPPED-one-shot / DEAD-chain / manager-failsafe / roster+snapshot
freshness, PASS-FAIL per invariant, nonzero exit on FAIL), per-trigger health folded
into `scripts/gen_roster.py` so the roster (Actions substrate) carries the record,
wake-ritual wiring in `docs/playbook.md` + the fleet-manager v3 prompts, proof runs
against the current snapshot AND a replay of the 2026-07-12 incident snapshot, then
the ORDER 020 DONE flip in `control/inbox.md` — in progress.

## Close-out

- **Deliverable 1 — `scripts/check_trigger_health.py`** (stdlib + sibling modules):
  six invariants, one PASS/FAIL line each, exit 1 on any FAIL — I1 WEDGED-cron
  (`enabled ∧ next_run_at < capture − 15min`), I2 DROPPED one-shot (enabled past
  `run_once_at`; QUEUED-vs-LOST flagged indistinguishable per the spec note), I3
  DEAD-chain (dropped tick + no future tick on the session; recovery line names
  `send_message` + the Q-0242 venue caveat), I4 manager-failsafe present + unwedged,
  I5 roster freshness (4h bar; stale = the regen cron may itself be wedged), I6
  snapshot freshness. `--selfcheck` (13 offline assertions, PASS), `--now` replay,
  `--advisory`.
- **Deliverable 2 — roster health record (spec step 2)**: `scripts/gen_roster.py`
  gained shared health primitives (`trigger_wedged` / `oneshot_dropped` /
  `health_report` / `snapshot_eval_time` / `attribute_lane`), a per-lane **Trigger
  health** column, a header summary line, and a fleet-wide **Trigger health** section
  — the record rides the Actions regen cron (second substrate, survives a CCR
  scheduler outage). gen_roster `--selfcheck` extended (health assertions) — PASS.
- **Capture-instant eval (measured design decision):** judging a snapshot at
  wall-clock fabricates wedges (the 11:25Z gen-14 snapshot read at 13:54Z
  false-wedges 7/9 healthy crons — the regen-PR merge lag), while the newest record
  stamp understates capture by 3h during the outage (a frozen scheduler writes
  nothing). Fix: NEW top-level `captured_at` stamp written at every export
  (telemetry/README.md recipe step 3), with a labeled conservative fallback ladder
  in `snapshot_eval_time`.
- **Wake wiring (stateless):** playbook **R26** (procedure + WHY); verify lines in
  `docs/prompts/v3/per-project/fleet-manager-startup.md` +
  `fleet-manager-custom-instructions.md`; `projects/fleet-manager/`
  coordinator-prompt.md + instructions.md byte-synced with a delta stamp comment.
  `docs/ROUTINES.md` deliberately NOT edited — kit-owned, regenerated on every
  upgrade (last at #123); its "Scheduler health" doctrine already teaches the wedge
  signature this script mechanizes.
- **Proof run A (live, committed gen-14 snapshot, eval 11:12Z record-stamp basis):
  FAIL 4/6** — REAL findings, hand-verified against the raw records: game-lab
  failsafe `trig_01JD1t7rD5jUCqkJQJaNCi3E` wedged (next frozen 10:50Z, 22m past at
  capture), 6 dropped-or-queued one-shots across 5 sessions (oldest due 09:10Z), 2
  DEAD chains (`session_014Z1fPG7Wa6VHprJqLcux4f` substrate-kit,
  `session_01SphTJEnN1PYjYZhHNWoJik`), snapshot 7h stale; manager failsafe + roster
  freshness PASS. Recorded in control/status.md for the next wake to act on.
- **Proof run B (incident replay, snapshot `4111da4` @ 06:33Z, `--now` pin):
  FAIL 5/6** — the spec's done-when: 6 WEDGED crons incl. venture-lab money-seat
  (frozen 04:06Z), kit-lab loop (frozen 06:08Z) and the manager's own failsafe
  (04:31Z); 6 dropped one-shots; 4 DEAD chains each naming its `send_message`
  recovery. The 6-hour silent outage is now a single-wake catch.
- **Records:** ORDER 020 DONE flip appended to `control/inbox.md` (grammar-validated
  against the kit's inbox gate locally, exit 0); `control/status.md` orders roll +
  trigger-health line updated.

💡 Session idea: `gen_roster.py`'s LANES registry has no `game-lab` entry, so the
game-lab failsafe wake (`trig_01JD1t7rD…`, the one REAL wedge in proof run A)
attributes to "(unattributed)" — the seat exists (v3 prompts, per-project package)
but is invisible to lane attribution. Add a registry-only `game-lab` LANES row (or
fold it under pokemon-mod-lab/gba-homebrew as a parent seat) so the next wedge names
its seat instead of "(unattributed)" — attribution is what turns a flag into a
recovery target.

⟲ Previous-session review: the midday staleness sweep (#113) captured a
high-quality 832-trigger snapshot and even counted the enabled/dropped split — but
it read the registry WITHOUT judging it: 6 one-shots already 2h+ past due and a
wedged game-lab failsafe sat in the very JSON it committed, unflagged (the same
watching-gap ORDER 020 closes). Improvement adopted here: the snapshot now carries
`captured_at` so any later reader can judge it at the right instant; systemic
improvement to carry forward: sweep sessions should treat "data captured" as
incomplete until a checker has GRADED the capture — commit the verdict, not just
the export.
