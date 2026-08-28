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

# Repository names and their human aliases share one token boundary. A final
# full stop is prose punctuation and a terminal ``.git`` is a repository URL
# suffix, while ``repo.component``, ``repo.gitignore``, ``repo-extra`` and
# ``repo2`` are longer slug-like tokens and must not route ``repo``. Keep the
# same boundary on the JSON route table's repository patterns below; otherwise
# a permissive Layer-2 alias can re-add the comment index that this matcher
# deliberately rejected.
REFERENCE_START = r"(?<![A-Za-z0-9._-])"
REFERENCE_END = (
    r"(?![A-Za-z0-9_-]|\."
    r"(?!git(?:$|\.(?![A-Za-z0-9_-])|[^A-Za-z0-9._/\\-]))"
    r"[A-Za-z0-9_-])"
)


def reference_pattern(body: str) -> str:
    """Wrap one repository name/alias body in the shared token boundary."""
    return rf"{REFERENCE_START}(?:{body}){REFERENCE_END}"


# Each row is (bounded alias body, repositories, Layer-2 repositories shadowed
# by this meaning).  Shadows resolve documented product vocabulary that embeds
# another product's name: "Substrate Kit Dashboard" is the dashboard experiment,
# not the kit, and Slingy-Spider-server/community-bot work is spider-bot, not the
# game.  An independently named canonical repository still wins below, so a
# prompt that explicitly asks to compare both products continues to route both.
COMMENT_ALIAS_REPOS = (
    (
        reference_pattern(r"menno[- ]creator[- ]kit|the[- ]creator[- ]kit|the[- ]freecad[- ]thing"),
        ("creator-kit",),
        (),
    ),
    (
        reference_pattern(r"(?:the[- ])?spider[- ]bot"),
        ("spider-bot",),
        (),
    ),
    (
        reference_pattern(
            r"(?:the[- ])?community[- ]bot"
            r"(?:[- ](?:in|of|for)[- ](?:the[- ])?slingy[- ]spider"
            r"(?:[- ](?:discord[- ])?server)?)?|game[- ]community[- ]bot|"
            r"(?:the[- ])?slingy[- ]spider"
            r"(?:['’]s[- ]community[- ]bot|"
            r"[- ](?:(?:discord[- ])?server|(?:community[- ])?bot))"
        ),
        ("spider-bot",),
        ("spider-swing",),
    ),
    (
        reference_pattern(r"slingy[- ]spider"),
        ("spider-swing",),
        (),
    ),
    (
        reference_pattern(
            r"couch[- ]legend|idle[- ]stoner|(?:the[- ])?lucid[- ]chronicle"
        ),
        ("couch-legend",),
        (),
    ),
    (
        reference_pattern(
            r"(?:the|my)[- ]websites|websites[- ]repo|control[- ]plane|"
            r"botsite|(?:the[- ])?review[- ]site"
        ),
        ("websites",),
        (),
    ),
    (
        reference_pattern(r"product[- ]forge|phone[- ]controller|controller[- ]app"),
        ("product-forge",),
        (),
    ),
    (reference_pattern(r"superbot[- ]games"), ("superbot-games",), ()),
    (
        reference_pattern(r"superbot[- ]idle|the[- ]idle[- ]engine"),
        ("superbot-idle",),
        (),
    ),
    (
        reference_pattern(r"superbot[- ]mineverse|mineverse"),
        ("superbot-mineverse",),
        (),
    ),
    (
        reference_pattern(r"superbot[- ]plugin[- ]hello|plugin[- ]hello"),
        ("superbot-plugin-hello",),
        (),
    ),
    (
        reference_pattern(r"superbot[- ]world"),
        ("superbot-games", "superbot-idle", "superbot-mineverse", "superbot-plugin-hello"),
        (),
    ),
    (
        reference_pattern(r"superbot[- ]next|superbot[- ]2\.0|the[- ](?:old[- ])?rebuild"),
        ("superbot-next",),
        (),
    ),
    (
        reference_pattern(r"the[- ]kit(?![- ]dashboard)|kit[- ]release"),
        ("substrate-kit",),
        (),
    ),
    (
        reference_pattern(
            r"venture[- ]lab|stripe[- ]webhook[- ]test[- ]kit|(?:the[- ])?night[- ]kiln|"
            r"lull/dreamline|dreamline|ultramarine"
        ),
        ("venture-lab",),
        (),
    ),
    (reference_pattern(r"mdverify"), ("codetool-lab-opus4.8",), ()),
    (reference_pattern(r"envdrift"), ("codetool-lab-fable5",), ()),
    (reference_pattern(r"cfgdiff"), ("codetool-lab-sonnet5",), ()),
    (
        reference_pattern(r"codetool[- ]labs?"),
        ("codetool-lab-opus4.8", "codetool-lab-fable5", "codetool-lab-sonnet5"),
        (),
    ),
    (reference_pattern(r"shift[- ]calendar"), ("shiftlife",), ()),
    (
        reference_pattern(
            r"lumen[- ]drift|gba[- ](?:project|game|games|rom|roms|homebrew)|"
            r"wickroad|brineward|underroot"
        ),
        ("gba-homebrew",),
        (),
    ),
    (reference_pattern(r"pokemon[- ](?:mod|hack)"), ("pokemon-mod-lab",), ()),
    (reference_pattern(r"pokemon[- ]mod[- ]lab"), ("pokemon-mod-lab",), ()),
    (reference_pattern(r"ideas[- ]lab"), ("idea-engine", "sim-lab"), ()),
    (reference_pattern(r"idea[- ]engine"), ("idea-engine",), ()),
    (reference_pattern(r"sim[- ]lab"), ("sim-lab",), ()),
    (
        reference_pattern(r"trading[- ]strategy|trading[- ]lab"),
        ("trading-strategy",),
        (),
    ),
    (reference_pattern(r"curious[- ]research"), ("curious-research",), ()),
    (
        reference_pattern(
            r"(?:the[- ])?kit[- ]dashboard|substrate[- ]kit[- ](?:app|dashboard)"
        ),
        ("Substrate-kit-app",),
        ("substrate-kit",),
    ),
)

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


