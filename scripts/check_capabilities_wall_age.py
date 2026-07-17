#!/usr/bin/env python3
"""check_capabilities_wall_age.py — flag stale WALL findings that need a re-probe.

================================ PROVENANCE ================================
Why added : NEXT-TASKS.md item S9 (first-build set for the recreated
            fleet-manager). docs/CAPABILITIES.md records "verified walls"
            (blocked operations), but a platform wall can self-resolve
            AGENT-INVISIBLY — the canonical live case is 2026-07-17's own
            "Self-scheduling the seat wake chain — WALL", recorded at ~02Z
            and REFUTED hours later (native scheduling via deferred
            ToolSearch tools WORKS; the classifier was nondeterministic,
            not a wall). THE DISCOVERY RULE step 5 already says "an entry
            older than the staleness window that your work depends on is a
            CLAIM, not a fact — re-verify with one cheap attempt", but
            nothing enforces it, so a stale wall silently hardens into
            assumed-permanent. This checker parses the wall findings, ages
            each by its verified date, and flags any older than
            --max-age-days (default 30) as re-probe-due — turning the prose
            discipline into a mechanical prompt.
Date      : 2026-07-17 (lane worker, model: Opus 4.8, dispatched by the
            recreated fleet-manager coordinator; fleet-manager PR #296)
Reliability: unverified — confirm its output against ground truth a few
            times across sessions before trusting it. The date-extraction
            and supersession heuristics are best-effort text parsing over a
            hand-written living ledger, not a strict schema; a superseded
            wall is excluded on a shared-keyword match, so a genuinely
            distinct wall that happens to share a title word with an UPDATE
            bullet could be under-flagged (fails SAFE — a missed re-probe
            prompt, never a false merge block; this checker is advisory and
            never wired into a blocking gate).
Kill-switch: delete this if it proves unreliable over multiple sessions.
=============================================================================

WHAT IT CHECKS (docs/CAPABILITIES.md, or --capabilities PATH)
  Every WALL finding in the ledger is aged by its most recent verified date
  and flagged when older than --max-age-days.

  WALL DETECTION (by the markers the file actually uses):
    - Dated append-log / mirrored-aggregate bullets whose 2nd `·`-delimited
      field is `wall` (e.g. `- 2026-07-14 · wall · any · **…**`). A field
      `capability` marks a working capability and is SKIPPED; a field
      starting `UPDATE` marks a supersession notice (used for exclusion,
      below) and is not itself aged.
    - Seed / prose bullets with NO dated kind-token are classified by their
      section heading: a bullet under a heading matching /wall/i (## Walls,
      ## WALLED) is a wall; under a capabilities heading (## Capabilities,
      ## CAN …) it is skipped.

  VERIFIED DATE (freshest wins), extracted per wall block in priority order:
    1. `LAST-VERIFIED: YYYY-MM-DD`  (seed-row format)
    2. a leading `- YYYY-MM-DD ·`   (append-log / mirror format)
    3. `(re-)verified|appended|added|recorded|updated … YYYY-MM-DD`
    4. any YYYY-MM-DD in the block (max)
    A wall block with NO parseable date is reported as an `[undated-wall]`
    note (it has no freshness data — itself a re-probe candidate) but does
    NOT affect the exit code.

  SUPERSESSION / RESOLUTION EXCLUSION (a self-resolved wall must not nag):
    A wall is EXCLUDED from flagging when EITHER
      (a) its own block carries a resolution marker — `supersed…`,
          `RESOLVED`, `no longer a (blanket) wall`, `RETIRES the recorded`,
          or a `retired … wall` phrase; OR
      (b) a SEPARATE `UPDATE (supersedes …)` / `supersed…` bullet dated on
          or after the wall shares a distinctive title keyword with it
          (the 2026-07-17 self-scheduling case: the WALL bullet and the
          `UPDATE (supersedes … self-scheduling WALL …)` bullet share
          "scheduling").
    Excluded walls are listed as `[superseded]` notes, never flagged.

SEVERITY CONTRACT (sibling-parity: check_owner_queue / check_roster_freshness
/ check_docs_links)
  Default DIRECT run exits 1 when any wall is re-probe-due, 0 when clean.
  `--advisory` prints FLAG lines as `::warning::` and always exits 0 (S9 is
  specced ADVISORY / never merge-blocking, satisfied structurally too: this
  checker is standalone and NOT wired into `bootstrap.py check`).

USAGE
  python3 scripts/check_capabilities_wall_age.py                  # default 30d
  python3 scripts/check_capabilities_wall_age.py --max-age-days 14
  python3 scripts/check_capabilities_wall_age.py --today 2026-08-20
  python3 scripts/check_capabilities_wall_age.py --advisory       # exit 0
  python3 scripts/check_capabilities_wall_age.py --capabilities PATH
  python3 scripts/check_capabilities_wall_age.py --selftest       # offline

No third-party deps: stdlib only.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import date, datetime

# The ledger separates fields with a MIDDLE DOT (U+00B7); tolerate padding.
MIDDOT = "·"
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
LEADING_DATE_RE = re.compile(r"^-\s+(\d{4}-\d{2}-\d{2})\s*" + MIDDOT)
LAST_VERIFIED_RE = re.compile(r"LAST-VERIFIED[:\s]+(\d{4}-\d{2}-\d{2})",
                              re.IGNORECASE)
VERIFIED_NEAR_RE = re.compile(
    r"\b(?:re-?verified|verified|appended|added|recorded|updated)\b"
    r"[^\n]{0,40}?(\d{4}-\d{2}-\d{2})", re.IGNORECASE)
BOLD_TITLE_RE = re.compile(r"\*\*(.+?)\*\*")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
BULLET_RE = re.compile(r"^-\s+\S")

# Resolution markers that mean a wall block has already self-resolved.
RESOLVED_MARKERS = (
    re.compile(r"(?<!un-)supersed", re.IGNORECASE),
    re.compile(r"\bRESOLVED\b"),
    re.compile(r"no longer a (?:blanket )?wall", re.IGNORECASE),
    re.compile(r"RETIRES the recorded", re.IGNORECASE),
    re.compile(r"\bretir(?:ed|ing)\b[^\n]{0,40}\bwall\b", re.IGNORECASE),
)

# Words too generic to prove two bullets are about the SAME wall.
STOPWORDS = {
    "earlier", "finding", "findings", "update", "supersedes", "supersede",
    "superseded", "sameday", "autonomous", "project", "projects", "verified",
    "venue", "walls", "walled", "cannot", "blocked", "denied", "agent",
    "agents", "agentside", "session", "sessions", "fleet", "manager",
    "coordinator", "worker", "workers", "native", "around", "before",
    "never", "always", "seat", "seats", "chain", "these", "their", "there",
    "which", "while", "about", "still", "other", "every", "known", "record",
}


def repo_root() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ------------------------------------------------------------ block parse ---

def iter_blocks(text: str):
    """Yield (start_lineno, first_line, [lines], heading) for each bullet.

    A bullet block starts at a ``- `` line and runs until the next bullet,
    heading, blank line, code fence, or horizontal rule. Fenced code regions
    are skipped so shell samples are never parsed as bullets. ``heading`` is
    the nearest preceding ``#`` heading text (for section classification).
    """
    lines = text.splitlines()
    in_fence = False
    heading = ""
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if FENCE_RE.match(line):
            in_fence = not in_fence
            i += 1
            continue
        if in_fence:
            i += 1
            continue
        hm = HEADING_RE.match(line)
        if hm:
            heading = hm.group(2).strip()
            i += 1
            continue
        if BULLET_RE.match(line):
            start = i
            block = [line]
            j = i + 1
            while j < n:
                nxt = lines[j]
                if (not nxt.strip() or BULLET_RE.match(nxt)
                        or HEADING_RE.match(nxt) or FENCE_RE.match(nxt)
                        or nxt.lstrip().startswith(("<!--", "-->", "---"))):
                    break
                block.append(nxt)
                j += 1
            yield start + 1, line, block, heading
            i = j
            continue
        i += 1


def _kind_token(first_line: str) -> str | None:
    """`wall` / `capability` / `update` from the 2nd `·`-delimited field."""
    parts = [p.strip() for p in first_line.split(MIDDOT)]
    for p in parts[1:]:
        low = p.lower()
        if low == "wall":
            return "wall"
        if low == "capability":
            return "capability"
        if low.startswith("update"):
            return "update"
    return None


def _is_capabilities_heading(h: str) -> bool:
    low = h.lower()
    if "wall" in low:            # "## WALLED" is a walls heading, not CAN
        return False
    # "## Capabilities …" and the several "## CAN — …" headings.
    return "capabilit" in low or re.match(r"can\b", low) is not None


def _is_walls_heading(h: str) -> bool:
    return "wall" in h.lower()


def classify(first_line: str, heading: str) -> str:
    """One of: 'wall', 'capability', 'update', 'skip'."""
    tok = _kind_token(first_line)
    if tok == "capability":
        return "capability"
    if tok == "wall":
        return "wall"
    if tok == "update":
        return "update"
    # No dated kind-token: fall back to the section heading.
    if _is_capabilities_heading(heading):
        return "capability"
    if _is_walls_heading(heading):
        return "wall"
    return "skip"


def extract_date(block_text: str, first_line: str) -> date | None:
    """Freshest verified date in a block, by the documented priority."""
    def newest(matches):
        best: date | None = None
        for raw in matches:
            try:
                d = datetime.strptime(raw, "%Y-%m-%d").date()
            except ValueError:
                continue
            if best is None or d > best:
                best = d
        return best

    lv = newest(LAST_VERIFIED_RE.findall(block_text))
    if lv:
        return lv
    lead = LEADING_DATE_RE.match(first_line)
    if lead:
        try:
            return datetime.strptime(lead.group(1), "%Y-%m-%d").date()
        except ValueError:
            pass
    near = newest(VERIFIED_NEAR_RE.findall(block_text))
    if near:
        return near
    return newest(DATE_RE.findall(block_text))


def title_tokens(first_line: str) -> set[str]:
    """Distinctive lowercase tokens from a bullet's title (for supersession)."""
    m = BOLD_TITLE_RE.search(first_line)
    src = m.group(1) if m else first_line
    toks = set()
    for w in re.split(r"[^a-z0-9]+", src.lower()):
        if len(w) >= 5 and w not in STOPWORDS and not w.isdigit():
            toks.add(w)
    return toks


