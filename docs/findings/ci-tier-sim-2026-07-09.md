# CI-tier simulation — findings (2026-07-09)

> **Status:** `reference`
> **Provenance:** owner directive 2026-07-09 (CI-tier decision) + calibration mined
> the same night (451 PRs, ~1250 CI runs across 10 fleet repos, read-only GitHub MCP).
> **Artifacts (committed):** [`tools/sim/ci_tier_sim.py`](../../tools/sim/ci_tier_sim.py)
> (stdlib-only, deterministic), the CI-TIER STANDARD section in
> [`gen2-blueprint.md`](../gen2-blueprint.md), and the Tier-1 fast-full workflow
> template [`environments/templates/smoke.yml`](../../environments/templates/smoke.yml).
> **Reproduce:** `python3 tools/sim/ci_tier_sim.py --sweep --seeds 40 --out-prefix results`
> regenerates `results.json` / `results.md` (the full per-cell tables; not committed —
> byte-identical on re-run); `--self-test` passes 15/15 invariants.

## 1. Question

Which CI regime should each repo class run during autonomous free-window bursts?

- **R0 no-CI** — merge instantly; breakage invisible until the promotion point at window end.
- **R1 smoke-only** — one fast check per PR + nightly full suite + promotion gate.
- **R2 full per-PR** — calibrated full CI as required check, auto-merge/arm mechanics.
- **R3 batch-only** — no per-PR checks; single full run at window end.

Prior to test (owner 2026-07-09): Tier 0 docs/coordination = no CI; Tier 1 labs =
smoke-only; Tier 2 production = full per-PR.

## 2. Calibration highlights (mined numbers the sim is built on)

- **Arrivals are burst-shaped:** labs 1.87–3.13 PRs/h sustained over 5.7–7.0h active
  spans, hourly-bucket p95 3.7–7.0/h; superbot 1.95/h, burst p95 3.83/h. Sim sweeps
  1×/2×/4× a class base rate (docs 1.9, lab 2.5, prod 2.0/h) over an 8h window —
  4× lab = 10/h, beyond the observed max (~7/h).
