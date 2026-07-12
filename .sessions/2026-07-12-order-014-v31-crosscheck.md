# 2026-07-12 — ORDER 014 cross-check: kit hardening input vs shipped prompts v3.1

> **Status:** `in-progress`

📊 Model: Claude (Fable family, fable-5) · start 2026-07-12T06:57Z · lane
worker (dispatched) — coordinator-assigned slice, no control/status.md write.

## Declared at open (born-red)

Verify every claim in substrate-kit's ORDER 014 deliverable
(`docs/reports/2026-07-12-prompt-template-hardening-input.md` @ 8a544a6, kit
PR #256) against the shipped v3.1 prompt artifacts (`docs/prompts/v3/`,
PR #103 + codex fixes): each §(c) "fleet states this wrongly" item gets a
verdict quoted from the shipped files (real defect vs already-correct), and
§(a)/(b) doctrine items are mapped to v3.1 coverage. Verified deltas are
appended to the known-defects queue in `docs/prompts/v3/per-project/README.md`
(queue-only — no prompt artifact is edited). Claim:
`control/claims/claude-order-014-v31-crosscheck.md` (removed at the flip).
