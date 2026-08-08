#!/usr/bin/env python3
"""PreToolUse hook: notice when a session describes a file it has not opened.

The failure this exists to stop, MEASURED 2026-08-08 on this repo's own
transcript. A session built `docs/repos/spider-swing/` and wrote a boot-path
table describing eight of that repo's files with one line each. Split by whether
the session had actually fetched the file before writing the line:

    fetched first (3 files) -> 0 wrong
    not fetched   (5 files) -> 3 wrong

The three errors were all the same shape and all plausible: `AGENT_ORIENTATION.md`
called an instruction set when it is a reading-*router*, `decisions.md` called an
ADR log when it cites `[D-NNNN]` ids, and `architecture.md` listed as ordinary
reference when its badge is `binding` — so a downstream session would have been
told there was one binding contract where there are two.

**The point is that an unread description reads exactly like a read one.** There
is no hedge in the prose to notice, no uncertainty marker, nothing a reviewer
could catch without opening the file themselves. That is what makes it worth a
mechanism rather than a rule: prose cannot signal its own provenance, but the
transcript can.

WHAT THIS CHECKS, AND WHAT IT DELIBERATELY DOES NOT

It checks a **fact**: did this session issue a read whose input named this path,
before writing prose about it. That is mechanisable and is all this does.

It does NOT check whether the file was *understood* — that is a judgement, and
this estate has twice withdrawn a gate that tried to mechanise meaning (the
provenance gate, and the "attached a repo => touched its folder" gate). Hence:

1. **Advisory. Never blocks.** Exit 0 on every path including a crash.
2. **Silent unless it has something.** Once per path per session, capped.
3. **No repo writes.** Session state lives in /tmp, keyed by session id.

Registered on PreToolUse for both halves — read tools record, Write/Edit check.
Recording on PreToolUse rather than PostToolUse means an attempted read counts
even if it failed; that is the lenient direction, which is the right one for an
advisory that must not cry wolf.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

STATE_DIR = Path(os.environ.get("TMPDIR", "/tmp")) / "claude-read-set"

RECORD_TOOLS = {"Read", "Grep", "Glob", "WebFetch", "Bash", "NotebookRead"}
CHECK_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
RECORD_FIELDS = ("file_path", "command", "url", "pattern", "path", "glob", "notebook_path")

# A path-like token: at least one directory separator or a known doc/code
# extension, so bare prose words never qualify.
PATH_RE = re.compile(
    r"(?<![\w./-])((?:[\w.-]+/)+[\w.-]+\.\w{1,5}|[\w-]+\.(?:md|py|gd|json|ya?ml|toml|cfg|sh|ts|js))(?![\w/])"
)

# Only a path that is FOLLOWED BY PROSE is a description. A bare link, an import,
# or a path in a command is a pointer and is none of this hook's business. The
# separators are the ones a describing line actually uses: a markdown table cell,
# an em-dash gloss, or a colon.
DESCRIBED_RE = re.compile(
    r"`?([^`\s|]+\.\w{1,5})`?\s*(?:\|[^|\n]*?|[—:-]\s+)(\S+(?:\s+\S+){2,})"
)

MAX_REPORTED = 5


def tokens(text: str) -> set[str]:
    return set(PATH_RE.findall(text or ""))


def load(session: str) -> set[str]:
    try:
        return set(json.loads((STATE_DIR / f"{session}.json").read_text()))
    except Exception:
        return set()


def save(session: str, seen: set[str]) -> None:
    try:
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        (STATE_DIR / f"{session}.json").write_text(json.dumps(sorted(seen)))
    except Exception:
        pass  # advisory state; losing it costs one duplicate line


# Markdown link syntax hides the path from the describing pattern: an index row
# reads `[`docs/x.md`](../docs/x.md) | what it is`. Collapse the link to its
# label first, so both the plain and the linked table form are seen. Found by
# testing the hook against this repo's own records.md, where it went silent on
# 25 described paths — a silent miss, which for an advisory is the worst
# outcome available.
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")


def described(text: str) -> dict[str, str]:
    """Paths this content is making a claim ABOUT -> the claim it is making.

    Returns the gloss, not just the path, because the gloss is what makes the
    warning actionable: the session has to decide whether *this particular
    assertion* is worth a fetch, and it cannot weigh that from a bare filename.
    Owner-directed 2026-08-08 — the hook stays advisory "as long as it tells a
    session about what it's about to do, so that session can decide whether or
    not the files are worth opening."
    """
    out: dict[str, str] = {}
    for line in (text or "").splitlines():
        line = MD_LINK_RE.sub(r"\1", line)
        for path, gloss in DESCRIBED_RE.findall(line):
            # a gloss that is itself mostly paths/urls is a pointer list, not prose
            if gloss.count("/") > 3 or gloss.startswith(("http", "(")):
                continue
            if PATH_RE.fullmatch(path) or "." in path:
                out.setdefault(path, " ".join(gloss.split())[:110].rstrip(" |"))
    return out


def main() -> int:
    try:
        event = json.loads(sys.stdin.read() or "{}")
    except Exception:
        return 0

    tool = event.get("tool_name", "")
    inp = event.get("tool_input") or {}
    session = str(event.get("session_id") or "nosession")

    if tool in RECORD_TOOLS:
        blob = " ".join(str(inp.get(k, "")) for k in RECORD_FIELDS)
        found = tokens(blob)
        # A read also legitimises the basenames it names, so `docs/x.md` fetched
        # by full path answers a later mention of `x.md`.
        found |= {Path(p).name for p in found}
        if found:
            save(session, load(session) | found)
        return 0

    if tool not in CHECK_TOOLS:
        return 0

    content = str(inp.get("content", "")) + "\n" + str(inp.get("new_string", ""))
    target = str(inp.get("file_path", ""))
    seen = load(session)

    claims = described(content)
    # The file being written is not a claim about itself; nor is anything already
    # read, by full path or basename.
    unread = sorted(
        p for p in claims
        if p not in seen
        and Path(p).name not in seen
        and Path(p).name != Path(target).name
    )
    if not unread:
        return 0

    # Report each path once per session — then treat it as reported, so a doc
    # revised five times does not repeat itself five times.
    fresh = [p for p in unread if f"!reported:{p}" not in seen]
    if not fresh:
        return 0
    save(session, seen | {f"!reported:{p}" for p in fresh})

    shown = fresh[:MAX_REPORTED]
    more = len(fresh) - len(shown)
    lines = [
        "You are describing files this session has not opened. MEASURED on this "
        "repo's own transcript (2026-08-08): of eight such one-line descriptions, "
        "the 3 written after reading the file were all correct and the 5 written "
        "without reading were wrong 3 times — including one that told a later "
        "session there was one binding contract where there are two.",
        "",
        "An unread description reads exactly like a read one, so nothing "
        "downstream can catch it. Either open these, or say plainly that the "
        "line is inferred from the filename:",
        "",
    ]
    for p in shown:
        lines.append(f"  · {p}")
        if claims.get(p):
            lines.append(f'      you are about to say: "{claims[p]}"')
    if more:
        lines.append(f"  · … and {more} more")
    lines += [
        "",
        "Weigh each claim on its own — some are worth a fetch and some plainly "
        "are not. Not a blocker, and not a claim that you are wrong: only that "
        "nothing here establishes that you are right.",
    ]

    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": "\n".join(lines),
            },
            "suppressOutput": True,
        },
        sys.stdout,
    )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # fail open, always
