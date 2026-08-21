#!/usr/bin/env python3
"""check_estate_index.py — keep docs/ESTATE.md, docs/repos/ and the doc-routes consistent.

================================ PROVENANCE ================================
Why added : The 2026-08-21 fleet-wide review (fm #878) built docs/ESTATE.md —
            the estate index, one routing row per repository the account
            holds — because the estate had NO live surface enumerating its
            own repos (Substrate-kit-app appeared nowhere; naming most repos
            in a prompt routed nothing). An index like that drifts in three
            silent ways: a Layer-2 folder is built and never gets a row; a
            row links a folder that does not exist; a doc-route points a
            repo name at the index (or a folder) that no longer answers it.
            Each is a fact, not a judgement, so it is checkable.
Date      : 2026-08-21 (fleet review session, fm #878)
Reliability: unverified — confirm output against ground truth across a few
            sessions before trusting it. The table parser handles the row
            shape ESTATE.md actually uses (first cell `` `repo` ``), not
            arbitrary markdown.
Kill-switch: delete this if it proves unreliable over multiple sessions.
=============================================================================

WHAT IT CHECKS
  1. folder-without-row  — every directory under docs/repos/ has a row in
     docs/ESTATE.md whose Layer-2 cell links into that folder.
  2. row-links-missing-folder — every `repos/<name>/` link in an ESTATE row
     resolves to an existing docs/repos/<name>/README.md; and
     row-links-foreign-folder — the linked folder belongs to that row's repo
     (a swapped pair of links passes every existence check otherwise).
  3. duplicate-row — no repo name appears in two rows.
  4. route-target-missing — every route in .claude/hooks/doc-routes.json
     whose docs[] names docs/ESTATE.md or a docs/repos/<name>/README.md has
     an existing target file; and for docs/repos targets, the folder's repo
     has an ESTATE row (the index is the superset).
  5. folder-without-route-pair — every built docs/repos/<name>/ folder has
     BOTH halves of its doc-route pair (tool events + UserPromptSubmit),
     the repos/README.md § The-files rule; route-pair-id-mismatch — the
     halves form one <id>/<id>-prompt pair; route-pair-unnamed — EACH half
     is recognisably the repo's own (a when-pattern matching the folder
     name, or the base id carrying it).
  6. missing-baseline — the index header carries at least one
     "verified YYYY-MM-DD" stamp; missing-declared-count /
     row-count-mismatch — the header's "all <N> repositories" matches the
     row count, so a silently dropped folderless row reds.

SEVERITY CONTRACT (sibling-parity: check_docs_links.py)
  Direct run exits 1 when anything is inconsistent, 0 when clean.
  `--advisory` prints findings as ::warning:: and always exits 0. NOT wired
  into any blocking gate; promotion is the owner's call.

USAGE
  python3 scripts/check_estate_index.py              # check the repo
  python3 scripts/check_estate_index.py --advisory   # report-only, exit 0
  python3 scripts/check_estate_index.py --root PATH  # check a fixture tree
  python3 scripts/check_estate_index.py --selftest   # offline fixtures

No third-party deps: stdlib only.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile

ROW_RE = re.compile(r"^\|\s*`([^`]+)`")
REPO_LINK_RE = re.compile(r"repos/([A-Za-z0-9._-]+)/(?:README\.md)?")
VERIFIED_RE = re.compile(r"verified (?:on )?\*{0,2}(\d{4}-\d{2}-\d{2})")
NON_FOLDER_CELLS = ("on demand", "none needed", "—")


def parse_rows(estate_text: str):
    """Return {repo_name: layer2_cell} for every table row whose first cell
    is a backticked repo name."""
    rows = {}
    dupes = []
    for line in estate_text.splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        name = m.group(1)
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if name in rows:
            dupes.append(name)
        rows[name] = cells[-1] if cells else ""
    return rows, dupes


def check(root: str):
    findings = []
    estate_path = os.path.join(root, "docs", "ESTATE.md")
    repos_dir = os.path.join(root, "docs", "repos")
    routes_path = os.path.join(root, ".claude", "hooks", "doc-routes.json")

    if not os.path.isfile(estate_path):
        return [("missing-index", "docs/ESTATE.md does not exist")]
    text = open(estate_path, encoding="utf-8").read()
    rows, dupes = parse_rows(text)

    for name in dupes:
        findings.append(("duplicate-row", f"`{name}` appears in more than one row"))

    if not VERIFIED_RE.search(text):
        findings.append(("missing-baseline",
                         "no 'verified YYYY-MM-DD' stamp anywhere in ESTATE.md — "
                         "staleness must be visible"))

    # The header declares how many repositories the index enumerates; the row
    # count must match, so silently dropping a folderless row (which no other
    # invariant covers) reds instead of shrinking the estate (Codex, fm #878).
    m = re.search(r"all (\d+) repositories", text)
    if not m:
        findings.append(("missing-declared-count",
                         "the header must declare 'all <N> repositories' so "
                         "row-count drift is detectable"))
    elif int(m.group(1)) != len(rows):
        findings.append(("row-count-mismatch",
                         f"header declares {m.group(1)} repositories but the "
                         f"tables hold {len(rows)} rows — a row was dropped or "
                         f"added without restating the baseline"))

    # 1. every Layer-2 folder has a row that links it
    linked_folders = set()
    for name, cell in rows.items():
        for m in REPO_LINK_RE.finditer(cell):
            linked_folders.add(m.group(1))
    if os.path.isdir(repos_dir):
        for entry in sorted(os.listdir(repos_dir)):
            if not os.path.isdir(os.path.join(repos_dir, entry)):
                continue
            if entry not in linked_folders:
                findings.append(("folder-without-row",
                                 f"docs/repos/{entry}/ exists but no ESTATE.md row "
                                 f"links it — the index no longer covers the estate"))

    # 2. every folder link in a row resolves — and belongs to that row.
    #    A swapped pair of links would leave every existence check green while
    #    routing two repos into each other's folders (Codex, fm #878).
    for name, cell in rows.items():
        for m in REPO_LINK_RE.finditer(cell):
            folder = m.group(1)
            target = os.path.join(repos_dir, folder, "README.md")
            if not os.path.isfile(target):
                findings.append(("row-links-missing-folder",
                                 f"row `{name}` links repos/{folder}/ but "
                                 f"docs/repos/{folder}/README.md does not exist"))
            if folder != name:
                findings.append(("row-links-foreign-folder",
                                 f"row `{name}`'s Layer-2 cell links "
                                 f"repos/{folder}/ — a row links its own "
                                 f"folder, never another repo's"))

    # 4. routes that target the index or a Layer-2 README. A missing route
    #    table is itself a finding — skipping route validation silently would
    #    let every reverse invariant below pass vacuously (Codex, fm #878).
    routed = {}  # folder -> {"tool": bool, "prompt": bool}
    routes = []
    if not os.path.isfile(routes_path):
        findings.append(("routes-unreadable",
                         ".claude/hooks/doc-routes.json does not exist — "
                         "route validation cannot run"))
    else:
        try:
            routes = json.load(open(routes_path, encoding="utf-8")).get("routes", [])
        except (json.JSONDecodeError, OSError) as exc:
            findings.append(("routes-unreadable", f"doc-routes.json: {exc}"))
    for route in routes:
        tools = route.get("tools") or ["Bash", "WebFetch", "Read", "Glob", "Grep"]
        is_prompt = tools == ["UserPromptSubmit"]
        for doc in route.get("docs", []):
            if doc == "docs/ESTATE.md" or (
                    doc.startswith("docs/repos/") and doc.endswith("README.md")):
                if not os.path.isfile(os.path.join(root, doc)):
                    findings.append(("route-target-missing",
                                     f"route `{route.get('id')}` targets {doc}, "
                                     f"which does not exist"))
            if doc.startswith("docs/repos/") and doc.endswith("README.md"):
                folder = doc.split("/")[2]
                if folder not in linked_folders:
                    findings.append(("folder-without-row",
                                     f"route `{route.get('id')}` targets "
                                     f"docs/repos/{folder}/ which has no "
                                     f"ESTATE.md row linking it"))
                half = routed.setdefault(folder, {"tool": False, "prompt": False})
                half["prompt" if is_prompt else "tool"] = True
                # The halves must be the documented <id>/<id>-prompt pair AND
                # actually fire on the repo's name — two unrelated routes that
                # merely target the file would otherwise satisfy the pair
                # check while naming the repo routes nothing (Codex, fm #878).
                rid = str(route.get("id", ""))
                base = rid[:-7] if rid.endswith("-prompt") else rid
                half.setdefault("ids", set()).add(base)
                # "named" = the route is recognisably the repo's own: a `when`
                # pattern matches the folder name, or the pair's base id
                # carries it (deliberately-precise patterns like
                # `menno420/superbot(?![\w-])` are legitimate and must pass).
                # Tracked PER HALF — a tool half naming the repo must not
                # certify a prompt half that never does (Codex, fm #878 r3).
                named_key = "named_prompt" if is_prompt else "named_tool"
                if folder in base:
                    half[named_key] = True
                try:
                    if any(re.search(p, folder, re.I)
                           for p in route.get("when", [])):
                        half[named_key] = True
                except re.error:
                    pass

    # 5. every built folder ships with its route PAIR (docs/repos/README.md
    #    § The files: "a built folder ships with its doc-route pair" — the
    #    product-forge week-long routeless gap is the measured failure). Runs
    #    whenever the route table was readable, so an EMPTY table with built
    #    folders reds rather than passing vacuously.
    routes_ok = not any(k == "routes-unreadable" for k, _ in findings)
    if routes_ok and os.path.isdir(repos_dir):
        for entry in sorted(os.listdir(repos_dir)):
            if not os.path.isdir(os.path.join(repos_dir, entry)):
                continue
            halves = routed.get(entry, {"tool": False, "prompt": False})
            missing = [k for k in ("tool", "prompt") if not halves.get(k)]
            if missing:
                findings.append(("folder-without-route-pair",
                                 f"docs/repos/{entry}/ has no "
                                 f"{' or '.join(missing)} route half in "
                                 f"doc-routes.json — a built folder ships "
                                 f"with its route pair"))
                continue
            if len(halves.get("ids", set())) != 1:
                findings.append(("route-pair-id-mismatch",
                                 f"docs/repos/{entry}/'s routes are not one "
                                 f"<id>/<id>-prompt pair (ids: "
                                 f"{sorted(halves.get('ids', set()))})"))
            unnamed = [h for h in ("tool", "prompt")
                       if not halves.get(f"named_{h}")]
            if unnamed:
                findings.append(("route-pair-unnamed",
                                 f"docs/repos/{entry}/'s "
                                 f"{' and '.join(unnamed)} route half never "
                                 f"matches the repo's own name — naming the "
                                 f"repo would route nothing on that event"))
    return findings


def selftest() -> int:
    failures = []

    def build(tmp, estate, folders=(), routes=None, routes_file=True):
        os.makedirs(os.path.join(tmp, "docs", "repos"), exist_ok=True)
        os.makedirs(os.path.join(tmp, ".claude", "hooks"), exist_ok=True)
        with open(os.path.join(tmp, "docs", "ESTATE.md"), "w") as f:
            f.write(estate)
        for name in folders:
            d = os.path.join(tmp, "docs", "repos", name)
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, "README.md"), "w") as f:
                f.write("# entry\n")
        if routes_file:
            with open(os.path.join(tmp, ".claude", "hooks",
                                   "doc-routes.json"), "w") as f:
                json.dump({"routes": routes or []}, f)

    clean = ("# index\nall 2 repositories verified 2026-08-21 baseline\n"
             "| `alpha` | thing | [entry](repos/alpha/README.md) |\n"
             "| `beta` | thing | on demand |\n")
    pair = [{"id": "r2", "when": ["alpha"],
             "docs": ["docs/repos/alpha/README.md"]},
            {"id": "r2-prompt", "tools": ["UserPromptSubmit"],
             "when": ["alpha"],
             "docs": ["docs/repos/alpha/README.md"]}]

    # positive: clean tree (folder + row + full route pair)
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, clean, folders=["alpha"],
              routes=[{"id": "r1", "docs": ["docs/ESTATE.md"]}] + pair)
        got = check(tmp)
        if got:
            failures.append(f"clean tree flagged: {got}")

    # negative: folder without a row
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, clean, folders=["alpha", "gamma"], routes=pair)
        kinds = [k for k, _ in check(tmp)]
        if "folder-without-row" not in kinds:
            failures.append("missed folder-without-row")

    # negative: swapped/foreign folder link (row `beta` links alpha's folder)
    with tempfile.TemporaryDirectory() as tmp:
        swapped = ("# index\nverified 2026-08-21 baseline\n"
                   "| `alpha` | thing | [entry](repos/alpha/README.md) |\n"
                   "| `beta` | thing | [entry](repos/alpha/README.md) |\n")
        build(tmp, swapped, folders=["alpha"], routes=pair)
        kinds = [k for k, _ in check(tmp)]
        if "row-links-foreign-folder" not in kinds:
            failures.append("missed row-links-foreign-folder")

    # negative: built folder missing one half of its route pair
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, clean, folders=["alpha"], routes=[pair[0]])  # tool half only
        kinds = [k for k, _ in check(tmp)]
        if "folder-without-route-pair" not in kinds:
            failures.append("missed folder-without-route-pair")

    # negative: two unrelated routes masquerading as a pair (wrong ids, and
    # neither pattern names the repo)
    with tempfile.TemporaryDirectory() as tmp:
        fake = [{"id": "zzz-route", "when": ["omega"],
                 "docs": ["docs/repos/alpha/README.md"]},
                {"id": "other-prompt", "tools": ["UserPromptSubmit"],
                 "when": ["omega"], "docs": ["docs/repos/alpha/README.md"]}]
        build(tmp, clean, folders=["alpha"], routes=fake)
        kinds = [k for k, _ in check(tmp)]
        if "route-pair-id-mismatch" not in kinds:
            failures.append("missed route-pair-id-mismatch")
        if "route-pair-unnamed" not in kinds:
            failures.append("missed route-pair-unnamed")

    # negative: only ONE half names the repo (per-half coverage — a naming
    # tool half must not certify a prompt half that matches something else)
    with tempfile.TemporaryDirectory() as tmp:
        lopsided = [{"id": "zz", "when": ["alpha"],
                     "docs": ["docs/repos/alpha/README.md"]},
                    {"id": "zz-prompt", "tools": ["UserPromptSubmit"],
                     "when": ["omega"],
                     "docs": ["docs/repos/alpha/README.md"]}]
        build(tmp, clean, folders=["alpha"], routes=lopsided)
        kinds = [k for k, _ in check(tmp)]
        if "route-pair-unnamed" not in kinds:
            failures.append("missed per-half route-pair-unnamed")

    # negative: routes table missing entirely
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, clean, folders=["alpha"], routes_file=False)
        kinds = [k for k, _ in check(tmp)]
        if "routes-unreadable" not in kinds:
            failures.append("missed routes-unreadable on absent table")

    # negative: a folderless row dropped without restating the baseline
    with tempfile.TemporaryDirectory() as tmp:
        shrunk = ("# index\nall 2 repositories verified 2026-08-21 baseline\n"
                  "| `alpha` | thing | [entry](repos/alpha/README.md) |\n")
        build(tmp, shrunk, folders=["alpha"], routes=pair)
        kinds = [k for k, _ in check(tmp)]
        if "row-count-mismatch" not in kinds:
            failures.append("missed row-count-mismatch")

    # negative: row links a missing folder
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, clean, folders=[])
        kinds = [k for k, _ in check(tmp)]
        if "row-links-missing-folder" not in kinds:
            failures.append("missed row-links-missing-folder")

    # negative: duplicate row
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, clean + "| `alpha` | again | on demand |\n", folders=["alpha"])
        kinds = [k for k, _ in check(tmp)]
        if "duplicate-row" not in kinds:
            failures.append("missed duplicate-row")

    # stale/missing-data: no verified stamp
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, "# index\n| `alpha` | thing | on demand |\n", folders=[])
        kinds = [k for k, _ in check(tmp)]
        if "missing-baseline" not in kinds:
            failures.append("missed missing-baseline")

    # negative: route targets a README that does not exist
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, clean, folders=["alpha"],
              routes=[{"id": "r3", "docs": ["docs/repos/omega/README.md"]}])
        kinds = [k for k, _ in check(tmp)]
        if "route-target-missing" not in kinds:
            failures.append("missed route-target-missing")

    # missing index entirely
    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(os.path.join(tmp, "docs"), exist_ok=True)
        kinds = [k for k, _ in check(tmp)]
        if "missing-index" not in kinds:
            failures.append("missed missing-index")

    if failures:
        for f in failures:
            print(f"SELFTEST FAIL: {f}")
        return 1
    print("selftest: 13/13 cases pass")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--advisory", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    findings = check(os.path.abspath(args.root))
    for kind, msg in findings:
        if args.advisory:
            print(f"::warning::estate-index {kind}: {msg}")
        else:
            print(f"FLAG {kind}: {msg}")
    print(f"{len(findings)} finding(s)")
    if args.advisory:
        return 0
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
