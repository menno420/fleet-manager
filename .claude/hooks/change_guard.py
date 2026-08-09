#!/usr/bin/env python3
"""change_guard — three checks that fire at the moment a change is made.

Built 2026-08-09 from fm #830's error ledger, which recorded 13 errors and
attributed each to whatever caught it. **Zero were caught by documentation being
available.** The three classes below were picked because each recurred, each is
mechanically decidable, and each has a moment where a machine can see it and the
author reliably cannot.

    A  PreToolUse   kit-skill amendment    — the change will be silently reverted
    B  PreToolUse   markdown table breaks  — rows will render as literal text
    C  PostToolUse  un-propagated edit     — the old text survives elsewhere

**C is why this file exists at an event nothing else uses.** The estate had
hooks on `PreToolUse` (3), `Stop` (1) and `UserPromptSubmit` (1), and **nothing
on `PostToolUse`** — so no mechanism could ever say *"that worked, and here is
what it implies."* Propagation is only knowable after the edit lands: before it,
the old string is still everywhere by definition.

**Advisory, fail-open, silent unless it has something.** Never blocks, never
raises, exits 0 on every path including its own bugs — a guard that breaks a
session is worse than the defect it hunts. Noise is the enemy: `check --strict`
already prints 94 advisory lines with the verdict at line 92, and these checks
earn their place only by staying quiet.

Registered for `Write|Edit|MultiEdit` on `PreToolUse` and `Edit|MultiEdit` on
`PostToolUse`. Lives in `.claude/hooks/`, which is **not** in the kit copy loop —
unlike `.claude/skills/`, whose 14 kit-named entries check A exists to protect.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(
    os.environ.get("CLAUDE_PROJECT_DIR")
    or subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=False,
    ).stdout.strip()
    or "."
)

# A change smaller than this is not worth a propagation grep — short strings are
# common substrings and the check would fire on everything.
MIN_FRAGMENT = 45
# Words per shingle. Long enough to be distinctive, short enough to survive the
# rewrapping that a copy in another document almost always has.
SHINGLE = 9
# More hits than this means the phrase is idiomatic, not a claim being corrected.
MAX_HITS = 8
RE_APPLY_DOC = "docs/SKILLS-local.md"


# ---------------------------------------------------------------- check A
def kit_skill_amendment(target: str) -> str | None:
    """Editing a kit-shipped skill? The next upgrade reverts it.

    fm #830 P1: `intake` was amended with the whole Phase 2 intent map. The
    documented copy loop overwrites every kit-named skill from
    `.substrate/skills/`, whose staged copy still held the superseded body — so
    the upgrade the owner had just approved would have reverted Phase 2 while
    the roadmap and two ledgers went on claiming it ran. Caught by Codex, not by
    the author, who had read the warning 60 lines from his own edit.
    """
    m = re.search(r"\.claude/skills/([^/]+)/SKILL\.md$", target.replace("\\", "/"))
    if not m:
        return None
    name = m.group(1)
    if not (REPO / ".substrate" / "skills" / name / "SKILL.md").is_file():
        return None  # fm-local skill — nothing reverts it

    # Scope the lookup to the ⚠ re-apply region, NOT the whole document. Every
    # skill is named in that file's 27-row roster, so a whole-file search reports
    # "already listed" for all of them — measured while testing this hook, on
    # `analysis`, which has no amendment at all.
    listed = False
    doc = REPO / RE_APPLY_DOC
    if doc.is_file():
        text = doc.read_text(errors="replace")
        for start in (i for i, _ in enumerate(text) if text.startswith("⚠", i)):
            end = text.find("\n## ", start)
            region = text[start: end if end != -1 else len(text)]
            if f"`{name}`" in region:
                listed = True
                break

    note = (
        f"KIT-NAMED SKILL — `{name}` is shipped by the kit and staged at "
        f"`.substrate/skills/{name}/SKILL.md`. The documented copy loop in "
        f"{RE_APPLY_DOC} overwrites every kit-named skill from that staged tree, "
        f"so **this amendment is reverted by the next `upgrade-distribution` run** "
        f"and the record keeps claiming it is live."
    )
    if listed:
        return note + (
            f" `{name}` IS already named in {RE_APPLY_DOC} — check it is in the "
            f"⚠ re-apply table specifically, not just mentioned, and that the "
            f"entry still describes what you are about to change."
        )
    return note + (
        f" **`{name}` is NOT named in {RE_APPLY_DOC}.** Add it to the ⚠ re-apply "
        f"table beside `session-close`, or promote the change upstream to "
        f"substrate-kit so every adopter gets it instead of one repo losing it."
    )


# ---------------------------------------------------------------- check B
def orphan_table_rows(content: str) -> str | None:
    """Table rows with no delimiter row above them render as literal pipe text.

    GFM needs `| --- |` under a header before any row parses as a table. Prose
    inserted mid-table silently splits it, and the rows below become plain text
    with visible pipes.

    Measured twice: `2026-08-08-layer2-ratification.md` shipped 6 of 11 error
    rows as literal text, and the session that repaired it reproduced the exact
    defect at the exact count in its own card four hours later — 2 for 2 in the
    only two cards carrying multi-part tables.
    """
    lines = content.split("\n")
    in_table = False
    orphans: list[int] = []
    for i, line in enumerate(lines):
        is_row = line.lstrip().startswith("|")
        if is_row and not in_table:
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if re.match(r"^\s*\|[\s:|-]+\|", nxt):
                in_table = True
            else:
                orphans.append(i + 1)
        elif not is_row and not line.strip():
            in_table = False
    if not orphans:
        return None
    where = ", ".join(f"L{n}" for n in orphans[:6])
    more = f" (+{len(orphans) - 6} more)" if len(orphans) > 6 else ""
    return (
        f"TABLE BREAK — {len(orphans)} row(s) start with `|` but have no "
        f"delimiter row above them: {where}{more}. GFM will render these as "
        f"literal pipe-delimited text, not table rows. Usually a blank line or a "
        f"paragraph split the table: close the gap, or give the fragment its own "
        f"header + `|---|` row."
    )


# ---------------------------------------------------------------- check C
def _fragments(old: str) -> list[str]:
    """Word-shingles from the replaced text, to hunt for surviving copies.

    **Whole-line matching was tried first and does not work**, measured while
    building this: a copy in another document is almost never a copy of the same
    *line* — it is the same claim wrapped differently. Shingles of a few words
    survive rewrapping, reindentation and surrounding edits, and stay exact
    (no fuzzy matching, so no false positives from near-misses).

    **MEASURED 2026-08-09 — this check does NOT catch the case it was built for,
    and that is the most useful thing known about it.** Both of fm #830's
    propagation failures were replayed against it from git:

      · error #6      roadmap *"false-negative rate of 1 in 21"* vs the program
                      ledger's *"a 1-in-21 false-negative rate"*  → SILENT
      · round-2 #2    the pre-fix `intake` line at `28ecc2c`, against the three
                      other files carrying the same claim               → SILENT

    Both were **paraphrases**, and no exact matcher reaches a paraphrase. What it
    does catch is verbatim survivors, which are common here — 441 duplicated
    9-word shingles across the repo's markdown at the time of writing — so it
    earns its place on a different class than the one that prompted it.

    **A clean run is therefore not evidence that a correction propagated.** The
    paraphrase class currently has no mechanical catcher; Codex found both, by
    reading for meaning rather than for strings.
    """
    words = re.sub(r"\s+", " ", re.sub(r"[`*_|>#]", "", old)).strip().split(" ")
    words = [w for w in words if w]
    if len(words) < SHINGLE:
        return []
    spans = [0, max(0, (len(words) - SHINGLE) // 2), max(0, len(words) - SHINGLE)]
    out: list[str] = []
    for s in dict.fromkeys(spans):                     # dedupe, keep order
        frag = " ".join(words[s: s + SHINGLE])
        if len(frag) >= MIN_FRAGMENT and frag not in out:
            out.append(frag)
    return out[:3]


def unpropagated(old: str, target: str) -> str | None:
    """The text you just replaced still exists somewhere else.

    fm #830's most repeated defect, three times in one session: a claim was
    corrected in one file while a copy stood in another, each time in a document
    a session actually reads. Once the copy was in the *same ledger row* as the
    fix. Codex found the first; the third was found while fixing the second.

    Only knowable *after* the edit: before it, the string is still in the target.
    """
    frags = _fragments(old)
    if not frags:
        return None
    tgt = os.path.relpath(target, REPO) if os.path.isabs(target) else target
    hits: list[str] = []
    frag = frags[0]
    for f in frags:
        try:
            out = subprocess.run(
                ["git", "grep", "-l", "--fixed-strings", f],
                cwd=REPO, capture_output=True, text=True, timeout=10, check=False,
            ).stdout
        except Exception:
            continue
        found = [h.strip() for h in out.split("\n") if h.strip() and h.strip() != tgt]
        if found:
            frag = f
            hits = sorted(set(hits) | set(found))
    if not hits or len(hits) > MAX_HITS:
        return None
    shown = "\n".join(f"  · {h}" for h in hits[:MAX_HITS])
    return (
        f"STILL ELSEWHERE — the text you just replaced survives in "
        f"{len(hits)} other file(s):\n{shown}\n"
        f'Matched on: "{frag[:90]}{"…" if len(frag) > 90 else ""}"\n'
        f"If this was a correction, those copies now contradict it, and a session "
        f"reading them gets the superseded version. Fixing the source and leaving "
        f"the copies is this repo's most-repeated defect — three times in fm #830 "
        f"alone, once inside the fix for the previous instance."
    )


# ---------------------------------------------------------------- driver
def emit(event: str, notes: list[str]) -> None:
    if not notes:
        return
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": event,
            "additionalContext": "\n\n".join(notes),
        }
    }))


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except Exception:
        return 0

    name = event.get("hook_event_name", "")
    tool = event.get("tool_name", "")
    inp = event.get("tool_input") or {}
    target = str(inp.get("file_path", ""))
    notes: list[str] = []

    if name == "PreToolUse":
        if target:
            hit = kit_skill_amendment(target)
            if hit:
                notes.append(hit)
        if target.endswith(".md"):
            body = inp.get("content") or inp.get("new_string") or ""
            if body:
                hit = orphan_table_rows(body)
                if hit:
                    notes.append(hit)

    elif name == "PostToolUse" and tool in {"Edit", "MultiEdit"}:
        edits = inp.get("edits") or [inp]
        for e in edits[:5]:
            old = e.get("old_string") or ""
            if old:
                hit = unpropagated(old, target)
                if hit:
                    notes.append(hit)
                    break  # one is enough to make the point

    emit(name, notes)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        # Fail-open, always. A guard that breaks the session is worse than the
        # defect it hunts — owner_review.py earned this the hard way when an
        # uncaught error exited 1 at every Stop.
        sys.exit(0)
