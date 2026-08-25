#!/usr/bin/env python3
"""Do the E1 documents still state the figures the mail actually has?

WHY THIS EXISTS. `render_eap_mail.py --count` computes the authoritative number,
but computing is not enforcing: the count is hard-coded into FIVE living
documents, so one re-wording of the mail silently falsifies all of them. On
2026-08-25 a four-word P1 fix moved the mail 1,477 -> 1,481 and left nine stale
figures behind (`@codex`, fm #946).

THREE DEFECTS THIS FILE HAS ALREADY HAD, each of which made it useless while
looking like it worked — they are why it is written the way it is:

  1. It searched each file for the literal it expected and compared that to the
     computed value: `int("1,477") != 1477`. An `X != X` condition. It could not
     fail. NOW: the number is read OUT of the prose by a capture group.
  2. It used `re.search`, which returns only the FIRST match. A stale duplicate
     in a second document passed because an earlier correct copy satisfied the
     pattern. NOW: `finditer`, every occurrence, in every file, with line numbers.
  3. It advertised five consumers in its own docstring and loaded two of them,
     so `docs/owner-queue.md`, `docs/current-state.md` and the program ledger
     could go stale while this exited 0. NOW: CONSUMERS is the list, and a
     document is only protected if it is in it.

Two failure modes, both reported, because a check that cannot fail is worse than
no check:
  * MISMATCH               - prose states a number the mail does not have.
  * PATTERN NEVER MATCHED  - the phrasing moved, so that claim is unguarded.

Every pattern uses `\\s+` for spaces: the docs hard-wrap at ~76 columns and a
literal space cannot cross a line break. Every run re-checks itself against a
corrupted copy and prints whether the corruption fired.

USAGE
    python3 tools/check_eap_figures.py     # exit 0 = every consumer agrees
"""
from __future__ import annotations
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import render_eap_mail as R                                        # noqa: E402

CONSUMERS = [
    "docs/planning/2026-08-24-final-eap-email-draft.md",
    "docs/owner-queue.md",
    "docs/current-state.md",
    "docs/planning/2026-07-26-consolidation-program.md",
    ".sessions/2026-08-25-e1-owner-revision-pass.md",
]
BASE = "9b2d83a:docs/planning/2026-08-24-final-eap-email-draft.md"
CENSUS_FIX = ", and **seven were created after the program closed**"

# (pattern, keys-in-group-order). Every occurrence in every consumer is checked.
CLAIMS = [
    (r"Part\s+2\s+was\s+([\d,]+)\s+words\s+at",                    ["before"]),
    (r"9b2d83a`,\s+([\d,]+)\s+after\s+the\s+cut",                  ["cut_only"]),
    (r"and\s+([\d,]+)\s+as\s+it\s+now\s+stands",                   ["now"]),
    (r"·\s+([\d,]+)\s+words\s+is\s+about\s+three\s+pages",         ["now"]),
    (r"([\d,]+)\s+words\s+is\s+still\s+about\s+three\s+pages",     ["now"]),
    (r"measured\s+([\d,]+),\s+and\s+those\s+two",                  ["floor"]),
    (r"carries\s+\*\*([\d,]+)\s+bold",                             ["bold"]),
    (r"bold\s+and\s+([\d,]+)\s+italic\s+spans",                    ["italic"]),
    (r"the\s+route\s+lands\s+at\s+\*\*([\d,]+)\*\*",               ["cut_only"]),
    (r"\*\*([\d,]+)\s+→\s+([\d,]+)\s+words",                       ["before", "now"]),
    (r"Part\s+2\s+is\s+\*\*([\d,]+)\s+words\*\*",                  ["now"]),
    (r"`--selftest`\s+\((\d+)\s+assertions\)",                     ["assertions"]),
]


# WHERE EACH CLAIM IS EXPECTED TO LIVE — pinned per pattern AND per file.
# WHY IT IS PINNED. Counting occurrences GLOBALLY cannot see a claim that
# disappears: reword the card's "(13 assertions)" and the program ledger's copy
# still satisfies the pattern, so the total is unchanged, no MISMATCH fires, and
# the run exits 0 on a document whose claim is now unguarded (`@codex`, fm #946
# round 3 — the fifth distinct way this file has found to pass while being
# incapable of failing). A per-file inventory makes the disappearance itself the
# error.
#
# When a claim legitimately moves or a document is added, this must be updated in
# the same commit — that is the point, not friction around it.
EXPECTED_INVENTORY = {
    (0, "docs/planning/2026-08-24-final-eap-email-draft.md"): 1,
    (1, "docs/planning/2026-08-24-final-eap-email-draft.md"): 1,
    (2, "docs/planning/2026-08-24-final-eap-email-draft.md"): 1,
    (3, "docs/planning/2026-08-24-final-eap-email-draft.md"): 1,
    (4, "docs/owner-queue.md"): 1,
    (5, "docs/planning/2026-08-24-final-eap-email-draft.md"): 1,
    (6, "docs/planning/2026-08-24-final-eap-email-draft.md"): 1,
    (7, ".sessions/2026-08-25-e1-owner-revision-pass.md"): 1,
    (7, "docs/planning/2026-08-24-final-eap-email-draft.md"): 1,
    (8, ".sessions/2026-08-25-e1-owner-revision-pass.md"): 1,
    (8, "docs/planning/2026-08-24-final-eap-email-draft.md"): 1,
    (9, "docs/owner-queue.md"): 1,
    (9, "docs/planning/2026-08-24-final-eap-email-draft.md"): 1,
    (10, "docs/current-state.md"): 1,
    # x2: the card states the count once as fact and once inside the quoted
    # round-3 scenario. Both go stale together if the count moves, so both are
    # pinned. This entry was found by the checker failing on its own author's
    # commit, which is the behaviour it exists for.
    (11, ".sessions/2026-08-25-e1-owner-revision-pass.md"): 2,
    (11, "docs/planning/2026-07-26-consolidation-program.md"): 1,
}

