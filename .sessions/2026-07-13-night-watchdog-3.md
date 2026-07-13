# 2026-07-13 — Night watchdog 3 (R26)

> **Status:** `complete`
> 📊 Model: fable-5 (worker, dispatched by the fleet-manager coordinator)

Third night-watchdog slice (R26), same procedure as #150/#154: full
`list_triggers` export to exhaustion, snapshot transform + capture_notes,
`check_trigger_health.py` run, prune-list-only posture (nothing deleted).

## Capture

- **12 pages, limit 100, cursor-to-exhaustion; window
  2026-07-13T04:06:22Z–04:09:05Z; 1112 records; 0 cursor-overlap
  duplicates; enabled 25** (was 35 at 02:28:33Z — the drop is the
  ~02:30–02:50Z queue flush firing pending one-shots, not deletions).
- Splice provenance: the final page (12 oldest records) returned inline
  rather than to a result file; bodies spliced verbatim from the
  committed 02:28:33Z capture after verifying `updated_at` identical on
  all 12 (registry-unchanged since).
- Deltas since 02:28:33Z: **+34 new, 0 deleted** (nothing pruned
  between captures).

## 02:28Z open items — all four resolved

- **(a) SuperBot 2.0 failsafe trig_01TuQrpMVpDCXB3K3VbjQUoA:
  RECOVERED** — fired 03:07:55Z, next 05:07:07Z. It skipped exactly one
  slot (01:07Z) and resumed; the "wedge" was a queued/slipped tick, not
  a dead cron. The dead-chain also resolved: the seat woke on the
  failsafe and holds a fresh pacemaker (trig_01911MzZ2DD7CTSfw4yCaf8t,
  04:31Z). No send_message recovery needed.
- **(b) Ideas Lab failsafe trig_01Kz3j5ECTZ29hNZCHukgCA1: RECOVERED** —
  fired 03:39:29Z, next 05:38:53Z (same one-slot-skip signature).
- **(c) Curious Research failsafe trig_01WLfpsEhiPEoT18G9ds1sM5: FIRST
  FIRE PROVEN** — last_fired 02:49:00Z (the 02:20Z slot, ~29min late in
  the flush), next 04:20:00Z. Ninth-seat coverage moves
  armed-but-unproven → proven.
- **(d) The 6-id prune list is MOOT — all six FIRED (run_once_fired),
  none pruned, none remain**: trig_01E91ZrhYCWauAFCePvGZdzJ 02:30:25Z ·
  trig_01AGpPVhsG8DvuJe4kpfg4bo 02:45:36Z ·
  trig_01RhVf5C5Y65rd7yfVgRiUjx 02:41:01Z ·
  trig_01Y5f5tZLyWfvqHFarni8GUE 02:46:50Z ·
  trig_01USg5i3qna4fCX5ZeePg7Gj 02:46:55Z ·
  trig_018rSkhaVaGJK3mXf6bA2v8K 02:46:49Z. The five "keep" ticks also
  fired 02:30–02:49Z — the predicted double/triple wakes (Venture Lab ×3
  in 6min) occurred and self-cleared. The whole 01:08–01:58Z undelivered
  backlog flushed ~02:30–02:50Z, dating the 02:28:33Z capture as roughly
  the LAST moment of the degradation window.

## check_trigger_health.py — verdicts at eval 04:06Z

- I1 WEDGED-CRON **PASS** · I2 DROPPED-ONESHOT **PASS** · I3 DEAD-CHAIN
  **PASS** · I4 MANAGER-FAILSAFE **PASS** (fm failsafe next 04:37:36Z) ·
  I6 SNAPSHOT-FRESH **PASS**.
- **I5 ROSTER-FRESH FAIL at eval (SELF-HEALED one minute later)** —
  roster was 4.7h old (23:32Z) because the roster-regen Actions cron
  (`40 */2`) skipped its 00:40 and 02:40 slots (GitHub best-effort
  skips, same family as the merge-on-green cron lag). Run #19 fired
  04:10:37Z, succeeded, and Generation #23 (generated-at 04:10Z) landed
  on main (#156); re-run of the checker against the fresh roster shows
  I5 PASS. No action needed; the skip-two-slots gap is worth a morning
  eye.
- **I7 TICK-PILE-UP FAIL — 1 pile-up. PRUNE LIST for the coordinator
  (worker deletes NOTHING):** Ideas Lab
  (session_01Q5sGKgKCngGa7jgfzEGeEQ): keep
  trig_014gcRs4kQGL4n2GpJnuXxAT (04:18Z), **prune
  trig_013tQ6NxnCfZh9n48LZrWNiS** (04:10Z — due 4min after capture, so
  delivery has likely beaten the prune again; verify before deleting).

## merge-on-green cron backstop — PROVEN (headline for the morning tally)

Was zero `schedule`-event runs through 02:33Z (watchdog 2 flagged
"unproven if still zero at ~04:10Z"). **First schedule-event run — #49,
id 29222650560 — fired 03:53:24Z, conclusion success.** GitHub's
new-cron activation lag ended ~3h16m after the first 00:37Z slot; the
`7,37 * * * *` backstop lane is live. A CCR-side outage no longer leaves
only event lanes merging.

## 💡 Session idea

**I7 PRUNE-RACE annotation in check_trigger_health.py.** Tonight is the
third consecutive proof that delivery beats pruning: watchdog 1's Ideas
Lab prune target fired before the coordinator could act, watchdog 2's
entire 6-id list fired in the 02:30–02:50Z flush, and tonight's flagged
tick was due 4 minutes after capture. I7 should annotate any prune
candidate whose `run_once_at` is within ~15min of the eval instant (or
already past it) as `PRUNE-RACE: verify last_fired_at before deleting` —
turning the remedy line from "delete the rest" into race-aware advice
and preventing a coordinator from deleting a tick mid-delivery. (Deduped:
watchdog 1's idea is page ingestion, watchdog 2's is seat attribution;
neither covers prune imminence — this amends the I7 remedy string plus
one timestamp comparison in existing machinery.)

## ⟲ Previous-session review

Watchdog 2 (PR #154) made two calls that paid off tonight: its
forecast-note doctrine (state the exact field + expected value the next
export should show) made all four open items one-line lookups —
(a)/(b)/(c) resolved by exactly the fields its capture_notes named — and
its "re-check merge-on-green at watchdog 3" framing turned the cron
backstop into a binary morning-tally verdict. One genuine gap: its 6-id
prune list carried a caveat that late delivery was possible but still
routed the list to the coordinator as actionable; all six fired within
~20 minutes of capture, so the actionable-looking list was already stale
when read. Concrete improvement (this session's idea): make I7 itself
annotate imminent-due prune candidates as PRUNE-RACE so the freshness
judgment is in the tool, not in a prose caveat a tired coordinator may
skip.

## Merge posture

No self-merge — merge-on-green sweeps this PR (#157, touches no
workflows). ≤2 CI polls then report.
