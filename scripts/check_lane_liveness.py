#!/usr/bin/env python3
"""check_lane_liveness.py — seat-chain stall detector (per-lane liveness verdicts).

================================ PROVENANCE ================================
Why added : Overnight 2026-07-18→19 the websites lane went silent — no commits
            after 21:52Z, ORDER 036 unacked across the 23:45Z / 01:45Z /
            03:45Z failsafe windows, the lane's failsafe cron still ENABLED
            the whole time (firing into a session that produced no landed
            output). The stall was only caught by a ~06Z human-style read
            and became `OQ-WEBSITES-036-STALL` roughly 4h late. Everything
            needed to catch it sooner was already readable: each lane repo's
            newest main commit + heartbeat `updated:` stamp, and the lane's
            failsafe cadence in the committed triggers snapshot. This script
            mechanizes exactly that sweep (planned as slice 1 of
            docs/planning/2026-07-19-next-slices.md; idea from the
            2026-07-19 ~06Z morning card).
Date      : 2026-07-19 (build-slice worker, model: fable-5, dispatched by the
            fleet-manager coordinator seat; fleet-manager PR #350)
Reliability: unverified — confirm its output against ground truth a few
            times across sessions before trusting it.
            Ground-truth run 1 (2026-07-19, PR #350): live run at ~07:4xZ
            scored websites STALLED (last signal 2026-07-18T21:52Z, ~5
            2h-windows silent, failsafe enabled) and fleet-manager LIVE
            (minutes-old commits) — both matching the night-watch record
            by hand. Verbatim table in the PR #350 body + session card.
Kill-switch: delete this if it proves unreliable over multiple sessions.
=============================================================================

WHAT IT DOES
  For every LIVE lane in the roster registry (gen_roster.LANES — the one
  hand-maintained lane→repo map), measure the lane's newest liveness signal:

    signal = max( newest main-commit timestamp,
                  heartbeat `updated:` stamp from control/status*.md )

  read over the roster's proven transport (gen_roster.read_heartbeat: shallow
  fetch looped until FETCH_HEAD == a fresh ls-remote SHA — never trust a
  single fetch through the stale git proxy). Compare the signal's age against
  the lane's expected wake cadence and count silent wake windows:

    windows = age_hours / cadence_hours

  CADENCE SOURCE (per lane, printed in the table so a wrong assumption is
  visible): the lane's own enabled standing cron(s) in the committed
  triggers snapshot (attribution = gen_roster.owns_record, same tokens the
  roster uses); else the covering multi-repo SEAT's cron via SEAT_COVER
  below (the seat failsafes are named after the SEAT, not the repo — the
  INC-62 lesson); else an assumed 2.0h default, labelled "assumed".

VERDICT LADDER
  LIVE          windows <= 2 (activity within ~2 wake windows — the roster's
                own FRESH bar).
  QUIET         2 < windows <= 4; also >4 windows when NO failsafe is armed
                (silence without a wake chain may be by design — flagged,
                never called STALLED).
  STALLED       windows > 4 while the lane's failsafe shows ENABLED in the
                snapshot: wakes should have fired and nothing landed. This
                is the websites-036 signature.
  DARK          repo readable but NO liveness signal measurable at all
                (no parseable commit date, no parseable `updated:` stamp).
  NOT MEASURED  the repo could not be read (auth wall / non-convergent
                proxy). A measurement artifact, never a verdict on the lane
                — reason quoted verbatim, nothing invented (roster
                UNREADABLE doctrine, gen #21 lesson).
  SKIP          archived lanes (stale-by-design) and registry-only seats
                (no repo to measure; their crons still feed SEAT_COVER).

  Trigger-column caveat (same as the roster's): failsafe enabled-ness is
  only as fresh as the committed snapshot's `captured_at`. An enabled
  failsafe proves wakes were SCHEDULED, not delivered — a STALLED verdict
  therefore means "windows passed, nothing landed", whichever side dropped.

EXIT CONTRACT (advisory-only tier, same as the S3/S5/S9 trio — this checker
is NEVER merge-blocking):
  default    exit 0 always (table + one summary line).
  --strict   exit 1 when any lane scores STALLED (wake-procedure use).

USAGE
  python3 scripts/check_lane_liveness.py                     # full fleet
  python3 scripts/check_lane_liveness.py --repos websites,fleet-manager
  python3 scripts/check_lane_liveness.py --strict            # wake gate
  python3 scripts/check_lane_liveness.py --now 2026-07-19T07:45Z
  python3 scripts/check_lane_liveness.py --selfcheck         # pure logic

No third-party deps: stdlib + the git binary via gen_roster's transport.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import gen_roster  # noqa: E402  (sibling module: LANES, transport, parsers)

DEFAULT_CADENCE_H = 2.0
LIVE_MAX_WINDOWS = 2.0
QUIET_MAX_WINDOWS = 4.0

# Multi-repo seats name their failsafe after the SEAT, not any constituent
# repo ("SuperBot World failsafe wake"), so repo-token attribution misses
# them (INC-62). This map hands a constituent repo its covering registry-only
# seat lane. HAND-MAINTAINED like gen_roster.LANES — only pairs verifiable
# from the seat lane names themselves are listed; a repo not covered here
# and without its own cron falls back to the labelled "assumed" default,
# never to a guessed seat.
SEAT_COVER = {
    "superbot-games": "SuperBot World seat (games+idle+mineverse)",
    "superbot-idle": "SuperBot World seat (games+idle+mineverse)",
    "superbot-mineverse": "SuperBot World seat (games+idle+mineverse)",
    "idea-engine": "Ideas Lab seat (idea-engine+sim-lab)",
    "sim-lab": "Ideas Lab seat (idea-engine+sim-lab)",
    "substrate-kit": "Self Improvement seat (substrate-kit)",
    "superbot": "SuperBot 2.0 seat (superbot+superbot-next)",
    "superbot-next": "SuperBot 2.0 seat (superbot+superbot-next)",
}


def lane_by_name(name: str) -> dict | None:
    for lane in gen_roster.LANES:
        if lane["lane"] == name:
            return lane
    return None


def lane_cadence(lane: dict, records: list[dict]) -> tuple[float, bool, str]:
    """(cadence_hours, failsafe_enabled, source_label) for one lane.

    Pure over (lane, records) so --selfcheck pins it. Cadence = the minimum
    across the lane's own enabled standing crons; else the covering seat's;
    else the assumed default. failsafe_enabled is True only when a real
    enabled standing cron was found on either rung — the assumed rung never
    claims an armed failsafe.
    """
    own = gen_roster.match_lane_triggers(lane, records)["standing"]
    cads = [gen_roster.cadence_hours(r["cron_expression"]) for r in own]
    cads = [c for c in cads if c]
    if cads:
        return min(cads), True, "own failsafe cron"
    cover_name = SEAT_COVER.get(lane.get("repo") or "")
    cover = lane_by_name(cover_name) if cover_name else None
    if cover:
        seat = gen_roster.match_lane_triggers(cover, records)["standing"]
        cads = [gen_roster.cadence_hours(r["cron_expression"]) for r in seat]
        cads = [c for c in cads if c]
        if cads:
            return min(cads), True, f"seat cron ({cover_name.split(' (')[0]})"
    return DEFAULT_CADENCE_H, False, "assumed (no armed cron found)"


def verdict_for(windows: float | None, failsafe_enabled: bool) -> str:
    """Pure verdict ladder (see module docstring). None windows = DARK."""
    if windows is None:
        return "DARK"
    if windows <= LIVE_MAX_WINDOWS:
        return "LIVE"
    if windows <= QUIET_MAX_WINDOWS:
        return "QUIET"
    if failsafe_enabled:
        return "STALLED"
    return "QUIET (no failsafe armed — may be by design)"


def newest_signal(hb: dict) -> tuple[datetime | None, str]:
    """(instant, label) of the newest liveness signal in a read_heartbeat()."""
    best, label = None, "none"
    head = gen_roster.parse_when(hb.get("head_date") or "")
    if head is not None:
        best, label = head, "main commit"
    for st in hb.get("statuses") or []:
        stamp = gen_roster.parse_status(st["text"]).get("updated", "")
        when = gen_roster.parse_when(stamp)
        if when is not None and (best is None or when > best):
            best, label = when, f"heartbeat {st['path']}"
    return best, label


def measure_lane(lane: dict, records: list[dict], now: datetime,
                 max_attempts: int) -> dict:
    """One lane's row: signals fetched live, verdict from the pure ladder."""
    cadence, armed, source = lane_cadence(lane, records)
    row = {"lane": lane["lane"], "cadence": cadence, "armed": armed,
           "source": source, "signal": None, "signal_kind": "—",
           "age_h": None, "windows": None}
    if lane["disposition"] != "live":
        row["verdict"] = ("SKIP (archived — stale-by-design)"
                          if lane["disposition"] == "archived"
                          else "SKIP (registry-only, no repo)")
        return row
    url = gen_roster.GITHUB_BASE + lane["repo"]
    try:
        hb = gen_roster.read_heartbeat(url, max_attempts)
    except gen_roster.Wall as wall:
        row["verdict"] = ("NOT MEASURED "
                          f"(wall: {gen_roster.describe_wall(str(wall))})")
        return row
    signal, kind = newest_signal(hb)
    if signal is None:
        row["verdict"] = "DARK"
        return row
    age_h = (now - signal).total_seconds() / 3600.0
    windows = age_h / cadence
    row.update(signal=signal.strftime("%Y-%m-%dT%H:%MZ"), signal_kind=kind,
               age_h=age_h, windows=windows,
               verdict=verdict_for(windows, armed))
    return row


