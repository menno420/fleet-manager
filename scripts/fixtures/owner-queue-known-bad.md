# Owner queue — KNOWN-BAD fixture (check_owner_queue.py must FLAG)

> **Status:** `fixture` — Q-0120 ground-truth fixture for
> `scripts/check_owner_queue.py` (P2, fleet-manager PR #85). Historical
> shape: both items below are modeled on REAL 2026-07-11 queue drift —
> they cite PRs that genuinely MERGED earlier that day
> (fleet-manager #76 merged 15:26:47Z; superbot-games #34 merged
> 13:40:40Z), exactly the "already-satisfied ask" class the checker
> exists to catch. A clean run against this file means the checker is
> BROKEN — do not "fix" the fixture to make it pass.

## Active queue — grouped by click surface

### (A) GitHub merges — one click each

1. **superbot-games PR #34 — collection scope: MERGE.**
   - id: OQ-FIXTURE-GAMES-PR34-MERGE
   - WHERE: https://github.com/menno420/superbot-games/pull/34
   - HOW: click "Squash and merge".
   - UNBLOCKS: per-suite floors on main.
   - VERIFIED-NEEDED: fixture — this PR truly merged 2026-07-11T13:40:40Z
     (merge `5147a23`); the checker must fire [merged-citation].
   - Blocking: not-blocking.

### (B) Hot items

2. **🔥 HOT — land the corrected UNIVERSAL.md merge-authority clause.**
   - id: OQ-FIXTURE-UNIVERSAL-CLAUSE
   - **STATUS: ✅ RESOLVED — RESOLVED-PENDING-MERGE of PR #76**
     (https://github.com/menno420/fleet-manager/pull/76 — the rebuilt
     payload). The owner merges #76 personally.
   - WHERE: `projects/UNIVERSAL.md` on menno420/fleet-manager.
   - HOW: merge PR #76 on green.
   - UNBLOCKS: ORDER 017 + the paste wave.
   - VERIFIED-NEEDED: fixture — fm #76 truly merged 2026-07-11T15:26:47Z
     (merge `e1848ff`); the checker must fire [resolved-not-swept].
   - Blocking: no longer blocking.

## Resolved (fixture tail — outside the active region, never scanned)

- A resolved entry citing https://github.com/menno420/fleet-manager/pull/76
  must NOT double-flag from down here.
