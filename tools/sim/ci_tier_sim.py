#!/usr/bin/env python3
"""ci_tier_sim.py — discrete-event simulation of CI-tier regimes for the fleet.

Simulates one repo lane during a free-window burst under four CI regimes and
reports merge latency, breakage time-to-detection, cascaded damage, integration
debt, and CI machine-minutes. Built to settle the Tier 0/1/2 CI-tier decision
(fleet-manager gen2-blueprint), in the spirit of superbot's claim_layout_sim.

Regimes
-------
R0  no-CI       : merge instantly (REST, agent action delay); breakage invisible
                  until the promotion/integration point at window end.
R1  smoke-only  : one fast smoke check per PR (class-calibrated 10-60s) that
                  catches only "smoke-catchable" breakage; nightly full suite
                  at window end catches the rest.
R2  full per-PR : calibrated full-CI wall time (labs ~25-45s matrix; prod
                  ~330-450s superbot Code Quality class) + true post-flip flake
                  rate; required-check gating; auto-merge arm rules (arm refused
                  on born-red / no-pending, GraphQL quota outages force REST);
                  up-to-date repos re-run a second round when main advances
                  mid-flight (the mined 2-round ~14-min tier).
R3  batch-only  : no per-PR checks; single full run at window end.

Calibration provenance (mined 2026-07-09, calibration-{prod,labs}.json)
-----------------------------------------------------------------------
- Arrivals: labs 1.87-3.13 PRs/h sustained, hourly-bucket p95 3.7-7.0/h;
  superbot 1.95/h, burst p95 3.83. Traffic sweep 1x/2x/4x covers up to 10/h.
- Check walls: substrate-gate 9-14s; lab matrices 22-45s (5 cells, 2x
  push+PR double-fire verified on fable5); superbot Code Quality 337s wall on
  a real code PR, CodeQL 210s parallel -> full wall 330-450s, ~10 machine-min.
- Born-red is a HOLD, not flakiness: raw gate "failure rates" of 20-35%
  (superbot 35%, substrate-kit 30%, fleet-manager 26%) are deliberate
  session-card holds. True post-flip failure is <=2% (CodeQL 1.6%, labs 0/83).
- Arm-refusal mechanics: GitHub refuses enable_pr_auto_merge on born-red PRs
  ("unstable status") and no-check repos ("only applies when checks are
  pending") — R21; landing falls back to REST merge-on-green (agent poll).
- GraphQL quota exhausts ~hourly at fleet scale (R8) -> arm fails during the
  outage tail of each hour -> REST fallback.
- Stall-not-fail: 1/42 lab runs stuck queued forever (macos hang) -> modeled
  as p_stall with a 10-min timeout + redispatch.

Breakage model
--------------
Each PR is independently broken with probability --pbreak (swept: the key
unknown). Broken PRs split into "smoke-catchable" (default 60%: import/boot/
syntax/config/gate-strict class — the only true failures observed in the mined
night were exactly this class) vs "full-suite-only" (behavioral/logic, needs
the full suite). Cascade: every PR merged while >=1 undetected breakage sits
on main counts as cascaded damage.

Composite damage score (agent-minutes, reported alongside raw metrics):
    damage = severity x (8/caught + 30/cascaded + (20+attrib)/escaped)
             + wait_minutes
where severity is a class multiplier on breakage handling cost:
    docs 0.25 (breakage = doc drift; no runtime to break; cascades are cheap
               re-edits), lab 1.0, prod 3.0 (merge IS deploy, Q-0193: an
               escaped break is live in production within minutes; cascades
               compound onto a deployed-broken bot)
and wait_minutes charges merge latency ONLY on unarmed landing paths — the
agent foreground-polls for green before merging (R4 blocking waits + R21 REST
merge-on-green), so that latency is real agent time; armed auto-merge PRs
land server-side after the session ends and cost ~0 wait.
CI minutes are reported separately (free-tier public repos pay ~0 for them).

Determinism: all randomness flows from hashlib-derived per-cell seeds; no
wall-clock anywhere. Same CLI args -> byte-identical output. Workload draws
(arrivals/breakage) use a regime-independent seed (common random numbers), so
regime comparisons within a cell share the exact same PR stream.

Usage
-----
  python3 ci_tier_sim.py --self-test
  python3 ci_tier_sim.py --sweep --out-prefix results          # full sweep
  python3 ci_tier_sim.py --quick --sweep --out-prefix results  # 5 seeds, fast
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import statistics
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence, Tuple

# --------------------------------------------------------------------------
# Calibrated repo classes (provenance: calibration-prod.json / calibration-labs.json)
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class RepoClass:
    """Calibrated parameters for one repo class (docs / lab / prod)."""

    name: str
    arrival_per_hour: float          # sustained burst-day rate (1x traffic)
    smoke_wall_s: Tuple[float, float]    # uniform wall-time range, seconds
    smoke_machine_min: float             # machine-minutes per smoke run
    full_wall_s: Tuple[float, float]     # uniform wall-time range, seconds
    full_machine_min: float              # machine-minutes per full run
    double_fire: float                   # push+PR double-fire cost multiplier
    born_red_frac: float                 # share of PRs opened born-red (HOLD)
    hold_min: Tuple[float, float]        # born-red work-hold window, minutes
    up_to_date_required: bool            # main-advance forces a 2nd CI round
    p_flake_full: float                  # true post-flip red on a full run
    p_flake_smoke: float                 # true post-flip red on a smoke run
    p_stall: float                       # run stuck-in-queue forever (redispatch)
    severity: float                      # breakage-cost multiplier (see docstring)


CLASSES: Dict[str, RepoClass] = {
    # fleet-manager / coordination repos: substrate-gate ~11s, born-red by
    # design (7/11 session PRs), arrivals 1.87/h, holds 8-16 min.
    "docs": RepoClass(
        name="docs",
        arrival_per_hour=1.9,
        smoke_wall_s=(9.0, 14.0),
        smoke_machine_min=0.2,
        full_wall_s=(25.0, 35.0),
        full_machine_min=0.5,
        double_fire=1.0,
        born_red_frac=0.6,
        hold_min=(8.0, 16.0),
        up_to_date_required=False,
        p_flake_full=0.005,
        p_flake_smoke=0.005,
        p_stall=0.002,
        severity=0.25,
    ),
    # codetool-lab-*: arrivals 1.87-3.13/h (use 2.5), 3-5-cell matrices
    # 22-45s wall / ~2 machine-min with 2x push+PR double-fire (fable5
    # verified, opus 42 runs / 22 PRs); 0/83 true reds; 1/42 stuck-queued.
    "lab": RepoClass(
        name="lab",
        arrival_per_hour=2.5,
        smoke_wall_s=(15.0, 25.0),
        smoke_machine_min=0.35,
        full_wall_s=(22.0, 45.0),
        full_machine_min=2.0,
        double_fire=2.0,
        born_red_frac=0.15,
        hold_min=(5.0, 10.0),
        up_to_date_required=False,
        p_flake_full=0.005,
        p_flake_smoke=0.005,
        p_stall=0.01,
        severity=1.0,
    ),
    # superbot / superbot-next class: arrivals 1.95/h, Code Quality 337s +
    # CodeQL 210s parallel -> wall 330-450s, ~10 machine-min/round; born-red
    # session PRs with long holds; superbot-next's up-to-date requirement
    # produces the mined 2-round ~14-min tier; CodeQL true flake 1.6%.
    "prod": RepoClass(
        name="prod",
        arrival_per_hour=2.0,
        smoke_wall_s=(30.0, 60.0),
        smoke_machine_min=0.9,
        full_wall_s=(330.0, 450.0),
        full_machine_min=10.0,
        double_fire=1.0,
        born_red_frac=0.5,
        hold_min=(10.0, 90.0),
        up_to_date_required=True,
        p_flake_full=0.02,
        p_flake_smoke=0.005,
        p_stall=0.005,
        severity=3.0,
    ),
}

REGIMES: Tuple[str, ...] = ("R0", "R1", "R2", "R3")

# Damage-score weights (agent-minutes). See module docstring.
COST_CAUGHT_PREMERGE = 8.0
COST_CASCADED = 30.0
COST_ESCAPED_FIX = 20.0
COST_ATTRIB_ENDRUN = 5.0     # R1 nightly / R3 batch localizes the break
COST_ATTRIB_ADHOC = 15.0     # R0 promotion surfaces it with no run to point at

# Mechanics constants (doctrine / mined behavior).
STALL_TIMEOUT_MIN = 10.0     # agent notices a stuck-queued run and redispatches
FIX_DELAY_MIN = (4.0, 12.0)  # agent fixes a genuinely red PR in-context
FLAKE_RETRY_MIN = (1.0, 3.0)  # notice + re-run a flake red
REST_POLL_MIN = (0.3, 1.5)   # REST merge-on-green agent poll->merge delay
NOCHECK_MERGE_MIN = (0.17, 1.0)  # R0/R3 agent open->merge (mined median 0.6-0.7)
BORNRED_FASTFAIL_MACHINE_MIN = 0.1  # the seconds-long red gate run at open
MAX_CI_ATTEMPTS = 6          # safety cap on the red->fix->rerun loop
QUOTA_EXHAUST_MIN = (30.0, 55.0)  # GraphQL quota dies this far into each hour


# --------------------------------------------------------------------------
# Workload
# --------------------------------------------------------------------------


@dataclass
class PR:
    """One pull request in the workload stream."""

    idx: int
    t_open: float            # minutes from window start
    born_red: bool
    hold: float              # work-hold minutes (0 if not born-red)
    broken: bool
    smoke_catchable: bool    # only meaningful when broken

    @property
    def ready(self) -> float:
        """Time the PR is green-eligible (card flipped / final push)."""
        return self.t_open + self.hold


def stable_seed(*parts: object) -> int:
    """Derive a deterministic 64-bit seed from a tuple of labels."""
    digest = hashlib.sha256("|".join(str(p) for p in parts).encode()).digest()
    return int.from_bytes(digest[:8], "big")


def make_workload(
    cls: RepoClass,
    traffic: float,
    p_break: float,
    smoke_frac: float,
    window_min: float,
    seed: int,
) -> List[PR]:
    """Draw the PR stream for one seed (regime-independent: common random numbers)."""
    rng = random.Random(stable_seed("workload", cls.name, traffic, p_break, seed))
    rate_per_min = cls.arrival_per_hour * traffic / 60.0
    prs: List[PR] = []
    t = 0.0
    idx = 0
    while True:
        t += rng.expovariate(rate_per_min)
        if t >= window_min:
            break
        born_red = rng.random() < cls.born_red_frac
        hold = rng.uniform(*cls.hold_min) if born_red else 0.0
        broken = rng.random() < p_break
        smoke_catchable = rng.random() < smoke_frac  # drawn always: keeps CRN aligned
        prs.append(PR(idx, t, born_red, hold, broken, smoke_catchable))
        idx += 1
    return prs


# --------------------------------------------------------------------------
# Regime simulation
# --------------------------------------------------------------------------


@dataclass
class SeedMetrics:
    """Raw per-seed outcome of one (class, regime, traffic, p_break) cell."""

    n_prs: int = 0
    n_broken: int = 0
    latencies: List[float] = field(default_factory=list)
    stalled_gt10: int = 0
    ttds: List[float] = field(default_factory=list)
    cascaded: int = 0
    debt: int = 0                # escaped-to-main breakage revealed only at window end
    ci_minutes: float = 0.0
    caught_premerge: int = 0
    wait_minutes: float = 0.0    # agent foreground poll time (unarmed paths)
    damage_minutes: float = 0.0


def _quota_exhaust_offsets(rng: random.Random, window_min: float) -> List[float]:
    """Per-hour GraphQL exhaust offsets (minutes into the hour). R8 doctrine."""
    hours = int(math.ceil(window_min / 60.0)) + 2
    return [rng.uniform(*QUOTA_EXHAUST_MIN) for _ in range(hours)]


def _quota_available(t: float, offsets: Sequence[float]) -> bool:
    """True if the GraphQL quota is alive at minute t (resets on the hour)."""
    hour, into = int(t // 60.0), t % 60.0
    if hour >= len(offsets):
        return True
    return into < offsets[hour]


def _run_check_pipeline(
    pr: PR,
    check: str,  # "smoke" | "full"
    cls: RepoClass,
    rng: random.Random,
    m: SeedMetrics,
) -> Tuple[float, bool]:
    """Run the red->fix->rerun loop for one PR's required check.

    Returns (t_green, caught_breakage). Mutates metrics (ci minutes, ttd for
    pre-merge catches). Starts at pr.ready (the flip push triggers the run).
    """
    if check == "smoke":
        wall_rng, machine = cls.smoke_wall_s, cls.smoke_machine_min
        p_flake, catchable = cls.p_flake_smoke, pr.smoke_catchable
    else:
        wall_rng, machine = cls.full_wall_s, cls.full_machine_min
        p_flake, catchable = cls.p_flake_full, True

    t = pr.ready
    broken_pending = pr.broken and catchable
    caught = False
    for _ in range(MAX_CI_ATTEMPTS):
        m.ci_minutes += machine * cls.double_fire
        if rng.random() < cls.p_stall:
            # Stuck-queued forever (the macos hang class): timeout + redispatch.
            t += STALL_TIMEOUT_MIN
            continue
        t_end = t + rng.uniform(*wall_rng) / 60.0
        if broken_pending:
            # Real red: agent fixes in-context, then re-runs.
            m.ttds.append(t_end - pr.ready)
            m.caught_premerge += 1
            caught = True
            broken_pending = False
            t = t_end + rng.uniform(*FIX_DELAY_MIN)
            continue
        if rng.random() < p_flake:
            t = t_end + rng.uniform(*FLAKE_RETRY_MIN)
            continue
        return t_end, caught
    return t, caught  # attempt cap: give up green at last known t (rare)


def simulate_regime(
    regime: str,
    prs: Sequence[PR],
    cls: RepoClass,
    window_min: float,
    seed: int,
) -> SeedMetrics:
    """Simulate one regime over a fixed workload; return per-seed metrics."""
    rng = random.Random(stable_seed("dyn", regime, cls.name, seed))
    quota = _quota_exhaust_offsets(rng, window_min)
    m = SeedMetrics(n_prs=len(prs), n_broken=sum(1 for p in prs if p.broken))

    merges: List[float] = []               # merge times so far (ready-order approx)
    escaped: List[Tuple[float, int]] = []  # (merge_time, pr_idx) of undetected breaks
    merged_at: List[Tuple[float, int]] = []

    for pr in sorted(prs, key=lambda p: p.ready):
        armed = False
        if regime in ("R0", "R3"):
            # No checks: arm structurally refused ("only applies when checks
            # are pending") -> REST; agent merges near-instantly at ready.
            t_merge = pr.ready + rng.uniform(*NOCHECK_MERGE_MIN)
            if pr.broken:
                escaped.append((t_merge, pr.idx))
        else:
            check = "smoke" if regime == "R1" else "full"
            # Arm attempt at PR open (R5): refused on born-red ("unstable
            # status", R21) and during GraphQL quota outages (R8).
            armed = (not pr.born_red) and _quota_available(pr.t_open, quota)
            if pr.born_red:
                m.ci_minutes += BORNRED_FASTFAIL_MACHINE_MIN  # red gate run at open
            t_green, _caught = _run_check_pipeline(pr, check, cls, rng, m)
            # Main-advance second round (the mined 2-round ~14-min tier).
            if cls.up_to_date_required and any(pr.ready < mt < t_green for mt in merges):
                m.ci_minutes += (cls.full_machine_min if check == "full"
                                 else cls.smoke_machine_min) * cls.double_fire
                t_green += rng.uniform(*(cls.full_wall_s if check == "full"
                                         else cls.smoke_wall_s)) / 60.0
            t_merge = t_green if armed else t_green + rng.uniform(*REST_POLL_MIN)
            if pr.broken and regime == "R1" and not pr.smoke_catchable:
                escaped.append((t_merge, pr.idx))  # full-suite-only slips smoke
            # R2 catches all injected breakage pre-merge: nothing escapes.

        merges.append(t_merge)
        merged_at.append((t_merge, pr.idx))
        latency = t_merge - pr.ready
        m.latencies.append(latency)
        if latency > 10.0:
            m.stalled_gt10 += 1
        if not armed:
            # R4 foreground blocking wait + R21 REST poll: unarmed landings
            # are live agent time; armed auto-merge fires server-side (~free).
            m.wait_minutes += latency

    # --- End-of-window detection -----------------------------------------
    # R0: promotion/integration point at window end (no run, ad-hoc attribution).
    # R1: nightly full suite. R3: the single batch full run.
    if regime in ("R1", "R3"):
        m.ci_minutes += cls.full_machine_min  # single end run, no double-fire
    attrib = COST_ATTRIB_ADHOC if regime == "R0" else COST_ATTRIB_ENDRUN
    for t_merge, _idx in escaped:
        m.debt += 1
        if t_merge <= window_min:
            m.ttds.append(window_min - t_merge)

    # --- Cascade: PRs merged while >=1 undetected break sat on main ------
    intervals = [(t, window_min) for t, _ in escaped if t <= window_min]
    breakers = {idx for _, idx in escaped}
    for t_merge, idx in merged_at:
        if idx in breakers:
            continue
        if any(lo < t_merge <= hi for lo, hi in intervals):
            m.cascaded += 1

    # --- Composite damage score (see module docstring) --------------------
    m.damage_minutes = cls.severity * (
        COST_CAUGHT_PREMERGE * m.caught_premerge
        + COST_CASCADED * m.cascaded
        + (COST_ESCAPED_FIX + attrib) * m.debt
    ) + m.wait_minutes
    return m


# --------------------------------------------------------------------------
# Aggregation and sweep
# --------------------------------------------------------------------------

METRIC_NAMES = (
    "median_latency_min", "p95_latency_min", "stalled_gt10", "mean_ttd_min",
    "cascaded", "debt", "ci_minutes", "caught_premerge", "wait_minutes",
    "damage_minutes", "n_prs", "n_broken",
)


def pctl(sorted_vals: Sequence[float], p: float) -> float:
    """Linear-interpolated percentile of a pre-sorted sequence."""
    if not sorted_vals:
        return 0.0
    k = (len(sorted_vals) - 1) * p
    f, c = math.floor(k), math.ceil(k)
    if f == c:
        return float(sorted_vals[int(k)])
    return sorted_vals[f] + (sorted_vals[c] - sorted_vals[f]) * (k - f)


def seed_metric_row(m: SeedMetrics) -> Dict[str, float]:
    """Flatten one seed's metrics into scalars."""
    lat = sorted(m.latencies)
    return {
        "median_latency_min": pctl(lat, 0.5),
        "p95_latency_min": pctl(lat, 0.95),
        "stalled_gt10": float(m.stalled_gt10),
        "mean_ttd_min": (sum(m.ttds) / len(m.ttds)) if m.ttds else float("nan"),
        "cascaded": float(m.cascaded),
        "debt": float(m.debt),
        "ci_minutes": m.ci_minutes,
        "caught_premerge": float(m.caught_premerge),
        "wait_minutes": m.wait_minutes,
        "damage_minutes": m.damage_minutes,
        "n_prs": float(m.n_prs),
        "n_broken": float(m.n_broken),
    }


