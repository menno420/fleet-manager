#!/usr/bin/env python3
"""Regression suite for the doc-routes patterns that guard TRAP-004.

================================ PROVENANCE ================================
Why added : On 2026-08-26 the `claim-beyond-the-sample` route was widened —
            it had been scoring 0 of 4 against real sentences from that day's
            own session. The widening fixed those four AND silently deleted
            coverage the route already had: `\\bevery (repo|repository|file)
            in\\b` was replaced with a plural-only noun set, so "every
            repository in" stopped firing. `@codex` caught it on fm #950.
            Nothing tested this table, so a change that narrowed it looked
            identical to a change that widened it.
Date      : 2026-08-26 (fleet-manager PR #950)
Reliability: Deterministic. Reads the live `doc-routes.json`, so it fails when
            a future edit breaks a case rather than when this file goes stale.
=============================================================================

usage: python3 tools/test_doc_route_patterns.py
       Exits 0 all-green, 1 on any failure.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

TABLE = Path(__file__).resolve().parents[1] / ".claude/hooks/doc-routes.json"


def patterns(route_id: str) -> list[re.Pattern]:
    table = json.loads(TABLE.read_text(encoding="utf-8"))
    route = next(r for r in table["routes"] if r["id"] == route_id)
    return [re.compile(w) for w in route["when"]]


def fires(pats: list[re.Pattern], text: str) -> bool:
    return any(p.search(text) for p in pats)


# Every MUST_FIRE sentence is one an agent in this estate actually wrote, or a
# form the route was built to catch. Every MUST_BE_SILENT is prose that merely
# contains a number or a noun — a route that fires on those is worse than the
# gap it closes.
SAMPLE = "claim-beyond-the-sample"
MUST_FIRE = [
    # the four TRAP-004 instances measured on 2026-08-26
    ("shallow-clone commit count", "git history | 50 commits, one author, every one squash-merged"),
    ("ratio over a population", "MEASURED: 0 of 419 cards in this repo record which machine ran them"),
    ("count with a qualifier", "the estate wrote 74 session cards across six repositories"),
    ("universal over a set", "all 51 notifications were replays of events I had already handled"),
    ("cards reported as sessions", "fleet-manager ran 163 sessions between 2026-07-22 and 2026-08-26"),
    ("a plan's own headline", "2,849 session cards across 14 kit repos"),
    # the route's own origin sentence
    ("origin sentence", "only 3 of 26 repositories are in the search/code index"),
    # the singular `every X in` forms — deleted by the 2026-08-26 widening
    ("every + singular repository", "every repository in the account was probed"),
    ("every + singular repo", "every repo in the estate carries the kit"),
    ("every + singular file", "every file in docs/ was read"),
]
MUST_BE_SILENT = [
    ("plain prose, no count", "the cards that matter are the ones a session actually reads"),
    ("count with a relative clause", "the 12 cards that were added this week are listed below"),
    ("a rule, not a claim", "every session should contribute an idea for the next agent"),
]

SHALLOW = "shallow-clone-commit-counts"
SHALLOW_MUST_FIRE = [
    ("git log", "git log --oneline | head -20"),
    ("git rev-list", "git rev-list --count HEAD"),
    ("git shortlog", "git shortlog -sn"),
    ("piped count", "git log --pretty=format:%an | wc -l"),
]


# ---------------------------------------------------------------- plumbing --
# The cases above test PATTERNS. These test the ROUTING that carries them, a
# separate axis and the one that failed on 2026-08-28: every pattern was
# correct, and the routes were registered `Edit`/`Write` only while auto mode
# instructs sessions to author through Bash heredocs — so the whole
# claim-quality set went silent for a session that then made three of the exact
# errors those routes exist to catch. A pattern suite could not have caught it,
# because nothing was wrong with the patterns.
CLAIM_ROUTES = (
    "stamping-a-measured-claim",
    "claim-beyond-the-sample",
    "absence-claim",
    "recording-a-wall",
)

HEREDOC_DOC = "cat > docs/findings/x.md <<'EOF'\nall 26 repositories were swept\nEOF"
HEREDOC_MENTION = "grep -rn 'all 26 repositories' docs/traps.md"

# Heredoc spelling varies, and a variant `authored_only()` misses is a guard
# silently back off for that spelling — the same failure this whole change
# exists to fix, one level down. The `<<-` and multiple-heredoc cases were
# raised by `@codex` on fm #963 against an earlier head; they pass, and they
# are pinned here so a future regex tightening cannot quietly drop one.
MARK = "all 26 repositories"
HEREDOC_VARIANTS = [
    ("single-quoted delimiter", f"cat > a.md <<'EOF'\n{MARK}\nEOF", True),
    ("double-quoted delimiter", f'cat > a.md <<"EOF"\n{MARK}\nEOF', True),
    ("bare delimiter", f"cat > a.md <<EOF\n{MARK}\nEOF", True),
    ("tab-stripping <<-", f"cat > a.md <<-EOF\n\t{MARK}\n\tEOF", True),
    ("custom delimiter name", f"cat > a.md <<'CARD'\n{MARK}\nCARD", True),
    ("python3 - heredoc", f"python3 - <<'PY'\nprint('{MARK}')\nPY", True),
    ("second of two heredocs",
     f"cat > a.md <<'A'\nnothing\nA\ncat > b.md <<'B'\n{MARK}\nB", True),
    ("indented terminator", f"cat > a.md <<'EOF'\n{MARK}\n  EOF", True),
    # The silent half: a command that merely NAMES the text must not be
    # matched, or the guard is spent by its own documentation (fm #923).
    ("grep mention, no heredoc", f"grep -rn '{MARK}' docs/traps.md", False),
    ("plain redirect, no heredoc", f"echo '{MARK}' > a.md", False),
]


def route(route_id: str) -> dict:
    for r in json.loads(TABLE.read_text())["routes"]:
        if r["id"] == route_id:
            return r
    raise SystemExit(f"route {route_id!r} not in the table")


def check_plumbing() -> list[str]:
    bad: list[str] = []
    for rid in CLAIM_ROUTES:
        r = route(rid)
        tools = set(r.get("tools") or [])
        if "Bash" not in tools:
            bad.append(
                f"{rid}: must list Bash — a document authored via heredoc is "
                f"invisible to it otherwise (tools={sorted(tools)})"
            )
        if not r.get("authored_only"):
            bad.append(
                f"{rid}: reaches Bash but lacks authored_only, so it matches "
                f"whole commands — a grep MENTION would spend it (fm #923)"
            )
        if not r.get("repeat"):
            bad.append(
                f"{rid}: guards a RECURRING claim class, so one firing must not "
                f"spend it for the session"
            )

    # The extraction itself: heredoc body visible, bare command not.
    sys.path.insert(0, str(TABLE.parent))
    try:
        from route_docs import authored_only  # noqa: PLC0415
    except Exception as exc:  # pragma: no cover - import failure is the failure
        bad.append(f"cannot import authored_only from route_docs: {exc}")
        return bad
    if "all 26 repositories" not in authored_only(HEREDOC_DOC):
        bad.append("authored_only() dropped the heredoc body it must expose")
    if authored_only(HEREDOC_MENTION).strip():
        bad.append(
            "authored_only() returned text for a command with no heredoc — a "
            "mention would fire the guard and spend it"
        )
    for label, command, should_see in HEREDOC_VARIANTS:
        seen = MARK in authored_only(command)
        if seen != should_see:
            want = "expose" if should_see else "stay silent on"
            bad.append(f"authored_only() must {want} the {label} form")
    return bad


def main() -> int:
    failures: list[str] = []
    failures.extend(check_plumbing())
    sample = patterns(SAMPLE)
    for label, text in MUST_FIRE:
        if not fires(sample, text):
            failures.append(f"{SAMPLE}: SHOULD FIRE but is silent — {label}: {text!r}")
    for label, text in MUST_BE_SILENT:
        if fires(sample, text):
            failures.append(f"{SAMPLE}: SHOULD BE SILENT but fires — {label}: {text!r}")

    shallow = patterns(SHALLOW)
    for label, text in SHALLOW_MUST_FIRE:
        if not fires(shallow, text):
            failures.append(f"{SHALLOW}: SHOULD FIRE but is silent — {label}: {text!r}")

    plumbing_cases = len(CLAIM_ROUTES) * 3 + 2 + len(HEREDOC_VARIANTS)
    total = (len(MUST_FIRE) + len(MUST_BE_SILENT) + len(SHALLOW_MUST_FIRE)
             + plumbing_cases)
    if failures:
        for f in failures:
            print(f"FAIL  {f}")
        print(f"\ndoc-route patterns: {len(failures)} of {total} case(s) FAILED")
        return 1
    print(f"doc-route patterns: {total} case(s) — CLEAN "
          f"({len(MUST_FIRE)} must-fire, {len(MUST_BE_SILENT)} must-be-silent, "
          f"{len(SHALLOW_MUST_FIRE)} shallow-clone, "
          f"{plumbing_cases} plumbing)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
