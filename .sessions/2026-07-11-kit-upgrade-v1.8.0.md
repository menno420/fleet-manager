# 2026-07-11 — substrate-kit upgrade v1.7.1 → v1.8.0

> **Status:** `complete`

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

## Done (close-out) · end 2026-07-11T01:00Z (`date -u`)

Declared scope landed exactly on PR #56 (born-red dabb143 → upgrade e69035f
→ this flip):

- **Canonical upgrade executed**: `python3 bootstrap.py.new upgrade` with
  `release.json` adjacent (sha256/version verification ACTIVE). Vendored
  `bootstrap.py` now `substrate-kit 1.8.0`, sha256 byte-equal to the release
  asset (`28c5dcb64b713dde8d64a513a9a1aa860b4a07bf17d832686f0009932dc89b9b`,
  625,066 bytes); `substrate.config.json` + `.substrate/state.json` pins →
  `1.8.0`; staging files self-cleaned.
- **v1.8.0 plants**: `control/claims/README.md` (unified claims convention;
  `claims_dir: control/claims` pinned in config; no legacy claims dir existed
  here — clean plant, no migration advisories) and `scripts/env-setup.sh`
  (setup-script contract; no `scripts/` existed pre-upgrade, so plant, not
  skip — skip-if-exists therefore not exercised here).
- **Auto-merge enabler — STAGED, not live (correct case)**: no enabler
  workflow was live pre-upgrade, so it landed only at
  `.substrate/ci/auto-merge-enabler.yml`; `.github/workflows/` still contains
  exactly `substrate-gate.yml`. Config gained the `automerge` block
  (`claude/*` → required context `substrate-gate`).
- **Kit #156 fixes, first fleet exercise here**:
  (a) `.substrate/upgrade-report.md` now has an explicit `## Carve-out scan`
  section — `ran, 0 found` — the negative result is auditable (exactly the
  v1.7.1 session's 💡 idea, shipped);
  (b) collision-banking: clean bank (no name collision), exactly one new
  archive `.substrate/backup/bootstrap-1.7.1.py` byte-equal to the
  pre-upgrade vendored dist (sha256 `2aa4fedd…`); `bootstrap-1.4.0.py` /
  `bootstrap-1.7.0.py` hashes unchanged; sha8 dedup path
  (`bootstrap-<ver>.<sha8>.py`, bootstrap.py §_archive) present but not
  triggered;
  (c) gate hold-tightening LIVE in the regenerated gate: an ADDED card in a
  PR that also touches the gate workflow keeps the FULL locked door — this
  very PR is held red until this flip (semantics may only tighten mid-PR);
  (d) code-span-aware unrendered-slot scan present in the dist.
- **Diverged doc (NOT auto-applied, per kit contract)**: `control/README.md`
  is consumer-edited AND the template moved (claims-convention section +
  grammar-constants pointers) — the kit surfaced the delta in the upgrade
  report for the repo's own next session to merge manually. This worker does
  not touch control/ docs (hard scope).
- **Gate**: `python3 bootstrap.py check --strict` — the only findings
  pre-flip were this card's expected born-red markers; the
  `owner-action-fields` advisory on `control/status.md` is pre-existing,
  advisory-only, and out of this worker's scope.
- **Diff audit**: every changed file kit-owned (`bootstrap.py`, config, live
  gate, `.substrate/` state/report/backup/staged-CI/guard-fires, plants) +
  this card. `control/inbox.md` + `control/status.md` untouched.

Flagged for the repo's next session (NOT done here, hard scope):
(1) `control/status.md` `kit:` heartbeat line still says v1.7.1 — update to
`kit: v1.8.0 · check: green · engaged: yes`; (2) merge the
`control/README.md` template delta (claims convention + grammar-constants
pointers) from the upgrade report's diff block.

## 💡 Session idea

**Make `upgrade` print a one-line "staged vs live" verdict for the auto-merge
enabler.** v1.8.0's enabler is kit-owned with a staged-by-default/live-where-
already-live split, but the upgrade output only says
`staged: .substrate/ci/auto-merge-enabler.yml` — a distribution worker must
independently `ls .github/workflows/` to prove the live/staged case was
decided correctly. One explicit line (`enabler: staged only (no live enabler
pre-upgrade)` / `enabler: regenerated LIVE at .github/workflows/…`) makes the
fleet's per-repo verification mechanical and the wrong-case failure
(accidentally going live) loudly visible in the report.

## ⟲ Previous-session review

Previous card (`2026-07-11-owner-codex-fleetwide.md`, PR #54) did well:
crisp ORDER propagation with per-repo evidence links. The prior *kit* card
(`2026-07-10-kit-upgrade-v1.7.1.md`, PR #40) deserves the real review here:
its 💡 idea (explicit carve-out line even at zero) shipped upstream as kit
#156(a) and this session consumed it — the idea loop demonstrably closes.
Improvement it surfaces: its landing-note prediction ("no gate run fires on
any post-gate-regen event") is repo-critical knowledge that still lives only
in a session card and playbook R21 prose; this session re-verified it by
hand. `docs/capabilities.md` should carry it as a tested wall entry with the
discovery rule, so distribution workers stop re-deriving it each wave.
