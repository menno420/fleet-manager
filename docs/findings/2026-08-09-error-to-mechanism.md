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
>
> **§ 4b is a correction to § 4 and should be read with it** — the "un-mechanizable"
> verdict was reached by evaluating one family of mechanism and concluding about
> the space, while the counter-example was running in the same command.

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
| 6 | corrected a claim in one file, left the copy in another | **no text-matching catcher** — measured, § 4. But the **anchor** family was never evaluated and this repo already runs one (§ 4b), so this is an open design question, not a wall |
| 7 | called agent-quoted fragments "owner messages" | **already caught** — `Stop` hook |
| 8 | measured an absence here, claimed a presence there | **skill step** — positive control (§ 5) |
| 9 | tagged an invented mechanism `MEASURED` | **buildable, not built** — require a command/path/output near a `MEASURED` tag. False-positive risk is real, and it would be a new red condition, which is the owner's call |
| 10 | stated counts without running the count | **already caught** — `Stop` hook. No hook can know whether a number was computed; the reply-reader can ask |
| 11 | described a file without opening it | **already caught** — `Stop` hook. `read_before_write` covers this for *writes*; the gap was *replies* |
| 12 | broke a markdown table so six rows rendered as text | **BUILT** — check B, § 6 |
| 13 | amended a kit-named skill that the next upgrade reverts | **BUILT** — check A, § 6 |

**4 already caught · 2 built here · 3 skill steps · 2 buildable and deliberately
not built · 1 with no moment · 1 open design question** (#6 — see § 4b; this row
read *"measured un-mechanizable"* until owner-review asked what had actually been
evaluated).

**Read across the rows rather than down them: 8 of 13 have a machine-decidable
moment** — the 4 already watched, the 2 built here, and the 2 buildable-but-unbuilt,
because *buildable* means the moment exists and only the building was declined.
3 need a human procedure, 1 has no moment, 1 is an open design question. **Do not
compress this to "six"** — a reply did, by counting only the rows with a
mechanism *shipped*, which silently reclassifies a deliberate trade-off as an
impossibility.

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

### 4b · The conclusion above was overstated, and this repo already holds the counter-example

**Corrected 2026-08-09 after owner-review asked whether anything but text
matching had been evaluated. It had not.** This file said paraphrased propagation
*"has no mechanical catcher."* The honest claim is narrower: **no
text-matching catcher — and one whole family of mechanism was never considered.**

Anchors. Give a claim a stable id, cite the id wherever the claim is repeated,
and propagation becomes decidable **regardless of wording**, because the checker
follows the id rather than the prose.

**The estate already runs one, and it fired on this very session.**
`bootstrap.py:9308` flags *"a decision id cited from more than one doc outside
the ledger — stamp each decision at one home"*, and it caught the Gemini
paid-key decision cited from both this file and `providers/gemini.md`. That is
exactly the paraphrase-proof propagation check declared impossible three
paragraphs above, running in the same command whose output was being read while
the claim was written.

**And it fired again on this very paragraph.** Naming the decision id as evidence
made this file a second citation site, so the check reported it — which is the
cleanest possible demonstration that anchors work: the mechanism caught a
propagation it had no way to recognise by wording, in the document arguing that
such a mechanism does not exist. The id is now described rather than stamped.

**Read precisely, it is not the check this paragraph first called it — and the
difference points somewhere better.** `check_stamp_discipline` lives at
`bootstrap.py:9307`; the line cited above is its docstring. It walks
`config.docs_root`, skips the ledger, matches `_LED_ID_RE = re.compile(r"\bD-\d{3,}\b")`
(`:9043` — **decision ids only**, verified rather than inferred), and flags any id
appearing in **more than one** document.

That makes it a **duplication** check, not a **divergence** check. It does not
notice when two copies of a claim drift apart; it caps how many may exist —
**one citing document is permitted, the second is flagged.** Its own rationale
says so: *"a second citation is drift risk — when the
decision changes, one of the two goes stale."*

