#!/usr/bin/env python3
"""Build the `estate` seed manifest from the audit fleet's retained output.

Deterministic by construction: the manifest is a pure function of the fleet's
journal plus the committed classification, so re-running it reproduces the same
file, and a later session can re-run it against a fresh fleet to see what moved.

The survival rule lives in `seed_rule.py` and is applied here rather than
restated — a second copy of a rule is a second rule. **Items the rule kills are
written to the manifest with `survives=no` and the branch that fired**, never
dropped: a reader must be able to argue with the rule, which is impossible if
its casualties are invisible.

Usage
-----
    python3 tools/estate_baseline/build_manifest.py \
        --journal <workflow journal.jsonl> [--journal <another>] \
        --classification docs/findings/data/2026-09-04-estate-truth-baseline/classification.json \
        --out docs/planning/2026-09-04-estate-seed-manifest.csv \
        --evidence-out docs/findings/data/2026-09-04-estate-truth-baseline/

Refute-lane schema for `overclaimed_certainty` (added 2026-09-04, finding § 12
item 11)
------------------------------------------------------------------------------
The 2026-09-04 fleet collected 73 certainty overclaims as FREE TEXT — *"claims
tagged MEASURED that are actually REASONED, and why"* — and only 10 resolved to
a row by content-word containment; the other 63 named no seed subject any join
could reach. That is a schema defect, not a matching one, so the next run's
refute lane MUST emit each overclaim as an object naming the subject it judges:

    {"subject": "<the seed item's subject, verbatim>", "reason": "<why the tag is not earned>"}

Objects join EXACTLY on the case-folded subject within the audited reading —
no heuristic, no threshold. Bare strings are still read, by the containment
join, so the retained 2026-09-04 journals reproduce the committed manifest
unchanged; the builder prints how many strings matched a kill-eligible row, a
row of some other certainty, or no row at all, so the residual is a number
rather than a sentence.

Exit: 0 built · 1 incomplete manifest without --allow-partial · 2 usage/input error.
"""

from __future__ import annotations

import argparse
import collections
import csv
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from seed_rule import SCHEMA_FIELDS, dies, why  # noqa: E402

COLUMNS = [
    "subject", "source_repo", "source_path", "verification_point", "certainty",
    "canonical_owner", "estate_role", "disposition", "transform_required",
    "links_that_must_survive", "blocker", "verifier", "contradicted_by",
    "contradiction_resolution", "refuted", "stale_on_copy",
    "only_source_is_hub_summary", "certainty_overclaimed", "fact", "origin_lane",
    "survives", "killed_by", "canonical_state_source",
]

# The hub's own canonical ledger. Each repository reading records its
# `canonical_state_source`; fleet-manager was read by five AREA lanes that record
# none, so the hub's value is taken from the file that declares itself the
# ledger: `docs/current-state.md` opens with `Status: living-ledger` and *"It
# carries live hub state"*, and `.claude/CLAUDE.md`'s deep read path names it
# *"the living ledger"*. Finding § 7 explains why the column exists: a consumer
# of the CSV alone must be able to tell a repository's canonical ledger from
# whichever file supplied a claim, or the seed imports stale front doors.
HUB_STATE_SOURCE = "docs/current-state.md"


CENSUS: set[str] = set()


def canon_repo(value: str, lane: str) -> str:
    """A repository name, or an honest marker — never a path fragment.

    `owner/repo` is trimmed to `repo`, but only when the result is a repository
    the census actually holds. An agent that wrote a file path into this column
    previously yielded `source_repo == "README.md"`; fall back to the lane, which
    always names the repository or area the row came from.
    """
    v = (value or "").strip()
    if v in CENSUS:
        return v
    tail = v.split("/")[-1].strip()
    if tail in CENSUS:
        return tail
    if lane.startswith("repo:"):
        return lane.split(":", 1)[1].split("/")[-1]
    if lane.startswith("area:"):
        return "fleet-manager"
    return v or "(unstated)"


