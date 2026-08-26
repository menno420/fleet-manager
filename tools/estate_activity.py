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
VENUE_RE = re.compile(r"\N{ROUND PUSHPIN}\s*Venue:\*{0,2}\s*`?([a-z-]+)`?", re.I)
MODEL_RE = re.compile(r"\N{BAR CHART}\s*Model:\*{0,2}\s*(.+)")
STATUS_RE = re.compile(r"\*\*Status:\*\*\s*`([a-z-]+)`", re.I)


# ---------------------------------------------------------------- transport

class GitHub:
    """Whichever of the two paths this machine actually has."""

    def __init__(self) -> None:
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
            if r.status_code == 404:
                return None
            r.raise_for_status()
            return r.json()
        # gh CLI fallback — the laptop path.
        p = subprocess.run(
            ["gh", "api", path.lstrip("/")], capture_output=True, text=True
        )
        if p.returncode != 0:
            if "404" in p.stderr or "Not Found" in p.stderr:
                return None
            raise RuntimeError(f"gh api {path} failed: {p.stderr.strip()[:300]}")
        return json.loads(p.stdout)


# ---------------------------------------------------------------- refresh

def parse_card(text: str) -> dict:
    venue = VENUE_RE.search(text)
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


def collect(gh: GitHub, days: int) -> tuple[list[dict], list[dict], list[str]]:
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).date()
    repos = gh.get("/user/repos?per_page=100&sort=pushed&affiliation=owner") or []
    repos = [r for r in repos if not r["archived"]]

    entries: list[dict] = []
    silent: list[dict] = []
    no_protocol: list[str] = []

    for r in repos:
        name = r["name"]
        pushed = datetime.fromisoformat(r["pushed_at"].replace("Z", "+00:00")).date()
        listing = gh.get(f"/repos/{OWNER}/{name}/contents/.sessions")
        if listing is None:
            no_protocol.append(name)
            if pushed >= cutoff:
                silent.append({"repo": name, "pushed": pushed.isoformat(),
                               "why": "no .sessions/ directory"})
            continue

        fresh = []
        for item in listing:
            m = CARD_RE.match(item["name"])
            if not m:
                continue
            try:
                when = date.fromisoformat(m.group(1))
            except ValueError:
                continue
            if when >= cutoff:
                fresh.append((when, item))

        for when, item in fresh:
            blob = gh.get(f"/repos/{OWNER}/{name}/contents/.sessions/{item['name']}")
            if blob is None:
                continue
            text = base64.b64decode(blob["content"]).decode("utf-8", "replace")
            card = parse_card(text)
            card.update({"repo": name, "date": when.isoformat(), "file": item["name"]})
            entries.append(card)

        if pushed >= cutoff and not fresh:
            dated = any(CARD_RE.match(i["name"]) for i in listing)
            silent.append({"repo": name, "pushed": pushed.isoformat(),
                           "why": ("has cards, none dated in the window" if dated
                                   else "`.sessions/` exists but holds no card at all")})

    entries.sort(key=lambda e: (e["date"], e["repo"]), reverse=True)
    silent.sort(key=lambda s: s["pushed"], reverse=True)
    return entries, silent, sorted(no_protocol)


def render(entries: list[dict], silent: list[dict], no_protocol: list[str],
           days: int) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%MZ")
    stated = sum(1 for e in entries if e["venue_stated"])
    by_venue: dict[str, int] = {}
    for e in entries:
        by_venue[e["venue"]] = by_venue.get(e["venue"], 0) + 1

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
    add(f"> **Window:** the last **{days} days**. **Generated:** {now}.")
    add(f"> **Cards:** {len(entries)} across {len({e['repo'] for e in entries})} "
        f"repositories; **{stated} of {len(entries)}** state their venue.")
    add("")
    add("## What ran where")
    add("")
    if by_venue:
        add("| venue | cards |")
        add("|---|--:|")
        for v, n in sorted(by_venue.items(), key=lambda kv: -kv[1]):
            add(f"| `{v}` | {n} |")
    else:
        add("No session cards dated inside the window. That is an honest null, "
            "not an error — check the invisible-work section below before "
            "concluding nothing happened.")
    add("")
    add("## Sessions, newest first")
    add("")
    if entries:
        add("| date | repo | venue | model | status | card |")
        add("|---|---|---|---|---|---|")
        for e in entries:
            link = (f"[{e['file']}](https://github.com/{OWNER}/{e['repo']}"
                    f"/blob/main/.sessions/{e['file']})")
            add(f"| {e['date']} | `{e['repo']}` | `{e['venue']}` | "
                f"{e['model'] or '—'} | `{e['status']}` | {link} |")
    else:
        add("(none)")
    add("")
    add("## Invisible work — repositories that moved and left no card in the window")
    add("")
    add("This is the section the log exists for. A repository here was pushed")
    add("inside the window but has no session card dated inside it, so **nothing")
    add("in the estate's records says who did that work or why.** A row is a")
    add("prompt to go and look, not an accusation: a hand-merged owner commit is")
    add("a perfectly good reason to appear here.")
    add("")
    if silent:
        add("| repo | last push | why it is here |")
        add("|---|---|---|")
        for s in silent:
            add(f"| `{s['repo']}` | {s['pushed']} | {s['why']} |")
    else:
        add("None — every repository pushed inside the window left a card.")
    add("")
    add("## Repositories with no card protocol at all")
    add("")
    add("No `.sessions/` directory, so no session there can ever appear above.")
    add("Adopting substrate-kit is what closes this, per repository.")
    add("")
    add(", ".join(f"`{n}`" for n in no_protocol) if no_protocol else "None.")
    add("")
    return "\n".join(out)


# ---------------------------------------------------------------- log

ENTRY_MARKER = "<!-- newest entry goes directly below this line -->"


def append_entry(args: argparse.Namespace) -> int:
    if args.venue not in VENUES:
        print(f"ERROR  --venue must be one of: {', '.join(VENUES)}")
        return 1
    if not OFF_REPO.exists():
        print(f"ERROR  {OFF_REPO.relative_to(REPO)} is missing")
        return 1
    text = OFF_REPO.read_text()
    if ENTRY_MARKER not in text:
        print(f"ERROR  {OFF_REPO.relative_to(REPO)} has lost its entry marker")
        return 1

    when = args.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    block = [
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
    ]
    OFF_REPO.write_text(text.replace(ENTRY_MARKER, ENTRY_MARKER + "\n".join(block), 1))
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
    if gh.session is None and not _have_gh():
        print("ERROR  no usable GitHub path: set $GITHUB_PAT (with `requests` "
              "installed) or install and sign in to the `gh` CLI.")
        return 1
    entries, silent, no_protocol = collect(gh, args.days)
    body = render(entries, silent, no_protocol, args.days)
    if args.stdout:
        print(body)
    else:
        DERIVED.parent.mkdir(parents=True, exist_ok=True)
        DERIVED.write_text(body)
        print(f"wrote {DERIVED.relative_to(REPO)}: {len(entries)} cards, "
              f"{len(silent)} repositories with unexplained movement")
    return 0


def _have_gh() -> bool:
    return subprocess.run(["which", "gh"], capture_output=True).returncode == 0


if __name__ == "__main__":
    sys.exit(main())
