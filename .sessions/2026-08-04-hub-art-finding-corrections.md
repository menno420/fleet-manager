# 2026-08-04 · hub — correcting the art finding: decomposition, not batch size

> **Status:** `complete`

- **📊 Model:** opus-5 · high · research — owner-corrected causal claim

Time: 2026-08-04 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1` (restarted from main post-#713)

💡 Session idea: **a finding derived from transcripts inherits the transcripts'
blind spots, and only the person who ran them can see the confound.** The
2026-08-04 art finding (#713) read a 41-asset failure as proof that serial
beats batch. The owner then supplied two facts no transcript contains: that
session was a *deliberate cost experiment* on a non-integrated surface (plain
chat and image generation do not draw down the weekly Work allowance), and the
real difference is that **an integrated environment decomposes a request into
separately-executed parts while a plain chat cannot**. So the failure had two
causes, not one, and the rule I extracted was the wrong shape — a prohibition
where the truth is a design requirement.

The generalisable form: **evidence supplied by a person carries their intent,
and the intent is not in the artifact.** A transcript shows what happened; only
its author knows what was being tested. Ask before concluding — the same
mistake, in miniature, as a subagent nearly filing this session's own test
prompt as historical owner convention.

## previous-session review

`2026-08-04-hub-art-pipeline-archaeology.md` (PR #713, merged) produced the
findings doc and the `image-prompt` skill. Its honest-nulls list was accurate
about what it could not see, but it did not flag the strongest inference in the
document — "specification did not save it; serial discipline was the missing
ingredient" — as an inference at all. It was stated as fact from a single
session with two uncontrolled variables. **The lesson: the claims most worth
marking are the tidy ones**, because a clean causal story is the shape a
confound takes when you only have one data point.

## Scope

Fold three owner corrections into the finding and the skill. No new research.
Not a program step; NOW (E1) untouched.

## What landed

- **`docs/findings/2026-08-04-generated-art-pipeline.md` §2** rewritten:
  *"One asset per generation **call** — the rule is decomposition, not batch
  size."* Names the execution boundary as the mechanism, flags the two-variable
  confound explicitly, and adds the two-tier reading (diverge cheaply on a
  non-integrated surface, converge expensively on the integrated one).
- **`.claude/skills/image-prompt/SKILL.md`** — hard rules updated to match, plus
  a new *"diverge cheaply, converge expensively"* rule pointing at the same
  two-tier shape as the Grok Imagine standard-then-quality recipe.

One detail worth keeping: the failed batch **had read access to the committed
docs stating the six-visible-leg convention and drifted off it anyway.**
*Readable is not binding.* That is a sharper statement of why repo integration
matters than "the agent can see the repo" — enforcement, not visibility, is the
active ingredient.

## Honest nulls

- **Still one data point.** No session has run a 41-item queue *in* the
  integrated environment, so "decomposition fixes it" is a mechanism the owner
  states from experience, not something this estate has measured. The doc says
  so.
- **The cost claim is owner-reported** — that plain chat and image generation
  do not draw down the weekly Work allowance is not verified against a vendor
  page, and `providers/chatgpt.md` still carries plan details as
  secondary-sourced.
- The `image-prompt` skill **has still not fired**; it was edited before its
  first invocation.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
