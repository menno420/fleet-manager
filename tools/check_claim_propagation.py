#!/usr/bin/env python3
"""Claim-propagation sweep — does a corrected claim still stand somewhere else?

WHY THIS EXISTS. On 2026-08-24 (fm #943) five consecutive review rounds each
found the same defect shape: a claim was corrected in the outbound document and
left standing in its source, or vice versa. The fix announced in round 4 was a
one-line `grep -rn` with five alternatives — one of which was `never got\\nan
answer`. **A basic-regex `\\n` cannot express a newline** — POSIX/GNU call a
backslash before an ordinary character *unspecified*, and GNU grep 3.11 here
matches the literal text `never gotnan answer` — so that alternative could not
match a line break and therefore could not fail. It returned clean and was
reported as a passing check. (An earlier version of this comment said grep reads
it as a literal backslash-n; the conclusion held, the mechanism was wrong.)

THE RULE THIS ENFORCES, and it is the transferable half:
    A check whose failure mode is SILENCE must be shown to fire
    before its silence means anything.

So this file ships `--selftest`, which asserts every pattern matches a fixture
built to contain it. A pattern that stops matching its own fixture is a broken
pattern, not a clean repo.

USAGE
    python3 tools/check_claim_propagation.py            # sweep docs/ + .sessions/
    python3 tools/check_claim_propagation.py --selftest # prove each pattern fires

Exit 0 = no residual withdrawn claim. Exit 1 = residual sites, named.
Patterns are RETRACTED wordings. A hit inside an explicit retraction is expected
and is why `ALLOW_IN_RETRACTION` exists.
"""
import pathlib, re, sys

# name -> (regex for the WITHDRAWN wording, fixture line that MUST match)
CLAIMS = {
    "search-index-blind": (
        r"[Dd]o not measure this account with `?search/issues",
        "Do not measure this account with `search/issues` or `search/code`."),
    "agents-created-every-byte": (
        r"[Aa]gents created (all of it|every byte)",
        "Agents created every byte of it and no agent surface could see it."),
    "tool-call-only": (
        r"binds only if it \*?fires\*? at the\s+tool call",
        "a rule binds only if it *fires* at the\ntool call, so we built routes."),
    "never-got-an-answer": (
        r"never got\s+an answer",
        "offered this estate as a test harness and never got\nan answer."),
    "three-queries": (
        r"[Tt]hree independent queries|three queries with a passing",
        "Three independent queries, each returning consistently:"),
    "near-700-words": (
        r"near 700 words|700-word route",
        "keep asks 1-5, and the mail lands near 700 words."),
    "116-present-tense": (
        r"This repo carries \*\*116|repository carries \*\*116",
        "This repo carries **116 committed statements of the rule."),
    "61-doc-routes-undated": (
        r"\b61 (doc-routes|documentation routes)\b(?![^\n]*20\d\d-\d\d-\d\d)",
        "we built 61 documentation routes onto a pre-tool hook."),
    "nobody-else-can-send": (
        r"nobody else can send|the only one (that|who) kept",
        "why nobody else can send it"),
    "full-read-every-file": (
        r"[Aa] full read of every tracked file(?![^\n]*structural)",
        "A full read of every tracked file found 101 defects."),
    "no-agent-surface-at-all": (
        r"no agent surface could see any of it(?![^\n]*proactiv)",
        "and no agent surface could see any of it."),
    # Deliberately shape-based, not spelling-based: the retired claim is the
    # UNIVERSAL "agents append / do not retract", however punctuated, bolded or
    # paraphrased. An earlier version matched only the exact bolded sentence with
    # a semicolon and `do not`, so `Agents append; they never retract` and any
    # unbolded copy passed (@codex, fm #944). A guard that only catches the
    # spelling it retired is theatre.
    "agents-append-universal": (
        r"agents\s+append\b[\s\S]{0,60}?(?:not|never|n't)\s+retract",
        ["read as correct. **Agents append; they\ndo not retract.** A defect",
         "Agents append; they never retract.",
         "agents append and do not retract",
         "Agents append, they don't retract.",
         "*Agents append — they never retract.*"]),
    "every-human-review": (
        r"which is every review a human actually performs",
        "invisible to any review that reads for coherence, which is every review a human actually performs."),
}

# A hit is EXPECTED when the surrounding line explicitly marks a retraction.
ALLOW_IN_RETRACTION = re.compile(
    r"~~|RETRACTED|WITHDRAWN|withdrawn|struck|was headed|first said|"
    r"an earlier (version|draft)|no basis for|does not reproduce|"
    r"not established|removed from the mail|was wrong about|is now fixed|"
    r"claimed every channel", re.I)
# NOT in this list, deliberately: bare `corrected` and `conceded`. Both are
# ordinary English that appears in prose ABOUT defects, so either one silences
# the guard wherever a document merely discusses a correction. Measured fm #944:
# `corrected` in the mail's own Finding 2 paragraph swallowed a deliberately
# reintroduced paraphrase, and the sweep reported CLEAN. Every entry above names
# a RETRACTION; none is a word that ordinary prose reaches for.

# Every match site passes re.I. Until fm #944 none did, so a pattern written in
# lower case could not match a capitalised sentence: `agents append` missed
# `Agents append`. The selftest reported DEAD PATTERN rather than a false CLEAN,
# which is the only reason it was cheap to find.
ROOTS = ("docs", ".sessions")

# A dated finding legitimately carries its own claim in the present tense — that
# is what a dated document IS. Sweeping it reports a false positive. This is a
# per-claim exemption for the ONE file that owns each claim, never a blanket one.
EXEMPT = {
    "116-present-tense": {"docs/findings/2026-08-08-why-rules-dont-bind.md"},
}

