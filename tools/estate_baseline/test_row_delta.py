#!/usr/bin/env python3
"""Instrument fixtures for the row-level source drift check.

Two halves, as for `test_delta.py` (fleet-preflight § 2 / TRAP-003: a matcher
that passes fixtures and returns nothing on the real corpus is still broken):

  1. the pure parts on hand-written cases — provenance parsing over the shapes
     readers actually wrote, SHA extraction over the forms that appear in the
     committed manifest, and the classifier including the branch that must NOT
     fire (differing objects must never read UNCHANGED; identical ones must
     never read MOVED);
  2. live controls over an output file: rows whose cited file demonstrably
     changed after the SHA they were verified at must read SOURCE_MOVED, and
     rows whose file demonstrably did not — including rows in repositories
     that DID move — must read SOURCE_UNCHANGED against the committed snapshot.

Run:  python3 tools/estate_baseline/test_row_delta.py [row-delta.tsv]
Exit: 0 all fixtures pass · 1 a fixture failed.
"""

from __future__ import annotations

import csv
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
from row_delta import classify_path, classify_row, paths_of, shas_of  # noqa: E402

# --- 1a · provenance shapes, each taken from a live manifest cell ------------------
PATHS = [
    # (source_path cell, expected paths, expected shape, why)
    ("docs/ESTATE.md", ["docs/ESTATE.md"], "path", "the clean case"),
    ("owner/intent-workbooks/", ["owner/intent-workbooks/"], "path", "a directory is a path"),
    ("docs/ESTATE.md (cross-reference line)", ["docs/ESTATE.md"], "path+annotation",
     "a parenthetical is annotation, the path is recovered and the annotation is reported"),
    ("tools/gen_owner_index.py; tools/gen_workbook_progress.py",
     ["tools/gen_owner_index.py", "tools/gen_workbook_progress.py"], "paths:2", "a semicolon list"),
    (".github/workflows/dump.yml, .github/workflows/sizing.yml",
     [".github/workflows/dump.yml", ".github/workflows/sizing.yml"], "paths:2", "a comma list"),
    ("owner/intent-workbooks/ (agents/, estate/, folders/)", ["owner/intent-workbooks/"],
     "path+annotation", "a directory with its children listed in parentheses"),
    ("products/x/README.md; GitHub release page", ["products/x/README.md"], "path+annotation",
     "a non-path token is dropped and reported, never resolved as a path"),
    ("(live PR list)", [], "narration", "the § 12 item 10 case: passes the rule, has no path"),
    ("", [], "narration", "empty is narration, not a crash"),
]

# --- 1b · verification-point forms, each taken from a live manifest cell -----------
SHAS = [
    # (verification_point cell, expected SHAs in order, expected shape, why)
    ("caa6cd2@2026-09-03T21:42:38Z", ["caa6cd2"], "sha@instant", "the canonical form"),
    ("d877ed0b611418f35ad9e578785b012a844d1992@2026-09-04",
     ["d877ed0b611418f35ad9e578785b012a844d1992"], "sha@instant", "full SHA, date only"),
    ("sha7d99f7d@2026-08-29", ["7d99f7d"], "sha+instant",
     "a `sha` prefix glued to the hex must not yield `a7d99f7d`"),
    ("sha@21b19be", ["21b19be"], "sha-only", "the `sha@<hex>` inversion"),
    ("caa6cd2, headers read", ["caa6cd2"], "sha-only", "a SHA with narration and no instant"),
    ("caa6cd2; README header re-read at 7ccc88a; current-state.md lines 107-112",
     ["caa6cd2", "7ccc88a"], "sha-only", "two SHAs: a reading and a later re-read"),
    ("live-api@2026-09-04 (repo state)", [], "instant-only", "an instant with no commit"),
    ("06dbbfe@2026-09-04; judge ls docs/x.md -> present, 6451 bytes @2026-09-04",
     ["06dbbfe"], "sha+instant", "one SHA amid narration; `6451` is too short to be one"),
    ("defaced by nobody", [], "narration", "hex-letter English words are not SHAs"),
    ("", [], "narration", "empty is narration, not a crash"),
]

