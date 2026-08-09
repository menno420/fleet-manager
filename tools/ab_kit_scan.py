#!/usr/bin/env python3
"""A/B one kit function across two vendored dists — the banked one and the live one.

WHY THIS EXISTS
    `upgrade` banks the outgoing dist to `.substrate/backup/bootstrap-<old>.py`
    before overwriting `bootstrap.py`. That means every upgrade leaves both
    versions on disk, and any behaviour change is directly measurable instead of
    inferred from a changelog. On fm #833 this is the ONLY method that found
    *regressions* rather than long-standing holes: two of v1.20.2's five
    false-wall clearing relaxations mis-fire, one in each direction, and neither
    is mentioned in the release notes.

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

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Each case is (label, text, what-a-correct-scanner-should-do).
# `True` = should be flagged as a standing wall; `False` = should be clear.
CASES: list[tuple[str, str, bool]] = [
    ("bare wall (control)",
     "Agents cannot merge pull requests.", True),
    ("wall after 'because' (kit defect 7)",
     "The failure does not reproduce because agents cannot merge pull requests.", True),
    ("second assertion after repudiated quote (kit defect 2)",
     '"agents cannot merge" was superseded, agents cannot merge', True),
    ("valid repudiation, conjunction (kit defect 6)",
     'The "agents cannot merge" rule is false and no longer applies.', False),
    ("valid repudiation, same line",
     'The "agents cannot merge" rule was superseded.', False),
    ("deploy wall (kit defect 3 — family never matches)",
     "Merging is not walled, agents cannot deploy", True),
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
import importlib.util, json, sys
path, cases = sys.argv[1], json.loads(sys.argv[2])
spec = importlib.util.spec_from_file_location("kit_under_test", path)
mod = importlib.util.module_from_spec(spec)
sys.modules["kit_under_test"] = mod
spec.loader.exec_module(mod)
if not hasattr(mod, "scan_text"):
    print(json.dumps({"missing": True})); raise SystemExit(0)
print(json.dumps({"hits": [len(mod.scan_text(t)) for t in cases]}))
"""


def scan_in_subprocess(path: str, texts: list[str]) -> dict:
    """Run `scan_text` over `texts` inside a fresh interpreter. Never raises."""
    try:
        out = subprocess.run([sys.executable, "-c", _CHILD, path, json.dumps(texts)],
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

    cases = list(CASES) + [(f"ad-hoc {i + 1}", t, None) for i, t in enumerate(args.case)]

    print(f"old: {os.path.relpath(old, REPO)}")
    print(f"new: {os.path.relpath(args.new, REPO)}\n")

    texts = [t for _, t, _ in cases]
    res_old = scan_in_subprocess(old, texts)
    res_new = scan_in_subprocess(args.new, texts)

    for who, res in (("old", res_old), ("new", res_new)):
        if res.get("error"):
            print(f"{who} dist failed to scan: {res['error']}")
            return 0
        if res.get("missing"):
            print(f"`scan_text` is absent from the {who} dist — that version "
                  f"predates the function; pick a newer bank with --old.")
            return 0

    differs = 0
    for i, (label, text, expected) in enumerate(cases):
        a, b = res_old["hits"][i], res_new["hits"][i]
        flag = "DIFFERS" if a != b else ""
        if a != b:
            differs += 1
        want = "" if expected is None else ("  want=flag" if expected else "  want=clear")
        print(f"  {label:<52} old={a} new={b}  {flag}{want}")

    print(f"\n{differs} behaviour change(s) between the two dists.")
    if differs:
        print("A DIFFERS row is a change, not automatically a bug — decide per row.")
        print("A wall that stops being caught is SILENT; prose that starts being")
        print("rejected announces itself. Rank the silent ones first.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
