#!/usr/bin/env python3
"""PreToolUse + UserPromptSubmit hook: surface the estate's own doc before a
session probes blind — or before it starts work on a repo it has a folder for.

The failure this exists to stop, measured 2026-08-05: a session wanted a
multi-turn Gemini conversation, fetched the `generativelanguage` discovery
document, found no `interactions` endpoint, and wrote "unavailable" into the
capability ledger — while `docs/providers/gemini.md:151` carried the working
recipe the whole time. Prose did not prevent it; the same session had authored
the rule it broke, three hours earlier.

So this is a mechanism, not another rule. When a tool call mentions something
the estate has already written down, the hook injects the doc path and one
sentence of what it says.

Design constraints, in priority order:

1. **Never block.** Advisory only, exit 0 on every path including a crash. A
   hook that can stop work will eventually stop the wrong work.
2. **Silence is the default.** It fires only when a route matches AND the doc
   exists AND that route has not already fired this session. An agent tries to
   satisfy whatever appears in its feedback channel, so a channel that is
   usually empty is the only kind worth writing to.
3. **No repo writes.** Session state lives in /tmp, keyed by session id, so
   running the hook never dirties the tree the session is trying to keep clean.

The second event exists for a different failure, added 2026-08-08. On
`PreToolUse` the hook reads TOOL INPUT ONLY, so saying "this session is for
spider-swing" routes nothing until the session itself happens to grep that
string — the retrieval fires after orientation instead of before it. On
`UserPromptSubmit` naming a repo pulls its Layer 2 `docs/repos/<name>/README.md`
in directly, which is what lets Layer 1 stay light: the boot file need not
describe each repo, because naming one fetches it.

Prompt routing is **opt-in per route** (`"tools": ["UserPromptSubmit", ...]`).
Adding the event to DEFAULT_TOOLS instead would have switched all 21 existing
probe routes onto the owner's prose at once — patterns written to match a shell
command or a URL, now matching conversation. Silence is the default here, and a
blast radius of "every route, immediately" is not how to keep it.

Wired by tools/install_root_hooks.py, which installs into whichever directory
is actually the session root — see .claude/hooks/README.md for why that is not
always this repo.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
ROUTES = Path(__file__).resolve().parent / "doc-routes.json"
STATE_DIR = Path(os.environ.get("TMPDIR", "/tmp")) / "claude-doc-routes"

# Where each tool hides the text worth matching against. Anything not listed
# falls back to a bounded JSON dump of the whole input.
FIELDS = {
    "Bash": ("command",),
    "WebFetch": ("url", "prompt"),
    "Read": ("file_path",),
    "Glob": ("pattern", "path"),
    "Grep": ("pattern", "path", "glob"),
    # Write/Edit match on what is being WRITTEN, not on the path — the route
    # that matters here is "you are recording a wall", and that lives in the
    # prose. Kept off the default tool set below so a doc edit that merely
    # quotes a hostname does not trip every probe route.
    "Write": ("file_path", "content"),
    "Edit": ("file_path", "new_string"),
}

# A route with no `tools` key is a probe route: it fires when a session is
# about to go ask a vendor something. Content routes opt in explicitly.
# UserPromptSubmit is deliberately NOT here — see the module docstring.
DEFAULT_TOOLS = ("Bash", "WebFetch", "Read", "Glob", "Grep")

PROMPT_EVENT = "UserPromptSubmit"
LAYER2_INDEX_RE = re.compile(r"^docs/repos/([^/]+)/README\.md$")

# Session plumbing, never content. Only used by the defensive fallback below —
# without this, a `cwd` or a `transcript_path` could trip a route on its own.
EVENT_NOISE = {
    "session_id", "transcript_path", "cwd", "permission_mode",
    "hook_event_name", "prompt_id", "tool_use_id", "session_title",
}


def haystack(event: dict) -> tuple[str, str]:
    """Return (route-matching key, text to match against).

    The key is the tool name for PreToolUse and the literal event name for
    UserPromptSubmit, so both share one `tools` opt-in list on a route.

    MEASURED 2026-08-08: UserPromptSubmit carries no `tool_input` at all — the
    message arrives as a TOP-LEVEL `prompt` key, sibling to `hook_event_name`.
    Read out of the shipped binary (`/opt/claude-code/bin/claude`, not
    stripped), which builds the payload as
    `{...,hook_event_name:"UserPromptSubmit",prompt:e,...}`. The public hooks
    reference does not publish this field, so it was verified rather than
    assumed — and the fallback below means a future rename degrades to
    slightly-noisier matching instead of silence.
    """
    if (event.get("hook_event_name") or "") == PROMPT_EVENT:
        text = event.get("prompt")
        if isinstance(text, str) and text.strip():
            return PROMPT_EVENT, text
        return PROMPT_EVENT, "\n".join(
            v for k, v in event.items()
            if k not in EVENT_NOISE and isinstance(v, str)
        )[:4000]

    tool = event.get("tool_name", "")
    payload = event.get("tool_input") or {}
    keys = FIELDS.get(tool)
    if keys:
        return tool, "\n".join(str(payload.get(k, "")) for k in keys)
    return tool, json.dumps(payload)[:4000]


def code_only(text: str) -> str:
    """Blank single/double-quoted spans, preserving length and separators count.

    A Bash command is code; its quoted arguments are DATA. A route that guards an
    ACTION (`git push`) must not fire on a quoted mention of that action, because
    firing consumes it once-per-session and the real action then goes unwarned.
    MEASURED 2026-08-23 (Codex, fm #923): `grep -n '; git push' docs/traps.md;
    curl api.github.com/...` stored `card-flip-before-push` and the next real
    `git push` produced nothing.

    Opt-in per route via `"code_only": true` — it is NOT safe globally: the
    `github-api` route matches URLs that legitimately live inside quotes.
    """
    out, quote = [], None
    for ch in text:
        if quote:
            out.append(" " if ch != quote else ch)
            if ch == quote:
                quote = None
        elif ch in "'\"":
            quote = ch
            out.append(ch)
        else:
            out.append(ch)
    return "".join(out)


def already_fired(session: str) -> set[str]:
    try:
        return set(json.loads((STATE_DIR / f"{session}.json").read_text()))
    except Exception:
        return set()


def remember(session: str, fired: set[str]) -> None:
    try:
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        (STATE_DIR / f"{session}.json").write_text(json.dumps(sorted(fired)))
    except Exception:
        pass  # advisory state; losing it costs one duplicate line


def routed_docs(route: dict) -> list[str]:
    """Return existing route docs plus the repo's stable comment index.

    Owner comments use arbitrary durable ids, while this hook can route only
    literal files. Every Layer-2 repository route therefore carries its stable
    ``docs/owner-comments/<repo>/README.md`` companion automatically. The
    generated index exists for every ESTATE row; this small rule avoids a
    parallel 20-entry hand-maintained list in ``doc-routes.json``.
    """
    docs: list[str] = []
    for candidate in route.get("docs", []):
        if (REPO / candidate).is_file() and candidate not in docs:
            docs.append(candidate)
        match = LAYER2_INDEX_RE.fullmatch(candidate)
        if match:
            companion = f"docs/owner-comments/{match.group(1)}/README.md"
            if (REPO / companion).is_file() and companion not in docs:
                docs.append(companion)
    return docs


def main() -> int:
    try:
        event = json.loads(sys.stdin.read() or "{}")
    except Exception:
        return 0

    tool, text = haystack(event)
    if not text.strip():
        return 0

    try:
        routes = json.loads(ROUTES.read_text())["routes"]
    except Exception:
        return 0

    # The actual edited path, NOT the concatenated haystack. A route that must
    # only fire on a class of FILE has to test the path field itself: haystack()
    # joins file_path with the written content, so prose that merely NAMES a path
    # satisfies a path pattern searched over the combination. MEASURED 2026-08-24
    # (Codex, fm #938): an Edit of docs/traps.md whose new_string mentioned
    # `.sessions/example.md` and a `Status: complete` header fired
    # `card-flip-to-complete` and spent it — the real card flip later in that
    # session was SILENT. Same class as fm #923, one field deeper.
    target_path = str((event.get("tool_input") or {}).get("file_path") or "")

    session = str(event.get("session_id") or "nosession")
    fired = already_fired(session)
    hits = []

    for route in routes:
        rid = route.get("id", "")
        # `repeat` routes are never spent. Once-per-session is right for a
        # REFERENCE pointer (say it once, the agent has it) and wrong for an
        # ACTION guard, whose whole job is to speak at each occurrence of the
        # action. Three measured incidents are the same shape — fm #922, fm #923
        # and fm #937 — and the first two were patched by narrowing what CONSUMES
        # the route, which fixes the instance and leaves the class. MEASURED
        # 2026-08-24 (Codex, fm #938) on the real sequence: write red card -> push
        # -> flip to complete -> push. Steps 3 and 4 — the only two that matter —
        # were BOTH silent, because step 1 spent `card-status-write` and step 2
        # spent `card-flip-before-push`. Opt-in per route, like `code_only`:
        # blanket repetition would nag on every reference route.
        if rid in fired and not route.get("repeat"):
            continue
        if tool not in tuple(route.get("tools") or DEFAULT_TOOLS):
            continue
        docs = routed_docs(route)
        if not docs:
            continue
        # Suppress each doc already being opened. Most routes have one, so that
        # still means the hook has nothing to add; Layer-2 routes now have the
        # stable owner-comment companion and can surface just that unopened doc.
        # Applies to probe routes AND to explicit read-event routes (Codex on
        # fm #878: a folder route re-fired on the very Read its prompt half had
        # just directed, repeating "read this file" onto the read itself).
        # Content routes (Edit/Write) still fire ON their own doc — that is
        # the entire point of the wall-recording route; prompt routes are
        # untouched (a prompt naming a doc path is not an open of it).
        # …but NOT for a pre-execution guard. A Bash command that merely NAMES
        # the doc (`grep -c TRAP docs/traps.md`) is not an agent reading it, and
        # marking the route fired there silently disarms the guard for the rest
        # of the session. MEASURED 2026-08-23 (Codex, fm #922): one combined
        # command — `grep docs/traps.md; curl api.github.com/...` — persisted
        # ["card-flip-before-push", …] because the github-api route supplied a
        # hit, and the next REAL `git push` produced nothing. fm #920 merged
        # unreviewed behind exactly that silence. The fm #878 defect this branch
        # exists for was a Read re-firing onto its own directed read, so scoping
        # the exemption away from Bash leaves that fix intact.
        if tool != "Bash" and (
                not route.get("tools") or tool in DEFAULT_TOOLS):
            unopened = [doc for doc in docs if doc not in text]
            if not unopened:
                fired.add(rid)
                continue
            # A Layer-2 read still has one useful companion to surface: the
            # stable owner-comment index. Suppress only paths actually being
            # opened, not the whole route.
            docs = unopened
        # `path_when` is checked against the file_path FIELD alone, never the
        # haystack, so naming a path in prose cannot satisfy it (fm #938).
        path_pats = route.get("path_when") or []
        if path_pats:
            try:
                if not target_path or not any(
                        re.search(pp, target_path, re.I) for pp in path_pats):
                    continue
            except re.error:
                continue

        # A route guarding an ACTION matches against code with quoted data
        # blanked, so a mention inside an argument cannot consume it (fm #923).
        match_text = code_only(text) if route.get("code_only") else text
        try:
            if not any(re.search(p, match_text, re.I) for p in route.get("when", [])):
                continue
        except re.error:
            continue  # a bad pattern silences its own route, never the hook
        fired.add(rid)
        hits.append((docs, route.get("says", "")))

    if not hits:
        return 0
    remember(session, fired)

    if tool == PROMPT_EVENT:
        lines = [
            "You named something this estate keeps its own record for. Read "
            "the entry point below BEFORE attaching the repo or searching for "
            "it — it exists so orientation costs one read instead of a sweep."
        ]
    else:
        lines = [
            "This estate has already written down how this works. Read the "
            "doc before deriving the behaviour from a probe — a probe that fails "
            "tells you about one call, not about what is possible."
        ]
    for docs, says in hits:
        lines.append("")
        lines.append("· " + " + ".join(f"`{d}`" for d in docs))
        if says:
            lines.append("  " + says)

    json.dump(
        {
            # Must be the event actually being handled — the host validates
            # hookSpecificOutput against a schema discriminated on this field.
            "hookSpecificOutput": {
                "hookEventName": PROMPT_EVENT if tool == PROMPT_EVENT else "PreToolUse",
                "additionalContext": "\n".join(lines),
            },
            "suppressOutput": True,
        },
        sys.stdout,
    )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # fail open, always
