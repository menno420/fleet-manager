# Every worksheet, in one file

> **Working copy — generated, and two-way.** The individual worksheets under
> `owner/intent-workbooks/` are canonical. This file exists so the collection
> can be read and answered in one place, on a phone or tablet, with no tooling.
>
> **Answer anywhere in it.** Use `OWNER:` on its own line, or an inline
> `(OWNER <date>: …)` — the same convention as the separate files
> (`HOW-TO-ANSWER.md`). Nothing else is parsed.
>
> **When you are back**, one command puts every answer into its own worksheet:
>
> ```
> python3 tools/gen_workbook_bundle.py --split
> ```
>
> It is all-or-nothing: if anything about the file's structure does not
> reconcile, it writes nothing and says what is wrong. Do not delete the
> `<!-- ===== BEGIN … -->` / `<!-- ===== END … -->` comment lines — they are
> how your writing finds its way home. Everything between them is yours to
> change.

---

## Contents

- `agents/how-agents-should-ask-you.md`
- `agents/how-agents-should-report-back.md`
- `agents/mistakes-that-must-not-repeat.md`
- `agents/what-agents-may-do-without-asking.md`
- `agents/what-done-means.md`
- `agents/when-an-agent-disagrees-with-you.md`
- `agents/when-an-agent-should-stop.md`
- `agents/which-agent-for-which-work.md`
- `agents/working-across-devices-and-surfaces.md`
- `estate/how-agents-should-work-with-you.md`
- `estate/how-priorities-should-work.md`
- `estate/how-repositories-begin-change-and-end.md`
- `estate/minimum-baseline-for-a-new-repository.md`
- `estate/risk-and-owner-authority.md`
- `estate/what-success-looks-like.md`
- `estate/where-truth-should-live.md`
- `estate/why-this-estate-exists.md`
- `folders/archive.md`
- `folders/decisions.md`
- `folders/evidence.md`
- `folders/ideas.md`
- `folders/owner.md`
- `folders/plans.md`
- `folders/practices.md`
- `folders/repositories.md`
- `folders/sessions.md`
- `folders/state.md`
- `folders/tools.md`
- `products/slingy-spider.md`
- `products/what-money-means-here.md`
- `products/what-you-would-build-with-more-agents.md`
- `products/who-you-are-building-for.md`
- `repositories/Substrate-kit-app.md`
- `repositories/codetool-lab-fable5.md`
- `repositories/codetool-lab-opus4.8.md`
- `repositories/codetool-lab-sonnet5.md`
- `repositories/couch-legend.md`
- `repositories/creator-kit.md`
- `repositories/curious-research.md`
- `repositories/estate-backups.md`
- `repositories/fleet-manager.md`
- `repositories/gba-homebrew.md`
- `repositories/idea-engine.md`
- `repositories/pokemon-mod-lab.md`
- `repositories/product-forge.md`
- `repositories/proxybench.md`
- `repositories/shiftlife.md`
- `repositories/sim-lab.md`
- `repositories/spider-bot.md`
- `repositories/spider-swing.md`
- `repositories/substrate-kit.md`
- `repositories/superbot-games.md`
- `repositories/superbot-idle.md`
- `repositories/superbot-mineverse.md`
- `repositories/superbot-next.md`
- `repositories/superbot-plugin-hello.md`
- `repositories/superbot.md`
- `repositories/trading-strategy.md`
- `repositories/venture-lab.md`
- `repositories/websites.md`
- `successor/how-the-new-hub-should-feel.md`
- `successor/naming-and-file-size.md`
- `successor/the-door-test.md`
- `successor/what-carries-over.md`
- `successor/what-happens-to-fleet-manager.md`
- `successor/what-the-new-hub-is-called.md`
- `successor/why-agents-misread-this-repo.md`
- `you/how-you-decide.md`
- `you/how-you-want-to-be-talked-to.md`
- `you/how-you-work.md`
- `you/time-money-and-limits.md`
- `you/what-frustrates-you.md`
- `you/what-you-want-to-learn.md`
- `you/your-vocabulary.md`

---

<!-- ===== BEGIN agents/how-agents-should-ask-you.md ===== -->
# How I think agents should ask you things

## My current understanding

`VERIFIED`: `docs/intent.md` records your default question form — an agent
**states its interpretation back** and you correct it. *"Most of the time by
stating back your perceived intent I will see if you understood and will
correct you if you are wrong."* Structured A/B options are for genuine forks,
not a routine habit.

`VERIFIED`: there is no target number of questions — enough to resolve the
ambiguity that remains, no minimum and no maximum.

`DERIVED`: the questions that cost you are not the hard ones. They are the ones
whose answer is already in the repository, and the ones asked one at a time
across an evening instead of batched.

## What I suggest

`PROPOSED`: an agent should ask the moment a fork appears and keep working; it
should batch everything non-blocking to your check-in rhythm; and it should
never ask a question it has not first tried to answer from the records.

## Questions for you

1. What makes a question feel worth answering versus a waste of your time?
2. Do you prefer questions in the chat, in a file you can read later, or both?
3. How do you want a batch of questions formatted when there are five of them?
4. Should an agent ever ask you the same question twice — for example if the
   context changed?
5. When you answer briefly, is that "that is all I have" or "stop asking"?
6. Is there a question you wish agents would ask you more often?

## Your words

`OWNER`:
<!-- ===== END agents/how-agents-should-ask-you.md ===== -->

---

<!-- ===== BEGIN agents/how-agents-should-report-back.md ===== -->
# How I think agents should tell you what they did

## My current understanding

`VERIFIED`: every session here writes a session card, and there is a generated
index (`owner/README.md`) sweeping everything waiting on you into one page.
There is also an `owner-brief` skill for status-shaped questions.

`DERIVED`: the card is written for the next agent, not for you. That is
correct, and it means you currently have no artifact written for *you* that
says what happened while you were away.

`DERIVED`: what you want after an absence is probably three things — what
landed, what needs you, what is next — and not a log.

## What I suggest

`PROPOSED`: a short standing report shape, always the same three headings, no
technical vocabulary, decisions rendered as one-letter choices. If you confirm
it, it becomes a generated file rather than something an agent composes.

## Questions for you

1. After a week away, what would you want to open first?
2. Do you want a running record of everything, a summary, or only exceptions?
3. Should agents tell you about work that failed and was abandoned?
4. How much do you care about *how* something was done versus *that* it was?
5. Would a weekly written summary be useful, or would it go unread?
6. Is there a report you currently ignore? Which one, and why?

## Your words

`OWNER`:
<!-- ===== END agents/how-agents-should-report-back.md ===== -->

---

<!-- ===== BEGIN agents/mistakes-that-must-not-repeat.md ===== -->
# The mistakes you never want to see again

> **Companion to [`../you/what-frustrates-you.md`](../you/what-frustrates-you.md).**
> That page asks what annoys you. This one asks the narrower, more actionable
> question: which specific mistakes should the estate make **structurally
> impossible**, and what should happen when one is about to occur.

## My current understanding

`VERIFIED`: `docs/traps.md` is the register of recurring execution mistakes
agents made here — seven entries as of this writing, each with a dated
measurement. Examples: a dated document read as current state; a count taken
from a sample and published as if it covered everything; a session card marked
complete before the work reached the remote.

`VERIFIED`: `docs/intent.md` § 4 sets the rule that governs this whole page —
**the fix for an unfollowed instruction is a mechanism that delivers it at the
right moment, never another statement of it.**

`DERIVED`: the register is written from the *agents'* experience of failing.
Nothing in it came from you. The mistakes that cost you may be different ones
entirely.

## Questions for you

1. Which agent mistakes have actually cost you time or trust? Not the ones the
   register lists — yours.
2. Has an agent ever broken something you cared about? What happened?
3. Is there a mistake you have corrected more than twice?
4. When an agent is about to make one of these, would you rather it be blocked,
   warned, or left alone and told afterwards?
5. Is there a class of work you would rather agents simply never touch?
6. What would make you trust an agent less permanently, rather than for one
   session?

## Your words

`OWNER`:
<!-- ===== END agents/mistakes-that-must-not-repeat.md ===== -->

---

<!-- ===== BEGIN agents/what-agents-may-do-without-asking.md ===== -->
# What I think agents may do without asking you

> **Overlaps with**
> [`../estate/risk-and-owner-authority.md`](../estate/risk-and-owner-authority.md),
> which asks the same boundary from the risk side — spending, restarts, private
> repositories, unsent messages. That page asks what is dangerous; this one
> asks what is routine. Either is a real answer to both.

## My current understanding

`VERIFIED`: `docs/intent.md` records the standing rule — continue approved or
derivable work, never invent product intent; decide and flag when a choice is
reversible and roughly balanced; ask when undoing it would cost more than a
session.

`VERIFIED`: agents in this estate hold admin and push on every repository, can
merge pull requests, change repository settings, and update deployment
variables. The capability is not the constraint; your intent is.

`DERIVED`: you are more permissive than most owners on *execution* and stricter
on *meaning*. Deleting a stale file is fine; deciding what a product is for is
not.

## The boundary as I would draw it

`PROPOSED`: agents may do without asking — write and merge documentation, fix
CI, refactor structure, delete genuinely spent files with a stated reason,
create branches and pull requests, run checks, spend the free provider tiers.

`PROPOSED`: agents must ask first — anything that reaches other people
(publishing, a store listing, a message in your name), anything that costs
money you have not already authorised, deleting a repository, and any change to
what a product *is*.

## Questions for you

1. Where is that boundary wrong — in either direction?
2. Is there something on the "ask first" list you are tired of being asked?
3. Is there anything on the "no need to ask" list that makes you uneasy?
4. Does the boundary change per repository? Which ones are stricter?
5. May an agent delete things? Files, branches, whole repositories?
6. What is the worst thing an agent could do here without you noticing?

## Your words

`OWNER`:
<!-- ===== END agents/what-agents-may-do-without-asking.md ===== -->

---

<!-- ===== BEGIN agents/what-done-means.md ===== -->
# What I think "done" means to you

## My current understanding

`VERIFIED`: this estate has a strict mechanical definition of done — the branch
pushed, the pull request landed, the checks green, the session card flipped
last. `docs/traps.md` records that agents here have marked work finished before
it landed, which is why the mechanism exists.

`DERIVED`: your definition is different and softer, and the two have never been
written next to each other. Mechanically-done work can still be not-done to
you, because what you check is whether the thing *works and feels right*, not
whether the pipeline was green.

`DERIVED`: for a game, "done" is a feeling. For a document, it is whether the
next reader understands it. Neither is testable by CI, and agents currently
have no instruction for either.

## Questions for you

1. When do you consider something finished? Give an example of each: a
   document, a feature, a whole repository.
2. What does an agent have to show you before you believe it works?
3. Is there work here you consider finished that agents keep touching?
4. Is there work agents consider finished that you do not?
5. How much testing is enough? Where does it start feeling like ceremony?
6. When something is "good enough for now", how does an agent know it may stop
   rather than keep polishing?
7. What is the difference between something that is done and something you are
   proud of?

## Your words

`OWNER`:
<!-- ===== END agents/what-done-means.md ===== -->

---

<!-- ===== BEGIN agents/when-an-agent-disagrees-with-you.md ===== -->
# What an agent should do when it thinks you are wrong

> **Overlaps with**
> [`../estate/how-agents-should-work-with-you.md`](../estate/how-agents-should-work-with-you.md)
> question 5. Answer either one.

## My current understanding

`VERIFIED`: this estate's rule is that your live word beats any written record,
**and** that the agent owes you the contradiction — name what it conflicts
with, give both sides, recommend one, then follow your word. Never resolve the
conflict silently in either direction.

`VERIFIED`: you framed it yourself: *"it could be possible that I personally
misunderstood something and gave the wrong orders, though this is not
likely."*

