#!/usr/bin/env python3
"""check_fleet_triage_staleness.py — flag stale fleet-triage register verdicts.

================================ PROVENANCE ================================
Why added : NEXT-TASKS.md item S3 (first-build set for the recreated
            fleet-manager, last of the S3/S5/S9 trio; S5/S9 merged).
            docs/fleet-triage.md is the standing "should it exist?" REGISTER
            — a per-repo KEEP/KEEP-SEQUENCE/KEEP-PARKED/ARCHIVE/SEED/DELETE
            verdict table. The file's own §How-to-re-verdict says "a verdict
            is a dated judgment, not a decree" — but nothing enforces the
            dating, so an ACTIVE repo's verdict can silently rot while
            reality moves under it (a KEEP that should now be ARCHIVE, an
            action item already done). This checker parses the register,
            computes each ACTIVE row's evidence pin (the newest date that
            substantiates its verdict — an in-row re-verdict/SHA/PR date OR
            the newest dated sweep-note that names the repo), ages it, and
            flags any active row unsubstantiated past --max-age-days as
            re-verify-due. It turns the prose discipline into a mechanical
            prompt — the S3 sibling of S9's wall-age flagger.
Date      : 2026-07-18 (lane worker, model: Opus 4.8, dispatched by the
            recreated fleet-manager coordinator; fleet-manager PR #299)
Reliability: unverified — confirm its output against ground truth a few
            times across sessions before trusting it. The row-verdict split
            and the sweep-note substantiation are best-effort text parsing
            over a hand-written living ledger, not a strict schema: a repo is
            credited by a dated sweep-note when its canonical name appears in
            that note's body (word-boundary match, hyphen-variant guarded),
            so a note that only *alludes* to a repo without naming it could
            under-credit it (fails SAFE — an extra re-verify prompt, never a
            false merge block; this checker is advisory and never wired into
            a blocking gate). Frozen-by-design rows are excluded on verdict +
            marker heuristics; a mis-tagged row could be under-flagged.
Kill-switch: delete this if it proves unreliable over multiple sessions.
=============================================================================

WHAT IT CHECKS (docs/fleet-triage.md, or --triage PATH)
  Only the REGISTER table (the rows under the "## Register (verdicts as of
  YYYY-MM-DD …)" heading, up to the next "## " heading). The seat-restructure
  table and the dated sweep-note tables are NOT register rows and are skipped
  for verdict-aging — but the dated sweep NOTES are read as *substantiating
  evidence* for the rows (see below).

  REGISTER ROW GRAMMAR (6-column markdown table):
    | Repo | Seat | Health | Verdict | rationale | next action |
    - Repo   : column 0, e.g. `**superbot-next** (rebuild)` -> `superbot-next`
               (strip bold, take the text before the first ` (`).
    - Verdict: column 3, first recognized token of
               KEEP-SEQUENCE | KEEP-PARKED | KEEP-QUIET | KEEP unarchived |
               KEEP | ARCHIVE | SEED | DELETE (may be **bold** and trailed by
               a `*(re-verdict …)*` parenthetical).

  ACTIVE vs FROZEN-BY-DESIGN (only ACTIVE rows are aged):
    - FROZEN / stable states (EXCLUDED, listed as notes — a parked/finished
      repo's verdict is a stable state, not rot):
        * verdict in {ARCHIVE, SEED, DELETE}
        * verdict in {KEEP-PARKED, KEEP-QUIET} or a "KEEP unarchived"/dormant
          KEEP verdict
        * any row whose text carries a by-design stability marker
          (/dormant|by design|by-design|wound-down|archive-ready|frozen|
          stale-by-design/i)
    - ACTIVE (AGED / flaggable): a plain KEEP or KEEP-SEQUENCE row with no
      such marker — the repos actively managed, whose verdicts can rot.

  EVIDENCE PIN (freshest wins) for an ACTIVE row:
    max of
      (1) the newest YYYY-MM-DD embedded in the row itself (a re-verdict /
          SHA-note / "post-seed" date), else the register SEED date parsed
          from the "## Register (verdicts as of YYYY-MM-DD …)" heading; and
      (2) the newest dated sweep-NOTE (a "## YYYY-MM-DD · …" section) whose
          body names the repo — the living register is swept ~daily, and a
          verdict named in a fresh sweep IS freshly substantiated.
    age = today - pin; flag when age > --max-age-days.

SEVERITY CONTRACT (sibling-parity: check_capabilities_wall_age /
check_owner_queue / check_roster_freshness / check_docs_links)
  Default DIRECT run exits 1 when any active verdict is re-verify-due, 0 when
  clean. `--advisory` prints FLAG lines as `::warning::` and always exits 0
  (S3 is specced ADVISORY / never merge-blocking, satisfied structurally too:
  this checker is standalone and NOT wired into `bootstrap.py check`).

USAGE
  python3 scripts/check_fleet_triage_staleness.py                 # default 21d
  python3 scripts/check_fleet_triage_staleness.py --max-age-days 30
  python3 scripts/check_fleet_triage_staleness.py --today 2026-08-20
  python3 scripts/check_fleet_triage_staleness.py --advisory      # exit 0
  python3 scripts/check_fleet_triage_staleness.py --triage PATH
  python3 scripts/check_fleet_triage_staleness.py --selftest      # offline

No third-party deps: stdlib only.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import date, datetime

DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
# A register table data row: starts with "| ", not the header/separator.
TABLE_ROW_RE = re.compile(r"^\|(?!-)(.+)\|\s*$")
SEP_ROW_RE = re.compile(r"^\|[\s:|-]+\|\s*$")

# Verdict tokens, longest-first so KEEP-SEQUENCE wins over KEEP.
VERDICT_RE = re.compile(
    r"\b(KEEP[-‑]SEQUENCE|KEEP[-‑]PARKED|KEEP[-‑]QUIET|"
    r"KEEP[-‑]unarchived|KEEP\s+unarchived|KEEP|ARCHIVE|SEED|DELETE)\b",
    re.IGNORECASE,
)

# Register default seed date if the heading carries none.
DEFAULT_SEED = date(2026, 7, 11)

# Stable-state markers: a row carrying one is a settled state, not rot. These
# are the file's PRECISE stability phrasings only — bare "by design" is
# deliberately excluded because it also appears in a non-freezing sense in an
# active row (sim-lab's "idle-by-design not stuck"). Every genuinely-frozen
# register row is ALSO caught by its verdict token (FROZEN_VERDICTS /
# KEEP-UNARCHIVED), so this marker only widens the net to a plain-KEEP row that
# the register itself calls dormant / wound-down / archive-ready.
FROZEN_MARKERS = re.compile(
    r"\bdormant\b|wound[-\s]down|archive[-\s]ready|\bfrozen\b|stale-by-design",
    re.IGNORECASE,
)

# Verdicts that are themselves stable states (never aged).
FROZEN_VERDICTS = {"ARCHIVE", "SEED", "DELETE", "KEEP-PARKED", "KEEP-QUIET"}


def repo_root() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ------------------------------------------------------------ block parse ---

def _split_cells(row_line: str) -> list[str]:
    """Split a markdown table row into stripped cell texts."""
    inner = row_line.strip()
    if inner.startswith("|"):
        inner = inner[1:]
    if inner.endswith("|"):
        inner = inner[:-1]
    return [c.strip() for c in inner.split("|")]


def _repo_name(cell: str) -> str:
    """`**superbot-next** (rebuild)` -> `superbot-next`."""
    s = cell.replace("*", "").strip()
    s = s.split("(", 1)[0].strip()
    # Drop any trailing markdown emphasis / stray tokens.
    return s.strip()


def _norm_verdict(raw: str) -> str | None:
    m = VERDICT_RE.search(raw)
    if not m:
        return None
    tok = m.group(1).upper().replace("‑", "-")
    tok = re.sub(r"\s+", " ", tok)
    if tok == "KEEP UNARCHIVED":
        tok = "KEEP-UNARCHIVED"
    return tok


def _newest_date(text: str) -> date | None:
    best: date | None = None
    for raw in DATE_RE.findall(text):
        try:
            d = datetime.strptime(raw, "%Y-%m-%d").date()
        except ValueError:
            continue
        if best is None or d > best:
            best = d
    return best


def _repo_pattern(name: str) -> re.Pattern:
    """Word-boundary match for a repo name, guarded against hyphen variants.

    `superbot` must NOT match inside `superbot-next` / `superbot-idle`, so a
    trailing `-<word>` is negatively looked-ahead; `superbot-next` still
    matches literally.
    """
    return re.compile(r"\b" + re.escape(name) + r"\b(?!-\w)", re.IGNORECASE)


def parse_register(text: str):
    """Return (seed_date, [rows]) — rows only from the Register table.

    Each row dict: {repo, verdict, lineno, row_text, row_date}.
    row_date = newest date embedded in the row line itself (or None).
    """
    lines = text.splitlines()
    seed_date = DEFAULT_SEED
    rows: list[dict] = []
    in_register = False
    seen_header = False
    for i, line in enumerate(lines):
        hm = HEADING_RE.match(line)
        if hm:
            title = hm.group(2)
            if hm.group(1) == "##":
                # Enter the register on its heading; leave on the next H2.
                if re.match(r"Register\b", title, re.IGNORECASE):
                    in_register = True
                    seen_header = False
                    d = _newest_date(title)
                    if d:
                        seed_date = d
                else:
                    in_register = False
            continue
        if not in_register:
            continue
        if SEP_ROW_RE.match(line):
            seen_header = True
            continue
        m = TABLE_ROW_RE.match(line)
        if not m:
            continue
        cells = _split_cells(line)
        if len(cells) < 4:
            continue
        # The first table row is the column header (Repo | Seat | …); skip it
        # until the separator row is seen.
        if not seen_header:
            continue
        verdict = _norm_verdict(cells[3])
        if verdict is None:
            continue
        repo = _repo_name(cells[0])
        if not repo:
            continue
        rows.append({
            "repo": repo,
            "verdict": verdict,
            "lineno": i + 1,
            "row_text": line,
            "row_date": _newest_date(line),
        })
    return seed_date, rows


def parse_sweep_notes(text: str):
    """Return [(date, body_text)] for each dated '## YYYY-MM-DD · …' section."""
    lines = text.splitlines()
    notes: list[tuple[date, str]] = []
    cur_date: date | None = None
    cur_body: list[str] = []

    def flush():
        if cur_date is not None:
            notes.append((cur_date, "\n".join(cur_body)))

    for line in lines:
        hm = HEADING_RE.match(line)
        if hm and hm.group(1) == "##":
            flush()
            cur_body = []
            title = hm.group(2)
            # A sweep note's heading LEADS with a date (e.g.
            # "## 2026-07-18 · overnight oversight sweep").
            mdate = re.match(r"\s*(\d{4}-\d{2}-\d{2})\b", title)
            cur_date = None
            if mdate:
                try:
                    cur_date = datetime.strptime(
                        mdate.group(1), "%Y-%m-%d").date()
                except ValueError:
                    cur_date = None
        else:
            cur_body.append(line)
    flush()
    return notes


def _is_frozen(row: dict) -> bool:
    if row["verdict"] in FROZEN_VERDICTS:
        return True
    if row["verdict"] == "KEEP-UNARCHIVED":
        return True
    if FROZEN_MARKERS.search(row["row_text"]):
        return True
    return False


# --------------------------------------------------------------- checks -----

def analyse(text: str, today: date, max_age_days: int):
    """Return (flags, notes) line lists for the register.

    flags = re-verify-due active verdicts (exit-code-affecting); notes =
    frozen-by-design rows (informational, never affect the exit code).
    """
    seed_date, rows = parse_register(text)
    sweeps = parse_sweep_notes(text)

    flags: list[str] = []
    notes: list[str] = []
    for row in rows:
        repo = row["repo"]
        if _is_frozen(row):
            notes.append(
                f"note  [frozen-by-design] L{row['lineno']}: {repo} "
                f"({row['verdict']}) — stable state, not aged")
            continue
        # Evidence pin: newest of in-row date (or seed) + newest sweep-note
        # that names the repo.
        pin = row["row_date"] or seed_date
        pin_src = "in-row date" if row["row_date"] else "register seed"
        pat = _repo_pattern(repo)
        for d, body in sweeps:
            if d > pin and pat.search(body):
                pin = d
                pin_src = f"sweep-note {d.isoformat()}"
        age = (today - pin).days
        if age > max_age_days:
            flags.append(
                f"FLAG [reverify-due] L{row['lineno']}: {repo} "
                f"({row['verdict']}) — last substantiated {pin.isoformat()} "
                f"({pin_src}) is {age}d old (> {max_age_days}d); re-verify "
                "against live source and re-date the row (§How-to-re-verdict)")
    return flags, notes


# ------------------------------------------------------------ selftest ------

_FIXTURE = """# Fleet triage register — fixture

