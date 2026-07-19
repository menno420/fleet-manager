#!/usr/bin/env python3
"""emit_routine_claims.py — write-side updater for the routine-claims fence.

================================ PROVENANCE ================================
Why added : 2026-07-19 (PR #341 review flag → the PR #349 plan's below-the-
            line "write-side fence emitter" item). The ```json routine-claims```
            fence in control/status.md is hand-edited JSON at every heartbeat,
            and its volatile fields (`next_run_at`, `last_fired`, `updated`)
            demonstrably go stale by hand — the read side got tooling in
            PR #335/#339 (verify_routine_state.py), the write side had none.
            This script IS the write side: it rewrites the fence from CLI
            args (unspecified fields carry forward unchanged), validates the
            result round-trips through verify_routine_state.py's OWN fence
            parser before writing a byte, and refuses loudly (exit 2) when
            the file doesn't hold exactly one tagged fence. Heartbeat
            writers call this instead of editing JSON in place.
Date      : 2026-07-19 (build-slice worker, model: fable-5, dispatched by
            the coordinator; fleet-manager PR #357)
Reliability: unverified — confirm its output against ground truth a few
            times across sessions before trusting it.
Kill-switch: delete this if it proves unreliable over multiple sessions.
=============================================================================

USAGE
  python3 scripts/emit_routine_claims.py --dry-run          # print, no write
  python3 scripts/emit_routine_claims.py \
      --failsafe-id trig_X --cron "30 */2 * * *" \
      --next-run 2026-07-19T12:31:48Z --last-fired 2026-07-19T10:32:09Z \
      --deleted trig_OLD1 --deleted trig_OLD2 \
      --pacemaker-cadence 30 --pacemaker-note "chain healthy" \
      --updated 2026-07-19T11:05Z
  python3 scripts/emit_routine_claims.py --selfcheck        # offline

SEMANTICS
  * Unspecified args carry the fence's current values forward unchanged;
    `--updated` alone is a legitimate "claims re-verified, nothing moved"
    heartbeat bump. `--updated` defaults to now (UTC, minute precision).
  * `--deleted` is wholesale-overwrite like the heartbeat itself: passing it
    at least once REPLACES the whole deleted list; omitting it keeps the
    current list.
  * The result must round-trip through verify_routine_state.parse_fence_claims
    (the consumer's parser) or nothing is written and the exit is 2.
  * Exactly ONE tagged fence must exist — zero or multiple is exit 2 (this
    tool updates a contract fence, it never creates or disambiguates one).
  * The fence's failsafe must be the single-object shape to be CLI-editable;
    a list-of-failsafes fence is refused (exit 2) — edit that rarity by hand.

EXIT  0 = written (or --dry-run OK) · 2 = refused, file untouched.

No third-party deps: stdlib + this repo's verify_routine_state (parser).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import verify_routine_state as vrs  # noqa: E402  (sibling: fence contract)


class EmitError(Exception):
    """The fence cannot be safely rewritten; the file must stay untouched."""


def locate_fence(text: str) -> tuple[int, int, list[str]]:
    """Find THE tagged fence → (open_line_idx, close_line_idx, body_lines).

    Mirrors verify_routine_state.parse_fence_claims's detection (same
    open/close/info-string rules) but keeps line positions, which the
    read-side parser doesn't need. Raises EmitError unless exactly one
    tagged fence with a closing line exists.
    """
    lines = text.splitlines()
    found: list[tuple[int, int]] = []
    open_idx: int | None = None
    tagged = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if open_idx is None:
            if stripped.startswith("```"):
                info = stripped.lstrip("`").strip()
                tagged = vrs.FENCE_TAG in info.split()
                open_idx = i
        elif stripped.startswith("```"):
            if tagged:
                found.append((open_idx, i))
            open_idx = None
    if tagged and open_idx is not None:
        raise EmitError(f"`{vrs.FENCE_TAG}` fence opened at line "
                        f"{open_idx + 1} is never closed")
    if len(found) != 1:
        raise EmitError(f"{len(found)} `{vrs.FENCE_TAG}` fences found — "
                        "this tool updates exactly one; create or prune by "
                        "hand first")
    a, b = found[0]
    return a, b, lines[a + 1:b]


def apply_args(obj: dict, args: argparse.Namespace) -> tuple[dict, list[str]]:
    """Apply CLI args over the parsed fence object → (new_obj, changed keys).

    Carries every unspecified field forward, preserving key order.
    """
    if not isinstance(obj, dict):
        raise EmitError("fence body must be a single JSON object, got "
                        f"{type(obj).__name__}")
    new = json.loads(json.dumps(obj))  # deep copy, order preserved
    changed: list[str] = []

    new["updated"] = args.updated
    if new["updated"] != obj.get("updated"):
        changed.append("updated")

    fs_args = {"id": args.failsafe_id, "cron": args.cron,
               "next_run_at": args.next_run, "last_fired": args.last_fired,
               "state": args.state}
    if any(v is not None for v in fs_args.values()):
        fs = new.get("failsafe")
        if isinstance(fs, list):
            raise EmitError("fence carries a LIST of failsafes — CLI edit "
                            "supports the single-object shape only; edit the "
                            "list by hand")
        if not isinstance(fs, dict):
            fs = {}
            new["failsafe"] = fs
        for key, val in fs_args.items():
            if val is not None and fs.get(key) != val:
                fs[key] = val
                changed.append(f"failsafe.{key}")

    if args.deleted:  # wholesale-overwrite semantics (see module docstring)
        deleted = list(dict.fromkeys(args.deleted))
        if new.get("deleted") != deleted:
            new["deleted"] = deleted
            changed.append("deleted")

    if args.pacemaker_cadence is not None or args.pacemaker_note is not None:
        pm = new.get("pacemaker")
        if not isinstance(pm, dict):
            pm = {"mode": "send_later"}
            new["pacemaker"] = pm
        if (args.pacemaker_cadence is not None
                and pm.get("cadence_minutes") != args.pacemaker_cadence):
            pm["cadence_minutes"] = args.pacemaker_cadence
            changed.append("pacemaker.cadence_minutes")
        if (args.pacemaker_note is not None
                and pm.get("note") != args.pacemaker_note):
            pm["note"] = args.pacemaker_note
            changed.append("pacemaker.note")
    return new, changed


def render(text: str, new_obj: dict) -> tuple[str, str]:
    """Rewrite the fence body in TEXT → (new_full_text, new_fence_block).

    The rewritten full text is round-tripped through the consumer's parser
    (verify_routine_state.parse_fence_claims) before being returned; a
    result that parser rejects raises EmitError and nothing is written.
    """
    a, b, _ = locate_fence(text)
    lines = text.splitlines()
    body = json.dumps(new_obj, indent=2, ensure_ascii=False)
    new_lines = lines[:a + 1] + body.splitlines() + lines[b:]
    trailing_nl = "\n" if text.endswith("\n") else ""
    new_text = "\n".join(new_lines) + trailing_nl
    try:
        claims = vrs.parse_fence_claims(new_text)
    except vrs.FenceError as exc:
        raise EmitError(f"round-trip through verify_routine_state's fence "
                        f"parser FAILED — refusing to write: {exc}") from exc
    if claims is None:
        raise EmitError("round-trip lost the fence entirely — refusing to "
                        "write")
    fence_block = "\n".join(new_lines[a:a + 1]) + "\n" + body + "\n" + lines[b]
    return new_text, fence_block


# ------------------------------------------------------------- selfcheck --

_SYNTH = (
    "prose above\n"
    "```json routine-claims\n"
    '{"seat": "fleet-manager (coordinator)", "updated": "2026-07-19T00:00Z",\n'
    ' "failsafe": {"id": "trig_A", "cron": "30 */2 * * *",\n'
    '              "next_run_at": "2026-07-19T02:31:48Z",\n'
    '              "last_fired": "2026-07-19T00:32:09Z", "state": "armed"},\n'
    ' "deleted": ["trig_OLD"],\n'
    ' "pacemaker": {"mode": "send_later", "cadence_minutes": 30, '
    '"note": "n"}}\n'
    "```\n"
    "prose below\n"
)


def _ns(**kw) -> argparse.Namespace:
    base = dict(failsafe_id=None, cron=None, next_run=None, last_fired=None,
                state=None, deleted=[], pacemaker_cadence=None,
                pacemaker_note=None, updated="2026-07-19T11:00Z")
    base.update(kw)
    return argparse.Namespace(**base)


def selfcheck() -> int:
    fails: list[str] = []

    def ok(cond, msg):
        if not cond:
            fails.append(msg)

    _, _, body = locate_fence(_SYNTH)
    obj = json.loads("\n".join(body))

    # updated-only bump: single change, everything else carried forward
    new, changed = apply_args(obj, _ns())
    ok(changed == ["updated"], f"updated-only bump changes exactly it "
       f"({changed})")
    ok(new["failsafe"]["last_fired"] == "2026-07-19T00:32:09Z"
       and new["deleted"] == ["trig_OLD"], "unspecified fields carry forward")

    # volatile-field bump + deleted overwrite
    new, changed = apply_args(obj, _ns(
        next_run="2026-07-19T04:31:48Z", last_fired="2026-07-19T02:32:09Z",
        deleted=["trig_OLD", "trig_OLD2"]))
    ok("failsafe.next_run_at" in changed and "failsafe.last_fired" in changed
       and "deleted" in changed, f"volatile bump tracked ({changed})")
    ok(new["deleted"] == ["trig_OLD", "trig_OLD2"],
       "--deleted wholesale-overwrites the list")
    ok(list(new.keys()) == list(obj.keys()), "key order preserved")

    # render round-trips through the consumer's parser
    text, block = render(_SYNTH, new)
    claims = vrs.parse_fence_claims(text)
    ok(claims is not None
       and claims["armed"] == {"trig_A": "30 */2 * * *"}
       and claims["deleted"] == ["trig_OLD", "trig_OLD2"],
       "rendered text parses to the new claims")
    ok(text.startswith("prose above\n") and text.endswith("prose below\n"),
       "surrounding prose untouched")
    ok(block.startswith("```json routine-claims") and block.endswith("```"),
       "fence block prints whole")

    # a bad state is refused by the round-trip, file-untouched path
    try:
        render(_SYNTH, dict(obj, failsafe=dict(obj["failsafe"],
                                               state="disarmed")))
        fails.append("bad failsafe state did not refuse")
    except EmitError:
        pass

    # zero / two fences refused; unclosed fence refused
    for label, bad in (
            ("zero fences", "no fence here\n"),
            ("two fences", _SYNTH + _SYNTH),
            ("unclosed fence", "```json routine-claims\n{}\n"),
    ):
        try:
            locate_fence(bad)
            fails.append(f"{label} did not refuse")
        except EmitError:
            pass

    # list-shaped failsafe refused for CLI edit
    try:
        apply_args(dict(obj, failsafe=[obj["failsafe"]]),
                   _ns(last_fired="2026-07-19T02:32:09Z"))
        fails.append("list-shaped failsafe did not refuse")
    except EmitError:
        pass

    for msg in fails:
        print(f"SELFCHECK FAIL: {msg}", file=sys.stderr)
    print(f"selfcheck: {'FAIL' if fails else 'PASS'} ({len(fails)} failure(s))")
    return 1 if fails else 0


# ------------------------------------------------------------------ main --

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    root = vrs.gen_roster.repo_root()
    ap.add_argument("--status",
                    default=os.path.join(root, "control", "status.md"),
                    help="heartbeat file holding the routine-claims fence "
                    "(default: control/status.md)")
    ap.add_argument("--failsafe-id", help="failsafe trigger id (trig_…)")
    ap.add_argument("--cron", help="failsafe cron expression")
    ap.add_argument("--next-run", help="failsafe next_run_at (UTC instant)")
    ap.add_argument("--last-fired", help="failsafe last_fired (UTC instant)")
    ap.add_argument("--state", help="failsafe state (contract: 'armed')")
    ap.add_argument("--deleted", action="append", default=[],
                    help="claimed-deleted trigger id; repeatable — passing "
                    "it REPLACES the whole deleted list")
    ap.add_argument("--pacemaker-cadence", type=int,
                    help="pacemaker cadence_minutes")
    ap.add_argument("--pacemaker-note", help="pacemaker note text")
    ap.add_argument("--updated",
                    default=datetime.now(timezone.utc)
                    .strftime("%Y-%m-%dT%H:%MZ"),
                    help="claims-verified instant (default: now, UTC)")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the new fence, write nothing")
    ap.add_argument("--selfcheck", action="store_true",
                    help="run offline assertions and exit")
    args = ap.parse_args(argv)

    if args.selfcheck:
        return selfcheck()

    try:
        with open(args.status, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        print(f"REFUSED — cannot read {args.status}: {exc}")
        return 2
    try:
        _, _, body = locate_fence(text)
        try:
            obj = json.loads("\n".join(body))
        except json.JSONDecodeError as exc:
            raise EmitError(f"current fence body is not valid JSON: {exc}")
        new_obj, changed = apply_args(obj, args)
        new_text, fence_block = render(text, new_obj)
    except EmitError as exc:
        print(f"REFUSED — {exc}")
        return 2

    rel = os.path.relpath(args.status, root)
    print(f"fence in {rel} — changed: "
          + (", ".join(changed) if changed else "nothing (values identical)"))
    print(fence_block)
    if args.dry_run:
        print("DRY-RUN — nothing written.")
        return 0
    with open(args.status, "w", encoding="utf-8") as fh:
        fh.write(new_text)
    print(f"WROTE {rel} (round-trip verified against "
          "verify_routine_state.parse_fence_claims).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
