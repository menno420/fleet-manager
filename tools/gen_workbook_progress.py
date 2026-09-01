#!/usr/bin/env python3
"""gen_workbook_progress.py — read every owner intent worksheet, detect which
ones the owner has written in, and generate owner/intent-workbooks/PROGRESS.md.

================================ PROVENANCE ================================
Why added : Owner, live 2026-09-01: he is pausing every AI subscription for
            about a week to read and answer the workbook collection, then
            restarting them gradually. That plan has one structural gap — for
            the whole week NO agent is running, so nothing observes the
            answers as they are written, and the first session back has to
            find them across ~75 files. Re-reading the collection by hand to
            locate owner text is exactly the kind of judgement-heavy sweep
            this estate keeps getting wrong (docs/traps.md TRAP-003: a
            keyword search is not a read; TRAP-004: a sample published as a
            census). A deterministic marker plus a generated index removes
            the judgement entirely.
What it does: walks owner/intent-workbooks/**/*.md, skips the indexes, and
            classifies each worksheet as answered / unanswered by looking for
            an owner marker. Writes a progress page grouped by section.
Detection : two literal forms, case-insensitive, and BOTH are required
            because the owner already used the second one before this tool
            existed (owner/intent-workbooks/estate/why-this-estate-exists.md,
            landed fm #995):
              1. a line that is exactly the `OWNER:` block marker, with any
                 non-whitespace text after it or on a following line;
              2. an inline `(OWNER <date>: …)` or `(Owner reply <date>: …)`.
            The bare `\x60OWNER\x60:` template line with nothing after it is
            NOT an answer — every unanswered worksheet ends with one, so
            treating it as a hit would report 100% on an empty collection.
            That negative control is asserted in main().
Design    : GENERATED, never hand-maintained — same contract as
            tools/gen_owner_index.py. The worksheets are the truth; this only
            counts them. A hand-ticked checklist would drift the first time
            he answered a page without updating it, and during the offline
            week he cannot run the generator to correct it.
Honest nulls: a file that cannot be read is listed as unreadable in the
            output rather than silently dropped.
Date      : 2026-09-01
============================================================================
"""

from __future__ import annotations

import datetime
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
ROOT = REPO / "owner" / "intent-workbooks"
OUT = ROOT / "PROGRESS.md"

# Files that are indexes or instructions, not worksheets with an OWNER slot.
NOT_A_WORKSHEET = {"README.md", "PROGRESS.md", "HOW-TO-ANSWER.md",
                   "WHEN-I-AM-BACK.md"}

# Form 2: an inline marker the owner writes mid-page.
INLINE = re.compile(r"\(\s*owner(?:\s+reply)?\s+[^:)]{0,40}:", re.IGNORECASE)
# Form 1: the block marker at the end of a worksheet.
BLOCK = re.compile(r"^`?OWNER`?\s*:\s*(.*)$", re.IGNORECASE)

SECTION_TITLES = {
    ".": "Top level",
    "estate": "The estate as a whole",
    "you": "You",
    "agents": "The agent working contract",
    "products": "The products",
    "successor": "The new hub",
    "folders": "Folder contracts",
    "repositories": "One per repository",
}


def answered(text: str) -> bool:
    """True when the owner has written anything under either marker."""
    if INLINE.search(text):
        return True
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = BLOCK.match(line.strip())
        if not m:
            continue
        # Same line, or any non-blank line after it.
        if m.group(1).strip():
            return True
        if any(ln.strip() for ln in lines[i + 1:]):
            return True
    return False


def worksheets() -> tuple[dict[str, list[tuple[str, bool]]], list[str]]:
    found: dict[str, list[tuple[str, bool]]] = {}
    unreadable: list[str] = []
    for path in sorted(ROOT.rglob("*.md")):
        if path.name in NOT_A_WORKSHEET:
            continue
        rel = path.relative_to(ROOT)
        section = rel.parent.as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            unreadable.append(rel.as_posix())
            continue
        found.setdefault(section, []).append((rel.as_posix(), answered(text)))
    return found, unreadable


def render(found, unreadable, stamp: str) -> str:
    total = sum(len(v) for v in found.values())
    done = sum(1 for v in found.values() for _, ok in v if ok)
    L: list[str] = []
    a = L.append
    a("# Workbook progress")
    a("")
    a("> **Status:** `generated` — **do not hand-edit;** regenerate with")
    a("> `python3 tools/gen_workbook_progress.py`. It reads the worksheets")
    a("> themselves, so it cannot disagree with them. Ticking a box here by")
    a("> hand would be undone the next time it runs.")
    a(">")
    a(f"> generated-at {stamp}")
    a("")
    a(f"**{done} of {total} worksheets carry your words.** A worksheet counts as")
    a("answered when it contains an `OWNER:` block with text under it, or an")
    a("inline `(OWNER <date>: …)` marker — see")
    a("[`HOW-TO-ANSWER.md`](HOW-TO-ANSWER.md).")
    a("")
    a("Nothing here is a deadline and no order is required. The count exists so")
    a("the first session after your offline week knows where to look instead of")
    a("re-reading every file.")
    a("")
    if unreadable:
        a(f"⚠ **{len(unreadable)} file(s) could not be read** and are excluded "
          "from the count: " + ", ".join(f"`{u}`" for u in unreadable))
        a("")
    for section in sorted(found, key=lambda s: (s == ".", s)):
        rows = sorted(found[section])
        sec_done = sum(1 for _, ok in rows if ok)
        title = SECTION_TITLES.get(section, f"`{section}/`")
        a(f"## {title} — {sec_done}/{len(rows)}")
        a("")
        for rel, ok in rows:
            mark = "✅" if ok else "☐"
            a(f"- {mark} [`{rel}`]({rel})")
        a("")
    return "\n".join(L) + "\n"


def main() -> int:
    found, unreadable = worksheets()
    if not found:
        print(f"workbook progress: no worksheets under {ROOT.relative_to(REPO)}")
        return 1

    # Negative control, asserted every run: the bare template tail that every
    # unanswered worksheet ends with must NOT read as an answer. Without this
    # the tool would report every page complete and nobody would notice.
    assert not answered("## Your words\n\n`OWNER`:\n"), \
        "detector reads an empty OWNER slot as answered"
    assert answered("## Your words\n\n`OWNER`:\nyes, this is why.\n")
    assert answered("(Owner reply 31-08-2026: yes)\n")

    stamp = datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")
    content = render(found, unreadable, stamp)

    if "--check" in sys.argv:
        strip = lambda s: "\n".join(
            ln for ln in s.splitlines() if not ln.startswith("> generated-at "))
        try:
            live = OUT.read_text(encoding="utf-8")
        except OSError:
            print(f"workbook progress: {OUT.relative_to(REPO)} is missing — run "
                  "`python3 tools/gen_workbook_progress.py`")
            return 1
        if strip(live) != strip(content):
            print(f"workbook progress: DRIFT — {OUT.relative_to(REPO)} does not "
                  "match the worksheets; run "
                  "`python3 tools/gen_workbook_progress.py` and commit the result")
            return 1
        print(f"workbook progress: {OUT.relative_to(REPO)} is current")
        return 0

    OUT.write_text(content, encoding="utf-8")
    total = sum(len(v) for v in found.values())
    done = sum(1 for v in found.values() for _, ok in v if ok)
    print(f"workbook progress: {done} of {total} worksheets answered -> "
          f"{OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
