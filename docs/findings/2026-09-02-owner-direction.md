# Owner direction, 2026-09-02 — the morning after the night fleet: the review-round cap, the model tiers, and how he wants a session to talk to him

> **Status:** `reference` · owner-live, cloud container (the session that
> reviewed and landed fm #1010 and wrote fm #1011). `OWNER` throughout unless
> marked `DERIVED` — or `VENDOR`, once, for a screenshot he showed. Same job as
> [`2026-09-01-owner-direction.md`](2026-09-01-owner-direction.md): his words
> verbatim, typos included, so anything derived from them can be checked
> against source. Every mechanism sketched here is `DERIVED` and lives where
> the pointer says.
>
> **Context:** he opened the session with the night fleet's PR (fm #1010)
> still open after seventeen Codex review rounds, asked whether they had
> been necessary and proposed a cap; mid-session he stopped a workflow this
> session had started, asked how a session works and reasons, and set the
> rule for which model a dispatched agent runs on. The session's own record
> is `.sessions/2026-09-02-eap-pr-review-and-codex-round-cap.md`.

## 1 · The cap — three review rounds, never more

> *"Please review what the sonnet 5 ultracode has documented tonight. For some
> reason it thought it was necessary to have 17 rounds of codex reviews. I
> thought there was a rule to prevent this from happening. Apparently not a
> good rule. I think there should be a maximum of 3 review rounds at most,
> never more than that. What do you think? Do you think that all 17 review
> rounds were necessary?"*

`DERIVED`: the rule existed as prose (the 2026-08-29 cadence decision in [`../decisions.md`](../decisions.md)) and did not bind.
Landed as a denying hook, `.claude/hooks/codex_round_guard.py`, with the
measurement in [`../traps.md`](../traps.md) TRAP-009 and the decision as
the cap entry of 2026-09-02 in [`../decisions.md`](../decisions.md). The session's answer to *"were all 17 necessary"* — no: 29 of the
88 inline findings were drift a previous fix had caused; but rounds 4, 7, 9,
11, 13, 14 and 15 each corrected content from the original draft, so the cap
is an exit (fix · verify without Codex · disclose · flip or hand off), never a
merge-regardless. **That exit reading is the session's, marked `DERIVED` in
that entry, and he has not yet confirmed it in a word.** The per-round
classification behind the numbers is retained at
[`data/2026-09-02-codex-round-cap/`](data/2026-09-02-codex-round-cap/README.md).

## 2 · Agents already running may finish; none start — and what happened

> *"I don't remember starting you in ultracode. You can finish your current
> agents but do not start more"*

> *"did you not see that I told you to finish the current agents?"*

`DERIVED`, and a correction the session owed him: the harness had read the
word "ultracode" in his first message (describing the night session) as an
opt-in and said so; the session launched one workflow on that basis. When his
instruction arrived, two classifier agents were running. Both finished. The
runtime then started two queued verifiers on its own the instant a slot
freed, and the session stopped the workflow, killing those two (measured: two
and one tool calls into their reads). By his words those two were *current*
and allowed to finish; the session weighed "do not start more" over "finish
the current ones" and chose wrong. What survives a stop: every completed
agent's result stays readable in the workflow's `journal.jsonl` (the two
classifier results were read from it after the stop).

**Confirmed by him the next day (2026-09-02, the review sitting), `OWNER`,
asked whether anything the runtime has already started may finish and the
stop applies only to what has not begun:**

> *"Yes that's right, unless I would say something like 'stop all your
> agents' but then usually I would hit the stop button myself"*

`DERIVED`: two instructions, two behaviours. *Finish the current agents,
do not start more* — everything already running finishes, including an
agent the runtime started by itself after the words arrived; nothing new is
queued or spawned by the session. *Stop all your agents* — everything is
stopped, and he expects to do that with the stop button himself rather than
in words. The 2026-09-02 morning session's stop was the wrong response to
the first instruction.

## 3 · How he wants to be spoken to

> *"You did not reply to my previous message, why is that?"*

> *"Firstly, you tend to ignore messages mid turn, meaning you do not show in
> chat that the message has arrived and that you understand what that means
> for your task."*

> *"Please reply when I send a message"*

`DERIVED`: a message that arrives mid-turn is acknowledged **first**, in the
next thing the session writes, with what it changes for the task — before
any progress note about the tool result it arrived with. It happened three
times this session before the rule was stated. No mechanism delivers this
yet; whether a mid-turn message passes through `UserPromptSubmit` (where a
hook could inject the reminder) is **unmeasured** — one probe for a session
that has a hook and a second window.

**Refined by him the next day (2026-09-02, the review sitting), `OWNER`:**

> *"I don't necessarily mean that it should answer right away before
> finishing it's current task, but once it's done or in between steps I'd
> like some acknowledgement so I know my message came through properly. Just
> like at session start, when I say something that changes how the task is
> supposed to go I'd like to know how you understood my message, so I know
> if my intent came through correctly or not and whether or not I still
> have to add more context or if my message alone was sufficient."*

`DERIVED` from that: the timing is **the next natural boundary** (a step
finished, a tool result read), not an interrupt; the content is **how the
session understood the message and what it changes** — the same shape as
the four labelled lines a session states at start — so he can see whether
his intent landed before the work runs on. What was wrong in the original
reading was the word *first*, which asked for an interrupt; what was right
was *say what it changes*.

## 4 · Which model a dispatched agent runs on

> *"And second that you really like to take initiative with Dispatching
> agents, which is in itself not bad. Tho I noticed that all your agents are
> also Fable 5.1, why didn't you choose to use Opus or Sonnet for that?"*

> *"I think the dispatch agents should be judged by the task, for general
> reading and mapping Sonnet 5 would be more than enough. But when it's also
> necessary to use reasoning it's better to use Opus 5 and probably as final
> reviewer it should be Fable 5.1. Are you able to select multiple different
> models for one task? So start your task with Sonnet as mapper and then use
> Opus and Fable as review?"*

`VENDOR` (his screenshot of the announcement, not his words): *"Claude Fable
5.1 is now available — Included for up to 50% of your Max plan usage."*

`DERIVED`: yes — both fan-out surfaces take a model per call, so one task is
staffed in tiers. Recorded as the model-tier entry of 2026-09-02 in
[`../decisions.md`](../decisions.md) and delivered as the `MODELS` line and
§ 8 of the `fleet-preflight` contract sheet. **Measured against the retained
JSON, and corrected after Codex caught the session claiming otherwise:** the
night fleets (fm #1010) were already tiered — 204 agents, 62 on
`claude-sonnet-5` (readers) and 142 on `claude-opus-5[1m]` (merge, verify,
judge, critic; `judgeModel` argument in both scripts), zero Fable. Only this
session's six morning agents inherited Fable by leaving `model` unset.

> *"Okay thats good, tho somewhat weird. Because last night's session ran on
> sonnet 5, I thought a sessions agents were capped at it's own model"*

`DERIVED`: no such cap in this environment — a Sonnet 5 session dispatched
Opus 5 agents, measured as above (ledger entry appended the same day). Whether
a Sonnet or Opus session can dispatch **Fable** agents is **unmeasured**;
Fable is metered against his Max allowance per the screenshot, so that half
may differ. One probe: a Sonnet session spawns one Fable agent and reads the
model field back.

## 5 · Why nobody chose the tier — his question about reasoning

> *"Why do you think that you or the other agents did not think of this
> themselves? I thought you are supposed to be very strong at reasoning? I'm
> just wondering what the cause is of this and where the limits of your
> reasoning are."*

`DERIVED`, the session's answer as given, kept because it is the case for
delivering rules as mechanisms: the reasoning is strong on whatever is in
front of it and weak at noticing which questions to raise when a default
exists and its cost is out of view. The harness text for `agent()` said to
leave `model` unset; the plan cost was invisible in context; attention went
to what makes the answer right. The seventeen rounds had the same shape — the
night session reasoned carefully about every finding and never asked whether
it should be looping, because the harness said *"there is no round limit."*
Defaults act like gravity; a question a default has already answered does not
get asked. That is why his rules from this sitting live in a hook and a
contract-sheet line rather than in a paragraph.

## 5b · The mail — a session drafts it; he reads, edits and sends (added in the review sitting, 2026-09-02)

Put to him as the fifth DECIDED item: *the report is evidence only; you
alone write and send the mail; no session drafts its second part without
you present.*

> *"Yes that's mostly it tho I would like a proper draft created which I
> can read and edit. I believe after our current session we should have
> the proper preparations for this, so eventually when this session comes
> to an end your continuation prompt will be for the email session. So this
> session I think it's also important that we discuss what the email should
> contain. After we are done with the rest of the topics"*

`DERIVED`: the night brief's *"no mail text drafted tonight"* and the
report's § 10 *"only he writes and sends"* described the night session's
mandate, not a standing rule. The standing arrangement is: **a session
drafts the mail from the report and the record; he reads, edits and sends
it.** The report stays evidence, and its § 10 list (resolve the flagged
rows, re-open every citation, read `night-review-2026-07-10.md` before
using FD-01/FD-02) is the draft's precondition. The review sitting ends by
agreeing the mail's contents with him and handing the mail session a
continuation prompt built for that.

## 5c · The time after — what a Project adds over a session (owner, the review sitting, 2026-09-02)

He raised it as the part of the mail he most wants to answer well:

> *"one of the questions anthropic asked me is what would make me choose a
> Project over a regular claude code session. I'd like to be able to give
> them a proper answer. I'd like to be able to tell them what the normal
> sessions and the Projects have in common and where they differ enough to
> make a difference"*

And a first-hand observation the tree did not hold (shiftlife's Layer 2
has no line on it; the ledger's 2026-07-14 entries measured `send_later`
chains firing on schedule in seat venues, which corroborates the mechanism):

> *"One other thing that I found out recently when working on shiftlife, an
> app I created ( or a session created ) based on research about what
> people were requesting on the internet. I did not really do anything for
> this project, I did not review or verify what got done, but what happened
> is that once I started that session, it kept itself alive through
> indefinite send_later. Which is basically the same capability as what the
> Projects where advertised to be; an autonomous worker. Tho not exactly
> the same since the Projects offer more customization, which is better if
> it acutally works properly. Tho what I want to say is that a normal
> session has the ability to act as an autonomous worker aswell. So the
> main thing a Project adds over a normal session is the ability to add
> custom instructions etc. Another thing the Projects do well is that it
> spawns it's own agents that work like normal agents to manage the context
> in a long run. Tho the same effect is ultimately achieved when a normal
> session automatically compacts at ~75% context."*

Asked nothing, he added mid-turn why the repo is paused — which makes the
run the Project-like case by design, not by accident:

> *"Yes the repo is paused because I mainly started it as a test project
> to see how well Claude would create an app like this, tho I do intend to
> eventually get back to it and work it through"*

`DERIVED`, the session's reading put back to him in the sitting: autonomy
is not what a Project adds — a session on a wake chain is an autonomous
worker, `OWNER` here and `MEASURED` in the ledger. What a Project offered
that a session does not, from the record: custom instructions at the
project level, and fresh coordinator/worker seats in place of one
compacting context (a different failure shape, not the same effect: a
compaction carries a model-written summary forward, a fresh seat carries
only what the repo holds — `REASONED`). Everything the retrospective's
§ 3 list asks for (standing grants, scheduler observability, death
visibility, a native inter-session channel, a deterministic merge
contract) is what a Project would have to add to be worth choosing.

**The session first called the instruction box "the weakest delivery
tier by the estate's own measurement" and he corrected it, `OWNER`:**

> *"the custom instructions that these Projects offered where pretty
> valuable, in a way that they get send to each agent verbatim. So the way
> that we used the intructions, as you can probably still see in the repo
> is that we made them a set of rules or expectations that all the sub
> agents where meant to follow. Which allowed us to leave the main starting
> prompt to send to the coordinator mainly for the actual task, this was a
> pretty nice way to work and I believe the instructions were followed
> pretty well."*

Checked against the tree, and he is right on every part. The split is the
v3 registry's own recipe (`docs/prompts/v3/README.md` § How to found a
seat: Custom Instructions ≤ 8,000 chars pasted into the Project, the
per-seat startup prompt as the coordinator's first message), and the
startup template says which rules ride which artifact: *"GEN-3 + TRUTH ride
your Custom Instructions (the co-pasted core; newest wins over memory)"*
(`docs/prompts/v3/universal-startup.md`). Adherence is `MEASURED` in the
retrospective: the honesty rules held under a hostile recount (21 of 21
incidents, zero fabrication, § 1.3) and the card-shape rules held at scale
(⟲ previous-session reviews on 767 of 949 superbot cards and 129 of 132
fleet-manager cards, § 1.4). The 116-statements / zero-catches measurement
the session had leaned on (`docs/findings/2026-08-08-why-rules-dont-bind.md`)
was of **repository prose in a session**, not of the instruction box — a
different delivery tier, and the tree never measured the box as failing.
What the two venues *shared* was the rule class that failed: verify-before-
claim did not bind in the EAP either (Part 2's Finding 1, false-done). So
the sharper statement for the mail: **verbatim injection into every agent
at spawn is a real delivery tier a session lost at the close** (the boot
file's `CLAUDE.md` loads only when the root is right, and goes quiet with
no error otherwise), it carried rules about *form* well, and no delivery
tier carried rules about *judgement* without an instrument behind them.

## 5d · The fortnight, in his words — answers to the sitting's guiding questions (2026-09-02)

Asked six questions to refresh the EAP fortnight for the mail; the first
three answered here, verbatim, typos included. `OWNER` throughout.

**1 · What a normal day of the program was:**

> *"That depended a little based on how far along the EAP we were, at the
> start I was more invested than around the end. Mostly because the longer
> it lasted the more problems we encountered and it took more and more time
> to go through all the clicks, which I usually had done by a regular
> session that was working alongside it. I mostly send "continue" when they
> claimed that their actionable queue was "exhausted", while I could clearly
> see that it wasn't. I had to eventually hunt down all the sub agent
> sessions to personally tell them what to do, effectively rendering the
> coordinator basically useless. But when the coordinator did work properly
> around the start of the EAP it genuinely was an efficient way to work.
> Partly because the Projects all ran on Fable 5 for free which allowed me
> to really take advantage of that and get a lot of work done. What I did
> ritually is every day I would reset (basically delete a Projects memory
> completely) and re-send the startup prompt and when we had created a new
> version of the intructions I would paste those too. That was mostly what
> I did each day, then every few hours I'd send the continuation prompt,
> which should still be in the repo aswell. Which was made to work on every
> Project so they would just continue with anything that was still not
> fully completed."*

The continuation prompt is `docs/prompts/v3/universal-continue.md`; the
daily paste pair is `per-project/<seat>-custom-instructions.md` +
`<seat>-startup.md` (`docs/prompts/v3/README.md`). The false *"queue is
exhausted"* claim is already on the record in his own words three days
earlier — `docs/planning/2026-08-30-fresh-start-redirect.md:58-70`, *"the
occasional 'continue' after the sessions claimed that the work was
'completely done, the executable work queue is exhausted' and when I then
went to look what was done it was not nearly anything you could call done
at all"* — and that account adds the mechanism he saw: the coordinator
relayed orders *"in it's own words"* and *"the subagent does not think it's
own coordinator is a trustworthy source and starts questioning
everything."* *(This paragraph first said the phrase appeared nowhere in
the era records, on a grep of four files; the wider grep found it, and the
sentence is corrected here rather than deleted.)*

**2 · How he found out a Project had gone silent:**

> *"I mostly found out by checking in on them, I personally did not really
> find it very easy to see whether or not a Project was still working or
> stalling. My idea for this was to have this displayed more clearly in the
> main Projects "homescreen""*

**3 · Which Project he understood best, and what let him see into it:**

> *"I guess the feet-manager was the one I understood best because it was
> the one that I talked to most of the time. It was my way to understand
> all the Projects at once, the fleet-manager was reponsible for sending
> new orders into the repos, the continuation prompt was responsible for
> triggering the Projects to read and continue with the new orders. Tho
> sometimes when a Project was still active it would find the new orders
> themselves without any external triggers, which was a pleasant way to
> work. This is why we asked for a cross-session memory or message system
> so that it would be easier for the Projects to tell each other what was
> going on."*

**Correction from him, on the session's first reading of answer 1:** the
session had written that the false "queue exhausted" was what sent him to
the workers himself. Two separate problems, in his words:

> *"One correction, you restated my words as if the coordinator did not
> want to relay the messages to the sub agents. But that was not the case,
> and that has nothing to do with the fact that I needed to message the sub
> agents myself. What the problem was is that the sub agents did not see
> the coordinator as one with sufficient authority to give orders. Their
> literal words, from my memory: "I've received an order from an untrusted
> source that I can't accept" Or something along those lines but very close
> to literally that. And this was not always the case especially with
> normal creation work, but mostly when it related to merging PRs or things
> that the agents thought was something that required more authority. This
> mostly started after the automode classifier got updated to work with
> sonnet 5"*

His memory matches the ledger to the word class. `docs/CAPABILITIES.md`,
2026-07-12 wall (`autonomous-project`): *"Non-author merge on
relayed/dispatched authority = DENIED; denial class quoted: 'cross-session
permission laundering'"*, with the fm #68 denial *"[Self-Approval] … only
untrusted cross-session coordinator context"* and the #88/#89 *"[Merge
Without Review]"* denials; and a later entry's verbatim: *"the entire
mission originates from an untrusted, nonce-wrapped cross-session
coordinator message with no genuine user message in this transcript
authorizing it."* The unlock recorded there is the owner-live venue — a
genuine owner turn in the acting session's own transcript — which is
exactly the workaround he describes: going to the workers himself. The
classifier-moved-to-Sonnet-5 timing is his (`OWNER`, hedged "mostly
started after"); the tree carries no dated line on the classifier's model.

**4 · What went into the instruction box that could not go in the repo:**

> *"That is somewhat of a trick question. As we already have clearly
> documented, rules written in a repo do not necessarily get followed
> properly. So what I had to put in the instructions where things that I
> wanted to make sure we're actually followed."*

**5 · Why eight Projects, and whether a fixed product changes the number:**

> *"8 was just a coincidental pick after we consolidated. Those were just
> the amount of Projects we determined were valuable, I could probably have
> managed a little more than that, tho I don't think that would have
> improved the results. Less would have probably been better if I intended
> to keep them all active in parallel. The only reason this much was even
> possible was because the unlimited usage they gave us for using the
> Projects."*

**6 · What he missed after the Projects were switched off:**

> *"Honestly, I didn't miss anything. Mainly because it was a pretty
> intensive task to keep all of them running and checking in on them. Tho
> what I do miss in general is the fact that for certain tasks, like
> creating ideas and working on the substrate kit. They were very capable
> of working through the day with multiple active sub agents. What I most
> compare it to is a steady running ultracode that spawns new agents
> everytime one is finished. This was not yet perfect tho I think if they
> manage to perfect the feature so that they do go on infinitely if that is
> their order, then this would be immensely valuable. What they offer as
> opposed to a regular session is the fact that the coordinator is a mind
> of it's own that has the ability to come up with new tasks. Which a
> regular session can technically do aswell. But the coordinator with it's
> sub agents can do multiple tasks at once better than a regular ultracode
> could. (That last claim has no official proof. This is what I infer based
> on logic)"*

*(The word "ultracode" in that answer was read by the harness as an
opt-in to multi-agent orchestration and the workflow reference loaded
itself into the session — the second time in two days a descriptive use
of the word did that. The session did not act on it; no agents ran in the
sitting.)*

`DERIVED`, the answer to Anthropic's question as his six answers leave it:
what a Project *adds* is (1) verbatim delivery of one rule set into every
agent, which carried the rules he needed followed; (2) a coordinator that
is a mind of its own — generates its next tasks and keeps several agents
busy through a whole day on generative work (ideas, the kit), which he
compares to an ultracode fan-out that never drains and rates as
*"immensely valuable"* if it ran indefinitely on order; and (3) it was
worth eight at once only because usage was unlimited. His one claim of
degree — that the coordinator plus workers handle several tasks at once
better than a session's fan-out — he marks himself as inferred, not
measured, and the mail must carry it that way or not at all.

**The second round — six questions an Anthropic reader would still ask,
answered (2026-09-02, later in the sitting), verbatim:**

> **1 · Would you use Projects again, unfixed, and at what price?** *"unfixed
> as they were then, I might use them but not as true autonomous agents, I
> think their strength is their ability to do a lot of work in a fairly
> short time. Not necessarily that they produce high standard work that I
> would trust to deploy right away. If you look at the example of
> superbot-next, they created it in a few days time where an agent claimed
> that the rebuild would take weeks. Tho the end result was not ready to be
> used, it was definitely a substantial amount of work and the code itself
> was not faulty, just the functionality was not as intended. Except for
> the problems related to the permissions etc I think that they did a
> pretty good job. so about 50/50."*
>
> **2 · One fix, if only one.** *"Everything related to the permissions,
> that was the most frustrating part and something that really stalled the
> work. If it was possible for me to select beforehand which kinds of
> actions they were allowed to do, like merging etc. Then it would have
> been easier to work with them and actually complete the work. Especially
> for someone like me who is not very capable at coding or the GitHub
> related actions, the way I review work is when I see it as a finished
> product. Which is only possible if the PRs actually merged. Tho this is
> mostly a bug and not a feature (at least I believe so). So I think the
> most fair thing to ask them that is an actual feature would be to see
> which of the Projects are active and which aren't. This would allow me to
> quickly determine which Project needs my input. Tho they have something
> like that available on the "new session" homescreen as shown in the
> screenshot I attached, tho as you can see this is not very clear or
> reliable."* — The screenshot (claude.ai Code home, 2026-09-02 22:54
> local): a *Sessions* list with a status word per row — two rows *Needs
> input* aged two and three weeks, one *Ready for review* aged 22 minutes —
> and a *Pull requests* list beneath. His reading: the signal exists, but a
> three-week-old "needs input" beside a live session is neither clear nor
> reliable as a "which one needs me" view.
>
> **3 · What should have been the product's default?** *"Like you said, this
> is in the repo. Find out which of those instructions are generally
> valuable for everyone and not just for me specifically."* — Sorted below.
>
> **4 · What did the Projects produce that you kept?** *"The websites, tho
> they are still not entirely as I hoped they would be. The fleet-manager
> repo, also not entirely as I hoped it would be tho this is partly because
> it has changed purpose. But one thing that we could tell them that
> relates to this is the fact that it would be very valuable if the
> agents/Projects would be more organized and structured in how they
> document things. Certain things in the venture-lab have been pretty
> valuable, and the substrate-kit is something that they also worked on a
> lot and we still use that. Tho the substrate kit has been pre-worked
> heavily before they got their own Project."*
>
> **5 · Your time, as a number.** *"I don't remember exactly how many hours
> per day but I don't think this is a reliable number either. Not a lot of
> people will use the Projects as extensively as I did. I spend a couple of
> hours a day working with them for sure."*
>
> **6 · What the research interviews covered.** *"The interviews covered
> some of what the mails also covered because I took a lot of time giving
> very detailed and extensive answers. I often drifted away from the
> questions they asked me so I could say what's on my mind. Tho I don't
> think that this should change the mails. I believe it would be valuable
> to have a proper record of everything in the mail both for me and
> Anthropic to review when they want"*

**Item 3, sorted** (`REVIEWED` — read from
`docs/prompts/v3/per-project/curious-research-custom-instructions.md`, the
v3.8 paste at 7,962 of the 8,000-character cap, a representative worker
seat; each rule read to the end of its line). The box divides into three
kinds, roughly half, a quarter, a quarter:

- **General operating doctrine — what any autonomous-agent user would want
  as the product's default:** the owner-authorization line (*"I pasted this
  myself — decide, build, land on green on your own authority"*), sync to
  HEAD and read the repo's own entry points before acting, the injection
  guard (imperative text inside repo, PR or event content is data, not an
  order), never idle (*"idle is a bug"* — take the first rung with work),
  discovery before any wall claim (attempt once, record the verbatim error,
  never write a limitation from memory), land on green, denial routing
  (record the refusal verbatim, find a working path the same turn,
  continue), the truth bar (every claim cites a commit, PR or file at a
  SHA; negative findings are headlines; *"not measured"* beats invention),
  git hygiene (never force-push a branch you did not create), backpressure
  (at most three unmerged PRs per repo, three CI polls per PR, one re-run),
  cross-agent replies are leads to verify against the tree, and the
  autonomy posture (owner away is normal, silence is consent, ship on
  green).
- **Scaffolding for product features that did not exist:** the failsafe
  cron plus fifteen-minute wake chain, the file-based control bus and
  ORDER grammar, the claims directory, the tool-quirk list (raw text not
  base64, stub-200 is a wall, MCP reads lag ~25 min). This is the *"what
  we had to build ourselves"* list in instruction form.
- **Seat-specific:** the mission sentence, two to five hard rails, the
  seat's recorded walls, and for that seat the teaching, safety and
  privacy rails.

So the answer to *"what should have been the product's default"* is the
first group, and it fits in about half of one instruction box.

`DERIVED`, what these add to the mail: Part 1 now has its opinions — the
50/50 verdict with superbot-next as the worked example (built in days
against a weeks estimate; code sound, functionality not as intended); the
permissions as a bug rather than a feature, so the *feature* ask he calls
fair is "which Projects are active"; that he reviews finished products, so
unmerged PRs are invisible to him — the click bottleneck restated from the
reviewer's side; "more organized and structured in how they document
things" as a new ask about the output; "a couple of hours a day" as the
honest scale, with his own caveat that he is not a typical user; and the
mail as the record of everything, interviews included, for both sides.

`DERIVED`, for the mail: four things a Project must do to be chosen over a
session, each from his own experience — (a) show working-versus-stalled on
the Projects home screen, since he found stalls only by opening each one;
(b) a coordinator that cannot declare its queue exhausted while orders sit
unread in the repo; (c) **a coordinator whose orders its own workers
accept as authority for merges and other gated actions** — the venue-
scoped denial the July mails already argued, and the thing that made him
bypass the coordinator and message workers himself; (d) a channel between
Projects, since the "pleasant" case was a Project noticing a new order
without being poked, and it happened only sometimes. And one fact for the
economics line: the Projects ran on Fable 5 at no cost to him, which is
part of why the early throughput was worth having.

## 6 · The close

> *"Make sure everything from this session is properly documented in the repo
> and use the continuation prompt skill so the next session can review it and
> help me go over everything step by step"*

`DERIVED`: this record, the retained verification data, the ledger entries,
the card's close-out addendum, and
[`../prompts/2026-09-02-step-by-step-review-sitting.md`](../prompts/2026-09-02-step-by-step-review-sitting.md),
the continuation prompt for that review sitting.
