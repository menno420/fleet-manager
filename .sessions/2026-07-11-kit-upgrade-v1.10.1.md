# 2026-07-11 — kit: upgrade v1.10.0 → v1.10.1

> **Status:** `complete`

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

## Shipped (close-out)

- **Upgrade landed (commit 225613e):** `bootstrap.py` v1.10.0 (sha256
  ba69fc5c…) → v1.10.1 (sha256 fbe83ce3…, byte-identical to the verified
  release asset); `kit_version: 1.10.1` recorded in `.substrate/state.json` +
  `substrate.config.json`; `last-upgrade.json` from 1.10.0 → to 1.10.1.
- **All payload verifications passed:** (1) regenerated
  `.github/workflows/substrate-gate.yml` — the `tail -1` card picker is GONE,
  replaced by per-card `while` loops that grade EVERY card in the diff (added
  in-progress card HOLDs; sibling cards modified alongside an add are
  advisory-only, never grade-affecting; modify-only diffs keep the full
  locked door per card; gate-touching PRs keep the locked door on added cards
  too); (2) doctrine idempotent — `.sessions/README.md` byte-identical
  before/after (sha256 2abe859a…), no duplicate append; (3) exactly one new
  bank `.substrate/backup/bootstrap-1.10.0.py`, all five pre-existing banks
  (1.4.0/1.7.0/1.7.1/1.8.0/1.9.0) byte-identical before/after; (4) carve-out
  scan ran, 0 found (`.substrate/upgrade-report.md`).
- **Gate exercised live:** run 216 (card-only, e86fcd4) RED on the designed
  `session-card-hold` born-red finding; run 217 (upgrade commit, 225613e) ran
  the NEW gate's locked-door lane (gate-touching PR) with the
  `--simulate-added-card` verdict "the added-card lane would HOLD" in the log,
  red only on this card's designed hold.
- `check --strict` exit 0 when pinned to a complete card;
  `--simulate-added-card` verified advisory-only (exit 0 while reporting
  would-HOLD).

💡 Session idea: the gate's per-card loop now prints one
"modified sibling card (advisory…)" line per shadow candidate — a
fleet-roster grep target; a kit-side counter token (e.g.
`sibling-advisories: N`) in the check summary would let telemetry spot repos
where sessions habitually backfill sibling cards (a discipline smell) without
parsing job logs.

⟲ Previous-session review: the v1.10.0 upgrade card (#69) set the exact
template this session reused — its hash-before/after bank discipline and
live both-sides gate exercise made this run mechanical. One improvement it
surfaces: it recorded the asset's three-way verification inline in the card
prose; a structured `verified:` field (asset sha, tag commit, release run)
would make that machine-checkable by roster tooling instead of prose-greppable.

Lane-owed (not done here, kit scope only): heartbeat `kit:` line in
`control/status.md` still says an older version → bump to `kit: v1.10.1`;
the pre-existing `owner-action-fields` advisory on `control/status.md`
remains open.
