# 2026-07-11 — kit: upgrade v1.10.1 → v1.11.0

> **Status:** `in-progress`

📊 Model: Claude (Fable family, fable-5) · start 2026-07-11T13:0xZ ·
distribution worker (owner directive Q-0261.3)

## Declared at open (born-red)

About to upgrade kit v1.10.1 → v1.11.0. Scope: substrate-kit upgrade only,
kit-owned files (bootstrap.py, .github/workflows/substrate-gate.yml,
.substrate/*) — no lane work, no control/inbox.md or control/status.md edits.
Plan: stage the sha256-verified release asset
(`c339bd6a2eb3a139dd0106d5fd3873eb2d067f79723fccb5781d4e72a74a8d29`, three-way
verified: tag v1.11.0 → 640f8a1a, release run 29152928040 success, asset
digest match) as `bootstrap.py.new` + `release.json` → `python3
bootstrap.py.new upgrade` → verify the v1.11.0 MINOR payload landings
(HANDOFF.md composer in dist; planted CLAUDE.md read-first rider staged —
note fleet-manager has NO live CLAUDE.md; gate action pins bumped to
`actions/checkout@v5` + `actions/setup-python@v6` post-regen; guard-fires
10-minute dedupe; `kit:` heartbeat bullet/bold-label grammar leniency;
exactly one new `bootstrap-1.10.1.py` bank with all six pre-existing banks
byte-identical; carve-out scan ran) → `check --strict` exit 0 → flip this
card `complete` as the deliberate LAST step, deleting the claim in the same
commit.
