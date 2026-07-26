# Fleet plan v2 — verification-led consolidation

> **Status:** `historical`
>
> **⚠ SUPERSEDED same day by [`2026-07-26-consolidation-program.md`](2026-07-26-consolidation-program.md)**
> — the owner set the definitive frame in the hub chat (evening): Projects
> terminated, regular sessions possibly indefinitely; pace slow; documentation
> first, websites second; CI toward one check per repo; the deliverable is a
> step-ledger program any future session can continue. This plan's analysis
> (review surfaces, verification-led folds, the conformance instrument) is
> carried into that program; read the program, not this.
>
> **Supersedes [`2026-07-26-fleet-consolidation-plan.md`](2026-07-26-fleet-consolidation-plan.md)**
> (v1, merged as fm #540) after the owner pushed back that the fleet's own docs
> had not been read. He was right. v1 was built on repo *metadata* — the GitHub
> API census — and skipped the fleet's written memory. This version is built on
> both.
>
> Companion, unchanged and still valid: [`2026-07-26-ci-consolidation.md`](2026-07-26-ci-consolidation.md).

---

## 1 · What v1 got wrong

Four errors, each traceable to a doc that was sitting in this repo:

| v1 said | The record says | Where |
|---|---|---|
| "Most valuable: consolidate the bot" — i.e. **ship more** | *"**This is now the highest-value work: verification, not more shipping.**"* | `owner-reflection-2026-07-21.md` §"Open threads" |
| Archive `websites`' control-plane + review | *"He reviews through what he can see. The websites/dashboards were his review surface. Build things he can inspect."* Archiving the review surface during a verification phase is backwards. | `owner-reflection-2026-07-21.md` §"How this owner works" |
| Derived a repo structure from scratch | The owner **already grouped the fleet into 8 standing Projects** on 2026-07-11 — SuperBot 2.0, SuperBot World, Websites, Game Lab, Ideas Lab, Venture Lab, Self Improvement, Fleet Manager | `fleet-triage.md` §"2026-07-11 owner restructure" |
| Opened with three blocking questions | *"**Decide, don't default to asking.** When a task ends, weigh the options and take the follow-up that most benefits the owner. Reserve questions for genuine forks only he can resolve."* | `owner-reflection-2026-07-21.md` §"Standing instruction" |

`current-state.md` even carries the line **"Read this if you read nothing else:
`owner-reflection-2026-07-21.md`"**. v1 walked past it.

Two of the three questions v1 asked were also **already open owner-queue items
with recorded recommendations** — `OQ-CONSOLIDATION-DELETE-VS-ARCHIVE`
(recommended A: archive) and the venture-lab disposition. Asking them again spent
owner attention the queue exists to protect.

---

## 2 · The reframe — repo count is a symptom

The owner's finding, in his words: **"The platform scales infinitely. Human
management does not."** And the measurement that follows from it:

> *"No realistic amount of oversight tooling would let one person truly run more
> than ~10 projects; even 8 was heavy."*

So the number to minimize is **not repos — it is review surfaces**: how many
distinct things one person must hold in his head to know the fleet is honest.
That reframes everything:

- Two repos that are always reviewed together (`gba-homebrew` +
  `pokemon-mod-lab`, forced apart by copyright) cost **one** review surface, not
  two. Merging them would be illegal and would save nothing.
- Thirteen archived repos cost **zero** review surfaces. Archiving is the cheap
  win; merging is the expensive one, and only pays where it genuinely collapses
  a review surface.
- A repo you have never read costs **more** than one surface, because you do not
  know what is in it.

### And the drift is real, not hypothetical

The owner's inference — *"quality drifts wherever no one looks"* — is proven
inside the fleet, in the one repo that went looking. From
`shiftlife/docs/plan-conformance.md`:

> *"This file exists because **ten self-directed slices once drifted from it
> without anyone noticing**, and it took a deliberate audit to find three missing
> free-core items."*

Ten slices. Unnoticed. In the **newest, healthiest, most-attended repo in the
fleet**. The unreviewed older repos have no such audit at all.

A second confirmation surfaced during v1's own census, before any of these docs
were read: `superbot-games`' README says its games ship as plugin packages
against superbot-next's contract, and `superbot-idle` really is pinned by hash in
`plugins.lock.json` — but `superbot-games` has **no `pyproject.toml` and no
`manifest.py`**. The claim outran the code. That is exactly the class of drift
this plan exists to find, and it was found by accident.

---

## 3 · The instrument — "contains vs claims", already proven

The owner asked for this specifically:

> *"Consider a lightweight, owner-reviewable **'what each repo actually contains
> vs. what it claims'** pass, starting with the repos he never got to see."*

**It already exists and works.** `shiftlife/docs/plan-conformance.md` is that
document: a per-item table of *claim → state (done / half / missing) → the exact
module and test that back it*, with honest caveats kept in place rather than
smoothed over —

> *"Delivery does not exist: no `expo-notifications`, no permission flow, **no
> notification has ever fired.**"*

That is the template. It is short, it is owner-readable, it names the file and
test behind every row, and it earns its keep by making drift visible without a
session going looking.

**Generalize it.** Every repo gets a `docs/conformance.md` before it is folded or
archived. Its rules:
1. **Re-verify against the code, never against the docs.** Memory drifts; only
   the code is true.
2. Every row names the module *and* the test.
3. **A wrong row is worth more than a tidy table** — a found gap is the point.
4. Honest states only: `done` / `half` / `claimed-not-built`.

---

## 4 · Target — 6 review surfaces

Down from 8 seats and 22 repos. Six, not eight, because the owner recorded that
**eight was already heavy**.

| # | Review surface | Repos | Why it is one surface |
|---|---|---|---|
| 1 | **ShiftLife** | `shiftlife` | The revenue bet. Live API, beta-ready, already conformance-audited. **Untouched by this plan.** |
| 2 | **SuperBot** | `superbot-next` (absorbing games · idle · mineverse · plugin-hello · botsite/dashboard); old `superbot` archived at cutover | One product. Everything absorbed exists only to serve the bot. |
| 3 | **Phone Controller** | `phone-controller` (graduated from product-forge) | Shipped Android app, own release cadence, zero coupling. |
| 4 | **Game Lab** | `gba-homebrew` + `pokemon-mod-lab` | Two repos, **one** surface — always reviewed together; the copyright rail forbids merging. |
| 5 | **Venture** | `venture-lab` | The money lane. **Has live revenue** — Stripe Webhook Test Kit, $29 on Gumroad since 2026-07-12, purchase path owner-verified. 3 more products publish-ready. |
| 6 | **Workshop** | `substrate-kit` + `fleet-manager` + `websites` (control-plane) | The kit, the records archive, **and the review surface itself**. |
| — | *Archive (read-only)* | idea-engine · sim-lab · trading-strategy · codetool-lab ×3 · product-forge remainder · old superbot | **Zero** review surfaces. |
| — | *Untouched* | `curious-research` | A gift repo with an audience of one. Not fleet work; no review load. |

### The one structural change v1 got backwards

**`websites`' control-plane and review sites stay live.** v1 filed them under
"fleet-oversight automation, monitoring a program that ended." That misread what
they are for: they are how a non-coder owner *sees* his fleet, and this plan's
whole thesis is that seeing is the bottleneck. The right move is the opposite of
archiving — **point the control-plane at the conformance passes**, so "which
repos have been verified, and what did the verification find" is a page he can
look at instead of a question he has to ask.

Only `botsite` + `dashboard` leave `websites` (they follow the bot, and resolve
the live duplication against old `superbot`).

---

## 5 · The sequence — review-and-fold, one repo at a time

The owner asked for a structure "so we can work on one thing at a time." This is
that structure, and it satisfies both goals at once, because **you cannot safely
fold a repo you have not read.** The conformance pass *is* the merge prep.

Each cycle, one repo:

> **1. Verify** — write `docs/conformance.md`: claims vs code.
> **2. Surface** — anything found goes to the owner in one place, plainly.
> **3. Fold** — merge into its destination surface, or archive.
> **4. Land** — the destination's CI goes to the 3-check standard as it lands.

### Order, highest claim-risk first

| | Repo | Why here | Cost |
|---|---|---|---|
| **V1** | `superbot-next` | 21MB, **claims 533/533 golden parity and 49 ported subsystems**, never live-tested, and the owner has decided it is the bot's future. Highest-value claim in the fleet, entirely unverified in production. **The conformance pass IS the live-test prep** — V1 and the cutover are the same work, not competing priorities. | Large |
| **V2** | `superbot-games` · `superbot-idle` · `superbot-mineverse` | One already has proven drift (no plugin packaging). Verify, then fold into surface #2. | Medium |
| **V3** | `venture-lab` | **Commercial claims**: 19 "publish-ready" SKUs, 1 live. If "ready" is not ready, that is worth knowing before any publish click. Live revenue makes this real money, not bookkeeping. | Medium |
| **V4** | Archive-bound: codetool ×3 · `product-forge` · `idea-engine` · `sim-lab` · `trading-strategy` | Cheap passes. **Release-before-archive is now unblocked** (see §6). | Small |
| **V5** | `websites` | Split botsite/dashboard → bot; keep control-plane; point it at the conformance results. | Medium |
| **V6** | `phone-controller` graduation | Smallest blast radius; proves the subtree-split + signing-secret recipe. Can run any time — **do it first if a quick win is wanted.** | Small |

`shiftlife` is deliberately absent: it is already audited and is the only healthy
repo in the fleet. Route around it.

---

## 6 · Unblocked by the owner's 2026-07-26 decisions

Recorded as OD-1/2/3 in v1 and now reconciled against the standing queue:

- **OD-3 (archive, never delete) resolves `OQ-CONSOLIDATION-DELETE-VS-ARCHIVE`**,
  open since 2026-07-12 with recommendation A. Answer = **A**.
- That in turn **unblocks release-before-archive**, which is real agent work and
  time-sensitive: **archiving freezes the tag-push path forever**, so
  `cfgdiff` v0.1.1 (codetool-lab-sonnet5) and `envdrift` v0.1.0/v0.2.0
  (codetool-lab-fable5) must be **tagged and released BEFORE** their repos are
  archived. Both are finished, documented CLIs with **zero releases today**.
  (`mdverify` already has live releases; `codetool-lab-opus4.8` stays unarchived
  so its install URLs keep working.)
- **OD-1** — `superbot-next` is the destination, live testing gates the cutover.
  This is why V1 leads the sequence.
- **OD-2** — `venture-lab` stays live. V3 verifies its inventory is real.

---

## 7 · Two standing items this plan does not re-litigate

- **`OQ-FM-APPARATUS-SIZING`** already carries per-workflow KEEP/HOLD verdicts.
  The CI companion doc reached the same conclusions independently; the queue item
  is the older and more precise record, and it wins where they differ.
- **Un-wiped routines cost money after the freeze.** Flagged in the reflection as
  worth a clean sweep independent of everything else — any wake-timer left on a
  frozen session burns quota on every fire for nothing.

## 7b · Addendum — owner corrections, same day (evening)

Recorded from the hub chat after this plan merged; they amend §4 and §5:

- **OD-4 — `idea-engine` and `sim-lab` REMAIN ACTIVE.** Not archive material:
  the owner intends them as standing assets for future projects — the idea
  corpus (566 idea files across 13 per-repo sections, unreviewed by the owner)
  and the verification instrument (267 verdict dirs; the 4-gate reproduce-
  from-scratch method). The target becomes **7 review surfaces** — the pair is
  surface #7 (Ideas Lab), two repos / one surface, like Game Lab. §5's V4 row
  no longer includes them; their V-cycle is a **conformance pass only**, not a
  fold. Open sub-question routed to the owner: standing loop vs on-demand.
- **Full-corpus read-back completed.** The owner asked for a documentation-
  derived account he can diff against reality before consolidation proceeds:
  [`../fleet-account-2026-07-26.md`](../fleet-account-2026-07-26.md). Facts
  found there that bear on this plan: `superbot` has been **frozen as the
  behavioral oracle since 2026-07-17** (the "stop landing work in old superbot"
  goal is already policy); the recorded cutover ladder ends in a **7-day shadow
  run** (W3's shape is already designed); venture-lab's pre-registered **T+14
  kill-clock dates to 2026-07-26**; and consolidation itself is the planned
  phase 2 of ruling **Q-0266** ("volume-first … consolidate later").

## 8 · What is deliberately not done

- **No repo is merged before it is verified.** That inverts the point.
- **`shiftlife` is untouched.**
- **Nothing is deleted** (OD-3).
- **The two GBA repos are not merged** — copyright rail.
- **The production bot is not cut over** until V1's verification and real live
  testing are done.