# --- 1c · the classifier; expected outcome written BEFORE the run ------------------
PATH_CASES = [
    # (base object, tip object, expected, why)
    ("abc1", "abc1", "UNCHANGED", "survival: identical objects"),
    ("abc1", "abc2", "MOVED", "kill: the branch that must fire on any difference"),
    ("abc1", None, "GONE", "kill: verified, then removed"),
    (None, "abc2", "MISSING_AT_VERIFICATION", "kill: the row claims to have read a file that was not there"),
    (None, None, "NOT_FOUND", "kill: exists at neither point"),
]
ROW_CASES = [
    (["UNCHANGED"], "SOURCE_UNCHANGED", "one clean path"),
    (["UNCHANGED", "UNCHANGED"], "SOURCE_UNCHANGED", "several clean paths"),
    (["UNCHANGED", "MOVED"], "SOURCE_MOVED", "one moved path outranks any number unchanged"),
    (["MOVED", "GONE"], "SOURCE_GONE", "gone outranks moved"),
    (["UNCHANGED", "MISSING_AT_VERIFICATION"], "SOURCE_MISSING_AT_VERIFICATION",
     "a provenance defect outranks a clean sibling"),
    (["NOT_FOUND", "MISSING_AT_VERIFICATION"], "SOURCE_MISSING_AT_VERIFICATION",
     "missing-at-verification outranks not-found"),
]

# --- 2 · live controls over the real manifest ------------------------------------
# Positives — the file the row cites changed after its verification SHA. These
# hold against a FRESH file too: once a file has moved relative to a fixed SHA
# it stays moved (a byte-identical revert is the one exception, and would be
# news). fleet-manager took sixteen commits between the audit and 2026-09-04T18:19Z
# that modified all three of these files (compare caa6cd2ab659...69e1a71c0554).
POSITIVE = [
    ("fleet-manager", "docs/current-state.md"),
    ("fleet-manager", "docs/ESTATE.md"),
    ("fleet-manager", "docs/decisions.md"),
]
# Negatives — the file did NOT change, checked against the committed SNAPSHOT
# only (the estate keeps moving). The three satellite rows are the reason this
# instrument exists at row level: each repository moved (CHANGED_REAUDIT in the
# 2026-09-04 delta) and the one file its surviving row cites did not.
NEGATIVE = [
    ("spider-swing", "docs/current-state.md"),
    ("substrate-kit", "docs/NEXT-TASKS.md"),
    ("couch-legend", "README.md"),
    ("shiftlife", "docs/current-state.md"),
]
# A row whose provenance is narration must be UNCHECKABLE, never classified.
UNCHECKABLE_SUBJECT_FRAGMENT = "live PR list"
SNAPSHOT = "docs/findings/data/2026-09-04-estate-truth-baseline/row-delta.tsv"
MANIFEST = "docs/planning/2026-09-04-estate-seed-manifest.csv"