`VERIFIED`: there is a measured reason to trust you — three separate sessions
counted your claims about this estate against their own transcripts and found
you near 90–100 % correct on the claims you stated without hedging, with the
errors concentrated in the ones you explicitly marked uncertain.

`DERIVED`: so the useful behaviour is not deference and not challenge — it is
reading your hedges. An unhedged statement from you is worth acting on; a
hedged one is worth checking.

## Questions for you

1. How much pushback do you actually want? Give an example of the right amount.
2. Has an agent ever agreed with you when it should have argued?
3. When an agent thinks your plan is wrong, what should it do first?
4. Do you want to be told when you contradict something you said earlier?
5. Is there an area where you would rather an agent just did what you asked
   without the argument?

## Your words

`OWNER`:
<!-- ===== END agents/when-an-agent-disagrees-with-you.md ===== -->

---

<!-- ===== BEGIN agents/when-an-agent-should-stop.md ===== -->
# When I think an agent should stop and wait for you

## My current understanding

`VERIFIED`: `docs/intent.md` is unusually firm here — *ask immediately, but do
not stop working for it.* Stop only when there is genuinely no next step
available without your answer. If another approved step exists, take it and
collect the answer on your next check-in.

`VERIFIED`: you also said the opposite failure is worse: *"I'd rather have an
agent ask me something so I can clarify than that they misunderstand the
goal."*

`DERIVED`: so stopping is nearly always wrong and asking is nearly always
right, and the estate's older instinct to conserve your attention is the part
that needs unlearning, not the asking.

`DERIVED`: the case you have not addressed is a **long absence**. Everything
above assumes you are back within thirty minutes. A week away changes which
choice is correct, and nothing here says how.

## Questions for you

1. When you are away for days rather than minutes, what should an agent do with
   a question it cannot answer — stop, guess and flag, or pick the safest
   option and record it?
2. Would you rather come back to finished work built on one wrong assumption,
   or to unfinished work that waited for you?
3. Has an agent ever stopped when you wished it had continued? Or continued
   when you wished it had stopped?
4. If an agent is unsure whether something is in scope, what should it do?
5. Is "I ran out of useful work" an acceptable way for a session to end?

## Your words

`OWNER`:
<!-- ===== END agents/when-an-agent-should-stop.md ===== -->

---

<!-- ===== BEGIN agents/which-agent-for-which-work.md ===== -->
# Which AI should do which work

## My current understanding

`VERIFIED`: `docs/intent.md` § 7 records your own roster, given 2026-08-08 —
Claude as the main agent doing planning, implementation and documentation with
the widest capability; ChatGPT doing real implementation and proven reliable;
Gemini and Grok routed to review, brainstorming and planning; Codex for
independent pull-request review. You also said not to assume every method works
on every agent.

`VERIFIED`: on 2026-08-29 you narrowed the Codex rule live — reserve it for
readiness checks and genuinely important changes rather than after every push,
because it burns usage limits.

`DERIVED`: that roster is a year-old-at-most snapshot of a fast-moving field,
and you are about to re-subscribe gradually, which is exactly the moment to
restate it rather than inherit it.

## Questions for you

1. Restate the roster in your own words as of now. Who does what?
2. Which of them do you actually enjoy working with, separately from which is
   most capable?
3. Which subscription would you keep if you could only keep one?
4. Is there work you deliberately give to two of them to compare?
5. Should an agent ever hand work to another AI on its own initiative?
6. What do you want from having several rather than one — better answers, a
   second opinion, or not being dependent on one company?

## Your words

`OWNER`:
<!-- ===== END agents/which-agent-for-which-work.md ===== -->

---

<!-- ===== BEGIN agents/working-across-devices-and-surfaces.md ===== -->
# Where you work, and what an agent should assume about it

## My current understanding

`VERIFIED`: sessions in this estate run in several places — a remote container
launched from the web, a desktop application, a laptop, and other AI tools
entirely. `docs/activity/` exists precisely because work done on your laptop
produces no commit here and nothing else could see it.

`VERIFIED`: an agent booted in a satellite repository loads that repository's
setup and none of this hub's, silently. Where a session starts changes what it
can do, without saying so.

`DERIVED`: you move between surfaces more than the records assume, and some of
your best thinking happens where no agent is watching — which is exactly what
this offline week will be.

## Questions for you

1. Where do you actually work from — which devices, which apps, in what
   proportion?
2. Do you ever want to work on this from a phone? What would you want to do
   there?
3. What do you do outside these repositories that agents cannot see?
4. Is there anything you would like to capture on the move and have an agent
   pick up later?
5. Does it matter to you which surface a session runs on, or only that it
   works?

## Your words

`OWNER`:
<!-- ===== END agents/working-across-devices-and-surfaces.md ===== -->

---

<!-- ===== BEGIN estate/how-agents-should-work-with-you.md ===== -->
# How I think agents should work with you

## My current understanding

`VERIFIED`: you prefer to attend planning and delegate execution once the goal,
method, and important decisions are settled. You would rather answer a real
clarifying question than have an agent misunderstand the goal.

`VERIFIED`: you expect agents to verify live state, decide safe and reversible
implementation details, preserve unrelated work, and ask at action time for
consequential external changes.

`DERIVED`: what you want is not maximum autonomy. It is correctly bounded
autonomy: agents should keep moving without inventing product intent or hiding
the assumptions on which a plan depends.

## What I suggest

`PROPOSED`: planning updates should show interpretation, recommendation, the
important uncertainty, and the next consequence. Execution updates should be
brief and outcome-led. A genuine non-blocking question should be asked while
other approved work continues.

## Questions for you

1. What is the most annoying small thing agents repeatedly do?
2. When you check after roughly 30 minutes, what do you most want to see?
3. What would you like to hand over completely but do not yet trust agents to
   handle?
4. When should an agent fix an adjacent problem without asking?
5. When an agent disagrees with your proposed direction, how should it present
   that disagreement?
6. What kind of mistake should stop work immediately, even if other tasks remain?

## Your words

`OWNER`:

<!-- ===== END estate/how-agents-should-work-with-you.md ===== -->

---

<!-- ===== BEGIN estate/how-priorities-should-work.md ===== -->
# How I think priorities should work

## My current understanding

`VERIFIED`: current records place method reliability ahead of broad feature
work while treating Slingy Spider and the bot/community work as important
products. Several other repositories are paused, parked, or archived.

`DERIVED`: priority should follow your present interest and real-world value,
not whichever repository has the longest backlog or loudest automation.

`DERIVED`: reliability work is justified when it prevents repeated failures in
real work. It should not grow into a permanent reason to postpone the products
the estate exists to help you make.

## What I suggest

`PROPOSED`: every plan should say which of these it serves: owner value, a real
user, an outside deadline, risk reduction, reusable capability, learning, or
cleanup. Work with no clear answer should not become urgent by accumulation.

## Questions for you

1. What currently deserves the largest share of agent time?
2. Which outside clocks should be allowed to override your normal priorities?
3. When does method or infrastructure work earn priority over product work?
4. Which active repository would you be comfortable pausing tomorrow?
5. Which paused repository do you still think about often?
6. Should agents recommend stopping low-value work even after substantial time
   has already been spent on it?

## Your words

`OWNER`:

<!-- ===== END estate/how-priorities-should-work.md ===== -->

---

<!-- ===== BEGIN estate/how-repositories-begin-change-and-end.md ===== -->
# How I think repositories should begin, change, and end

## My current understanding

`DERIVED`: repositories have often been created quickly around an idea or an
agent workflow. That made creation easy but left later agents to infer audience,
finish lines, and boundaries from implementation history.

`DERIVED`: a repository should exist when it owns a durable product, reusable
tool, operational boundary, or evidence corpus. A temporary experiment or a
small component does not automatically need its own repository.

`VERIFIED`: you already use active, paused, parked, frozen, and archived states,
but the meaning and exit conditions of those states are not consistently stated
inside each repository.

## What I suggest

`PROPOSED`: every repository records why it exists, who it serves, what good
looks like, what it must not become, what would cause a pause, and what would
allow archive or deletion. Status changes should be explicit decisions, not
inferences from the date of the last commit.

## Questions for you

1. What must be true before an idea earns its own repository?
2. When should a project be a folder inside an existing repository instead?
3. What is the practical difference between paused, parked, frozen, and
   archived for you?
4. How long can an active repository go untouched before its status should be
   reconsidered?
5. What evidence is enough to declare something finished?
6. Are there conditions under which you want a repository deleted rather than
   archived?

## Your words

`OWNER`:

<!-- ===== END estate/how-repositories-begin-change-and-end.md ===== -->

---

<!-- ===== BEGIN estate/minimum-baseline-for-a-new-repository.md ===== -->
# Minimum baseline I think every new repository needs

## My current understanding

`DERIVED`: you do not want another large universal scaffold copied everywhere.
You want a small baseline that prevents the same ambiguity now present in older
repositories.

`PROPOSED`: a new repository should begin with:

- a plain README explaining the product or purpose;
- an owner-intent page with labelled inference and open questions;
- a current-state page that can be replaced without rewriting history;
- a short plan with completion criteria and non-goals;
- agent instructions and repository-specific safety boundaries;
- a decision home, an evidence home, and concise session handoffs;
- proportionate checks that verify the repository's real risks;
- a named relationship to the estate hub and any shared kit.

`PROPOSED`: experiments can use a lighter version, but they still need a stated
question, time or effort box, evidence format, and disposal decision.

## Questions for you

1. Which of these items are essential on day one?
2. What should an agent be forbidden from scaffolding before real use proves it
   is needed?
3. Should every new repository start private unless you choose otherwise?
4. What is the minimum check for a non-code or research repository?
5. When should the shared kit be adopted: at birth, after the first useful
   result, or only when the repository becomes long-lived?
6. Who should review the first plan before implementation begins?

## Your words

`OWNER`:

<!-- ===== END estate/minimum-baseline-for-a-new-repository.md ===== -->

---

<!-- ===== BEGIN estate/risk-and-owner-authority.md ===== -->
# How I think risk and owner authority should work

## My current understanding

`VERIFIED`: agents may handle safe, reversible technical details within the
requested scope. They should ask before spending, publishing, sending messages,
changing access or privacy, handling credentials, deleting material, or taking
another consequential external action.

`DERIVED`: the important boundary is consequence, not whether a task is
technically difficult. You want agents to act decisively inside the boundary
and to make the exact consequential step visible when your authority is needed.

`DERIVED`: repositories with real users, production services, private data, or
payments need stronger repository-specific rails than experiments.

## What I suggest

`PROPOSED`: each repository declares its consequence profile: users, production,
money, private data, external communication, destructive operations, and
recovery path. Shared rules remain short; repository-specific risks live beside
the code they govern.

## Questions for you

1. What level of spending is always meaningful enough to ask about?
2. Which services may agents restart or redeploy without asking?
3. Which repositories must remain private, and why?
4. What kinds of temporary downtime are acceptable without your approval?
5. When is a reversible deletion, such as archiving or trashing, still important
   enough to ask first?
6. Are there external messages agents may draft but never send without you?

## Your words

`OWNER`:

<!-- ===== END estate/risk-and-owner-authority.md ===== -->

---

<!-- ===== BEGIN estate/what-success-looks-like.md ===== -->
# What I think success looks like

## My current understanding

`VERIFIED`: the current intent record names three outcomes: a fresh session
takes a correct first action without steering; the same mistake is not corrected
twice; and sessions stop asking questions the repository already answers.

`DERIVED`: those are means, not the full result. The deeper result is that you
can trust agents to make steady progress on things you care about without the
estate becoming harder to understand each month.

`DERIVED`: repository counts, document counts, and automation counts are poor
success measures. Useful products, correct decisions, findable truth, fewer
repeated failures, and less supervision are better measures.

## What I suggest

`PROPOSED`: give the successor a small set of observable success tests:

