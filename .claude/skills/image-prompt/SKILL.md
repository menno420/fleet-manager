---
name: image-prompt
description: "The shared method for ANY image-generation prompt — eight sections, anchored to an existing asset, one asset per call, chroma-keyed, function criterion, acceptance question. Route to sprite-prompt, parallax-prompt, or cover-art-prompt when the ask matches one; use this directly for anything else."
---

# image-prompt — the shared method

Write an image-generation prompt using the structure that produced
spider-swing's art — 33 zone assets and 5 sprites with zero chroma fringe on
32 of 33, and dimensional consistency across separate sessions.

> **Provenance.** Reverse-derived from the ChatGPT sessions that made
> spider-swing's art, where the model built it for itself under kit-derived
> instructions; mechanisms re-measured here 2026-08-04
> (`tools/chroma_spill_probe.py`). Full evidence:
> [`docs/findings/2026-08-04-generated-art-pipeline.md`](../../../docs/findings/2026-08-04-generated-art-pipeline.md).

## Route first

Three asset types have their own skill carrying the type-specific deltas —
**load the matching one and this one together**:

| Ask | Skill |
|---|---|
| Character or object sprite on chroma | `sprite-prompt` |
| Layered / parallax background, wall or rail material | `parallax-prompt` |
| Cover, key art, app icon, banner, store asset | `cover-art-prompt` |

Anything else (UI decoration, collectible, one-off illustration): apply this
skill directly.

## When this runs

The owner asks for an image, or a prompt to generate one, on any provider.
Also when a previous generation came back wrong and the instinct is to
re-roll: usually the prompt is missing a section below, and re-rolling
without adding it just buys another dice throw.

## The rule that outranks the prompt

**A prompt cannot carry what a contract should carry.** If the asset must match
an existing set, the match comes from anchoring to a named existing file and
from a committed spec — not from adjectives. Before writing the prompt, check
whether the project already has a source record (spider-swing keeps them at
`assets/source/*/README.md`) and read the invariants out of it rather than
inventing new ones.

## The eight sections

Write them in this order. Omit one only when you can say why it does not apply.

1. **Anchor + exclusion.** Name the existing asset this must match, then state
   what is inherited and what is explicitly NOT. The load-bearing line from the
   original sessions: *"The Garden Spider supplied the pose, orientation,
   dimensions, and quality reference — not its jumping-spider anatomy."*
   Attach the reference image when the surface accepts one — with a reference
   plus this structure, all three measured surfaces converged on compliant
   output (2026-08-04); without one, they diverge.
2. **Subject**, in one sentence.
3. **Style**, stated positively and negatively — the medium and finish it IS,
   and the nearest thing it must NOT be ("painterly semi-realistic, NOT
   cartoon, NOT vector").
4. **Composition and camera** — angle, framing, what fills the canvas, what
   stays empty. For anything with limbs or repeated parts, **enumerate the
   parts by position** rather than counting them — models obey placement far
   better than counts.
5. **Background** — per the type skill; default is a flat chroma field (see
   hard rules). Never ask for transparency directly: generators answer with a
   baked checkerboard.
6. **Standing negatives** — the project's invariants, repeated every single
   time. spider-swing's, verbatim from its own records: *"no text, UI,
   characters, pickups, frames, watermark, border, or apparent extra
   collision"*, plus *"no directional cast shadow"*. (Cover art relaxes the
   text rule — see `cover-art-prompt`.)
7. **Function criterion** — what the art must let the viewer read, at what
   size and speed: *"strong silhouette and material readability at 1280×720
   mobile scale"*, *"readable during 60 m/s play"*, *"must not falsely imply
   collision"*.
8. **One asset only**, stated. Plus target dimensions if known.

Then, outside the prompt, hand back **one acceptance question** the human can
answer in seconds — spider-swing's was *"does it have any colored fringe around
its edges?"*, asked per delivery, and it is the likeliest cause of the 32/33
zero-fringe record.

## Hard rules — these are where quality is lost

- **One asset per generation *call*.** No sprite sheets, no pose grids, no
  multi-asset boards in a single image — sheets are where character
  consistency dies. **The rule is decomposition, not batch size**: a queue is
  safe exactly when the surface turns it into N separate calls (an integrated
  agent environment does; a plain chat collapses the queue into one composite
  board — measured: 41 items → *"Production-ready candidates: None"*). Ask
  what the surface does with a queue before handing it one.
- **Never upscale.** Generate at or above the runtime size and downscale.
  Extracting an asset from a composite sheet counts as upscaling.
- **Diverge cheaply, converge expensively.** A non-integrated surface earns
  its keep for concept exploration at no allowance cost; take the chosen
  concept through the integrated path for the master. Same shape as Grok
  Imagine's standard-then-quality recipe (`docs/CAPABILITIES.md`).
- **Despill at full resolution — the step everything else depends on.**
  Measured (`tools/chroma_spill_probe.py`): semi-transparent edge pixels carry
  ≈+100 green excess at **every** scale including source; clamping green to
  `max(red, blue)` takes it to ≈0. Downscaling does *not* introduce the fringe
  — it makes the existing spill proportionally larger. Audit at source,
  runtime and 25% gameplay scale as a **check**, not a repair step.
- **Key by sampling, never by hex.** Generated "green" fields measured near
  `#22C022` and `#3E8E3E` — none within tolerance 40 of `#00FF00`, so a
  literal match keys zero pixels. Put `#00FF00` in the prompt (it anchors the
  model toward a saturated field); sample an actual corner pixel in the
  pipeline. Chroma choice: magenta `#FF00FF` default, green when the subject
  contains magenta/pink. Record the choice in the manifest.
- **Pose changes are edits, not generations.** Novel physics poses are
  out-of-distribution and failed on all four surfaces tested 2026-08-04.
  Generate a neutral pose, then ask for a small delta from the existing image,
  or transform in-engine.

## Traps

- **A weak result is usually a missing section, not a weak model.** Diagnose
  which of the eight is absent before re-rolling — and before switching
  provider: with structure + reference, the measured surfaces converge.
- **"The art looks wrong" may not be the art.** In the source sessions a
  faint-outline complaint turned out to be two renderer paths drawing
  collision polygons over finished art. Check the renderer before
  regenerating.
- **A model's own aesthetic prior can override your layout on cold prompts.**
  Good for exploration, wrong for matching a set. The fix is the anchor image,
  not a longer style paragraph.
- **Don't let the prompt promise what the collision data does not.** Art that
  implies an anchor where none exists is worse than ugly art.
- **A provider's quality tier can be a persistent *mode*, not a per-image
  button** (measured on Grok Imagine) — check the surface's settings before
  attributing a result to your prompt change.

## Output

Give the owner the prompt as a single fenced block he can paste unchanged, with
no commentary inside it. Follow with the acceptance question and, when
relevant, which surface to run it on (per
[`docs/providers/`](../../../docs/providers/README.md), measured 2026-08-04:
ChatGPT for spec-bound assets on cold prompts; any of the three once an anchor
image + this structure is used; Grok Imagine standard-then-quality for variant
batches; Gemini for expressive one-offs).
