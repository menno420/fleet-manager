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
> **This is stage-one mapping input, not a plan (OD-26 § 13).** The owner said
> mid-sitting, unprompted: *"I am currently running 3 parrallel ultracode
> session to map most of all the repos, once this mapping is all done we should
> use this information to come up with a revised plan. Only after that will we
> move to execution of the 'GO'"*. **This session is one of those three.** Its
> output is therefore a contribution to the revised plan, and § 6's four moves
> are candidate inputs — **not a queue to work.** They are deliberately left
> unsequenced-for-execution below.
>
> **Adds to, does not restate, the three 2026-08-28 audits** (genesis dig ·
> router-band re-read · kit-tree truth pass). Where this record converges with
> them it says so and gives the independent measurement.
>
> Certainty tags per
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).

## 0 · The answer in one paragraph

The estate has **excellent** reusable material, and the question of *which
container it goes into* decides whether it is ever used again. `MEASURED`: the artifact **gated by `check --strict`** holds at **95–97 %
across 3,836 cards**, and a **template-carried ritual** is completely countable
because its text is written by construction (`Session idea (Q-0089)` in **598 of
969**). **Skill invocation is not measurable at all** — no trace is required and
none is kept — so an earlier quantified ranking of the three was withdrawn (§ 1).
The surviving argument is stronger for not needing the numbers: prefer
mechanisms whose use leaves a record, because one that leaves none cannot be
shown to work even when it does. Separately and more prosaically:
**substrate-kit cannot deliver a skill at all** — it stages them and never
installs, so promoting one into the kit reaches nobody.

**On idea consumption, this record twice published a wrong answer and now
publishes a bounded one.** See § 2: the corrected measurement shows **wide
variance, not uniform failure**, and the two repositories built as idea engines
convert at better than 1 : 1.

## 1 · Delivery mechanisms — the ranking is WITHDRAWN, and what replaces it is better

