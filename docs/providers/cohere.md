# Cohere — provider capability reference

> **Status:** `living-ledger`
>
> The Command generation models, the Embed/Rerank retrieval stack, and the
> licensing. **Derived 2026-08-04 from Cohere's own docs
> ([docs.cohere.com](https://docs.cohere.com/docs/models))**, prompted by an
> owner-supplied Deep Research report whose Cohere claims were verified
> per-claim against those pages before entering this file.
> **Not a routing table** — see [`README.md`](README.md).

## What this provider is, concretely

The enterprise-retrieval specialist: first-party **Embed and Rerank** models
alongside the Command chat line, aimed at RAG, citations, multilingual business
use and private deployment. Its 2026 flagship ships **Apache 2.0 open weights**
at frontier-adjacent size — the same posture as Mistral, from a
retrieval-first angle.

## Models

*Source: vendor docs (models page + Command A+ page, fetched 2026-08-04).*

| Model | ID | Context | Max output | Modalities |
|---|---|---|---|---|
| **Command A+** | `command-a-plus-05-2026` | 128k | 64k | text + image in → text |
| Command A | `command-a-03-2025` | 256k | 8k | text |
| Command R+ | `command-r-plus-08-2024` | 128k | 4k | text |
| Embed v4.0 | `embed-v4.0` | 128k | — | text, images, *"mixed texts/images (i.e. PDFs)"* |
| Rerank v4.0 Pro / Fast | `rerank-v4.0-{pro,fast}` | 32k | — | text |

Note the shape: the **older Command A carries the larger context (256k) but an
8k output cap; the newer A+ trades context down to 128k for a 64k output** —
a long-report generation job and a long-document reading job pick different
models here.

Command A+ facts, verified on the vendor page:

- Released **2026-05-20**; sparse MoE, *"218B total, 25B active"* parameters.
- *"48 languages, including all of the official European Union languages."*
- **Apache 2.0, weights downloadable on Hugging Face** — frontier-adjacent
  open weights with no user-count clause (contrast the Llama license).
- Runs on *"1× B200 at W4A4 or 2× H100s at W4A4"* — the only provider in this
  set that states a minimum self-host GPU configuration on the model page.
- Reasoning via a `thinking` operation with token budgets (vendor's dedicated
  Reasoning guide).
- Embed v4.0's 128k context takes whole PDFs as mixed text+image input — a
  retrieval-side capability the general-purpose providers don't match
  first-party.

Per-token pricing is **not published on the models pages fetched** — honest
null; the owner-supplied report carried figures (Command A $2.50/$10) that
could not be verified on a vendor page this pass, so they are not recorded as
fact.

## Weaknesses — relative, not absolute

Graded per [`README.md`](README.md): worse at, not incapable of.

- **No generation stack** (image/video/audio out) and text-only output — like
  DeepSeek, anything visual is read, not made.
- **Specialist ecosystem:** strongest when the job is retrieval-shaped;
  general agentic work has more tooling on the bigger platforms. Steer, not
  stop — the API supports tools and reasoning.

## Honest nulls

- Per-token pricing (absent from the fetched vendor pages).
- Command A parameter count (the report says 111B; not verified on a vendor
  page this pass).
- Consumer surface, if any, and SaaS data-retention terms.
- Nothing here is measured in this estate yet.
