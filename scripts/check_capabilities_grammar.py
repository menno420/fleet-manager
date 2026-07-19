#!/usr/bin/env python3
"""check_capabilities_grammar.py — format linter for the CAPABILITIES append surfaces.

================================ PROVENANCE ================================
Why added : PR #337 session-card 💡 idea, planned as the last below-the-line
            slice of the PR #349 plan. docs/CAPABILITIES.md is the fleet's
            ONE walls/capabilities ledger and its append log declares a
            grammar (`- YYYY-MM-DD · capability|wall · <venue> · finding ·
            evidence · workaround`) — but nothing enforces it, and the S9
            ager's own header admits its parsing is "best-effort text
            parsing over a hand-written living ledger, not a strict schema".
            A hand-written entry that drifts outside the grammar silently
            falls outside the ager's wall/supersession detection: an
            undated wall can't be aged, a malformed UPDATE bullet never
            registers as a supersession notice, and an out-of-order append
            breaks the "newest first" reading contract. This linter checks
            the FORMAT surface so the content checkers can trust it.
NEIGHBORS (complement, never duplicate — the three split the labor):
            - tools/check_no_false_walls.py guards the PROSE: it bans
              present-tense standing capability-denial claims in the ACTIVE
              region of living docs (it deliberately stops scanning
              CAPABILITIES.md at `## Append log` — the dated region is the
              legitimate home for wall observations). It never checks entry
              format.
            - scripts/check_capabilities_wall_age.py (S9) guards CONTENT
              FRESHNESS: it ages dated WALL findings, excludes superseded
              ones, and notes undated walls. It ASSUMES the grammar holds.
            - THIS linter guards the FORMAT of the hand-written append
              surfaces (`## Append log` + `## Mirrored lane findings`) plus
              the lowercase-stub rule, so the two neighbors stand on firm
              ground. It never judges staleness or wall-vs-truth content.
Date      : 2026-07-19 (build-slice worker, model: fable-5, dispatched by
            the coordinator; fleet-manager PR #358)
Reliability: unverified — confirm its output against ground truth a few
            times across sessions before trusting it. The field-splitting
            and venue/kind heuristics mirror the ager's tolerant parsing of
            a hand-written ledger, not a strict schema; it fails SAFE —
            advisory by default (exit 0), standalone, NOT wired into
            `bootstrap.py check`, so a false flag never blocks a merge.
Kill-switch: delete this if it proves unreliable over multiple sessions.
=============================================================================

WHAT IT CHECKS (docs/CAPABILITIES.md, or --capabilities PATH)

  Linted regions — the HAND-WRITTEN append surfaces only:
    * `## Append log` (down to the first `---` / next `## ` heading)
    * `## Mirrored lane findings` (each `### <lane>` subsection separately)
  The kit-owned seed fence (`substrate-kit:capability-seed BEGIN..END`) and
  the folded legacy manifest are NOT grammar-linted (the seed refreshes at
  kit upgrade; the manifest predates the grammar and keeps original stamps)
  — except rule G5, which scans everything below the seed fence, because a
  malformed supersession note ANYWHERE breaks the ager's exclusion logic
  (the live case: the 2026-07-16 inbox-append wall's `SUPERSEDED 2026-07-18`
  note lives in the folded manifest).

  G1 dated        — every top-level bullet leads with `- YYYY-MM-DD ·`, the
                    date parseable and not in the future. A bullet with a
                    date only elsewhere in its body is `[g1-misdated]`; one
                    with no date at all is `[g1-undated]` (a bare claim).
  G2 kind         — the 2nd `·`-field classifies as capability | wall |
                    UPDATE, using the SAME token rule as the ager's
                    `_kind_token` (imported; verbatim fallback below).
  G3 venue        — the 3rd `·`-field is one of the declared venue tokens
                    (`owner-live` · `autonomous-project` · `routine-fired` ·
                    `subagent` · `any`). ABSENT venue is a note, not a flag —
                    the ledger's own format note grandfathers venue-less
                    lines as `any`. A token-shaped 3rd field that is NOT in
                    the set (a typo) is flagged.
  G4 newest-first — within each linted section, leading dates never
                    increase downward (the `## Append log — newest first`
                    contract, applied per `###` subsection in the mirror).
  G5 supersession — any block (below the seed fence) carrying a
                    resolution/supersession marker — the ager's own
                    RESOLVED_MARKERS, imported — must also carry a parseable
                    `YYYY-MM-DD` date (the ager's date-guard needs one), and
                    an UPDATE-kind bullet must match the ager's exclusion
                    regex `(?<!un-)supersed` (RESOLVED_MARKERS[0], cited
                    from scripts/check_capabilities_wall_age.py) or it never
                    registers as a supersession notice there.
  G6 stub         — `docs/capabilities.md` (lowercase) stays a POINTER STUB
                    (the I-44 resolution, 2026-07-12): it must reference
                    CAPABILITIES.md, must NOT grow its own `## Append log`
                    or dated capability|wall rows, and must stay small.

SEVERITY CONTRACT (sibling-parity: check_capabilities_wall_age /
check_docs_links / check_fleet_triage_staleness / check_lane_liveness)
  Default run prints findings + notes and ALWAYS exits 0 (WARN-level
  advisory; standalone, never wired into `bootstrap.py check`).
  `--strict` exits 1 on any FLAG (notes never affect the exit code).

USAGE
  python3 scripts/check_capabilities_grammar.py                  # advisory
  python3 scripts/check_capabilities_grammar.py --strict         # exit 1 on FLAGs
  python3 scripts/check_capabilities_grammar.py --today 2026-08-01
  python3 scripts/check_capabilities_grammar.py --capabilities PATH \
      --stub PATH
  python3 scripts/check_capabilities_grammar.py --selftest       # offline

No third-party deps: stdlib only (plus an optional same-directory import of
check_capabilities_wall_age for the shared shapes, with verbatim fallbacks).
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import date, datetime

# --- shared shapes: import from the S9 ager (same directory) when present ---
# The ager carries a kill-switch header and may legitimately be deleted; the
# fallbacks below are VERBATIM copies of its shapes (keep in sync with
# scripts/check_capabilities_wall_age.py — that file is the exclusion
# authority the G5 interop check exists for).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:  # pragma: no cover - exercised implicitly in-repo
    from check_capabilities_wall_age import (MIDDOT, RESOLVED_MARKERS,
                                             _kind_token)
    _SHAPES_SOURCE = "imported from check_capabilities_wall_age"
except ImportError:  # verbatim fallback copies
    _SHAPES_SOURCE = "fallback copies (ager not importable)"
    MIDDOT = "·"
    RESOLVED_MARKERS = (
        re.compile(r"(?<!un-)supersed", re.IGNORECASE),
        re.compile(r"\bRESOLVED\b"),
        re.compile(r"no longer a (?:blanket )?wall", re.IGNORECASE),
        re.compile(r"RETIRES the recorded", re.IGNORECASE),
        re.compile(r"\bretir(?:ed|ing)\b[^\n]{0,40}\bwall\b", re.IGNORECASE),
    )

    def _kind_token(first_line: str) -> str | None:
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

# RESOLVED_MARKERS[0] is the ager's supersession-EXCLUSION regex — an UPDATE
# bullet must match it to register as a notice there (G5).
SUPERSEDE_RE = RESOLVED_MARKERS[0]

VENUES = {"owner-live", "autonomous-project", "routine-fired", "subagent",
          "any"}

DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
LEADING_DATE_RE = re.compile(r"^-\s+(\d{4}-\d{2}-\d{2})\s*" + MIDDOT)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
BULLET_RE = re.compile(r"^-\s+\S")
HR_RE = re.compile(r"^---\s*$")
SEED_BEGIN_RE = re.compile(r"substrate-kit:capability-seed BEGIN")
SEED_END_RE = re.compile(r"substrate-kit:capability-seed END")
APPEND_LOG_RE = re.compile(r"^##\s+Append log", re.IGNORECASE)
MIRROR_RE = re.compile(r"^##\s+Mirrored lane findings", re.IGNORECASE)
# A token-shaped venue candidate (lowercase word/hyphens) after stripping
# formatting — used to tell a TYPO venue from an OMITTED venue.
TOKENISH_RE = re.compile(r"^[a-z][a-z-]{2,24}$")


def repo_root() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def parse_date(raw: str) -> date | None:
    try:
        return datetime.strptime(raw, "%Y-%m-%d").date()
    except ValueError:
        return None


# ------------------------------------------------------------ block parse ---

def iter_blocks(lines: list[str], start: int, end: int):
    """Yield (lineno_1based, first_line, block_text) for each top-level bullet
    in lines[start:end]. Same block rules as the ager's iter_blocks."""
    in_fence = False
    i = start
    while i < end:
        line = lines[i]
        if FENCE_RE.match(line):
            in_fence = not in_fence
            i += 1
            continue
        if in_fence:
            i += 1
            continue
        if BULLET_RE.match(line):
            block = [line]
            j = i + 1
            while j < end:
                nxt = lines[j]
                if (not nxt.strip() or BULLET_RE.match(nxt)
                        or HEADING_RE.match(nxt) or FENCE_RE.match(nxt)
                        or nxt.lstrip().startswith(("<!--", "-->", "---"))):
                    break
                block.append(nxt)
                j += 1
            yield i + 1, line, "\n".join(block)
            i = j
            continue
        i += 1


