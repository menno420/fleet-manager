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
  IDLE-DECLARED a STALLED/QUIET lane whose OWN heartbeat carries a FRESH,
                dated idle declaration ("backlog dry" / "honest idle" /
                "standing down" / "…slices are drained…" — see the
                DECLARED-IDLE section below): the lane said it stopped on
                purpose. Exit-neutral (--strict never fails on it); the
                headline lists it separately; the matched line is quoted
                verbatim under the table. An UNDATED declaration converts
                the label but keeps the STALLED escalation hint (and the
                --strict failure) — honesty over comfort.
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

WAKE COLUMN — wake-without-work refinement (2026-07-19, groom slice #2)
  The STALLED verdict alone cannot tell WHICH side dropped. The snapshot's
  `last_fired_at` on the lane's failsafe cron can — so each armed lane also
  gets a wake-state annotation that splits silence into two distinct states:

    asleep        the failsafe is armed on paper but was NOT actually firing
                  at the capture instant (no fire on record, or the last fire
                  is > 2 cadence windows older than `captured_at`) — the
                  scheduler side dropped; silence costs nothing but delivers
                  nothing.
    WAKING-IDLE   the failsafe HAS fired >= 2 windows (from the cron cadence
                  + `last_fired_at`) after the lane's newest landed signal —
                  wakes are being delivered and BURNING TOKENS WITH ZERO
                  OUTPUT. A distinct, worse state than mere quiet: the chain
                  runs, the work doesn't land.
    waking        firing on schedule, and the lane's output is not >= 2 fire
                  windows behind (healthy, or too early to call).

  The verdict ladder above is unchanged — the wake column refines STALLED
  (and QUIET) with the burn signal, it never replaces them. Honest caveat:
  the column reads the COMMITTED snapshot only, so fires after `captured_at`
  are invisible (capture lag) — the capture instant is printed with the
  table so the reader knows the blind window. With a single most-recent
  `last_fired_at`, earlier fires are inferred from the cron cadence (a fire
  every cadence window between the lane's last signal and the recorded
  fire), which the on-schedule check above supports.

LEDGER + DIFF — run-to-run transition memory (2026-07-20, #381-card idea)
  Each run's table evaporates when the session ends, so lane-state
  transitions across runs (LIVE→STALLED onset, WAKING-IDLE recovery) are
  invisible unless a human diffs old outputs. Two additions turn the
  checker into a committed time series:

    --ledger [PATH]   append one JSON line per run to PATH (bare --ledger
                      uses telemetry/lane-liveness-ledger.jsonl):
                      {evaluated_at, snapshot_captured_at,
                       lanes: {lane: {verdict, wake_state, fires_since,
                                      age_hours}}}
                      Entries are one line each — no cap needed yet.
                      Partial runs (--repos filter) never append: a
                      filtered entry would poison the time series.
    --diff            compare the CURRENT run against the ledger's last
                      entry and print a TRANSITIONS block (lane ·
                      old→new verdict/wake state) + a one-line headline
                      (N transitions; recoveries vs degradations). With
                      no prior entry it says so honestly. Comparison is
                      on the *class* (LIVE/QUIET/STALLED/DARK/NOT
                      MEASURED; —/waking/asleep?/asleep/WAKING-IDLE), so
                      fire-count or age churn inside the same state never
                      reads as a transition. --diff reads before --ledger
                      appends, so one command does compare-then-record.

EXIT CONTRACT (advisory-only tier, same as the S3/S5/S9 trio — this checker
is NEVER merge-blocking):
  default    exit 0 always (table + one summary line).
  --strict   exit 1 when any lane scores STALLED — including an
             IDLE-DECLARED whose declaration is UNDATED (escalation hint
             kept); a dated-fresh IDLE-DECLARED never fails --strict.
  (--ledger/--diff never change the exit code.)

USAGE
  python3 scripts/check_lane_liveness.py                     # full fleet
  python3 scripts/check_lane_liveness.py --repos websites,fleet-manager
  python3 scripts/check_lane_liveness.py --strict            # wake gate
  python3 scripts/check_lane_liveness.py --now 2026-07-19T07:45Z
  python3 scripts/check_lane_liveness.py --diff --ledger     # compare + record
  python3 scripts/check_lane_liveness.py --selfcheck         # pure logic

No third-party deps: stdlib + the git binary via gen_roster's transport.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import gen_roster  # noqa: E402  (sibling module: LANES, transport, parsers)

DEFAULT_CADENCE_H = 2.0
LIVE_MAX_WINDOWS = 2.0
QUIET_MAX_WINDOWS = 4.0

# Wake-without-work thresholds (see "WAKE COLUMN" in the module docstring).
ASLEEP_LAG_WINDOWS = 2.0     # last fire > this many cadences before capture
WAKING_IDLE_MIN_FIRES = 2    # fires since last output that mean "burning"

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


def _newest_fire(recs: list[dict]) -> datetime | None:
    """Newest parseable `last_fired_at` across enabled standing records."""
    fires = [gen_roster.parse_when(r.get("last_fired_at") or "") for r in recs]
    fires = [f for f in fires if f is not None]
    return max(fires) if fires else None


def lane_cadence(lane: dict,
                 records: list[dict]) -> tuple[float, bool, str,
                                               datetime | None]:
    """(cadence_hours, failsafe_enabled, source_label, last_fired) per lane.

    Pure over (lane, records) so --selfcheck pins it. Cadence = the minimum
    across the lane's own enabled standing crons; else the covering seat's;
    else the assumed default. failsafe_enabled is True only when a real
    enabled standing cron was found on either rung — the assumed rung never
    claims an armed failsafe. last_fired = the newest `last_fired_at` across
    the winning rung's records (None on the assumed rung, or when the
    snapshot carries no parseable fire stamp).
    """
    own = gen_roster.match_lane_triggers(lane, records)["standing"]
    cads = [gen_roster.cadence_hours(r["cron_expression"]) for r in own]
    cads = [c for c in cads if c]
    if cads:
        return min(cads), True, "own failsafe cron", _newest_fire(own)
    cover_name = SEAT_COVER.get(lane.get("repo") or "")
    cover = lane_by_name(cover_name) if cover_name else None
    if cover:
        seat = gen_roster.match_lane_triggers(cover, records)["standing"]
        cads = [gen_roster.cadence_hours(r["cron_expression"]) for r in seat]
        cads = [c for c in cads if c]
        if cads:
            return (min(cads), True,
                    f"seat cron ({cover_name.split(' (')[0]})",
                    _newest_fire(seat))
    return DEFAULT_CADENCE_H, False, "assumed (no armed cron found)", None


# ---------------------------------------------------------------------------
# Wake-without-work detector (groom slice #2)
# ============================== PROVENANCE =================================
# Why added : The 2026-07-19 SBW finding — a seat whose failsafe keeps firing
#             while its lanes land NOTHING is a distinct, worse state than
#             mere quiet: wakes are burning tokens with zero output. The
#             STALLED verdict already correlates last-activity vs cadence but
#             cannot say WHICH side dropped; the committed snapshot's
#             `last_fired_at` can. Splits "asleep" (failsafe not firing) from
#             "WAKING-IDLE" (firing on schedule, no landed output). Evening
#             re-groom rank #2, docs/planning/2026-07-19-next-slices.md;
#             dispatched via the control/status.md baton.
# Date      : 2026-07-19 (build-slice worker, model: fable-5, dispatched by
#             the fleet-manager coordinator seat; PR #379)
# Reliability: unverified — confirm its output against ground truth a few
#             times across sessions before trusting it. Ground-truth run 1
#             (2026-07-19, PR #379): the STALLED SBW constituent lanes scored
#             WAKING-IDLE (seat failsafe last fired 17:15Z, hours after each
#             lane's newest landed signal) — matching the day's hand-read
#             SBW record. Verbatim table in the PR body + session card.
# Kill-switch: delete this block (and the Wake column wiring) if it proves
#             unreliable over multiple sessions.
# ===========================================================================

def fires_since(last_fired: datetime | None, signal: datetime | None,
                cadence_h: float) -> int:
    """Inferred count of failsafe fires AFTER the lane's newest signal.

    Only `last_fired_at` (the most recent fire) is recorded, so earlier
    fires are inferred from the cron cadence: one fire per cadence window
    across the signal→last_fired gap, plus the recorded fire itself.
    0 when the lane landed output at/after the last recorded fire.
    """
    if last_fired is None or signal is None or last_fired <= signal:
        return 0
    gap_h = (last_fired - signal).total_seconds() / 3600.0
    return int(gap_h / cadence_h) + 1


def wake_state(armed: bool, last_fired: datetime | None,
               signal: datetime | None, cadence_h: float,
               captured: datetime | None) -> str:
    """Pure wake-without-work ladder (see module docstring, WAKE COLUMN)."""
    if not armed:
        return "—"
    if last_fired is None:
        return "asleep? (armed, no fire on record)"
    if captured is not None:
        lag_h = (captured - last_fired).total_seconds() / 3600.0
        if lag_h > ASLEEP_LAG_WINDOWS * cadence_h:
            return f"asleep (last fire {gen_roster.age_str(lag_h)} " \
                   "before capture)"
    if signal is None:
        return "waking (no signal to compare)"
    fires = fires_since(last_fired, signal, cadence_h)
    if fires >= WAKING_IDLE_MIN_FIRES:
        return f"WAKING-IDLE ({fires} fires since last output)"
    if fires == 1:
        return "waking (1 fire since output)"
    return "waking"


# ---------------------------------------------------------------------------
# Declared-idle detector (honest idle ≠ silent stall)
# ============================== PROVENANCE =================================
# Why added : 2026-07-20 — the Self Improvement seat closed its wake chain
#             DELIBERATELY at 07:53Z per its honesty guard; its substrate-kit
#             heartbeat's Baton said so in plain text ("Agent-buildable kit
#             slices are drained through v1.20.1 + #555", updated 07:45:00Z)
#             — and the 15:52Z liveness run still scored the lane STALLED,
#             firing the OQ-SI-CHAIN-DEAD escalation + a manager nudge for a
#             halt the lane had honestly declared. The checker read the very
#             heartbeat containing the declaration and ignored its words.
#             This block scans the ALREADY-FETCHED heartbeat text (zero new
#             reads; walls unchanged → NOT MEASURED) for an idle declaration
#             and converts a fresh, dated one into the exit-neutral
#             IDLE-DECLARED verdict. Grammar grounded on the live
#             substrate-kit heartbeat quoted above plus the coordinator's
#             dispatch vocabulary ("backlog dry", "honest idle",
#             "idle-declared", "standing down").
# Date      : 2026-07-20 (build-slice worker, model: fable-5, dispatched by
#             the fleet-manager coordinator seat; PR #400)
# Reliability: unverified — confirm its output against ground truth a few
#             times across sessions before trusting it. Ground-truth run 1
#             (2026-07-20, PR #400): quoted verbatim in the PR body +
#             session card.
# Kill-switch: delete this block (and the IDLE-DECLARED wiring in
#             measure_lane/render/main + the VERDICT_RANK entry) if it
#             proves unreliable over multiple sessions.
# ===========================================================================

# Case-insensitive idle-declaration grammar. The last alternative keys on
# the REAL committed grammar observed in substrate-kit's control/status.md
# ("Agent-buildable kit slices are drained through v1.20.1 + #555") without
# matching unrelated prose: a backlog/slice/queue/lane word followed by
# "drained" within the same sentence fragment.
IDLE_DECLARATION_RE = re.compile(
    r"backlog\s+dry|honest\s+idle|idle-declared|standing\s+down"
    r"|\b(?:backlog|slices?|queue|lanes?)\b[^\n.]{0,60}?\bdrained\b",
    re.IGNORECASE)

# A dated declaration is FRESH only while the declaring heartbeat's
# `updated:` stamp is within this many cadence windows of the lane's newest
# signal — a declaration superseded by later landed activity never converts.
IDLE_FRESH_MAX_WINDOWS = 1.0


def find_idle_declaration(
        statuses: list[dict]) -> tuple[str, datetime | None, str] | None:
    """(verbatim matched line, declaring heartbeat's updated stamp, path).

    Scans the control/status*.md texts a read_heartbeat() already carries —
    no extra fetch. First match wins (control/status.md is always first in
    the statuses list — the primary heartbeat). None when no status text
    declares idle.
    """
    for st in statuses or []:
        text = st.get("text") or ""
        m = IDLE_DECLARATION_RE.search(text)
        if not m:
            continue
        start = text.rfind("\n", 0, m.start()) + 1
        end = text.find("\n", m.end())
        line = text[start: end if end != -1 else len(text)].strip()
        if len(line) > 200:                     # keep the quote readable —
            line = line[:200] + " …[truncated]"  # truncation always marked
        stamp = gen_roster.parse_when(
            gen_roster.parse_status(text).get("updated", ""))
        return line, stamp, st["path"]
    return None


def apply_idle_declaration(
        verdict: str,
        decl: tuple[str, datetime | None, str] | None,
        signal: datetime | None,
        cadence_h: float) -> tuple[str, bool, str | None]:
    """(final verdict, strict_stalled, quoted declaration line). Pure.

    Only a STALLED/QUIET base verdict can convert — LIVE needs no excuse
    and DARK/NOT MEASURED have no readable words to trust. Ladder:
      dated + fresh   → IDLE-DECLARED (exit-neutral; --strict passes).
      dated + stale   → base verdict kept, annotated (superseded claim).
      undated         → IDLE-DECLARED (undated — <base> hint stands);
                        a STALLED base still fails --strict (honesty:
                        an undatable claim cannot clear an escalation).
    """
    base = state_class(verdict)
    strict_stalled = base == "STALLED"
    if decl is None or base not in ("STALLED", "QUIET"):
        return verdict, strict_stalled, None
    quote, stamp, _path = decl
    if stamp is None:
        return (f"IDLE-DECLARED (undated — {base} hint stands)",
                strict_stalled, quote)
    lag_h = ((signal - stamp).total_seconds() / 3600.0
             if signal is not None else 0.0)
    if lag_h > IDLE_FRESH_MAX_WINDOWS * cadence_h:
        return (f"{verdict} (idle declaration stale: "
                f"{gen_roster.age_str(lag_h)} behind newest signal)",
                strict_stalled, quote)
    return "IDLE-DECLARED", False, quote


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
                 max_attempts: int, captured: datetime | None = None) -> dict:
    """One lane's row: signals fetched live, verdict from the pure ladder."""
    cadence, armed, source, last_fired = lane_cadence(lane, records)
    row = {"lane": lane["lane"], "cadence": cadence, "armed": armed,
           "source": source, "signal": None, "signal_kind": "—",
           "age_h": None, "windows": None, "wake": "—", "fires": 0,
           "strict_stalled": False, "idle_quote": None}
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
        row["wake"] = wake_state(armed, last_fired, None, cadence, captured)
        return row
    signal, kind = newest_signal(hb)
    if signal is None:
        row["verdict"] = "DARK"
        row["wake"] = wake_state(armed, last_fired, None, cadence, captured)
        return row
    age_h = (now - signal).total_seconds() / 3600.0
    windows = age_h / cadence
    verdict, strict_stalled, idle_quote = apply_idle_declaration(
        verdict_for(windows, armed),
        find_idle_declaration(hb.get("statuses") or []), signal, cadence)
    row.update(signal=signal.strftime("%Y-%m-%dT%H:%MZ"), signal_kind=kind,
               age_h=age_h, windows=windows, verdict=verdict,
               strict_stalled=strict_stalled, idle_quote=idle_quote,
               wake=wake_state(armed, last_fired, signal, cadence, captured),
               fires=fires_since(last_fired, signal, cadence))
    return row


def render(rows: list[dict], now: datetime, captured_at: str) -> str:
    out = ["# Lane liveness — seat-chain stall detector",
           f"evaluated-at {now.strftime('%Y-%m-%dT%H:%MZ')} · "
           f"triggers snapshot captured_at {captured_at}",
           "",
           "| Lane | Last signal | Kind | Age | Cadence (source) | Windows "
           "| Failsafe | Wake (snapshot) | Verdict |",
           "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        age = gen_roster.age_str(r["age_h"]) if r["age_h"] is not None else "—"
        win = f"{r['windows']:.1f}" if r["windows"] is not None else "—"
        out.append(
            f"| {r['lane']} | {r['signal'] or '—'} | {r['signal_kind']} "
            f"| {age} | {r['cadence']:g}h ({r['source']}) | {win} "
            f"| {'enabled' if r['armed'] else '—'} | {r.get('wake', '—')} "
            f"| {r['verdict']} |")
    stalled = [r["lane"] + (" (undated idle claim)"
                            if r["verdict"].startswith("IDLE-DECLARED")
                            else "")
               for r in rows if r.get("strict_stalled")]
    declared = [r["lane"] for r in rows
                if r["verdict"].startswith("IDLE-DECLARED")
                and not r.get("strict_stalled")]
    dark = [r["lane"] for r in rows if r["verdict"] == "DARK"]
    unmeasured = [r for r in rows if r["verdict"].startswith("NOT MEASURED")]
    idle = [r["lane"] for r in rows
            if r.get("wake", "").startswith("WAKING-IDLE")]
    asleep = [r["lane"] for r in rows
              if r.get("wake", "").startswith("asleep")]
    out += ["", f"STALLED: {', '.join(stalled) if stalled else 'none'} · "
                f"IDLE-DECLARED: {', '.join(declared) if declared else 'none'}"
                " · "
                f"WAKING-IDLE: {', '.join(idle) if idle else 'none'} · "
                f"asleep: {', '.join(asleep) if asleep else 'none'} · "
                f"DARK: {', '.join(dark) if dark else 'none'} · "
                f"not measured: {len(unmeasured)}",]
    quotes = [r for r in rows if r.get("idle_quote")]
    if quotes:
        out += [""] + [f"idle declaration — {r['lane']}: "
                       f"\"{r['idle_quote']}\"" for r in quotes]
    out += [
            "",
            "Wake-column caveat: reads the COMMITTED snapshot only — fires "
            f"after captured_at {captured_at} are invisible (capture lag). "
            "WAKING-IDLE = failsafe fired ≥2 windows after the lane's newest "
            "landed signal (earlier fires inferred from the cron cadence): "
            "wakes are burning tokens with zero landed output. asleep = "
            "armed on paper, not firing at capture."]
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Ledger + transition diff (run-to-run memory)
# ============================== PROVENANCE =================================
# Why added : Each liveness run prints a table that evaporates with the
#             session — lane-state transitions across runs (LIVE→STALLED
#             onset, WAKING-IDLE onset/recovery) were invisible unless a
#             human diffed old outputs (the 21:40Z-vs-20:36Z recovery read
#             on 2026-07-19 was exactly that manual diff). A committed
#             one-line-per-run JSONL ledger + a --diff mode make the
#             checker its own time series. Idea recorded on the PR #381
#             card; dispatched via the control/status.md baton.
# Date      : 2026-07-20 (build-slice worker, model: fable-5, dispatched by
#             the fleet-manager coordinator seat; PR #386)
# Reliability: unverified — confirm its output against ground truth a few
#             times across sessions before trusting it. Ground-truth run 1
#             (2026-07-20, PR #386): first --diff honestly reported "no
#             prior ledger entry"; the second run diffed against the seeded
#             entry minutes earlier. Verbatim outputs in the PR body +
#             session card.
# Kill-switch: delete this block (and the --ledger/--diff wiring + the
#             telemetry/lane-liveness-ledger.jsonl file) if it proves
#             unreliable over multiple sessions.
# ===========================================================================

LEDGER_DEFAULT_REL = os.path.join("telemetry", "lane-liveness-ledger.jsonl")

# Severity ranks for classifying a transition as recovery vs degradation.
# NOT MEASURED / SKIP / NEW / gone rank None → "other" (a measurement or
# roster change, never a lane health verdict — the roster UNREADABLE
# doctrine again).
VERDICT_RANK = {"LIVE": 0, "QUIET": 1, "IDLE-DECLARED": 1, "STALLED": 2,
                "DARK": 2}
WAKE_RANK = {"—": 0, "waking": 0, "asleep?": 1, "asleep": 1, "WAKING-IDLE": 2}


def state_class(text: str) -> str:
    """Collapse a verdict/wake string to its class — the diff unit.

    'WAKING-IDLE (5 fires since last output)' → 'WAKING-IDLE';
    'QUIET (no failsafe armed — may be by design)' → 'QUIET'. Diffing on
    the class means fire-count/age churn inside a state is never a
    transition.
    """
    return text.split(" (")[0].strip()


def ledger_entry(rows: list[dict], now: datetime, captured_at: str) -> dict:
    """One run → one JSONL ledger line (pure over its inputs)."""
    lanes = {}
    for r in rows:
        lanes[r["lane"]] = {
            "verdict": r["verdict"],
            "wake_state": r.get("wake", "—"),
            "fires_since": r.get("fires", 0),
            "age_hours": (round(r["age_h"], 2)
                          if r["age_h"] is not None else None),
        }
    return {"evaluated_at": now.strftime("%Y-%m-%dT%H:%MZ"),
            "snapshot_captured_at": captured_at,
            "lanes": lanes}


def read_last_entry(path: str) -> dict | None:
    """Last parseable JSON line of the ledger, else None (missing/empty)."""
    try:
        with open(path, encoding="utf-8") as fh:
            lines = [ln for ln in fh.read().splitlines() if ln.strip()]
    except OSError:
        return None
    for ln in reversed(lines):
        try:
            entry = json.loads(ln)
        except json.JSONDecodeError:
            continue
        if isinstance(entry, dict) and isinstance(entry.get("lanes"), dict):
            return entry
    return None


def diff_entries(prev: dict, cur: dict,
                 cur_lanes_only: bool = False) -> tuple[list[str], str]:
    """(transition lines, headline) between two ledger entries. Pure.

    A lane transitions when its verdict class OR wake class changed.
    Classification: sum the rank deltas across both dimensions — net down
    = recovery, net up = degradation, else other (incl. mixed moves,
    NEW/gone lanes, NOT MEASURED ends). cur_lanes_only skips gone-lane
    detection (for --repos-filtered runs).
    """
    pl, cl = prev.get("lanes", {}), cur.get("lanes", {})
    names = list(cl) if cur_lanes_only else sorted(set(pl) | set(cl),
                                                   key=str.lower)
    lines, rec, deg, oth = [], 0, 0, 0
    for name in names:
        if name not in pl:
            lines.append(f"- {name} · NEW lane (no prior state)  [other]")
            oth += 1
            continue
        if name not in cl:
            lines.append(f"- {name} · gone (not in this run)  [other]")
            oth += 1
            continue
        pv, cv = state_class(pl[name]["verdict"]), state_class(cl[name]["verdict"])
        pw, cw = (state_class(pl[name].get("wake_state", "—")),
                  state_class(cl[name].get("wake_state", "—")))
        if pv == cv and pw == cw:
            continue
        parts = []
        if pv != cv:
            parts.append(f"verdict {pv}→{cv}")
        if pw != cw:
            parts.append(f"wake {pw}→{cw}")
        deltas = []
        for old, new, rank in ((pv, cv, VERDICT_RANK), (pw, cw, WAKE_RANK)):
            if old != new and old in rank and new in rank:
                deltas.append(rank[new] - rank[old])
        net = sum(deltas)
        tag = ("other" if not deltas else
               "recovery" if net < 0 else
               "degradation" if net > 0 else "other")
        rec += tag == "recovery"
        deg += tag == "degradation"
        oth += tag == "other"
        lines.append(f"- {name} · {' · '.join(parts)}  [{tag}]")
    n = len(lines)
    since = prev.get("evaluated_at", "unknown")
    if n == 0:
        headline = (f"no transitions — all {len(names)} lanes unchanged "
                    f"vs {since}")
    else:
        headline = (f"{n} transition{'s' if n != 1 else ''} vs {since}: "
                    f"{rec} recover{'ies' if rec != 1 else 'y'} · "
                    f"{deg} degradation{'s' if deg != 1 else ''} · "
                    f"{oth} other")
    return lines, headline


def render_diff(prev: dict | None, cur: dict, ledger_path: str,
                cur_lanes_only: bool = False) -> str:
    out = ["", f"## Transitions (vs ledger {ledger_path})"]
    if prev is None:
        out.append("no prior ledger entry — nothing to diff against "
                   "(this run seeds the baseline when --ledger is given)")
        return "\n".join(out)
    lines, headline = diff_entries(prev, cur, cur_lanes_only=cur_lanes_only)
    out.extend(lines)
    out.append(headline)
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
             "cron_expression": "45 */2 * * *",
             "last_fired_at": "2026-07-19T16:45:12.229448Z"},
            {"id": "trig_b", "name": "SuperBot World failsafe wake",
             "created_at": "2026-07-19T00:00:00Z", "enabled": True,
             "cron_expression": "15 1-23/2 * * *",
             "last_fired_at": "2026-07-19T17:15:27Z"}]
    web = lane_by_name("websites")
    assert web and lane_cadence(web, recs) == (
        2.0, True, "own failsafe cron",
        datetime(2026, 7, 19, 16, 45, 12, tzinfo=timezone.utc))
    idle = lane_by_name("superbot-idle (Seat B)")
    cad, armed, src, fired = lane_cadence(idle, recs)
    assert (cad, armed) == (2.0, True) and src.startswith("seat cron"), src
    assert fired == datetime(2026, 7, 19, 17, 15, 27, tzinfo=timezone.utc)
    forge = lane_by_name("product-forge")
    cad, armed, src, fired = lane_cadence(forge, recs)
    assert (cad, armed, fired) == (DEFAULT_CADENCE_H, False, None)
    assert "assumed" in src
    # wake-without-work ladder (pure pins)
    t = lambda h, m=0: datetime(2026, 7, 19, h, m, tzinfo=timezone.utc)  # noqa: E731
    assert fires_since(None, t(10), 2.0) == 0            # no fire on record
    assert fires_since(t(17, 15), None, 2.0) == 0        # no signal (DARK)
    assert fires_since(t(10), t(12), 2.0) == 0           # output after fire
    assert fires_since(t(12, 30), t(12), 2.0) == 1       # sub-window gap
    assert fires_since(t(17, 15), t(7, 34), 2.0) == 5    # the SBW signature
    assert wake_state(False, t(17), t(7), 2.0, t(18)) == "—"
    assert wake_state(True, None, t(7), 2.0, t(18)).startswith("asleep?")
    assert wake_state(True, t(9), t(7), 2.0, t(18)).startswith(
        "asleep (last fire")                             # 9h lag > 2 windows
    assert wake_state(True, t(17, 15), None, 2.0, t(18)) == \
        "waking (no signal to compare)"
    assert wake_state(True, t(17, 15), t(7, 34), 2.0, t(18)) == \
        "WAKING-IDLE (5 fires since last output)"        # SBW ground truth
    assert wake_state(True, t(12, 30), t(12), 2.0, t(13)) == \
        "waking (1 fire since output)"
    assert wake_state(True, t(12, 30), t(13), 2.0, t(13)) == "waking"
    assert wake_state(True, t(17, 15), t(7, 34), 2.0, None) == \
        "WAKING-IDLE (5 fires since last output)"        # no captured_at
    # declared-idle grammar (grounded on the LIVE substrate-kit heartbeat,
    # 2026-07-20 — the verbatim Baton line the SI seat actually wrote)
    kit_line = ("Agent-buildable kit slices are drained through v1.20.1 + "
                "#555. The honest next slice is: land #555 on green.")
    assert IDLE_DECLARATION_RE.search(kit_line)
    for s in ("backlog dry", "Backlog DRY declared", "honest idle",
              "idle-declared this wake", "standing down until orders",
              "queue is drained", "all lanes drained"):
        assert IDLE_DECLARATION_RE.search(s), s
    for s in ("the pool drained overnight",        # no backlog-word anchor
              "drained slices",                    # wrong order
              "backlog grew. Later it drained",    # sentence boundary
              "busy building v1.21"):
        assert not IDLE_DECLARATION_RE.search(s), s
    # declaration finder over synthetic heartbeats
    hb_txt = ("# seat heartbeat\nupdated: 2026-07-20T07:45:00Z\n"
              "phase: waiting\n\n## Baton\n" + kit_line + "\n")
    got = find_idle_declaration([{"path": "control/status.md",
                                  "text": hb_txt}])
    assert got is not None and got[0].startswith(
        "Agent-buildable kit slices are drained")
    assert got[1] == datetime(2026, 7, 20, 7, 45, tzinfo=timezone.utc)
    assert got[2] == "control/status.md"
    assert find_idle_declaration([{"path": "control/status.md",
                                   "text": "phase: building v1.21\n"}]) \
        is None
    undated = find_idle_declaration([{"path": "control/status.md",
                                      "text": "note: backlog dry\n"}])
    assert undated is not None and undated[1] is None
    long = find_idle_declaration(
        [{"path": "control/status.md",
          "text": "backlog dry " + "x" * 300 + "\n"}])
    assert long is not None and long[0].endswith(" …[truncated]")
    assert len(long[0]) == 200 + len(" …[truncated]")
    # apply ladder: (verdict, strict_stalled, quote)
    sig = datetime(2026, 7, 20, 7, 45, tzinfo=timezone.utc)
    fresh = ("backlog dry", sig, "control/status.md")
    assert apply_idle_declaration("STALLED", fresh, sig, 2.0) == \
        ("IDLE-DECLARED", False, "backlog dry")
    assert apply_idle_declaration("QUIET", fresh, sig, 2.0) == \
        ("IDLE-DECLARED", False, "backlog dry")
    assert apply_idle_declaration("STALLED", None, sig, 2.0) == \
        ("STALLED", True, None)
    assert apply_idle_declaration("LIVE", fresh, sig, 2.0) == \
        ("LIVE", False, None)                     # LIVE needs no excuse
    v, strict_flag, q = apply_idle_declaration(
        "STALLED", ("backlog dry", None, "control/status.md"), sig, 2.0)
    assert v == "IDLE-DECLARED (undated — STALLED hint stands)"
    assert strict_flag is True and q == "backlog dry"   # escalation kept
    stale = ("backlog dry",
             datetime(2026, 7, 20, 1, 0, tzinfo=timezone.utc),
             "control/status.md")                 # 6.75h behind signal
    v, strict_flag, _ = apply_idle_declaration("STALLED", stale, sig, 2.0)
    assert v.startswith("STALLED (idle declaration stale:") and strict_flag
    assert state_class("IDLE-DECLARED (undated — STALLED hint stands)") == \
        "IDLE-DECLARED"
    assert VERDICT_RANK["IDLE-DECLARED"] < VERDICT_RANK["STALLED"]  # recovery
    # ledger + diff (pure pins)
    assert state_class("WAKING-IDLE (5 fires since last output)") == \
        "WAKING-IDLE"
    assert state_class("QUIET (no failsafe armed — may be by design)") == \
        "QUIET"
    assert state_class("NOT MEASURED (wall: x)") == "NOT MEASURED"
    assert state_class("waking") == "waking" and state_class("—") == "—"
    rows_a = [{"lane": "a", "verdict": "LIVE", "wake": "waking",
               "fires": 0, "age_h": 0.5},
              {"lane": "b", "verdict": "STALLED",
               "wake": "WAKING-IDLE (5 fires since last output)",
               "fires": 5, "age_h": 10.0}]
    ent_a = ledger_entry(rows_a, t(10), "2026-07-19T09:00:00Z")
    assert ent_a["evaluated_at"] == "2026-07-19T10:00Z"
    assert ent_a["lanes"]["b"] == {"verdict": "STALLED",
                                   "wake_state": "WAKING-IDLE (5 fires "
                                                 "since last output)",
                                   "fires_since": 5, "age_hours": 10.0}
    # identical run → no transitions (fire-count churn is NOT a transition)
    ent_a2 = ledger_entry(
        [dict(rows_a[0]),
         dict(rows_a[1], wake="WAKING-IDLE (7 fires since last output)",
              fires=7)], t(12), "2026-07-19T11:00:00Z")
    lines, head = diff_entries(ent_a, ent_a2)
    assert lines == [] and head.startswith("no transitions — all 2 lanes")
    assert "2026-07-19T10:00Z" in head
    # recovery + degradation + NEW lane
    ent_b = ledger_entry(
        [dict(rows_a[0], verdict="STALLED",
              wake="WAKING-IDLE (3 fires since last output)", fires=3),
         dict(rows_a[1], verdict="LIVE", wake="waking", fires=0),
         {"lane": "c", "verdict": "LIVE", "wake": "—", "fires": 0,
          "age_h": None}], t(12), "2026-07-19T11:00:00Z")
    lines, head = diff_entries(ent_a, ent_b)
    assert lines == [
        "- a · verdict LIVE→STALLED · wake waking→WAKING-IDLE  "
        "[degradation]",
        "- b · verdict STALLED→LIVE · wake WAKING-IDLE→waking  [recovery]",
        "- c · NEW lane (no prior state)  [other]"], lines
    assert head == ("3 transitions vs 2026-07-19T10:00Z: 1 recovery · "
                    "1 degradation · 1 other"), head
    # gone lane detected on full runs, skipped when cur_lanes_only
    lines, _ = diff_entries(ent_b, ent_a)
    assert any("c · gone" in ln for ln in lines)
    lines, _ = diff_entries(ent_b, ent_a, cur_lanes_only=True)
    assert not any("gone" in ln for ln in lines)
    # NOT MEASURED end of a move is never a recovery/degradation
    ent_c = ledger_entry(
        [dict(rows_a[0], verdict="NOT MEASURED (wall: x)", wake="—",
              age_h=None)], t(12), "x")
    lines, _ = diff_entries(ent_a, ent_c, cur_lanes_only=True)
    assert lines == ["- a · verdict LIVE→NOT MEASURED · wake waking→—  "
                     "[other]"], lines
    # no-prior-entry honesty + missing file
    assert read_last_entry("/nonexistent/ledger.jsonl") is None
    assert "no prior ledger entry" in render_diff(None, ent_a, "x.jsonl")
    print("selfcheck OK (69 pins)")
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
    ap.add_argument("--ledger", nargs="?",
                    const=os.path.join(gen_roster.repo_root(),
                                       LEDGER_DEFAULT_REL),
                    default=None, metavar="PATH",
                    help="append this run as one JSON line to the ledger "
                         "(bare --ledger = telemetry/"
                         "lane-liveness-ledger.jsonl); skipped on "
                         "--repos-filtered runs")
    ap.add_argument("--diff", action="store_true",
                    help="print transitions vs the ledger's last entry "
                         "(reads before --ledger appends)")
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
    captured = gen_roster.parse_when(str(payload.get("captured_at") or ""))
    wanted = ({r.strip() for r in args.repos.split(",") if r.strip()}
              if args.repos else None)
    rows = []
    for lane in gen_roster.LANES:
        if wanted is not None and (lane.get("repo") or "") not in wanted:
            continue
        if wanted is None and lane["disposition"] != "live":
            continue  # full runs skip archived/registry-only silently
        rows.append(measure_lane(lane, records, now,
                                 args.max_fetch_attempts,
                                 captured=captured))
    captured_str = str(payload.get("captured_at") or "unknown")
    print(render(rows, now, captured_str))
    if args.diff or args.ledger is not None:
        entry = ledger_entry(rows, now, captured_str)
        ledger_path = args.ledger or os.path.join(gen_roster.repo_root(),
                                                  LEDGER_DEFAULT_REL)
        if args.diff:
            print(render_diff(read_last_entry(ledger_path), entry,
                              os.path.relpath(ledger_path,
                                              gen_roster.repo_root()),
                              cur_lanes_only=wanted is not None))
        if args.ledger is not None:
            if wanted is not None:
                print("\nledger append SKIPPED: --repos filter active — a "
                      "partial run would poison the time series")
            else:
                with open(args.ledger, "a", encoding="utf-8") as fh:
                    fh.write(json.dumps(entry, ensure_ascii=False,
                                        sort_keys=True) + "\n")
                print(f"\nledger: appended entry {entry['evaluated_at']} → "
                      f"{os.path.relpath(args.ledger, gen_roster.repo_root())}")
    if args.strict and any(r.get("strict_stalled") for r in rows):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
