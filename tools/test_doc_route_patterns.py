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
import os
import re
import subprocess
import sys
import tempfile
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

# Bash authoring has many spellings, and the test is WRITE INTENT rather than
# the presence of a heredoc. The first cut of `authored_only()` keyed on the
# heredoc alone; `@codex` found four ways that is wrong (fm #963), one of them
# P1, and every case below pins one of them. The `False` rows matter as much as
# the `True` ones: a command that writes nothing must stay silent, or with the
# repeat cap in place three mentions exhaust a route before the session's first
# real document write.
MARK = "all 26 repositories"
BASH_AUTHORING = [
    # writes — must be visible
    ("redirect before heredoc", f"cat > docs/x.md <<'EOF'\n{MARK}\nEOF", True),
    ("redirect after delimiter", f"cat <<'EOF' > docs/x.md\n{MARK}\nEOF", True),
    ("piped into tee", f"cat <<'EOF' | tee docs/x.md\n{MARK}\nEOF", True),
    ("double-quoted delimiter", f'cat > docs/x.md <<"EOF"\n{MARK}\nEOF', True),
    ("bare delimiter", f"cat > docs/x.md <<EOF\n{MARK}\nEOF", True),
    ("tab-stripping <<-", f"cat > docs/x.md <<-EOF\n\t{MARK}\n\tEOF", True),
    ("custom delimiter name", f"cat > docs/x.md <<'CARD'\n{MARK}\nCARD", True),
    ("second of two heredocs",
     f"cat > a.md <<'A'\nnothing\nA\ncat > b.md <<'B'\n{MARK}\nB", True),
    ("printf into a redirect", f"printf '%s\\n' '{MARK}' > docs/x.md", True),
    ("echo into a redirect", f"echo '{MARK}' > docs/x.md", True),
    ("append redirect", f"echo '{MARK}' >> docs/x.md", True),
    ("sed -i in place", f"sed -i 's/x/{MARK}/' docs/x.md", True),
    ("python heredoc that redirects",
     f"python3 - <<'PY' > docs/x.md\nprint('{MARK}')\nPY", True),
    # no write — must stay silent, or a mention spends the guard (fm #923)
    ("grep mention", f"grep -rn '{MARK}' docs/traps.md", False),
    ("heredoc fed to grep", f"grep -f - docs/x.md <<'EOF'\n{MARK}\nEOF", False),
    ("python heredoc that only prints",
     f"python3 - <<'PY'\nprint('{MARK}')\nPY", False),
    ("plain read", "cat docs/traps.md | head", False),
    # R3 additions
    ("extensionless target", f"cat > README <<'EOF'\n{MARK}\nEOF", True),
    ("python write_text in a heredoc",
     f"python3 - <<'PY'\nPath('docs/x.md').write_text('{MARK}')\nPY", True),
    ("python open(...,'w') in a heredoc",
     f"python3 - <<'PY'\nopen('docs/x.md','w').write('{MARK}')\nPY", True),
    ("special sink is not a document", f"echo '{MARK}' > /dev/null", False),
    ("mention in one segment, write in another",
     f"grep '{MARK}' docs/traps.md; echo ok > docs/x.md", False),
]

# `path_when` routes gate on the target path, which a Bash payload does not
# carry in a `file_path` field. Until the target was derived from the redirect,
# both card routes skipped before their content was examined and stayed silent
# for the very authoring path this change added them to (fm #963 P1).
CARD_PATH_CASES = [
    ("card write via redirect", "cat > .sessions/2026-01-01-x.md <<'EOF'\nx\nEOF",
     ".sessions/2026-01-01-x.md"),
    ("card write, redirect after delimiter",
     "cat <<'EOF' > .sessions/2026-01-01-x.md\nx\nEOF", ".sessions/2026-01-01-x.md"),
    ("a read names no target", "grep -rn x .sessions/2026-01-01-x.md", None),
]


