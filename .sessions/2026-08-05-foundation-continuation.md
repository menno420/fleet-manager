# 2026-08-05 · hub — review the session with Gemini, and set the next order of work

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-05 · venue: owner-live hub chat (owner asleep — autonomous close) ·
branch `claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: the review found the one thing this session measured and then
failed to interrogate — it recorded the owner's detection **precision** (7 of 7,
zero false positives) and never asked about his **recall**. His signals are all
exterior, so they only catch agents that fail *loudly*.

## Previous-session review

The three next-actions left earlier today are superseded. They were written
before the foundation problem was understood and before the owner explained that
he has never reviewed a repo or a PR, which changes what an instrument has to be.

## Scope

Owner-directed final task: review the whole session, run an adversarial Gemini
conversation on the load-bearing conclusions, land everything in fleet-manager
with explicit certainty labels, and emit a handoff prompt.

## What landed

- `docs/findings/2026-08-05-foundation-continuation.md` — the close-out: a
  certainty legend, the revised order of work, the false-negative gap, the
  salvaged purpose ledger, the gating correction, and honest nulls.
- `docs/CAPABILITIES.md` — the Gemini Interaction API recorded as a **shape, not
  a wall**: full request schema read from the discovery document, project not
  enrolled, owner console action.
- `docs/findings/README.md` — index row.
- A handoff prompt, written via `continuation-prompt` under its own §4b
  comprehension exception.

## Measured

**The Interaction API.** Exists only on Vertex `v1beta1` —
`interactions:create`, chained by `previousInteractionId` with `store: true`.
Read from the discovery document rather than guessed. This project is rejected
`400 RESOURCE_PROJECT_INVALID` on **both** the project ID and its number
`785901392159`, across `global`, `us-central1`, `us-east4`, `europe-west4`. The
AI Studio surface has no such method at `v1beta` or `v1alpha` (both fetched,
both 200). The uniformity across two identifiers and four regions is what makes
a preview allowlist the reading rather than a malformed request. Reviewed
multi-turn with client-side history instead — identical behaviour, costs tokens
not capability.

**The review corrected me twice and was itself wrong once.** It refuted the
purpose ledger as I framed it (the *why it is built that way* clause is
unfalsifiable to a non-coder) and refuted "wire every checker to a gate" (a
noisy heuristic gated hard makes an agent hallucinate fixes). It was wrong that
the dependabot deadlock was unfixed — that landed hours earlier.

**The gap neither of us had until asked directly:** this session measured the
owner's detection *precision* and never asked about his *recall*.

## Verification

- `python3 tools/check_no_false_walls.py --strict` → **exit 0**.
- `python3 bootstrap.py check --strict` → **exit 0**, run **post-commit**.
- Every state claim in the handoff prompt re-derived at HEAD via the direct
  path, because the local git proxy serves stale refs — that check caught a
  **stray branch I had created in the wrong clone** (`claude/fleet-superbot-…`
  in substrate-kit, local only, never pushed; deleted, clone returned to `main`).

**Honest nulls.** The review is one model over four turns, not a panel. The §4
instrument is designed and costed only by the reviewer's estimate — `UNVERIFIED`.
Whether removing advisory output from agent feedback is safe is reasoned, not
tested. And the false-negative rate the whole document turns on is
`NOT-VERIFIABLE` by construction.

## ⟲ Previous-session review

The three next-actions I left earlier today were aimed at the bot while the
instrument that would verify the bot did not exist, and they silently assumed a
reviewer who reads code. Both assumptions were available to check at the time —
the owner had already said he directs rather than reviews. The habit worth
carrying: **before proposing an order of work, ask who verifies each step and
whether that person can.**

## 💡 Session idea

**Give every findings doc a machine-readable certainty header.** This document
labels each claim by hand, which works exactly once — the labels are prose and
the next session may or may not honour them.

The durable form is a front-matter block a checker can read: which claims are
`MEASURED` and with what command, which are `UNVERIFIED`. Then
`check_stale_claims` could re-run the recorded commands and flag any `MEASURED`
line whose command no longer produces the recorded answer. It turns a certainty
label from an assertion into something that decays visibly — which is the one
property every stale claim in this estate has lacked.
