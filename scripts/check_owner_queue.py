#!/usr/bin/env python3
"""check_owner_queue.py — flag owner-queue items whose cited PRs already landed.

================================ PROVENANCE ================================
Why added : P2 (QUEUE GENERATION) of the fleet centralization plan (superbot
            docs/planning/fleet-centralization-plan-2026-07-11.md §3b): the
            owner queue is hand-curated, so an item citing "MERGE PR #N" or
            "RESOLVED-PENDING-MERGE of PR #N" silently rots the moment the
            PR lands — on 2026-07-11 items 1–3 and 13 of the live queue
            would ALL have fired (their cited PRs merged earlier that day).
            This checker queries live PR state at each wake/regen and flags
            already-merged/closed citations, so no already-done item
            survives a sweep. Promoted from the session-idea
            `verify_owner_queue.py` named in the plan.
Date      : 2026-07-11 (lane worker, model: fable-5, dispatched by
            coordinator cse_012o8pySy5K3AV6JWoPKryZL; fleet-manager PR #85)
Reliability: unverified — confirm its output against ground truth a few
            times across sessions before trusting it.
            Fixture run 1 (2026-07-11, PR #85): known-bad fixture (items
            citing fm PR #76 + superbot-games PR #34, both truly merged
            earlier that day) fired on every planted citation, live API and
            offline --selftest; known-good fixture came back clean —
            verbatim output in the PR #85 session card.
Kill-switch: delete this if it proves unreliable over multiple sessions.
=============================================================================

WHAT IT CHECKS (docs/owner-queue.md, or --queue PATH)
  1. MERGED-CITATION DRIFT — for every ACTIVE queue item that is
     merge-actionable (title/body says MERGE, RESOLVED-PENDING-MERGE, or its
     HOW line asks for a merge click), every cited PR
     (github.com/menno420/<repo>/pull/<n> URLs; bare `PR #n` mentions are
     attributed only when the item cites exactly one repo — never guessed)
     is queried live. A cited PR that is MERGED or CLOSED-unmerged flags the
     item: the ask is (at least partially) already satisfied and the item
     needs a re-verify/sweep. An item whose own text already says
     `✅ RESOLVED` gets the softer "sweep it to the Resolved section" flag.
     1b. DIRTY PARKED PR (added 2026-07-15, oversight wake 1458Z; unverified —
     confirm against ground truth across sessions) — a cited PR that is still
     OPEN but whose live `mergeable_state` is `dirty` (merge-conflicted)
     flags the item: the row's "one-click merge" claim has rotted (the A#63
     class — fm #227 went dirty when the roster cron advanced main past it).
     Softer note when the item's own text already acknowledges the conflict
     (mentions dirty/conflict) — the checker catches SILENT rot, not
     already-surfaced state. `mergeable_state` is API-only (the HTML fallback
     carries no reliable marker, and GitHub may report `unknown` while
     recomputing) — both degrade honestly to a NOT MEASURED note, never a
     flag; the Actions regen run is the reliable venue.
  2. SLUG DISCIPLINE — every active item must carry a stable
     `- id: OQ-<slug>` line (P2: positional numbers reshuffle on every
     rewrite — the fm PR #75 renumbering broke a cross-reference), and ids
     must be unique. Reports are keyed on these slugs.
  3. POSITIONAL-REFERENCE LINT — living config surfaces (.github/,
     scripts/ minus fixtures, projects/) must not reference
     "owner-queue item <N>" by position; historical bytes (.sessions/,
     control/status.md slice records, docs/ narrative) are append-only
     records and are deliberately OUT of lint scope.
  4. SATISFIED REQUIRED-CHECK ASKS (INC-06 residue, added 2026-07-14, wake
     0434z / fm PR #185; unverified — confirm against ground truth across
     sessions) — an ACTIVE item asking the owner to add a `context` as a
     REQUIRED check is probed against the repo's live branch rules
     (GET /repos/menno420/<repo>/rules/branches/main). If the asked context
     is already required, the ask is satisfied and flags — the INC-06 class
     (OQ-MINEVERSE-PYTEST-REQUIRED-CHECK survived 3 days after the owner
     clicked it) rots silently because no PR citation exists to catch.
     Repo attribution follows the check-1 discipline: exactly one
     menno420/<repo> reference in the item, else note-skip (never guessed).
     In agent sessions api.github.com is proxy-walled (403) and there is no
     HTML fallback for rules — the probe degrades honestly to NOT MEASURED;
     the Actions regen run is the reliable venue for this check.

API ACCESS
  Plain REST via urllib (stdlib only) — the same access class the
  roster-regen workflow proved works from an Actions runner (fleet-manager
  PR #82–#84; machine-merged roster gen #7 ad8659a). Sends
  `Authorization: Bearer $GITHUB_TOKEN` when the env var is set (Actions);
  anonymous otherwise (sessions — all cited repos are public today except
  pokemon-mod-lab). A PR that cannot be queried degrades HONESTLY to
  "NOT MEASURED (wall: <verbatim>)" and never flags — walls are reported,
  never guessed through.

SEVERITY CONTRACT (decide-and-flag; the plan doc leaves it unstated)
  REPORT-ONLY in the regen workflow: run with --advisory (print flags as
  ::warning::, always exit 0) — a stale queue item must alert, never jam an
  unrelated merge. Direct runs exit 1 when anything flags, 0 when clean.

USAGE
  python3 scripts/check_owner_queue.py                    # live, repo queue
  python3 scripts/check_owner_queue.py --queue PATH       # live, fixture
  python3 scripts/check_owner_queue.py --advisory         # report-only
  python3 scripts/check_owner_queue.py --selftest         # offline fixtures

No third-party deps: stdlib only.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

API_BASE = "https://api.github.com/repos/menno420"
PR_URL_RE = re.compile(r"github\.com/menno420/([\w.-]+)/pull/(\d+)")
BARE_PR_RE = re.compile(r"\bPR\s*#(\d+)\b")
ID_LINE_RE = re.compile(r"^\s*-\s*id:\s*(OQ-[A-Z0-9-]+)\s*$")
ITEM_START_RE = re.compile(r"^(\d+)\.\s+(.*)$")
MERGE_ACTION_RE = re.compile(r"\bMERGE\b|RESOLVED-PENDING-MERGE|"
                             r"\bHOW\b[^\n]*\bmerge\b", re.IGNORECASE)
RESOLVED_SELF_RE = re.compile(r"✅\s*RESOLVED")
# Check 1b: an item that already names the conflict is surfaced state, not
# silent rot — downgrade the dirty-parked flag to a note.
DIRTY_ACK_RE = re.compile(r"\bdirty\b|\bconflict", re.IGNORECASE)
POSITIONAL_REF_RE = re.compile(r"owner[- ]queue\s+item\s+#?\d+", re.IGNORECASE)
# Check 4 (INC-06 residue): "add/make/set/tick/enable … `<context>` … required"
# — the backticked context must sit near the ask verb and the word
# "required" near the context, so prose that merely mentions "required"
# elsewhere never fires.
REQUIRED_CHECK_ASK_RE = re.compile(
    r"\b(?:add|make|set|tick|enable)\b[^\n`]{0,80}`([\w][\w .\-/]*)`"
    r"[^\n]{0,60}\brequired\b", re.IGNORECASE)
REPO_REF_RE = re.compile(r"menno420/([\w.-]+?)(?=[/\s`).,;:]|$)")


def repo_root() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ------------------------------------------------------------- parsing -----

def parse_queue(text: str) -> list[dict]:
    """Split the ACTIVE region of an owner-queue file into items.

    Active region = from '## Active queue' to the next '## ' heading
    ('### ' sub-groups stay inside). Each numbered item carries: number,
    slug id (or None), title line, full body text.
    """
    lines = text.splitlines()
    items: list[dict] = []
    active = False
    current: dict | None = None
    for line in lines:
        if line.startswith("## "):
            if current:
                items.append(current)
                current = None
            active = line.lower().startswith("## active queue")
            continue
        if not active:
            continue
        m = ITEM_START_RE.match(line)
        if m:
            if current:
                items.append(current)
            current = {"number": int(m.group(1)), "id": None,
                       "title": m.group(2).strip(), "body": [line]}
            continue
        if current is not None:
            if line.startswith("### "):
                items.append(current)
                current = None
                continue
            current["body"].append(line)
            idm = ID_LINE_RE.match(line)
            if idm:
                current["id"] = idm.group(1)
    if current:
        items.append(current)
    for it in items:
        it["text"] = "\n".join(it["body"])
    return items


def cited_prs(item: dict) -> tuple[list[tuple[str, str]], list[str]]:
    """(repo, number) citations of an item + notes about skipped bare refs."""
    pairs = list(dict.fromkeys(PR_URL_RE.findall(item["text"])))
    notes: list[str] = []
    repos = {r for r, _ in pairs}
    bare = [n for n in BARE_PR_RE.findall(item["text"])
            if n not in {num for _, num in pairs}]
    if bare:
        if len(repos) == 1:
            only = next(iter(repos))
            for n in dict.fromkeys(bare):
                pairs.append((only, n))
        else:
            which = ("no repo URL" if not repos
                     else f"{len(repos)} different repos")
            notes.append(f"bare PR refs #{', #'.join(dict.fromkeys(bare))} "
                         f"skipped (item cites {which} — attribution would "
                         "be a guess, and walls/guesses are never invented)")
    return pairs, notes


# ------------------------------------------------------------ PR state -----

# Fallback marker: PR pages embed exactly ONE `"state":"OPEN|CLOSED|MERGED"`
# JSON payload marker (verified on both page styles 2026-07-11: open #85
# React payload, merged #76 — one occurrence each); older server-rendered
# pages carry the `State State--merged` badge class instead. Heuristic tier:
# covered by this script's UNVERIFIED header — confirm across sessions.
HTML_JSON_STATE_RE = re.compile(r'"state":"(OPEN|CLOSED|MERGED)"')
HTML_BADGE_STATE_RE = re.compile(r"State State--(open|closed|merged|draft)")


def fetch_pr_state(repo: str, number: str, token: str | None,
                   cache: dict) -> dict:
    key = (repo, number)
    if key in cache:
        return cache[key]

    def wall(reason: str) -> dict:
        return {"state": None, "merged": False, "merged_at": None,
                "mergeable_state": None, "wall": reason}

    url = f"{API_BASE}/{repo}/pulls/{number}"
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "fleet-manager-check-owner-queue",
        **({"Authorization": f"Bearer {token}"} if token else {}),
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
        state = {"state": data.get("state"), "merged": bool(data.get("merged")),
                 "merged_at": data.get("merged_at"),
                 "mergeable_state": data.get("mergeable_state"), "wall": None}
    except (urllib.error.URLError, OSError, json.JSONDecodeError) as api_exc:
        # SESSION FALLBACK (live-verified 2026-07-11): in agent sessions the
        # egress proxy policy-blocks api.github.com — verbatim
        # `HTTP Error 403: Forbidden`, with AND without a token — while
        # github.com itself is allowed (it is the git-transport host the
        # roster regen already relies on). Read the PR's public page and
        # extract its single embedded state marker. Actions runners never
        # take this branch (their api.github.com works, PR #82–#84 proof).
        page = f"https://github.com/menno420/{repo}/pull/{number}"
        req2 = urllib.request.Request(page, headers={
            "User-Agent": "fleet-manager-check-owner-queue"})
        try:
            with urllib.request.urlopen(req2, timeout=30) as resp:
                html = resp.read().decode("utf-8", "replace")
            m = (HTML_JSON_STATE_RE.search(html)
                 or HTML_BADGE_STATE_RE.search(html))
            if m:
                s = m.group(1).lower()
                state = {"state": "open" if s in ("open", "draft") else "closed",
                         "merged": s == "merged",
                         "merged_at": ("(timestamp n/a — html fallback)"
                                       if s == "merged" else None),
                         # html pages carry no reliable mergeable_state
                         # marker — check 1b degrades to NOT MEASURED.
                         "mergeable_state": None,
                         "wall": None}
            else:
                state = wall(f"api: {api_exc}; html fallback: page fetched "
                             "but no state marker found (format drift?)")
        except (urllib.error.URLError, OSError) as html_exc:
            state = wall(f"api: {api_exc}; html fallback: {html_exc}")
    cache[key] = state
    return state


def fetch_required_contexts(repo: str, token: str | None,
                            cache: dict) -> dict:
    """Live required status-check contexts on <repo> main (check 4).

    Rules API only — no HTML fallback exists for branch rules, so a walled
    probe degrades honestly to NOT MEASURED (sessions hit the api.github.com
    proxy 403; Actions runners do not — same split as fetch_pr_state).
    """
    key = ("rules", repo)
    if key in cache:
        return cache[key]
    url = f"{API_BASE}/{repo}/rules/branches/main"
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "fleet-manager-check-owner-queue",
        **({"Authorization": f"Bearer {token}"} if token else {}),
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
        contexts: list[str] = []
        for rule in data if isinstance(data, list) else []:
            if rule.get("type") == "required_status_checks":
                for chk in (rule.get("parameters") or {}).get(
                        "required_status_checks", []):
                    ctx = chk.get("context")
                    if ctx:
                        contexts.append(ctx)
        result = {"contexts": contexts, "wall": None}
    except (urllib.error.URLError, OSError, json.JSONDecodeError) as exc:
        result = {"contexts": [], "wall": str(exc)}
    cache[key] = result
    return result


# ------------------------------------------------------------- checks ------

def check_required_check_asks(item: dict, fetch_rules, out: list[str],
                              label: str) -> int:
    """Check 4: flag required-check asks the owner already satisfied."""
    m = REQUIRED_CHECK_ASK_RE.search(item["text"])
    if not m:
        return 0
    ctx = m.group(1).strip()
    repos = list(dict.fromkeys(REPO_REF_RE.findall(item["text"])))
    if len(repos) != 1:
        which = ("no menno420/<repo> reference" if not repos
                 else f"{len(repos)} different repos")
        out.append(f"note  [{label}] required-check ask for `{ctx}` "
                   f"skipped (item cites {which} — attribution would be a "
                   "guess, and walls/guesses are never invented)")
        return 0
    st = fetch_rules(repos[0])
    if st["wall"]:
        out.append(f"note  [{label}] {repos[0]} branch rules NOT MEASURED "
                   f"(wall: {st['wall']}) — never guessed; the Actions "
                   "regen run is the reliable venue for this probe")
        return 0
    if ctx in st["contexts"]:
        out.append(f"FLAG [satisfied-required-check-ask] {label}: `{ctx}` "
                   f"is ALREADY a required check on {repos[0]} main "
                   f"(live contexts: {st['contexts']}) — the ask is "
                   "satisfied; mark it ✅ RESOLVED and sweep (INC-06 class)")
        return 1
    return 0


def check_queue(text: str, fetch, out: list[str], fetch_rules=None) -> int:
    """Run checks 1+2 (+4 when fetch_rules given). Returns flag count."""
    items = parse_queue(text)
    flags = 0
    if not items:
        out.append("FLAG [no-items] no numbered items parsed from the "
                   "Active queue region — format drift or wrong file")
        return 1
    seen_ids: dict[str, int] = {}
    for it in items:
        label = it["id"] or f"(no-id, item {it['number']})"
        if it["id"] is None:
            flags += 1
            out.append(f"FLAG [missing-slug] item {it['number']} "
                       f"({it['title'][:60]!r}) has no `- id: OQ-…` line — "
                       "positional numbers reshuffle on rewrite (the PR #75 "
                       "break); give it a stable slug")
        else:
            if it["id"] in seen_ids:
                flags += 1
                out.append(f"FLAG [duplicate-slug] {it['id']} used by items "
                           f"{seen_ids[it['id']]} and {it['number']}")
            seen_ids[it["id"]] = it["number"]
        if fetch_rules is not None:
            flags += check_required_check_asks(it, fetch_rules, out, label)
        if not MERGE_ACTION_RE.search(it["text"]):
            continue
        pairs, notes = cited_prs(it)
        for note in notes:
            out.append(f"note  [{label}] {note}")
        for repo, num in pairs:
            st = fetch(repo, num)
            if st["wall"]:
                out.append(f"note  [{label}] {repo}#{num} NOT MEASURED "
                           f"(wall: {st['wall']}) — never guessed")
                continue
            if st["merged"]:
                flags += 1
                kind = ("resolved-not-swept"
                        if RESOLVED_SELF_RE.search(it["text"])
                        else "merged-citation")
                extra = (" (item already self-declares ✅ RESOLVED — sweep "
                         "it to the Resolved section)"
                         if kind == "resolved-not-swept" else
                         " — the ask is (at least partially) satisfied; "
                         "re-verify and sweep")
                out.append(f"FLAG [{kind}] {label}: cited {repo}#{num} is "
                           f"MERGED ({st['merged_at']}){extra}")
            elif st["state"] == "closed":
                flags += 1
                out.append(f"FLAG [closed-citation] {label}: cited "
                           f"{repo}#{num} is CLOSED unmerged — the click "
                           "described no longer exists; re-verify the item")
            elif st["state"] == "open":
                # Check 1b — dirty parked PR (the A#63 class).
                ms = st.get("mergeable_state")
                if ms == "dirty":
                    if DIRTY_ACK_RE.search(it["text"]):
                        out.append(
                            f"note  [{label}] cited {repo}#{num} is OPEN "
                            "with mergeable_state=dirty, but the item "
                            "already acknowledges the conflict — "
                            "already-surfaced state, not silent rot")
                    else:
                        flags += 1
                        out.append(
                            f"FLAG [dirty-parked-pr] {label}: cited "
                            f"{repo}#{num} is OPEN but mergeable_state="
                            "dirty (merge-conflicted) — the row's "
                            "one-click merge claim has rotted; resolve "
                            "the conflict or re-verify the item "
                            "(the A#63 / fm#227 class)")
                elif ms in (None, "unknown"):
                    out.append(
                        f"note  [{label}] {repo}#{num} OPEN, "
                        f"mergeable_state NOT MEASURED "
                        f"({'html fallback carries none' if ms is None else 'GitHub still computing'}) "
                        "— dirty-parked check skipped, never guessed")
    return flags


def check_positional_refs(root: str, out: list[str]) -> int:
    """Check 3: positional owner-queue references on living config surfaces."""
    flags = 0
    scan_dirs = [".github", "scripts", "projects"]
    # projects/UNIVERSAL.md is OWNER-PROVENANCE (its own header: the owner is
    # the only writer) and its item-16 mentions are frozen v4 provenance
    # notes, not living pointers — agents can neither fix nor should flag
    # them (decide-and-flag, PR #85).
    skip_files = {os.path.join(root, "projects", "UNIVERSAL.md"),
                  os.path.abspath(__file__)}
    for d in scan_dirs:
        base = os.path.join(root, d)
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [x for x in dirnames if x != "fixtures"]
            for fn in filenames:
                if not fn.endswith((".md", ".yml", ".yaml", ".py", ".sh")):
                    continue
                path = os.path.join(dirpath, fn)
                if os.path.abspath(path) in skip_files:
                    continue
                try:
                    with open(path, encoding="utf-8") as fh:
                        for ln, line in enumerate(fh, 1):
                            if POSITIONAL_REF_RE.search(line):
                                flags += 1
                                rel = os.path.relpath(path, root)
                                out.append(
                                    f"FLAG [positional-ref] {rel}:{ln} "
                                    "references an owner-queue item by "
                                    "POSITION — renumbering breaks it (the "
                                    "PR #75 class); cite the `id: OQ-…` "
                                    "slug instead")
                except (OSError, UnicodeDecodeError):
                    continue
    return flags


# ------------------------------------------------------------ selftest -----

KNOWN_STATES = {
    # Ground truth recorded 2026-07-11 (fixture run 1):
    ("fleet-manager", "76"): {"state": "closed", "merged": True,
                              "merged_at": "2026-07-11T15:26:47Z", "wall": None},
    ("superbot-games", "34"): {"state": "closed", "merged": True,
                               "merged_at": "2026-07-11T13:40:40Z", "wall": None},
    ("fleet-manager", "85"): {"state": "open", "merged": False,
                              "merged_at": None, "mergeable_state": "clean",
                              "wall": None},
    # Ground truth recorded 2026-07-15 (oversight wake 1458Z): fm #227 went
    # mergeable_state=dirty after the roster cron (#231, Gen #59) advanced
    # main past it at 12:04Z — the A#63 queue amendment records it. Pinned
    # dirty here so the check-1b fixture never rots (live it may later read
    # `unknown` while GitHub recomputes, or merge — the stub is the pin).
    ("fleet-manager", "227"): {"state": "open", "merged": False,
                               "merged_at": None, "mergeable_state": "dirty",
                               "wall": None},
}


def selftest() -> int:
    """Offline: fixtures against recorded PR states. Exit 0 on pass."""
    root = repo_root()
    fails: list[str] = []

    def stub_fetch(repo, num):
        return KNOWN_STATES.get(
            (repo, num),
            {"state": None, "merged": False, "merged_at": None,
             "wall": f"no recorded state for {repo}#{num} (selftest stub)"})

    def stub_rules(repo):
        # Ground truth recorded 2026-07-14 (INC-06 live probe, wake 0235Z):
        # mineverse main requires exactly ["substrate-gate", "pytest"]
        # (enabler rules probe verbatim, Actions run 29260140367).
        if repo == "superbot-mineverse":
            return {"contexts": ["substrate-gate", "pytest"], "wall": None}
        return {"contexts": [],
                "wall": f"no recorded rules for {repo} (selftest stub)"}

    def run(name):
        path = os.path.join(root, "scripts", "fixtures", name)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        out: list[str] = []
        return check_queue(text, stub_fetch, out, fetch_rules=stub_rules), out

    bad_flags, bad_out = run("owner-queue-known-bad.md")
    if bad_flags < 2:
        fails.append(f"known-bad fixture must fire >=2 flags, got {bad_flags}")
    if not any("[resolved-not-swept]" in ln and "fleet-manager#76" in ln
               for ln in bad_out):
        fails.append("known-bad: RESOLVED-PENDING-MERGE of merged fm#76 "
                     "did not fire resolved-not-swept")
    if not any("[merged-citation]" in ln and "superbot-games#34" in ln
               for ln in bad_out):
        fails.append("known-bad: MERGE item citing merged games#34 did not "
                     "fire merged-citation")
    if not any("[satisfied-required-check-ask]" in ln and "pytest" in ln
               for ln in bad_out):
        fails.append("known-bad: satisfied required-check ask (mineverse "
                     "pytest, the INC-06 case) did not fire")
    if not any("[dirty-parked-pr]" in ln and "fleet-manager#227" in ln
               for ln in bad_out):
        fails.append("known-bad: parked MERGE item citing dirty fm#227 did "
                     "not fire dirty-parked-pr (the A#63 class)")
    good_flags, good_out = run("owner-queue-known-good.md")
    if good_flags != 0:
        fails.append(f"known-good fixture must be clean, got {good_flags} "
                     f"flag(s): {good_out}")
    for msg in fails:
        print(f"SELFTEST FAIL: {msg}", file=sys.stderr)
    print(f"selftest: {'FAIL' if fails else 'PASS'} ({len(fails)} failure(s))")
    if not fails:
        print("--- known-bad fixture output ---")
        print("\n".join(bad_out))
        print("--- known-good fixture output ---")
        print("\n".join(good_out) or "(clean)")
    return 1 if fails else 0


# ---------------------------------------------------------------- main -----

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--queue",
                    default=os.path.join(repo_root(), "docs", "owner-queue.md"),
                    help="queue file to check (default: docs/owner-queue.md)")
    ap.add_argument("--advisory", action="store_true",
                    help="report-only: print flags as ::warning::, exit 0")
    ap.add_argument("--selftest", action="store_true",
                    help="offline fixture assertions (no network) and exit")
    ap.add_argument("--skip-positional-lint", action="store_true",
                    help="only check the queue file (fixture runs)")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    try:
        with open(args.queue, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        print(f"check_owner_queue: cannot read {args.queue}: {exc}",
              file=sys.stderr)
        return 2

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    cache: dict = {}
    out: list[str] = []
    flags = check_queue(text, lambda r, n: fetch_pr_state(r, n, token, cache),
                        out,
                        fetch_rules=lambda r: fetch_required_contexts(
                            r, token, cache))
    if not args.skip_positional_lint:
        flags += check_positional_refs(repo_root(), out)

    for line in out:
        if args.advisory and line.startswith("FLAG"):
            print(f"::warning::{line}")
        else:
            print(line)
    verdict = ("CLEAN — no merged/closed citations, slugs intact"
               if flags == 0 else f"{flags} FLAG(S) — queue needs a sweep")
    print(f"check_owner_queue: {verdict} "
          f"(queried {len(cache)} record(s), {args.queue})")
    return 0 if (flags == 0 or args.advisory) else 1


if __name__ == "__main__":
    sys.exit(main())
