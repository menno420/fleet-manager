# 2026-07-10 — substrate-kit upgrade v1.7.0 → v1.7.1

> **Status:** `in-progress`

📊 Model: kit-distribution worker (kit seat, substrate-kit v1.7.1 distribution wave) · start 2026-07-10T21:32Z (`date -u`)

## Declared at open (born-red)

Distribution worker landing the substrate-kit **v1.7.0 → v1.7.1** upgrade on
this repo, using the sha256-verified release asset (release.json sha256
`2aa4fedd…` confirmed against the downloaded `bootstrap.py`; tag `v1.7.1` →
commit `1cbd666a`; release run 29124338479 conclusion success). Scope — kit-owned
files only:

1. **Canonical upgrade**: `bootstrap.py.new` + `release.json` placed next to the
   vendored copy, `python3 bootstrap.py.new upgrade` (archive-first; the upgrade
   self-cleans both staging files).
2. **Kit-owned gate regeneration**: `.github/workflows/substrate-gate.yml`
   regenerated to the v1.7.1 kit-owned content; carve-out detection report read
   from `.substrate/upgrade-report.md`; pre-regen gate banked under
   `.substrate/backup/`.
3. **Verification before flip**: exactly one newly banked old dist
   (`bootstrap-1.7.0.py`, byte-equal to the pre-upgrade vendored copy — the #137
   spurious-backup regression check), `python3 bootstrap.py check --strict` green,
   diff contains kit-owned files + this card only.
4. **This card**, flipped `complete` as the deliberate last commit.

Landing: born-red card holds the gate red; upgrade commit next; gate run
pre-flip; flip last; REST squash-merge on the branch's substrate-gate run going
green (playbook R21 — auto-merge arming is a documented wall in this repo).

Out of scope (hard): `control/inbox.md`, `control/status.md` (the release
checklist's `kit:` heartbeat line is deliberately NOT touched by this worker —
flagged for the repo's own next session), all non-kit files.

## Done (close-out)

_(to be written at close)_
