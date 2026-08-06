# 2026-08-06 · hub — round 5 falsified my prediction, and my own stop-condition fired

> **Status:** `complete`

- **📊 Model:** opus-5 · high · review/verify

Time: 2026-08-06 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: I told another session its Codex findings were converging and
set a stop-condition. **Round 5 went the other way.** Recording a falsified
prediction is cheaper than defending it, and the stop-condition I supplied now
answers the question the owner was being asked.

## The prediction, and what happened

I read the curve **9 → 9 → 8 → 2** as convergence and wrote: *stop if round 5
finds a NEW defect class, not more of this one.*

**Round 5 returned 6.** My convergence claim is falsified. Their "not
converging" is not established either — five points with a bounce is not a
trend. What is established: **five rounds, 34 findings, and it has not
stopped.**

## The stop-condition fired on its own terms

The round-5 cluster is a **different diagnosis**, not a fifth form of the same
defect:

- the distribution-wave trigger has **no observable event**
- per-adopter rollback state has **no source**
- `adopters.md` is generated agent-side, **cannot refresh in CI, 16 days stale**
- the impact mapping has no catch-all

Not prose failing to describe a mechanism — **a spec written over data the
estate does not have.** The stale generated file settles the exporter scope on
its own, without any proportionality argument.

## The finding that corrects something I landed

> *"I built a script last round specifically to stop verifying by re-reading,
> then pointed it at the wrong file."*

`docs/conventions/adversarial-review.md` said **verify by script, not by
reading**. That is incomplete, and this is the proof: the script was correct and
the **target** was assumed. § 8 names the session card; the script opened a
standalone `docs/reviews/` file. Both failed, and the green script said nothing
about either.

**The script's target is itself a claim — and the one most likely to be assumed
rather than checked.** Worse than the original failure, because a passing script
*feels* like mechanical verification. Rule corrected in place: derive the target
from the rule text, never from memory of what the rule meant.

## Independent convergence

That session recommended — **before seeing the hub's block** — ship Layers 1–2
un-gated, drop the gate from v1, scope the exporter to facts it can source. The
hub reached the same three from a failure corpus and trigger scoring. Neither
saw the other. Same shape as the three-session convergence behind DISCOVERY RULE
step 0, and worth more than either analysis alone.

## Verification

- `python3 tools/check_doc_routes.py --strict` → recorded at close
- `python3 tools/check_no_false_walls.py --strict` → recorded at close
- `python3 bootstrap.py check --strict --require-session-log --simulate-added-card`
  → recorded at close

## Honest nulls

- **All `#580` figures are `MEASURED-PRIOR`** — 34 findings "all correct" is
  self-reported by the reviewed session. I verified only the one finding that
  targeted my own text.
- **Five rounds is a small sample and the bounce may be noise.** Nothing here
  establishes a trend in either direction.
- **The exporter data claims are second-hand** — I did not read `adopters.md`,
  `currency.py`, or the registry myself.
- **Whether dropping the gate is right remains the owner's call.** Two sessions
  agreeing is corroboration, not proof, and both are the same model family.

## ⟲ Previous-session review

The card before this recorded a reading that was wrong before it reached
anything. This one records a **prediction** that was wrong after it reached
another session — I told them the curve was converging and they acted on it for
one more round. The mitigation was already built in: **the stop-condition
travelled with the prediction**, so the wrong call had a bounded cost. That is
the only thing that made this cheap, and it is worth doing every time a
prediction leaves this session.
