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
needs **far less** — mostly it has to notice whether an answer exists. That
distinction is what stops the review manufacturing objections, which is the
failure mode that makes mandatory review worse than none.

**Corrected 2026-08-06:** this originally said *"needs no domain knowledge at
all"*, which overstates it. **The split is by layer.** The automated gate needs
none — it checks presence and resolution. The *reviewer* needs some, because
telling a genuine source from a confident restatement of the claim is still
semantic judgement. Conceded to Gemini on `substrate-kit#580`.

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
- **At least one `path:line` citation is present** — see the correction below;
  this clause is load-bearing and was missing in the first version.
- **Every** `path:line` citation resolves — file exists, has at least that many
  lines. Pure fact extraction, no prose inference. Same trick
  [`tools/check_doc_routes.py`](../../tools/check_doc_routes.py) already uses:
  verify the pointer resolves, never judge the prose.
- **Layer 2 must be recorded as having OCCURRED.** Gate on occurrence, never on
  the result. Without this a triggered change merges with the reviewer never
  having run and nothing noticing.
- **Commands and error strings are recorded but NOT gated.** Re-executing them
  in CI is unsafe — stateful, possibly destructive — and regex-matching their
  shape proves only that they look like commands, which is theatre by the same
  argument that kills word-count.

> ### ⚠ Scope, not just cost — added 2026-08-06 after round 6
>
> **Two of the clauses above look free and are not, and the difference is
> scope.** The kit's session-card marker mechanism is a `{label, needle}`
> substring list driven by config rather than code, so *"presence"* and
> *"Layer 2 occurred"* cost nothing to add. But `missing_markers` scans **every
> configured needle against every completed card**, and `check_added_card` calls
> it on any added card. **There is no conditional form.**
>
> So routing those clauses through session markers does **not** implement a
> conditional trigger set — it silently implements **gate-every-card, in every
> adopter that upgrades**, reddening work that never touched a decision surface.
>
> **Free on cost. Global in scope.** The hub session verified what the mechanism
> *does* and assumed what it *applies to* — PL-015's second corollary (*point
> the script at the artifact that will actually be graded*) applied to a claim
> rather than a script. Found by Codex on `substrate-kit#580` round 6, verified
> in the tree by the kit session rather than taken on the hub's word.
>
> **Consequence for the design:** either all four clauses move into a
> conditional checker — at which point "mostly free" is false and the cheap
> version is not cheap — or gate-every-card is accepted and **stated plainly**
> rather than described as conditional. **Do not describe a trigger set the
> mechanism cannot deliver.**

**Be honest about what that buys: it catches an ABSENT answer, not an unsound
one.** Soundness is read by the owner. That is the same division session cards
already use — the checker verifies the card exists and is complete, the owner
judges whether it is any good, and nobody calls that theatre.

> ### ⚠ Correction, 2026-08-06 — the first version of this gate passed vacuously
>
> This section originally read *"the section is non-empty AND every citation
> resolves"*, and claimed **"'I based this on general knowledge' cannot produce
> a resolving citation."** That claim is **false of the gate as written**:
> **zero citations satisfies "every citation resolves" vacuously**, so the
> document's own worked example of a *failing* answer would have **passed the
> document's own gate.**
>
> Found by **Codex** on `menno420/substrate-kit#580`. Neither the author nor a
> four-turn Gemini review saw it — it is a logic hole in the single load-bearing
> claim of the mechanism, and it invalidated the gate entirely until the
> minimum-count clause above was added.
>
> Two further overstatements from the same author, corrected in place:
> **"needs no domain knowledge at all"** overstates it — distinguishing a
> genuine source from a confident restatement is still semantic judgement (see
> § *Why provenance rather than correctness*). And `path:line` resolution is
> **not** more gaming-resistant than quote-matching; it is **cheaper to fake**.
> The gate never claimed to catch unsound answers, only absent ones — that
> mechanism stands, the framing around it did not.

## Two practices that came out of testing this

**Test a new instrument out of bounds before trusting it.** The 2026-08-06
coverage error came from a correlation search that **silently clamped instead of
failing** when asked for a value outside its range — it returned a plausible
number, not an error. One known-bad input would have exposed it. When you
introduce a measurement tool, feed it a case you know it cannot handle and
confirm it fails **loudly**.

**And verify what the instrument is POINTED AT, not only that it runs.**
Corrected 2026-08-06 after round 5 on `substrate-kit#580`. A session built a
validator specifically to stop verifying its provenance record by re-reading —
the right response — **and pointed it at the wrong artifact.** The spec's § 8
says CI grades the **session card**; the script checked a standalone
`docs/reviews/` file. Both failed, and the green script said nothing about
either.

