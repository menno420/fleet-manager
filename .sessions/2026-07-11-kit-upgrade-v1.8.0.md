# 2026-07-11 — substrate-kit upgrade v1.7.1 → v1.8.0

> **Status:** `in-progress`

📊 Model: kit-distribution worker (kit seat, substrate-kit v1.8.0 distribution wave) · start 2026-07-11T00:51Z (`date -u`)

## Declared at open (born-red)

Distribution worker landing the substrate-kit **v1.7.1 → v1.8.0** upgrade on
this repo, using the sha256-verified release asset (release.json sha256
`28c5dcb6…c89b9b` confirmed against the downloaded `bootstrap.py`, size
625,066 bytes; tag `v1.8.0` → commit `63c6b39`; release run 29133041799).
Scope — kit-owned files only:

1. **Canonical upgrade**: `bootstrap.py.new` + `release.json` placed next to
   the vendored copy, `python3 bootstrap.py.new upgrade` (archive-first; the
   upgrade self-cleans both staging files).
2. **v1.8.0 payload verification**: unified claims convention
   (`control/claims/README.md` plant), setup-script contract
   (`scripts/env-setup.sh` plant — none exists here pre-upgrade, so plant,
   not skip), grammar constants, auto-merge enabler kit-owned — this repo has
   NO live enabler workflow pre-upgrade, so it must land STAGED under
   `.substrate/ci/` only, never live; kit #156 fixes: (a) explicit carve-out
   section even at zero carve-outs, (b) backup collision-banking with sha8
   dedup names, (c) gate hold-tightening, (d) code-span slot scan.
3. **Verification before flip**: exactly one newly banked old dist (the
   v1.7.1 copy, sha256 `2aa4fedd…`), existing backups
   (`bootstrap-1.4.0.py`, `bootstrap-1.7.0.py`) undisturbed,
   `python3 bootstrap.py check --strict` exit 0, diff contains kit-owned
   files + this card only.
4. **This card**, flipped `complete` as the deliberate last commit.

Landing: card-first-open (this card is the FIRST commit, PR opens READY on
it before the gate-modifying upgrade commit — the open event is the one
event verified to still fire a gate run); upgrade commit next; flip last;
REST squash-merge per playbook R21 (auto-merge arming is a documented wall
here, and post-gate-regen events produced zero runs on PR #40 — expect the
same wall).

Out of scope (hard): `control/inbox.md`, `control/status.md`, all non-kit
files, any lane/domain work.

## Done (close-out)

(pending — flipped at close)
