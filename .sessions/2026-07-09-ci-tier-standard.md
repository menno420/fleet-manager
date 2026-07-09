# 2026-07-09 — CI-tier standard: sim-backed 3-tier CI doctrine + blueprint amendment

> **Status:** `complete`

📊 Model: Claude Fable 5 (claude-fable-5) · docs + tooling session · night (~23:35–23:45Z)

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

## Done (all four, this PR)

- **Simulator committed** at `tools/sim/ci_tier_sim.py` verbatim from the
  research worker; `python3 tools/sim/ci_tier_sim.py --self-test` run in the
  repo copy before commit — **15/15 invariants green**.
- **Findings** at `docs/findings/ci-tier-sim-2026-07-09.md` (`reference`),
  header artifacts rewritten to committed repo paths (results.{json,md} stay
  uncommitted — byte-identical regenerable via the sweep command); README
  index row added.
- **Blueprint §2b CI-TIER STANDARD** inserted between §2a (wake cadence) and
  §3 (owner setup), with provenance line, changelog entry, §1 checklist
  cross-ref ("CI tier assigned at repo birth — per §2b"), and §3 ruleset
  item now citing the sim's up-to-date-rule numbers. Sim-vs-prior
  disagreements flagged inline: **Tier 1 labs = fast-full** (whole suite in
  one ≤60s cell + nightly matrix — labs' full suites already run at smoke
  speed, 22–45s, so a smoke subset buys nothing), **Tier 0 born-red repos
  keep the 11s substrate-gate** (enforcement of the card hold, not
  detection), **Tier 2 full per-PR stands** with riders (never require
  up-to-date branches; the 5–7 min Code Quality wall is the next cost
  target).
- **`environments/templates/smoke.yml`** — the fast-full reference workflow
  (PR+main triggers only to kill the double-fire, concurrency-cancel, 3-min
  stall guard, `smoke` as the required-context name); environments README
  map row added.

## Landing note

Born-red the whole session (local `bootstrap.py check --strict` confirmed the
hold: missing close-out markers until this flip); no arm attempt (R21 — this
repo's shape refuses it); landed via REST merge-on-green after this flip.

## 💡 Session idea

**Tier line in `control/status.md` + a tier column in the environment
archetype map:** the blueprint now defines CI tiers, but nothing *records*
which tier each live lane is on — the next auditor must re-derive it from
each repo's workflows. A one-line `ci-tier: 0|1|2` field in each lane's
status/control header (and a column in `environments/archetypes.md`'s
project→archetype table) would make tier drift visible at a glance and give
the §2b escalation rule ("graduates to Tier 2 when merges become deploys")
something concrete to flip.

## ⟲ Previous-session review

The PR #11 session (idea capture ×9 + R21 + handoff) was a model close-out:
it practiced the rule it wrote (landed via REST merge-on-green, zero arm
attempts) and its card said so explicitly — doctrine and behavior in the same
diff. Two genuine improvables: (1) its 9 idea files were captured with
routing destinations but no *sizing* signal (a one-word S/M/L on each would
let the grooming pass pick by available capacity, not by re-reading all
nine); (2) its R21 playbook text and the blueprint alignment shipped in one
commit with the handoff updates — three concerns in one commit made the
`git show` review of the *rule* change noisier than it needed to be;
rule-changes deserve their own commit even inside a batched PR (adopted
here: sim / findings / blueprint / template each landed as separate commits).
