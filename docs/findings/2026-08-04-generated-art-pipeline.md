# How spider-swing's generated art got consistent — and why it is not a prompting story

> **Status:** `reference`
>
> Derived 2026-08-04 from six owner-supplied ChatGPT share transcripts (read
> with `tools/read_shared_chat.py`), spider-swing's committed source records
> (`assets/source/*/README.md`, `docs/visual/zones/zone-art-audit.json`), and
> its engine code (`game/presentation/scripts/swing_lab.gd`). Quotes are
> verbatim from those sources. Cross-provider claims are marked as inference
> where they are inference.

## Why this document exists

On 2026-08-04 a four-surface image-generation comparison
([`../CAPABILITIES.md`](../CAPABILITIES.md), same date) measured ChatGPT,
Gemini, Grok chat and Grok Imagine on identical cold prompts and found ChatGPT
best at instruction compliance. **That result is true and its implied
explanation is wrong.** spider-swing's 33 audited zone assets and 5 spider
sprites are not good because a model is good at prompts. They are good because
a *pipeline* was built, committed, and enforced. A session that reads only the
comparison will try to fix an art problem by writing a better prompt, which is
the wrong tool.

This document records the pipeline, its origin, and the one non-obvious
technical fact that makes it work.

## The headline finding — the kit's loop ran on a non-Claude agent

**The owner specified none of it.** Across five real production sessions he
never named a dimension, a file format, a colour, a chroma key value, or a
naming convention. His own account — *"I did not always provide clear specs and
mostly just gave them the freedom to design their own things"* — checks out
against the transcripts.

What produced the consistency was a ChatGPT session, running under project
instructions descended from this estate's substrate-kit conventions, executing
**the kit's central discipline: turn a struggle into a durable guide for the
next session.** It wrote its own art contract, hit its own failure mode,
invented its own audit, and committed all three so successors inherited them.

The pivotal moment is the model writing its own governing instructions, after
the owner asked for a handover prompt for context-length reasons:

> "You are the lead design, engineering, and delivery agent for Spider Swing.
> Menno defines the product vision and evaluates playable feel; you are expected
> to turn that direction into coherent technical and design decisions,
> implementation, verification, and merged results."

and, in twenty-five words, the entire pipeline that followed:

> "Generated artwork is a production asset: create it deliberately, inspect it
> visually, revise it when necessary, integrate it without distortion, and
> verify it in-engine."

plus the anti-drift clause that let it survive across sessions — the same
principle as this repo's own precedence rule:

> "Treat the repository's current main, executable tests, merged commits, build
> artifacts, and current project documentation as authoritative. Treat earlier
> conversations, summaries, plans, session journals, and PR descriptions as
> useful history, not automatically current truth."

**Why this matters beyond art:** the kit's method is not Claude-specific. It is
a working discipline a capable agent of any provider can run, and this is the
first *evidenced* transfer rather than an assumed one.

## The five mechanisms, in order of leverage

### 1. Freeze the first good asset as a written contract

Nobody chose `384×181`. It is whatever the first finished Garden Spider
happened to be. The model then named it a *"source contract"*, wrote it into
repo documentation, and made every later spider conform. The decomposition it
used is the reusable part:

> "The Garden Spider supplied the pose, orientation, dimensions, and quality
> reference — **not its jumping-spider anatomy**."

Inherit pose, size, framing and quality bar; explicitly exclude the thing that
must differ. That is why five spiders are pixel-identical in dimensions while
reading as five genuinely different species.

It only worked because the model refused to scale before the contract existed:

> "I intentionally stopped at the Classic spider; other profiles retain their
> procedural art until they can receive equally careful treatment."

One asset shipped instead of five mediocre ones — a direct execution of the
owner's only real art brief: *"it's not about speed or volume, it's about making
sure that what we have is actually usable."*

### 2. Never batch — the batch failure is total, not partial

One session attempted 41 assets at once with a **more** detailed manifest than
anything in the successful sessions. Outcome:

> "Production-ready candidates: **None.**"

> "The image generator repeatedly interpreted the 41-item queue as a single
> comprehensive production board, even when given isolated asset instructions
> and a specific reference image… several were **enlarged from board cells**."

Specification did not save it; serial discipline was the missing ingredient.
Corollary rule: **generate at or above native size and downscale only — never
upscale, and never extract an asset from a composite sheet.**

### 3. Key at full resolution, then re-audit *after* downscaling

The single non-obvious technical fact in the corpus, discovered by the model's
own scan:

> "The first automated edge scan caught exactly the failure mode the requirement
> warned about: **downscaling reintroduced magenta into partially transparent
> edge pixels even though the full-resolution key was clean.**"

A single-scale check would have shipped a faint halo on every asset. The fix
became a permanent three-scale audit — source, runtime, and 25% gameplay scale
— and it kept catching real defects:

> "The first source/runtime/gameplay alpha audit caught seven small matte
> defects — including only a handful of chroma-colored edge pixels, but exactly
> the sort that becomes a faint halo at speed."

Committed result, in `docs/visual/zones/zone-art-audit.json`: **zero chroma
fringe pixels on 32 of 33 runtime assets** (the exception,
`silk-hollow-floor-wall`, carries 46).

