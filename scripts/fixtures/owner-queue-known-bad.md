# Owner queue — KNOWN-BAD fixture (check_owner_queue.py must FLAG)

> **Status:** `fixture` — Q-0120 ground-truth fixture for
> `scripts/check_owner_queue.py` (P2, fleet-manager PR #85; converted to the
> 2026-07-17 wind-down inline-slug bullet format in fm PR #288). Historical
> shape: the items below are modeled on REAL 2026-07-11 queue drift —
> they cite PRs that genuinely MERGED earlier that day
> (fleet-manager #76 merged 15:26:47Z; superbot-games #34 merged
> 13:40:40Z), exactly the "already-satisfied ask" class the checker
> exists to catch. A clean run against this file means the checker is
> BROKEN — do not "fix" the fixture to make it pass.

## Active — grouped by click surface

### (A) GitHub merges — one click each

- **`OQ-FIXTURE-GAMES-PR34-MERGE` — superbot-games PR #34 — collection scope: MERGE.**
  WHERE: https://github.com/menno420/superbot-games/pull/34 · HOW: click "Squash and merge".
  UNBLOCKS: per-suite floors on main.
  VERIFIED-NEEDED: fixture — this PR truly merged 2026-07-11T13:40:40Z (merge `5147a23`);
  the checker must fire [merged-citation]. Blocking: not-blocking.
- **`OQ-FIXTURE-FM-PR227-PARKED-ROT` — fleet-manager PR #227 — lanes.json regen fix: MERGE.**
  WHERE: https://github.com/menno420/fleet-manager/pull/227 · HOW: click "Squash and merge".
  UNBLOCKS: lanes.json generation-lag fix on main.
  VERIFIED-NEEDED: fixture — modeled on the REAL A#63 rot (fm #227's one-click claim rotted
  when roster cron #231 / Gen #59 advanced main past it, 2026-07-15T12:04Z; state pinned in
  `--selftest`); the item text deliberately does NOT name the rotted state, so the checker must
  fire the check-1b parked-rot flag. (The two acknowledgment trigger words — and the flag's own
  name, which contains one — are avoided in this item's text on purpose: naming the rotted state
  would trip the check-1b downgrade to a note.) Blocking: not-blocking.

### (B) Hot items

- **`OQ-FIXTURE-UNIVERSAL-CLAUSE` — 🔥 HOT — land the corrected UNIVERSAL.md merge-authority clause.**
  **STATUS: ✅ RESOLVED — RESOLVED-PENDING-MERGE of PR #76**
  (https://github.com/menno420/fleet-manager/pull/76 — the rebuilt payload). The owner merges
  #76 personally. WHERE: `projects/UNIVERSAL.md` on menno420/fleet-manager. HOW: merge PR #76 on
  green. UNBLOCKS: ORDER 017 + the paste wave.
  VERIFIED-NEEDED: fixture — fm #76 truly merged 2026-07-11T15:26:47Z (merge `e1848ff`); the
  checker must fire [resolved-not-swept]. Blocking: no longer blocking.

### (C) Settings toggles

- **`OQ-FIXTURE-MINEVERSE-PYTEST-REQUIRED` — superbot-mineverse — make the test suite blocking.**
  WHERE: https://github.com/menno420/superbot-mineverse settings → Rules → main ruleset.
  HOW: add `pytest` as a required status check on main.
  UNBLOCKS: red suites can no longer land.
  VERIFIED-NEEDED: fixture — modeled on the REAL INC-06 drift
  (OQ-MINEVERSE-PYTEST-REQUIRED-CHECK survived 3 days after the owner clicked it 2026-07-11; live
  contexts `["substrate-gate","pytest"]`, Actions run 29260140367); the checker must fire
  [satisfied-required-check-ask]. Blocking: not-blocking.

## Resolved (fixture tail — outside the active region, never scanned)

- A resolved entry citing https://github.com/menno420/fleet-manager/pull/76
  must NOT double-flag from down here.
