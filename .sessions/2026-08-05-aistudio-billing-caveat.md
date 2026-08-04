# 2026-08-05 · hub — the paid-key caveat on AI Studio's free usage

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only — one conditional added to a
  recommendation

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1`

💡 Session idea: **a true claim with a false citation still has to be
re-sourced, and it takes one fetch.** An owner-shared Gemini answer quoted
Google's billing FAQ correctly but cited `ai-navigate-news.com` — an aggregator
— as "the official FAQ". The temptation is to accept it (the text was
verbatim-accurate) or to reject it (the provenance was wrong). Both are
guesses. The fetch that settles it costs one call, and it upgraded the claim
from *plausible* to *Google-sourced* — which is exactly the difference between
a steer and a fact this estate is built on.

## previous-session review

`2026-08-05-gemini-quotas-and-interactions.md` (PR #731, merged) recorded that
AI Studio use does not spend API quota. True, and incomplete: it holds only
while no paid key is linked.

## What landed

- `docs/providers/gemini.md` — the conditional on Studio's free usage, sourced
  from Google's own billing page, plus the note that the free/paid split is a
  per-project switch rather than a one-way door.

## The correction to the recommendation

I told the owner that a $10 prepay buys the data-use boundary (paid tiers do
not train on prompts). That is still true, and now carries a cost I had not
stated: **linking that paid key in AI Studio makes his Studio usage billable
too.** Verbatim from
[Google's billing FAQ](https://ai.google.dev/gemini-api/docs/billing): *"AI
Studio usage remains free of charge unless users link a paid API key for access
to paid features."* The FAQ also notes projects can be switched between tiers as
needed, so the free Studio surface survives if the paid key stays unlinked
there.

## Honest nulls

- **What counts as "linking" is untested** — whether merely holding a paid key
  in the same project bills Studio use, or only selecting it in a Studio
  session, is not established here.
- The owner-shared answer that raised this cited an aggregator, not Google;
  the text was accurate but was re-sourced before being recorded.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