# --------------------------------------------------------------- checks -----

def analyse(text: str, today: date, max_age_days: int):
    """Return (flags, notes) line lists for the ledger.

    flags = re-probe-due walls (exit-code-affecting); notes = superseded /
    undated walls (informational, never affect the exit code).
    """
    walls: list[dict] = []
    supersede_notices: list[dict] = []
    for lineno, first, block, heading in iter_blocks(text):
        kind = classify(first, heading)
        block_text = "\n".join(block)
        d = extract_date(block_text, first)
        if kind == "update":
            supersede_notices.append(
                {"date": d, "tokens": title_tokens(first)})
            continue
        if kind != "wall":
            continue
        # A wall bullet may itself contain "supersedes" -> also a notice.
        if any(rx.search(block_text) for rx in RESOLVED_MARKERS[:1]):
            supersede_notices.append(
                {"date": d, "tokens": title_tokens(first)})
        walls.append({"lineno": lineno, "first": first, "text": block_text,
                      "date": d, "tokens": title_tokens(first)})

    flags: list[str] = []
    notes: list[str] = []
    for w in walls:
        label = _short(w["first"])
        # (a) in-block resolution marker.
        if any(rx.search(w["text"]) for rx in RESOLVED_MARKERS):
            notes.append(f"note  [superseded] L{w['lineno']}: {label} — the "
                         "block carries a resolution/supersession marker; "
                         "already handled, not aged")
            continue
        # (b) a later supersession notice sharing a distinctive keyword.
        sup = _superseded_by(w, supersede_notices)
        if sup is not None:
            shared = ", ".join(sorted(sup))
            notes.append(f"note  [superseded] L{w['lineno']}: {label} — a "
                         f"later UPDATE/supersedes bullet shares {shared!r}; "
                         "the wall is resolved, not aged")
            continue
        if w["date"] is None:
            notes.append(f"note  [undated-wall] L{w['lineno']}: {label} — no "
                         "parseable verified date; add one (a wall with no "
                         "freshness data cannot be aged and is itself a "
                         "re-probe candidate)")
            continue
        age = (today - w["date"]).days
        if age > max_age_days:
            flags.append(f"FLAG [reprobe-due] L{w['lineno']}: {label} — wall "
                         f"verified {w['date'].isoformat()} is {age}d old "
                         f"(> {max_age_days}d); re-probe once and APPEND the "
                         "result (THE DISCOVERY RULE step 5)")
    return flags, notes


