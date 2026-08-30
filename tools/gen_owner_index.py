#!/usr/bin/env python3
"""gen_owner_index.py — sweep every surface that holds something waiting on the
owner and generate ONE index of it.

================================ PROVENANCE ================================
Why added : Owner, live 2026-08-30, in the fresh-start structure sitting:
            "We should create a folder directed at me, so I can see everything
            that needs my attention at once. For example the Ideas, any
            decisions I should make, open questions, and the files I was
            looking for yesterday, those that explain the intent of all the
            repos, I could not find them so maybe you can."
            He had gone looking for the per-repo intent files, failed to find
            them, and concluded from that failure that the repo was less
            structured than he thought. MEASURED the same day: grepping the
            per-repo intent path across README.md, docs/MAP.md,
            .claude/CLAUDE.md, docs/repos/README.md and docs/current-state.md
            returns ZERO hits; the only pointer in the tree is inside
            docs/owner-queue.md, itself one of the surfaces he could not find
            things in.
What it does: reads five source surfaces and writes owner/README.md.
            1. docs/owner-queue.md   -> Decide  (OQ- entries, open ones only)
            2. docs/repos/*/intent.md + docs/intent.md -> Answer (the ❓ lines)
            3. owner-guidance docs + the prepared prompts -> Read and edit
            4. idea backlog + unconsumed owner comments   -> Triage
            5. owner/*.md siblings                        -> Read now
Design    : GENERATED, never hand-maintained. The truth stays in the source
            files; this only aggregates. A hand-kept "needs Menno" page would
            be the highest-churn document in the repo and the first to rot,
            which is the exact failure the owner asked us to fix. Same shape as
            the two generated indexes this estate already relies on
            (docs/owner-comments/*/README.md, docs/planning/idea-backlog.md).
Honest nulls: a source that cannot be read is reported as unreadable IN the
            output, never silently skipped — an index that hides a missing
            surface is worse than no index.
Date      : 2026-08-30
Reliability: The owner-queue status classification is the only judgement here;
            every other step is a literal extraction. Entries whose header
            carries "(original body)" are historical duplicates kept for their
            evidence base and are deliberately excluded.
============================================================================
"""

from __future__ import annotations

import datetime
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
OUT = REPO / "owner" / "README.md"

OQ_HEAD = re.compile(r"^- \*\*`(OQ-[A-Z0-9-]+)`(.*)$")
# A closed entry announces itself in its own header line.
CLOSED = ("✅", "CLOSED", "RESOLVED", "DONE", "MOOT")
PARTIAL = ("◐", "HALF-ANSWERED", "TWO OF THREE", "▶", "RE-BRIEFED")
HELD = ("⏸",)


def read(rel: str) -> str | None:
    try:
        return (REPO / rel).read_text(encoding="utf-8")
    except OSError:
        return None


def oq_entries() -> tuple[list[tuple[str, str, str]], str | None]:
    """(slug, state, headline) for every OQ- entry that is not a duplicate body."""
    text = read("docs/owner-queue.md")
    if text is None:
        return [], "docs/owner-queue.md could not be read"
    out: list[tuple[str, str, str]] = []
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = OQ_HEAD.match(line)
        if not m:
            continue
        slug, tail = m.group(1), m.group(2)
        # The header can wrap; take the next line too when the first is short.
        headline = tail.strip()
        if len(headline) < 40 and i + 1 < len(lines):
            headline = (headline + " " + lines[i + 1].strip()).strip()
        # Both duplicate forms the queue actually uses. Recognizing only
        # "(original body)" left the SUPERSEDED copy of a resolved entry
        # showing as open (Codex, fm #988: OQ-FM-APPARATUS-SIZING).
        if "(original body)" in headline or "(superseded body)" in headline:
            continue
        # PARTIAL and HELD are tested FIRST and the order is load-bearing: a
        # partly-answered entry carries ✅ for the half that IS answered, so a
        # closed-first test hides it. Caught by positive control 2026-08-30 —
        # OQ-FM-FRESH-START-CONFIRMS ("✅ TWO OF THREE ANSWERED") vanished from
        # the first generated index, which is the entry most live that day.
        if any(t in headline for t in PARTIAL):
            state = "partial"
        elif any(t in headline for t in HELD):
            state = "held"
        elif _closed_state(headline):
            state = "closed"
        else:
            state = "open"
        headline = re.sub(r"\*\*|`|—\s*$", "", headline).strip(" -—*")
        out.append((slug, state, headline[:200]))
    return out, None


