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

Exit: 0 built · 2 usage/input error.
"""

from __future__ import annotations

import argparse
import collections
import csv
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from seed_rule import SCHEMA_FIELDS, dies, why  # noqa: E402

COLUMNS = [
    "subject", "source_repo", "source_path", "verification_point", "certainty",
    "canonical_owner", "estate_role", "disposition", "transform_required",
    "links_that_must_survive", "blocker", "verifier", "contradicted_by",
    "contradiction_resolution", "refuted", "stale_on_copy",
    "only_source_is_hub_summary", "fact", "origin_lane", "survives", "killed_by",
]


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
    out.setdefault("contradiction_resolution", "none")
    if not out["contradiction_resolution"]:
        out["contradiction_resolution"] = "none"
    out["fact"] = str(item.get("fact", ""))
    out["origin_lane"] = lane
    return out


def flatten(cell) -> str:
    return " | ".join(cell) if isinstance(cell, list) else str(cell)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--journal", action="append", required=True)
    ap.add_argument("--classification", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--evidence-out")
    args = ap.parse_args()

    classification = json.load(open(args.classification, encoding="utf-8"))

    items, drops, refutations, readings, areas = [], {}, [], [], []
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
                for it in r.get("successor_seed") or []:
                    n = normalise(it, f"repo:{r.get('repo', '?')}")
                    if n:
                        n.setdefault("source_repo", r.get("repo", ""))
                        items.append(n)

            # An adversary's verdict: its drops are applied to the reading above.
            if "seed_items_to_drop" in r:
                refutations.append(r)
                for d in r.get("seed_items_to_drop") or []:
                    if d.get("subject"):
                        drops[d["subject"].strip().lower()] = d.get("reason", "dropped by refuter")

            # A disposition judge's output for a fleet-manager area.
            if "items" in r and "killed" in r:
                areas.append(r)
                for it in r.get("items") or []:
                    n = normalise(it, f"area:{r.get('area', '?')}")
                    if n:
                        items.append(n)
                for k in r.get("killed") or []:
                    if k.get("subject"):
                        n = {"subject": k["subject"], "fact": k.get("why", ""),
                             "refuted": True, "source_path": "", "verification_point": "",
                             "certainty": "UNVERIFIED", "canonical_owner": "hub",
                             "estate_role": "archive/", "disposition": "archive_only"}
                        nn = normalise(n, f"area:{r.get('area', '?')}")
                        if nn:
                            nn["blocker"] = f"killed by the survival rule: {k.get('branch', '')}"
                            items.append(nn)

    # An adversary's drop is applied here, in aggregation, where it can actually
    # decide something. The 2026-08-29 fleet collected exactly this signal and
    # keyed its survival rule only on `refuted`, discarding 815 of 925 dissents.
    applied = 0
    for it in items:
        key = it["subject"].strip().lower()
        if key in drops and not it["refuted"]:
            it["refuted"] = True
            it["blocker"] = (it["blocker"] + "; " if it["blocker"] else "") + \
                            f"refuter dropped it: {drops[key]}"
            applied += 1

    # De-duplicate on (subject, source_path); a survivor never silently replaces
    # a killed twin — the kill wins, because the point is refutation.
    merged: dict[tuple, dict] = {}
    for it in items:
        k = (it["subject"].strip().lower(), it["source_path"])
        if k not in merged or (dies(it) and not dies(merged[k])):
            merged[k] = it
    rows = sorted(merged.values(), key=lambda r: (r["estate_role"], r["source_repo"], r["subject"]))

    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            d = dies(r)
            w.writerow({**{c: flatten(r.get(c, "")) for c in COLUMNS},
                        "survives": "no" if d else "yes",
                        "killed_by": "; ".join(why(r)) if d else ""})

    survivors = [r for r in rows if not dies(r)]
    killed = [r for r in rows if dies(r)]
    print(f"manifest      : {len(rows)} rows -> {out}")
    print(f"survives      : {len(survivors)}")
    print(f"killed        : {len(killed)}  (published with the branch that fired, never dropped)")
    print(f"refuter drops applied in aggregation: {applied}")
    print("by disposition:", dict(collections.Counter(r["disposition"] for r in survivors)))
    print("by estate role:", dict(collections.Counter(r["estate_role"] for r in survivors)))
    print("kill branches :", dict(collections.Counter(
        b for r in killed for b in why(r))))
    print(f"lanes         : {len(readings)} repository readings · {len(refutations)} refutations · "
          f"{len(areas)} area dispositions")

    if args.evidence_out:
        ev = pathlib.Path(args.evidence_out)
        ev.mkdir(parents=True, exist_ok=True)
        json.dump(readings, (ev / "repo-readings.json").open("w"), indent=1)
        json.dump(refutations, (ev / "refutations.json").open("w"), indent=1)
        json.dump(areas, (ev / "area-dispositions.json").open("w"), indent=1)
        print(f"evidence      : repo-readings.json, refutations.json, area-dispositions.json -> {ev}")

    unaudited = [r for r in classification
                 if r not in {x.get("repo") for x in readings}
                 and classification[r]["classification"] in
                 ("CHANGED_REAUDIT", "WEAK_OR_INCOMPLETE", "NEW")
                 and r != "fleet-manager"]
    if unaudited:
        print("NOTE — in the re-audit slice but with no reading in these journals:", unaudited)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
