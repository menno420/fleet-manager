#!/usr/bin/env python3
"""check_no_false_walls.py — ban present-tense standing capability-denial claims.

================================ PROVENANCE ================================
Why added : The owner's #309 doctrine ("evidence-backed verified capabilities
            ledger") bans **present-tense standing agent-capability-denial
            claims** from the repo's living/binding docs — a statement that
            an agent *cannot* merge / flip a PR / delete a branch, framed as
            a permanent limit. A one-off platform refusal is transient and
            platform-mutable; it belongs in a DATED / QUOTED incident row
            (which self-resolves and is re-verified by S9
            `check_capabilities_wall_age.py`), NEVER written as a standing
            rule in the prose. #309 named this guard as a required check, but
            the script was never created — this fills that gap. The canonical
            false wall it catches: CONSTITUTION's "Ref/branch deletion stays a
            genuine wall (403)" — refuted by #309 (branch deletion is a normal
            capability, 204 via the direct-token path; only the proxied path
            403s). This checker guards the PROSE; S9 ages the dated ledger —
            the two split the labor.
Date      : 2026-07-18 (lane worker, model: Opus 4.8, dispatched by the
            fleet-manager coordinator; fleet-manager PR #316)
Reliability: unverified — confirm its output against ground truth a few times
            across sessions before trusting it. Detection is best-effort text
            heuristics over hand-written prose (seed term + core-capability
            context + present-tense standing shape, minus dated/quoted/negated/
            meta exemptions), not a parser; it fails SAFE — advisory only, never
            wired into a blocking gate, so a miss or a false flag never blocks a
            merge. PROMOTE to a required check once it stays clean across a few
            sessions. DELETE this if it proves unreliable over multiple sessions.
=============================================================================

WHAT IT CHECKS (living/binding docs only — a NARROW allowlist)
  A line is a FALSE-WALL finding when ALL hold:
    1. it carries a WALL signal (word-boundary): `wall`/`walls`/`walled`,
       `blocked`, `owner-only`, `classifier-denied`/`classifier-walled`,
       `agents? cannot/can't`, `must not merge/flip`, `not allowed to`, or a
       present-tense `is|are|stays|remains|verified … 40[39]` framing; AND
    2. it names a CORE agent capability #309 declares NORMAL — merge/merging,
       draft->ready flip, branch/ref deletion, auto-merge arm. (This context
       gate is what keeps GENUINE constraints — `tag-push is 403-walled`,
       `api.github.com` 403, secrets/rulesets owner-only, protected-main 409 —
       from tripping the guard.) AND
    3. it is NOT exempt (below).

  EXEMPTIONS (any one → the line is clean):
    - DATED: the surrounding block carries a `YYYY-MM-DD` or `LAST-VERIFIED`
      date — a dated incident is the LEGITIMATE home for a wall observation.
    - QUOTED: the wall signal sits inside `"..."`, or the line says
      `verbatim` / `Reason:` (a verbatim platform-refusal quote).
    - NEGATED / anti-wall: a negation (`not`/`never`/`no`/`n't`/`isn't`/
      `without`/`≠`/`NOT`) precedes the wall signal, or the line says
      `not a wall` / `never a … wall` / `no longer` / `is not`.
    - META / discovery-discipline: the line is ABOUT declaring/recording walls,
      not asserting one — `declare`, `discover`, `cite`, `mint`, `invent`,
      `imagine`, `document(s)`, `record`, `re-verify`, `false wall`, `doc-wall`,
      `check_no_false_walls`, `flagger`, `write down a limitation`.
    - NON-CAPABILITY noun: `blocked branch`, `firewall`, `paywall`,
      `stonewall`, `hub`.

SCAN SET (living/binding surfaces only — see --list)
  CONSTITUTION.md · docs/current-state.md · docs/owner-queue.md ·
  .claude/CLAUDE.md · and the ACTIVE region of docs/CAPABILITIES.md (top of
  file down to the `## Append log` heading — the dated append-log / mirrored-
  lane / folded-manifest region below it is the dated-incident home, not
  scanned).
  EXCLUDED by design: .sessions/**, docs/CAPABILITIES-verified-*.md snapshots,
  bootstrap.py, .substrate/**, fixtures, and — explicitly, meta-risk —
  THIS guard's own file (its inline fixtures carry every seed term).

SEVERITY CONTRACT (sibling-parity: check_owner_queue / check_docs_links /
check_capabilities_wall_age / check_fleet_triage_staleness)
  Default DIRECT run prints findings + a summary and exits 0 (ADVISORY — #309
  named this a required check, but it ships advisory-first, standalone, NOT
  wired into `bootstrap.py check`, so it can never jam the substrate-gate).
  `--strict` exits 1 on any finding (opt-in, for promotion to required later).

USAGE
  python3 tools/check_no_false_walls.py                 # advisory, exit 0
  python3 tools/check_no_false_walls.py --strict        # exit 1 on findings
  python3 tools/check_no_false_walls.py --list          # print the scan set
  python3 tools/check_no_false_walls.py --root PATH      # scan a fixture tree
  python3 tools/check_no_false_walls.py --selftest      # offline fixtures

No third-party deps: stdlib only.
"""

