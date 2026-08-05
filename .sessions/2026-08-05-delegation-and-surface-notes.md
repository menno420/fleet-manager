# 2026-08-05 · hub — record two measurements the provider docs left open

> **Status:** `in-progress`

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

*(in progress — filled at close)*

## Verification

*(in progress — both gates, real exit codes, post-commit)*