## Register (verdicts as of 2020-01-01; seed)

| Repo | Seat | Health | Verdict | rationale | next action |
|---|---|---|---|---|---|
| **repo-stale** (active thing) | Seat A | 🟢 | KEEP | active, verdict last touched 2020-02-02 | do a thing |
| **repo-fresh** (active thing) | Seat A | 🟢 | KEEP-SEQUENCE | active, mid-build; no in-row date | build the next slice |
| **repo-archived** (finished CLI) | none | ⚫ parked | **ARCHIVE** | finished, wound-down 2020-01-01 | owner archive click |
| **repo-parked** (dormant) | Seat B | 🟢 | **KEEP-PARKED** | keep the asset, park the loop; idle by design | leave parked |
| **superbot** (hub) | Seat H | 🟢 | KEEP | hub, verdict 2020-03-03 | live-verify |

## 2020-01-01 owner restructure — seat table (NOT register)

| Seat | dir | repos | notes |
|---|---|---|---|
| Seat A | a/ | repo-fresh | should never be aged as a register row |

## 2026-07-17 · a dated sweep note that names repo-fresh

> repo-fresh shipped a fresh slice today; superbot hub also swept.
The other active repo is not named in this note.
"""


def selftest() -> int:
    fails: list[str] = []
    today = date(2026, 7, 18)
    flags, notes = analyse(_FIXTURE, today, max_age_days=30)
    jf = "\n".join(flags)
    jn = "\n".join(notes)

    # 1. Stale active KEEP (in-row 2020, no sweep mention) -> flagged.
    if "repo-stale" not in jf:
        fails.append("stale active KEEP (2020, unswept) should be re-verify-due")
    # 2. Active KEEP-SEQUENCE substantiated by a 2026-07-17 sweep -> NOT flagged.
    if "repo-fresh" in jf:
        fails.append("repo-fresh (sweep-substantiated 2026-07-17) must not flag")
    # 3. ARCHIVE row -> frozen note, never flagged.
    if "repo-archived" in jf:
        fails.append("ARCHIVE row must not be flagged")
    if "repo-archived" not in jn or "frozen-by-design" not in jn:
        fails.append("ARCHIVE row should be a [frozen-by-design] note")
    # 4. KEEP-PARKED row -> frozen note, never flagged.
    if "repo-parked" in jf:
        fails.append("KEEP-PARKED row must not be flagged")
    # 5. The seat-restructure table row must NOT be parsed as a register row.
    #    (repo-fresh appears there too; if mis-parsed it would double-list.)
    if jf.count("repo-fresh") + jn.count("repo-fresh") > 0 and "repo-fresh" in jf:
        fails.append("seat-table row must not leak into register aging")
    # 6. superbot hub: named in the 2026-07-17 sweep (word-boundary, not via
    #    a hyphen variant) -> substantiated fresh, NOT flagged despite 2020 row.
    if "superbot (hub)" in jf or re.search(r"\bsuperbot\b.*reverify", jf):
        fails.append("superbot hub named in fresh sweep must not be flagged")

    for msg in fails:
        print(f"SELFTEST FAIL: {msg}", file=sys.stderr)
    print(f"selftest: {'FAIL' if fails else 'PASS'} ({len(fails)} failure(s))")
    if not fails:
        print("--- fixture flags ---")
        print(jf or "(none)")
        print("--- fixture notes ---")
        print(jn or "(none)")
    return 1 if fails else 0


# ---------------------------------------------------------------- main ------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--triage",
                    default=os.path.join(repo_root(), "docs",
                                         "fleet-triage.md"),
                    help="register file (default: docs/fleet-triage.md)")
    ap.add_argument("--max-age-days", type=int, default=21,
                    help="flag active verdicts unsubstantiated longer than "
                         "this many days (default 21 — the living register is "
                         "swept ~daily, so 21d spans ~20 missed sweep windows)")
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
            print(f"check_fleet_triage_staleness: bad --today {args.today!r} "
                  "(want YYYY-MM-DD)", file=sys.stderr)
            return 2
    else:
        today = date.today()

    try:
        with open(args.triage, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        print(f"check_fleet_triage_staleness: cannot read "
              f"{args.triage}: {exc}", file=sys.stderr)
        return 2

    flags, notes = analyse(text, today, args.max_age_days)
    for line in notes:
        print(line)
    for line in flags:
        print(f"::warning::{line}" if args.advisory else line)

    if flags:
        verdict = (f"{len(flags)} ACTIVE VERDICT(S) RE-VERIFY-DUE "
                   f"(> {args.max_age_days}d as of {today.isoformat()}) — "
                   "re-verify each against live source and re-date the row")
    else:
        verdict = (f"CLEAN — no active register verdict is unsubstantiated "
                   f"longer than {args.max_age_days}d as of "
                   f"{today.isoformat()}")
    print(f"check_fleet_triage_staleness: {verdict} "
          f"({len(notes)} note(s): frozen-by-design)")
    return 0 if (not flags or args.advisory) else 1


if __name__ == "__main__":
    sys.exit(main())
