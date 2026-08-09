#!/usr/bin/env python3
"""A/B one kit function across two vendored dists — the banked one and the live one.

WHY THIS EXISTS
    `upgrade` banks the outgoing dist to `.substrate/backup/bootstrap-<old>.py`
    before overwriting `bootstrap.py`. That means every upgrade leaves both
    versions on disk, and any behaviour change is directly measurable instead of
    inferred from a changelog. On fm #833 this was the ONLY method that found
    *regressions* rather than long-standing holes. The independent fm #835 review
    extended it to every recorded defect: five behaviours are new in v1.20.2 and
    two persist across both dists. One old red is right for the wrong reason, so
    raw hit counts remain evidence to interpret, never the interpretation itself.

    It was first written as a fenced code block inside
    `docs/findings/2026-08-09-substrate-kit-defects.md`. That was wrong in the
    same way the section it sat in complains about: a reproduction you have to
    copy-paste is not runnable, and one typo away from proving nothing. Raised
    by owner-review.

USAGE
    python3 tools/ab_kit_scan.py                     # auto-pick newest bank
    python3 tools/ab_kit_scan.py --old <path>        # pin the old dist
    python3 tools/ab_kit_scan.py --case "some text"  # add an ad-hoc case

    Exit 0 always — this is an instrument, not a gate. It reports; you judge.

READING THE OUTPUT
    A `DIFFERS` row is a behaviour change between the two releases. That is not
    automatically a bug: v1.20.2 legitimately FIXED a false positive (the
    same-line quoted repudiation). Decide per row which direction is right, and
    remember which direction is dangerous — a wall that stops being caught is
    silent, while prose that starts being rejected announces itself.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import subprocess
import sys
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Each scanner case is (label, text, what-a-correct-scanner-should-do,
# scan-as-render-path). Defect 5 is a command/template contract rather than a
# `scan_text` case and is probed separately below.
# `True` = should be flagged as a standing wall; `False` = should be clear.
SCAN_CASES: list[tuple[str, str, bool, bool]] = [
    ("bare wall (control)",
     "Agents cannot merge pull requests.", True, False),
    ("authored prose in render file (kit defect 1)",
     "Never edit this file: regenerate with python3 bootstrap.py seat-digest\n"
     "Agents cannot merge pull requests.", True, True),
    ("wall after 'because' (kit defect 7)",
     "The failure does not reproduce because agents cannot merge pull requests.", True, False),
    ("second assertion after repudiated quote (kit defect 2)",
     '"agents cannot merge" was superseded, agents cannot merge', True, False),
    ("valid repudiation, conjunction (kit defect 6)",
     'The "agents cannot merge" rule is false and no longer applies.', False, False),
    ("valid repudiation, same line",
     'The "agents cannot merge" rule was superseded.', False, False),
    ("deploy wall (kit defect 3 — family never matches)",
     "Merging is not walled, agents cannot deploy", True, False),
    ("cue across a fence (kit defect 4)",
     'The rule is "agents cannot merge"\n```\n'
     'This example was superseded\n```', True, False),
]


# Each dist runs in its OWN SUBPROCESS. The first version loaded both into one
# process under different sys.modules names, which was inherited from an ad-hoc
# scratchpad probe rather than chosen -- and `exec_module` runs a dist's entire
# module body, so any global side effect from one could silently corrupt the
# other's numbers. Every row here would still print, just meaninglessly. The
# risk was never measured, so it is designed out instead: one dist per process
# cannot share state by construction. Verified equal to the in-process results
# before the switch, so the published numbers are unaffected.
_CHILD = r"""
import importlib.util, inspect, json, sys
path, cases = sys.argv[1], json.loads(sys.argv[2])
spec = importlib.util.spec_from_file_location("kit_under_test", path)
mod = importlib.util.module_from_spec(spec)
sys.modules["kit_under_test"] = mod
spec.loader.exec_module(mod)
if not hasattr(mod, "scan_text"):
    print(json.dumps({"missing": True})); raise SystemExit(0)
supports_render_path = "is_render_path" in inspect.signature(mod.scan_text).parameters
hits = []
for case in cases:
    kwargs = {"is_render_path": True} if (case["render_path"] and supports_render_path) else {}
    hits.append(len(mod.scan_text(case["text"], **kwargs)))