_HEREDOC = re.compile(
    r"<<-?\s*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\1\s*\n(.*?)^\s*\2\s*$",
    re.DOTALL | re.MULTILINE,
)


def authored_only(text: str) -> str:
    """Return only the prose a Bash command WRITES — its heredoc bodies.

    The complement of `code_only()`. That one exists because a quoted MENTION of
    an action must not spend an action guard; this one exists because an actual
    AUTHORED DOCUMENT must not escape a claim guard just because it arrived
    through Bash instead of Write.

    The failure this exists to stop, MEASURED 2026-08-28 on this session's own
    transcript. Eight routes are registered `Edit`/`Write` only — the whole
    claim-quality set: `stamping-a-measured-claim`, `claim-beyond-the-sample`,
    `absence-claim`, `recording-a-wall`, and the four card-discipline routes.
    Auto mode's standing instruction is to author through Bash ("make file
    changes with sed, heredocs, or short scripts, rather than using the
    dedicated Read, Edit, or Write tools"), so a session following it writes
    every document via `cat > f <<'EOF'` and **all eight go silent for the whole
    session** — with no error and nothing to notice.

    Measured A/B on this hook, same offending text both ways:

        Write tool      -> TRAP-001 and TRAP-004 both fire
        Bash heredoc    -> no output, exit 0

    That session then published a `MEASURED` label on owner-console state, a
    checker count taken from grep hits, and a commit count from memory — three
    of the exact errors those two routes exist to catch, all of them written
    through a heredoc.

    Why heredoc bodies ONLY, and not the whole command: the command is code, and
    matching claim patterns against code re-creates the fm #923 failure in the
    opposite direction — `grep -n 'MEASURED' docs/traps.md` would spend the
    route and leave the real write unwarned. A heredoc body is unambiguously
    authored prose, which is the only thing these routes should read.
    """
    return "\n".join(m.group(3) for m in _HEREDOC.finditer(text))


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


def comment_repository_names() -> list[str]:
    """Repositories with stable indexes, from the generated root projection."""
    try:
        data = json.loads((REPO / "docs/owner-comments/index.json").read_text())
        names = [row["repository"] for row in data["repositories"]]
        return [
            name for name in names
            if isinstance(name, str)
            and (REPO / f"docs/owner-comments/{name}/README.md").is_file()
        ]
    except Exception:
        return []


