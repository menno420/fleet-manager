# The owner intent elicitation — his own words, per repo and above them

> **Status:** `living-ledger` · opened 2026-08-28, owner-live · **IN PROGRESS**
>
> **What this is:** the record of the intent sitting he asked for — *"I'd like
> to spend a good while thinking and writing about these things"* — capturing
> what he is actually trying to achieve, why each repo exists, and where the
> intent already recorded has gone stale or self-contradictory. Answers are
> written down **as they arrive**, in his words, `OWNER` separated from
> `DERIVED`.
>
> **Why it exists, in his words:** *"I feel like a lot of my original intent got
> lost along the way or hasn't been properly documented."*
>
> **The deliverable he named:** for each repo and each subsection where
> applicable, a `README.md` carrying his own words (or a close variant) *"so
> that my intent for everything is stored in the places where it's usefull."*
>
> **This file is the transcript, not the destination.** The per-repo records are
> the destination; this is where the raw material lives so the per-repo writing
> can be checked against it.

> **The questions he writes against live in their own file:**
> [`../planning/2026-08-28-owner-intent-questions.md`](../planning/2026-08-28-owner-intent-questions.md)
> — open-ended prompts, no options, answerable in any order. This file holds the
> answers; that one holds the asking.

## 0 · What the estate already holds — so he is not asked twice

Retrieved before any question was put to him (the `intake` skill's RETRIEVE
step, which exists because eye-filtering measured one miss in 21 on the
2026-08-08 batch).

| surface | what it already carries | what it does NOT carry |
|---|---|---|
| [`../intent.md`](../intent.md) | **fleet-manager's** intent, `OWNER`-labelled from the 2026-08-08 interview (21 questions): what the repo is for, the three success criteria, the failure costs in his order, the growth rule, non-goals, decision heuristics, the agent roster | any **other** repo's intent — § 9 names this as still open, verbatim: *"Where the durable intent surface lives for other repos — this file is fleet-manager's"* |
| [`../owner-profile.md`](../owner-profile.md) | his **working style**: presence model (attend planning, delegate execution), asking/interrupting, question form, scope freedom, live-word-wins | anything about **what he wants built** or why |
| [`../owner-reflection-2026-07-21.md`](../owner-reflection-2026-07-21.md) | his thesis (*the wall is verification, not capability*), how he works, the "real mind" direction | per-repo purpose; anything after 2026-07-21 |
| the program's **OD table** | 26 dated directives — what he decided, each with provenance | *why* he decided it, in most rows |
| [`../ESTATE.md`](../ESTATE.md) | all 28 repos, one line each: what it is, state, aliases, entry point | **why the repo exists to him**, what he wants from it, what would make him stop |
| `../repos/<name>/README.md` | 10 Layer-2 folders — where the last session left off | his intent — these are agent-facing handoffs, written by sessions |

