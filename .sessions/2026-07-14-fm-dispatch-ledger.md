# 2026-07-14 — fm dispatch ledger (coordinator fan-out close-out)

> **Status:** `complete`

📊 Model: Fable 5 · start 2026-07-14 ·
coordinator-dispatched worker (dispatch-log truing + outbox completion note)

## Declared at open (born-red)

Close out the 2026-07-14 coordinator dispatch fan-out (provenance: fm
heartbeat baton PR #182; dispatch executed against fm main @ 780c81b):
(1) annotate the 7 "Pending lane writes" ledger rows in
`docs/dispatch-log.md` with dispatched/satisfied outcomes + PR numbers,
(2) add a dated dispatch-log entry for the fan-out, (3) append a
completion block to `control/outbox.md`. No inbox edits, no heartbeat
write, no lane writes.

## Close-out

**Shipped (this PR):**

- `docs/dispatch-log.md`: all 7 pending-lane-write rows annotated with
  outcomes — rows 1+2 superbot PR #2094 / ORDER 005 / MERGED (one ORDER);
  row 3 substrate-kit PR #361 / ORDER 020 / MERGED 04:12:59Z (premise
  check at kit `a4d858e`: sub-items a/b/c already satisfied lane-side,
  build items d+e live); row 4 idea-engine PR #396 / ORDER 010 / MERGED
  04:10:55Z; row 5 sim-lab PR #127 / ORDER 006 / MERGED 04:11:31Z
  (outbox grown 875KB→993KB); row 6 pokemon-mod-lab PR #82 / ORDER 007 /
  OPEN on merge-on-green; row 7 product-forge OWNER-GATED, not written
  (DARK by verdict, rides E#44). Plus a new dated section
  "2026-07-14 — early morning (coordinator dispatch fan-out)".
- `control/outbox.md`: appended dispatch-complete block (04:22:20Z) —
  6/7 rows dispatched as 5 lane PRs, no denials.

**Verify suite:** `check_roster_freshness.py` exit 0 (roster 0.4h old,
threshold 4h — no regen needed); `bootstrap.py check --strict` red ONLY
on the designed born-red hold + session-ender expectations, both cleared
by this flip commit.

**Rails held:** no `control/status.md` heartbeat write, no inbox edits,
no lane writes; only the named files touched.

## 💡 Session idea

The "Pending lane writes" pattern (a numbered deferral ledger inside
`docs/dispatch-log.md`, trued row-by-row after the fan-out) worked well
enough this cycle that it deserves a tiny checker: a script that greps
the newest `### Pending lane writes` section for numbered rows lacking a
`→ ✅ dispatched` / `→ ⏸` outcome line older than N days, and WARNs in
`check --strict`. Today nothing catches a deferral row that silently
never gets dispatched — the exact orphaned-write risk row 7 documents.
(Deduped against `docs/ideas/`: existing outbox/roster/owner-queue
checker ideas don't cover dispatch-log deferral aging.)

## ⟲ Previous-session review

The wake-0235Z session (Slices C+D) set this dispatch up unusually well:
its pending-lane-writes ledger carried one-line why-deferred context per
row, which made the fan-out relays and this truing pass mechanical — no
re-derivation needed. One genuine gap: two of its ledgered measurements
were already stale at dispatch time (sim-lab outbox ~875KB had grown to
993KB; kit sub-items a–c had been satisfied lane-side before the ORDER
went out). Concrete improvement: deferral rows that embed a measurement
or premise should carry a "measured-at SHA/time" token so the dispatcher
knows to re-verify rather than relay the number — the kit premise check
caught it this time only because the dispatch rails mandated a premise
check per row.
