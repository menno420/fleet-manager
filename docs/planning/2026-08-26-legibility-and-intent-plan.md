# 2026-08-26 — the legibility plan: what is gated happens, what is instructed does not

> **Status:** `plan`
>
> **What this is:** the owner's 2026-08-26 diagnosis of why standards do not
> hold across the estate, the measurement that tested it, and the plan for
> working through it structurally. Written because the diagnosis existed only in
> a chat — the loss mode the boot file logs as entry 1b, which has now bitten
> three times in three weeks.
>
> **What it is NOT:** current state (`../current-state.md`), a replacement for
> the [consolidation program](2026-07-26-consolidation-program.md) or the
> [agent-operating-environment roadmap](2026-08-08-agent-operating-environment-roadmap.md).
> It is the missing *enforcement* half of that roadmap's Phase 2 and Phase 3:
> the roadmap says every repo needs a durable intent surface and a common
> operating protocol; this says **why the protocol the estate already has is not
> being followed**, with a number.
>
> Provenance per entry. `OWNER` = his words. `MEASURED` = a live read, dated,
> with the method. `DERIVED` = inference, revisable. Legend:
> [`../findings/2026-08-05-foundation-continuation.md`](../findings/2026-08-05-foundation-continuation.md).
>
> **Execution decomposition (same day, evening):**
> [the estate execution packets](2026-08-26-estate-execution-packets.md) — this
> plan broken into per-repo work packets for the two boot venues, with two
> corrections to this document stated in its § 2 (the § 2.4 `.claude/` census
> reads 4 and the measured figure is 10 of 19; § 4's "the deployed token is
> READ-scoped" is the docstring's claim, `UNVERIFIED` at the deployment).

## 1 · The owner's diagnosis, in his words

`OWNER`, 2026-08-26, hub chat. Kept verbatim because the plan below is checked
against it.

> *"it's hard to maintain a proper standard with this many repos, especially
> when the agents don't follow the rules etc. This is already why I have a lot
> of hooks and skills, to make sure everything agent works in the right way with
> as little mistakes as possible."*

> *"one thing I keep noticing is that it seems like there is too much
> information for an agent to remember. Which I already tried to solve by making
> the files shorter and more specific, and by enforcing a lot through hooks.
> Also I already created per repo boot files inside the fleet manager, but they
> are still not all finished."*

> *"it's important that the fleet manager repo has the right info available
> right away to get an agent to understand the big picture right away. Because
> even tho I have a lot of repos which seemingly have nothing to do with each
> other, a lot of times it happens that one of my repos is referenced or looked
> at/used while working either locally or in another repo. So it's important
> that each agent knows what exists, why it exists, and what my intent for it
> is."*

> *"the substrate-kit does not properly do it's job in the repos as intended,
> because each agent working in any repo should contribute to ideas and journals
> and helping to improve the repo for the next agent. If this had been done
> consistently and properly then most of what I needed to intervene for would
> have resolved itself much faster."*

**Three claims, and they are not the same claim.** (a) agents do not follow the
rules; (b) there is too much for an agent to hold; (c) the kit's next-agent
contract — ideas and journals — is not being kept. Only (c) is directly
measurable, and § 2 measures it. It turns out to explain (a), and to reframe (b).

## 2 · The measurement — `MEASURED` 2026-08-26

Live reads of all 19 non-archived repositories over the direct-PAT path
(`GET /user/repos`, `contents`, `.substrate/state.json` planted-doc hashes).
14 carry substrate-kit.

### 2.1 The ratio that settles it

| artifact | enforced by | result |
|---|---|---|
| **session card** | `substrate-gate`'s added-card hold — a red required check | **2,849 cards** across 14 repositories |
| **`docs/ideas/` entry** | a sentence in the `session-close` skill | **3 added in fleet-manager since the program closed** |
| **`.session-journal.md`** | a generated template and nothing else | **untouched in 11 of 14** |

**fleet-manager landed 163 dated session cards between 2026-07-22 and
2026-08-26 and added 3 ideas.** The `session-close` skill asks every session to
*"groom one idea forward; add one new 💡 idea you genuinely believe in."*

**Cards, not sessions — and the distinction is not pedantry.** One session can
land two cards (this tree holds `2026-07-23-hub-forge-slice4-handoff.md` and
`…-landed.md`, the second saying in its own text that it is the same owner-live
session), and a session that lands none is invisible to the count entirely. So
**3 ideas per 163 cards** is the measurement; a per-session compliance rate is
not derivable from it and is not claimed. The order of magnitude is what the
plan rests on, and it survives either denominator (`@codex`, fm #949).

Method: `ls .sessions/` filtered to dated cards from 2026-07-22; `ls
docs/ideas/*.md` grouped by the date in the filename — **15 of 18 are dated
2026-07-09/10/11**, inside the EAP fortnight, when a seat was *ordered* to file
them. Three are from August.

### 2.2 The journal is worse, and it is the one that costs the most

`.session-journal.md` is the kit's cross-session process memory. Its own
headings are *"Recurring problems + fixes — so the next session doesn't
re-discover them."*

**Byte-identical to the planted template in 11 of 14 kit repositories** — never
written, or written and reverted; the hash cannot tell them apart. Written in three:
`spider-swing`, `substrate-kit`, `websites`. fleet-manager's is a template, and
[`../MAP.md`](../MAP.md) has said so in writing since 2026-08-10 without anyone
filling it.

**That is the direct mechanical cause of the owner's last sentence.** Every repo
re-derives its own traps every time, because the file built to stop that is
empty. The estate noticed the symptom at hub level and built
[`../traps.md`](../traps.md) to fix it *for fleet-manager only* — while the same
file, shipped to all 14, sat blank.

### 2.3 `docs/ideas/` never opened at all

Virgin README (byte-identical to the planted template) **and** zero idea files:
`creator-kit`, `idea-engine`, `product-forge`, `shiftlife`, `sim-lab`.

The sharpest pair: **`idea-engine` has 503 session cards and 0 files in
`docs/ideas/`**; `sim-lab` has 259 and 0. *(`idea-engine`'s canonical idea corpus
is 566 fleet-era files held elsewhere in that repo — see
[`../ESTATE.md`](../ESTATE.md) — so this is a statement about the kit's channel,
not about the repo having no ideas. The kit's channel is unused.)*

### 2.4 The apparatus is uneven in ways nobody can currently see

- **`AGENTS.md` exists in 0 of 19 non-archived repositories.** Every
  ChatGPT/Codex session in the estate boots with no boot file, everywhere.
  `@codex` reviews every PR the owner opens.
- **Kit versions have drifted silently — five live versions across 16
  adopters**, `MEASURED` over *every* non-archived repo (an earlier draft said
  "three versions" from a **ten-repo sample**, and the estate's own records
  already contradicted it — `@codex`, fm #949; the same sample-as-population
  error this plan warns about, made inside it):
  **1.21.0** ×10 (`couch-legend`, `creator-kit`, `fleet-manager`, `gba-homebrew`,
  `idea-engine`, `substrate-kit`, `superbot`, `superbot-next`, `venture-lab`,
  `websites`) · **1.20.2** `spider-swing` · **1.20.1** `shiftlife` ·
  **1.15.0** ×3 (`pokemon-mod-lab`, `sim-lab`, `superbot-plugin-hello`) ·
  **1.7.0** `product-forge`. `pokemon-mod-lab` is owner-held on its upgrade
  (program, 2026-08-14), so a laggard is not automatically a defect.
- **No `.claude/` at all:** `product-forge`, `creator-kit`, `spider-bot`,
  `estate-backups`.
- **No kit and no session cards at all:** `spider-bot` (live in production),
  `estate-backups`, `curious-research`, `superbot-plugin-hello`.
- **Planted docs still byte-identical to the kit's planted copy** — a
  mechanical "how much of this repo speaks for itself" gauge. **It proves
  current identity, not that nobody ever edited**: an edit and a revert leave
  the same hash (`@codex`, fm #949). The same caveat governs every "untouched"
  and "virgin" label in this document — none of them inspected commit history.
  Ratios: `creator-kit` **25/25**, `product-forge` **15/19**,
  `idea-engine` 19/26, `couch-legend` 13/26, `spider-swing` 12/26, `websites`
  7/10, fleet-manager 7/22.
  **Not a score — a prompt to look.** `websites` is a healthy repo with a high
  ratio; a small repo does not need all 26 kit documents filled. Read it as
  "how much of this repo speaks for itself", never as a grade.

## 3 · The reframe — it is not a memory problem

`DERIVED`, and it is the load-bearing inference of this plan.

The owner's instinct is that there is too much for an agent to hold. The
measurement says otherwise: **the session card is long, structured, demanding
and complied with 2,849 times.** Volume is not the binding constraint.

**What separates the card from the idea and the journal is not size. It is that
the card is demanded at a moment, by a gate, in a machine-checkable shape.**

```
gated at a moment              → 2,849 done
asked for in prose, at the end → 3 done
```

**Narrowed under review, and the narrowing matters (`@codex`, fm #949).** That
comparison changes **four** things at once, not one: the card is gated, it is
*also* auto-drafted by the kit when missing, it is structurally templated, and
an idea or a journal entry is materially harder semantic work than filling a
known slot. So the evidence supports **"the card mechanism vastly outperforms
prose instruction"** and does **not** isolate the gate as the operative
variable, nor settle that memory plays no part. The claim this plan acts on is
the narrow one — and it is enough, because every move below improves the
mechanism rather than asking anyone to remember more. A clean test would hold
difficulty constant: gate one artifact of comparable semantic weight and
measure. **That test is not run, and the plan does not pretend it was.**
This is the estate's own law, already written and already measured:
[`../findings/2026-08-08-why-rules-dont-bind.md`](../findings/2026-08-08-why-rules-dont-bind.md)
found **116 committed statements across 66 files catching 0 of 16 incidents**,
and [`../intent.md`](../intent.md) § 4 rules that *"the fix for an unfollowed
rule is a mechanism that delivers it at the right moment, never another
statement of it."* The ideas-and-journal contract is the largest surviving
instance of the thing that law forbids.

**So the owner's three fixes rate differently than they feel:**

| his fix | verdict |
|---|---|
| shorter, more specific files | reduces reading cost; **does not change compliance** — the card is neither short nor optional |
| enforce through hooks | **the one that works.** Everything with high compliance in this estate is hooked or gated |
| per-repo boot files in fleet-manager | good, and **structurally limited**: they load only in a fleet-manager-rooted session, so they cannot reach an agent working inside a satellite |

**Where "too much information" *is* real:** not in what an agent must comply
with, but in what it must **find**. 19 repositories, no per-repo digest, and a
satellite session that loads none of this hub's apparatus. That is a retrieval
problem, and § 5 Move 2 answers it with compression rather than deletion.

## 4 · What already exists — this plan builds nothing it can reuse

`MEASURED` 2026-08-26 by reading the `websites` tree and `app/main.py`.

- **The owner-writeback engine is already built.** `app/writeback.py` (ORDER
  020): *"the owner authors on the site, git gets the truth."* It maps a gated
  owner submission to one GitHub contents-API commit, stores it first in a local
  audit log, and **never claims a commit that did not land**. Three kinds today:
  `assist` → an ORDER block, `note` → `docs/owner/owner-notes.md`, `complete`.
  **Two things make it unusable as-is:** it commits to `menno420/websites`, not
  fleet-manager, and its destinations are seat-era. **And the deployed token is
  READ-scoped**, so a write 403s until the owner pastes a write-scoped PAT into
  Railway. The owner's comment idea is therefore a **repoint, not a build**.
- **The control plane has a per-*something* detail page pointed at a dead
  abstraction.** `/projects/{package}` and `/fleet` render the terminated seat
  roster. There is no per-**repo** page; `/journal/{repo}` browses journals, not
  configuration or intent.
- **The site's house style is drift, not inventory** — `freshness`, `codedrift`,
  `releasedrift`, `envdrift` all exist.
- **The generate-then-render pattern shipped today** in
  [`../activity/`](../activity/README.md): a generator in `tools/`, a committed
  artefact, a reader. The manifest below is its second instance.

## 5 · The plan — three moves, in this order

### Move 1 · Gate the next-agent contribution (closes § 2.1–2.3)

The card already carries a required `💡` marker, so an *idea sentence* is
gated — but it dies on a card nobody re-reads. Nothing carries it into
`docs/ideas/`, and nothing asks for the journal at all.

**Do:** add **one closed-vocabulary marker** to the card grammar, checked in the
added-card lane exactly as the existing markers are:

```
- **♻ Carried forward:** idea | journal | both | null — <one line>
```

The checker's whole rule, and it reads no prose (`@codex`, fm #949 — an earlier
draft said *"when a card claims a new idea"*, which requires deciding what a
free-form sentence means, i.e. the semantic grading the next paragraph forbids):

| value | required in the same diff |
|---|---|
| `idea` | a change under `docs/ideas/` |
| `journal` | a change to `.session-journal.md` |
| `both` | both |
| `null` | nothing — and the one-line reason is the record |

**Do not grade the content.** This estate has withdrawn two gates for
mechanising meaning
([`../../.claude/skills/session-close/SKILL.md`](../../.claude/skills/session-close/SKILL.md)
step 5b). The gate checks a **declared value against a file delta** — both
mechanical — and `null` stays a first-class answer, the way the Layer-2 handoff
line makes `null` legitimate. A session can still declare `null` dishonestly;
that is deliberate, because the alternative is a checker reading prose.

**Ship it in substrate-kit, not here** — roadmap § 5.3: the kit owns the
universal method, each repo owns its specialisation.

**But shipping is not inheriting, and that gap is the move's real cost
(`@codex`, fm #949).** Adopters vendor a *pinned* release and upgrade
independently — § 2.4 measures **five live versions across 16 adopters**, three
of them at 1.15.0 and one at 1.7.0 — so a checker released into the kit changes
nothing in a repo until that repo upgrades. **Move 1 is therefore two things:
the checker, and a rollout wave** (`upgrade-distribution`, one adopter at a
time, born-red PR each). Any claim that the inflow closes estate-wide is a claim
about the *wave*, not about the release. And `pokemon-mod-lab`'s upgrade is
owner-held (program, 2026-08-14), so the wave has an owner-gated row in it.

### Move 2 · The per-repo digest — one generator, two readers

`OWNER`: *"every repo should be featured and have multiple subsections under it,
so I can see things like the claude.md, the reading order, summaries of certain
files"* — and *"I do not want this to be a direct clone of a repo."*

**Do:** a generator in `tools/` producing a committed per-repo digest carrying

- **Configured** — kit version and delta · `.claude/` apparatus · `AGENTS.md` ·
  card protocol · required checks · gate command · deploy binding · live
  scheduled workflows · last local-session touch (the `📍 Venue:` token) ·
  planted-docs-untouched ratio.
- **Intent** — the declared entry point from [`../ESTATE.md`](../ESTATE.md),
  whether it exists, its date, written-or-still-template · Layer-2 threads · the
  dated audit verdict, stamped as a judgement and never as live state.
- **Digest** — short summaries of the files that matter, written by an agent and
  committed. This is the part that is not derivable, and it is the part that
  answers "too much information": **the digest is the compression layer**, so an
  agent reads one page instead of a tree.

**Derive the field list, never write it.** Diff each repo's whole
`substrate.config.json` against a reference so new keys appear by themselves.
Every hand-written enumeration in this repo has gone stale — the hook count, the
check list, the skills count, and twice in the session that wrote this file.

**Generated is not the same as fresh — the digest needs a freshness contract
(`@codex`, fm #949).** § 8 rules out a schedule, and the digest additionally
carries hand-written summaries plus volatile facts (deploy bindings, live
workflows, required checks). Without one it becomes the thing this plan exists
to remove: an inherited state rendered as current. Minimum:

- a **`measured_at` stamp per repo**, rendered in the open, never in a footer;
- a **staleness threshold** — the kit's own `cadence.staleness_days` is 14 —
  after which the page marks the row stale **rather than hiding it**;
- **refresh at the moment of use**: the session-close skill regenerates the
  digest for a repo it worked, the same way the born-red card is written for a
  session it ran. That is refresh-on-touch, not a cron, and it keeps the
  active repos current while letting resting ones visibly age.

**Two readers, one artefact:** an agent reads the markdown; the control plane
renders it.

### Move 3 · The review surface (closes the owner's loop)

`OWNER`: *"allowing me to leave a comment wherever I feel like the agents did
not understand my intent or their tasks properly … it gives me an easy way to
look at what I think is important in each repo while the agent works, so I can
also have visual confirmation about what I believe to be true."*

**Do:** `/repos` and `/repos/{name}` on the control plane, rendering Move 2's
digest, behind the existing owner gate (`app/owner_login.py`); extend
`writeback.py` with a fleet-manager target and a per-repo comment kind so a
comment becomes a committed file; then
**route that file to the next agent working that repo**, so a correction is
delivered at the moment of action rather than filed where nobody looks.

**The comment is only worth building if it lands somewhere agents read.** A
comment box writing to a database is worse than no comment box: it feels like
the loop closed. The route is the deliverable, not the box.

**Then retire or repoint `/fleet` and `/projects`.** Leaving them up means two
competing answers to "what is the estate," one of them describing seats
terminated 2026-07-21 — on the owner's own board. The review site's era framing
was fixed in websites #512; the control plane's was not.

### Sequencing, and why this order

`OWNER`: *"once this is all more orderly, I intend to have more in depth
conversations with multiple claude sessions to really take my time and map out
the proper intent and goals of each repo."*

Those conversations are the expensive part — fleet-manager's own intent document
took **21 questions answered by him**, and there are 19 repositories. **Move 2
is what makes them cheap:** each conversation starts from a digest that already
says what exists, what is configured, what is missing and what the last session
did, so his time goes to *intent* instead of to reconstruction. **One order, stated once, and § 9 does not contradict it (`@codex`, fm #949 —
an earlier draft had Move 1 "parallel" here and "first" there, which leaves an
implementing session unable to tell what to start):**

> **Move 1 → Move 2 → the intent conversations → Move 3.**

Move 1 leads because it is the only one that shrinks the problem while nobody is
working a repo (§ 9 lever 2). Its *checker* is small; its *rollout wave* is the
long pole and runs alongside Move 2 rather than blocking it — that is the only
concurrency in this plan, and it is between the wave and Move 2, never between
Move 1 and Move 2.

## 6 · The risk this plan carries

`DERIVED`, and it is the objection to take seriously: **this is a plan to add
surfaces to an estate whose stated problem is too many surfaces.**

The constraint that answers it, and every item above is checked against it:

> **Nothing hand-maintained gets added. Every new surface is either derived from
> the repositories (so it cannot rot), or replaces a seat-era surface (so the
> count goes down).**

The digest is generated. The config panel is generated. The comment is a commit,
not a document to maintain. `/repos` replaces `/projects` and `/fleet` rather
than joining them. The one genuinely hand-written addition is the per-file
summaries — and those are the compression that removes reading elsewhere.

## 7 · Owner-only

- **A write-scoped PAT in Railway** for `writeback.py`. Today's is read-scoped
  and a contents PUT 403s; the engine handles that honestly, but the comment
  loop cannot close without it.
- **The intent conversations themselves.** Intent is produced by asking him. No
  session derives it from the decision record — that was tried and
  [the roadmap § 4.6](2026-08-08-agent-operating-environment-roadmap.md) records
  that **20 of 21 questions were unanswered anywhere in the corpus**.
- **Whether `AGENTS.md` lands estate-wide** (`OQ-FM-AGENTS-BOOT`, currently
  scoped to this repo; § 2.4 shows it is estate-wide). **ANSWERED 2026-08-28:
  yes, estate-wide** — *"Agents.md should indeed be everywhere"*
  ([owner direction](../findings/2026-08-28-owner-direction.md) § 5); rollout
  is PKT-B4, sequenced, and waits on his GO for plan execution.

## 8 · Honest nulls

- **The kit's own interview mechanism is dead, not underused.** `open_questions`,
  `mode` and `promotion_rights` are identical and empty in every repo (`0`,
  `guided`, `propose`). Do not build on it.
- **No compliance measurement exists for the other 13 repos' ideas-per-session
  ratio.** § 2.1's ~2 % is fleet-manager's, measured; the others are shown by
  presence/absence only. The estate-wide ratio is unmeasured.
- **Nothing here is scheduled.** No cron, no bot commits. The estate has been
  retiring those (superbot #2450), and a generated file is corrected by one
  command.

## 9 · How to work through 19 repositories without a 19-session slog

`DERIVED`. **The failure mode to design against is already on the record:** D2 has existed
since 2026-07-26 with a per-repo acceptance test, and in a month **one repo has
had a completed truth pass** (fleet-manager; `substrate-kit` is recorded
partial). `idea-engine` and `sim-lab` had front-door fixes landed, and
`spider-swing` and `product-forge` were *classified* — which the program's
2026-08-24 row is explicit changed what their fixes must be **without doing
them**. Audited is not fixed, and an earlier draft of this line counted
classifications as movement (`@codex`, fm #949). A plan that is a list of 19 repos will do the same.
Five levers, in the order they matter.

**1 · The survey is a command, not a sweep.** Everything in § 2 and § 2.4 — kit
versions, apparatus presence, planted-doc ratios, ideas and journals across all
19 repositories — came from **one script run this session**, not from 19 reads.
Move 2's generator makes that repeatable. So the per-repo cost drops to the part
that genuinely needs a mind: the summaries and the intent. Everything a machine
can see, a machine should already have seen before anyone opens a session.

**2 · Move 1 first, because it is the only one that makes the problem shrink
while nobody is working.** It is listed as parallel because it lives in the kit
and blocks nothing — but it is the move that stops the bleeding. Once the
next-agent contribution is gated, every future session in every repo adds to the
record instead of drawing from it. Draining a backlog that is still filling is
bailing; this closes the inflow.

**3 · Traffic decides the order, not tidiness.** A stale front door in a repo
nobody opens costs nothing until someone arrives. **Use the surviving *ordering*, not those numbers.** The program's 2026-08-23
row quotes `fleet-manager` 99 · `superbot` 64 · `websites` 19 · `couch-legend`
18 · `spider-swing` 2 — and **its own 2026-08-24 row retracts them as a
comparable set**: no 14-day window ending on 08-23 reproduces the 99 (595 PRs
swept, range 83–93), so *"they came from different methods and must never be
mixed"*, and `spider-swing` re-reads **5**, not 2. What that re-measurement
explicitly preserved is the **ordering**; what it killed is *dormant*. So rank
by a **single-window measurement taken fresh**, and read the old figures as
order only (`@codex`, fm #949 — I cited a corrected row without reading its
correction, which is the un-propagated-correction class this repo keeps a
checker for). Do **not** rank by last-commit dates: this repo did that once and
withdrew it under review the same session.

**4 · Where traffic ties, the intent audit's rule breaks it** — already written,
already argued: *contradicting beats empty; among contradicting, the one whose
falsehood is not corrected on contact goes first; a running clock breaks any
remaining tie* ([the audit](../findings/2026-08-23-active-repo-intent-audit.md)
§ 6). Do not invent a second ranking rule.

**5 · Size the owner's input per repo, and batch it by cluster.** fleet-manager's
intent needed **21 questions** because it is the hub and the corpus answered
almost none of them. A small repo needs three: *what is this for · what is
explicitly not in scope · what would make you call it working.* Cluster the
sittings — the bots, the games, the labs — so one conversation covers several,
and let the digest carry the reconstruction so his time goes to intent alone.

**The test that keeps this honest.** If **Move 1 lands and nothing else does**,
the estate is still better off, because the contract self-heals from that point
forward. If **Move 3 lands first and Move 1 never does**, the website renders a
decaying picture beautifully. So Move 1 is the one that must not slip, and any
session that reports progress on this plan should say where Move 1 stands before
anything else.
