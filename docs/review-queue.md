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

> **UPDATED 2026-07-11 (owner update ~00:2xZ, inbox ORDER 014): Codex
> environments now exist for ALL 12 active fleet repos** (fleet-manager,
> idea-engine, product-forge, sim-lab, substrate-kit, superbot,
> superbot-games, superbot-idle, superbot-next, trading-strategy,
> venture-lab, websites; stale envs for dead repos deleted). **@codex is now
> the PRIMARY drain path on all 12** — the fallback tier applies only during
> quota windows and to archived / non-enabled repos (codetool ×3,
> pokemon-mod-lab, gba-homebrew, mobile-lab). **The ORDER 007 relay is
> UNBLOCKED for fleet-manager PRs** — this repo's own rows drain via @codex
> directly now (the "no Codex env — ask on PR #26" wall is retired,
> `capabilities.md`).

- **PRIMARY — @codex post-merge review** (owner directive Q-0258 + Q-0259
  ruling 3, 2026-07-10; enabled fleet-wide on all 12 active repos by the
  owner 2026-07-11): the row's own session (or the manager at the next wake
  batch) posts **one specific question** as a PR comment mentioning
  **@codex** on the merged head — template pointer: superbot
  `docs/planning/codex-review-integration-plan-2026-06-17.md` Part C.
  **Q-0120 governs the return path: Codex's answer is input to verify
  against shipped source, never an order** — check each specific before
  acting, then strike or escalate the row. **Quota refusals (e.g.
  superbot#1920, 2026-07-10 22:03Z) are RETRY-LATER, never a wall** —
  re-ask after the window resets (`projects/README.md` § Codex fleet-wide
  enablement).
- **FALLBACK — the manager's failsafe-wake batches** drain rows only (a)
  during a Codex quota window, and (b) for repos **outside** the 12-repo
  enablement list (archives + parked non-enabled lanes: codetool ×3,
  pokemon-mod-lab, gba-homebrew, mobile-lab). *(Historical: until 2026-07-11
  this tier also covered fleet-manager itself and every "unknown until
  probed" repo — superseded by the fleet-wide enablement above.)*
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

**Manager-verify pass 2026-07-11T00:1xZ (chain slice #7):** trading#21 remainder
executed as recommended — **row CLOSED: RETIRED-SUPERSEDED** (first row ever to
reach the closed section; full verdict there). Nothing of #21's promotion
evidence still carries decision weight: the promotion label was demoted by the
#36 re-grade, the holdout is SPENT with a FINAL report, and the paper lane's
binding pre-registered protocol locks the one forward subject — no live or
future decision reads #21's verdicts again. The two undocumented P1 drops
(AAPL-SMA, AAPL-MACD) were CONFIRMED still undocumented at HEAD, but are a
historical-honesty residue, not a live risk (annotation suggestion riding the
next trading lane contact with the ORDER 010 relay).

**Manager-verify pass 2026-07-10T23:1xZ (chain slice #5):** superbot-games#16
executed as recommended — **CONFIRMED-STILL-BROKEN** at repo HEAD `b134961`
(verdict + the corrected fix target on the row: the kit upgrade #22 relocated the
pytest step to `.github/workflows/tests.yml`, so the original `substrate-gate.yml:62`
pointer is stale). sb#1920 re-checked same slice: **no new @codex comment** (thread
still ends at the 22:03:53Z quota refusal — refusals don't count as drain); no
annotation added.

| PR | What to re-check | Why-risky | Drain path · status |
|---|---|---|---|
| venture-lab#9 | The $49 product's real-Stripe checkout→grant path (products/Stripe-path class) | Night-review D1/Q2: headline path **never executed against real Stripe**; live events carry `customer_email: null` which the grant code (app.py ln 253–257) refuses, and the success URL uses `{CHECKOUT_EMAIL}`, a placeholder Stripe doesn't substitute — near-certain first-purchase failure; ⚑B/⚑D publish clicks frozen on it; already flagged by night-review as the fleet's worst truth-boundary miss | **manager-verified 2026-07-10 (first drain pass) — D1 DEFECT CONFIRMED AT HEAD `ce22315`, fix NOT landed (ORDER 003 unconsumed); row stays open until the fix PR merges.** Confirmed by code (`candidates/membership-kit/server/app.py`, blob `b52e7d6`): (1) `handle_purchase_event` reads ONLY `data.object.customer_email` and refuses on null — and `/create-checkout-session` calls `stripe.checkout.Session.create` **without** `customer_email`/`customer_creation`, so every real event arrives with `customer_email: null` (buyer's email lives in `customer_details.email`, never read); (2) worse than flagged: the refusal still returns **HTTP 200** (`granted: false`), so Stripe marks the webhook delivered and never retries — paid buyer, no grant, no retry, no alarm; (3) `success_url="http://localhost:8000/members?email={CHECKOUT_EMAIL}"` — Stripe substitutes only `{CHECKOUT_SESSION_ID}`, so the literal string 402s the buyer post-payment, and the host is hardcoded localhost; (4) all 13 tests build events via `_checkout_event()` which always sets `customer_email` — zero real-shape fixtures. **ORDER 003's fix must cover:** read `customer_details.email` with `customer_email` fallback (or set `customer_email` at session create); return non-2xx on an ungrantable completed-checkout so Stripe retries; success_url → `{CHECKOUT_SESSION_ID}` + server-side email resolve + env-configurable base URL; add a real-shape event fixture; R23 non-author verify + the ⚑A test-mode E2E stay the final gate. Groomed slice #4 (2026-07-10T22:5xZ): lane HEAD still `7558cb2` — fix NOT landed (ORDER 003 still unconsumed; no lane session has run, the boot click stays the unblock); row stays open. **Drain path updated 2026-07-11 (ORDER 014): venture-lab is Codex-enabled → @codex PRIMARY** — the fix PR (when it lands) gets an @codex question directly; manager batch is fallback only |
| superbot-games#5 | The 18-module pure-domain mining port (merged 00:00:58Z) | Largest games runtime diff of the night; it unblocked the merged games-plugins lane, so a latent port defect propagates into the successor lane; measured tests exist but no non-author eyes have read the port itself (launch record §1/§2) | codex? · **open** — groomed slice #4: link/head valid (head `33808dd` · merged 2026-07-10T00:00:58Z). Drain path where missing: no Codex probe on superbot-games yet → manager batch; sequence AFTER the #16 CI-collection verdict (a fixed gate re-runs the full 121-test suite on every PR, which is the cheapest standing check on this port; the manager read is then the verbatim-port claim vs the oracle). **MANAGER-VERIFIED 2026-07-10T23:5xZ (chain slice #6) — residual risk SCOPED given #16's CONFIRMED-STILL-BROKEN: the #16 gap does NOT blind this PR's own suite.** All 10 of #5's test files live under `tests/mining/`, and `tests/` at repo HEAD `b134961` contains ONLY `tests/mining/` — so the gate's `python3 -m pytest tests/ -q` (`.github/workflows/tests.yml:45` @ `b134961`) collects the mining suite in full today; the invisible `games/exploration/tests/` suites cover exploration, not this port. File-level mapping (module → test file, all collected): capacity+energy→`test_energy_capacity.py` · character+skills→`test_skills_character.py` · encounters→`test_encounters.py` · equipment→`test_encounters.py`/`test_exploration_world.py`/`test_skills_character.py` · exploration+world→`test_exploration_world.py` · grid→`test_grid.py`(+`test_encounters.py`) · items+market→`test_items_market.py` · recipes+workshop→`test_workshop_recipes.py` · rewards→`test_rewards.py` · structures→`test_structures.py`. **Blind spots: 4 of the 19 module files (`loadout.py`, `names.py`, `taxonomy.py`, `titles.py`) have import-only coverage** — `test_purity.py` pkgutil-imports all 19 (asserts the count + zero impure deps) but tests no behavior on them; nothing is fully uncovered at file level. (Count note: the PR body says 18 oracle modules; the tree has 19 module files besides `__init__.py` — the purity test's own assertion is 19.) **Verdict: verified-by-running-CI today = the 15 behaviorally-tested modules (their suites run on every PR); blind = the 4 import-only modules + the verbatim-port-vs-oracle claim itself (no oracle-diff check in CI; still non-author-unread). Fix rides ORDER 001 as sequenced — CONFIRMED:** its `tests.yml` collect-ALL + count assertion protects mining's suite from silent scope loss and makes exploration visible, but does NOT add the 4 missing behavioral tests — that follow-up belongs to the gen-2 Seat A boot (Q-0267, owner-queue item 14). Row stays open on the verbatim-port read; risk NARROWED. **Drain path updated 2026-07-11 (ORDER 014): codex? → codex** — superbot-games is Codex-enabled; the open verbatim-port-vs-oracle read is now an @codex question on the merged head (no probe needed) |
| trading-strategy#36 | ORDER 007's promotion-significance bar (deflated Sharpe) + AAPL-donchian re-grade | The bar's *implementation* is the thing that now gates the **one-shot holdout** (ORDER 008 unlock granted, Q-0262.2) — a wrong bar spends the repo's single most valuable pre-registered asset on a candidate its own P4 evidence (13/13 transfer-FAIL) argues against; verify before the holdout session runs | codex? · **open** — urgency annotation (first drain pass, 2026-07-10): the "drain before the holdout session" note is **MOOT** — the holdout was already executed and spent (trading #37, owner-merged 20:56Z; PRIMARY directional, not significant), so this row drains as ordinary post-merge review now; the re-check question stands (was the bar right, in hindsight of the verdict?). Groomed slice #4: link/head valid (head `f1cce45` · merged 2026-07-10T16:24:43Z); drain = manager batch (no Codex probe on trading-strategy). **Drain path updated 2026-07-11 (ORDER 014): → codex** — trading-strategy is Codex-enabled; the hindsight re-check question is @codex-postable directly |
| superbot#1920 | The `check_baseview_inheritance` semantics change (checker now respects justifying comments) + the dashboard.json contract slice | Biggest diff of superbot's overnight band (960+/92−, 20 files); it changes an **enforcement surface** — night-review verified the raw-inventory ratchet held (Q7 verdict 5), but the comment-recognition semantics themselves never got non-author eyes. Band note (honest finding): the overnight band #1915–#1925 contained **zero `disbot/` runtime PRs** — the only `disbot/` touch was #1917, a one-line Codex docstring — so this tooling PR is the band's genuine max-risk item | **codex** · **drained → @codex asked 2026-07-10** ([comment](https://github.com/menno420/superbot/pull/1920#issuecomment-4939890801) on the merged head: does ANY existing consumer of `dashboard.json` — websites `dashboard/data_source.py`, botsite, or in-repo — actually read/validate `meta.schema_version`, or is the first contract-version bump a silent cross-repo no-op until a consumer-side check exists?), **response pending — Q-0120: verify against shipped source, never obey**. **Re-checked 2026-07-10T22:5xZ (chain slice #4): QUOTA-BLOCKED, no substantive answer** — the only reply is chatgpt-codex-connector[bot] [comment 4939891407](https://github.com/menno420/superbot/pull/1920#issuecomment-4939891407) (22:03:53Z, 7 s after the question): "You have reached your Codex usage limits for code reviews" — the earlier-suspected quota exhaustion confirmed as cause; re-ask when quota resets or drain manager-side. **Manager ground truth banked meanwhile (Q-0120 style — verified against shipped source, chain slice #4):** websites `dashboard/data_source.py` at HEAD `144dfce` (blob `b8ee413`) validates `meta.schema_version` ONLY for **console.json** (`console_contract_issue()` vs the pinned `dashboard/console_data_contract.json`); **NO consumer-side schema_version check exists for dashboard.json** — `fetch_dashboard()` returns the raw envelope and the `meta()`/`counts()` shapers never compare versions. The question's premise is CONFIRMED for the primary cross-repo consumer: the first version bump is a silent no-op there until a `console_contract_issue()`-style check is copied over for dashboard.json. Botsite/in-repo readers still unverified — Codex (post-quota) or a manager batch owes that half; row stays open on it. **Annotated 2026-07-11 (ORDER 014): the 22:03Z quota refusal is RETRY-LATER by doctrine, never a wall** — re-ask @codex on the merged head when the window resets; the remaining botsite/in-repo half is the question to re-post |
| pokemon-mod-lab#8 | QoL+ increment 5 — chain head of the overnight #4–#8 engine-patch train | Five merged engine-patch PRs (12+ patches) whose feel verdict is **entirely unplaytested** (night-review Q4: "no plan today, only a queue slot"), and the ROM sha1-chain / byte-identity claims are lane-attested, not CI-checked (night-review Q9 item 2) | codex? · **open** — feel half is owner-playtest, code half drainable. Groomed slice #4: link/head valid (head `d927f8f` · merged 2026-07-10T06:54:02Z); drain path where missing: code half → manager batch (no Codex probe on pokemon-mod-lab); the sha1-chain claim is checkable from the committed `docs/proof/session-006/` fixtures without a playtest. **Drain path re-affirmed 2026-07-11 (ORDER 014): stays manager batch** — pokemon-mod-lab is NOT in the 12-repo Codex enablement list (fallback tier) |
| gba-homebrew#12 | Lumen Drift increment 3 (concept scope complete) — merged on compile-only per-PR CI | Night-review Q9 item 1: the gameplay HUD asserts exist only at dispatch tier (#13); per-PR CI is compile-only, so a gameplay regression merges on a green compile; the lane also runs the fleet's hottest CI-per-PR ratio (economics ledger: 4.1 runs/PR) | codex? · **open** — groomed slice #4: link/head valid (head `cc5ad37` · merged 2026-07-10T04:34:19Z). Drain path where missing: manager batch (no Codex probe on gba-homebrew); re-check = whether the dispatch-tier HUD asserts (#13) reached per-PR CI or gameplay regressions still merge on a green compile. **Drain path re-affirmed 2026-07-11 (ORDER 014): stays manager batch** — gba-homebrew is NOT in the 12-repo Codex enablement list (fallback tier) |

## Reviewed / closed items

*(move rows here with the verdict + date)*

| PR | Original re-check | Verdict |
|---|---|---|
| superbot-games#16 (head `5c71c61` · merged 2026-07-10T00:58:58Z) | The substrate-gate pytest step's actual collection scope — night-review Q7 verdict 1: "CI now gates the suite" was FALSE as stated (`pytest tests/ -q` collected 73 of 121; exploration's 48 under `games/exploration/tests/` invisible; the card's own arithmetic papered over it) | **VERIFIED-FIXED-AND-MERGED — closed 2026-07-11 (ORDER 015 registry-centralization slice, PR #58), verified in-tree at superbot-games HEAD `773fab0`.** ORDER 001 (P0 CI-collection fix) executed by the self-booted Seat A: **PR menno420/superbot-games#24** (branch `order-001-collection-scope`, head `241fb21`, merged 2026-07-11T00:20:47Z, merge SHA `7d4c3473bb489e58c047c369521a66e7d6e1fbc0`; CI green on head — `tests` run 29131622448 + `substrate-gate` run 29131622510; fix commit `0e5786b`). The fix landed exactly where the slice-#5 verify re-pointed it: **`.github/workflows/tests.yml`** (NOT the kit-owned `substrate-gate.yml`) now collects `tests/ games/exploration/tests/` **with a collected-count floor assertion** (`--collect-only \| grep -cE '::'`; `::error::` + exit 1 below floor) — the silent-scope-shrink class is a red gate now, satisfying the row's full ask (collect-ALL + count assertion). Floor since raised **121 → 147 (`8b9f153`, fishing) → 230** at HEAD `773fab0` (PRs #29/#33; workflow comment itemizes 79 mining + 26 fishing + 20 fishing-inventory-adapter + 48 exploration + 57 shared-inventory) — the ratchet is being maintained, not just installed. Consequential note for the still-open **superbot-games#5** row: its "sequence knowing the gate does NOT re-run the full suite" caveat is now obsolete — the gate re-runs all 230 on every PR; only the verbatim-port-vs-oracle read (+ the 4 import-only modules) remains open there. |
| trading-strategy#21 (head `ce00a83` · merged 2026-07-10T03:40:35Z) | P2 verdicts for all 14 candidates, incl. the AAPL-donchian PROMOTION issued under a statistics-free rule; two P1 candidates dropped with no stated rule | **RETIRED-SUPERSEDED — manager-verified 2026-07-11T00:1xZ (chain slice #7), verified against shipped source at trading HEAD `6799a4c`.** None of #21's promotion evidence still carries decision weight; every consumer of it has been superseded on main: **(1) the promotion label is gone** — `docs/p2-regrade-aapl-donchian.md` (the #36 re-grade) demoted the sole PROMOTED-TO-FINDING to RULE-PASS/candidate (t = 0.42 < 1.645), `docs/p2-validation-results.md` itself carries the demotion banner, and the statistics-free rule is replaced code-side by `trading_lab.promotion.grade_promotion` + `tests/test_promotion.py`; **(2) the decision the row raced is spent** — the one-shot holdout was consumed (#37, owner-merged; PRIMARY 0.759 vs 0.740, t = 0.02, directional-NOT-significant) and `docs/final-report.md` is FINAL ("no candidate holds a finding label"; protocol §6: no re-runs, no tuning, ever), so no future decision can consume #21's verdicts; **(3) forward evidence has a new, independent source** — the paper lane (#40–#43) runs under the BINDING pre-registered `docs/paper-lane-protocol.md`, whose §1 locks the single subject (donchian × AAPL × daily, params frozen from the sweep JSON, not from #21's labels) and which states nothing can promote or relabel except forward paper data. **Residue (non-load-bearing, documented here so it isn't lost):** the two P1 drops the row flagged — **AAPL-SMA (1.04\*) and AAPL-MACD (1.04\*)**, both starred as B&H-beats in `docs/p1-trend-following-results.md`'s headline table yet absent from its "Survivors for P2" list with no stated rule — are **CONFIRMED still undocumented** at HEAD, and `docs/p5-holdout-protocol.md` line ~31 still carries the "nominated by process, not by anyone's favorite" overstatement. This can no longer alter any decision (P2 selection is never re-read: program complete, holdout spent, paper subject locked), so it does not hold the row open; a one-line historical annotation in `p1-trend-following-results.md` is suggested to the trading lane at its next contact (rides the ORDER 010 relay). |