def _short(first_line: str) -> str:
    m = BOLD_TITLE_RE.search(first_line)
    if m:
        return m.group(1).strip()
    s = first_line.lstrip("- ").strip()
    return (s[:70] + "…") if len(s) > 71 else s


def _superseded_by(wall: dict, notices: list[dict]) -> set[str] | None:
    """Return the shared distinctive tokens if a notice supersedes the wall."""
    for note in notices:
        if note["tokens"] is wall["tokens"]:
            continue  # the wall's own self-registered notice
        # Date guard: an UPDATE must be on/after the wall to supersede it.
        if (wall["date"] is not None and note["date"] is not None
                and note["date"] < wall["date"]):
            continue
        shared = wall["tokens"] & note["tokens"]
        if shared:
            return shared
    return None


# ------------------------------------------------------------ selftest ------

_FIXTURE = """# fixture capabilities

## Capabilities — verified working

- `any` · **A working capability from long ago**: proven. — LAST-VERIFIED: 2020-01-01

## Walls — verified blocked

- `any` · **Ancient seed wall**: 403 everywhere. — LAST-VERIFIED: 2020-01-01
- `any` · **Fresh seed wall**: 403 today. — LAST-VERIFIED: 2026-07-16
- `any` · **A wall carrying no date anywhere in its body** — should surface
  as an undated note, never aged.

## Append log — newest first

- 2026-07-17 · UPDATE (supersedes the earlier widget-teleport WALL finding):
  native widget teleport WORKS via the deferred ToolSearch tool.
- 2020-02-02 · wall · autonomous-project · **Widget teleport blocked** —
  classifier denied the teleport twice.
- 2019-05-05 · wall · any · **Old prose-dated merge wall** recorded
  2019-05-05 — a genuinely stale, still-blocked wall nothing has lifted.
- 2019-09-09 · capability · any · **A capability that is old** — still works.
"""


