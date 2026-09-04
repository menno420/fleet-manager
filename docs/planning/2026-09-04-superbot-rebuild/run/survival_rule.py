#!/usr/bin/env python3
"""AGGREGATE contract — the rule that decides what survives synthesis.

Two populations, two rules. A finding is either a STRENGTH claim ("this is
genuinely good, keep/adapt it") or a DEFECT claim ("this is wrong, and here is
why"). They must not share a rule: the asymmetry is the point — a strength must
clear a high bar because the failure mode this whole review exists to prevent is
"it looked good because of docs, tests, abstraction quality or history".
"""

# ---- the rules, as expressions over field names ---------------------------
STRENGTH_SURVIVES = (
    "(not refuted)"
    " and (evidence_class in {'PRODUCTION-PROVEN','LIVE-TESTED','SOURCE-ENFORCED','OWNER-VALUED'}"
    "      or (evidence_class == 'TEST-PROVEN' and effect_asserted))"
    " and (enforcement_locus not in {'documentation_only','none'})"
    " and (consumers >= 2 or prevents_failure != '')"
)
DEFECT_SURVIVES = (
    "(not refuted)"
    " and (evidence_class in {'PRODUCTION-PROVEN','LIVE-TESTED','SOURCE-ENFORCED','TEST-PROVEN','OWNER-VALUED','MEASURED'})"
    " and (failure_scenario != '')"
)
# already_covered_by is READ by the merge step below, not discarded (the
# 815/925 defect in the measured estate run). A finding naming a prior id does
# not vanish: it MERGES into that id and raises its corroboration count.
MERGE_KEY = "already_covered_by"

# REPORT_ONLY is PER RULE. enforcement_locus decides for a strength (a rule
# nothing enforces is not a strength) and merely describes for a defect (an
# unguarded defect and a guarded one are both defects), so it cannot sit in one
# shared set — that shared set is how a deciding field becomes a decorative one.
_COMMON_REPORT_ONLY = {
    "id", "repo", "area", "claim", "file", "line_span", "quote",
    "simpler_than_counterpart", "disposition_recommended", "note",
    "refute_reason", "new_failure_class", "successor_recommendation",
}
REPORT_ONLY_STRENGTH = set(_COMMON_REPORT_ONLY)
REPORT_ONLY_DEFECT = _COMMON_REPORT_ONLY | {"enforcement_locus"}

STRENGTH_SCHEMA = {
    "id","repo","area","claim","file","line_span","quote","evidence_class",
    "enforcement_locus","consumers","prevents_failure","effect_asserted",
    "simpler_than_counterpart","new_failure_class","disposition_recommended",
    "successor_recommendation","refuted","refute_reason","already_covered_by",
}
DEFECT_SCHEMA = {
    "id","repo","area","claim","file","line_span","quote","evidence_class",
    "failure_scenario","enforcement_locus","new_failure_class",
    "disposition_recommended","successor_recommendation","refuted",
    "refute_reason","already_covered_by","note",
}

def field_audit(rule, schema, report_only, extra_read=()):
    import ast
    read = {n.id for n in ast.walk(ast.parse(rule)) if isinstance(n, ast.Name)}
    read |= set(extra_read)
    unread = schema - read - report_only
    undefined = read - schema
    return sorted(unread), sorted(undefined)

def evaluate(rule, row):
    return bool(eval(rule, {"__builtins__": {}}, row))

# ---- fixtures: at least one MUST die and one MUST survive, per rule --------
S_MUST_SURVIVE = dict(  # superbot-next config-accessor seam: a real machine-enforced boundary
    id="S1", repo="superbot-next", area="config", claim="only sb/kernel/config may read env",
    file="tests/architecture/test_config_seam.py", line_span="1-40", quote="no os.getenv outside sb/kernel/config",
    evidence_class="SOURCE-ENFORCED", enforcement_locus="ci_check", consumers=40,
    prevents_failure="config split-brain", effect_asserted=True,
    simpler_than_counterpart="yes", new_failure_class="", disposition_recommended="PRESERVE_CONTRACT",
    successor_recommendation="keep", refuted=False, refute_reason="", already_covered_by="",
)
S_MUST_DIE_DOC = dict(S_MUST_SURVIVE, id="S2", evidence_class="REASONED",
                      enforcement_locus="documentation_only", consumers=1, prevents_failure="",
                      claim="the architecture doc says layers are clean")
S_MUST_DIE_GOLDEN = dict(S_MUST_SURVIVE, id="S3", evidence_class="TEST-PROVEN",
                         effect_asserted=False, enforcement_locus="test_only", consumers=1,
                         prevents_failure="", claim="533/533 golden parity green")
S_MUST_DIE_REFUTED = dict(S_MUST_SURVIVE, id="S4", refuted=True, refute_reason="guard has an unbounded allowlist")

D_MUST_SURVIVE = dict(
    id="D1", repo="superbot-next", area="help", claim="60 of 66 help panels have zero buttons",
    file="manifest.snapshot.json", line_span="-", quote='"actions": []',
    evidence_class="MEASURED", failure_scenario="a user opening /help reaches a text list with nothing to press",
    enforcement_locus="none", new_failure_class="", disposition_recommended="REBUILD",
    successor_recommendation="route graph is the source of help", refuted=False,
    refute_reason="", already_covered_by="", note="",
)
D_MUST_DIE = dict(D_MUST_SURVIVE, id="D2", evidence_class="UNVERIFIED", failure_scenario="")

if __name__ == "__main__":
    import sys
    bad = 0
    for label, rule, schema, ro, extra in (
        ("STRENGTH", STRENGTH_SURVIVES, STRENGTH_SCHEMA, REPORT_ONLY_STRENGTH, [MERGE_KEY]),
        ("DEFECT",   DEFECT_SURVIVES,   DEFECT_SCHEMA,   REPORT_ONLY_DEFECT,   [MERGE_KEY]),
    ):
        unread, undefined = field_audit(rule, schema, ro, extra)
        print(f"{label:9s} UNREAD={unread or 'none'}  UNDEFINED={undefined or 'none'}")
        if unread or undefined: bad += 1
    print()
    cases = [
        ("STRENGTH survives (source-enforced seam)", STRENGTH_SURVIVES, S_MUST_SURVIVE, True),
        ("STRENGTH dies (documentation only)",       STRENGTH_SURVIVES, S_MUST_DIE_DOC, False),
        ("STRENGTH dies (golden parity, no effect)", STRENGTH_SURVIVES, S_MUST_DIE_GOLDEN, False),
        ("STRENGTH dies (refuted)",                  STRENGTH_SURVIVES, S_MUST_DIE_REFUTED, False),
        ("DEFECT survives (measured + scenario)",    DEFECT_SURVIVES,   D_MUST_SURVIVE, True),
        ("DEFECT dies (unverified, no scenario)",    DEFECT_SURVIVES,   D_MUST_DIE, False),
    ]
    for name, rule, row, want in cases:
        got = evaluate(rule, row)
        flag = "ok " if got == want else "FAIL"
        if got != want: bad += 1
        print(f"  [{flag}] {name:44s} want={want} got={got}")
    kills = sum(1 for n,r,row,w in cases if not w)
    lives = sum(1 for n,r,row,w in cases if w)
    print(f"\nfixture kill {kills}/{len(cases)} · fixture survive {lives}/{len(cases)}")
    sys.exit(1 if bad else 0)
