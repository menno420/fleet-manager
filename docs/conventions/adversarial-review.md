# The review ladder — provenance, not correctness

> **Status:** `reference` · drafted 2026-08-06
>
> **This is a proposal with a verification record, not ratified policy.** The
> owner asked for mandatory adversarial review; a second session is building the
> mechanism; this document is what the hub session contributed and what survived
> being run through itself. Treat it as input to that work, not as a decided
> rule. When the mechanism lands, this either becomes the convention or is
> superseded by it — and whichever happens, say so here.

## The problem it solves

Measured across 2026-08-05/06: **every correction came from an instrument, an
adversary, or the owner — none from an agent re-reading its own work.** The
estate instruments execution (CI, checkers, gates) and does not instrument
judgement. This is an attempt at the second.

## Why provenance rather than correctness

**A reviewer asked *"is this right?"* must form a domain opinion, and will
invent one if it has no basis.** A reviewer asked *"what is this based on?"*
needs no domain knowledge at all — it only has to notice whether an answer
exists. That single distinction is what stops the review manufacturing
objections, which is the failure mode that makes mandatory review worse than
none.

It also exploits a real asymmetry: **stating a claim is cheap; stating its
provenance is not.** "Vertex doesn't support X" takes four words. Answering
"what did you base that on?" cannot be done without revealing that it came from
one call.

The first question alone would have caught the three worst errors of 2026-08-06,
before any reviewer was involved:

| claim | *"what did you base this on?"* |
|---|---|
| Interactions API unavailable | *"a discovery document that omits it"* — the gap is in the answer |
| Rules API is walled to agents | *"the kit's NOTE"* — plainly not a measurement |
| 100 % coverage at 8 fps | *"a displacement estimator"* → could it measure that range? No |

## Two layers, different authors

**An agent generating its own adversarial questions has no distance from its own
blind spots, so it is never asked to.**

### Layer 1 — the fixed list, answered by the agent, in writing, before calling out

1. **What did you base this claim on?** A source, a command, an exact error —
   not a feeling.
2. **Which documents covering this did you read?** Cite `path:line`.
3. **If you asserted something is impossible or unavailable: which paths did you
   try, and what would a DIFFERENT path look like?** Naming the untried path is
   the point — it is what broke the Interactions API wall.
4. **What are the consequences, and who else do they affect?**
5. **What did you NOT do, check, or verify? What would change this conclusion?**

Most of the value is captured here. The call only catches what survives.

### Layer 2 — the reviewer, which has distance because it did not write the plan

- Context-specific follow-ups the fixed list cannot anticipate.
- **"Which claims are stated more confidently than their evidence supports?"**

### Why question 5 is split the way it is

Question 5 asks *"what did I not run?"* — **coverage of effort**, a known
unknown, and demonstrably self-answerable: the 2026-08-06 cards caught *"fps
above 16 is untested"*, *"n = 3 sessions, one person"*, *"the new CI step has
never gone red on a real defect"* unprompted and correctly.

It does **not** ask *"am I overconfident?"* — that is a blind spot by
definition. If the agent knew the honest hedge it would have used it. *"100 %
coverage at 8 fps"* was stated flat with no hedge and was false, because the
error was in the **instrument**, not in the effort. That half belongs to the
reviewer.

> **Self-answerable: what I did not do. Not self-answerable: whether what I did
> works.**

## The gate — narrower than it first looks

Gating on soundness is impossible, and quote-matching is gameable: a real quoted
line can refute nothing, and checking relevance is prose inference. But *"don't
gate at all"* skips the option that fits. Gate on this and nothing more:

- The provenance section **exists and is non-empty**.
- Every **`path:line` citation resolves** — file exists, has at least that many
  lines. Pure fact extraction, no prose inference. Same trick
  [`tools/check_doc_routes.py`](../../tools/check_doc_routes.py) already uses:
  verify the pointer resolves, never judge the prose.
- **Commands and error strings are recorded but NOT gated.** Re-executing them
  in CI is unsafe — stateful, possibly destructive — and regex-matching their
  shape proves only that they look like commands, which is theatre by the same
  argument that kills word-count.

**Be honest about what that buys: it catches an ABSENT answer, not an unsound
one.** *"I based this on general knowledge"* cannot produce a resolving
citation. Soundness is read by the owner. That is the same division session
cards already use — the checker verifies the card exists and is complete, the
owner judges whether it is any good, and nobody calls that theatre.

## Two practices that came out of testing this

**Test a new instrument out of bounds before trusting it.** The 2026-08-06
coverage error came from a correlation search that **silently clamped instead of
failing** when asked for a value outside its range — it returned a plausible
number, not an error. One known-bad input would have exposed it. When you
introduce a measurement tool, feed it a case you know it cannot handle and
confirm it fails **loudly**.

**Flag owner-dependent claims explicitly.** Five of thirteen owner corrections
on 2026-08-06 came from ground truth only he has — his screen, his thumb, his
console, his billing page. An agent cannot self-diagnose missing tacit
knowledge, but it **can recognise the domains**: anything about what he did,
saw, intended or decided, and anything about hardware or accounts it cannot
read. In those domains, mark the claim owner-dependent instead of asserting it.

