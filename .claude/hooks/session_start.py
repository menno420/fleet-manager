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

1. **That the apparatus loaded, and how much of it.** The boot triad's two
   dangerous cases — root is a satellite repo, root is the bare clone parent
   `/home/user` — are both SILENT: settings, hooks, skills and the auto-loaded
   CLAUDE.md go quiet with no error, and the session cannot tell "the rule did
   not apply" from "the rule never arrived". Two halves:
     · **Nothing loaded** — this hook did not run either, so its FIRING is the
       only signal, which is why the injected text names itself.
     · **This repo's `.claude/` did not auto-load, but its hooks are
       registered** — the state after `tools/install_root_hooks.py --apply`.
       That IS detectable, by comparing `CLAUDE_PROJECT_DIR` against this
       file's own location, and `_root_note` reports it. It reports only that
       much: the root could be a satellite repo with a full `.claude/` of its
       own, or the bare clone parent with none, and the comparison cannot tell
       them apart. From the inside both look exactly like a normal boot.
2. **Whether the six documents are still there.** Same discipline as
   `tools/check_doc_routes.py`: a pointer at a moved or deleted doc is worse
   than no pointer, because the session stops looking. Every path is checked
   with `isfile` — matching that checker's `Path.is_file()`, so a directory
   reusing a document's old pathname still reports as missing — and a missing
   one is named rather than printed as a live link.
3. **Which start this is.** `source` distinguishes a cold boot from a resume or
   a post-compaction continuation; the six-read mandate is written for the cold
   case, and re-injecting it verbatim after every compaction would spend context
   restating what the session already did.

CONTRACT (identical to every other advisory hook here)
------------------------------------------------------
· Never blocks. Exit 0 on every path, including a crash — with ONE deliberate
  exception: `KeyboardInterrupt` and `SystemExit` are re-raised, so a SIGINT
  still terminates. Fail-open is a promise about bugs, not a licence to outlive
  the process that owns us (`owner_review.py`, MEASURED 2026-08-08). Flagged as
  a contract violation by the Gemini pass on the R2 fixes and kept — but the
  bullet used to read as an absolute, which is why it now names its exception.
· Writes nothing to the repo — telemetry goes to /tmp, so a session trying to
  keep a clean tree never finds this in `git status`.
· Every firing is countable at /tmp/claude-session-start/log.jsonl, INCLUDING
  the skips. That is not decoration: `owner_review.py` shipped a silent-skip
  path, its absence went unnoticed for eighteen days, and this estate rates a
  false guardrail as costlier than a false wall. A mechanism whose absence is
  invisible is indistinguishable from a working one.

