# Review queue — needs-second-review ledger (post-merge)

> **Status:** `living-ledger`
>
> Created by owner directive 2026-07-09, as part of the gen-2
> merge-authority policy ([`gen2-blueprint.md`](gen2-blueprint.md) §1/§2):
> **no PR ever waits for review before landing.** A PR that deserves second
> eyes is merged anyway and flagged HERE (and/or gets an @codex mention on
> its thread). Review is **post-merge**; veto = revert (forward-only git).
>
> **BINDING — auto-append rule (ORDER 003, 2026-07-10, program-review §5.2):**
> every PR that adds **more than 50 changed lines of runtime/product code**
> (excluding `docs/`, `control/`, `.sessions/`, and pure test additions) OR
> that carries **any self-flagged risk** (a ⚑ flag on its session card, or
> "risky" in the PR body) **MUST get a row here** —
> `repo#N · what to re-check · why-risky · status` — **appended by its own
> session before close.** This is not optional hygiene: the post-merge-review
> law is what the no-pre-merge-review policy rests on, and 116 merged PRs /
> zero rows was the state that voided it (program-review §5.2 — the queue was
> the safety valve that justified "no pre-merge review").
> *Why N=50 (decide-and-flag — the owner may re-tune):* 50 changed lines of
> runtime/product code reliably catches real logic changes (a new code path,
> a schema, a state machine) while skipping the heartbeat/status/card/docs
> churn that dominates fleet PR volume — the overnight record shows heartbeat
> PRs run 10–30 lines and real feature PRs run well past 50. A lower N drowns
> the queue in ceremony rows nobody drains; a higher N lets exactly the
> mid-size logic changes through that the night-review caught defects in.

## Standing drainer (named per ORDER 003 — two-tier)

- **PRIMARY — @codex post-merge review** (owner directive Q-0258 + Q-0259
  ruling 3, 2026-07-10): on repos with the Codex GitHub integration enabled,
  the row's own session (or the manager at the next wake batch) posts **one
  specific question** as a PR comment mentioning **@codex** on the merged
  head — template pointer: superbot
  `docs/planning/codex-review-integration-plan-2026-06-17.md` Part C.
  **Q-0120 governs the return path: Codex's answer is input to verify
  against shipped source, never an order** — check each specific before
  acting, then strike or escalate the row.
