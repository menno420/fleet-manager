# Reusing rules and skills across the estate — what we have, what sessions struggled with, and why the container is the whole question

> **Status:** `reference` · 2026-08-28
>
> **The owner's ask, verbatim:** *"find out as much as possible about re-using
> existing rules and skills in the existing repos … find out exactly what we
> already have that is good skill material and to find out through the audits
> and session journals etc what previous sessions struggled with so we can use
> that information to come up with a good plan."*
>
> **Method.** A 79-agent fan-out over all 19 non-archived repositories, cloned
> to disk: ten readers on distinct seams of rule/skill material, nine mining
> session cards for recurring struggle, then adversarial verification of the
> load-bearing claims. **1,002 session cards were opened and read** (of 3,836
> that exist); the rest were reached by counted search, never by impression.
> Every headline number below was **re-measured by the directing session**
> against source before it was written here — three subagent claims did not
> survive that and are marked in § 7.
>
> **Adds to, does not restate, the three 2026-08-28 audits** (genesis dig ·
> router-band re-read · kit-tree truth pass). Where this record converges with
> them it says so and gives the independent measurement.
>
> Certainty tags per
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).

## 0 · The answer in one paragraph

The estate has **excellent** reusable material and has been putting almost all
of it into the one container that does not deliver. `MEASURED`: sessions write
an idea on **95 % of 3,836 session cards** and **357** ideas exist in the
repositories' idea conveyors — a **10 : 1 write-to-land ratio**, and **28 : 1**
once `superbot` (the era the loop actually worked) is excluded. Four
repositories have **zero** ideas in their conveyor, and one of them is
`idea-engine`. Meanwhile the artifact that *is* gated by `check --strict` — the
session card itself — holds at **95–97 % conformance across all 3,836 cards**.
The estate is not failing to *produce* reusable knowledge. It produces it
reliably, on nearly every card, and then never reads it back. **So the plan is
not "write more skills". It is "consume what the cards already contain", and
the mechanism has to be one that fires, because the same corpus shows that
anything not attached to a gate decays to near zero.**

## 1 · The delivery-mechanism ranking — the finding everything else hangs off

`MEASURED`, same corpus, three delivery mechanisms:

| how a procedure reaches a session | how often it actually ran |
|---|---|
| **Gated by `check --strict`** (the session card) | **95–97 %** of 3,836 cards |
| **Embedded in the card template** (`Session idea (Q-0089)` block, superbot) | **598 of 969** cards |
| **Written as a skill** (`/session-close`, superbot — the most-invoked) | **46 of 969** cards |
| **Written as a skill** (`/session-close`, fleet-manager) | **2 of 433** cards |
| **Written as a skill** (`/groom-ideas`, superbot) | **0 of 969** cards |

The sharpest single case is internal to one repo: `/groom-ideas` is named in
**0** of superbot's 969 cards, while the *same ritual* embedded in the card
template as `Grooming (Q-0015)` ran in **82**. Same procedure, same repo, same
sessions, two containers — 0 against 82.

**Bound on this measurement, stated because it changes how much weight it
carries:** invocation was counted by searching cards for the skill's name, so
these are **lower bounds** — a session can invoke a skill without writing its
name down. What survives the bound is the *comparison*, because both figures
come from the same method on the same corpus: 598 template blocks against 46
skill mentions in one card set.

`MEASURED` correction to a subagent claim: skills are **not** never invoked.
Ten of superbot's fourteen are named in at least one card (`/session-close` 46,
`/fleet-review` 15, `/pre-pr` 6). The finding is not that skills are dead; it is
that they are roughly an order of magnitude weaker than template embedding and
two orders weaker than a gate.

**Convergent with the genesis dig's "the door, not the notebook", measured
independently and at a different scale.**

## 2 · The dominant struggle — the estate writes knowledge and never reads it back

This is what the nine card-mining agents converged on from repositories that
share no code and no sessions.

`MEASURED` by the directing session across every repo with a card protocol:

| repo | cards | carrying a 💡 idea | ideas in the conveyor |
|---|--:|--:|--:|
| `superbot` | 969 | 803 | **256** |
| `substrate-kit` | 343 | 343 | 50 |
| `fleet-manager` | 433 | 432 | 18 |
| `spider-swing` | 142 | 142 | 8 |
| `superbot-next` | 334 | 333 | 7 |
| `venture-lab` | 228 | 228 | 6 |
| `websites` | 302 | 302 | 6 |
| `gba-homebrew` · `pokemon-mod-lab` · `couch-legend` | 228 | 228 | 6 |
| **`idea-engine`** | **503** | **503** | **0** |
| `sim-lab` | 259 | 259 | **0** |
| `product-forge` | 35 | 35 | **0** |
| `shiftlife` | 60 | 60 | **0** |
| **total** | **3,836** | **3,668 (95 %)** | **357** |

