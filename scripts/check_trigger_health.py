#!/usr/bin/env python3
"""check_trigger_health.py — per-wake seat wake-health invariants (ORDER 020).

================================ PROVENANCE ================================
Why added : ORDER 020 (control/inbox.md, 2026-07-12T16:10Z, P1 reliability;
            canonical spec: superbot docs/owner/
            trigger-health-order-2026-07-12.md). On 2026-07-12
            ~02:30-08:00Z the trigger scheduler degraded SILENTLY: 9
            one-shot ticks dropped, several cron failsafes wedged
            (next_run_at frozen hours in the past while still enabled),
            two seats dark ~6h (Venture Lab, Self Improvement). Everything
            needed to catch it was visible in list_triggers all night —
            nothing was watching. This script is the watcher: run it at
            EVERY manager wake against the freshly exported registry
            snapshot. Detection signature verified against the incident
            registry: `enabled ∧ next_run_at < eval − 15min`.
Date      : 2026-07-12 (lane worker, model: fable-5, dispatched by the
            coordinator; fleet-manager PR #133)
Reliability: unverified — confirm its output against ground truth a few
            times across sessions before trusting it.
            Proof run 1 (2026-07-12, PR #133): replay of the mid-incident
            snapshot (commit 4111da4, captured 06:33Z) surfaced the
            venture-lab failsafe + kit-lab loop wedges and 6
            dropped-by-then one-shots — the spec's done-when; live run
            against the committed gen-14 snapshot found real midday
            degradation residue. Verbatim output in the PR #133 session
            card.
Kill-switch: delete this if it proves unreliable over multiple sessions.
=============================================================================

WHAT IT CHECKS (one PASS/FAIL line per invariant; exit 1 on any FAIL)
  I1 WEDGED-CRON       no enabled standing cron has next_run_at frozen
                       > grace (15min) in the past. A healthy trigger
                       ADVANCES next_run_at after each fire.
  I2 DROPPED-ONESHOT   no enabled one-shot is > grace past run_once_at
                       (a delivered one-shot disables itself). CAVEAT: a
                       QUEUED tick (bound to a busy session; delivers at
                       turn idle — sound by design) is indistinguishable
                       from a LOST one on the registry, so both flag.
  I3 DEAD-CHAIN        no seat session has a dropped tick AND no future
                       tick armed. Recovery = send_message that session
                       (the ONLY working cross-session revival path;
                       fire/update/create_trigger on another session are
                       org-refused; do NOT re-edit .claude/settings.json
                       for the permission prompts — Q-0242).
  I4 MANAGER-FAILSAFE  the fleet-manager seat itself has an enabled,
                       non-wedged standing cron (the dead-man backstop).
  I5 ROSTER-FRESH      docs/roster.md generated-at within the bar (4h) —
                       a stale roster means the regen cron may ITSELF be
                       wedged, and a stale roster hides exactly the
                       silent-dark class this check exists to find.
  I6 SNAPSHOT-FRESH    the snapshot's capture instant is within the bar
                       (4h) of now — findings from an old snapshot
                       describe the past; refresh (list_triggers, ALL
                       pages, write top-level `captured_at`) first.

EVAL INSTANT (why not wall-clock now): a snapshot is a point-in-time
export — judging it at a later wall clock FABRICATES wedges (measured:
the 11:25Z gen-14 snapshot read at 13:54Z false-wedges 7/9 healthy
crons). Health verdicts are evaluated AT the capture instant, resolved by
gen_roster.snapshot_eval_time's ladder: `captured_at` in the export → git
commit time of the snapshot → newest record stamp (labeled conservative).
`--now` overrides everything (replays and tests).

WAKE PROCEDURE (playbook R26): export list_triggers (ALL pages) →
telemetry/triggers-snapshot.json with top-level `captured_at` → run this
script → act on FAILs same wake (send_message recovery / re-arm / owner
queue) → commit snapshot + record the verdict in control/status.md. The
roster's "Trigger health" column/section (gen_roster.py) is the same
logic on the Actions substrate, so the record survives a CCR outage.

USAGE
  python3 scripts/check_trigger_health.py                      # repo default
  python3 scripts/check_trigger_health.py --triggers PATH      # replay file
  python3 scripts/check_trigger_health.py --now 2026-07-12T06:33Z  # replay
  python3 scripts/check_trigger_health.py --selfcheck          # offline
  python3 scripts/check_trigger_health.py --advisory           # warn, exit 0

No third-party deps: stdlib + this repo's gen_roster / check_roster_freshness.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import check_roster_freshness  # noqa: E402  (sibling module, stamp parser)
import gen_roster  # noqa: E402  (sibling module, shared health primitives)

MANAGER_LANE = {"lane": "fleet-manager (this repo)",
                "tokens": ["fleet-manager", "fleet manager"]}
FRESH_BAR_HOURS = 4.0  # same bar as check_roster_freshness (2x wake cadence)


def fmt(dt: datetime | None) -> str:
    return dt.strftime("%Y-%m-%dT%H:%MZ") if dt else "n/a"


def check(records: list[dict], eval_dt: datetime, now: datetime,
          roster_text: str | None, snapshot_age_known: bool) -> list[tuple]:
    """Return [(invariant, passed, detail_lines)] for all six invariants."""
    results = []
    hr = gen_roster.health_report(records, eval_dt)

    # I1 WEDGED-CRON
    lines = []
    for r in hr["wedged"]:
        lines.append(f"`{r['id']}` {r['name']!r} `{r.get('cron_expression')}`"
                     f" next frozen {(r.get('next_run_at') or '?')[:16]}Z"
                     f" · lane: {gen_roster.attribute_lane(r) or '(unattributed)'}")
    results.append(("I1 WEDGED-CRON", not lines, lines or
                    [f"no enabled cron frozen > {gen_roster.WEDGE_GRACE_MIN}m"
                     f" past at {fmt(eval_dt)}"]))

    # I2 DROPPED-ONESHOT
    lines = []
    groups: dict = {}
    for r in hr["dropped"]:
        groups.setdefault(r.get("persistent_session_id"), []).append(r)
    for sess in sorted(groups, key=str):
        rs = groups[sess]
        oldest = min((r.get("run_once_at") or "?")[:16] for r in rs)
        lanes = sorted({gen_roster.attribute_lane(r) or "(unattributed)"
                        for r in rs})
        lines.append(f"`{sess or '(no session id)'}`: {len(rs)} "
                     f"dropped-or-queued, oldest due {oldest}Z · lane: "
                     + ", ".join(lanes))
    if lines:
        lines.append("QUEUED (busy session, delivers at idle) vs LOST is "
                     "indistinguishable on the registry — verify each seat.")
    results.append(("I2 DROPPED-ONESHOT", not groups, lines or
                    ["no enabled one-shot past run_once_at beyond grace"]))

    # I3 DEAD-CHAIN
    lines = []
    for d in hr["dead_chains"]:
        lanes = sorted({gen_roster.attribute_lane(r) or "(unattributed)"
                        for r in d["dropped"]})
        lines.append(f"`{d['session']}` — {len(d['dropped'])} dropped tick(s),"
                     f" NO future tick armed · lane: " + ", ".join(lanes)
                     + f" → RECOVER: send_message session {d['session']} "
                     "to resume + re-arm + verify its own chain")
    results.append(("I3 DEAD-CHAIN", not lines, lines or
                    ["every session with a dropped tick still has a future "
                     "tick armed (or no drops at all)"]))

    # I4 MANAGER-FAILSAFE
    trig = gen_roster.match_lane_triggers(MANAGER_LANE, records)
    standing = trig["standing"]
    if not standing:
        results.append(("I4 MANAGER-FAILSAFE", False,
                        ["NO enabled standing cron attributed to the "
                         "fleet-manager seat — the dead-man backstop is "
                         "missing; re-arm per the startup prompt step 3a"]))
    else:
        wedged = [r for r in standing
                  if gen_roster.trigger_wedged(r, eval_dt)]
        detail = [f"`{r['id']}` {r['name']!r} `{r.get('cron_expression')}` "
                  f"next {(r.get('next_run_at') or '?')[:16]}Z"
                  + (" — WEDGED" if r in wedged else " (future)")
                  for r in standing]
        results.append(("I4 MANAGER-FAILSAFE", not wedged, detail))

    # I5 ROSTER-FRESH
    if roster_text is None:
        results.append(("I5 ROSTER-FRESH", False,
                        ["docs/roster.md unreadable"]))
    else:
        stamp = check_roster_freshness.parse_stamp(roster_text)
        if stamp is None:
            results.append(("I5 ROSTER-FRESH", False,
                            ["no parseable `generated-at **...**` stamp in "
                             "docs/roster.md"]))
        else:
            age_h = (now - stamp).total_seconds() / 3600
            passed = 0 <= age_h <= FRESH_BAR_HOURS
            results.append(("I5 ROSTER-FRESH", passed,
                            [f"generated-at {fmt(stamp)}, {age_h:.1f}h old "
                             f"(bar {FRESH_BAR_HOURS:g}h)"
                             + ("" if passed else
                                " — the roster-regen cron may ITSELF be "
                                "wedged; a stale roster hides the "
                                "silent-dark class (spec step 6)")]))

    # I6 SNAPSHOT-FRESH
    age_h = (now - eval_dt).total_seconds() / 3600
    passed = age_h <= FRESH_BAR_HOURS
    line = (f"snapshot capture instant {fmt(eval_dt)}, {age_h:.1f}h before "
            f"now={fmt(now)} (bar {FRESH_BAR_HOURS:g}h)")
    if not passed:
        line += (" — findings above describe the PAST: refresh the export "
                 "(list_triggers, ALL pages, write top-level `captured_at`) "
                 "and re-run; a wake that skips the refresh is flying blind")
    if not snapshot_age_known:
        line += " [capture instant is a fallback estimate — see basis above]"
    results.append(("I6 SNAPSHOT-FRESH", passed, [line]))
    return results


def selfcheck() -> int:
    """Offline assertions over the invariant wiring. Exit 0 on pass."""
    fails = []

    def ok(cond, msg):
        if not cond:
            fails.append(msg)

    t0 = datetime(2026, 7, 12, 6, 33, tzinfo=timezone.utc)
    manager_ok = {"id": "trig_m", "name": "fleet-manager failsafe wake",
                  "created_at": "t", "enabled": True,
                  "cron_expression": "30 */2 * * *",
                  "next_run_at": "2026-07-12T06:30:00Z"}
    manager_wedged = dict(manager_ok, next_run_at="2026-07-12T04:31:00Z")
    wedged = {"id": "trig_w", "name": "venture-lab money-seat failsafe wake",
              "created_at": "t", "enabled": True,
              "cron_expression": "0 */2 * * *",
              "next_run_at": "2026-07-12T04:06:00Z"}
    dropped = {"id": "trig_o", "name": "send_later 2026-07-12T06:00Z #x",
               "created_at": "t", "enabled": True,
               "run_once_at": "2026-07-12T06:00:00Z",
               "persistent_session_id": "session_dead"}
    roster = "generated-at **2026-07-12T06:00Z**"

    def run(recs, roster_text=roster, now=t0):
        return {name: (passed, detail)
                for name, passed, detail in check(recs, t0, now,
                                                  roster_text, True)}

    healthy = run([manager_ok])
    ok(all(p for p, _ in healthy.values()),
       f"all-green registry passes every invariant ({healthy})")
    r = run([manager_ok, wedged, dropped])
    ok(not r["I1 WEDGED-CRON"][0], "wedged cron reds I1")
    ok(not r["I2 DROPPED-ONESHOT"][0], "dropped one-shot reds I2")
    ok(not r["I3 DEAD-CHAIN"][0], "dropped + no future tick reds I3")
    ok("send_message" in " ".join(r["I3 DEAD-CHAIN"][1]),
       "dead chain names the send_message recovery path")
    ok(r["I4 MANAGER-FAILSAFE"][0], "healthy manager failsafe passes I4")
    ok(not run([wedged])["I4 MANAGER-FAILSAFE"][0],
       "missing manager failsafe reds I4")
    ok(not run([manager_wedged])["I4 MANAGER-FAILSAFE"][0],
       "wedged manager failsafe reds I4")
    live = dict(dropped, id="trig_l", run_once_at="2026-07-12T07:00:00Z")
    ok(run([manager_ok, dropped, live])["I3 DEAD-CHAIN"][0],
       "future tick on the same session keeps the chain out of I3")
    ok(not run([manager_ok], roster_text=None)["I5 ROSTER-FRESH"][0],
       "unreadable roster reds I5")
    ok(not run([manager_ok],
               roster_text="generated-at **2026-07-11T06:00Z**")
       ["I5 ROSTER-FRESH"][0], "24h-stale roster reds I5")
    late = datetime(2026, 7, 12, 13, 54, tzinfo=timezone.utc)
    ok(not run([manager_ok], now=late)["I6 SNAPSHOT-FRESH"][0],
       "7h-old snapshot reds I6")

    for msg in fails:
        print(f"SELFCHECK FAIL: {msg}", file=sys.stderr)
    print(f"selfcheck: {'FAIL' if fails else 'PASS'} ({len(fails)} failure(s))")
    return 1 if fails else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    root = gen_roster.repo_root()
    ap.add_argument("--triggers",
                    default=os.path.join(root, "telemetry",
                                         "triggers-snapshot.json"),
                    help="list_triggers JSON export (default: the committed "
                    "snapshot)")
    ap.add_argument("--roster",
                    default=os.path.join(root, "docs", "roster.md"),
                    help="roster path for the freshness invariant")
    ap.add_argument("--now", help="ISO UTC instant for BOTH the eval instant "
                    "and wall-clock now (replays/tests); default: capture "
                    "instant from the snapshot + real now")
    ap.add_argument("--advisory", action="store_true",
                    help="print the verdict but always exit 0")
    ap.add_argument("--selfcheck", action="store_true",
                    help="run offline assertions and exit")
    args = ap.parse_args(argv)

    if args.selfcheck:
        return selfcheck()

    try:
        with open(args.triggers, encoding="utf-8") as fh:
            payload = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"TRIGGER HEALTH: RED — cannot read {args.triggers}: {exc}")
        return 0 if args.advisory else 1
    try:
        records = gen_roster.validate_export(payload)
    except gen_roster.SchemaError as exc:
        print(f"TRIGGER HEALTH: RED — snapshot schema mismatch: {exc}")
        return 0 if args.advisory else 1

    if args.now:
        now = gen_roster.parse_when(args.now)
        if now is None:
            print(f"cannot parse --now {args.now!r}", file=sys.stderr)
            return 2
        eval_dt, basis = now, "--now override (replay)"
        snapshot_age_known = True
    else:
        now = datetime.now(timezone.utc)
        eval_dt, basis = gen_roster.snapshot_eval_time(
            payload, args.triggers, records)
        snapshot_age_known = "captured_at" in basis
        if eval_dt is None:
            print("TRIGGER HEALTH: RED — no capture-time basis derivable "
                  "from the snapshot (write top-level `captured_at` at "
                  "export time)")
            return 0 if args.advisory else 1

    roster_text = None
    try:
        with open(args.roster, encoding="utf-8") as fh:
            roster_text = fh.read()
    except OSError:
        pass

    enabled = [r for r in records if r.get("enabled")]
    print("=" * 72)
    print(f"TRIGGER HEALTH (ORDER 020) — {len(records)} records, "
          f"{len(enabled)} enabled")
    print(f"evaluated at {fmt(eval_dt)} (basis: {basis}) · "
          f"grace {gen_roster.WEDGE_GRACE_MIN}min · now {fmt(now)}")
    print("=" * 72)
    results = check(records, eval_dt, now, roster_text, snapshot_age_known)
    failed = 0
    for name, passed, detail in results:
        print(f"[{name:<19}] {'PASS' if passed else 'FAIL'} — {detail[0]}")
        for extra in detail[1:]:
            print(f"{'':>28}{extra}")
        failed += 0 if passed else 1
    print("-" * 72)
    if failed:
        print(f"VERDICT: FAIL — {failed}/{len(results)} invariant(s) red. "
              "Act SAME WAKE: send_message dead seats, re-arm/verify wedged "
              "crons you own, refresh stale substrates; record the verdict "
              "in control/status.md (spec step 5; recovery venue caveat "
              "Q-0242).")
    else:
        print(f"VERDICT: PASS — all {len(results)} invariants green.")
    if failed and args.advisory:
        print("(advisory mode: exit 0)")
        return 0
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