# ------------------------------------------------------------- regions ------

def find_regions(lines: list[str]):
    """Return (append_region, mirror_sections, below_seed_start).

    append_region      = (start, end) line-index bounds of `## Append log`
                         (exclusive of the heading, ending at the first
                         top-level `---` or `## ` heading), or None.
    mirror_sections    = [(label, start, end), ...] one per `###` subsection
                         of `## Mirrored lane findings`.
    below_seed_start   = first line index after the seed END fence (0 when
                         no fence exists) — the G5 scan floor.
    """
    n = len(lines)
    below_seed_start = 0
    for i, ln in enumerate(lines):
        if SEED_END_RE.search(ln):
            below_seed_start = i + 1
            break

    append_region = None
    mirror_bounds = None
    for i, ln in enumerate(lines):
        if APPEND_LOG_RE.match(ln) and append_region is None:
            j = i + 1
            while j < n and not (HR_RE.match(lines[j])
                                 or re.match(r"^##\s", lines[j])):
                j += 1
            append_region = (i + 1, j)
        elif MIRROR_RE.match(ln) and mirror_bounds is None:
            j = i + 1
            while j < n and not re.match(r"^##\s", lines[j]):
                j += 1
            mirror_bounds = (i + 1, j)

    mirror_sections = []
    if mirror_bounds:
        mstart, mend = mirror_bounds
        i = mstart
        cur_label, cur_start = None, None
        while i < mend:
            m = re.match(r"^###\s+(.*)$", lines[i])
            if m:
                if cur_label is not None:
                    mirror_sections.append((cur_label, cur_start, i))
                cur_label, cur_start = m.group(1).strip(), i + 1
            i += 1
        if cur_label is not None:
            mirror_sections.append((cur_label, cur_start, mend))
    return append_region, mirror_sections, below_seed_start


