#!/usr/bin/env python3
"""estate_activity.py — the cross-session activity log for the whole estate.

================================ PROVENANCE ================================
Why added : The owner asked, 2026-08-26, *"how well does a cloud session
            understand what the local sessions have been doing?"* — and
            proposed the fix in the same message: a dedicated section in
            fleet-manager where his local AIs keep track of what they did.
            The measurement that produced this file is in
            `docs/findings/2026-08-26-cross-session-visibility.md`; the
            short version is that a cloud session booted here sees **this
            repo's** session cards and nothing else, so a local session that
            worked `spider-bot`, seeded `creator-kit` or spent an evening on
            the laptop is invisible to it.
Date      : 2026-08-26 (fleet-manager PR #947)
Reliability: ADVISORY generator, wired into no gate. It only ever writes
            `docs/activity/estate-log.md` (fully regenerated) and appends to
            `docs/activity/off-repo-log.md`. It never edits a session card,
            and it makes no claim a card did not already make.
=============================================================================

TWO LANES, and the split is the whole design:

  DERIVED  — `refresh` reads every non-archived repository's `.sessions/`
             directory and rolls the cards dated inside the window into
             `docs/activity/estate-log.md`. Nobody has to remember anything:
             a session that wrote its card in its own repo is already logged
             here. This is the lane that covers repository work, wherever it
             ran.

  HAND-WRITTEN — `log` appends to `docs/activity/off-repo-log.md`, for the
             work that touches no repository and therefore CANNOT be derived:
             laptop setup, a ChatGPT or Gemini sitting, a Drive
             reorganisation, an install, a decision taken in a chat. Nothing
             can generate this lane, which is exactly why it needs one
             command rather than a procedure.

WHAT `refresh` REPORTS THAT A CARD DOES NOT

  A repository that was PUSHED inside the window but left no card dated
  inside it gets its own section. That is the honest signal for invisible
  work — it is how `creator-kit` (created 2026-08-25, one commit, no card)
  shows up at all.

AUTH — either path, whichever the machine has:
  * `$GITHUB_PAT` over DIRECT egress (`trust_env=False`, the container CA).
    The proxied REST path 403s here; that is a path quirk, not a wall.
  * `gh api`, which is what the owner's laptop has after the Claude Desktop
    setup installs it.

Usage
  python3 tools/estate_activity.py refresh [--days 14] [--stdout]
  python3 tools/estate_activity.py log --venue local-desktop \
      --title "FreeCAD library rebuild" [--agent ...] [--touched ...] \
      [--why ...] [--state ...] [--next ...]
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DERIVED = REPO / "docs/activity/estate-log.md"
OFF_REPO = REPO / "docs/activity/off-repo-log.md"
CA = "/root/.ccr/ca-bundle.crt"
OWNER = "menno420"

# The closed venue vocabulary. `unstated` is never written by a session — it
# is what this generator prints when a card carries no 📍 Venue line, and an
# honest null beats a guess about which machine ran something.
VENUES = (
    "local-desktop",   # Claude Desktop Code tab, on the owner's laptop
    "local-cli",       # `claude` in a terminal on the owner's laptop
    "cloud-container", # Claude Code on the web / a remote container
    "codex-cloud",     # ChatGPT Codex cloud
    "chatgpt-work",    # ChatGPT Work
    "other",
)

CARD_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.md$")
# Anchored to the complete bullet line on purpose. An unanchored search reads
# prose *about* the convention — of which this estate now has a great deal — as
# a stated venue, which corrupts the very stated-vs-total count that exists to
# keep the nulls honest (@codex, fm #947).
VENUE_RE = re.compile(
    r"^[ \t]*[-*][ \t]+\*\*\N{ROUND PUSHPIN}[ \t]*Venue:\*\*[ \t]*`?([A-Za-z][A-Za-z-]*)`?[ \t]*$",
    re.M,
)
# Line-anchored like VENUE_RE, for the same reason: an unanchored search over the
# whole card read prose *about* the model line (a card titled after the model
# slot, a sentence quoting the convention) as the model itself, and the derived
# table showed a lone backtick or a sentence fragment in the model cell
# (@codex, fm #1012 round 1). Unlike VENUE_RE it accepts the documented
# unbolded forms — `.sessions/README.md` § Model defines the selector as the
# first LINE-ANCHORED `📊 Model:` occurrence, "bold or not", and 170 cards use
# the plain `📊 Model: …` line (@codex, fm #1012 round 2: requiring the bolded
# bullet silently blanked those).
MODEL_RE = re.compile(
    r"^[ \t]*(?:[-*][ \t]+)?\*{0,2}\N{BAR CHART}[ \t]*Model:\*{0,2}[ \t]*(.+?)[ \t]*$",
    re.M,
)
STATUS_RE = re.compile(r"\*\*Status:\*\*\s*`([a-z-]+)`", re.I)


# ---------------------------------------------------------------- transport

class GitHub:
    """Whichever of the two paths this machine actually has."""

    def __init__(self) -> None:
        self.available = True
        self.token = os.environ.get("GITHUB_PAT") or os.environ.get("GH_TOKEN")
        self.session = None
        if self.token:
            try:
                import requests  # noqa: PLC0415 — optional dependency
            except ImportError:
                self.token = None
            else:
                self.session = requests.Session()
                self.session.trust_env = False
        self.verify = CA if os.path.exists(CA) else True

    def get_all(self, path: str, cap: int = 20):
        """Follow pagination until a short page. `path` must already carry
        per_page. Returns a flat list; a single unpaginated page still works."""
        out: list = []
        page = 1
        while page <= cap:
            chunk = self.get(f"{path}&page={page}")
            if not chunk:
                break
            out.extend(chunk)
            if len(chunk) < 100:
                break
            page += 1
        return out

    def get(self, path: str):
        """Return parsed JSON, or None on 404. Raises on anything else."""
        if self.session is not None:
            r = self.session.get(
                "https://api.github.com" + path,
                headers={
                    "Authorization": f"Bearer {self.token}",
                    "Accept": "application/vnd.github+json",
                },
                verify=self.verify,
                timeout=30,
            )
            if r.status_code in (404, 409):
                # 409 is GitHub's "Git Repository is empty" — an unborn
                # repository, which must reach the no-protocol classification
                # rather than abort the whole refresh (@codex, fm #947 r5).
                return None
            r.raise_for_status()
            return r.json()
        # gh CLI fallback — the laptop path. `shutil.which`, never Unix
        # `which`: that is not an executable on Windows, which is the exact
        # machine this branch exists for (@codex, fm #947).
        exe = shutil.which("gh")
        if exe is None:
            raise RuntimeError(
                "no usable GitHub path: set $GITHUB_PAT (with `requests` "
                "installed), or install and sign in to the `gh` CLI"
            )
        p = subprocess.run([exe, "api", path.lstrip("/")],
                           capture_output=True, text=True, encoding="utf-8")
        if p.returncode != 0:
            err = p.stderr
            if ("404" in err or "Not Found" in err
                    or "409" in err or "empty" in err.lower()):
                return None
            raise RuntimeError(f"gh api {path} failed: {p.stderr.strip()[:300]}")
        return json.loads(p.stdout)


# ---------------------------------------------------------------- refresh

def parse_card(text: str) -> dict:
    # The protocol puts the venue line in the card header, above the first `##`.
    # Anchoring to the complete bullet already rejects prose about the
    # convention; restricting to the header also rejects a FENCED EXAMPLE of the
    # bullet inside a card body, which this estate's cards now plausibly carry.
    header = text.split("\n## ", 1)[0]
    venue = VENUE_RE.search(header)
    # The model selector is the first LINE-ANCHORED occurrence anywhere in the
    # card (.sessions/README.md § Model) — some cards open with a `## Correction`
    # section above their header block, so the header-only search of the venue
    # line does not apply here (@codex, fm #1012 round 3).
    model = MODEL_RE.search(text)
    status = STATUS_RE.search(text)
    title = ""
    for line in text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break
    v = venue.group(1).lower() if venue else "unstated"
    if v not in VENUES and v != "unstated":
        v = "other"
    return {
        "title": title,
        "venue": v,
        "venue_stated": bool(venue),
        # Segment 1 of the Model line is the model; the rest is effort + class.
        "model": model.group(1).strip().strip("*").split("·")[0].strip() if model else "",
        "status": status.group(1).lower() if status else "unknown",
    }


def _sessions_tree(gh: GitHub, repo: str, branch: str):
    """Card entries in `.sessions/`, via the Git Trees API.

    NOT the Contents API: a Contents directory listing is capped at 1,000
    entries and `superbot/.sessions/` was already at ~970 on 2026-08-24, so
    that call was ~30 cards away from silently truncating — and because
    date-prefixed names sort oldest-first, the entries it would have dropped
    are exactly the newest ones this window needs (@codex, fm #947).

    Returns `(blobs, truncated)`; `blobs` is None when the repository has no
    `.sessions/` at all. `truncated` is propagated INTO the generated file
    rather than printed and forgotten: a warning on stdout does not stop the
    artifact presenting a floor as a total, and under `--stdout` it would
    contaminate the Markdown stream (@codex, fm #947 round 2).
    """
    root = gh.get(f"/repos/{OWNER}/{repo}/git/trees/{branch}")
    if not root:
        return None, False
    node = next((t for t in root.get("tree", [])
                 if t["path"] == ".sessions" and t["type"] == "tree"), None)
    if node is None:
        return None, False
    sub = gh.get(f"/repos/{OWNER}/{repo}/git/trees/{node['sha']}")
    if not sub:
        return [], False
    truncated = bool(sub.get("truncated"))
    if truncated:
        print(f"WARNING  {repo}/.sessions came back truncated — counts for it "
              f"are a floor, not a total.", file=sys.stderr)
    return [t for t in sub.get("tree", []) if t["type"] == "blob"], truncated


def _read_blob(gh: GitHub, repo: str, sha: str) -> str:
    blob = gh.get(f"/repos/{OWNER}/{repo}/git/blobs/{sha}")
    if not blob:
        return ""
    return base64.b64decode(blob["content"]).decode("utf-8", "replace")


def _in_flight(gh: GitHub, repo: str) -> list[dict]:
    """Cards on OPEN PR branches — the born-red claim, before it merges.

    The default branch cannot answer "what is another session doing right
    now": under this estate's landing discipline a card is pushed to a PR
    branch first and reaches `main` only when the work is finished, so a
    default-branch-only read shows an active repository as silent (@codex,
    fm #947). This is the half that makes the log a coordination surface
    rather than a history.
    """
    out: list[dict] = []
    for pr in gh.get_all(f"/repos/{OWNER}/{repo}/pulls?state=open&per_page=100") or []:
        head = pr.get("head", {}).get("sha", "")
        head_date = None
        head_tried = False
        for f in gh.get_all(
                f"/repos/{OWNER}/{repo}/pulls/{pr['number']}/files?per_page=100") or []:
            path = f["filename"]
            if not path.startswith(".sessions/") or f["status"] == "removed":
                continue
            m = CARD_RE.match(path.split("/", 1)[1])
            if not m:
                continue
            try:
                when = date.fromisoformat(m.group(1))
            except ValueError:
                continue
            if not head_tried and head:
                head_tried = True
                # The PR head's commit date, so an in-flight card can excuse
                # the branch push that carried it WITHOUT excusing every other
                # push in the repository (@codex, fm #947 round 3). Guarded on
                # ATTEMPTED rather than on the result: a head that cannot be
                # resolved (deleted fork, 404) leaves head_date None, and
                # keying on the result would re-request it for every further
                # card in the same PR — in exactly the degraded case this
                # branch exists to tolerate (@codex, round 4).
                c = gh.get(f"/repos/{OWNER}/{repo}/commits/{head}")
                if c:
                    head_date = datetime.fromisoformat(
                        c["commit"]["committer"]["date"].replace("Z", "+00:00")).date()
            blob = gh.get(f"/repos/{OWNER}/{repo}/contents/{path}?ref={head}")
            if not blob:
                continue
            card = parse_card(base64.b64decode(blob["content"]).decode("utf-8", "replace"))
            card.update({"repo": repo, "date": when.isoformat(),
                         "file": path.split("/", 1)[1], "pr": pr["number"],
                         "in_flight": True,
                         "head_date": head_date.isoformat() if head_date else None})
            out.append(card)
    return out


def collect(gh: GitHub, days: int):
    # `days - 1`: a bare `now - timedelta(days=7)` date compared with `>=`
    # spans parts of eight UTC calendar dates. This is a calendar-day window
    # and it matches what the header advertises (@codex, fm #947).
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days - 1)).date()
    repos = gh.get_all("/user/repos?per_page=100&sort=pushed&affiliation=owner")
    archived = sum(1 for r in repos if r["archived"])
    repos = [r for r in repos if not r["archived"]]

    entries: list[dict] = []
    silent: list[dict] = []
    no_protocol: list[str] = []
    incomplete: list[str] = []
    seen: set[tuple[str, str]] = set()
    flight_seen: set[tuple[str, str, int]] = set()

    today = datetime.now(timezone.utc).date()
    for r in repos:
        name = r["name"]
        # A repository with no commits reports `pushed_at: null`; calling
        # .replace() on it aborted the entire estate refresh (@codex, round 3).
        raw_push = r.get("pushed_at")
        pushed = (datetime.fromisoformat(raw_push.replace("Z", "+00:00")).date()
                  if raw_push else None)
        moved = pushed is not None and pushed >= cutoff

        blobs, truncated = _sessions_tree(gh, name, r.get("default_branch") or "main")
        if truncated:
            incomplete.append(name)

        # ONE path, deliberately. Rounds 3 and 4 each found the same three bugs
        # in a second, near-parallel branch for repositories adopting the
        # protocol — a missing `<= today` bound, a missing coverage check, a
        # dropped head date — because that branch `continue`d past the shared
        # logic. Fixing the symptoms drew a reshaped finding each time, so the
        # branch is gone: everything below runs for every repository, and a
        # repository with no `.sessions/` on its default branch is simply one
        # whose `dated` list is empty (@codex, fm #947 round 4).
        dated: list[tuple] = []
        for b in (blobs or []):
            m = CARD_RE.match(b["path"])
            if not m:
                continue
            try:
                when = date.fromisoformat(m.group(1))
            except ValueError:
                continue
            # Upper bound as well as lower: a mistyped future date would sort
            # ahead of real activity, count inside "the last N days", and
            # suppress invisible-work detection until it arrived.
            if when > today:
                continue
            dated.append((when, b))

        # Un-windowed on purpose, and used for two different jobs below.
        # Protocol existence is not window-scoped, and neither is coverage: an
        # open PR whose card filename predates the window can still be what
        # accounts for a push inside it.
        flights = _in_flight(gh, name)
        has_protocol = blobs is not None or bool(flights)

        # --- rendered entries: windowed on both sides
        for when, b in dated:
            if not (cutoff <= when <= today):
                continue
            card = parse_card(_read_blob(gh, name, b["sha"]))
            card.update({"repo": name, "date": when.isoformat(),
                         "file": b["path"], "pr": None, "in_flight": False,
                         "head_date": None})
            entries.append(card)
            seen.add((name, b["path"]))

        for card in flights:
            when = date.fromisoformat(card["date"])
            if not (cutoff <= when <= today):
                continue
            # Suppress only what is already on the default branch. Keep the PR
            # in the key so two open PRs claiming the same card filename BOTH
            # appear — that collision is the conflict this surface exists to
            # show, not noise to fold away (@codex, round 2).
            if (card["repo"], card["file"]) in seen:
                continue
            key = (card["repo"], card["file"], card["pr"])
            if key not in flight_seen:
                entries.append(card)
                flight_seen.add(key)

        if not has_protocol:
            no_protocol.append(name)

        # --- movement without a card: the section this whole log exists for.
        #
        # Four corrections are folded into the predicate below, in the order
        # @codex found them (fm #947), and two of them pull against each other:
        #   r1: it only fired when a repository had NO card in the window, so
        #       an 08-20 card plus an uncarded 08-25 push went unreported.
        #   r2: an in-flight card has to count, or every repository with an
        #       open born-red PR reports itself as unexplained movement.
        #   r3: but "any open card" is too coarse the other way — `pushed_at`
        #       is the repository-wide latest push and can belong to a branch
        #       no PR touches, so an old carded PR would hide a fresh uncarded
        #       push to main.
        #   r4: and the coverage set must NOT be windowed, or an open PR whose
        #       card filename predates the window stops covering the push its
        #       own branch made inside it.
        #
        # What excuses a push is therefore a DATE that covers it — a card's own
        # date, or the head-commit date of the open PR whose branch carried the
        # push — never the mere existence of an open card, and never a date
        # filtered out for being outside the rendering window.
        # `<= today` on BOTH halves. The rendered-entry filter already bounds
        # in-flight dates; coverage did not, so a mistyped future date on an
        # open PR would have suppressed the invisible-work row until it
        # arrived — the same bug as the default-branch one, in the other list
        # (@codex, fm #947 r5). Head dates come from real commits and cannot be
        # in the future, but are bounded with them rather than trusted.
        covered = ([w for w, _ in dated]
                   + [d for d in (date.fromisoformat(c["date"]) for c in flights)
                      if d <= today]
                   + [d for d in (date.fromisoformat(c["head_date"])
                                  for c in flights if c.get("head_date"))
                      if d <= today])
        newest = max(covered, default=None)
        if moved:
            if not has_protocol:
                silent.append({"repo": name, "pushed": pushed.isoformat(),
                               "why": "no `.sessions/` directory"})
            elif newest is None:
                silent.append({"repo": name, "pushed": pushed.isoformat(),
                               "why": "`.sessions/` exists but holds no card at all"})
            elif pushed > newest:
                gap = (pushed - newest).days
                silent.append({
                    "repo": name, "pushed": pushed.isoformat(),
                    "why": (f"newest card is {newest.isoformat()} — "
                            f"pushed {gap} day{'s' if gap != 1 else ''} later "
                            f"with no card for it")})

    entries.sort(key=lambda e: (e["date"], e["repo"]), reverse=True)
    silent.sort(key=lambda s_: s_["pushed"], reverse=True)
    return (entries, silent, sorted(no_protocol), len(repos), archived,
            sorted(incomplete))


def render(entries, silent, no_protocol, live_count, archived_count,
           incomplete, days) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%MZ")
    stated = sum(1 for e in entries if e["venue_stated"])
    inflight = [e for e in entries if e["in_flight"]]
    by_venue: dict[str, int] = {}
    by_repo: dict[str, int] = {}
    for e in entries:
        by_venue[e["venue"]] = by_venue.get(e["venue"], 0) + 1
        by_repo[e["repo"]] = by_repo.get(e["repo"], 0) + 1

    out: list[str] = []
    add = out.append
    add("# The estate activity log — derived lane")
    add("")
    add("> **Status:** `reference` \N{EM DASH} **GENERATED, do not hand-edit.** Every line below is")
    add("> regenerated by `python3 tools/estate_activity.py refresh`; an edit here")
    add("> is erased by the next run. Hand-written entries belong in")
    add("> [`off-repo-log.md`](off-repo-log.md), and per-repo detail stays")
    add("> canonical in each repository's own `.sessions/` card — this file is a")
    add("> pointer index, never a copy.")
    add(">")
    add(f"> **Window:** the last **{days} calendar days** (UTC). **Generated:** {now}.")
    add(f"> **Scope: the {live_count} NON-ARCHIVED repositories** — "
        f"{archived_count} archived ones are excluded, so every count here is")
    add("> non-archived-only and is not a total for the estate's whole history.")
    add(f"> **Cards:** {len(entries)} across {len(by_repo)} repositories, "
        f"of which **{len(inflight)} "
        f"{'is' if len(inflight) == 1 else 'are'} in flight** on an open PR.")
    add(f"> **Venue stated:** {stated} of {len(entries)}.")
    if incomplete:
        add(">")
        add("> \N{WARNING SIGN} **INCOMPLETE — these counts are a floor, not a total.** "
            "GitHub returned a truncated")
        add("> `.sessions/` listing for: "
            + ", ".join(f"`{n}`" for n in incomplete)
            + ". Cards from them are missing here.")
    add("")
    add("## In flight right now — cards on open PR branches")
    add("")
    add("Not yet on any default branch. This is the born-red claim another")
    add("session collides with, so read it before starting work in these repos.")
    add("")
    if inflight:
        add("| repo | PR | venue | card |")
        add("|---|---|---|---|")
        for e in sorted(inflight, key=lambda x: (x["repo"], x["date"])):
            add(f"| `{e['repo']}` | [#{e['pr']}](https://github.com/{OWNER}/"
                f"{e['repo']}/pull/{e['pr']}) | `{e['venue']}` | {e['file']} |")
    else:
        add("None.")
    add("")
    add("## What ran where")
    add("")
    if by_venue:
        add("| venue | cards |")
        add("|---|--:|")
        for v, n in sorted(by_venue.items(), key=lambda kv: -kv[1]):
            add(f"| `{v}` | {n} |")
        add("")
        add("`unstated` is an honest null, never a guess: a card with no")
        add("\N{ROUND PUSHPIN} Venue: line means nobody said, not `cloud-container`.")
    else:
        add("No session cards dated inside the window. That is an honest null, "
            "not an error — check the invisible-work section below before "
            "concluding nothing happened.")
    add("")
    add("## Where the cards are — reachability from fleet-manager")
    add("")
    add("A session booted in this repository reads `fleet-manager/.sessions/`")
    add("and nothing else. This is the split that made the log necessary.")
    add("")
    add("| repo | cards | reachable from a fleet-manager session without this log |")
    add("|---|--:|---|")
    for repo, n in sorted(by_repo.items(), key=lambda kv: -kv[1]):
        add(f"| `{repo}` | {n} | {'yes' if repo == 'fleet-manager' else '**no**'} |")
    add("")
    add("## Sessions, newest first")
    add("")
    if entries:
        add("| date | repo | venue | model | status | card |")
        add("|---|---|---|---|---|---|")
        for e in entries:
            ref = f"pull/{e['pr']}/files" if e["in_flight"] else "blob/HEAD/.sessions"
            link = (f"[{e['file']}](https://github.com/{OWNER}/{e['repo']}/{ref})"
                    if e["in_flight"] else
                    f"[{e['file']}](https://github.com/{OWNER}/{e['repo']}"
                    f"/blob/HEAD/.sessions/{e['file']})")
            flag = " ⏳" if e["in_flight"] else ""
            add(f"| {e['date']}{flag} | `{e['repo']}` | `{e['venue']}` | "
                f"{e['model'] or '—'} | `{e['status']}` | {link} |")
    else:
        add("(none)")
    add("")
    add("## Invisible work — repositories that moved without a card to explain it")
    add("")
    add("This is the section the log exists for. A repository here was pushed")
    add("inside the window and has no session card accounting for that push, so")
    add("**nothing in the estate's records says who did that work or why.** A row")
    add("is a prompt to go and look, not an accusation: a hand-merged owner")
    add("commit is a perfectly good reason to appear here.")
    add("")
    if silent:
        add("| repo | last push | why it is here |")
        add("|---|---|---|")
        for s_ in silent:
            add(f"| `{s_['repo']}` | {s_['pushed']} | {s_['why']} |")
    else:
        add("None — every repository pushed inside the window left a card for it.")
    add("")
    add("## Repositories with no card protocol at all")
    add("")
    add("No `.sessions/` directory, so no session there can ever appear above.")
    add("Adopting substrate-kit is what closes this, per repository.")
    add("Non-archived only, like everything else here.")
    add("")
    add(", ".join(f"`{n}`" for n in no_protocol) if no_protocol else "None.")
    add("")
    return "\n".join(out)


# ---------------------------------------------------------------- log

ENTRY_MARKER = "<!-- newest entry goes directly below this line -->"


HEADING_RE = re.compile(r"^### (\d{4}-\d{2}-\d{2}) ", re.M)
EMPTY_STATE = "*No entries yet.*"
EMPTY_REPLACEMENT = "*Entries begin 2026-08-26.*"


def append_entry(args: argparse.Namespace) -> int:
    if args.venue not in VENUES:
        print(f"ERROR  --venue must be one of: {', '.join(VENUES)}")
        return 1
    if args.date:
        try:
            when = date.fromisoformat(args.date).isoformat()
        except ValueError:
            print(f"ERROR  --date must be YYYY-MM-DD, got {args.date!r}")
            return 1
    else:
        when = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if not OFF_REPO.exists():
        print(f"ERROR  {OFF_REPO.relative_to(REPO)} is missing")
        return 1
    # Explicit encoding on both ends: the command this file advertises is run
    # on a Windows laptop, where the locale default can fail on the 📍 the file
    # itself contains (@codex, fm #947).
    text = OFF_REPO.read_text(encoding="utf-8")
    if ENTRY_MARKER not in text:
        print(f"ERROR  {OFF_REPO.relative_to(REPO)} has lost its entry marker")
        return 1

    block = "\n".join([
        "",
        "",
        f"### {when} — {args.title}",
        "",
        f"- **venue:** `{args.venue}`",
        f"- **agent:** {args.agent}",
        f"- **touched:** {args.touched}",
        f"- **why:** {args.why}",
        f"- **state left:** {args.state}",
        f"- **next:** {args.next}",
    ])

    if EMPTY_STATE in text:
        # Otherwise the lane says "no entries yet" directly above its first
        # entry (@codex, fm #947 round 2).
        text = text.replace(EMPTY_STATE, EMPTY_REPLACEMENT, 1)

    # "Newest first" is a promise, so a backfilled --date is inserted in its
    # place rather than jammed at the top (@codex, fm #947).
    insert_at = None
    for m in HEADING_RE.finditer(text):
        if m.group(1) <= when:
            insert_at = m.start()
            break
    if insert_at is None:
        marker_end = text.index(ENTRY_MARKER) + len(ENTRY_MARKER)
        headings = list(HEADING_RE.finditer(text))
        insert_at = len(text.rstrip()) if headings else marker_end
        OFF_REPO.write_text(text[:insert_at] + block + text[insert_at:],
                            encoding="utf-8")
    else:
        OFF_REPO.write_text(text[:insert_at].rstrip("\n") + block + "\n\n"
                            + text[insert_at:], encoding="utf-8")
    print(f"appended to {OFF_REPO.relative_to(REPO)}: {when} — {args.title}")
    return 0


# ---------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("refresh", help="regenerate the derived lane")
    r.add_argument("--days", type=int, default=7)
    r.add_argument("--stdout", action="store_true",
                   help="print instead of writing the file")

    lg = sub.add_parser("log", help="append one entry to the hand-written lane")
    lg.add_argument("--venue", required=True, help=f"one of: {', '.join(VENUES)}")
    lg.add_argument("--title", required=True)
    lg.add_argument("--date", default="", help="YYYY-MM-DD; defaults to today (UTC)")
    lg.add_argument("--agent", default="unstated")
    lg.add_argument("--touched", default="unstated")
    lg.add_argument("--why", default="unstated")
    lg.add_argument("--state", default="unstated")
    lg.add_argument("--next", default="unstated")

    args = ap.parse_args()
    if args.cmd == "log":
        return append_entry(args)

    gh = GitHub()
    if gh.session is None and shutil.which("gh") is None:
        print("ERROR  no usable GitHub path: set $GITHUB_PAT (with `requests` "
              "installed), or install and sign in to the `gh` CLI.")
        return 1
    if args.days < 1:
        # `--days 0` puts the cutoff in the FUTURE and writes a clean-looking
        # empty ledger over the real one (@codex, fm #947 round 2).
        print(f"ERROR  --days must be a positive integer, got {args.days}")
        return 1
    try:
        entries, silent, no_protocol, live, archived, incomplete = collect(gh, args.days)
    except RuntimeError as exc:
        print(f"ERROR  {exc}")
        return 1
    body = render(entries, silent, no_protocol, live, archived, incomplete, args.days)
    if args.stdout:
        print(body)
    else:
        DERIVED.parent.mkdir(parents=True, exist_ok=True)
        DERIVED.write_text(body, encoding="utf-8")
        print(f"wrote {DERIVED.relative_to(REPO)}: {len(entries)} cards "
              f"({sum(1 for e in entries if e['in_flight'])} in flight), "
              f"{len(silent)} repositories with unexplained movement")
    return 0


if __name__ == "__main__":
    sys.exit(main())