**And its reach is one tree of three.** `:9318` walks `docs_root.rglob("*.md")`,
called at `:24282` with `config.docs_root`, which defaults to `"docs"` (`:349`).
Citations in `.claude/` and `.sessions/` are **invisible to it** — the Gemini
paid-key id currently appears in `.claude/CLAUDE.md` and four session cards that
the check never scans. So the existing anchor mechanism is narrower than "one
home per decision": it is *one home per decision, within `docs/`*.

**Two strategies, and the estate already picked the stronger one:**

| | how it works | cost |
|---|---|---|
| **detect** | allow copies, notice when they diverge | needs to compare meaning — the thing text matching cannot do |
| **prevent** | allow exactly one home, so there is nothing to diverge from | needs an id, and a rule that copies cite rather than restate |

**Precisely, and it matters for what an anchor rule would have to say:** the
ledger is excluded by path (`:9317` resolves it, `:9319-9320` skips it), each
document's mentions collapse via `set()` (`:9326`), and the flag fires at
`:9330` only when **two or more non-ledger docs** cite the same id. So it *does*
separate the canonical definition from citations, and it does **not** reject a
second occurrence — it permits **exactly one** citing document and flags the
second.

**So the recommendation changes.** The fix for paraphrased propagation is
probably not a cleverer matcher — it is **capping the number of homes**, which is
cheap, decidable, and already proven here for decisions. What this repo lacks is
not the mechanism but the **anchors**: it stamps decisions (`D-NNN`) and nothing
else, so anything else restated in a second document is a retyping that can
drift.

**What was actually retyped — audited, 2026-08-09, after this file asserted it
without auditing.** Three propagation instances exist across the two PRs:

| instance | what was propagated | kind |
|---|---|---|
| fm #830 error #6 | *"a 1-in-21 false-negative rate"* | **measurement** |
| fm #830 Codex round-2 #2 | *"ten real owner messages"* — and the wrong part was *"real owner messages"*, not the count | **provenance claim** |
| the miss inside that fix | the same provenance claim, in the ledger row's opening sentence | **provenance claim** |

**A fourth instance, found by sweeping rather than by an instrument — and it is a
third kind.** After writing the row above, a `git grep` for every withdrawn
phrasing in this PR found the retired *"un-mechanizable"* verdict still standing
in **three** places: `docs/current-state.md` (a read-path doc), this file's § 4b,
and — worst — the shipped `change_guard.py` docstring, where the code's own
documentation still asserted the claim the code's own testing had retired.

So the propagated items across four events are a **measurement**, a **provenance
claim** (×2 events), and a **verdict**. Three different kinds, none of them
anchored, which is the argument: it is not measurements that need ids, it is
*any claim restated in a second document*.

**This one was caught by the author, and that is the only time that happened
today** — not by re-reading, but by running a grep for each retired phrasing. The
sweep took one command. Six re-readings of the same files had not surfaced it.

**One measurement and two provenance claims — not "every one a measurement",
which is what this file said.** The correction widens the argument rather than
narrowing it: the class that needs anchors is **any unanchored claim repeated
across documents**, and provenance statements turn out to be the more common
half. Note also that only **one of the sixteen numbered errors** is a propagation
failure; the other two were Codex findings recorded as dispositions, so "every
propagation failure today" was a generalisation over a set that had never been
enumerated. **Filed as error #17.**

### 4c · What would have to be anchored — the boundary this file did not define

`REASONED`, and **added only after owner-review asked for it.** § 4b argued that
*"any claim restated in a second document"* needs an id, which is unactionable as
written: taken literally it anchors every sentence, which is the
mandatory-infrastructure-everywhere move the promotion rule exists to reject.

The four instances suggest a boundary that is decidable in practice:

> **Anchor a claim if re-deriving it means redoing work.**

| anchor | do not anchor |
|---|---|
| a measurement (*"1 miss in 21"*, *"94 advisory lines"*, *"448 s"*) | operational state — the head SHA, whether CI is green, what a file currently contains |
| a count over a corpus (*"13 errors"*, *"14 kit-named skills"*) | anything the **live surface** answers directly |
| a verdict from a test (*"check C is silent on both cases"*) | narrative, argument, commentary |
| a provenance characterisation (*"agent-quoted fragments, not owner messages"*) | a pointer to where a claim lives |