> **"Verify by script, not by eye" is incomplete. The script's TARGET is itself
> a claim, and it is the one most likely to be assumed rather than checked.**

This is the inspection failure recurring one level up, and it is worse than the
original because a passing script *feels* like mechanical verification. Ask of
any checker: **which artifact does the rule name, and is that the artifact this
script opens?** Derive the target from the rule text, never from memory of what
the rule meant.

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

**Use a record format that makes the tally countable**, not a reading:
`[survived]` / `[conceded]` / `[partial]` per objection. First full run,
`substrate-kit#580`, across Gemini **and** Codex: **13 objections — 10
conceded, 2 partial, 1 refuted.** That is a distribution, not the
all-conceded pattern that prompted this section, and it only reads as one
because the format forces each objection to be dispositioned individually.

## Routing

> **Superseded 2026-08-29 ([D-0020]), noted here 2026-09-02:** Vertex is
> retired; the free `GEMINI_API_KEY` is the route, and its cap is **per day,
> per model** — so the per-turn Stop hook runs on a lite model
> (`gemini-3.5-flash-lite`) and the flip-time verification pass on
> `gemini-3.6-flash`, each on its own budget. The paragraph below is the
> credit-era routing, kept as the record it is.

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
| Codex on the PR | code + diff | **implementability** — specs that read fine and cannot be built |
| the owner | ground truth | his screen, his thumb, his console |

**The third rung's real specialty, measured 2026-08-06 and not what was
predicted here.** This table originally said Codex catches "implementation
defects nobody reasoned about." The actual result on `substrate-kit#580` was
sharper: **three of its five P1 findings were about a specification that read
correctly as prose and was not implementable.**

- the gate that **passed vacuously** on zero citations (§ 5 correction above)
- a known-bad reviewer test that required data the reviewer never receives
- a trigger that required **inferring intent from prose**

That is a distinct failure class from anything the first two rungs caught, and
it is not about judgement at all — it is the **gap between prose and
mechanism**. A sentence can be true, well-sourced, and un-buildable.

**So Codex belongs at the spec→code boundary, not only at decision points.**
When a mechanism described here gets built, it should look again at the build.

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

## Growth under review is a measurement, not a cost — and this is the finding

`OWNER`, 2026-08-06. The document grew **+50 % in one day** (1 595 → 2 391
words, three commits) and substrate-kit's copy roughly doubled across two Codex
rounds. A session flagged that as a proportionality risk. **The owner's read is
better and it inverts the conclusion:**

> *"We should not consider this as a fault in our plan, but exactly the plan
> working as intended."*

He is right. **Eighteen findings, every one verified correct, means the spec
contained eighteen real defects.** Had the reviews found nothing, the document
would be the size it started — *and still broken*. The growth is the visible
trace of the input's defect density. It measures how wrong the thing was, not
how expensive the process is.

**The near-error is worth recording too.** The proposed response was a
subtraction pass targeting half the length — which would have **deleted
verified-correct content on the theory that length is itself a defect.** That is
the same species as writing a false wall: taking a signal and reading it as a
limitation.

### What does survive: the file is two artifacts under one name

| | constraint | may grow? |
|---|---|---|
| the **record** — what was found, what survived, what was refuted | as long as the evidence demands | **yes, and it should** |
| the **instruction** — what a session does at a decision surface | must fit working attention *in the moment* | **no** |

Growth is correct for the first and corrosive for the second, and while they
share a file the record's legitimate expansion silently degrades the
instruction. The estate already separates them: `docs/findings/` for evidence,
`docs/conventions/` for the rule, and the `says` field in
[`.claude/hooks/doc-routes.json`](../../.claude/hooks/doc-routes.json) for the
one sentence that actually reaches a session at the moment it matters.

**So the fix is a split, not a cut, and it costs no correct content.** Deferred
until substrate-kit's spec lands — restructuring both copies mid-review creates
divergence that has to be reconciled twice, which is the same proportionality
judgement applied to itself.

### The general form, which outlives this document

**When a reviewed artifact grows, ask what the growth measures before treating
it as a problem.** Under a review that finds only real defects, size is a
readout of the input. The instinct to trim is an instinct to hide the readout —
and every local reviewer in the ladder can only ever add, because each asks a
local question. **Nothing in the design asks "is the whole thing worth its
weight?"** That question belongs to the owner, and it is a different question
from "is each clause correct."

