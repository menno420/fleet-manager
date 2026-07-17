# Owner queue — KNOWN-GOOD fixture (check_owner_queue.py must come back CLEAN)

> **Status:** `fixture` — Q-0120 ground-truth fixture for
> `scripts/check_owner_queue.py` (P2, fleet-manager PR #85; converted to the
> 2026-07-17 wind-down inline-slug bullet format in fm PR #288). Items below
> are healthy: a merge-actionable item citing a PR that was genuinely OPEN
> at fixture-authoring time (fleet-manager #85 — the P2 PR itself, live
> while this fixture was built), plus a non-merge item with no PR
> citation. **The offline `--selftest` pins #85's state as open and never
> rots**; a LIVE run of this fixture flags once #85 lands — that is the
> checker working, not breaking (an earlier draft cited substrate-kit
> #181 as the "stays open" PR; the owner ratified it at 14:56:40Z the
> same day — in this fleet everything healthy eventually merges, so no
> live citation stays green forever). Any `--selftest` flag on this file
> is a checker false-positive — investigate the checker, not the fixture
> (Q-0120: a red that fights visible evidence is the tool's bug).

## Active — grouped by click surface

### (A) GitHub merges — one click each

- **`OQ-FIXTURE-FM-PR85-MERGE` — fleet-manager PR #85 — P2 queue generation: MERGE.**
  WHERE: https://github.com/menno420/fleet-manager/pull/85 · HOW: click "Squash and merge".
  UNBLOCKS: the P2 deliverables on main.
  VERIFIED-NEEDED: fixture — OPEN at fixture time (2026-07-11 ~21:0xZ); state pinned open in
  `--selftest`. Blocking: not-blocking.

### (D) External services

- **`OQ-FIXTURE-VENTURE-STRIPE-KEYS` — venture-lab — Stripe TEST keys.**
  WHERE: Stripe Dashboard (test mode) → Developers → API keys.
  HOW: paste `sk_test_…` into the server `.env` (never committed).
  UNBLOCKS: the only unverified leg of the payment path.
  VERIFIED-NEEDED: payment accounts/keys are owner-only (hard rail).
  Blocking: blocks payment-path E2E verification.