# --------------------------------------------------------------- checks -----

def _strip_field(field: str) -> str:
    return field.strip().strip("*`_ ").strip()


def lint_section(lines, start, end, label, today, flags, notes):
    """G1–G4 over one linted section's top-level bullets."""
    prev_date: date | None = None
    prev_lineno = 0
    for lineno, first, block in iter_blocks(lines, start, end):
        where = f"L{lineno}"
        short = first.lstrip("- ").strip()
        short = (short[:60] + "…") if len(short) > 61 else short

        # G1 — leading parseable date.
        lead = LEADING_DATE_RE.match(first)
        if not lead:
            if DATE_RE.search(block):
                flags.append(
                    f"FLAG [g1-misdated] {where} ({label}): bullet does not "
                    f"LEAD with `- YYYY-MM-DD ·` (a date appears later in "
                    f"the block, where the ager's leading-date rule misses "
                    f"it): {short}")
            else:
                flags.append(
                    f"FLAG [g1-undated] {where} ({label}): undated bare "
                    f"claim — no date anywhere in the entry: {short}")
            continue
        d = parse_date(lead.group(1))
        if d is None:
            flags.append(f"FLAG [g1-baddate] {where} ({label}): leading date "
                         f"{lead.group(1)!r} does not parse as a real "
                         f"YYYY-MM-DD: {short}")
            continue
        if d > today:
            flags.append(f"FLAG [g1-future] {where} ({label}): leading date "
                         f"{d.isoformat()} is in the future "
                         f"(today {today.isoformat()}): {short}")

        # G2 — kind classifiable (the ager's own token rule).
        kind = _kind_token(first)
        if kind is None:
            flags.append(
                f"FLAG [g2-kind] {where} ({label}): 2nd `·`-field is not "
                f"classifiable as capability|wall|UPDATE — the ager cannot "
                f"type this entry: {short}")
        elif kind == "update":
            # G5 interop — an UPDATE must match the ager's exclusion regex.
            if not SUPERSEDE_RE.search(block):
                flags.append(
                    f"FLAG [g5-update-shape] {where} ({label}): UPDATE "
                    f"bullet does not match the ager's supersession-"
                    f"exclusion regex `(?<!un-)supersed` "
                    f"(check_capabilities_wall_age.RESOLVED_MARKERS[0]) — "
                    f"it will never register as a notice there: {short}")
        else:
            # G3 — venue token (capability/wall entries only).
            fields = [p for p in first.split(MIDDOT)]
            venue_raw = _strip_field(fields[2]) if len(fields) > 2 else ""
            if venue_raw in VENUES:
                pass
            elif TOKENISH_RE.match(venue_raw):
                flags.append(
                    f"FLAG [g3-venue] {where} ({label}): 3rd field "
                    f"{venue_raw!r} looks like a venue token but is not one "
                    f"of {sorted(VENUES)}: {short}")
            else:
                notes.append(
                    f"note  [g3-venue-any] {where} ({label}): no venue "
                    f"token — valid per the ledger's own note (read as "
                    f"`any`), but new entries should carry one: {short}")

        # G4 — newest-first (non-increasing downward).
        if prev_date is not None and d > prev_date:
            flags.append(
                f"FLAG [g4-order] {where} ({label}): {d.isoformat()} "
                f"appears BELOW the older {prev_date.isoformat()} "
                f"(L{prev_lineno}) — the section is `newest first`: {short}")
        prev_date, prev_lineno = d, lineno


