# AGENTS.md — DRAFT for the future `estate` hub

> **Status:** `draft-for-owner-review` — this is proposed shared agent policy
> for `estate`, stored in fleet-manager only as planning evidence. It does not
> replace fleet-manager's current instructions before the cutover.

## Start here

`README.md` is the recommended front door, not a mandatory reading ladder. The
tree and role-named folders must be sufficient for a cold agent to find purpose,
live state, and the next action without a prescribed document sequence. Read
the vendor delta for the surface you are actually using when its context or
access matters: `CLAUDE.md`, `codex.md`, `gemini.md`, or `grok.md`.

If a statement would be true in two vendor files, it is shared policy and
belongs here instead. Vendor files contain only differences in context loading,
access, and surface limits.

## What this hub is

`estate` is the owner's cross-repository map and records home. It records what
each repository is for, what is true now, decisions, plans, ideas, evidence,
owner attention, and handoffs. Product code and detailed product truth stay in
the product repository.

The merged target repository is truth for implementation state. This hub is
truth for estate-wide routing and provenance. If they disagree, report the
disagreement; do not silently choose the more convenient copy.

## Write for the owner

The owner directs and reviews; do not assume he programs. For every topic on
which you take a position, state in plain language:

1. how you see it;
2. what you suggest;
3. one guiding question.

Mark his quoted words `OWNER`. Mark session inference `DERIVED` and make it easy
to replace. An honest null is a deliverable. Do not fill an unknown with a
plausible guess.

## Put each kind of truth in one role

- `owner/`: only things needing the owner's words, choice, or triage.
- `repositories/`: purpose and routing for each external repository.
- `state/`: facts true now.
- `plans/`: intended future work with explicit status.
- `decisions/`: settled choices and their provenance.
- `ideas/`: possibilities not yet promised.
- `evidence/`: dated findings, audits, experiments, and research.
- `practices/`: estate-specific ways of working and traps.
- `tools/`: implementations of checks, generators, and migrations.
- `sessions/`: in-progress and recent handoffs.
- `archive/`: frozen history, excluded from default search.

Do not copy the same fact into several front doors. Link to its canonical home.
Generated files declare themselves and must be regenerated, never hand-edited.

## Work and landing

Create a session card as the first commit, with `in-progress` status. Use one
ready pull request for the session. Run the repository's strict check and read
the command's real exit code. Ask for review before completion. Resolve or
record each review finding. Flip the card to `complete` in the final commit.

Do not weaken a gate to make a change pass. A born-red session hold is a safety
state, not a defect. Keep unrelated user changes intact.

## Judgment and safety

Act on reversible work inside the requested scope. Ask the owner when a choice
depends on his intent, spends meaningful money, publishes externally, changes
access, or destroys material. State the exact failed operation before calling
something impossible; re-check recorded capability walls when their evidence is
stale or the surface has materially changed.

Archive tools may surface candidates and rewrite links. Only a person may judge
that a file has no remaining value and authorize its move.

## Keep the hub small

Prefer a short canonical record plus evidence links over another summary. Fix a
small adjacent defect when it is clearly in scope; record a large one for later.
Promote repeated, proven practice to the shared kit. Do not build permanent
machinery for a one-off inconvenience.