from __future__ import annotations

import argparse
import os
import re
import sys

# ---- WALL signals (a present-tense capability-denial marker) ---------------
WALL_SIGNAL_RES = (
    re.compile(r"\bwall(?:s|ed)?\b", re.IGNORECASE),
    re.compile(r"\bclassifier[-\s]?(?:denied|walled|blocked)\b", re.IGNORECASE),
    re.compile(r"\bowner-only\b", re.IGNORECASE),
    re.compile(r"\bblocked\b", re.IGNORECASE),
    re.compile(r"\bagents?\b[^.\n]{0,20}\b(?:cannot|can'?t|may not|"
               r"must not|are not allowed to|not allowed to)\b", re.IGNORECASE),
    re.compile(r"\bmust not\b[^.\n]{0,20}\b(?:merge|flip|delete)\b",
               re.IGNORECASE),
    # A present-tense "is/are/stays/remains/verified … 403|409" framing — the
    # bare HTTP code becomes a wall signal ONLY in a standing-claim shape.
    re.compile(r"\b(?:is|are|was|were|stays?|remains?|verified)\b"
               r"[^.\n]{0,24}\b40[39]\b", re.IGNORECASE),
)

# ---- CORE agent capabilities #309 declares NORMAL (the context gate) -------
# A wall signal only counts when the line ALSO names one of these — so a
# genuine constraint (tag-push, api.github.com, secrets, protected-main) is
# never flagged.
CORE_CAP_RES = (
    re.compile(r"\bmerg(?:e|es|ing)\b", re.IGNORECASE),
    re.compile(r"\bauto-merge\b", re.IGNORECASE),
    re.compile(r"\b(?:draft[\s-]*(?:to|->|→)[\s-]*ready|ready[\s-]*flip|"
               r"flip(?:ping|s)?)\b", re.IGNORECASE),
    re.compile(r"\bbranch[-\s]?delet\w*\b", re.IGNORECASE),
    re.compile(r"\bdelet\w*\b[^.\n]{0,20}\b(?:branch|ref|head)\b",
               re.IGNORECASE),
    re.compile(r"\b(?:branch|ref|head)\b[^.\n]{0,20}\bdelet\w*\b",
               re.IGNORECASE),
)

# ---- Exemptions ------------------------------------------------------------
# No trailing \b: a date is frequently followed by a `T`ime ("2026-07-17T09:..")
# where \b would fail (digit->letter is not a boundary).
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
LAST_VERIFIED_RE = re.compile(r"LAST-VERIFIED", re.IGNORECASE)
QUOTE_MARK_RE = re.compile(r'["“”]')

