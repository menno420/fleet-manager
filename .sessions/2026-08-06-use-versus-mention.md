# 2026-08-06 · hub — the false positive that keeps improving the prose

> **Status:** `complete`

- **📊 Model:** opus-5 · high · research

Time: 2026-08-06 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: the same false positive fired three times today, in three
documents, by two authors — and **every time the fix made the document better.**
That is rare enough to record as a property rather than tolerate as noise.

## The three instances

| what tripped it | author |
|---|---|
| the `recording-a-wall` hook route firing on the commit that documents it | hub |
| a boot-file line refuting the kit's NOTE about the rules API — which returns 200 | hub |
| PL-015's example table of walls, on `substrate-kit#580` | kit session |

**One cause, and it has a precise name: a checker over prose cannot distinguish
use from mention.**

That is sharper than *"never mechanise meaning"*, because it says **which**
meaning is out of reach. A repo whose doctrine is *"never write a wall"* will
always contain documents that discuss walls. Its checker will always flag them.
Permanent, predictable, not a bug.

## Why not to carve out an exemption

**The false positive was productive all three times.** Every instance forced the
same fix — put the repudiation in the same clause as the phrase — and every time
that produced better prose: an ambiguous *"this is a wall"* became an
unambiguous *"this was claimed and is false."*

So the cost is a rewrite that improves the document. Exemptions get gamed; this
noise is earning its place. Both authors reached the same workaround
independently, which is itself evidence it is the natural fix rather than a
contortion.

## Instance four: it fired on the section describing itself

Writing the section above tripped it a **fourth** time. The table row for
instance two quoted its token directly, with a repudiation word beside it, and
the checker flagged it anyway — because **a table cell is its own clause
scope**, too small to carry both.

**Then instance five fired on the fix**: the first draft of the refinement
*quoted the flagged row* to explain it. **Documenting a mention creates another
mention.** The incident report must be written without the trigger — describe
the claim, never quote it. That is the only place the recursion terminates.

So the workaround has a boundary: **in prose**, same-sentence refutation works;
**in a cell, heading or list item**, describe the claim instead of quoting the
token. The row now reads *"the kit's NOTE about the rules API — which returns
200"*, which is clearer anyway — the fix improved the prose for the fourth time
running.

And the two checkers disagreed: fleet-manager's `check_no_false_walls.py`
returned **0** while the kit's `bootstrap.py check --strict` flagged it. Same
doctrine, different sensitivity. **"The gate is green" is a claim about *which*
gate** — running one says nothing about the other, which is its own instance of
PL-015.

## The general form

When a deterministic checker matches a **token**, it is mechanising a token and
not meaning — correct, cheap, gateable. Its false positives land exactly where
the token is **quoted rather than asserted**. That is a *writing* problem with a
cheap fix, not a checker defect, and it is the boundary
MECHANISE FACTS / NEVER MECHANISE MEANING was already drawing without naming the
mechanism.

## Also this exchange

The kit session **verified** the claim that three of the gate's four clauses are
free rather than taking it — `lib/config.py:248`, a `{label, needle}` substring
list driven by `substrate.config.json`. The hub had flagged it as measured in
fleet-manager only, and asked for exactly that check. It held.

**Refinement to the stop condition, because it has already fired once.** The
hub's condition was *"a new defect class means escalate; more forms of the old
one does not."* Round 5 **was** a new class — the data-availability cluster — and
was discharged by rescoping the exporter. **If round 6 produces another new
class, that is not a third escalation; it is the answer to the proportionality
question.** Two new classes in two rounds means the spec's surface is still
unexplored, and § 9's ratio cannot be collected from a specification that keeps
changing shape.

## Verification

- `python3 tools/check_no_false_walls.py --strict` → **exit 0** — this card and
  the convention both discuss walls at length and pass, because every mention
  carries its repudiation in-clause. The workaround, applied to the document
  that describes it.
- `python3 tools/check_doc_routes.py --strict` → recorded at close
- `python3 bootstrap.py check --strict --require-session-log --simulate-added-card`
  → recorded at close

## Honest nulls

- **Three instances, one checker, one repo family.** Nothing establishes the
  rate, and "always" is a claim about a mechanism rather than a measurement.
- **PL-015's instance is `MEASURED-PRIOR`** — reported by the kit session, not
  read here.
- **Whether the workaround stays cheap at scale is untested.** Three rewrites
  were each a sentence; a document dense with quoted walls might not be.
- **No alternative was tried.** An exemption list, a context window around the
  token, or a mention-marker convention might all work; none was evaluated.

## ⟲ Previous-session review

The card before this recorded a prediction of mine that was falsified. This one
records a *noise complaint* that turned out to be a feature — and the two are
the same lesson from opposite ends: **read what a signal measures before acting
on what it feels like.** The growth number felt like waste and measured defect
density; this checker felt like noise and measured ambiguous prose.