- **Check walls:** substrate-gate 9–14s; lab matrices 22–45s wall (3–5 cells,
  ~2 machine-min with the verified 2× push+PR double-fire — fable5 PR #9: 10 check
  runs for 1 head; opus4.8: 42 runs / 22 PRs); superbot Code Quality 337s wall on a
  real code PR (#1907), CodeQL 210s parallel → prod full round 330–450s wall,
  ~10 machine-min.
- **Born-red is a HOLD, not flakiness.** Raw gate failure rates of 20–35% (superbot
  Code Quality 35%, substrate-kit CI 30%, fleet-manager substrate-gate 26%, websites
  27%) are deliberate session-card holds (Q-0133 convention; failures timestamped at
  PR-open). **True post-flip failure is ≤2%**: CodeQL 1.6%, labs 0 red in 83 runs,
  trading-strategy 0–8% (one draft episode). The sim models born-red as a hold state
  with arm-refusal ("unstable status", R21) and measures latency from card-flip.
- **Arm/landing mechanics:** arm refused on born-red and no-check repos (R21,
  fleet-manager PR #10's 3 failed attempts; venture-lab PR #1); GraphQL quota
  exhausts ~hourly (R8) → REST merge-on-green fallback (agent poll). Modeled: quota
  dies U(30,55) min into each hour; unarmed landings pay a 0.3–1.5 min poll delay.
- **Stall-not-fail:** 1/42 lab runs permanently queued (macos-13 hang) → modeled as
  p_stall ≈ 1% with 10-min timeout + redispatch. Zero superseded-run cancels found
  in any sampled window (push-batching holds), so supersede-cancel is not modeled.
- **Up-to-date two-round tier:** superbot-next (6 required checks + up-to-date rule)
  measured ~14 min dispatch→main when main advances mid-flight. The sim's prod class
  reproduces this endogenously: R2 at 4× traffic → median latency 12.3 min (validation
  anchor). No-check merges: sim medians 0.56–0.60 min vs mined 0.6–0.7 min.

## 3. Method

Discrete-event simulation of one repo lane per class over an 8h burst window;
Poisson arrivals at the calibrated class rate × traffic multiplier; 40 seeds/cell
(≥20 required); common-random-number workloads so regimes within a cell see the
identical PR stream. Fully deterministic (hashlib-derived seeds, no wall clock;
sweep re-run diffs byte-identical).

**Breakage injection** (the key unknown — swept): each PR broken with p ∈
{0.003, 0.01, 0.03, 0.08} (0.3% added below the asked 1/3/8% to locate the Tier-0
boundary). Split **60% smoke-catchable** (import/boot/syntax/config/`check --strict`
class — the *only* true failures observed in the mined night were exactly this
class) / **40% full-suite-only** (behavioral; needs the full suite). Sensitivity at
40/60/80% reported below.

**Cascade:** every PR merged while ≥1 undetected break sits on main = cascaded
damage. **Debt:** breaks still undetected at window end (revealed by the nightly/
batch run, or ad hoc at promotion for R0).

**Composite damage score** (agent-minutes; raw metrics reported alongside):

```
damage = severity × (8·caught_premerge + 30·cascaded + (20+attrib)·escaped) + wait
severity: docs 0.25 · lab 1.0 · prod 3.0   (prod: merge IS deploy, Q-0193)
attrib:   +5 when an end-of-window run localizes the break (R1/R3), +15 ad hoc (R0)
wait:     merge latency charged only on unarmed landing paths (R4 foreground waits
          + R21 REST poll are live agent time; armed auto-merge lands server-side)
```

CI machine-minutes are reported separately (≈free on public repos; real quota if
private).

## 4. Results (damage composite, mean ± stdev agent-min/window; full tables via the reproduce command)

### docs class (severity 0.25; substrate-gate 11s)

| p_break | traffic | R0 | R1 | R2 | R3 |
|---|---|---|---|---|---|
| 0.003 | ×1 | **13.3±20** | 16.2±21 | 14.8±6 | 13.3±20 |
| 0.01 | ×1 | 16.3±21 | 17.1±18 | 17.1±6 | 16.3±20 |
| 0.03 | ×1 | 37.7±42 | 25.3±30 | **20.9±9** | 36.2±41 |
| 0.03 | ×4 | 326±138 | 261±166 | **81±16** | 322±136 |

### lab class (severity 1.0; matrix 22–45s wall, 2 machine-min ×2 double-fire)

| p_break | traffic | R0 | R1 | R2 | R3 |
|---|---|---|---|---|---|
| 0.003 | ×1 | 11.3±3 | **10.3±6** | 12.3±8 | 10.7±2 |
| 0.01 | ×1 | 65.2±132* | 24.1±70 | **15.4±9** | 62.8±128 |
| 0.03 | ×1 | 195±238 | 73.6±158 | **17.7±11** | 189±232 |
| 0.03 | ×4 | 1625±759 | 938±859 | **80±25** | 1596±747 |
| 0.08 | ×4 | 2045±435 | 1610±806 | **116±36** | 1983±423 |

*Huge stdevs on R0/R1/R3 are real: damage is driven by rare cascade avalanches
(one undetected break early in a burst poisons everything merged after it).

### prod class (severity 3.0; full round 330–450s wall / 10 machine-min; up-to-date 2-round)

| p_break | traffic | R0 | R1 | R2 | R3 |
|---|---|---|---|---|---|
| 0.003 | ×1 | 44±216 | **19.2±10** | 99.6±49 | 43±211 |
| 0.03 | ×1 | 281±443 | **86±214** | 108±39 | 268±430 |
| 0.08 | ×1 | 901±535 | 502±546 | **145±53** | 855±514 |
| 0.03 | ×2 | 1029±1003 | 731±946 | **240±70** | 993±981 |
| 0.03 | ×4 | 3019±2005 | 1520±2004 | **535±100** | 2970±1973 |

Other headline metrics (×1 traffic, p=0.03 unless noted):

- **Merge latency (ready→merged):** R0/R3 ≈ 0.56–0.60 min everywhere. R1: docs 0.89,
  lab 0.48, prod 1.36 min. R2: docs 1.17, lab 0.79, **prod 7.4 min median /
  14.7 p95** (12.3 median at ×4 — the 2-round tier).
- **Stalls >10 min:** ~0 except prod R2: 3.6/window at ×1 → **37.7/window at ×4**
  (main-advance re-rounds dominate; this is the up-to-date rule's cost, not CI's).
- **Time-to-detection:** R2 0.5 min (docs/lab) / 6.4 min (prod); R1 50–140 min
  (smoke catches fast, full-only waits for nightly); R0/R3 ≈ 200–310 min.
- **CI machine-min/window (×1, p=0.03):** docs R1 4.5 / R2 8.9; lab R1 16 / R2 80
  (double-fire + 5-cell matrix); prod R1 26 / R2 197. R0 = 0; R3 = one full run.

## 5. Crossovers (where regimes flip, on the damage composite)

| class | traffic | R1 beats R0 at p_break | R2 beats R1 | R2 beats R0 |
|---|---|---|---|---|
| docs | ×1 | **0.011** | always | 0.011 |
| docs | ×2 | 0.006 | 0.013 | 0.008 |
| docs | ×4 | 0.004 | 0.004 | 0.004 |
| lab | ×1 | always | 0.004 | 0.003 |
| lab | ×2/×4 | always | always | always |
| prod | ×1 | always | **0.033** | 0.015 |
| prod | ×2 | always | 0.009 | 0.004 |
| prod | ×4 | always | 0.011 | always |

R3 vs R0: within noise everywhere (identical detection timing; R3 buys clean
attribution for one full-run cost — cheap insurance, never a big win).

## 6. Reading the crossovers honestly

- **docs:** below ~1% breakage, **no-CI genuinely wins** — but the entire decision
  is worth single-digit agent-minutes per 8h window (13.3 vs 16.2 at p=0.003). The
  11s substrate-gate costs ~3 wait-min/window and buys the *enforcing* born-red
  card hold, which no-CI repos lose entirely (nothing pends → nothing holds).
  Verdict: no-CI is defensible; a single fast gate is near-free and keeps the hold.
- **lab:** the prior's "smoke-only" premise — that full CI is expensive — is
  **false in labs**: the full suite (22–45s matrix) is as fast as a smoke check.
  R2 beats R1 from 0.4% breakage at 1× and *always* at 2×/4×, by 4–12× on damage at
  p≥0.03. Smoke-only's only win is machine-minutes (16 vs 80/window), and half of
  R2's bill is the accidental push+PR **double-fire** and the 5-cell matrix, not the
  suite. **Run the full suite per PR in one slim cell** and you get R2's damage at
  ~R1's cost. Nightly keeps the full matrix.
- **prod:** at 1× traffic and the observed ≤2–3% true failure rate, **smoke-only
  actually beats full per-PR CI on the composite** (86 vs 108 at p=0.03; 19 vs 100 at
  p=0.003) — full CI's 5–7 min wall × born-red poll paths costs more agent-wait than
  the breakage it prevents. Said plainly, because honesty was asked: a calm prod lane
  over-pays for full CI. **But** the crossover sits at exactly the operating point
  the fleet bursts to (R2 wins from ~1% breakage at ≥2× traffic, and from 3.3% at 1×),
  the observed ≤2% failure rate is *conditioned on full CI existing* (deterrence +
  the pre-push local mirror), and merge=deploy (Q-0193) makes escaped-break tail risk
  live-user-facing. Keep full CI on prod; recover the over-payment by fixing what
  actually costs: the up-to-date two-round tier (37 stalls/window at ×4) and the
  5–7 min Code Quality wall.

## 7. Winner by repo class

| class | winner (sim) | margin at plausible operating point |
|---|---|---|
| docs/coordination | R0/R3 below ~1% breakage; R1/R2 above — all within ~15 agent-min/window | decision is low-stakes; keep the gate for the born-red hold |
| lab | **R2 (full suite per PR)** — provided the suite stays ≤60s and double-fire is fixed | 73.6 → 17.7 damage at p=0.03 ×1; 938 → 80 at ×4 |
| production | **R2 (full per-PR)** at burst traffic / by risk asymmetry; R1 wins calm-lane composite | R2 145 vs R1 502 at p=0.08 ×1; R1 86 vs R2 108 at p=0.03 ×1 |

Sensitivity (smoke-catchable fraction 0.4→0.8, R1, ×1, p=0.03): damage moves
docs 33→20, lab 116→32, prod 186→67 agent-min. Direction of every conclusion above
is unchanged; the R2-vs-R1 prod crossover moves ~±1 point of p_break.

## 8. Limitations (what this sim cannot capture)

- **Human/agent context-switch cost is a stylized constant** (8/20/30-min weights +
  severity multipliers). Real cost of a broken main mid-burst is likely superlinear
  (blocked lanes, confused parallel sessions) — which would favor *more* CI than
  shown, never less.
- **Deterrence is invisible:** the mined ≤2% true failure rate was measured *under*
  full CI + local CI-mirror discipline. Removing CI plausibly raises p_break itself;
  the sim treats p_break as exogenous (that's why it's swept).
- **Flake correlation not modeled:** flakes are i.i.d. here; real flakes cluster
  (a broken runner image reddens a whole afternoon).
- **One writer per lane (R7) is assumed via calibrated arrival rates**, not queue
  contention; merge-order approximation processes PRs in ready-order.
- **GraphQL quota is a per-hour outage model** ("~hourly at fleet scale" is the
  manager's calibrated estimate per playbook R8 — no raw RATE_LIMITED transcript
  exists).
- **Breakage class split (60/40)** is a defensible judgment from one night's failure
  census, not a measured distribution; sensitivity swept at 40/60/80.
- **R0's promotion-point detection is assumed to happen** at window end; a promotion
  that silently ships broken work is worse than modeled.
- Burst shape is homogeneous Poisson within the window; real days had dead-air gaps
  (18:10–19:54Z). Traffic 2×/4× brackets the observed burst peaks instead.

## 9. Recommendation (3 sentences)

Adopt the tiers with two amendments: **Tier 1 labs should run the full suite per PR
in one slim ≤60s cell (not a reduced smoke subset) plus a nightly full matrix**,
because lab full suites already run at smoke speed and full-catch cuts damage 4–12×;
and **Tier 0 stays no-CI but repos using the born-red card convention keep the 11s
substrate-gate as the hold mechanism** (its damage cost is noise). **Tier 2 prod
keeps full per-PR CI** — it wins everywhere the fleet actually bursts (≥2× traffic
or ≥3% breakage) and merge=deploy risk asymmetry covers the calm-lane gap — with the
sim-quantified riders: never require up-to-date branches (the 2-round tier is 37
stalls/window at 4×) and treat the 5–7 min Code Quality wall as the next cost target.
