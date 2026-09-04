#!/usr/bin/env python3
"""Estate baseline delta — has a repository's authoritative state moved since
the prior evidence measured it?

The successor plan's step 2 is *re-audit only where the information changed*
(`docs/planning/2026-08-30-fresh-start-redirect.md` § His sequence, item 2).
That test is only honest if it is mechanical and repeatable, so this script
computes it rather than leaving it to a reading.

For each row of the anchor file it resolves two points on the repository's
default branch and reports the commits between them:

  baseline  the last commit on the default branch at or before the prior
            evidence's measurement instant.  Most of this estate's 2026-08
            audit wave recorded a DATE and no SHA, so the SHA is recovered
            from the date via the API rather than invented.
  live      the default branch tip right now.

Usage
-----
    python3 tools/estate_baseline/delta.py \
        --anchors docs/findings/data/2026-09-04-estate-truth-baseline/anchors.tsv \
        --out     docs/findings/data/2026-09-04-estate-truth-baseline/delta.tsv

Anchor file: TSV, one row per repository, `#` comments and blank lines skipped.

    repo <TAB> baseline_utc <TAB> evidence_ref <TAB> certainty

`baseline_utc` is an ISO-8601 instant (`2026-08-21T00:00:00Z`). Use the START
of the measurement day: an audit written on the 21st read a tree that existed
that day, and taking the day's end would silently absorb same-day commits the
audit never saw.

Network: the proxied GitHub REST path 403s in this estate, so every call goes
out on direct egress with `$GITHUB_PAT` (`docs/CAPABILITIES.md`).

Exit codes: 0 all rows resolved · 1 one or more rows unresolved (the row is
still written, with `status=INACCESSIBLE` and the wall in `note`) · 2 usage.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.github.com"
OWNER = "menno420"


def _get(path: str, token: str) -> tuple[int, object]:
    """One direct-egress GET. Returns (status, decoded-json-or-error-text)."""
    req = urllib.request.Request(
        API + path,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "estate-baseline-delta",
        },
    )
    # The estate's git/HTTP proxy 403s the REST path; bypass it explicitly
    # rather than inheriting proxy env vars.
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(req, timeout=60) as resp:
            return resp.status, json.load(resp)
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace")[:300]
    except Exception as exc:  # noqa: BLE001 — the wall text is the deliverable
        return 0, f"{type(exc).__name__}: {exc}"


def default_branch(repo: str, token: str) -> tuple[str | None, str]:
    status, body = _get(f"/repos/{OWNER}/{repo}", token)
    if status != 200 or not isinstance(body, dict):
        return None, f"repo lookup HTTP {status}: {body}"
    return body["default_branch"], ""


def commit_at(repo: str, branch: str, until: str | None, token: str) -> tuple[dict | None, str]:
    """The newest commit on `branch` at or before `until` (or the tip)."""
    q = {"sha": branch, "per_page": "1"}
    if until:
        q["until"] = until
    status, body = _get(f"/repos/{OWNER}/{repo}/commits?" + urllib.parse.urlencode(q), token)
    if status != 200:
        return None, f"commits HTTP {status}: {body}"
    if not isinstance(body, list) or not body:
        return None, f"no commit on {branch} at or before {until or 'HEAD'}"
    c = body[0]
    return {"sha": c["sha"], "date": c["commit"]["committer"]["date"]}, ""


def commits_between(repo: str, base: str, head: str, token: str) -> tuple[int | None, str]:
    """Commits on head not on base — and never 0 for a head that is not base.

    `ahead_by` alone is not enough. If a default branch is force-reset to an
    ancestor of the recovered baseline, compare returns `status: "behind"` with
    `ahead_by == 0` while the head SHA and tree genuinely differ, and the
    repository would be classified UNCHANGED_REUSABLE and skipped — the one case
    where skipping a re-audit is least safe, because history was rewritten.
    """
    if base == head:
        return 0, ""
    status, body = _get(f"/repos/{OWNER}/{repo}/compare/{base}...{head}", token)
    if status != 200 or not isinstance(body, dict):
        return None, f"compare HTTP {status}: {body}"
    ahead = body.get("ahead_by")
    if ahead == 0:
        # different SHAs, nothing ahead: behind or diverged. Report it as moved,
        # with the compare status so the reason survives into the TSV.
        return max(1, body.get("behind_by") or 1), \
            f"head differs from baseline with ahead_by=0 (compare status: {body.get('status')})"
    return ahead, ""


def classify(ahead: int | None, archived: bool) -> str:
    """The mechanical half only.

    UNCHANGED / CHANGED is a fact about the tree and is decided here.
    WEAK_OR_INCOMPLETE and NEW are judgements about the *prior evidence*, not
    about movement, so they are set in the anchor file's certainty column and
    applied by the caller — a script must not launder a judgement into a
    measurement.
    """
    if ahead is None:
        return "INACCESSIBLE"
    if archived:
        return "ARCHIVED_OR_NONACTIVE"
    return "UNCHANGED_REUSABLE" if ahead == 0 else "CHANGED_REAUDIT"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--anchors", required=True, help="TSV: repo, baseline_utc, evidence_ref, certainty")
    ap.add_argument("--out", help="write TSV here (default: stdout)")
    args = ap.parse_args()

    token = os.environ.get("GITHUB_PAT")
    if not token:
        print("delta: GITHUB_PAT is not set", file=sys.stderr)
        return 2

    rows, unresolved = [], 0
    with open(args.anchors, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                print(f"delta: malformed anchor row: {line!r}", file=sys.stderr)
                return 2
            repo, baseline_utc, ref, certainty = (p.strip() for p in parts[:4])

            status_code, meta = _get(f"/repos/{OWNER}/{repo}", token)
            if status_code != 200 or not isinstance(meta, dict):
                rows.append([repo, "", "", "", "", "INACCESSIBLE", ref, certainty,
                             f"repo lookup HTTP {status_code}: {meta}"])
                unresolved += 1
                continue
            branch, archived = meta["default_branch"], bool(meta["archived"])

            base, err_b = commit_at(repo, branch, baseline_utc, token)
            head, err_h = commit_at(repo, branch, None, token)
            if base is None or head is None:
                rows.append([repo, branch, "", "", "", "INACCESSIBLE", ref, certainty,
                             (err_b or err_h)])
                unresolved += 1
                continue

            ahead, err_c = commits_between(repo, base["sha"], head["sha"], token)
            note = err_c
            if ahead is None:
                unresolved += 1
            rows.append([
                repo, branch,
                f'{base["sha"][:12]}@{base["date"]}',
                f'{head["sha"][:12]}@{head["date"]}',
                "" if ahead is None else str(ahead),
                classify(ahead, archived),
                ref, certainty, note,
            ])

    header = ["repo", "branch", "baseline_commit", "live_commit",
              "commits_since", "delta_status", "evidence_ref",
              "prior_certainty", "note"]
    out = "\n".join("\t".join(r) for r in [header] + rows) + "\n"
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(out)
        print(f"delta: {len(rows)} rows -> {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(out)
    return 1 if unresolved else 0


if __name__ == "__main__":
    raise SystemExit(main())
