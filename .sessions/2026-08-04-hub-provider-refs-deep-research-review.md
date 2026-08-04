# 2026-08-04 · hub — reviewing an external Deep Research report against the provider set

> **Status:** `in-progress`

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

## What landed

*(written at close)*

## Honest nulls

*(written at close)*

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