Unlike `route_docs.py`, this one is NOT silent-by-default and NOT deduplicated.
Those rules exist because an advisory that fires on every tool call becomes
noise the session learns to skip. `SessionStart` fires once per SESSION-START
TRANSITION — not once per session, since `compact` and `clear` fire it again in
a live session (Codex, fm #992 R3; the earlier "once per session by
construction" hid exactly the repeated-compaction population this file's own
source table handles). Either way it is bounded by transitions rather than by
tool calls, so there is no noise field to join — and the estate's own measured
finding on selective firing (`docs/findings/2026-08-06-provenance-mechanism-measured.md`
§ 8: *"fixed-and-always-on and blended-into-conversation both avoid the
test-signal; selective firing is the worst of the three"*) argues against making
it conditional on content.

VERIFY
------
    # cold/warm routing — `made-up` MUST come back cold, not warm
    for s in made-up startup clear resume compact fork; do
      echo "{\"session_id\":\"t\",\"source\":\"$s\"}" > /tmp/in.json
      python3 .claude/hooks/session_start.py < /tmp/in.json | head -c 20; echo " <- $s"
    done
    echo '{"session_id":"t"}' | python3 .claude/hooks/session_start.py   # absent -> cold
    # rescue path: root is NOT the repo — reads must still resolve, and say so
    echo '{"source":"startup"}' > /tmp/in.json
    CLAUDE_PROJECT_DIR=/home/user python3 .claude/hooks/session_start.py < /tmp/in.json \
      | grep -c "MISSING AT THIS HEAD"      # must be 0
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

# The documents live beside THIS FILE, so resolve them from __file__ and never
# from the session root. `<repo>/.claude/hooks/session_start.py` → up three.
#
# The first version read CLAUDE_PROJECT_DIR first, and Codex caught what that
# breaks (fm #992, P2): the two are the same directory in an ordinary boot and
# DIFFERENT in exactly the case this hook is installed for by
# `tools/install_root_hooks.py`. There, root is the bare clone parent
# `/home/user` while the reads are under `/home/user/fleet-manager` — so the
# env-first version would have reported all eight paths missing precisely on the
# rescue surface, or matched unrelated same-named files in another clone. A
# missing-doc warning that fires only when it is wrong is worse than none.
#
# Never `git rev-parse` here: a hook must not need a subprocess to find its own
# repo, and the rescue case has no repo at the session root to ask.
#
# `realpath`, not `abspath`: abspath does not resolve symlinks, and `_root_note`
# compares REPO against the session root with realpath on both sides. Mixing the
# two would make a symlinked checkout report a spurious "root is not this repo"
# warning — a false alarm in the one message whose whole value is that it only
# appears when something is genuinely wrong. Raised by the free-key Gemini pass
# on this fix commit (D-0019 cadence).
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# Set when Claude Code launched us. Compared against REPO rather than used as
# it: a mismatch means this repo's .claude/ did not auto-load, which is worth
# saying out loud — but NOT which root replaced it. See _root_note.
SESSION_ROOT = os.environ.get("CLAUDE_PROJECT_DIR")

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

# WARM is the closed set; everything else is cold. A resume or a
# post-compaction continuation already walked the contract, or had its context
# dropped and re-reading is cheaper than re-injecting; `fork` inherits the
# parent's context.
#
# Stated as the WARM set rather than the cold one because the first version had
# it the other way round and got the default backwards — Codex, fm #992 (P2).
# `cold = source in {"startup","clear"} or source == "unknown"` sends a
# genuinely unrecognised value (an upstream sixth `source`, a typo) down the
# WARM path, which is the opposite of what this file's own docstring, the hooks
# README table and the commit message all promised. Only the ABSENT case
# reached the cold default, which is exactly the case that was tested — the
# unrecognised-value path was asserted from reading the code and never run.
# Inverting it makes the closed set the thing that must be maintained, so a new
# upstream value fails safe instead of silently.
WARM_SOURCES = {"resume", "compact", "fork"}


def _log(rec: dict) -> None:
    try:
        os.makedirs(CACHE_DIR, exist_ok=True)
        with open(LOG, "a") as f:
            f.write(json.dumps(rec) + "\n")
    except Exception:
        pass  # telemetry must never be the thing that breaks a boot


def _present(rel: str) -> bool:
    """A REGULAR FILE at the path, not merely something at the path.

    `os.path.exists` returns true for a directory, so a moved document whose old
    pathname was reused by a directory would print as a live read and be omitted
    from both warnings (Codex, fm #992 R2, P2). That is weaker than the
    `tools/check_doc_routes.py` discipline this hook's docstring claims to
    share — that checker uses `Path.is_file()` — so the claim was wrong before
    this line was.
    """
    return os.path.isfile(os.path.join(REPO, rel))


def _missing_note(missing: list[str]) -> str:
    """The moved-read warning. Shown on EVERY start, warm ones included.

    Warm starts dropped this in the first version (Codex, fm #992, P2): the list
    was computed and then used only by the cold block, so a resumed session was
    handed `docs/current-state.md` as a live pointer even when it had moved.
    A dead route is worse on a resume than on a cold start, because a resumed
    session has more reason to trust a path it already used.
    """
    if not missing:
        return ""
    return (
        "\n\n⚠ " + str(len(missing)) + " orientation path(s) do not exist at "
        "this HEAD: " + ", ".join(missing) + ". Do not silently substitute a "
        "similar file — a moved read is a defect in the front door, and "
        "recording it is worth more than compensating for it."
    )


def _root_note() -> str:
    """Say so when the session root is not this repo — and no more than that.

    What the comparison ESTABLISHES: fleet-manager is not the session root, so
    this repo's `.claude/` did not auto-load and the hook is running from an
    installed registration.

    What it does NOT establish is which root produced the mismatch, and the
    first version asserted one anyway — "this is the multi-root boot… only the
    installer's hooks are live". `tools/install_root_hooks.py` targets whichever
    root the environment names, so the root can equally be a SATELLITE REPO
    whose own hooks, skills and CLAUDE.md are loaded and live (Codex, fm #992
    R2, P2). Naming the bare-clone-parent case would then be a confident wrong
    diagnosis in the one message whose value is that it only appears when
    something is genuinely off. So the note reports the fact and names both
    possibilities without picking.
    """
    if not SESSION_ROOT or os.path.realpath(SESSION_ROOT) == os.path.realpath(REPO):
        return ""
    return (
        f"\n\n⚠ SESSION ROOT IS NOT THIS REPO — root is {SESSION_ROOT}, the "
        f"reads above are under {REPO}. So this repo's .claude/ did not "
        "auto-load: its skills and CLAUDE.md are NOT available to you, and "
        "these hooks are running from an installed registration. What IS "
        "loaded depends on the root, which this check cannot see — a satellite "
        "repo brings its own .claude/, the bare clone parent brings none. "
        "Check `ls /root/.claude/projects/` if it matters; invoke this repo's "
        "skills by name, because nothing will route you to them."
    )


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
    lines += [
        "",
        "Also live, and not part of the six: docs/MAP.md (one line per area, "
        "CORE/TASK/RECORD) · docs/ESTATE.md (every repository, one line) · "
        "docs/activity/ (what sessions did ANYWHERE, including his laptop — "
        "this repo's .sessions/ is fleet-manager's work alone) · "
        "docs/traps.md (the recurring execution mistakes, delivered by route "
        "at the moment each one happens).",
        "",
        "This hook firing is proof that the hook apparatus loaded. When root is "
        "a satellite repo or the bare clone parent, it goes quiet with no error "
        "and nothing says so — see the root warning below if one is present.",
    ]
    return "\n".join(lines) + _missing_note(missing) + _root_note()


def _warm_block(source: str, missing: list[str]) -> str:
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
    ) + _missing_note(missing) + _root_note()