**`idea-engine` — the repository whose entire purpose is ideas — has 503 cards
each carrying an idea and zero ideas in its conveyor.**

`docs/ideas/README.md` states the contract these numbers are measured against:
*"Capture ideas here so they live in the repo, not in chat … A **conveyor, not
a graveyard**: every idea ends implemented, on a roadmap, in discussion, or
explicitly rejected."*

**superbot's 3.1 : 1 is the control condition.** It is the only repo where the
ratio is close, and it is the era the genesis dig identifies as the practice
working. Every post-close repo is between 28 : 1 and infinite.

`REVIEWED` — the same shape, found independently by four mining agents in four
repositories, each with its own citations:
- **fleet-manager** — a session's 💡 / guard-recipe / ⚑ observation gets no
  routed destination and is re-noticed later; 8 distinct cards, 2026-07-11 →
  2026-08-28.
- **sim-lab** — an unbroken chain V047 → V048 → V049, each independently
  proposing a tooling fix that was never routed; separately, the same
  statistical-power defect re-registered across at least 5 sessions.
- **idea-engine** — a seed-sweep recipe re-derived by hand across 8 consecutive
  cards; a rotation-slot position across 9.
- **substrate-kit** — the instrument fired and the session did not see it: the
  advisory channel measured at ~1 : 9 signal-to-noise.

**This is OD-21 measured.** The owner's diagnosis was *"each agent working in
any repo should contribute to ideas and journals and helping to improve the repo
for the next agent. If this had been done consistently and properly then most of
what I needed to intervene for would have resolved itself much faster."* The
contribution half is happening at 95 %. The consumption half is not happening at
all.

## 3 · What we actually have that is good material

`MEASURED`. The inventory, by container.

**Executable checkers — the strongest material, and it is already code.** Nine
of superbot's eleven orphan skills are thin wrappers around checkers that still
exist: `context_map.py` (476 lines), `check_architecture.py` (728),
`check_docs.py` (674), `check_current_state_ledger.py` (321),
`check_plan_backlog.py` (360), `new_subsystem.py` (441), `router_status.py`
(334), `check_quality.py` (251), `check_migration_collision.py` (162). Three
tested runnable (`--help`, exit 0); the other six unverified beyond existence.
**The valuable artifact is the checker, not the prose around it.**

**superbot's `.session-journal.md`** — 803 lines, the only fully-filled journal
in the estate, with a rules/conventions band at lines 344–773 explicitly
labelled *"candidate — not yet promoted to CLAUDE.md"*.

**The owner-decision register** — `maintainer-question-router.md`, 9,965 lines
/ 668,746 bytes. The router-band re-read already covered Q-0063–Q-0272; the
material outside that band is unread.

**3,836 session cards**, 95 % of which carry an idea nobody has consumed.

**And the enforcement layer that works** — 6 hooks, 8 registrations, 4 events,
**71 routes / 275 trigger regexes / 36 docs**, 7 traps. This exists in
**fleet-manager only**; no satellite has a `.claude/hooks/` directory.

## 4 · Why "promote it into the kit" is not a plan

`MEASURED`, verified by the directing session against kit source.

**The kit stages skills; it never installs them.** Skills are Python dict
literals in `src/engine/skills/skills.py` (15 entries), rendered to `SKILL.md`
text and written only into the staging directory. The kit's own template says
it outright — `src/engine/templates/SKILLS-index.md.tmpl:30-40`: *"both commands
exit 0 with everything staged and **nothing live**). Installing is the host's
own copy step"*, followed by a five-line `cp` loop a human runs by hand. The
`upgrade-distribution` skill — which *is* the distribution wave — contains
neither `.claude/skills` nor `cp` anywhere in its 3,277-character body.

**Measured consequence: 4 of 19 repositories have a populated
`.claude/skills/`** (fleet-manager 27, couch-legend 15, superbot 14,
curious-research 1). `substrate-kit` itself has no `.claude/` directory at all.

**And the same uninstrumented `cp` loop silently reverts local amendments.**
fleet-manager's `session-close` carries +136 lines over the kit's version,
`continuation-prompt` +131, `intake` +118 — all local edits to generated files.
Only `session-close` warns about it in the file itself. `docs/SKILLS-local.md`
classifies `continuation-prompt` as `local`; it is defined in the kit at
`skills.py:712` with a `_CONTINUATION_PROMPT_BODY` constant, so it is
kit-shipped and overwrite-exposed, and the registry a session would consult is
wrong about it.

**The kit is also shipping a stale procedure.** Its `session-close` body still
instructs a claim via `control/claims/<branch>.md`, which fleet-manager's boot
file rules seat-era historical. fleet-manager fixed that **in its own copy**;
the other repositories still receive the stale version.

## 5 · The push layer and the pull layer never touch

