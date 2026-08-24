#!/usr/bin/env python3
"""Claim-propagation sweep — does a corrected claim still stand somewhere else?

WHY THIS EXISTS. On 2026-08-24 (fm #943) five consecutive review rounds each
found the same defect shape: a claim was corrected in the outbound document and
left standing in its source, or vice versa. The fix announced in round 4 was a
one-line `grep -rn` with five alternatives — one of which was `never got\\nan
answer`. **grep reads `\\n` in a basic pattern as a literal backslash-n**, so that
alternative could not match a line break and therefore could not fail. It
returned clean and was reported as a passing check.

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
    "every-human-review": (
        r"which is every review a human actually performs",
        "invisible to any review that reads for coherence, which is every review a human actually performs."),
}

# A hit is EXPECTED when the surrounding line explicitly marks a retraction.
ALLOW_IN_RETRACTION = re.compile(
    r"~~|RETRACTED|WITHDRAWN|withdrawn|struck|was headed|first said|"
    r"an earlier (version|draft)|no basis for|does not reproduce|"
    r"not established|removed from the mail|was wrong about|is now fixed|"
    r"claimed every channel|corrected|conceded", re.I)

ROOTS = ("docs", ".sessions")


def sweep() -> int:
    residual = 0
    for name, (pat, _fixture) in CLAIMS.items():
        sites = []
        for root in ROOTS:
            for f in pathlib.Path(root).rglob("*.md"):
                text = f.read_text(errors="replace")
                lines = text.splitlines()
                for m in re.finditer(pat, text):
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
                    ctx = "\n".join(lines[start:end + 1])
                    if ALLOW_IN_RETRACTION.search(ctx):
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
    for name, (pat, fixture) in CLAIMS.items():
        fires = bool(re.search(pat, fixture))
        # B: the bare fixture carries no retraction marker, so it must survive.
        swallowed = bool(ALLOW_IN_RETRACTION.search(fixture))
        status = "fires" if fires and not swallowed else (
            "DEAD PATTERN" if not fires else "SWALLOWED BY FILTER")
        if not fires or swallowed:
            bad.append(f"{name} ({status})")
        print(f"{name:28} {status}")
    if bad:
        print(f"\nBROKEN ({len(bad)}): {', '.join(bad)}", file=sys.stderr)
        return 1
    print(f"\nall {len(CLAIMS)} patterns fire, and none is swallowed by the "
          f"retraction filter")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else sweep())
