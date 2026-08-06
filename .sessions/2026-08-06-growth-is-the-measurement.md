# 2026-08-06 · hub — the doc doubling is the finding, not the fault

> **Status:** `complete`

- **📊 Model:** opus-5 · high · idea/planning

Time: 2026-08-06 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: I measured the review convention growing **+50 % in a day** and
read it as a proportionality risk. The owner read the same number as evidence
the mechanism works. **He is right, and the difference is not a matter of
emphasis — it changes what you do next.**

## The two readings

| | reads growth as | prescribes |
|---|---|---|
| mine | a cost signal — the doc is outgrowing its usefulness | **cut it in half** |
| his | a discovery signal — the input had that many defects | **leave it; this is the mechanism working** |

> *"We should not consider this as a fault in our plan, but exactly the plan
> working as intended."*

**Eighteen findings, every one verified correct, means the spec contained
eighteen real defects.** Had the reviews found nothing, the document would be
the size it started — and still broken. Length is the visible trace of the
input's defect density.

## The near-error, which is the part worth keeping

I had offered to run a subtraction pass targeting half the length. That would
have **deleted verified-correct content on the theory that length is itself a
defect** — the same species as writing a false wall: taking a signal and reading
it as a limitation.

Fourth time today I have come close to that shape. **First time it was caught
before I acted rather than after.**

## What survives the correction

The file is **two artifacts under one name**, with opposite constraints:

- the **record** — what was found, survived, refuted. Should grow.
- the **instruction** — what a session does at a decision surface. Must not.

While they share a file, the record's legitimate growth silently degrades the
instruction. The estate already has the separation: `docs/findings/` for
evidence, `docs/conventions/` for the rule, `doc-routes.json`'s `says` for the
sentence that reaches a session in the moment.

**So the fix is a split, not a cut, and costs no correct content.**

## Deliberately not done

**The split is deferred** until substrate-kit's spec lands. Restructuring both
copies mid-Codex-review creates divergence needing reconciliation twice — which
is the same proportionality judgement, applied to itself.

**And the self-consistency test is not added**, though it is a good idea: feed a
spec's own failing worked example to its own rule and confirm it fails. It
caught two P1s in one document (the vacuous gate, then an evidence record whose
six citations did not resolve). Adding it now would be a further addition to a
document under scrutiny for additions. It goes after the split.

## The general form

**When a reviewed artifact grows, ask what the growth measures before treating
it as a problem.** Under a review that finds only real defects, size is a
readout of the input, and the instinct to trim is an instinct to hide the
readout.

Structural reason it will keep happening: **every rung of the ladder asks a
local question** — is this clause implementable, is this claim sourced, what did
I not verify — so all of them can only add. **Nothing in the design asks whether
the whole is worth its weight.** That is a different question and it belongs to
the owner.

## Verification

- `python3 tools/check_doc_routes.py --strict` → recorded at close
- `python3 tools/check_no_false_walls.py --strict` → recorded at close
- `python3 bootstrap.py check --strict --require-session-log --simulate-added-card`
  → recorded at close
- Growth measured from git history: 1 595 → 1 883 → 2 391 words across three
  commits on `origin/main`; comparison set `.claude/CLAUDE.md` 2 027 words,
  `foundation-continuation.md` 2 424.

## Honest nulls

- **The "18 findings, all correct" figure is `MEASURED-PRIOR`** — reported by
  the session that ran the reviews. I verified only the one finding that
  targeted my own text.
- **substrate-kit's doubling is not measured here**, only reported.
- **Whether the mechanism is proportionate remains genuinely open.** This card
  argues the growth is not evidence against it; that is not the same as evidence
  for it. § 9's ratio settles it after rollout, and nothing settles it before.
- **The split is described, not designed.** No file boundary has been drawn.

## ⟲ Previous-session review

The card before this recorded a thing that reached everyone and was wrong. This
one records a reading that was wrong before it reached anything — and the
difference is that the owner was in the loop at the moment of judgement rather
than after the artifact shipped. **That is the presence model from
`docs/owner-profile.md` paying out exactly as described**, on the same day it
was written down.
