# 2026-07-13 — night watchdog 2 (R26 registry export + trigger health)

> **Status:** `complete`

📊 Model: fable-5 · start 2026-07-13 ·
coordinator-dispatched worker (night watchdog slice 2, R26, per ORDER
039/040)

## Declared at open (born-red)

Night watchdog wake per playbook R26, same procedure as watchdog 1
(PR #150): (1) full paginated `list_triggers` export (limit 100,
cursor-to-exhaustion — 11 pages, 1078 records, capture window
2026-07-13T02:28:33Z–02:31:32Z); (2) transform into the committed
`telemetry/triggers-snapshot.json` schema (id-sorted, absent-key-for-null,
indent-2, top-level `captured_at` + `capture_notes` documenting deltas
since the 00:39:53Z capture); (3) run `scripts/check_trigger_health.py` —
all invariants — and act same-wake: wedged crons headlined, pile-ups →
prune list (ids reported to the coordinator, NO self-deletes), dropped
one-shots on seat sessions named + whether the seat's failsafe covers
them. Also noting for the coordinator whether merge-on-green has produced
SCHEDULE-event runs yet (was zero at 01:12Z). Per tonight's owner rule:
no self-merge — the merge-on-green sweep lands this PR; ≤2 CI polls then
report.

## Close-out

