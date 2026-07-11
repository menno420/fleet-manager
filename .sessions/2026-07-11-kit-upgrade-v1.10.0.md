# 2026-07-11 — kit: upgrade v1.9.0 → v1.10.0

> **Status:** `complete`

📊 Model: Claude (Fable family, fable-5) · start 2026-07-11T06:48Z · kit-seat
distribution worker (owner directive Q-0261.3)

## Declared at open (born-red)

Scope: substrate-kit upgrade v1.9.0 → v1.10.0, kit-owned files only (no lane
work, no control/ edits). Plan: stage the sha256-verified release asset
(`ba69fc5cf21619cc85e4c733ebe3d9eda8803e678f810fcc39b94d60c2f3b5a4`, three-way
verified against tag commit 1b5db16 and release run 29142780212) as
`bootstrap.py.new` + `release.json` → `python3 bootstrap.py.new upgrade` →
verify the four payload landings (session-card-hold in the regenerated gate;
retroactive model-doctrine append to this README; exactly one new
`bootstrap-1.9.0.py` bank; apply-docs carve-out section intact) → `check
--strict` exit 0 + exercise the new `check --simulate-added-card` → flip this
card `complete` as the deliberate LAST step → REST squash on green (R21
fallback path). NOTE: this card itself is the first live exercise of the
v1.10.0 born-red card-hold fix on this repo — the ADDED in-progress card must
HOLD the gate even before the upgrade payload lands.

## Shipped (close-out)

- **Upgrade landed (commit 611f2d5):** `bootstrap.py` v1.9.0 (sha256
  55181082…) → v1.10.0 (sha256 ba69fc5c…, byte-identical to the release asset
  and the kit's committed `dist/bootstrap.py` at tag v1.10.0);
  `kit_version: 1.10.0` recorded in `.substrate/state.json` +
  `substrate.config.json`.
- **All four payload verifications passed:** (1) regenerated
  `.github/workflows/substrate-gate.yml` added-card lane now HOLDs an ADDED
  in-progress card (engine finding `session-card-hold`) and runs
  `--simulate-added-card` on gate-touching PRs; (2) model-attribution doctrine
  APPENDED to the pre-existing `.sessions/README.md` under the provenance
  marker `<!-- substrate-kit: model-attribution doctrine … ORDER 012 -->`,
  host content preserved byte-for-byte; (3) exactly one new bank
  `.substrate/backup/bootstrap-1.9.0.py`, all four pre-existing banks
  byte-identical before/after; (4) carve-out section intact in
  `.substrate/upgrade-report.md` ("carve-out scan: … ran, 0 found").
- **Loophole fix exercised live, both sides:** gate run 210 (card-only diff,
  OLD v1.9.0 gate) went GREEN — the superbot-games #40 loophole demonstrated
  one last time pre-fix; gate run 211 (NEW gate, 611f2d5) went RED with the
  HOLD-by-design banner holding this very card, and its log carries the
  simulation verdict "the added-card lane would HOLD". R21 check-run wall did
  NOT recur (runs fired on every commit).
- `check --strict` red only on this card's designed hold (exit 0 expected once
  this flip lands); `--simulate-added-card` verified advisory-only both ways
  (HOLD on this in-progress card, PASS on a complete sibling card).

💡 Session idea: the gate's job log now shows the simulate-added-card verdict
only on gate-touching PRs; a one-line `check` summary token (e.g.
`added-card-lane: would-HOLD`) emitted on EVERY PR with an added card would
let roster/telemetry tooling grep lane behavior across the fleet without
opening job logs — cheap observability for the newest gate semantics.

⟲ Previous-session review: the roster-gen-5 session (#65) set the standard
this card follows — machine-generated claims verified cell-by-cell against
ground truth before trust. It did well pinning generator verification to the
Q-0105 header. Improvement it surfaces for the workflow: its
future-dated-heartbeat finding (product-forge) still relies on a human
reading the card; a `check`-level advisory that flags `updated:` timestamps
ahead of wall-clock would convert that one-off catch into an enforced guard.

Lane-owed (not done here, kit scope only): heartbeat `kit:` line in
`control/status.md` still says 1.9.0 → bump to `kit: v1.10.0`; the
pre-existing `owner-action-fields` advisory on `control/status.md` remains
open.