# Line is ABOUT declaring / recording / refuting walls, not asserting one.
META_RE = re.compile(
    r"\b(?:declar\w*|discover\w*|cite|cited|cites|mint\w*|invent\w*|"
    r"imagin\w*|document\w*|record\w*|re-?verif\w*|flagg\w*|"
    r"false[-\s]walls?|doc-wall|check_no_false_walls|"
    r"write down a limitation|assumption[-\s]based)\b",
    re.IGNORECASE)

# Non-capability nouns that merely share the substring.
NONCAP_RE = re.compile(
    r"\bblocked branch\b|\bfirewall\b|\bpaywall\b|\bstonewall\b|\bhub\b",
    re.IGNORECASE)

# Negation / anti-wall tokens (checked in the ~48 chars BEFORE a wall signal,
# plus a few whole-line anti-wall idioms). The contraction alternative REQUIRES
# the apostrophe (`n't`) — a bare `nt` would falsely match "age-nt", "curre-nt".
NEG_TOKEN_RE = re.compile(
    r"\bnot\b|\bnever\b|\bno\b|n't\b|\bwithout\b|\banti\b|≠", re.IGNORECASE)
ANTIWALL_LINE_RE = re.compile(
    r"not a wall|never a[^.\n]{0,40}wall|no longer[^.\n]{0,30}wall|"
    r"≠[^.\n]{0,20}wall|isn'?t a[^.\n]{0,20}wall|is not a[^.\n]{0,20}wall",
    re.IGNORECASE)

CAPABILITIES_STOP_HEADING_RE = re.compile(r"^\s*##\s+Append log", re.IGNORECASE)
FENCE_RE = re.compile(r"^\s*(```|~~~)")
BULLET_RE = re.compile(r"^\s*[-*]\s+\S")
HEADING_RE = re.compile(r"^\s*#{1,6}\s+")

# The guard's own file basename — excluded explicitly (its fixtures carry
# every seed term).
SELF_BASENAME = os.path.basename(__file__)


def repo_root() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# --------------------------------------------------------------- scan set ---

def scan_set(root: str) -> list[str]:
    """Absolute paths of the living/binding docs to scan (existing only)."""
    rels = [
        "CONSTITUTION.md",
        os.path.join("docs", "current-state.md"),
        os.path.join("docs", "owner-queue.md"),
        os.path.join(".claude", "CLAUDE.md"),
        os.path.join("docs", "CAPABILITIES.md"),
    ]
    out = []
    for rel in rels:
        p = os.path.join(root, rel)
        if os.path.isfile(p) and os.path.basename(p) != SELF_BASENAME:
            out.append(p)
    return out


# ------------------------------------------------------------ block dates ---

def dated_line_set(lines: list[str]) -> set[int]:
    """Line numbers (1-based) that belong to a DATED block.

    A block = a bullet and its continuation lines (until the next bullet,
    heading, blank line, or fence). If ANY line in the block carries a
    YYYY-MM-DD or LAST-VERIFIED date, every line of the block is dated
    (a dated incident is the legitimate home for a wall observation).
    Non-bullet prose paragraphs are treated the same way, block by block.
    """
    dated: set[int] = set()
    in_fence = False
    n = len(lines)
    i = 0
    while i < n:
        line = lines[i]
        if FENCE_RE.match(line):
            in_fence = not in_fence
            i += 1
            continue
        if in_fence or not line.strip() or HEADING_RE.match(line):
            i += 1
            continue
        # Start a block at any non-blank, non-heading line; extend over
        # continuation lines that are not a new bullet/heading/blank/fence.
        start = i
        j = i + 1
        while j < n:
            nxt = lines[j]
            if (not nxt.strip() or BULLET_RE.match(nxt)
                    or HEADING_RE.match(nxt) or FENCE_RE.match(nxt)):
                break
            j += 1
        block_text = "\n".join(lines[start:j])
        if DATE_RE.search(block_text) or LAST_VERIFIED_RE.search(block_text):
            dated.update(range(start + 1, j + 1))
        i = j
    return dated


# ------------------------------------------------------------- detection ---

