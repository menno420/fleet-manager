# 2026-07-19 · fm build slice — wake-without-work detector in `check_lane_liveness.py`

> **Status:** `complete`

About to happen (declared born-red): groom slice #2 (evening re-groom's ranked #2,
baton "Next slice" as of 20:2xZ) — extend `scripts/check_lane_liveness.py` with a
wake-without-work signal. For each lane whose failsafe shows ENABLED in the committed
`telemetry/triggers-snapshot.json`, compare the failsafe's `last_fired_at` against the
lane's newest observed liveness signal: a failsafe that has fired ≥2 windows (from the
cron cadence + last_fired) after the lane's last landed output is **WAKING-IDLE** —
wakes are burning tokens with zero output, a distinct and worse state than mere quiet —
vs **asleep** (failsafe armed on paper but not actually firing at capture). Existing
verdict ladder unchanged; this refines STALLED with the burn signal as a new column.
Honest capture-lag caveat printed (fires after `captured_at` are invisible). Ground
truth demo: the STALLED SBW constituent lanes. Also: selfcheck pins for the new pure
logic, Q-0105 note on the new block, `control/status.md` baton advance, claim
`control/claims/claude-fm-wake-idle-detector.md` (deleted in the flip commit).
No trigger-MCP calls from this venue; no sibling repo written.

- **📊 Model:** fable-5 · high · feature build — extend verified checker, tooling+docs (Q-0105 provenance tier)

## What shipped (PR #379)

- `scripts/check_lane_liveness.py` — wake-without-work detector (Q-0105
  provenance block, kill-switch included): `lane_cadence` now also returns the
  winning rung's newest `last_fired_at` (`_newest_fire`); new pure functions
  `fires_since` (fires after the lane's newest signal, earlier fires inferred
  from the cron cadence — one per window across the signal→last_fired gap,
  plus the recorded fire) and `wake_state` (ladder: `—` unarmed · `asleep?`
  armed-no-fire-on-record · `asleep` last fire > 2 cadences before
  `captured_at` · `waking (no signal to compare)` for DARK/NOT MEASURED ·
  `WAKING-IDLE (N fires since last output)` at ≥2 · `waking (1 fire since
  output)` · `waking`). New **Wake (snapshot)** table column + summary-line
  `WAKING-IDLE:` / `asleep:` lists + printed capture-lag caveat quoting the
  capture instant (fires after `captured_at` are invisible). **Verdict ladder
  + exit contract unchanged** — regression-checked: `--strict` on a LIVE lane
  → exit 0, on a STALLED lane → exit 1. Selfcheck 10 → 24 pins (incl. the
  SBW signature: last fire 17:15Z vs signal 07:34Z at 2h cadence → 5 fires →
  WAKING-IDLE).
