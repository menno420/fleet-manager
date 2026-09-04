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
    "Killed by the judge": "no",         # kill: a disposition judge applied the rule
}

# The fixture journal has no readings for the real re-audit slice, so the
# builder's new refusal to report success over an incomplete manifest fires
# here by design; --allow-partial is the deliberate opt-in that flag exists for.

# The scoping case: `other-repo` emits an item whose subject is IDENTICAL to the
# drop written about `demo`. Correctly scoped it survives; pooled globally it
# dies. It is keyed by (subject, source_path) because the subject collides.
SCOPED_SURVIVOR = ("Dropped by the adversary", "docs/x.md", "other-repo")

# A refuter judges ONE repository's reading, so its drops must apply to that
# reading and to nothing else. Pooling every refuter's drops into one namespace
# let a drop written about one repository kill a row from another — caught on
# live data by the count going ABOVE the number of drops that exist (49 applied
# against 44 written). The fixture's reader and refuter therefore share a repo.

# A judge that already applied the rule NAMED the branch that fired. The
# manifest must publish that branch, not one this script re-derives from the
# blank fields it synthesised for the row — the first version of the builder
# reported every judge-killed row as "no source path · no verification point ·
# certainty UNVERIFIED", three artefacts of its own normalisation, burying the
# real reason. Measured on live fleet output before it was fixed.
JUDGE_BRANCH = "stale_on_copy and disposition == 'carry'"


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        out = pathlib.Path(tmp) / "manifest.csv"
        proc = subprocess.run(
            [sys.executable, str(HERE / "build_manifest.py"),
             "--journal", str(FIXTURE),
             "--classification", str(REPO / "docs/findings/data/2026-09-04-estate-truth-baseline/classification.json"),
             "--out", str(out), "--allow-partial"],
            capture_output=True, text=True, cwd=REPO)
        if proc.returncode != 0:
            print(proc.stdout, proc.stderr)
            print("FAIL: builder exited", proc.returncode)
            return 1
        rows = list(csv.DictReader(out.open(encoding="utf-8")))

    bad = []
    for subject, want in EXPECTED.items():
        cands = [r for r in rows if r["subject"] == subject and r["source_repo"] != "other-repo"]
        got = cands[0]["survives"] if cands else None
        if got != want:
            bad.append(f"{subject!r}: survives={got}, expected {want}")
    subj, path, repo = SCOPED_SURVIVOR
    scoped = [r for r in rows if r["subject"] == subj and r["source_repo"] == repo]
    if not scoped:
        bad.append(f"scoping case missing from output: {subj!r} @ {repo}")
    elif scoped[0]["survives"] != "yes":
        bad.append(f"a drop written about another repository killed {repo}'s row "
                   f"(killed_by={scoped[0]['killed_by']!r}) — drops are not scoped")
    dropped = [r for r in rows if r["subject"] == "Dropped by the adversary"
               and r["source_repo"] != "other-repo"]
    if dropped and dropped[0].get("killed_by", "") == "":
        bad.append("a killed row must publish the branch that fired, not just a flag")
    jrows = [r for r in rows if r["subject"] == "Killed by the judge"]
    judged = jrows[0].get("killed_by", "") if jrows else ""
    if judged != JUDGE_BRANCH:
        bad.append(f"a judge-killed row must publish the JUDGE's branch, got {judged!r} "
                   f"expected {JUDGE_BRANCH!r}")

    kills = sum(1 for v in EXPECTED.values() if v == "no")
    survivals = sum(1 for v in EXPECTED.values() if v == "yes")
    print(f"aggregation fixture: {len(EXPECTED)} cases, {kills} kill / {survivals} survival")
    for b in bad:
        print("FAIL:", b)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