def lint_supersessions(lines, floor, today, flags, notes):
    """G5 — every supersession/resolution-marked block below the seed fence
    carries a parseable date (the ager's date-guard input)."""
    for lineno, first, block in iter_blocks(lines, floor, len(lines)):
        if not any(rx.search(block) for rx in RESOLVED_MARKERS):
            continue
        if not DATE_RE.search(block):
            short = first.lstrip("- ").strip()
            short = (short[:60] + "…") if len(short) > 61 else short
            flags.append(
                f"FLAG [g5-undated] L{lineno}: block carries a resolution/"
                f"supersession marker but NO parseable YYYY-MM-DD date — "
                f"the ager's supersession date-guard cannot order it: "
                f"{short}")


def lint_stub(stub_text: str | None, flags, notes):
    """G6 — the lowercase pointer stub stays a pointer."""
    if stub_text is None:
        notes.append("note  [g6-stub-missing] docs/capabilities.md (lowercase"
                     ") not found — old links to it will break; the I-44 "
                     "resolution keeps a pointer stub there")
        return
    lines = stub_text.splitlines()
    if "CAPABILITIES.md" not in stub_text:
        flags.append("FLAG [g6-stub] docs/capabilities.md: stub no longer "
                     "points at CAPABILITIES.md — old links dead-end")
    if any(APPEND_LOG_RE.match(ln) for ln in lines):
        flags.append("FLAG [g6-stub] docs/capabilities.md: stub grew its own "
                     "`## Append log` — the ledger must stay ONE file "
                     "(uppercase); append THERE")
    for i, ln in enumerate(lines, 1):
        if LEADING_DATE_RE.match(ln) and _kind_token(ln) in ("wall",
                                                            "capability"):
            flags.append(f"FLAG [g6-stub] docs/capabilities.md:L{i}: dated "
                         f"capability/wall row in the POINTER STUB — content "
                         f"is diverging from the one true ledger")
    if len(lines) > 40:
        flags.append(f"FLAG [g6-stub] docs/capabilities.md: {len(lines)} "
                     f"lines — a pointer stub should stay small (>40 "
                     f"suggests content is accreting at the dead path)")