**The line is cost of re-derivation, and it falls out of a rule the estate
already has.** Operational state does not need an anchor because *the live
surface always beats any doc* — a stale copy of it is self-correcting the moment
someone looks. A measurement has no live surface: nothing re-runs the count, so a
stale copy stands until a reader happens to doubt it, which today took four
adversarial rounds.

**Untested.** No anchor scheme has been designed, and the existing one covers
only `docs/` (above). This is the shape of the question, not the answer to it.

Anchoring measurements the way decisions are anchored is the design question
worth its own session. **Filed as error #16** — the first version of this
paragraph called the stamp check *"exactly the paraphrase-proof propagation check
declared impossible above"*, which overstated it in the direction of the point
being made.

**Filed as this session's error #14**, and it is the same shape as the rest:
evaluating one family of solutions and concluding about the space.

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

**Triggers and cost, `MEASURED` 2026-08-09** — asked for by owner-review, and it
should have been measured before shipping rather than after. Registered on
`PreToolUse` for `Write|Edit|MultiEdit` and `PostToolUse` for `Edit|MultiEdit`,
so it runs on **every file change a session makes**:

| invocation | median | max |
|---|---|---|
| `PreToolUse`, markdown write (A+B) | 41.6 ms | 50.2 ms |
| `PreToolUse`, kit-named skill edit (A) | 40.4 ms | 42.0 ms |
| `PostToolUse`, edit large enough for the shingle greps (C) | 81.9 ms | 137.2 ms |
| `PostToolUse`, edit below the shingle floor | 41.7 ms | 47.8 ms |

**~41 ms of every figure is Python interpreter startup** — the floor is identical
across all four, including the case that does no work. So the checks themselves
cost ~0 ms, ~0 ms, and ~40 ms; only C's `git grep` calls are measurable, and only
on edits big enough to shingle. Acceptable on the hot path, but **the ordering
was wrong: a hook on every edit should have its latency measured before it is
registered, not after someone asks.**

A detail that generalises: **check A's first version was wrong in a way only a
test showed.** It asked whether the skill was named anywhere in
`docs/SKILLS-local.md` — and every skill is, in that file's 27-row roster, so it
reported "already handled" for skills with no amendment at all. Caught by running
it against `analysis`. The check now scopes to the ⚠ re-apply region.

## 7 · The rule this leaves behind

**Score the moment, not the mistake.** A recurring error is not automatically a
mechanism; it becomes one when a moment exists where a machine sees the defect
and the author does not. **Of thirteen errors, 8 have such a moment** — 4 already
watched, 2 built here, 2 buildable and declined — while 3 need a human procedure,
1 has no moment, and 1 is an open design question.

*(This sentence said "six" until Codex flagged it P1 on fm #831, one section after
§ 3 had been corrected to 8. A summary that outlives the table it summarises is
the whole propagation defect in miniature — and it landed in the **conclusion**,
which is the part a reader who skips the table still gets.)*

And the corollary, learned the hard way in § 4: **replay a new mechanism against
the history that motivated it before believing it.** Two of the three checks here
pass that test. The third does not, and says so.

**A third corollary, added after Codex reviewed the code rather than the prose.**
Nine findings came back, seven of them real defects *in the checks themselves* —
check B fired on shell pipes inside code fences and on every ordinary single-row
table edit; check C joined shingles across newlines and then grepped line-by-line,
so most could never match. **All were shipped after testing that I called
two-directional.** The tests were real and the defects were real at the same time:
I tested the cases the checks were designed for, and none of the cases they would
actually meet. **"Tested in both directions" means the intended defect and its
absence — not the routine traffic the mechanism will sit in.** For a hook on every
file edit, that traffic *is* the risk, and a hook that cries wolf on a table-cell
correction would have been ignored inside one session.
