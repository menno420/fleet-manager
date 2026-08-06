# 2026-08-06 · hub — "free" was true on cost and false on scope

> **Status:** `complete`

- **📊 Model:** opus-5 · high · review/verify

Time: 2026-08-06 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: I told another session three of four gate clauses were **free**,
and it acted on that. Round 6 holed it. **I verified what the mechanism does and
assumed what it applies to** — which is PL-015's second corollary applied to a
claim instead of a script, on the day I helped write it.

## The error

I read the kit's session-card markers — a `{label, needle}` substring list
driven by config rather than code — and concluded the *presence* and
*Layer 2 occurred* clauses were free.

**They are free on cost and global in scope.** `missing_markers` scans **every
configured needle against every completed card**, and `check_added_card` calls
it on any added card. There is **no conditional form**.

So routing those clauses through markers does not implement §7c's conditional
trigger set. It silently implements **gate-every-card, in every adopter that
upgrades**, reddening work that never touched a decision surface.

The kit session **verified it in the tree rather than taking my word** — which
is exactly what I had asked for when I flagged the claim as measured in
fleet-manager only. It held on mechanism and failed on scope.

## Why this settles the open question

**My stop-condition has now fired twice.** Round 5 produced a new defect class
(data availability); round 6 produced several. By the refinement I stated — *a
second new-class round is the answer to the proportionality question, not
another escalation* — six rounds and 44 findings with the surface still
producing new classes means **§9's ratio cannot be collected from a
specification that keeps changing shape.**

And the finding removes the last argument for the cheap gate. *"Mostly free"*
was the entire case for building it now. What remains is a conditional checker
(six rounds of evidence that specifying it correctly is expensive) or
gate-every-card (a fleet-wide behaviour change nobody asked for). **Ship
un-gated.**

## The other one that was mine

Round 6: *"the hook's injected instruction is unspecified beyond one line —
any one-liner satisfies the spec while preventing none of the 11 failures."*

Correct. I gave a **cost** constraint and no **content** requirement. The fix is
the acceptance test already proposed for the skill, turned on the hook: **a
candidate line is admissible only if you can name which corpus failures it would
have surfaced.** Deterministic, uses evidence that exists, and stops the line
being decorative.

## The best finding of the round, and it was not mine or Gemini's

`git diff --name-only` **drops the source path on rename**, so moving a governed
file *out* of a triggered directory escapes both the trigger and the impact
class. Codex verified it with an actual `R100` test rather than asserting it.

That is a real hole in **any** path-triggered design, including the hook I
proposed, and no prose review reaches it.

## What landed

- `docs/conventions/adversarial-review.md` § gate — a scope callout: free on
  cost, global in scope, *do not describe a trigger set the mechanism cannot
  deliver*.
- Same doc — the hook's line now requires a corpus acceptance test, not just a
  length limit.

## Verification

- `python3 tools/check_doc_routes.py --strict` → recorded at close
- `python3 tools/check_no_false_walls.py --strict` → recorded at close
- `python3 bootstrap.py check --strict --require-session-log --simulate-added-card`
  → recorded at close
- The "three clauses are free" claim **never reached the repo** — it existed
  only in a chat block and PR bodies. What was landed and wrong is subtler: the
  gate section listed clauses and said nothing about scope, which is what
  produced the claim downstream.

## Honest nulls

- **Round 6's findings are `MEASURED-PRIOR`** — reported and verified by the kit
  session, not read here. I did not open `missing_markers` myself.
- **Six rounds is still a small sample**, and "the surface keeps producing new
  classes" is a reading of six points.
- **The rename hole is unfixed** in anything I have proposed; naming it is not
  closing it.
- **Whether gate-every-card would actually be harmful is unmeasured** — it is
  asserted from the shape of the mechanism, not from an adopter that tried it.

## ⟲ Previous-session review

Two cards ago I recorded a falsified prediction; one ago, a productive false
positive; now a claim of mine that another session built on and Codex holed.
**Three consecutive cards where the thing corrected was mine and the corrector
was not a person re-reading their own work.** That is the ladder's whole thesis,
demonstrated three times running against its own author.
