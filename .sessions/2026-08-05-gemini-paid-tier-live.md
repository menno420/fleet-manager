# 2026-08-05 · hub — Gemini paid tier live, and two standing owner decisions

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · docs-only — capture two policies and the
  measured paid-tier facts

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1`

💡 Session idea: **a spend permission is only usable if it is written where the
spender reads.** The owner granted sessions free use of a capped Gemini budget
in chat. Left there, the next session would have found a working paid key, no
stated permission, and would have either asked (wasting his attention on a
settled call) or refused to spend his money (wasting the budget). A permission
that lives only in conversation is functionally a prohibition.

## previous-session review

`2026-08-05-studio-api-asymmetry.md` (PR #733, merged) recorded that the free
API served strictly less than the Studio UI. That asymmetry is now closed from
the other side: the paid key reaches everything.

## What landed

- **[D-0011]** — the Gemini paid key is free for sessions to spend, capped.
- **[D-0012]** — publication default: work is public unless it exposes a key.
- `docs/providers/gemini.md` — paid tier measured: what it unlocks, the image
  delivery mechanism, and the per-image price.

## Measured — first paid call, 2026-08-05

| Fact | Value |
|---|---|
| Models visible, paid key | **58** (vs 50 free) |
| Image generation | works — `gemini-3.1-flash-image` |
| Delivery | base64 `inlineData` in the JSON response → decoded straight to disk |
| Output | 1408×768 **JPEG** (not PNG), 549 KB |
| Chroma at corner | RGB(6,250,5) — corner-sample keying viable |
| Tokens | 69 in · 1,120 image out · 1,491 total |
| Cost | **≈ $0.086** at $60/1M output tokens |
| Nano Banana Pro equivalent | ≈ $0.134 per 1K/2K image |

Provenance: all rows **measured** — API response and `usageMetadata` from the
call; prices quoted from
[Google's pricing page](https://ai.google.dev/gemini-api/docs/pricing).

## Honest nulls

- **Pro and search grounding are listed but were not called on the paid key** —
  only image generation was exercised after billing went live. Their cost and
  behaviour on this key are unmeasured.
- The generated sprite has a real defect for game use: far-side legs render as
  pale translucent shapes, and JPEG delivery puts compression artefacts on the
  chroma edge. Prompt/pipeline issues, not model limits — but unfixed.
- **No spend guard exists.** The €10 is a hard cap only because auto-reload is
  off; nothing warns before it is consumed.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
