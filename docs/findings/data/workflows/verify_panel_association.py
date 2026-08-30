#!/usr/bin/env python3
"""Re-derive the judge-verdict → draft association in skill-design-panel-output.json.

The workflow emitted the nine `judge_verdicts` UNLABELLED and not grouped by draft,
so each verdict's `draft_name` / `draft_index` / `draft_mean_score` was reconstructed
after the fact. Checking those labels against themselves would be circular. This
script strips them and re-derives the assignment from the INDEPENDENT aggregates the
run computed before any labelling existed (`reconstruction.
independent_aggregates_from_run_ranking`), then asserts two things:

  1. exactly ONE partition of the nine verdicts into three one-per-lens triples
     reproduces all three drafts' mean score, mean catches and verdict multiset; and
  2. that unique partition equals the labels actually committed.

Exit 0 = the labels are sound and self-contained. Exit 1 = they are not.
Reads only the committed JSON — no network, no scratch run, stdlib only.

    python3 docs/findings/data/workflows/verify_panel_association.py
"""
from __future__ import annotations

import json
import sys
from itertools import combinations
from pathlib import Path

PANEL = Path(__file__).with_name("skill-design-panel-output.json")
TOL = 0.005  # the aggregates are rounded to 2dp in the run output
LABELS = ("draft_name", "draft_index", "draft_mean_score", "association_note")


def lens(verdict: dict) -> str:
    """The lens name alone — the run stores it with a trailing prose gloss."""
    return verdict["lens"].split("—")[0].strip()


def fits(triple: tuple[int, ...], agg: dict, verdicts: list[dict]) -> bool:
    """True when these three verdicts reproduce one draft's aggregates."""
    group = [verdicts[i] for i in triple]
    if len({lens(v) for v in group}) != 3:
        return False
    if abs(sum(v["score"] for v in group) / 3 - agg["mean_score"]) > TOL:
        return False
    if abs(sum(v["catches_count"] for v in group) / 3 - agg["mean_catches"]) > TOL:
        return False
    return sorted(v["verdict"] for v in group) == sorted(agg["verdicts"])


def partitions(remaining: set[int], names: list[str], aggs: dict,
               verdicts: list[dict], acc: dict) -> list[dict]:
    if not names:
        return [dict(acc)] if not remaining else []
    name, rest = names[0], names[1:]
    found: list[dict] = []
    for triple in combinations(sorted(remaining), 3):
        if fits(triple, aggs[name], verdicts):
            found += partitions(remaining - set(triple), rest, aggs, verdicts,
                                {**acc, name: sorted(triple)})
    return found


def main() -> int:
    data = json.loads(PANEL.read_text(encoding="utf-8"))
    aggs = {a["draft_name"]: a
            for a in data["reconstruction"]["independent_aggregates_from_run_ranking"]}
    stripped = [{k: v for k, v in x.items() if k not in LABELS}
                for x in data["judge_verdicts"]]

    sols = partitions(set(range(len(stripped))), list(aggs), aggs, stripped, {})
    if len(sols) != 1:
        print(f"FAIL: {len(sols)} consistent assignments — the association is not "
              "uniquely determined by the preserved aggregates.")
        return 1

    committed: dict[str, list[int]] = {}
    for i, v in enumerate(data["judge_verdicts"]):
        committed.setdefault(v["draft_name"], []).append(i)
    committed = {k: sorted(v) for k, v in committed.items()}

    if sols[0] != committed:
        print(f"FAIL: the unique re-derivation {sols[0]} disagrees with the "
              f"committed labels {committed}.")
        return 1

    print("OK: exactly one consistent assignment, and it reproduces the committed "
          "labels.")
    for name, idx in sorted(sols[0].items(), key=lambda kv: -aggs[kv[0]]["mean_score"]):
        scores = [stripped[i]["score"] for i in idx]
        print(f"  {name:<18} verdicts {idx}  scores {scores}  "
              f"mean {aggs[name]['mean_score']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