- a new agent can identify the right repository and first action;
- a repository can explain its purpose, present state, next meaningful outcome,
  and safety boundaries without the hub copying its internals;
- a correction becomes a durable fix at the right layer;
- you can see what genuinely needs your attention without reading an agent log;
- old material does not dominate ordinary search.

## Questions for you

1. What would make you say after three months that the new hub was worth doing?
2. What would make it a failure even if every automated check passed?
3. How much maintenance of the hub itself is acceptable in a normal month?
4. What should an agent be able to understand in five minutes?
5. What outcome matters more than speed when the two conflict?
6. When should the structure be simplified rather than extended?

## Your words

`OWNER`:

<!-- ===== END estate/what-success-looks-like.md ===== -->

---

<!-- ===== BEGIN estate/where-truth-should-live.md ===== -->
# Where I think truth should live

## My current understanding

`VERIFIED`: the target repository owns implementation truth. The estate hub owns
cross-repository routing, provenance, relationships, and owner attention. When
the two disagree, the disagreement must be reported rather than hidden.

`DERIVED`: you want one fact in one logical home, with pointers elsewhere. You
also want small, purpose-named files because agents retrieve from obvious names
more reliably than from long general documents.

`DERIVED`: owner intent is special. It needs a discoverable place in each
repository, but agents must not turn their interpretation into your words.

## What I suggest

`PROPOSED`: every durable statement declares its type: owner intent, current
state, plan, decision, idea, evidence, practice, or history. A generated index
may repeat a title and link, but not a hand-maintained copy of the underlying
claim.

## Questions for you

1. Which information do you personally want duplicated for convenience, if any?
2. Should owner intent live inside each product repository, in the hub, or in
   both with one clearly canonical?
3. How should a later change to your intent preserve the older reasoning?
4. When live behavior contradicts a written plan, which record should be fixed
   first?
5. How much evidence do you want attached to ordinary decisions?
6. Should the successor forbid loose files outside named role folders?

## Your words

`OWNER`:

<!-- ===== END estate/where-truth-should-live.md ===== -->

---

<!-- ===== BEGIN estate/why-this-estate-exists.md ===== -->
# Why I think this estate exists

## My current understanding

`VERIFIED`: you own 28 repositories today. They include products, experiments,
shared methods, operational infrastructure, finished tools, and historical
records.

`DERIVED`: the estate is not valuable because it contains many repositories.
It is valuable because it lets you turn ideas into real, testable things with
agents while keeping enough continuity that work can continue across sessions
and across different AI systems.

(Owner reply 31-08-2026: Yes that's some of why it's important, but mainly it's also there as the main boot repo for my agents.
The goal of this repo and it's successor is to provide a stable source of information and a well designed workflow with rules, hooks and skills for my agents to use.
This is important because I have so many repos and different projects that having one consistent base is very valuable to help every agent undertand the bigger picture.
Each agent should be able to understand the current goals and how we work here based on the required reading order.

All information related to what I do and how I do it as well as how and what my agents can do in different environments should all be easily discoverable and feel intuitive to find and read. Meaning that based on folder and file names, everyone should immediatly understand what kind of information is written in certain places.)


`DERIVED`: you want to spend your attention on intent, judgement, product feel,
and meaningful choices. You do not want to repeatedly reconstruct history,
explain the same correction, navigate agent-created clutter, or supervise
routine execution.

(Owner reply 31-08-2026: Correct, I want to prepare this repo and it's successor in such a way that helps prevent repeated mistakes and explains to my agents how I intend to work and what I expect them to do.
The important part is that my agents take initiative to leave the repo(s) in a better shape than before and to help make the next agents task easier. )

## What I think the successor should protect

`PROPOSED`: useful work should become easier and more reliable. The hub,
methods, records, and checks are support systems for that outcome, not ends in
themselves.

`PROPOSED`: the estate should preserve experiments and null results when they
still teach something, but it should not preserve every artifact merely because
an agent created it.

(owner reply 31-08-2026: Both agreed. I want to make sure that my agents understand that they should not just create and leave a lot of clutter in the repo(s) but that they should also clean up after themselves and make sure that the repo(s) are left in a better shape than before. )

## Questions for you

