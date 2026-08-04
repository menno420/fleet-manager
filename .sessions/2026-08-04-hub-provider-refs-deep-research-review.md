# 2026-08-04 · hub — reviewing an external Deep Research report against the provider set

> **Status:** `complete`

- **📊 Model:** fable-5 · high · research — cross-validate external report, verify, fold in

Time: 2026-08-04 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1` (restarted from main post-#708)

💡 Session idea: **an external report over the same ground is a free adversarial
review — but only after per-claim verification, because its errors arrive in the
same confident prose as its facts.** The owner ran ChatGPT Deep Research on the
provider-capability task and handed over the output. Where it overlapped the
vendor-sourced set it agreed on every checked fact, which corroborates both;
where it went further, each specific claim was re-verified against the vendor
page before anything entered the repo. The one place it was wrong in detail
(a Gemini output price) and the one place it was materially behind (the OpenAI
fine-tuning wind-down had a harder deadline than it implied) were both exactly
the volatile-fact classes README rule 4 predicts.

## previous-session review

`2026-08-04-hub-provider-capability-reference.md` (PR #708, merged) shipped the
broadened set and closed on the coverage call: Copilot, Grok, DeepSeek,
Mistral, Meta — Cohere et al. deferred. This session, the deferred provider
arrived with owner-supplied research attached, which is the cheapest possible
way for a deferred item to come due.

## Scope

Owner: review the attached Deep Research report, extract anything useful,
verify anything uncertain. Also: automode disabled, so land the telemetry
commit stranded by the previous session's classifier denials.

## The review verdict on the report

Where it overlapped the vendor-sourced set (Claude dates/specs, GPT-5.6 sol
figures, Llama 4, Mistral dates, Sonnet 5 intro pricing) it agreed on every
checked fact — mutual corroboration. Errors found under verification, both in
the volatile classes README rule 4 predicts: Gemini 3.6 Flash output price
(page says $7.50; report's tables didn't carry it and its 3.5 figure invited
the wrong inference), and the fine-tuning wind-down stated softer than the
vendor page's actual deadlines. Its Cohere pricing ($2.50/$10) could not be
verified on a vendor page and was NOT recorded. Its Stability/Falcon/MPT
sections are accurate-looking but estate-irrelevant; skipped, not folded.

## What landed

- **`cohere.md`** — new provider file, every folded claim re-verified on
  docs.cohere.com: Command A+ (2026-05-20, 218B/25B MoE, 128k/64k, Apache 2.0,
  48 languages, stated GPU minimums), the context-vs-output trade inside the
  Command line (A: 256k/8k vs A+: 128k/64k), Embed v4.0 taking whole PDFs.
- **`chatgpt.md`** — the fine-tuning wind-down, verified on the vendor
  deprecations page and harder than the report implied: new-org access already
  closed, existing customers lose new jobs 2027-01-06, Evals/Agent Builder
  shut down 2026-11-30.
- **`gemini.md`** — verified API pricing table and the free-tier-trains /
  paid-tier-doesn't split, quoted verbatim.
- **Stranded telemetry landed** — the guard-fires delta blocked by the
  previous session's classifier denials rides in this PR after the owner
  disabled automode.

## Honest nulls

- Cohere per-token pricing and Command A's parameter count: absent from the
  fetched vendor pages, so recorded as nulls even though the report carries
  figures.
- Gemini 3.1 Pro API pricing was not in the fetched table.
- The report's privacy/retention dimension (data-use-for-training per
  provider) is broader than what was folded — only the verified Gemini split
  entered; a per-provider retention pass remains open work.
- Stability AI, Falcon, MPT, Hugging Face, Azure-as-a-layer: reviewed,
  deliberately not folded — estate relevance too low to carry maintenance
  weight. Revisit if the estate starts generating media or self-hosting.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
