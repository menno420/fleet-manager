#!/usr/bin/env python3
"""check_trigger_health.py — per-wake seat wake-health invariants (ORDER 020).

================================ PROVENANCE ================================
Why added : ORDER 020 (control/inbox.md, 2026-07-12T16:10Z, P1 reliability;
            canonical spec: docs/trigger-health-spec.md — moved into fm
            2026-07-14 per central-docs-plan A2; was superbot docs/owner/
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
Amended   : 2026-07-12 (ORDER 020 update 19:20Z, PR #142) — I7 TICK-PILE-UP
            added after the same-evening live incident: one session held FOUR
            identical pending pacemaker ticks (19:11/19:17/19:39/19:57Z) and
            flooded its chat with degenerate replies as they fired minutes
            apart; the owner had to notice by eye and hand-prune. I7 automates
            that detection + names the hand-prune remedy.
Amended   : 2026-07-14 (wake 0235Z, INC-10) — I8 DUPLICATE-CRON added:
            the 2026-07-13T12:36Z export (f09ba87) held TWO enabled
            identical "Fleet Manager failsafe wake" crons (`30 */2`) and
            both PASSED I4 — the check verified a failsafe exists but
            never flagged duplication (double-fire per wake window). The
            duplicate (trig_01UQTZFvknBosXVo4YKKfazZ) was deleted
            upstream between the 12:36Z and 16:56Z captures (a
            rebind-then-delete cutover; the keeper was created 12:32Z);
            full live enumeration 2026-07-14T03:2xZ confirmed it absent,
            so nothing was deleted this wake. The invariant catches the
            window itself next time.
Amended   : 2026-07-19 (build slice, next-slices queue #3, PR #353) — I8
            remedy made SEAT-PROVENANCE-AWARE: the generic "keep the
            OLDEST-created" rule gave the WRONG answer on the live SBW
            duplicate pair (OQ-SBW-DUP-FAILSAFE, escalated 06:15Z) —
            there the NEWER cron was the current seat session's failsafe
            and the OLDER was the crash-orphan to delete. The remedy now
            says: verify each id's bound session against the owning
            seat's live heartbeat; the id bound to the seat's CURRENT
            session stays, others are crash-orphans (owning seat or hub
            deletes); newest-created is printed as a hint only.
Amended   : 2026-07-13 (heartbeat "Checker gap" + Next-2 baton item 2,
            PR #167) — I1b AMBIGUOUS-ENABLED added: I1 only looks at
            records with `enabled` == True, so a record whose `enabled`
            key is ABSENT from the export was invisible entirely — a cron
            frozen weeks in the past (`trig_011XAWqPeksS8LBrS5G9RvVc`,
            next_run 2026-07-02T03:07Z, observed live 2026-07-13) slipped
            the watchdog. I1b surfaces the absent-`enabled` class without
            guessing liveness.
Amended   : 2026-07-14 (dispatch 0530Z close) — I1b decode RESOLVED:
            live verification ~05:35Z (full 17-page list_triggers
            enumeration, ~1,642 routines; recorded in
            docs/fleet-triage.md) confirmed the API OMITS `enabled` when
            false — absent = DISABLED. Both live instances
            (trig_01MWHvQFnRF1dVdZFSP6SM5L superbot night executor,
            trig_011XAWqPeksS8LBrS5G9RvVc superbot autonomous dispatch)
            are DISABLED/user-paused; a frozen next_run_at on such a
            record is the expected footprint of a pause (a disabled
            routine's next_run_at does not advance), NOT a scheduler
            fault. I1b's frozen-record WARN downgraded to INFO (PASS);
            records stay LISTED, never dropped.
=============================================================================

WHAT IT CHECKS (one PASS/FAIL line per invariant; exit 1 on any FAIL —
WARN lines never affect the exit code)
  I1 WEDGED-CRON       no enabled standing cron has next_run_at frozen
                       > grace (15min) in the past. A healthy trigger
                       ADVANCES next_run_at after each fire.
  I1b AMBIGUOUS-ENABLED registry records with the `enabled` key ABSENT
                       (not False) are invisible to I1. Decode RESOLVED
                       (live-verified 2026-07-14): the API OMITS
                       `enabled` when false, so absent = DISABLED. A
                       fired/ended record also carries an ended_reason
                       (expected history — counted, not listed); an
                       absent-`enabled` record with NO ended_reason is a
                       disabled/user-paused routine — LISTED as INFO,
                       and a frozen next_run_at on it is the expected
                       footprint of a pause (a disabled routine's
                       next_run_at does not advance), not a scheduler
                       fault. Always PASS.
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
  I8 DUPLICATE-CRON    no two ENABLED standing crons share an identical
                       normalized name AND schedule (double-fire every
                       wake window — the INC-10 class: two identical
                       "Fleet Manager failsafe wake" `30 */2` crons both
                       passed I4). WARN, not FAIL: registry `enabled`
                       can lie (I1b caveat), so the remedy is verify EACH
                       live via list_triggers first, then decide by SEAT
                       PROVENANCE: check each id's bound session against
                       the owning seat's live heartbeat — the id bound to
                       the seat's CURRENT session stays; the others are
                       crash-orphans the owning seat (or hub) deletes.
                       Keep-oldest is NOT the rule (2026-07-19 SBW
                       lesson). Lane attribution printed per group.
  I7 TICK-PILE-UP      no session holds >1 PENDING (enabled, unfired)
                       one-shots with same/near-identical message text
                       (timestamps, `#hex` suffixes and digits stripped
                       before comparing). Long-fuse DISTINCT scheduled
                       deliverables (different normalized text) are NOT
                       pile-up. Remedy: prune to the NEWEST tick; record
                       the prune in the roster health column +
                       control/status.md. (ORDER 020 amendment
                       2026-07-12T19:20Z — pacemaker discipline: re-arm
                       ONLY after consuming the prior tick; ONE
                       outstanding tick per session, ever.)

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
import re
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


# ------------------------------------------------ I7 TICK-PILE-UP (helpers) --
# ORDER 020 amendment 2026-07-12T19:20Z: >1 pending pacemaker/work-loop
# one-shot bound to the SAME session with same/near-identical message text
# is a PILE-UP (the stacked-tick chat-flood incident). Distinct long-fuse
# scheduled deliverables on one session (different normalized text) are fine.

_TS_RE = re.compile(r"\d{4}-\d{2}-\d{2}T[\d:.]+Z?")   # ISO timestamps
_HEX_RE = re.compile(r"#[0-9a-fA-F]+\b")               # send_later #hex tags
_DIGIT_RE = re.compile(r"\d+")


def normalize_tick_text(text: str) -> str:
    """Normalize a tick's text for near-identity comparison.

    Strips ISO timestamps, `#hex` suffixes, and remaining digits, then
    lowercases and collapses whitespace — two re-arms of the same work-loop
    prompt differ only in those tokens.
    """
    text = _TS_RE.sub(" ", text)
    text = _HEX_RE.sub(" ", text)
    text = _DIGIT_RE.sub(" ", text)
    return " ".join(text.lower().split())


def pending_oneshot(rec: dict) -> bool:
    """PENDING one-shot: enabled, has run_once_at, no fired/ended state.

    A delivered one-shot disables itself and records
    ended_reason=run_once_fired, so enabled ∧ no ended_reason = not yet
    consumed (whether future-due or past-due/queued).
    """
    return bool(rec.get("enabled") and rec.get("run_once_at")
                and not rec.get("ended_reason"))


def tick_text(rec: dict) -> str:
    """The tick's message text (stored prompt), name as the fallback.

    The stored prompt is the identity that matters — distinct deliverables
    ride distinct prompts even when every send_later NAME normalizes to the
    same string (verified: two SWTK checkpoints, T+7 vs T+14, same session).
    """
    return gen_roster.prompt_text(rec) or rec.get("name", "")


def tick_pileups(records: list[dict]) -> list[dict]:
    """Group pending one-shots by (session, normalized text); >1 = pile-up.

    Returns [{"session", "norm", "ticks"(oldest→newest by run_once_at)}].
    Sessionless one-shots cannot pile onto a session and are skipped.
    """
    groups: dict = {}
    for r in records:
        if not pending_oneshot(r):
            continue
        sess = r.get("persistent_session_id")
        if not sess:
            continue
        groups.setdefault((sess, normalize_tick_text(tick_text(r))),
                          []).append(r)
    pileups = []
    for (sess, norm), ticks in sorted(groups.items()):
        if len(ticks) > 1:
            ticks.sort(key=lambda r: (r.get("run_once_at") or "",
                                      r.get("created_at") or ""))
            pileups.append({"session": sess, "norm": norm, "ticks": ticks})
    return pileups


# ------------------------------------------ I8 DUPLICATE-CRON (helpers) --
# INC-10 (2026-07-14): two enabled standing crons with identical name +
# schedule double-fire every wake window, and I4 passes both (it verifies
# existence, never uniqueness). Signature: identical whitespace-collapsed
# case-folded name AND identical cron_expression, both enabled.


def duplicate_cron_groups(records: list[dict]) -> list[dict]:
    """Group ENABLED standing crons by (normalized name, cron); >1 = dup.

    Returns [{"name", "cron", "crons"(oldest→newest by created_at)}].
    Normalization is deliberately shallow (lowercase + collapse spaces):
    the observed incident was byte-identical names, and a looser match
    would false-positive distinct seats sharing a schedule slot.
    """
    groups: dict = {}
    for r in records:
        if not (r.get("enabled") and r.get("cron_expression")):
            continue
        key = (" ".join(r.get("name", "").lower().split()),
               r["cron_expression"])
        groups.setdefault(key, []).append(r)
    dups = []
    for (name, cron), rs in sorted(groups.items()):
        if len(rs) > 1:
            rs.sort(key=lambda r: r.get("created_at") or "")
            dups.append({"name": name, "cron": cron, "crons": rs})
    return dups


# -------------------------------------- I1b AMBIGUOUS-ENABLED (helpers) --
# PR #167 (2026-07-13): I1 (via gen_roster.health_report) only sees records
# with `enabled` == True, so a record whose `enabled` key is ABSENT from the
# export is skipped by every invariant. Most absent-`enabled` records are
# expected history (a delivered one-shot loses `enabled` and records
# ended_reason=run_once_fired; auto_disabled_* likewise explains itself).
# Decode RESOLVED 2026-07-14 (dispatch 0530Z close; live-verified against
# the full 17-page registry enumeration): the API OMITS `enabled` when
# false, so absent = DISABLED — an absent-`enabled` record with NO
# ended_reason is a disabled/user-paused routine, listed as INFO.


def split_absent_enabled(records: list[dict]) -> tuple[list[dict], list[dict]]:
    """Split absent-`enabled` records into (disabled/paused, remnants).

    First list = `enabled` key absent AND no ended_reason (disabled,
    user-paused — absent decodes as False per the 2026-07-14 live verify);
    remnants = `enabled` key absent WITH an ended_reason (expected history).
    Records that CARRY `enabled` (True or False) belong to the other
    invariants and are not this class.
    """
    absent = [r for r in records if "enabled" not in r]
    ambiguous = [r for r in absent if not r.get("ended_reason")]
    remnants = [r for r in absent if r.get("ended_reason")]
    return ambiguous, remnants


def ambiguous_frozen(rec: dict, eval_dt: datetime) -> bool:
    """Ambiguous record with a FROZEN fire signal: standing cron whose
    next_run_at is > grace in the past — gen_roster.trigger_wedged's
    signature minus the `enabled` gate (which is exactly what's absent).
    """
    if not rec.get("cron_expression"):
        return False
    nra = gen_roster.parse_when(rec.get("next_run_at") or "")
    return (nra is not None
            and (eval_dt - nra).total_seconds() / 60
            > gen_roster.WEDGE_GRACE_MIN)


def check(records: list[dict], eval_dt: datetime, now: datetime,
          roster_text: str | None, snapshot_age_known: bool) -> list[tuple]:
    """Return [(invariant, status, detail_lines)] for all nine invariants.

    status is True (PASS), False (FAIL), or the string "WARN" — WARN is
    truthy on purpose: it never counts toward the failing exit code.
    """
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

    # I1b AMBIGUOUS-ENABLED (PR #167 blind spot; decode RESOLVED
    # 2026-07-14: the API omits `enabled` when false, so absent = disabled
    # — a frozen next_run_at on one is a pause footprint, INFO not WARN)
    disabled, remnants = split_absent_enabled(records)
    frozen = [r for r in disabled if ambiguous_frozen(r, eval_dt)]
    remnant_note = (f"{len(remnants)} ended/fired absent-`enabled` "
                    "remnant(s) — expected history, not listed")
    if not disabled:
        results.append(("I1b AMBIGUOUS-ENABLED", True,
                        [f"no absent-`enabled` record lacks an ended_reason "
                         f"({remnant_note})"]))
    else:
        lines = []
        for r in disabled:
            state = ("FROZEN next_run_at — expected pause footprint, INFO "
                     "(a disabled routine's next_run_at does not advance)"
                     if r in frozen else "no frozen fire signal")
            lines.append(f"`{r['id']}` {r['name']!r} "
                         f"`{r.get('cron_expression')}` next "
                         f"{(r.get('next_run_at') or '?')[:16]}Z — {state}"
                         f" · lane: "
                         f"{gen_roster.attribute_lane(r) or '(unattributed)'}")
        lines.append(remnant_note)
        if frozen:
            lines.append("absent `enabled` = DISABLED (live-verified decode "
                         "2026-07-14: the API omits `enabled` when false) — "
                         "these are user-paused routines, not scheduler "
                         "faults; re-enable or delete via the owner "
                         "Routines screen if unwanted")
        results.append(("I1b AMBIGUOUS-ENABLED", True, lines))

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

    # I7 TICK-PILE-UP (ORDER 020 amendment 2026-07-12T19:20Z)
    lines = []
    for p in tick_pileups(records):
        ids = " → ".join(
            f"`{r['id']}` (due {(r.get('run_once_at') or '?')[:16]}Z)"
            for r in p["ticks"])
        lanes = sorted({gen_roster.attribute_lane(r) or "(unattributed)"
                        for r in p["ticks"]})
        lines.append(f"`{p['session']}`: {len(p['ticks'])} pending "
                     f"near-identical ticks, oldest→newest: {ids} · lane: "
                     + ", ".join(lanes)
                     + f" · text: {p['norm'][:60]!r}"
                     + f" → REMEDY: prune to the NEWEST tick "
                     f"(keep `{p['ticks'][-1]['id']}`, delete the rest); "
                     "record the prune in the roster health column + "
                     "control/status.md")
    results.append(("I7 TICK-PILE-UP", not lines, lines or
                    ["no session holds >1 pending near-identical work-loop "
                     "one-shots (distinct long-fuse deliverables exempt)"]))

    # I8 DUPLICATE-CRON (INC-10, 2026-07-14)
    # ---- remedy REWRITTEN seat-provenance-aware, 2026-07-19 ------------
    # Why changed: the original "keep the OLDEST-created" heuristic gave
    #   the WRONG answer on the live SBW duplicate pair (2026-07-19,
    #   OQ-SBW-DUP-FAILSAFE): the NEWER cron (trig_01DbcKVWxn6RJPhfyRkgTg6m,
    #   created 07-18T17:08Z) was the current seat session's cutover-armed
    #   failsafe — the keeper — while the OLDER (trig_01XJJ88pQaQFRSpVAviCfAZe,
    #   07-17T22:11Z) was the crash-orphan to delete. The 06:15Z escalation
    #   had to invert the checker's advice by hand; a remedy line that can
    #   contradict a correct escalation is worse than none. Duplicates are
    #   almost always a BOOT-4 crash-orphan class (a seat re-armed its
    #   failsafe without its predecessor's cleanup running), so the live
    #   session binding — not creation order — identifies the keeper.
    #   Creation time stays printed as a HINT only (newest-created is
    #   usually the live one), but the heartbeat check decides.
    # Date: 2026-07-19 (build slice, next-slices queue #3, PR #353).
    # Reliability: wording verified against the SBW pair in the committed
    #   snapshot this session; re-confirm on the next live duplicate.
    # --------------------------------------------------------------------
    lines = []
    for d in duplicate_cron_groups(records):
        ids = " · ".join(
            f"`{r['id']}` (created {(r.get('created_at') or '?')[:16]}Z)"
            for r in d["crons"])
        lanes = sorted({gen_roster.attribute_lane(r) or "(unattributed)"
                        for r in d["crons"]})
        lines.append(f"{len(d['crons'])}× enabled {d['name']!r} "
                     f"`{d['cron']}`, oldest→newest: {ids} · lane: "
                     + ", ".join(lanes)
                     + f" → REMEDY: verify EACH live (list_triggers — "
                     "registry `enabled` can lie, I1b caveat), then "
                     "verify EACH id's bound session against the owning "
                     "seat's live heartbeat; the id bound to the seat's "
                     "CURRENT session stays, others are crash-orphans — "
                     "the owning seat (or hub) deletes them; keep-oldest "
                     "is NOT the rule (2026-07-19 SBW lesson: the keeper "
                     "was the NEWEST). Hint: the newest-created "
                     f"(`{d['crons'][-1]['id']}`) is usually the live "
                     "one, but the heartbeat check decides; record the "
                     "dedup in control/status.md + the dispatch log")
    results.append(("I8 DUPLICATE-CRON", "WARN" if lines else True, lines or
                    ["no two enabled standing crons share an identical "
                     "name+schedule"]))
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

    # I7 TICK-PILE-UP (ORDER 020 amendment): two pending re-arms of the
    # same work-loop prompt on one session = pile-up; two DISTINCT
    # long-fuse deliverables on one session = exempt.
    tick_old = {"id": "trig_p1", "name": "send_later 2026-07-12T06:50Z #aa11",
                "created_at": "t", "enabled": True,
                "run_once_at": "2026-07-12T06:50:00Z",
                "persistent_session_id": "session_pile"}
    tick_new = dict(tick_old, id="trig_p2",
                    name="send_later 2026-07-12T06:55Z #bb22",
                    run_once_at="2026-07-12T06:55:00Z")
    r = run([manager_ok, tick_old, tick_new])
    ok(not r["I7 TICK-PILE-UP"][0], "2 pending near-identical ticks red I7")
    i7_text = " ".join(r["I7 TICK-PILE-UP"][1])
    ok("trig_p1" in i7_text and "trig_p2" in i7_text
       and i7_text.index("trig_p1") < i7_text.index("trig_p2"),
       "I7 names the ticks oldest→newest")
    ok("keep `trig_p2`" in i7_text and "prune" in i7_text,
       "I7 remedy prunes to the NEWEST tick")
    fuse_a = {"id": "trig_f1", "name": "send_later 2026-07-19T16:37Z #c1",
              "created_at": "t", "enabled": True,
              "run_once_at": "2026-07-19T16:37:00Z",
              "persistent_session_id": "session_fuse",
              "job_config": {"ccr": {"events": [{"data": {"message":
                  {"content": "T+7 checkpoint: log the funnel numbers"}}}]}}}
    fuse_b = {"id": "trig_f2", "name": "send_later 2026-07-26T16:37Z #c2",
              "created_at": "t", "enabled": True,
              "run_once_at": "2026-07-26T16:37:00Z",
              "persistent_session_id": "session_fuse",
              "job_config": {"ccr": {"events": [{"data": {"message":
                  {"content": "T+14 KILL-RULE checkpoint: assess and act"}}}]}}}
    ok(run([manager_ok, fuse_a, fuse_b])["I7 TICK-PILE-UP"][0],
       "distinct long-fuse deliverables on one session stay out of I7")
    fired = dict(tick_old, id="trig_p3", ended_reason="run_once_fired")
    del fired["enabled"]  # a delivered one-shot loses `enabled` on export
    ok(run([manager_ok, tick_new, fired])["I7 TICK-PILE-UP"][0],
       "an already-fired sibling does not count toward a pile-up")

    # I8 DUPLICATE-CRON (INC-10): two enabled standing crons with an
    # identical normalized name + schedule WARN oldest-first; a disabled
    # twin, a different schedule, or a different name is NOT a duplicate.
    dup_a = {"id": "trig_d1", "name": "Fleet Manager failsafe wake",
             "created_at": "2026-07-12T20:33:00Z", "enabled": True,
             "cron_expression": "30 */2 * * *",
             "next_run_at": "2026-07-12T06:30:00Z"}
    dup_b = dict(dup_a, id="trig_d2", created_at="2026-07-13T12:32:00Z")
    r = run([dup_a, dup_b])
    ok(r["I8 DUPLICATE-CRON"][0] == "WARN",
       "two enabled identical name+schedule crons WARN I8")
    i8_text = " ".join(r["I8 DUPLICATE-CRON"][1])
    ok("trig_d1" in i8_text and "trig_d2" in i8_text
       and i8_text.index("trig_d1") < i8_text.index("trig_d2"),
       "I8 lists the duplicates oldest→newest")
    ok("keep the OLDEST-created" not in i8_text,
       "I8 remedy no longer recommends keep-oldest (2026-07-19 SBW lesson)")
    ok("bound session against the owning seat's live heartbeat" in i8_text,
       "I8 remedy decides by seat provenance (heartbeat session binding)")
    ok("keep-oldest is NOT the rule" in i8_text,
       "I8 remedy states keep-oldest is NOT the rule")
    ok("newest-created (`trig_d2`)" in i8_text,
       "I8 remedy hints the newest-created id (hint only, heartbeat decides)")
    ok("verify EACH live" in i8_text,
       "I8 remedy verifies live before any delete (I1b caveat)")
    ok(run([dup_a, dict(dup_b, cron_expression="0 */2 * * *")])
       ["I8 DUPLICATE-CRON"][0] is True,
       "same name, different schedule is not a duplicate")
    ok(run([dup_a, dict(dup_b, name="Websites failsafe wake")])
       ["I8 DUPLICATE-CRON"][0] is True,
       "different name, same schedule is not a duplicate")
    ok(run([dup_a, dict(dup_b, enabled=False)])
       ["I8 DUPLICATE-CRON"][0] is True,
       "a disabled twin is not a duplicate")
    ok(run([manager_ok])["I8 DUPLICATE-CRON"][0] is True,
       "a single enabled cron passes I8")

    # I1b AMBIGUOUS-ENABLED (PR #167): a record with `enabled` ABSENT is
    # invisible to I1. Decode resolved 2026-07-14 (live-verified: the API
    # omits `enabled` when false): absent = disabled — records are LISTED
    # as INFO and a frozen standing cron among them is a pause footprint
    # (PASS, was WARN). Shapes from the observed live instances
    # (snapshot @ f09ba87; both confirmed disabled/user-paused live).
    ambig_frozen_rec = {"id": "trig_a1", "name": "superbot autonomous dispatch",
                        "created_at": "t",
                        "cron_expression": "0 */3 * * *",
                        "next_run_at": "2026-07-02T03:07:12Z"}
    ambig_idle_rec = {"id": "trig_a2", "name": "superbot night executor",
                      "created_at": "t",
                      "next_run_at": "0001-01-01T00:00:00Z"}
    r = run([manager_ok, ambig_frozen_rec, ambig_idle_rec])
    ok(r["I1 WEDGED-CRON"][0],
       "absent-enabled frozen cron still stays out of I1 (the blind spot "
       "is surfaced by I1b, not folded into I1's enabled semantics)")
    ok(r["I1b AMBIGUOUS-ENABLED"][0] is True,
       "disabled (absent-enabled) record with FROZEN next_run_at PASSes "
       "I1b as INFO (pause footprint — was WARN before the decode)")
    i1b_text = " ".join(r["I1b AMBIGUOUS-ENABLED"][1])
    ok("trig_a1" in i1b_text and "FROZEN" in i1b_text,
       "I1b lists the frozen disabled record as FROZEN")
    ok("trig_a2" in i1b_text, "I1b lists the non-frozen disabled record too")
    ok("pause footprint" in i1b_text and "DISABLED" in i1b_text,
       "I1b decodes absent-enabled as disabled (pause footprint, not fault)")
    ok(run([manager_ok, ambig_idle_rec])["I1b AMBIGUOUS-ENABLED"][0] is True,
       "disabled without a frozen fire signal PASSes I1b (listed only)")
    ok(run([manager_ok, fired])["I1b AMBIGUOUS-ENABLED"][0] is True,
       "ended/fired absent-enabled remnants are expected history, not "
       "the disabled/paused class")

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
    failed = warned = 0
    for name, status, detail in results:
        label = status if isinstance(status, str) else (
            "PASS" if status else "FAIL")
        print(f"[{name:<21}] {label} — {detail[0]}")
        for extra in detail[1:]:
            print(f"{'':>30}{extra}")
        failed += 0 if status else 1        # "WARN" is truthy: never fails
        warned += 1 if status == "WARN" else 0
    print("-" * 72)
    if failed:
        print(f"VERDICT: FAIL — {failed}/{len(results)} invariant(s) red. "
              "Act SAME WAKE: send_message dead seats, re-arm/verify wedged "
              "crons you own, refresh stale substrates; record the verdict "
              "in control/status.md (spec step 5; recovery venue caveat "
              "Q-0242).")
    elif warned:
        print(f"VERDICT: PASS — {len(results) - warned}/{len(results)} "
              f"green, {warned} WARN (see the WARN line(s) above for the "
              "verify-live remedy; exit stays 0).")
    else:
        print(f"VERDICT: PASS — all {len(results)} invariants green.")
    if failed and args.advisory:
        print("(advisory mode: exit 0)")
        return 0
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