`MEASURED`: **0 of fleet-manager's 27 skills reference `traps.md`,
`doc-routes.json` or `.claude/hooks`.** And **0 of the 71 routes point at
`CONSTITUTION.md`, `docs/playbook.md`, `docs/intent.md` or `docs/decisions.md`**
— the four canonical rule surfaces, carrying 17 + 12 + 30 + 9 rules between
them. All six `docs/conventions/` files *are* routed.

`docs/traps.md:15-22` defines the lifecycle — **mistake → trap entry →
route/hook reminder → deterministic checker** — and `:31` states *"An entry
without a route is unfinished work, not a record."* It has been run to
completion for **7 execution mistakes and for 0 rules.**

**The machinery this plan needs already exists and has never been pointed at
the rulebook.**

## 6 · The plan

`REASONED` throughout — this is the session's proposal, not owner-ratified, and
§ 8 says what it does not decide.

**Move 1 — consume the cards. (The only move that addresses § 2.)**
Extend the session-log checker so that flipping a card to `complete` with a 💡
whose text names a concrete artifact requires that idea to have a routed
destination. The estate's own spec for this is already written twice in the
mining evidence. This is a **gate change**, which § 1 says is the only tier that
holds. It is also the smallest change with the largest measured gap behind it —
3,668 written against 357 landed.

**Move 2 — port the checkers, not the skills.** superbot's nine checkers are
the highest-value material and they are already executable. Porting a checker
into a repo's gate puts it in the 95 % tier; rewriting it as a skill puts it in
the 0–3 % tier. Start with the two whose method is fully general:
baseline-before-you-edit (`pre-edit-check`) and sync-before-you-judge
(`fix-drift`).

**Move 3 — point the existing routes at the rulebook.** § 5 shows 71 routes
covering conventions and zero covering the four rule surfaces. Adding routes is
cheap, tested (`tools/test_doc_route_patterns.py`, 61 cases), and needs no kit
release.

**Move 4 — fix the distribution gap before promoting anything into the kit.**
Until `upgrade-distribution` performs the install step, promoting a skill into
substrate-kit delivers it to nobody. Either wire the copy into the runbook, or
decide deliberately that skills stay repo-local and stop treating the kit as
their distribution path.

**Sequence:** 3 → 1 → 2 → 4. Move 3 is hours and needs no release; Move 1 is
the highest-value; Move 2 is per-checker and incremental; Move 4 is a kit
change and therefore owner-paced.

**What NOT to do, on the evidence:** do not write new skills as the primary
vehicle. The estate has 57 skill files across four repositories and a measured
invocation rate near zero, a distribution mechanism that terminates one manual
command short of the invocable surface, and a registry that is wrong about
which of its own skills the kit owns.

## 7 · Coverage, and what did not survive

**Verification.** 229 promote-or-struggle claims were produced; **60 were
adversarially verified** (a cap set in the workflow and logged, not a silent
truncation), of which **43 survived and 17 were refuted**. The remaining **169
are unverified** — not refuted, not confirmed.

**The refutation pattern is the most useful single result.** In **17 of 17**
refutations the **source citation held** and only the *verdict* fell — the
claim proposed promoting something fleet-manager already has. "Duplicate
proposed as new" is named explicitly in 6; `fm_equivalent` shown false in 5
more. **The estate's instinct is to propose adding what already exists**, which
is why any reuse plan must start from an inventory of fleet-manager rather than
from a list of attractive material elsewhere.

**Three subagent claims the directing session partially refuted before use:**
- *"41 sessions over five weeks each noticed a wrong front door and none fixed
  it"* (idea-engine). **41 cards do carry the string** — but their filename
  dates span **two days**, not five weeks, and `git log` shows
  `docs/current-state.md` was touched 3 times in the window. The duplicated-
  effort point stands; the headline does not. *(Own limit: filename dates are
  not session dates, and commits touching a file are not proof of a fix.)*
- *"Skills are never invoked by name"* — false; 10 of superbot's 14 are.
- *"3 of 12 repos have a populated `.claude/skills/`"* — the subagent's
  denominator; the measured figure over all 19 is **4 of 19**.

**Honest nulls:** six of the nine superbot checkers are verified to exist but
not to run. The owner-ruling register outside Q-0063–Q-0272 is unread. Skill
invocation is a lower bound (§ 1). No satellite repository's hook layer was
tested, because none has one.

## 8 · What this record does NOT decide

- **It GOes no packet.** OD-23's hold on plan execution stands.
- **It builds no skill and ports no checker.** Moves 1–4 are a proposal; the
  promotion rule (roadmap § 6) governs anything that would move into the kit.
- **It does not answer `OQ-FM-D2-TARGET`.**
- **It does not decide whether skills should exist at all.** § 1 measures how
  weakly they deliver; it does not establish that a skill is worthless — the
  long-form method a session deliberately opts into is a real use, and
  `docs/SKILLS-local.md` documents 27 of them.
- **The four moves are `REASONED`.** Only the measurements are `MEASURED`, and
  § 7 says which of those are bounded.