# Fired through the real hook, not through a helper. `card-status-write` gates
# on `path_when`, so it exercises the whole chain: tool opt-in -> target-path
# derivation -> authored_only() -> pattern match.
E2E_CASES = [
    ("card authored via redirect",
     "cat > .sessions/2026-01-01-x.md <<'EOF'\n> **Status:** `complete`\nEOF",
     # UNIQUE to card-flip-to-complete. "TRAP-006" is NOT — it appears in
     # card-status-write too, so the first version of this case passed with
     # card-flip-to-complete deleted outright (`@codex` R5). Verified by
     # set-differencing the two routes' says text.
     "a review binds the SHA it ran on"),
    # R3 P1: the card is the SECOND write target, so taking only the first
    # made both card routes fail path_when and let a completed card through.
    ("card is the second write target",
     "echo ok > docs/x.md; cat > .sessions/2026-01-01-x.md <<'EOF'\n"
     "> **Status:** `complete`\nEOF", "a review binds the SHA it ran on"),
    # R3: card-status-write's `when` is the card PATH, so the Bash haystack has
    # to carry the target as well as the content, mirroring FIELDS["Write"].
    ("in-progress card matches on its path",
     "cat > .sessions/2026-01-01-y.md <<'EOF'\n> **Status:** `in-progress`\nEOF",
     # UNIQUE to card-status-write, set-differenced against its neighbour.
     "Status is a merge control"),
    ("read of a card names no target",
     "grep -rn Status .sessions/2026-01-01-x.md", None),
    # R3: a mention in one segment must not be authorised by a write in another.
    ("compound: mention then unrelated write",
     "grep 'all 26 repositories' docs/traps.md; echo ok > docs/x.md", None),
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
    for label, command, should_see in BASH_AUTHORING:
        seen = MARK in authored_only(command)
        if seen != should_see:
            want = "expose" if should_see else "stay silent on"
            bad.append(f"authored_only() must {want} the {label} form")

    # END-TO-END, and it must be end-to-end. A first version of this check
    # called bash_write_targets() directly and passed with the P1 wiring
    # deleted — the helper was fine and the CALL SITE was the defect, which is
    # this whole change's own failure shape repeating one level down. Run the
    # hook as a subprocess with a real payload instead.
    for index, (label, command, expect) in enumerate(E2E_CASES):
        # A fresh TMPDIR per case. The hook persists fired routes under
        # $TMPDIR, and `hash()` is deterministic when PYTHONHASHSEED is set, so
        # reusing ids made a second run of this suite fail on an already-spent
        # route — the suite was not repeatable, which is the one property a
        # regression suite must have (`@codex`, fm #963 R3).
        with tempfile.TemporaryDirectory() as state:
            env = {**os.environ, "TMPDIR": state}
            event = json.dumps({
                "session_id": f"selftest-{index}",
                "tool_name": "Bash",
                "tool_input": {"command": command},
            })
            proc = subprocess.run(
                [sys.executable, str(TABLE.parent / "route_docs.py")],
                input=event, capture_output=True, text=True, env=env,
            )
        # Assert WHICH route answered, never merely that something did. A bare
        # "did anything fire" passed with the P1 fix deleted, because a
        # neighbouring route with no `path_when` fired on the same payload and
        # satisfied the assertion — the third time in this change that a test
        # was too weak in exactly this way.
        out = proc.stdout
        if expect is None:
            if out.strip():
                bad.append(f"end-to-end: {label} must stay silent, but a route fired")
        elif expect not in out:
            bad.append(
                f"end-to-end: {label} must surface {expect!r} and did not — a "
                f"path route needs EVERY write target, and the Bash haystack "
                f"needs the path as well as the content"
            )

    from route_docs import bash_write_targets  # noqa: PLC0415
    for label, command, expected in CARD_PATH_CASES:
        got = bash_write_targets(command)
        first = got[0] if got else None
        if first != expected:
            bad.append(
                f"bash_write_targets() must yield {expected!r} for {label} "
                f"so path_when can gate on it — got {got!r}"
            )
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

    plumbing_cases = len(CLAIM_ROUTES) * 3 + 2 + len(BASH_AUTHORING) + len(CARD_PATH_CASES) + len(E2E_CASES)
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