def rec(**kw) -> None:
    """One log line, timestamped. EVERY exit from main() goes through this."""
    _log({"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), **kw})


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        # Malformed or absent stdin is not a reason to spend a boot on a
        # traceback. Logged, because an unlogged skip is the defect this file's
        # header is about.
        return rec(skip="bad-stdin")

    # Valid JSON of the WRONG SHAPE parses fine and then raises downstream:
    # `[]` has no .get, `{"source": 1}` has no .lower. Both used to escape to
    # the module-level BaseException handler, which exits 0 WITHOUT logging — so
    # an upstream schema change would look exactly like a hook that never ran,
    # in a file whose own header calls that the false guardrail (Codex, fm #992
    # R2, P2). Shape is checked here; anything else that raises is caught and
    # logged by the wrapper below.
    if not isinstance(data, dict):
        return rec(skip="bad-payload", payload_type=type(data).__name__)

    raw = data.get("source")
    if raw is not None and not isinstance(raw, str):
        # Not fatal — an unreadable source is just an unknown one, and unknown
        # is cold. Recorded so a schema change is visible rather than assumed.
        rec(note="non-string-source", source_type=type(raw).__name__)
        raw = None
    # NO .lower() before the WARM_SOURCES test. Lower-casing widened the warm set
    # past the documented values — "RESUME" and "Resume" took the warm path while
    # the contract says the closed set is those exact strings and everything else
    # is cold (Codex, fm #992 R3, P2). It fails in the wrong direction: the whole
    # asymmetry argument is that an unrecognised value must get the FULL
    # contract, and a cased variant is an unrecognised value until upstream says
    # otherwise. Costing a resume ~500 tokens is the safe error here.
    source = raw or "unknown"

    missing = [p for p, _ in READS if not _present(p)]
    missing += [p for p in COMPANIONS if not _present(p)]

    # COLD is the default: warm is the closed set, everything else falls to the
    # full contract. Under-injecting on a real cold start loses the orientation
    # this hook exists to deliver; over-injecting on a warm one costs ~500
    # tokens. The asymmetry picks the default, and stating WARM as the closed
    # set is what makes an unrecognised value fail safe — see WARM_SOURCES.
    cold = source not in WARM_SOURCES
    text = _cold_block(missing) if cold else _warm_block(source, missing)

    rec(session=data.get("session_id"), source=source, cold=cold,
        missing=missing, chars=len(text), repo=REPO,
        session_root=SESSION_ROOT,
        root_moved=bool(SESSION_ROOT) and
        os.path.realpath(SESSION_ROOT) != os.path.realpath(REPO))

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
    except BaseException as exc:
        # BaseException rather than Exception: MEASURED 2026-08-08 in this
        # directory, a native panic (PanicException -> BaseException -> object)
        # escaped a narrower catch and the hook exited 1. A SessionStart hook
        # that exits non-zero starts the session with an error notice.
        #
        # And it LOGS before it swallows. Until fm #992 R2 this was a bare
        # `pass`, which made the contract three lines above ("every firing is
        # countable, including the skips") false for exactly the population that
        # matters — an unanticipated crash. That is the same defect this file's
        # header criticises owner_review.py for, shipped in the file criticising
        # it. `rec` has its own try, so a broken log cannot resurrect the crash.
        try:
            rec(skip="crashed", error=f"{type(exc).__name__}: {exc}"[:300])
        except BaseException:
            pass
    sys.exit(0)
