# 2026-08-04 · hub — provider references at model granularity, broadened past the first three

> **Status:** `in-progress`

- **📊 Model:** fable-5 · high · research — per-model capability sweep across providers

Time: 2026-08-04 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1`

💡 Session idea: **a capability reference keyed to products answers "where do I
click"; keyed to models it answers "can this be done at all" — and sessions need
the second question far more often.** The first three provider docs described
surfaces (modes, plans, apps) because surfaces are what a browser shows. But the
questions a session actually brings — how much context fits, what modalities go
in and out, whether tool use and structured reasoning exist on this thing — are
properties of the *model*, and the same product answers them differently
depending on which model is selected. A reference that stops at the product layer
forces every session to re-derive the model layer, which is exactly the
re-derivation these docs exist to end.

## previous-session review

`2026-08-04-hub-provider-docs-accuracy-pass.md` (PR #707, merged) re-derived
gemini.md from the official release notes and closed on *when a process can fail
silently, the artifact should carry the evidence of how much work went into it*,
proposing a sourcing line per section. That card's own honest-nulls list was
better than its predecessor's — it named the Anthropic changelog gap that this
session now works — and its sourcing-line proposal is adopted here: every file
this session touches carries per-section source classes.

## Scope

Owner: make the set answer *what each model can do*, not limited to the three
covered so far. This session: (1) sweep Anthropic's own changelog and re-derive
claude.md's model table from it — the table has only ever been a skill cache;
(2) deepen chatgpt.md's model coverage from the reachable vendor docs site;
(3) broaden with new provider files, changelog-first, ordered by plausible use in
this estate. Not a program step; the NOW pointer (E1) is untouched.

## What landed

*(written at close)*

## Honest nulls

*(written at close)*

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
