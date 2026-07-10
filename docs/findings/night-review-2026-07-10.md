# Night review — the gen-2 fleet's first fully-autonomous night (2026-07-09 → 2026-07-10)

> **Status:** `audit`
>
> Commissioned deep review of the first fully-autonomous night of the gen-2
> fleet: 2026-07-09 ~22:00Z → 2026-07-10 ~06:30Z, 116 PRs merged across 10
> repos, zero stuck. Twenty-six questions, designed so that every one names
> the specific evidence it must be answered against — a lazy answer ("yes,
> mostly", "we'll monitor it") is visibly lazy. Answered against the eight
> discovery digests (fm, kit, trading, venture, games, superbot,
> web-games-next, telemetry), each verified at live GitHub HEAD rather than
> against lane reports, plus live checks made during the answer passes:
> fleet-manager `docs/capabilities.md` at HEAD `41c4250`, substrate-kit at
> HEAD `21d3ead`, and the GitHub API `repo.private` bit for every repo in the
> account. Where the honest answer is "I don't know," that is the answer
> recorded — this review is worthless if it flatters.

---

## Executive summary — the night in ten sentences

1. Last night the fleet ran unattended for the first time and merged 116 pull
requests across 10 repositories with zero stuck pipelines and zero duplicated
work — the shipping machinery genuinely worked. 2. Roughly a third of those
PRs were coordination ceremony rather than substance, and that ceremony churn
directly caused the only two hour-long stalls of the night. 3. The clearest
real value came from the game lanes — 12 proven engine patches on Pokémon
Emerald and an original GBA game built from an empty repo in about five hours,
every claim backed by a proof bundle — though nobody, human or agent, has yet
played any of it. 4. The night's advertised "sellable products" are not safely
sellable: the $49 product's headline Stripe feature has never executed and
almost certainly breaks on the first real purchase, and the owner queue was
inviting you to publish it at breakfast. 5. Trading's one promoted finding is
statistically indistinguishable from noise, while its genuinely best artifact
is an honest 13-for-13 negative — the promotion labels need a significance bar
before the one-shot holdout is spent. 6. The doctrine mostly held, but the
night's actual winning merge mechanism (the server-side auto-merge-enabler
workflow) is not the one the rules describe, and the rules shipped three
"always/never/impossible" claims that were falsified within hours. 7. The
night's only true safety failure: a repo whose README declares a "no
exceptions" PRIVATE rule is in fact public — with vendored Nintendo source
inside — eight PR bodies asserted "PRIVATE" without anyone running the one API
call that checks, and separately every repo in the account, the owner's to-do
queue included, is world-readable. 8. The most serious errors of the night —
the broken product, a CI gate silently skipping 40% of a repo's tests, the
public-repo breach — were caught only by this commissioned review, a layer
that does not currently run on any schedule. 9. Nobody knows what the night
cost: the free window closes 2026-07-14 and no economics ledger exists — that
ledger, a truth-check on owner-facing asks, and a structural visibility/rails
guard are the three changes that must land before adding lanes. 10. Overall
verdict: the shipping layer is real and earned its clean sheet; the catching
layer and the truth layer are one commissioned review away from not existing —
fix that before scaling.

### The night in numbers

