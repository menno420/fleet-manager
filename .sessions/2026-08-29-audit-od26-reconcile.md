# 2026-08-29 — the agent-error audit reconciled against OD-26, and its §1 scope named

> **Status:** `in-progress` — born-red. Follow-up to fm #967, which merged on
> green while this work was in flight; the branch is restarted from the merged
> `main` per the merged-PR discipline and this is a new change, not a reopen.

- **📊 Model:** withheld · high · review/verify
- **⚑ Model-slot note:** the harness policy for this session forbids a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container

## Mission

Two corrections the merged audit
([`docs/findings/2026-08-29-estate-agent-error-audit.md`](../docs/findings/2026-08-29-estate-agent-error-audit.md))
does not carry, both authored after `merge-on-green` fired on `0a5b14ef`.

1. **Reconcile against OD-26.** The owner's discussion sitting
   ([`2026-08-28-od24-sitting-answers.md`](../docs/findings/2026-08-28-od24-sitting-answers.md),
   fm #964) landed *after this audit launched and before it merged*. He gave
   **one root cause** — *"agents don't take enough initiative to leave the repos
   in a better shape"* — where the audit assumed a gap taxonomy, and his sitting
   records that the round *"reproduced, on itself, the exact defect it was
   auditing."* The audit is **reframed rather than defended**: a new §8
   reconciles it, and §9's recommendation is judged by **his** test (*does this
   make a session more likely to leave the repo better?*) instead of by gap
   class. Checked deliberately against his **Move 1 hold**, which covers the
   *function* rather than the filename: tool-time delivery is not a close-time
   declaration, so the recommendation is not held work.
2. **Name §1's population.** The section's conclusion was correctly scoped in
   its table and unscoped in its heading. Issue comments were enumerated across
   **6 of 28 repositories**; review comments across all 12 that have any. The
   extension to the other 22 is `REASONED` from the credential mechanism, not
   measured. Heading narrowed, and the gap added to §7.

## Why this is a new PR

fm #967 **merged** (squash `06d29b0b`) at 12:22:52Z, on `0a5b14ef`, while the
OD-26 reconciliation was being written and pushed. A merged PR cannot carry
follow-up work, so the branch was restarted from the merged `main` and the one
unmerged commit reapplied onto it. Nothing is reopened and nothing is
duplicated: `git diff` against `main` is these two corrections only.

## Not done here

No trap registered, no route, no checker, no skill edit. The five trap
candidates stay proposals, owner-gated under the roadmap's §6 promotion rule and
OD-26 §7's hold.
