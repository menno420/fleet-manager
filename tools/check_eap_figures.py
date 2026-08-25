#!/usr/bin/env python3
"""Do the documents still state the figures the mail actually has?

WHY THIS EXISTS. `render_eap_mail.py --count` computes the authoritative number,
but computing is not enforcing: on 2026-08-25 the count was hard-coded into FIVE
living documents — the draft, `docs/owner-queue.md`, `docs/current-state.md`, the
program's § 7 ledger and the session card — so a single re-wording of the mail
silently falsified all of them at once (`@codex`, fm #946). That happened during
the very session that added the tool: a four-word P1 fix to ask 5 moved the mail
from 1,477 to 1,481 and left nine stale figures behind. This check caught them.

It reads the number OUT OF the prose with a capture group and compares it against
the computed value. It does NOT trust that a document containing "1,481"
therefore agrees — an earlier version of this check searched for the literal it
expected and compared it to itself, an `X != X` condition that could never fire.

TWO FAILURE MODES, both reported, because a check that cannot fail is worse than
no check:
  * MISMATCH          — the prose states a number the mail does not have.
  * PATTERN NEVER MATCHED — the phrasing moved, so that claim is now unguarded.
Every pattern uses `\\s+` for spaces: the docs hard-wrap at ~76 columns and a
literal space cannot cross a line break.

Every run also re-runs itself against a deliberately corrupted copy and prints
whether the corruption fired, so the exit code means something.

USAGE
    python3 tools/check_eap_figures.py     # exit 0 = docs agree with the mail
"""
from __future__ import annotations
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import render_eap_mail as R                                    # noqa: E402

CARD = ROOT / ".sessions/2026-08-25-e1-owner-revision-pass.md"
BASE = "9b2d83a:docs/planning/2026-08-24-final-eap-email-draft.md"
CENSUS_FIX = ", and **seven were created after the program closed**"

CLAIMS = [
    (r"Part\s+2\s+was\s+([\d,]+)\s+words\s+at",                 "before"),
    (r"9b2d83a`,\s+([\d,]+)\s+after\s+the\s+cut",               "cut_only"),
    (r"and\s+([\d,]+)\s+as\s+it\s+now\s+stands",                "now"),
    (r"d\s+·\s+([\d,]+)\s+words\s+is\s+about\s+three\s+pages",  "now"),
    (r"measured\s+([\d,]+),\s+and\s+those\s+two",               "floor"),
    (r"carries\s+\*\*([\d,]+)\s+bold",                          "bold"),
    (r"bold\s+and\s+([\d,]+)\s+italic\s+spans",                 "italic"),
    (r"the\s+route\s+lands\s+at\s+\*\*([\d,]+)\*\*",            "cut_only"),
]


def computed() -> dict:
    md = R.DRAFT.read_text(encoding="utf-8")
    mw = lambda ls: sum(1 for w in R.to_text(ls).split() if re.search(r"[A-Za-z0-9]", w))
    N = R.extract(md)
    base = subprocess.run(["git", "show", BASE], cwd=ROOT,
                          capture_output=True, text=True, check=True).stdout
    idx = lambda p: next(k for k, l in enumerate(N) if l.startswith(p))
    gp, so, ev = (idx("**What genuinely worked"), idx("**A standing offer"),
                  idx("Everything above is public"))
    c = R.count(N)
    return {"before": mw(R.extract(base)),
            "cut_only": mw(R.extract(md.replace(CENSUS_FIX, ""))),
            "now": mw(N),
            "floor": mw(N) - mw(N[gp:so]) - mw(N[so:ev]),
            "bold": c["bold"], "italic": c["italic"]}


def run(text: str, want: dict, label: str) -> int:
    problems, matched = [], 0
    for pat, key in CLAIMS:
        m = re.search(pat, text)
        if not m:
            problems.append(f"PATTERN NEVER MATCHED (that claim is unguarded): {pat}")
            continue
        matched += 1
        stated = int(m.group(1).replace(",", ""))
        if stated != want[key]:
            problems.append(f"MISMATCH: prose states {stated:,} for {key}; the mail has {want[key]:,}")
    print(f"  [{label}] {matched}/{len(CLAIMS)} patterns matched; problems: {len(problems)}")
    for p in problems:
        print("      ", p)
    return len(problems)


def main() -> int:
    want = computed()
    print("computed from the mail:", want)
    text = R.DRAFT.read_text(encoding="utf-8") + "\n" + CARD.read_text(encoding="utf-8")
    real = run(text, want, "draft + card")
    fired = run(text.replace("carries **27 bold", "carries **99 bold"), want, "corrupted copy")
    live = fired > real
    print("\nliveness:", "check FIRED on corruption" if live
          else "!! CHECK DID NOT FIRE — its result means nothing !!")
    return 0 if (real == 0 and live) else 1


if __name__ == "__main__":
    raise SystemExit(main())