def mentioned_repositories(
    text: str,
    repositories: list[str],
    *,
    strip_checkout_prefix: bool = False,
) -> tuple[set[str], set[str]]:
    """Resolve canonical slugs and product aliases by longest contained match.

    This makes a full canonical slug beat a generic prefix (the exact
    ``codetool-lab-opus4.8`` must not fan out through ``codetool labs``), while
    a qualified product alias beats a shorter canonical prefix (``SuperBot
    2.0`` is ``superbot-next``, not also ``superbot``).  The second result is
    canonical repositories shadowed by a longer alias; matched legacy routes
    must not re-add them later.
    """
    subject = text
    prompt_mentions_checkout = (
        not strip_checkout_prefix
        and "fleet-manager" in repositories
        and any(
            re.search(reference_pattern(re.escape(spelling)), text, re.I)
            for spelling in {str(REPO), REPO.as_posix()}
        )
    )
    if strip_checkout_prefix:
        # Tool payloads commonly carry absolute paths. Fleet Manager's checkout
        # directory is plumbing there, not a repository mention: without
        # stripping it, every absolute Read from this tree spuriously routes
        # ``fleet-manager`` feedback. Owner prompt text is intentional content,
        # though, and an absolute checkout selection must remain discoverable.
        for prefix in {str(REPO) + os.sep, REPO.as_posix() + "/"}:
            subject = subject.replace(prefix, "")
        # Repository-relative routing uses POSIX paths. Normalize tool payloads
        # after removing this checkout's plumbing so Windows absolute paths do
        # not become invisible (or route the checkout itself as Fleet Manager).
        subject = subject.replace("\\", "/")
    else:
        # Prompt text may name this checkout or a sibling whose path begins
        # with it.  The full-path decision above owns that meaning; remove the
        # checkout plumbing before canonical-slug matching so a CI layout such
        # as ``.../fleet-manager/fleet-manager-old`` cannot route the ancestor
        # directory as an explicit Fleet Manager mention.
        for spelling in {str(REPO), REPO.as_posix()}:
            subject = re.sub(re.escape(spelling), "", subject, flags=re.I)

    candidates: list[
        tuple[int, int, frozenset[str], bool, frozenset[str]]
    ] = []
    for repository in repositories:
        pattern = reference_pattern(re.escape(repository))
        for match in re.finditer(pattern, subject, re.I):
            candidates.append(
                (
                    match.start(),
                    match.end(),
                    frozenset({repository}),
                    True,
                    frozenset(),
                )
            )
    for pattern, aliases, route_shadows in COMMENT_ALIAS_REPOS:
        for match in re.finditer(pattern, subject, re.I):
            candidates.append(
                (
                    match.start(),
                    match.end(),
                    frozenset(aliases),
                    False,
                    frozenset(route_shadows),
                )
            )

    selected: set[str] = set()
    if prompt_mentions_checkout:
        selected.add("fleet-manager")
    shadowed: set[str] = set()
    for start, end, names, canonical, route_shadows in candidates:
        dominated = any(
            other_start <= start
            and other_end >= end
            and other_end - other_start > end - start
            for (
                other_start,
                other_end,
                _other_names,
                _canonical,
                _route_shadows,
            ) in candidates
        )
        if dominated:
            if canonical:
                shadowed.update(names)
        else:
            selected.update(names)
            shadowed.update(route_shadows)
    return selected, shadowed


def reference_match(pattern: str, text: str) -> bool:
    """Match a route-table repository pattern at the shared token boundary."""
    for match in re.finditer(pattern, text, re.I):
        start, end = match.span()
        if start and re.match(r"[A-Za-z0-9._-]", text[start - 1]):
            continue
        if end < len(text):
            suffix = text[end:]
            terminal_git = re.match(
                r"\.git(?:$|\.(?![A-Za-z0-9_-])|[^A-Za-z0-9._/\\-])",
                suffix,
                re.I,
            )
            if not terminal_git and re.match(
                r"[A-Za-z0-9_-]|\.[A-Za-z0-9_-]", suffix
            ):
                continue
        return True
    return False


