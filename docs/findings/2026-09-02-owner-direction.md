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

`DERIVED`, the session's reading put back to him in the sitting: autonomy
is not what a Project adds — a session on a wake chain is an autonomous
worker, `OWNER` here and `MEASURED` in the ledger. What a Project offered
that a session does not, from the record: custom instructions at the
project level (the weakest delivery tier by the estate's own measurement —
`docs/findings/2026-08-08-why-rules-dont-bind.md`, the night report's
survivor #1), and fresh coordinator/worker seats in place of one
compacting context (a different failure shape, not the same effect: a
compaction carries a model-written summary forward, a fresh seat carries
only what the repo holds — `REASONED`). Everything the retrospective's
§ 3 list asks for (standing grants, scheduler observability, death
visibility, a native inter-session channel, a deterministic merge
contract) is what a Project would have to add to be worth choosing; none
of it is custom instructions.

## 6 · The close

> *"Make sure everything from this session is properly documented in the repo
> and use the continuation prompt skill so the next session can review it and
> help me go over everything step by step"*

`DERIVED`: this record, the retained verification data, the ledger entries,
the card's close-out addendum, and
[`../prompts/2026-09-02-step-by-step-review-sitting.md`](../prompts/2026-09-02-step-by-step-review-sitting.md),
the continuation prompt for that review sitting.
