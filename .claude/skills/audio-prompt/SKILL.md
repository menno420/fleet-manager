---
name: audio-prompt
description: "Create or improve game audio — sound effects, loops, music stems — by either route (procedural generator or AI generation), delivered against the committed audio contract: mono 44.1kHz 16-bit WAV, sub-0dBFS with edge fades, manifested, loops mathematically continuous. Use for any audio ask."
---

# audio-prompt

The audio member of the asset family. Unlike the image skills, this one is
**not reverse-derived from an accepted example** — the owner is explicitly not
yet happy with the current samples (2026-08-04). What IS measured is the
**delivery contract** (spider-swing's committed
`assets/source/audio/README.md`), and the method that made the image family
work transfers. Provenance is marked per section below.

## When this runs

Any audio ask: a new sound effect, a loop, a music stem, a voice line — or
"make the audio better." Also when an audio asset clicks, pops, or breaks at
its loop point: that is a contract violation, not a taste problem.

## The delivery contract — measured, committed, non-negotiable

From spider-swing's own production contract; any route must land here:

- **Mono, 44.1 kHz, 16-bit PCM WAV** (non-positional cues gain nothing from
  baked stereo; mono halves memory and APK cost).
- **Every transient peaks below 0 dBFS and carries a 3 ms edge fade** — the
  anti-click rule.
- **Loops are mathematically continuous, never crossfaded to silence**: short
  loops from integer-Hz components only (the committed 0.5 s reel loop);
  long stems from whole-loop-period oscillators with wrapped tails (the
  committed synchronized 32 s pair).
- **Round-robin variants** for frequently-fired cues (attach, release, burst,
  catch) — repetition of one sample is the tell of cheap audio.
- **The manifest is the provenance record**: duration, peak, RMS, SHA-256,
  event mapping, loop state per file
  (`assets/runtime/audio/audio-sample-manifest.json`).
- **Presentation owns timing; simulation never chooses or times a sound.**

## Route A — the procedural generator (current, reproducible)

`tools/generate_audio_samples.py` (spider-swing): oscillators, Karplus–Strong
plucks, seeded noise, filters, envelopes, delays. Deterministic —
`--check` proves exact reproducibility. **Improving existing samples means
editing this generator**, which keeps provenance perfect (no external
material, no rights questions) and every change diffable.

Steer: this route is strongest for UI cues, whooshes, plucks, tonal loops —
weakest for organic/textured sounds (creatures, foliage, impacts with body).
When the owner says a sample "doesn't feel right," ask WHICH quality is wrong
(too synthetic · too harsh · too repetitive · wrong pitch/length) before
touching code — each maps to a different part of the synthesis.

## Route B — AI generation (the likely upgrade path; provider unmeasured)

*Provenance: method transferred from the measured image findings; no audio
provider has been measured in this estate yet.* The image lessons that carry
over directly:

1. **One asset per generation call.** Never "generate my sound pack".
2. **A prompt states subject, function criterion, and negatives** — e.g.
   *"single soft web-attach thwip, organic not synthetic, no reverb tail, no
   music, no voice, under 400 ms"*. The function criterion for game audio is
   always: readable at gameplay pace, distinct from the other cues in its
   family, tolerable on the thousandth repetition.
3. **First accepted asset becomes the reference** — later asks anchor to it
   ("same material world as the attached sample") exactly as sprites anchor
   to the Garden Spider.
4. **Run the provider comparison before committing to one** — same brief to
   2–3 surfaces, scored on the contract + the acceptance questions, exactly
   like the 2026-08-04 sprite test. Candidate surfaces from the provider
   docs: Grok Imagine's video-with-audio path, ElevenLabs-class SFX tools,
   Stable Audio-class models — none measured here; the first real run should
   append the result to `docs/CAPABILITIES.md`.
5. **Rights are part of delivery**: record the generating service and its
   output-rights terms in the source record. The current pack's "no external
   material" purity is a property worth keeping deliberately, not losing
   accidentally.

Post-generation pipeline (either route): convert to the contract format →
normalize peaks below 0 dBFS → apply/verify edge fades → for loops, verify
sample-exact boundary continuity → regenerate the manifest entry.

## Acceptance questions (per delivery, in this order)

1. Loop it ten times — any click, pop, or audible seam at the boundary?
2. Fire it the way gameplay will (rapid repetition for cues) — annoying by
   the tenth time?
3. Played next to its family (other cues in the same event group) — distinct
   at a glance, same sonic world?

## Traps

- **"Better audio" is not a brief.** Decompose the complaint into the quality
  axis first; the owner's dissatisfaction with the current pack is data — get
  the WHICH before generating anything.
- **A crossfaded loop is a hidden defect** — it survives casual listening and
  fails in-game where the loop runs for minutes. The contract's
  integer-Hz/whole-period discipline exists because fades to silence were
  rejected.
- **Stereo files that "sound richer" cost double memory for nothing** on
  non-positional mobile cues. The mono rule is a decision, not an oversight.
- **Don't mix provenance regimes silently.** One AI-generated file in a
  procedurally-pure pack changes the rights story of the whole pack — the
  source record must say which files came from where.