def _wall_signal_span(line: str):
    """Return (start, end) of the first wall signal on the line, or None."""
    best = None
    for rx in WALL_SIGNAL_RES:
        m = rx.search(line)
        if m and (best is None or m.start() < best[0]):
            best = (m.start(), m.end())
    return best


def _is_quoted(line: str, span) -> bool:
    """True if the wall signal appears inside a "..." quote."""
    before = QUOTE_MARK_RE.findall(line[:span[0]])
    after = QUOTE_MARK_RE.findall(line[span[1]:])
    return len(before) % 2 == 1 and len(after) >= 1


def line_is_false_wall(line: str, prev: str = "") -> bool:
    """Line-level test (dated-block exemption is applied by the caller).

    ``prev`` is the preceding physical line. Markdown hard-wraps sentences, so
    a governing qualifier (``documents``, ``check_no_false_walls``, a negation,
    an opening quote) frequently sits on the previous line while the wall
    signal lands on this one. META / anti-wall / quote exemptions are evaluated
    over the ``prev + line`` window; the NEGATION lead stays bounded to the ~48
    chars immediately before the signal (measured across the window) so an
    earlier-in-the-bullet ``never`` cannot over-exempt a genuine standing wall.
    """
    span = _wall_signal_span(line)
    if span is None:
        return False
    # Context gate: must name a core capability #309 declares normal.
    if not any(rx.search(line) for rx in CORE_CAP_RES):
        return False
    window = (prev + " " + line) if prev else line
    win_low = window.lower()
    # --- exemptions ---
    if NONCAP_RE.search(window):
        return False
    if META_RE.search(window):
        return False
    if ANTIWALL_LINE_RE.search(window):
        return False
    if "verbatim" in win_low or "reason:" in win_low:
        return False
    if _is_quoted(window, (len(prev) + 1 + span[0], len(prev) + 1 + span[1])
                  if prev else span):
        return False
    # Negation in the ~48 chars before the wall signal (across the window).
    sig_start = (len(prev) + 1 + span[0]) if prev else span[0]
    lead = window[max(0, sig_start - 48):sig_start]
    if NEG_TOKEN_RE.search(lead):
        return False
    return True


