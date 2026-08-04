# 2026-08-04 · hub — how spider-swing's art got consistent: reading the sessions that made it

> **Status:** `complete`

- **📊 Model:** opus-5 · high · research — transcript archaeology, findings doc + skill

Time: 2026-08-04 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1` (restarted from main post-#712)

💡 Session idea: **the substrate-kit's core discipline — turn every struggle into
a guide the next session can use — transferred intact to a non-Claude agent, and
produced the estate's most consistent artifact set.** The owner's observation,
and it is the finding that outranks everything else here: spider-swing's art
pipeline was never specified by him. A ChatGPT session, working under
kit-derived project instructions, wrote its own art contract, discovered its own
failure mode, invented its own three-scale audit, and committed all of it so the
next session inherited it. That is precisely the kit's loop, executed by a
different provider. The generalisable claim: **the kit's value is not
Claude-specific — it is a working method that any capable agent can run, and its
transfer is now evidenced rather than assumed.**

## previous-session review

`2026-08-04-hub-image-generation-comparison.md` (PR #712, merged) measured four
surfaces on cold prompts and concluded ChatGPT wins on instruction compliance.
That conclusion survives but was **incomplete in its explanation**: it implied
the shipped art's quality came from the model. Reading the sessions that made
the art shows the quality came from a *committed contract plus a serial gate*,
which no cold prompt can reproduce. The correction matters — a session reading
only #712 would try to solve an art problem by writing a better prompt.

## Scope

The owner supplied six shared ChatGPT transcripts from spider-swing's art
production. Read all six via `tools/read_shared_chat.py` (verified path), plus
the spider-swing repo's own source records and the engine's parallax code.
Deliverables: a findings doc, an `image-prompt` local skill built on the
structure the model created for itself, and a paste-ready prompt for the owner.
Not a program step; NOW (E1) untouched.

## What landed

- **`docs/findings/2026-08-04-generated-art-pipeline.md`** — the five mechanisms
  with verbatim quotes, the two corrections, and the reusable recipe.
- **`.claude/skills/image-prompt/SKILL.md`** + a row in `SKILLS-local.md`.

Two corrections worth naming, because both would have cost a future session:

1. **Seamless horizontal tiling is not required for spider-swing backdrops.**
   Measured: most shipped backdrops score 8–16× interior variance at the wrap
   seam. `swing_lab.gd` mirrors alternate tiles, so the seam is invisible by
   construction, and the art record says the compositions were made knowing
   this. I had advised the owner to check tiling earlier the same day — wrong
   advice, corrected in the finding.
2. **#712's conclusion needed its cause restated.** "ChatGPT wins on image
   generation" is true of cold-prompt compliance and misleading about the
   shipped art, whose quality is a pipeline property. A session reading only
   #712 would try to fix an art problem with a better prompt.

## Honest nulls

- **No image-generation prompts survive in the transcripts** — ChatGPT share
  exports collapse the model's working turns. The reconstruction rests on its
  summaries plus spider-swing's committed prompt records.
- **The magenta-vs-green rule is inferred** from per-asset assignments and
  confirmed only by the repo's later prose; no transcript states it.
- **The cross-provider claim is untested** — running this pipeline on Gemini or
  Grok Imagine would settle whether the advantage is really pipeline-not-model.
- **`chat1` of the six was this session's own test prompt**, not a historical
  art session; a subagent nearly filed its `#FF00FF` as owner-originated
  convention. Caught because this session authored it — a reminder that
  supplied evidence needs provenance, not just reading.
- The skill has **not been invoked yet**; per `SKILLS-local.md`'s own rule,
  skills earn their place by firing.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
