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
from row_delta import bind_verification, classify_path, classify_row, paths_of, shas_of, tsv_cell  # noqa: E402

# --- 1a · provenance shapes, each taken from a live manifest cell ------------------
N = None
PATHS = [
    # (source_path cell, expected (repo hint, path) pairs, expected shape, why)
    ("docs/ESTATE.md", [(N, "docs/ESTATE.md")], "path", "the clean case"),
    ("owner/intent-workbooks/", [(N, "owner/intent-workbooks/")], "path", "a directory is a path"),
    ("docs/ESTATE.md (cross-reference line)", [(N, "docs/ESTATE.md")], "path+annotation",
     "a parenthetical is annotation, the path is recovered and the annotation is reported"),
    ("tools/gen_owner_index.py; tools/gen_workbook_progress.py",
     [(N, "tools/gen_owner_index.py"), (N, "tools/gen_workbook_progress.py")], "paths:2", "a semicolon list"),
    (".github/workflows/dump.yml, .github/workflows/sizing.yml",
     [(N, ".github/workflows/dump.yml"), (N, ".github/workflows/sizing.yml")], "paths:2", "a comma list"),
    ("owner/intent-workbooks/ (agents/, estate/, folders/)", [(N, "owner/intent-workbooks/")],
     "path+annotation", "a directory with its children listed in parentheses"),
    ("products/x/README.md; GitHub release page", [(N, "products/x/README.md")], "path+annotation",
     "a non-path token is dropped and reported, never resolved as a path"),
    ("(live PR list)", [], "narration", "the § 12 item 10 case: passes the rule, has no path"),
    ("", [], "narration", "empty is narration, not a crash"),
    # the forms Codex found misread on the committed corpus (fm #1036 round 1)
    ("docs/operations/ (runbooks, present in tree) + fleet-manager docs/repos/superbot/README.md",
     [("runbooks", "docs/operations/"), ("fleet-manager", "docs/repos/superbot/README.md")],
     "paths:2+qualified+annotation",
     "a ` + ` join with the second path qualified by its repository; without a census the "
     "parenthetical's first word is a CANDIDATE hint too — CENSUS_CASES shows it filtered"),
    ("(repo API object) + README.md", [(N, "README.md")], "path+annotation",
     "an annotation joined to a path is still a path"),
    ("docs/repos/ (absence) + docs/ESTATE.md creator-kit row", [("absence", "docs/repos/"), (N, "docs/ESTATE.md")],
     "paths:2+qualified+annotation",
     "trailing words after a path are annotation, never a hint; a parenthetical's first word is a "
     "candidate until the census says otherwise"),
    ("git/trees (harness/*)", [], "api-reference", "the git data API is not a tree path"),
    ("live API: pulls?state=open", [], "api-reference", "a query string names a live surface"),
    ("live-api:pulls?state=open", [], "api-reference", "same, glued"),
    ("releases API (tag postgres-botsite-final-2026-08-16)", [], "api-reference", "the releases API"),
    ("README.md, tests/*.py", [(N, "README.md"), (N, "tests/*.py")], "paths:2+glob",
     "a wildcard path is a path — dropping it would let the row read UNCHANGED on README alone (round 2)"),
    ("README.md (what it fails to say) + docs/repos/estate-backups/README.md (fleet-manager, which does say it)",
     [(N, "README.md"), ("fleet-manager", "docs/repos/estate-backups/README.md")],
     "paths:2+qualified+annotation", "a repository named as the first word of the parenthetical after a path"),
]
# With a census, a hint the census does not know is annotation — `runbooks` is a
# word; `fleet-manager` is a repository. Expected outcome written before the run.
CENSUS_CASES = [
    ("docs/operations/ (runbooks, present in tree) + fleet-manager docs/repos/superbot/README.md",
     {"fleet-manager", "superbot"}, [(N, "docs/operations/"), ("fleet-manager", "docs/repos/superbot/README.md")]),
    ("docs/ESTATE.md (cross-reference line)", {"fleet-manager"}, [(N, "docs/ESTATE.md")]),
    ("x docs/a.md", {"fleet-manager"}, [(N, "docs/a.md")]),
    ("docs/repos/ (absence) + docs/ESTATE.md creator-kit row", {"fleet-manager", "creator-kit"},
     [(N, "docs/repos/"), (N, "docs/ESTATE.md")]),
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
    ("deadbee@2026-09-04", ["deadbee"], "sha@instant",
     "a digit-free hex run glued to @<date> is the canonical form, not a word (round 3)"),
    ("abcdefa, headers read", [], "narration",
     "a digit-free hex run in bare narration stays a word — only the glued form is exempt"),
    ("", [], "narration", "empty is narration, not a crash"),
]

# --- 1b'' · a TSV cell never carries a record or field boundary ---------------------
CELLS = [
    ("plain", "plain", "unchanged"),
    ("a\r\nb", "a  b", "a CRLF from a quoted CSV field: neither half survives (round 3)"),
    ("a\rb", "a b", "a bare CR is a record boundary to most TSV readers"),
    ("a\tb", "a b", "a tab is the field boundary"),
]

