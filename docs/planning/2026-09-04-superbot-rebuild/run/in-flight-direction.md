# In-flight owner direction — caught by the BASE re-read, mid-run

> **Status:** `reference` · recorded 2026-09-04T12:55Z, **while this session's
> review fleet was still running.** This is exactly the case `CONTRACTS.md`
> § BASE exists for, and it fired: a change landed on a surface this review
> depends on, between launch and synthesis.

## What happened

A **parallel** fleet-manager session opened
[#1021](https://github.com/menno420/fleet-manager/pull/1021)
(`claude/spider-bot-ai-ops-sthix0`, head `864c36ad`, opened 2026-09-04T12:18Z)
recording a **live owner statement made the same day**. At the time of writing it
was **open, not merged** at the time of writing — so everything below was *in
flight*, and the synthesis step was required to re-check whether it landed,
changed, or was rejected.

> **RESOLVED 2026-09-04T17:1xZ, at the base re-read this file demanded.**
> #1021 **merged** as `104c2e5`, and the decision is now stamped in
> [`../../../decisions.md`](../../../decisions.md) as **`[D-0042]`** — its
> permanent home. **Nothing below changed on the way in**: the statement this
> file recorded is the statement that landed, so every use the plan package
> makes of it stands as written. This file remains the *record of it arriving
> mid-run*; the ledger is where it lives. The standing action at the bottom of
> this file is therefore discharged.

Two other sessions are working this repository concurrently: #1021 above and
[#1020](https://github.com/menno420/fleet-manager/pull/1020) (the estate truth
baseline / `estate` seed manifest). This plan touches neither's files.

## The statement — `OWNER`, live, 2026-09-04, verbatim

> *"Spider Bot exists to manage the Slingy Spider server and help during testing
> of the game. It should become a reliable automoderator with heavy AI
> integration. People should be able to talk naturally to it for guidance,
> complaints, bugs, feedback and improvement ideas. Those reports should become
> durable, easy for the developer to find and act on — preferably through GitHub
> or an equally clear developer-facing system."*

Recorded as `[D-0042]` in that PR, with `docs/repos/spider-bot/intent.md`
rewritten from DRAFT to ANSWERED and the 2026-08-21 game-community plan given a
`NARROWED 2026-09-04` banner.

## What it changes for THIS review — four things

**1 · `OQ-GCB-REVIEW-SCOPE` is answered, by his own words rather than by a pick
from the queue's A/B/C/D menu.** The review-oriented bot is *the
testing-and-feedback loop, plus moderation of the server that runs it.* That
question had been the named blocker on re-sequencing the GCB roadmap since
2026-08-23.

**2 · The GCB plan's multi-game headline is narrowed — for `spider-bot`, and
not for the successor.** The PR is careful about this and so is this plan:
`[D-0042]` states it *"does not supersede his 2026-08-28 'one real well
functioning bot … without architectural debt' direction — that one governs the
shape this input must be in; this one governs what it is for."* So **whether the
eventual single bot is multi-game, or a second instance of a one-server tool,
remains open** and is carried into [`../12-owner-decisions.md`](../12-owner-decisions.md)
as a real decision rather than assumed either way.

**3 · The AI authority contract is now owner-derived, and this plan adopts it
rather than proposing its own.** From `[D-0042]`, refining rather than deleting
spider-bot's invariant 5 (*"the AI never performs side effects"*):

```
Discord event → deterministic pre-check → optional AI analysis
  → TYPED, SCHEMA-VALIDATED VERDICT → deterministic policy engine
  → permission/risk gate → typed operation → Discord API → audit + case record
```

with two rules attached: *free-form prose is never parsed into a moderation
action*, and *invalid or incomplete model output means no automatic action.*
**The AI supplies judgement; deterministic code supplies authority.**

This composes exactly with what the evidence already pointed at — `superbot`'s
production AI surface is 36 catalogued tools of which **one** writes, through the
audited mutation seam (I-11). The owner's pipeline and the production bot's
proven shape are the same design, arrived at independently. That is the
strongest single warrant in this plan for an AI section, and neither half is
this session's invention.

**4 · Three further design rules arrive with it**, each `OWNER`-derived in that
PR and each carried into the successor's product definition:

- **Conversation is a first-class route, not a fallback.** Buttons and forms
  stay; nobody needs to know a command or a form name. **One intake
  implementation, many entry points.**
- **Reports are durable first and projected second.** A confirmed report enters
  durable private storage with a stable id **before** any GitHub call; GitHub is
  a projection and a sink, never the primary store, and never a place private or
  interpersonal material is published.
- **New autonomous moderation starts in shadow mode** with a staff review
  surface — *"because `reliable` is his word and an unfalsifiable classifier
  cannot earn it."*

## The ranking number this plan inherits

Also recorded there and unchanged: Google will not let Slingy Spider leave
closed testing until **12 testers stay opted in for 14 continuous days.** It is
the estate's one hard external clock, and it ranks work: *a capability that does
not serve server operations, the testing assistant, the AI community assistant,
AI-assisted moderation, or that number, is later — not wrong.*

## The method note, because it is the point

This review's launch snapshot was taken at 11:52Z. The statement above was
recorded at 12:18Z, and this session found it at 12:55Z **only because the
contract sheet scheduled a base re-read and because a parallel PR listing was
part of it.** Had the plan been published against the launch pins alone it would
have carried a product definition contradicted by an owner statement made the
same morning — the precise failure `fleet-preflight` § 6 was written from.

**Standing action for the synthesis step — ✅ DISCHARGED 2026-09-04T17:1xZ.**
#1021's state was re-read before publishing: **merged** as `104c2e5`, unchanged
in substance, and the decision is stamped as `[D-0042]` in the estate ledger.
The plan package links back to *this* file rather than restating the id, under
the one-home rule; the ledger entry and the rewritten `intent.md` are the
canonical text.
If still open, cite it as in-flight and quote the owner statement, which stands
on its own under the estate's precedence rule regardless of the PR's fate.