- `control/status.md` — `updated:` → 20:39Z; slice-landed section; baton
  advanced (next = groom #3 I8-reads-lane-fence or honest idle; ~22:00Z
  snapshot cycle stands and also refreshes the wake column's blind window).
- Claim `control/claims/claude-fm-wake-idle-detector.md` (born-red commit,
  deleted in this flip commit).

## Ground-truth run 1 (2026-07-19T20:36Z, full fleet, verbatim)

```
# Lane liveness — seat-chain stall detector
evaluated-at 2026-07-19T20:36Z · triggers snapshot captured_at 2026-07-19T17:57:56Z

| Lane | Last signal | Kind | Age | Cadence (source) | Windows | Failsafe | Wake (snapshot) | Verdict |
|---|---|---|---|---|---|---|---|---|
| superbot (hub) | 2026-07-19T19:37Z | main commit | ~58m | 2h (seat cron (SuperBot 2.0 seat)) | 0.5 | enabled | waking | LIVE |
| superbot-next | 2026-07-19T20:31Z | main commit | ~4m | 2h (seat cron (SuperBot 2.0 seat)) | 0.0 | enabled | waking | LIVE |
| substrate-kit | 2026-07-19T13:41Z | main commit | ~6h54m | 2h (seat cron (Self Improvement seat)) | 3.5 | enabled | WAKING-IDLE (2 fires since last output) | QUIET |
| websites | 2026-07-19T20:24Z | main commit | ~11m | 2h (own failsafe cron) | 0.1 | enabled | waking | LIVE |
| trading-strategy | 2026-07-19T18:54Z | main commit | ~1h41m | 2h (assumed (no armed cron found)) | 0.8 | — | — | LIVE |
| venture-lab | 2026-07-19T18:29Z | main commit | ~2h06m | 2h (own failsafe cron) | 1.1 | enabled | waking | LIVE |
| superbot-games · Seat A | 2026-07-19T08:50Z | main commit | ~11h45m | 2h (seat cron (SuperBot World seat)) | 5.9 | enabled | WAKING-IDLE (5 fires since last output) | STALLED |
| superbot-idle (Seat B) | 2026-07-19T07:26Z | main commit | ~13h09m | 2h (seat cron (SuperBot World seat)) | 6.6 | enabled | WAKING-IDLE (5 fires since last output) | STALLED |
| superbot-mineverse | 2026-07-19T07:26Z | main commit | ~13h09m | 2h (seat cron (SuperBot World seat)) | 6.6 | enabled | WAKING-IDLE (5 fires since last output) | STALLED |
| pokemon-mod-lab | 2026-07-19T07:34Z | main commit | ~13h01m | 2h (assumed (no armed cron found)) | 6.5 | — | — | QUIET (no failsafe armed — may be by design) |
| gba-homebrew | 2026-07-19T20:25Z | main commit | ~10m | 2h (assumed (no armed cron found)) | 0.1 | — | — | LIVE |
| product-forge | 2026-07-19T09:05Z | main commit | ~11h30m | 2h (assumed (no armed cron found)) | 5.8 | — | — | QUIET (no failsafe armed — may be by design) |
| idea-engine | 2026-07-19T20:32Z | main commit | ~3m | 2h (seat cron (Ideas Lab seat)) | 0.0 | enabled | waking | LIVE |
| sim-lab | 2026-07-19T20:30Z | main commit | ~5m | 2h (seat cron (Ideas Lab seat)) | 0.0 | enabled | waking | LIVE |
| fleet-manager (this repo) | 2026-07-19T20:25Z | main commit | ~10m | 2h (own failsafe cron) | 0.1 | enabled | waking | LIVE |

STALLED: superbot-games · Seat A, superbot-idle (Seat B), superbot-mineverse · WAKING-IDLE: substrate-kit, superbot-games · Seat A, superbot-idle (Seat B), superbot-mineverse · asleep: none · DARK: none · not measured: 0

Wake-column caveat: reads the COMMITTED snapshot only — fires after captured_at 2026-07-19T17:57:56Z are invisible (capture lag). WAKING-IDLE = failsafe fired ≥2 windows after the lane's newest landed signal (earlier fires inferred from the cron cadence): wakes are burning tokens with zero landed output. asleep = armed on paper, not firing at capture.
```

(exit 0.) The target ground truth landed exactly: all three STALLED SBW
constituent lanes score `WAKING-IDLE (5 fires since last output)` — the seat
failsafe kept firing (last recorded 17:15Z) hours after each lane's newest
landed signal (07:26–08:50Z), today's SBW burn finding made mechanical.
Bonus signal: substrate-kit scores `WAKING-IDLE (2 fires)` while still QUIET
— the column catching the burn state *before* the STALLED bar, the
early-warning shape. `selfcheck OK (24 pins)` verbatim in-session.

## Design notes

- **Inference honesty:** only the single most-recent `last_fired_at` exists
  in the snapshot, so fire counts are *inferred* (one per cadence window
  across the gap) — stated in the docstring, the caveat line, and the
  provenance block. The `asleep` on-schedule check (last fire within 2
  cadences of capture) is what supports the inference.
- **Self-correcting on capture lag:** output landing after the recorded fire
  → `fires_since = 0` → plain `waking`; the column can under-report fires
  after `captured_at` but never invents burn.
- **Refine, don't replace:** `verdict_for` untouched; WAKING-IDLE is a
  column + summary list, so `--strict` semantics and every existing consumer
  of the verdict ladder are unaffected.

## Enders

- 💡 **Session idea (dedup-checked — `docs/planning/idea-backlog.md`, the
  evening re-groom's 12-item list, `docs/ideas/` incl.
  fleet-economics-ledger, today's cards):** **WAKING-IDLE escalation → a
  paste-ready owner-queue burner item.** The detector now *names* the burn
  state, but the fix is owner-venue (pause/delete the failsafe or unstick
  the seat) — when a lane stays WAKING-IDLE across ≥2 consecutive detector
  runs, a small step could auto-draft the `docs/owner-queue.md` item
  (lane · trigger id · fires-since-output count · one-line hint: unstick
  the seat or disarm the burner), the same paste-ready mechanic as
  OQ-SBW-DUP-FAILSAFE. Turns the new signal into a routed action instead of
  a table row someone must notice. Adjacent to (not covered by) the
  fleet-economics-ledger idea: that prices usage; this routes a specific
  stop-the-burn decision.
- ⟲ **Previous-session review (PR #377, evening groom + top slice):** strong
  pattern — 12 ideas ranked with honest one-line park/drop reasons, the top
  pick chosen by an explicit venue constraint (zero network/classifier
  surface), built with selfcheck + determinism proof, and the baton left
  naming this slice with its ground truth ("the SBW trio is the live ground
  truth to demo on") — which made this session's target unambiguous.
  Miss/improvement: the groom pinned the *vocabulary*
  (`WAKES-DELIVERED-BUT-IDLE` vs `NO-WAKE`) which the build renamed
  (WAKING-IDLE / asleep) for table width and ladder fit — grooms should pin
  the *semantics* (the two states to split) and mark names as provisional,
  so the builder isn't silently diverging from a spec word.
- **Doc-audit:** everything durable is homed — detector rationale + evidence
  pointer + kill-switch in the code's Q-0105 block, facts + baton in
  `control/status.md`, verbatim table + design notes in this card and the
  PR body. The plan doc's evening-re-groom entry stays as-groomed by
  convention (DONE marks live in the baton, not the dated plan — PR #352
  card precedent). No orphaned chat-only conclusions.
- **Guard-fires:** `.substrate/guard-fires.jsonl` delta committed
  (do-not-revert); born-red HOLD was the only red in `bootstrap.py check
  --strict` pre-flip.
- **Claim:** `control/claims/claude-fm-wake-idle-detector.md` deleted in
  this flip commit.