def _closed_state(headline: str) -> bool:
    """Closure must be the ENTRY's status, never an incidental status word.

    A substring test anywhere in the wrapped headline drops live owner work:
    `OQ-SHIFTLIFE-PHASE0` says only that a *sync* is DONE while explicitly
    retaining two owner asks, and was omitted from the index entirely
    (Codex, fm #988). Require the marker to sit in the entry-status position —
    the leading run of the headline, before the em-dash that opens the prose —
    so a status word inside the description cannot close an entry.
    """
    head = re.split(r"\s+[—–]\s+", headline, maxsplit=1)[0]
    return any(tok in head for tok in CLOSED)


def intent_questions() -> tuple[dict[str, list[str]], list[str]]:
    """The ❓ lines in every intent document, keyed by path."""
    found: dict[str, list[str]] = {}
    missing: list[str] = []
    paths = sorted(REPO.glob("docs/repos/*/intent.md")) + [REPO / "docs/intent.md"]
    for p in paths:
        rel = p.relative_to(REPO).as_posix()
        try:
            lines = p.read_text(encoding="utf-8").splitlines()
        except OSError:
            missing.append(rel)
            continue
        # Questions wrap across lines; keeping only the ❓ line emitted
        # fragments ending in "and" or "the" (Codex, fm #988). Take each
        # question through its continuation, to the next blank line,
        # question, or heading.
        qs = []
        i = 0
        while i < len(lines):
            if "❓" in lines[i]:
                buf = [lines[i].strip(" >*").rstrip()]
                j = i + 1
                while j < len(lines):
                    nxt = lines[j].strip(" >*").rstrip()
                    if not nxt or "❓" in lines[j] or lines[j].lstrip().startswith("#"):
                        break
                    buf.append(nxt)
                    j += 1
                qs.append(" ".join(buf).strip())
                i = j
                continue
            i += 1
        if qs:
            found[rel] = qs
    return found, missing


# The estate's own live/historical split, cited rather than guessed: the boot
# file records docs/prompts/ and docs/proposals/ as seat-era apparatus —
# historical record, not current truth — naming three live exceptions. A date
# in the filename earlier than the seat-era close (2026-07-21) is the second
# signal. Both are stated in the output so a demotion is visible and arguable,
# never silent: the owner's own A2 principle is that historical and current
# material must not sit in one undifferentiated list.
HISTORICAL_DIRS = ("docs/prompts/", "docs/proposals/")
HISTORICAL_EXCEPTIONS = (
    "docs/prompts/chatgpt-project-instructions.md",
    "docs/prompts/chatgpt-couch-legend-project-instructions.md",
)
SEAT_ERA_CLOSE = "2026-07-21"
DATE_IN_NAME = re.compile(r"(20\d{2}-\d{2}-\d{2})")


def owner_guidance_docs() -> tuple[list[str], list[str]]:
    """(live, historical) documents declaring themselves for the owner's hand."""
    live: list[str] = []
    old: list[str] = []
    for p in sorted(REPO.glob("docs/**/*.md")):
        try:
            head = p.read_text(encoding="utf-8")[:600]
        except OSError:
            continue
        if "owner-guidance" not in head:
            continue
        rel = p.relative_to(REPO).as_posix()
        m = DATE_IN_NAME.search(rel)
        historical = (
            (any(rel.startswith(d) for d in HISTORICAL_DIRS)
             and rel not in HISTORICAL_EXCEPTIONS)
            or (m is not None and m.group(1) < SEAT_ERA_CLOSE)
        )
        (old if historical else live).append(rel)
    return live, old


def owner_workbooks() -> list[str]:
    """Editable owner-facing siblings beside the generated index."""
    out: list[str] = []
    for p in sorted((REPO / "owner").glob("*.md")):
        if p == OUT:
            continue
        try:
            head = p.read_text(encoding="utf-8")[:600]
        except OSError:
            continue
        if "owner-guidance" in head:
            out.append(p.relative_to(REPO).as_posix())
    return out