**Shipped (PR #154):**

- `telemetry/triggers-snapshot.json` — full verbatim registry snapshot,
  `captured_at` 2026-07-13T02:28:33Z (window 02:28:33Z–02:31:32Z), 11
  pages, **1078 records / 35 enabled**, 0 cursor-overlap duplicates,
  id-sorted, absent-key-for-null. Deltas vs 00:39:53Z: **1 deletion**
  (trig_0123fu7onT7wGMNB9ZtbtdqL — the watchdog-1 prune recommendation,
  confirming the coordinator executed it), **45 new records**.
  capture_notes also record the watchdog-1 open-item resolutions (Ideas
  Lab pile-up self-cleared by delivery, not prune; the SuperBot World
  00:14Z tick proved QUEUED-not-LOST — delivered 02:08:14Z, ~1h54m late),
  the partial scheduler-degradation recurrence (below), and next-export
  forecasts per the R26 forecast-note doctrine.

**Health run (`scripts/check_trigger_health.py`, eval at captured_at
2026-07-13T02:28Z): VERDICT FAIL — 4/7 red, exit 1.**

- **I1 WEDGED-CRON FAIL — HEADLINE: two seat failsafes wedged**, the
  2026-07-12 incident signature back in miniature:
  - trig_01TuQrpMVpDCXB3K3VbjQUoA "SuperBot 2.0 failsafe wake"
    (`0 1-23/2`) next frozen 01:07:07Z (81 min past at eval; last fired
    23:07Z).
  - trig_01Kz3j5ECTZ29hNZCHukgCA1 "Ideas Lab failsafe wake"
    (`30 1-23/2`) next frozen 01:38:53Z (50 min past; last fired 23:38Z).
  - Selective, not a full outage: sibling failsafes fired at 01:15Z
    (SuperBot World), 01:45Z (Venture Lab), 02:07–02:10Z (Self
    Improvement, Websites, Game Lab); queued one-shot delivery visibly
    resumed ~02:08Z.
- **I2 DROPPED-ONESHOT FAIL** — undelivered ticks due 01:08Z–01:58Z on 8
  seat sessions. Named, with failsafe coverage:
  - Game Lab (session_015xJBwRogy1ByzZmeWC38qW, tick due 01:08Z) —
    **covered** (failsafe fired 02:10Z, next 02:50Z).
  - Venture Lab (session_01CXEh5TBKBNTDGgsDstfcjc, 01:27Z) — **covered**
    (failsafe fired 01:45Z, next 03:45Z).
  - Websites (session_01K3A7v82YxTxzaFztpbgEY2, 01:39Z) — **covered**
    (failsafe fired 02:10Z, next 02:45Z).
  - SuperBot 2.0 (session_01KhzyfUk76YB9Bj2TPF6h5z, 01:37Z pacemaker +
    01:58Z self-armed scheduler-wedge PROBE tick, both undelivered) —
    **NOT covered**: its failsafe is one of the two wedged crons.
  - PR-watch lane (session_01Kn5PjZR5EDJL75BeELkUfr, 01:55Z curious-
    research PR #1 check-in) — no failsafe, but a distinct future tick
    (02:42Z, superbot #2060 check) is armed; chain alive.
  - Self Improvement (session_01MSze9jQLdxByyv2j6rm29c, 01:49Z) —
    **covered** (failsafe fired 02:07Z, next 04:07Z).
  - Curious Research (session_01N9QvWRsgjhunTTPJU3UoZA, 01:39Z pacemaker)
    — **armed-but-unproven**: failsafe cron trig_01WLfpsEhiPEoT18G9ds1sM5
    (`20 */2`, created 01:22:54Z) was 8.5 min past its FIRST-EVER fire
    (02:20Z) at capture — inside I1 grace, zero fire history.
  - Ideas Lab (session_01Q5sGKgKCngGa7jgfzEGeEQ, 01:39Z) — failsafe
    wedged, but a future pacemaker (02:39Z) is armed; chain alive.
- **I3 DEAD-CHAIN FAIL — two seats for coordinator recovery
  (send_message, the only working cross-session revival path, Q-0242):**
  **SuperBot 2.0** (session_01KhzyfUk76YB9Bj2TPF6h5z — 2 dropped ticks +
  wedged failsafe, fully dark) and **Curious Research**
  (session_01N9QvWRsgjhunTTPJU3UoZA — dropped pacemaker, failsafe unproven
  at eval; verify its 02:20Z fire happened before messaging).
- I4 MANAGER-FAILSAFE **PASS** — trig_01UQTZFvknBosXVo4YKKfazZ
  (`30 */2`) next 02:37:36Z. Note: the fm coordinator session holds ZERO
  pending one-shots at capture — failsafe-only coverage.
- I5 ROSTER-FRESH **PASS** (3.1h, bar 4h — aging; regen cron should
  refresh before watchdog 3) · I6 SNAPSHOT-FRESH **PASS** (0.1h — verdict
  on a fresh basis).
- **I7 TICK-PILE-UP FAIL — 5 pile-ups. PRUNE LIST for the coordinator
  (worker reports ids, deletes NOTHING; keep NEWEST, prune the rest):**
  - SuperBot World (session_013CEaD81nh2E4wK1NsrKMPV): keep
    trig_01F4AVwutFqnh3JyDwDt7dFU (02:34Z), **prune
    trig_01E91ZrhYCWauAFCePvGZdzJ** (02:30Z).
  - Venture Lab (session_01CXEh5TBKBNTDGgsDstfcjc): keep
    trig_019aoHQmoBKLGwmNYHZM2kbc (02:47Z), **prune
    trig_01AGpPVhsG8DvuJe4kpfg4bo** (01:27Z) **and
    trig_01RhVf5C5Y65rd7yfVgRiUjx** (02:41Z).
  - Websites (session_01K3A7v82YxTxzaFztpbgEY2): keep
    trig_015bHF2GUHkFNehKkqnVqKuA (02:30Z), **prune
    trig_01Y5f5tZLyWfvqHFarni8GUE** (01:39Z).
  - Self Improvement (session_01MSze9jQLdxByyv2j6rm29c): keep
    trig_01QsU2UCJ5q6KbNCMn8HcsqR (02:24Z), **prune
    trig_01USg5i3qna4fCX5ZeePg7Gj** (01:49Z).
  - Ideas Lab (session_01Q5sGKgKCngGa7jgfzEGeEQ): keep
    trig_01XR69tzhvJ2VxRE3JtdJr45 (02:39Z), **prune
    trig_018rSkhaVaGJK3mXf6bA2v8K** (01:39Z).
  - Total: **6 prune ids.** Caveat: the 5 older ticks are in the
    01:27–02:30Z undelivered window and may deliver late (as the SBW
    00:14Z one did at 02:08Z) — prune remains correct either way, it
    removes the double-wake.

**Cron-lag note:** healthy standing crons carry accumulated fire-time
offsets — next_run_at = last-fire + interval, so the fm failsafe's `:30`
schedule now fires ~`:37` (next 02:37:36Z), Ideas Lab `:30` → `:38`,
SuperBot 2.0 `:00` → `:07`. Lag is cosmetic on healthy crons but means
"due" times drift later every cycle.

**merge-on-green SCHEDULE-event check (asked in dispatch):** still ZERO
`schedule`-event runs as of the newest run (#40, 02:33:54Z) — the 30 most
recent runs are all `workflow_run`/`pull_request` events. The `7,37 * * *
*` cron backstop has missed every slot so far (00:37–02:07); the event
lanes did all the merging (#150–#153 landed via workflow_run-triggered
sweeps). Consistent with GitHub's known new-cron activation lag; worth
re-checking at watchdog 3 — if still zero, the cron backstop lane is
unproven and a scheduler outage would leave only event lanes.

**Merge posture:** no self-merge — merge-on-green sweeps this PR (#154,
touches no workflows). ≤2 CI polls then report.

## 💡 Session idea

Registry-derived seat attribution for `gen_roster.attribute_lane`. Every
health finding tonight printed `lane: (unattributed)` — the existing
token-based LANES matching misses session-bound records, so the watchdog
hand-derived every seat name (SuperBot 2.0, Curious Research, …) from
failsafe-cron names + message text. The registry is already
self-describing: each seat failsafe cron carries both the seat name
("<Seat> failsafe wake") and the seat's persistent_session_id — one pass
over the snapshot builds a session→seat map for free, and
`attribute_lane` falling back to that map would make every I1–I7 line
name its seat directly. Cuts the most manual step of the watchdog wake
and makes prune lists/dead-chain flags copy-paste unambiguous. (Deduped:
docs/ideas/ has no attribution/seat-map idea; nearest is watchdog-1's
ingest_trigger_pages.py which is ingestion, not attribution — this one
amends existing machinery in scripts/gen_roster.py.)

## ⟲ Previous-session review

Watchdog 1 (PR #150) set the template this session executed nearly
verbatim, and its two judgment calls both paid off measurably: (a) the
prune-list-not-delete posture was validated — its Ideas Lab prune target
fired before the coordinator could prune it, which under a delete-it-
yourself posture would have raced a live delivery; (b) its review's
forecast-note doctrine converted three of tonight's checks (failsafe
cutover, dropped-tick fate, replacement-pacemaker fate) into
assert-and-verify one-liners. One genuine gap: watchdog 1 verified the
QUEUED-vs-LOST ambiguity could not be settled from the registry but
didn't record WHERE the answer would appear — it showed up tonight as
last_fired_at on the "dropped" tick (delivered 02:08Z). Concrete
improvement, folded into this session's capture_notes forecasts: state
the exact field + expected value the next export should show, so
ambiguous verdicts always name their own resolution test.
