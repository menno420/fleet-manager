# 2026-08-06 · hub — video is readable; the question is how much of it you read

> **Status:** `complete`

- **📊 Model:** opus-5 · high · research

Time: 2026-08-06 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: the owner asked whether a fast screen recording could be read,
and hypothesised Gemini might do better *"since there is no frame extraction."*
There is frame extraction — it just happens server-side, at 1 fps, invisibly.
That is the whole finding: **the failure mode is not an error, it is a confident
transcription of the 63 % that arrived.**

## The measurement — corrected twice, the second time by the owner

A 6.65 s / 119.73 fps / 480×1040 phone capture, 3.9 MB. **Gaps counted properly:
pairs of consecutive frames that share no content at all.**

| sampling | frames | pairs | pairs with **no shared content** |
|---|---|---|---|
| **1 fps — Gemini's default** | 7 | 6 | **5** |
| 2 fps | 14 | 13 | 11 |
| 4 fps | 27 | 26 | 15 |
| 8 fps | 53 | 52 | 5 |
| **16 fps** | 106 | 105 | **0 — complete** |

Tokens: 518 / 3 273 / 6 462 at 1 / 8 / 16 fps.

**Two of my measurements were wrong, and one of them was published.**

1. **A correlation search cannot report a shift larger than its window.** Given
   1 fps samples that had jumped far past it, it returned a bounded, plausible
   `369 px` — not an error, a *measurement*. Caught by arithmetic.
2. **Row-profile correlation aliases on repetitive UI.** A Claude Code
   transcript is wall-to-wall near-identical rows, and the estimator locked onto
   the wrong period, **inventing 2 890 px of reverse scrolling that never
   happened** — plus a "100 % coverage at 8 fps" claim that is false (8 fps has
   5 gaps). Both reached a pushed commit and an open PR.

**The owner caught the second one**, from knowing what his own thumb had done:
*"I did not move the text back in the opposite direction at any time."* No check
in this estate would have. Re-measured on his word first, per DISCOVERY RULE
step 0 — and he was right: every resolvable shift is one-directional, and
Gemini at 16 fps independently reports *"one-directional (downwards) throughout
the entire video. It never reversed."*

The diagnostic worth keeping: at 8 fps only **9 of 52** pairs yielded a
confident displacement, and all nine were moments the scroll had **paused**. An
estimator that only works when nothing is moving still emits numbers while
everything is.

**The method that works asks a different question** — *do two consecutive frames
share any content?* Several text bands from frame N, searched across the whole
of frame N+1, one strong normalized match required. A pair with no match **is**
a gap. No displacement estimate, nothing to alias.

## Gemini's honesty is the reusable finding

At default sampling, unled, it volunteered the gap:

> *"I observed 7 distinct scroll positions… there are clear gaps in the
> narrative and context between each frame… I believe I only saw samples of the
> conversation, not the whole thing."*

At `fps: 16` it reported **14 positions, continuous, no gaps, one-directional** —
all three independently confirmed. So the convention says to end every recording
prompt with a coverage question. It converts a silent gap into a stated one.

## What landed

| File | |
|---|---|
| `docs/conventions/reading-screen-recordings.md` | new — the recipe, the coverage table, the coverage question, the clamping trap |
| `tools/read_screen_recording.py` | the script, hardcoded scratchpad path replaced with `$VERTEX_SA` |
| `.claude/hooks/doc-routes.json` | the `video-audio` route leads with the new convention and warns that the default sees almost nothing |
| `docs/CAPABILITIES.md` | append-log entry with the full measurement |

The route change matters more than the doc: the trigger already fired on
`.mp4`/`ffmpeg`, so a session reaching for a recording now gets *"the default
sees 63 % of a scroll"* before it takes the default.

## Verification

- `python3 tools/check_doc_routes.py --strict` → **exit 0** (20 routes, 15 docs
  routed, 0 errors), and the route re-tested live against an `ffmpeg` command.
- `python3 tools/check_no_false_walls.py --strict` → recorded at close.
- `python3 bootstrap.py check --strict` → recorded at close.

## Honest nulls

- **`fps` above 8 is untested.** 8 sufficed for a thumb-flick on a 1040 px
  screen; a faster flick or taller viewport may need more, and nothing here
  establishes the ceiling.
- **The 20 MB inline limit is from the API contract, not measured** — the
  largest clip actually sent was 7.3 MB.
- **Audio untested** — both clips were silent screen captures.
- **One clip, one device, one app.** The coverage percentages are exact for this
  recording and indicative for others.

## ⟲ Previous-session review

The card before this one moved a requirement into the artifact its reader
actually opens. This one does the same thing to a *number*: the recipe existed
in `CAPABILITIES.md` § CAN and was correct, but said nothing about sampling
rate — so a session could follow it exactly and still read two-thirds of a
video. Correct instructions with a missing parameter fail quietly, which is the
same shape as the placement failures, one level down.
