# 2026-08-09 · hub — turn the error ledger into mechanisms that fire at the moment

> **Status:** `complete`

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
| 17 | **generalised over a set never enumerated** — *"every propagation failure today was a retyped measurement."* Audited afterwards: three instances, **one measurement and two provenance claims**, and only one of the sixteen numbered errors is a propagation failure at all. The correction widens the anchor argument rather than narrowing it | **the owner-review Stop hook**, fifth round, asking for the breakdown |
| 18 | **compressed a six-way table into a three-way sentence and lost two rows** — told the owner *"six had a moment… four already watching, two now guarded, and the rest need a person or a habit."* The documented breakdown is **4 already caught · 2 built · 3 skill steps · 2 buildable-not-built · 1 no moment · 1 open design question.** Buildable means the moment exists, so **eight** have a machine-decidable moment, not six; and #4/#9 do not "need a person" — they need a checker I chose not to build, for stated trade-offs | **the owner-review Stop hook**, sixth round, asking how the breakdown was derived |
| 19 | **"substantially inert" for a defect never quantified** — check C's cross-line shingles were called *"most could never match"* from mechanism alone. **Measured after being asked: 52.2%** (1098 shingles, 400 real paragraphs). Half-blind, not mostly-blind — and the overstatement ran *toward* the drama of the finding | **the owner-review Stop hook**, asking for the percentage |
| 20 | **attributed a reviewer split to reading style without controlling for input** — claimed the hook and Codex "see different things", when `owner_review.py:4-5` shows the hook is *given* only the reply. Half the split is forced by input scope, and the confound was one `grep` away | **the owner-review Stop hook**, asking whether both saw the same artifacts |
| 21 | **declared a coverage gap without surveying the instruments — third time** — told the owner doc-vs-code contradictions are *"invisible to both instruments."* Wrong twice over: Codex's diff carries the docs **and** the code, and it caught a cross-document contradiction on this very PR (its P1, § 7 vs § 3); and `check_doc_routes.py:118-121` already implements the claim-vs-artifact shape, failing a route whose trigger no longer appears in the doc it points at. **What survives is narrower: the *reply* is in no reviewer's scope** | **the owner-review Stop hook**, asking which instruments had been evaluated |
| 22 | **four different totals for the same set, in one reply** — *"three confirmed"*, *"six more"*, *"13 real defects"*, *"Codex caught 15"*, with per-PR and cross-PR scopes never distinguished. Counted from the API afterwards: **#830 = 10 findings, all in docs; #831 = 15, of which 14 code; 25 total.** The *"13"* was simply wrong | **the owner-review Stop hook**, asking for the breakdown |
| 23 | **conflated two gaps into one recommendation** — *"reading claims against code is a much smaller job because the mechanism already exists."* The mechanism named was `check_stamp_discipline`, which walks `docs_root.rglob("*.md")` (`bootstrap.py:9318`) and **never reads code** — it addresses doc↔doc propagation. **Reconciled with row 21**, which is right that `check_doc_routes.py:118-121` already implements the claim-vs-artifact *shape*: that one checks a **config↔doc** pair, not prose against the code it describes. The honest statement is neither "nearly solved" nor "nothing exists" — **the shape is proven here and has never been pointed at code** | **the owner-review Stop hook**, same round |
| 24 | **a mechanical fix applied without scoping corrupted the ledger it was fixing** — a reorder collected every numeric-first row in the file, not just the errors table, and redistributed them: **8 Codex disposition rows landed in the error ledger and 8 error rows in the review section.** Restored from git, redone bounded by the section's own headings | **self, immediately** — by reading the result back instead of trusting the command's success message |

**#24 is the cheapest lesson here and the most transferable:** the command reported success, and success meant *the sort ran*, not *the file is right*. Nothing was wrong with the sort — it was pointed at the whole file when the target was one table. **A mechanical operation needs its scope verified, not just its exit code**, which is the same shape as `$?`-after-a-pipe and cost one `git checkout` rather than a merged corruption because the result was read back.

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
id to cite. **What was actually retyped: one measurement and two provenance
claims** (audited under #17, after this very paragraph said *"every propagation
failure was a retyped measurement"* and was left standing two lines below the row
correcting it — propagation, inside the fix for the propagation claim). Both
kinds are unanchored, which is the point: the class needing ids is *any repeated
claim*, and provenance turns out to be the commoner half.