# --- 1b' · which verification SHA binds — the later one, and only if all resolved ----
C1 = {"sha": "caa6cd2" * 5, "date": "2026-09-03T21:42:38Z"}
C2 = {"sha": "7ccc88a" * 5, "date": "2026-09-04T12:24:49Z"}
BIND = [
    # (candidates, resolved map, expected sha or None, why)
    (["caa6cd2"], {"caa6cd2": C1}, C1["sha"], "one SHA, resolved"),
    (["caa6cd2", "7ccc88a"], {"caa6cd2": C1, "7ccc88a": C2}, C2["sha"], "two resolved: the later binds"),
    (["7ccc88a", "caa6cd2"], {"caa6cd2": C1, "7ccc88a": C2}, C2["sha"], "order in the cell does not matter"),
    (["caa6cd2", "7ccc88a"], {"caa6cd2": C1, "7ccc88a": None}, None,
     "the later re-read did not resolve: UNCHECKABLE, never a fallback to the stale reading (round 2)"),
    (["caa6cd2"], {"caa6cd2": None}, None, "nothing resolved"),
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
    (["UNCHANGED", "UNRESOLVED_GLOB"], "SOURCE_UNRESOLVED_GLOB",
     "a glob nobody could expand is never reported unchanged by omission"),
    (["UNRESOLVED_GLOB", "MOVED"], "SOURCE_MOVED", "a moved path still outranks an unexpanded glob"),
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
# A row whose provenance is narration must be UNCHECKABLE, never classified —
# and an API reference must be named as one, not reported as a file not found.
UNCHECKABLE_SUBJECT_FRAGMENT = "live PR list"
API_REFERENCE_FRAGMENT = "git/trees"
SNAPSHOT = "docs/findings/data/2026-09-04-estate-truth-baseline/row-delta.tsv"
MANIFEST = "docs/planning/2026-09-04-estate-seed-manifest.csv"


def main() -> int:
    failures = []

    for cell, want_paths, want_shape, why in PATHS:
        got_paths, got_shape = paths_of(cell)
        if got_paths != want_paths or got_shape != want_shape:
            failures.append(f"paths_of({cell!r}) -> {got_paths}, {got_shape!r}; "
                            f"expected {want_paths}, {want_shape!r} ({why})")
    for cell, census, want in CENSUS_CASES:
        got, _shape = paths_of(cell, census)
        if got != want:
            failures.append(f"paths_of({cell!r}, census) -> {got}; expected {want}")
    for cell, want_shas, want_shape, why in SHAS:
        got_shas, got_shape = shas_of(cell)
        if got_shas != want_shas or got_shape != want_shape:
            failures.append(f"shas_of({cell!r}) -> {got_shas}, {got_shape!r}; "
                            f"expected {want_shas}, {want_shape!r} ({why})")
    for raw, want, why in CELLS:
        got = tsv_cell(raw)
        if got != want:
            failures.append(f"tsv_cell({raw!r}) -> {got!r}, expected {want!r} ({why})")
    for cands, resolved, want, why in BIND:
        got, _note = bind_verification(cands, resolved)
        got_sha = got["sha"] if got else None
        if got_sha != want:
            failures.append(f"bind_verification({cands}) -> {got_sha}, expected {want} ({why})")
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
    # Coverage before controls: a truncated snapshot that still holds the control rows
    # would pass every control below (Codex, round 3). The output must carry exactly
    # the manifest's rows — same count, same (subject, source_repo) multiset.
    from collections import Counter
    key = lambda r: (r["subject"], r["source_repo"])  # noqa: E731
    want_keys, got_keys = Counter(map(key, manifest)), Counter(map(key, rows))
    if len(rows) != len(manifest):
        failures.append(f"coverage: snapshot has {len(rows)} rows, manifest {len(manifest)}")
    if want_keys != got_keys:
        missing = list((want_keys - got_keys).elements())[:5]
        extra = list((got_keys - want_keys).elements())[:5]
        failures.append(f"coverage: row keys differ — missing {missing} extra {extra}")
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
        if any(r["row_status"].startswith(("INACCESSIBLE", "UNCHECKABLE")) for r in cands):
            # A negative control has clean provenance by selection, so UNCHECKABLE on
            # one is a resolution regression, not an honest null — it fails on a
            # fresh file too (Codex, fm #1036 round 1: the fresh branch accepted it).
            failures.append(f"negative control unreadable: {repo} {file} -> "
                            f"{sorted({r['row_status'] for r in cands})}")
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

    apiref = [r for r in rows if API_REFERENCE_FRAGMENT in src.get((r["subject"], r["source_repo"]), "")]
    if not apiref:
        failures.append(f"api-reference control missing: no row whose source_path carries {API_REFERENCE_FRAGMENT!r}")
    elif any(r["row_status"] != "UNCHECKABLE:api-reference-not-a-path" for r in apiref):
        failures.append("an API-reference provenance must read UNCHECKABLE:api-reference-not-a-path, got "
                        + "; ".join(r["row_status"] for r in apiref))
    else:
        hits += 1

    total = len(POSITIVE) + len(NEGATIVE) + 2
    print(f"unit fixtures  : {len(PATHS)} provenance shapes · {len(SHAS)} verification forms · "
          f"{len(BIND)} binding cases · {len(CELLS)} cell cases · "
          f"{len(PATH_CASES)} path cases ({kills} kill / {survivals} survival) · "
          f"{len(ROW_CASES)} row-precedence cases")
    print(f"coverage       : {len(rows)} snapshot rows against {len(manifest)} manifest rows, keys "
          f"{'identical' if want_keys == got_keys else 'DIFFER'}")
    print(f"real-slice     : {hits}/{total} controls correct ({len(POSITIVE)} positive, "
          f"{len(NEGATIVE)} negative, 1 uncheckable, 1 api-reference"
          f"{', snapshot-relative' if not fresh else ', fresh file — negatives checked for readability only'})"
          f" over {len(rows)} rows in {path}")
    for f in failures:
        print("FAIL:", f)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
