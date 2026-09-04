#!/usr/bin/env python3
"""Instrument fixtures for the estate baseline delta.

Two halves, because a matcher that passes fixtures and returns nothing on the
real corpus is still broken (fleet-preflight § 2 / TRAP-003):

  1. `classify()` on hand-written branches — including the branch that must
     NOT fire (a moved repo must never read UNCHANGED_REUSABLE);
  2. a live positive/negative control over the real estate, asserting that
     repositories whose default branch demonstrably moved since their anchor
     are classified CHANGED and that ones that demonstrably did not are
     classified UNCHANGED.

Run:  python3 tools/estate_baseline/test_delta.py [delta.tsv]
Exit: 0 all fixtures pass · 1 a fixture failed.
"""

from __future__ import annotations

import csv
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
from delta import classify  # noqa: E402

# --- 1 · branch fixtures: each names its expected outcome BEFORE it runs -----
UNIT = [
    # (ahead, archived, expected, why this case exists)
    (0, False, "UNCHANGED_REUSABLE", "survival: prior evidence still stands"),
    (1, False, "CHANGED_REAUDIT", "kill: one commit is enough to re-audit"),
    (23, False, "CHANGED_REAUDIT", "kill: many commits"),
    (0, True, "ARCHIVED_OR_NONACTIVE", "archived wins over unmoved"),
    (7, True, "ARCHIVED_OR_NONACTIVE", "archived wins over moved"),
    (None, False, "INACCESSIBLE", "a wall is recorded, never guessed"),
    (None, True, "INACCESSIBLE", "a wall outranks the archived flag"),
]

# --- 2 · live controls over the real estate ---------------------------------
# Positives: default branch moved after the anchor (independently visible in
# the repository's own commit dates).  Negatives: it had not, AT THE SNAPSHOT.
#
# BOTH lists are snapshot-relative, and doubly so now that anchors carry the SHA
# the audit read: from that point a repository that has not moved SINCE reads
# UNCHANGED, which is the instrument working. The estate keeps moving, so a fresh
# delta legitimately reclassifies one the day it receives a commit. Asserting
# UNCHANGED against a fresh run would turn ordinary movement into a red test —
# and the finding tells a seed session to run exactly that. So a negative is
# checked against the COMMITTED snapshot, and against a fresh file it is only
# required not to be INACCESSIBLE.
SNAPSHOT = "docs/findings/data/2026-09-04-estate-truth-baseline/delta.tsv"
POSITIVE = {"fleet-manager", "couch-legend", "substrate-kit", "websites"}
NEGATIVE = {"pokemon-mod-lab", "shiftlife", "gba-homebrew", "curious-research",
            "venture-lab", "superbot-next", "superbot-plugin-hello"}


def main() -> int:
    failures = []

    for ahead, archived, expected, why in UNIT:
        got = classify(ahead, archived)
        if got != expected:
            failures.append(f"unit: classify({ahead},{archived}) -> {got}, expected {expected} ({why})")

    # Partition ALL branches, not a subset: an earlier version counted kills and
    # survivals and left the two ARCHIVED_OR_NONACTIVE cases in neither, so the
    # printed tally read "7 cases, 4 kill / 1 survival" and did not add up.
    killed = sum(1 for a, ar, e, _ in UNIT if e in {"CHANGED_REAUDIT", "INACCESSIBLE"})
    survived = sum(1 for a, ar, e, _ in UNIT if e == "UNCHANGED_REUSABLE")
    diverted = sum(1 for a, ar, e, _ in UNIT if e == "ARCHIVED_OR_NONACTIVE")
    if killed + survived + diverted != len(UNIT):
        failures.append(f"unit: tally does not partition the cases "
                        f"({killed}+{survived}+{diverted} != {len(UNIT)})")
    if not killed or not survived:
        failures.append("unit: fixtures must contain at least one kill AND one survival")

    path = sys.argv[1] if len(sys.argv) > 1 else (
        "docs/findings/data/2026-09-04-estate-truth-baseline/delta.tsv")
    try:
        rows = {r["repo"]: r for r in csv.DictReader(open(path, encoding="utf-8"), delimiter="\t")}
    except OSError as exc:
        print(f"delta fixtures: cannot read the real-slice output ({exc}); "
              "run delta.py first — unit fixtures alone are not a positive control")
        return 1

    fresh = pathlib.Path(path).resolve() != (REPO / SNAPSHOT).resolve()
    hits = 0
    for repo in sorted(POSITIVE):
        row = rows.get(repo)
        if row is None:
            failures.append(f"positive control missing from output: {repo}")
        elif fresh:
            # Positives are snapshot-relative in BOTH directions once anchors carry
            # the audited SHA: a repository that has not moved SINCE THE AUDIT now
            # correctly reads UNCHANGED, so asserting CHANGED against a fresh delta
            # would fail on correct behaviour. Same reasoning as the negatives.
            if row["delta_status"] == "INACCESSIBLE":
                failures.append(f"positive control unreadable: {repo} — {row['note']}")
            else:
                hits += 1
        elif row["delta_status"] != "CHANGED_REAUDIT":
            failures.append(f"positive control inert: {repo} -> {row['delta_status']} "
                            f"(commits_since={row['commits_since']})")
        else:
            hits += 1
    for repo in sorted(NEGATIVE):
        row = rows.get(repo)
        if row is None:
            failures.append(f"negative control missing from output: {repo}")
        elif fresh:
            # against a fresh delta, movement is legitimate; only a wall is a failure
            if row["delta_status"] == "INACCESSIBLE":
                failures.append(f"negative control unreadable: {repo} — {row['note']}")
            else:
                hits += 1
        elif row["delta_status"] != "UNCHANGED_REUSABLE":
            failures.append(f"negative control overmatched: {repo} -> {row['delta_status']} "
                            f"(commits_since={row['commits_since']})")
        else:
            hits += 1

    print(f"unit fixtures  : {len(UNIT)} cases, {killed} kill / {survived} survival / "
          f"{diverted} archived-diverted")
    print(f"real-slice     : {hits}/{len(POSITIVE) + len(NEGATIVE)} controls correct "
          f"({len(POSITIVE)} positive, {len(NEGATIVE)} negative"
          f"{', snapshot-relative' if not fresh else ', fresh file — negatives checked for readability only'})"
          f" over {len(rows)} rows in {path}")
    for f in failures:
        print("FAIL:", f)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