print(json.dumps({"hits": hits, "supports_render_path": supports_render_path}))
"""


def scan_in_subprocess(path: str, cases: list[dict]) -> dict:
    """Run `scan_text` cases inside a fresh interpreter. Never raises."""
    try:
        out = subprocess.run([sys.executable, "-c", _CHILD, path, json.dumps(cases)],
                             capture_output=True, text=True, timeout=120)
    except Exception as exc:  # noqa: BLE001 — an instrument never breaks a session
        return {"error": f"{type(exc).__name__}: {exc}"}
    if out.returncode != 0:
        return {"error": (out.stderr or "").strip().split("\n")[-1][:160] or f"exit {out.returncode}"}
    try:
        return json.loads(out.stdout.strip().split("\n")[-1])
    except Exception:  # noqa: BLE001
        return {"error": "unparseable child output"}


def _vkey(path: str) -> tuple:
    """Sort banks by SEMVER, not lexicographically.

    The first version of this picked `bootstrap-1.9.0.py` over
    `bootstrap-1.20.1.py`, because as strings "1.9.0" > "1.20.1" — and 1.9.0
    predates `scan_text` entirely, so every case errored. Caught by running the
    harness instead of shipping it. A version sort that is really a string sort
    is silently wrong for exactly one release in twenty, which is the worst
    frequency for noticing.
    """
    m = re.search(r"bootstrap-(\d+(?:\.\d+)*)", os.path.basename(path))
    return tuple(int(n) for n in m.group(1).split(".")) if m else (-1,)


def newest_bank() -> str | None:
    banks = sorted(glob.glob(os.path.join(REPO, ".substrate", "backup", "bootstrap-*.py")), key=_vkey)
    return banks[-1] if banks else None


def probe_skills_install_contract(path: str) -> dict:
    """Run the documented defect-5 command in a fresh adopter root.

    The bad instruction is an embedded template contract, not scanner input.
    Count both the staged output and the live destination so a successful
    command cannot be mistaken for a successful install.
    """
    try:
        dist_text = open(path, encoding="utf-8").read()
        with tempfile.TemporaryDirectory(prefix="ab-kit-skills-") as target:
            init = subprocess.run(
                [sys.executable, path, "init", "--target", target],
                capture_output=True, text=True, timeout=120,
            )
            build = subprocess.run(
                [sys.executable, path, "skills", "--build", "--target", target],
                capture_output=True, text=True, timeout=120,
            )
            staged = glob.glob(os.path.join(target, ".substrate", "skills", "*", "SKILL.md"))
            live = glob.glob(os.path.join(target, ".claude", "skills", "*", "SKILL.md"))
        return {
            "claim": dist_text.count("python3 bootstrap.py skills --build"),
            "init": init.returncode,
            "build": build.returncode,
            "staged": len(staged),
            "live": len(live),
        }
    except Exception as exc:  # noqa: BLE001 — an instrument never breaks a session
        return {"error": f"{type(exc).__name__}: {exc}"}


def _skills_result(result: dict) -> str:
    if result.get("error"):
        return f"ERROR({result['error'][:60]})"
    return (f"claim={result['claim']},init={result['init']},build={result['build']},"
            f"staged={result['staged']},live={result['live']}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--old", help="path to the banked dist (default: newest in .substrate/backup/)")
    ap.add_argument("--new", default=os.path.join(REPO, "bootstrap.py"), help="path to the live dist")
    ap.add_argument("--case", action="append", default=[], help="extra text to scan (repeatable)")
    args = ap.parse_args(argv)

    old = args.old or newest_bank()
    if not old or not os.path.exists(old):
        print("no banked dist found under .substrate/backup/ — nothing to compare against.")
        print("(a bank appears the first time `upgrade` runs in this repo)")
        return 0

    cases = list(SCAN_CASES) + [
        (f"ad-hoc {i + 1}", text, None, False)
        for i, text in enumerate(args.case)
    ]

    print(f"old: {os.path.relpath(old, REPO)}")
    print(f"new: {os.path.relpath(args.new, REPO)}\n")

    payload = [
        {"text": case_text, "render_path": render_path}
        for _, case_text, _, render_path in cases
    ]
    res_old = scan_in_subprocess(old, payload)
    res_new = scan_in_subprocess(args.new, payload)

    for who, res in (("old", res_old), ("new", res_new)):
        if res.get("error"):
            print(f"{who} dist failed to scan: {res['error']}")
            return 0
        if res.get("missing"):
            print(f"`scan_text` is absent from the {who} dist — that version "
                  f"predates the function; pick a newer bank with --old.")
            return 0

    differs = 0
    for i, (label, _case_text, expected, _render_path) in enumerate(cases):
        a, b = res_old["hits"][i], res_new["hits"][i]
        flag = "DIFFERS" if a != b else ""
        if a != b:
            differs += 1
        want = "" if expected is None else ("  want=flag" if expected else "  want=clear")
        print(f"  {label:<52} old={a} new={b}  {flag}{want}")

    skills_old = probe_skills_install_contract(old)
    skills_new = probe_skills_install_contract(args.new)
    print("  skills install contract (kit defect 5)")
    print(f"    old: {_skills_result(skills_old)}")
    print(f"    new: {_skills_result(skills_new)}")
    print("    want: command exits 0 AND live>0; claim should not describe staging as install")

    print(f"\n{differs} scanner behaviour change(s) between the two dists.")
    print("Seven defect probes ran: six scanner defects plus one command/template contract.")
    if differs:
        print("A DIFFERS row is a change, not automatically a bug — decide per row.")
        print("A wall that stops being caught is SILENT; prose that starts being")
        print("rejected announces itself. Rank the silent ones first.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