def normalise(item: dict, lane: str) -> dict | None:
    """Fill missing optional fields so the rule can be evaluated at all.

    A missing field is NOT silently treated as benign: `source_path` and
    `verification_point` default to "" and the rule kills on empty, which is the
    intended reading of "an agent did not supply provenance".
    """
    if not isinstance(item, dict) or not item.get("subject"):
        return None
    out = {}
    for f in SCHEMA_FIELDS:
        v = item.get(f)
        if f in ("contradicted_by", "links_that_must_survive"):
            v = v if isinstance(v, list) else ([] if v in (None, "") else [str(v)])
        elif f in ("refuted", "stale_on_copy", "only_source_is_hub_summary", "transform_required"):
            v = bool(v)
        else:
            v = "" if v is None else str(v)
        out[f] = v
    # A missing decision field must not become a usable default. `certainty=""`
    # survives a rule that kills only the literal 'UNVERIFIED', and a
    # contradiction with no resolution silently becomes 'none'.
    CERTS = {"MEASURED", "MEASURED-PRIOR", "OWNER", "REASONED", "REVIEWED",
             "UNVERIFIED", "NOT-VERIFIABLE"}
    if not str(item.get("certainty", "")).strip():
        out["certainty"] = "UNVERIFIED"
        out["blocker"] = (out.get("blocker", "") + "; " if out.get("blocker") else "") + \
            "malformed record: no certainty supplied, read as UNVERIFIED"
    elif out["certainty"] not in CERTS:
        out["blocker"] = (out.get("blocker", "") + "; " if out.get("blocker") else "") + \
            f"malformed record: certainty {out['certainty']!r} is not in the legend"
        out["certainty"] = "UNVERIFIED"
    if out["contradicted_by"] and not str(item.get("contradiction_resolution", "")).strip():
        out["contradiction_resolution"] = "unresolved"
        out["blocker"] = (out.get("blocker", "") + "; " if out.get("blocker") else "") + \
            "malformed record: contradiction named with no resolution, read as unresolved"
    out["estate_role"] = canon_role(out["estate_role"])
    out["source_repo"] = canon_repo(out["source_repo"], lane)
    out["judge_branch"] = str(item.get("judge_branch", ""))
    out.setdefault("contradiction_resolution", "none")
    if not out["contradiction_resolution"]:
        out["contradiction_resolution"] = "none"
    out["fact"] = str(item.get("fact", ""))
    out["origin_lane"] = lane
    return out


ROLES = {"owner", "repositories", "state", "plans", "decisions", "ideas",
         "evidence", "practices", "tools", "sessions", "archive", "root"}


def canon_role(value: str) -> str:
    """One spelling per destination.

    The eleven `estate` roles are a closed, agreed set. Agents wrote them both
    ways ("state" and "state/"), which silently split one destination into two
    rows of the role census. `root` is the one member with no trailing slash,
    because it is not a folder.
    """
    v = (value or "").strip().strip("/").split("/")[0].lower()
    if v in ROLES:
        return v if v == "root" else v + "/"
    return value.strip() or "(unassigned)"


def _key(text: str) -> frozenset:
    """Content words of a subject, for joining a verdict to the item it judges."""
    words = re.findall(r"[a-z0-9]+", (text or "").lower())
    return frozenset(w for w in words if len(w) > 2 and w not in _STOP)


_STOP = {"the", "and", "for", "its", "his", "her", "not", "but", "with", "from",
         "that", "this", "are", "was", "has", "have", "into", "onto", "own"}


