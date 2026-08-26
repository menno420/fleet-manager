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

**fleet-manager ran 163 sessions between 2026-07-22 and 2026-08-26 and added 3
ideas.** The `session-close` skill says every session *"groom one idea forward;
add one new 💡 idea you genuinely believe in."* Compliance is **~2 %**.

Method: `ls .sessions/` filtered to dated cards from 2026-07-22; `ls
docs/ideas/*.md` grouped by the date in the filename — **15 of 18 are dated
2026-07-09/10/11**, inside the EAP fortnight, when a seat was *ordered* to file
them. Three are from August.

### 2.2 The journal is worse, and it is the one that costs the most

`.session-journal.md` is the kit's cross-session process memory. Its own
headings are *"Recurring problems + fixes — so the next session doesn't
re-discover them."*

**Untouched planted template in 11 of 14 kit repositories.** Written in three:
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
- **Kit versions have drifted silently:** `product-forge` at **1.7.0**,
  `spider-swing` at **1.20.2**, the rest at **1.21.0**.
- **No `.claude/` at all:** `product-forge`, `creator-kit`, `spider-bot`,
  `estate-backups`.
- **No kit and no session cards at all:** `spider-bot` (live in production),
  `estate-backups`, `curious-research`, `superbot-plugin-hello`.
- **Planted docs never edited** — a mechanical "nobody has written this repo's
  own truth" gauge: `creator-kit` **25/25**, `product-forge` **15/19**,
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
gated at a moment          → 2,849 done
asked for in prose, at the end → 3 done
```

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

**Do:** a deterministic checker in the added-card lane — when a session card
claims a new idea or records a recurring problem, require a corresponding change
to `docs/ideas/` or `.session-journal.md` in the same diff.

**Do not:** grade the content. This estate has withdrawn two gates for
mechanising meaning
([`../../.claude/skills/session-close/SKILL.md`](../../.claude/skills/session-close/SKILL.md)
step 5b). Check **presence of a delta**, never quality — and make "nothing
learned this session" an explicit, writable answer, the way the Layer-2 handoff
line makes `null` a legitimate outcome.

**Ship it in substrate-kit, not here**, so all 14 repos inherit it. That is
roadmap § 5.3: the kit owns the universal method; each repo owns its
specialisation.

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

**Two readers, one artefact:** an agent reads the markdown; the control plane
renders it.

### Move 3 · The review surface (closes the owner's loop)

`OWNER`: *"allowing me to leave a comment wherever I feel like the agents did
not understand my intent or their tasks properly … it gives me an easy way to
look at what I think is important in each repo while the agent works, so I can
also have visual confirmation about what I believe to be true."*

**Do:** `/repos` and `/repos/{name}` on the control plane, rendering Move 2's
digest, behind the existing owner gate (`app/owner_login.py`); repoint
`writeback.py` at fleet-manager so a comment becomes a committed file; then
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
did, so his time goes to *intent* instead of to reconstruction. So the order is
**Move 2 → the intent conversations → Move 3**, with Move 1 running in parallel
because it lives in the kit and blocks nothing.

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
  scoped to this repo; § 2.4 shows it is estate-wide).

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
