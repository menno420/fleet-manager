# 2026-08-29 — the agent-error audit reconciled against OD-26, and its §1 scope named

> **Status:** `complete` — landed after two Codex rounds on this PR (8 + 9
> findings, **all 17 `[conceded]`, zero `[survived]`**; 37 across four rounds
> counting fm #967's two). **Flip exemption, declared:** the last reviewed SHA
> is `52a375a2`; after it come only the R2 fix commit — nine mechanical
> corrections, each named in the thread — and this flip. **No third re-review
> is requested**, and the reason is stated in the thread: severity converged to
> zero P1s while count stayed flat, because each round's fixes were creating the
> next round's stale copies — which is this audit's own TRAP-008.
>
> Follow-up to fm #967, which merged on
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

## ⟲ Previous-session review

Previous card:
[`2026-08-28-estate-agent-error-audit.md`](2026-08-28-estate-agent-error-audit.md)
(fm #967, merged `06d29b0b`).

**Held up on the substance.** Its finding survived 20 external review findings
across two rounds with all 20 conceded, and the two P1s that overturned
conclusions were answered by re-measuring rather than by hedging — the adopter
census and the corpus recount both landed as numbers.

**Three defects it carried into `main`, which this card exists to close or
name.**

1. **It never met OD-26.** The owner's sitting merged as fm #964 *while that
   session was writing*, and the session read it only at the very end — after
   the finding's §8 recommendation had already been framed in the gap taxonomy
   his answer retired. The reconciliation was written but lost the race with
   `merge-on-green`. Closed here.
2. **§1's heading outran §1's table.** The table said *"6 busiest repos"*; the
   heading said *"on GitHub"*. The session then repeated the unscoped form in
   its own reporting — the audit's own *"the qualifier that does not survive the
   copy"* pattern, committed twice by the session that named it. Closed here.
3. **It misread a merged PR as a lagging one.** For roughly twelve minutes it
   polled `mergeable: null` / `head: 0a5b14ef` and diagnosed GitHub-side PR-ref
   lag, posting that diagnosis to the PR. The PR had been **merged** at
   12:22:52Z. The `/git/ref` read it used as its authority answered a different
   question (branch tip) than the one it was asking (PR state), and the poll
   printed `head.sha`, `mergeable` and `mergeable_state` while never reading
   `state` — which the same response carried.
   **Scoped precisely, because the first cut of this line overstated it:** the
   PR was `closed` from **12:22:52Z onward**, which covers the later poll
   iterations for certain. The session did not record per-iteration timestamps,
   so how many of the earliest iterations preceded the merge is **unknown** —
   "unread the whole time" was written and is withdrawn. **CLOSED where it was
   delivered:** a correction is now posted on the merged #967 thread beside the
   original, which stands. Codex (fm #968) was right that a card is not
   discoverable from that thread, so recording it here alone left the false
   claim delivered and uncorrected.

## 💡 Session idea

**A gate lane for "the record you are citing moved while you wrote".**

Three of this two-session sequence's errors share one shape and none is in the
trap register: fm #963 merged and fixed the route gap §4 was measuring; fm #964
landed the owner ruling that retired §8's frame; fm #967 itself merged while its
own follow-up was being pushed. Each time the session cited a state that had
been true when it started reading.

The mechanical part is small and decidable: at gate time, for every `#NNN`,
40-hex SHA or `docs/**` path a diff cites, compare the cited object's current
state against the session's branch point — and warn when it moved. It is the
write-side sibling of TRAP-001, whose routes fire on `MEASURED` phrasing and so
never see a citation that was accurate at authoring time and is stale at merge
time.

**Why it is an idea and not an action:** it is a new gate lane in every adopter,
which OD-24 §3 says an agent does not introduce on its own initiative, and
OD-26 §7's hold makes the bar higher rather than lower. It also needs the
measurement §9 already recommends — run it against this corpus first and count
how many incidents it would actually have caught.
