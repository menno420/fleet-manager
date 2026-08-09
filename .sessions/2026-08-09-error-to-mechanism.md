# 2026-08-09 · hub — turn the error ledger into mechanisms that fire at the moment

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · feature build — score fm #830's 13 errors against
  "could a hook or skill have caught this at the moment?", then build the ones
  that can

Time: 2026-08-09 · venue: owner-live hub chat · branch
`claude/intent-architecture-phase-2-ntsffd` (restarted from `1f620a8` = `origin/main`
after fm #830 merged)

💡 Session idea: **the estate could guard the moment before an action, the
prompt, and the finished reply — and had nothing at all for the moment *after* an
action succeeded.** Three `PreToolUse` hooks, one `Stop`, one `UserPromptSubmit`,
zero `PostToolUse`. That gap is not stylistic: a whole class of defect is
*only* knowable once the change lands. "Did this edit leave the old claim
standing somewhere else?" cannot be answered before the edit, because before it
the old claim is still in the target by definition. The estate had been asking
that question in review, hours later, when the reply was already written.

Layer-2 handoff: null (fleet-manager itself; no satellite repo attached)

## Previous-session review

⟲ fm #830 landed the Phase 2 intent map, the prompt-route bar, and an audit of
the intent-architecture thread. Its most useful output was not the slice but its
**13-error ledger with catcher attribution**: 0 caught by documentation being
available, 9 by adversarial instruments. The owner read that and drew the right
conclusion — *"nearly all of them have been caught without my attention, so this
is already a good example of the system working"* — and asked the follow-on this
session answers: **which of those 13 could a hook or skill have caught at the
moment, and what do the ones that already did tell us about how to build more.**

## What is about to happen

1. **Score all 13** against a single question: is there a moment, and is the
   defect decidable by a machine at that moment?
2. **Build the ones that pass** — as hooks firing at the moment, not checkers
   firing at gate time. A gate-time check is a reviewer; a hook is a guard.
3. **Record the ones that do not pass, with the measurement that says so** —
   including one check that was built, tested against its own motivating case,
   and **failed it**.

## Verification

At close: `python3 bootstrap.py check --strict`, both checkers directly, real
exit codes, each on its own line. Every new check tested **in both directions**
and, where the defect is historical, **replayed against the real pre-fix state
from git** rather than a synthetic fixture. Codex review requested while this
card is born-red.

## This session's errors, catcher-attributed

Continuing fm #830's numbering, because it is the same day and the same author.

| # | error | caught by |
|---|---|---|
| 14 | **evaluated one family of mechanism and concluded about the space** — declared paraphrased propagation *"has no mechanical catcher"* having tried only text matching (whole-line, then shingles). **Anchors were never considered, and `bootstrap.py:9308` already runs one** — it flags a decision id cited from more than one doc, is paraphrase-proof by construction, and **fired on this very session** (the Gemini paid-key decision, in the same command output being read while the claim was written) — **and fired again on the paragraph documenting it**, because naming the id made the finding a second citation site | **the owner-review Stop hook**, asking whether anything but text matching had been evaluated |
| 15 | **registered a hook on every file change without measuring its latency** — `PreToolUse` on `Write\|Edit\|MultiEdit` and `PostToolUse` on `Edit\|MultiEdit` is the hot path, and the cost was not measured until asked for | **the owner-review Stop hook**, same round |
| 16 | **overstated the counter-example in the direction of the point** — called `check_stamp_discipline` *"exactly the paraphrase-proof propagation check declared impossible above"*, having read its **docstring** (`:9308`) and not its body (`:9307`). It is a **duplication** check: it forbids a decision id from having a second home, rather than detecting divergence between two copies. The correction is an improvement — *prevent* beats *detect*, and the estate already chose it | **the owner-review Stop hook**, fourth round, asking what exact check lives at that line |

**#14 is the sharpest error of the two days**, because it is the session's own
subject turned on itself. The whole file argues that *availability is not
retrieval*; the counter-example to its central claim was **in the output of the
command being read at the time**, and was not retrieved. It also produced a
*worse* recommendation than the evidence supported: "un-mechanizable" closes a
question that is actually open and promising.

**#14 and #16 are one arc, and it is the useful one.** #14 was a claim made
without evaluating a whole family of solutions; #16 was the correction to it,
overstated in the direction of the point being made. Both were caught by the same
instrument asking the same question — *what did you actually read?* — and the
second answer is better than the first: the estate does not detect propagation
drift, it **prevents second homes**, and the gap is that only decisions carry an
id to cite. Every propagation failure in fm #830 was a retyped **measurement**,
and measurements have no anchor.

**#15 measured out fine** — ~41 ms for the `PreToolUse` checks, ~82 ms median /
137 ms max for the `PostToolUse` grep path, and ~41 ms of every figure is Python
interpreter startup, identical in the case that does no work. Acceptable. **The
ordering was still wrong**, and "it turned out fine" is not the same as "it was
checked": a hook on every edit earns a measurement before registration, not after
a reviewer asks.

## A process note — do not promise a frozen head

Told Codex at `1428cd4`: *"final, no further pushes until you answer."* Then
pushed twice, because the owner-review hook surfaced errors #16 and the arc note
in the replies that followed.

**The promise was unkeepable when it was made, and predictably so.** The
owner-review hook fires on *every* reply; a session that is still talking to the
owner is still generating changes. Promising a frozen head while an adversarial
reviewer of your prose is running is promising that reviewer will find nothing.

fm #830 recorded the opposite trap — pushing *after* requesting a review — and
this is its overcorrection. **The honest form of the commitment is "I will
re-request after any further push," which is a thing a session controls.** No new
mechanism proposed; the fix is to stop writing a sentence that is not true when
written.

## Close-out

**Built:** `.claude/hooks/change_guard.py` (checks A, B, C), `capability-probe`
step 3b, and the thirteen-error scoring in
[`../docs/findings/2026-08-09-error-to-mechanism.md`](../docs/findings/2026-08-09-error-to-mechanism.md).

**The honest scoreboard for the mechanisms this session shipped:** two verified
against the real history that motivated them (A, B), one that **fails its own
motivating case and says so** (C), and one design direction that was wrongly
closed and is now reopened (anchored claims, § 4b).

**Verification** — real exit codes, each command on its own line, never `$?`
after a pipe. Every check tested in both directions; where the defect is
historical, replayed against the real pre-fix state from git rather than a
fixture. Latency measured, 10 runs per path.

**Left for the owner, unchanged from fm #830:** the kit upgrade is next by his
decision A — and check A now warns whoever runs it that `intake` must be
re-applied afterwards, which is the P1 turned into a guard.