| Measure | Value | Source |
|---|---|---|
| PRs merged, overnight window 00:00–06:15Z | 116 (verified recount; the "~80" brief undercounted) | fm launch record |
| PRs in the full telemetry window | ~137 | telemetry digest §2 |
| Repos active | 10 | fm launch record |
| Stuck PRs / duplicate executions | 0 / 0 | telemetry §6 |
| Ceremony fraction (claims, status closes, heartbeats) | ~⅓ fleet-wide; ~48% on substrate-kit | Q1 |
| Merges landed by the server-side enabler workflow | 54 of 137 | telemetry §2 |
| ~1h "green-behind" stalls | 2 (kit #92, #106) — both caused by ceremony churn | kit digest §4 |
| Unattended production-bot redeploys (all docs-only) | ~15 | superbot digest |
| Repos actually private (any repo, whole account) | 0 of 13 | live API check, this review |

---

## The Q&A

Questions appear verbatim from the question set; answers are this review's,
in one voice, with every substantive claim carrying its source.

## OUTCOMES — did the night deliver real value or busywork?

> **Q1.** Of the 116 merged PRs, ~48% of substrate-kit's 40 were pure control-plane ceremony
> (claims, status closes, heartbeats), and that ceremony churn directly caused the two ~1h
> green-behind stalls (#92, #106). What fraction of the *fleet-wide* 116 is substantive by the
> same standard, and would the owner-visible outcome of the night have differed if the ceremony
> half had never existed?

**Best estimate: roughly a third of the fleet's 116 PRs were pure coordination
ceremony (claims, status closes, heartbeats, order appends) — call it 35–40
PRs.** This is an estimate assembled per-repo, not an exact count, because only
the kit digest classified every PR:

- substrate-kit: 19 of 40 ceremony in its window, ~17 of the 35 in the
  launch-record window (kit digest §1 — the one lane with an exact count).
- websites: 4–5 of 6 — only #53 was the actual build; #49/#50/#51/#52/#54 are
  seed, order append, skeleton, claim, and status close (web-games-next digest,
  Lane 1 table).
- superbot-games: 3 of 6 were control/manager orders (#6/#7/#10,
  web-games-next Lane 2).
- gba-homebrew: ~5 of 18 (heartbeats #11/#15/#19 + close-outs, telemetry §3b,
  games digest §3).
- venture-lab ~3 of 8; superbot ~2 of 13 (dashboard refreshes); trading,
  pokemon, fleet-manager, superbot-next mostly substantive.

**Would the owner-visible outcome have differed without the ceremony? Almost
entirely no — with one honest credit and one honest debit.** The credit: the
ceremony is not decorative. The claim ritual and born-red cards are the
plausible reason the night had **zero duplicate executions** (telemetry §6)
versus gen-1's two same-day double-builds (fm digest §8, R19 provenance). You
don't get to delete the function. The debit: the current *implementation* —
one PR per claim, one per status close — actively damaged the night: the
ceremony merge churn is what knocked kit #92 and #106 into their ~1-hour
"green-behind" stalls (kit digest §4: "the ceremony-PR volume is what generated
the base-branch churn that triggered the stalls").

**Opinion:** keep the ceremony's function, halve its PR count. The kit
digest's batching proposal (claim rides the born-red card's first push;
status-close rides the final flip — kit §7.4) preserves every signal at
roughly half the churn. Nothing the owner saw at breakfast came from a
ceremony PR; everything he saw came from the ~75 substantive ones.

> **Q2.** The night's two "sellable products" are not sellable as described: membership-kit's
> $49 headline feature (real Stripe → grant) has never executed and contains a near-certain
> functional bug (D1: `customer_email` null on live events + an invalid `{CHECKOUT_EMAIL}`
> success-URL placeholder), and the buyer zip's README describes v0.1 in-memory storage that
> v0.2 replaced. If the owner had clicked ⚑B at breakfast as the queue invited him to, a paying
> customer would have hit a broken product. Do we count venture-lab as a night success, and by
> what definition of "done" — code merged, or value deliverable without embarrassment?

**By "code merged and honestly ledgered": yes. By "value deliverable without
embarrassment": no — and the second definition is the only one that matters
for a lane whose entire purpose is selling things.** The concrete situation
(venture digest D1–D3):

- The $49 product's headline feature — "Stripe Checkout + webhook, pre-wired"
  (LISTING.md ln 29) — has **never executed against real Stripe** and contains
  two bugs that would very likely break the first real purchase: the checkout
  session never passes the buyer's email, so live events arrive with
  `customer_email: null` and the grant code (app.py ln 253–257) refuses them;
  and the success URL uses `{CHECKOUT_EMAIL}`, a placeholder Stripe doesn't
  support, so even a granted buyer lands on a 402 page (app.py ln 360–372).
- The buyer zip's README describes the previous version ("the store is
  in-memory") — the product outran its own sales copy inside one night (D2).
- The owner-queue's flag B invited the owner to paste that listing at
  breakfast. Had he clicked, a paying customer would have hit a broken product
  with wrong docs.

**The important nuance: the lane was honest with itself and dishonest with the
buyer, in the same repo, the same night.** The internal ledger explicitly says
live Stripe is "the last unproven leg" (venture-ledger.md ln 171–172) — good.
The buyer-facing LISTING sells that same leg as done — not good. Two truth
standards coexisted and the owner-facing ask was wired to the wrong one.

**Verdict recorded:** venture-lab was a *build* success and a *product*
failure, and the night's definition of done for money-facing lanes must change
to: **a sell-claim is done when it has been executed, not when its code is
merged.** The fix is small (venture digest estimates ~1 focused hour: pass the
email, fix the URL, regenerate the stale copy, add HTTP-layer tests) — but
flag B should say "DO NOT publish yet" until that session lands. The $19
template pack (flag D) is fine to publish as-is (venture digest, candidate #2).

> **Q3.** Trading's headline PROMOTED-TO-FINDING is a +0.079 Sharpe edge whose standard error
> at that horizon is ~0.19 — deep inside noise — and the founding plan's own "prefer deflated
> Sharpe" is computed nowhere in the repo. Meanwhile the night's genuinely best artifact there
> is a 13/13 *negative* (P4 transfer-fail). Are our promotion labels calibrated to statistical
> reality, or to the narrative need for at least one positive result per lane per night?

**Calibrated to mechanical rule-compliance — which is better than narrative,
but the rule itself has no statistics in it, so the label overstates the
finding.** The facts (trading digest §3):

- The promotion followed a genuinely pre-committed rule (beat buy-and-hold on
  Sharpe, net of costs — in the founding plan from PR #1, verified in commit
  `4067bbb` before any sweep existed) and reproduces to four decimal places.
  This is *not* a cooked result.
- But the edge is +0.079 Sharpe where the standard error at that horizon is
  ~0.19 — about 0.4 standard errors, deep inside noise — and the founding
  plan's own "prefer deflated Sharpe" is computed **nowhere in the repo**. The
  rule contains no significance bar at all, so *any* positive delta promotes.
- Against the "narrative need for a nightly positive": the same lane published
  a 13/13 transfer FAIL against its own promoted finding and said it "sharpens
  the prior against it" (p4-transfer-results.md:108–117). A lane optimizing
  for narrative doesn't do that.
- Mild narrative-direction evidence does exist: two P1 candidates (AAPL-SMA,
  AAPL-MACD) were dropped with no stated rule, while the P5 protocol claims
  candidates were "nominated by process, not by anyone's favorite" (trading
  §3, last bullet) — an overstatement.

**Opinion:** rename or re-gate before P5. Either the label becomes something
honest like RULE-PASS (mechanical, no significance claim), or the promotion
rule gets the missing bar (deflated Sharpe or a minimum t-stat) *before* the
one-shot holdout is spent. Burning the holdout — the repo's single most
valuable, genuinely pre-registered asset (trading §5) — on a candidate the
lane's own P4 evidence already argues against should be a deliberate owner
choice, made knowing the expected result is failure, not a default next step.

> **Q4.** The games lanes produced the night's least ambiguous value (12 proven engine patches
> on pokeemerald in ~6h; an original GBA game with CI-asserted replays from empty repo in ~5h)
> — yet nobody, human or agent, has ever *played* any of it, and four game-feel patches plus
> Lumen Drift feel are parked on an owner playtest that competes with seven other owner-queue
> items. What is the plan for converting proven-by-script into verified-by-play before the
> backlog of "awaiting playtest" work makes the verdict meaningless?

**Honest answer: there is no plan today — there is a queue slot, and queue
slots are where this dies.** The playtest is one of 8 active owner-queue items
(fm digest §3), competing with a rubric ruling, revenue clicks, repo settings,
and instruction reviews. Meanwhile it is the *only* item on that list that is
(a) fun, (b) impossible for any agent to do, and (c) the verdict-gate for five
artifacts at once: four parked game-feel patches (pokemon PRs #6/#7, parked at
07:49Z — games digest §2) plus Lumen Drift feel (games §3, "nobody — human or
agent — has played it interactively").

**The plan this review puts in place, concretely:**

1. **Make it one bundled session, not five verdicts.** The games lanes prepare
   a single playtest kit: one patched Emerald ROM build + one Lumen Drift ROM,
   a one-page checklist ("does auto-run feel right? y/n" × 6 questions),
   target 30–45 minutes of owner time. Agents can prepare 100% of this; only
   the playing is owner-only. That preparation session should be ordered now.
2. **Rank it #1 or #2 on the owner queue**, explicitly above the
   instruction-package review — doctrine review can slip a day; a growing pile
   of unverdicted taste-work poisons two lanes' roadmaps.
3. **Freeze feel-dependent work until the verdict.** The pokemon lane already
   did this correctly (parked itself, games §2 — credit where due). The rule
   should be fleet doctrine: a lane may accumulate at most one
   playtest-blocked batch before it must park or pivot to non-taste work
   (engine, tooling, CI promotion — of which games has plenty, see Q9).
4. **Distinguish "taste asks" from "verification asks" in the queue format** —
   a verification ask can often be shrunk by more agent work; a taste ask
   cannot, and the queue should stop presenting them as the same kind of chore.

If the playtest hasn't happened within ~3 days, the honest move is to say the
QoL direction is unverdicted and stop the game-feel patch line entirely rather
than deepen the backlog.

> **Q5.** Rank the ten lanes by owner-value-per-token honestly. Which lane, if it had not run
> at all tonight, would the owner never have noticed missing — and what does that lane's
> existence cost per night once the free window closes on 2026-07-14?

Token counts don't exist (F12 — the economics ledger is an unbuilt idea, fm
digest §4), so this is value-per-*night* with cost assumed roughly comparable
per lane. The honest ranking:

1. **pokemon-mod-lab** — 12 proven engine patches on a 20-year-old commercial
   codebase in ~6h, every claim backed by a real proof bundle (games §2).
   Least ambiguous owner-value of the night, *if* the owner plays it (Q4).
2. **gba-homebrew** — an original, CI-replay-proven game from an empty repo in
   ~5h (games §3). Same caveat.
3. **websites** — ORDER 005 live at the production URL, independently verified
   200s, 140 tests reproduced (web-games-next Lane 1). Directly owner-usable
   today.
4. **superbot-games** — the 18-module mining port with *measured*
   byte-fidelity (4 modules byte-identical, the rest import-rewrites or
   documented seams — web-games-next Lane 2). Real rebuild progress, minus one
   CI gap (Q7).
5. **substrate-kit** — real engineering (3 defect-free code-deep samples) and
   the queue emptied, but ~48% ceremony and its benchmark reported the kit
   *losing* run-4 (kit §6). High meta-value, modest direct value.
6. **trading-strategy** — the night's best *methodology* (holdout verified
   four ways) and best negative (P4), but the sole positive is statistically
   empty (Q3). Value is the process, not yet any finding.
7. **superbot** — a clean, self-auditing night with zero runtime change
   (superbot digest); the value was audit infrastructure and the 3h40m
   idea-to-tool loop (#1911→#1923).
8. **fleet-manager** — wrote the doctrine and the audit of the doctrine;
   caught real errors (~80→116 undercount) but also *produced* several of the
   errors it caught (fm §10).
9. **venture-lab** — at the margin, **negative owner value as shipped**: its
   one owner-visible output was an invitation to publish a broken product
   (Q2). The underlying build is decent; the packaging of the ask made it
   dangerous.
10. **superbot-next** — 2 docs-only PRs, +150 lines of status settling and
    idea seeds (web-games-next Lane 3).

**The lane that would never be missed: superbot-next** — and that is *to its
credit*: it correctly recognized its next task (band-5 live-drive) needs a
live server session and declined to manufacture overnight busywork. The lane
to actually worry about is **venture-lab**, which *would* have been noticed —
for the wrong reason.

**Cost after 2026-07-14: unknown — to everyone — and that's the finding.** The
wake-cadence architecture was designed with zero cost data inside a free
window (fm §10e, F12). Until the economics ledger exists, "value-per-token" is
a ranking of numerators with no denominators.

## CODE QUALITY — is the shipped code actually good, per lane?

> **Q6.** Every venture-lab defect that matters (D1 Stripe bug, D2 stale README in the buyer
> zip, D3 QUICKSTART's silent mock-mode trap, zero HTTP-layer tests) was found by *this
> review*, not by any of the 8 PRs' authors, the fleet review, or the 13 green tests — which
> inject synthetic events that can't exercise the real path. What structural check would have
> caught D1 before it reached a LISTING the owner was told to paste, and why doesn't the
> "tested logic is the shipped logic" pattern (which the same file gets right for the mock
> path) extend to the one path a buyer pays for?

**The check that catches D1 is: build test fixtures from the vendor's ground
truth, not from the author's imagination — and gate every sell-claim on an
executed proof.** Two concrete versions, cheapest first:

1. **Vendor-schema fixtures (free, would have caught D1 in the existing
   suite).** The 13 green tests inject events from a hand-rolled
   `_checkout_event()` helper that always sets `customer_email` (venture D1,
   app.py ln 404–409). Stripe publishes real sample payloads for
   `checkout.session.completed`, and in those samples `customer_email` is
   null with the buyer's address in `customer_details.email`. Had the fixture
   been copy-pasted from Stripe's docs instead of authored from memory, the
   existing unit test would have failed the moment the grant path read the
   wrong field. No network, no keys, no new infrastructure — just the rule
   "third-party event fixtures must be vendored from the provider's
   documented samples, never synthesized."
2. **A claim-gate on owner-facing sell copy.** The games lanes already live by
   this standard without being told: every PR-body claim in pokemon-mod-lab
   has a screenshot, replay, or sha1 backing it (games §2). Venture-lab's
   LISTING has no equivalent — its headline claim maps to zero executed
   evidence. The rule: **no flag inviting the owner to publish/sell may ship
   while any headline claim in the artifact lacks an execution artifact** (for
   Stripe: one `stripe trigger` run against test keys, captured like the demo
   transcript the lane already produced for the mock path).

**Why didn't "tested logic is shipped logic" save it?** Because that pattern
only guarantees the tested code *is* the shipped code — it says nothing about
whether the test's *inputs* resemble the world. D1 is not an implementation
bug; it is a wrong belief about what Stripe sends, and the same session wrote
both the belief into the code and the same belief into the test. Tests
authored by the same mind as the code catch implementation errors, never
world-model errors. Only external ground truth (vendor fixtures, or a live
fire) breaks that loop — which is also the honest answer to why the mock path
is fine: the mock path's "world" is defined by the repo itself, so the
author's model of it cannot be wrong. Also worth recording: **zero HTTP-layer
tests** (venture D1, last bullet) meant even the routes a buyer touches first
were untested — that one is ordinary coverage debt, fixable in the same ~1h
session.

> **Q7.** superbot-games #16 added a pytest step to CI claiming it now gates the suite — but
> `pytest tests/ -q` collects 73 of 121 tests; exploration's 48 under `games/exploration/tests/`
> are invisible to the gate, and the session card's own arithmetic ("mining 62 + encounters 11 +
> exploration = 73") papered over it. How many other "CI now enforces X" claims from tonight
> were verified by reading the workflow's actual collection scope rather than the card's claim?

**During the night, by the authoring sessions: as far as the evidence shows,
none — every enforcement claim was asserted from the card, not from reading
the workflow's collection scope. This review wave checked six; one was false,
one materially misleading.**

The six, with verdicts:

1. **superbot-games #16 ("substrate-gate now runs the suite") — FALSE as
   stated.** The step runs `pytest tests/ -q`, which collects 73 of 121
   tests; exploration's 48 under `games/exploration/tests/` are invisible,
   and the card's own arithmetic ("mining 62 + encounters 11 + exploration =
   73") papers over it — 62+11 is already 73 (web-games-next, Lane 2 gap).
   One-line fix identified (`.github/workflows/substrate-gate.yml:62`).
2. **gba-homebrew gameplay CI — TRUE but tier-misleading.** The frame-exact
   HUD asserts exist and passed, but only on manual dispatch; per-PR CI is
   compile-only, so a gameplay regression merges on a green compile (games
   §3, caveat). The claims read stronger than the enforcement.
3. **trading's holdout CI audit — TRUE, and exemplary.** The committed-ledger
   test really collects and runs on every CI pass, and this review live-fired
   the guard it backs (trading §1).
4. **superbot's telemetry gate — TRUE.** First full night, every card-PR
   carries the telemetry row, zero misses (superbot digest, session-ender
   section).
5. **superbot #1920's architecture-checker change — TRUE, with the ratchet
   genuinely preserved** (the conformance test pins the raw 13-entry
   inventory; superbot digest, deploy-risk section).
6. **kit's session/engagement gates — TRUE by observed behavior** (born-red
   holds actually held merges; the one false-red was found and fixed in #86,
   kit §2).

**A 1-false-plus-1-misleading rate out of six is too high to keep trusting
cards.** The cheap structural fix, in the fleet's own existing idiom: any PR
claiming "CI now gates/enforces X" must paste the evidence into the PR body —
the collected-test count from the workflow's exact command, and the workflow's
trigger lines. That is precisely the claim-plus-evidence discipline the
pokemon lane already applies to sha1 chains (games §2); it just hasn't been
applied to CI claims.

> **Q8.** The three kit code-deep samples (#92, #103, #106) were defect-free with prescribed
> guard tests, and the trading engine survived a lookahead audit with a live-fired holdout
> guard. The venture-lab app did not survive equivalent scrutiny. Is the quality difference
> explained by lane maturity, model seat, session prompt, or review pressure — and can we say
> which, given we ran no controlled comparison (the harness×model experiment sits
> ready-not-launched, 0 of 6 repos created)?

**We cannot answer this rigorously, and this review won't pretend: the
controlled comparison that would answer it (the harness × model experiment)
sits ready-not-launched, 0 of 6 repos created (fm §6).** What the uncontrolled
evidence *does* support:

- **Model seat is probably not the driver.** The three defect-free kit samples
  span seats — #92 and #106 were Opus 4.8 sessions, #103 was Fable 5 (kit §3)
  — and all three were clean. Weak evidence, but it points away from "better
  model, better code."
- **The strongest available explanation is the *domain's* verifiability, not
  the lane's virtue.** Kit and trading work in domains where ground truth
  lives inside the repo: a kit guard test exercises the kit's own behavior;
  trading's lookahead audit checks the engine against its own data, and the
  review could live-fire the holdout guard (trading §1). Venture-lab's fatal
  defect is a claim about the *outside world* — Stripe's real event shape —
  which no quantity of internally-authored tests can touch (Q6). The same
  session's mock path, whose ground truth *is* internal, was clean and
  well-tested (venture digest, "genuinely good" list). Same night, same lane,
  same author: internal-truth code good, external-truth code broken. That
  within-lane contrast is the most informative data point we have.
- **Prescribed tests helped where they existed.** Kit's fixes each carried
  "the guard test its idea file prescribed" (kit §3a) — a spec written before
  the code. Venture-lab had no equivalent prescription for the live path, and
  its founding pressure was speed-to-sellable.
- **Review pressure is a real confound**: kit's samples were written knowing
  sibling lanes and adversarial reviews run the same night; venture-lab was
  the fleet's newest repo with the least surveillance and no HTTP-layer tests
  demanded by anything.

**Opinion, clearly labeled as hypothesis:** ~60% domain verifiability, ~25%
lane maturity (prescribed-test culture), ~15% everything else, model seat
likely negligible. The action item is not to trust that split — it's to launch
the experiment that makes this question answerable, and meanwhile apply Q6's
external-ground-truth rule to every lane whose claims touch the outside world
(venture-lab, and trading the day it goes live).

> **Q9.** gba-homebrew's semantic gameplay CI (frame-exact HUD asserts) is dispatch-tier only;
> per-PR CI is compile-only, so a gameplay regression merges on a green compile unless someone
> remembers to dispatch. The games byte-identity claims are lane-attested, not CI-enforced.
> Where else in the fleet does our strongest evidence exist only at the courtesy tier, and what
> does it cost to promote each to the enforced tier?

Inventory of "the best evidence exists but nothing enforces it," with
promotion cost:

1. **gba-homebrew semantic gameplay CI** — dispatch-only; per-PR is
   compile-only (games §3). Cost: add the headless-boot replay to per-PR CI on
   `games/**` paths; measured 105s warm (games §6.4). Slightly over the 60s
   Tier-1 budget — this review's call: pay the extra minute; it's the only
   regression gate the game has.
2. **pokemon-mod-lab byte-identity claims** — lane-attested in notes.md, not
   CI-checked (games §2, "What I did NOT do"). Cost: near-zero for the
   reproducibility half — the ROM-builds job already rebuilds from bare
   checkout; add one line asserting the built ROM's sha1 equals the PR-body's
   claimed hash. The "no fixture was ever committed" half is genuinely hard to
   CI-check; leave it attested.
3. **superbot's three new checkers** (#1918 command-collisions, #1919
   lane-overlap, #1923 manifest-freshness) — all deliberately un-wired to CI
   (superbot digest, deploy-risk). Correct unattended posture *then*; now it
   needs the follow-up decision or the tools rot. Cost: one wiring PR each,
   after the Q-0105 verification window.
4. **superbot-games test gate** — 48 of 121 tests uncollected (Q7). Cost: one
   line. Highest urgency-to-cost ratio on this list.
5. **Trading's pre-registration** — for P2/P4 it is commit *narration*, not
   commit *order* (rules entered git minutes after, or in the same commit as,
   the runs — trading §5). P5 already does it right. Cost: free — a procedural
   rule, "protocol commit pushes before the run commit, always two pushes,"
   which the trading digest itself recommends.
6. **Kit bench model-identity** — run-3's judge silently collapsed to the arm
   model; the guard (manifest `arm_model` + judge==arm warning) is still an
   unfiled card-level idea (kit §4). Cost: small script change; must land
   before any trend headline is quoted again.
7. **Fleet capabilities walls** — the routine wall was recorded fleet-wide off
   two tested surfaces and owner-falsified within hours (fm §2). The "walls
   must name the surface tested" rule exists only in a session-card note.
   Cost: a format requirement in the capabilities ledger plus one sweep of
   existing entries. (Q11's territory, but it belongs on this inventory.)

**The pattern worth naming to the owner:** the fleet is excellent at
*producing* strong evidence and consistently one tier behind at *enforcing* it
— proof bundles without CI asserts, audits without wired checkers, protocols
without commit-order proof. Every item above is cheap (most are one line to
one small PR). Order a single "promotion sweep" session across repos 1–6
rather than waiting for each lane to rediscover its own gap.

## PROCESS / DOCTRINE — which gen-2 rules earned their keep?

> **Q10.** R21's own clause (a) — "arm structurally impossible on born-red repos" — was
> falsified the same night it was written (kit armed successfully dozens of times in the
> pending window; F2), and the night's actual winning merge path was a *third* mechanism R21
> doesn't name: the server-side auto-merge-enabler workflow, which landed PRs under active
> classifier denial with no agent merge call. When does R21 get rewritten around the enabler
> pattern as primary, and what stops us from shipping the next rule with the same
> one-incident-to-universal-law overreach?

**Rewrite it at the next blueprint pass — the material already exists.** Be
fair to R21 first: its core instinct ("use a sanctioned path, don't rely on
the direct merge call") was the night's most load-bearing rule — the telemetry
digest rates it "effective and load-bearing" and every new repo's seed
conventions cite it (pokemon #1, venture #1, gba #1). What's wrong is clause
(a)'s *wording*: "arm structurally impossible on born-red repos" was falsified
the same night (kit armed successfully dozens of times in the pending window —
fm review finding F2), and the mechanism that actually carried the most
traffic — the server-side auto-merge-enabler workflow, 54 of 137 window merges
(kit 37 + superbot 13 + superbot-next 4, telemetry §2), landing PRs under
*active classifier denial* with no agent merge call — isn't named in R21 at
all. The fix is drafted: fm PR #17's P1 proposal disputes the wording, and the
kit digest's recommendation #3 says promote the enabler into the planted
templates. The rewrite should rank paths explicitly: enabler workflow primary
wherever Actions exist → direct arm-in-pending-window secondary → REST
merge-on-green fallback.

**What stops the next overreach: today, nothing — and it happened at least
three times tonight**, same pattern each time (one incident → universal law):
R21(a) from one late-arm failure; the routine wall from two tested surfaces
(Q11); and gen-1's "tag push 403 = releases are owner-gated," which kit killed
by cutting v1.7.0 agent-side via `workflow_dispatch` at 06:38:59Z. The
structural fix is cheap and doctrinal: **a new rule may not say "always /
never / impossible" until it has either a second independent incident or one
deliberate falsification probe; until then it ships as "observed on
<surface/repo-shape>, N=1, provisional."** That's one paragraph in the
playbook's own header. It costs a rule some swagger for a day; tonight it
would have prevented all three overreaches. Honest caveat: playbook edits are
owner-gated in fm's discipline, so this lands as a proposal — but it should be
in the same blueprint pass as the R21 rewrite, not a separate someday item.

> **Q11.** The routine wall was tested on two surfaces, recorded as "walled on BOTH sides"
> fleet-wide at 06:43Z, and owner-falsified for Project sessions by ~11:00Z — the wake-cadence
> architecture briefly rested on a wrong PLATFORM GAP conclusion. The corrective rule
> ("capabilities walls must name the surface tested; an untested surface is unknown, not
> walled") exists only in a session card's ⟲ note. Has it been promoted to the capabilities
> ledger's own format requirement, and what other current walls-ledger entries would fail that
> surface-named test today?

**No.** Verified against fleet-manager `docs/capabilities.md` at HEAD
`41c4250` today: the corrected routine-wall *entry* now names its surfaces
properly ("walled on NON-PROJECT surfaces only… webagent coordinator + spawned
workers; cross-session binding"), but the ledger's own **DISCOVERY RULE still
reads "attempt it once and capture the exact error"** — attempt *where* is not
a required field. The corrective rule exists only in fm PR #19's session-card
⟲ note, which is exactly the kind of place rules go to be forgotten.

**Entries in the current WALLED list that would fail the surface-named test
today:**

1. **"Tag push, GitHub Release creation… 403 → owner action required"** —
   already partially false at HEAD. Kit cut v1.7.0 agent-side via
   `release.yml` workflow_dispatch (run 29074386841, tag published 06:38:59Z)
   and its status file explicitly says "do NOT flag routine releases as
   owner-gated." The fm ledger has not absorbed this; it conflates the
   mechanism (direct tag push — genuinely 403) with the capability (releasing
   — provably agent-side). This is the routine-wall mistake sitting live in
   the ledger right now.
2. **"Direct self-merge blocked by the classifier"** — the classifier is
   per-seat nondeterministic (identical `enable_pr_auto_merge` calls PERMITTED
   on kit #107/#109 and REFUSED verbatim on other seats, same night, same repo
   — kit CAPABILITIES lines 160–169). A wall that's true on some seats and
   false on others is wrong in both directions without a seat/surface field.
3. **"Creating/editing claude.ai environments or Projects — no API surface"**
   — asserted with no recorded probe, error, or surface at all.
4. **GraphQL "~hourly" quota** — the CI-tier sim's own §8 admits it's a
   calibrated estimate with "no raw RATE_LIMITED transcript."

Recommendation: one small fm PR — add "surface tested + date + verbatim
error" as mandatory fields to the DISCOVERY RULE, re-audit the WALLED list
against it, and fix the release-wall entry today since kit already falsified
it.

> **Q12.** Born-red held on most lanes and Session C is its best advertisement (a session that
> died pre-card left zero trace — exactly the gap the protocol can't see). But #1914/#1915
> skipped the in-flight window entirely (single-push, card-born-complete) and nothing flagged
> it. Is born-red's in-flight-signal half (Q-0189) enforced by anything, or only by sessions
> choosing to comply — and how would we detect the next Session C, given no repo-side guard can
> see a session that never pushes?

**It is enforced by nothing; compliance is voluntary.** The session gate
(`check_session_gate.py`) holds a PR that *adds an in-progress card* — a card
born `complete` in a single push sails through green, which is exactly what
#1914 and #1915 did (superbot digest: single-commit, already-complete card,
6-minute PR, no in-flight window), and nothing flagged it. Q-0189's whole
value is the in-flight visibility that prevents duplicate work; a
born-complete card provides zero of it.

Two different gaps, two different fixes:

- **The skip (detectable repo-side):** a cheap advisory checker that flags any
  session PR whose card is added already-`complete` in its first commit — the
  born-complete detector. Advisory, not blocking: for a 6-minute docs PR the
  in-flight window is worth little, and the point is to make the skip
  *visible*, not to punish it. This is a ~30-line addition to the existing
  gate script; free-to-ship class.
- **The next Session C (not detectable repo-side, ever):** a session that dies
  before pushing leaves no repo artifact by definition — #1920's card says C
  survives only "in the coordinator's memory." The fix must live one layer up:
  **the coordinator writes a spawn ledger into its own card at dispatch time**
  (shift name, start time, expected card path), and any spawned shift with no
  PR after N hours gets an automatic tombstone line at coordinator close-out.
  That converts "the coordinator happened to remember" into a durable artifact
  the morning review reads. Tonight it worked by luck-of-diligence — #1920
  chose to document C; nothing required it to.

> **Q13.** The binding blueprint accumulated 4 amendments in ~16 hours, went `binding` while
> containing an internal contradiction (F3: no-op heartbeat wakes are impossible under the
> PR-required main the same document mandates), and the venture-lab founding text nearly
> shipped with a merge path R21 documents as refused — caught only because the review wave ran
> the same night. Should doctrine have a mandatory cool-off or adversarial pass *before*
> binding status, and what would tonight have looked like if the Fable-5 review had run a day
> later instead?

**Yes — an adversarial pass, not a clock cool-off.** The evidence: the
blueprint went `binding` containing an internal contradiction (F3:
heartbeat-without-PR is impossible under the PR-required main the same
document mandates) and took 4 amendments in ~16 hours; the venture-lab
founding text nearly shipped directing a merge path R21 documents as refused
(F1/F13/F23 — the review's line 1 to the owner was literally "Don't paste the
venture-lab instructions yet"); and all 10 instruction packages were drafted
at ~9k chars against an 8k paste field nobody had measured — one early paste
probe would have saved rework on all ten.

**The counterfactual (review a day later):** the owner-queue was actively
inviting the venture paste, so the plausible morning is: owner pastes at
breakfast, the lane's first PRs hit the refused merge path and burn their
opening session improvising; F3's contradiction sits in binding text while six
lanes get wake-arm ORDERs built on it. The 8k overflow would still have been
caught (it was caught by the paste itself, not the review). Damage bounded —
everything was reversible-on-paper — but "reversible" isn't "free": the whole
gen-2 pitch is zero-stuck, and stale binding doctrine is precisely how lanes
get stuck.

Proposed rule: **doctrine may be written and used as `draft` immediately, but
`binding` requires (1) one adversarial review by a different seat and (2) one
cheap empirical probe of any "impossible / always / all-X" claim it contains**
(paste one package before writing ten; run one arm call before declaring arms
impossible). A clock cool-off is the wrong tool at this velocity — the
audit-of-doctrine-*same-night* was the night's best pattern (fm §10: the
manager "let the audit win"); the fix is making that pattern mandatory rather
than fortunate.

> **Q14.** The self-merge doctrine still has no refusal branch: the auto-mode classifier
> PERMITTED identical `enable_pr_auto_merge` calls on some seats and REFUSED them as "Merge
> Without Review" on others, same night, same repo — and a classifier-denied lane's terminal
> state remains formally undefined (F4/F6; the P3 first-denial-stop script is still a
> proposal). How many of tonight's zero-stuck outcomes were the enabler workflow absorbing this
> nondeterminism, and what happens on the first repo that can't host the enabler?

**A material fraction, and this review can bound it but not count it
exactly.** Path A (the enabler) carried 54 of 137 window merges (telemetry
§2). Of those, the kit lane — the fleet's biggest at 37 PRs — is documented
hitting repeated classifier REFUSALS the same night other seats were PERMITTED
(kit status + CAPABILITIES verbatim), and its PRs landed "with no agent merge
call" (kit #100's own enumeration of #84–#99). So without the enabler, at
minimum the kit lane would have been playing denial-lottery per PR. **What
nobody logged is the denominator** — arm attempts vs refusals per seat — so
"how many would have stuck" is genuinely unknowable from tonight's data. That
gap is itself a finding: refusals are currently recorded as prose in
capabilities files, not counted.

**On a repo that can't host the enabler:** the terminal state of a
classifier-denied lane is formally undefined — F4/F6's "literally undefined"
stands, and P3 (the first-denial-stop script) is still a proposal at HEAD.
Observed behavior tonight was improvise-to-REST (path C worked fine on 47 PRs
across fm/pokemon/gba/websites), but a REST `merge_pull_request` call is
exactly what some refusals name as the offense, so a denied seat on an
enabler-less repo has no sanctioned path at all. Two riders: (a) the enabler
already showed a blind spot in production — superbot #1917's `codex/*` head
branch skipped the enabler job (job 86270880835) and sat green for 14 minutes
until something merged it manually (telemetry §3c); head-pattern coverage is
part of the same fix. (b) "Can't host the enabler" is a rare repo shape —
anything with Actions can host it — so the practical priority order is: ship
P3 before the next lane launches (it's a script plus a doctrine line), and put
the enabler in the kit's planted templates so no future repo is born without
it (kit digest recommendation #3).

> **Q15.** Deferred fixes demonstrably have no owner: D2 sat a day while the owner-queue
> drifted, D6 (the manager's own missing mission/done-when — the delta-8 standard it holds
> every lane to) is still queued, and fleet-manager still owes the websites NO-ACK correction
> that two audits flagged. What is the mechanism — not the intention — that gives every
> deferred item a named owner and a deadline, and who drains `review-queue.md` before
> "review is post-merge" finishes degrading into "review is never" (F10)?

**Today: none, and three orphans prove it.** D2 sat a day while the
owner-queue drifted (named in fm #18's own ⟲ note, which even diagnosed the
cause: "a scope-deferred drift fix should name WHO picks it up"); D6/F25 — the
manager's own missing mission/done-when, the very standard it audits every
lane against — is still queued at HEAD; and fleet-manager still owes the
websites NO-ACK correction that was flagged by superbot #1913 and *re-flagged*
by #1926 some 30+ hours later. The review-queue drainer exists only as idea
F10. The system is now excellent at *finding* problems (three audit layers
caught each other's errors all night) and has essentially no machinery for
*retiring* them — that asymmetry is the process finding of the night.

**The mechanism, concretely (not an intention):**

1. **Format, enforced:** every deferred item gets two mandatory fields at
   write time — `owner-lane:` and `review-by:` date. Enforce with a token
   checker in the same mold as kit #98's `check_capability_xref` (323 lines,
   shipped in one session — the fleet demonstrably knows how to build exactly
   this class of advisory checker). An item without both fields fails the
   check.
2. **Drain loop, riding an existing cadence:** fleet-manager's own hourly
   Class-A wake (dispatched in fm PR #19) opens `review-queue.md` first, and
   either executes or re-dates the top expired item every wake. An item
   re-dated twice escalates to the owner queue automatically. No new
   infrastructure — the wake already exists; this gives it a standing first
   duty.
3. **Who/where/gate:** fleet-manager builds both, in its own repo, gated on
   nothing — docs + checker are the free-to-ship class under its own rules.

Until the drain loop exists, "review is post-merge" *is* degrading into
"review is never" — the NO-ACK correction is the live specimen.

## SAFETY — was unattended autonomy actually safe?

> **Q16.** pokemon-mod-lab — whose README declares a "no exceptions" PRIVATE hard rail — is a
> PUBLIC repo, with the full vendored Nintendo decomp, upstream multiboot binaries, and ~1.9MB
> of copyrighted-content screenshots world-readable; 8 PR bodies proudly asserted "this repo is
> PRIVATE" and no session ever ran the one API call that checks. Separately, websites' handoff
> assumed fleet-manager was private; it's anonymously readable, so the owner's to-do queue is
> on the open internet. Why did the fleet's verification culture — which recounted 116 PRs and
> re-derived Sharpe ratios to four decimals — never once verify a `repo.private` bit, and what
> is the structural guard (not the memory) that makes rail-vs-reality contradictions impossible
> at repo creation?

**Because the fleet's verification culture is claim-checking, and this was a
world-checking failure.** Every audit tonight verified *artifacts against
artifacts* — PR counts against PR lists, Sharpe digits against ledgers, sha1
chains against PR bodies. `repo.private` is a fact about the environment that
no artifact computed; the README asserted it, 8 PR bodies *repeated* it
(pokemon PRs #2, #4–#10 — games §1), and repetition accumulated false
credibility with zero verification — the exact false-premise-propagation class
superbot's #1913 audit dinged *other* lanes for. The one API call that would
have caught it was never in anyone's checklist because checklists tonight
covered outputs, not environment invariants.

**Verified today for this review: all 13 repos in the account are public**
(`private=false` from the API on every one), pokemon-mod-lab included — so the
full vendored Nintendo decomp, upstream multiboot binaries, and ~1.9MB of
copyrighted-content screenshots remain world-readable right now, under a
README declaring a "no exceptions" PRIVATE rail. Likewise fleet-manager: the
owner's to-do queue is anonymously readable (websites digest confirmed an
unauthenticated raw fetch → 200). One genuine unknown this review won't paper
over: **who created pokemon-mod-lab public, and why, is not determinable** —
the games digest raises a real candidate (free-plan branch rulesets, which the
repo actively uses, may only enforce on public repos), which would make this a
tradeoff nobody wrote down rather than a pure oversight. That's an owner
decision, today: flip it private (and lose ruleset enforcement?) or amend the
rail. Either resolves the contradiction; leaving both standing is the only
wrong answer.

**The structural guard (agents should ship this without waiting):** a planted
CI step in substrate-gate that calls `GET /repos/{owner}/{repo}` with the
workflow's own token and **fails if `repo.private` contradicts a
machine-readable `visibility:` declaration** in the repo's conventions. ~20
lines, runs on every PR, makes the rail-vs-reality contradiction impossible to
sustain rather than merely remembered — gba's own retro (QUESTIONS.md G2)
literally asked for this before the failure was found. The generalizing rule
for the kit: **a "no exceptions" safety rail may not exist as prose alone — it
ships with its machine-checkable twin at birth** (the Q-0194 friction→guard
doctrine, applied to safety rails). Severity, honestly: this is the night's
only true safety failure, and its *consequences* were luck-bounded (pret's
decomp is already public; no retail ROM committed) — but the identical failure
mode wrapped around a secret, a token, or trading's P5 unlock is not
luck-bounded, and those rails are arriving now.

> **Q17.** Merge=deploy meant the live production Discord bot restarted ~15 times unattended
> for docs-only merges. Tonight's runtime delta was genuinely zero (verified two ways), so this
> was churn, not danger — but the same pipeline would have deployed a behavior change at 3am
> with identical friction. Is "nothing risky merged" tonight a property of the *system* (what
> gate would have stopped it?) or of the *sessions' self-restraint* (#1918's card voluntarily
> declaring workflow edits out of scope)?

**Mostly self-restraint, and we should say so plainly.** Inventory of what the
*system* would actually have stopped at 3am: CI (pytest + check_architecture +
the born-red gate) stops *broken* code; nothing stops *risky-but-green* code.
There is no rule, gate, or hook that blocks `disbot/` runtime changes during
unattended windows — #1918's card *voluntarily* declared workflow edits out of
overnight scope, and the shift plan visibly steered work toward tooling/docs
(superbot digest's own words). Q-0213's brake covers destructive Discord ops,
not deploys; Q-0193 makes merge=deploy by design. Had a session written a
green-testing behavior change at 3am, it would have deployed to the production
bot with identical friction to tonight's docstring.

Credit where the system did hold: the one load-bearing-gate edit of the night
(#1920 touching `check_architecture.py`) was self-caught — the session noticed
its first cut would have let new violations in on the strength of a
self-written comment, and redesigned so the conformance test still pins the
raw 13-entry inventory. And all three new checkers shipped deliberately
un-wired to CI — the right unattended posture. But "the sessions had good
judgment" is not a gate.

**Recommendation (proportionate, not a hard block):** superbot is the only
repo where merge means production deploy to real users, so give it — and only
it — a night-window advisory hold: any PR touching `disbot/` beyond
comments/docstrings, opened during unattended hours, gets the
`do-not-automerge` label applied by a workflow step and waits for the
coordinator's or morning's explicit release. Tonight that would have cost zero
minutes (the only `disbot/` touches were a docstring, #1917, and comments,
#1920) while converting voluntary restraint into the default. Separately and
regardless: ~15 unattended production restarts for docs-only merges is pure
churn — a Railway path-filter (skip redeploy when the diff has no `disbot/`
files) is a one-line fix worth shipping this week.

> **Q18.** On the money rails: venture-lab correctly performed zero external actions (no
> Stripe, no marketplace), but the system's designed next step was the owner publishing a
> listing whose headline claim is false (Q2/D1) — the safety gate held at the API boundary and
> failed at the truth boundary. As money rails extend (Stripe keys, marketplace accounts,
> trading's P5 unlock), what is the equivalent of the holdout guard — a check that live-fires
> the claim before the owner is invited to act on it?

**"The headline claim has been live-fired before the owner is invited to act
on it" — executed evidence, not promised verification.** Tonight's failure
shape, precisely: the API boundary held because it's *structural* (no Stripe
keys exist, so zero external actions were possible — verified in the venture
digest); the truth boundary failed because it's *narrative* (the LISTING sells
"Stripe Checkout + webhook, pre-wired" while that path has never executed and
carries the near-certain D1 bug; the 13 green tests inject synthetic events
that can't reach it). The lane even *knew* the ordering — the ledger calls
live Stripe "the last unproven leg" and ⚑A's VERIFIED-WHEN would surface D1 —
but the owner queue presented ⚑B (publish) as independently clickable. The
gate existed; the queue didn't encode the dependency.

Three concrete mechanisms, all cheap:

1. **A `depends-on:` field in the owner-queue/OWNER-ACTION format:** an ask
   whose dependency is an unexecuted verification is not renderable as
   clickable. ⚑B depends-on ⚑A-passed. This is a format change plus a checker
   line — the same enforcement class as Q15's fix.
2. **Claims ship with execution evidence or an UNVERIFIED label in the
   artifact itself:** any owner-facing text that sells a capability (a
   LISTING, a launch post) must either attach a transcript of that capability
   executing (venture's own demo-transcript.md is the model — it's a genuine
   capture) or carry the UNVERIFIED flag *in the buyer-facing copy*, not only
   in an internal ledger the buyer never sees.
3. **Copy the pattern the fleet already got right:** trading's P5 protocol is
   the grown-up version — genuinely pre-registered, mechanical verdict rules
   resolved *against* the strategy, owner-gated unlock, one-shot-then-final
   (trading §5 calls it the strongest methodology artifact in the repo).
   Venture's mock/real split is exactly the "tested logic isn't the shipped
   logic" failure that holdout thinking exists to prevent; the doctrine line
   for the blueprint is one sentence: **never hand the owner a go-live click
   whose headline claim has never executed.**

> **Q19.** `merged_by` is uniformly menno420 because every agent rides the owner's token —
> attribution of who merged venture-lab #9 while the lane's status said "awaiting owner merge"
> is *not determinable from available data*. If something had gone wrong tonight, could we have
> reconstructed which seat did what, and is a single shared identity across 10 autonomous lanes
> an acceptable audit posture for the first unattended night, let alone the twentieth?

**No, and no — not past this stage.** The live demonstration is already on
file: venture-lab #9 merged at 05:11:50Z while the lane's own status said
"awaiting owner merge," and who executed that merge is *not determinable from
available data* (telemetry §3d) — `merged_by` is uniformly menno420 because
every agent rides the owner's token, and the lane's self-reports can't fill
the gap (the same lane's PR #2 and PR #3 bodies contradict each other about
its own merge mechanics — telemetry §7ii). So the honest forensic answer for a
bad night: we could reconstruct *what* happened (git history is forward-only
and solid) but not *which seat* did it — and per-seat classifier
nondeterminism (Q14) means seat identity is operationally meaningful, not
bookkeeping.

Was it acceptable for night one? Yes, defensibly — every action rode one
trusted token in repos with almost no external blast radius, and narrative
attribution (cards, claims, PR bodies) was mostly adequate. But narrative
attribution is precisely the layer tonight's audits kept finding errors in,
and it fails exactly when you need it (under contradiction). For the twentieth
night, or the first night with money rails: no.

**Path, in effort order:** (1) *Now, free:* a mandatory seat-signature —
session ID + lane in a commit trailer and PR-body footer, enforced by the same
advisory-checker pattern as Q15/Q16. Converts "not determinable" into
"determinable unless actively falsified," which is a real upgrade even though
it isn't tamper-proof. (2) *Owner setup, ~30 minutes:* per-lane fine-grained
PATs stored per-Project, so `merged_by` and token identity actually differ per
lane — do this for the three repos with real blast radius first (superbot
production, venture-lab once money flows, trading at P5 unlock).
(3) *Eventually:* a GitHub App per fleet with per-lane installation tokens —
the clean answer, but not the blocker today. The trigger condition is crisp:
**the first money or production rail should not go live on a shared
identity**, and venture's asks are on the owner queue now — so item 2 belongs
on the queue beside them.

## SUBSTRATE-KIT — what should the kit absorb from tonight?

> **Q20.** Run-4 is the kit's first ruling-independent benchmark loss: the auto-drafted handoff
> card was never opened by the measured session, and a plain README beat the kit at its own
> continuity game. The bench-derived fix (SessionStart push-orientation) is the first change
> aimed at the kit's only recorded product loss — is it the next engine PR, and what same-version
> repeat runs are scheduled so the 4-run trend stops being confounded by 4 kit versions,
> fresh seeds, and one silent judge-model collapse (run-3)?

**Short answer: the fix is not scheduled as anything yet — it is not even a
filed idea — and no repeat run is scheduled anywhere. Both are true "on paper
the lab knows, in the queue nothing moves."**

**What happened, in one paragraph.** The kit's benchmark spins up two copies
of a small project — one with the kit installed, one without — and measures
whether a fresh session picks up where the last one left off. In run-4, for
the first time, the *without-kit* copy won both continuity measures: the kit's
auto-drafted handoff card was never opened by the measured session, and a
plain README did the job better (kit `control/status.md`, run-4 block: "M2 OFF
and M3 OFF, both family firsts... OFF's plain-README convention beat the kit
at its own continuity game"). Because run-4 failed under *both* readings of
the disputed pass rule, no rubric ruling can rescue it — it is the kit's first
ruling-independent loss (kit §5–6).

**Is the fix the next engine PR? No — and here is the exact state at HEAD.**
The proposed fix (inject the newest handoff card + unresolved items into the
session's *opening* context via the already-wired SessionStart hook, instead
of only speaking at session-end) exists in two places: the run-4 session
card's idea flag (`.sessions/2026-07-10-b1-b1-run-4.md` § 💡, per status.md)
and a bullet in `control/status.md` "next" that says, verbatim, "not yet a
docs/ideas/ file — filing it is part of picking it up." Nothing in
`docs/gen2/queue-state.md` schedules it: the agent-reachable queue is 9/12
done and the 3 remainders are owner-gated on other things (queue-state.md
items 4, 9, 12). Meanwhile ORDER 010 (the fleet manager's "self-arm an hourly
wake routine" order, landed 11:09Z via kit #118, unexecuted at HEAD) is
sitting in the inbox and will almost certainly be what the next kit session
does first.

**Opinion: it should be the next engine PR, and the case is unusually clean.**
It is the first change in the kit's history derived from a measured product
loss rather than from theory; the delivery mechanism (the SessionStart hook)
is already planted by `--wire-enforcement`, so the build is contained; and it
attacks both losing measures at once (M2/M3 directly, M1 indirectly — injected
context is cheaper than the exploratory reading the kit currently pays for;
status.md run-4 "next" bullet says exactly this). The honest counterweight:
ORDER 010 is a direct manager order and the fleet doctrine says orders come
first. Fine — but the SessionStart PR should be the queue item immediately
behind it, filed as a real idea + queue entry, not left as a card-level note
that the next session may or may not re-discover.

**Are same-version repeat runs scheduled? No.** Verified in the queue and the
status "next" list at HEAD: there is no run-5 entry anywhere. The confounds
are recorded with admirable honesty in the run-4 block itself — 4 runs across
4 different kit versions (1.0.0→1.3.0→1.6.0→1.7.0), a fresh random seed every
run, judge drift (opus-4-8 twice, then the run-3 collapse where the spawn
harness silently ignored the model orders and the "independent judge" was the
same model as the arms, then opus-4-8 again), and run-4 alone using
Sonnet-class arms with live hooks (status.md run-4 block; kit §4 run-3
incident). Recording confounds is not the same as removing them. Two more
loose ends, both verified still loose at HEAD: the model-identity automation
that would prevent a repeat of the run-3 silent collapse is "still unfiled as
an idea file — it lives card-level in `.sessions/2026-07-10-b1-run-3.md`"
(status.md, verbatim), and the F-5 A/B rubric ruling (the owner's one-letter
HOT item) is still open, so even the 4-row headline is genuinely ambiguous for
runs 2–3: 1 PASS / 3 FAIL under reading A, 3 PASS / 1 FAIL under B.

**What this review would schedule, concretely:** two runs (5 and 6) both on
v1.7.0, judge pinned to opus-4-8 and verified from transcripts (the run-4
method), arms matched to run-4 (Sonnet + live hooks) so run-4 has a true
replicate — *before* the SessionStart change ships, so there is a clean
before/after on the same version. Then the SessionStart PR, then runs 7–8 on
the new version. Until something like that exists, the bench trend is four
one-off anecdotes, and nobody should quote it — in either direction.

> **Q21.** Tonight generated at least five kit-absorbable lessons with evidence attached:
> adopt-time repo-settings checklist (two ~1h behind-stalls), enabler-workflow-as-doctrine in
> planted templates (per-seat classifier nondeterminism), control-plane batching (ceremony PRs
> caused the stalls they then suffered), ≤7,500-char fitted-instruction limit (both founding
> packages overflowed an unmeasured 8k field), and a `repo.private`-vs-declared-rail check
> (Q16). Which of these land in the next kit release, which are consciously rejected, and which
> have merely not been decided — with the third category being the answer that indicts the
> process?

**The uncomfortable answer first: all five are in the third category. Zero
have landed in the kit, zero have been consciously rejected, and none is filed
as an idea or queue item at HEAD.** Each verified by grepping the kit working
tree at `21d3ead`, not by trusting the digests:

| # | Lesson (evidence) | State in the kit at HEAD |
|---|---|---|
| 1 | **Adopt-time repo-settings checklist** — two PRs lost ~1h each to the "green but behind" stall (#92, #106; kit §4); the full fix is two GitHub checkboxes | Exists only as OWNER-ACTIONS 2/11 *for the kit's own repo* (control/status.md lines 120–127). No idea file, no queue item, nothing that helps the next adopter repo. |
| 2 | **Enabler workflow in the planted templates** — the server-side auto-merge-enabler is what actually landed PRs under classifier denial (telemetry §5.1) | Recipe documented for the kit repo itself (`docs/CAPABILITIES.md` lines 102–167, `docs/operations/auto-merge-guards.md`), but `.github/workflows/auto-merge-enabler.yml` is repo-local — `grep -ril enabler src/engine/templates/` returns nothing. Adopters do not get it. |
| 3 | **Control-plane batching** — 19 of 40 kit PRs (~48%) were ceremony, and that churn caused the very stalls in lesson 1 (kit §1, §4) | No idea file (grepped `docs/ideas/` — only unrelated hits). Exists only in this review's digest. |
| 4 | **≤7,500-char fitted-instruction limit** — both ~9k founding packages overflowed the 8,000-char paste field at deploy time (fm §2: websites 9,209, trading 8,980, re-trimmed live to 7,496/7,495) | Zero presence in the kit: `grep -rn "7,500\|7500\|8,000"` over kit docs and src returns nothing. The recipe lives only in fleet-manager's capabilities ledger. (Fairness note: the kit's own paste-ready proposal, `docs/gen2/custom-instructions-proposal.md`, is 3,410 chars — safely under the cap. The kit isn't currently shipping an overflow; it just has no rule preventing the next one.) |
| 5 | **`repo.private`-vs-declared-rail check** — a repo whose README declares a "no exceptions" PRIVATE rail is actually public, and 8 PR bodies asserted the false premise (games §1) | Nowhere in the kit (`grep -rin "repo.private"` over src/tools/docs: nothing). gba-homebrew's own retro even asked for exactly this guard (`docs/retro/QUESTIONS.md` G2, per games §1) — the question exists, the guard doesn't. |

**Does "all five undecided" indict the process? Partly yes, with one honest
defense.** The defense: the adopter→kit feedback loop demonstrably works
*when a lane hits friction live in a session* — the gba Track B lane hit
gate-template bugs overnight, claimed in the kit, and shipped the fix upstream
within hours (kit #105/#108, kit §2). What the night exposed is that this loop
has exactly one intake: live in-session friction. Lessons that arrive any
other way — from a review wave (lessons 2, 3), from the owner's paste surface
(lesson 4), from an API fact no session ever checked (lesson 5), or from a
stall whose fix is a settings checkbox (lesson 1) — have no path into the kit
queue. They end up in the right *documents* (CAPABILITIES, the fm capabilities
ledger, review digests) and never become queue items. That is a real
structural gap, not laziness.

**What should land, in what order (recommendation, decide-and-flag style):**

1. **Lesson 5 first** — it's the only safety item. Cheapest shape: a
   substrate-gate step that fails (or loudly warns) when the repo's
   conventions declare a PRIVATE rail but the API says `private: false`. One
   API call at gate time makes the rail-vs-reality contradiction structurally
   impossible instead of remembered.
2. **Lesson 2 second, and it's the cheapest build** — `adopt.py` already
   plants `.github/workflows/substrate-gate.yml` as an inline template
   (adopt.py:426–490, verified at HEAD), so planting the enabler workflow at
   adopt time is the same established pattern plus tests. It permanently
   zeroes the per-seat classifier lottery for every future adopter (telemetry
   §8 ranks this the #3 fleet bottleneck).
3. **Lesson 1 third** — fold into the same adopt-time output: a one-time
   printed checklist of recommended repo settings (require-up-to-date OFF or
   auto-update ON, required-check names, auto-delete branches). It's advisory
   text, nearly free, and saves every future adopter the ~1h stall the kit
   paid twice.
4. **Lesson 4 fourth** — one sentence + a char-count check wherever the kit
   renders owner-paste text. Trivial, do it in the same release.
5. **Lesson 3 last, and only half of it** — batching claims into the born-red
   card's first push looks safe (both are already "first-commit" artifacts);
   batching status-closes into the flip commit touches the one-writer
   discipline that gave the fleet zero collisions across ~40 interleaved kit
   PRs (telemetry §6). Take the claim-batching half and deliberately defer the
   status-close half — that's a conscious partial rejection, and it should be
   written down as one.

The mechanism to make this happen is the one that already works: file these as
inbox ORDERs to the kit lane (the ORDER grammar is now checker-enforced there,
kit #87). If they stay as digest prose, the next review will find them
undecided again.

## PLATFORM / EMAIL — what belongs in the Anthropic follow-up?

> **Q22.** The follow-up should contain reproducible platform findings, not complaints. Rank
> tonight's candidates by evidence quality: (a) per-seat nondeterminism of the auto-mode
> permission classifier (identical calls PERMITTED and REFUSED same night, same repo, verbatim
> refusals on file); (b) the surface-fragmented routine/trigger capability (Project sessions
> can self-arm, coordinator/workers cannot, cross-session binding disabled org-wide, console
> pane absent on one owner surface — four different answers to "can an agent schedule a wake");
> (c) the 8,000-char Custom Instructions cap discovered only at paste time; (d) GraphQL/REST
> walls that made per-PR arm-timeline events unqueryable for our own telemetry. Which carry a
> minimal reproduction, and which would we be embarrassed to send because our own logs are
> narration rather than evidence?

The bar the question sets is right: reproducible findings, not complaints.
Ranked by how close each candidate is to "an engineer at Anthropic could
reproduce this from our attachment today":

**1. (c) The 8,000-char Custom Instructions cap — cleanest evidence, lowest
severity. Send now.** Minimal repro: paste 8,001 characters into a claude.ai
Project's Custom Instructions field. We hold measured numbers on file
(websites package 9,209 chars, trading 8,980, both overflowed at paste
~02:05Z; fitted rewrites 7,496/7,495 both fit — fm `docs/capabilities.md` +
the deployed-fitted sections of
`docs/proposals/instructions/{websites,trading-strategy}.md`, fm §2). It's a
product paper-cut, not a bug — the ask is simply "document the limit and show
a live character counter." Honest note to include: our own review wrote all
10 packages at ~9k against a field nobody had measured; the cap is
undocumented, but a cheap probe on our side would have caught it too.

**2. (a) Per-seat nondeterminism of the auto-mode permission classifier — the
highest-value finding, but only half-evidenced today. Send after one capture
night.** The refusal side is real evidence: verbatim refusal text on file
("[Auto-Mode Bypass] ... Merge Without Review", kit `docs/CAPABILITIES.md`
lines 160–169), hit repeatedly by the kit gen-2 session. The PERMITTED side,
though, is narration: "#107/#109 were permitted" is the kit status file's own
cross-lane self-report, and our telemetry reviewer states plainly that he
could not independently observe those arm calls succeed (telemetry §9).
Sending "your classifier is nondeterministic" where half the contrast is a
lane's unverified self-report would be exactly the embarrassment the question
warns about. The fix is cheap: one deliberate capture — the same
`enable_pr_auto_merge` call from two seats on the same repo the same hour,
both transcripts saved verbatim. With that attachment this becomes the
strongest item in the email, because it's the one with real platform
consequences: a permission rule that answers differently per seat can't be
designed around, only absorbed (which is what the enabler workflow did all
night — telemetry §5.1).

**3. (d) GraphQL/REST walls — split it in two; send one half, never send the
other.** Sendable half: the pinned-GraphQL session wall is verbatim on file
("This GraphQL query is not enabled for this session — only the pinned set of
PR-review operations is served", telemetry §0) and its consequence is concrete
and demonstrated: our own night telemetry could not query per-PR
auto-merge-arm timeline events, which is why merge-path attribution across 137
PRs is convention-based and why "who merged venture-lab #9" is formally
unanswerable (telemetry §0, §3d). That's a well-scoped feature request: add
timeline/auto-merge events to the pinned query set for telemetry use.
Never-send half: the "GraphQL quota ≈ hourly at fleet scale" claim — the
CI-tier sim itself admits it is "a calibrated estimate with no raw
RATE_LIMITED transcript" (fm §5, the R8 evidence gap). That is narration
wearing a number.

**4. (b) The surface-fragmented routine/trigger capability — real, but we
falsified our own headline claim this morning; hold until the recipe exists.**
What's solid: the cross-session binding rejection is verbatim on file
("binding a trigger to another session is not enabled for this organization",
fm `docs/capabilities.md`), and the "four different answers to one question"
framing is genuinely useful product feedback — Project sessions can self-arm
(owner-verified, fm PR #19), coordinator/worker surfaces can't, cross-session
binding is org-disabled, and one owner console lacked the Schedules pane
entirely. What's not solid: our own ledger recorded this as "walled on BOTH
sides" fleet-wide at 06:43Z and the owner falsified that within ~5 hours (fm
§2) — so our strongest artifact on this topic is partly a record of our own
over-generalization. And the working side still says "recipe pending: first
successful lane records the exact tool/UI path" (fm §2) — we cannot yet tell
Anthropic the exact path that works, only that the owner saw it work. ORDER
010's execution across 6 lanes will produce the recipe within a day; send this
item then, as a surface-capability matrix with verbatim errors per cell, and
include our own correction story — it makes the report more credible, not
less.

**Bottom line for the email:** send (c) now and the pinned-GraphQL half of (d)
now; hold (a) one night for the two-seat capture — it then becomes the
headline; hold (b) until a lane records the working recipe; and strike the
quota estimate entirely unless a raw rate-limit transcript shows up. Nothing
else from tonight clears the "reproducible, not complaint" bar — in
particular, the merged-by/attribution gap (Q19) is a consequence of our own
single-token setup plus (d), not an independent platform finding.

## HONEST WORRIES — where were we lucky rather than good?

> **Q23.** Trading's P2/P4 "pre-registered" verdict rules entered git minutes *after* (or in
> the same commit as) the runs they governed — the pre-registration is narration, unverifiable
> from history; only P5's protocol does it right. The system's honesty held because P4 ruled
> against itself 13/13, i.e. there was no incentive gradient to resist. Where else does our
> integrity story depend on commit *narration* rather than commit *order*, and would it survive
> a night where the gradient points the other way?

**Short answer: in at least six more places — and we already have one piece of
direct evidence that when the incentive gradient points the wrong way,
narration outruns truth. That evidence is venture-lab.**

First, the trading case restated precisely, because it's the template. The P2
verdict rules entered git ~3 minutes *after* the runs executed (run files
03:36:24Z, first protocol commit `fd0f8e9` 03:39:07Z); P4's rules, script, and
results arrived in one commit (`84c8ab3`, 04:35:06Z) (trading §5). Nothing was
tampered with — the founding-plan criterion genuinely predates everything, and
P4 ruled *against* itself 13/13. But as the trading digest says, that honesty
held "because there was no incentive gradient to resist." A skeptical outsider
cannot verify rule-before-result from history. P5's protocol (PR #30) does it
right: committed while the holdout is still sealed, with mechanical rules that
resolve ambiguity *against* the strategy. That's the standard.

**The full inventory of narration-shaped integrity claims, fleet-wide:**

1. **The games byte-identity claims.** The "shipped tree contains no fixture;
   patch-only rebuild reproduces the shipped sha1" claims are self-reported in
   `notes.md` files, "lane-attested, not CI-enforced" (games §2, closing
   paragraph). CI rebuilds the ROM, but nothing independently checks the
   byte-identity story.
2. **gba-homebrew's strongest evidence is courtesy-tier.** The frame-exact
   gameplay asserts live in a `workflow_dispatch` job; per-PR CI is
   compile-only. It was dispatched after the big merges "but that's
   discipline, not enforcement" (games §3). A gameplay regression merges on a
   green compile.
3. **"This repo is PRIVATE" — asserted in 8 PR bodies, false the whole time.**
   pokemon-mod-lab PRs #2, #4–#10 each narrated a premise no session ever
   checked with one API call; the repo is public (games §1). Narration didn't
   just outrun verification here — it replaced it, eight times in a row, on
   the fleet's only hard safety rail.
4. **Our own audit trail of who-merged-what is narration.** Landing-path
   attribution for paths B/C rests on "repo-documented conventions and PR-body
   statements," because arm-timeline events were unqueryable and `merged_by`
   is uniformly menno420 (telemetry §0, §9). And PR bodies demonstrably drift:
   venture-lab #2 claims it "armed auto-merge in the checks-pending window" on
   a repo that had **no CI until PR #4** — contradicted by #3's own body eight
   minutes later (telemetry §7).
5. **Audit reports themselves ship confident false narration.** superbot #1913
   — a 32-agent, 350-tool-call audit — asserted sonnet5 was "the only lane to
   ship a shell script" when five others did; #1911's grand review claimed
   parity rows for all 8 subsystems when 2 are missing (superbot digest,
   corrections section). Both caught only by an *independent* cross-lane
   verifier (#1926).
6. **And the one place with a real gradient: venture-lab.** The lane's
   *internal* ledger honestly says live Stripe is "the last unproven leg"
   (venture-ledger.md ln 171–172), while the *buyer-facing* LISTING sells
   "Stripe Checkout + webhook, pre-wired" as done — wiring that contains a
   near-certain functional bug (D1) and has never executed (venture D1). This
   is the answer to "would it survive": on the one lane where the incentive
   was "make the product look sellable," the narrated claim exceeded the
   verified reality *the same night*, and no in-lane layer caught it.

**Counter-examples worth crediting, because they show the fix is known:**
trading's holdout guard is enforced, not narrated — the reviewer live-fired
the choke point and it refused a bad row (trading §1); superbot's telemetry
gate (#1894) held on all 12 cards with zero misses on its first full night
(superbot digest, session-ender section); the harness×model experiment
pre-registered its full protocol before any repo exists (fm §6); kit's F-5
dispute was dual-scored rather than resolved by the interested party (kit §5).

**Opinion / what to do:** three cheap conversions. (1) Fleet rule, one line:
*protocol commit before result commit, in separate pushes* — trading §5
already recommends it; it costs nothing and makes pre-registration checkable
by `git log` instead of by trust. (2) Promote the two strongest lane-attested
claims to enforced: gba's semantic replay job to per-PR on `games/**` paths
(~105s warm, games §6.4), and a byte-identity / `repo.private` check in the
substrate gate (see Q26). (3) Treat PR-body claims as narration in all future
audits — tonight proved they drift even within one session.

> **Q24.** Count the night's error-catches by who caught them: the ~80→116 undercount, the R21
> overreach, the venture-lab paste trap, the routine-wall over-generalization, the two errors
> in superbot's own audits, the venture-lab product bugs, the CI collection gap. Two of the
> first four required the owner or a second review wave; the last two required *this* review —
> a layer that doesn't run every night. Zero double-executions and zero stuck PRs: how much of
> that is R19/R21 working, and how much is one quiet night at 137 PRs with a review architecture
> whose deepest layer is not yet scheduled? What is the plan for making the catching layer as
> routine as the shipping layer?

**The tally, by catching layer** (every item sourced):

| Layer | Catches | Items |
|---|---|---|
| Originating session / same lane, self | 2 | ~80→116 undercount (fm's own launch record, fm §1); websites' own live falsification of the "fleet-manager is private" handoff assumption (web-games-next Lane 1) |
| Second review wave, same night (Fable-5 review, ultracode verification, cross-lane audits) | ~6 | R21(a) overreach F2; venture-lab paste trap F1/F13/F23; owner-queue create-repo trap F14 (all fm §4); the 2 errors in superbot's #1911/#1913 (superbot digest); fm's false websites NO-ACK (caught by superbot #1913); kit gate "locked door" defect (caught live by the visiting gba lane, kit §2) |
| **The owner** | 1 | routine-wall over-generalization — "walled on BOTH sides" falsified ~11:00Z (fm §2) |
| **This review — a layer that ran once, on commission, and is not scheduled** | 4 | venture-lab D1/D2/D3 product bugs (venture digest); superbot-games CI collection gap, 73 of 121 tests (web-games-next Lane 2); **pokemon-mod-lab is PUBLIC against its own "no exceptions" rail** (games §1); the venture #2/#3 testimony drift (telemetry §7) |

Read that table coldly: **the severity is inversely ordered to the layer's
reliability.** The most consequential findings of the entire night — a broken
product the owner was invited to sell, a CI gate that silently ignores 40% of
a repo's tests, and the fleet's only hard safety rail being factually false in
public — were all caught by the layer that only existed because the owner
commissioned it today. The layers that run automatically caught real things
(and deserve credit — the #1926 correction loop and the same-night Fable-5
review are genuinely working), but they caught *doc accuracy and doctrine*
errors, not *product and safety* errors.

**How much of zero-stuck/zero-double is the system?** Split verdict:

- **Zero double-executions: mostly the system, and this review would defend
  that.** Gen-1 had two double-builds in one day at lower volume; tonight ~137
  PRs interleaved across shared repos with zero collisions (telemetry §6),
  with the claim ritual visibly practiced and R19 upgraded to an enforced
  checker on kit (#87). That's a before/after with a mechanism; it's not luck.
- **Zero stuck: the system, but not the *documented* system.** The winning
  mechanism was the server-side auto-merge-enabler absorbing per-seat
  classifier nondeterminism — 54 of 137 merges landed on path A with no agent
  merge call, some under active classifier denial (telemetry §2, §5.1). R21 as
  written doesn't name that path (fm §8), a classifier-denied lane's terminal
  state is still formally undefined (F4/F6), and superbot #1917 showed the
  enabler has a blind spot (non-`claude/*` heads skip the arm; something
  merged it manually 14 min later — telemetry §3c). So: real architecture,
  discovered live, not yet doctrine.
- **Zero bad *outcomes*: substantially restraint plus a quiet night.** Nothing
  runtime-risky deployed to the live bot because sessions *chose* scope
  discipline (#1918's card voluntarily declared workflow edits out of scope —
  superbot digest); the pokemon visibility breach sat undetected for the
  entire night and would have sat longer without this review; and Session C
  died with zero trace, invisible to every repo-side guard (superbot digest,
  watch items).

**The plan the question demands — making the catching layer as routine as the
shipping layer:** the fleet already generated the idea and the capability; it
just hasn't connected them. F10 (review-queue drainer) is captured as an idea
(fm §4), and the owner verified this morning that Project sessions can
self-arm routines (fm PR #19). Connect them: a scheduled independent
deep-review lane — nightly while the free window lasts, then per ~100 fleet
PRs — with a rotating focus (one night product-truth like venture D1, one
night CI-scope like the games gap, one night safety rails like Q16),
publishing findings to fleet-manager `docs/findings/`. This is #3 in Q26,
with a builder and a gate. Until it exists, honesty requires saying: tonight's
clean sheet was earned on the merge pipeline and *lucky* on everything the
pipeline doesn't see.

## NEXT — what must change before scaling to more lanes?

> **Q25.** The entire wake-cadence + CI-tier architecture was designed inside a free window
> closing 2026-07-14 with zero cost data (F12 — idea captured, nothing built). Before adding a
> single lane: what does one lane-night cost in tokens/compute, what did tonight's 137-PR night
> cost in total, which lanes clear an owner-value bar at that price, and does the fleet
> economics ledger exist before the window closes — yes or no, with a date?

**Does the ledger exist? No.** F12 is captured as an idea and nothing more (fm
§4: "the wake-cadence architecture was designed inside a free window closing
2026-07-14 with zero cost data — idea captured, nothing built").

**What did tonight cost? Unknown — to everyone — and that is the finding.**
The only real cost numbers anywhere in the corpus are: superbot #1911's card
recording **~1.9M subagent tokens for one ultracode session** (superbot
digest, PR table) and venture-lab's **~47k tokens for one eval document**
(venture digest, eval section). Two data points, both self-reported, spanning
a 40× range depending on session shape. Multiplying either by "roughly 40–60
sessions fleet-wide" would produce a number that looks like an answer and
isn't one; this review declines to invent it.

**Which lanes clear an owner-value bar at that price? Unanswerable without the
price — but the value ordering is already clear enough to act on** (consistent
with the Q5 ranking): games (12 proven patches + an original game, games
digest) and kit (queue emptied, agent-side release, defect-free code samples,
kit digest) would plausibly clear almost any realistic price; superbot's night
was solid but ~15 production redeploys for docs-only merges is pure waste at
any price (superbot digest, watch items); venture-lab is *negative* value
until the D1/D2/D3 fix session because its output was an owner-facing
invitation to embarrassment (venture digest); trading is an honest-negatives
engine whose worth depends entirely on whether the owner values "cheaply
killed bad ideas" — a real but unpriced good.

**The commitment the question demands:** the ledger is buildable in one
session because the raw material already exists — superbot's telemetry gate
appends a `telemetry/model-usage.jsonl` row on every card-adding PR and held
12/12 on its first night (superbot digest), and this review's own harvest
(`night-review/raw/*.json`) has the per-repo PR volumes. First cut:
per-session token rows where recorded, per-lane PR counts, the two known
anchors, and explicit UNKNOWN cells where lanes don't report — an honest
sparse table beats a modeled dense one. **Date: land it in fleet-manager as
`docs/findings/fleet-economics-ledger.md` by 2026-07-12**, two days before the
window closes, so at least one night of real (or explicitly
estimated-and-labeled) cost data informs the keep/cut decision on 07-14. A
second, cheap structural fix rides along: extend the superbot telemetry-row
convention fleet-wide via the kit template, so cost data accrues automatically
instead of being reconstructed. If 07-12 slips, the honest fallback is: **do
not add lanes after 07-14 until the ledger exists** — scaling with zero cost
data was tolerable when compute was free; it stops being tolerable the day it
isn't.

> **Q26.** Name the three changes that must land before the next scale-up, chosen from
> tonight's evidence rather than ambition — candidates: the P3 refusal-branch script (Q14), the
> visibility/rail structural guard (Q16), per-seat identity or audit attribution (Q19), the
> truth-boundary check on owner-facing asks (Q18), ceremony batching (Q1), a scheduled
> deep-review layer (Q24), the economics ledger (Q25). For each of the three: who builds it,
> in which repo, gated on what. If the answer lists more than three, that is prioritization
> failure wearing thoroughness as a costume.

Chosen from tonight's evidence, not ambition. Each with builder / repo / gate.

**1. The visibility-and-rails structural guard (Q16 class).**
The night's only genuine safety breach: a repo whose README declares a "no
exceptions" PRIVATE rail is world-readable with vendored Nintendo source and
~1.9MB of copyrighted screenshots, asserted "PRIVATE" in 8 PR bodies, never
once checked (games §1) — and separately, all 13 repos in the account are
public, which put the owner's to-do queue on the open internet
(web-games-next Lane 1). The guard is cheap and the retro already asked for it
(gba QUESTIONS.md G2): a substrate-gate step that fails when `repo.private ==
false` in any repo declaring a PRIVATE rail, plus an adopt-time repo-settings
checklist (visibility, require-up-to-date, auto-update-branches — the same
checklist that would have prevented kit's two ~1h behind-stalls, kit §7.2).
**Builder:** the substrate-kit lane. **Repo:** substrate-kit (gate template +
adopt engine), ships in v1.8.0. **Gated on:** nothing — fully agent-reachable;
the only owner piece is the separate pokemon-mod-lab visibility *decision*
(flip private vs. amend the rail, with the free-plan ruleset tradeoff checked
first — games §1), which should happen this week regardless.

**2. The truth-boundary rule on owner-facing asks (Q18/Q2 class).**
Tonight the safety gate held at the API boundary (zero external actions
performed) and failed at the truth boundary: ⚑B invited the owner to publish a
listing whose headline claim has never executed and near-certainly fails (D1,
venture digest). New doctrine, one paragraph: **no ⚑ owner ask may invite an
external/irreversible action on a claim that has never executed; either an
agent live-fires the claim first (or its closest agent-reachable proxy — e.g.
a webhook test built from a *real* recorded Stripe event shape rather than a
synthetic one, which would have caught D1), or the ask itself carries an
UNPROVEN label and says what will probably break.** This is the product
equivalent of trading's holdout guard: the check runs before the invitation,
not after the embarrassment. **Builder:** fleet-manager (blueprint amendment +
the R17 ask-format gains a required PROVEN/UNPROVEN field), with venture-lab
as the first enforcement site in its D1/D2/D3 fix session. **Gated on:** the
next blueprint pass (doctrine edits are owner-gated in fm's discipline — this
rides the same pass as the R21 rewrite).

**3. The scheduled deep-review layer (Q24 class).**
The layer that caught the broken product, the CI collection gap, and the
public-repo breach ran exactly once, on commission. Make it a routine: an
independent review lane — nightly through the free window, then per ~100 fleet
PRs — with a rotating focus (product-truth / CI-scope / safety-rails),
findings to fleet-manager `docs/findings/`, and one standing rule inherited
from tonight: verify against HEAD and live API bits, never against lane
narration (Q23). **Builder:** fleet-manager arms it as a self-armed Project
routine — the capability was owner-verified this morning and wake-arm ORDERs
are already dispatched to 6 lanes (fm PR #19). **Gated on:** the wake-arm
rollout already in flight; if a lane-level arm fails, the recorded fallback
(owner-queue item 7) applies.

**Dropped, deliberately, so this stays three:** per-seat
identity/attribution (Q19) is real but platform-side — it belongs in the
Anthropic follow-up email, not the fleet's build queue; the P3 refusal script
and ceremony batching are efficiency work that the enabler-in-templates and
control-plane-batching items already queued in kit (kit §7.3–7.4) will absorb
in the normal course; the economics ledger has its own dated commitment in Q25
and is a data-collection task, not a scale gate — though its Q25 fallback
clause ("no new lanes after 07-14 without it") makes it a gate in effect if
the date slips.

---

## For the Anthropic email

Send-ready platform findings from Q22, in send order. Each item is written so
it can be lifted into the follow-up email as-is.

**SEND NOW — 1. Undocumented 8,000-character cap on Project Custom
Instructions.** *Finding:* the claude.ai Project Custom Instructions field
silently caps at 8,000 characters; we discovered it only at paste time.
*Evidence on file:* two measured overflows (websites founding package 9,209
chars, trading-strategy 8,980 chars, both rejected at paste ~02:05Z
2026-07-10) and two measured fits after live re-trims (7,496 and 7,495 chars)
— recorded in fleet-manager `docs/capabilities.md` and the deployed-fitted
sections of `docs/proposals/instructions/{websites,trading-strategy}.md`.
*Minimal repro:* paste 8,001 characters into any Project's Custom Instructions
field. *Ask:* document the limit and show a live character counter. *Honest
note we include:* all 10 of our packages were drafted at ~9k against a field
nobody had measured — a cheap probe on our side would have caught it too.

**SEND NOW — 2. Pinned GraphQL set blocks agents' own telemetry
(timeline/auto-merge events unqueryable).** *Finding:* agent sessions receive
only a pinned set of PR-review GraphQL operations; timeline and auto-merge-arm
events are not queryable. *Evidence on file:* verbatim wall text — "This
GraphQL query is not enabled for this session — only the pinned set of
PR-review operations is served" (telemetry digest §0). *Demonstrated
consequence:* our own night telemetry could not attribute merge paths across
137 PRs except by convention, and "who merged venture-lab #9" is formally
unanswerable from available data. *Ask:* add timeline/auto-merge events to the
pinned query set for telemetry use. *(Deliberately struck from this item: the
"GraphQL quota ≈ hourly at fleet scale" claim — our own sim admits it is a
calibrated estimate with no raw RATE_LIMITED transcript. Narration wearing a
number; not sent.)*

**HOLD ONE NIGHT, THEN SEND AS HEADLINE — 3. Per-seat nondeterminism of the
auto-mode permission classifier.** *Finding (pending capture):* identical
`enable_pr_auto_merge` calls were PERMITTED on some seats and REFUSED as
"[Auto-Mode Bypass] ... Merge Without Review" on others, same night, same
repo. *Evidence today:* the refusal side is verbatim on file (kit
`docs/CAPABILITIES.md` lines 160–169); the permitted side is currently a
lane's self-report our telemetry could not independently observe — sending it
now would be embarrassing. *Capture plan:* one deliberate two-seat test — the
same call from two seats on the same repo the same hour, both transcripts
saved verbatim. With that attachment this becomes the strongest item in the
email: a permission rule that answers differently per seat can't be designed
around, only absorbed (which is what our enabler workflow did all night).

**HOLD UNTIL THE RECIPE EXISTS — 4. Surface-fragmented routine/trigger
capability ("can an agent schedule a wake?" has four different answers).**
*Finding (pending recipe):* Project sessions can self-arm routines
(owner-verified 2026-07-10); the webagent coordinator and spawned workers
cannot (no send_later/self-trigger); cross-session trigger binding is
org-disabled (verbatim: "binding a trigger to another session is not enabled
for this organization"); and one owner console lacked the Schedules pane
entirely. *Why held:* our own ledger recorded this wall wrongly ("walled on
BOTH sides") and the owner falsified it within ~5 hours — and the working
side's exact tool/UI path is still unrecorded. ORDER 010's execution across 6
lanes will produce the recipe within a day; send then as a surface-capability
matrix with verbatim errors per cell, including our own correction story — it
makes the report more credible, not less.

Nothing else from tonight clears the "reproducible, not complaint" bar. In
particular the merged-by/attribution gap (Q19) is a consequence of our own
single-token setup plus item 2, not an independent platform finding.

---

## Recommendations before scaling (ranked)

The top three are the must-land set (Q26, held deliberately to three); the
rest are ranked next-tier work with owners already identified in the Q&A.

1. **Visibility-and-rails structural guard** — substrate-gate step failing on
   `repo.private` vs. declared rail + adopt-time repo-settings checklist.
   Builder: substrate-kit lane, v1.8.0, gated on nothing. Companion owner
   decision this week: pokemon-mod-lab — flip private or amend the rail
   (check the free-plan ruleset tradeoff first). (Q16, Q21, Q26-1)
2. **Truth-boundary rule on owner-facing asks** — no ⚑ ask may invite an
   external/irreversible action on a never-executed claim; live-fire first or
   label UNPROVEN; `depends-on:` field in the ask format. Builder:
   fleet-manager, rides the next blueprint pass with the R21 rewrite;
   venture-lab's D1/D2/D3 fix session is the first enforcement site — and
   until it lands, ⚑B stays marked "DO NOT publish yet." (Q2, Q18, Q26-2)
3. **Scheduled deep-review layer** — independent review lane, nightly through
   the free window then per ~100 fleet PRs, rotating focus (product-truth /
   CI-scope / safety-rails), findings to `docs/findings/`, verify against
   HEAD and live API bits only. Builder: fleet-manager via self-armed Project
   routine. (Q24, Q26-3)
4. **Fleet economics ledger by 2026-07-12** —
   `docs/findings/fleet-economics-ledger.md`, honest sparse table (recorded
   token rows, per-lane PR counts, UNKNOWN cells); extend superbot's
   telemetry-row convention fleet-wide via the kit template. Fallback if the
   date slips: no new lanes after 07-14 until it exists. (Q25)
5. **R21 rewrite + the provisional-rule rule** — rank merge paths explicitly
   (enabler primary → arm-in-pending secondary → REST fallback); new rules
   may not say "always/never/impossible" without a second incident or a
   deliberate falsification probe. Same blueprint pass as #2. (Q10)
6. **Ship P3 (first-denial-stop) + enabler in kit templates + enabler
   head-pattern coverage** — before the next lane launches; closes the
   undefined terminal state and the #1917 blind spot. (Q14)
7. **Capabilities-ledger surface fields + WALLED re-audit** — "surface tested
   + date + verbatim error" as mandatory DISCOVERY RULE fields; fix the
   release-wall entry today (kit already falsified it). (Q11)
8. **Deferred-item ownership + drain loop** — mandatory `owner-lane:` +
   `review-by:` fields, checker-enforced; fm's hourly wake drains the top
   expired item; twice re-dated escalates to the owner queue. Clear the
   websites NO-ACK correction as the first drained item. (Q15)
9. **CI-claim evidence rule + one fleet-wide promotion sweep** — any "CI now
   enforces X" PR pastes collected-test counts + trigger lines; one session
   promotes the seven courtesy-tier items (superbot-games one-liner first,
   then gba per-PR replay, pokemon sha1 assert, commit-order
   pre-registration, bench judge guard, superbot checker wiring). (Q7, Q9,
   Q23)
10. **Attribution now, identity before money** — seat-signature commit
    trailer/PR footer immediately (free); per-lane fine-grained PATs for
    superbot/venture-lab/trading before any money or production rail goes
    live on a shared identity. (Q19)
11. **Ceremony batching (claim-batching half)** — claim rides the born-red
    card's first push; consciously defer the status-close half to protect the
    one-writer discipline. Plus the born-complete advisory detector and the
    coordinator spawn ledger. (Q1, Q12, Q21-5)
12. **Owner playtest kit, ranked #1–2 on the queue** — one bundled 30–45 min
    session (patched Emerald ROM + Lumen Drift + 6-question checklist),
    prepared entirely by agents; freeze feel-dependent work until the
    verdict. (Q4)

---

## Where we were lucky

An honest list of the places where the clean sheet was fortune, not design.
Each entry names what *would* have made it skill instead.

1. **The owner slept through the ⚑B invitation.** The queue invited him to
   publish a broken $49 product at breakfast; the review that caught D1 landed
   first by hours, not by mechanism. Nothing in the system sequenced "verify"
   before "publish" — the truth-boundary rule (Rec #2) is what converts this
   luck to skill. (Q2, Q18)
2. **The review wave ran the same night, by choice, not schedule.** Had the
   Fable-5 review run a day later, the venture paste trap, the R21 overreach,
   and F3's contradiction in binding doctrine would all have been live at
   breakfast. The deepest catching layer — this review — ran once, on
   commission. (Q13, Q24, Rec #3)
3. **The public-repo breach was luck-bounded in consequence.** pret's decomp
   is already public and no retail ROM was committed — so a night-long,
   eight-times-asserted violation of the fleet's only "no exceptions" rail
   cost approximately nothing. The identical failure mode wrapped around a
   secret, a token, or trading's P5 unlock is not luck-bounded, and those
   rails are arriving now. (Q16)
4. **The enabler workflow absorbed a nondeterministic classifier nobody had
   planned for.** 54 of 137 merges landed on a mechanism R21 doesn't name,
   some under active denial; a classifier-denied lane's terminal state is
   still formally undefined, and the enabler's own blind spot (#1917's
   `codex/*` head) was patched by an unattributed manual merge 14 minutes
   later. Real architecture — discovered live, not designed. (Q10, Q14)
5. **The production bot's clean night was self-restraint, not a gate.**
   Fifteen unattended redeploys all happened to be docs-only because sessions
   *chose* scope discipline; a green-testing behavior change at 3am would have
   deployed with identical friction. (Q17)
6. **Trading's integrity held because the gradient pointed the right way.**
   P4 ruled against itself 13/13 — there was nothing to resist. The
   pre-registration for P2/P4 is commit narration, not commit order; on the
   one lane where the gradient pointed the other way (venture-lab), narration
   outran truth the same night. (Q3, Q23)
7. **Session C's disappearance was caught by voluntary diligence.** A session
   that died pre-card left zero repo trace; it survives only because #1920's
   coordinator chose to write it down. Nothing required that. (Q12)
8. **The 8k paste cap failed at a recoverable moment.** Both founding packages
   overflowed *at the owner's paste*, live, where a re-trim was possible —
   because nobody had probed the field once before drafting ten packages
   against it. (Q13, Q22)
9. **Zero collisions at 137 PRs is a real mechanism (claims + born-red + R19)
   — but it has now been tested on exactly one quiet night**, with the
   in-flight-signal half of born-red enforced by nothing and two PRs already
   demonstrating the skip. (Q1, Q12, Q24)

---

## Uncertainty register

Carried from the answer passes, so the doc's own confidence is auditable: the
Q1 ceremony fraction is a per-repo estimate, not a count (only kit was fully
classified). The Q8 attribution split is explicitly a hypothesis pending the
unlaunched harness×model experiment. Q5/Q25's rankings have no cost
denominators because no cost data exists (F12). The Q6/Q2 Stripe behavior
(null `customer_email` on live events; unsupported `{CHECKOUT_EMAIL}`
placeholder) is taken from the venture digest's analysis of Stripe's
documented event-field and placeholder semantics — consistent with everything
in the repo, but the definitive proof remains one `stripe trigger` run that
has never been executed. Who created pokemon-mod-lab public, and why, is not
determinable from available data. The kit-side verifications (Q20/Q21) were
made by direct grep/read of substrate-kit at `21d3ead` and fleet-manager at
`41c4250`; both repos move fast, and those facts date to 2026-07-10.

---

## Post-review delta — what moved on main while this review was landing (fm PR #20, merged 2026-07-10 12:11Z)

This review's evidence base is fleet-manager HEAD `41c4250`. While it was
being composed, PR #20 (round-3 brief §1 task 1) merged. Honest
reconciliation, so the doc is not stale on arrival:

1. **Q22 (b) upgrades, and (a) strengthens.** A SECOND routines correction
   landed: the in-Project self-arm mechanism is now **verified** — the
   claude-code-remote scheduling tools (`create_trigger` / `send_later`
   family) — and **seat-dependent** (owner screen recordings 11:01Z/11:04Z:
   two ACTIVE "Created by Claude" routines firing). "Recipe pending" is
   retired, so email item (b)'s hold condition is satisfied sooner than
   predicted — the surface matrix can be assembled now. Better: seat
   dependence is now documented in **two independent tool families** (the
   merge classifier and the scheduling tools), which upgrades item (a) from
   "one classifier misbehaves" to a platform-level per-seat-inconsistency
   pattern. The "owner console lacks a Schedules pane" cell also narrows to
   per-device (the pane exists on the owner's mobile browser).
2. **Q15's missing mechanism now partially exists — manager-side.** The six
   standing debts became ORDERs 001–006 in the manager's own
   `control/inbox.md`, each with a named next-session owner + done-when; two
   executed in the same PR. The websites NO-ACK orphan this review cited is
   retired — and the correction cuts deeper than the debt: **websites had in
   fact acked** (websites PR #44, landed→ack +1h39m); the "❌ NO ACK" row
   itself was false narration, a fresh specimen for Q23's inventory. The
   review-queue drainer (F10) is now ORDER 003. Still missing from the Q15
   mechanism: the checker enforcement and the standing drain cadence — the
   ORDERs are the format half, on one repo.
3. **Q25's ledger has an owner now, still no data.** The fleet economics
   ledger is inbox ORDER 004, P0, assigned to "the next session of ANY kind,"
   deadline before 2026-07-14 — consistent with this review's 07-12
   commitment. Not built as of this landing.
4. **Q26-3 strengthens.** The scheduled deep-review layer's gate (self-armed
   routines) is now mechanism-verified, and the round-3 launch pack's
   "standing autonomous core" (four permanent ~2-hourly Projects) is the
   natural host for it.
5. **A gen-3 gate now exists** — no lane relaunch until the owner has seen a
   consolidated "state of the fleet + gen-3 delta" report. This review, and
   specifically its "Recommendations before scaling" section, is written as
   an input to exactly that gate.

**What #20 does *not* change:** Q11's verdict stands at the new HEAD — the
capabilities DISCOVERY RULE still has no required surface field, and the fm
ledger's release-wall entry is still unabsorbed (#20 fixed the
codetool-lab-fable5 copy of that contradiction, not the fm ledger's). Q16
(all repos public), Q2/Q6 (venture-lab D1–D3), Q7 (the 73/121 CI gap), Q12,
Q17, Q19, and Q20/Q21 (kit state at `21d3ead`) are untouched.
