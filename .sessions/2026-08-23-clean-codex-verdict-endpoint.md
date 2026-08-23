# 2026-08-23 — A clean Codex verdict is an issue comment, and I wrote "no review arrived" because I never read that endpoint

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

fm #924's card, now on `main`, states: *"No review had arrived by 11:44:48Z —
~24 minutes."* **That is false, and it is my query that was wrong, not the relay.**

`MEASURED` 2026-08-23:

| endpoint | returns for fm #924 |
|---|---|
| `GET /pulls/924/reviews` — what I polled | **0** |
| `GET /issues/924/comments` — what I never read | `chatgpt-codex-connector[bot]` at **`2026-08-23T11:23:57Z`**: *"Codex Review: Didn't find any major issues."* |

So the review answered in **~3 minutes**, comfortably inside the measured ~335 s
relay, and the PR I described as landing unreviewed had in fact **passed review
clean** before it merged.

**The mechanism — and the estate had already written it down, which is the actual
finding.** I first framed this as *"the missing half"* of the inline-comments
fact. **That was false, and Codex caught it on this PR.** `CAPABILITIES.md`
carries a full canonical section, *"Codex's CLEAN verdict is an issue comment"*,
written **2026-08-22 from websites #511 — the day before**. It has everything:
the endpoint, the `Reviewed commit:` SHA-matching requirement I omitted, the
filter-by-Codex-login trap, and its own note that it *"cost a session ten minutes
today."*

**So the estate diagnosed this yesterday and it still cost me 24 minutes and a
false claim in a committed card.** `MEASURED`: **no route delivered it.** Probed
before fixing — `pulls/{n}/reviews`, `issues/{n}/comments` and `@codex review`
all returned *silent*. A document that exists and is delivered by nothing is the
exact defect this session's own D3 work was about, and I became its fourth
instance today.

**Fixed as a mechanism, not a fourth statement:** route `codex-verdict-poll` now
fires on any of the three polling calls and carries the SHA-matching and
login-filter requirements. It fired on my own next command while writing this.

**This is the estate's own named failure, in its milder form.** The boot file
records a session that *"waited 150 s, wrote 'no review appeared' into a public
comment as if that were evidence, and merged three minutes before four real
findings landed."* I waited 24 minutes and wrote it into a committed card. The
outcome was benign — the verdict was clean — but **absence of evidence recorded
as evidence of absence is TRAP-003**, and I committed it while the register that
names it sits in the same tree.

## Previous-session review

⟲ fm **#924** (`53bbfff`) — the telemetry delta, merged; its card carries the
false claim corrected here. Checked at `main`: `check --strict` exit 0,
`check_doc_routes --strict` exit 0, telemetry 21,741 lines / 0 unparseable /
0 conflict markers, and **0 open PRs** in fleet-manager or websites.

## What is about to happen

Correct #924's card at its site, and add the clean-verdict endpoint to the
capability ledger beside the inline-comments fact it completes.

## Verify

- **The correction is measured, both endpoints, same PR:**
  `GET /pulls/924/reviews` → **0** · `GET /pulls/924/comments` → **0** ·
  `GET /issues/924/comments` → `chatgpt-codex-connector[bot]` at
  **`2026-08-23T11:23:57Z`**, *"Didn't find any major issues."*
- #924's card is corrected **at its site**, with the false claim preserved under
  a banner rather than rewritten — the estate's own defect class is *an appended
  correction that leaves the wrong sentence reading as current*, so the retraction
  sits above the text it retracts.
- **No new ledger prose.** My first attempt duplicated the canonical section,
  worse — it omitted the SHA match, so a stale clean verdict from an earlier head
  would read as covering the current one (Codex, P1). Replaced with a **pointer**
  at the inline-comments line, and the canonical section's `n=1` caveat updated
  to **observed twice** (websites #511, fm #924).
- `tools/check_doc_routes.py --strict` → **exit 0**, 62 routes · 31 docs · 0 errors;
  the new route's patterns match the doc's own `{n}` notation *and* live calls, so
  its coverage is proved rather than asserted.
- `python3 bootstrap.py check --strict` → **exit 0** at the flip (real exit code,
  redirected never piped — TRAP-002); `tools/check_doc_routes.py --strict` → exit 0.

## What this costs and what it buys

The outcome was benign: #924 passed clean, so nothing unreviewed reached `main`.
What was wrong is the **record** — and on a day whose entire product was a record
going to a third party, a false claim about verification is the expensive kind.

**The one-sentence version:** I polled two endpoints, a clean verdict lands on a
third, and I wrote the absence down as a fact — while the ledger had said so
since yesterday and nothing delivered it.

## Layer-2 handoff

`null` — fleet-manager itself; no satellite repo attached.