# WHICH marker retracts THIS claim — a structural rule, deliberately not a
# character window. A -320/+160 window was tried first and measured: the
# tightest real case cleared it by TWO characters, i.e. the number fitted the
# corpus by luck and any nearby edit would have flipped a valid retraction into
# a false residual. A threshold that has to be re-tuned whenever prose moves is
# not a check, it is a tripwire.
#
# The structural discriminator, which needs no number: **a retraction announces
# itself and then quotes what it retracts.** So a marker counts when it is on
# the claim's own line, or anywhere EARLIER in the same block. A marker that
# appears only AFTER the claim is a different sentence talking about something
# else — which is exactly the hostile case part B builds.


def sweep() -> int:
    residual = 0
    for name, (pat, _fixture) in CLAIMS.items():
        sites = []
        for root in ROOTS:
            for f in pathlib.Path(root).rglob("*.md"):
                if f.as_posix() in EXEMPT.get(name, ()):
                    continue
                text = f.read_text(errors="replace")
                lines = text.splitlines()
                for m in re.finditer(pat, text, re.I):
                    ln = text[:m.start()].count("\n")
                    # Context = the ENCLOSING BLOCK (blank-line delimited), not a
                    # fixed line window. A fixed window was tried first and gave
                    # false positives every time a retraction ran longer than a
                    # few lines — and the reflex fix, adding whatever words the
                    # missed case happened to use, is vocabulary whack-a-mole
                    # that ratchets the filter toward never firing. The block is
                    # the unit a human actually reads a claim in, so it is the
                    # unit that decides whether the claim is being ASSERTED or
                    # QUOTED-AS-WITHDRAWN.
                    start = end = ln
                    while start > 0 and lines[start - 1].strip():
                        start -= 1
                    while end < len(lines) - 1 and lines[end + 1].strip():
                        end += 1
                    block_lines = lines[start:end + 1]
                    block = "\n".join(block_lines)
                    # The marker must belong to THIS claim, not merely share a
                    # block with it. Scanning the whole block was the previous
                    # rule and it is unsafe: one retraction anywhere in a long
                    # paragraph or list silences every live claim beside it —
                    # which is a check that cannot fail, the defect this file
                    # exists to prevent. So: a bounded window around the match.
                    off = block.find(m.group(0))
                    own_line = lines[ln]
                    preceding = block[:off]          # everything earlier in the block
                    if (ALLOW_IN_RETRACTION.search(own_line)
                            or ALLOW_IN_RETRACTION.search(preceding)):
                        continue          # a retraction naming its own claim
                    sites.append(f"{f}:{ln + 1}")
        print(f"{name:28} {'CLEAN' if not sites else 'RESIDUAL -> ' + ', '.join(sites)}")
        residual += len(sites)
    print(f"\nresidual sites: {residual}")
    return 1 if residual else 0


def selftest() -> int:
    """Two halves, and the second is the one that keeps this check honest.

    A · every pattern must match its fixture — a pattern that cannot fire is a
        dead pattern, not a clean repo. (The round-4 `never got\\nan answer`
        grep failed exactly here.)
    B · the retraction filter must NOT swallow a LIVE claim. Widening
        ALLOW_IN_RETRACTION to silence false positives is the obvious next
        mistake: widen it far enough and the sweep can never fail again. So each
        fixture is also run through the filter as if it stood alone, and must
        still be reported.
    """
    bad = []
    for name, (pat, fixtures) in CLAIMS.items():
        if isinstance(fixtures, str):
            fixtures = [fixtures]
        # EVERY variant must fire, not just the first. A pattern that catches
        # only the wording it retired cannot stop a paraphrase restoring it.
        fires = all(re.search(pat, f, re.I) for f in fixtures)
        fixture = fixtures[0]
        # B — and it must run the PRODUCTION path, not a simplified one.
        # An earlier version tested the bare fixture against the filter while
        # sweep() applied the filter to the whole enclosing block, so a live
        # claim sharing a block with an unrelated retraction was swallowed in
        # production while this test passed (@codex, fm #943 round 6). The
        # fixture is therefore embedded in a hostile block: a live claim, then
        # an UNRELATED retraction marker far enough away that it must not reach
        # it. If the windowing regresses, this goes red.
        hostile = (fixture + "\n" + "filler. " * 40 +
                   "\nSeparately, an unrelated claim was corrected earlier today.")
        hl = hostile.splitlines()
        m = re.search(pat, hostile, re.I)
        off = m.start() if m else 0
        own_line = hl[hostile[:off].count("\n")] if m else ""
        preceding = hostile[:off]
        swallowed = bool(ALLOW_IN_RETRACTION.search(own_line)
                         or ALLOW_IN_RETRACTION.search(preceding))
        n = len(fixtures)
        status = (f"fires ({n} variant{'s' if n > 1 else ''})"
                  if fires and not swallowed else
                  "DEAD PATTERN" if not fires else "SWALLOWED BY FILTER")
        if not fires or swallowed:
            missed = [f for f in fixtures if not re.search(pat, f, re.I)]
            bad.append(f"{name} ({status}"
                       + (f"; missed: {missed!r}" if missed else "") + ")")
        print(f"{name:28} {status}")
    if bad:
        print(f"\nBROKEN ({len(bad)}): {', '.join(bad)}", file=sys.stderr)
        return 1
    print(f"\nall {len(CLAIMS)} patterns fire, and none is swallowed by the "
          f"retraction filter")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else sweep())
