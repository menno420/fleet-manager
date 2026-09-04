#!/usr/bin/env python3
"""The survival rule for a proposed `estate` seed claim — and its audit.

fleet-preflight § 1 exists because the 2026-08-28/29 estate-error fleet
collected the deciding signal and then ignored it in aggregation: 815 of 925
verdicts named something in `already_covered_by` and the survival rule keyed
only on `refuted`.  This module is the answer for THIS run: the rule is one
expression over named fields, every schema field is either read by it or
declared REPORT_ONLY, and the fixtures below contain kills AND survivals.

A claim that dies is not deleted — it is published as a downgraded row with
the branch that killed it, so a reader can argue with the rule rather than
with a silence.
"""

from __future__ import annotations

import ast
import json
import sys

# The rule, as source.  The audit below parses THIS string, so a field that
# stops being read is caught here rather than at the end of the run.
DIES_IF_SRC = (
    "refuted "
    "or not source_path "
    "or not verification_point "
    "or certainty == 'UNVERIFIED' "
    "or (contradicted_by and contradiction_resolution == 'unresolved') "
    "or (stale_on_copy and disposition == 'carry') "
    "or (canonical_owner not in ('hub', 'owner') and disposition == 'carry') "
    "or (only_source_is_hub_summary and certainty != 'OWNER') "
    "or (certainty_overclaimed and certainty in ('MEASURED', 'OWNER'))"
)

# Collected to be PUBLISHED, never to decide.  Anything not here and not read
# by the rule is a field nobody uses — the 815/925 defect in its egg.
REPORT_ONLY = {
    "subject", "source_repo", "estate_role", "transform_required",
    "links_that_must_survive", "blocker", "verifier",
}

SCHEMA_FIELDS = sorted(REPORT_ONLY | {
    "source_path", "verification_point", "certainty", "canonical_owner",
    "disposition", "contradicted_by", "contradiction_resolution", "refuted",
    "stale_on_copy", "only_source_is_hub_summary", "certainty_overclaimed",
})


def dies(item: dict) -> bool:
    """Evaluate the rule over one seed item."""
    return bool(eval(DIES_IF_SRC, {"__builtins__": {}}, dict(item)))  # noqa: S307


def why(item: dict) -> list[str]:
    """Which branches fired — the published reason a claim was downgraded."""
    f = []
    if item["refuted"]:
        f.append("refuted by an adversarial lens")
    if not item["source_path"]:
        f.append("no source path")
    if not item["verification_point"]:
        f.append("no verification point")
    if item["certainty"] == "UNVERIFIED":
        f.append("certainty UNVERIFIED")
    if item["contradicted_by"] and item["contradiction_resolution"] == "unresolved":
        f.append("unresolved contradiction: " + "; ".join(item["contradicted_by"]))
    if item["stale_on_copy"] and item["disposition"] == "carry":
        f.append("would be stale the moment it is copied — carry is the wrong verb")
    if item["canonical_owner"] not in ("hub", "owner") and item["disposition"] == "carry":
        f.append(f"product truth ({item['canonical_owner']}) carried whole into the hub")
    if item["only_source_is_hub_summary"] and item["certainty"] != "OWNER":
        f.append("only source is a hub document restating something with no primary")
    if item.get("certainty_overclaimed") and item["certainty"] in ("MEASURED", "OWNER"):
        f.append(f"an adversary showed the {item['certainty']} tag is not earned")
    return f


def audit() -> int:
    """Field audit — UNREAD is the discard defect, UNDEFINED its twin."""
    read = {n.id for n in ast.walk(ast.parse(DIES_IF_SRC, mode="eval"))
            if isinstance(n, ast.Name)}
    schema = set(SCHEMA_FIELDS)
    unread, undefined = schema - read - REPORT_ONLY, read - schema
    print("RULE     :", DIES_IF_SRC)
    print("UNREAD   :", sorted(unread) or "none")
    print("UNDEFINED:", sorted(undefined) or "none")
    return 1 if (unread or undefined) else 0


BASE = {
    "subject": "x", "source_repo": "fleet-manager", "source_path": "docs/x.md",
    "verification_point": "caa6cd2@2026-09-03T21:42:38Z", "certainty": "MEASURED",
    "canonical_owner": "hub", "estate_role": "state/", "disposition": "carry",
    "transform_required": False, "links_that_must_survive": [], "blocker": "",
    "verifier": "delta.py", "contradicted_by": [],
    "contradiction_resolution": "none", "refuted": False,
    "stale_on_copy": False, "only_source_is_hub_summary": False,
    "certainty_overclaimed": False,
}

# Expected outcome written down BEFORE the run, per fleet-preflight § 1b.
FIXTURES = [
    ("survives: fully provenanced hub fact", {}, False),
    ("survives: owner's words with no primary beyond the hub record",
     {"certainty": "OWNER", "only_source_is_hub_summary": True}, False),
    ("survives: product truth POINTED AT rather than carried",
     {"canonical_owner": "spider-swing", "disposition": "distill"}, False),
    ("survives: a contradiction that was resolved",
     {"contradicted_by": ["ESTATE.md row"], "contradiction_resolution": "resolved:source wins"}, False),
    ("kills: an adversarial lens refuted it", {"refuted": True}, True),
    ("kills: no source path", {"source_path": ""}, True),
    ("kills: no verification point", {"verification_point": ""}, True),
    ("kills: certainty UNVERIFIED", {"certainty": "UNVERIFIED"}, True),
    ("kills: unresolved contradiction",
     {"contradicted_by": ["repo README"], "contradiction_resolution": "unresolved"}, True),
    ("kills: stale the moment it is copied", {"stale_on_copy": True}, True),
    ("kills: product truth duplicated into the hub",
     {"canonical_owner": "superbot"}, True),
    ("kills: a hub summary with no primary and no owner authority",
     {"only_source_is_hub_summary": True}, True),
    ("kills: an adversary showed the MEASURED tag is not earned",
     {"certainty_overclaimed": True}, True),
    ("survives: an overclaim flag on a row that is only REASONED anyway",
     {"certainty_overclaimed": True, "certainty": "REASONED"}, False),
]


def fixtures() -> int:
    bad, kills, survivals = [], 0, 0
    for name, patch, expected in FIXTURES:
        item = dict(BASE, **patch)
        got = dies(item)
        kills += bool(expected)
        survivals += not expected
        if got != expected:
            bad.append(f"{name}: dies()={got}, expected {expected} · fired={why(item)}")
    print(f"fixtures : {len(FIXTURES)} cases, {kills} kill / {survivals} survival")
    for b in bad:
        print("FAIL:", b)
    if not kills or not survivals:
        print("FAIL: the fixture set must contain at least one kill AND one survival")
        return 1
    return 1 if bad else 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    rc = 0
    if mode in ("all", "audit"):
        rc |= audit()
    if mode in ("all", "fixtures"):
        rc |= fixtures()
    if mode == "schema":
        print(json.dumps(SCHEMA_FIELDS, indent=1))
    raise SystemExit(rc)
