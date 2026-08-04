---
name: image-prompt
description: "Write a generation prompt for a game or product image — anchored to an existing asset, one asset per generation, chroma-keyed, with a function criterion and an acceptance question. Use whenever the owner asks for an image prompt, a sprite, a background, or art for any model."
---

# image-prompt

Write an image-generation prompt using the structure that produced
spider-swing's art — 33 zone assets and 5 sprites with zero chroma fringe on
32 of 33, and dimensional consistency across separate sessions.

> **Provenance.** This structure was not designed here. It was reverse-derived
> from the ChatGPT sessions that made spider-swing's art, where the model built
> it for itself under kit-derived instructions. Full evidence, with quotes:
> [`docs/findings/2026-08-04-generated-art-pipeline.md`](../../../docs/findings/2026-08-04-generated-art-pipeline.md).

## When this runs

The owner asks for an image, a sprite, a background, key art, or a prompt to
generate any of those — on any provider. Also when a previous generation came
back wrong and the instinct is to re-roll: usually the prompt is missing a
section below, and re-rolling without adding it just buys another dice throw.

## The rule that outranks the prompt

**A prompt cannot carry what a contract should carry.** If the asset must match
an existing set, the match comes from anchoring to a named existing file and
from a committed spec — not from adjectives. Before writing the prompt, ask
whether the project already has a source record (spider-swing keeps them at
`assets/source/*/README.md`), and if it does, read the invariants out of it
rather than inventing new ones.

## The eight sections

Write them in this order. Omit one only when you can say why it does not apply.

1. **Anchor + exclusion.** Name the existing asset this must match, then state
   what is inherited and what is explicitly NOT. The load-bearing line from the
   original sessions: *"The Garden Spider supplied the pose, orientation,
   dimensions, and quality reference — not its jumping-spider anatomy."*
   Attach the reference image when the surface accepts one.
2. **Subject**, in one sentence.
3. **Style**, stated positively and negatively — the medium and finish it IS,
   and the nearest thing it must NOT be ("painterly semi-realistic, NOT cartoon,
   NOT vector").
4. **Composition and camera** — angle, framing, what fills the canvas, what
   stays empty. For anything with limbs or repeated parts, **enumerate the
   parts by position** rather than counting them ("4 legs near side spaced left
   to right, 2 far legs visible past the head, 6 visible total") — models obey
   placement far better than counts.
5. **Background** — a flat chroma field, `#FF00FF` magenta by default,
   `#00FF00` green when the subject itself contains magenta or pink. Say
   *uniform*, and forbid gradients, glow and cast shadows explicitly. Never ask
   for transparency directly: generators answer that with a baked checkerboard.
6. **Standing negatives** — the project's invariants, repeated every single
   time. spider-swing's, verbatim from its own records: *"no text, UI,
   characters, pickups, frames, watermark, border, or apparent extra
   collision"*, plus *"no directional cast shadow"*.
7. **Function criterion** — what the art must let the viewer read, at what size
   and speed. This is what separates a good asset from a pretty one: *"strong
   silhouette and material readability at 1280×720 mobile scale"*, *"readable
   during 60 m/s play"*, *"must not falsely imply collision"*.
8. **One asset only**, stated. Plus target dimensions if known.

Then, outside the prompt, hand back **one acceptance question** the human can
answer in seconds — spider-swing's was *"does it have any colored fringe around
its edges?"*, and asking it per delivery is the likeliest cause of the 32/33
zero-fringe record.

## Hard rules — these are where quality is lost

- **One asset per generation *call*.** No sprite sheets, no pose grids, no
  multi-asset boards *in a single image*. Sheets are where character
  consistency dies.
  **The rule is decomposition, not batch size.** A queue is safe exactly when
  the surface turns it into N separate calls: an integrated agent environment
  (ChatGPT Work, Claude Code) decomposes and executes the parts separately; a
  plain chat has no boundary between items and collapses a 41-item queue into
  one composite board, then slices assets back out of it — which produced
  *"Production-ready candidates: None"* despite a more detailed manifest than
  any successful run. **Ask what the surface does with a queue before handing
  it one.**
- **Never upscale.** Generate at or above the runtime size and downscale.
  Extracting an asset from a composite sheet counts as upscaling and was named
  as a primary cause of that failed batch.
- **Diverge cheaply, converge expensively.** A non-integrated surface still
  earns its keep for concept exploration — the failed batch produced *"useful
  visual concepts, not production-ready masters"* at no Work-allowance cost.
  Explore broadly there, then take the chosen concept through the integrated
  path for the master. Same shape as Grok Imagine's standard-then-quality
  recipe in [`docs/CAPABILITIES.md`](../../../docs/CAPABILITIES.md).
- **Key at full resolution, then re-check after downscaling.** Downscaling
  reintroduces chroma into partially transparent edge pixels even when the
  full-resolution key was clean. This is the single non-obvious fact in the
  whole method.
- **Pose changes are edits, not generations.** Novel physics poses ("gripped in
  one front leg, mid-swing") are out-of-distribution and failed on all four
  surfaces tested 2026-08-04. Generate a neutral pose, then ask for a small
  delta from the existing image, or rotate in-engine.
- **Do not ask for seamless horizontal tiling unless the renderer needs it.**
  Check first: spider-swing's swing-lab view mirrors alternate tiles, so
  backdrops need no edge match and requiring one costs composition for nothing.
  Its purpose-built rail tiles do need it.

## Traps

- **A weak result is usually a missing section, not a weak model.** Diagnose
  which of the eight is absent before re-rolling.
- **"The art looks wrong" may not be the art.** In the source sessions a
  faint-outline complaint turned out to be two renderer paths drawing collision
  polygons over finished art. Check the renderer before regenerating.
- **A model's own aesthetic prior can override your layout.** Measured
  2026-08-04: Gemini produced anatomically better far-side legs while ignoring
  the enumerated layout. Good for exploration, wrong for matching a set.
- **Don't let the prompt promise what the collision data does not.** Art that
  implies an anchor where none exists is worse than ugly art.

## Output

Give the owner the prompt as a single fenced block he can paste unchanged, with
no commentary inside it. Follow with the acceptance question and, when relevant,
which surface to run it on (per
[`docs/providers/`](../../../docs/providers/README.md) — as of 2026-08-04:
ChatGPT for spec-bound assets, Grok Imagine standard-then-quality for variant
exploration, Gemini for expressive one-offs).