**An earlier version of this section ranked three delivery mechanisms by how
often each "actually ran". That ranking is withdrawn.** `@codex` (fm #963 R4)
showed the comparison is invalid, and it is right: the mechanisms have
**different observability**, so the numbers are not commensurable.

- A **template block** writes its own identifying text into the card *by
  construction* — `Session idea (Q-0089)` is in the card because the template
  put it there. Counting it counts every occurrence.
- A **skill invocation** need not leave any trace in the card at all. So
  `/session-close` appearing in 46 of superbot's 969 cards is a **floor with no
  ceiling**: the true number could be anything from 46 to 969.

Ranking a complete count against an unbounded floor produces a number that
looks like a measurement and is not one. **The estate has no skill-invocation
telemetry**, so the earlier claims — "an order of magnitude weaker", "the 0–3 %
tier" — were unsupportable and are removed.

**What survives, and it is the more useful statement:**

| mechanism | what can be measured | value |
|---|---|---|
| **Gated by `check --strict`** | conformance, directly — the checker itself is the instrument | **95–97 %** of 3,836 cards |
| **Template-carried ritual** | complete, because the text is written by construction | `Session idea (Q-0089)` in **598 of 969**; `Grooming (Q-0015)` in **82** |
| **Skill invocation** | **nothing** — no trace is required and none is kept | unmeasurable; card mentions give a floor only |

**The finding is the third row**, stated at the width the evidence supports:
**there is no complete invocation telemetry.** Not that skill use is invisible —
46 recorded invocations exist and are observable, and controlled verification of
a skill is entirely possible. What is missing is an *exhaustive* count, which is
what a rate would require (`@codex` R5 narrowed this; the first cut said
"cannot be observed at all", which its own evidence contradicted). A mechanism whose use leaves no record
cannot be counted exhaustively, so no rate is derivable and no claim about how
often skills run — in either direction — is checkable. That is a stronger argument for preferring gates and
template-carried rituals than the false quantification it replaces, because it
does not depend on knowing how often skills run.

**It also makes skill-invocation telemetry a concrete, cheap thing to add** —
and until it exists, no claim about skill effectiveness in this estate, in
either direction, is checkable.

## 2 · Idea consumption — corrected twice, and the corrected reading is different

**This section was wrong twice and the errors are recorded rather than edited
away, because the method failure is more reusable than the number.**

**Version 1** claimed a *"10 : 1 write-to-land ratio"* — 3,668 ideas written
against 357 landed. Withdrawn: `docs/ideas/` is *a* destination, not *the*
destination. An idea can equally land as a trap entry, a route, an `OQ-` ask or
a finding.

**Version 2** retreated to *"four repositories have zero, and one is
`idea-engine`"*. **Also wrong, and worse** — the zeros were an artifact of
counting one directory name in repositories that keep ideas elsewhere.

**The corrected measurement.** Unit: **one idea item** — an `*.md` file in the
repo's idea tree, or one `verdict-*` directory where verdicts are the output
form. Stated because version 3 of this table mixed units (it counted
directories *and* their contents for some repos and files only for others,
inflating exactly the two rows it was correcting).

**Positive control, unplanned:** `idea-engine` returns **566**, which is the
same figure the boot file has carried since OD-4 (*"566 idea files"*) from an
independent count. A measurement that lands on a number already in the tree
from another source is the closest thing to corroboration available here.

| repo | cards | idea items | store | ratio |
|---|--:|--:|---|--:|
| `idea-engine` | 503 | **566** | `ideas/` (`*.md`) | **1.13** |
| `sim-lab` | 259 | **268** | `sims/verdict-*/` (dirs) | **1.03** |
| `couch-legend` | 7 | 2 | `docs/ideas/` | 0.29 |
| `superbot` | 969 | 256 | `docs/ideas/` | 0.26 |
| `substrate-kit` | 343 | 50 | `docs/ideas/` | 0.15 |
| `spider-swing` | 142 | 8 | `docs/ideas/` | 0.06 |
| **`fleet-manager`** | **433** | **18** | `docs/ideas/` | **0.04** |
| `venture-lab` | 228 | 6 | `docs/ideas/` | 0.03 |
| `pokemon-mod-lab` | 70 | 2 | `docs/ideas/` | 0.03 |
| `superbot-next` | 334 | 7 | `docs/ideas/` | 0.02 |
| `websites` | 302 | 6 | `docs/ideas/` | 0.02 |
| `gba-homebrew` | 151 | 2 | `docs/ideas/` | 0.01 |
| `product-forge` | 35 | 0 | `docs/ideas/` empty | 0 |
| `shiftlife` | 60 | 0 | `docs/ideas/` empty | 0 |

**What this actually shows — and it is not what versions 1 and 2 said.** The
**two repositories built as idea and verification engines convert at roughly
1 : 1**: `idea-engine` holds 566 idea files across per-repository folders, and
`sim-lab` 268 verdict directories, which *are* its output form. They are the
estate's **best** performers, and this record twice named them as its worst.

The gap is between **purpose-built conveyors and everything else**. `superbot`
at 0.27 is the best of the rest — again the era the genesis dig identifies as the
practice working. **`fleet-manager`, the hub that writes the most process
knowledge in the estate, sits at 0.04**: 433 cards, 18 idea files.

**Bound, stated because two versions of this section lacked one:** a card's 💡 is
one field and an idea artifact is one file; they are not the same unit, and a
ratio between them measures *relative* conveyor use across repositories, not
survival. Nothing here establishes that any specific idea was lost. What it
supports is a **comparison between repositories on one consistent measure**.

**The independent evidence for re-derivation is qualitative and unaffected by
any of this.** Four mining agents found the same shape in four repositories,
each with card citations rather than counts:
- **fleet-manager** — a 💡 / guard-recipe / ⚑ observation gets no routed
  destination and is re-noticed later; 8 distinct cards, 2026-07-11 → 2026-08-28.
- **sim-lab** — an unbroken chain V047 → V048 → V049, each independently
  proposing a tooling fix that was never routed; separately the same
  statistical-power defect re-registered across at least 5 sessions. *(Note the
  tension with sim-lab's 1.03 above: a repo can convert ideas into its own
  product and still lose process observations. The two measure different things.)*
- **idea-engine** — a seed-sweep recipe re-derived across 8 consecutive cards.
- **substrate-kit** — the instrument fired and the session did not see it; the
  advisory channel measured at ~1 : 9 signal-to-noise.

**OD-21's diagnosis is supported by that citation evidence, not by this table.**

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

**Move A — consume the cards. ⚠ THIS IS THE HELD FUNCTION — DO NOT BUILD IT.**
The proposal was: extend the session-log checker so that flipping a card to
`complete` with a 💡 naming a concrete artefact requires that idea to have a
routed destination.

**That is the estate's own Move 1, in another shape, and OD-26 § 7 holds it.**
His words there: *"Hold — still planning"*, and the section states the bound
explicitly — *"No adjacent mechanism may be built that is Move 1 in another
shape. The hold is on the function — a close-time declaration of what a session
left behind — not on the filename."* A gate at card-flip asking whether the
session's idea reached a destination **is** a close-time declaration of what the
session left behind.

**This record scored it highest of the four and recommended it hardest, while
it was already held.** Retained as evidence *for* the held function — the four
mining chains and the § 2 variance are exactly the case a revised plan would
weigh — and withdrawn as a thing to build. It also **collided by name** with the
estate's Move 1, which is why the moves here are now lettered. The estate's own spec for this is already written twice in the
mining evidence. This is a **gate change**, which § 1 says is the only tier that
holds. **Its rationale is NOT the withdrawn ratio.** 3,668 counted a marker and 357
covered one destination of several; neither half measures written-against-landed
(§ 2). What supports Move A is the **citation evidence** — the four
re-derivation chains, each naming distinct sessions in a repo — and nothing
numerical.

**Move B — port the checkers, not the skills.** superbot's nine checkers are
the highest-value material and they are already executable. A checker in the
gate is **measurable and enforced**; the same method rewritten as a skill is
neither — its use leaves no record at all (§ 1). Start with the two whose method
is fully general:
baseline-before-you-edit (`pre-edit-check`) and sync-before-you-judge
(`fix-drift`).

**Move C — point the existing routes at the rulebook.** § 5 shows 71 routes
covering conventions and zero covering the four rule surfaces. Adding routes is
cheap, tested (`tools/test_doc_route_patterns.py`, 61 cases), and needs no kit
release.

**Move D — fix the distribution gap before promoting anything into the kit.**
Until `upgrade-distribution` performs the install step, promoting a skill into
substrate-kit delivers it to nobody. Either wire the copy into the runbook, or
decide deliberately that skills stay repo-local and stop treating the kit as
their distribution path.

**The sequence proposed here (3 → 1 → 2 → 4) is withdrawn as a sequence.**
Under OD-26 § 13 the revised plan is the owner's to write from the mapping, and
a stage-one map that arrives pre-sequenced is asking him to skip his own stage.
What follows instead is each move scored against **his two criteria**, which is
the form an input should take.

**OD-26 § 20 — does it stop something being re-derived?** *(his stated waste:
"redoing the same things over and over"; less stalling is a bonus, not the case
for a mechanism)*
**OD-26 § 4 — does it make a session more likely to leave the repo better than
it found it?** *(his single root cause, which replaces mechanism-class as the
organising question)*

| move | stops re-derivation? | makes a session leave the repo better? |
|---|---|---|
| **A · consume the cards** ⚠ held | **Directly.** A 💡 naming a concrete artefact that reaches no destination is re-noticed by a later session — the four mining chains are exactly this | **Directly.** It is the leave-it-better act, made a condition of closing |
| **B · port the checkers** | **Yes, and it is already paid for** — nine executable checkers exist; rewriting their method is itself re-derivation | Yes, if gated: a checker in the gate makes the next session's tree cleaner |
| **C · route the rulebook** | **Partly.** Routes deliver a rule at the moment of action; they do not preserve a session's own finding | Weakly — it prevents a mistake rather than improving the repo |
| **D · fix kit distribution** | **No.** It unblocks delivery; nothing is re-derived today because of it | No — enabling work, not leave-it-better work |

**On his criteria the ranking inverts the one this record first proposed.**
Move C was put first for being cheap; on the re-derivation test it is the
weakest of the four. **Move A is the only one that scores directly on both —
and it is the one OD-26 § 7 holds**, which is itself a data point: the estate's
strongest available lever is the one the owner has deliberately paused. Move D
scores on neither — it is a prerequisite for a path (promoting into
the kit) that § 4 shows is not currently worth taking.

**This section is `REASONED` and is an input. The owner writes the revised
plan.**

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

**Section 2 was wrong twice, and the second error was worse than the first.**
Version 1 published a lossage ratio whose denominator was never established.
Version 2, correcting it, retreated to "four repos have zero, one is
`idea-engine`" — and that zero was a **directory-name mismatch in the one
repository guaranteed to keep ideas somewhere else**. `idea-engine` holds 566
idea files in `ideas/`; `sim-lab` 268 verdict directories in `sims/`. Both were
named as the estate's worst performers when they are its best. **A third
version then mixed units** — counting directories and their contents together
for those two rows and files only for the rest — which inflated precisely the
figures it was correcting. The unit is now stated in the table. **The
correction and the original error were the same mistake — measuring a proxy and
reporting it as the thing — made twice, twenty minutes apart, the second time
while explicitly correcting the first.** Anyone re-running this: enumerate each
repository's own store before comparing, and treat a zero as a question about
your query before it is a finding about the repo (TRAP-003).

**The withdrawn ratio, recorded as a method failure and not just an edit.** The
first version of this record led with a 10 : 1 write-to-land ratio built on the
assumption that `docs/ideas/` is an idea's only destination. It is not, and the
disproof was one `ls` away in directories this session had used all day. The
write side was checked (35 of 40 sampled cards carry a substantive 💡); the
land side never was. **A ratio needs both halves established, and only one was.**

**`@codex` R4 attacked this document and landed two P1s.** (1) The 💡 count is
a marker count, not an idea count — verified against `bootstrap.py:326-330` and
a card that passes while carrying nothing. (2) `idea-engine/ideas/` is recorded
as canonical in this repo's **own tree**, so the § 2 error was not a
hard-to-find fact. **Verified rather than relayed, and one of R4's three
citations does not hold:**
- `tools/build_notebook_bundle.py:109-115` — holds, and is stronger than R4
  claimed: the comment reads *"`ideas/` holds everything, subdivided by CONSUMER
  REPO"* and names a **742-file group**, the exact figure this session hit on
  its first `find`.
- `docs/ESTATE.md:93` — holds verbatim: *"566 fleet-era idea files"*.
- `docs/owner-queue.md:353-356` — **does not.** Those lines concern database
  history pruning and Railway cost; no 566, no idea-engine. A third instance
  does exist, found by grepping for the number rather than from any citation:
  `docs/fleet-account-2026-07-26.md:194`.

**Recorded because the failure mode is specific:** two of the three citations
held, and this record initially repeated all three as fact. **A batch of
citations launders a bad member through the credibility of its neighbours** —
check each, or attribute the batch. It also showed the delivery ranking was incommensurable (§ 1,
withdrawn) and that 41 cards sharing a string does not establish 41 independent
derivations.

**A citation debt this record has not paid.** The four mining bullets in § 2 are
presented with per-repository specifics but carry **no card paths or line
numbers**, and the clones and agent outputs they came from are not committed —
so nothing in them is reproducible from this repository. `@codex` R4 called
this correctly. They are retained as `REVIEWED` leads, not as findings, until
the citations are committed.

**Honest nulls:** six of the nine superbot checkers are verified to exist but
not to run. The owner-ruling register outside Q-0063–Q-0272 is unread. Skill
invocation is a lower bound (§ 1). No satellite repository's hook layer was
tested, because none has one.

## 7b · This session paid the tax it is describing

`MEASURED`, on itself, and recorded because OD-26 § 20 names re-derivation as
**the** waste the workflow exists to prevent.

Section 2 of this record was rewritten **four times**. The fact it kept getting
wrong — that `idea-engine` keeps its ideas in `ideas/`, not `docs/ideas/` — was
already written in this repository in three places: `docs/ESTATE.md:93` (*"566
fleet-era idea files"*), `tools/build_notebook_bundle.py:109-115` (whose comment
names a **742-file group**, the exact number the first `find` returned), and
`docs/fleet-account-2026-07-26.md:194`. **The session re-derived, badly and
repeatedly, a fact its own repository stated three times.**

That is his sentence — *"redoing the same things over and over"* — measured on
the session writing it down, and it is the fourth instance in this round after
the three OD-26 § 20 already lists. It is also the strongest available argument
for Move 1 and against Move 3: routing delivers a rule at the moment of action,
but no route existed for *"before you count a repo's ideas, ask that repo where
it keeps them"*, and no rule would have fired. What would have caught it is the
check that eventually did — **measure something whose answer is already written
down, and see whether you get it.**

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