def assign_drops(items: list, drops_by_lane: dict) -> dict:
    """Resolve drops to items ONE-TO-ONE, per audited lane.

    A per-item lookup cannot prevent reuse: with a single drop `Release`, both
    `Release signing` and `Release notes` score 1.0 under containment and each
    lookup sees exactly one candidate, so an ambiguity guard never fires and both
    rows die on one verdict. Assignment is the fix — every drop is spent at most
    once, on its best-scoring subject, and ties are refused rather than guessed.

    Returns {id(item): reason}.
    """
    out: dict[int, str] = {}
    by_lane: dict[str, list] = {}
    for it in items:
        by_lane.setdefault(audited_of(it), []).append(it)
    for lane, drops in drops_by_lane.items():
        pool = by_lane.get(lane, [])
        if not pool:
            continue
        pairs = []
        for cand, reason in drops.items():
            ck = _key(cand)
            if not ck:
                continue
            for it in pool:
                sk = _key(it["subject"])
                if not sk:
                    continue
                inter = len(sk & ck)
                score = max(inter / len(sk), inter / len(ck))
                if score >= 0.6:
                    pairs.append((score, cand, reason, id(it)))
        # Maximum one-to-one matching, not greedy edge order. Committing the
        # highest-scoring edge first can consume the only viable subject for a
        # more specific drop and strand a legitimate refutation; augmenting paths
        # find an assignment of maximum size instead. Sets here are tiny (a
        # repository's drops against its own rows), so the simple algorithm is
        # the right one.
        edges: dict[str, list] = {}
        for score, cand, reason, iid in sorted(pairs, reverse=True, key=lambda t: t[0]):
            edges.setdefault(cand, []).append((score, iid, reason))

        match_item: dict[int, str] = {}     # item -> drop

        def augment(cand: str, seen: set) -> bool:
            for _score, iid, _reason in edges.get(cand, []):
                if iid in seen:
                    continue
                seen.add(iid)
                if iid not in match_item or augment(match_item[iid], seen):
                    match_item[iid] = cand
                    return True
            return False

        for cand in edges:
            augment(cand, set())

        # Ambiguity is judged on the COMPLETED assignment: a drop whose chosen
        # subject is within 0.15 of another still-unmatched subject is refused.
        for iid, cand in list(match_item.items()):
            chosen = next(s_ for s_, i_, _ in edges[cand] if i_ == iid)
            rivals = [s_ for s_, i_, _ in edges[cand]
                      if i_ != iid and match_item.get(i_) != cand
                      and abs(s_ - chosen) < 0.15]
            if rivals:
                continue                    # ambiguous: spend it on nobody
            out[iid] = next(r_ for s_, i_, r_ in edges[cand] if i_ == iid)
    return out


def audited_of(item: dict) -> str:
    """The repository whose reading produced this item, from its origin lane."""
    lane = item.get("origin_lane", "")
    return lane.split(":", 1)[1].split("/")[-1] if ":" in lane else ""


def match_drop(subject: str, drops: dict) -> str | None:
    """Find an adversary's drop for this item, tolerating a qualified subject.

    Exact equality is not enough and the miss is not hypothetical: on this run's
    own data an exact case-folded join matched 25 of 44 drop verdicts and lost
    19, because adversaries write `"<subject> — the <clause> clause"` while the
    reader wrote `"<subject>"`. Losing a dissent in the join is the same failure
    as ignoring it in the rule.
    """
    s_norm = (subject or "").strip().lower()
    if s_norm in drops:
        return drops[s_norm]
    sk = _key(subject)
    if not sk:
        return None
    scored = []
    for cand, reason in drops.items():
        ck = _key(cand)
        if not ck:
            continue
        inter = len(sk & ck)
        # Containment alone is not enough: a two-word generic subject is a subset
        # of half the corpus, so `Release` would match `Release signing` at 1.0
        # and one drop could kill rows it never judged. Require substantial
        # overlap in BOTH directions.
        score = max(inter / len(sk), inter / len(ck))
        if score >= 0.6:
            scored.append((score, reason))
    if not scored:
        return None
    scored.sort(reverse=True, key=lambda t: t[0])
    if len(scored) > 1 and abs(scored[0][0] - scored[1][0]) < 0.15:
        return None          # ambiguous: refuse rather than guess which drop applies
    return scored[0][1]


