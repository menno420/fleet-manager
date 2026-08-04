# DeepSeek — provider capability reference

> **Status:** `living-ledger`
>
> The V4 model pair, thinking modes, tool support, and the open-weights story.
> **Derived 2026-08-04 from DeepSeek's own API docs
> ([api-docs.deepseek.com](https://api-docs.deepseek.com/quick_start/pricing),
> including its updates/news pages) and the official `deepseek-ai` Hugging Face
> model cards.** **Not a routing table** — see [`README.md`](README.md).

## What this provider is, concretely

Frontier-adjacent capability at prices one to two orders of magnitude below the
US flagships, with **MIT-licensed open weights for the same models the API
serves**. The trade: text-only, and operational quirks (peak-hour pricing,
Beijing-hours cadence) that other providers don't have.

## Models

*Source: vendor pricing page + V4 announcement
([news260424](https://api-docs.deepseek.com/news/news260424)), fetched
2026-08-04.*

| | `deepseek-v4-flash` | `deepseek-v4-pro` |
|---|---|---|
| Context | 1M (*"the default across all official DeepSeek services"*) | 1M |
| Max output | up to **384k** | up to 384k |
| Params (vendor figures) | 284B total / 13B active ¹ | 1.6T total / 49B active |
| $/1M in (cache miss) | **$0.14** | $0.435 |
| $/1M in (cache hit) | $0.0028 | $0.003625 |
| $/1M out | **$0.28** | $0.87 |
| Concurrency limit | 2500 | 500 |

¹ The news post says 284B; the HF card for V4-Flash-0731 shows 304B — both are
vendor figures, recorded as found.

For scale: v4-flash's output price is ~1/180th of Claude Fable 5's. **Peak
pricing at 2× applies 9:00–12:00 and 14:00–18:00 Beijing time (UTC+8) daily**
per the pricing page — a cost consideration Western-hours batch jobs can dodge
entirely.

Model-level facts:

- **Text in, text out only.** No image modality appears anywhere in the fetched
  API docs. A weakness, not a limitation — pair it with local extraction
  (ffmpeg, OCR) as this estate already does for other text-only paths.
- **Thinking / non-thinking dual mode on both models, thinking default-on**,
  controlled via `thinking: {"type": "enabled"}` plus a `reasoning_effort`
  parameter. The HF card recommends the full 384k output ceiling *"for high and
  max reasoning effort levels"*.
- **Tool calls in thinking mode** are supported (*"from DeepSeek-V3.2"*), with
  a beta `strict: true` schema-validated mode on the `/beta` base URL. JSON
  mode exists, with the vendor's own caveat quoted: *"The API may occasionally
  return empty content. We are actively working on optimizing this issue."*
- **API shapes:** OpenAI ChatCompletions **and Anthropic-compatible** endpoints;
  a Responses API serves v4-flash only, with v4-pro *"anticipated in early
  August 2026"*.
- **`deepseek-v4-flash` is a rolling pointer** — currently serving
  V4-Flash-0731 (public beta 2026-07-31); *"the calling method remains
  unchanged."* Pinning requires the open weights, not the API.

## Open weights

*Source: official [deepseek-ai HF collection](https://huggingface.co/collections/deepseek-ai/deepseek-v4)
and model cards.* The V4 collection ships Flash and Pro, base and instruct,
plus DSpark variants — *"licensed under the MIT License"* (both cards checked).
That is the least restrictive license of any frontier-class weights in this
set: no acceptable-use policy, no user-count clause.

## Release cadence

*Source: vendor [updates page](https://api-docs.deepseek.com/updates).*
V4-Flash-0731 public beta 2026-07-31 · V4 (Pro + Flash) 2026-04-24 · V3.2
2025-12-01 · V3.1 (*"hybrid reasoning architecture"*) 2025-08-21 · R1-0528
2025-05-28 · V3 2024-12-26. Roughly a major release per quarter.

## Consumer surface

deepseek.com offers free web chat with the *"newest flagship model"* (page is
Chinese-language; it does not name the serving model or enumerate features —
honest null on DeepThink/search toggles).

## Weaknesses — relative, not absolute

Graded per [`README.md`](README.md): worse at, not incapable of.

- **No vision, no image/video/audio generation.** The most single-modal
  provider in this set. Anything visual routes through extraction first.
- **Rolling model pointer + peak-hour pricing** make reproducibility and cost
  slightly less predictable than fixed-snapshot providers. Steers: pin via open
  weights; batch outside UTC+8 business hours.

## Honest nulls

- Default (non-maximum) output length; whether flash's thinking default
  matches pro's (pricing page implies yes, the guide only demonstrates pro).
- The consumer app's feature set and serving model.
- The 284B-vs-304B param discrepancy (both vendor figures).
- Nothing here is measured in this estate yet.
