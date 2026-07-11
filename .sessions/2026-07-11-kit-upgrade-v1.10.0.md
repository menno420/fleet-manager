# 2026-07-11 — kit: upgrade v1.9.0 → v1.10.0

> **Status:** `in-progress`

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
