# 2026-07-11 — kit: upgrade v1.10.0 → v1.10.1

> **Status:** `in-progress`

📊 Model: Claude (Fable family, fable-5) · start 2026-07-11T08:0xZ · kit-seat
distribution worker (owner directive Q-0261.3)

## Declared at open (born-red)

About to upgrade kit v1.10.0 → v1.10.1. Scope: substrate-kit upgrade only,
kit-owned files (bootstrap.py, .github/workflows/substrate-gate.yml,
.substrate/*) — no lane work, no control/inbox.md or control/status.md edits.
Plan: stage the sha256-verified release asset
(`fbe83ce35d1fb3b544ac58fc60ee2609eaa6c69c13d77883e9fdc5da6bbad158`, three-way
verified) as `bootstrap.py.new` + `release.json` → `python3 bootstrap.py.new
upgrade` → verify the payload landings (gate tail-1 multi-card shadowing fix:
every card in the diff graded, added in-progress card HOLDs, modified-sibling
advisory; emphasis-blind `_MODEL_DOCTRINE_PHRASE`; exactly one new
`bootstrap-1.10.0.py` bank; carve-out scan ran with 0 found; doctrine
idempotent — no duplicate README append) → `check --strict` exit 0 +
`check --simulate-added-card` → flip this card `complete` as the deliberate
LAST step, deleting the claim in the same commit.
