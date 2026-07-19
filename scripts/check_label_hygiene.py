#!/usr/bin/env python3
"""check_label_hygiene.py — nothing-stuck hold-label detector (fleet-wide).

================================ PROVENANCE ================================
Why added : Owner live directive 2026-07-19 ~08:00Z (verbatim, recorded in
            control/status.md + docs/fleet-triage.md): "There are 'do not
            automerge' labels in some repos and I want then gone, nothing
            should ever be stuck, I'm not going to look through PRs to merge
            them." That morning's enforcement was a one-off hand sweep
            (9 definitions found, 1 open application stripped — websites
            #434); the definitions were routed to the hub queue as
            `OQ-LABEL-DEFS-DELETE`. This script mechanizes the sweep so
            hold-label re-appearance (e.g. the websites
            `host-automerge-extras.yml` auto-re-creation trap) is caught by
            a command, not a human-style read. Planned as slice 3 of
            docs/planning/2026-07-19-next-slices.md.
Date      : 2026-07-19 (build-slice worker, model: fable-5, dispatched by
            the fleet-manager coordinator seat; fleet-manager PR #370)
Reliability: unverified — confirm its output against ground truth a few
            times across sessions before trusting it.
            Ground-truth run 1 (2026-07-19T16:1xZ, PR #370): 19/19 repos
            measured, 0 hold-class definitions, 0 open applications —
            i.e. the 9 `do-not-automerge` definitions listed in
            `OQ-LABEL-DEFS-DELETE` (queue text of 08:38Z) are GONE at run
            time; the checker is the item's verification command
            ("re-run after deletions → 0 definitions"). Verbatim table in
            the PR #370 body + session card.
Kill-switch: delete this if it proves unreliable over multiple sessions.
=============================================================================

WHAT IT DOES
  For every fleet repo (gen_roster.LANES entries with a repo, live AND
  archived — a parked PR in an archived repo is still a stuck item — plus
  EXTRA_REPOS below):

    1. Read the repo's label DEFINITIONS (GET /repos/<o>/<r>/labels) and
       classify each against the hold-class vocabulary (below).
    2. For each hold-class definition found, read the OPEN issues/PRs
       carrying it (GET /repos/<o>/<r>/issues?labels=<name>&state=open —
       the issues API returns PRs too; an item is a PR iff it has a
       `pull_request` key). Completeness note: on GitHub an applied label
       always has a repo-level definition (deleting the definition strips
       it everywhere), so scanning applications only under found
       definitions misses nothing.

HOLD-CLASS VOCABULARY (normalized: lowercased, spaces/underscores→hyphens)
  Ground truth for what actually parks a PR in this fleet is
  .github/workflows/merge-on-green.yml `PARK_LABELS = {"do-not-automerge",
  "owner-held"}` (and the websites twin's carve-out). The pattern set
  covers those plus known/likely variants:
    do-not-automerge · do-not-merge · owner-held · owner-hold · on-hold ·
    hold · held · parked · park · blocked · stuck · needs-hermes-review
    (superbot's retired park label, Q-0197 — must never reappear)
  DELIBERATELY EXCLUDED: `needs-human-review` (fleet-manager's codex-triage
  routing label — merge-on-green ignores it, it routes attention, holds
  nothing) and the codex-cleared/codex-flagged pair, same tier.

API ACCESS (same class as check_owner_queue.py, PR #82–#84 lineage)
  Plain REST via urllib, stdlib only. Two-rung transport per request:
  direct egress first (proxy bypass — the CAPABILITIES direct-PAT path;
  in agent sessions the *proxied* api.github.com 403s, a path quirk not a
  wall), then the default (proxied) opener once (Actions runners' working
  path). Sends `Authorization: Bearer` from $GITHUB_PAT or $GITHUB_TOKEN
  when set; anonymous otherwise (all fleet repos public except
  pokemon-mod-lab). RATE-LIMIT AWARE: a 403/429 (anonymous IP quota on
  shared egress is routinely exhausted — verbatim observed this session)
  degrades that repo to `NOT MEASURED (wall: <verbatim>)` and the sweep
  CONTINUES; walls are reported, never guessed through.

OUTPUT
  Markdown per-repo table + one headline (N hold-class definitions ·
  M applications to OPEN items · K repos not measured). Every finding
  emits a WARN line with its paste-ready remedy:
    application → strip via MCP (`issue_write`/label removal) or the hub
      REST one-liner (DELETE .../issues/<n>/labels/<name>);
    definition  → hub REST one-liner
      (DELETE /repos/menno420/<repo>/labels/<name>, direct-egress PAT
      path) — the `OQ-LABEL-DEFS-DELETE` remedy shape. Re-run this script
      after deletions → 0 definitions is the verification.

EXIT CONTRACT (advisory tier, same as the S3/S5/S9 trio + lane-liveness —
NEVER merge-blocking, not wired into `bootstrap.py check`):
  default    exit 0 always (table + headline + WARNs).
  --strict   exit 1 ONLY when a hold label is applied to an OPEN item
             (a mere definition stays WARN-only — it can't park anything
             until applied). An unmeasured repo never satisfies --strict
             cleanliness silently: the headline names the count.

USAGE
  python3 scripts/check_label_hygiene.py                    # full fleet
  python3 scripts/check_label_hygiene.py --repos websites,fleet-manager
  python3 scripts/check_label_hygiene.py --strict           # gate use
  python3 scripts/check_label_hygiene.py --selfcheck        # pure logic

No third-party deps: stdlib + the sibling gen_roster module (LANES only).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import gen_roster  # noqa: E402  (sibling module: LANES — the one lane→repo map)

OWNER = "menno420"
API_BASE = f"https://api.github.com/repos/{OWNER}"

# Fleet repos NOT in gen_roster.LANES (which is lane/seat-keyed): the
# Curious Research seat is registry-only there ("no repo"), but the repo
# exists and is fleet stock (verified readable 2026-07-19, this slice).
# HAND-MAINTAINED, same doctrine as gen_roster.LANES / SEAT_COVER.
EXTRA_REPOS = ["curious-research"]

# Hold-class patterns over the NORMALIZED name (see normalize()). Anchored
# full-match so `hold` never fires on e.g. `holdings-parser`.
HOLD_PATTERNS = [
    r"do-not-(?:auto-?)?merge",
    r"owner-hold|owner-held",
    r"on-hold|hold|held",
    r"parked?",
    r"blocked|stuck",
    r"needs-hermes-review",   # superbot's retired park label (Q-0197)
]
HOLD_RE = re.compile(r"^(?:" + "|".join(HOLD_PATTERNS) + r")$")


def normalize(name: str) -> str:
    return re.sub(r"[\s_]+", "-", name.strip().lower())


def is_hold_label(name: str) -> bool:
    return bool(HOLD_RE.match(normalize(name)))


def fleet_repos() -> list[str]:
    repos = [lane["repo"] for lane in gen_roster.LANES if lane.get("repo")]
    return repos + [r for r in EXTRA_REPOS if r not in repos]


# ------------------------------------------------------------ transport ----

_DIRECT = urllib.request.build_opener(urllib.request.ProxyHandler({}))
_PROXIED = urllib.request.build_opener()


def api_get(path: str, token: str | None) -> tuple[object | None, str | None]:
    """(json, None) on success, (None, verbatim wall) on failure.

    Two rungs, each attempted once: direct egress (sessions' working path),
    then the default proxied opener (Actions runners' working path). The
    wall string quotes BOTH failures verbatim — nothing invented.
    """
    req = urllib.request.Request(API_BASE + path, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "fleet-manager-check-label-hygiene",
        **({"Authorization": f"Bearer {token}"} if token else {}),
    })
    walls = []
    for tag, opener in (("direct", _DIRECT), ("proxied", _PROXIED)):
        try:
            with opener.open(req, timeout=30) as resp:
                return json.loads(resp.read().decode()), None
        except urllib.error.HTTPError as exc:
            remaining = exc.headers.get("X-RateLimit-Remaining")
            extra = (f", X-RateLimit-Remaining: {remaining}"
                     if remaining is not None else "")
            walls.append(f"{tag}: HTTP {exc.code} {exc.reason}{extra}")
        except (urllib.error.URLError, OSError,
                json.JSONDecodeError) as exc:
            walls.append(f"{tag}: {exc}")
    return None, "; ".join(walls)


# ------------------------------------------------------------- measure -----

def measure_repo(repo: str, token: str | None) -> dict:
    """One repo's row: hold definitions + open applications, or the wall."""
    row = {"repo": repo, "definitions": [], "applications": [],
           "wall": None, "app_walls": []}
    labels, wall = api_get(f"/{repo}/labels?per_page=100", token)
    if wall is not None:
        row["wall"] = wall
        return row
    row["definitions"] = [lab["name"] for lab in labels
                          if is_hold_label(lab.get("name", ""))]
    for name in row["definitions"]:
        q = urllib.parse.quote(name)
        items, wall = api_get(
            f"/{repo}/issues?labels={q}&state=open&per_page=100", token)
        if wall is not None:
            row["app_walls"].append(f"{name}: {wall}")
            continue
        for it in items:
            row["applications"].append({
                "number": it.get("number"),
                "kind": "PR" if "pull_request" in it else "issue",
                "label": name,
                "title": (it.get("title") or "")[:70],
            })
    return row


# -------------------------------------------------------------- render -----

def remedy_definition(repo: str, name: str) -> str:
    q = urllib.parse.quote(name)
    return (f"delete the definition (hub REST one-liner, direct-egress PAT "
            f"path — the `OQ-LABEL-DEFS-DELETE` remedy shape): "
            f"curl --noproxy '*' -sS -X DELETE -H \"Authorization: Bearer "
            f"$GITHUB_PAT\" {API_BASE}/{repo}/labels/{q}")


def remedy_application(repo: str, app: dict) -> str:
    q = urllib.parse.quote(app["label"])
    return (f"strip it via MCP (GitHub `issue_write`/label update on "
            f"{OWNER}/{repo} #{app['number']}) or the hub REST one-liner: "
            f"curl --noproxy '*' -sS -X DELETE -H \"Authorization: Bearer "
            f"$GITHUB_PAT\" {API_BASE}/{repo}/issues/{app['number']}"
            f"/labels/{q}")


def render(rows: list[dict]) -> tuple[str, int, int, int]:
    out = ["# Label hygiene — nothing-stuck hold-label detector",
           "",
           "| Repo | Hold-class definitions | Open items carrying one "
           "| Verdict |",
           "|---|---|---|---|"]
    n_defs = n_apps = n_unmeasured = 0
    warns: list[str] = []
    for r in rows:
        if r["wall"] is not None:
            n_unmeasured += 1
            out.append(f"| {r['repo']} | — | — "
                       f"| NOT MEASURED (wall: {r['wall']}) |")
            continue
        n_defs += len(r["definitions"])
        n_apps += len(r["applications"])
        defs = ", ".join(f"`{d}`" for d in r["definitions"]) or "none"
        apps = ", ".join(f"#{a['number']} ({a['kind']}, `{a['label']}`)"
                         for a in r["applications"]) or "none"
        if r["applications"]:
            verdict = "STUCK-RISK (open item held)"
        elif r["app_walls"]:
            verdict = "definition present; applications NOT MEASURED"
            n_unmeasured += 0  # counted in headline note via warns below
        elif r["definitions"]:
            verdict = "definition present (parkable)"
        else:
            verdict = "clean"
        out.append(f"| {r['repo']} | {defs} | {apps} | {verdict} |")
        for d in r["definitions"]:
            warns.append(f"WARN {r['repo']}: hold-class label definition "
                         f"`{d}` exists — {remedy_definition(r['repo'], d)}")
        for a in r["applications"]:
            warns.append(f"WARN {r['repo']} #{a['number']} (OPEN "
                         f"{a['kind']}: \"{a['title']}\") carries "
                         f"`{a['label']}` — directive violation ("
                         f"nothing-stuck, 2026-07-19) — "
                         f"{remedy_application(r['repo'], a)}")
        for aw in r["app_walls"]:
            warns.append(f"WARN {r['repo']}: applications not measured "
                         f"for {aw}")
    out += ["",
            f"HEADLINE: {n_defs} hold-class definition(s) · {n_apps} "
            f"application(s) to OPEN items · {n_unmeasured} repo(s) not "
            f"measured (of {len(rows)})"]
    if warns:
        out += [""] + warns
    return "\n".join(out), n_defs, n_apps, n_unmeasured


# ----------------------------------------------------------- selfcheck -----

def selfcheck() -> int:
    """Offline pins of the pure logic (no network)."""
    # classification — the 08:38Z sweep vocabulary and known variants
    for name in ("do-not-automerge", "Do Not Automerge", "do_not_merge",
                 "owner-held", "owner-hold", "on-hold", "HOLD", "held",
                 "parked", "blocked", "stuck", "needs-hermes-review",
                 "do-not-auto-merge"):
        assert is_hold_label(name), name
    # deliberate exclusions + anchored-match safety
    for name in ("needs-human-review", "codex-cleared", "codex-flagged",
                 "holdings-parser", "shareholder", "unblocked", "bug",
                 "enhancement", "reconcile", "friction"):
        assert not is_hold_label(name), name
    # exit contract: strict fires only on applications to OPEN items
    clean = {"repo": "x", "definitions": [], "applications": [],
             "wall": None, "app_walls": []}
    defs_only = dict(clean, definitions=["do-not-automerge"])
    applied = dict(defs_only, applications=[{
        "number": 7, "kind": "PR", "label": "do-not-automerge",
        "title": "t"}])
    walled = dict(clean, wall="direct: HTTP 403 rate limit; proxied: ...")
    _, d, a, u = render([clean])
    assert (d, a, u) == (0, 0, 0)
    _, d, a, u = render([defs_only])
    assert (d, a, u) == (1, 0, 0)
    text, d, a, u = render([applied, walled])
    assert (d, a, u) == (1, 1, 1)
    assert "STUCK-RISK" in text and "NOT MEASURED" in text
    assert "OQ-LABEL-DEFS-DELETE" in text  # remedy cites the queue item
    assert "issues/7/labels/do-not-automerge" in text  # paste-ready strip
    # repo universe: LANES repos + curious-research, no dupes
    repos = fleet_repos()
    assert "fleet-manager" in repos and "curious-research" in repos
    assert len(repos) == len(set(repos))
    print(f"selfcheck OK (pins over {len(repos)}-repo universe)")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repos", help="comma-separated repo filter")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 when any OPEN item carries a hold label")
    ap.add_argument("--selfcheck", action="store_true")
    args = ap.parse_args(argv)
    if args.selfcheck:
        return selfcheck()
    token = os.environ.get("GITHUB_PAT") or os.environ.get("GITHUB_TOKEN")
    repos = fleet_repos()
    if args.repos:
        wanted = {r.strip() for r in args.repos.split(",") if r.strip()}
        repos = [r for r in repos if r in wanted]
    rows = [measure_repo(repo, token) for repo in repos]
    text, _, n_apps, _ = render(rows)
    print(text)
    if args.strict and n_apps:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
