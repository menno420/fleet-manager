# 2026-08-09 · hub — Layer-2 ratification, and the flip-before-review incident

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · docs-only — land the Layer-2 ratification; record the auto-merge incident

Time: 2026-08-09 · venue: owner-live hub chat · branch
`claude/fleet-manager-rules-enforcement-18o8t1` (restarted from `4e6a05a` after
fm #827 merged)

💡 Session idea: **the born-red card is not only a completeness gate — it is the
only thing holding a PR away from the automatic lander, and flipping it is
therefore an irreversible act.** Every written rule in this estate treats the
flip as a *bookkeeping* step performed at the end. It is not: it is the moment
the PR becomes merge-eligible, and anything you still intend to do to that PR —
Codex review above all — has to happen before it, not after.

Layer-2 handoff: null (fleet-manager itself; no satellite repo attached)

## Previous-session review

⟲ fm #827 recorded the owner's intent and amended two standing directives. It
landed correctly, but its close-out sequence was wrong in a way the card could
not see, and this session exists partly to fix what that cost.

## What is about to happen

Two things:

1. **Re-apply the Layer-2 ratification** that #827 lost — three surfaces still
   said *"awaiting owner sign-off on the shape"* after the owner signed off on
   it (`repos/README.md`'s coverage table, `working-here.md`'s PROPOSAL header,
   and the earned-files row calling it an open question). The commit was pushed
   ~55 seconds after the lander had already merged the PR, so it never reached
   `main`.
2. **Record the incident itself**, below, because it is a repeatable trap with a
   one-line fix.

Verification at close: `python3 bootstrap.py check --strict`, plus both checkers
directly, real exit codes — and **Codex review requested while this card is still
born-red**, which is the corrected order.