def ungroomed_ideas() -> tuple[list[str], str | None]:
    text = read("docs/planning/idea-backlog.md")
    if text is None:
        return [], "docs/planning/idea-backlog.md could not be read"
    rows = [ln for ln in text.splitlines() if ln.startswith("| ") and "ungroomed" in ln]
    return rows, None


def unconsumed_comments() -> tuple[list[tuple[str, int]], list[str]]:
    """Unconsumed counts per repository, plus the indexes that could not be read.

    A skipped unreadable index used to be indistinguishable from a zero, so the
    page could assert "none unconsumed" on a source it never read — the exact
    false affirmative the honest-null contract forbids (Codex, fm #988).
    """
    out: list[tuple[str, int]] = []
    unreadable: list[str] = []
    for p in sorted(REPO.glob("docs/owner-comments/*/README.md")):
        try:
            text = p.read_text(encoding="utf-8")
        except OSError:
            unreadable.append(p.parent.name)
            continue
        m = re.search(r"## Unconsumed \((\d+)\)", text)
        if m is None:
            unreadable.append(p.parent.name)
            continue
        if int(m.group(1)) > 0:
            out.append((p.parent.name, int(m.group(1))))
    return out, unreadable


def main() -> int:
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    oq, oq_err = oq_entries()
    questions, q_missing = intent_questions()
    guidance, guidance_old = owner_guidance_docs()
    workbooks = owner_workbooks()
    ideas, idea_err = ungroomed_ideas()
    comments, comments_unreadable = unconsumed_comments()

    live = [e for e in oq if e[1] != "closed"]
    L: list[str] = []
    a = L.append

    a("# Waiting on you")
    a("")
    a("> **Status:** `generated` — **do not hand-edit;** regenerate with")
    a("> `python3 tools/gen_owner_index.py`. **NOT SOURCE OF TRUTH:** every item")
    a("> below is a pointer, and the linked file wins. This page exists because")
    a("> what needs your attention was spread across several surfaces you had to")
    a("> already know about; it is swept from them so it cannot go stale.")
    a(">")
    a(f"> generated-at {stamp}")
    a("")
    a("**What is here:** things only you can decide · questions written for you ·")
    a("documents waiting for your own words · piles that need triage. **What is")
    a("not here:** anything an agent can settle without you.")
    a("")

    a("## Read now — short workbooks in this folder")
    a("")
    if workbooks:
        a("These are short drafts made for your own edits. Each separates your")
        a("quoted words (`OWNER`) from a session's revisable inference (`DERIVED`).")
        a("")
        for rel in workbooks:
            name = pathlib.PurePosixPath(rel).name
            a(f"- [`{name}`]({name})")
        a("")
    else:
        a("No editable sibling workbooks found.")
        a("")

    a("## Decide — open items in the owner queue")
    a("")
    if oq_err:
        a(f"⚠ **{oq_err}** — this section is empty because its source could not be read,")
        a("not because there is nothing to decide.")
    else:
        a(f"{len(live)} open of {len(oq)} entries in "
          "[`docs/owner-queue.md`](../docs/owner-queue.md) "
          "(historical duplicate bodies excluded). Each entry there carries its")
        a("own WHAT / WHERE / WHY-IT-MATTERS / UNBLOCKS.")
        a("")
        for state in ("open", "partial", "held"):
            rows = [e for e in live if e[1] == state]
            if not rows:
                continue
            label = {"open": "Open", "partial": "Partly answered",
                     "held": "Held by your own word"}[state]
            a(f"**{label} ({len(rows)})**")
            a("")
            for slug, _, head in rows:
                a(f"- **`{slug}`** — {head}")
            a("")

    a("## Answer — questions written to you, inside the intent files")
    a("")
    if questions:
        total = sum(len(v) for v in questions.values())
        a(f"{total} question(s) across {len(questions)} file(s). These are the")
        a("documents you went looking for: each states what the estate can prove")
        a("about a repo and marks every line `OWNER` (your words) or `DERIVED`")
        a("(a session's inference, revisable). They are thin on purpose.")
        a("")
        for rel, qs in questions.items():
            a(f"### [`{rel}`](../{rel})")
            a("")
            for q in qs:
                a(f"- {q}")
            a("")
    else:
        a("No ❓ markers found in any intent document — either none are open, or")
        a("the marker convention changed. Check the files directly before trusting")
        a("this null.")
        a("")
    for rel in q_missing:
        a(f"⚠ `{rel}` exists but could not be read.")
    if q_missing:
        a("")

    a("## Read and edit — written for your hand, not ours")
    a("")
    if guidance:
        a(f"**{len(guidance)} live** of {len(guidance) + len(guidance_old)} documents")
        a("declaring `Status: owner-guidance` — drafted from evidence and waiting")
        a("for your words to replace the inferences:")
        a("")
        for rel in guidance:
            a(f"- [`{rel}`](../{rel})")
        a("")
    if guidance_old:
        a(f"<details><summary>{len(guidance_old)} more, filed historical — "
          "seat-era apparatus (<code>docs/prompts/</code>, "
          "<code>docs/proposals/</code>) or dated before the program closed "
          "2026-07-21. Listed so the demotion is visible and arguable, not "
          "hidden.</summary>")
        a("")
        for rel in guidance_old:
            a(f"- [`{rel}`](../{rel})")
        a("")
        a("</details>")
        a("")
    prompts = "docs/planning/2026-08-28-owner-intent-questions.md"
    if (REPO / prompts).exists():
        a(f"And the prepared prompts: [`{prompts}`](../{prompts}) — open-ended,")
        a("any order, any length, skip what does not spark. *\"I don't know yet\"*")
        a("is a real answer. Tracked as `OQ-INTENT-WRITE-UP`.")
        a("")

    a("## Triage — piles that grow if nobody looks")
    a("")
    if idea_err:
        a(f"⚠ **{idea_err}**")
    else:
        a(f"**Ideas:** {len(ideas)} ungroomed in "
          "[`docs/planning/idea-backlog.md`](../docs/planning/idea-backlog.md). "
          "**Read that file's own header before trusting this number** — it")
        a("harvests one of three idea formats and calls its own count *\"a floor")
        a("over one formatting style, never a measurement of the corpus.\"*")
        a("")
        # A bare "| … |" run is not a Markdown table without a header row —
        # GitHub collapses it into a pipe-delimited paragraph (Codex, fm #988).
        a("| Card date | Source card | Idea | Groom status |")
        a("|---|---|---|---|")
        for row in ideas:
            a(row)
        a("")
    if comments:
        a("**Owner comments not yet consumed:**")
        a("")
        for repo, n in comments:
            a(f"- [`{repo}`](../docs/owner-comments/{repo}/README.md) — {n}")
    else:
        a("**Owner comments:** none unconsumed.")
    if comments_unreadable:
        a("")
        a("⚠ **Unreadable owner-comment indexes — this section is INCOMPLETE:** "
          + ", ".join(f"`{r}`" for r in comments_unreadable)
          + ". Their unconsumed counts are unknown, not zero.")
    a("")

    content = "\n".join(L) + "\n"
    # --check is the drift gate: the generated CORE surface is only correct if
    # regenerating it here reproduces what is committed. Without it the index
    # goes stale on the next queue edit — the exact failure the generated
    # design claims to prevent (Codex, fm #988). The generated-at stamp is
    # volatile by construction and is excluded from the comparison.
    if "--check" in sys.argv:
        strip = lambda s: "\n".join(
            ln for ln in s.splitlines() if not ln.startswith("> generated-at "))
        try:
            live = OUT.read_text(encoding="utf-8")
        except OSError:
            print(f"owner index: {OUT.relative_to(REPO)} is missing — run "
                  "`python3 tools/gen_owner_index.py`")
            return 1
        if strip(live) != strip(content):
            print(f"owner index: DRIFT — {OUT.relative_to(REPO)} does not match its "
                  "sources; run `python3 tools/gen_owner_index.py` and commit the result")
            return 1
        print(f"owner index: {OUT.relative_to(REPO)} is current")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(content, encoding="utf-8")
    print(f"owner index: {len(live)} open of {len(oq)} queue entries · "
          f"{sum(len(v) for v in questions.values())} question(s) · "
          f"{len(guidance)} owner-guidance doc(s) · {len(workbooks)} workbook(s) · "
          f"{len(ideas)} ungroomed idea(s) · "
          f"{len(comments)} repo(s) with unconsumed comments -> {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
