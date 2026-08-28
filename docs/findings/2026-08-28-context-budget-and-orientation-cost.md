# The cold-boot context budget — what orientation costs, and the owner's ruling that it is worth paying

> **Status:** `reference` · 2026-08-28
>
> **What this record is:** the owner ran a deliberate experiment — he started a
> cloud session with *"Orient yourself in the repo and tell me your findings"*
> for the stated purpose of measuring **how much context a fleet-manager cold
> boot consumes**, then took the result into a ChatGPT sitting and reasoned
> about what it means. This is that measurement, his ruling on it, and the
> design framing the sitting produced.
>
> **Source:** [the shared ChatGPT conversation](https://chatgpt.com/share/6a91b2c3-a398-83ed-b737-04c2c9466582),
> read with `tools/read_shared_chat.py` (19,704 characters; the plain fetcher
> returns a title and nothing else — [the convention](../conventions/reading-shared-ai-chats.md)).
> The measured session is **this repository's fm #962**, whose orientation
> report is quoted in full inside that conversation.
>
> **Provenance is labelled per claim and never merged.** `OWNER` = his words.
> `REVIEWED` = the ChatGPT sitting's framing — a second reading, not a second
> authority, labelled the way [`intent.md`](../intent.md) § 8b labels its
> ChatGPT distillation. `DERIVED` = this record's inference. Certainty legend:
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).
>
> **The context figures are `OWNER` · `NOT-VERIFIABLE`, and NOT `MEASURED`.**
> They were read off **his Claude Code UI**, which is the authoritative
> instrument for them. A session cannot instrument its own context-window
> occupancy from the inside — the token counter visible to a running agent is a
> *budget* counter, not a window gauge — so this record **reproduces** his
> readings and does not independently verify them. The legend reserves
> `MEASURED` for *"a command and a real exit code, reproducible"* and gives
> **owner-console state** as its named example of `NOT-VERIFIABLE`; these
> figures are owner-console state exactly. **Corrected after `@codex` R3**,
> which caught this record labelling them `MEASURED` in the same breath as
> saying no session can reproduce them — the label would have told every future
> agent to treat them as re-runnable evidence. Act on them as his statement
> (DISCOVERY RULE step 0); do not cite them as something this estate measured,
> and do not try to re-derive them from inside a session.

## 1 · The measurement

`OWNER` · `NOT-VERIFIABLE` (his UI readout, reported in the sitting). The
session was a cold boot in fleet-manager that walked `README.md`'s mandatory
six-read order and then investigated live state.

| checkpoint | context | added |
|---|--:|--:|
| session initialized, before any repo reading | 69.7k | — |
| six mandatory reads + initial live surfaces | 127.6k | **+57.9k** |
| full orientation and live-state investigation | 157.3k | **+29.7k** |
| **total repo-orientation delta** | | **+87.6k** |

**The composition at 157.3k**, which is the part that redirects the obvious
conclusion — and **read the arithmetic note under it before quoting any row**:

| component | tokens |
|---|--:|
| messages | 99.9k |
| system tools | 18k |
| MCP tools | 14.6k |
| system prompt | 11k |
| memory files | 9.6k |
| **skills** | **5.9k** |

**These six rows sum to 159.0k against a stated total of 157.3k — a 1.7k gap
this record cannot resolve, and does not smooth over.** `@codex` R3 caught it.
The gap is too large for the displayed precision to explain as rounding, so the
rows are **not** provably exclusive components of one snapshot: either two
categories overlap, or a row was read a moment apart from the total. Reported as
he reported it, with the discrepancy named. **Consequence for use:** the
*proportions* are safe to reason about (skills are a small single-digit
percentage however the 1.7k is distributed), and any *derived subtraction* on
individual rows is not.

`REVIEWED`, and it is the sitting's sharpest observation: **skills are not what
consumes the context.** At 5.9k they are under 4 % of the total, and the figure
did not move across the sitting's two readings. The growth is in *messages* —
repository reads, tool outputs, and accumulated reasoning. The direct
consequence: **a skill can cost several thousand tokens and still pay for
itself many times over** if it prevents an agent re-reading or re-deriving tens
of thousands of tokens of procedure.