### 4. Chroma key beats asking for transparency — and the key colour is per-asset

Generators produce baked checkerboards when asked for alpha directly:

> "The first repair came back with a **baked checkerboard rather than usable
> alpha**, so it fails the asset pipeline even though the silhouette is right."

So every source was generated on a flat chroma field and keyed afterwards. The
shipped split is **25 magenta / 8 green**, and the rule — never stated in any
transcript, but later committed to spider-swing's zone-art record — is palette
collision avoidance:

> "flat `#ff00ff`-family chroma field, **or green where magenta would collide
> with warm Silk/City fibres**, later keyed to alpha"

Magenta is the default; green is the escape hatch for subjects containing
magenta or pink. **The key colour belongs in the manifest, not in the model's
head** — in the 41-asset run its own chroma assignments drifted between the
plan table and the result table within a single session.

### 5. Art must make the same promise as the collision data

The rule that separates game art from illustration, and the model held it even
when breaking it would have been easier:

> "The measurement found real detachments… Silk ceiling pieces are 11–23 px from
> the wall, Storm's spire 29 px, Web City's egg support 69 px… **Painting across
> those gaps would create fake collision.**"

> "If a gap is only transparent padding, the renderer will close it; if the
> collision itself is detached, **I will not paint a fake support over
> traversable space** — I'll keep that defect explicit."

It also repaired art that lied in the other direction — a spire that was
ceiling-anchored in data but *"reads as floor-rooted"* in the painting — *"so
the art makes the same promise as the anchor data."* The associated audit
vocabulary it invented and reused: **false-anchor**, **false-route**,
**collision-promise**, **seam-first**, **hazard separation**.

## Two corrections this investigation forced

**1. Seamless horizontal tiling is NOT required for spider-swing backdrops.**
Measured here: most shipped backdrops do not tile (`web-city-backdrop` scores
16× its interior variance; `bramble-backdrop-mid` 15×). This is not a defect.
`swing_lab.gd` draws every second tile mirrored —

```gdscript
var mirrored := posmod(tile_index, 2) == 1
```

— so each tile's right edge always meets its own reflection and the seam is
invisible by construction. The art was made knowing this; the source record
says so: *"seam-aware compositions mirrored on alternating tiles by
`SwingLabView`."* Tiling **is** required for the purpose-built rail tiles, and
those measure clean (`canopy-vine-rail-tile` at 0.00). Asking a generator for
seamless backdrops here is a false constraint that costs quality for nothing.

**2. "ChatGPT is better at image generation" understates and misplaces the
cause.** Its measured advantage is instruction compliance under a cold prompt.
The shipped art's advantage is a committed contract, a serial gate, and a
numeric audit — none of which is a model property. Any of the four surfaces
tested would produce more consistent output inside this pipeline than outside
it. *(Inference — not tested across providers.)*

## What the owner did that mattered

His feedback was short, blunt, comparative, and never technical. The single
highest-leverage turn in the corpus:

> "the first 2 environments are actually finished… **reproduce the standard of
> the first 2 finished environments** (0 - 5000 and 5000 - 10000)"

He did not describe a standard — he pointed at his own finished artifact and
named it the standard. The model converted that into four measurable axes
(parallax depth, wall construction, obstacle edge treatment, physical
attachment) and, in doing so, found that the complaint was not an art problem
at all:

> "The 'faint outlines' are not in the PNG edges: two renderer paths were
> deliberately redrawing collision and rest-position polygons over finished art."

**Generalisable: benchmark against your own best existing artifact, not against
a description — and diagnose before regenerating.** A whole regeneration cycle
was nearly spent on a renderer bug.

## The reusable recipe

Implemented as [`.claude/skills/image-prompt/SKILL.md`](../SKILLS-local.md).

1. **Anchor** to a specific existing asset; state what is inherited and what is
   explicitly not.
2. **One asset per generation.** Never a sheet, never a batch, never a
   multi-pose grid.
3. **Native size or larger**, then downscale. Never upscale, never crop out of a
   composite.
4. **Flat chroma field**, magenta by default, green when the subject contains
   magenta/pink. Record the choice in the manifest.
5. **Standing negative list** — the project's invariants, repeated every time
   (no text, UI, watermark, frame, border, cast shadow, extra objects).
6. **Function criterion** — what the art must let the player read, at what
   scale and speed.
7. **Audit after downscaling**, not only after keying.
8. **One named acceptance question** handed back to the human per delivery
   (spider-swing's was *"has no colored fringe around its edges"* — likely the
   direct cause of the 32/33 zero-fringe record).

## Honest nulls

- **Image-generation prompts are not visible in the transcripts.** ChatGPT share
  exports collapse the model's working turns; the reconstruction above comes
  from its summaries plus spider-swing's committed prompt records.
- **Rounds per asset are unknowable** — only elapsed-time headers survive (31m
  for one sprite; 50m and 41m for obstacle-art PRs).
- **The magenta-vs-green rule is inferred** from the per-asset assignments and
  confirmed only by the repo's later prose, never stated in a transcript.
- **The cross-provider claim in correction 2 is untested.** Running this
  pipeline on Gemini or Grok Imagine would settle it and has not been done.
