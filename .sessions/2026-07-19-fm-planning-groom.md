# 2026-07-19 · fm planning pass — groom night-shift ideas into next executable slices

> **Status:** `in-progress`

About to happen (declared born-red): planning slice for the coordinator seat, per the
owner's universal continue prompt (~07:45Z — when executable work is drained, PLAN).
Survey the ~8 💡 ideas the night shift recorded across the 2026-07-18/19 `.sessions/`
cards; write `docs/planning/2026-07-19-next-slices.md` — an honest, ranked list of
next executable slices for this seat (what · why it earns its place · effort S/M ·
lane fm-buildable vs routed), dropping any idea that doesn't genuinely earn a slice;
refresh the `control/status.md` heartbeat + baton with the top picks as the standing
"next slice" queue. Docs-only; no trigger-MCP calls from this venue; no sibling repo
touched.

- **📊 Model:** fable-5 · high · docs-only — planning slice (idea grooming + next-slices plan + heartbeat baton)

## What shipped (PR #349)

- `docs/planning/2026-07-19-next-slices.md` — the ranked next-slices plan. Top 3
  (the standing queue): (1) `check_lane_liveness.py` seat-chain stall detector
  (tonight's websites 036 silence was caught ~4h late by a human read) ·
  (2) regen-window skip detector in `check_roster_freshness.py` (00:40Z + 02:40Z
  windows both silently dropped) · (3) seat-provenance-aware I8 remedy in
  `check_trigger_health.py` (the keep-oldest heuristic contradicted the correct
  SBW escalation). Below the line: fence emitter, capabilities-grammar linter.
  Dropped/parked/routed with reasons: `post_capture_deltas` (superseded by the
  routine-claims fence), `gen_hub_queue_baton.py` (inputs don't exist fleet-wide
  yet), bake auto-supersede (websites-lane work, ORDER 036 follow-up stream).
- `docs/planning/README.md` — index row for the plan.
- `control/status.md` — `updated:` → 07:28Z; "~07:2xZ planning pass" facts
  subsection; baton refreshed to 3 items: (1) hub queue unchanged (forge #29 +
  fm #344 + `OQ-SBW-DUP-FAILSAFE`), (2) next executable slices = the top 3 above,
  (3) watches unchanged (websites 036 stall, odd-hour cron proof post-#344, I6
  snapshot refresh due ~10:15Z). Routine state untouched; no trigger-MCP calls.
- `.substrate/guard-fires.jsonl` — telemetry delta committed (do-not-revert).

## Enders

- 💡 **Session idea (dedup-checked — `docs/ideas/` 16 files + the 2026-07-18/19
  cards' 💡 set: apparatus-provenance, current-state-freshness, fence + emitter,
  post_capture_deltas, auto-supersede, capabilities-grammar, regen-window,
  lane-liveness, tripwire-checker, I8-provenance, snapshot-seat-coverage,
  owner-steps-freshness, reconcile-routing, cite-the-live-HEAD, baton aggregator —
  none cover idea *capture lifecycle*; novel):** a `gen_idea_backlog.py` harvester.
  This planning pass had to hand-grep ~25 session cards for 💡 blocks because
  card-ideas have no aggregated home — `docs/ideas/` holds only the 07-09/10 lane
  seeds and none of the night shift's tooling ideas. A stdlib script could harvest
  `💡` blocks from `.sessions/*.md` into a generated, dated backlog index (idea ·
  source card · groomed-into pointer or `ungroomed`), and advisorily flag
  card-ideas older than N days never groomed into a plan — so the next grooming
  pass starts from a machine-built candidate list and no card-idea silently rots.
- ⟲ **Previous-session review (PR #347, the 06:15Z snapshot + SBW escalation):**
  it honored the 00:06Z tripwire exactly as armed (escalated on the second
  duplicated capture, not earlier, not never), cited both captures, and — best —
  inverted the checker's seat-blind keep-oldest remedy on provenance grounds with
  the honest note why, which is the direct evidence behind this plan's slice #3.
  One miss worth naming: the tripwire only fired because a human re-read the
  prose watch item — the 00Z card's tripwire-checker idea (condition-over-snapshot
  grammar) remains the mechanization gap; it sits adjacent to slice #1
  (lane-liveness) and should be re-ranked when the top-3 queue drains. Workflow
  improvement this surfaces: checker remedy lines are heuristics and records
  slices now know to re-derive them — slice #3 turns that session-lore into code.
- 📋 **Doc-audit:** everything durable has a home — the ranked plan + drop
  rationale in `docs/planning/2026-07-19-next-slices.md` (indexed in the planning
  README), the standing queue mirrored in the `control/status.md` baton, and this
  card records the pass. No chat-only residue; no owner-queue changes needed
  (hub items and watches carried unchanged).
- 🔥 **Guard-fires:** `bootstrap.py check --strict` ran twice (born-red HOLD
  pre-flip by design → clean at flip); appended guard-fire telemetry committed
  with the session (do-not-revert).
- 🧹 **Claim:** `control/claims/claude-fm-planning-groom.md` deleted in the flip
  commit (`bootstrap claim fm-planning-groom --delete`).
