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

## The incident — flip-before-review, `MEASURED` on fm #827

| time | event |
|---|---|
| `19:06:39Z` | `@codex review` requested on #827 |
| `19:07:01Z` | **`merge-on-green` merged it — 22 seconds later**, actor `github-actions[bot]`, at head `a0bac75` |
| `19:07:55Z` | the Layer-2 ratification commit pushed — to a branch whose PR was already merged; it never reached `main` |

**No session merged anything early, and no rule was broken as written.** The
boot file says *"never merge a PR you have asked Codex to review before it
answers"*, and nothing did. What happened is one step earlier: **the card had
already been flipped to `complete`**, and the flip is what makes a PR
merge-eligible. `merge-on-green` then did exactly its job.

The mistake is a **sequence** error, and its root is that every written
description of the close treats the flip as end-of-session bookkeeping.
`session-close` step 7 said *"flip … green then merges server-side"* — accurate
and incomplete: it never said that the born-red hold is the only thing keeping
the automatic lander away, so anything still owed to the PR must precede the
flip. Committing a review request *after* the flip is racing a server-side
process, and 22 seconds is the size of the window.

**Fixed in the procedure, not in prose:** `session-close` gains step **6c** —
everything owed to the PR happens before the flip, review included, with the
measured timing above as its reason — and step 7 now ends with *"after the flip,
treat the PR as gone."* This PR runs the corrected order as its own first test.

**Two second-order facts worth keeping:**

- **The PR API read was stale and would have hidden this.** `GET /pulls/827`
  returned head `a0bac75` and `mergeable_state: unknown` *after* the push to
  `ff0a16d` had succeeded; `git ls-remote` returned `ff0a16d` immediately. The
  merged state only surfaced because the read was cross-checked against the ref
  — which is the `CONSTITUTION` rule about staleness-sensitive reads, earning
  itself again.
- **`git_state_guard` fired correctly on the recovery force-push** and named all
  four at-risk files. The answer was a tree comparison, not reassurance: three
  doc files byte-identical between the discarded head and the new one, so the
  content survived the restart.
