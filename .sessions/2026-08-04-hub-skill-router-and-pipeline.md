# 2026-08-04 · hub — the skill router, the pipeline skill, and de-controlling the close

> **Status:** `in-progress`

- **📊 Model:** fable-5 · high · docs-only — router in the boot file, asset-pipeline skill, control/ reconciliation

Time: 2026-08-04 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1` (restarted from main post-#720)

💡 Session idea: **a skill that isn't routed to is a document with extra steps —
and the routing surface already exists, unused.** The estate's skills fire only
when a session matches its task against a description list it may never read.
But every session reads the boot file, unconditionally, before its first
action. Putting a task→skill router THERE converts "remember the skill exists"
(owner memory, session luck) into "the boot path names the skill as part of the
task" (structure). Same shape as PL-013: visibility is not enough; the router
makes loading the skill part of what the task *is*.

## previous-session review

`2026-08-04-hub-skill-family-and-audit.md` (PR #720, merged) built the image
family and closed with the invocation question implicit in its honest null —
"none of the three new skills has fired yet." This session answers the
question structurally instead of waiting for luck: the router in the boot
file, plus the one missing skill (the post-generation pipeline) that the audit
ranked first.

## Scope

Owner-directed: execute the ranked suggestions and design the invocation
mechanism. Here: boot-file router, `asset-pipeline` skill, local half of the
control/ reconciliation. Kit half (template collision fix, effort tiers) is a
separate kit PR. Not a program step; NOW (E1) untouched.

## What landed

*(written at close)*

## Honest nulls

*(written at close)*

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
