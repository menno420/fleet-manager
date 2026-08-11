---
state: historical
origin: lab
shipped_pr: null
shipped_repo: null
merged_date: null
outcome: rejected
---

# Roster advisory: ARCHIVE-READY lanes with zero retro notes

> **Status:** `ideas`

**Captured 2026-07-11** (archive-prep closeout, PR #87) — grooming promotion
of the P3 session card's idea (`.sessions/2026-07-11-p3-coverage-index.md`
§ 💡), moved here so it survives in the backlog rather than orphaned in a
card.

## The idea

The evidence index (`docs/evidence-index.md`, generated with the roster)
already knows, per lane, whether `docs/retro/` exists and how many notes it
holds — but nothing alarms when a lane whose phase says ARCHIVE-READY /
close-out has **zero** retro notes. That is exactly the lane most likely to
lose its chat-only knowledge at archive (the class of loss this very
close-out slice exists to prevent, done by hand).

## Shape

A `gen_roster.py` advisory section listing lanes whose phase matches
archive/close-out vocabulary but whose evidence row shows `docs/retro/ = —`.
All data is already in the generated rows; estimated ~15 lines + a
`--selfcheck` pin. Advisory-only (no gate) — the roster's honest-signal
doctrine.

## Route

Quick-win, fleet-manager-side (`scripts/gen_roster.py`), no lane
coordination needed. Good first slice for the successor coordinator between
orders.

**Route died 2026-08-07 (recorded 2026-08-11, audit D68):** the roster this
advisory would write into was retired by owner directive — both regen cron
lines removed, `docs/roster.md` bannered "⛔ RETIRED … do not read the rows
below as the state of anything" — and the "successor coordinator" seat closed
with the program on 2026-07-21. Building it now would emit an advisory into a
file whose own header disclaims it, on a schedule that never fires. State
flipped `captured` → `historical`, outcome `rejected`; do not pull this
forward in a groom.
