# 2026-07-13 — night watchdog 1 (R26 registry export + trigger health)

> **Status:** `complete`

📊 Model: fable-5 · start 2026-07-13 ·
coordinator-dispatched worker (night watchdog slice, R26)

## Declared at open (born-red)

Night watchdog wake per playbook R26: (1) full paginated `list_triggers`
export (limit 100, cursor-to-exhaustion — 11 pages, 1034 records captured
2026-07-13T00:39:53Z–00:43:16Z); (2) transform into the committed
`telemetry/triggers-snapshot.json` schema (id-sorted, absent-key-for-null,
top-level `captured_at` + `capture_notes` documenting deltas — this export
is FULL VERBATIM, so no merge-over-prior-bodies is needed, unlike the
trimmed 20:41Z capture); capture_notes also record the DROPPED TICK
trig_0123fu7onT7wGMNB9ZtbtdqL (send_later, scheduled 2026-07-13T00:06:00Z,
bound session_01UutkJqyMcHC1VyFW8fe1a9, never delivered) and the seat
failsafe trig_01UQTZFvknBosXVo4YKKfazZ that fired 00:37Z and caught the
stall; (3) run `scripts/check_trigger_health.py` against the new snapshot —
all invariants incl. I7 TICK-PILE-UP — and act on any FAIL same wake
(pile-up → prune list reported to the coordinator, no self-deletes; wedged
cron → headline). Per tonight's owner rule: no self-merge — the
merge-on-green sweep lands this PR.

## Close-out

