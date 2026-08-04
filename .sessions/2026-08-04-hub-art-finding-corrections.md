# 2026-08-04 · hub — correcting the art finding: decomposition, not batch size

> **Status:** `in-progress`

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

*(written at close)*

## Honest nulls

*(written at close)*

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
