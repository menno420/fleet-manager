# 2026-08-09 · hub — the owner's intent, asked and captured

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only — capture 21 owner intent answers; reconcile the directives they change

Time: 2026-08-09 · venue: owner-live hub chat · branch
`claude/fleet-manager-rules-enforcement-18o8t1` (restarted from `f53d7ea` —
Phase 1 merged as fm #826, so the prior commits are already-merged history)

💡 Session idea: **the estate has been recording what it decided and almost never
what it is for.** Twelve OD rows, two D-entries and a PL register all answer
*"what was chosen"*; nothing answered *"what would make the owner say yes, that
is what I meant"*. This session asked, and the answers immediately contradicted
two standing directives — which is the point: intent that is never asked for
does not stay consistent with the rules written under it.

Layer-2 handoff: null (fleet-manager itself; no satellite repo attached)

## Previous-session review

⟲ Phase 1 (fm #826) made the corpus trustworthy enough to retrieve from, and its
own roadmap named the next thing: *every actively developed repo must have one
discoverable canonical intent source.* It could not build one, because the
content did not exist anywhere to be assembled — **it had to be asked for.** This
session is that ask. Phase 1's judgement to stop at retrieval was right: an
intent surface written on top of a misleading corpus would have inherited its
errors.

## What shipped

**[`docs/intent.md`](../docs/intent.md)** — fleet-manager's durable intent
surface. Purpose (router and records home; **the primary reader is the next agent,
not the owner**), the three success criteria he picked, the non-goals, the decision
heuristics, the growth rule, and the **agent roster** — Claude does everything and
holds the credentials; ChatGPT's *Work* environment is doing real, reliable
implementation in spider-swing; Gemini and Grok are routed to review and planning;
Codex reviews PRs. Nothing in this repo had recorded that.

**Two standing directives amended by his own answers**, appended not rewritten:

| directive | change |
|---|---|
| **OD-3** archive-never-delete | cleanup of spent docs *and repos* is now wanted, with a stated reason per item — *"the goal is not a perfect archive, but rather an efficient workflow"* |
| **OD-6** *"pace: slow"* | restated as **one thing at a time, finished properly** — *"that does not mean we should ever rush things, though it does also not mean we can't make progress"* |

**New: OD-13** — method and enforcement work, and settling the multi-provider
agent mix, come **before** high-value product work. This is now the standing
answer to *"what should a session pick up"*. **OD-14** — intent is what a plan is
checked against.

**A live contradiction corrected.** The boot file and `owner-profile.md` both
carried *"his attention is the scarcest resource"*, which reads as *minimise
asks*. He wants close to the opposite: *"I'd rather have an agent ask me
something so I can clarify than that they misunderstand the goal."* Both now say
**ask immediately, keep working, stop only when genuinely blocked** — with the
30-minute check-in rhythm and the don't-interrupt-implementation rule that make
it operable.

Also: `execution-surfaces.md` said *"it assigns no roles"* — true when written,
false now, so it points at the roster instead of contradicting it; the roadmap's
§ 4.6 and § 4.8 record the first live run of the interview method.

## Measured

**The corpus had no intent layer, and that is the result worth keeping.** Every
one of the 21 questions was filtered against the repo before being asked, per the
*never ask what the repo already answers* rule — **none of the 21 was already
answered.** Twelve OD rows, two `[D-NNNN]` entries, a PL register, a 280-line
fleet account and a 1,146-line owner queue all record *what was decided*; nothing
recorded what the repo is **for**.

**Two of 21 answers contradicted standing directives.** That is the argument for
the surface, and it is a design input Phase 2 did not have: the interview's output
is **not additive-only**, so the procedure needs an explicit reconciliation step —
now recorded in the roadmap § 4.8.

**His verdict on the format, which corrects my default:** the large lettered batch
was right *"for this task"* because the subject was the method itself; the per-task
version should be sized to *"the remaining ambiguous items"* with **no minimum or
maximum**, and the routine form is a **restated interpretation**, not a menu —
*"most of the time by stating back your perceived intent I will see if you
understood and will correct you if you are wrong."*

**Boot file: +93 words.** Stated rather than hidden, because Phase 1 held itself
to net-zero and this session did not. Paid partly by trimming the
read-before-write bullet (the hook prints that measurement verbatim at write
time, so the boot file was duplicating a payload that already arrives on time)
and by replacing the flag-rule bullet rather than adding beside it. The remainder
is the intent pointer and two restated directives — which is the *"good reason"*
his own growth rule requires.

## Verification

Real exit codes, each command run on its own — never `$?` after a pipe:

- `python3 tools/check_doc_routes.py --strict` → **exit 0**, 23 routes · 19 docs
  routed · 0 errors · 0 notes.
- `python3 tools/check_no_false_walls.py --strict` → **exit 0**, CLEAN across 5
  living/binding docs.
- `python3 bootstrap.py check --strict` → **exit 1 while born-red** (sole finding:
  this card in-progress, via `scripts/preflight.py`'s added-card lane — the
  designed hold, and Phase 1's parity fix working), then **exit 0** on the flip.

## Honest nulls

- **Nothing here is measured about whether intent capture changes behaviour.**
  The claim that a stated intent prevents drift is the *reason* for the file, not
  a result of it. The first real test is a future session whose plan gets checked
  against § 2 and fails.
- **The agent roster is his report, not this session's measurement.** No run of
  ChatGPT-on-documentation exists; he named it as the thing to test.
- **Question 22 was begun and left blank.** Recorded as open in `intent.md` § 9
  rather than guessed at.
- **`docs/intent.md` is fleet-manager's only.** No other repo has one, and the
  roadmap deliberately does not require a file of that name everywhere.