`REVIEWED`, a second distinction worth keeping for future benchmarking — **with
one boundary the sitting blurred and this record does not.** The +87.6k splits
into **~58k for the six reads _plus the first live surfaces_** and **~30k of
further operational investigation**. The first checkpoint is a *combined* one:
by the sitting's own description it covers the mandatory reads **and** initial
live-surface reads, so **the ~58k is not the six reads' cost and must never be
quoted as it** (`@codex` R3 — the downstream index and directive rows made
exactly that slip and are corrected). **No clean post-six-read checkpoint was
taken**, so the boot path's isolated cost is currently unmeasured; taking that
reading is cheap and is the obvious next experiment. What the ~30k covers:
live PR state, owner comments, the
activity records, the held execution packets, the running review round, CI and
gate output, the shallow-clone condition, owner-gated questions, and
record-versus-live discrepancies. Only the first half is what "read the boot
documents" means; the second half is what makes the session able to act.

**His prior was correct.** `OWNER`: he opened the follow-up session saying the
answer was *"approximately 150K like I already assumed"* — the measurement
landed at 157.3k against an assumption of ~150k.

## 2 · The ruling — broad boot context is a product requirement, not overhead

`OWNER`, and this is the load-bearing paragraph of the whole sitting. The
assistant had just proposed treating the 150k as an optimization target. He
declined:

> *"this booting context does not seem weird to me nor bothers me, what this
> currently gives me is an agent that knows what's going on without the need
> for me to explain everything again. And even if broad context isn't always
> necessary, I do think it's pretty usefull that all my agents are aware of
> certin things that are happening or have happened etc"*

And on what that memory is worth to him:

> *"the memory my agents have, which also allowed you to be a part of all the
> knowledge, is the most valuable thing we have now"*

`REVIEWED`, accepting the correction and restating the goal:

> *"I would not make 'minimize context' the goal. The better goal is: maximize
> useful shared context, minimize duplicated or mechanically derivable
> context."*

— and, in the sitting's own words, *"for your estate, I would consider shared
situational awareness one of the product requirements of the agent operating
environment, not overhead to eliminate."*

`DERIVED`, and this is why the row matters beyond the sitting: **this bounds
OD-17.** OD-17 makes cleanup the priority with *agent legibility* as its bar,
and the tier vocabulary in [`MAP.md`](../MAP.md) as its instrument — cut
RECORD-tier bulk out of read paths, never CORE-tier detail. A future session
that met the 157.3k figure without this ruling could reasonably have read it as
evidence that the CORE reads are themselves the bulk to cut. They are not: the
owner has now said the cost buys the thing he most values, and that the six
reads are working as designed. **Token count is not a defect. Duplicated,
stale, or mechanically derivable context is.**

## 3 · His context operating policy — the session-length habit, stated

`OWNER`, verbatim, and it has never been recorded anywhere in this estate:

> *"most of my sessions end at about 500-800K context after a large task, and
> for a small or medium task most sessions reach about 300-500K, which is
> perfect right now. If a session reaches 750K or more it automatically
> compacts, which also uses a lot of usage sometimes, so I prefer to just keep
> a session going untill about 500K before starting a new session with the
> continuation prompt. This has worked really well so far"*

So the working shape is: **~150k informed orientation + ~250–350k of active
work = a controlled handoff at ~500k**, taken deliberately *before* the
platform's automatic compaction at ~750k can take it for him.

`REVIEWED`, on why that ordering is the point rather than a detail:

> *"your continuation prompt is doing the compression deliberately, before the
> platform is forced to do it automatically. That gives you control over what
> survives"*

— decisions, rejected approaches, open questions, verified live state, the
current next step, repo pointers, acceptance criteria — *"instead of relying on
an opaque compaction process to decide which details matter."* The sitting
recommends treating this as **a first-class estate method, not a personal
habit**, while explicitly declining to fix `500k` as doctrine, *"because model
behaviour and context economics can change."*

`DERIVED`: this estate already ships the mechanism — the `continuation-prompt`
skill — and what it has never carried is a **trigger condition**. The skill
says how to hand off; nothing says *when*. That is the gap this section closes,
and it is the same shape as every other gap the OD-24 round has been
classifying: not absent, **unrouted**.

**The plan reasoning, also `OWNER`, also unrecorded until now:**

> *"I do have the x20 plan right now, not even really for the weekly usage but
> more because the x5 plan has really low 5 hour usage and that makes it nearly
> impossible to run a decent fable 5 session. and for a lot of things,
> especially planning and reviews I do prefer fable right now"*

`DERIVED`: the binding constraint on his workflow is **burst capacity inside
the 5-hour window**, not weekly allowance — he reported ~50 % Fable-5 usage and
~65 % global usage with three hours left before the weekly reset. Any future
estimate of what a plan or a workflow costs him should be sized on
uninterrupted-session length, not on monthly totals. `NOT-VERIFIABLE` from
here: no session can read his subscription telemetry.