def aggregate(rows: List[Dict[str, float]]) -> Dict[str, Dict[str, float]]:
    """mean +/- stdev per metric across seeds (NaN-aware for TTD)."""
    out: Dict[str, Dict[str, float]] = {}
    for name in METRIC_NAMES:
        vals = [r[name] for r in rows if not math.isnan(r[name])]
        if not vals:
            out[name] = {"mean": 0.0, "stdev": 0.0, "n": 0}
            continue
        out[name] = {
            "mean": round(statistics.fmean(vals), 3),
            "stdev": round(statistics.stdev(vals), 3) if len(vals) > 1 else 0.0,
            "n": len(vals),
        }
    return out


def run_cell(
    cls: RepoClass,
    regime: str,
    traffic: float,
    p_break: float,
    smoke_frac: float,
    window_min: float,
    seeds: int,
) -> Dict[str, Dict[str, float]]:
    """Run one sweep cell across seeds; return aggregated metrics."""
    rows = []
    for s in range(seeds):
        prs = make_workload(cls, traffic, p_break, smoke_frac, window_min, s)
        rows.append(seed_metric_row(simulate_regime(regime, prs, cls, window_min, s)))
    return aggregate(rows)


def find_crossover(
    pbreaks: Sequence[float],
    a_vals: Sequence[float],
    b_vals: Sequence[float],
) -> Optional[float]:
    """Smallest p_break where regime B's damage <= regime A's (linear interp).

    Returns None if B never wins in the swept range; 0.0 if B wins everywhere.
    """
    diffs = [a - b for a, b in zip(a_vals, b_vals)]  # >0 where B wins
    if diffs[0] >= 0:
        return 0.0
    for i in range(1, len(diffs)):
        if diffs[i] >= 0:
            x0, x1, y0, y1 = pbreaks[i - 1], pbreaks[i], diffs[i - 1], diffs[i]
            if y1 == y0:
                return x1
            return round(x0 + (0 - y0) * (x1 - x0) / (y1 - y0), 4)
    return None