def analyse(text: str, today: date, stub_text: str | None = None):
    """Return (flags, notes) for the ledger text (+ optional stub text)."""
    flags: list[str] = []
    notes: list[str] = []
    lines = text.splitlines()
    append_region, mirror_sections, seed_floor = find_regions(lines)

    if append_region is None:
        flags.append("FLAG [structure] no `## Append log` heading found — "
                     "the append surface the grammar governs is missing")
    else:
        lint_section(lines, append_region[0], append_region[1],
                     "Append log", today, flags, notes)
    for label, s, e in mirror_sections:
        lint_section(lines, s, e, f"mirror: {label[:40]}", today, flags,
                     notes)
    lint_supersessions(lines, seed_floor, today, flags, notes)
    lint_stub(stub_text, flags, notes)
    return flags, notes


# ------------------------------------------------------------ selftest ------

_FIXTURE = """# fixture ledger

<!-- substrate-kit:capability-seed BEGIN -->
- `any` · **Seed row, kit-owned — never grammar-linted even undated.**
<!-- substrate-kit:capability-seed END -->

## Append log — newest first

- 2026-07-18 · capability · autonomous-project · **Good entry** · evidence ·
  workaround.
- 2026-07-17 · UPDATE (supersedes the earlier teleport WALL): teleport WORKS.
- 2026-07-16 · UPDATE (corrects the earlier teleport reading): teleport is
  actually fine now.
- 2026-07-15 · wall · autonomus-project · **Typo venue** · evidence.
- 2026-07-19 · wall · any · **Out of order — newer below older** · evidence.
- 2026-07-10 · gizmo · any · **Unclassifiable kind token** · evidence.
- A bare claim with no date at all — merging is fine everywhere.
- Misdated: the date 2026-07-09 hides mid-block instead of leading.
- 2026-07-08 · wall · **No venue token, old-style five-field line** · ev.

---

## Mirrored lane findings

### lane-a — mirrored

- 2026-07-14 · wall · any · **Mirror good** · evidence @ `abc1234`.
- 2026-07-14 · capability · owner-live · **Mirror good too** · evidence.

### lane-b — mirrored

- 2026-07-12 · wall · any · **Fine** · evidence.
- 2026-07-13 · wall · any · **Mirror inversion** · evidence.

## Fleet capability manifest (folded)

- **Old wall, SUPERSEDED but with no date anywhere in the block** — the
  marker is present, the date-guard input is not.
- **Old wall, retired properly** — RETIRES the recorded thing, recorded
  2026-07-11.
"""

_STUB_GOOD = ("# moved\n\n> Folded into [CAPABILITIES.md](CAPABILITIES.md). "
              "Do not add content here.\n")
_STUB_BAD = ("# moved\n\n## Append log\n\n- 2026-07-13 · wall · any · "
             "**diverging row** · evidence.\n")


