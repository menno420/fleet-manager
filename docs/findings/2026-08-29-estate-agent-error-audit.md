# The estate-wide agent-error harvest — OD-24 §6 step 1, extended

> **Status:** `living-ledger` · opened 2026-08-29 · **complete** — all eight
> sections landed; nine Codex findings conceded and folded in (fm #967).
>
> **What this is:** the drift-incident corpus OD-24 §6 step 1 asked for, taken
> at estate scale. The [genesis dig](2026-08-28-substrate-kit-genesis-dig.md)
> executed step 1 **fleet-manager-side only**, over the August window, and its
> §9 names the remainder as skipped: the eighteen satellite repositories, the
> June/July bulk, and superbot's PR review threads. This is that remainder.
>
> Certainty tags per
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).

## 0 · The corpus

`MEASURED` 2026-08-28/29. Two deliberately independent halves — session cards
are **self-reported**, review comments are **externally caught after the agent
declared the work done**.

| source | volume | span |
|---|---|---|
| Records, 20 repositories | **7,214 error-bearing sections** → 68 shards — **89 % from `.sessions/` cards, 10 % from findings, retros, audits, reviews, trap files, program docs, `CLAUDE.md` and control records** | 2026-05-29 → 2026-08-28 |
| PR review comments, 12 repositories | **1,592** — 155 attributed to `menno420`, **1,437 not**, of which 1,431 are the Codex reviewer and 6 are code-scanning | 2026-06-17 → 2026-08-28 |
| Per-repo instruction surfaces | **20 of 20** censused | at HEAD |

