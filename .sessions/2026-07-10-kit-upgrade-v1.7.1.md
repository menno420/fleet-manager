# 2026-07-10 — substrate-kit upgrade v1.7.0 → v1.7.1

> **Status:** `complete`

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

## Done (close-out) · end 2026-07-10T21:37Z (`date -u`)

Declared scope landed exactly on PR #40 (born-red bd621a8 → upgrade a401cdf →
this flip):

- **Canonical upgrade executed**: `python3 bootstrap.py.new upgrade` with
  `release.json` adjacent (sha256/version verification ACTIVE, not skipped).
  Vendored `bootstrap.py` now `substrate-kit bootstrap v1.7.1`,
  `KIT_VERSION = "1.7.1"`, sha256 byte-equal to the release asset
  (`2aa4feddf7de7e20b00f46866826985ca8fd11f40bc51ebe261bbdef3118486d`);
  `substrate.config.json` + `.substrate/state.json` pins → `1.7.1`; staging
  files self-cleaned by the upgrade.
- **Kit-owned gate regenerated**: `.github/workflows/substrate-gate.yml` now
  byte-equal to the staged kit gate (`diff` clean vs
  `.substrate/ci/substrate-gate.yml`) — the previously-LATENT inbox
  append-only gate (`--inbox-base` wiring) is now live in both lanes.
- **Carve-out detector (first live exercise on this repo)**: zero host-added
  jobs/steps detected — clean regen, no `carve-out:` lines in
  `.substrate/upgrade-report.md` and no pre-regen bank (per the
  `gate_carveouts()` contract, banking fires only when host additions exist;
  a merely-stale gate regens clean).
- **#137 spurious-backup regression check PASSED**: exactly one banked old
  dist for this upgrade — `.substrate/backup/bootstrap-1.7.0.py`, byte-equal
  to the pre-upgrade vendored copy (sha256 `00f4f4cd…`) — and NO
  `bootstrap-1.7.1.py` spurious copy; `last-upgrade.json` names the archive
  (`from 1.7.0 → to 1.7.1`). (`bootstrap-1.4.0.py` predates this upgrade —
  the 1.4.0→1.7.0 hop's archive.)
- **Gate**: `python3 bootstrap.py check --strict` exit 0 pre-flip — the only
  session-log findings were the expected born-red markers this section
  supplies; the `owner-action-fields` advisory on `control/status.md` is
  pre-existing and out of this worker's scope.
- **Diff audit**: every changed file kit-owned (`bootstrap.py`,
  `substrate.config.json`, live gate, `.substrate/` state/report/backup/
  staged-CI/guard-fires) + this card. `control/` untouched.

Flagged for the repo's next session (NOT done here, hard scope):
`control/status.md` `kit:` heartbeat line still says v1.7.0 — update to
`kit: v1.7.1 · check: green · engaged: yes` per the release checklist.

## 💡 Session idea

**Teach `bootstrap upgrade` to emit an explicit "carve-outs: none" line in
`upgrade-report.md`.** This upgrade was the carve-out detector's first live
exercise here, and the report is silent when nothing is detected — a reader
(or a distribution worker verifying kit #137) cannot distinguish "detector ran,
found nothing" from "detector never ran" without reading `gate_carveouts()`
source. One unconditional report line (`gate regen: carve-outs detected: 0`)
makes the negative result auditable and costs nothing.

## ⟲ Previous-session review

Previous card (`2026-07-10-wake-heartbeat.md`, PR #28) did well: its
"Landing:" paragraph named the exact merge mechanics (poll workflow runs, not
commit statuses; REST squash on green) — this session reused that recipe
verbatim, which is the card format doing its job. Improvement it surfaces:
that landing recipe is re-typed by hand into every card; it belongs once in
`.sessions/README.md` (or the playbook R21 entry) as the canonical
born-red-landing snippet cards can point to instead of restating —
restatement is where drift will eventually creep in.

