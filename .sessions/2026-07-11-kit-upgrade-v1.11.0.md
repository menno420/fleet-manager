# 2026-07-11 — kit: upgrade v1.10.1 → v1.11.0

> **Status:** `complete`

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

## Shipped (close-out)

- **Upgrade landed (commit 8b0872d):** `bootstrap.py` v1.10.1 (sha256
  fbe83ce3…) → v1.11.0 (sha256 c339bd6a…, byte-identical to the verified
  release asset); `kit_version: 1.11.0` in `bootstrap.py:90`,
  `substrate.config.json:47`, `.substrate/state.json:10`.
- **All payload verifications passed:** (1) HANDOFF.md composer in dist
  (`HANDOFF_POINTER_FILENAME` at bootstrap.py:4885, marker-guarded,
  host-owned copies never touched); (2) planted CLAUDE.md read-first rider
  present in the staged `.substrate/claude/CLAUDE.md:16` (`HANDOFF.md` at
  slot 2) — **staged only: fleet-manager has NO live CLAUDE.md**, see
  lane-owed below; (3) gate action pins bumped post-regen —
  `.github/workflows/substrate-gate.yml:21` `actions/checkout@v5`, `:80`
  `actions/setup-python@v6` (live gate byte-identical to the new staged
  template); (4) guard-fires dedupe present
  (`GUARD_FIRES_DEDUPE_WINDOW_S = 600`, bootstrap.py:4502); (5) `kit:`
  heartbeat grammar leniency (`KIT_LINE_RE` bootstrap.py:752 now accepts
  optional list marker / bold label); (6) exactly one new bank
  `.substrate/backup/bootstrap-1.10.1.py` (sha256 fbe83ce3…), all six
  pre-existing banks byte-identical before/after.
- **Carve-out scan anomaly (false positive, no action needed):** the scan
  flagged the OLD kit pins (`checkout@v4`, `setup-python@v5`) as host-added
  steps and banked `substrate-gate.pre-regen-4f50eb4d.yml`. The banked
  pre-regen live gate is byte-identical to the old kit-owned staged template
  — zero real host additions existed; the "carve-outs" are the kit's own
  pin bump seen by a detector that diffs against the NEW template. Nothing
  moved to host-ci.yml (there is nothing to move). Kit-side idea: teach the
  carve-out detector to ignore steps that match the OUTGOING template.
- `check --strict` bare = designed born-red HOLD on this card;
  pinned to the previous complete card = exit 0, "all checks passed"
  (only the pre-existing `owner-action-fields` advisory, never
  exit-affecting).

💡 Session idea: the upgrade engine already knows the outgoing template's
byte content (it banks it) — the carve-out scanner should three-way compare
(live vs old-template vs new-template) instead of two-way (live vs new), so
kit-authored template evolution (like this release's action-pin bump) can
never masquerade as a host carve-out and scare an upgrade session into
inventing a host-ci.yml.

⟲ Previous-session review: the v1.10.1 card (#70) again made this run
mechanical — its structured before/after bank hashes were directly reusable.
Improvement it surfaces, now proven twice: its own suggestion of a
machine-checkable `verified:` field (asset sha / tag commit / release run)
still isn't a kit feature; two consecutive cards carrying the same prose
verification is the signal it should graduate into the upgrade-report
template itself.

Lane-owed (not done here, kit scope only): fleet-manager has NO live
CLAUDE.md (kit copy staged at `.substrate/claude/CLAUDE.md`) — the v1.11.0
planted-CLAUDE.md read-first rider (the run-6 delivery-gap fix) cannot reach
workers here until the lane adopts a live CLAUDE.md; heartbeat `kit:` line
in `control/status.md` needs its bump to v1.11.0; the pre-existing
`owner-action-fields` advisory on `control/status.md` remains open.
