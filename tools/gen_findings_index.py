#!/usr/bin/env python3
"""gen_findings_index.py — keep docs/findings/README.md's membership true.

================================ PROVENANCE ================================
Why added : Owner, live 2026-09-01, authorizing the fix after a measurement:
            the index listed 65 of 72 findings. Its own header records being
            "regenerated **complete** on 2026-08-10 ... after the old index was
            measured listing 25 of 42" — so this is the SECOND drift in three
            weeks, by the same mechanism: a hand-kept index of a directory that
            keeps growing. The estate already knows the answer and applies it
            elsewhere (owner/README.md, docs/owner-comments/*/README.md,
            owner/intent-workbooks/PROGRESS.md are all generated + drift-
            checked). This surface simply never got it.
What it does: reconciles the table's MEMBERSHIP against the directory. It does
            NOT rewrite descriptions.
The split, and it is the whole design:
            * MEMBERSHIP is mechanical      -> generated, drift-checked.
            * DESCRIPTION is authored value -> preserved VERBATIM, forever.
            An existing row's prose is carried through untouched, ★ included.
            A file with no row gets a placeholder built from ITS OWN `# ` title,
            quoted -- never a description invented from the filename. That
            distinction is TRAP-008, added to the register the same day after
            six instances, one of which was characterising a findings file from
            its name alone. A generator that summarised files it had not read
            would automate the trap.
Honest nulls: a file whose title cannot be read is listed with an explicit
            "title unreadable" marker rather than skipped or guessed.
Date      : 2026-09-01
============================================================================
"""

from __future__ import annotations

import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
DIR = REPO / "docs" / "findings"
OUT = DIR / "README.md"

ROW = re.compile(r"^\| (★ )?\[`([^`]+)`\]\([^)]*\) \| (.*?) \|\s*$", re.M)
TABLE_HEAD = "| finding | what it holds |\n|---|---|\n"


def title_of(path: pathlib.Path) -> str:
    """The file's OWN h1, quoted. Never a summary written here."""
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    except OSError:
        return "**title unreadable** — file could not be opened; row added so "\
               "the gap is visible, description still owed"
    return "**no `# ` title** — row added so the gap is visible, description "\
           "still owed"


def build() -> tuple[str, int, int]:
    text = OUT.read_text(encoding="utf-8")
    kept = {m.group(2): (m.group(1) or "", m.group(3)) for m in ROW.finditer(text)}
    files = sorted((p for p in DIR.glob("*.md") if p.name != "README.md"),
                   key=lambda p: p.name, reverse=True)

    lines = []
    added = 0
    for p in files:
        star, desc = kept.get(p.name, ("", None))
        if desc is None:
            added += 1
            desc = (f"*(indexed 2026-09-01 by `tools/gen_findings_index.py`; "
                    f"description still owed)* — its own title: “{title_of(p)}”")
        lines.append(f"| {star}[`{p.name}`]({p.name}) | {desc} |")

    head, _, rest = text.partition(TABLE_HEAD)
    tail = rest[rest.rfind("|\n") + 2:] if "|\n" in rest else "\n"
    return head + TABLE_HEAD + "\n".join(lines) + "\n" + tail, len(files), added


def main() -> int:
    if not DIR.is_dir():
        print(f"findings index: {DIR} is not a directory")
        return 1
    content, total, added = build()

    if "--check" in sys.argv:
        if OUT.read_text(encoding="utf-8") != content:
            print("findings index: DRIFT — docs/findings/README.md does not list "
                  "every finding (or lists one that is gone); run "
                  "`python3 tools/gen_findings_index.py` and commit the result")
            return 1
        print(f"findings index: current — {total} finding(s) listed")
        return 0

    OUT.write_text(content, encoding="utf-8")
    print(f"findings index: {total} finding(s) listed ({added} newly added) -> "
          f"{OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
