# 2026-07-09 — CI-tier standard: sim-backed 3-tier CI doctrine + blueprint amendment

> **Status:** `in-progress`

📊 Model: Claude Fable 5 (claude-fable-5) · docs + tooling session · night (~23:35Z)

## Declared at open (born-red)

Land the fleet's CI-tier standard, backed by tonight's calibration + simulation
run (451 PRs / ~1250 CI runs mined across 10 fleet repos; 144-cell × 40-seed
discrete-event sim):

1. `tools/sim/ci_tier_sim.py` — the stdlib-only, deterministic simulator
   (self-test 15/15 green in this repo copy before commit).
2. `docs/findings/ci-tier-sim-2026-07-09.md` — calibration data, results
   tables, crossovers, honest limitations, 3-sentence recommendation;
   findings README indexed.
3. `docs/gen2-blueprint.md` — new **CI-TIER STANDARD** section (Tier 0 docs
   no-CI + born-red gate hold; Tier 1 labs FAST-FULL, adjusted from the
   smoke-only prior; Tier 2 prod full per-PR with sim-quantified riders),
   provenance: owner directive 2026-07-09 + the findings doc.
4. `environments/templates/smoke.yml` — the Tier-1 fast-full reference
   workflow template; environments README map row.

Landing: born-red card holds the gate red; card flips `complete` as the last
commit; lands via REST merge-on-green (R21 — no arm attempt, this repo is
born-red by design).