## Do not concede on reflex

**Record what SURVIVED, not just what was conceded.** A report of "three
objections raised, three conceded" reads as rigour and is equally consistent
with deference — and the reviewer has a known error rate here: one Gemini review
was flatly wrong about a dependabot deadlock, another overclaimed on video
coverage and was caught only by independent measurement.

**Agreement is nearly worthless as evidence; the objections are the product.**
If a review raises nothing, say so plainly — that is a result, not a pass.

## Routing

**Vertex**, per [`vertex-first-for-gemini.md`](vertex-first-for-gemini.md) —
prepaid credit, no daily cliff. `GEMINI_API_KEY` (free tier) is fine for AI
Studio calls but carries ~20 requests/day on flagship Flash, which a
per-session review would exhaust. `GEMINI_API_KEY_PAID` bills a real card —
only when Vertex has actually failed, or for Deep Research, which exists on no
other path.

## The ladder — every rung a different instrument

This is the property that stops it being theatre. Four models doing the same
review is redundancy; four different **instruments** is coverage.

| rung | instrument | catches |
|---|---|---|
| agent self-answer | provenance recall | absent sources, unread docs, untried paths |
| reviewer (Gemini, Vertex) | reasoning distance | unsupported and over-confident claims |
| Codex on the PR | code + diff | implementation defects nobody reasoned about |
| the owner | ground truth | his screen, his thumb, his console |

**Codex is the rung closest to the two hardest catches of 2026-08-06** — a test
suite seeing `staged_regen` fire on the cold-adoption arc, and a bench catching
a lazy import that works in the source layout and dies in the built dist
adopters actually run. Neither was reachable by reasoning about prose.

### First evidence, 2026-08-06 — and read the diff comments, not the summary

`MEASURED-PRIOR` (reported by the session that ran it, not re-derived here). On
`menno420/substrate-kit#580`, a plan **Gemini had already reviewed**, Codex
returned **9 findings — 5×P1, 4×P2.**

That is the ladder claim surviving contact. A third *opinion* would overlap with
the second; a different *instrument* returns orthogonal findings, and it did.
The clearest one is a claim about what code does rather than what prose says:
`currency.py` fetches four file paths, not trees, **so `adopters.md` cannot
establish absence of alternate linkage.** No prose review reaches that.

> **THE TRAP, and it is expensive: the Codex review summary body is
> BOILERPLATE. The findings are inline comments on the diff.** A session that
> reads only the summary concludes Codex found nothing — a silent, plausible
> null, which is the failure shape this whole document exists to catch. Fetch
> the review *comments*, and if a fetch returns an empty list, say so explicitly
> rather than reporting "no findings".

The session also did, unprompted, both things this document asks for: it
**verified Codex's checkable claims before responding to any of them** (both
held — including two `.gitmodules` cases it had itself missed), and it recorded
what was objected to rather than that a review had occurred.

**One caution on the comparison.** "Materially sharper than Gemini's" was that
session's own judgement, on one PR, about a review of its own work. Suggestive,
not measured — and the ladder argument does not need it. The claim that matters
is that different instruments find *different* things, which 9 orthogonal
findings support on their own.

Two rules carry over to it: **record what it objected to, not that it
approved**, and **state a fallback for silence** —
`menno420/superbot-next#602` sat open fifteen days because a correct diagnosis
had no owner, and a review rung must not become a new version of that.

## The verification record

This document was run through its own mechanism before being written — four
turns, Gemini on Vertex, ~4 600 prompt tokens, client-side history.

**It produced eight substantive changes and zero invented objections**, and
twice said "well-founded, no objections there" rather than manufacturing
balance. What it changed:

- Killed the command/error-string half of the gate as unverifiable.
- Forced the gate claim down from "checks specificity" to "catches absence".
- Split question authorship into the two layers above.
- Split question 5 into an agent half and a reviewer half.
- **Caught the word "reliably" being over-stated — in the sentence arguing that
  agents can detect their own over-statement.**
- Added the out-of-bounds instrument test.
- Raised owner-dependent-claim flagging.
- Accepted a pushback (session cards are dynamic; planning-phase review is
  needed, not PR-phase only) rather than conceding uniformly.

**All eight came from the four times it disagreed. Its agreement taught
nothing** — which is the argument for recording what survived rather than a
boolean.

## Honest nulls

- **Unratified.** The owner has not adopted this; a second session is building
  the mechanism and may land something different or better.
- **The gate is unbuilt.** No `path:line` resolver exists yet; nothing here has
  been run in CI.
- **One review, one model, one subject.** The eight-changes figure is this
  document reviewing itself. Nothing establishes the rate on other material.
- **The Codex rung has one data point** (`substrate-kit#580`), reported by the
  session under review rather than measured independently.
- **The metric is proposed, not measured**: the ratio of corrections arriving
  from an instrument or reviewer versus from an agent re-reading its own work.
  If the practice works that ratio moves; if it does not move, this is ritual.
- **Whether the reviewer's error rate is tolerable is unmeasured** — two known
  errors in three days of use is the entire sample.
