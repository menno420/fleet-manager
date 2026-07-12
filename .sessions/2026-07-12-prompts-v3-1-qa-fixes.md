# 2026-07-12 — Prompts v3.1: apply QA fixes (boot-sim, incident-replay, question-rounds)

> **Status:** `in-progress`

📊 Model: fable-5 · finalize worker dispatched by coordinator (Wave 4, owner-directed overnight rebuild) · start 2026-07-12 (born-red at open)

## Declared at open (born-red)

Build prompts v3.1 on `claude/prompts-v3-1`: apply every required fix from the
three QA audits (#100 incident-replay, #101 question-rounds, #102 boot-sim) to
the v3.0 set in `docs/prompts/v3/` (PR #98 @ 8056b7e), regenerate all 8 B files
from the fixed A, recount every char budget (fitted ≤7,500 / hard 8,000), and
park the PR READY+green for coordinator confirmation.