**#15 measured out fine** — ~41 ms for the `PreToolUse` checks, ~82 ms median /
137 ms max for the `PostToolUse` grep path, and ~41 ms of every figure is Python
interpreter startup, identical in the case that does no work. Acceptable. **The
ordering was still wrong**, and "it turned out fine" is not the same as "it was
checked": a hook on every edit earns a measurement before registration, not after
a reviewer asks.

**#22 and #23 are class B and class A respectively, and both landed in the same
reply — the one summarising a PR about exactly these classes.** #22 is a count
asserted four ways without counting; #23 is a conclusion one step past the
measurement, merging *anchors solve doc↔doc propagation* (true, and the estate
runs one) with *doc↔code contradiction is nearly solved* (false — nothing reads
code against the claims about it). **The corrected recommendation is worse news
and more useful:** doc↔code is not a small job riding on existing machinery, it
is an unbuilt one, and it is where 14 of this PR's 15 findings lived.

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

## Codex review — round 1, nine findings

**1 P1 · 8 P2 · all nine verified against source before acting · 8 conceded ·
1 partial. Seven were real defects in the checks themselves**, which is the
result that matters: the prose was reviewed twice by the owner-review hook and
came out clean, while the code had not been read by anything but its author.

| # | finding | disposition |
|---|---|---|
| P1 | § 7's conclusion still said **six** one section after § 3 was corrected to **8** | **[conceded]** — and it landed in the conclusion, which is what a reader who skips the table takes away |
| 1 | check B treated `\|`-leading lines inside ```` ``` ```` fences as table rows | **[conceded]** — verified on the hooks README itself, which false-positived at exactly the L147/L151 Codex predicted |
| 2 | check B only ended table state on a **blank** line, so prose with no blank line before it let the real defect through | **[conceded]** — GFM ends a table at any non-row line |
| 3 | check B judged `new_string` alone, so **every ordinary single-row table edit** looked like an orphan | **[conceded]** — now reconstructs the resulting file |
| 4 | `MultiEdit` nests payloads in `tool_input.edits`; check B read only top-level keys, so it was silent for every markdown MultiEdit **that the matcher had just been registered for** | **[conceded]** |
| 5 | check C excluded the target file, but post-edit a remaining hit there is a survivor | **[partial]** — see below |
| 6 | check C's `git grep` omitted `--untracked`, missing documents written this session | **[conceded]** |
| 7 | `MAX_HITS` applied to the union, so one idiomatic shingle suppressed a distinctive one | **[conceded]** — now capped per fragment |
| 8 | `_fragments` joined shingles across newlines, then `git grep -F` matched line-by-line, so a fragment spanning a wrap point could never match | **[conceded]** — and now **`MEASURED` at 52.2%** unmatchable (1098 shingles from 400 real multi-line paragraphs). Half-blind, not inert; see error #19 |

**Finding 5 is the partial, and the hook proved it itself.** Codex reasoned that
the replaced occurrence is gone by `PostToolUse`, so any remaining hit in the
target is a survivor. True only for text the replacement did not carry forward —
and the very next edit rewrote a paragraph while keeping its opening sentence,
so the newly-unexcluded target fired a **false positive on the fix for the
finding**. Now scoped to fragments present in `old_string` and absent from
`new_string`; both directions re-tested.

**What this round actually taught, and it is not "test more".** All seven code
defects shipped *after* testing I had called two-directional. The tests were real;
they covered the defect each check was designed for and its absence. **They did
not cover the traffic the check would sit in** — fenced code, single-row edits,
MultiEdit payloads, wrapped prose. For a hook on every file change, that traffic
is the entire risk surface, and a check that cries wolf on a table-cell
correction is ignored inside one session. *Two-directional is not the same as
representative.*

**The split is real but half of it is trivial, and the trivial half is the
finding.** `owner_review.py:4-5` reads *"the final assistant reply from the
transcript"* — **only the reply, never the diff.** So its six-for-six claim-defect
record is *forced by its input*, not evidence of a different reading style. Codex
had the whole diff, prose and code together, and still skewed **7 of 9 to code** —
that half of the contrast is genuine.

**What it exposes, stated at the width the evidence supports** (narrowed under
#21, after a first version overreached): **the reply is in no reviewer's scope.**
Codex reads the diff and never the chat; the Stop hook reads the chat and never
the diff. A claim made to the owner *only in a reply*, and contradicted by the
code, is seen by neither.

**Doc-vs-code inside the diff is NOT the gap** — that was the overreach. Codex has
both artifacts and demonstrated the capability on this PR, and
`check_doc_routes.py:118-121` already runs a claim-vs-artifact check of exactly
that shape for routes. The estate is better covered here than the first version of
this paragraph claimed.

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
