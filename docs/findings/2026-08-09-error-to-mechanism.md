# Thirteen errors, scored against "could a machine have caught this at the moment?"

> **Status:** `reference` · 2026-08-09
>
> The owner's question, after reading fm #830's error ledger: *"can you find out
> if any of the errors could have been prevented through hooks or skills that
> would have activated right before or after you made them. And those that
> already did should be an example of how this should be made."*
>
> His premise is the finding underneath it — **nearly every error that day was
> caught without his attention.** This scores all thirteen against one question
> and builds what passes.
>
> Certainty tags per
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).
> Verdicts are `REASONED`; the two built checks and the one **failed** check are
> `MEASURED`, each replayed against the real pre-fix state from git.

## 1 · The test a mechanism has to pass

Two conditions, and most ideas die on the second:

1. **There is a moment** — a tool call, a write, a reply — where the defect
   already exists and the action has not yet had its effect.
2. **It is decidable there** — from the text in front of the machine, without
   knowing what the author meant.

*"Be careful about X"* fails both. It has no moment and nothing decides it. That
is the whole content of the 116-statements-0-catches measurement
([`2026-08-08-why-rules-dont-bind.md`](2026-08-08-why-rules-dont-bind.md)):
statements are not mechanisms, however many there are and however true.

## 2 · The templates — what already worked, and the one property they share

| instrument | caught | why it works |
|---|---|---|
| **the Edit tool's exact-match** | #2 | **The ideal shape.** No judgement, no config, no way to argue with it: a composed quotation simply fails to apply. Cost of a false positive is one retry. |
| **the owner-review `Stop` hook** | #7 #8 #9 #10 #11 | Reads **the reply**, which no diff-scoped tool ever sees — and four of its five catches were claims that existed *only* in the reply. |
| **Codex** | #6 #12 #13 | Reads **the tree**, and does not share the author's beliefs about it. Both defects it found had survived the author's own re-reading. |
| `read_before_write` | 0 | Fired twice, **both false positives** — on `claude.ai` and on `2.2`, neither a file path. It guards writes, not claims, and its precision is the thing to fix before its coverage. |