## 4 · The design framing the sitting produced

`REVIEWED` throughout — a proposal, not a decision, and nothing below is
owner-ratified.

**The optimization target it proposes** is not a smaller boot but a *separated*
one: *"Separate procedural knowledge from project truth, then only retrieve the
project truth required for the current task."* The sitting's own split of what
this session had to learn:

| method — belongs in reusable skills/mechanisms | project truth — must be retrieved |
|---|---|
| how to orient · classify records · handle stale state · inspect PRs · interpret born-red · deal with gate telemetry · distinguish owner decisions · close and land work | what fleet-manager currently contains · what is currently happening · what the current task touches |

**The four layers**, which is the most reusable thing in the sitting:

```
BOOT             "You know the estate and what's happening."
SKILL            "You know exactly how to perform this class of work."
REPO ROUTE       "You know the specific product truth relevant to this task."
TOOLS/CHECKERS   "You can prove you followed the method."
```

**What it says to keep eagerly loaded** — estate purpose, current priorities,
major recent decisions, active work, important constraints, cross-repo
relationships, known traps — *"can prevent an agent from making a locally
reasonable but globally wrong decision"*. **What it says to load on demand** —
full implementation rules, long historical narratives, deep subsystem
architecture, specialized APIs, detailed procedures, large test inventories.

**What it names as actual waste**, as distinct from size: repeatedly re-reading
the same procedure; carrying obsolete historical detail; tool output that could
have been summarized deterministically; duplicate rules; giant subagent results
copied back verbatim; and compaction-triggering churn.

`DERIVED`: three of those six are things this estate can already measure on
itself, and one of them — *"giant subagent results copied back verbatim"* — is
a live risk in the `delegate-read` path.

## 5 · The procedure gap the experiment exposed live

`MEASURED` for the mechanical half — running `python3 bootstrap.py check
--strict` appends to `.substrate/guard-fires.jsonl` and prints *commit the delta
with your session; do not revert*, reproducible on any tree — and **the session's
own committed record** for the behavioural half, which is a fact about one
session rather than a re-runnable one. This is the sitting's second
deliverable. The session hit a genuine tension: running the repository's
required gate **modified telemetry**, which activated the repository's standing
instruction that the delta must be committed — inside a task the owner had
framed as read-only orientation. The session first treated *"orientation only"*
as a reason to withhold action and recommend instead, and reversed only after
the `Stop` hook's git check surfaced the uncommitted change.

`REVIEWED`, the sitting's reading of it — *"almost a perfect demonstration of
why your proposed skills matter"* — with the rule it proposes standardizing:

```
READ-ONLY ORIENTATION
↓
Do not make product changes.

BUT

If mandatory diagnostic tooling creates
expected bookkeeping/telemetry:
→ follow the repository's prescribed cleanup/landing route.
```

*"Then every model gets the same answer instead of having to reason through
that tension anew."*

`DERIVED`: this is a textbook case for [`intent.md`](../intent.md) § 4 — the
rule already exists (the gate prints *commit the delta with your session; do
not revert* every single run) and it still did not bind, because it arrives as
a line of gate output rather than as an instruction at the moment the session
is deciding what its task permits. **The fix is a mechanism at that moment, not
another statement of the rule.** Which is exactly the classification the OD-24
review round is built to produce, and this belongs in its gap set as
**unrouted**.

## 6 · What this record does NOT decide

- **No packet GO.** OD-23's hold on plan execution stands; nothing here lifts it.
- **It does not authorize a boot-path trim, and it does not forbid one.** § 2 is
  a ruling about *why* the context is spent, not a freeze on the read path.
  Anything that changes what a cold session loads is still the roadmap's and the
  program's to decide.
- **It builds no skill.** Whether the orientation procedure of § 5 becomes a
  skill, a hook, or kit text — and whether it lives in fleet-manager or
  substrate-kit — is exactly what the **promotion rule** governs (the roadmap
  § 6), and it is round work, not a decision to take here.
- **`500k` is not doctrine.** § 3 records his habit and the reasoning behind it.
  The sitting itself declined to fix the number, and so does this record.
- **The "AI Mapper" is his product idea, not an fm decision.** The sitting
  proposes it should eventually evaluate a subscription on weekly capacity,
  5-hour burst, model-specific caps, context ceiling, compaction behaviour and
  usable uninterrupted session length. Recorded because it is where his
  reasoning was heading, not because anything here acts on it.
- **The sitting's framing is not owner-ratified.** §§ 4 and 5 are `REVIEWED`.
  Only § 2's ruling and § 3's policy statement are his.
