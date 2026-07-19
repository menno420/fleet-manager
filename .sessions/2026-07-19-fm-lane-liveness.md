# 2026-07-19 · fm build slice — `scripts/check_lane_liveness.py` (seat-chain stall detector)

> **Status:** `complete`

About to happen (declared born-red): build slice #1 from
`docs/planning/2026-07-19-next-slices.md` — a new stdlib-only advisory checker
`scripts/check_lane_liveness.py` that measures each fleet lane's liveness signals
(newest main commit timestamp + heartbeat `updated:` stamp, read over the roster's
verified git transport) against the lane's failsafe wake cadence (parsed from the
committed `telemetry/triggers-snapshot.json`), and emits a per-lane
LIVE / QUIET / STALLED / DARK verdict table. Motivation: tonight's websites silence
(no commits after 21:52Z, ORDER 036 unacked across three failsafe windows) was caught
~4h late by a human-style read — this mechanizes exactly that sweep. Also: smallest
true playbook index edit, `control/status.md` baton advance (slice 2 = regen-window
skip detector next), claim `control/claims/claude-fm-lane-liveness.md` (deleted in
the flip commit). Advisory-only — never merge-blocking; `--strict` for wake use.
No trigger-MCP calls from this venue; no sibling repo written.

- **📊 Model:** fable-5 · high · feature build — new advisory checker, tooling+docs (Q-0105 provenance tier)

## What shipped (PR #350)

- `scripts/check_lane_liveness.py` (new, stdlib + gen_roster sibling imports) —
  per-lane LIVE / QUIET / STALLED / DARK verdicts. Signals: newest main-commit
  timestamp + every `control/status*.md` `updated:` stamp, read via
  `gen_roster.read_heartbeat` (ls-remote-verified fetch, auth/wall doctrine
  inherited). Cadence: lane's own enabled standing cron → covering seat cron via
  the hand-maintained `SEAT_COVER` map (only name-derivable pairs; Game Lab
  constituents deliberately NOT guessed) → assumed 2.0h, labelled. Thresholds:
  LIVE ≤2 windows · QUIET ≤4 · STALLED >4 with failsafe enabled · DARK no
  signal · NOT MEASURED on a wall (verbatim reason, nothing invented). Exit:
  advisory 0; `--strict` → 1 on any STALLED; `--selfcheck` 10 offline pins
  (including the exact websites-036 signature: 21:52Z signal read at 07:45Z on a
  2h cadence → STALLED).
- `docs/playbook.md` — R27 "DETECTION IS MECHANIZED" note (smallest true index
  edit; carries the open-PR-heads caveat forward).
- `control/status.md` — `updated:` → 07:40Z; slice-1 facts subsection; baton
  advanced (slice 1 DONE, next = regen-window skip detector in
  `check_roster_freshness.py`, then I8 provenance remedy).

## Ground-truth run 1 (2026-07-19T07:36Z, full fleet, ~25s, verbatim)

