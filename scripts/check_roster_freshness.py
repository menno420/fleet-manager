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

USAGE
  python3 scripts/check_roster_freshness.py                 # repo default
  python3 scripts/check_roster_freshness.py --roster PATH   # fixture tests
  python3 scripts/check_roster_freshness.py --max-age-hours 4 --now ISO
  python3 scripts/check_roster_freshness.py --advisory      # warn, exit 0

No third-party deps: stdlib only.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import datetime, timezone

STAMP_RE = re.compile(r"generated-at\s+\*\*(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}"
                      r"(?::\d{2})?Z?)\*\*")


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
    if age_h > args.max_age_hours:
        return verdict(
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
    return verdict(0, f"ROSTER FRESHNESS: OK — generated-at {stamp_s}, "
                   f"{age_h:.1f}h old (threshold {args.max_age_hours:g}h)")


if __name__ == "__main__":
    sys.exit(main())
