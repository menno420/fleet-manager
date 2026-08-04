# 2026-08-04 · hub — structure converges the models: the skill's first fire

> **Status:** `complete`

- **📊 Model:** opus-5 · high · research — owner-run convergence test

Time: 2026-08-04 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1` (restarted from main post-#715)

💡 Session idea: **a ranking measured under one prompt regime is a fact about
that regime, not about the things ranked.** This morning's four-surface test
concluded ChatGPT wins on instruction compliance. It does — *on cold prompts
with no reference*. Given the eight-section structure and an anchor image, all
three surfaces produced usable, spec-compliant sprites, including the one that
had failed the background spec four times running. The ranking was never wrong;
its scope was unstated, and an unscoped ranking reads as a property of the
model. The generalisable form: **when you publish a comparison, publish the
conditions in the same sentence** — otherwise the next session inherits a
verdict and not the experiment.

## previous-session review

`2026-08-04-hub-inhabiting-vs-observing.md` (PR #715, merged) minted PL-013 and
cited it. Its honest-nulls list said the decomposition claim rested on the
owner's experience rather than an estate measurement. This session is the first
of today's claims to get an actual counterfactual run — and it moved the
answer, which is the argument for running them.

## Scope

Record the owner-run convergence test and correct the scope of the 2026-08-04
image-generation entry. Fold in two capability facts from Grok Imagine's
settings panel. Not a program step; NOW (E1) untouched.

## What landed

- **`docs/CAPABILITIES.md`** — two entries. A **scope correction** on the
  morning's four-surface ranking (it holds for cold prompts; with structure +
  reference all three converged, Grok included after four prior failures on the
  same spec), with the owner-flagged confound stated inline. And a new
  capability entry: **Grok Imagine's settings panel publishes what the vendor
  docs do not** — video 6s/10s/15s at 480p with audio, and a persistent
  Snelheid↔Kwaliteit image mode.
- **`docs/providers/grok.md`** — the duration null closed, the quality-tier
  entry corrected from "button" to "persistent mode", and the convergence
  result recorded.

Two things worth keeping. **Gemini narrated the anchor/exclusion decomposition
back** — *"I maintained the specific three-quarter perspective and 6-leg
configuration as requested… rather than inheriting the more rounded proportions
of the reference garden spider"* — which is section 1 of the skill restated by
the model, from the surface whose prior had silently overridden layout two
rounds earlier. Given structure, the same prior became deliberate and legible.
And **the quality tier is a mode, not a button**: an earlier one-off "quality
pass" may govern every later generation, which is exactly how a tier difference
gets mistaken for a prompt difference.

## Honest nulls

- **The causal claim for Grok is confounded and says so.** Its image mode was
  set to Kwaliteit; whether that predated the test or was set by the earlier
  quality press is unknown. Structure and tier both moved. The owner flagged
  this before the writeup — the second time today the person who ran the
  experiment caught the confound the analysis would have missed.
- **One image per provider.** Convergence on n=1 each.
- **Fringe after downscaling to 384×181 is still untested** — the whole point
  of the three-scale audit is that clean-at-source predicts nothing about
  clean-at-runtime. This remains the highest-value open measurement of the day.
- The settings-panel facts are **owner-screenshot-sourced**, not read from a
  vendor page; xAI still publishes no duration caps.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
