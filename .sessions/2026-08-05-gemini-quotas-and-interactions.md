# 2026-08-05 · hub — the real Gemini quotas, and a correction

> **Status:** `complete`

- **📊 Model:** opus-5 · high · research — owner-supplied dashboard + docs,
  probed against the API

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1`

💡 Session idea: **the owner's screen was a better instrument than my probe.**
I was burning requests in paced waves to find a daily ceiling by exhaustion;
his AI Studio dashboard states every ceiling outright, and its footnote answered
a question I had no way to probe at all (whether Studio use spends API quota).
The probe was stopped mid-run once the better instrument arrived — which is the
correct move, not a wasted effort, but it is worth naming the reflex: **check
whether the number is already displayed somewhere before measuring it by
consumption.**

## previous-session review

`2026-08-05-gemini-surface-probe.md` (PR #729, merged) recorded the API surface
from probes alone. Two of its claims are corrected here — one was incomplete,
one was wrong — which is why this card exists rather than a quiet edit.

## Corrections to the record

1. **"Multi-turn is stateless — history is resent every call" was true only of
   `generateContent`.** The newer **Interactions API**
   (`POST /v1beta/interactions`) stores conversation state server-side and is
   reachable on this free key: measured A/B — turn 2 with
   `previous_interaction_id` recalled the number, turn 3 without it answered
   *"You have not provided a number for me to remember in this conversation."*
   Retention is **1 day free / 55 days paid**, opt-out via `store=false`. So
   "the API keeps nothing" was wrong as a general claim.
2. **The daily cap's number is now known, not just its metric name:** 20 for
   `gemini-3.6-flash`. Probing by exhaustion also over-attributed the binding
   constraint to tokens; on the flagship free model the binding constraint is
   **requests**.

## The ceilings — owner's AI Studio dashboard, read directly

| Model | RPM | TPM | RPD |
|---|---|---|---|
| Gemini 3.6 Flash | 5 | 250K | **20** |
| Gemini 3.1 / 3.5 Flash Lite | 15 | 250K | **500** |
| Gemini 2.5 Flash | 5 | 250K | 20 |
| Embedding 1 / 2 | 100 | 30K | 1K |
| Live API (3 Flash Live, 3.5 Live Translate) | unlimited | 65K / 20K | unlimited |
| Map grounding | — | — | 500 |
| Search grounding | — | — | **not served** |

Agreement between instruments: the dashboard shows `3.6 Flash` at **20/20 RPD**
and `3.1 Flash Lite` at **15/15 RPM** — exactly the two ceilings this estate hit
by probe, independently.

## Studio use does NOT spend API quota

Verbatim from the dashboard footnote: *"Usage information displayed is for the
API and does not reflect AI Studio usage, which is offered free of charge (when
no API key is selected)."* Also: *"Usage data may take up to 15 minutes to
update"* — which explains a counter that lagged this session's burst.

## Honest nulls

- **The lite daily ceiling was never reached by probe** — stopped at ~196
  requests when the dashboard supplied 500. Measured lower bound: >196.
  Dashboard-stated: 500. Those agree but are not the same evidence.
- The Interactions API was tested for continuation only. Background execution,
  agent mixing, and retention configuration are unprobed.
- Dashboard figures are **peak usage over 28 days**, read from a screen
  recording, not from an API.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