1. What decision or frustration originally made you start working this way?
(Owner reply 31-08-2026: This started because of the EAP Projects. Since that created a lot of repos and an insane amount of work, I thought it would be a good idea to create a central repo that would help my agents understand how I work and what I expect from them. This way they can work more independently and I can focus on the important things. Previously I was still using /superbot for all the documentation but that repo wasn't meant to hold the context of multiple other repos. )
2. If this works very well a year from now, what do you spend a normal evening
   doing—and what have agents taken off your plate completely?
   (Owner reply 31-08-2026: 
   a year from now is honestly a pretty long time. I'm not sure what I'll be doing then. For now I'm still busy with a lot of things and maybe some of these things will become a bigger part of my life, but maybe I won't be spemding as much time with this as I do now. I think it's important that no matter what I intend to do, the work will always be able to go smoothly and with few mistakes. I want to make sure that my intent is correctly known and that my agents reliably know the way I like to work.)
3. What do you most want to build, even if no current repository contains it?
(Owner reply 31-08-2026: I don't really have anything like this at the moment, I guess I do really want the slingy spider game to be finished and released on the play store and the app store. I hope to be able to make some money with this game and possibly even to make it a large hit. Tho I understand that this is not something that happens easily, so I don't have large expectations from it.)
4. Which part of creating things with agents do you genuinely enjoy most?
(Owner reply 31-08-2026: I enjoy a lot of it actually, even when it feels a little boring and time consuming sometimes. I am eager to learn more about the capabilities of the agents and to discover what they can do for me. Im trying to find out just how much I can ask my agents to do before I need to step in, preferably I would like to be able to do everything just from the chat, by telling my agents what the desired end goal is, I expect that my agents then find out all the necessary steps to reach that goal and to execute it to completion. I really like finding out how much is possible and the kind of things AI can make these days.)
5. Which recurring part do you tolerate only because nobody has made it
   reliable enough to hand over?
   (Owner reply 31-08-2026: I don't really know yet, I think probably what I'm trying to improve right now by mapping my intent more clearly across the repos and making sure that my agents understand what I have in mind and what I expect from them to get there. I wan't to be able to fully trust that my agents create files and folders in the repos in logical and structured positions. )
6. If only three current repositories could remain, which three would you keep
   and why?
(Owner reply 31-08-2026: If only 3 repos could remain to exist I would keep /superbot /spider-swing and /websites. Tho I guess instead of keeping /superbot I'd rather rebuild it correctly in a new repo that's properly structured from the start.)
## Your words

`OWNER`:
Owner reply 31-08-2026: To summarize, I want to make sure that my agents understand how I work and what I expect from them. I want to make sure that they can work independently and that they can leave the repo(s) in a better shape than before. I want to make sure that my intent is correctly known and that my agents reliably know the way I like to work.

This repo and it's successor should be a stable source of information and a well designed workflow with rules, hooks and skills for my agents to use. It shoul help to guide all kinds of different AI models to properly work by themselves and with each other on my repos.

I should not have to re-explain everything over and over again, each part of this repo should have a clear purpose and make sure that it helps an agent understand more about what is possible and expected.
<!-- ===== END estate/why-this-estate-exists.md ===== -->

---

<!-- ===== BEGIN folders/archive.md ===== -->
# What I think the `archive/` folder is for

## Proposed contract

`VERIFIED`: the present direction requires human judgement before a file is
archived. Age and missing references may create a candidate; they cannot prove
that the file has no remaining value.

`PROPOSED`: archive under the file's original role and archive month, freeze the
path, exclude the whole folder from ordinary search, and generate a manifest of
old path, new path, date, reason, replacement, commit, and rewritten links.

The archive is not a second live tree and never receives current updates.

## Questions for you

1. When looking for old material, would you rather browse its former role or
   search one manifest?
2. How long should material remain untouched before it becomes a candidate?
3. Which classes of files should never be archived automatically or in bulk?
4. Do you want repository-level history and hub-document history treated the
   same way?

## Your words

`OWNER`:

<!-- ===== END folders/archive.md ===== -->

---

<!-- ===== BEGIN folders/decisions.md ===== -->
# What I think the `decisions/` folder is for

## Proposed contract

`PROPOSED`: one settled choice per small file, with the question, decision,
reason, authority, date, consequences, and links to the evidence or owner words.

Decisions are not silently edited into a new meaning. A later choice supersedes
the earlier one and links both directions. This folder does not contain open
questions or implementation detail.

## Questions for you

1. Which decisions are too small to deserve a durable record?
2. Do you prefer readable names alone or a stable decision number as well?
3. Should agent-made reversible decisions be recorded differently from your
   product or policy decisions?

## Your words

`OWNER`:

<!-- ===== END folders/decisions.md ===== -->

---

<!-- ===== BEGIN folders/evidence.md ===== -->
# What I think the `evidence/` folder is for

## Proposed contract

`PROPOSED`: dated audits, experiments, research, measurements, and findings. An
evidence page states method, source, certainty, limits, and what question it
answers.

Evidence informs decisions but does not become policy by itself. Repeated or
superseded evidence can be archived; the conclusion that still matters should
link to the underlying record rather than copying it.

## Questions for you

1. How much raw evidence is worth keeping after a conclusion is settled?
2. Which findings deserve periodic re-verification?
3. Should outside research live here or in the repository that uses it?

## Your words

`OWNER`:

<!-- ===== END folders/evidence.md ===== -->

---

<!-- ===== BEGIN folders/ideas.md ===== -->
# What I think the `ideas/` folder is for

## Proposed contract

`PROPOSED`: possibilities that are worth remembering but are not promises. Each
idea states the problem or opportunity, likely home, origin, and disposition.

New ideas are always recordable. A provisional queue cap triggers review rather
than suppressing entry #51. An idea may become a plan, merge with another, stay
for later, or be retired with a reason.

## Questions for you

1. Do you want ideas grouped by repository, theme, or maturity?
2. What should make an idea surface before the queue reaches its cap?
3. May agents retire weak ideas on their own if the retirement is visible and
   reversible?

## Your words

`OWNER`:

<!-- ===== END folders/ideas.md ===== -->

---

<!-- ===== BEGIN folders/owner.md ===== -->
# What I think the `owner/` folder is for

## Proposed contract

`PROPOSED`: this is your workbench: questions requiring your intent, judgement,
choice, or personal action. It should make everything needing you visible from
one short generated index.

It contains editable workbooks, unanswered owner questions, and pointers to
consequential actions. It does not contain work an agent can settle, secrets,
general project documentation, or copies of long queues from other folders.

An answered page records where the durable answer moved. The index is generated;
the individual pages are written for your hand.

## Questions for you

1. Do you want one combined index or separate “read,” “decide,” and “do” views?
2. Should answered workbooks remain visible here for a while or move immediately?
3. Which items are too sensitive to place in a public repository even without
   credentials?

## Your words

`OWNER`:

<!-- ===== END folders/owner.md ===== -->

---

<!-- ===== BEGIN folders/plans.md ===== -->
# What I think the `plans/` folder is for

## Proposed contract

`PROPOSED`: intended future work with an owner, status, outcome, dependencies,
completion criteria, verification, and rollback. Large cross-repository plans
also name which repository owns each change.

It does not contain undeveloped possibilities, current-state reports, or dated
session narration. Superseded plans are closed visibly and then archived when
their remaining value has been judged.

## Questions for you

1. What makes a possibility mature enough to become a plan?
2. Do you want one current estate plan or several independent active plans?
3. How should plans show work that is deliberately waiting on your attention?

## Your words

`OWNER`:

<!-- ===== END folders/plans.md ===== -->

---

<!-- ===== BEGIN folders/practices.md ===== -->
# What I think the `practices/` folder is for

## Proposed contract

`PROPOSED`: estate-specific ways of working that have earned their place through
use: how to verify, route, review, migrate, or handle recurring traps.

It does not repeat universal agent policy or hide repository-specific rules.
When a practice is reusable across independent repositories and enforceable, it
should be considered for `substrate-kit`; the hub keeps only the estate context
and adoption record.

## Questions for you

1. Which practices do you consider part of your working style rather than a
   technical method?
2. How many successful uses should a practice need before promotion?
3. Who decides that a practice has become unnecessary?

## Your words

`OWNER`:

<!-- ===== END folders/practices.md ===== -->

---

<!-- ===== BEGIN folders/repositories.md ===== -->
# What I think the `repositories/` folder is for

## Proposed contract

`PROPOSED`: one small folder per external repository. It explains purpose,
owner vocabulary, relationships, consequence profile, current route, and where
that repository keeps its own truth.

It does not copy architecture, internal plans, detailed state, or instructions
owned by the target repository. If a repository has no clear purpose, this
folder makes the gap visible instead of inventing one.

## Questions for you

1. Should every repository have a hub folder, or only active and important ones?
2. Which facts must be visible in the one-line estate index?
3. Should archived repositories keep full routing pages or only a short record?

## Your words

`OWNER`:

<!-- ===== END folders/repositories.md ===== -->

---

<!-- ===== BEGIN folders/sessions.md ===== -->
# What I think the `sessions/` folder is for

## Proposed contract

`PROPOSED`: concise continuity records for in-progress and recently completed
work. Each starts with three to five lines explaining what the next session
needs to know, followed by evidence and decisions that are not yet canonical
elsewhere.

A new session reads the three most relevant recent cards, not necessarily the
three newest across the whole estate. Completed cards age out on a defined
clock after durable facts have moved to their proper homes.

## Questions for you

1. Should “last three” mean globally recent, repository-relevant, or both?
2. How long should completed cards remain in normal search?
3. Which information should never be left only in a session card?

## Your words

`OWNER`:

<!-- ===== END folders/sessions.md ===== -->

---

<!-- ===== BEGIN folders/state.md ===== -->
# What I think the `state/` folder is for

## Proposed contract

`PROPOSED`: short answers to “what is true now?” across the estate: active work,
important external services, repository lifecycle status, and current owner
holds. Facts carry a checked date and a source.

It does not contain future work, historical narratives, or copied product state.
Where possible it is generated from repository pointers or live checks. Stale
state remains visibly stale rather than being presented as current.

## Questions for you

1. What estate-level state do you want available without asking an agent?
2. How old may a state claim be before it must display a warning?
3. Which state should be checked automatically and which requires judgement?

## Your words

`OWNER`:

<!-- ===== END folders/state.md ===== -->

---

<!-- ===== BEGIN folders/tools.md ===== -->
# What I think the `tools/` folder is for

## Proposed contract

`PROPOSED`: implementations of hub checks, generators, importers, migrations,
and reports. Every tool names the human problem it solves and the canonical data
it reads or writes.

Policy must not exist only in code. One-off scripts should not become permanent
machinery without repeated need. Tools that belong to a product or the shared
kit stay in those repositories.

## Questions for you

1. Which checks are important enough to block a change?
2. When should a useful one-off script be kept?
3. Do you want a plain-language catalogue of tools separate from technical help?

## Your words

`OWNER`:

<!-- ===== END folders/tools.md ===== -->

---

<!-- ===== BEGIN products/slingy-spider.md ===== -->
# Slingy Spider — the product, not the repository

> The repository page is
> [`../repositories/spider-swing.md`](../repositories/spider-swing.md) and asks
> about state. This page asks about the game.

## My current understanding

`VERIFIED`: the estate's records place core feel ahead of unlock systems,
campaign depth and monetisation, by your directive; a signed build has reached
Play internal testing; and the release path carries a hard floor of twelve
testers for fourteen continuous days plus review time.

`VERIFIED`: you have said you hope to make money from it and possibly for it to
be a hit, while also saying you do not have large expectations.

`DERIVED`: those two sentences are the whole tension in this product. If it is
an evening project, the three-week testing floor is irrelevant. If it is a
commercial attempt, it is the most important date in the estate and nothing is
scheduled against it.

## Questions for you

1. Describe a genuinely good run in the game — what the player is doing and
   what it feels like when it works.
2. Why a swinging game, of all the things you could have built?
3. What is currently wrong with it that you would fix first?
4. Is this an evening project that might earn something, or an attempt at a
   product that you work on in the evenings? They lead to different plans.
5. What would you consider a successful launch — a number, a feeling, or
   something else?
6. If the twelve testers say the core is not fun, what happens?
7. What is the smallest version of this you would still be happy to release?
8. What would you want an agent to do about the launch that it is not doing?

## Your words

`OWNER`:
<!-- ===== END products/slingy-spider.md ===== -->

---

<!-- ===== BEGIN products/what-money-means-here.md ===== -->
# What money means in this estate

## My current understanding

`VERIFIED`: two repositories in the estate are commercial in shape — the game,
which you hope earns something, and `venture-lab`, whose open owner asks
include Stripe test keys and publishing products on a storefront.

`VERIFIED`: you have said of the game that you *"hope to be able to make some
money"* and *"understand that this is not something that happens easily, so I
don't have large expectations."*

`DERIVED`: money here is a signal more than a goal — evidence that something
you made was worth something to a stranger. That reading changes what an agent
should optimise: reaching real users matters more than maximising revenue per
user.

`DERIVED`: but that is an inference from one sentence, and it would be an
expensive one to have wrong.

## Questions for you

1. What would earning your first €100 from something here actually mean to you?
2. Is there an amount at which this stops being a hobby?
3. Would you take money that came with obligations — ads, a publisher, a
   deadline someone else sets?
4. Which of your projects do you think is most likely to earn something, and
   which do you *want* to be?
5. Is there anything here you would refuse to monetise?
6. If none of this ever earns anything, does that change what you do?

## Your words

`OWNER`:
<!-- ===== END products/what-money-means-here.md ===== -->

---

<!-- ===== BEGIN products/what-you-would-build-with-more-agents.md ===== -->
# What you would build if the agents were better — mostly settled

> **You answered the core of this on 2026-08-31 and this page asked it again.**
> Folded 2026-09-01 rather than left for you to answer twice —
> `docs/intent.md` § 2 counts *"sessions stop asking things the repo already
> answers"* as one of the three things that make this estate working.

## What you already said

`OWNER`, 2026-08-31, asked what you most want to build even if no repository
contains it:

> *"I don't really have anything like this at the moment, I guess I do really
> want the slingy spider game to be finished and released on the play store and
> the app store. I hope to be able to make some money with this game and
> possibly even to make it a large hit. Tho I understand that this is not
> something that happens easily, so I don't have large expectations from it."*

And on the direction you are testing:

> *"Preferably I would like to be able to do everything just from the chat, by
> telling my agents what the desired end goal is… I'm trying to find out just
> how much I can ask my agents to do before I need to step in."*

`DERIVED`: so the honest answer to this page's original question is **"nothing
beyond Slingy Spider, yet"** — and that is a real answer, not a gap. The
product questions moved to [`slingy-spider.md`](slingy-spider.md); the
capability question is
[`../you/what-you-want-to-learn.md`](../you/what-you-want-to-learn.md).

## What is still genuinely open

`DERIVED`: your answer describes what you want **finished**. It does not
describe what you would **start**, and those differ — the second only matters
once the first ships.

## Questions for you

1. Is *"nothing beyond Slingy Spider, yet"* right, or was that the answer for
   that evening rather than in general?
2. Once the game ships — or stops — what would you want the agents pointed at
   next?
3. Is there something you would build purely because it would be funny or
   interesting, with no other reason?

## Your words

`OWNER`:
<!-- ===== END products/what-you-would-build-with-more-agents.md ===== -->

---

<!-- ===== BEGIN products/who-you-are-building-for.md ===== -->
# Who you are building for

## My current understanding

`VERIFIED`: at least one product here has real users already — the Discord bot
runs live and serves the game's community server.

`DERIVED`: most of the estate has no stated audience at all. Repositories say
what they do and never who for, which means an agent making a judgement call
about a feature has nothing to check it against.

`DERIVED`: my guess is that the honest answer for much of it is "me" — you
build things you want to exist and a few of them turn outward. That is a
legitimate answer and worth recording plainly rather than dressing up.

## Questions for you

1. Who is the game for? Describe one real person who would enjoy it.
2. Which of your projects are genuinely for other people, and which are for
   you?
3. Do you want an audience, or do you want the things to exist?
4. What do you want people to say about something you made?
5. Is there anyone whose opinion of this work matters to you particularly?
6. Would you rather have a thousand people play it once, or ten people play it
   every day?

## Your words

`OWNER`:
<!-- ===== END products/who-you-are-building-for.md ===== -->

---

<!-- ===== BEGIN repositories/Substrate-kit-app.md ===== -->
# `Substrate-kit-app` — what I think you intend

## Current evidence

`VERIFIED`: this archived repository is a one-shot Gemini/AI Studio dashboard
experiment over hardcoded data. Much of its copied documentation misidentifies
it as the real Substrate Kit.

## My interpretation

`DERIVED`: its remaining purpose is evidence: what one AI Studio attempt made,
what was useful, and how copied scaffolding can obscure a repository's real
identity. It is not a Substrate Kit adopter or product.

## Questions for you

1. Is the generated interface or any design idea worth preserving separately?
2. What lesson from this experiment should affect future AI-generated apps?
3. Is keeping the whole repository useful after that lesson is recorded?
4. Would a screenshot and short evidence note preserve what you care about?

## Your words

`OWNER`:

<!-- ===== END repositories/Substrate-kit-app.md ===== -->

---

<!-- ===== BEGIN repositories/codetool-lab-fable5.md ===== -->
# `codetool-lab-fable5` — what I think you intend

## Current evidence

`VERIFIED`: this archived repository contains `envdrift`, a finished
zero-dependency environment-file drift and lint tool. Releases exist; the PyPI
name belongs to another project, while the Git install remains available.

## My interpretation

`DERIVED`: this is a completed code-tool experiment with possible estate value,
not an active packaging project. A future need should decide whether it is
revived, renamed, absorbed, or simply used as-is.

## Questions for you

1. Is environment drift still a problem you want this tool to solve?
2. Do you expect anyone outside the estate to use it?
3. Would you rename it for package distribution, or is Git installation enough?
4. What would justify unarchiving it?
5. Should its useful checks move into Substrate Kit instead?

## Your words

`OWNER`:

<!-- ===== END repositories/codetool-lab-fable5.md ===== -->

---

<!-- ===== BEGIN repositories/codetool-lab-opus4.8.md ===== -->
# `codetool-lab-opus4.8` — what I think you intend

## Current evidence

`VERIFIED`: this archived repository contains `mdverify`, a finished command-line
tool that checks executable Markdown examples. Releases remain readable and the
documented Git install path still works.

## My interpretation

`DERIVED`: the experiment produced a genuinely useful small tool, but you do
not intend to run it as an actively marketed package. Maintenance should happen
only for a real user, security issue, or estate need.

## Questions for you

1. Do you or your agents still use `mdverify`?
2. Should it remain a standalone tool or be absorbed into another toolkit?
3. Who, if anyone, is its intended user beyond your estate?
4. What kind of defect would justify unarchiving it?
5. Is a working Git install sufficient, or did you ever want normal package
   distribution?

## Your words

`OWNER`:

<!-- ===== END repositories/codetool-lab-opus4.8.md ===== -->

---

<!-- ===== BEGIN repositories/codetool-lab-sonnet5.md ===== -->
# `codetool-lab-sonnet5` — what I think you intend

## Current evidence

`VERIFIED`: this archived repository contains `cfgdiff`, a finished semantic
configuration diff and conversion tool. A release exists; PyPI publication was
not completed.

## My interpretation

`DERIVED`: this is a completed tool experiment rather than a current product.
Its durable value is the capability and evidence, not keeping a release pipeline
alive without users.

## Questions for you

1. Do you or your agents still need semantic configuration comparison?
2. Should the tool remain independently installable?
3. Is PyPI publication still desirable or now unnecessary work?
4. What would justify unarchiving it?
5. Should any capability move into a maintained shared toolkit?

## Your words

`OWNER`:

<!-- ===== END repositories/codetool-lab-sonnet5.md ===== -->

---

<!-- ===== BEGIN repositories/couch-legend.md ===== -->
# `couch-legend` — what I think you intend

## Current evidence

`VERIFIED`: Couch Legend is a live idle stoner simulation that began as a
one-prompt Grok prototype and graduated into a maintained application. Its
current design includes a longer life story and a planned Android shell.

## My interpretation

`DERIVED`: this repository tests whether a playful generated concept can become
a coherent product with its own look, progression, humour, and long-term feel.
It is no longer only proof that the prototype pipeline works.

`DERIVED`: the game succeeds when the progression remains funny and satisfying
long enough to feel like a life story, rather than when it merely accumulates
more content.

## Questions for you

1. Did this turn into a game you care about, or is it mainly a successful
   pipeline demonstration?
2. Who do you imagine playing it, and for how long?
3. What kind of humour or tone must it preserve?
4. What should the Android version add beyond a different package?
5. What would make the late game feel finished?
6. What would cause you to stop expanding it?

## Your words

`OWNER`:

<!-- ===== END repositories/couch-legend.md ===== -->

---

<!-- ===== BEGIN repositories/creator-kit.md ===== -->
# `creator-kit` — what I think you intend

## Current evidence

`VERIFIED`: Menno Creator Kit is a reusable FreeCAD and Godot starting point for
physical parts and spatial experiments, designed to be usable without writing
code. It is new and its current-state template is not yet filled.

## My interpretation

`DERIVED`: this is meant to lower the distance between a physical idea and a
movable, editable model. It may become your personal workshop toolkit rather
than a conventional software product.

`DERIVED`: putting FreeCAD and Godot together suggests two connected needs:
precise printable geometry and an easier spatial environment in which to inspect,
move, or demonstrate ideas.

## Questions for you

1. What object or project made you want this kit?
2. Is it primarily for you, or should someone else eventually use it too?
3. What does “usable without coding” mean in a normal session?
4. Which outputs matter: printable files, reusable parts, interactive scenes,
   instructions, or all of these?
5. Should FreeCAD and Godot remain one repository if their use diverges?
6. What would make the kit feel ready rather than merely seeded?

## Your words

`OWNER`:

<!-- ===== END repositories/creator-kit.md ===== -->

---

<!-- ===== BEGIN repositories/curious-research.md ===== -->
# `curious-research` — what I think you intend

## Current evidence

`VERIFIED`: this is a parked workshop notebook around 3D printing, a robot arm,
Arduino, and a live site. Current records say it should receive a new mission
later.

## My interpretation

`DERIVED`: it is a creative research space rather than a normal product
repository. Its value is helping you explore physical ideas and gifts, collect
useful sources, and turn curiosity into a practical next experiment.

## Questions for you

1. What new mission do you imagine for it?
2. Is the main audience you, gift recipients, or people reading the site?
3. Which past research remains useful enough to carry forward?
4. Should the canonical material live in GitHub, a Gemini notebook, Drive, or a
   deliberate combination?
5. What kind of output should a research thread produce?
6. Is Creator Kit part of this mission or a separate tool that it may use?

## Your words

`OWNER`:

<!-- ===== END repositories/curious-research.md ===== -->

---

<!-- ===== BEGIN repositories/estate-backups.md ===== -->
# `estate-backups` — what I think you intend

## Current evidence

`VERIFIED`: this is a private GitHub Actions venue for estate data backups and
carefully scoped Railway/Postgres operations. It is dormant between explicit
owner asks.

## My interpretation

`DERIVED`: this repository should be deliberately boring: minimal code, narrow
permissions, recoverable workflows, clear evidence, and no feature roadmap. Its
success is reliable recovery and safe one-shot operations, not activity.

## Questions for you

1. Which databases or data sets must it protect?
2. How long should backups be retained?
3. How often should restore—not just backup—be tested?
4. Which operations may run automatically and which always require you?
5. Should backup storage and operational workflows remain in the same repository?
6. What failure or growth would justify replacing this approach?

## Your words

`OWNER`:

<!-- ===== END repositories/estate-backups.md ===== -->

---

<!-- ===== BEGIN repositories/fleet-manager.md ===== -->
# `fleet-manager` — what I think you intend

## Current evidence

`VERIFIED`: this is the active cross-repository router and records home. Its
live branch now contains draft instructions and owner workbooks for a clean
successor named `estate`.

`VERIFIED`: you now want a new repository to take over rather than reorganizing
this one in place. The present repository remains useful but mixes several eras,
roles, and operating systems.

## My interpretation

`DERIVED`: `fleet-manager` has completed an important phase. Its successor
should preserve valuable intent, decisions, evidence, and routes without
carrying forward the crowded namespace or making historical machinery live
again.

`DERIVED`: after a verified cutover, this repository should become read-only
historical evidence. There should never be two writable hubs competing to say
what is current.

## Questions for you

1. Is `estate` still the name you want for the successor?
2. Which three parts of `fleet-manager` would be most damaging to lose?
3. Which parts should remain readable here but not be migrated?
4. What must the successor prove before this repository becomes read-only?
5. Should old links keep landing here, redirect to the successor, or be rewritten
   before cutover?
6. What would make you postpone the cutover even if the new tree looked cleaner?

## Your words

`OWNER`:

<!-- ===== END repositories/fleet-manager.md ===== -->

---

<!-- ===== BEGIN repositories/gba-homebrew.md ===== -->
# `gba-homebrew` — what I think you intend

## Current evidence

`VERIFIED`: this repository contains original-IP GBA and NDS homebrew projects,
including the released Lumen Drift and several parked game concepts plus a web
arcade. Further work waits on your picks and playtest judgements.

## My interpretation

`DERIVED`: the repository is a creative retro-game workshop. Shipping a real
ROM matters, but experimentation, game feel, and building several distinct
worlds are also part of the value.

## Questions for you

1. Which game or world in this repository do you care about most now?
2. Is the aim to release finished homebrew games, explore ideas quickly, or both?
3. Who do you imagine playing them and on what hardware?
4. What did Lumen Drift teach you that should shape the next game?
5. What playtest result would make a project worth continuing?
6. Should the web arcade remain part of the repository's purpose?

## Your words

`OWNER`:

<!-- ===== END repositories/gba-homebrew.md ===== -->

---

<!-- ===== BEGIN repositories/idea-engine.md ===== -->
# `idea-engine` — what I think you intend

## Current evidence

`VERIFIED`: Idea Engine is the canonical half of the former Ideas Lab, holding
hundreds of fleet-era idea files and a completed mathematical verification
loop. It is an on-demand asset at rest.

## My interpretation

`DERIVED`: the original need remains real: good ideas should not disappear,
and weak ideas should be challenged before consuming implementation time. The
present repository may contain more historical process than the future need
requires.

`DERIVED`: the successor hub's `ideas/` role risks overlapping this repository.
The boundary must be chosen before migration.

## Questions for you

1. Do you still want a separate idea repository, or should the new hub own the
   estate-wide idea queue?
2. Which part mattered most: capturing ideas, developing them, testing them, or
   proving that most should not be built?
3. Which historical ideas are still genuinely alive?
4. Should product-specific ideas live in their product repositories instead?
5. What would a useful future Idea Engine do that a simple queue cannot?
6. What can be archived without losing the method's lesson?

## Your words

`OWNER`:

<!-- ===== END repositories/idea-engine.md ===== -->

---

<!-- ===== BEGIN repositories/pokemon-mod-lab.md ===== -->
# `pokemon-mod-lab` — what I think you intend

## Current evidence

`VERIFIED`: this private repository is an Emerald quality-of-life mod lab with
18 optional toggles, a byte-identical-when-off promise, and a source-only safety
rail. Work is frozen pending your next product choice.

## My interpretation

`DERIVED`: this is about improving a familiar game carefully without turning it
into an unrelated redesign. Reversibility and proof that disabled changes do
nothing are core to the concept, not only technical gates.

## Questions for you

1. Is this primarily a mod you want to play yourself or something for other
   players too?
2. What does “QoL+” include, and where should it stop?
3. Do you eventually want a public release or only a source and research lab?
4. Which proposed next direction still excites you?
5. What compatibility or authenticity promise must never be weakened?
6. What would make the repository complete?

## Your words

`OWNER`:

<!-- ===== END repositories/pokemon-mod-lab.md ===== -->

---

<!-- ===== BEGIN repositories/product-forge.md ===== -->
# `product-forge` — what I think you intend

## Current evidence

`VERIFIED`: Product Forge was a seat-era home for projects without another
home. Its main living asset is the released Android phone-controller app, which
current plans propose graduating to its own repository.

## My interpretation

`DERIVED`: this was useful as an incubator, but “home to homeless projects” is
not a stable long-term purpose. A successful product should graduate; a failed
experiment should close; the forge should not become a permanent mixed drawer.

## Questions for you

1. Do you still want an incubation repository at all?
2. What must a project prove before it graduates to its own repository?
3. Should phone-controller graduate now, and what should its new name be?
4. Is there anything else in Product Forge that you still value?
5. After graduation, should this repository be reset for future experiments or
   archived as a record of the seat era?
6. What is the maximum number of unrelated projects it should ever contain?

## Your words

`OWNER`:

<!-- ===== END repositories/product-forge.md ===== -->

---

<!-- ===== BEGIN repositories/proxybench.md ===== -->
# `proxybench` — what I think you intend

## Current evidence

`VERIFIED`: this archived repository is a small, dependency-free proxy-provider
benchmark built largely as a joke and parked without further action.

## My interpretation

`DERIVED`: this is a finished curiosity, not a product or maintained
infrastructure. Its value is the compact benchmark and the story of the
experiment, if either still amuses or teaches you.

## Questions for you

1. Does the benchmark still have any practical value?
2. Is the fact that it was “mostly a joke” part of why you want to keep it?
3. Should future proxy testing reuse it or start fresh?
4. Is archive the final state, or would a short evidence record be enough?

## Your words

`OWNER`:

<!-- ===== END repositories/proxybench.md ===== -->

---

<!-- ===== BEGIN repositories/shiftlife.md ===== -->
# `shiftlife` — what I think you intend

## Current evidence

`VERIFIED`: ShiftLife is a private shift calendar for shift-working households,
with inland shipping as the first audience. It has a free core, a proposed
one-time Pro layer, and is paused with some real-world and deployment work still
open.

## My interpretation

`DERIVED`: this is unusually important because it aims at a known everyday
problem for real people beyond the estate. Reliability, understandable setup,
and notifications matter more than breadth.

`DERIVED`: the pause does not mean the idea is discarded. It means the product
needs a deliberate return point and owner attention for on-phone testing and
business choices.

## Questions for you

1. What personal experience made this problem worth solving?
2. Who is the first real household you want it to work for?
3. What is the smallest promise the free version must always keep?
4. Is one-time Pro still the model you want, and what should never be paywalled?
5. What would need to be true for you to resume work?
6. What result would make you stop rather than continue improving it?

## Your words

`OWNER`:

<!-- ===== END repositories/shiftlife.md ===== -->

---

<!-- ===== BEGIN repositories/sim-lab.md ===== -->
# `sim-lab` — what I think you intend

## Current evidence

`VERIFIED`: Sim Lab is the evidence half of the Ideas Lab and contains a reusable
verification harness. The name also describes a method that has since been run
inside other target repositories.

## My interpretation

`DERIVED`: the durable idea is more important than the current repository: test
important claims with explicit gates before committing to a feature or concept.
Reusable harness code may deserve a home, while each result belongs beside the
product or question it evaluates.

## Questions for you

1. Is Sim Lab primarily a repository, a reusable method, or both?
2. What kinds of decisions should require a simulation or four-gate review?
3. Where should experiment results live after the decision is made?
4. Which harness pieces are valuable enough to maintain?
5. Should the general method move into Substrate Kit?
6. What would justify reactivating this repository?

## Your words

`OWNER`:

<!-- ===== END repositories/sim-lab.md ===== -->

---

<!-- ===== BEGIN repositories/spider-bot.md ===== -->
# `spider-bot` — what I think you intend

## Current evidence

`VERIFIED`: Spider Bot is the live AI community bot for the Slingy Spider
Discord server. It supports the tester funnel, human roster, feedback path,
server management, and AI conversation. Pushes to `main` deploy to a real
Railway worker.

## My interpretation

`DERIVED`: this repository exists to give the game community a clean, safe bot
that can be improved without inheriting the old SuperBot architecture. It is
both operational infrastructure and part of the server experience.

`DERIVED`: its first finish line is a reliable tester/community loop, but it may
grow into a community product if you want the server to outlive the closed test.

## Questions for you

1. Is Spider Bot mainly a tool for the game, or a community product in its own
   right?
2. What should people feel about the bot: quiet utility, server character, or
   something between?
3. What should happen to it if the closed test ends and the community stays small?
4. Which actions should it never take without a human?
5. Is direct deployment from `main` deliberate, or merely how the repo started?
6. What would make you consider the tester and feedback funnel complete?

## Your words

`OWNER`:

<!-- ===== END repositories/spider-bot.md ===== -->

---

<!-- ===== BEGIN repositories/spider-swing.md ===== -->
# `spider-swing` — what I think you intend

## Current evidence

`VERIFIED`: Slingy Spider is an Android-first Godot physics-swinging game and is
described as your evening product. A signed build has reached Play internal
testing; current records place core feel ahead of unlock systems, campaign
depth, or monetisation.

## My interpretation

`DERIVED`: this is one of the repositories you genuinely want to become a good
product, not merely a technical demonstration. The feeling of movement and a
fun repeatable run matter more than checking off a launch date.

`DERIVED`: releasing on Play matters because it creates a real completed path
to players, but a release that does not feel good would not satisfy the deeper
goal.

## Questions for you

1. Why did you choose a swinging game in the first place?
2. Describe what a genuinely good run feels like.
3. Who do you picture enjoying it most?
4. Is the goal primarily to ship it, to make it good, to learn from it, or some
   combination—and which wins when those conflict?
5. What would make you proud to call version 1.0 finished?
6. If testers say the core is not fun, what would make you keep tuning versus
   stop?
7. Where did the 25,000 target in the current records come from?

## Your words

`OWNER`:

<!-- ===== END repositories/spider-swing.md ===== -->

---

<!-- ===== BEGIN repositories/substrate-kit.md ===== -->
# `substrate-kit` — what I think you intend

## Current evidence

`VERIFIED`: Substrate Kit is the shared method and enforcement kit used across
the estate. Current intent says it is a real product, should become
correction-free, and should grow from proven new problems rather than speculative
rules. Portability across agent surfaces matters.

## My interpretation

`DERIVED`: the kit exists so good working methods survive individual chats and
repositories. Its value is not the size of its doctrine but whether it makes
agents more reliable and autonomous at the moment a rule matters.

`DERIVED`: it should contain general mechanisms. Estate-specific routing and a
product's own rules should remain outside it.

## Questions for you

1. What event originally made you decide a shared kit was necessary?
2. Who besides your own repositories should eventually be able to use it?
3. What exactly would “correction-free” look like in practice?
4. Was it right to make autonomy mechanics binding while leaving daily culture
   as optional house style?
5. Which agent surfaces must be first-class, even if their implementations differ?
6. When should the kit refuse a new rule or mechanism?
7. What would ever make you stop maintaining it?

## Your words

`OWNER`:

<!-- ===== END repositories/substrate-kit.md ===== -->

---

<!-- ===== BEGIN repositories/superbot-games.md ===== -->
# `superbot-games` — what I think you intend

## Current evidence

`VERIFIED`: this archived repository contains SuperBot's pure-Python game world:
mining, fishing, D&D, and exploration. It is complete, parked, and unmaintained.

## My interpretation

`DERIVED`: it is now a readable record and possible donor, not an active
product. Its value is in proven mechanics and domain ideas that a future game or
bot may selectively reuse.

## Questions for you

1. Which game systems are still worth preserving or reusing?
2. Do you want any of these experiences to live again outside SuperBot?
3. Is the archive state final unless a new product explicitly adopts something?
4. What lesson should a future agent read before reusing the code?

## Your words

`OWNER`:

<!-- ===== END repositories/superbot-games.md ===== -->

---

<!-- ===== BEGIN repositories/superbot-idle.md ===== -->
# `superbot-idle` — what I think you intend

## Current evidence

`VERIFIED`: this archived repository contains one idle-game engine and 21
data-only themes. It is distinct from Couch Legend and is unmaintained.

## My interpretation

`DERIVED`: this is a finished engine experiment and theme library. It should
remain available as a donor without creating a standing obligation to update it
or reconcile it with newer idle-game work.

## Questions for you

1. Do any themes or mechanics still matter to you?
2. Should future idle work borrow from this engine or start from Couch Legend?
3. Is the current archive state the intended permanent state?
4. Should its still-running advisory automation be retired if nothing consumes it?

## Your words

`OWNER`:

<!-- ===== END repositories/superbot-idle.md ===== -->

---

<!-- ===== BEGIN repositories/superbot-mineverse.md ===== -->
# `superbot-mineverse` — what I think you intend

## Current evidence

`VERIFIED`: this archived repository is the former browser dashboard for
SuperBot's mining economy. Its Railway service is gone and the planned bot-side
write path never landed.

## My interpretation

`DERIVED`: Mineverse is a closed product path whose remaining value is design,
architecture, and the SuperBot-world historical record. It should not retain a
misleading go-live plan as if deployment were still intended.

## Questions for you

1. Is there any part of the dashboard you still want in another product?
2. What should a future reader understand about why the go-live path stopped?
3. Is any user or economy data still worth preserving separately?
4. Is the archive now final?

## Your words

`OWNER`:

<!-- ===== END repositories/superbot-mineverse.md ===== -->

---

<!-- ===== BEGIN repositories/superbot-next.md ===== -->
# `superbot-next` — what I think you intend

## Current evidence

`VERIFIED`: this is the complete-but-parked ground-up SuperBot rebuild. Its
architecture and parity tests are valuable, but the clean game-community path
now lives in Spider Bot and this repository is not the production successor.

## My interpretation

`DERIVED`: its remaining purpose is to act as an architecture donor and a
record of an attempted rebuild. It should not quietly resume product work unless
you give it a new mission.

## Questions for you

1. Do you still expect any future bot to descend from this architecture?
2. Which parts must be extracted before it can be archived?
3. Is golden parity still valuable now that the product direction changed?
4. What would justify reviving the repository instead of starting clean again?
5. When should its donor role be considered complete?

## Your words

`OWNER`:

<!-- ===== END repositories/superbot-next.md ===== -->

---

<!-- ===== BEGIN repositories/superbot-plugin-hello.md ===== -->
# `superbot-plugin-hello` — what I think you intend

## Current evidence

`VERIFIED`: this is a hello-world contract example for SuperBot Next. The host
vendors its own copy, so the standalone repository is not a runtime dependency.
It is complete and parked but not currently archived.

## My interpretation

`DERIVED`: its purpose was to prove and demonstrate the plugin contract. That
purpose is complete unless you still expect an external plugin ecosystem or a
future host to use the example.

## Questions for you

1. Do you still expect to build plugins against this contract?
2. Is the standalone example useful beyond the vendored copy?
3. Should it be archived together with SuperBot Next after final extraction?
4. Does any lesson belong in a maintained template elsewhere?
5. Would you create this as a separate repository again today?

## Your words

`OWNER`:

<!-- ===== END repositories/superbot-plugin-hello.md ===== -->

---

<!-- ===== BEGIN repositories/superbot.md ===== -->
# `superbot` — what I think you intend

## Current evidence

`VERIFIED`: this frozen repository still backs a live production Discord bot.
It is treated as a behavior and user-experience oracle; agents must not touch
the worker or database without an explicit request.

## My interpretation

`DERIVED`: SuperBot should remain stable for existing users while newer work
extracts only what is still valuable. It is not the place for new architecture
or ambitious feature work.

`DERIVED`: its eventual finish line is a safe retirement or a deliberately
small maintenance life, not indefinite parallel development beside Spider Bot.

## Questions for you

1. Who still relies on the production bot today?
2. Which behaviours or communities must be preserved before it can retire?
3. Do you expect Spider Bot ever to replace it, or are their purposes now
   permanently different?
4. What maintenance is allowed without asking you first?
5. What should happen to its database when the bot is eventually shut down?
6. What evidence would make you comfortable decommissioning it?

## Your words

`OWNER`:

<!-- ===== END repositories/superbot.md ===== -->

---

<!-- ===== BEGIN repositories/trading-strategy.md ===== -->
# `trading-strategy` — what I think you intend

## Current evidence

`VERIFIED`: this archived quantitative research repository tested 5,940
configurations across 11 rounds, promoted none, and spent its holdout. The null
result is explicitly treated as the deliverable.

## My interpretation

`DERIVED`: the repository succeeded by refusing to manufacture a trading edge.
It should remain evidence of disciplined negative research, not quietly turn
into a live-trading system.

## Questions for you

1. Do you regard the null result as a finished success?
2. Is any harness or research method worth extracting for future work?
3. If you revisit trading, should it begin in a new repository with a new
   question?
4. Would any future path be paper-only unless you give a separate real-money
   mandate?

## Your words

`OWNER`:

<!-- ===== END repositories/trading-strategy.md ===== -->

---

<!-- ===== BEGIN repositories/venture-lab.md ===== -->
# `venture-lab` — what I think you intend

## Current evidence

`VERIFIED`: Venture Lab contains commerce experiments, including a Stripe
webhook tool, one live paid item, many prepared products, and finished books. It
is paused by owner direction.

## My interpretation

`DERIVED`: this repository explored whether agents could help create and sell
real digital products. It is not presently an obligation to run a business or
publish the accumulated inventory.

`DERIVED`: any restart must begin with which product or learning still matters
to you, not with pressure to finish the largest existing pile.

## Questions for you

1. Was the main goal revenue, learning how commerce works, making the products,
   or testing agent autonomy?
2. Which existing product do you still personally care about?
3. Who did you imagine buying or using these products?
4. What would make you resume the repository?
5. Should prepared but unpublished products be treated as assets, ideas, or
   unfinished work?
6. What outcome would let you close this chapter without feeling it failed?

## Your words

`OWNER`:

<!-- ===== END repositories/venture-lab.md ===== -->

---

<!-- ===== BEGIN repositories/websites.md ===== -->
# `websites` — what I think you intend

## Current evidence

`VERIFIED`: this repository owns several estate web surfaces: control plane,
bot site, dashboard, and a static review site. Some run on Railway and some on
GitHub Pages.

## My interpretation

`DERIVED`: the repository exists to make useful estate or bot information
visible and, where appropriate, controllable through a browser. It should not
become a catch-all simply because several small sites share hosting knowledge.

`DERIVED`: truth and broken user journeys matter more here than visual polish.
A page that looks finished but reports stale or contradictory state is a
failure.

## Questions for you

1. Who is the intended user of each surviving site: you, bot users, agents, or
   the public?
2. Which current sites should definitely still exist a year from now?
3. Which actions should a browser control plane be allowed to perform?
4. Which information should remain public, and which should require sign-in?
5. When does a site deserve its own repository instead of staying here?
6. What would make this repository complete rather than an indefinite bundle?

## Your words

`OWNER`:

<!-- ===== END repositories/websites.md ===== -->

---

<!-- ===== BEGIN successor/how-the-new-hub-should-feel.md ===== -->
# How the new hub should feel to open

## My current understanding

`VERIFIED`: your clearest statement about structure, 2026-08-31: information
*"should all be easily discoverable and feel intuitive to find and read.
Meaning that based on folder and file names, everyone should immediately
understand what kind of information is written in certain places."*

`VERIFIED`: the failure that produced this whole line of work was a findability
failure — on 2026-08-30 you went looking for the per-repository intent files,
could not find them, and concluded the repository was less structured than it
actually was.

`DERIVED`: so the test for the new hub is not whether it contains the right
things. It is whether **you** can find a thing in it without asking an agent,
on a day when you have not looked at it for a month.

## What I suggest

`PROPOSED`: before the successor is built, do one concrete exercise — name five
things you might go looking for, and say where you would expect each to be.
Where your expectation and the proposed folder structure disagree, the
structure is wrong. It is the cheapest possible test and it needs no tooling.

## Questions for you

1. Do that exercise. Five things you would look for, and where you would look.
2. How many folders is too many at the top level?
3. Would you rather have fewer, longer documents or more, shorter ones?
4. What should be visible the moment you open the repository on GitHub?
5. Is there a repository or website whose structure you find genuinely easy to
   navigate? What does it do right?

## Your words

`OWNER`:
<!-- ===== END successor/how-the-new-hub-should-feel.md ===== -->

---

<!-- ===== BEGIN successor/naming-and-file-size.md ===== -->
# Your naming rule — and the two conditions on it

> Your words, live 2026-09-01: *"more folders and shorter but more specific
> files… the filename tells you exactly what the file contains… the folder name
> should tell you exactly which types of files are there… whenever an agent
> opens a file, it reads it whole."* Shape clarified same day: **nested**, not
> sibling — `superbot/goals/{completed,in-progress,planned}` ·
> `superbot/problems/{cogs,API,railway}`.

## Why the rule is right

`MEASURED`: against this session's three misses your scheme catches **two**; my
counter-proposal, a line-length lint, caught **one**.

`DERIVED`: *"reads it whole"* cannot be an instruction — `docs/intent.md` § 4
is explicit that instructions do not bind and mechanisms do. **Your rule
carries its own mechanism: a 30-line file is read whole because it is 30
lines.** Length is the enforcement; the sentence about reading is decoration.

## Condition 1 — state in the path needs a command

`MEASURED`: `docs/owner-comments/<repo>/{unconsumed,consumed}/` is your scheme
running today. `tools/owner_comments.py consume` moves the file, writes `state`
inside it too, and reindexes — one diff — and `tools/owner_comments.py check`
is a preflight lane, so a file whose folder and contents disagree **reds the
build**. Copy that, not the folder names. Left to agent discipline, a goal that
finishes and is not moved is wrong twice: wrong path *and* wrong state.

## Condition 2 — closed sets in the path, open sets need an index

`DERIVED`: your two examples differ. `{completed,in-progress,planned}` is
**closed** — an agent guesses the path correctly forever.
`{cogs,API,railway}` is **open**: the next subsystem invents a folder nobody
can guess, and guessing is the whole point.

## The measurement that redirects the effort

`MEASURED`: **the folder-per-topic scheme already exists.** `docs/repos/<name>/`
was adopted 2026-08-08 with fixed filenames. **10 of 28** repositories have a
folder; **3 of 10** have anything beyond `README.md`; **1 of 10**
(`spider-swing`) has the full set. It was designed, adopted, and never
populated. A rebuild that re-designs it spends effort on the half that worked.

## Questions for you

1. Which category sets are closed for good, and which will keep growing?
2. What line count should force a split?
3. Which folders must exist in *every* topic, no exceptions?
4. `docs/repos/` was adopted and left empty. What would make the new one fill?

## Your words

`OWNER`:
<!-- ===== END successor/naming-and-file-size.md ===== -->

---

<!-- ===== BEGIN successor/the-door-test.md ===== -->
# The door test

> Your analogy, live 2026-09-01: *"you are standing in a room with a few named
> doors… you can't see past the doors unless you walk through them… if you
> could only see the named doors with no other guideline, you should be able to
> find your way to the room that holds the information you seek."*

`PROPOSED`: make it the successor's acceptance test, not a metaphor. Pick a
question, walk from the root using **only folder names**, and count. A door you
open and back out of is a defect at that level, not a mistake by the walker.

## First run — "what is the current work on spider-swing?"

`MEASURED` 2026-09-01 against this repo, four doors:

| Level | Seen | Defect |
|---|---|---|
| root | 10 doors | **3 dead rooms with live names** — `control/`, `projects/`, `telemetry/` are seat-era history |
| `docs/` | 15 doors **+ 64 loose files** | the floor must be checked before the doors can be trusted |
| `docs/repos/` | 10 repo doors | none |
| `repos/spider-swing/` | 5 files named by *type* | you must open one to learn which |

## Level 4 was graded wrong, and how is the point

I first wrote *"no door says current — it is buried inside `records.md`"* —
from the `ls` output, **without opening anything**. `README.md` carries a
section titled *"Where it stands right now"* and answers in its first
paragraph. **I ran a door test and never opened a door.** Graded the room from
the corridor, which is the one move the analogy exists to forbid.

`DERIVED`, the real and much weaker defect: the answer is behind `README.md`
and nothing on the *outside* of those five names says so — a reader must know
the convention. `goals/current` puts it in the door name. A genuine
improvement, smaller than the false version claimed.

## The amendment — it binds agents *harder*

`DERIVED`: you wrote it would differ for an agent *"since you can probably see
the whole structure at once."* Listing gives me **door names only**, as it does
you — and the error above is the proof. **You open a wrong door, see an
unfamiliar room and back out. I grade the room from the corridor.**

## What the analogy cannot express

`DERIVED`: doors make a tree; some things belong in two rooms. The Play Store
testing floor is a `problems/` fact *and* a `goals/current` fact. A strict tree
picks one and the other is empty. The estate's answer: **one home, the other
room gets a signpost** — `docs/intent.md` § 1.

## Questions for you

1. May a room hold both doors and loose files, or is that always wrong?
2. When something belongs in two rooms, who decides the real home?
3. What question should the door test use as its standard walk?

## Your words

`OWNER`:
<!-- ===== END successor/the-door-test.md ===== -->

---

<!-- ===== BEGIN successor/what-carries-over.md ===== -->
# What comes to the new hub and what stays behind

## My current understanding

`VERIFIED`: `fleet-manager` currently holds a large documentation tree, a
session-card archive, hooks and skills, generated indexes, and a great deal of
material from a program that closed on 2026-07-21 and is explicitly marked
historical.

`VERIFIED`: your own standard, stated 2026-08-31, is that agents should leave
repositories in better shape than they found them and not accumulate clutter.
A fresh hub is the one moment where that is cheap to act on.

`DERIVED`: the temptation will be to copy everything across "just in case",
which would recreate the exact problem the fresh start is meant to solve — a
large archive nobody reads, which `docs/intent.md` already names as a non-goal.

## What I suggest

`PROPOSED`: default to **not** carrying something over. The old repository
stays readable, so leaving a document behind loses nothing except the illusion
that it is current. Carry across only what an agent must load to work
correctly: the boot file, the intent records, the working method, the per-repo
index, and your answered workbooks.

## Questions for you

1. What must be in the new hub on day one for it to be usable?
2. Is there anything here you would be upset to lose track of?
3. Should the session-card history come across, be linked, or be left behind?
4. Do you want the new hub to start small and grow, or start complete?
5. What in the current repository do you think nobody has ever read?

## Your words

`OWNER`:
<!-- ===== END successor/what-carries-over.md ===== -->

---

<!-- ===== BEGIN successor/what-happens-to-fleet-manager.md ===== -->
# What happens to this repository

## My current understanding

`VERIFIED`: `[D-0025]` says this repository becomes the **read-only archive**
once the successor exists. Nothing records what that means mechanically —
archived on GitHub, left writable but unused, or something in between.

`VERIFIED`: archiving a repository on GitHub is reversible and blocks writes
only; deletion is the irreversible one. So the archive decision is cheap to
make and cheap to undo.

`DERIVED`: the risk is not losing this repository. It is that both repositories
stay half-alive — an agent boots into the old one out of habit, finds a
plausible boot file, and works from a frozen record. Nothing currently prevents
that, and the boot file here would not tell it anything is wrong.

## What I suggest

`PROPOSED`: whatever you decide, the cutover should include a redirect at the
top of this repository's boot file and README that names the successor and says
this tree is frozen. That single change is what stops a stale session, and it
costs one commit.

## Questions for you

1. Do you want this repository archived on GitHub, or just left alone?
2. How long do you expect to still refer back to it?
3. Is there anything here you would want to keep working on rather than freeze?
4. Would you ever want it deleted, or does it stay indefinitely?

## Your words

`OWNER`:
<!-- ===== END successor/what-happens-to-fleet-manager.md ===== -->

---

<!-- ===== BEGIN successor/what-the-new-hub-is-called.md ===== -->
# What the new hub is called — settled

> **This page was drafted as an open question and was wrong to be.** You
> settled the name on 2026-08-30 and the record was right there. Corrected
> 2026-09-01 rather than left for you to answer twice — `docs/intent.md` § 2
> counts "sessions stop asking things the repo already answers" as one of the
> three things that make this estate working.

## Settled

`VERIFIED`: the successor is called **`estate`**, in your own words, recorded
in `docs/planning/2026-08-30-fresh-start-redirect.md` line 271:

> *"I think 'estate' might be a good call, I was personally considering calling
> it 'structure' but I feel like that name would make it a bit ambiguous to
> discuss."*

`VERIFIED`: your rejection reason is recorded with it and is worth keeping —
a repository named `structure` cannot be discussed without collision ("the
structure of `structure`"). The same record notes that `estate` is already your
own vocabulary (`docs/ESTATE.md`) and that it names the thing rather than a
mechanism, which is how `fleet-manager` went stale: it names a seat
architecture retired 2026-07-21.

## What is genuinely still open

`PROPOSED`: only two things, and neither needs answering this week.

1. Whether `fleet-manager` survives anywhere as an alias — covered on
   [`what-happens-to-fleet-manager.md`](what-happens-to-fleet-manager.md).
2. Whether the repository is public or private at creation.

## Questions for you

1. Is `estate` still the name, a day's distance from deciding it?
2. Public or private on day one?

## Your words

`OWNER`:
<!-- ===== END successor/what-the-new-hub-is-called.md ===== -->

---

<!-- ===== BEGIN successor/why-agents-misread-this-repo.md ===== -->
# Why agents misread this repo — measured, not guessed

> Written 2026-09-01 after this session made three errors on material the
> repository already records correctly. Your reading: *"so many things are
> already clearly documented but unable to be found by you in one try."*

## What actually happened

`MEASURED` against this session's transcript. **Nothing was unfindable.**

| Miss | Findable? | Cause | A check could catch it? |
|---|---|---|---|
| Asked what the new hub is called | yes, 3 places | never opened the doc | no — a reading habit |
| Called `superbot-next` a finished rebuild | yes, first grep | stopped reading inside the line | **yes** |
| Counted 10 citing pages; 9 were real | n/a | matched a date, called it a citation | no — my method |

The name sits at `docs/decisions.md:650` and twice in
`docs/planning/2026-08-30-fresh-start-redirect.md`, a doc both `README.md` and
`.claude/CLAUDE.md` name. The `superbot-next` qualifier was inside the line I
had already quoted.

## The shape defect

`MEASURED`: `docs/ESTATE.md:85` is **869 characters**, one cell of it **673**.
That cell opens *"the ground-up bot rebuild"* and puts the reversing qualifier
*"parity ≠ ported"* ~400 characters later.

`MEASURED`, lines over 400 chars: `ESTATE.md` **15** (max 1365) · the
consolidation program **71** (max **7393**) · `MAP.md` 3 · rest 0–1.

`DERIVED`: **a mechanical rule covers one miss in three.** Corrected
2026-09-01 — this page first claimed shape was *the* failing axis, and its own
table disagrees. Worth building, but the other two need the hub designed so the
obvious read is the correct one. That is what you asked for, and it is harder
than a lint rule.

## What I propose

1. **One claim per line** — a qualifier never shares a line or cell with the
   claim it reverses. The only one of these a build can fail on.
2. **Anything settled lives in the decisions file, consulted first.**
3. **The boot file routes, it does not summarise** — 404 dense lines teach an
   agent that reading the summary is reading the source.

## Questions for you

1. Rule 3 costs you: a shorter, less useful-feeling boot file, in exchange for
   agents opening real documents. Worth it?
2. Accept a hard line-length limit enforced by a failing check?
3. Is there a document here you have half-read for the same reason?

## Your words

`OWNER`:
<!-- ===== END successor/why-agents-misread-this-repo.md ===== -->

---

<!-- ===== BEGIN you/how-you-decide.md ===== -->
# How I think you make decisions

## My current understanding

`VERIFIED`: `docs/intent.md` records your rule for agents — reversible and
roughly 50/50 means decide and flag; ask when undoing it would cost more than a
session. It also records that a session doing good work on a slightly different
scope is a *small* problem.

`DERIVED`: you decide fast on things you can picture and slowly on things whose
consequences you cannot see. The slow ones are not indecision — they are
missing information about what a choice actually costs.

`DERIVED`: you would rather be given one recommended option with its reason
than three balanced ones, because the balanced set moves the work back to you.

## What I suggest

`PROPOSED`: agents should classify a fork before presenting it — reversible or
not, and what it costs to undo — and lead with a recommendation every time.

## Questions for you

1. Think of a decision here you made instantly, and one you sat on. What was
   different about them?
2. Which decisions do you actively want to keep making yourself, even if an
   agent could make them well?
3. Which decisions would you happily never see again?
4. When you say "you decide", what would break that trust?
5. How do you feel about an agent making a call you would have made
   differently, but that worked out fine?
6. What do you need to see before you can say yes to something irreversible?
7. Have you ever regretted giving an agent freedom here? What happened?

## Your words

`OWNER`:
<!-- ===== END you/how-you-decide.md ===== -->

---

<!-- ===== BEGIN you/how-you-want-to-be-talked-to.md ===== -->
# How I think you want agents to talk to you

## My current understanding

`VERIFIED`: `docs/owner-profile.md` describes you as a non-coder product owner
who wants plain language and pre-chewed decisions — a recommendation plus a
default rather than an open menu. `docs/intent.md` records your preferred
question form: an agent **states its interpretation back** and you correct it.

`VERIFIED`: parts of the estate are written in Dutch (at least one owner-queue
entry is), so agents cannot assume English is the only register you use.

`DERIVED`: you tolerate technical detail but you do not want it as the default
answer. What you want first is *what happened, what it means, what is next*.

## What I suggest

`PROPOSED`: a default reply shape — outcome first, then what needs you, then
detail only if it changes a decision. Evidence links rather than pasted output.

## Questions for you

1. How long should a normal reply be? Give a rough sense — a paragraph, a
   screen, as long as it needs?
2. Dutch, English, or does it depend? Does it differ between chat and files?
3. How much technical vocabulary is fine, and where does it start costing you?
4. When an agent is uncertain, do you want the uncertainty stated openly or the
   best answer with a footnote?
5. Do you want to see the reasoning, or only the conclusion and the evidence?
6. What tone do you dislike most in an AI reply?
7. When something goes wrong, what do you want in the first sentence?

## Your words

`OWNER`:
<!-- ===== END you/how-you-want-to-be-talked-to.md ===== -->

---

<!-- ===== BEGIN you/how-you-work.md ===== -->
# How I think you actually work

## My current understanding

`VERIFIED`: `docs/owner-profile.md` records that you attend planning closely
and step away during implementation, that implementation runs for hours, and
that you check in roughly every 30 minutes. It also records that a plan being
*locked in* is what makes stepping away safe.

`DERIVED`: your working unit is an evening, not a workday. Long unattended runs
are valuable to you mainly because they fit around a life that does not stop
for them.

`DERIVED`: you would rather come back to one finished thing than to three
started ones — but "finished" for you means *landed and verified*, not
*reported done*.

## What I suggest

`PROPOSED`: agents should size work to what can reach a landed state inside one
of your sessions, and say plainly when something cannot.

## Questions for you

1. When do you actually work on this — which days, which hours, how long a
   stretch before you stop?
2. What does a good session with an agent feel like from your side? Describe a
   recent one that went well and one that annoyed you.
3. How long are you willing to wait for one task before you want an update?
4. What do you do while an agent is running — watch it, do something else,
   leave entirely?
5. What usually makes you stop for the night: finishing, tiredness, or losing
   interest in what you were doing?
6. Is there work you keep meaning to do here and never get to? What is it, and
   what actually blocks it?
7. When you come back after days away, what is the first thing you want to see?

## Your words

`OWNER`:
<!-- ===== END you/how-you-work.md ===== -->

---

<!-- ===== BEGIN you/time-money-and-limits.md ===== -->
# Time, money, and what an agent may spend

> **Overlaps with**
> [`../estate/risk-and-owner-authority.md`](../estate/risk-and-owner-authority.md)
> question 1 on the spending threshold. This page asks about the budget behind
> it.

## My current understanding

`VERIFIED`: this repository already records one standing spending decision —
`[D-0011]`, that a paid Gemini key may be spent without asking — and a later
correction that the free key is now the default route because the prepaid
credits expired. So the estate has a budget rule but no statement of the
*shape* of your budget.

`VERIFIED`: you have said you plan to pause every AI subscription for about a
week and restart them gradually.

`DERIVED`: cost matters to you as a recurring commitment rather than as a
per-task expense. A subscription you are not using is worse than a one-off
spend that produced something.

`DERIVED`: the scarcer resource is your evenings, not euros — but nothing in
the records says that outright, so agents optimise for neither.

## Questions for you

1. Roughly what are you paying per month for all of this today, and does that
   number feel right, high, or low?
2. What would you happily pay more for, and what feels wasted?
3. May an agent spend money without asking? Up to what, and on what?
4. Which subscriptions are you actually pausing, and which will come back
   first?
5. How many hours a week do you want to be spending on this?
6. Is there a point where this has to start paying for itself?
7. What is the most expensive thing here that you would cancel tomorrow if
   somebody made a good case for it?

## Your words

`OWNER`:
<!-- ===== END you/time-money-and-limits.md ===== -->

---

<!-- ===== BEGIN you/what-frustrates-you.md ===== -->
# What I think goes wrong for you, and what must stop

> **This is the highest-value page in the collection.** Every concrete answer
> here can become a hook, a check or a routed reminder — a mechanism that fires
> at the moment the mistake would happen. `docs/intent.md` § 4 is explicit that
> this, not another written rule, is how a correction becomes durable.

> **Overlaps deliberately with**
> [`../estate/how-agents-should-work-with-you.md`](../estate/how-agents-should-work-with-you.md)
> question 1, which already asks for the most annoying small thing agents
> repeatedly do. Answer it in whichever file you open first — the other can
> point at it. This page is the wider version.

## My current understanding

`VERIFIED`: on 2026-08-31 you named clutter directly — agents should *"not just
create and leave a lot of clutter"* and should leave the repositories in better
shape than they found them. You also named findability: on 2026-08-30 you went
looking for the per-repo intent files, could not find them, and concluded the
repository was less structured than it is.

`VERIFIED`: `docs/traps.md` records seven recurring execution mistakes agents
here actually made — stale documents read as current, counts taken from a
sample and published as a census, a session card marked finished before the work
landed, among others.

`DERIVED`: the frustrations that cost you most are not bugs. They are an agent
sounding certain about something it did not check, and work that looks finished
and is not.

## Questions for you

1. Name the three things agents do here that annoy you most. Be specific and
   petty — small repeated things matter more than dramatic ones.
2. What is the most recent moment you thought *"I have explained this before"*?
3. Has an agent ever told you something confidently that turned out to be
   wrong? What was it, and how did you find out?
4. What kind of file or folder do you not want to see created again?
5. When you open a repository and feel it is a mess, what specifically are you
   looking at?
6. Is there anything an agent does that makes you check its work more closely
   for the rest of the session?
7. What would you like to never have to say to an agent again?

## Your words

`OWNER`:
<!-- ===== END you/what-frustrates-you.md ===== -->

---

<!-- ===== BEGIN you/what-you-want-to-learn.md ===== -->
# What I think you want to learn versus hand over

## My current understanding

`VERIFIED`: on 2026-08-31 you wrote that you enjoy most of this work, that you
are *"eager to learn more about the capabilities of the agents"*, and that you
are trying to find out how much you can ask an agent to do before you must step
in — ideally directing everything from chat by stating the desired end goal.

`DERIVED`: your learning goal is about **agents**, not about code. You are not
trying to become a developer; you are trying to become very good at directing
developers who happen to be machines.

`DERIVED`: that makes "teach me" and "do it for me" the same request here — the
teaching that helps you is seeing what an agent *can* be trusted with, not how
its code works.

## What I suggest

`PROPOSED`: when an agent does something newly possible, it should say so in
one line — not as a lesson, as a capability you now know you have.

## Questions for you

> Q1 was *"what do you want to understand better a year from now"* — you
> answered it on 2026-08-31 (quoted above) and this page asked it again.
> Removed 2026-09-01; what remains is what your answer left open.

1. Is there anything technical you *want* to learn rather than delegate?
2. What do you currently not trust an agent to do, that you wish you could?
3. When an agent explains something, what makes the explanation useful to you
   rather than noise?
4. What have you learned in the past year here that surprised you?
5. Is there a skill of your own you are worried about losing to delegation?

## Your words

`OWNER`:
<!-- ===== END you/what-you-want-to-learn.md ===== -->

---

<!-- ===== BEGIN you/your-vocabulary.md ===== -->
# Your words for things

## Why this page exists

`VERIFIED`: on 2026-08-31 you wrote that information should be discoverable and
intuitive — *"based on folder and file names, everyone should immediately
understand what kind of information is written in certain places."*

`DERIVED`: names can only do that if they are **your** names. Much of this
estate is named in agent vocabulary — `substrate`, `layer 2`, `the program`,
`OQ-`, `born-red` — and those names are precise but they are not the words you
reach for when you go looking for something.

`PROPOSED`: fill in the right-hand column below with whatever you would
actually type or say. Where the two differ, the successor hub should use yours
and leave the agent term as an alias, not the other way round.

## The table

| The thing | What the estate calls it | What you call it |
|---|---|---|
| This hub repository | `fleet-manager` | |
| The swinging game | `spider-swing` / Slingy Spider | |
| The Discord bot | `spider-bot` | |
| The shared method package | `substrate-kit` | |
| A record of one agent run | session card | |
| Something only you can do | owner queue entry / `OQ-` | |
| A decision written down | `[D-NNNN]` | |
| A per-repository summary | Layer 2 folder | |
| Things you might build later | idea backlog | |
| The repeated-mistake list | trap register | |
| A finished but kept repository | archived | |

## Questions for you

1. Which name above made you pause? That is a name that is costing you.
2. When you go looking for something here, what word do you search for first?
3. Are there things you have a word for that this estate has no file for?
4. Do you want Dutch names anywhere, or English throughout?

## Your words

`OWNER`:
<!-- ===== END you/your-vocabulary.md ===== -->

---

