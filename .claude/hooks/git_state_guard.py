#!/usr/bin/env python3
"""PreToolUse advisory for the two git states that produced every conflict today.

Both failures on 2026-08-08 were the same shape: the repo state carried the
answer, the session acted from the plan instead. This hook computes the answer
and puts it in front of the action.

1. **Continuing a branch whose PR already squash-merged.** merge-on-green lands
   PRs as squashes, so the branch's own commits stop being ancestors of main
   while their CONTENT is fully merged. Committing or pushing more work on that
   branch guarantees a conflict — it caused fm#820's and fm#822's, and the owner
   had to point the second one out twice. Detection: a local-only commit whose
   subject reappears in origin/main's recent history suffixed ` (#N)`.

2. **Force-pushing over evidence.** The safe check before a force-push after a
   squash is a TREE comparison (is the remote head's content already in main?),
   not a commit listing — `git log --not origin/main` lists squash-merged work
   as "unmerged" by SHA and misled a session into a caption that its own output
   contradicted (seven `unmerged:` lines read past, push anyway; safe only by
   luck, established only afterwards). This hook runs the right comparison and
   injects the numbers, so the correct check is in context before the push.

Contract, same as every advisory here: never blocks, exits 0 on every path,
silence is the default, each distinct warning once per session. It computes
FACTS (diffs, subjects); the decision stays with the session — a subject match
can be legitimate (an intentionally recycled commit message), and the message
says so instead of pretending to be a verdict.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
STATE_DIR = Path(os.environ.get("TMPDIR", "/tmp")) / "claude-git-guard"
TIMEOUT = 10

GIT_CMD_RE = re.compile(r"\bgit\b[^|;&]*\b(push|commit)\b")
FORCE_RE = re.compile(r"\bgit\b[^|;&]*\bpush\b[^|;&]*(--force|-f\b)")
RESET_HARD_RE = re.compile(r"\bgit\b[^|;&]*\breset\b[^|;&]*--hard")


def git(*argv: str) -> str:
    p = subprocess.run(["git", *argv], cwd=REPO, capture_output=True,
                       text=True, timeout=TIMEOUT)
    return p.stdout.strip() if p.returncode == 0 else ""


def once(session: str, key: str) -> bool:
    """True the first time `key` is seen this session."""
    try:
        f = STATE_DIR / f"{session}.json"
        seen = set(json.loads(f.read_text())) if f.exists() else set()
        if key in seen:
            return False
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        f.write_text(json.dumps(sorted(seen | {key})))
        return True
    except Exception:
        return True  # losing state costs a duplicate line, never a silence


def squash_stack_warning(branch: str) -> str | None:
    """Local-only commits whose subjects reappear in main as squash merges."""
    local = git("log", "--format=%s", "origin/main..HEAD").splitlines()[:10]
    if not local:
        return None
    recent = git("log", "--format=%s", "-40", "origin/main").splitlines()
    hits = []
    for s in local:
        s = s.strip()
        if len(s) < 12:
            continue
        for m in recent:
            if m.startswith(s + " (#"):
                hits.append((s, m[m.rfind("(#"):].rstrip(")").lstrip("(")))
                break
    if not hits:
        return None
    listing = "\n".join(f"    · \"{s[:70]}\" merged as {n}" for s, n in hits)
    return (
        f"Branch `{branch}` carries commits whose subjects already merged into "
        f"main as squashes:\n{listing}\n"
        "  If those ARE this work, the PR merged and this branch is stale — "
        "continuing on it guarantees a conflict (it caused fm#820's and "
        "fm#822's). Reset first: `git fetch origin main && git checkout -B "
        f"{branch} origin/main`, then re-apply only what is new.\n"
        "  If a subject is legitimately recycled (e.g. a fresh telemetry "
        "delta), check content instead: `git diff --stat origin/main` shows "
        "what this branch truly adds."
    )


def force_push_report(branch: str) -> str | None:
    """The tree comparison that IS the safety check for a post-squash force."""
    remote_head = git("rev-parse", f"origin/{branch}")
    if not remote_head:
        return None  # no remote counterpart — nothing to discard
    vs_main = git("diff", "--name-only", f"origin/{branch}", "origin/main")
    files = [f for f in vs_main.splitlines() if f.strip()]
    if files:
        head5 = "".join(f"\n    · {f}" for f in files[:5])
        more = f"\n    · … and {len(files) - 5} more" if len(files) > 5 else ""
        verdict = (f"differs from origin/main in {len(files)} file(s):"
                   f"{head5}{more}\n  Those differences are DISCARDED by this "
                   "force-push unless your HEAD carries them. Stop and inspect.")
    else:
        verdict = ("is content-identical to origin/main — everything being "
                   "discarded is already merged; the force is safe.")
    return (
        f"Force-push check (computed, not recalled): remote head "
        f"{remote_head[:7]} {verdict}\n"
        "  Note: `git log --not origin/main` is the WRONG check after a squash "
        "— it lists fully-merged content as unmerged by SHA. Trees decide, "
        "commits mislead (measured 2026-08-08: seven misleading `unmerged:` "
        "lines on a push that tree-comparison proved safe)."
    )


def dirty_reset_warning() -> str | None:
    """Tracked modifications a `reset --hard` is about to destroy.

    Added the hour it happened (2026-08-08): a session ran `reset --hard` to
    drop a one-commit probe while its OWN uncommitted hook edits sat in the
    tree — three tracked-file edits destroyed, rebuilt from context. The rule
    ("before deleting or overwriting, look at the target") was in the session's
    instructions; the look is what this injects.
    """
    # Parse by split, not by index: the shared git() helper strips the whole
    # output, which eats the FIRST line's leading status-space and shifted its
    # path by one character ("claude/hooks/…" for ".claude/hooks/…") in the
    # first test run of this very warning. A guard that misnames the files it
    # is protecting teaches the wrong lesson.
    dirty = []
    for ln in git("status", "--porcelain").splitlines():
        parts = ln.strip().split(None, 1)
        if len(parts) == 2 and parts[0] != "??":
            dirty.append(parts[1])
    if not dirty:
        return None
    head5 = "".join(f"\n    · {f}" for f in dirty[:5])
    more = f"\n    · … and {len(dirty) - 5} more" if len(dirty) > 5 else ""
    return (
        f"`reset --hard` will DESTROY uncommitted changes in {len(dirty)} "
        f"tracked file(s):{head5}{more}\n"
        "  Untracked files survive; these do not. Stash or commit first if any "
        "of this is work. (This exact command destroyed three tested hook edits "
        "on 2026-08-08 — the probe being cleaned up was one commit; the "
        "collateral was the session's own uncommitted build.)"
    )


def main() -> int:
    try:
        event = json.loads(sys.stdin.read() or "{}")
    except Exception:
        return 0
    if event.get("tool_name") != "Bash":
        return 0
    cmd = str((event.get("tool_input") or {}).get("command", ""))

    session = str(event.get("session_id") or "nosession")
    notes = []

    if RESET_HARD_RE.search(cmd):
        r = dirty_reset_warning()
        if r:  # every time — each firing names different files about to die
            notes.append(r)

    m = GIT_CMD_RE.search(cmd)
    if not m:
        if notes:
            json.dump({"hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": "\n\n".join(notes)},
                "suppressOutput": True}, sys.stdout)
        return 0

    branch = git("symbolic-ref", "--short", "HEAD") or "HEAD"

    if FORCE_RE.search(cmd):
        git("fetch", "origin", branch, "main")
        r = force_push_report(branch)
        if r and once(session, f"force:{branch}:{git('rev-parse', 'HEAD')[:7]}"):
            notes.append(r)
    elif m.group(1) == "push":
        git("fetch", "origin", "main")

    w = squash_stack_warning(branch)
    if w and once(session, f"stack:{branch}"):
        notes.append(w)

    if not notes:
        return 0
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": "\n\n".join(notes),
            },
            "suppressOutput": True,
        },
        sys.stdout,
    )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyboardInterrupt, SystemExit):
        raise
    except BaseException:
        sys.exit(0)  # fail open, always — advisory must never trap the session
