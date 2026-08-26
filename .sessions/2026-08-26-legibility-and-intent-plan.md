# 2026-08-26 — the legibility plan: why the kit's next-agent contract is not being kept

> **Status:** `complete` — born red on purpose and verified red at open and on
> every head since. Flipped after `python3 bootstrap.py check --strict` returned
> a real exit 0 read from the process, never after a pipe, and after **one**
> `@codex` round at the exact head, requested as one and landed on: **14
> findings, 14 `[conceded]`, 0 `[survived]`.** No review request is outstanding
> at the flip (TRAP-007).

- **📊 Model:** opus-5 · high · idea/planning
- **📍 Venue:** cloud-container

## 💡 Session idea

The owner said he suspected substrate-kit was not doing its job — that every
agent should contribute ideas and journals for the next agent, and does not.
That is a measurable claim about 14 repositories, and measuring it before
writing turned a suspicion into a plan with a number in it. **The number
reframed the plan**: it is not that agents forget, it is that only gated things
happen.

**The new idea worth believing in, not built here:** the `♻ Carried forward`
marker this plan specifies is a *general* shape — a closed-vocabulary
declaration checked against a file delta. Nothing else in the card grammar works
that way; the other four markers check presence of a heading. If it holds, it is
the template for gating any contribution whose *quality* must not be graded, and
that is most of them.

## What shipped

- [`docs/planning/2026-08-26-legibility-and-intent-plan.md`](../docs/planning/2026-08-26-legibility-and-intent-plan.md)
  — the diagnosis in his words, the measurement, the reframe, three moves, the
  risk, and § 9's execution levers.
- **OD-21** in the program's directive table, and the planning-index row.

## 🔢 The measurement, and what it changed

`MEASURED` across all 19 non-archived repositories:

| artifact | enforced by | result |
|---|---|---|
| session card | a red required check | **2,849** across 14 kit repos |
| `docs/ideas/` entry | a sentence in a skill | **3** in fleet-manager against 163 post-close cards |
| `.session-journal.md` | nothing | planted template in **11 of 14** |

**It changed the plan's own thesis.** The session went in expecting to write
about information volume — his framing, and a reasonable one. The card is long,
structured and complied with 2,849 times, so volume is not the binding
constraint, and the plan became about enforcement instead.

## ⚑ The @codex relay — one round, requested as one, landed on

**14 findings · 14 `[conceded]` · 0 `[survived]`**, five of them P1. Requested
as a single round under this repo's convergence rule after fm #947 ran to five
where three would have done.

**Three of the fourteen caught this plan committing errors it warns about:**

1. **The kit-version census was a ten-repo sample stated over the population.**
   Re-measured across every adopter: **five live versions across 16**, not
   three — `1.15.0` ×3 and `1.7.0` ×1 among them. The estate's own records
   already said so. Sample-as-population, inside the document that names it.
2. **I cited the program's 2026-08-23 traffic figures without reading its
   2026-08-24 row**, which retracts them as a comparable set (*"must never be
   mixed"*; `spider-swing` re-reads 5, not 2). Un-propagated correction — the
   class this repo keeps a checker for.
3. **OD-21 recorded my design choices under "what it binds"** — the
   control-plane selection and the agent-routing mechanism. That is the exact
   inference-as-owner-decision failure the row itself cites from fm #937.

**The sharpest finding was none of those.** The reframe — *"not a memory
problem"* — does not follow from the comparison, because the card is gated
**and** auto-drafted by the kit **and** structurally templated, while an idea is
harder semantic work. Four variables move at once. The claim is narrowed to what
the evidence carries, the clean test is named, and the plan says plainly it was
not run.

**Two design findings changed what gets built:** Move 1's checker as first
drafted had to read prose to decide whether a card "claims a new idea" — the
semantic grading the next paragraph forbids, so it is now a closed-vocabulary
marker checked against a file delta; and shipping a checker into substrate-kit
does **not** make adopters inherit it, since they vendor pinned releases — so
Move 1 is a checker *and a rollout wave*, which is the honest cost.

## ⟲ Previous-session review

[`2026-08-26-cross-session-activity-log.md`](2026-08-26-cross-session-activity-log.md)
built `docs/activity/` after measuring that a cloud session could reach 54 of
74 cards. Its lesson was that hand-written numbers drift from generated ones,
and it fixed that by generating them. **This session repeated the shape it was
warned about** — a sample stated as a population, twice — which says the lesson
did not transfer as a habit. It transferred as a *mechanism* only where a
mechanism exists, which is precisely this plan's thesis, arrived at the hard
way.

Layer-2 handoff: null (fleet-manager itself; no satellite attached — the
per-repo facts came from live API reads, and every repo-specific action is left
as planned work rather than written blind).

## Capability delta

None new. One method note: **`GET /repos/{o}/{r}/contents/substrate.config.json`
across every non-archived repo is a two-minute estate-wide census** and should
be the default over sampling — the ten-repo shortcut is what produced this
session's worst finding.
