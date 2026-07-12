# 2026-07-12 — ORDER 014 cross-check: kit hardening input vs shipped prompts v3.1

> **Status:** `complete`

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

## Shipped (close-out)

Appended the "v3.1 KNOWN DEFECTS queue — ORDER 014 cross-check (v3.2 input)"
section to `docs/prompts/v3/per-project/README.md` (commit e8af353, PR #107).
Verdict tally, every line verified against the shipped tree at dbd8cdc:

- **§(c): 5 checked, 0 real v3.1 defects.** All five corrections (retired
  trigger/session ids · meta.md stale counts · coordinator-prompt staleness ·
  lab-loop self-arm claim · model/env-id display anomaly) audited the LEGACY
  prompts (`projects/substrate-kit/` @ e801da5c); the v3.1 rebuild already
  states the corrected facts — each entry records the evidence line
  (e.g. `custom-instructions-core.md:81` bans baked trigger ids;
  `:45` mandates family-level model names). §(c)6 (instructions.md v2) had
  no wrong facts per the kit itself.
- **§(a)/(b): 3 genuine gaps queued** — (7) fresh-session-per-fire binding
  rule absent + A step 4's generic BUSINESS-cron rebind text conflicts with
  it (P2); (8) heartbeat `kit:` exact line grammar / bold-form negative
  example / adopters.md deference not prompt-carried (P2); (9) stale-MCP-
  PR-read cross-check not explicit in TOOL FACTS (P3). All other §(a)
  classes and §(b) rows verified covered, cited file@line; the §b ❌ rows
  are kit-template graduation work (Self Improvement lane), not v3.1
  defects.

## 💡 Session idea

The queue-append pattern would be cheaper to verify if `regen_b_files.py`
also emitted a machine-readable fact index (trigger ids, counts, SHAs baked
into any prompt artifact) — a cross-check like this one becomes one diff of
two fact lists instead of a hand grep per claim.

## ⟲ Previous-session review

The v3.1 build (PR #103 + codex fixes) held up remarkably under an
adversarial cross-check: zero of the kit's five stated-wrongly facts survived
into v3.1 — the "no baked ids / verify-at-boot" design rules did exactly
their job. Improvement: the one place a wrong generic rule slipped through
(BUSINESS-cron rebind vs fresh-session loops, entry 7) is a rule the QA
passes never exercised because only one live instance exists — future QA
should include a "one instance of each trigger-binding kind" replay.
