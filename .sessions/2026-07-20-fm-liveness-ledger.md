# 2026-07-20 · fm build slice — lane-liveness ledger + transition diff

> **Status:** `complete`

About to happen (declared born-red): the committed lane-liveness ledger + `--diff`
idea (recorded on the #381 card). Each liveness run currently prints a table that
evaporates — lane-state transitions across runs (LIVE→STALLED, WAKING-IDLE
onset/recovery) are invisible unless a human diffs old outputs. Extend
`scripts/check_lane_liveness.py` with `--ledger [path]` (default
`telemetry/lane-liveness-ledger.jsonl`): append one JSON line per run
`{evaluated_at, snapshot_captured_at, lanes: {lane: {verdict, wake_state,
fires_since, age_hours}}}`; and `--diff` mode: compare the current run vs the
ledger's last entry — print TRANSITIONS (lane · old→new verdict/wake_state) + a
one-line headline (N transitions; recoveries vs degradations). Ground-truth demo:
run twice (seed entry + diff). Selfcheck extended; Q-0105 provenance note; seeded
first ledger entry committed (telemetry, like triggers-snapshot). Then
`control/status.md` baton advance. Claim
`control/claims/claude-fm-liveness-ledger.md` (deleted in the flip commit).
Decide-and-flag rationale: S/M, zero network beyond what the checker already
does, turns the checker into a time series. No trigger-MCP calls from this venue.

- **📊 Model:** fable-5 · high · feature build — extend verified checker, tooling+telemetry (Q-0105 provenance tier)

## What shipped (PR #386)

- `scripts/check_lane_liveness.py` — ledger + transition diff (Q-0105
  provenance block, kill-switch included). `--ledger [PATH]` (bare flag =
  `telemetry/lane-liveness-ledger.jsonl`) appends one JSON line per run:
  `{evaluated_at, snapshot_captured_at, lanes: {lane: {verdict, wake_state,
  fires_since, age_hours}}}` (new pure `ledger_entry`; `measure_lane` now
  also records `fires` via the existing `fires_since`). `--diff` compares
  the current run against the ledger's last parseable entry
  (`read_last_entry`) and prints a TRANSITIONS block + headline (pure
  `diff_entries` / `render_diff`). Diffing is on the state **class**
  (`state_class`: `WAKING-IDLE (5 fires…)` → `WAKING-IDLE`), so fire-count/
  age churn inside a state is never a transition; each transition is tagged
  recovery / degradation / other via severity ranks (`VERDICT_RANK` /
  `WAKE_RANK`; NOT MEASURED / SKIP / NEW / gone ends are always "other" —
  measurement artifacts never read as health moves, the roster UNREADABLE
  doctrine). `--repos`-filtered runs never append (poisoned-series guard,
  printed) and diff only the lanes present. **Exit contract unchanged** —
  `--ledger`/`--diff` never change the exit code. Selfcheck 24 → 41 assert
  pins (ledger shape, class collapse, no-transitions on fire-churn,
  recovery/degradation/NEW/gone/NOT-MEASURED tagging, cur_lanes_only,
  no-prior-entry honesty, missing-file read).
- `telemetry/lane-liveness-ledger.jsonl` — seeded first entry (04:07Z run,
  15 lanes) committed as telemetry, like triggers-snapshot.
- `telemetry/README.md` — new file documented (shape, why, no-cap-yet note).
- `control/status.md` — `updated:` → 04:09Z; slice-landed section; baton
  (next = groom #3 I8-reads-lane-fence or honest idle; ~05:00Z snapshot
  cycle; wake procedures should prefer `--diff --ledger` so the series
  accrues).
- Claim `control/claims/claude-fm-liveness-ledger.md` (born-red commit,
  deleted in this flip commit).

## Ground-truth runs (2026-07-20, verbatim)

Run 1 — first `--diff --ledger` (04:07Z, full fleet; no ledger file existed):

```
## Transitions (vs ledger telemetry/lane-liveness-ledger.jsonl)
no prior ledger entry — nothing to diff against (this run seeds the baseline when --ledger is given)

ledger: appended entry 2026-07-20T04:07Z → telemetry/lane-liveness-ledger.jsonl
```

(Table headline that run: `STALLED: superbot-idle (Seat B) · WAKING-IDLE:
superbot-next, websites, superbot-games · Seat A, superbot-idle (Seat B),
superbot-mineverse · asleep: none · DARK: none · not measured: 0`.)

Run 2 — `--diff` minutes later (04:07:38Z start, read-only): honest null,

```
## Transitions (vs ledger telemetry/lane-liveness-ledger.jsonl)
no transitions — all 15 lanes unchanged vs 2026-07-20T04:07Z
```

Run 3 — transition grammar demo on real fleet data, read-only simulated
evaluation `--diff --now 2026-07-20T12:00Z` (nothing appended):

```
## Transitions (vs ledger telemetry/lane-liveness-ledger.jsonl)
- fleet-manager (this repo) · verdict LIVE→STALLED  [degradation]
- idea-engine · verdict LIVE→QUIET  [degradation]
- sim-lab · verdict LIVE→STALLED  [degradation]
- substrate-kit · verdict LIVE→STALLED  [degradation]
- superbot (hub) · verdict QUIET→STALLED  [degradation]
- superbot-games · Seat A · verdict QUIET→STALLED  [degradation]
- superbot-mineverse · verdict QUIET→STALLED  [degradation]
- superbot-next · verdict QUIET→STALLED  [degradation]
- venture-lab · verdict QUIET→STALLED  [degradation]
- websites · verdict QUIET→STALLED  [degradation]
10 transitions vs 2026-07-20T04:07Z: 0 recoveries · 10 degradations · 0 other
```

Run 4 — `--repos fleet-manager --ledger --diff --strict`: diff restricted to
the filtered lane, append refused, strict exit intact:

```
## Transitions (vs ledger telemetry/lane-liveness-ledger.jsonl)
no transitions — all 1 lanes unchanged vs 2026-07-20T04:07Z

ledger append SKIPPED: --repos filter active — a partial run would poison the time series
exit=0
```

`selfcheck OK (41 pins)` verbatim in-session. Ledger stayed 1 line through
runs 2–4 (append only fired on run 1) — verified by `wc -l`.

## Design notes

- **Class-level diffing:** transitions compare `state_class` (text before
  the first ` (`), never the full string — otherwise every fire-count tick
  (`5 fires`→`7 fires`) or QUIET-suffix change would spam false
  transitions. The full `wake_state` string and `fires_since` are still
  stored per entry, so the detail is in the time series even though the
  diff ignores it.
- **Recovery vs degradation is a net severity delta** across both
  dimensions (verdict rank LIVE 0 · QUIET 1 · STALLED/DARK 2; wake rank
  —/waking 0 · asleep?/asleep 1 · WAKING-IDLE 2); any end outside the rank
  maps (NOT MEASURED, SKIP, NEW, gone) makes the transition "other" — a
  wall or roster change is never counted as a lane recovering/degrading.
- **Read-before-append:** `--diff` reads the last entry before `--ledger`
  appends, so `--diff --ledger` in one command is compare-then-record — the
  intended wake-procedure form.
- **Partial-run guard:** a `--repos` run never appends (a 1-lane entry
  would make the next full diff report 14 "gone" lanes) and its diff skips
  gone-detection for the same reason.
- **Honest nulls everywhere:** missing/empty/corrupt ledger → "no prior
  ledger entry" (corrupt lines are skipped, last *parseable* entry wins);
  identical runs → "no transitions — all N lanes unchanged".
- **Prior-print correction:** the old selfcheck printed "24 pins" but
  contained 26 asserts; the count now matches `grep -c "assert "` (41).

## Session incident — shared-clone branch race (for the coordinator)

The ~05Z records worker is live in the SAME clone (`/home/user/fleet-manager`)
and switched the checked-out branch to `claude/fm-05z-cycle` between this
session's edit and commit steps, so the payload commit (ef9fb63) initially
landed on that branch locally (unpushed there). Resolution taken: no touch of
the shared worktree or the other branch (their unstaged snapshot/status edits
were in flight); this session moved to an isolated `git worktree` and
cherry-picked the payload onto `claude/fm-liveness-ledger` (fd26c5c). Residue
flagged: local `claude/fm-05z-cycle` still carries ef9fb63 (identical patch —
merges as identical content if their push includes it), and 4 guard-fire
records from this session's first `bootstrap check` run sit unstaged in the
shared worktree (append-only telemetry, harmless if the 05Z session commits
them). Friction→guard candidate noted in the enders.

## Enders

- 💡 **Session idea (dedup-checked — `docs/planning/idea-backlog.md`,
  `docs/planning/2026-07-19-next-slices.md`, recent cards incl. the #379
  card's WAKING-IDLE-escalation idea):** **`--streaks` mode over the
  ledger.** Read the last N ledger entries and print per-lane *current-state
  streaks* (state · consecutive runs · wall-clock span, e.g. "superbot-idle:
  STALLED × 5 runs / ~12h"). The #379 card idea (auto-draft an owner-queue
  burner item when WAKING-IDLE persists ≥2 consecutive runs) needs exactly
  this persistence predicate — today it relies on someone remembering the
  previous run; the ledger now makes it a pure committed-data computation.
  Distinct from that idea (it routes an action; this computes durations) and
  from `--diff` (which only sees the last step, not how long a state has
  held).
- ⟲ **Previous-session review (PR #385, 01Z night cycle records slice):**
  clean records discipline — snapshot refreshed with dup/delta counts,
  SBW fifth-cycle escalation annotated with the keeper unchanged, and the
  night baton kept honest (idle cadence, groom #3 available). Improvement
  it surfaces: its liveness paragraph derived transitions BY HAND against
  the 22Z section's text ("recovered vs 20:36Z…", "new overnight 2-fire
  tags") — exactly the manual diff this slice mechanizes; wake/records
  procedures should now run `--diff --ledger` so those sentences come from
  the TRANSITIONS block instead of prose archaeology. Second, workflow-level
  improvement from this session's own incident: two concurrent workers
  sharing one clone race on `git checkout -B` — a cheap enforcing guard
  would be worker-side "commit only via an isolated `git worktree`" (or a
  pre-commit branch assertion `[ "$(git branch --show-current)" =
  "$EXPECTED_BRANCH" ]`) in the dispatch template; flagged for the
  coordinator rather than self-applied (dispatch prompts are the
  coordinator's surface).
- **Doc-audit:** everything durable is homed — mechanics + honesty caveats
  in the module docstring, rationale/evidence/kill-switch in the Q-0105
  block, file shape in `telemetry/README.md`, facts + baton in
  `control/status.md`, verbatim ground truth + design notes + the race
  incident in this card and the PR body. No chat-only conclusions.
- **Guard-fires:** `.substrate/guard-fires.jsonl` delta from this worktree's
  `bootstrap.py check --strict` run committed with the flip (do-not-revert);
  the born-red HOLD was the designed red pre-flip.
- **Claim:** `control/claims/claude-fm-liveness-ledger.md` deleted in this
  flip commit.
