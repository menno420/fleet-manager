# 2026-07-18 · fm capability record + night-watch heartbeat

> **Status:** `complete`

About to happen: records slice — append a newly VERIFIED capability to
`docs/CAPABILITIES.md` (cross-repo lane-inbox ORDER writes via PR work end-to-end;
evidence: websites ORDER 036 / websites#433, landed 2026-07-18T21:19:37Z, merge sha
`5689537`), amend the superseded 2026-07-16 relayed-authority inbox-append wall entry
with a dated supersession note, and refresh `control/status.md` with tonight's
night-watch state (owner asleep ~21:25Z, standing directive, stretched pacemaker
cadence, baton). Docs-only, no sibling repo touched.

- **📊 Model:** Fable 5 · high · docs-only

## What shipped (PR #337)

- `docs/CAPABILITIES.md` — new 2026-07-18 append-log capability entry (grammar-matching,
  newest-first): cross-repo lane-inbox ORDER writes via the coordinator-seat PR route
  work end-to-end with zero classifier refusals (websites ORDER 036 → websites#433,
  landed by the websites landing workflow 2026-07-18T21:19:37Z, merge sha
  `5689537208d4277d9c8355897dad5c3210745207`). The 2026-07-16 "agent-side
  `control/inbox.md` ORDER appends on relayed authority" WALL got a dated
  **SUPERSEDED 2026-07-18** note inside its block (history kept, per the
  never-delete-history + never-record-limitations rules; the supersession marker is the
  exclusion shape `check_capabilities_wall_age.py` recognizes).
- `control/status.md` — heartbeat refreshed (`updated: 2026-07-18T21:32Z`): new
  "Night watch" section (owner asleep ~21:25Z; standing directive: watch projects,
  route where necessary, improve own repo; pacemaker ~30 min overnight,
  decide-and-flag; failsafe cron `30 */2` unchanged), ORDER-036/websites#433 + fm #335
  records, refreshed next-2-tasks baton (hub lands pokemon #98 + forge #29; ~22:00Z
  wake re-sweeps the 8 born-red in-flight PRs + roster/trigger-health + websites
  #422/ORDER-036 follow-through). Verified routine block kept intact — sanity-run:
  `verify_routine_state.py` still parses the edited heartbeat and reports the known
  capture-lag DRIFT exactly as its capture-instant honesty note predicts.
- `.substrate/guard-fires.jsonl` — telemetry delta from the strict-check run committed
  with the session (guard-fires swept: 7 records, all from this session's own check
  runs; do-not-revert rule honored).

## Gates

- `python3 bootstrap.py check --strict` → only the designed born-red HOLD pre-flip;
  advisory model-line warnings belong to an earlier session's card
  (`2026-07-18-fm-wake-oversight.md`), not this one — noted, not mine to rewrite.

## 💡 Session idea

**A `check_capabilities_grammar.py` advisory linter for the append log.** The
CAPABILITIES append log declares a five-field grammar (`- YYYY-MM-DD · capability|wall
· <venue> · finding · evidence · workaround`), but nothing enforces it, and
`check_capabilities_wall_age.py`'s own provenance header admits its parsing is
"best-effort text parsing over a hand-written living ledger, not a strict schema" —
so every hand-written entry (including this session's) risks quietly falling outside
the ager's wall/supersession detection. A stdlib linter that validates each append-log
bullet's leading date, kind token, and venue token against the declared grammar
(advisory, standalone, never merge-blocking) would keep the ledger machine-parseable
and give the S9 ager firm ground instead of heuristics. Dedup-checked `docs/ideas/`
(16 files) + recent session-card ideas (apparatus-provenance, current-state-freshness,
no-false-walls + its fleet mode, reconcile-routing, cite-the-live-HEAD, fill-dates,
registry-meta-stamp): those check *content* (staleness, false walls, citations); this
checks the ledger's *format* surface so the content checkers can trust it — novel and
distinct. (Not the forbidden trio: not auto-supersede, not post_capture_deltas, not
verify_routine_state.)

## ⟲ Previous-session review

**PR #335 (fm-verify-routine-state — `verify_routine_state.py`)** did the right
things: it converted a measured friction (a 20-page hand `list_triggers` pagination to
prove routine state after a hung call) into a one-command claimed-vs-actual diff with
a full provenance/reliability/kill-switch header; it accepted the flat-array export
shape that PR #334's review had flagged as hand-wrapping friction (fixing the adjacent
bug, not just its own case); and — best — its proof run was HONEST: it demonstrated
the DRIFT path on the real stale snapshot and explained the verdict as capture lag via
the built-in capture-instant honesty note rather than manufacturing a clean pass. I
re-ran it this session against my edited heartbeat: it parsed the new claims fine and
reported exactly the predicted capture-lag DRIFT — early ground-truth confirmation for
its unverified-reliability header. One improvement it surfaces: its C1/C3 verdicts
depend on the committed snapshot's freshness, and tonight's known-stale snapshot means
every run until the next refresh prints DRIFT that a reader must interpret via the
honesty note — the cheap next step is a `--refresh-required-age` flag (or exit-code
distinction) that separates "stale-capture DRIFT, refresh the export" from "live
drift, investigate", so a wake script can branch on it mechanically instead of reading
prose.

## Doc audit

Anything from this session not in its durable home? No — the capability + supersession
live in `docs/CAPABILITIES.md`, the night-watch state + baton in `control/status.md`,
the claim (`control/claims/claude-fm-capability-heartbeat.md`) rides this PR and is
the coordinator's to release at seat close per its own claim-lifecycle; PR #337 is the
session record. No sibling repo touched; no owner-queue change needed (no new
owner-only work discovered).
