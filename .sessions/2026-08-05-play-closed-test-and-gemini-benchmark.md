# 2026-08-05 · hub — the tool decided, not the model

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · research + build — closed-test path, Gemini benchmark

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/swingy-spider-play-submission-wno3nb`

💡 Session idea: **the same model, the same key, the same day, gave opposite
answers to the same question — and the difference was which tool it used.**
Asked how many testers Play requires, `google_search` grounding said **12** and
volunteered that it had been reduced from 20. `url_context`, pointed at the very
page that says 12, failed to retrieve it, answered **20** from training data, and
prefaced it with *"Based on the Google Play support page."* Nothing in the prose
marked the difference. The retrieval-status field did.

## previous-session review

`2026-08-05-play-submission-requirements.md` (PR #743, merged) recorded the Play
requirements with fetched sources and filed six `OQ-PLAY-*` items. The owner then
supplied three corrections that reshaped the plan: the developer account is
already created and paid; the game **does** retain run data; and leaderboards will
eventually send data off device. He also directed this benchmark.

## What landed

- `docs/findings/2026-08-05-gemini-url-accuracy-benchmark.md` — the ten-URL
  measurement, scored against pages fetched by hand first.
- `docs/providers/gemini.md` — `url_context` row corrected: it is host-dependent.
- `docs/owner-queue.md` — `OQ-PLAY-ACCOUNT` closed; `OQ-PLAY-LISTING` promoted to
  the critical path; `OQ-PLAY-CLOSED-TEST` corrected on two counts.
- `menno420/spider-swing` PR #163 — privacy policy draft, Console answer sheet,
  listing copy, closed-test runbook, upload-key script.

## Measured

[[fill: measured]]

## Verification

[[fill: verification]]
