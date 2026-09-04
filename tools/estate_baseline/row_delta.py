#!/usr/bin/env python3
"""Row-level source drift for the `estate` seed manifest — did the FILE a row
cites change since the SHA the row was verified at?

`delta.py` answers the question per repository: has the default branch moved
since the prior evidence measured it? That is the right first question and the
wrong last one. A repository can take sixteen commits that touch none of the
files a manifest row cites, and one commit that rewrites the one file a `carry`
row copies. The baseline's own handoff (finding § 11, "every `carry` row's source
SHA") asks the seed session to re-check each row; this script makes that check
mechanical, so it is run rather than remembered.

For each manifest row it:

  1. reads the row's provenance — `source_path` and `verification_point` — and
     classifies its SHAPE. The survival rule tests these fields for
     non-emptiness only (finding § 12 item 10), so a narration such as
     `(live PR list)` passes as provenance. Here a row whose provenance cannot
     be resolved to a path and a commit is published as `UNCHECKABLE` with the
     reason, never silently skipped and never guessed at;
  2. resolves the verification SHA(s) in the row's source repository. Where a
     row names two (a reading and a later re-read) the LATER one is the
     verification point — it is the last time anyone confirmed the content;
  3. compares the cited path's blob (or, for a directory, its tree listing) at
     that SHA against the same path at the live default-branch tip. Identical
     object SHAs mean the content the reader verified is the content that is
     live. Anything else is drift, and the kind of drift is named.

Row status vocabulary (one per row; `paths_checked` carries the per-path detail):

  SOURCE_UNCHANGED                 every cited path is byte-identical at the tip
  SOURCE_MOVED                     at least one cited path differs at the tip
  SOURCE_GONE                      a cited path existed at the SHA and is absent at the tip
  SOURCE_MISSING_AT_VERIFICATION   a cited path did not exist at the SHA the row
                                   claims to have read it at — a provenance defect
  SOURCE_NOT_FOUND                 the path exists at neither point
  UNCHECKABLE:<reason>             provenance that cannot be resolved (no path,
                                   no SHA, SHA not in the source repository, …)
  INACCESSIBLE:<reason>            an API wall — recorded, never classified

Precedence when a row cites several paths: GONE > MOVED > MISSING_AT_VERIFICATION
> NOT_FOUND > UNCHANGED, because the worst case is the one a `carry` must hear.

Usage
-----
    python3 tools/estate_baseline/row_delta.py \
        --manifest docs/planning/2026-09-04-estate-seed-manifest.csv \
        --classification docs/findings/data/2026-09-04-estate-truth-baseline/classification.json \
        [--delta docs/findings/data/2026-09-04-estate-truth-baseline/delta.tsv] \
        --out docs/findings/data/2026-09-04-estate-truth-baseline/row-delta.tsv

`--delta` joins the repository-level result onto each row (`repo_delta_status`,
`repo_commits_since`) so the two instruments can be read side by side: a row
reading SOURCE_UNCHANGED inside a CHANGED_REAUDIT repository is the case this
script exists for.

Network: direct egress with `$GITHUB_PAT`, as `delta.py` (the proxied REST path
403s in this estate — `docs/CAPABILITIES.md`).

Exit: 0 every row classified (UNCHECKABLE is a classification) · 1 one or more
rows INACCESSIBLE · 2 usage/input error.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.github.com"
OWNER = "menno420"

COLUMNS = [
    "subject", "source_repo", "survives", "disposition", "certainty",
    "provenance_shape", "verification_shape", "verification_sha",
    "verification_sha_date", "sha_on_default_branch", "live_sha", "live_sha_date",
    "repo_delta_status", "repo_commits_since", "row_status", "paths_checked", "note",
]

# --- provenance parsing ----------------------------------------------------------

_PATH_TOKEN = re.compile(r"^[A-Za-z0-9_./@+\-]+$")
_PAREN = re.compile(r"\([^)]*\)")
_HEX = re.compile(r"(?<![0-9A-Za-z])([0-9a-f]{7,40})(?![0-9A-Za-z])")
_INSTANT = re.compile(r"\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}:\d{2}Z?)?")
_CANON_VP = re.compile(r"^\s*[0-9a-f]{7,40}@\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}:\d{2}Z?)?\s*$")


def paths_of(source_path: str) -> tuple[list[str], str]:
    """Path tokens in a `source_path` cell, and the SHAPE of the cell.

    Readers wrote this field four ways on live data: one path; several joined
    by `;` or `,`; a path followed by a parenthetical annotation (`docs/ESTATE.md
    (cross-reference line)`); and pure narration (`(live PR list)`). Parenthetical
    groups are stripped, the remainder split, and only tokens that look like a
    repository path are kept. Anything dropped is reported in the shape, so a
    reader can see that the cell was not a clean path even when a path was
    recovered from it.
    """
    raw = source_path or ""
    stripped = _PAREN.sub(" ", raw)
    had_annotation = stripped != raw
    paths, dropped = [], []
    for tok in re.split(r"[;,]", stripped):
        t = tok.strip().strip("`'\"")
        if not t:
            continue
        if _PATH_TOKEN.match(t) and ("/" in t or "." in t) and not t.lower().startswith("http"):
            paths.append(t)
        else:
            dropped.append(t)
    if dropped:
        had_annotation = True
    if not paths:
        return [], "narration"
    shape = "path" if len(paths) == 1 else f"paths:{len(paths)}"
    return paths, shape + ("+annotation" if had_annotation else "")


def shas_of(verification_point: str) -> tuple[list[str], str]:
    """Candidate SHAs in a `verification_point` cell, and the cell's SHAPE.

    The canonical form is `<sha>@<instant>`. Live cells also read `sha7d99f7d@…`
    (a `sha` prefix glued to the hex), `sha@21b19be`, `caa6cd2, headers read`
    (no instant), `caa6cd2; re-read at 7ccc88a` (two SHAs), and `live-api@…`
    (no SHA at all). Every hex run of 7–40 characters that contains a digit is a
    candidate — the digit rule keeps English words spelt in hex letters
    (`defaced`) out — and resolution against the repository decides which are
    commits.
    """
    raw = verification_point or ""
    cleaned = re.sub(r"\bsha@?", " ", raw, flags=re.I)
    seen: list[str] = []
    for m in _HEX.finditer(cleaned):
        h = m.group(1)
        if re.search(r"\d", h) and h not in seen:
            seen.append(h)
    # The shape is judged on the SAME candidates the caller will resolve: an
    # earlier draft tested the raw hex regex here and called `defaced by nobody`
    # sha-only while returning no SHA for it — two answers to one question.
    if _CANON_VP.match(raw):
        shape = "sha@instant"
    else:
        has_instant = bool(_INSTANT.search(raw))
        shape = {(True, True): "sha+instant", (True, False): "sha-only",
                 (False, True): "instant-only", (False, False): "narration"}[(bool(seen), has_instant)]
    return seen, shape


# --- classification (pure; the part the fixtures exercise) -------------------------

def classify_path(base_blob: str | None, tip_blob: str | None) -> str:
    """One cited path, from its object SHA at the verification point and at the tip."""
    if base_blob is None and tip_blob is None:
        return "NOT_FOUND"
    if base_blob is None:
        return "MISSING_AT_VERIFICATION"
    if tip_blob is None:
        return "GONE"
    return "UNCHANGED" if base_blob == tip_blob else "MOVED"


_PRECEDENCE = ["GONE", "MOVED", "MISSING_AT_VERIFICATION", "NOT_FOUND", "UNCHANGED"]


def classify_row(path_statuses: list[str]) -> str:
    """The row's status from its paths' — the worst case wins.

    A `carry` copies bytes. If ANY file it cites moved, the copy would be a stale
    fork of a live document, so one moved path outranks any number of unchanged
    ones. An empty list is not a row this function may classify: the caller has
    already named why the row is UNCHECKABLE.
    """
    if not path_statuses:
        raise ValueError("classify_row needs at least one path status; an "
                         "unresolvable row is UNCHECKABLE, decided by the caller")
    for s in _PRECEDENCE:
        if s in path_statuses:
            return "SOURCE_" + s
    raise ValueError(f"unknown path status among {path_statuses!r}")


# --- API ------------------------------------------------------------------------

class GitHub:
    """Direct-egress GETs with a per-process cache; every wall is returned, not raised."""

    def __init__(self, token: str) -> None:
        self.token = token
        self.cache: dict[str, tuple[int, object]] = {}
        self.calls = 0

    def get(self, path: str) -> tuple[int, object]:
        if path in self.cache:
            return self.cache[path]
        req = urllib.request.Request(
            API + path,
            headers={"Authorization": f"Bearer {self.token}",
                     "Accept": "application/vnd.github+json",
                     "User-Agent": "estate-baseline-row-delta"})
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        self.calls += 1
        try:
            with opener.open(req, timeout=60) as resp:
                out: tuple[int, object] = (resp.status, json.load(resp))
        except urllib.error.HTTPError as exc:
            out = (exc.code, exc.read().decode("utf-8", "replace")[:300])
        except Exception as exc:  # noqa: BLE001 — the wall text is the deliverable
            out = (0, f"{type(exc).__name__}: {exc}")
        self.cache[path] = out
        return out

    def repo_tip(self, repo: str) -> tuple[dict | None, str]:
        st, meta = self.get(f"/repos/{OWNER}/{repo}")
        if st != 200 or not isinstance(meta, dict):
            return None, f"repo lookup HTTP {st}: {meta}"
        branch = meta["default_branch"]
        st2, c = self.get(f"/repos/{OWNER}/{repo}/commits/{urllib.parse.quote(branch, safe='')}")
        if st2 != 200 or not isinstance(c, dict):
            return None, f"tip lookup HTTP {st2}: {c}"
        return {"branch": branch, "sha": c["sha"], "date": c["commit"]["committer"]["date"],
                "archived": bool(meta.get("archived"))}, ""

    def resolve(self, repo: str, sha: str) -> tuple[dict | None, str]:
        st, c = self.get(f"/repos/{OWNER}/{repo}/commits/{sha}")
        if st == 200 and isinstance(c, dict):
            return {"sha": c["sha"], "date": c["commit"]["committer"]["date"]}, ""
        return None, f"HTTP {st}"

    def on_branch(self, repo: str, sha: str, tip: str) -> str:
        """`yes` when `sha` is an ancestor of the tip (or the tip), `no` when the
        repository knows the commit but the default branch does not descend from
        it (a PR-branch head, say), `unknown` on a wall."""
        if sha == tip:
            return "yes"
        st, body = self.get(f"/repos/{OWNER}/{repo}/compare/{sha}...{tip}")
        if st != 200 or not isinstance(body, dict):
            return "unknown"
        return "yes" if body.get("status") in ("ahead", "identical") else "no"

    def object_sha(self, repo: str, path: str, ref: str) -> tuple[str | None, str | None]:
        """The git object SHA of `path` at `ref`: a blob for a file, a stable digest
        of the listing for a directory. (None, None) = absent; (None, wall) = wall."""
        p = path.rstrip("/")
        st, body = self.get(f"/repos/{OWNER}/{repo}/contents/{urllib.parse.quote(p, safe='/')}"
                            f"?ref={urllib.parse.quote(ref, safe='')}")
        if st == 404:
            return None, None
        if st != 200:
            return None, f"contents HTTP {st}: {body}"
        if isinstance(body, list):
            # A directory: its identity is the sorted (name, type, sha) listing. A
            # change anywhere beneath a subdirectory changes that subdirectory's
            # tree SHA, so one level is exact.
            return "dir:" + "|".join(f"{e['name']}:{e['type']}:{e['sha']}"
                                     for e in sorted(body, key=lambda e: e["name"])), None
        if isinstance(body, dict):
            return body.get("sha"), None
        return None, f"contents: unexpected body {type(body).__name__}"


# --- main -------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--classification", required=True,
                    help="the census: rows whose source_repo is not in it are UNCHECKABLE")
    ap.add_argument("--delta", help="delta.py output to join per repository (optional)")
    ap.add_argument("--out", help="write TSV here (default: stdout)")
    args = ap.parse_args()

    token = os.environ.get("GITHUB_PAT")
    if not token:
        print("row_delta: GITHUB_PAT is not set", file=sys.stderr)
        return 2
    try:
        census = set(json.load(open(args.classification, encoding="utf-8")))
        rows_in = list(csv.DictReader(open(args.manifest, encoding="utf-8", newline="")))
    except (OSError, ValueError) as exc:
        print(f"row_delta: cannot read inputs: {exc}", file=sys.stderr)
        return 2
    need = {"subject", "source_repo", "source_path", "verification_point"}
    if rows_in and not need <= set(rows_in[0]):
        print(f"row_delta: manifest lacks {sorted(need - set(rows_in[0]))}", file=sys.stderr)
        return 2
    delta: dict[str, dict] = {}
    if args.delta:
        with open(args.delta, encoding="utf-8") as fh:
            delta = {r["repo"]: r for r in csv.DictReader(fh, delimiter="\t")}

    gh = GitHub(token)
    tips: dict[str, tuple[dict | None, str]] = {}
    out_rows: list[dict] = []
    inaccessible = 0

    for r in rows_in:
        repo = (r.get("source_repo") or "").strip()
        row = {c: "" for c in COLUMNS}
        row.update({"subject": r["subject"], "source_repo": repo,
                    "survives": r.get("survives", ""), "disposition": r.get("disposition", ""),
                    "certainty": r.get("certainty", "")})
        if repo in delta:
            row["repo_delta_status"] = delta[repo].get("delta_status", "")
            row["repo_commits_since"] = delta[repo].get("commits_since", "")
        paths, pshape = paths_of(r.get("source_path", ""))
        shas, vshape = shas_of(r.get("verification_point", ""))
        row["provenance_shape"], row["verification_shape"] = pshape, vshape
        notes: list[str] = []

        def finish(status: str) -> None:
            row["row_status"] = status
            row["note"] = "; ".join(notes)
            out_rows.append(row)

        if repo not in census:
            finish(f"UNCHECKABLE:source_repo-not-in-census ({repo or 'empty'})")
            continue
        if not paths:
            finish("UNCHECKABLE:no-path-in-source_path")
            continue
        if not shas:
            finish("UNCHECKABLE:no-sha-in-verification_point")
            continue

        if repo not in tips:
            tips[repo] = gh.repo_tip(repo)
        tip, err = tips[repo]
        if tip is None:
            inaccessible += 1
            finish(f"INACCESSIBLE:{err}")
            continue
        row["live_sha"], row["live_sha_date"] = tip["sha"], tip["date"]
        if tip["archived"]:
            notes.append("repository is archived")

        resolved = []
        for s in shas:
            c, e = gh.resolve(repo, s)
            if c:
                resolved.append(c)
            else:
                notes.append(f"{s} not a commit in {repo} ({e})")
        if not resolved:
            finish("UNCHECKABLE:sha-unresolved-in-source-repo")
            continue
        # The LATER of several verification points is the one that binds: a row
        # reading "caa6cd2; re-read at 7ccc88a" was last confirmed at 7ccc88a.
        ver = max(resolved, key=lambda c: c["date"])
        if len(resolved) > 1:
            notes.append("several SHAs; the latest-dated is the verification point")
        row["verification_sha"], row["verification_sha_date"] = ver["sha"], ver["date"]
        row["sha_on_default_branch"] = gh.on_branch(repo, ver["sha"], tip["sha"])

        statuses, detail, wall = [], [], None
        for p in paths:
            b, wb = gh.object_sha(repo, p, ver["sha"])
            t, wt = gh.object_sha(repo, p, tip["sha"])
            if wb or wt:
                wall = wb or wt
                break
            s = classify_path(b, t)
            statuses.append(s)
            detail.append(f"{p}={s}")
        if wall:
            inaccessible += 1
            finish(f"INACCESSIBLE:{wall}")
            continue
        row["paths_checked"] = " | ".join(detail)
        finish(classify_row(statuses))

    text = "\n".join("\t".join(str(r[c]).replace("\t", " ").replace("\n", " ") for c in COLUMNS)
                     for r in [dict(zip(COLUMNS, COLUMNS))] + out_rows) + "\n"
    if args.out:
        pathlib.Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"row_delta: {len(out_rows)} rows -> {args.out}  ({gh.calls} API calls)", file=sys.stderr)
    else:
        sys.stdout.write(text)

    # The summary is printed from the rows just written, never retyped.
    import collections
    by = collections.Counter(r["row_status"].split(":")[0] if r["row_status"].startswith(("UNCHECKABLE", "INACCESSIBLE"))
                             else r["row_status"] for r in out_rows)
    surv = [r for r in out_rows if r["survives"] == "yes"]
    by_s = collections.Counter(r["row_status"].split(":")[0] if r["row_status"].startswith(("UNCHECKABLE", "INACCESSIBLE"))
                               else r["row_status"] for r in surv)
    print(f"rows           : {len(out_rows)} · statuses {dict(by)}", file=sys.stderr)
    print(f"survivors      : {len(surv)} · statuses {dict(by_s)}", file=sys.stderr)
    moved_carry = [r for r in surv if r["disposition"] == "carry" and r["row_status"] in
                   ("SOURCE_MOVED", "SOURCE_GONE")]
    print(f"carry survivors whose source moved or is gone: {len(moved_carry)}", file=sys.stderr)
    for r in moved_carry:
        print(f"  {r['source_repo']:14} {r['subject'][:70]}", file=sys.stderr)
    unch = collections.Counter(r["row_status"] for r in surv if r["row_status"].startswith("UNCHECKABLE"))
    print(f"survivors UNCHECKABLE by reason: {dict(unch)}", file=sys.stderr)
    return 1 if inaccessible else 0


if __name__ == "__main__":
    raise SystemExit(main())