def run_sweep(args: argparse.Namespace) -> Dict[str, object]:
    """Run the full sweep and assemble the results structure."""
    window_min = args.window_hours * 60.0
    cells: Dict[str, Dict[str, Dict[str, float]]] = {}
    for cname in args.classes:
        cls = CLASSES[cname]
        for traffic in args.traffic:
            for pb in args.pbreak:
                for regime in REGIMES:
                    key = f"{cname}|{regime}|x{traffic:g}|b{pb:g}"
                    cells[key] = run_cell(cls, regime, traffic, pb,
                                          args.smoke_catch_frac, window_min,
                                          args.seeds)
    # Crossovers on the composite damage score, per class x traffic.
    crossovers: Dict[str, Dict[str, Optional[float]]] = {}
    for cname in args.classes:
        for traffic in args.traffic:
            dmg = {
                r: [cells[f"{cname}|{r}|x{traffic:g}|b{pb:g}"]["damage_minutes"]["mean"]
                    for pb in args.pbreak]
                for r in REGIMES
            }
            crossovers[f"{cname}|x{traffic:g}"] = {
                "R1_beats_R0_at_pbreak": find_crossover(args.pbreak, dmg["R0"], dmg["R1"]),
                "R2_beats_R1_at_pbreak": find_crossover(args.pbreak, dmg["R1"], dmg["R2"]),
                "R2_beats_R0_at_pbreak": find_crossover(args.pbreak, dmg["R0"], dmg["R2"]),
                "R3_beats_R0_at_pbreak": find_crossover(args.pbreak, dmg["R0"], dmg["R3"]),
            }
    # Sensitivity: smoke-catchable fraction at 1x traffic, mid breakage.
    sensitivity: Dict[str, Dict[str, Dict[str, float]]] = {}
    pb_mid = args.pbreak[len(args.pbreak) // 2]
    for frac in (0.4, 0.6, 0.8):
        for cname in args.classes:
            key = f"{cname}|R1|x1|b{pb_mid:g}|smokefrac{frac:g}"
            sensitivity[key] = run_cell(CLASSES[cname], "R1", 1.0, pb_mid,
                                        frac, window_min, args.seeds)
    return {
        "meta": {
            "generated_by": "ci_tier_sim.py",
            "calibration_sources": [
                "calibration-prod.json (2026-07-09, 451 PRs / ~1250 runs mined)",
                "calibration-labs.json (2026-07-09)",
                "doctrine-constraints.md (R5/R6/R8/R21, born-red, quota)",
            ],
            "window_hours": args.window_hours,
            "seeds": args.seeds,
            "traffic_multipliers": list(args.traffic),
            "pbreak_sweep": list(args.pbreak),
            "smoke_catch_frac": args.smoke_catch_frac,
            "damage_weights_min": {
                "caught_premerge": COST_CAUGHT_PREMERGE,
                "cascaded": COST_CASCADED,
                "escaped_fix": COST_ESCAPED_FIX,
                "attribution_endrun": COST_ATTRIB_ENDRUN,
                "attribution_adhoc_R0": COST_ATTRIB_ADHOC,
                "formula": ("damage = severity*(8*caught + 30*cascaded + "
                            "(20+attrib)*escaped) + wait_minutes; severity "
                            "docs 0.25 / lab 1.0 / prod 3.0 (Q-0193 merge=deploy)"),
            },
            "classes": {
                n: {k: getattr(c, k) for k in (
                    "arrival_per_hour", "smoke_wall_s", "smoke_machine_min",
                    "full_wall_s", "full_machine_min", "double_fire",
                    "born_red_frac", "hold_min", "up_to_date_required",
                    "p_flake_full", "p_flake_smoke", "p_stall")}
                for n, c in CLASSES.items() if n in args.classes
            },
        },
        "cells": cells,
        "crossovers_damage_minutes": crossovers,
        "sensitivity_smoke_catch_frac": sensitivity,
    }


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------

REPORT_METRICS = (
    ("median_latency_min", "med lat (m)"),
    ("p95_latency_min", "p95 lat (m)"),
    ("stalled_gt10", ">10m stalls"),
    ("mean_ttd_min", "TTD (m)"),
    ("cascaded", "cascaded"),
    ("debt", "debt"),
    ("ci_minutes", "CI min"),
    ("wait_minutes", "wait (m)"),
    ("damage_minutes", "damage (m)"),
)


def fmt_ms(cell: Dict[str, float]) -> str:
    """Format mean +/- stdev compactly."""
    return f"{cell['mean']:.2f}±{cell['stdev']:.2f}"


def render_markdown(res: Dict[str, object], args: argparse.Namespace) -> str:
    """Render results.md from the sweep structure."""
    meta = res["meta"]
    cells = res["cells"]  # type: ignore[assignment]
    lines: List[str] = [
        "# CI-tier simulation — full sweep results",
        "",
        f"Window {meta['window_hours']}h · {meta['seeds']} seeds/cell · "  # type: ignore[index]
        f"traffic ×{meta['traffic_multipliers']} · p_break {meta['pbreak_sweep']} · "  # type: ignore[index]
        f"smoke-catchable {meta['smoke_catch_frac']}. Mean ± stdev across seeds. "  # type: ignore[index]
        "Latency measured from PR-ready (born-red card flip) to merged. "
        "Damage = composite agent-minutes (weights in results.json meta).",
        "",
    ]
    for cname in args.classes:
        lines.append(f"## class `{cname}` "
                     f"(arrival ×1 = {CLASSES[cname].arrival_per_hour}/h)")
        for pb in args.pbreak:
            lines.append(f"\n### p_break = {pb:g}\n")
            hdr = "| traffic | regime | " + " | ".join(h for _, h in REPORT_METRICS) + " |"
            lines.append(hdr)
            lines.append("|" + "---|" * (len(REPORT_METRICS) + 2))
            for traffic in args.traffic:
                for regime in REGIMES:
                    c = cells[f"{cname}|{regime}|x{traffic:g}|b{pb:g}"]  # type: ignore[index]
                    row = [f"×{traffic:g}", regime] + [fmt_ms(c[k]) for k, _ in REPORT_METRICS]
                    lines.append("| " + " | ".join(row) + " |")
        lines.append("")
    lines.append("## Crossovers (composite damage, linear interpolation over the p_break sweep)")
    lines.append("")
    lines.append("| class | traffic | R1 beats R0 at p_break | R2 beats R1 | R2 beats R0 | R3 beats R0 |")
    lines.append("|---|---|---|---|---|---|")
    for key, x in res["crossovers_damage_minutes"].items():  # type: ignore[union-attr]
        cname, tr = key.split("|")
        def show(v: Optional[float]) -> str:
            if v is None:
                return "never (in sweep)"
            if v == 0.0:
                return "always"
            return f"{v:.3f}"
        lines.append(f"| {cname} | {tr} | {show(x['R1_beats_R0_at_pbreak'])} | "
                     f"{show(x['R2_beats_R1_at_pbreak'])} | {show(x['R2_beats_R0_at_pbreak'])} | "
                     f"{show(x['R3_beats_R0_at_pbreak'])} |")
    lines.append("")
    lines.append("## Sensitivity — smoke-catchable fraction (R1, ×1 traffic, mid p_break)")
    lines.append("")
    lines.append("| cell | debt | cascaded | damage (m) |")
    lines.append("|---|---|---|---|")
    for key, c in res["sensitivity_smoke_catch_frac"].items():  # type: ignore[union-attr]
        lines.append(f"| {key} | {fmt_ms(c['debt'])} | {fmt_ms(c['cascaded'])} | "
                     f"{fmt_ms(c['damage_minutes'])} |")
    lines.append("")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Self-test
# --------------------------------------------------------------------------


def self_test() -> int:
    """Invariant checks; returns 0 on success, 1 on failure."""
    failures: List[str] = []
    window = 480.0
    cls = CLASSES["lab"]

    def check(cond: bool, msg: str) -> None:
        if not cond:
            failures.append(msg)
        print(("  ok  " if cond else "  FAIL") + " " + msg)

    # 1. Determinism: same cell twice -> identical aggregates.
    a = run_cell(cls, "R2", 2.0, 0.03, 0.6, window, 5)
    b = run_cell(cls, "R2", 2.0, 0.03, 0.6, window, 5)
    check(a == b, "determinism: identical cell run twice gives identical output")

    # 2. Common random numbers: workload identical across regimes.
    w1 = make_workload(cls, 1.0, 0.03, 0.6, window, 7)
    w2 = make_workload(cls, 1.0, 0.03, 0.6, window, 7)
    check(w1 == w2, "workload draw is reproducible")
    n_by_regime = {r: simulate_regime(r, w1, cls, window, 7).n_prs for r in REGIMES}
    check(len(set(n_by_regime.values())) == 1, "same PR stream across regimes (CRN)")

    # 3. R0 consumes zero CI minutes; R3 exactly one full run.
    m0 = simulate_regime("R0", w1, cls, window, 7)
    m3 = simulate_regime("R3", w1, cls, window, 7)
    check(m0.ci_minutes == 0.0, "R0 CI minutes == 0")
    check(abs(m3.ci_minutes - cls.full_machine_min) < 1e-9,
          "R3 CI minutes == one batch full run")

    # 4. R2 catches all injected breakage: zero debt, zero cascade.
    m2 = run_cell(cls, "R2", 4.0, 0.08, 0.6, window, 10)
    check(m2["debt"]["mean"] == 0.0 and m2["cascaded"]["mean"] == 0.0,
          "R2: no injected breakage escapes to main")

    # 5. p_break=0 -> no breakage anywhere.
    for r in REGIMES:
        c = run_cell(cls, r, 2.0, 0.0, 0.6, window, 5)
        check(c["debt"]["mean"] == 0.0 and c["cascaded"]["mean"] == 0.0
              and c["caught_premerge"]["mean"] == 0.0,
              f"{r}: p_break=0 yields zero breakage metrics")

    # 6. R1 with smoke_frac=1.0 catches everything (like R2).
    c = run_cell(cls, "R1", 2.0, 0.08, 1.0, window, 10)
    check(c["debt"]["mean"] == 0.0, "R1 with 100% smoke-catchable: zero debt")

    # 6b. Damage identity: with p_break=0, damage == wait (pure poll overhead).
    m_clean = simulate_regime("R2", make_workload(cls, 2.0, 0.0, 0.6, window, 3),
                              cls, window, 3)
    check(abs(m_clean.damage_minutes - m_clean.wait_minutes) < 1e-9,
          "damage == wait_minutes when no breakage is injected")

    # 7. Monotonicity: R0 debt grows with p_break (CRN seeds).
    d = [run_cell(cls, "R0", 2.0, pb, 0.6, window, 10)["debt"]["mean"]
         for pb in (0.01, 0.03, 0.08)]
    check(d[0] <= d[1] <= d[2], f"R0 debt monotone in p_break: {d}")

    # 8. Latency sanity: non-negative, median <= p95, prod R2 slower than R1.
    lat_r1 = run_cell(CLASSES["prod"], "R1", 1.0, 0.01, 0.6, window, 10)
    lat_r2 = run_cell(CLASSES["prod"], "R2", 1.0, 0.01, 0.6, window, 10)
    check(0.0 <= lat_r1["median_latency_min"]["mean"] <= lat_r1["p95_latency_min"]["mean"],
          "latency ordering: 0 <= median <= p95")
    check(lat_r2["median_latency_min"]["mean"] > lat_r1["median_latency_min"]["mean"],
          "prod: full-CI median latency exceeds smoke-only")

    print()
    if failures:
        print(f"SELF-TEST FAILED ({len(failures)} failures)")
        return 1
    print("SELF-TEST PASSED")
    return 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    """CLI definition."""
    p = argparse.ArgumentParser(
        description="CI-tier discrete-event simulation (fleet calibration 2026-07-09).")
    p.add_argument("--seeds", type=int, default=20, help="seeds per cell (default 20)")
    p.add_argument("--window-hours", type=float, default=8.0,
                   help="free-window burst length in hours (default 8)")
    p.add_argument("--traffic", type=float, nargs="+", default=[1.0, 2.0, 4.0],
                   help="arrival-rate multipliers to sweep")
    p.add_argument("--pbreak", type=float, nargs="+",
                   default=[0.003, 0.01, 0.03, 0.08],
                   help="per-PR breakage probabilities to sweep (0.003 added "
                        "below the asked 1/3/8%% to locate the Tier-0 boundary)")
    p.add_argument("--smoke-catch-frac", type=float, default=0.6,
                   help="share of breakage that a smoke check catches (default 0.6)")
    p.add_argument("--classes", nargs="+", default=["docs", "lab", "prod"],
                   choices=list(CLASSES), help="repo classes to simulate")
    p.add_argument("--sweep", action="store_true", help="run the full sweep and write outputs")
    p.add_argument("--out-prefix", default="results",
                   help="output file prefix for --sweep (writes <prefix>.json/.md)")
    p.add_argument("--quick", action="store_true", help="5 seeds/cell (fast sanity sweep)")
    p.add_argument("--self-test", action="store_true", help="run invariant checks and exit")
    return p


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Entry point."""
    args = build_parser().parse_args(argv)
    if args.self_test:
        return self_test()
    if args.quick:
        args.seeds = 5
    if not args.sweep:
        build_parser().print_help()
        return 0
    res = run_sweep(args)
    json_path = f"{args.out_prefix}.json"
    md_path = f"{args.out_prefix}.md"
    with open(json_path, "w") as f:
        json.dump(res, f, indent=1, sort_keys=True)
        f.write("\n")
    with open(md_path, "w") as f:
        f.write(render_markdown(res, args))
    print(f"wrote {json_path} and {md_path} "
          f"({len(res['cells'])} cells x {args.seeds} seeds)")  # type: ignore[arg-type]
    return 0


if __name__ == "__main__":
    sys.exit(main())
