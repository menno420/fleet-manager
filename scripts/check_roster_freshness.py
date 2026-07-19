#!/usr/bin/env python3
"""check_roster_freshness.py — red LOUDLY when docs/roster.md goes stale.

================================ PROVENANCE ================================
Why added : P1 (FRESHNESS) of the fleet centralization plan (superbot
            docs/planning/fleet-centralization-plan-2026-07-11.md §3a):
            the roster was regenerated only when the manager agent woke AND
            hand-exported the trigger registry — if the seat parked, the
            roster silently froze (live proof: ~13h stale on 2026-07-11
            under its own 24h kill-switch). Motivating incident: roster
            gen #6 (2026-07-11) found NINE lane failsafe triggers
            auto-disabled (ended_reason=auto_disabled_env_deleted,
            14:45-16:16Z — likely owner env rebuild; owner verification in
            progress). That silent-dark class is invisible exactly when the
            roster is stale; this checker makes staleness impossible to
            miss. Replaces the retired check_manifest_freshness.py
            (superbot #1974) but pointed at the CANONICAL roster.
Date      : 2026-07-11 (lane worker, model: fable-5, dispatched by
            coordinator cse_012o8pySy5K3AV6JWoPKryZL; fleet-manager PR #81)
Reliability: unverified — confirm its output against ground truth a few
            times across sessions before trusting it.
            Fixture run 1 (2026-07-11, PR #81): known-bad fixture
            (fabricated 2026-07-10T06:00Z stamp) exited 1 RED; known-good
            fixture (fresh stamp) exited 0 — both verbatim in the PR #81
            session card.
Kill-switch: delete this if it proves unreliable over multiple sessions.
=============================================================================

WHAT IT CHECKS
  docs/roster.md carries `generated-at **YYYY-MM-DDTHH:MMZ**` in its header
  (written by scripts/gen_roster.py). This checker parses that stamp and
  exits NONZERO with a loud message when it is older than --max-age-hours
  (default 4.0 = 2x the 2h regen cadence, per the plan's §3a bar; the
  roster's own in-file kill-switch stays the 24h hard line).

SEVERITY CONTRACT (who treats this as blocking)
  - roster-regen workflow: BLOCKING self-check after each regeneration.
  - roster-freshness workflow (PRs): BLOCKING on manager-authored (claude/*)
    branches, ADVISORY elsewhere — a lane/owner PR must never be jammed by
    the manager's own stale roster. The workflow passes --advisory for the
    non-blocking lane; the checker itself stays honest either way.

REGEN-WINDOW SKIP DETECTOR (2026-07-19 addition — advisory, never a new red)
  Parses the cron line(s) out of .github/workflows/roster-regen.yml, computes
  the scheduled regen windows between the roster's generated-at and now, and
  reports `REGEN WINDOWS: N scheduled since generated-at, M missed (grace Xh)`.
  A window is MISSED only when it is older than the grace period (default 2h —
  GitHub delivers crons up to ~2h late) and no newer regen stamp covers it
  (with a single generated-at stamp, every window in range is by construction
  uncovered; a covered window would have advanced generated-at past itself and
  left the range). WARN lines are informational: the 4h freshness bar stays
  the ONLY red. `--strict-windows` is an opt-in exit-1-on-miss for future CI.

USAGE
  python3 scripts/check_roster_freshness.py                 # repo default
  python3 scripts/check_roster_freshness.py --roster PATH   # fixture tests
  python3 scripts/check_roster_freshness.py --max-age-hours 4 --now ISO
  python3 scripts/check_roster_freshness.py --advisory      # warn, exit 0
  python3 scripts/check_roster_freshness.py --workflow PATH # fixture tests
  python3 scripts/check_roster_freshness.py --window-grace-hours 2
  python3 scripts/check_roster_freshness.py --strict-windows  # exit 1 on miss

No third-party deps: stdlib only.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import datetime, timedelta, timezone

STAMP_RE = re.compile(r"generated-at\s+\*\*(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}"
                      r"(?::\d{2})?Z?)\*\*")

# ========================= REGEN-WINDOW SKIP DETECTOR ========================
# ================================ PROVENANCE ================================
# Why added : Slice #2 of docs/planning/2026-07-19-next-slices.md. GitHub's
#             schedule silently dropped the 00:40Z AND 02:40Z regen windows
#             on 2026-07-19 (second consecutive skip night — a 3-night 00:40Z
#             pattern preceded it); this checker stayed green until the 4h
#             bar nearly crossed (03:31Z), so the drops were invisible until
#             a human diffed run history. This block makes every wake that
#             runs the checker self-announce skipped windows while the 4h
#             freshness bar stays the ONLY exit-red. Complements PR #344
#             (odd-hour second cron): #344 reduces drop impact; this makes
#             drops announce themselves whether or not #344 lands.
# Date      : 2026-07-19 (build-slice worker, model: fable-5, dispatched by
#             the fleet-manager coordinator seat; fleet-manager PR #352)
# Reliability: unverified — confirm its output against ground truth a few
#             times across sessions before trusting it. Run 1 (real repo) +
#             a synthetic replay of the 2026-07-19 00:40Z miss are verbatim
#             in the PR #352 session card.
# Kill-switch: delete this block (and its flags) if it proves unreliable
#             over multiple sessions; the freshness contract is untouched.
# ============================================================================

CRON_LINE_RE = re.compile(r"^\s*-\s*cron\s*:\s*[\"']?([^\"'#\n]+)")

# Iteration cap for the minute-walk between generated-at and now. A roster
# older than this is deep past the 24h kill-switch anyway; the report says so
# honestly instead of walking an unbounded range.
_WINDOW_SCAN_MAX_DAYS = 30


def parse_workflow_crons(path: str) -> tuple[list[str], str | None]:
    """Return ([cron specs], None) or ([], reason) when not measurable.

    Tolerates the workflow moving/missing (→ reason string, never a crash).
    Comment lines are skipped so prose mentions of `cron:` don't count;
    duplicate specs are collapsed.
    """
    try:
        with open(path, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
    except OSError as exc:
        return [], f"cannot read workflow {path}: {exc}"
    crons: list[str] = []
    for line in lines:
        if line.lstrip().startswith("#"):
            continue
        m = CRON_LINE_RE.match(line)
        if m:
            spec = m.group(1).strip()
            if spec and spec not in crons:
                crons.append(spec)
    if not crons:
        return [], f"no `- cron:` schedule line found in {path}"
    return crons, None


def _expand_field(spec: str, lo: int, hi: int) -> set[int] | None:
    """Expand one cron field to its value set; None on unsupported syntax."""
    values: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        step = 1
        if "/" in part:
            part, _, step_s = part.partition("/")
            if not step_s.isdigit() or int(step_s) < 1:
                return None
            step = int(step_s)
        if part == "*":
            start, end = lo, hi
        elif "-" in part:
            a, _, b = part.partition("-")
            if not (a.isdigit() and b.isdigit()):
                return None
            start, end = int(a), int(b)
        elif part.isdigit():
            start = end = int(part)
        else:
            return None  # names / L / W / ? — not needed for our workflows
        if start < lo or end > hi or start > end:
            return None
        values.update(range(start, end + 1, step))
    return values or None


def compile_cron(spec: str):
    """Compile a 5-field cron spec → matcher dict, or None on parse failure."""
    fields = spec.split()
    if len(fields) != 5:
        return None
    ranges = [(0, 59), (0, 23), (1, 31), (1, 12), (0, 7)]
    expanded = []
    for raw, (lo, hi) in zip(fields, ranges):
        vals = _expand_field(raw, lo, hi)
        if vals is None:
            return None
        expanded.append(vals)
    minute, hour, dom, month, dow = expanded
    dow = {0 if v == 7 else v for v in dow}  # 7 ≡ Sunday ≡ 0
    return {
        "minute": minute, "hour": hour, "dom": dom, "month": month,
        "dow": dow,
        # standard cron: when BOTH day fields are restricted, match on OR
        "dom_star": fields[2] == "*", "dow_star": fields[4] == "*",
    }


def _cron_matches(c: dict, dt: datetime) -> bool:
    if dt.minute not in c["minute"] or dt.hour not in c["hour"] \
            or dt.month not in c["month"]:
        return False
    dom_ok = dt.day in c["dom"]
    dow_ok = ((dt.weekday() + 1) % 7) in c["dow"]  # Monday=0 → cron Sunday=0
    if c["dom_star"] or c["dow_star"]:
        return dom_ok and dow_ok
    return dom_ok or dow_ok


def scheduled_windows(crons: list[str], start: datetime,
                      end: datetime) -> tuple[list[datetime], str | None]:
    """All scheduled fire instants T with start < T <= end, across all crons.

    Returns (sorted windows, truncation note or None). Raises ValueError on
    an unparseable cron spec — the caller reports "not measured", never a
    guess.
    """
    compiled = []
    for spec in crons:
        c = compile_cron(spec)
        if c is None:
            raise ValueError(f"unsupported cron syntax {spec!r}")
        compiled.append(c)
    note = None
    scan_start = start
    max_span = timedelta(days=_WINDOW_SCAN_MAX_DAYS)
    if end - scan_start > max_span:
        scan_start = end - max_span
        note = (f"scan truncated to the last {_WINDOW_SCAN_MAX_DAYS} days "
                "(roster is deep past the 24h kill-switch)")
    windows: list[datetime] = []
    t = scan_start.replace(second=0, microsecond=0) + timedelta(minutes=1)
    while t <= end:
        if any(_cron_matches(c, t) for c in compiled):
            windows.append(t)
        t += timedelta(minutes=1)
    return windows, note


def report_windows(workflow: str, stamp: datetime, now: datetime,
                   grace_hours: float) -> int:
    """Print the REGEN WINDOWS report; return the number of MISSED windows.

    Informational only — the caller decides what (if anything) exits red.
    A not-measured state prints one line and returns 0 (never invented).
    """
    crons, reason = parse_workflow_crons(workflow)
    if reason:
        print(f"REGEN WINDOWS: not measured — {reason}")
        return 0
    try:
        windows, note = scheduled_windows(crons, stamp, now)
    except ValueError as exc:
        print(f"REGEN WINDOWS: not measured — {exc}")
        return 0
    grace = timedelta(hours=grace_hours)
    missed = [t for t in windows if now - t > grace]
    pending = len(windows) - len(missed)
    print(f"REGEN WINDOWS: {len(windows)} scheduled since generated-at "
          f"{stamp.strftime('%Y-%m-%dT%H:%MZ')} "
          f"(cron {', '.join(crons)}), {len(missed)} missed "
          f"(grace {grace_hours:g}h"
          + (f", {pending} still within grace" if pending else "") + ")")
    if note:
        print(f"REGEN WINDOWS: note — {note}")
    for t in missed:
        age_h = (now - t).total_seconds() / 3600
        print(f"REGEN WINDOWS: WARN — window {t.strftime('%Y-%m-%dT%H:%MZ')} "
              f"MISSED ({age_h:.1f}h ago, no covering regen stamp): the "
              "Actions cron dropped or the landing failed — check "
              ".github/workflows/roster-regen.yml run history")
    return len(missed)

# ====================== end REGEN-WINDOW SKIP DETECTOR ======================


def parse_stamp(text: str) -> datetime | None:
    m = STAMP_RE.search(text)
    if not m:
        return None
    raw = m.group(1).rstrip("Z")
    if len(raw) == 16:
        raw += ":00"
    try:
        return datetime.fromisoformat(raw).replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    default_roster = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "docs", "roster.md")
    ap.add_argument("--roster", default=default_roster,
                    help="path to the roster file (default: docs/roster.md)")
    ap.add_argument("--max-age-hours", type=float, default=4.0,
                    help="staleness threshold (default 4.0 = 2x the 2h "
                    "regen cadence)")
    ap.add_argument("--now", help="ISO UTC instant to measure against "
                    "(testing); default: real now")
    ap.add_argument("--advisory", action="store_true",
                    help="print the verdict but always exit 0")
    default_workflow = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        ".github", "workflows", "roster-regen.yml")
    ap.add_argument("--workflow", default=default_workflow,
                    help="regen workflow to parse cron schedule(s) from "
                    "(default: .github/workflows/roster-regen.yml; missing "
                    "file → windows 'not measured', never a red)")
    ap.add_argument("--window-grace-hours", type=float, default=2.0,
                    help="how late a scheduled window may run before it "
                    "counts as MISSED (default 2.0 — GitHub delivers crons "
                    "up to ~2h late)")
    ap.add_argument("--strict-windows", action="store_true",
                    help="opt-in: exit 1 when any regen window is MISSED "
                    "(future CI use; default is informational WARN only — "
                    "the freshness bar stays the only red)")
    args = ap.parse_args(argv)

    def verdict(code: int, msg: str) -> int:
        print(msg)
        return 0 if args.advisory and code != 0 else code

    try:
        with open(args.roster, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        return verdict(1, f"ROSTER FRESHNESS: RED — cannot read roster: {exc}")

    stamp = parse_stamp(text)
    if stamp is None:
        return verdict(1, "ROSTER FRESHNESS: RED — no parseable "
                       "`generated-at **...**` stamp found in "
                       f"{args.roster} (gen_roster.py writes it; a missing "
                       "stamp means a hand edit or format drift)")

    if args.now:
        raw = args.now.rstrip("Z")
        if len(raw) == 16:
            raw += ":00"
        try:
            now = datetime.fromisoformat(raw)
            now = (now.replace(tzinfo=timezone.utc) if now.tzinfo is None
                   else now.astimezone(timezone.utc))
        except ValueError:
            print(f"cannot parse --now {args.now!r}", file=sys.stderr)
            return 2
    else:
        now = datetime.now(timezone.utc)

    age_h = (now - stamp).total_seconds() / 3600
    stamp_s = stamp.strftime("%Y-%m-%dT%H:%MZ")
    if age_h < 0:
        return verdict(1, f"ROSTER FRESHNESS: RED — generated-at {stamp_s} "
                       f"is IN THE FUTURE ({-age_h:.1f}h ahead of "
                       f"{now.strftime('%Y-%m-%dT%H:%MZ')}); a future stamp "
                       "poisons staleness math (the product-forge class) — "
                       "regenerate with a real `date -u` clock")

    # Regen-window skip report (advisory — see the provenance block above).
    # Runs on both the OK and stale-RED paths; a future stamp skips it
    # (window math on a poisoned clock would be invented, not measured).
    missed = report_windows(args.workflow, stamp, now,
                            args.window_grace_hours)

    if age_h > args.max_age_hours:
        code = verdict(
            1,
            "=" * 72 + "\n"
            f"ROSTER FRESHNESS: RED — docs/roster.md generated-at {stamp_s} "
            f"is {age_h:.1f}h old (threshold {args.max_age_hours:g}h = 2x "
            "regen cadence).\n"
            "THE ROSTER IS STALE: do NOT act on its rows — trust the lane "
            "heartbeats directly (the roster's own kill-switch rule).\n"
            "Fix: check .github/workflows/roster-regen.yml runs (cron "
            "40 */2 * * *) — a dead cron here is the single-point-of-"
            "freshness failing; regenerate via scripts/gen_roster.py "
            "--triggers telemetry/triggers-snapshot.json, and refresh the "
            "snapshot at the next manager wake (list_triggers is MCP-only).\n"
            "Why loud: roster gen #6 found 9 lane failsafes auto-disabled "
            "(auto_disabled_env_deleted) — that silent-dark class hides "
            "behind exactly this staleness.\n" + "=" * 72)
    else:
        code = verdict(0, f"ROSTER FRESHNESS: OK — generated-at {stamp_s}, "
                       f"{age_h:.1f}h old (threshold "
                       f"{args.max_age_hours:g}h)")
    if args.strict_windows and missed and code == 0 and not args.advisory:
        print(f"REGEN WINDOWS: STRICT — exiting 1 on {missed} missed "
              "window(s) (--strict-windows opt-in; without it this is "
              "informational only)")
        code = 1
    return code


if __name__ == "__main__":
    sys.exit(main())