def selftest() -> int:
    fails: list[str] = []
    today = date(2026, 7, 17)
    flags, notes = analyse(_FIXTURE, today, max_age_days=30)
    joined_flags = "\n".join(flags)
    joined_notes = "\n".join(notes)

    # 1. Ancient seed wall (2020) -> flagged re-probe-due.
    if "Ancient seed wall" not in joined_flags:
        fails.append("ancient seed wall (2020) should be re-probe-due")
    # 2. Fresh seed wall (2026-07-16, 1d) -> NOT flagged.
    if "Fresh seed wall" in joined_flags:
        fails.append("fresh seed wall (1d old) must not be flagged")
    # 3. Superseded wall -> excluded (note), not flagged.
    if "Widget teleport" in joined_flags:
        fails.append("superseded widget-teleport wall must not be flagged")
    if "Widget teleport" not in joined_notes or "superseded" not in joined_notes:
        fails.append("superseded widget-teleport wall should be a "
                     "[superseded] note")
    # 4. A capability (even old) is never a wall.
    if "capability that is old" in joined_flags:
        fails.append("an old capability must never be flagged as a wall")
    # 5. The genuinely stale, un-superseded 2019 wall IS flagged.
    if "prose-dated merge wall" not in joined_flags:
        fails.append("stale un-superseded 2019 wall should be re-probe-due")
    # 6. The no-date wall surfaces as an undated note, not a flag.
    if "no date at all" in joined_flags:
        fails.append("undated wall must not be aged/flagged")
    if "undated-wall" not in joined_notes:
        fails.append("undated wall should surface as an [undated-wall] note")

    for msg in fails:
        print(f"SELFTEST FAIL: {msg}", file=sys.stderr)
    print(f"selftest: {'FAIL' if fails else 'PASS'} ({len(fails)} failure(s))")
    if not fails:
        print("--- fixture flags ---")
        print(joined_flags or "(none)")
        print("--- fixture notes ---")
        print(joined_notes or "(none)")
    return 1 if fails else 0


# ---------------------------------------------------------------- main ------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--capabilities",
                    default=os.path.join(repo_root(), "docs",
                                         "CAPABILITIES.md"),
                    help="ledger file (default: docs/CAPABILITIES.md)")
    ap.add_argument("--max-age-days", type=int, default=30,
                    help="flag walls older than this many days (default 30)")
    ap.add_argument("--today", default=None,
                    help="override 'today' as YYYY-MM-DD (for testability)")
    ap.add_argument("--advisory", action="store_true",
                    help="report-only: print flags as ::warning::, exit 0")
    ap.add_argument("--selftest", action="store_true",
                    help="offline fixture assertions (no network) and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    if args.today:
        try:
            today = datetime.strptime(args.today, "%Y-%m-%d").date()
        except ValueError:
            print(f"check_capabilities_wall_age: bad --today {args.today!r} "
                  "(want YYYY-MM-DD)", file=sys.stderr)
            return 2
    else:
        today = date.today()

    try:
        with open(args.capabilities, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        print(f"check_capabilities_wall_age: cannot read "
              f"{args.capabilities}: {exc}", file=sys.stderr)
        return 2

    flags, notes = analyse(text, today, args.max_age_days)
    for line in notes:
        print(line)
    for line in flags:
        print(f"::warning::{line}" if args.advisory else line)

    if flags:
        verdict = (f"{len(flags)} WALL(S) RE-PROBE-DUE (> {args.max_age_days}d "
                   f"as of {today.isoformat()}) — re-verify each with one "
                   "cheap attempt and APPEND the result")
    else:
        verdict = (f"CLEAN — no wall finding is older than "
                   f"{args.max_age_days}d as of {today.isoformat()}")
    print(f"check_capabilities_wall_age: {verdict} "
          f"({len(notes)} note(s): superseded/undated)")
    return 0 if (not flags or args.advisory) else 1


if __name__ == "__main__":
    sys.exit(main())