def flatten(cell) -> str:
    return " | ".join(cell) if isinstance(cell, list) else str(cell)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--journal", action="append", required=True)
    ap.add_argument("--classification", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--evidence-out")
    ap.add_argument("--allow-partial", action="store_true",
                    help="exit 0 even when a repository in the re-audit slice has no reading")
    args = ap.parse_args()

    classification = json.load(open(args.classification, encoding="utf-8"))
    CENSUS.update(classification)

    items, drops, refutations, readings, areas = [], {}, [], [], []
    overclaims: dict[str, list[str]] = {}           # free text, per audited repo
    overclaims_by_subject: dict[str, dict[str, str]] = {}   # {repo: {subject: reason}}
    state_source: dict[str, str] = {"fleet-manager": HUB_STATE_SOURCE}
    for jpath in args.journal:
        for line in open(jpath, encoding="utf-8", errors="replace"):
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            if rec.get("type") != "result":
                continue
            r = rec.get("result")
            if not isinstance(r, dict):
                continue

            # A repository reading: its seed items, its contradictions, its walls.
            if "successor_seed" in r:
                readings.append(r)
                who_read = str(r.get("repo", "")).split("/")[-1]
                if str(r.get("canonical_state_source", "")).strip():
                    state_source[who_read] = str(r["canonical_state_source"]).strip()
                for it in r.get("successor_seed") or []:
                    n = normalise(it, f"repo:{r.get('repo', '?')}")
                    if n:
                        n.setdefault("source_repo", r.get("repo", ""))
                        items.append(n)

            # An adversary's verdict: its drops AND its certainty overclaims are
            # applied to the reading above. Collecting the overclaims and reading
            # none of them was the 2026-08-29 defect in miniature — 73 flagged,
            # 0 consumed, until the external round said so.
            if "seed_items_to_drop" in r:
                refutations.append(r)
                who = str(r.get("repo", "")).split("/")[-1]
                for d in r.get("seed_items_to_drop") or []:
                    if d.get("subject"):
                        drops.setdefault(who, {})[d["subject"].strip().lower()] = \
                            d.get("reason", "dropped by refuter")
                for oc in r.get("overclaimed_certainty") or []:
                    # The subject-bearing form joins exactly; the free-text form
                    # falls through to the containment heuristic below.
                    if isinstance(oc, dict) and str(oc.get("subject", "")).strip():
                        overclaims_by_subject.setdefault(who, {})[
                            str(oc["subject"]).strip().lower()] = str(
                            oc.get("reason") or oc.get("why") or "certainty overclaimed by refuter")
                    elif isinstance(oc, str) and oc.strip():
                        overclaims.setdefault(who, []).append(oc.strip())

            # A disposition judge's output for a fleet-manager area.
            if "items" in r and "killed" in r:
                areas.append(r)
                for it in r.get("items") or []:
                    n = normalise(it, f"area:{r.get('area', '?')}")
                    if n:
                        items.append(n)
                for k in r.get("killed") or []:
                    if not k.get("subject"):
                        continue
                    # A judge already applied the rule and named the branch that
                    # fired. Do NOT re-derive it from synthesised empty fields:
                    # blanking source_path and certainty to force a kill makes
                    # every judge-killed row report "no source path · no
                    # verification point · certainty UNVERIFIED", burying the
                    # real reason under three artefacts of this function.
                    n = {"subject": k["subject"], "fact": k.get("why", ""),
                         "refuted": True, "source_path": "(killed before a source was recorded)",
                         "verification_point": "(killed at disposition)",
                         "certainty": "REVIEWED", "canonical_owner": "hub",
                         "estate_role": "archive/", "disposition": "archive_only",
                         "verifier": f"disposition judge for area {r.get('area', '?')}"}
                    nn = normalise(n, f"area:{r.get('area', '?')}")
                    if nn:
                        nn["judge_branch"] = k.get("branch", "").strip()
                        nn["blocker"] = f"killed at disposition: {nn['judge_branch']}"
                        items.append(nn)

    # An adversary's drop is applied here, in aggregation, where it can actually
    # decide something. The 2026-08-29 fleet collected exactly this signal and
    # keyed its survival rule only on `refuted`, discarding 815 of 925 dissents.
    # An overclaim names a claim inside one repository's reading; attach it to
    # that repository's rows whose subject the flag text mentions.
    oc_applied = oc_by_subject_applied = 0
    for it in items:
        audited = audited_of(it)
        reason = overclaims_by_subject.get(audited, {}).get(it["subject"].strip().lower())
        if reason is not None and it["certainty"] in ("MEASURED", "OWNER"):
            it["certainty_overclaimed"] = True
            it["blocker"] = (it["blocker"] + "; " if it["blocker"] else "") + \
                            f"adversary (by subject): {reason[:160]}"
            oc_by_subject_applied += 1
            continue
        for flag in overclaims.get(audited, []):
            if match_drop(it["subject"], {flag: flag}) and it["certainty"] in ("MEASURED", "OWNER"):
                it["certainty_overclaimed"] = True
                it["blocker"] = (it["blocker"] + "; " if it["blocker"] else "") + \
                                f"adversary: {flag[:160]}"
                oc_applied += 1
                break
    # Where the free-text residual actually is. "10 of 73 applied" conflated two
    # different failures: a flag that names no row any join can reach (the
    # schema defect) and a flag that reaches a row whose certainty the rule does
    # not kill on (working as designed). Count them apart.
    oc_no_row = oc_ineligible_only = 0
    for audited, flags in overclaims.items():
        pool = [it for it in items if audited_of(it) == audited]
        for flag in flags:
            hit = [it for it in pool if match_drop(it["subject"], {flag: flag})]
            if not hit:
                oc_no_row += 1
            elif not any(it["certainty"] in ("MEASURED", "OWNER") for it in hit):
                oc_ineligible_only += 1

    # Scope by the AUDITED reading (origin_lane), not by the claim's own
    # source_repo: a repository reading that cites a hub file leaves
    # source_repo == "fleet-manager", and keying on that silently skipped its own
    # refuter (34 of 44 drops matched by source_repo against 43 by lane).
    assigned = assign_drops(items, drops)
    applied = 0
    for it in items:
        reason = assigned.get(id(it))
        if reason and not it["refuted"]:
            it["refuted"] = True
            it["blocker"] = (it["blocker"] + "; " if it["blocker"] else "") + \
                            f"refuter dropped it: {reason}"
            applied += 1

    # De-duplicate on (subject, source_path); a survivor never silently replaces
    # a killed twin — the kill wins, because the point is refutation.
    merged: dict[tuple, dict] = {}
    for it in items:
        # Two repositories can legitimately emit "Identity and purpose" from
        # "README.md"; a global key collapses them and the survivor then depends
        # on journal order. The audited origin is part of the identity.
        k = (it["subject"].strip().lower(), it["source_path"], it["origin_lane"])
        if k not in merged or (dies(it) and not dies(merged[k])):
            merged[k] = it
    rows = sorted(merged.values(), key=lambda r: (r["estate_role"], r["source_repo"], r["subject"]))
    for r in rows:
        r["canonical_state_source"] = state_source.get(r["source_repo"], "")
    no_state_source = sorted({r["source_repo"] for r in rows if not r["canonical_state_source"]})

    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            d = dies(r)
            # A judge's stated branch is the authoritative reason and outranks
            # anything this script can recompute about a row it did not read.
            reason = r.get("judge_branch") or "; ".join(why(r))
            w.writerow({**{c: flatten(r.get(c, "")) for c in COLUMNS},
                        "survives": "no" if d else "yes",
                        "killed_by": reason if d else ""})

    survivors = [r for r in rows if not dies(r)]
    killed = [r for r in rows if dies(r)]
    print(f"manifest      : {len(rows)} rows -> {out}")
    print(f"survives      : {len(survivors)}")
    print(f"killed        : {len(killed)}  (published with the branch that fired, never dropped)")
    total_drops = sum(len(r.get("seed_items_to_drop") or []) for r in refutations)
    print(f"refuter drops applied in aggregation: {applied} of {total_drops}"
          + ("  <-- OVER-APPLIED, a drop matched more than its own reading"
             if applied > total_drops else ""))
    n_free = sum(len(v) for v in overclaims.values())
    n_subj = sum(len(v) for v in overclaims_by_subject.values())
    print(f"certainty overclaims (free text): {n_free} flags · applied to {oc_applied} row(s) · "
          f"{oc_ineligible_only} reach only rows outside MEASURED/OWNER · "
          f"{oc_no_row} reach no row (the schema residual)")
    print(f"certainty overclaims (by subject): {n_subj} flags · applied to {oc_by_subject_applied} row(s)")
    print(f"canonical_state_source: {sum(1 for r in rows if r['canonical_state_source'])} of {len(rows)} rows carry one"
          + (f"; none recorded for source_repo {no_state_source}" if no_state_source else ""))
    print("by disposition:", dict(collections.Counter(r["disposition"] for r in survivors)))
    print("by estate role:", dict(collections.Counter(r["estate_role"] for r in survivors)))
    print("kill branches :", dict(collections.Counter(
        (r["judge_branch"] or "; ".join(why(r))) for r in killed)))
    echoed = sum(1 for r in killed if r.get("judge_branch"))
    print(f"kill origin   : {len(killed) - echoed} made by the rule itself · "
          f"{echoed} echoed from a disposition judge")
    print(f"lanes         : {len(readings)} repository readings · {len(refutations)} refutations · "
          f"{len(areas)} area dispositions")

    if args.evidence_out:
        ev = pathlib.Path(args.evidence_out)
        ev.mkdir(parents=True, exist_ok=True)
        json.dump(readings, (ev / "repo-readings.json").open("w"), indent=1)
        json.dump(refutations, (ev / "refutations.json").open("w"), indent=1)
        json.dump(areas, (ev / "area-dispositions.json").open("w"), indent=1)
        print(f"evidence      : repo-readings.json, refutations.json, area-dispositions.json -> {ev}")

    seen_repos = {str(x.get("repo", "")).split("/")[-1] for x in readings}
    unaudited = [r for r in classification
                 if r not in seen_repos
                 and classification[r]["classification"] in
                 ("CHANGED_REAUDIT", "WEAK_OR_INCOMPLETE", "NEW")
                 and r != "fleet-manager"]
    refuted_repos = {str(x.get("repo", "")).split("/")[-1] for x in refutations}
    unrefuted = sorted(seen_repos - refuted_repos)
    disposed = {str(a.get("area", "")) for a in areas}
    # Every area whose candidates reached the item list must also have been
    # disposed; an omitted disposition silently drops that area's rows from the
    # canonical manifest (measured: removing `planning` published 165 of 183 at
    # exit 0). The lanes are named by the origin_lane of the items themselves.
    seen_areas = {it["origin_lane"].split(":", 1)[1] for it in items
                  if it["origin_lane"].startswith("area:")}
    undisposed = sorted(seen_areas - disposed - {"run1-four-areas"})
    if undisposed:
        print("NOTE — area candidates present with no disposition lane:", undisposed)
    if unrefuted:
        print("NOTE — read but never refuted (the adversarial lane is incomplete):", unrefuted)
    if unaudited:
        print("NOTE — in the re-audit slice but with no reading in these journals:", unaudited)
    if unaudited or unrefuted or undisposed:
        if not args.allow_partial:
            print("build_manifest: FAILED — refusing to report success over an incomplete "
                  "manifest (a missing reading, refutation OR area disposition); pass "
                  "--allow-partial to publish one deliberately", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
