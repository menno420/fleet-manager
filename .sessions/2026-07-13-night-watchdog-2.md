# 2026-07-13 — night watchdog 2 (R26 registry export + trigger health)

> **Status:** `in-progress`

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
