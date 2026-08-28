# The OD-24 round's discussion sitting — his answers, verbatim

> **Status:** `reference` · 2026-08-28, owner-live · the review-and-discussion
> sitting he selected as session 4 of the OD-24 round (*"the next session can
> review everything that these 3 audits have produced, and then helps me to
> discuss and answer the open questions"*).
>
> **What this is:** the answers as he gave them, in his own words or as the
> option he selected, recorded **as each arrived** rather than at the end —
> because answers that live only in chat are the exact loss mode this round
> exists to correct (dig § 5 regression 5; gap #8, *owner-words capture*,
> classed **absent**: three losses in one month with recurrence self-predicted).
>
> **What it is NOT:** the mechanisms. Everything marked `DERIVED` below is the
> session's reading of what his answer implies, governed by the
> [roadmap's § 6 promotion rule](../planning/2026-08-08-agent-operating-environment-roadmap.md)
> (observe → prototype → measure → promote). **Nothing here GOes a held
> packet** — OD-23's *"no execution yet"* stands untouched.
>
> Input: [the round's open-questions agenda](../planning/2026-08-28-od24-round-open-questions.md).
> Certainty tags per [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).

## 1 · Do the June rules still stand? — **most of them do** (agenda § 2 · A)

His answer, verbatim, and it is **none of the three options offered**:

> *"Some of them might not be relevant anymore, but most of it still stands."*

`OWNER`. The options were (a) they stand until you retire one · (b) they are
archaeology · (c) case by case. He gave a fourth: **standing is the default,
with an obsolescence exception he did not enumerate.**

`DERIVED`, and the direction of the default is what matters:

- **A June ruling binds unless shown otherwise.** A session may not treat the
  router's rulings as archaeology, and may not quietly drop one because it is
  old. This settles the re-read's § 2 census in the direction of *carry them*:
  the five rules it found absent from every live fleet-manager document
  (superbot:Q-0191 · Q-0128 · Q-0131 · Q-0229 · Q-0136) are live estate law
  that no live surface currently carries.
- **The exception is real but is not a session's to apply silently.** He said
  *some* may no longer be relevant; he did not say which, and under his own
  ratification doctrine (OD-24 § 3 — *"I agreed to them so they can indeed
  stay"*) retiring a rule is his act, not an agent's. So a session that judges
  a June rule obsolete **flags it for retirement with its reason** and keeps
  obeying it meanwhile. Writing "this is probably stale" into a record and
  acting as if it were retired is the failure this bullet exists to prevent.
- **What it does NOT license:** a rule-by-rule sweep of all thirteen census
  entries put to him one at a time. He was explicit in the agenda's own framing
  that walking them would consume the whole sitting, and his answer is a
  default precisely so the walk is unnecessary.

## 2 · May anything BLOCK a session from calling its work done? — **no** (agenda § 2 · B)

His selection: **"No — never block, just guarantee pickup."**

`OWNER` (option selected, not free text). This **confirms his own June design**
rather than overturning it: superbot:Q-0180 chose post-merge review
(*"make every final push mention @codex in the PR for a forced review"*) and
superbot:Q-0174 supplied the reason it was safe — the next session fixes what
the reviewer flagged, first. The re-read established that the owner-precedented
defect was never merge timing; it was the **missing consumption loop**.

`DERIVED`:

- **The gap-#7 fix is now fully specified and needs no further permission.**
  Build the consumption loop — the next session works reviewer findings first —
  and build **no blocking gate**. The agenda already classed the loop as
  needing no GO; his answer additionally forecloses the alternative, which
  matters because two audits left the blocking option live.
- **The five 2026-08-23 flip-before-review incidents are not to be fixed by a
  brake.** They stop being incidents-against-a-rule and become evidence that
  the consumption half was never built.
- **First measure, then build** (unchanged from the agenda's § 5): re-check
  whether the defect has recurred since the routes hardened on 2026-08-24. He
  retired an unused review gate himself once for exactly this reason
  (superbot:Q-0197) — an unused mechanism is the failure mode, not the fix.

## 3 · May a brake ever stop and ask him? — **presence decides** (agenda § 2 · B2)

His selection: **"Never while I'm away; freely when I'm present."**

`OWNER` (option selected). This is the fork the round could not derive, and his
answer **reconciles his two rules instead of choosing between them**:
superbot:Q-0128 (*"I never want to see such a prompt asking me for my
confirmation ever again, no matter what it is for"*, 06-13) and OD-24 § 3's
re-ratified *confirm before sending or deleting* were read as contradictory for
the length of this round. They are not: **Q-0128's grievance was the unattended
case** — a prompt nobody is there to answer — and the 2026-08-09 line he gave
about `delete_trigger` (*"this will stall your session untill I get back"*)
names that mechanism exactly. The confirm-first line governs the attended case.

`DERIVED`:

- **The doctrine, in one line:** a kit-planted brake may surface an interactive
  prompt **only when a human is present in the session**; in unattended runs it
  must decide — refuse or proceed — and never wait.
- **`delete_trigger` stays PREVENTED in every venue**, attended or not. It was
  carved out of all three options before he answered and no answer re-authorises
  it; fm's never-delete-a-trigger decision ([`decisions.md`](../decisions.md))
  and the denying `trigger_tools_guard.py` hook are unaffected.
- **Presence must be a computed fact, not a guess.** The estate already
  distinguishes the venues this needs (owner-live hub chat · scheduled wake ·
  unattended cloud session) — this is a routing question with an existing
  vocabulary, not new apparatus, and it is a session's to work out.
- **`OQ-KIT-PROMPT-DOCTRINE` is ANSWERED** by this row.

## 4 · Which ways does the kit still not work? — **one root cause, not twelve gaps** (agenda § 2 · 0)

The question nobody had ever asked him. His answer, verbatim:

> *"Most of these combines, they are all related to the same root cause, which
> is mostly that agents don't take enough initiative to leave the repos in a
> better shape"*

`OWNER`. He was offered four of **his own prior statements** (initiative ·
leave-it-better · re-explaining · too-much-to-remember) rather than this
round's audit findings, deliberately, so the comparison against our
reconstruction would not be anchored. He declined the multiple-choice framing
and collapsed all four into one cause.

**This is the round's headline measurement, and it re-ranks the round's own
output.** Three audit sessions reconstructed a failure list from the committed
record — twelve classified gaps, a 187-file doc census, a 208-ruling re-read —
and the agenda said in advance that a divergence between his list and ours
would be the most valuable thing this round could produce. There is a
divergence, and it is one of **altitude, not of fact**:

- **Ours ranked mechanism classes.** The dig's dominant finding was
  *unenforced/unrouted* — instructions that exist but never arrive at the
  moment of action — with twelve gaps laid out flat and the fix families
  (write / route / hook / build) attached per row.
- **His is a single cause with a direction:** *initiative to leave the repos in
  a better shape.* Every one of our twelve is downstream of it.
- **We had already found this and had already ranked it first — in the one
  place a session would not meet it.** Dig § 6.1 judged the kit's failure to
  name the initiative half of his purpose *"the central drift, present from
  founding, and the review round's real charter"*, and measured the word
  **initiative** returning zero hits across the kit's README, closeout and
  program-law register. That paragraph sat in an audit finding's intent-delta
  section; the round's working agenda then organised itself around the gap
  table instead. **The round reproduced, on itself, the exact defect it was
  auditing** — the right finding existed, unrouted, and the work aimed
  elsewhere.

`DERIVED`, and it is a re-ranking rather than new work:

- **The gap table stays valid and stops being the organising frame.** The
  twelve rows are symptoms; the question asked of any candidate fix is now
  *does this make a session more likely to leave the repo better than it found
  it?* — not *which gap class does this close?*
- **The kit's charter question (§ 2b) stops being cosmetic.** *Initiative*
  being absent from every purpose statement in the kit is no longer a
  word-presence curiosity: it is the root cause missing from the artefact
  built to serve it.
- **It does not re-open anything already answered.** His § 2 · B answer (never
  block) and § 2 · B2 answer (presence decides) bound how any initiative
  mechanism may behave: it may not gate, and it may not interrupt an
  unattended run.

## 5 · Does the per-repo journal survive? — **his call delegated, with a function named** (agenda § 2 · E2)

His answer, verbatim:

> *"Your call, if the router records are functional in the same way thats good
> enough. But I think the session journals would definitely add some value so
> we can easily find out what went wrong each session."*

`OWNER`. Two distinct things, and the second is the load-bearing one: he
**delegated the disposition** and, in the same breath, **named a function the
journal serves that nothing else currently does** — *easily find out what went
wrong each session*, per repo.

**The decision, taken here under that delegation** (`DERIVED`, and recorded as
a decision rather than an ask, per his standing *decide rather than default to
asking*):

**Keep the journal, re-scoped to the function he named, and route it before
enforcing it.**

The reasoning, and each leg is measured rather than preferred:

- **The file failed; the function did not.** The 11-of-14 byte-identical
  measurement, the zero checkers and the absence from every boot list are
  facts about a **planted five-section guidebook skeleton** — a shape nobody
  asked for. He did not ask for a guidebook. He asked for a per-repo trail of
  what went wrong.
- **Nothing else serves that function per repo.** Routed trap records
  (`traps.md`) carry *recurring, estate-general* traps and are the surface that
  demonstrably works; session cards carry *one session each* and are not read
  as a trail. Neither gives the per-repo "what went wrong here, repeatedly"
  view he described. His *"if the router records are functional in the same
  way"* is a genuine conditional, and the honest answer is **they are not** —
  they are estate-scoped, not per-repo.
- **Route first, enforce only on measurement.** The measured failure was never
  that sessions refused to write it: the file is on **no boot list**, **0 of
  37 checkers** reference it, and the single checker that touches its path
  exists to **exempt** it (`check_template_sync`'s `LIVE_TRAFFIC_DESTS`). A
  surface nothing points at has not been tested for adoption. So the first move
  is routing, adoption is measured, and enforcement is a later promotion
  decision under roadmap § 6 — never idea → mandatory infrastructure.
- **His anti-stub ruling is honoured, not overridden.** superbot:Q-0101
  (*"generating 24 stubs that then rot would be worse than the current gap"*)
  is a ruling against **planting empty files**, which is exactly what happened
  and exactly what this decision stops doing. A routed, re-scoped, unenforced
  surface is not the thing he ruled against.

**Open and explicitly not decided here:** the re-scoped journal's shape, and
whether it is one file or a section of an existing one. That is design, it
belongs to a build session, and inventing it now would be the
idea-to-infrastructure move the promotion rule forbids.

## 6 · AGENTS.md — **hand-write per repo** (agenda § 2 · E)

His selection: **"Hand-write per repo."**

`OWNER` (option selected). The kit does **not** plant or maintain the nineteen
files; PKT-B4's recorded hand-write-per-repo position is **confirmed by him**,
not overturned. He was shown the trade explicitly — that hand-writing has no
maintenance story, and that planting is what produced the byte-identical
journals — and chose hand-write anyway.

`DERIVED`:

- **This closes the fork twice over.** The agenda carried it in two places that
  disagreed — as § 2 · E (his, per his own direction record) and in § 5 as a
  session's call. His answer settles it either way; no session needs to decide
  it and none may re-open it.
- **The maintenance gap is now a known, accepted cost**, not an oversight. If
  the nineteen go stale, the answer is a session noticing and fixing them under
  OD-24 § 2's initiative duty — which is precisely the § 2 · 0 root cause. The
  two answers are consistent: he would rather have sessions that maintain
  things than templates that pretend to.
- **Execution stays behind the packet hold.** OD-23's *"no execution yet"* is
  untouched; this answers *how*, not *when*.

## 7 · Move 1 — **HELD** (agenda § 2 · C)

His selection: **"Hold — still planning."**

`OWNER` (option selected). Move 1 — the one line every session fills before it
can close (*did I leave an idea, a note in the running journal, both, or
nothing?*) — **stays held.** OD-23's *"no execution yet, because I still have
more to plan"* is re-affirmed rather than merely un-lifted; he was offered
three GO shapes and a hold, with the note that his § 2 · B answer had already
reduced the line to record-and-warn, and he chose hold.

`DERIVED`:

- **Nothing about Move 1 is built, prototyped or released.** Not in
  fleet-manager, not in the kit, not as an "experiment". The evidence base
  (dig § 11 item 3, gaps #1/#2) stays assembled and unused.
- **No adjacent mechanism may be built that is Move 1 in another shape.** The
  hold is on the function — a close-time declaration of what a session left
  behind — not on the filename.

## 8 · The end-of-session interview — **something asks, and filters** (agenda § 2 · D)

His selection: **"Something asks, and shows me only what's worth showing."**

`OWNER` (option selected). The minimum answer this row asked for was one
sentence naming the questioner, and he named it: **not him.** A mechanism runs
the end-of-session interview and filters, surfacing to him only what is worth
his ratification. The mining half already ships in the kit
(`engine/loop/reflections.py`, v1.0.0, advisory); the **asking** half and the
**filter** are what he has now specified.

**The distinction that matters, stated because a session will otherwise get it
wrong:** § 2 · C is **held** and § 2 · D is **answered**, and they are both
close-time mechanisms. That is not a contradiction and D is **not** a backdoor
GO for C:

- **C is a specific designed mechanism awaiting a GO he declined to give.**
- **D is a direction naming who does the asking** — the row's own minimum
  answer — with the routing explicitly left to us and the ratification rule
  already his.
- **Reading D as authorising C would be the exact failure this estate has
  recorded twice** — an inference recorded as an owner decision (fm #937's
  withdrawn `OQ-FM-D2-TARGET` closure; fm #949's packet decomposition). Any
  build of the interview must be able to state which of his sentences
  authorises each part of it.

`DERIVED`: the interview's design is a **hub prototype under roadmap § 6**
(observe → prototype → measure → promote), it inherits § 2 · B (it may not
block a session finishing) and § 2 · B2 (it may not prompt an unattended run),
and its filter is the load-bearing half — an unfiltered interview that shows
him everything is the thing that consumed his attention and stopped.

## 9 · The kit's charter — **rewrite it to say initiative** (agenda § 2b)

His selection: **"Rewrite it — say initiative is what it's for."**

`OWNER` (option selected). The kit's stated purpose is rewritten to name the
initiative duty. The measurement behind the question: **initiative** returns
**zero hits** across `kit:README.md`, `kit:docs/PROJECT-CLOSEOUT.md` and
`kit:docs/program/rulings.md` (grep, re-run by the agenda session), while
OD-24 § 2 gives it as the reason the kit exists.

`DERIVED`:

- **This is now the round's most direct fix for the § 2 · 0 root cause**, and
  it is a records change in the kit's own venue — no mechanism, no promotion
  question, no packet dependency. It is unblocked agent work by his direction.
- **It is not this sitting's to execute.** This session is review-and-
  discussion by his selection; the kit doc-surface work is a separate session
  (the agenda's § 5 sweep), and the charter rewrite is now that session's lead
  item rather than one row among twenty-three.
- **Scope guard:** rewriting the charter means the purpose statements naming
  what the kit is *for*. It does not license editing the PL register's rulings,
  which are program law with append-only grammar and owner provenance.

## 10 · The leftovers pile — **a standing surface he reads; NOT scheduled unattended sessions** (agenda § 2 · F)

His selection: **"A standing surface I read."**

`OWNER` (option selected). Two genuinely owner-only halves were in this row and
he answered both — one by selection, one by exclusion:

- **He commits his attention:** a standing surface pointed at him is the
  drainer. Nobody could derive that he would actually read one; he says he
  will.
- **He did NOT sanction scheduled unattended sessions to drain it.** Two of the
  four options offered that (one alone, one as the lead), and he chose the one
  that does not. This is a **negative answer worth recording as such**, because
  it spends money while he is away — the class his own standing safety line
  reserves for him — and because an agent could otherwise read "the pile should
  drain" as licence to schedule it. It is not.

`DERIVED`: the fix family for dig gap #6 (*no executor/re-raiser for parked
worklists*) is **route**, not build-procedure — the fork the dig explicitly
called the owner's. His June precedent already names the shape:
superbot:Q-0153's daily idea-spotlight re-raise surface, *"so the owner can
mull it over"*. `owner-brief` exists and is the nearest live instrument. The
surface's shape and cadence are ours; **no cadence number is fixed here**, per
his own no-fake-precision rule.

## 11 · The kit's name — **change it, and he owes the name** (agenda § 2b)

His selection: **"Change it now while it's still cheap."**

`OWNER` (option selected). `kit:README.md:9` still reads *"`substrate-kit` is a
placeholder name"* and defers the published name to him; 21 releases have
shipped under the placeholder. He has now ruled that it changes.

**Blocked on one input from him: the name.** The option he chose carried the
note that he would need to supply it. Put to him in this sitting; recorded here
so that if the sitting ends without a name, the directive does not evaporate —
which is the owner-words-loss class (gap #8) this record exists to stop.

`DERIVED`, and none of it is executed here: a rename touches the GitHub repo
name (redirects are automatic), the vendored path references adopters carry,
the generated `docs/adopters.md`, and every fleet-manager document naming the
repo. It is a build-session job with a real blast radius, it happens **after**
he supplies the name, and it should not ride the same PR as a doc sweep.

## 12 · The next release — **cut when the next fix batch lands** (agenda § 2b)

His selection: **"Cut when the next fix batch lands."**

`OWNER` (option selected). kit #587 and #588 ride `main` unreleased; they wait
and go out with the next batch rather than as their own cut. This **sequences
the round's remaining kit work**: the charter rewrite (§ 9) and the doc-surface
sweep land first, then one release carries all of it.

**Still open, and he did not answer it:** which remaining adopters take the
v1.21.0 hop. `OQ-KIT-V1-21-RELEASE`'s adopter half stays open —
`pokemon-mod-lab` (owner-held, v1.15.0), `superbot-games` (*"no adopter yet"*,
2026-08-14), `trading-strategy` (archived). The question named them; his answer
addressed timing only, and reading a timing answer as an adopter answer would
be an inference recorded as a decision. It stays queued.

## 13 · The sequencing directive — **mapping → revised plan → execution** (unprompted, mid-sitting)

He said this without being asked, while the sitting was running. Verbatim:

> *"What we are doing now, is directly related to the plan. I am currently
> running 3 parrallel ultracode session to map most of all the repos, once this
> mapping is all done we should use this information to come up with a revised
> pan. Only after that will we move to execution of the 'GO'"*

`OWNER`. This is the **most consequential thing said in the sitting**, because
it re-frames every other answer in it and it was not on the agenda at all.

**What it establishes:**

1. **There is a three-stage order, and the estate is at stage one.**
   *map most of all the repos* → *use this information to come up with a
   revised plan* → *then* execution. No GO'd work starts before the revised
   plan exists.
2. **It explains and independently confirms the Move 1 hold** (§ 7). His
   *"still planning"* is not indecision or a deferral to be re-asked next
   session — it is a **stage**, with a named exit condition (the mapping
   completing and a revised plan being written). A future session must not
   re-put Move 1 to him before that exit condition is met; doing so would be
   asking him to skip his own stage.
3. **Work is happening outside this session that this session cannot see.**
   Three parallel mapping sessions were running while this sitting ran. Their
   output is an input to the revised plan, and **this round's output is another
   one.** That makes the round's deliverable a *contribution to a plan*, not a
   work queue to start executing.
4. **This round is on-plan, by his own word** — *"directly related to the
   plan"*. The OD-24 review round is not a detour from the consolidation
   program; it is feeding the same revision.

`DERIVED`, and stated as a bound on what any next session may do:

- **Session 5 of this round is not an execution session.** Whatever it does,
  its output must be shaped as an input to the revised plan.
- **The answers he gave in this sitting stay recorded and unexecuted where they
  are mechanisms** (§ 8's interview, § 10's standing surface). Where they are
  *records* changes he directly ordered (§ 9's charter rewrite), the boundary is
  a genuine question and is put to him rather than assumed — see § 14.
- **`docs/activity/` is the surface that would show the mapping sessions' work,
  and this session did not refresh it before writing this.** Named as a limit,
  not a claim: what those three sessions have produced is unread here.

## 14 · Does the kit-side RECORDS work wait for the revised plan? — **no, it goes now** (asked because § 13 created the boundary)

His selection: **"Records work can go now."**

`OWNER` (option selected). The boundary between his three-stage order (§ 13)
and the two records changes he ordered in this same sitting is now drawn by
him rather than inferred:

- **Mechanisms wait** for the revised plan — Move 1, the interview, the
  standing surface, the held packets.
- **Document corrections do not.** The charter rewrite (§ 9) and the truth
  pass's 23-file wrong-action sweep are cleared to proceed.

`DERIVED`, and the reason this distinction is worth his time: the doc sweep's
contents are **actively costing sessions capability right now**, including the
three mapping sessions he has running. `kit:docs/CAPABILITIES.md` still carries
seat-era "walls — verified blocked" that the estate's verified direct-PAT
matrix disproves, **in the repository whose own checker exists to prevent
exactly that**; `kit:docs/fleet-repos.txt` is the **live regen input** and omits
five real adopters, so every future registry regen ships incomplete;
`control/inbox.md` carries 24 seat-era ORDERs still reading `status: new`,
including one instructing a session to *arm an hourly routine*. Every day those
stand, a session either loses capability or acts on a dead order.

**Not executed in this session, and that is a scope call rather than a
hesitation:** this sitting is review-and-discussion by his own selection, and
the sweep is a 23-file kit-venue job with its own release discipline. It is
**session 5**, named from his answer.

## 15 · The kit's name — **he will pick it later** (agenda § 2b, follow-up to § 11)

His selection: **"I'll pick the name later."**

`OWNER` (option selected). He was offered three candidates in the estate's
naming style and declined all three. The § 11 directive stands — the name
**does** change — and the blocking input is his and is deferred.

`DERIVED`: this becomes an owner-queue entry rather than an agenda row, because
it is now a single-input ask with no discussion left in it. The rename does not
happen, and no session may pick a name on his behalf: he was given the chance
to delegate it and did not.

## 16 · OD-13's provider mix — **his to work out, sequenced after the plan, and he named the method** (agenda § 2b)

His answer, verbatim:

> *"Something I still need to work out, but this is not the most important
> thing right now, as soon as we have this plan ready and eventually executed,
> we can test all agents according to their default state and when running the
> improved kit"*

`OWNER`. Three separate things, and the third was not asked for:

1. **It stays his.** *"Something I still need to work out"* — not delegated,
   not overtaken. The option offered as "it's overtaken" is refused.
2. **It is sequenced last**, behind the revised plan **and** its execution —
   further back than any option offered. OD-13's two prerequisites are
   therefore **not** parallel tracks: methods first is not merely current
   priority, it is a dependency, because the provider comparison is only
   meaningful once there is an improved kit to compare against.
3. **He specified the method, unprompted, and nobody had one:** *"test all
   agents according to their default state and when running the improved
   kit"* — a **two-arm comparison per provider**: each agent in its default
   state as the control, the same agent running the improved kit as the
   treatment. That is an A/B design, and the estate has run this exact shape
   once before: the kit's own cold-start bench, which returned **1 PASS / 8
   FAIL** on 2026-07-12 and measured the enforcement pull as a null. The
   provider-mix session, when it comes, is that bench generalized across
   providers rather than a discussion about which model to use where.

`DERIVED`: nothing is built or scheduled for this. Recorded so that the method
survives — an unrecorded method sentence is precisely the loss class this round
catalogues (gap #8), and this one arrived unasked in the middle of a different
question.

## 17 · Spend caps — **not currently relevant** (agenda § 2 · H)

His answer, verbatim:

> *"There hasn't really been much API use lately, so this is currently not
> relevant"*

`OWNER`. Read precisely: this is **a dismissal on relevance grounds, not a
ruling that there will never be a ceiling.** He did not choose "no ceiling"
from the options; he said the question does not currently apply, and gave his
reason — low recent API use.

`DERIVED`:

- **No cap is adopted and none is built.** kit `PL-005` *"Observe-first
  budgets — telemetry before caps"* (2026-07-07, his own quote and method) is
  unchanged and remains program law: caps **deferred, not adopted**.
- **The meter still never ran, and he did not order one.** The option offering
  "no ceiling, but start metering" was available and not taken. So a session
  must not build a spend meter off this answer.
- **`OQ-EAP-SPEND-WINDOW-MOOT` closes.** Its real content — the ~09-07 window
  arriving with no average to look at — is answered: the window passes without
  a decision because the premise (meaningful spend to average) does not hold.
- **The condition under which it re-opens is named by his own sentence:** API
  use going up again. `[D-0011]`'s reconciled amendment (this session) is what
  makes that re-opening honest, since the card-billed route has no ceiling.

## 18 · D2's next target — **spider-swing, the measured order ratified** (agenda § 3)

His selection: **"Ratify the measured order — spider-swing first."**

`OWNER` (option selected). **`OQ-FM-D2-TARGET` is ANSWERED** — open since
2026-08-23, once recorded as answered by inference and withdrawn the same
session (`@codex`, fm #937). It is now answered by him.

**Verified before recording, because this is exactly where the earlier failure
happened:** the
[active-repo intent audit](2026-08-23-active-repo-intent-audit.md) § 6 is the
"measured order" he ratified, and it does put `spider-swing` first — its
PROVISIONAL marker was discharged 2026-08-24 once `spider-swing` was judged and
**displaced `product-forge` at the top**. Full order:
**`spider-swing` → `product-forge` → `estate-backups` → the `websites` date
stamp** (`idea-engine` and `sim-lab` already done). The tiebreak is stated in
the audit and is worth carrying: *contradicting beats empty; among contradicting,
the one whose falsehood is not corrected on contact goes first; a running clock
breaks any remaining tie.*

`DERIVED`, and it is a bound, not an unblock:

- **Naming the target does not start the work.** OD-13 still orders methods
  ahead of product work, and § 13's sequencing (mapping → revised plan →
  execution) governs everything. What his answer removes is the *unknown*, not
  the *queue position*.
- **The audit's own caveat survives ratification:** five repos remain unrated
  (`superbot`, `superbot-next`, `websites`, `couch-legend`, `shiftlife`), and
  any one could carry a contradicting front door that displaces the order. He
  ratified the best order the evidence supports, which is what it claims to be.
- **`OQ-FM-D2-TARGET` is retired from the queue** with his words as its answer.

## 19 · The final EAP mail — **soon, and the mapping feeds it** (agenda § 3)

**Answered twice, and the second answer supersedes the first.** His selection
was **"Leave it — not now"**; minutes later, unprompted, he revised it:

> *"About the mail, that really is something to work on soon, and I think that
> all the audits I'm doing right now will provide valuable information, not only
> about the EAP itself but generally about how agents work, whih would be a
> valuable addition to the mail"*

`OWNER`. Recorded as a supersession rather than a correction of the record: the
option he clicked is what he clicked, and his later live words outrank it
([`CONSTITUTION.md`](../../CONSTITUTION.md) — the live owner beats any stored
text, and that includes a stored answer from ten minutes earlier). A session
reading only the click would park this for months.

**What the revision actually changes — three things, and the third is new
scope:**

1. **Timing:** not *"leave it"* but *"soon"*. It stops being dormant queue
   material and becomes near-term work.
2. **A dependency that did not exist before:** the mail now **waits on the
   mapping audits he is running** (§ 13), because he intends their output to go
   into it. So the mail is a *third* consumer of that mapping, alongside the
   revised plan and this round.
3. **Its content brief widens, and this is the part nobody had:** the mail was
   scoped as an EAP wrap-up. He now wants it to carry what the audits show
   *"generally about how agents work"* — findings beyond the EAP itself. That
   is a materially different document from the one assembled, and it bears
   directly on the one-page-versus-three question the agenda framed: **the
   length problem cannot be settled until the content brief is, because he has
   just added to the content.**

`DERIVED`, and deliberately minimal: no restructure is done here, nothing is
sent, and the one-page constraint is neither dropped nor enforced — settling it
now would be settling it against the old brief. The queue entry is updated to
carry the new brief and the mapping dependency so the next session meets both.

## 20 · The cost function — **stalling is tolerable; REDOING is the waste** (unprompted, extends § 4)

Said unprompted, later in the same sitting, and it completes the root-cause
answer § 4 records:

> *"The thing is, there is so much to do that a lot of work just keeps stalling,
> which is not necessarily bad, but also a reason why I think it's important
> that the workflow is working correctly, so we don't waste so much time redoing
> the same things over and over agian"*

`OWNER`. § 4 gave the *cause* (agents not taking enough initiative to leave
repos better). This gives the **cost being paid for it**, and the two together
specify what a fix has to do:

- **Stalling is explicitly not the target.** *"not necessarily bad"* — with the
  estate's volume, work sitting is expected. A mechanism justified by "this
  stops things stalling" is aimed at something he did not ask to fix.
- **Re-derivation is.** *"redoing the same things over and over"* is the waste
  the workflow exists to prevent, and it is the criterion any candidate fix
  should be judged against.

**This is measured, three times over, in this round's own output** — which is
why it lands as confirmation rather than as a new direction:

1. **The re-read's dominant pattern, stated as its own headline:** *"the round
   keeps re-deriving designs the owner already ruled on in June; the router is
   where those rulings live."* Its § 3 table maps genesis precedents onto the
   dig's gap rows, including **three cases where the genesis system already
   built the exact mechanism a gap row presents as an open design question.**
2. **The truth pass's stalled conveyor, with the cost named in its own
   disposition:** four kit idea files still read `captured/open` while their
   deliverables sit in the tree with PR receipts, and the finding says plainly
   that *"shipped work presented as open sends a groom session rebuilding
   existing deliverables."* That is his sentence, measured, in the kit.
3. **This round, on itself.** § 4 records it: dig § 6.1 had already identified
   the initiative gap as *"the central drift … and the review round's real
   charter"*, and the round then organised around the gap table anyway. The
   re-derivation tax was being paid by the audit whose job was to find it.

`DERIVED`, and it is a **test**, not a new work item:

> **For any mechanism this round proposes: does it stop something being
> re-derived? If its benefit is that work stalls less, it is aimed at the wrong
> thing.**

Applied to what is already on the table, this re-ranks cleanly and without new
scope: **routing beats building.** The dig's own distribution said the dominant
gap classes are *unenforced* and *unrouted*, and that verification twice
reclassified rows from *absent* to **shipped-but-unrouted** (the reflection
miner; the planted question-router). A shipped mechanism nobody is routed to is
re-derivation waiting to happen — which is exactly the class his sentence
names, and exactly the class this round found most of.