def main() -> int:
    failures = []

    for cell, want_paths, want_shape, why in PATHS:
        got_paths, got_shape = paths_of(cell)
        if got_paths != want_paths or got_shape != want_shape:
            failures.append(f"paths_of({cell!r}) -> {got_paths}, {got_shape!r}; "
                            f"expected {want_paths}, {want_shape!r} ({why})")
    for cell, want_shas, want_shape, why in SHAS:
        got_shas, got_shape = shas_of(cell)
        if got_shas != want_shas or got_shape != want_shape:
            failures.append(f"shas_of({cell!r}) -> {got_shas}, {got_shape!r}; "
                            f"expected {want_shas}, {want_shape!r} ({why})")
    for base, tip, want, why in PATH_CASES:
        got = classify_path(base, tip)
        if got != want:
            failures.append(f"classify_path({base!r},{tip!r}) -> {got}, expected {want} ({why})")
    for statuses, want, why in ROW_CASES:
        got = classify_row(statuses)
        if got != want:
            failures.append(f"classify_row({statuses}) -> {got}, expected {want} ({why})")
    try:
        classify_row([])
        failures.append("classify_row([]) must refuse — an unresolvable row is UNCHECKABLE, "
                        "decided by the caller, never a classification made from nothing")
    except ValueError:
        pass
    kills = sum(1 for _b, _t, e, _w in PATH_CASES if e != "UNCHANGED")
    survivals = sum(1 for _b, _t, e, _w in PATH_CASES if e == "UNCHANGED")
    if not kills or not survivals:
        failures.append("path fixtures must contain at least one kill AND one survival")

    path = sys.argv[1] if len(sys.argv) > 1 else SNAPSHOT
    try:
        rows = list(csv.DictReader(open(path, encoding="utf-8"), delimiter="\t"))
        manifest = list(csv.DictReader(open(REPO / MANIFEST, encoding="utf-8", newline="")))
    except OSError as exc:
        print(f"row-delta fixtures: cannot read the real-slice output ({exc}); "
              "run row_delta.py first — unit fixtures alone are not a positive control")
        return 1
    fresh = pathlib.Path(path).resolve() != (REPO / SNAPSHOT).resolve()
    # Join back to the manifest by (subject, source_repo) to reach source_path,
    # which the output deliberately does not repeat.
    src = {(m["subject"], m["source_repo"]): m["source_path"] for m in manifest}

    def rows_citing(repo: str, file: str) -> list[dict]:
        out = []
        for r in rows:
            if r["source_repo"] != repo:
                continue
            sp = src.get((r["subject"], r["source_repo"]), "")
            if sp.split(" (")[0].strip() == file:
                out.append(r)
        return out

    hits = 0
    for repo, file in POSITIVE:
        cands = [r for r in rows_citing(repo, file) if not r["row_status"].startswith(("UNCHECKABLE", "INACCESSIBLE"))]
        if not cands:
            failures.append(f"positive control missing/unreadable: {repo} {file}")
            continue
        bad = [r for r in cands if r["row_status"] not in ("SOURCE_MOVED", "SOURCE_GONE")]
        if bad:
            failures.append(f"positive control inert: {repo} {file} -> "
                            f"{sorted({r['row_status'] for r in bad})} on {len(bad)} row(s)")
        else:
            hits += 1
    for repo, file in NEGATIVE:
        cands = rows_citing(repo, file)
        if not cands:
            failures.append(f"negative control missing from output: {repo} {file}")
            continue
        if any(r["row_status"].startswith("INACCESSIBLE") for r in cands):
            failures.append(f"negative control unreadable: {repo} {file}")
        elif fresh:
            hits += 1   # against a fresh file, movement is legitimate; only a wall fails
        else:
            bad = [r for r in cands if r["row_status"] != "SOURCE_UNCHANGED"]
            if bad:
                failures.append(f"negative control overmatched: {repo} {file} -> "
                                f"{sorted({r['row_status'] for r in bad})}")
            else:
                hits += 1
    narr = [r for r in rows if UNCHECKABLE_SUBJECT_FRAGMENT in
            src.get((r["subject"], r["source_repo"]), "")]
    if not narr:
        failures.append(f"UNCHECKABLE control missing: no row whose source_path carries "
                        f"{UNCHECKABLE_SUBJECT_FRAGMENT!r}")
    elif any(not r["row_status"].startswith("UNCHECKABLE") for r in narr):
        failures.append("a narration-provenance row was classified rather than UNCHECKABLE: "
                        + "; ".join(r["row_status"] for r in narr))
    else:
        hits += 1

    total = len(POSITIVE) + len(NEGATIVE) + 1
    print(f"unit fixtures  : {len(PATHS)} provenance shapes · {len(SHAS)} verification forms · "
          f"{len(PATH_CASES)} path cases ({kills} kill / {survivals} survival) · "
          f"{len(ROW_CASES)} row-precedence cases")
    print(f"real-slice     : {hits}/{total} controls correct ({len(POSITIVE)} positive, "
          f"{len(NEGATIVE)} negative, 1 uncheckable"
          f"{', snapshot-relative' if not fresh else ', fresh file — negatives checked for readability only'})"
          f" over {len(rows)} rows in {path}")
    for f in failures:
        print("FAIL:", f)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
