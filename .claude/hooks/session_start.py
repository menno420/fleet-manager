#!/usr/bin/env python3
"""SessionStart — deliver the cold-orientation contract at the one moment it applies.

WHY THIS EXISTS
---------------
`README.md` § "Mandatory reading order" and `.claude/CLAUDE.md` § "Cold
orientation" both state the six-read order. Stating it has failed at least
three times, each instance recorded in the boot file itself:

  · 2026-08-05 — the deep read path started at the program, so a session that
    followed it exactly never learned `docs/owner-reflection-2026-07-21.md`
    existed. Fixed by adding entry 0.
  · 2026-08-06 — `2026-08-05-foundation-continuation.md` called itself the doc
    that "supersedes everything else about what to do next" and NOTHING in the
    read path referenced it; it was reachable only by being handed a prompt
    that named it. Fixed by adding entry 2b.
  · 2026-08-10 — the 2026-08-08 roadmap appeared in neither the boot file nor
    README, while `current-state.md` carried it BELOW its own "preserved, not
    current" banner. Fixed by adding entry 1b.

Three defects, three repairs, and all three repairs were another paragraph of
prose in the file whose prose had just failed. `docs/intent.md` § 4 names that
as the wrong move — *records may grow; instructions may not; the fix for an
unfollowed rule is a mechanism that delivers it at the right moment.* The right
moment for orientation is boot, and until now nothing fired there:
`docs/findings/2026-08-29-estate-agent-error-audit.md:259` measured it —
*"`fleet-manager` wires no `SessionStart` hook."* OD-24 §4 names the event as
the cross-session chain's seam.

WHAT IT ADDS THAT PROSE CANNOT
------------------------------
Not the list — a session can already read the list. Three things prose cannot
carry, because each is only knowable at boot:

1. **That the apparatus loaded at all.** The boot triad's two dangerous cases —
   root is a satellite repo, root is the bare clone parent `/home/user` — are
   both SILENT: settings, hooks, skills and the auto-loaded CLAUDE.md go quiet
   with no error, and the session cannot tell "the rule did not apply" from
   "the rule never arrived". This hook cannot warn in those cases (it does not
   run either). Its FIRING is the signal, which is why it names itself.
2. **Whether the six documents are still there.** Same discipline as
   `tools/check_doc_routes.py`: a pointer at a moved or deleted doc is worse
   than no pointer, because the session stops looking. Every path is stat'd and
   a missing one is reported as missing rather than printed as a live link.
3. **Which start this is.** `source` distinguishes a cold boot from a resume or
   a post-compaction continuation; the six-read mandate is written for the cold
   case, and re-injecting it verbatim after every compaction would spend context
   restating what the session already did.

CONTRACT (identical to every other advisory hook here)
------------------------------------------------------
· Never blocks. Exit 0 on every path, including a crash.
· Writes nothing to the repo — telemetry goes to /tmp, so a session trying to
  keep a clean tree never finds this in `git status`.
· Every firing is countable at /tmp/claude-session-start/log.jsonl, INCLUDING
  the skips. That is not decoration: `owner_review.py` shipped a silent-skip
  path, its absence went unnoticed for eighteen days, and this estate rates a
  false guardrail as costlier than a false wall. A mechanism whose absence is
  invisible is indistinguishable from a working one.

Unlike `route_docs.py`, this one is NOT silent-by-default and NOT deduplicated.
Those rules exist because an advisory that fires on every tool call becomes
noise the session learns to skip. `SessionStart` fires once per session by
construction, so there is no noise field to join — and the estate's own measured
finding on selective firing (`docs/findings/2026-08-06-provenance-mechanism-measured.md`
§ 8: *"fixed-and-always-on and blended-into-conversation both avoid the
test-signal; selective firing is the worst of the three"*) argues against making
it conditional on content.

VERIFY
------
    for s in startup clear resume compact fork; do
      echo "{\"session_id\":\"t\",\"hook_event_name\":\"SessionStart\",\"source\":\"$s\"}" \
        | python3 .claude/hooks/session_start.py; done
    echo '{"session_id":"t"}' | python3 .claude/hooks/session_start.py   # absent source
    echo 'not json' | python3 .claude/hooks/session_start.py             # exit 0, silent
    cat /tmp/claude-session-start/log.jsonl
"""