**Two instrument defects, both found by review and both measured rather than
estimated** (Codex fm #967 R2):

- **The corpus was never card-only.** `fetch.sh` extracts findings, retros,
  audits and program docs too, and `extract.py` walks every Markdown file. An
  earlier cut of the table above called it *"4,583 cards → 7,214 sections"*,
  which mislabelled a mixed corpus. Re-counted by document type: **6,544 card
  sections (89 %), 797 from other documents (10 %)**. The W1 half is therefore
  *predominantly* self-report, not purely.
- **The error lexicon was partly dead.** `ERR_LEX` was compiled with `re.X`,
  which silently strips the literal spaces inside multi-word alternatives, so
  `was wrong` matched `waswrong` and never fired — 6 of 7 tested phrases were
  inert. **Measured impact after fixing it and re-running the whole extraction:
  7,341 sections against the published 7,214, +127 (+1 %)** — small, because
  the heading match already selected most sections and the single-token
  alternatives (`stale`, `drift`, `assumed`, `inferred`, `conceded`) carried the
  rest. The defect is real; its effect on corpus size is not. Effect on
  *composition* is unquantified.

Re-derivable: the five scripts are retained at
[`../../tools/agent_error_audit/`](../../tools/agent_error_audit/README.md)
(`census.py` → `fetch.sh` → `extract.py` → `shard.py` → `reviews.py`). The
**corpus itself is not committed** — it is 47 MB of other repositories' records
— so re-running the scripts reproduces it rather than reading it from here.

---

## 1 · The identity collision — the owner has no distinguishable voice on GitHub

**This is the finding with the widest blast radius, and no record in this
estate names it.**

`MEASURED` 2026-08-29, two endpoints, with positive controls:

| population | attributed to `menno420` | agent-authored |
|---|---|---|
| PR **review** comments (12 repos) | **155** | **135 (87 %)** by literal marker; the remaining 20 read identically (judged, not marker-matched) |
| **Issue** comments (6 busiest repos) | **564** | **499** by literal marker · **55** more by agent operational voice · **10 residue, every one read in full** |

**The 10-comment residue is enumerated rather than sampled** — an earlier cut of
this section characterised 65 comments from reading 14, which is TRAP-004 inside
the document whose §3 lists this session's errors. Read in full: five are
`spider-swing` landing reports (*"Phase 0 implementation merged in PR #6 as
`e5ec3c5`"*), two are structured `## Plan addendum` bodies, one opens
**_"Roadmap review decisions from owner:"_** — an agent relaying his decisions
**in the third person, under his account** — and two (a 2026-05-20 triage note, a
2026-06-14 duplicate-supersede) are too short to attribute from text either way.

**Scope, exactly:** of 564, **562 are attributable to agents and 2 are
indeterminate; none is identifiably the owner's first-person voice.** The
sharpest single line in the residue is an agent writing *"Menno also confirmed
the PR #8 Reel and DEBUG controls now work on Android"* — referring to the owner
in the third person from the owner's own account.

**Positive control:** the same marker regex over the 1,437 external-reviewer
comments returns **0** Claude Code footers and **1** disposition token, so the
markers discriminate rather than matching everything.

**Author distribution across those 6 repos:** `menno420` 564 · the reviewer bot
198 · dependabot 35 · code-scanning 1. **There is no separate identity for the
owner anywhere in it.**

The cause is mundane and was never written down: **agents authenticate with
`$GITHUB_PAT`, which is the owner's own credential**, so every comment, review
reply and PR body an agent posts is authored by `menno420`. The estate records
the PAT's *capabilities* in several places
(`docs/execution-surfaces.md`, `docs/providers/claude.md`) and its *attribution
consequence* in none — a grep for any record of agents posting under the owner's
identity returns nothing, against a positive control confirming the grep style
finds PAT records.

**Why it matters more than an attribution nit:**

1. **The `OWNER` certainty tag is unfalsifiable from GitHub.** The legend reads
   *"The owner stated it… Act on it. Do not probe first."* — the estate's
   strongest instruction, and on GitHub nothing distinguishes his statement from
   an agent's paraphrase of one.
2. **It is the mechanism behind a defect already observed independently.** The
   review corpus surfaced *"Inference filed as the owner's words"* (n=5, high)
   and two clean owner-authority fabrications: **OD-6 cited as capping landings
   per session when its text explicitly refuses to**, and **`spider-swing`
   promoted from an agent's own recommendation to a settled roadmap decision**.
   Both landed in artifacts whose job is to brief the next session. TRAP-005's
   mirror image: not failing to believe the owner, but manufacturing him.
3. **It contradicts an assumption the owner-comments apparatus rests on.**
   `docs/owner-comments/` exists to carry the owner's wording durably; its
   records are trusted as his. Nothing in the contract establishes authorship,
   because on the surface it draws from, authorship cannot be established.

**What it does NOT mean:** the owner's *chat* statements are unaffected — those
arrive through a channel agents cannot author. This is specific to GitHub-hosted
text. `REASONED`: the same collision applies to any surface reached with his
credentials (Railway, releases, gists), untested here.

**Consequence for this audit, stated because it cost a claim:** this session
told the owner the 155 comments were "his own voice — the highest-signal source
in the estate," and built a whole workflow lane on it. **Zero of them are.** One
harvest lane refused the premise, measured it, and reported an honest null
rather than filling the field — the correct behaviour, and it is what surfaced
this section.

---

## 2 · The enforcement census — 328 prose-only rules across 20 repositories

`MEASURED` 2026-08-29, one reader lane per repository over its `CLAUDE.md`,
`.claude/`, hooks, settings, checkers and recent cards.

| | |
|---|---|
| Rules stated with **no mechanism** delivering or checking them | **328** |
| Classified enforcement rows | **216** — of which **172 are mechanical** (78 checker · 55 CI · 39 hook) and 44 are not (25 prose-only · 19 none) |
| Repositories with kit divergences an upgrade would silently revert | **20 of 20** (2–10 each) |

So the contrast that matters is **328 prose-only rules against 172 mechanical
enforcers**, not against 216. This is OD-24 §6 step 2's taxonomy filled in with
a number: the dominant class
is **stated but undelivered**, exactly as the genesis dig predicted from a much
smaller sample.

The per-repo gaps are concrete, not atmospheric — `superbot-games` and
`superbot-idle` have **no `.claude/` directory at all** while carrying 18–24
stated instructions each; `spider-bot`'s landing path (push to main deploys to
production, CI informational) **defeats every mechanism the repo has**;
`substrate-kit`'s own flagship doctrine is the one thing it ships no mechanism
for. `fleet-manager`'s biggest gap is the moment *before* the first tool call.

**Load-bearing caveat:** each census is one lane's single read, and several
lanes wrote scope caveats into a schema field rather than the body, so the
counts are a **first pass, not a verified inventory**. The 328 should be read as
*"this order of magnitude, per this method"*, not as a countable register.

---

## 3 · Method, and where it under-performed

Two workflows: 68 harvest lanes over the card shards, 12 over the review shards,
20 census lanes, then per-class synthesis and a three-lens adversarial panel
(refute · already-covered · buildable).

**The panel did not discriminate, and that is a finding about the method rather
than about the estate.** On the review corpus it returned **140 survivors from
141 candidates — a 99.3 % pass rate**. A panel that refutes 1 in 141 is not
evidence that 140 patterns are real; it is evidence the bar was set where
nothing fails it. The survival rule (`refuters < 2` of 3 lenses) let a single
dissent be outvoted by two lenses answering *different questions* — only one of
the three was actually asked to refute. **The 140 are candidates. They are not
findings, and this document does not present them as any.**

`REASONED`, for the next pass: make all three lenses refute, from different
angles, and require the refuter to open the cited artifact.

### This session's own errors, recorded as corpus

Four, and three compress to one sentence — **a conclusion drawn from an absence
that the circumstance already explains**:

1. An extraction returned **564** sections instead of 7,214; Python's `glob`
   does not match dot-directories, so `.sessions/` was never scanned.
2. `merge-on-green` written into a published PR comment as *"already passing"*;
   it had no result on that head at all.
3. *"The session volume does not survive a container"* — inferred from no file
   predating the boot, which was the session's **first** container, so nothing
   older could exist. Disproved at 23:48:12Z when the container **was** replaced
   and the 47M corpus and both journals survived intact.
4. *"The census came back empty"* — the task output nests everything under
   `result` and the query read the top level. Caught in the same command by a
   fallback that went to the journal.

The fourth is the same class again and was caught **because a positive control
was built into the query rather than run afterwards** — which is the practical
form of the fix, and cheaper than the trap it prevents.

---

## 4 · The structural finding — the delivery layer cannot reach the errors

`MEASURED` in fleet-manager's live tree, 2026-08-29, and re-verified by hand
against the workflow's own claim:

| | |
|---|---|
| doc-routes total | **71** |
| …that can fire on an `Edit`/`Write` | **8** |
| …that can fire on a `Bash` | **42** |
| …that can fire on **both** | **0** |
| …that fire on neither (prompt-event only) | 21 |
| …carrying `repeat: true` | **1** (`card-flip-before-push`) |

`DEFAULT_TOOLS` in `route_docs.py:77` is `("Bash", "WebFetch", "Read", "Glob",
"Grep")` — **`Edit` and `Write` are excluded**, so a route reaches write-time
authoring only by naming those tools explicitly.

> **⚑ THE TABLE ABOVE IS AS-MEASURED AT `8a3a13d`, AND `main` HAS SINCE MOVED.**
> [fm #963](https://github.com/menno420/fleet-manager/pull/963) merged
> (`25f80fd`) **while this finding was being written**, and it fixes exactly
> this gap. Re-measured at the merged head: **Edit/Write-only 8 → 0 · reaching
> BOTH 0 → 8 · `repeat: true` 1 → 10 · `authored_only` 8**. So the *disjointness*
> defect is **closed on `main`** and the eight claim-quality routes now fire on
> Bash heredoc authoring too.
>
> The finding keeps both numbers rather than silently restating the current
> one: the corpus was harvested under the old behaviour, so every incident it
> counts happened in a world where those eight routes were disarmed. Presenting
> only the fixed figure would make the evidence unreadable — and presenting only
> the old one would be TRAP-001, in a document about TRAP-001. **What survives
> the fix untouched is everything below: the kit ships no routing, and 19 of 20
> repositories have no hook layer to route into.**

Two further measurements complete the picture:

- **`fleet-manager` wires no `SessionStart` hook.** Its `.claude/settings.json`
  registers `PreToolUse`, `PostToolUse`, `Stop`, `UserPromptSubmit` — nothing at
  session boot, which is the moment OD-24 §4's cross-session chain needs.
- **The kit ships no routing at all.** `grep -c -E "route_docs|doc-routes"
  bootstrap.py` → **0**, against a positive control of 203 hits for `hook` in
  the same file.
- **And no adopter has built its own.** `MEASURED` adopter-by-adopter after
  Codex refused the inference twice (fm #967 R1 and R2, both P1). The first pass
  searched only the fleet-manager filenames `doc-routes.json` and
  `route_docs.py`, which proves 19 repositories lack *that implementation* and
  not that none routes by another name. **Broadened:** every repository's tree
  searched for any `.claude/hooks/` file at all — **1 of 20 has one, and it is
  fleet-manager (8 files)**. The `*route*` hits elsewhere are product code (bot
  command routing, rom-hack tables), not agent-instruction delivery. Since a
  hook is the only tool-time injection point available to Claude Code, that is
  as close to exhaustive as this instrument gets. The trap-register lifecycle
  (*mistake → trap → route → checker*) therefore exists in one repository while
  most incidents in this corpus happened in the other nineteen. Per-repo table:
  [`../../tools/agent_error_audit/adopter_census.json`](../../tools/agent_error_audit/adopter_census.json).

**And the channel to fix it is already installed in 18 of the 20.** `MEASURED`
in the same census — `.substrate/hooks/settings.template.json` is present in 18
repositories; **`superbot` and `spider-bot` are the two exceptions**, so "every
adopter" was wrong and is corrected here. Where it exists it wires all four
events:

```
PreToolUse   → bootstrap.py hook pretooluse
SessionStart → bootstrap.py hook sessionstart
PostToolUse  → bootstrap.py hook postedit
Stop         → bootstrap.py hook stopcheck
```

So the highest-leverage kit slice is **not a new checker**. It is moving routing
and the hub's write-time hooks into a channel the kit already owns in 18 of the
20 repositories (the other two need the channel first). That is one structural change, and every checker below is worth
less until it lands.

---

## 5 · The convergence — what both corpora found independently

Session cards are what sessions **noticed about themselves**; review comments
are what an **external reviewer caught after the agent declared done**.

**They are not fully independent, and the overlap is now measured rather than
assumed.** Codex refused the original *"share no evidence"* claim (fm #967 R2,
P1) on the correct ground that `extract.py` deliberately selects
`review disposition` sections, so a reviewer finding can enter W1 as a card's
account of it and W2 as the original comment. Measured upper bound: **416 of
7,214 W1 sections (5 %) contain any reviewer vocabulary at all**, and **115
(1 %) are disposition-shaped sections mentioning the reviewer**. So corroboration
across the two is **mostly** independent, with a ≤5 % contamination ceiling —
not the clean separation originally claimed. Provenance matching per incident
was not performed.

**Method caveat, stated first:** the pairing below is **my reading** of two
independently-produced pattern sets, not a mechanical match. Names differ
between corpora; I matched on trigger and mechanism. Treat the pairing as
`REASONED` and the per-corpus counts as `MEASURED`.

| convergent pattern | cards (W1) | reviews (W2) |
|---|---|---|
| **A guard or verifier that cannot fail** — landed green, never seen red | n=29, 10 repos | 4 separate patterns (*gate shipped without a failing fixture* · *the verifier that cannot fail* · *guard fails open* · *never observed red*) |
| **A correction that leaves its own copies standing** | n=26, 9 repos | 2 patterns, n=20 (*superseded wording still delivered* · *survives elsewhere in the same file*) |
| **Green read as verification when the instrument could not see the failure** | n=27+30 | *green suite, wrong path* · *shipped without ever running it* · *under-reading tool publishing a completeness claim* |
| **A verdict written about an artifact never re-opened** | n=43, 11 repos | *writing about a file, workflow or mechanism never opened* |
| **A count written from memory** | n=30, 12 repos | 3 patterns (*stated count contradicting the thing counted* · *never measured at the revision it describes* · *arithmetic that does not close*) |
| **Enforcement vocabulary for a mechanism nothing implements** | n=17, 8 repos | *automation whose predicate means it never runs* · *registered in the defining surface, inert in the executing one* |
| **The companion record the diff owes, not shipped with it** | n=28, **13 repos** — the widest | *new artifact landed without its paired registration* · *paired surfaces updated asymmetrically* |

**Seven convergent pairings are shown, and seven is what this section claims.**
An earlier cut asserted *"ten of eleven top card patterns have a counterpart"*
without tabulating the other three; Codex refused it (fm #967) and the headline
is narrowed to the displayed evidence rather than the larger number.

**One card-corpus pattern is worth naming as explicitly NOT converging:** *the
handoff's stated state acted on instead of re-resolved at HEAD* (n=32, 12
repos). That supports rather than weakens the split — a stale handoff is
invisible to a reviewer reading a single PR, and only the session that inherited
it can see it.

### The five traps this earns

Each carries ≥2 named, dated instances across ≥2 repositories, per the register's
own bar. **Proposed, not registered** — §7.

- **TRAP-008 · A correction that leaves its own copies standing.**
- **TRAP-009 · Enforcement vocabulary for a mechanism nothing implements.**
  Its origin instance is the sharpest in the corpus: the **boot file** asserted
  `check_no_false_walls` was a required check while `grep -rn` over
  `.github/workflows/` returned nothing — *"in the one file whose job is to be
  true."*
- **TRAP-010 · A guard, test or checker that has never been seen red.**
- **TRAP-011 · A green from an instrument that could not have seen the failure.**
  Includes the owner-review hook dead all session behind a swallowed
  `ModuleNotFoundError`, its silence read as a pass.
- **TRAP-012 · A completion word beside a passing status field.** Extends
  TRAP-006 rather than replacing it. **Provenance differs from the other four:**
  it has no row in the convergence table — it rests on card-corpus evidence
  alone (three named instances across three repositories) and is therefore the
  weakest of the five on this audit's own standard.

---

## 6 · The era question — answered, and the half that cannot be

**The owner's "I stepped back and the agents forgot their purpose" hypothesis is
not visible in this corpus, and the honest answer separates two questions.**

What changed across the eras is the **kind** of error, and it tracks what the
work was:

- **2026-05/06 (superbot, effectively one repo):** engineering errors with
  product blast radius. **Both production outages in the entire three-month
  corpus are here**, each from a skipped grep.
- **2026-07 (the Projects program, ~13 repos in parallel):** coordination
  errors — claim files left on main across ~35 consecutive sessions, heartbeats
  contradicting the tree. High volume, near-zero blast radius outside a machine
  that no longer exists.
- **2026-08 (stepped back, single sessions):** epistemic errors in owner-facing
  artifacts — `MEASURED` badges on inferences, counts from memory, absence
  asserted without the search.

**The purpose-drift half is NOT answered here, and an earlier cut wrongly said
it was.** That cut argued the August records *"contain sessions doing exactly
the asked work"*. Codex refused it (fm #967 R2, P1) on a ground that is decisive
and mechanical: the extraction keeps only error-shaped headings and bodies with
lexicon hits, so **mission, goal, scope and work-summary sections were filtered
out of the corpus** — precisely the sections in which off-goal work would be
visible. The instrument can classify errors that were reported; it cannot see
whether the surrounding work served the ask. **So the hypothesis is untested,
not disproved**, and testing it needs a different extraction over the sections
this one discards.

What the corpus does support is narrower: within the reported-error population,
the *kind* of error tracks the era's work. Detection also improved sharply in
the same window, so a rising visible error count partly measures a better
instrument.

**The sharpest observed cluster — stated as an observation, not a trend.** A
distinct kind of incident is concentrated in August: rules broken by the session
that authored them, the same day. The DISCOVERY RULE violated three hours after
being written; TRAP-006 biting twice on the day it was registered; the densest
stale-record cluster falling on 2026-08-08 → 08-28 in fleet-manager — *where the
estate was actively studying this defect and kept committing it*.

An earlier cut called this *"what genuinely got worse"* and named delivery as
its cause. **Codex refused both halves and was right** (fm #967): a denser
observed cluster cannot establish worsening in the same document that rejects
cross-era rate comparison, and §4's route census shows a plausible *mechanism*
without establishing *causation*. So: the cluster is observed and dated; whether
it represents a real increase is unanswerable here for the same reason the rate
question is; and delivery is a **candidate** explanation, consistent with
[`2026-08-08-why-rules-dont-bind.md`](2026-08-08-why-rules-dont-bind.md)'s
measurement of 116 statements catching 0 of 16 incidents, not a demonstrated
cause.

**The half that cannot be answered:** there is no comparable per-session error
*rate* across eras. July ran ~15 parallel seats writing short formulaic cards;
August runs one session writing long, candid, adversarially-reviewed ones. The
denominator moves with the era, and the May/June slice is one repo against
twenty later. Any "errors per session, then vs now" would be TRAP-004 committed
inside a report about TRAP-004. **The kind question this corpus answers; the
rate question needs an instrument nobody has built.**

---

## 7 · What this does NOT establish

Recorded at the same weight as the findings, because the promotion rule depends
on it.

- **Nothing here is registered or built.** No trap is added to
  [`../traps.md`](../traps.md), no route, no checker, no skill edit. Under the
  roadmap's §6 promotion rule and OD-24 §3's freedom doctrine, a review round
  that emitted infrastructure before the owner saw it would recreate the
  wall-accretion he is correcting.
- **Every frequency here is an OBSERVED MENTION COUNT, not an incident count,
  and not a lower bound.** Two forces push in opposite directions and neither
  was measured. Errors nobody caught are structurally invisible, which
  under-counts; but **no deduplication was performed across cards**, so one
  incident discussed in a card, the next session's review of it and a later
  finding can enter three times, and the panels rejected almost nothing, so
  false positives survive. An earlier cut called every frequency a floor;
  Codex refused it (fm #967, P1) and it is withdrawn. Corpus-level precision
  and dedup are unmeasured.
- **Severity and the ranking are judgements**, not measurements. Cost per
  instance is unmeasured.
- **No false-positive rate was measured** for any proposed checker; each is an
  estimate from the predicate's shape.
- **The satellite repos' own gates were not inventoried.** *The kit ships no
  routing* is measured; *therefore the satellites have none* is an **inference**.
- **The adversarial panels under-performed.** 137 of 143 survived on the cards
  and 140 of 141 on the reviews — bars nothing fails. The §5 table is built from
  the top-ranked and cross-corpus-corroborated patterns rather than from
  survival, and the remaining ~270 candidates are held as raw material.
- **§2's 328 prose-only rules** is one lane's read per repo — an order of
  magnitude, not a register.
- **The corpus is 89 % cards, 10 % other records** — not the card-only
  population an earlier cut described.
- **The error lexicon was partly inert** (`re.X` ate multi-word phrases).
  Re-running with it fixed moved the section count +1 %; the effect on
  *composition* was not quantified.
- **The two corpora are ≤5 % contaminated**, so §5's convergence is mostly, not
  wholly, independent corroboration.
- **The purpose-drift question is untested**, because the extraction filters out
  the mission and scope sections that would answer it.
- **§4's route table is as-measured at `8a3a13d`**; `main` has since moved and
  fm #963 closed the disjointness defect. Both figures are kept deliberately.
- **The routing census searched for hook files**, which is exhaustive for Claude
  Code's tool-time injection but says nothing about reminders delivered by other
  means (prompt text, CI output, a repo's own scripts).
- **The retained scripts were themselves defective** in four ways review found —
  a dead lexicon, an unrunnable first step, and two failure paths that turned
  fetch errors into silently empty corpora. All four are fixed in the retained
  copies; the corpus this finding rests on was gathered with the old ones.

## 8 · The recommended next step

**One structural slice, measured before anything is promoted:** move routing
into the kit's existing hook channel, give the eight write-time routes `Bash`
reach (fm #963 does this for the hub already), and make the claim-quality routes
repeat. Then re-measure against this corpus: the incidents are dated and cited,
so *"would this route have fired on that instance"* is answerable rather than
asserted. Promote only what measures useful — §6 of the roadmap, verbatim.
