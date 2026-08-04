# Mistral — provider capability reference

> **Status:** `living-ledger`
>
> The model line-up with licenses per model, reasoning and structured-output
> support, the audio/OCR specialists, and the Vibe consumer surface.
> **Derived 2026-08-04 from Mistral's own docs
> ([docs.mistral.ai](https://docs.mistral.ai/getting-started/models/), model
> cards) and [mistral.ai/pricing](https://mistral.ai/pricing/api).** Where the
> vendor changelog's years contradicted a model card, the model card was
> preferred (the changelog fetch garbled 2025/2026 labels — noted per entry).
> **Not a routing table** — see [`README.md`](README.md).

## What this provider is, concretely

The European provider whose **default posture is open weights** — most current
models ship Apache 2.0, the least encumbered license in this set alongside
DeepSeek's MIT — with a specialist bench (OCR, transcription, TTS, embeddings)
priced per page/minute/character rather than per token.

## Core text/vision models

*Source: vendor model cards + API pricing page, fetched 2026-08-04.*

| Model | API ID | Context | $/1M in/out | License | Released |
|---|---|---|---|---|---|
| Medium 3.5 (flagship) | `mistral-medium-3-5-26-04` | 256k | $1.5 / $7.5 | **Modified MIT** (open weights) | 2026-04-28 |
| Small 4 | `mistral-small-2603` | 256k | $0.15 / $0.6 | Apache 2.0 | 2026-03-16 |
| Large 3 | `mistral-large-2512` | 256k | $0.5 / $1.5 | Apache 2.0 | 2025-12-02 |
| Ministral 3 (14B/8B/3B) | `ministral-3-{14b,8b,3b}` | n/v | $0.2 / $0.15 / $0.1 (symmetric) | Apache 2.0 | v25.12 |
| Codestral | `codestral` (v25.08) | n/v | $0.3 / $0.9 | Premier (proprietary) | n/v |
| Magistral Medium/Small (reasoning line) | n/v | n/v | $2/$5 · $0.5/$1.5 | n/v | n/v |

(n/v = not verified on a vendor page this pass.) Naming quirk worth a beat:
**"Large 3" is older, smaller-priced and Apache; "Medium 3.5" is the newer
flagship** — the size words track a family axis, not a capability ranking.

Model-level facts:

- **Modalities:** Medium 3.5 and Large 3 are multimodal in (text + image),
  text out; Ministral 3 has *"text and vision capabilities"*. Small 4 is a
  *"hybrid model unifying instruct, reasoning, and coding."*
- **Reasoning:** `reasoning_effort` with values `"high"` (full thinking chunk
  before the answer) and `"none"` — on `mistral-small-latest` and
  `mistral-medium-3-5`. A two-position switch, not the five-level ladders
  elsewhere in this set.
- **Function calling** across the current line (Large 3, Medium 3.5, Small,
  Devstral, Codestral, Magistral, Ministral 3 — vendor's *"non-exhaustive"*
  list). **Structured outputs** two ways: custom JSON-schema (vendor-recommended)
  and plain JSON mode.
- **Max output caps: published on no model card fetched** — honest null.

## The specialist bench

*Source: vendor models overview + API pricing.* Priced by unit, not token:

- **OCR 4** (`ocr-4`) — $4/1k pages, $5/1k pages for Document AI, with
  *"paragraph-level bounding boxes and structural block labels"*. Premier.
- **Voxtral** audio family — Mini Transcribe 2 $0.003/min (Premier); Mini
  Transcribe **Realtime** $0.006/min (Apache 2.0); Voxtral Small $0.004/min
  (Apache 2.0); **Voxtral TTS** $0.016/1k chars with *"zero-shot voice cloning
  and multilingual support"* (CC BY-NC 4.0 — the NC matters: not for
  commercial self-hosting).
- **Embeddings** — Codestral Embed $0.15/1M, Mistral Embed $0.1/1M.
- **Leanstral 1.5** (Apache 2.0) — Lean/theorem-proving line, June 2026.

## Open weights, per model

The per-model license column above is the real capability fact: **Apache 2.0**
(Large 3, Small 4, Ministral 3, Voxtral Small + Realtime, Leanstral) means
unrestricted self-hosting including commercial; **Modified MIT** (Medium 3.5)
is near-equivalent; **Premier** (Codestral, OCR 4, Voxtral Mini Transcribe 2)
is API-only; **CC BY-NC** (Voxtral TTS) is weights-you-can't-sell-with. No
other provider in this set mixes licenses per model this finely — check the
column before planning a self-host.

## Retirements

*Source: vendor models overview.* Medium 3.1 retires **2026-08-31**; Small 3.2
retired 2026-07-31; Voxtral Mini Transcribe (v1) and Large 2.1 retired
2026-05-31.

## Consumer surface — Le Chat is now "Mistral Vibe"

*Source: [mistral.ai/products/le-chat](https://mistral.ai/products/le-chat) +
[pricing](https://mistral.ai/pricing), fetched 2026-08-04.* Rebranded, with
*"all your conversations, settings, and plans carry over."* Plans: Free · Pro
$14.99/mo · Team $24.99/user/mo · Education $5.99/mo · Enterprise. Vibe layers
agentic features the raw API doesn't have — deep research, *"100+ tool
integrations"*, async coding agents — over Medium 3.5, Small 4 and OCR 4.

## Weaknesses — relative, not absolute

Graded per [`README.md`](README.md): worse at, not incapable of.

- **256k context tops the line** — a quarter of the 1M-class windows elsewhere
  in this set. Steer, not stop: chunking and retrieval close the gap for most
  document work, and OCR 4 is per-page anyway.
- **Two-position reasoning control** gives less cost/depth tuning than
  five-level effort ladders. Not a limitation — pick the model size instead.

## Honest nulls

- Max output caps (no model card fetched publishes one); Ministral/Codestral/
  Devstral/Magistral context windows and release dates; Magistral's
  current-vs-legacy status (priced but absent from the featured list).
- The vendor changelog's year labels garbled under fetch; model-card dates
  were used wherever they conflicted.
- A "Medium 3.5 is a dense 128B model" claim circulates but appeared only in a
  search snippet — excluded, since the model card doesn't state it.
- Nothing here is measured in this estate yet.
