# 2026-08-04 · hub — the skill router, the pipeline skill, and de-controlling the close

> **Status:** `complete`

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

- **The task→skill router in `.claude/CLAUDE.md`** — the answer to "how do the
  skills fire without the owner remembering them": nine recurring task classes
  mapped to their skill in the one file every session reads unconditionally,
  with the binding rule stated ("loading the skill is part of doing the task")
  and a defect framing for misses. Deliberately short — only recurring
  classes; the index files carry the rest.
- **`asset-pipeline` skill** — the post-generation half the audit ranked as
  the top gap: corner-sample keying, full-resolution despill (with the
  magenta variant), contract-size downscale, three-scale zero-fringe audit,
  source-record entry, in-engine proxy check. Runnable snippets inline so a
  session needs no other file open.
- **The `control/` conflict resolved locally, decide-and-flag** — venue notes
  in the four control-touching skills: in fleet-manager `control/` is
  historical per the boot file; live equivalents named (session card, PR
  description); format contract in `control/README.md` still citable. ⚑
  Flagged for veto rather than asked.
- `SKILLS-local.md` indexed.

## Honest nulls

- **The router's own effectiveness is unmeasured** — it is structure, not
  proof; the measurement is whether future cards show the right skills firing
  unprompted. Worth checking at the next repo-health pass.
- **The router lives only in fleet-manager.** Generalizing it into the kit's
  `CLAUDE.md.tmpl` (a routing-section scaffold every adopter fills) is the
  obvious follow-up; deliberately not done in the same PR as a template
  change of that reach deserves its own review.
- **`asset-pipeline` has never fired**, and its snippets — while derived from
  the measured probe — have not themselves processed a real delivered image
  end-to-end (the inline-image surface limit stands).
- **The kit half of the suggestions** (verify_command collision in the
  quality-gate template, effort-tier tuple) is a separate kit PR, not this
  one.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
