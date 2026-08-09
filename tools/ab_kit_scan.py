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
import re
import importlib.util
import os
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


def load(path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


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

    try:
        mo = load(old, "kit_old")
        mn = load(args.new, "kit_new")
    except Exception as exc:  # noqa: BLE001 — an instrument never breaks a session
        print(f"could not load both dists: {type(exc).__name__}: {exc}")
        return 0

    # A bank old enough to predate the function is a real and boring case: say so
    # once, plainly, instead of erroring per case (the first version did the
    # latter, which read like six failures rather than one wrong input).
    missing = [n for n, m in (("old", mo), ("new", mn)) if not hasattr(m, "scan_text")]
    if missing:
        print(f"`scan_text` is absent from the {' and '.join(missing)} dist — "
              f"that version predates the function; pick a newer bank with --old.")
        return 0

    differs = 0
    for label, text, expected in cases:
        try:
            a = len(mo.scan_text(text))
            b = len(mn.scan_text(text))
        except Exception as exc:  # noqa: BLE001
            print(f"  {label:<52} ERROR {type(exc).__name__}: {exc}")
            continue
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
