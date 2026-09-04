#!/usr/bin/env python3
"""The aggregation fixture: prove that a refuter's dissent actually KILLS.

This is the single test fleet-preflight § 1 exists for. The estate's 2026-08-29
fan-out collected the deciding signal and threw it away in aggregation — 815 of
925 verdicts named something the survival rule never read — and the run only
learned that after spending 88 % of its budget.

The fixture journal holds two seed items a reader emitted with `refuted: false`,
and one refuter verdict dropping the second by subject. If aggregation works,
one row survives and one dies with the branch that fired. If aggregation quietly
ignores refuter output, BOTH survive — and that is the failure this catches.

Run:  python3 tools/estate_baseline/test_manifest.py
Exit: 0 pass · 1 fail
"""

from __future__ import annotations

import csv
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
FIXTURE = HERE / "fixtures" / "journal-aggregation.jsonl"

# Expected outcome per subject, written down BEFORE the run.
EXPECTED = {
    "Survivor fact": "yes",              # survival: full provenance, hub-owned
    "Dropped by the adversary": "no",    # kill: the refuter dropped it
}


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        out = pathlib.Path(tmp) / "manifest.csv"
        proc = subprocess.run(
            [sys.executable, str(HERE / "build_manifest.py"),
             "--journal", str(FIXTURE),
             "--classification", str(REPO / "docs/findings/data/2026-09-04-estate-truth-baseline/classification.json"),
             "--out", str(out)],
            capture_output=True, text=True, cwd=REPO)
        if proc.returncode != 0:
            print(proc.stdout, proc.stderr)
            print("FAIL: builder exited", proc.returncode)
            return 1
        rows = {r["subject"]: r for r in csv.DictReader(out.open(encoding="utf-8"))}

    bad = []
    for subject, want in EXPECTED.items():
        got = rows.get(subject, {}).get("survives")
        if got != want:
            bad.append(f"{subject!r}: survives={got}, expected {want}")
    if len(rows) != len(EXPECTED):
        bad.append(f"expected {len(EXPECTED)} rows, got {len(rows)}")
    if rows.get("Dropped by the adversary", {}).get("killed_by", "") == "":
        bad.append("a killed row must publish the branch that fired, not just a flag")

    kills = sum(1 for v in EXPECTED.values() if v == "no")
    survivals = sum(1 for v in EXPECTED.values() if v == "yes")
    print(f"aggregation fixture: {len(EXPECTED)} cases, {kills} kill / {survivals} survival")
    for b in bad:
        print("FAIL:", b)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