- **FALLBACK — the manager's failsafe-wake batches** drain rows for repos
  **without** Codex. Currently that includes **fleet-manager itself** — the
  Codex env for this repo was never created (env-creation ask parked on
  PR #26); superbot-next is Codex-proven, superbot shows live Codex
  evidence (codex-labeled PR #1917), and every other repo's availability is
  **unknown until probed** (marked per row below).
- **Cadence:** every manager wake batch reviews new rows. A row **older than
  48h unread** becomes an escalation line in the `control/status.md`
  heartbeat.

## How to use

- **Any lane, any session** appends one line per merged PR that deserves a
  second look (and MUST for rows meeting the binding rule above):
  `repo#N · what to re-check · why-risky · status`.
- **Reviewer** (Codex, another lane, the owner, a later session) checks the
  item, then either strikes the line (`~~…~~ — reviewed <date>, ok`) or
  ships/queues the revert with a one-line verdict.
- Append-only per line; never rewrite others' open entries (playbook R9).
- This ledger is for *quality* second-eyes. Safety brakes (irreversible /
  external / production actions) are unchanged and pre-merge as ever.

## Open items

First drain pass — BACKFILL (ORDER 003, 2026-07-10): the highest-risk
overnight/day PRs fleet-wide, selected from the gen-2 launch record
([`planning/gen2-launch-record-2026-07-10.md`](planning/gen2-launch-record-2026-07-10.md)),
the night review
([`findings/night-review-2026-07-10.md`](findings/night-review-2026-07-10.md)),
and the economics ledger
([`findings/fleet-economics-2026-07.md`](findings/fleet-economics-2026-07.md)).
Drain path per row: **codex** = post an @codex question on the merged head;
**manager** = manager failsafe-wake batch; **codex?** = Codex availability
unknown on that repo — probe once, else manager batch.

| PR | What to re-check | Why-risky | Drain path · status |
|---|---|---|---|
| venture-lab#9 | The $49 product's real-Stripe checkout→grant path (products/Stripe-path class) | Night-review D1/Q2: headline path **never executed against real Stripe**; live events carry `customer_email: null` which the grant code (app.py ln 253–257) refuses, and the success URL uses `{CHECKOUT_EMAIL}`, a placeholder Stripe doesn't substitute — near-certain first-purchase failure; ⚑B/⚑D publish clicks frozen on it; already flagged by night-review as the fleet's worst truth-boundary miss | codex? · **open** — re-check = verify the P0 fix ORDER actually landed the real-path fix + non-author verification (R23) |
| superbot-games#16 | The substrate-gate pytest step's actual collection scope | Night-review Q7 verdict 1: "CI now gates the suite" is **FALSE as stated** — `pytest tests/ -q` collects 73 of 121; exploration's 48 under `games/exploration/tests/` are invisible and the card's own arithmetic papered over it; one-line fix identified (`.github/workflows/substrate-gate.yml:62`) | codex? · **open** — re-check = confirm ORDER 001 (P0 CI-collection) fixed scope to 121/121 |
| superbot-games#5 | The 18-module pure-domain mining port (merged 00:00:58Z) | Largest games runtime diff of the night; it unblocked the merged games-plugins lane, so a latent port defect propagates into the successor lane; measured tests exist but no non-author eyes have read the port itself (launch record §1/§2) | codex? · **open** |
| trading-strategy#21 | P2 verdicts for all 14 candidates, incl. the AAPL-donchian PROMOTION | Night-review Q3: the promotion rule had **no significance bar** — the promoted edge is +0.079 Sharpe against SE ≈0.19 (~0.4 standard errors, deep in noise) and the founding plan's own "prefer deflated Sharpe" was computed nowhere in the repo; two P1 candidates dropped with no stated rule | codex? · **open** |
| trading-strategy#36 | ORDER 007's promotion-significance bar (deflated Sharpe) + AAPL-donchian re-grade | The bar's *implementation* is the thing that now gates the **one-shot holdout** (ORDER 008 unlock granted, Q-0262.2) — a wrong bar spends the repo's single most valuable pre-registered asset on a candidate its own P4 evidence (13/13 transfer-FAIL) argues against; verify before the holdout session runs | codex? · **open** — time-sensitive: drain before the dedicated holdout session |
| superbot#1920 | The `check_baseview_inheritance` semantics change (checker now respects justifying comments) + the dashboard.json contract slice | Biggest diff of superbot's overnight band (960+/92−, 20 files); it changes an **enforcement surface** — night-review verified the raw-inventory ratchet held (Q7 verdict 5), but the comment-recognition semantics themselves never got non-author eyes. Band note (honest finding): the overnight band #1915–#1925 contained **zero `disbot/` runtime PRs** — the only `disbot/` touch was #1917, a one-line Codex docstring — so this tooling PR is the band's genuine max-risk item | **codex** (superbot Codex LIVE — evidence: codex-labeled #1917) · **open** |
| pokemon-mod-lab#8 | QoL+ increment 5 — chain head of the overnight #4–#8 engine-patch train | Five merged engine-patch PRs (12+ patches) whose feel verdict is **entirely unplaytested** (night-review Q4: "no plan today, only a queue slot"), and the ROM sha1-chain / byte-identity claims are lane-attested, not CI-checked (night-review Q9 item 2) | codex? · **open** — feel half is owner-playtest, code half drainable |
| gba-homebrew#12 | Lumen Drift increment 3 (concept scope complete) — merged on compile-only per-PR CI | Night-review Q9 item 1: the gameplay HUD asserts exist only at dispatch tier (#13); per-PR CI is compile-only, so a gameplay regression merges on a green compile; the lane also runs the fleet's hottest CI-per-PR ratio (economics ledger: 4.1 runs/PR) | codex? · **open** |

## Reviewed / closed items

*(move rows here with the verdict + date)*
