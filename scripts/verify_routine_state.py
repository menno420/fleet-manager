#!/usr/bin/env python3
"""verify_routine_state.py — one-command claimed-vs-actual routine-state proof.

================================ PROVENANCE ================================
Why added : 2026-07-18 wake friction (coordinator seat, PR #335). Proving
            the seat's routine-chain state after a HUNG create_trigger call
            took a 20-page hand list_triggers pagination, because the
            committed snapshot was 6.1h stale and the heartbeat's claims
            (armed failsafe id, deleted predecessor) had no one-command
            diff against a real export. This script IS that diff: feed it
            any list_triggers export and it verifies control/status.md's
            routine-block claims against it — claimed failsafe present +
            enabled + cron-matching, no unclaimed seat-named duplicates/
            orphans, claimed-deleted ids actually gone — and reports the
            seat's pending pacemaker one-shots. It also accepts a FLAT
            JSON ARRAY of records (the raw shape a hand export lands in),
            the friction PR #334's review flagged: no more hand-wrapping
            into the page shape just to run tooling over it.
Date      : 2026-07-18 (improvement-slice worker, model: fable-5,
            dispatched by the coordinator; fleet-manager PR #335)
Reliability: unverified — confirm its output against ground truth a few
            times across sessions before trusting it.
            Proof run 1 (2026-07-18, PR #335): run against the committed
            20:42:05Z snapshot + the 21:15Z heartbeat it correctly flagged
            DRIFT — the capture predates the failsafe cutover, so the
            export still holds old `trig_01Bo7dZxM9xz2hwR36L424Z8` and
            not new `trig_01GK4mjoKBP3yCabn9ux1MB2`, exactly the two
            post-capture deltas the snapshot's own capture_notes record.
            Verbatim output in the PR #335 session card.
Kill-switch: delete this if it proves unreliable over multiple sessions.
=============================================================================

WHAT IT CHECKS (claims come from the status file's routine block; actuals
from the export)
  C1 CLAIMED-FAILSAFE   every failsafe id the heartbeat claims ARMED is
                        present in the export, enabled, and (when the
                        claim names a cron) carries that exact cron.
  C2 UNCLAIMED-SEAT-CRON any OTHER enabled trigger attributed to this
                        seat ("Fleet Manager…") that the heartbeat does
                        not claim = duplicate/orphan → DRIFT (the INC-10
                        double-fire class, seen from the claims side).
  C3 CLAIMED-DELETED    any id the heartbeat says DELETED that is still
                        enabled in the export → DRIFT.
  INFO PENDING-TICKS    pending one-shot send_laters bound to the seat
                        (pacemaker chain), listed for the record — never
                        drift by themselves.

CAPTURE-LAG HONESTY: a DRIFT verdict against an export captured BEFORE the
heartbeat's claims were made may be capture lag, not live drift (today's
founding case). When the export carries a capture instant, the verdict
prints it + its age so you know which you are looking at; live truth needs
a fresh export (list_triggers, ALL pages).

EXIT  0 = OK (claims match export) · 1 = DRIFT · 2 = unreadable input
      (export unreadable/bad schema, status unreadable, or no routine
      claims parseable from the status file).

USAGE
  python3 scripts/verify_routine_state.py                    # committed snapshot
  python3 scripts/verify_routine_state.py --export fresh.json
  python3 scripts/verify_routine_state.py --export flat-array.json \
      --status control/status.md
  python3 scripts/verify_routine_state.py --selfcheck        # offline

Accepted --export shapes (all normalized + id-deduped, first wins):
  * committed snapshot / single page: {"data": [...], ...}
  * page-dump array: [{"data": [...]}, {"data": [...]}, ...]
  * FLAT ARRAY of trigger records: [{"id": "trig_...", ...}, ...]

No third-party deps: stdlib + this repo's gen_roster (schema + lane match).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import gen_roster  # noqa: E402  (sibling module, validate_export / owns_record)

MANAGER_LANE = {"lane": "fleet-manager (this repo)",
                "tokens": ["fleet-manager", "fleet manager"]}

_TRIG_RE = re.compile(r"trig_[A-Za-z0-9]+")
_CRON_NAMED_RE = re.compile(r"cron\s+`([^`]+)`")
_CRON_BARE_RE = re.compile(r"`((?:[\d*,/-]+\s+){4}[\d*,/-]+)`")
_DELETED_RE = re.compile(r"\b(deleted|absent|removed)\b", re.I)
_FAILSAFE_RE = re.compile(r"\bfailsafe\b", re.I)


def fmt(dt: datetime | None) -> str:
    return dt.strftime("%Y-%m-%dT%H:%MZ") if dt else "n/a"


# ----------------------------------------------------------- export side --

class ExportError(Exception):
    """The export file cannot be trusted as a list_triggers export."""


def normalize_export(obj) -> tuple[list[dict], str | None]:
    """Normalize any accepted export shape → (records, captured_at | None).

    Shapes: snapshot/page dict {"data": [...]}; array of page dicts; FLAT
    array of trigger records. Records are id-deduped (first occurrence
    wins — cursor-overlap duplicates) and schema-checked through
    gen_roster.validate_export so a malformed export exits 2, never
    produces a fabricated verdict.
    """
    captured_at = None
    if isinstance(obj, dict):
        if not isinstance(obj.get("data"), list):
            raise ExportError("top-level dict lacks a 'data' list "
                              f"(keys: {sorted(obj.keys())})")
        raw = list(obj["data"])
        ca = obj.get("captured_at")
        captured_at = ca if isinstance(ca, str) else None
    elif isinstance(obj, list):
        if obj and all(isinstance(p, dict) and isinstance(p.get("data"), list)
                       for p in obj):
            raw = [r for p in obj for r in p["data"]]  # page-dump array
        else:
            raw = list(obj)  # flat array of records
    else:
        raise ExportError(f"unsupported top-level type {type(obj).__name__}")
    try:
        return gen_roster.validate_export({"data": raw}), captured_at
    except gen_roster.SchemaError as exc:
        raise ExportError(f"schema mismatch: {exc}") from exc


# ----------------------------------------------------------- status side --

def parse_status_claims(text: str) -> dict:
    """Parse the heartbeat's routine-block claims from status-file text.

    Grammar (control/status.md, wholesale-overwrite heartbeat): any line
    naming a `trig_…` id is a claim about that id —
      * line says DELETED/absent/removed → claimed-deleted;
      * line says failsafe (and not deleted) → claimed-armed, with the
        cron taken from ``cron `…``` (or a bare 5-field backtick cron) on
        the same line or the two continuation lines below;
      * anything else (pacemaker mentions, prose) → mention only.
    Returns {"armed": {id: cron|None}, "deleted": [ids], "mentions": [ids]}.
    """
    armed: dict[str, str | None] = {}
    deleted: list[str] = []
    mentions: list[str] = []
    lines = text.splitlines()
    for i, line in enumerate(lines):
        ids = _TRIG_RE.findall(line)
        if not ids:
            continue
        window = " ".join(lines[i:i + 3])
        m = _CRON_NAMED_RE.search(window) or _CRON_BARE_RE.search(window)
        cron = " ".join(m.group(1).split()) if m else None
        for tid in ids:
            if _DELETED_RE.search(line):
                if tid not in deleted:
                    deleted.append(tid)
            elif _FAILSAFE_RE.search(line):
                if tid not in armed or armed[tid] is None:
                    armed[tid] = cron
            elif tid not in mentions:
                mentions.append(tid)
    # An id both claimed-armed and claimed-deleted on different lines is a
    # contradictory heartbeat; the deleted claim wins (safer: it forces a
    # drift line if the record is still enabled).
    for tid in deleted:
        armed.pop(tid, None)
    return {"armed": armed, "deleted": deleted, "mentions": mentions}


# -------------------------------------------------------------- the diff --

def diff_claims(claims: dict, records: list[dict]) -> list[tuple[str, str]]:
    """Diff status-file claims against export records.

    Returns [(status, line)] with status in {"OK", "DRIFT", "INFO"}.
    """
    out: list[tuple[str, str]] = []
    by_id = {r["id"]: r for r in records}

    # C1 CLAIMED-FAILSAFE — present + enabled + cron matches
    for tid, cron in claims["armed"].items():
        rec = by_id.get(tid)
        if rec is None:
            out.append(("DRIFT", f"C1 claimed failsafe `{tid}` ABSENT from "
                        "the export"))
        elif not rec.get("enabled"):
            out.append(("DRIFT", f"C1 claimed failsafe `{tid}` present but "
                        "NOT enabled in the export"))
        elif cron and rec.get("cron_expression") != cron:
            out.append(("DRIFT", f"C1 claimed failsafe `{tid}` cron "
                        f"mismatch: claimed `{cron}`, export "
                        f"`{rec.get('cron_expression')}`"))
        else:
            note = (f"cron `{cron}` matches" if cron
                    else "no cron claim parsed — presence+enabled only")
            out.append(("OK", f"C1 claimed failsafe `{tid}` present + "
                        f"enabled, {note}"))

    # C2 UNCLAIMED-SEAT-CRON — enabled seat-attributed standing crons the
    # heartbeat does not claim (duplicate/orphan; pacemaker one-shots are
    # INFO below, not this class)
    claimed = set(claims["armed"]) | set(claims["deleted"])
    for r in records:
        if not (r.get("enabled") and r.get("cron_expression")):
            continue
        if not gen_roster.owns_record(MANAGER_LANE, r):
            continue
        if r["id"] not in claimed:
            out.append(("DRIFT", f"C2 enabled seat-named cron `{r['id']}` "
                        f"{r.get('name')!r} `{r.get('cron_expression')}` is "
                        "NOT claimed by the heartbeat — duplicate/orphan; "
                        "verify live, then delete the loser or record it"))

    # C3 CLAIMED-DELETED — still enabled in the export
    for tid in claims["deleted"]:
        rec = by_id.get(tid)
        if rec is not None and rec.get("enabled"):
            out.append(("DRIFT", f"C3 claimed-DELETED `{tid}` "
                        f"{rec.get('name')!r} is still ENABLED in the "
                        "export"))
        else:
            state = "absent from export" if rec is None else "present, disabled"
            out.append(("OK", f"C3 claimed-DELETED `{tid}` — {state}"))

    # INFO PENDING-TICKS — the seat's pacemaker one-shots, for the record
    ticks = [r for r in records
             if r.get("enabled") and r.get("run_once_at")
             and not r.get("ended_reason")
             and gen_roster.owns_record(MANAGER_LANE, r)]
    ticks.sort(key=lambda r: r.get("run_once_at") or "")
    for r in ticks:
        out.append(("INFO", f"pending seat one-shot `{r['id']}` due "
                    f"{(r.get('run_once_at') or '?')[:16]}Z on session "
                    f"`{r.get('persistent_session_id') or '(none)'}`"))
    if not ticks:
        out.append(("INFO", "no pending seat-bound one-shot identifiable "
                    "in the export"))
    return out


# ------------------------------------------------------------- selfcheck --

_SYNTH_STATUS_OK = """\
seat: fleet-manager (coordinator)
- **Fresh seat failsafe ARMED + VERIFIED:** `trig_new1`
  ("Fleet Manager failsafe wake", cron `30 */2 * * *`, bound to the seat).