def computed() -> dict:
    md = R.DRAFT.read_text(encoding="utf-8")
    mw = lambda ls: sum(1 for w in R.to_text(ls).split() if re.search(r"[A-Za-z0-9]", w))
    N = R.extract(md)
    base = subprocess.run(["git", "show", BASE], cwd=ROOT,
                          capture_output=True, text=True, check=True).stdout
    at = lambda p: next(k for k, l in enumerate(N) if l.startswith(p))
    gp, so, ev = (at("**What genuinely worked"), at("**A standing offer"),
                  at("Everything above is public"))
    c = R.count(N)
    # the assertion count comes from the tool's own output, not from a constant
    out = subprocess.run([sys.executable, str(ROOT / "tools/render_eap_mail.py"), "--selftest"],
                         capture_output=True, text=True).stdout
    m = re.search(r"(\d+)/(\d+)\s+assertions", out)
    return {"before": mw(R.extract(base)),
            "cut_only": mw(R.extract(md.replace(CENSUS_FIX, ""))),
            "now": mw(N),
            "floor": mw(N) - mw(N[gp:so]) - mw(N[so:ev]),
            "bold": c["bold"], "italic": c["italic"],
            "assertions": int(m.group(2)) if m else -1}


def check(docs: dict[str, str], want: dict, label: str, ret_hits: bool = False):
    problems, hits = [], 0
    for pat, keys in CLAIMS:
        found = 0
        for path, text in docs.items():
            for m in re.finditer(pat, text):          # EVERY occurrence, not the first
                found += 1; hits += 1
                line = text.count("\n", 0, m.start()) + 1
                for gi, key in enumerate(keys, start=1):
                    stated = int(m.group(gi).replace(",", ""))
                    if stated != want[key]:
                        problems.append(f"MISMATCH {path}:{line} — states {stated:,} "
                                        f"for {key}; the mail has {want[key]:,}")
        if not found:
            problems.append(f"PATTERN NEVER MATCHED (claim unguarded): {pat}")
    print(f"  [{label}] {hits} occurrence(s) checked across {len(docs)} file(s); "
          f"problems: {len(problems)}")
    for p in problems:
        print("      ", p)
    return (len(problems), hits) if ret_hits else len(problems)


def main() -> int:
    want = computed()
    print("computed from the mail:", want)
    docs = {p: (ROOT / p).read_text(encoding="utf-8") for p in CONSUMERS}

    # INVENTORY FIRST. If a claim has vanished, no amount of value-checking on
    # what remains can tell you — so establish the shape before trusting the values.
    actual = {}
    for pi, (pat, _keys) in enumerate(CLAIMS):
        for path, text in docs.items():
            n = len(re.findall(pat, text))
            if n:
                actual[(pi, path)] = n
    drift = []
    for key, n in EXPECTED_INVENTORY.items():
        got = actual.get(key, 0)
        if got != n:
            drift.append(f"CLAIM {'VANISHED' if got == 0 else 'COUNT CHANGED'}: "
                         f"claim[{key[0]}] in {key[1]} — expected {n}, found {got}")
    for key, n in actual.items():
        if key not in EXPECTED_INVENTORY:
            drift.append(f"UNPINNED OCCURRENCE: claim[{key[0]}] in {key[1]} x{n} "
                         f"— add it to EXPECTED_INVENTORY")
    print(f"  [inventory] {len(actual)} pinned location(s); drift: {len(drift)}")
    for d in drift:
        print("      ", d)

    real, seen_before = check(docs, want, "all consumers", ret_hits=True)
    # Corrupt the LAST occurrence of a claim in the LAST file, so a
    # first-match-only regression is caught too. Done by REGEX, never by a
    # literal: the docs hard-wrap, so a literal like "the route lands at **"
    # does not exist in the file and the corruption silently becomes a no-op —
    # which is exactly how an earlier version of this probe reported a pass.
    poisoned, target = dict(docs), None
    for path in reversed(CONSUMERS):
        for pat, keys in reversed(CLAIMS):
            ms = list(re.finditer(pat, docs[path]))
            if ms:
                target, m = path, ms[-1]
                s, e = m.span(1)
                # "9999", not "9,999": the value must still MATCH the pattern.
                # A corruption the pattern cannot match makes the claim vanish
                # instead of mismatch, and the probe then reports zero problems
                # on a broken document — measured here, occurrence count 15->14.
                poisoned[path] = docs[path][:s] + "9999" + docs[path][e:]
                break
        if target: break
    if target is None:
        print("  !! no claim found to corrupt — liveness cannot be established !!")
        return 1
    print(f"  (liveness probe corrupts the last claim in {target})")
    # Liveness compares VALUE problems only. Folding inventory drift into `real`
    # made the probe report "did not fire" whenever drift existed, which is
    # misleading output on a run that is already failing for a different reason.
    fired, seen_after = check(poisoned, want, "corrupted copy", ret_hits=True)
    live = fired > real and seen_after == seen_before
    if seen_after != seen_before:
        print(f"  !! corruption changed the occurrence count "
              f"({seen_before} -> {seen_after}): the claim vanished rather than "
              f"mismatching, so this probe proves nothing !!")
    print("\nliveness:", "check FIRED on corruption" if live
          else "!! CHECK DID NOT FIRE — its result means nothing !!")
    return 0 if (real == 0 and not drift and live) else 1


if __name__ == "__main__":
    raise SystemExit(main())