**Shipped (PR #150):**

- `telemetry/triggers-snapshot.json` — full verbatim registry snapshot,
  `captured_at` 2026-07-13T00:39:53Z (window 00:39:53Z–00:43:16Z), 11 pages,
  **1034 records / 24 enabled**, 0 cursor-overlap duplicates, id-sorted,
  absent-key-for-null. Unlike the 20:41Z trimmed 12-field capture, every
  record carries its complete body, so no merge-over-prior-bodies was needed
  — these bodies supersede the trimmed-merge snapshot. capture_notes record:
  the created_at BOUND resolution for the 7 previously-bounded records; the
  10 deletions since 20:41Z (incl. old fm failsafe
  trig_01BKpsyoBzp1K1ob9H3iu1gM — the 20:41Z notes' forecast boot-cutover
  delta reconciled exactly as predicted, successor
  trig_01UQTZFvknBosXVo4YKKfazZ present); 99 new records; and the DROPPED
  TICK (below).

**Dropped tick (recorded in capture_notes):**
trig_0123fu7onT7wGMNB9ZtbtdqL (send_later one-shot, scheduled fire
2026-07-13T00:06:00Z, bound session_01UutkJqyMcHC1VyFW8fe1a9) never
delivered — still enabled and unfired 33+ min past run_once_at at capture.
The seat failsafe trig_01UQTZFvknBosXVo4YKKfazZ caught the stall (fired
2026-07-13T00:37:55Z); replacement pacemaker trig_01HRNuGwoSf1pR9nPhmE6QX7
(01:09Z) was armed at 00:38:31Z.

**Health run (`scripts/check_trigger_health.py`, eval at captured_at
2026-07-13T00:39Z): VERDICT FAIL — 2/7 red, exit 1.**

- I1 WEDGED-CRON **PASS** — no enabled cron frozen >15m past.
- I2 DROPPED-ONESHOT **FAIL** — two sessions with a dropped-or-queued tick:
  session_01UutkJqyMcHC1VyFW8fe1a9 (fleet-manager coordinator; the
  documented dropped tick above, due 00:06Z — failsafe already recovered
  the seat) and session_013CEaD81nh2E4wK1NsrKMPV (SuperBot World seat;
  trig_01Ufj7W9MvsMvboqTAALgWX8, work-loop tick due 00:14Z, unfired at
  capture; its own failsafe trig_0131tbQZs8HKmxKR4u5ZD1Hb is armed for
  01:15Z, so the failsafe net covers it — QUEUED-vs-LOST indistinguishable
  on the registry, coordinator to verify the seat responded).
- I3 DEAD-CHAIN **PASS** — every dropped-tick session has a future tick
  armed.
- I4 MANAGER-FAILSAFE **PASS** — trig_01UQTZFvknBosXVo4YKKfazZ
  (`30 */2 * * *`) healthy, next 02:37Z.
- I5 ROSTER-FRESH **PASS** (1.3h) · I6 SNAPSHOT-FRESH **PASS** (0.1h).
- I7 TICK-PILE-UP **FAIL** — two pile-ups. **Same-wake action taken = prune
  list for the coordinator (per R26 + tonight's dispatch: worker reports
  ids, does NOT delete):**
  - session_01Q5sGKgKCngGa7jgfzEGeEQ (Ideas Lab): keep NEWEST
    trig_01BWZxRpeqGdg46CCbAs8hYt (00:47Z), **prune
    trig_01Vsq76foscQRFz2YZNHpZCQ** (00:41Z) — same normalized work-loop
    text.
  - session_01UutkJqyMcHC1VyFW8fe1a9 (fleet-manager coordinator): keep
    NEWEST trig_01HRNuGwoSf1pR9nPhmE6QX7 (01:09Z), **prune
    trig_0123fu7onT7wGMNB9ZtbtdqL** (00:06Z, the dropped tick itself).
  - No wedged cron to headline (I1 clean). control/status.md recording left
    to the coordinator with the prune action (worker avoids racing the
    coordinator's wholesale heartbeat overwrites).

**Mid-session anomaly (for the coordinator):** a parallel worker created
`claude/v3-rider-fold` from this branch's tip and switched the shared
clone's HEAD mid-flight; this session's snapshot commit 8715bb0 briefly
landed under that checkout (and that branch, pushed at 154c237, now carries
this session's card + snapshot commits in its history). Resolved for this
lane by fast-forwarding `claude/night-watchdog-1` to 8715bb0 (my own
commit, parent = my card commit); the other branch was left untouched —
its PR will show this PR's files until it rebases.

**Merge posture:** per tonight's owner rule, no self-merge — the
merge-on-green sweep lands this PR (touches no workflows). ≤2 CI polls then
report.

## 💡 Session idea

`scripts/ingest_trigger_pages.py` — one-command snapshot transform. Tonight's
R26 export was ~10 manual steps: copy each oversized MCP page result file,
verify cursor-chain exhaustion by hand, dedupe, sort by id, hand-write the
delta capture_notes against the prior committed snapshot, match the committed
indent style. Every night-watchdog wake repeats this, and the checker's I6
depends on a correct top-level `captured_at` that is currently hand-derived
from tool-call epochs. A small stdlib script that takes the raw page files +
the prior committed snapshot and emits the schema-exact snapshot (validating
exhaustion: final page lacks `has_more`; refusing on cursor-overlap dupes)
plus a generated deleted/added/bound-resolution capture_notes skeleton would
cut the transform to one command and eliminate the merge-note drift class
the 20:41Z trimmed capture already exhibited. (Deduped: docs/ideas/ has no
snapshot/ingest/export-tooling idea; the nearest, order020 tick-pileup work,
is detection not ingestion.)

## ⟲ Previous-session review

The consolidation batch (PR #148) did the record-keeping right, and one
pattern from the 20:41Z snapshot it rode on paid off measurably tonight:
that capture's forward-looking note ("both reconcile in the next export" —
the failsafe cutover forecast) turned tonight's delta verification into a
checklist item instead of an investigation; predicted delta, observed delta,
done. Concrete workflow improvement: make that a doctrine line in R26 —
any known in-flight registry mutation at capture time gets a forecast
capture_note, so the next watchdog wake inherits assertions to check rather
than raw diffs to explain. One genuine gap in the consolidation session:
it ran the health checker against the then-current snapshot and reported
"PASS 7/7 at 20:41Z" without flagging that the snapshot was already ~3.5h
old at run time — within the I6 bar but close to it; stating snapshot age
next to a PASS verdict would make "PASS on stale basis" visibly different
from "PASS on fresh basis".
