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

## The measurement

A 6.65 s / 119.73 fps / 480×1040 phone capture, 3.9 MB. The scroll **doubles
back** — 11 466 px travelled but only 6 256 px covered — so unique content spans
**11 viewport-heights**, not the 20 the travel distance implies.

| sampling | frames | content seen |
|---|---|---|
| **1 fps — Gemini's default** | 7 | **63 %** |
| 2 fps | 14 | 83 % |
| 4 fps | 27 | 98 % |
| **8 fps — `videoMetadata.fps`** | 53 | **100 %** |

Cost of the override: **518 → 3 273 prompt tokens.** Not worth optimising.

Method: extract at 8 fps, measure per-pair vertical displacement by row-profile
correlation, chain the signed positions, then take the union of
`[position, position+viewport]` intervals per sampling rate.

## The best result was Gemini's honesty, not its coverage

Asked at default sampling to state what it had seen, it volunteered the gap
without being led:

> *"I observed 7 distinct scroll positions… there are clear gaps in the
> narrative and context between each frame… I believe I only saw samples of the
> conversation, not the whole thing."*

At `fps=8` it claimed 13 distinct positions, overlapping, no gaps — **and that
checks out**: 13 ≥ the 11 viewport-heights the content actually spans. So the
convention now says to end every recording prompt with a coverage question. It
converts a silent 63 % into a stated 63 %.

## A wrong measurement I nearly reported

The first pass concluded *"no gaps even at 1 fps."* False. Row-profile
correlation **cannot detect a displacement larger than the band it compares** —
given 1 fps samples that had jumped ~2 500 px, a 570 px band returned a bounded,
plausible 369 px. Not an error. A *measurement*, and a wrong one.

It was caught because the number contradicted both Gemini's own report and the
arithmetic (13 positions × 570 px cannot span 20 screens — which is what forced
the net-range calculation that resolved everything). **Same species as
concluding from one probe:** an instrument that silently clamps looks exactly
like an instrument that found something.

## What landed

| File | |
|---|---|
| `docs/conventions/reading-screen-recordings.md` | new — the recipe, the coverage table, the coverage question, the clamping trap |
| `tools/read_screen_recording.py` | the script, hardcoded scratchpad path replaced with `$VERTEX_SA` |
| `.claude/hooks/doc-routes.json` | the `video-audio` route now leads with the new convention and carries the 1 fps warning in its `says` |
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