- **Predecessor failsafe `trig_old1` DELETED** and verified absent.
"""

_SYNTH_NEW = {"id": "trig_new1", "name": "Fleet Manager failsafe wake",
              "created_at": "2026-07-18T20:58:28Z", "enabled": True,
              "cron_expression": "30 */2 * * *",
              "next_run_at": "2026-07-18T22:33:20Z"}
_SYNTH_OTHER = {"id": "trig_sib1", "name": "Websites failsafe wake",
                "created_at": "t", "enabled": True,
                "cron_expression": "45 */2 * * *",
                "next_run_at": "2026-07-18T22:45:00Z"}


def selfcheck() -> int:
    """Offline assertions over the parse + diff wiring. Exit 0 on pass."""
    fails: list[str] = []

    def ok(cond, msg):
        if not cond:
            fails.append(msg)

    claims = parse_status_claims(_SYNTH_STATUS_OK)
    ok(claims["armed"] == {"trig_new1": "30 */2 * * *"},
       f"armed claim parses id + cron ({claims['armed']})")
    ok(claims["deleted"] == ["trig_old1"], "deleted claim parses")

    def drifts(recs):
        return [l for s, l in diff_claims(claims, recs) if s == "DRIFT"]

    ok(not drifts([_SYNTH_NEW, _SYNTH_OTHER]),
       "matching export yields zero drift (sibling-seat cron ignored)")
    ok(any("ABSENT" in d for d in drifts([_SYNTH_OTHER])),
       "missing claimed failsafe drifts C1")
    ok(any("NOT enabled" in d
           for d in drifts([{k: v for k, v in _SYNTH_NEW.items()
                             if k != "enabled"}])),
       "disabled claimed failsafe drifts C1")
    ok(any("cron mismatch" in d
           for d in drifts([dict(_SYNTH_NEW, cron_expression="0 */2 * * *")])),
       "cron mismatch drifts C1")
    stale_old = {"id": "trig_old1", "name": "Fleet Manager failsafe wake",
                 "created_at": "t", "enabled": True,
                 "cron_expression": "30 */2 * * *",
                 "next_run_at": "2026-07-18T20:30:00Z"}
    ds = drifts([_SYNTH_NEW, stale_old])
    ok(any(d.startswith("C3") for d in ds),
       "claimed-deleted still enabled drifts C3")
    ok(not any(d.startswith("C2") for d in ds),
       "a claimed-deleted id is not double-flagged as C2 orphan")
    orphan = dict(stale_old, id="trig_dupX")
    ok(any(d.startswith("C2") for d in drifts([_SYNTH_NEW, orphan])),
       "unclaimed enabled seat cron drifts C2 (duplicate/orphan)")
    tick = {"id": "trig_t1", "name": "send_later 2026-07-18T21:14Z #ab",
            "created_at": "t", "enabled": True,
            "run_once_at": "2026-07-18T21:14:00Z",
            "persistent_session_id": "session_x",
            "job_config": {"ccr": {"events": [{"data": {"message": {
                "content": "fleet-manager pacemaker tick"}}}]}}}
    infos = [l for s, l in diff_claims(claims, [_SYNTH_NEW, tick])
             if s == "INFO"]
    ok(any("trig_t1" in l for l in infos), "seat pacemaker tick listed INFO")

    # shape normalization: flat array == page dump == snapshot dict
    flat, _ = normalize_export([_SYNTH_NEW, _SYNTH_OTHER])
    pages, _ = normalize_export([{"data": [_SYNTH_NEW], "has_more": True},
                                 {"data": [_SYNTH_OTHER, _SYNTH_NEW]}])
    snap, ca = normalize_export({"captured_at": "2026-07-18T20:42:05Z",
                                 "data": [_SYNTH_NEW, _SYNTH_OTHER]})
    ok([r["id"] for r in flat] == [r["id"] for r in pages]
       == [r["id"] for r in snap] == ["trig_new1", "trig_sib1"],
       "all three shapes normalize + dedupe to the same records")
    ok(ca == "2026-07-18T20:42:05Z", "snapshot captured_at surfaces")
    for bad in (42, {"nope": []}, [{"data": "x"}, {"data": []}]):
        try:
            normalize_export(bad)
            fails.append(f"bad shape {bad!r} did not raise")
        except ExportError:
            pass
    ok(parse_status_claims("no routine ids here") ==
       {"armed": {}, "deleted": [], "mentions": []},
       "claimless status parses to empty claims")

    for msg in fails:
        print(f"SELFCHECK FAIL: {msg}", file=sys.stderr)
    print(f"selfcheck: {'FAIL' if fails else 'PASS'} ({len(fails)} failure(s))")
    return 1 if fails else 0


# ------------------------------------------------------------------ main --

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    root = gen_roster.repo_root()
    ap.add_argument("--export",
                    default=os.path.join(root, "telemetry",
                                         "triggers-snapshot.json"),
                    help="list_triggers export: committed snapshot, page-dump "
                    "JSON, or a FLAT array of records (default: the "
                    "committed snapshot)")
    ap.add_argument("--status",
                    default=os.path.join(root, "control", "status.md"),
                    help="heartbeat file whose routine claims to verify "
                    "(default: control/status.md)")
    ap.add_argument("--selfcheck", action="store_true",
                    help="run offline assertions and exit")
    args = ap.parse_args(argv)

    if args.selfcheck:
        return selfcheck()

    try:
        with open(args.export, encoding="utf-8") as fh:
            payload = json.load(fh)
        records, captured_at = normalize_export(payload)
    except (OSError, json.JSONDecodeError, ExportError) as exc:
        print(f"VERDICT: UNREADABLE — export {args.export}: {exc}")
        return 2
    try:
        with open(args.status, encoding="utf-8") as fh:
            claims = parse_status_claims(fh.read())
    except OSError as exc:
        print(f"VERDICT: UNREADABLE — status {args.status}: {exc}")
        return 2
    if not claims["armed"] and not claims["deleted"]:
        print(f"VERDICT: UNREADABLE — no routine claims (armed failsafe / "
              f"deleted id) parseable from {args.status}")
        return 2

    now = datetime.now(timezone.utc)
    cap_dt = gen_roster.parse_when(captured_at or "")
    enabled = [r for r in records if r.get("enabled")]
    print("=" * 72)
    print(f"ROUTINE STATE — {len(records)} records ({len(enabled)} enabled) "
          f"vs {os.path.relpath(args.status, root)}")
    if cap_dt:
        print(f"export capture instant {fmt(cap_dt)} "
              f"({(now - cap_dt).total_seconds() / 3600:.1f}h before "
              f"now={fmt(now)})")
    else:
        print(f"export carries no capture instant · now={fmt(now)}")
    print("=" * 72)
    results = diff_claims(claims, records)
    for status, line in results:
        print(f"[{status:<5}] {line}")
    print("-" * 72)
    n_drift = sum(1 for s, _ in results if s == "DRIFT")
    if n_drift:
        print(f"VERDICT: DRIFT — {n_drift} mismatch(es) between the "
              "heartbeat's routine claims and the export."
              + (" Capture predates 'now' — if the claims are NEWER than "
                 f"the {fmt(cap_dt)} capture this may be capture lag, not "
                 "live drift: refresh the export (list_triggers, ALL pages) "
                 "and re-run for live truth." if cap_dt else
                 " Export carries no capture instant — confirm it is "
                 "fresher than the heartbeat before acting."))
        return 1
    print("VERDICT: OK — heartbeat routine claims match the export "
          f"({sum(1 for s, _ in results if s == 'OK')} claim(s) verified).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