def check_text(rel: str, text: str, out: list[str]) -> int:
    """Scan one file's text. Returns the finding count."""
    lines = text.splitlines()
    # CAPABILITIES.md: only the ACTIVE region above `## Append log`.
    if os.path.basename(rel) == "CAPABILITIES.md":
        cut = len(lines)
        for idx, ln in enumerate(lines):
            if CAPABILITIES_STOP_HEADING_RE.match(ln):
                cut = idx
                break
        lines = lines[:cut]
    dated = dated_line_set(lines)
    in_fence = False
    flags = 0
    prev = ""
    for lineno, line in enumerate(lines, 1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            prev = ""
            continue
        if in_fence:
            prev = ""
            continue
        if lineno in dated:
            prev = line
            continue
        if line_is_false_wall(line, prev):
            flags += 1
            out.append(f"FLAG [false-wall] {rel}:{lineno}: {line.strip()}")
        prev = line
    return flags


def check_files(files: list[str], root: str, out: list[str]) -> int:
    flags = 0
    for path in files:
        rel = os.path.relpath(path, root)
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        except (OSError, UnicodeDecodeError) as exc:
            out.append(f"FLAG [encoding] {rel}: unreadable as UTF-8: {exc}")
            flags += 1
            continue
        flags += check_text(rel, text, out)
    return flags


# -------------------------------------------------------------- selftest ---

# A present-tense STANDING wall line (flagged) — the #309 target class.
_STANDING = ("- Ref/branch **deletion** stays a genuine wall (403), but that "
             "is the exception, not merging.")
# A DATED / QUOTED historical incident line (NOT flagged) — the legit home.
_DATED = ("- 2026-07-12 · wall · autonomous-project · branch-delete refused: "
          '"Access to this GitHub path is not permitted" (403).')
# A NON-CAPABILITY "blocked branch" line (NOT flagged).
_BLOCKED_BRANCH = ("- A blocked branch -> update it (merge, never force) and "
                   "re-evaluate.")
# An ANTI-WALL / negated line (NOT flagged).
_ANTIWALL = ("- A landing refusal is venue-specific — never a standing "
             '"agents can\'t merge" wall, and merging is normal agent work.')
# A GENUINE constraint not in the core set (NOT flagged): tag-push 403.
_GENUINE = "- Agent tag-push is 403-walled; use the workflow_dispatch path."
# A META line about the guard itself (NOT flagged).
_META = ("- CI enforces this: a PR that documents an agent-capability wall "
         "goes red and cannot merge.")


def selftest() -> int:
    fails: list[str] = []

    def flagged(line: str) -> bool:
        out: list[str] = []
        # Wrap in a heading so no stray date/continuation attaches.
        check_text("fixture.md", "# fixture\n\n" + line + "\n", out)
        return bool(out)

    if not flagged(_STANDING):
        fails.append("a present-tense standing wall line must be flagged")
    if flagged(_DATED):
        fails.append("a dated/quoted historical wall line must NOT be flagged")
    if flagged(_BLOCKED_BRANCH):
        fails.append("a non-capability 'blocked branch' line must NOT be "
                     "flagged")
    if flagged(_ANTIWALL):
        fails.append("a negated / anti-wall line must NOT be flagged")
    if flagged(_GENUINE):
        fails.append("a genuine non-core constraint (tag-push 403) must NOT "
                     "be flagged")
    if flagged(_META):
        fails.append("a meta line describing the guard must NOT be flagged")

    # Dated-BLOCK exemption: a standing-shaped wall line inside a bullet whose
    # body carries a LAST-VERIFIED date is exempt (the ledger's legit home).
    dated_block = ("# fixture\n\n- **Branch deletion**: stays a genuine wall "
                   "(403) on merge paths.\n  — LAST-VERIFIED: 2026-07-10\n")
    out2: list[str] = []
    if check_text("fixture.md", dated_block, out2) != 0:
        fails.append("a LAST-VERIFIED dated BLOCK must exempt its wall line")

    for msg in fails:
        print(f"SELFTEST FAIL: {msg}", file=sys.stderr)
    print(f"selftest: {'FAIL' if fails else 'PASS'} ({len(fails)} failure(s))")
    if not fails:
        demo: list[str] = []
        check_text("fixture.md", "# fixture\n\n" + _STANDING + "\n", demo)
        print("--- fixture flag (expected) ---")
        print("\n".join(demo))
    return 1 if fails else 0


# ------------------------------------------------------------------ main ---

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=repo_root(),
                    help="repo/fixture root to scan (default: this repo)")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on any finding (default: advisory, exit 0)")
    ap.add_argument("--list", action="store_true",
                    help="print the scan set and exit")
    ap.add_argument("--selftest", action="store_true",
                    help="offline fixture assertions and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    root = os.path.abspath(args.root)
    files = scan_set(root)
    if args.list:
        for f in files:
            print(os.path.relpath(f, root))
        print(f"\ncheck_no_false_walls: {len(files)} file(s) in the scan set")
        return 0

    out: list[str] = []
    flags = check_files(files, root, out)
    for line in out:
        print(f"::warning::{line}" if not args.strict else line)
    if flags == 0:
        verdict = (f"CLEAN — no present-tense standing capability-denial claim "
                   f"in {len(files)} living/binding doc(s)")
    else:
        verdict = (f"{flags} FALSE-WALL LINE(S) across {len(files)} doc(s) — "
                   "reword to #309's verified reality, or move the observation "
                   "to a dated/quoted incident row")
    print(f"check_no_false_walls: {verdict}")
    # Advisory by default (exit 0); --strict reds on findings.
    return 0 if (flags == 0 or not args.strict) else 1


if __name__ == "__main__":
    sys.exit(main())