```
# Lane liveness — seat-chain stall detector
evaluated-at 2026-07-19T07:36Z · triggers snapshot captured_at 2026-07-19T06:15:10Z

| Lane | Last signal | Kind | Age | Cadence (source) | Windows | Failsafe | Verdict |
|---|---|---|---|---|---|---|---|
| superbot (hub) | 2026-07-19T06:48Z | main commit | ~47m | 2h (seat cron (SuperBot 2.0 seat)) | 0.4 | enabled | LIVE |
| superbot-next | 2026-07-19T01:36Z | main commit | ~6h00m | 2h (seat cron (SuperBot 2.0 seat)) | 3.0 | enabled | QUIET |
| substrate-kit | 2026-07-19T02:57Z | main commit | ~4h39m | 2h (seat cron (Self Improvement seat)) | 2.3 | enabled | QUIET |
| websites | 2026-07-19T07:26Z | main commit | ~10m | 2h (own failsafe cron) | 0.1 | enabled | LIVE |
| trading-strategy | 2026-07-18T21:18Z | main commit | ~10h18m | 2h (assumed (no armed cron found)) | 5.2 | — | QUIET (no failsafe armed — may be by design) |
| venture-lab | 2026-07-19T07:34Z | main commit | ~2m | 2h (own failsafe cron) | 0.0 | enabled | LIVE |
| superbot-games · Seat A | 2026-07-19T07:30Z | main commit | ~6m | 2h (seat cron (SuperBot World seat)) | 0.1 | enabled | LIVE |
| superbot-idle (Seat B) | 2026-07-19T07:26Z | main commit | ~10m | 2h (seat cron (SuperBot World seat)) | 0.1 | enabled | LIVE |
| superbot-mineverse | 2026-07-19T07:26Z | main commit | ~10m | 2h (seat cron (SuperBot World seat)) | 0.1 | enabled | LIVE |
| pokemon-mod-lab | 2026-07-19T07:34Z | main commit | ~2m | 2h (assumed (no armed cron found)) | 0.0 | — | LIVE |
| gba-homebrew | 2026-07-18T23:26Z | main commit | ~8h09m | 2h (assumed (no armed cron found)) | 4.1 | — | QUIET (no failsafe armed — may be by design) |
| product-forge | 2026-07-18T08:31Z | main commit | ~23h05m | 2h (assumed (no armed cron found)) | 11.5 | — | QUIET (no failsafe armed — may be by design) |
| idea-engine | 2026-07-19T07:26Z | main commit | ~9m | 2h (seat cron (Ideas Lab seat)) | 0.1 | enabled | LIVE |
| sim-lab | 2026-07-19T07:07Z | main commit | ~29m | 2h (seat cron (Ideas Lab seat)) | 0.2 | enabled | LIVE |
| fleet-manager (this repo) | 2026-07-19T07:29Z | main commit | ~7m | 2h (own failsafe cron) | 0.1 | enabled | LIVE |

STALLED: none · DARK: none · not measured: 0
```

**Honest deviation from the plan's expected demo:** the plan (drafted ~07:26Z)
expected websites to score STALLED/QUIET — but the lane RESUMED at 07:26:23Z
(websites #436, `cf314c2`, heartbeat commit), 10 minutes before this run, ending
a verified ~9.6h silence since `a5fdad4` 2026-07-18T21:52:34Z. The live LIVE
verdict is therefore correct ground truth, and the stall-window signature the
checker exists for is pinned offline in `--selfcheck` (21:52Z@07:45Z → STALLED).
The plan's own header said to re-verify volatile claims at HEAD — this is that
re-verification. `pokemon-mod-lab` read fine over plain transport this run
(no wall hit); NOT MEASURED path exercised only by the Wall branch + verdict
pins, not live this run.

## Enders

- 💡 **Session idea (dedup-checked — `docs/ideas/` 16 files, planning docs,
  2026-07-18/19 cards):** **machine-readable seat coverage (`covers:` field on
  registry-only LANES entries).** Building this slice required hand-deriving
  `SEAT_COVER` from seat lane display names, and Game Lab's constituents are
  not name-derivable at all — leaving gba-homebrew / product-forge /
  trading-strategy structurally unable to score STALLED (cadence "assumed",
  failsafe unattributable). One authored `covers: ["repo", …]` list per seat
  entry in `gen_roster.LANES` (flowing into the generated `registry/lanes.json`)
  gives gen_roster attribution, the liveness checker, and any future seat-aware
  tool one source of truth — and turns the blind spot into a one-question owner
  ask (what does Game Lab cover?).
- ⟲ **Previous-session review (PR #349, planning groom):** the slice-1 spec was
  buildable verbatim — verdict vocabulary, cadence source, thresholds, and the
  advisory tier all transferred without a single clarification needed; that is
  what a good plan looks like. Miss: its expected-demo claim ("websites should
  score STALLED") was volatile and aged out in 10 minutes; the header's generic
  R2 re-verify note covered it, but the improvement is to attach the re-verify
  flag to each specific volatile claim inline (e.g. "websites STALLED *as of
  drafting; re-check*"), so a builder can't quote an expired expectation as a
  result.
- **Doc-audit:** everything from this session is in a durable home — the
  checker's own Q-0105 header (motivation + run-1 evidence), playbook R27
  (index), `control/status.md` (facts + baton), this card (table verbatim).
  The plan doc's standing-queue section explicitly mirrors the status baton, so
  the DONE mark lives in the baton (live truth), not the dated plan.
- **Guard-fires:** `.substrate/guard-fires.jsonl` delta committed (do-not-revert);
  born-red HOLD was the only red in `bootstrap.py check --strict` pre-flip.
- **Claim:** `control/claims/claude-fm-lane-liveness.md` deleted in this flip
  commit.