**The property they share: none depends on the author noticing.** Each is either
mechanical, or a different reader. Every mechanism that failed this session was
one that required the author to remember something — including a ⚠ warning
**sixty lines from his own edit** (#13) and a defect he had **repaired four hours
earlier** (#12). Proximity is not retrieval. That result is now four sessions old
and has never once come out the other way.

## 3 · All thirteen, scored

| # | error | verdict |
|---|---|---|
| 1 | probe returned `0`, nearly recorded a feature as absent | **skill step** — positive control (§ 5) |
| 2 | composed a quotation | **already caught** — Edit exact-match |
| 3 | checked a spec's field *names*, concluded about field *values* | **no moment** — nothing tells a machine which dimensions of a spec matter |
| 4 | quoted a `REVIEWED` distillation as owner-verbatim | **buildable, not built** — a checker could resolve owner-attributed quotes against `OWNER`-labelled sections; narrow and repo-specific |
| 5 | stated an elapsed time from the wrong start point | **skill step** — never state a duration you did not compute |
| 6 | corrected a claim in one file, left the copy in another | **NOT mechanizable — measured, § 4** |
| 7 | called agent-quoted fragments "owner messages" | **already caught** — `Stop` hook |
| 8 | measured an absence here, claimed a presence there | **skill step** — positive control (§ 5) |
| 9 | tagged an invented mechanism `MEASURED` | **buildable, not built** — require a command/path/output near a `MEASURED` tag. False-positive risk is real, and it would be a new red condition, which is the owner's call |
| 10 | stated counts without running the count | **already caught** — `Stop` hook. No hook can know whether a number was computed; the reply-reader can ask |
| 11 | described a file without opening it | **already caught** — `Stop` hook. `read_before_write` covers this for *writes*; the gap was *replies* |
| 12 | broke a markdown table so six rows rendered as text | **BUILT** — check B, § 6 |
| 13 | amended a kit-named skill that the next upgrade reverts | **BUILT** — check A, § 6 |

**4 already caught · 2 built here · 3 skill steps · 2 buildable and deliberately
not built · 1 with no moment · 1 measured un-mechanizable.**

## 4 · The one that was built, tested, and failed — keep this

Propagation (#6) was the obvious candidate: a `PostToolUse` hook that takes the
text an edit replaced and greps for surviving copies. It was built (check C), and
then **replayed against both real propagation failures from fm #830**:

| case | what the two copies said | result |
|---|---|---|
| error #6 | roadmap *"false-negative rate of 1 in 21"* · ledger *"a 1-in-21 false-negative rate"* | **SILENT** |
| round-2 #2 | the pre-fix `intake` line at `28ecc2c` vs three other files carrying the claim | **SILENT** |

Both were **paraphrases**, and no exact matcher reaches a paraphrase. Whole-line
matching failed first; word-shingles failed too, for the same reason.

**The check ships anyway, on a different and honestly-labelled class** — verbatim
survivors, of which the repo's markdown held **441 duplicated 9-word shingles**
when this was written. But **a clean run is not evidence a correction
propagated**, and the paraphrase class currently has *no* mechanical catcher.
Codex found both, by reading for meaning rather than for strings.

**That is the most useful thing in this file.** The reflex on seeing a repeated
error is to build a checker for it; here the checker was built, aimed at its own
motivating case, and missed — and the only reason that is known is that it was
replayed against history instead of a fixture. **A mechanism that has not been
run against the error it was built for is a hypothesis.**

## 5 · The skill steps — one rule, two errors

Errors #1 and #8 are the same move: **a measurement showing nothing, read as
nothing being there.** #1 probed for a JSON key that does not exist, got `0`, and
was one sentence from recording that Phase 1's prompt route was missing — the
route exists, under a different shape. #8 found `ADVISORY_CENSUS` absent from this
repo and claimed it absent from a repo never opened.

**The rule: before recording an absence, run the positive control.** Confirm the
query finds a known-present instance, *then* trust the negative. One extra
command, and it converts "I found nothing" into "nothing is there" — which are
not the same sentence and were treated as the same sentence twice in one day.

Its home is [`capability-probe`](../../.claude/skills/capability-probe/SKILL.md),
which already owns *"before declaring anything impossible"* and is **fm-local**,
so nothing reverts it — unlike the 14 kit-named skills (§ 6, check A).

Error #5 has no home yet and does not earn a skill of its own: *never state a
duration, count or rate you did not compute in this session.* It is the same
class as #10, and the `Stop` hook already catches that class reliably — four
times in one session — so a second mechanism would be redundant before it is
useful.

## 6 · What was built — `.claude/hooks/change_guard.py`

Three checks, all advisory, all fail-open, all **silent unless they have
something**. Noise is the enemy: `check --strict` already prints 94 advisory
lines with its verdict at line 92, and a guard that cries wolf is worse than none.

| | event | catches | tested |
|---|---|---|---|
| **A** | `PreToolUse` on Write/Edit | amending one of the **14 kit-named skills**, which the documented copy loop reverts at the next upgrade | fires on `intake`/`session-close` as already-listed, on `analysis`/`quality-gate` as not-listed, **silent** on fm-local `owner-brief` |
| **B** | `PreToolUse` on Write/Edit | markdown rows with no delimiter above them, which GFM renders as literal pipe text | **replayed against the real defect** — the layer-2 card at `d7287ea` — and reports exactly its 6 orphan rows at L75–79 and L96 |
| **C** | `PostToolUse` on Edit | verbatim survivors of replaced text | fires on real duplication, silent on unique text, **and silent on both cases it was built for** (§ 4) |

**C sits on an event this estate had never used.** Before it: three `PreToolUse`
hooks, one `Stop`, one `UserPromptSubmit`, and **nothing after a successful
action** — so no mechanism could say *"that worked, and here is what it implies."*
Propagation is only knowable after the edit lands; before it, the old text is
still in the target by definition.

A detail that generalises: **check A's first version was wrong in a way only a
test showed.** It asked whether the skill was named anywhere in
`docs/SKILLS-local.md` — and every skill is, in that file's 27-row roster, so it
reported "already handled" for skills with no amendment at all. Caught by running
it against `analysis`. The check now scopes to the ⚠ re-apply region.

## 7 · The rule this leaves behind

**Score the moment, not the mistake.** A recurring error is not automatically a
mechanism; it becomes one when a moment exists where a machine sees the defect
and the author does not. Of thirteen errors, six had such a moment, four already
had a mechanism watching it, and three did not.

And the corollary, learned the hard way in § 4: **replay a new mechanism against
the history that motivated it before believing it.** Two of the three checks here
pass that test. The third does not, and says so.