def render(rows: list[dict], now: datetime, captured_at: str) -> str:
    out = ["# Lane liveness — seat-chain stall detector",
           f"evaluated-at {now.strftime('%Y-%m-%dT%H:%MZ')} · "
           f"triggers snapshot captured_at {captured_at}",
           "",
           "| Lane | Last signal | Kind | Age | Cadence (source) | Windows "
           "| Failsafe | Verdict |",
           "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        age = gen_roster.age_str(r["age_h"]) if r["age_h"] is not None else "—"
        win = f"{r['windows']:.1f}" if r["windows"] is not None else "—"
        out.append(
            f"| {r['lane']} | {r['signal'] or '—'} | {r['signal_kind']} "
            f"| {age} | {r['cadence']:g}h ({r['source']}) | {win} "
            f"| {'enabled' if r['armed'] else '—'} | {r['verdict']} |")
    stalled = [r["lane"] for r in rows if r["verdict"] == "STALLED"]
    dark = [r["lane"] for r in rows if r["verdict"] == "DARK"]
    unmeasured = [r for r in rows if r["verdict"].startswith("NOT MEASURED")]
    out += ["", f"STALLED: {', '.join(stalled) if stalled else 'none'} · "
                f"DARK: {', '.join(dark) if dark else 'none'} · "
                f"not measured: {len(unmeasured)}"]
    return "\n".join(out)


def selfcheck() -> int:
    """Offline pins of the pure logic (no network, no snapshot)."""
    assert verdict_for(None, True) == "DARK"
    assert verdict_for(0.4, True) == "LIVE"
    assert verdict_for(2.0, False) == "LIVE"          # boundary inclusive
    assert verdict_for(3.9, True) == "QUIET"
    assert verdict_for(4.0, True) == "QUIET"          # boundary inclusive
    assert verdict_for(4.1, True) == "STALLED"
    assert verdict_for(9.9, False).startswith("QUIET (no failsafe")
    # the websites-036 signature: 21:52Z signal read at 07:45Z, 2h cadence
    win = ((datetime(2026, 7, 19, 7, 45, tzinfo=timezone.utc)
            - datetime(2026, 7, 18, 21, 52, tzinfo=timezone.utc))
           .total_seconds() / 3600.0) / 2.0
    assert verdict_for(win, True) == "STALLED", win
    # cadence resolution over a synthetic registry
    recs = [{"id": "trig_a", "name": "Websites failsafe wake",
             "created_at": "2026-07-19T00:00:00Z", "enabled": True,
             "cron_expression": "45 */2 * * *"},
            {"id": "trig_b", "name": "SuperBot World failsafe wake",
             "created_at": "2026-07-19T00:00:00Z", "enabled": True,
             "cron_expression": "15 1-23/2 * * *"}]
    web = lane_by_name("websites")
    assert web and lane_cadence(web, recs) == (2.0, True, "own failsafe cron")
    idle = lane_by_name("superbot-idle (Seat B)")
    cad, armed, src = lane_cadence(idle, recs)
    assert (cad, armed) == (2.0, True) and src.startswith("seat cron"), src
    forge = lane_by_name("product-forge")
    cad, armed, src = lane_cadence(forge, recs)
    assert (cad, armed) == (DEFAULT_CADENCE_H, False) and "assumed" in src
    print("selfcheck OK (10 pins)")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--triggers",
                    default=os.path.join(gen_roster.repo_root(),
                                         "telemetry", "triggers-snapshot.json"))
    ap.add_argument("--now", help="ISO instant to evaluate at (default: now)")
    ap.add_argument("--repos", help="comma-separated repo filter")
    ap.add_argument("--max-fetch-attempts", type=int, default=5)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 when any lane is STALLED")
    ap.add_argument("--selfcheck", action="store_true")
    args = ap.parse_args(argv)
    if args.selfcheck:
        return selfcheck()
    now = (gen_roster.parse_when(args.now) if args.now
           else datetime.now(timezone.utc))
    if now is None:
        print(f"unparseable --now: {args.now!r}", file=sys.stderr)
        return 2
    try:
        with open(args.triggers, encoding="utf-8") as fh:
            payload = json.load(fh)
        records = gen_roster.validate_export(payload)
    except (OSError, json.JSONDecodeError, gen_roster.SchemaError) as exc:
        print(f"triggers snapshot unreadable: {exc}", file=sys.stderr)
        return 2
    wanted = ({r.strip() for r in args.repos.split(",") if r.strip()}
              if args.repos else None)
    rows = []
    for lane in gen_roster.LANES:
        if wanted is not None and (lane.get("repo") or "") not in wanted:
            continue
        if wanted is None and lane["disposition"] != "live":
            continue  # full runs skip archived/registry-only silently
        rows.append(measure_lane(lane, records, now,
                                 args.max_fetch_attempts))
    print(render(rows, now, str(payload.get("captured_at") or "unknown")))
    if args.strict and any(r["verdict"] == "STALLED" for r in rows):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
