# 2026-08-06 · hub — the restate requirement moves into the prompt

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-06 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: the owner watched a session open from one of this repo's own
handoff prompts and noticed it never said what it thought the job was. He named
the fix precisely — *"either link directly to the document that mentions it, or
directly request it in the prompt"* — and the two options are not equivalent.

## What the recording showed

The owner supplied a screen recording; Gemini on Vertex transcribed it from
inline video (7.3 MB, no frame extraction, no GCS bucket). The session's entire
first substantive response:

> *"I'll start by getting oriented — checking the environment, then landing
> #602 as instructed."*

A statement of first **action**, not of **understanding**. Nothing in it the
owner could have corrected, so his cheapest intervention point was spent on an
announcement.

**That session is good, and this matters for reading the finding correctly.**
The same transcript shows it catching `#602` already merged and flagging the
contradiction with its own handoff rather than trusting it; catching that the
handoff's *"zero required status checks"* claim is **stale for substrate-kit**
(`kit-quality` is required); and measuring fleet-manager's `check --strict`
output at **89 lines of which 76 — 85 % — are non-exit-affecting advisory**.
This is not a careless session. It is a strong session that skipped one step,
because the step lived somewhere it had no reason to look.

## Why linking loses

`intake` § RESTATE step 2 has required exactly this for a long time: *"state
back, inline in your first substantive response (never as a separate blocking
question), the fuller picture you built from the ask."* It was documented and it
still did not happen — **twice**, since this repo's own session skipped it the
day before while the skill sat in the same tree.

**`intake` binds a session that invokes `intake`.** A handoff prompt is consumed
by a session that has invoked nothing yet: it reads the prompt, then acts. A
pointer is precisely the mechanism that failed three times on 2026-08-05, each
time against the session that authored the rule.

So the requirement now travels **inside the artifact the reader actually
opens**, and the link stays in the skill for whoever writes the prompt.

## What landed

| File | Change |
|---|---|
| `.claude/skills/continuation-prompt/SKILL.md` | `BEFORE YOUR FIRST TOOL CALL` block in the emitted template; new § 4a with the rationale, the incident, and the two traps |
| `.claude/skills/implementation-prompt/SKILL.md` | same block in its template; points at § 4a rather than restating it |
| `menno420/substrate-kit#578` | the same block in `_CONTINUATION_PROMPT_BODY`, so every adopter repo inherits it |

The two traps, because the block is worthless if they are missed: **a plan is
not an understanding** (*"I'll verify state, then classify the checkers"*
restates the prompt — what is wanted is what the prompt did *not* say), and **it
is not a question** (stated inline, then proceed; blocking for approval spends
the owner's attention instead of saving it).

## Verification

- Kit side: `python3 -m pytest` → **2116 passed, 1 skipped**;
  `test_committed_bootstrap_is_current` **correctly failed first**, catching
  that `dist/bootstrap.py` had not been regenerated from the edited source;
  `python3 dist/bootstrap.py check --strict` → **exit 0** after the card flip.
- Hub side: recorded at close below.

## Honest nulls

- **Unmeasured whether it changes behaviour.** One incident motivated it; no
  session has yet been observed receiving a prompt that carries the block.
- **Adopter repos do not have it until they upgrade.** fleet-manager was edited
  directly; every other repo carries the old body until a distribution wave.
- **`implementation-prompt` is hub-local**, not in the kit, so the two skills
  stay in sync only by hand.
- **The 85 % advisory-noise figure is that session's measurement, read off a
  video** — `MEASURED-PRIOR`, not re-derived here. It corroborates § 5 of
  `docs/findings/2026-08-05-foundation-continuation.md`, which predicted exactly
  this shape without putting a number on it.

## ⟲ Previous-session review

Yesterday closed on *"this estate instruments execution and does not instrument
judgement."* This is the first repair aimed squarely at the judgement half — the
restate block exists so the owner can correct a session's **aim**, which is the
one thing no gate can check. It is also the fourth consecutive fix whose lesson
is placement rather than content: the rule was already written, already correct,
and already in the repo.
