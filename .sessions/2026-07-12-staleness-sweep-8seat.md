# 2026-07-12 — staleness sweep: first 8-seat registry sweep

> **Status:** `complete`

📊 Model: fable-5 · start 2026-07-12 ·
oversight boot worker (staleness sweep)

## Declared at open (born-red)

Staleness sweep of the fleet — first sweep under the new 8-seat registry
(projects/): trigger snapshot export, roster regen, per-seat
FRESH/STALE/DARK/DEAD verdicts, research doc.

## Close-out

Shipped on PR #105 (parked READY on green — merge authority denied for this
session; the manager records that separately):

- `telemetry/triggers-snapshot.json` refreshed: 783 triggers (8 MCP pages,
  783 unique ids).
- Roster regen generation #12 (`gen_roster.py` → roster.md,
  owner-queue-candidates.md, evidence-index.md); `check_roster_freshness.py`
  exit 0.
- Sweep report `docs/research/2026-07-12-staleness-sweep-8seat.md` (+ README
  link): 14 repos across 8 seats — roll-up 7/8 seats FRESH; **superbot-world
  STALE** (superbot-games heartbeat contradicted: its 5 "parked for owner
  merge" PRs all merged 20:25–20:43Z, HEAD moved 8 merges to `5ddfbee`, new
  PRs #59/#60 unmentioned); trading-strategy FRESH-borderline (drifts STALE
  ~2026-07-14 if parked PR #64 stays unmerged). 9-item needs-attention
  shortlist for the manager, headed by ⚑ HOT venture-lab PR #51 (unwatermarked
  owner photos publicly downloadable since 2026-07-11T18:24Z).
- Roster cross-check: 8 verdict mismatches (roster age-based STALE vs sweep
  claims-verified FRESH) — noted in the report, tables left untouched.
- `control/status.md` re-stamped 2026-07-12T03:56:06Z with the sweep record.

## 💡 Session idea

Staleness/oversight tooling should key on **required-check conclusions**, not
workflow-run conclusions: superbot-next's `golden-parity` workflow is
red-by-design on every main push (non-required `report` job stays red until
full parity while the required gate job is green), so any sweep or roster
logic reading workflow-run `conclusion` will falsely flag that repo every
single time. Keying on the required-check set makes the false positive
structurally impossible.

## ⟲ Previous-session review

The overnight registry-rebuild/heartbeat session (newest prior card:
2026-07-11-heartbeat-2350.md, PR #97) landed the 8-seat `projects/` registry
chain cleanly and left an accurate succession trail — this sweep booted off
it without friction. Miss: the manager heartbeat it shipped omitted open PR
#103 (prompts v3.1), its own program's major in-flight deliverable, so a
reader of `control/status.md` at main HEAD had no pointer to it (this sweep's
needs-attention item 7). Improvement: heartbeat updates should enumerate the
session's/program's own open PRs at stamp time — a one-line `open-prs:` field
in the heartbeat would make the omission impossible.
