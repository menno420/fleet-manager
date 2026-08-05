# 2026-08-05 · hub — record two measurements the provider docs left open

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: `docs/providers/` and `docs/execution-surfaces.md` are the two
files this session should have read before writing a handoff skill, and did not.
Reading them late produced measurements they were explicitly waiting for — an
open question in the delegation finding now has data, and this surface's own
recorded weakness gained two more dated instances from the same session that
was supposed to be studying it.

## Previous-session review

The handoff-fidelity session (#764) fixed the boot path and the skill, but
promoted `continuation-prompt` to the kit without noticing that
`execution-surfaces.md` names that skill as one of its four consumers. The
promoted copy therefore carries surface-adaptation advice with no surface data
behind it. Recorded here rather than silently left.

## Scope

Append-only additions to two documents, both recording measurements this
session made:

1. `docs/findings/2026-08-05-gemini-delegation.md` — a third reject taxonomy,
   and the Vertex-vs-free-tier data-handling distinction.
2. `docs/execution-surfaces.md` — two more dated instances of the recorded
   "states a limit it has not tested" weakness, and the kit-promotion gap.

## What landed

- `docs/findings/2026-08-05-gemini-delegation.md` — a third reject shape, and
  the Vertex-vs-free-tier distinction on data handling.
- `docs/execution-surfaces.md` — two more dated instances of the recorded
  "states a limit it has not tested" weakness, plus the kit-promotion gap.

## Measured

**A third reject taxonomy.** Two Vertex runs (1,843,098 + 641,442 input
tokens; 82 verified / 6 rejected) produced rejects of a kind not in the
recorded set: **all six carried no citation at all** — file, line and quote
absent, rather than a mismatched or reconstructed quote. That is the benign
shape; the verifier drops it without needing a coverage judgement.

It is only weak evidence on the open short-quote question. The rule was in
force and no fabrication appeared — but no marker mismatch appeared either, so
the runs cannot separate "short quotes prevent reconstruction" from "this task
shape produced none." The rule stays unmeasured.

**The path matters for what may be delegated.** These runs used Vertex, so the
free-tier training caveat did not bind. Two public bot repositories went
through without the public-repo rule being the constraint — that rule still
holds for the free key.

**This surface's recorded weakness, twice more.** `execution-surfaces.md` said
on 2026-08-03 that this surface *"will state a limit it has not tested — twice
today, both caught by the owner rather than by a guard."* It happened twice
more on 08-05 in the session reading that very file: nine dependabot PRs
dismissed on a status doc's word, and a four-path read list treated as the
boundary of a comprehension task. **Four in three days, all owner-caught, none
guard-caught.** Both times the stopping force was a document that had already
concluded, not a measurement.

## Verification

- `python3 tools/check_no_false_walls.py --strict` → **exit 0**.
- `python3 bootstrap.py check --strict` → **exit 0**, run **post-commit**.

**Honest nulls.** The third reject shape is n=6 from two runs of one task
class; it does not establish a rate. The kit-promotion gap is **recorded, not
fixed** — shipping `execution-surfaces.md` as a kit template is the proposed
shape, not a landed change, and nobody has tested whether a template with
adopter-filled rows survives an upgrade cleanly.

## ⟲ Previous-session review

The handoff-fidelity session (#764) did the right repair on the boot path and
the skill, and still shipped `continuation-prompt` to the kit without noticing
that `execution-surfaces.md` names it as one of four consumers. The pattern is
the one this whole day keeps producing: a fix that is correct in the file it
touches and incomplete in the graph around it. The cheap counter is a question,
not a tool — **before promoting a doc or skill, grep for what points at it.**

## 💡 Session idea

**Make the estate's own weakness log a boot-time read for the surface it
describes.** `execution-surfaces.md` now records four dated instances of this
surface stating an untested limit, all caught by the owner. That is the single
most predictive fact available about how a session here fails — and it sits in
a document a session only opens when writing a prompt.

The cheap version is one line in the boot file naming the surface's own
top recorded weakness and where the log lives, so a session meets its most
likely failure mode before it starts working rather than after. It costs a
line, it needs no tooling, and unlike a guard it degrades gracefully: worst
case a session reads it and ignores it, which is exactly today's baseline.