from __future__ import annotations

import json
import os
import sys
import time

CACHE_DIR = "/tmp/claude-session-start"
LOG = os.path.join(CACHE_DIR, "log.jsonl")

# Root is the session's working directory and is fixed at boot. CLAUDE_PROJECT_DIR
# is what Claude Code sets; the walk-up is the fallback for a hook invoked by
# hand from a subdirectory. Never `git rev-parse` here — a hook must not depend
# on a subprocess to find its own repo.
REPO = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# The six reads, in README.md's numbered order, each with what the read GIVES —
# so skipping one is a decision rather than an accident (README.md:34-37).
#
# Read 4 is deliberately three paths in one entry. README.md:45-58 makes the
# program and the roadmap a PAIR (OD-13 puts the roadmap's phases ahead of the
# lettered product steps, so a session reading only the program learns the steps
# but not their order), and [D-0025] adds the redirect on top. Splitting them
# into three numbered reads would silently turn the owner's six-read contract
# into an eight-read one; keeping them as one entry preserves the contract and
# the pairing at the same time.
READS = [
    ("README.md",
     "purpose, the story, this list, the map"),
    ("docs/intent.md",
     "WHY the repo exists — what 'working' means to him, the non-goals, "
     "who does what across Claude / ChatGPT / Gemini / Grok / Codex"),
    ("docs/current-state.md",
     "what is TRUE NOW — live state, work state, what shipped recently"),
    ("docs/planning/2026-07-26-consolidation-program.md",
     "the goals and the plan — the OD table, the step tracks, the NOW pointer. "
     "Read it WITH docs/planning/2026-08-08-agent-operating-environment-roadmap.md "
     "(OD-13 puts the roadmap's phases ahead of the lettered steps) AND "
     "docs/planning/2026-08-30-fresh-start-redirect.md ([D-0025]: the plan "
     "executes in a FRESH hub; this repo becomes the read-only archive)"),
    ("docs/fleet-account-2026-07-26.md",
     "how it came to exist — the EAP story to the close. Read once; "
     "do not re-derive the history"),
    ("docs/owner-reflection-2026-07-21.md",
     "how the OWNER thinks — the wall is verification not capability; "
     "decide rather than default to asking"),
]

# Companions to read 4, checked for existence with the six but never numbered —
# see the READS comment on why they are not separate reads.
COMPANIONS = [
    "docs/planning/2026-08-08-agent-operating-environment-roadmap.md",
    "docs/planning/2026-08-30-fresh-start-redirect.md",
]

# README.md:66-69 — the acceptance test, verbatim in substance. A session that
# cannot answer these has met a defective front door and should record the
# missing fact rather than compensating by searching harder.
ACCEPTANCE = (
    "After these six you must be able to state WITHOUT GUESSING: what this repo "
    "is for · what era it is in · what the owner is working on and why · what "
    "the next actionable step is. If you cannot, the front door is defective — "
    "record the missing fact instead of hunting through extra documents."
)

# A cold start gets the contract. A resume or a post-compaction continuation
# gets a pointer: the session already walked it, or its context was just
# dropped and re-reading is cheaper than re-injecting. `fork` inherits the
# parent's context, so it is warm too.
COLD_SOURCES = {"startup", "clear"}


def _log(rec: dict) -> None:
    try:
        os.makedirs(CACHE_DIR, exist_ok=True)
        with open(LOG, "a") as f:
            f.write(json.dumps(rec) + "\n")
    except Exception:
        pass  # telemetry must never be the thing that breaks a boot


def _present(rel: str) -> bool:
    return os.path.exists(os.path.join(REPO, rel))