def selftest() -> int:
    fails: list[str] = []
    today = date(2026, 7, 19)
    flags, notes = analyse(_FIXTURE, today, stub_text=_STUB_GOOD)
    jf, jn = "\n".join(flags), "\n".join(notes)

    def expect(cond: bool, msg: str):
        if not cond:
            fails.append(msg)

    expect("Good entry" not in jf and "Mirror good" not in jf,
           "well-formed entries must not be flagged")
    expect("Seed row" not in jf and "Seed row" not in jn,
           "the kit-owned seed fence must never be linted")
    expect("[g3-venue]" in jf and "Typo venue" in jf,
           "a token-shaped wrong venue must flag g3-venue")
    expect("[g3-venue-any]" in jn and "old-style five-field" in jn,
           "an omitted venue must be a note (grandfathered as any)")
    expect("[g4-order]" in jf and "Out of order" in jf,
           "an append-log inversion must flag g4-order")
    expect("Mirror inversion" in jf,
           "a mirror-subsection inversion must flag g4-order")
    expect(jf.count("[g4-order]") == 2,
           "exactly the two seeded inversions must flag g4-order "
           "(section resets must isolate subsections)")
    expect("[g2-kind]" in jf and "Unclassifiable" in jf,
           "an unclassifiable kind token must flag g2-kind")
    expect("[g1-undated]" in jf and "bare claim" in jf,
           "an undated bare claim must flag g1-undated")
    expect("[g1-misdated]" in jf and "Misdated" in jf,
           "a mid-block-only date must flag g1-misdated")
    expect("[g5-update-shape]" in jf and "corrects the earlier" in jf,
           "an UPDATE not matching the ager's supersed regex must flag")
    expect("supersedes the earlier teleport WALL" not in jf,
           "a well-formed UPDATE must not be flagged")
    expect("[g5-undated]" in jf and "no date anywhere" in jf.lower(),
           "an undated supersession block must flag g5-undated")
    expect("retired properly" not in jf,
           "a dated retirement block must not flag g5")
    expect("[g6" not in jf, "a good stub must not flag g6")

    flags2, _ = analyse(_FIXTURE, today, stub_text=_STUB_BAD)
    jf2 = "\n".join(flags2)
    expect(jf2.count("[g6-stub]") >= 3,
           "a diverging stub (no pointer + own append log + dated row) "
           "must flag g6-stub for each violation")

    for msg in fails:
        print(f"SELFTEST FAIL: {msg}", file=sys.stderr)
    print(f"selftest: {'FAIL' if fails else 'PASS'} ({len(fails)} failure(s))"
          f" [shapes: {_SHAPES_SOURCE}]")
    return 1 if fails else 0


# ---------------------------------------------------------------- main ------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--capabilities",
                    default=os.path.join(repo_root(), "docs",
                                         "CAPABILITIES.md"),
                    help="ledger file (default: docs/CAPABILITIES.md)")
    ap.add_argument("--stub",
                    default=os.path.join(repo_root(), "docs",
                                         "capabilities.md"),
                    help="lowercase pointer stub (default: "
                         "docs/capabilities.md)")
    ap.add_argument("--today", default=None,
                    help="override 'today' as YYYY-MM-DD (for testability)")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on any FLAG (default: advisory, exit 0)")
    ap.add_argument("--selftest", action="store_true",
                    help="offline fixture assertions and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    if args.today:
        today = parse_date(args.today)
        if today is None:
            print(f"check_capabilities_grammar: bad --today {args.today!r} "
                  "(want YYYY-MM-DD)", file=sys.stderr)
            return 2
    else:
        today = date.today()

    try:
        with open(args.capabilities, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        print(f"check_capabilities_grammar: cannot read "
              f"{args.capabilities}: {exc}", file=sys.stderr)
        return 2
    stub_text: str | None = None
    try:
        with open(args.stub, encoding="utf-8") as fh:
            stub_text = fh.read()
    except OSError:
        stub_text = None

    flags, notes = analyse(text, today, stub_text=stub_text)
    for line in notes:
        print(line)
    for line in flags:
        print(line)

    if flags:
        verdict = (f"{len(flags)} GRAMMAR FLAG(S) — fix the entry format so "
                   "the S9 ager / no-false-walls guard can parse it "
                   "(smallest true edit; never delete history)")
    else:
        verdict = "CLEAN — every linted append entry matches the grammar"
    print(f"check_capabilities_grammar: {verdict} "
          f"({len(notes)} note(s)) [shapes: {_SHAPES_SOURCE}]")
    return 1 if (flags and args.strict) else 0


if __name__ == "__main__":
    sys.exit(main())
