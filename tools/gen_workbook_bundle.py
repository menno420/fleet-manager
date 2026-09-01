#!/usr/bin/env python3
"""gen_workbook_bundle.py — one file holding every intent worksheet, and the
splitter that puts the answers back.

================================ PROVENANCE ================================
Why added : Owner, live 2026-09-01. He is pausing every AI subscription for
            about a week to answer the workbook collection. 74 worksheets in a
            nested tree is desk work; one document is couch/phone work, and he
            asked for the bundle so the week is spent writing rather than
            navigating.
The danger, and why --split exists:
            a bundle is a COPY of 74 files. docs/intent.md § 5 names "a second
            source of truth for anything a repo owns" as a non-goal, and a
            read-only bundle he cannot write back would be exactly that -- he
            answers in it, the worksheets never change, and a week of his words
            sits in a file nothing reads. So the bundle is deliberately
            TWO-WAY: generate out, edit anywhere, `--split` back. Shipping the
            generator without the splitter would have been the trap.
Direction : the WORKSHEETS are canonical. The bundle is a working copy.
            `--split` is how a working copy stops being a second truth.
Not gated : deliberately NOT wired into scripts/preflight.py. A drift lane
            would red continuously the moment he starts writing in the bundle
            -- a gate that fights its own user. The findings index gets a lane
            (its drift is silent decay); this one must not.
Safety    : --split is ALL-OR-NOTHING. If any marker names a file that does not
            exist, or the bundle's markers do not reconcile with the tree,
            nothing is written and the mismatch is reported. A partial split
            would silently lose part of a week of his writing.
Date      : 2026-09-01
============================================================================
"""

from __future__ import annotations

import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
ROOT = REPO / "owner" / "intent-workbooks"
OUT = ROOT / "ALL-IN-ONE.md"
SKIP = {"README.md", "PROGRESS.md", "HOW-TO-ANSWER.md", "WHEN-I-AM-BACK.md",
        "ALL-IN-ONE.md"}

# The markers sit on their own lines and the body between them is embedded
# VERBATIM -- no stripping, no padding. Measured 2026-09-01: 49 of 85 files in
# this tree do not end in exactly one newline, so a split that normalised
# trailing whitespace rewrote 46 worksheets on a no-op round trip. A tool that
# silently reformats a week of the owner's handwriting is worse than no tool.
BEGIN = "<!-- ===== BEGIN {} ===== -->"
END = "<!-- ===== END {} ===== -->"

HEADER = """# Every worksheet, in one file

> **Working copy — generated, and two-way.** The individual worksheets under
> `owner/intent-workbooks/` are canonical. This file exists so the collection
> can be read and answered in one place, on a phone or tablet, with no tooling.
>
> **Answer anywhere in it.** Use `OWNER:` on its own line, or an inline
> `(OWNER <date>: …)` — the same convention as the separate files
> (`HOW-TO-ANSWER.md`). Nothing else is parsed.
>
> **When you are back**, one command puts every answer into its own worksheet:
>
> ```
> python3 tools/gen_workbook_bundle.py --split
> ```
>
> It is all-or-nothing: if anything about the file's structure does not
> reconcile, it writes nothing and says what is wrong. Do not delete the
> `<!-- ===== BEGIN … -->` / `<!-- ===== END … -->` comment lines — they are
> how your writing finds its way home. Everything between them is yours to
> change.

---

"""


def worksheets() -> list[pathlib.Path]:
    return sorted((p for p in ROOT.rglob("*.md") if p.name not in SKIP),
                  key=lambda p: p.relative_to(ROOT).as_posix())


def build() -> str:
    parts = [HEADER, "## Contents\n\n"]
    sheets = worksheets()
    for p in sheets:
        rel = p.relative_to(ROOT).as_posix()
        parts.append(f"- `{rel}`\n")
    parts.append("\n---\n\n")
    for p in sheets:
        rel = p.relative_to(ROOT).as_posix()
        body = p.read_text(encoding="utf-8")
        parts.append(f"{BEGIN.format(rel)}\n{body}{END.format(rel)}\n\n---\n\n")
    return "".join(parts)


def split() -> int:
    if not OUT.exists():
        print(f"bundle: {OUT.relative_to(REPO)} does not exist — generate it first")
        return 1
    text = OUT.read_text(encoding="utf-8")
    pending: list[tuple[pathlib.Path, str]] = []
    problems: list[str] = []

    for p in worksheets():
        rel = p.relative_to(ROOT).as_posix()
        b, e = BEGIN.format(rel), END.format(rel)
        if text.count(b) != 1 or text.count(e) != 1:
            problems.append(f"{rel}: expected exactly one BEGIN and one END "
                            f"marker, found {text.count(b)}/{text.count(e)}")
            continue
        # Byte-exact: everything between the BEGIN line's newline and the
        # END marker is the file, unchanged.
        body = text.split(b + "\n", 1)[1].split(e, 1)[0]
        pending.append((p, body))

    # Every marker in the file must correspond to a real worksheet.
    for line in text.splitlines():
        if line.startswith("<!-- ===== BEGIN "):
            rel = line[len("<!-- ===== BEGIN "):].split(" =====")[0]
            if not (ROOT / rel).is_file():
                problems.append(f"{rel}: marker names a file that does not exist")

    if problems:
        print("bundle --split: REFUSED, nothing written —")
        for p_ in problems:
            print(f"  {p_}")
        return 1

    changed = [p for p, body in pending
               if p.read_text(encoding="utf-8") != body]
    for p, body in pending:
        if p.read_text(encoding="utf-8") != body:
            p.write_text(body, encoding="utf-8")
    print(f"bundle --split: {len(pending)} worksheet(s) reconciled, "
          f"{len(changed)} updated")
    for p in changed:
        print(f"  updated {p.relative_to(REPO)}")
    return 0


def main() -> int:
    if "--split" in sys.argv:
        return split()
    content = build()
    if "--check" in sys.argv:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != content:
            print("bundle: stale or missing — run "
                  "`python3 tools/gen_workbook_bundle.py`")
            return 1
        print(f"bundle: {OUT.relative_to(REPO)} matches the worksheets")
        return 0
    OUT.write_text(content, encoding="utf-8")
    print(f"bundle: {len(worksheets())} worksheet(s) -> {OUT.relative_to(REPO)} "
          f"({len(content.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