def _cold_block(missing: list[str]) -> str:
    lines = [
        "COLD ORIENTATION — the six mandatory reads (README.md § Mandatory "
        "reading order; owner directive 2026-08-10).",
        "",
        "This is a mechanism, not a reminder: the same rule was stated in prose "
        "three times (2026-08-05, 08-06, 08-10) and missed three times. Read "
        "these in order before acting. A fresh session should NOT read "
        "everything — after these six, docs/MAP.md routes the rest.",
        "",
    ]
    for i, (path, gives) in enumerate(READS, 1):
        mark = "" if _present(path) else "  ⚠ MISSING AT THIS HEAD"
        lines.append(f"{i}. {path}{mark}")
        lines.append(f"   → {gives}")
    lines += ["", ACCEPTANCE]
    if missing:
        lines += [
            "",
            "⚠ " + str(len(missing)) + " path(s) above do not exist at this "
            "HEAD: " + ", ".join(missing) + ". Do not silently substitute a "
            "similar file — a moved read is a defect in the front door, and "
            "recording it is worth more than compensating for it.",
        ]
    lines += [
        "",
        "Also live, and not part of the six: docs/MAP.md (one line per area, "
        "CORE/TASK/RECORD) · docs/ESTATE.md (every repository, one line) · "
        "docs/activity/ (what sessions did ANYWHERE, including his laptop — "
        "this repo's .sessions/ is fleet-manager's work alone) · "
        "docs/traps.md (the recurring execution mistakes, delivered by route "
        "at the moment each one happens).",
        "",
        "This hook firing is also the proof that root IS this repo and the "
        "apparatus loaded — hooks, skills and .claude/CLAUDE.md. When root is a "
        "satellite repo or the bare clone parent, all of it goes quiet with no "
        "error and nothing says so.",
    ]
    return "\n".join(lines)


def _warm_block(source: str) -> str:
    what = ("context was just compacted, so the orientation you did at boot may "
            "no longer be in the window"
            if source == "compact" else
            "this session continues earlier context")
    return (
        f"SESSION RESUMED ({source}) — {what}. The cold-orientation contract is "
        "README.md § Mandatory reading order (six reads, in order). Re-walk it "
        "if you cannot currently state: what this repo is for · what era it is "
        "in · what the owner is working on and why · the next actionable step. "
        "The quick mid-task re-check is docs/current-state.md + the "
        "consolidation program's NOW pointer."
    )


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        # Malformed or absent stdin is not a reason to spend a boot on a
        # traceback. Logged, because an unlogged skip is the defect this file's
        # header is about.
        return _log({"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                     "skip": "bad-stdin"})

    source = (data.get("source") or "unknown").lower()
    missing = [p for p, _ in READS if not _present(p)]
    missing += [p for p in COMPANIONS if not _present(p)]

    # An absent `source` is treated as COLD. The docs list five values and this
    # hook must not go quiet on a sixth: under-injecting on a real cold start
    # costs the orientation this exists to deliver, while over-injecting on a
    # warm one costs ~30 lines of context. The asymmetry picks the default.
    cold = source in COLD_SOURCES or source == "unknown"
    text = _cold_block(missing) if cold else _warm_block(source)

    _log({"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
          "session": data.get("session_id"), "source": source,
          "cold": cold, "missing": missing, "chars": len(text),
          "repo": REPO})

    # SessionStart adds plain-text stdout to the session's context — NOT the
    # JSON decision object the tool-time events use. Verified against
    # code.claude.com/docs/en/hooks 2026-08-31: "The exceptions are
    # UserPromptSubmit, UserPromptExpansion, SessionStart, and PostModelSwitch,
    # where Claude Code adds plain-text stdout as context that Claude can see
    # and act on." Printing a JSON blob here would deliver the braces as prose.
    print(text)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        # Deliberate termination is not a defect, and fail-open is a promise
        # about bugs — not a licence to outlive the process that owns us.
        # owner_review.py learned this the expensive way (2026-08-08).
        raise
    except BaseException:
        # BaseException rather than Exception: MEASURED 2026-08-08 in this
        # directory, a native panic (PanicException -> BaseException -> object)
        # escaped a narrower catch and the hook exited 1. A SessionStart hook
        # that exits non-zero starts the session with an error notice.
        pass  # FAIL-OPEN
    sys.exit(0)