def repositories_for_route(route: dict) -> set[str]:
    """Repository identity carried by a matched Layer-2 route."""
    result: set[str] = set()
    for doc in route.get("docs", []):
        match = re.fullmatch(r"docs/repos/([^/]+)/README\.md", doc)
        if match:
            result.add(match.group(1))
    return result


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
    normalized_target_path = target_path.replace("\\", "/")
    checkout_prefix = REPO.as_posix().rstrip("/") + "/"
    if normalized_target_path.casefold().startswith(checkout_prefix.casefold()):
        normalized_target_path = normalized_target_path[len(checkout_prefix):]
    while normalized_target_path.startswith("./"):
        normalized_target_path = normalized_target_path[2:]

    session = str(event.get("session_id") or "nosession")
    fired = already_fired(session)
    hits = []
    available_comments = comment_repository_names()
    if tool in DEFAULT_TOOLS or tool == PROMPT_EVENT:
        comment_repositories, shadowed_comment_repositories = (
            mentioned_repositories(
                text,
                available_comments,
                strip_checkout_prefix=tool != PROMPT_EVENT,
            )
        )
    else:
        comment_repositories, shadowed_comment_repositories = set(), set()
    explicitly_mentioned_comments = set(comment_repositories)

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
        route_repositories = repositories_for_route(route)
        # A documented product alias may embed another repository's product
        # name (for example, "Substrate Kit Dashboard").  Do not let that
        # shorter Layer-2 route steal the prompt back.  A separately named
        # canonical repository is explicit and therefore overrides the shadow.
        effective_shadows = (
            shadowed_comment_repositories - explicitly_mentioned_comments
        )
        unshadowed_route_repositories = route_repositories - effective_shadows
        if route_repositories and not unshadowed_route_repositories:
            continue
        docs = [d for d in route.get("docs", []) if (REPO / d).is_file()]
        if not docs:
            continue
        # Already opening one of these docs? Then the configured route has
        # nothing to add. The independent owner-comment route below still sees
        # a canonical repo slug in the path and can surface its stable index.
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
        if any(d in text for d in docs) and tool != "Bash" and (
                not route.get("tools") or tool in DEFAULT_TOOLS):
            fired.add(rid)
            continue
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
        # `authored_only` narrows a Bash command to its heredoc bodies so a
        # claim guard sees a document authored via `cat > f <<'EOF'` exactly as
        # it sees one authored with Write. Scoped to Bash: for Write/Edit the
        # text IS the authored content already, and narrowing it there would
        # blind the route to the ordinary case.
        if tool == "Bash" and route.get("authored_only"):
            match_text = authored_only(text)
        elif route.get("code_only"):
            match_text = code_only(text)
        else:
            match_text = text
        repository_reference_route = bool(route_repositories) or route.get(
            "docs"
        ) == ["docs/ESTATE.md"]
        try:
            if repository_reference_route:
                matched = any(
                    reference_match(pattern, match_text)
                    for pattern in route.get("when", [])
                )
            else:
                matched = any(
                    re.search(pattern, match_text, re.I)
                    for pattern in route.get("when", [])
                )
            if not matched:
                continue
        except re.error:
            continue  # a bad pattern silences its own route, never the hook
        fired.add(rid)
        hits.append((docs, route.get("says", "")))
        comment_repositories.update(
            unshadowed_route_repositories
        )

    for repository in available_comments:
        if repository not in comment_repositories:
            continue
        comment_route_id = f"owner-comments-{repository.lower()}"
        if comment_route_id in fired:
            continue
        comment_index = f"docs/owner-comments/{repository}/README.md"
        if tool != "Bash" and normalized_target_path == comment_index:
            fired.add(comment_route_id)
            # A self-read is intentionally silent, but it still consumes this
            # once-per-session pointer. Persist before the no-hit return below.
            remember(session, fired)
            continue
        fired.add(comment_route_id)
        hits.append(
            (
                [comment_index],
                f"Owner feedback for {repository}: open the Unconsumed section "
                "and each linked JSON record before acting. Consumed history is "
                "preserved but is not active work. The entire record and its "
                "metadata are public. Never put credentials, private-repository "
                "contents or private-only URLs, third-party contact details, or "
                "unreleased specifics here; the full contract is at "
                "docs/owner-comments/README.md.",
            )
        )

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
