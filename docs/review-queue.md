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

**First drain pass executed 2026-07-10 (chain slice #3):** superbot#1920 drained
to @codex (the only Codex-enabled row; one R24 question, response pending);
venture-lab#9 manager-verified (D1 defect confirmed at HEAD — verdict on the
row); trading#36 urgency annotation (holdout already spent — ordinary drain now).
Remaining codex? rows await either a Codex probe on their repos or the next
manager batch.

**Groom pass 2026-07-10T22:5xZ (chain slice #4):** every remaining open row's PR
re-validated live (all exist + merged; `head <sha> · merged <time>Z` stamp added
per row); superbot#1920's @codex drain came back **quota-blocked** (verdict on
the row — manager ground truth banked for the websites half); venture-lab#9
re-checked — lane HEAD still `7558cb2`, fix NOT landed, row stays open.
**Recommended NEXT manager-verify candidate: superbot-games#16** — its ORDER 001
(P0 CI-collection fix) is still unexecuted, so the verify has a crisp binary
outcome (gate collects 121/121, or it still doesn't → escalate the unconsumed
ORDER). Recommendation only; not executed this slice.

**Manager-verify pass 2026-07-10T23:1xZ (chain slice #5):** superbot-games#16
executed as recommended — **CONFIRMED-STILL-BROKEN** at repo HEAD `b134961`
(verdict + the corrected fix target on the row: the kit upgrade #22 relocated the
pytest step to `.github/workflows/tests.yml`, so the original `substrate-gate.yml:62`
pointer is stale). sb#1920 re-checked same slice: **no new @codex comment** (thread
still ends at the 22:03:53Z quota refusal — refusals don't count as drain); no
annotation added.

| PR | What to re-check | Why-risky | Drain path · status |
|---|---|---|---|
| venture-lab#9 | The $49 product's real-Stripe checkout→grant path (products/Stripe-path class) | Night-review D1/Q2: headline path **never executed against real Stripe**; live events carry `customer_email: null` which the grant code (app.py ln 253–257) refuses, and the success URL uses `{CHECKOUT_EMAIL}`, a placeholder Stripe doesn't substitute — near-certain first-purchase failure; ⚑B/⚑D publish clicks frozen on it; already flagged by night-review as the fleet's worst truth-boundary miss | **manager-verified 2026-07-10 (first drain pass) — D1 DEFECT CONFIRMED AT HEAD `ce22315`, fix NOT landed (ORDER 003 unconsumed); row stays open until the fix PR merges.** Confirmed by code (`candidates/membership-kit/server/app.py`, blob `b52e7d6`): (1) `handle_purchase_event` reads ONLY `data.object.customer_email` and refuses on null — and `/create-checkout-session` calls `stripe.checkout.Session.create` **without** `customer_email`/`customer_creation`, so every real event arrives with `customer_email: null` (buyer's email lives in `customer_details.email`, never read); (2) worse than flagged: the refusal still returns **HTTP 200** (`granted: false`), so Stripe marks the webhook delivered and never retries — paid buyer, no grant, no retry, no alarm; (3) `success_url="http://localhost:8000/members?email={CHECKOUT_EMAIL}"` — Stripe substitutes only `{CHECKOUT_SESSION_ID}`, so the literal string 402s the buyer post-payment, and the host is hardcoded localhost; (4) all 13 tests build events via `_checkout_event()` which always sets `customer_email` — zero real-shape fixtures. **ORDER 003's fix must cover:** read `customer_details.email` with `customer_email` fallback (or set `customer_email` at session create); return non-2xx on an ungrantable completed-checkout so Stripe retries; success_url → `{CHECKOUT_SESSION_ID}` + server-side email resolve + env-configurable base URL; add a real-shape event fixture; R23 non-author verify + the ⚑A test-mode E2E stay the final gate. Groomed slice #4 (2026-07-10T22:5xZ): lane HEAD still `7558cb2` — fix NOT landed (ORDER 003 still unconsumed; no lane session has run, the boot click stays the unblock); row stays open |
| superbot-games#16 | The substrate-gate pytest step's actual collection scope | Night-review Q7 verdict 1: "CI now gates the suite" is **FALSE as stated** — `pytest tests/ -q` collects 73 of 121; exploration's 48 under `games/exploration/tests/` are invisible and the card's own arithmetic papered over it; one-line fix identified (`.github/workflows/substrate-gate.yml:62`) | codex? · **open** — re-check = confirm ORDER 001 (P0 CI-collection) fixed scope to 121/121. Groomed slice #4: link/head valid (head `5c71c61` · merged 2026-07-10T00:58:58Z). **MANAGER-VERIFIED 2026-07-10T23:1xZ (chain slice #5) — CONFIRMED-STILL-BROKEN at repo HEAD `b134961`:** the pytest step still runs `python3 -m pytest tests/ -q` and **ORDER 001 (filed `099664c`, 12:47Z) has NOT been executed by any commit since `4493292`** (the only commits since are kit upgrades #22/#23). Collection scope re-confirmed by tree at HEAD: `tests/` contains ONLY `tests/mining/`, while exploration's 7 test files sit under `games/exploration/tests/` — invisible to the gate. **Precision — the row's fix pointer is STALE:** the v1.2.0→v1.7.0 kit upgrade (#22 @ `4493292`) relocated the pytest step verbatim out of the kit-owned `substrate-gate.yml` into the host carve-out **`.github/workflows/tests.yml`** (blob `09b65f4` at HEAD) — ORDER 001's one-line fix now targets THAT file: widen collection to ALL suites (e.g. `python3 -m pytest tests/ games/ -q` or rootdir-wide) **+ the count assertion** so silent scope loss fails red. Escalation: the P0 ORDER is unconsumed because the repo has NO trigger and both gen-1 lanes are archived — consumption rides the gen-2 boot (Q-0267 owner react, owner-queue item 14). Row stays open until the fix PR merges; sequence superbot-games#5's drain knowing the gate does NOT yet re-run the full suite |
| superbot-games#5 | The 18-module pure-domain mining port (merged 00:00:58Z) | Largest games runtime diff of the night; it unblocked the merged games-plugins lane, so a latent port defect propagates into the successor lane; measured tests exist but no non-author eyes have read the port itself (launch record §1/§2) | codex? · **open** — groomed slice #4: link/head valid (head `33808dd` · merged 2026-07-10T00:00:58Z). Drain path where missing: no Codex probe on superbot-games yet → manager batch; sequence AFTER the #16 CI-collection verdict (a fixed gate re-runs the full 121-test suite on every PR, which is the cheapest standing check on this port; the manager read is then the verbatim-port claim vs the oracle) |
| trading-strategy#21 | P2 verdicts for all 14 candidates, incl. the AAPL-donchian PROMOTION | Night-review Q3: the promotion rule had **no significance bar** — the promoted edge is +0.079 Sharpe against SE ≈0.19 (~0.4 standard errors, deep in noise) and the founding plan's own "prefer deflated Sharpe" was computed nowhere in the repo; two P1 candidates dropped with no stated rule | codex? · **open** — groomed slice #4: link/head valid (head `ce00a83` · merged 2026-07-10T03:40:35Z). Drain path where missing: no Codex probe on trading-strategy yet → manager batch; note the row is PARTLY SUBSUMED by trading#36 (ORDER 007 demoted the AAPL-donchian promotion this row flags: t = 0.42 < 1.64) — the live remainder is the two undocumented P1 drops |
| trading-strategy#36 | ORDER 007's promotion-significance bar (deflated Sharpe) + AAPL-donchian re-grade | The bar's *implementation* is the thing that now gates the **one-shot holdout** (ORDER 008 unlock granted, Q-0262.2) — a wrong bar spends the repo's single most valuable pre-registered asset on a candidate its own P4 evidence (13/13 transfer-FAIL) argues against; verify before the holdout session runs | codex? · **open** — urgency annotation (first drain pass, 2026-07-10): the "drain before the holdout session" note is **MOOT** — the holdout was already executed and spent (trading #37, owner-merged 20:56Z; PRIMARY directional, not significant), so this row drains as ordinary post-merge review now; the re-check question stands (was the bar right, in hindsight of the verdict?). Groomed slice #4: link/head valid (head `f1cce45` · merged 2026-07-10T16:24:43Z); drain = manager batch (no Codex probe on trading-strategy) |
| superbot#1920 | The `check_baseview_inheritance` semantics change (checker now respects justifying comments) + the dashboard.json contract slice | Biggest diff of superbot's overnight band (960+/92−, 20 files); it changes an **enforcement surface** — night-review verified the raw-inventory ratchet held (Q7 verdict 5), but the comment-recognition semantics themselves never got non-author eyes. Band note (honest finding): the overnight band #1915–#1925 contained **zero `disbot/` runtime PRs** — the only `disbot/` touch was #1917, a one-line Codex docstring — so this tooling PR is the band's genuine max-risk item | **codex** · **drained → @codex asked 2026-07-10** ([comment](https://github.com/menno420/superbot/pull/1920#issuecomment-4939890801) on the merged head: does ANY existing consumer of `dashboard.json` — websites `dashboard/data_source.py`, botsite, or in-repo — actually read/validate `meta.schema_version`, or is the first contract-version bump a silent cross-repo no-op until a consumer-side check exists?), **response pending — Q-0120: verify against shipped source, never obey**. **Re-checked 2026-07-10T22:5xZ (chain slice #4): QUOTA-BLOCKED, no substantive answer** — the only reply is chatgpt-codex-connector[bot] [comment 4939891407](https://github.com/menno420/superbot/pull/1920#issuecomment-4939891407) (22:03:53Z, 7 s after the question): "You have reached your Codex usage limits for code reviews" — the earlier-suspected quota exhaustion confirmed as cause; re-ask when quota resets or drain manager-side. **Manager ground truth banked meanwhile (Q-0120 style — verified against shipped source, chain slice #4):** websites `dashboard/data_source.py` at HEAD `144dfce` (blob `b8ee413`) validates `meta.schema_version` ONLY for **console.json** (`console_contract_issue()` vs the pinned `dashboard/console_data_contract.json`); **NO consumer-side schema_version check exists for dashboard.json** — `fetch_dashboard()` returns the raw envelope and the `meta()`/`counts()` shapers never compare versions. The question's premise is CONFIRMED for the primary cross-repo consumer: the first version bump is a silent no-op there until a `console_contract_issue()`-style check is copied over for dashboard.json. Botsite/in-repo readers still unverified — Codex (post-quota) or a manager batch owes that half; row stays open on it |
| pokemon-mod-lab#8 | QoL+ increment 5 — chain head of the overnight #4–#8 engine-patch train | Five merged engine-patch PRs (12+ patches) whose feel verdict is **entirely unplaytested** (night-review Q4: "no plan today, only a queue slot"), and the ROM sha1-chain / byte-identity claims are lane-attested, not CI-checked (night-review Q9 item 2) | codex? · **open** — feel half is owner-playtest, code half drainable. Groomed slice #4: link/head valid (head `d927f8f` · merged 2026-07-10T06:54:02Z); drain path where missing: code half → manager batch (no Codex probe on pokemon-mod-lab); the sha1-chain claim is checkable from the committed `docs/proof/session-006/` fixtures without a playtest |
| gba-homebrew#12 | Lumen Drift increment 3 (concept scope complete) — merged on compile-only per-PR CI | Night-review Q9 item 1: the gameplay HUD asserts exist only at dispatch tier (#13); per-PR CI is compile-only, so a gameplay regression merges on a green compile; the lane also runs the fleet's hottest CI-per-PR ratio (economics ledger: 4.1 runs/PR) | codex? · **open** — groomed slice #4: link/head valid (head `cc5ad37` · merged 2026-07-10T04:34:19Z). Drain path where missing: manager batch (no Codex probe on gba-homebrew); re-check = whether the dispatch-tier HUD asserts (#13) reached per-PR CI or gameplay regressions still merge on a green compile |

## Reviewed / closed items

*(move rows here with the verdict + date)*
