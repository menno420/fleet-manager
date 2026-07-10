# 2026-07-10 — Launch-readiness compiler (Q-0261 finalize-first checklist)

> **Status:** `in-progress`

📊 Model: compiler worker for the coordinator's launch-readiness deliverable (seat-based; model line intentionally generic — no model identifiers in this PR)

## Declared at open (born-red)

Compiler worker for the fleet-manager coordinator's launch-readiness deliverable
(owner dispatch, Q-0261 finalize-first relaunch). Five research reports (context
scout · fm+kit · superbot+superbot-next · product lanes · game+codetool lanes,
swept ~15:10–15:40Z at each repo's HEAD) are the source material. About to land
TWO files:

1. **`docs/launch-readiness-2026-07-10.md`** — the ONE committed checklist of
   everything to answer/click/fix/dispatch before each Project relaunches under
   the Q-0261 finalize-first order: fleet-wide items stated once
   (routine-vs-archive decision, kit-version table, settings-API wall), one
   section per seat/repo in Q-0261 order with a one-line verdict each, and a
   final routing table mapping every AGENT-DOABLE item to a boot or an ORDER,
   plus per-class totals. Citations (file@SHA / PR / commit) preserved from the
   research reports on every carried claim.
2. **`docs/owner-queue.md`** — deduped update: the genuinely new owner-only
   items from this research added in the existing six-field format (product-forge
   repo+Project, sixth-seat naming, kit OA8 setup-script paste, settings-sweep
   additions, codetool archive/cfgdiff clicks parked); no valid existing item
   removed.

Landing: born-red card holds the gate red; doc + queue commit next; gate run
(`python3 bootstrap.py check --strict --require-session-log --session-log
<this card>`) before the flip; flip last; PR ready (not draft); REST
squash-merge on the branch's substrate-gate Actions run going green (poll
workflow runs, not commit statuses).
