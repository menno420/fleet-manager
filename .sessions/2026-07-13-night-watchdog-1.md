# 2026-07-13 — night watchdog 1 (R26 registry export + trigger health)

> **Status:** `in-progress`

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

(to be written)