**The structural gap, stated precisely:** the estate records *what he decided*
and *how he works* in depth, and records *why he wants any of it* almost
nowhere. `intent.md` is the one real intent document and it covers **1 of 28
repositories**. The Layer-2 folder shape he ratified on 2026-08-08 included a
`goals.md` slot — **and it was deferred** (`intent.md` § 8: *"with
`current-state.md` and `goals.md` deferred"*). That deferred file is what this
sitting is now filling.

## 1 · Conflicts put to him — his own statements that disagree

Surfaced per his instruction: *"Things that seem to conflict with each other
should definitely be mentioned to me so I can see what the correct statement
is."* Each is two things **he** said; none is an agent inference about him.

*(answers recorded below as they arrive)*

### 1.1 · Money — **hobby; revenue is a nice side effect** (CONFLICT RESOLVED)

His selection: **"Hobby — revenue is a nice side effect."**

`OWNER`. The conflict was between superbot:Q-0263 (2026-07-11, *"we spend way
too much time on safety … this is just a hobby project"*) and the estate's
actual commercial structures — a paid Play developer account with a launch gated
on a 12-tester closed test, `venture-lab`'s 1 live $29 SKU plus 19 ready, and
`shiftlife`'s Pro tier. **The July line stands; the commercial structures are
not goals.**

`DERIVED`, and this is a real constraint rather than a mood:

- **No repo is prioritised because it might earn.** The option he chose says so
  explicitly. Any plan that ranks work by revenue potential is mis-aimed, and
  `venture-lab`'s pause (OD-11) needs no commercial justification.
- **It bounds the safety/verification budget too.** Q-0263's full line pairs the
  hobby framing with *"we spend way too much time on safety"* — the same
  sentence. Effort spent making commercial-grade guarantees is effort spent
  against his stated frame.
- **It does NOT mean the products are unserious.** He ships them, tests them
  with real people and maintains a live bot; hobby describes the *motivation*,
  not the standard.

### 1.2 · Autonomy — **full in some areas, never in others** (CONFLICT RESOLVED, and it opens a gap)

His selection: **"Full autonomy for some areas, never for others"** — area by
area, as he granted autonomy tiers through the router in June.

`OWNER`. The conflict was between superbot:Q-0015 (2026-06-08, *"not intended to
be 100% autonomous … so this project stays managable and reviewable"*) and
superbot:Q-0083 (2026-06-10, *"ultimately there will not be much else left to
do"*). **Neither is the destination.** He rejected both the
build-toward-removing-yourself reading and the reviewable-forever reading.

**`DERIVED` — and this is the gap the answer opens: the area map does not
exist.** The June mechanism he is pointing at (autonomy granted per area,
through the router) died with the router on 2026-07-15. Nothing in the estate
today records **which areas run themselves and which always come back to him**.
Post-close the estate has instead accumulated *global* rules — PL-002/PL-012's
never-wait, the ask-first list, the never-delete-a-trigger decision — which are
area-blind by construction. So:

- This answer is **not executable as stated** until the areas are named. It is
  the highest-value follow-up in this sitting and is put to him next.
- It also reframes § 2 · B2 of the OD-24 sitting (*presence decides* whether a
  brake may prompt): presence is one axis, **area** is the other, and he has now
  named the second.

### 1.3 · Who the intent records are for — **agent-first, rendered to him by the website** (CONFLICT RESOLVED: not stale)

His selection: **"Agent-first — I'll read them through the website."**

`OWNER`. [`../intent.md`](../intent.md) § 1's rule — *"the primary reader is the
next agent session, not the owner"* — **stands and is not stale.** The apparent
conflict with OD-21 (the website review surface, *"easy for me to see and review"*)
dissolves: **one source, rendered differently.** The website is the human view of
the same material, not a second document written for him.

`DERIVED`, and it constrains the deliverable he asked for in the same message:

- The per-repo intent records are **written for the next agent session**, even
  though they carry his words. His words are the *source*, not the audience.
- **This is a genuine constraint on how they get written** — precise, checkable,
  citable, provenance-labelled — rather than warm prose aimed at him.
- **It makes the website a dependency of this work, not a parallel project.**
  OD-21's comment lane is how he reads and corrects these records; without it he
  has no view of what was written in his name. Worth stating because the two
  were being planned as separate threads.

### 1.4 · The record shape — **a default template, plus room to keep talking**

His answer, verbatim:

> *"All of those probably, there should be a default template but also room for
> extra free explanation"*

`OWNER`. He was offered four slots, six slots, or free-form prose, and took
**the six plus free-form** rather than choosing between structure and voice.

`DERIVED`, the template this implies — six fixed slots so records are comparable
across 28 repos, then an open section so nothing gets truncated to fit:

| slot | the question he answers |
|---|---|
| **Why it exists** | what made him start it, in his words |
| **What done looks like** | the end condition, or *"never done"* said deliberately |
| **What it must never become** | the guardrail — the non-goal specific to this repo |
| **What would make me stop** | the kill criterion, which the estate records **nowhere** today |
| **Who it's for** | him, an audience, or nobody yet |
| **How much it matters right now** | the priority signal that lets a session tell a beloved project from a tolerated one |
| **— anything else** | free, unbounded, his voice, no schema |

**The `how much it matters right now` slot is the one that must carry a date**,
because it is the slot guaranteed to go stale — which is the whole reason this
sitting exists.

### 1.5 · Repo count — **deferred, not closed** (CONFLICT RESOLVED, and sessions have been over-reading it)

His answer, verbatim:

> *"This is still something to reconsider later, but I think this shouldn't be a
> concern now"*

`OWNER`. The conflict was between OD-18's keep-14/archive-12 disposition
(2026-08-22, 9 executed the next day) and OD-20's *"every repo genuinly adds
something valuable right now"* (2026-08-23).

**The correction matters, because the estate hardened his answer past what he
said.** OD-20 has been read — including in this repo's own program row — as
*"no further repo cuts, the reduction lever is spent."* He has now said it is
**reconsiderable later** and merely **not a concern now**. Those are different:
a spent lever is closed, a parked question is not.

`DERIVED`:

- **Nothing changes in the near term** — no cuts, no re-litigating dispositions,
  and legibility remains the work. His *"shouldn't be a concern now"* is
  unambiguous.
- **But OD-20 should stop being cited as a permanent closure.** A future session
  proposing a reasoned archive list is not contradicting him.
- **It is a "later" with no trigger**, which is exactly the shape that goes
  stale silently. Worth re-asking when the mapping and revised plan land, since
  that is when the estate's shape is next under review anyway.

### 1.6 · The kit vs the non-goal — **worth it now, but it MUST END** (CONFLICT RESOLVED, and it hands the round an exit condition)

His selection: **"Right now it's worth it, but it must end."**

`OWNER`. The conflict was between [`../intent.md`](../intent.md) § 5's non-goal —
*"an apparatus that needs maintenance sessions of its own"* — and the
substrate-kit round consuming four sessions this week plus a 34-row worklist.

**He did not exempt the kit. He confirmed the non-goal and time-boxed the
exception.** The option he chose reads: this round is a one-off correction
because he stepped back too far; afterwards the kit should go quiet again —
*and if it does not, that is the signal it is too big.*

`DERIVED`, and this is the most operationally useful answer in the sitting so
far:

- **The OD-24 round now has an exit condition it did not have.** It was open-
  ended ("review it again and improve it"). It ends when the kit stops needing
  sessions — and the 34-row worklist is not a mandate to work all 34.
- **It supplies a live test with a real failure branch.** If kit work keeps
  recurring after this round, the correct response is **to make the kit smaller**,
  not to schedule more maintenance. That is a conclusion no session would have
  reached on its own; every prior instinct in the record was to fix more rows.
- **It bounds session 5 and anything after it.** Records work he cleared, the
  charter rewrite, the release — then quiet. A fifth, sixth, seventh kit session
  is evidence against the kit, not progress.

### 1.7 · shiftlife — **paused, and he intends to come back** (CONFLICT RESOLVED)

His selection: **"Paused — I intend to come back to it."**

`OWNER`. OD-15's *"shiftlife is not active"* (2026-08-10) never said which kind
of inactive it was, and the estate has been treating it as functionally
abandoned — its four open owner asks have sat since July.

`DERIVED`:

- **It is a live intention, not a dead repo.** Its open asks stay in the queue
  and are legitimate; nobody should propose archiving it.
- **It has no Layer-2 folder** (`on demand` in `ESTATE.md`) — which is now wrong
  for a repo he intends to return to, since returning is exactly when a cold
  session needs the handoff most.
- **It is the estate's only private *product* repo** and the only one serving an
  identified outside audience (shift-working households, binnenvaart first) —
  which bears on the who-is-this-for question still open in § 2.

### 1.8 · Autonomy — **he rejects the axis itself** (and this is the batch's headline)

His answer, verbatim, to a proposed inside-the-estate / outside-the-estate
autonomy boundary:

> *"Not entirely sure, it really depends on the kind of task and personally I
> don't see a lot of difference between autonomous and directed apart from where
> the initiative comes from. The results will not automatically be better
> because I started the task. Tho right now there isn't really much autonomous
> work anyways since the EAP is done and most of the work right now really needs
> some type of input from me"*

`OWNER`. He was offered three shapes of an autonomy boundary and took none of
them. **He is not choosing between autonomy tiers — he is saying the tier
framing is not the interesting one.**

**Why this matters more than the question it answers.** The estate is built on
autonomy-as-permission: PL-002 and PL-012's never-wait, the decide-and-flag
ladder, the ask-first list, autonomy rails in the CONSTITUTION, fm's never-delete-a-trigger decision's
prohibition. All of it models the question *"how much may an agent do without
him?"* His answer says the only real difference between autonomous and directed
work is **where the initiative came from**, and that **his starting a task does
not make the result better**.

`DERIVED`, and stated as a correction to how this estate has been reasoning:

- **The estate has been solving a permissions problem while he describes an
  initiative problem.** This is the same thing he said as the OD-24 root cause —
  *agents don't take enough initiative to leave the repos in a better shape* —
  arriving from a different direction. Two independent answers, one subject.
  **Initiative, not permission, is the axis he cares about.**
- **It does not repeal any ratified brake.** The confirm-before-send/delete
  line, the trigger prohibition and the production rails are unaffected; he
  declined to *rank areas*, not to keep the safety lines. Nothing here
  authorises anything new.
- **The area map is therefore NOT the follow-up work** § 1.2 assumed it was.
  That entry called the area map "the highest-value follow-up in this sitting";
  his answer supersedes it. Recorded rather than edited away, because the
  wrong turn is the evidence: a session (this one) reached for a permissions
  artefact within minutes of him naming an initiative problem.
- **The question is near-moot in practice right now, by his own account** —
  *"there isn't really much autonomous work anyways since the EAP is done and
  most of the work right now really needs some type of input from me"*. So any
  effort spent designing autonomy tiers today is effort against a condition that
  does not currently exist.

### 1.9 · creator-kit, and a new thing he wants: **a repo-creation skill**

His answer, verbatim:

> *"A bit of the first 2 answers combined, this is not really a repo that will be
> doing much work, tho that could change. And when this was made there weren't
> really proper agreements made woth the local session. Which is also why I think
> it's important to make a repo creation skill, so all repos get created in the
> same way"*

`OWNER`. Three things, and the third was not asked for:

1. **The 2026-08-23 local-session rule was not yet real when creator-kit was
   made** — *"there weren't really proper agreements made woth the local
   session"*. So this is not a broken rule; it is a rule that had not landed on
   that venue yet. The OD-23 discipline is two days older than the repo, but
   arriving at a venue is not the same as being written down — the estate's own
   injection thesis, again.
2. **creator-kit is low-activity by intention** — *"not really a repo that will
   be doing much work, tho that could change"*. It is not neglected; it is
   quiet. Its unrendered `current-state.md` is still a defect, but a small one.
3. **He wants a repo-creation skill** — *"so all repos get created in the same
   way"*. **New, owner-originated, and not on any list.** Queued rather than
   built: it is a mechanism, and his mapping → revised plan → execution
   sequencing governs.

`DERIVED`: the skill's value is precisely that it makes the local venue and the
cloud venue produce identical repos — which is the OD-23 handoff goal expressed
as a tool rather than as a rule. It is also, notably, an **initiative-side** fix
rather than a permission-side one, which is consistent with § 1.8.

### 1.10 · How the interview runs — **draft first, ask where unsure, he writes**

His answer, verbatim:

> *"Draft it first, but also provide questions when certain things aren't sure.
> I want some time to write this out personally but some guiding questions would
> help"*

`OWNER`. And the first repo, by his selection: **`substrate-kit`** — *"while the
round is still fresh"*.

`DERIVED`, the working method for every remaining repo:

1. A session **drafts** the intent record from the committed evidence, marking
   every slot it inferred rather than sourced.
2. It attaches **guiding questions** exactly where the draft is guessing — not a
   generic questionnaire, only the genuinely uncertain slots.
3. **He rewrites it in his own words.** The draft exists to give him something to
   react to, which his own profile names as the form that works
   ([`../owner-profile.md`](../owner-profile.md): *"by stating back your perceived
   intent I will see if you understood and will correct you if you are wrong"*).
4. The final record carries **his** words, with the draft's inferences either
   confirmed, corrected, or removed.

### 1.11 · Where the records live — **fleet-manager global, repos full** (the deliverable's scope, settled)

His answer, verbatim:

> *"Fleet manager for the global intent, like the main goal and expectations,
> and the own repos for the whole report"*

`OWNER`. A split, not a location. **fleet-manager carries the global intent —
the main goal and his expectations per repo; each repo carries the full
record.**

`DERIVED`, and it resolves the tension cleanly rather than overriding either
side:

- It **matches [`../intent.md`](../intent.md) § 1's existing division** almost
  word for word (*fleet-manager carries what the repo is for*; the repo carries
  how to work inside it). The intent layer inherits the same split the
  orientation layer already uses — no new architecture.
- It **preserves the non-goal** (*"a second source of truth for anything a repo
  owns"*): the full record lives once, in the repo; fleet-manager holds a
  summary that points at it.
- **Scope, therefore:** ~28 short global entries here (main goal + expectations),
  and one full record per repo **in that repo**, at whatever depth the repo
  warrants. Per-subsection records stay a per-repo judgment rather than a
  blanket obligation.
- **Consequence for this session's draft:** `docs/repos/substrate-kit/intent.md`
  is a **staging draft**. Once he rewrites it, the full record belongs in the
  kit repo and fleet-manager keeps the summary.

### 1.12 · The kit's endgame — **quiet, but it may still grow when something proves out**

His selection: **"Quiet, but it can still grow when something proves out."**

`OWNER`. This **narrows § 1.6** rather than restating it: *"it must end"* means
**maintenance** ends, not development. New capability is still permitted — but
only through the promotion rule, after it measures useful in a real repo first.

`DERIVED`: so the failure signal is specifically **recurring upkeep**, not
growth. A kit that gains a checker because a repo demonstrated the need is
healthy; a kit that needs a fourth session to fix its own docs is not. He also
declined *"shrink from here"* — removal is not ordered.

### 1.13 · The kit's audience — **for others, and he was right that it says so** (verified, with two exceptions)

His answer, verbatim:

> *"The kit is definitely meant to be used by others and I'm pretty sure that
> that is already explained there. At least by the MIT license"*

`OWNER` on the intent (**for others** — settled), and a **hedged** claim about
the tree (*"pretty sure"*). Verified rather than accepted, per his own
calibration profile — verify the hedged, act on the unhedged. `MEASURED`
2026-08-28 against `menno420/substrate-kit` at `main`:

**Substantially correct.** `LICENSE` exists (GitHub reports `spdx_id: MIT`);
`README.md` carries an *"Install / adopt (one step)"* section with a
copy-one-file recipe, **three integration modes that explicitly "pace
adoption"**, and a pip-installable form. The voice is repo-agnostic —
*"everything a fresh repository needs"* — not estate-specific. An outsider
could adopt it.

**Two observations — and he corrected the first one the moment he read it:**

1. ~~The purpose sentence carries the autonomy half only.~~ **OWNER-CORRECTED,
   2026-08-28, minutes after this was written:** *"whats written there is also
   correct, the initiative part falls into place perfectly with the existing
   sentence of 'little steering'"*. The session had read `README.md:3-5` —
   *"everything a fresh repository needs for AI agents to work correctly with
   little steering"* — as carrying only steering-reduction and **missing**
   initiative. **He says the two are the same idea**: an agent that needs little
   steering is one taking initiative. So the charter rewrite is an
   **expansion that makes an implication explicit**, not a correction of
   something wrong.
   **Why the error is worth keeping:** the round's zero-hit grep for the word
   *initiative* was accurate and its conclusion was not. A word-presence test
   measured vocabulary and got read as measuring meaning — and it survived three
   audit sessions and a completeness critic before he read one sentence and
   dissolved it. `MEASURED` results do not stop being inferences when they are
   about what a document *means*.
2. **The repo's own description undersells it to exactly the audience he wants:**
   *"AI self improvement system in progress"*, **no topics, no homepage**. For a
   thing meant to be used by others that is the first surface a stranger meets.

`DERIVED`: the audience answer changes the charter rewrite's brief — it must read
as if a stranger might pick it up, which is a different sentence from one aimed
at his own agents. The description and topics are a two-minute fix in the same
session.

### 1.14 · The kit is a **real product that keeps existing** — the retirement question answered

His answer, verbatim, to the draft's guiding question *"is there a version of
this where you'd retire the kit entirely?"*:

> *"The kit is meant to be a real product that keeps existing, the main goal is
> to ensure it's working correctly in such a way that it does not need more
> corrections, but only occasionally an addition or improvement when we come
> across a new problem"*

`OWNER`. Three things, and together they close the kit's two hardest slots:

1. **It is permanent.** *"A real product that keeps existing"* — retirement is
   not on the table, and no session should propose going back to per-repo
   conventions. This also confirms § 1.13's audience answer from a second
   direction: a *product* implies users.
2. **"Done" is precisely defined, and it is about corrections:** working
   correctly *"in such a way that it does not need more corrections"*. Not
   feature-complete, not version-numbered — **correction-free**.
3. **Growth is problem-driven, not roadmap-driven:** *"only occasionally an
   addition or improvement when we come across a new problem"*.

`DERIVED`, and it sharpens § 1.12 rather than repeating it:

- **The 34-row worklist is not a plan.** Rows exist because problems were
  found, and they get fixed to reach correction-free — but the worklist is not
  a backlog to burn down for its own sake, and finishing it is not the goal.
- **"Correction" and "addition" are now separable, and the distinction is
  load-bearing.** A correction means the kit was wrong — those should trend to
  zero. An addition means the *world* presented something new — those are
  expected to keep arriving forever. A session proposing kit work should say
  which one it is; recurring **corrections** are the failure signal, recurring
  **additions** are healthy.
- **His "what would make me stop" answer for this repo is: nothing.** The slot
  is not empty for want of asking — it is genuinely not applicable here, which
  is a different and more useful record than a blank.

### 1.15 · The bots — **three converge into one, built without architectural debt**

His answer, verbatim, and it is the clearest product-intent statement in the
sitting:

> *"Superbot itself is a repo that's filled with too much history, too many
> trials and errors. What I want from spiderbot and superbot-next (this one will
> have to be remade aswell since the current build is nothing like the desired
> product) is that they eventually are rebuild as one real well functioning bot
> thats build right from the start, which is already documented but apparently
> not well enough.*
>
> *The goal is to create a bot without architectural debt for as far as that's
> possible. Everything should be planned and connected from the start so it
> remains manageable and able to grow indefinitely."*

`OWNER`. **The end state is ONE bot.** Not a successor plus a donor plus a
frozen oracle — one, rebuilt from the start, and the design criterion is named:
**no architectural debt**, everything *"planned and connected from the start"*,
**able to grow indefinitely**.

**His "already documented" claim — he is right, and the first pass of this entry
under-searched and got two of its three claims WRONG. Corrected below.**

`MEASURED` 2026-08-28, second pass, after an owner-review challenge asked what
the "nowhere" claim rested on. **The first pass ran one grep over one directory
with a fixed pattern list and never opened
`docs/repos/superbot-next/README.md` at all** — then asserted three things were
absent from the records. A broad re-search over the whole `docs/` tree:

1. ~~That `superbot-next` must be REMADE is unrecorded.~~ **WRONG — the
   substance is recorded and measured.** `docs/repos/superbot-next/README.md:29`
   carries it as the file's governing caveat: *"**The one caveat that governs
   everything here:** golden-parity green must not be read as 'ported'"* — with
   the 2026-08-05 owner-live audit's evidence: **capture-world literals**
   shipping as constants, and **60 of 66 help panels button-less**. A fresh-agent
   test file separately records *"the disband-or-rebuild decision that remains
   the owner's"*. **What is genuinely new is not the evidence — it is his
   verdict.** The record measured the gap and explicitly left the call to him;
   he has now made it: remade.
2. ~~That the end state is ONE bot is unrecorded.~~ **WRONG, and this one is
   nearly verbatim.**
   [`../planning/2026-08-21-game-community-bot/README.md`](../planning/2026-08-21-game-community-bot/README.md)`:40-43`:
   *"The bots remain separated — standing constraint. The eventual consolidation
   he describes is of the two `superbot` **repositories** into one new
   repository. It is **not** a merge of running bots."* His sentence names
   `spider-bot` where the plan names "one new repository" — and `spider-bot`
   **is** that repository. Same intent, already written down.
3. **"Able to grow indefinitely" — this one stands.** A whole-tree grep for
   `grow indefinitely` / `grow forever` / `unbounded growth` returns only
   unrelated uses and this session's own files. The growth-forever requirement
   is his and appears in no ESTABLISHED list.

**And the re-search found something the first pass missed entirely:** the GCB
plan flags its own unresolved contradiction immediately after the passage above
— *"The executable roadmap now contradicts this, and that is not resolved
here."* That is a live inconsistency inside the plan that governs this work,
and it is now the sharpest thing in this entry.

**Why this correction is kept rather than edited away.** It is the **second time
in one day** that a session asserted an absence from an under-scoped search and
was refuted — the first was the OD-24 round's *initiative* grep, which he
himself refuted on sight. Both had the same shape: **a narrow search treated as
a whole-population claim.** A grep proves what a pattern found in the paths it
was given; it never proves absence from a corpus it did not search.

`DERIVED`:

- **This is the first repo-level intent in the sitting that names a design
  criterion rather than a purpose** — *no architectural debt, grows
  indefinitely* — which makes it checkable in a way "what it's for" is not.
- **It re-frames what `spider-bot` currently is:** not the finished successor,
  but **one of two inputs to a bot that does not exist yet.** Its own record
  says its next feature is his pick; this says the *shape* is the point, not the
  features.
- **It creates a real question about sequencing** that nothing answers: the
  convergence rebuild is a third act after two live/parked codebases, and
  `spider-bot` is running in production with real users while it waits.
- **It supports his own "hobby" framing** in an unexpected way: *"managable and
  able to grow indefinitely"* is a maintainability goal, not a delivery goal.

## 2 · The core statement — why this era exists, in his words

Given unprompted, 2026-08-28, in answer to *"what do you wish you could hand
over completely but currently can't trust?"* — the question this sitting flagged
as the highest-value one it could ask. **It is the most consequential statement
in the sitting and probably in the estate's record.**

> *"What I wish to be able to fully hand over is basically everything.*
>
> *What I don't trust right now is that things are build according to what I
> have in mind. And this comes mostly from how superbot-next turned out to be.
> The task was to recreate superbot as it is right now but then in an improved
> way. But what was build was nothing like how the original superbot functions.
> That is the main reason why I started this extensive
> pause/research/planning/improvement period where basically no "real" execution
> work gets done with a few exceptions. The idea behind this is that I feel like
> the autonomous period has removed or mangled much of my intent and the desired
> workflow. Which is why right now all my time and effort goes towards improving
> the system so that the future implementations go smoothly without the need for
> multiple corrections each time, the goal is to find out the things that have
> gone wrong and to create a mechanism that prevents those errors in a way that
> basically forces certain things to be done in certain ways"*

`OWNER`. Five things, and each one settles something the estate had been
guessing at.

**1 · The ceiling is total.** *"Basically everything."* Not a list of areas, not
a tier. This closes the autonomy question a third time and from the opposite
direction to § 1.8: he does not want to keep work back. **What limits delegation
is not permission, not capability, and not risk appetite — it is whether the
result matches what he had in mind.**

**2 · The distrust has one named cause, and it is a specific event.**
`superbot-next`. *"The task was to recreate superbot as it is right now but then
in an improved way. But what was build was nothing like how the original
superbot functions."* The estate records `superbot-next` as an engineering
artefact — 533/533 golden parity, an architecture donor, capture-world literals,
60/66 help panels button-less. **It has never recorded what that repo actually
did to his willingness to delegate**, which is the more important fact about it.
It is not a parked asset; it is the reason for the current era.

**3 · This era has a stated purpose, and the estate never wrote it down.**
*"That is the main reason why I started this extensive
pause/research/planning/improvement period where basically no 'real' execution
work gets done with a few exceptions."* Every record describes the current
period in terms of its *contents* — the consolidation program, the roadmap, the
OD-24 round, the mapping sessions. **None states that the pause is deliberate,
that it is a response to `superbot-next`, or that no-real-execution is the
intended condition rather than a symptom of stalling.** A session reading the
estate today would try to restart execution, believing it was helping.

**4 · The diagnosis is his, and it is the injection thesis in his own words.**
*"I feel like the autonomous period has removed or mangled much of my intent and
the desired workflow."* Note **removed or mangled** — not "the agents were
incapable". The estate reached the same conclusion from measurement (the
practice held where gated, the loop died where prose-only); he reached it from
watching his intent come back wrong.

**5 · The acceptance criterion, and it is measurable.** *"future implementations
go smoothly without the need for multiple corrections each time"* — and the
method: *"find out the things that have gone wrong and create a mechanism that
prevents those errors in a way that basically forces certain things to be done
in certain ways."* **Same shape as his kit answer** (§ 1.14): done means
**correction-free**. Two independent answers, one criterion.

### 2.1 · The apparent contradiction with OD-24 § 3, and why it is not one

`DERIVED`, and it needs stating because a session will otherwise read these two
as opposites:

- **OD-24 § 3:** agents *"really like to add restrictions and walls and guards,
  while I personally would rather make sure that my agents have as much freedom
  as I have myself."*
- **Here:** *"create a mechanism that … basically forces certain things to be
  done in certain ways."*

**These are different objects.** § 3 objects to walls that restrict **what an
agent may do** — permission walls, confirmation prompts, capability limits.
This asks for mechanisms that constrain **how the work is done** — method
enforcement. He wants maximum freedom of action and minimum freedom of method.

**The estate has been conflating them**, and the conflation is expensive in both
directions: it makes a session hesitate to build a real method gate (reading
§ 3 as anti-mechanism), while permission-shaped brakes accumulate because they
feel like safety. The test that separates them: *does this stop an agent doing
something, or does it stop an agent doing it the wrong way?* **The first needs
his ratification. The second is what he is asking for.**

`DERIVED`, on what follows for the round's own output:

- **His Move 1 hold and this statement are consistent, not in tension.** He is
  not withholding mechanisms — he is refusing to build them before the mapping
  says which errors are real. *"Find out the things that have gone wrong"*
  precedes *"create a mechanism"* in his own sentence.
- **It re-ranks the OD-24 round's deliverable.** The round catalogued twelve
  gaps and the sitting reduced them to one root cause; this names what the fix
  must **be** — forcing mechanisms, derived from actual observed errors, not
  from a design.
- **It gives the revised plan its acceptance test**: implementations that need
  **one** correction rather than many. That is countable against future PRs
  without inventing a metric.

## 3 · The benchmark — the one-word test, and it is a real measured event

His statement, 2026-08-28, given as *"an example of what has been possible
before and what I mean by trusting an agent to work on it's own"*:

> *"Back when superbot still was the only repo, we created a very good system,
> tho nothing was yet turned into skills or hooks, we had a lot of CI checks
> that enforced thing to be made according to a set standard.*
>
> *Everything was so well documented that I have been able to create full
> working cogs with just 1 or 2 words of input, the 2 examples that have
> actually been build this way: chicken farm, and karma. I literally started a
> fresh session, wrote only "chicken farm" and the session created exactly what
> I had in mind, basically perfectly in one try from start to finish … The
> second test, I just wrote "karma" and again it build exactly what I had in
> mind without any further questions at all.*
>
> *This is the level I wish to achieve in all my repos, tho I understand that
> such a small prompt without any further context would not always work in every
> kind of repo, but it should be reasonably possible in any repo where one word
> could turn into a feature that matches what currently exists"*

`OWNER`. **This is the estate's success criterion, and unlike every other
statement of "working" in the record, it is a test that can actually be run.**

### 3.1 · Both examples verified — they exist, and the record corroborates him

`MEASURED` 2026-08-28 against the frozen `menno420/superbot` via the GitHub API.
He did not name PR numbers; these were found by search and match his account.

| | chicken farm | karma |
|---|---|---|
| PR | **#1328** *"feat(farm): NEW idle egg/chicken farm game (lazy-accrual idle loop)"* | **#1332** *"Implement Karma (thanks/upvote reputation) subsystem"* (plan PR **#1330** the same evening) |
| opened → merged | 20:45:53Z → 21:26:22Z — **41 minutes** | 21:54:01Z → 22:50:59Z — **57 minutes** |
| size | +1,668 / −148, **29 files**, 4 commits | +2,131 / −153, **37 files**, 9 commits |

**Both on 2026-06-22, within about two hours of each other.** That date places
them at the exact peak the genesis dig measured: the enforcement stack had
landed over the preceding twelve days (one-idea 06-10 · ⟲ review 06-12 ·
enders 06-12 · auto-merge 06-13 · **born-red gate 06-14**), and superbot:Q-0194
— friction becomes a guard, *"catching these should not depend on the owner
spotting them"* — is dated **the same day**. His causal account and the dig's
independent measurement agree without either having been derived from the other.

### 3.2 · The three things the PR bodies show, and the third is the answer

1. **The one-phrase input is recorded verbatim in the artefact.** #1328's body
   opens: *"Owner-directed task: **\"Idle egg/chicken farm\"**"*. The prompt he
   remembers giving is preserved in the PR itself.
2. **"Without any further questions" was decide-and-flag, not luck.** #1332's
   body reads *"Defaults used (the 5 design Qs weren't …"* — there **were** five
   design questions. The session did not ask him; it chose documented defaults
   and said so. That is the estate's decide-and-flag doctrine producing exactly
   the experience he describes.
3. **The session applied an owner preference it was never given — and this is
   the mechanism.** #1328 records: *"a **modest** faucet; the owner's 'rewards
   too large/frequent' caution is respected"*. Nobody put that in the prompt;
   the prompt was two words. The session **retrieved a previously recorded owner
   preference and applied it unprompted.** It also reused the existing
   `settle()` lazy-accrual pattern and cited ADR-001/002 by name rather than
   inventing a mechanism.

**That third row is what "one word" actually costs.** It is not model
capability and it is not permission — it is that everything needed to build the
thing correctly was *already written down and reachable*, so two words plus the
repository equalled a specification. His own caveat says the same in his words:
it should work *"in any repo where one word could turn into a feature that
matches what currently exists."* **The one-word test is a test of the
repository, not of the agent.**

### 3.3 · The uncomfortable part, stated plainly

`DERIVED`, and it should be checked rather than believed:

**He says the system that produced this had no skills and no hooks — it had CI
checks enforcing a standard, plus documentation.** *"nothing was yet turned into
skills or hooks, we had a lot of CI checks that enforced thing to be made
according to a set standard."* The estate's current effort is largely **skills
and hooks**, and the substrate-kit exists to carry them.

This is **not** evidence that skills and hooks are wrong — they did not exist
then, so nothing was measured against them, and the kit's own bench separately
found that *steering survives shipping while enforcement pull does not ship in
prose*. But it does mean the estate has **one demonstrated recipe for the result
he wants**, and it is: **enforced standards in CI + documentation complete
enough to substitute for a specification.** Any plan that reaches for a
different mechanism should say why it is not just rebuilding that.

### 3.4 · What this gives the plan that it did not have

- **A named acceptance test.** *Can a fresh session, given one or two words in
  this repo, produce a working feature that matches what already exists?* It is
  runnable per repo, it needs no new metric, and it fails informatively.
- **A benchmark with a reproducible target.** #1328 and #1332 are open in a
  frozen repository. A session can read what the repo looked like on
  2026-06-22 — the docs, the ADRs, the CI checks — and ask what is missing in
  a repo where the test would fail today.
- **It sharpens his own acceptance criterion from § 2.** *"Without multiple
  corrections each time"* and *"one word becomes a working feature"* are the
  same standard measured at two points: one on the work, one on the input.

