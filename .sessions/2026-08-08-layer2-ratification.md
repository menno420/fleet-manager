# 2026-08-08 · hub — Layer-2 ratification, and the flip-before-review incident

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · docs-only — land the Layer-2 ratification; record the auto-merge incident

Time: 2026-08-08 · venue: owner-live hub chat · branch
`claude/fleet-manager-rules-enforcement-18o8t1` (restarted from `4e6a05a` after
fm #827 merged)

💡 Session idea: **the born-red card is not only a completeness gate — it is the
only thing holding a PR away from the automatic lander, and flipping it is
therefore an irreversible act.** Every written rule in this estate treats the
flip as a *bookkeeping* step performed at the end. It is not: it is the moment
the PR becomes merge-eligible, and anything you still intend to do to that PR —
Codex review above all — has to happen before it, not after.

Layer-2 handoff: null (fleet-manager itself; no satellite repo attached)

## Previous-session review

⟲ fm #827 recorded the owner's intent and amended two standing directives. It
landed correctly, but its close-out sequence was wrong in a way the card could
not see, and this session exists partly to fix what that cost.

## What is about to happen

Two things:

1. **Re-apply the Layer-2 ratification** that #827 lost — three surfaces still
   said *"awaiting owner sign-off on the shape"* after the owner signed off on
   it (`repos/README.md`'s coverage table, `working-here.md`'s PROPOSAL header,
   and the earned-files row calling it an open question). The commit was pushed
   ~55 seconds after the lander had already merged the PR, so it never reached
   `main`.
2. **Record the incident itself**, below, because it is a repeatable trap with a
   one-line fix.

Verification at close: `python3 bootstrap.py check --strict`, plus both checkers
directly, real exit codes — and **Codex review requested while this card is still
born-red**, which is the corrected order.

## This session's errors, counted the way the baseline counts them

Axis 1 of the two-axis protocol (`docs/planning/2026-08-08-agent-operating-environment-roadmap.md`),
catcher-attributed exactly like the 16-incident table in
[`../docs/findings/2026-08-08-why-rules-dont-bind.md`](../docs/findings/2026-08-08-why-rules-dont-bind.md):

| # | error | caught by |
|---|---|---|
| 1 | **flip-before-review** — the card was flipped, then the review requested; the lander merged 22 s later and a subsequent commit missed `main` entirely | self, post-hoc (probing PR state instead of trusting the close) |
| 2 | `$?` read **after a pipe** on three consecutive `git push` calls, reporting `tail`'s status — one push had genuinely not landed and read as success | an **assertion** comparing local `rev-parse` to `ls-remote`, not vigilance |
| 3 | OD-13/OD-14 inserted **above** OD-12, breaking the table's ordering | self, immediately, on read-back |
| 4 | **the corpus measurement was overstated** — *"none of the 21 questions was already answered"* (it was 20 of 21) and *"two `[D-NNNN]` entries"* (there are three), repeated across five documents and stated to the owner | **Codex**, on fm #827 |
| 5 | **every new record stamped `2026-08-09` when it is `2026-08-08`** — 35 occurrences across 17 files, including two owner-directive rows, a `[D-NNNN]` entry, and both session-card filenames | **ChatGPT**, via the owner |

**Error 5 is the one that should not have been possible.** The date was in this
session's own opening context, `date -u` was one command away — and the Phase 1
card had **already recorded this exact error** the same day
([`2026-08-08-rules-enforcement-phase1.md:112`](2026-08-08-rules-enforcement-phase1.md):
*"dated the roadmap `2026-08-09` without checking; `date -u` says 08-08 —
composed, not transcribed, in the provenance line of a document about
provenance"*). A session read that card, wrote a follow-up to it, and reproduced
the error it documents — **in owner-attributed directive rows**, which is the
worst place for it, because an OD row's date is what a future session uses to
decide which directive is current. Corrected everywhere except the three
legitimate references (two Atlas-retirement dates and the Phase 1 record itself,
which must keep the wrong date it is reporting).

**Catcher attribution matters here:** neither gate, hook, nor Codex caught it —
a **second provider did**, reading the plan with no stake in it. That is a real
argument for the roster in `docs/intent.md` § 7 being a *review* asset and not
only an implementation one.

| 6 | **an OPEN item invented from a typo** — a trailing `22.` in the answer list was recorded as *"question 22, begun and left blank"* in three documents; there was no question 22 | **owner** |
| 7 | *"the one claim in the agent roster with nothing measured behind it"* — a composed gloss over a four-row table where **three** rows are unmeasured owner-report | **Stop hook** |

**Errors 6 and 7 are the same defect as 4, at three different targets.** Each is
a sentence composed *about* a record instead of read *off* it — the answer list,
the roster table, the corpus. Every factual error in this session is that shape,
which reproduces the finding's class-A result exactly
([`../docs/findings/2026-08-08-why-rules-dont-bind.md`](../docs/findings/2026-08-08-why-rules-dont-bind.md) § 3):
claims transcribed from tool output were right; claims composed from context
were not.

**Error 6 is worth its own note**, because it is a failure mode the Phase 2 design
did not anticipate: the intent map's **OPEN column can be fabricated**. The
EXPLICIT / ESTABLISHED / DERIVED columns all describe things that exist and can be
checked against a source; OPEN describes an *absence*, and an invented absence
looks identical to a real one while wearing the same provenance label. Recorded in
the roadmap § 4.8 — **an OPEN entry is a claim about the owner and needs the same
evidence as any other.**

## Codex review — dispositions

Five findings on #827, **all five verified against the tree before being acted
on** (never obey a review, verify it), and all five real:

| # | finding | disposition |
|---|---|---|
| P1 | §5 still read *"No deletions (OD-3)"* against the amended OD-3 | **[conceded]** — §5 now reads *no **undirected** deletions*, with the per-item bar |
| P1 | `CONSTITUTION.md:112` + `collaboration-model.md:29` still gate every ask behind attempt-or-exact-wall | **[conceded]**, and it sharpened the fix: the gate was never wrong for **action** asks — it is meaningless for **intent** asks, where there is nothing to attempt. Both docs now carry that split, recorded as **[D-0013]** |
| P2 | the corpus measurement was wrong | **[conceded]** — corrected in all five places, and the miss is now a `MEASURED` datum in its own right (see below) |
| P2 | `execution-surfaces.md` restated the roster it had just declared out of scope | **[conceded]** — reduced to a pointer, so it cannot drift |
| P2 | `docs/repos/README.md` still said *"not a template to stamp out, each repo earns its files"* and listed a fifth Tier-1 row | **[conceded]** — the earned set is now stated as the shape to replicate, with the narrower true remainder kept (departures are recorded with reasons); the fleet-manager row says explicitly that it is not one of the four |

**Zero refuted, and the P1 pair is the interesting result:** both were *the same
class of defect this whole session is about* — a directive changed in one place
while the surfaces a session actually consults kept the old rule. The session
that spent the day fixing stale routers created two new ones inside four hours,
and did not notice.

**The corpus miss is worth keeping as a number.** The questions were filtered
against the repo by reading, and **1 of 21 slipped through** — the purpose
question, already partially answered in two places. That is a measured
false-negative rate for eye-filtering, and it is the argument for making Phase
2's ESTABLISHED column a **retrieval** step rather than a recall step.

**Instruments that fired:** `git_state_guard`'s force-push tree check (correct —
answered with a tree comparison, three files byte-identical); the born-red hold,
twice, by design; `read_before_write` **once, falsely** — the session id rotated
across a usage-limit pause and split its `/tmp` read-set, which is the
false-positive class already named in the plan. Count catches, never firings.

**Error 2 is the one worth the ink**, because it is the estate's own most-repeated
rule (*"never `$?` after a pipe"*) broken by a session that had read that rule in
three separate documents the same day — and it was caught by a **mechanical
comparison**, which is the whole thesis: the rule did not bind at the moment of
action; a check did. It also proves the point negatively — the two pushes that
*did* succeed would have hidden a failure just as effectively.

## The incident — flip-before-review, `MEASURED` on fm #827

| time | event |
|---|---|
| `19:06:39Z` | `@codex review` requested on #827 |
| `19:07:01Z` | **`merge-on-green` merged it — 22 seconds later**, actor `github-actions[bot]`, at head `a0bac75` |
| `19:07:55Z` | the Layer-2 ratification commit pushed — to a branch whose PR was already merged; it never reached `main` |

**No session merged anything early, and no rule was broken as written.** The
boot file says *"never merge a PR you have asked Codex to review before it
answers"*, and nothing did. What happened is one step earlier: **the card had
already been flipped to `complete`**, and the flip is what makes a PR
merge-eligible. `merge-on-green` then did exactly its job.

**The mechanical link, read from the lander rather than inferred from the
timing** — [`.github/workflows/merge-on-green.yml`](../.github/workflows/merge-on-green.yml):

- **`:77-78`** — it triggers on `pull_request: types: [ready_for_review,
  synchronize, …]`, so **the flip commit's own push is the trigger**; also
  `workflow_run` (`:79`) and a `7,37 * * * *` cron (`:90`).
- **`:196-209`** — the sweep reads every in-diff `.sessions/*.md`, parses
  `**Status:** \`<token>\``, and **skips the PR while any card reads
  `in-progress`** — *"even if every check is green"* (`:47-48`).

So the born-red card is a **merge interlock**, not merely a completeness
signal, and flipping it is the act that releases the interlock **and** fires the
sweep in the same push. The 22-second interval is exactly that path.

The mistake is a **sequence** error, and its root is that every written
description of the close treats the flip as end-of-session bookkeeping.
`session-close` step 7 said *"flip … green then merges server-side"* — accurate
and incomplete: it never said that the born-red hold is the only thing keeping
the automatic lander away, so anything still owed to the PR must precede the
flip. Committing a review request *after* the flip is racing a server-side
process, and 22 seconds is the size of the window.

**Fixed in the procedure, not in prose:** `session-close` gains step **6c** —
everything owed to the PR happens before the flip, review included, with the
measured timing above as its reason — and step 7 now ends with *"after the flip,
treat the PR as gone."* This PR runs the corrected order as its own first test.

## What shipped

- **The Layer-2 ratification** — `docs/repos/README.md` (coverage table now
  records the shape as settled, and changes tier-2 from *pre-stubbed* to **on
  demand**), `docs/repos/spider-swing/working-here.md` (PROPOSAL → **RATIFIED**),
  and the earned-files row that called it an open question. Plus the one part of
  the shape not yet built, written down so the next folder carries it: **external
  workspace pointers** per repo (Drive · ChatGPT · Gemini notebook).
- **`session-close` step 6c and an amended step 7** — the mechanism fix for the
  incident below.
- **The §7 ledger row** for both this PR and the trap.

## Verification

Real exit codes, each command run on its own — never `$?` after a pipe:

- `python3 bootstrap.py check --strict` → **exit 1 while born-red** (sole
  finding: this card, via the added-card lane), **exit 0** on the flip.
- `python3 tools/check_doc_routes.py --strict` → **exit 0**.
- `python3 tools/check_no_false_walls.py --strict` → **exit 0**.
- Force-push safety established by **tree comparison**, not by assertion: three
  doc files byte-identical between the discarded head and the restarted branch.

**Two second-order facts worth keeping:**

- **The PR API read was stale and would have hidden this.** `GET /pulls/827`
  returned head `a0bac75` and `mergeable_state: unknown` *after* the push to
  `ff0a16d` had succeeded; `git ls-remote` returned `ff0a16d` immediately. The
  merged state only surfaced because the read was cross-checked against the ref
  — which is the `CONSTITUTION` rule about staleness-sensitive reads, earning
  itself again.
- **`git_state_guard` fired correctly on the recovery force-push** and named all
  four at-risk files. The answer was a tree comparison, not reassurance: three
  doc files byte-identical between the discarded head and the new one, so the
  content survived the restart.