## Round 5 falsified the convergence reading — and the stop-condition fired

`MEASURED-PRIOR`, `substrate-kit#580`. The hub session predicted convergence
from the finding curve **9 → 9 → 8 → 2** and set a stop-condition: *stop if the
next round finds a NEW defect class, not more of the same one.*

**Round 5 returned 6.** The convergence claim is falsified. "Not converging" is
not established either — five points with a bounce is not a trend — but **five
rounds and 34 findings without stopping** is the fact that matters.

**And the stop-condition fired, on its own terms.** The round-5 cluster is a
different diagnosis, not a fifth form of the gate defect:

- the distribution-wave trigger has **no observable event**
- per-adopter rollback state has **no source**
- `adopters.md` is generated agent-side, **cannot refresh in CI, and is 16 days
  stale**
- the impact mapping has no catch-all

That is not prose failing to describe a mechanism. **It is a specification
written over data the estate does not have** — and the stale generated file
settles the exporter question without any argument about proportionality.

**Two sessions converged independently** on the same three conclusions — ship
Layers 1–2 un-gated, drop the gate from v1, scope the exporter to facts it can
source — one from a failure corpus, the other from round-5 evidence, neither
having seen the other. Same shape as the three-session convergence behind
DISCOVERY RULE step 0.

## The permanent false positive: a checker cannot tell use from mention

`MEASURED`, three instances on 2026-08-06, in three different documents by two
authors:

| what tripped it | author |
|---|---|
| the `recording-a-wall` route firing on the commit documenting it | hub |
| a boot-file line refuting the kit's NOTE about the rules API — which returns 200 | hub |
| PL-015's example table of walls, in `substrate-kit#580` | the kit session |

One cause, and it has a precise name: **a checker over prose cannot distinguish
use from mention.** That is sharper than *"never mechanise meaning"* because it
says *which* meaning is out of reach. **A repo whose doctrine is "never write a
wall" will always contain documents that discuss walls, and its checker will
always flag them.** Permanent, predictable, and not a bug.

**Do not carve out an exemption.** The false positive has been **productive all
three times** — every instance forced the same fix, putting the repudiation in
the same clause as the phrase, and every time that produced *better* prose. An
ambiguous *"this is a wall"* became an unambiguous *"this was claimed and is
false."* The cost is a rewrite that improves the document; exemptions get gamed
and this noise is earning its place.

**The general form:** when a deterministic checker matches a *token*, it is
mechanising a token and not meaning — which is correct and gateable. Its false
positives land exactly where the token is **quoted rather than asserted**, and
that is a writing problem with a cheap fix, not a checker defect.

### Refinement, from instance four — which fired on this very section

Writing the paragraph above tripped it again. The table row for instance two
had quoted the offending token directly, with the word *refuting* beside it, and
the checker flagged it anyway. **A table cell is its own clause scope** — too
small to carry both a token and the sentence that repudiates it, because the
surrounding prose is out of scope.

**Then instance five fired on the fix.** The first draft of this very paragraph
*quoted the flagged row* in order to explain it — which reproduces the token one
more time. **Documenting a mention creates another mention**, so the incident
report has to be written without the trigger: **describe the claim, never quote
it.** That is where the recursion terminates, and only there.

So the workaround has a boundary worth knowing:

- **In prose**, put the refutation in the same sentence as the token. Works.
- **In a table cell, a heading, or a list item**, it often does not — the scope
  is too small to carry both. **Describe the claim instead of quoting the
  token.** The row now reads *"the kit's NOTE about the rules API — which
  returns 200"*, which is clearer anyway.

Two checkers also disagreed on it: fleet-manager's `check_no_false_walls.py`
returned **0** while the kit's `bootstrap.py check --strict` flagged it. Same
doctrine, different sensitivity — **so "the gate is green" is a claim about
*which* gate**, and running one is not evidence about the other.

## The hook's line needs an acceptance test, not just a length limit

Added 2026-08-06 after round 6, and it corrects a gap the hub left. The hook's
injected instruction was specified as **"one line"** — a *cost* constraint with
no *content* requirement. **Any one-liner satisfies that while preventing none
of the 11 corpus failures.**

The fix is the acceptance test already proposed for the skill, applied to the
hook itself:

> **A candidate line is admissible only if you can name which corpus failures it
> would have surfaced.** A line that scores zero does not go in.

That is deterministic, it uses evidence the estate already has, and it stops the
line being decorative — which is the same failure the gate work spent six rounds
demonstrating.

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
