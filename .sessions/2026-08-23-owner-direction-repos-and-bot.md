# 2026-08-23 — Owner direction captured, and this session's own D2 conclusion withdrawn

> **Status:** `complete` — branch `claude/active-projects-overview-kiftou`,
> cut from `origin/main` at `a8e0988` (fm #936). Born red on purpose: the card is
> the merge hold (TRAP-006), and it held while `@codex` answered — which is the
> only reason its six findings reached this tree instead of `main`. Flipped after
> `python3 bootstrap.py check --strict` returned a real exit 0 on this tree, read
> from a redirect and never after a pipe.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

The owner asked for oversight into the active projects, and in answering gave
**four pieces of direction that exist only in the chat transcript** — the exact
loss mode this repo's boot file records as entry 1b, where a plan set live on
2026-08-08 reached neither `CLAUDE.md` nor `README.md`, and a later session
walking the read path met a two-week-old plan instead.

This session records them, measures the one that makes a claim about the tree,
and answers a standing owner question his message resolves in passing.

## previous-session review

⟲ fm #936 (`a8e0988`, HEAD): the `idea-engine` notebook corpus and its
seam-count correction. Checked at `main` — present, and this branch was cut from
exactly `origin/main`. Nothing to repair.

Its closing lesson is the one this session had to apply first: *"an inference
that explains a real finding is still an inference."* The owner's directive here
carries an embedded claim about the tree — that the repos need documentation —
and the temptation was to accept it and start writing. **Measuring it first
changed the size of the work by an order of magnitude** (§ below), which is the
same move #936 wished it had made.

## What the owner said, and what was recorded

| His direction | Recorded as |
|---|---|
| The next bot: **review-oriented and small first**, cog-portable, **bots stay separated**; the two `superbot` repos consolidate into one new **repository** eventually | **OD-19**, plus an amendment at the head of the [pre-repository plan](../docs/planning/2026-08-21-game-community-bot/README.md) so a GCB session meets it before the headline |
| **Every repo earns its place**; the remedy is documentation + hub linking, not cuts | **OD-20**, which bounds OD-17 and closes OD-18's execution arc |
| *"so I will send the email tomorrow"*, deferred deliberately behind his setup work | **E1** status block, above the older 2026-08-01 note kept for provenance |
| The laptop as an AI-integrated workstation — his current priority | [`findings/2026-08-23-owner-direction.md`](../docs/findings/2026-08-23-owner-direction.md) § 4. **Not** an owner-queue entry — it is not an ask, and a permanent non-ask there reads as a blocker (`@codex`) |

**`OQ-FM-D2-TARGET` is NOT answered, and remains open.** This session recorded
it as answered by OD-20 and retargeted the NOW pointer to an all-repo front-door
sweep; **both were withdrawn the same session** on `@codex` review (§ below). His
words set an estate-wide *outcome* and select no repository. The queue entry, the
NOW pointer, OD-20's gloss and the current-state row all now say open, and the
entry records that it was briefly closed so a later session sees the error rather
than inheriting it.

## The measurement — and what `@codex` took away from it

`MEASURED` — all 17 non-archived repos, live default-branch trees via the
direct-PAT path. Method, limits and nulls:
[the back-link audit](../docs/findings/2026-08-23-front-door-audit.md).

**What survives review:**

| | |
|---|---|
| satellite READMEs naming this hub | **6 of 15** (`fleet-manager`'s own excluded) |
| `superbot` root README | **none** — the LIVE bot's repo |

The estate's linking is one-directional: `ESTATE.md` points outward to all 26
repositories; **9 of 15 satellite front doors point nowhere back.**

## `@codex` on this PR — 6 findings, 6 conceded, 0 survived

It answered at `23:11:25Z` on `287b206bb1`, ~9 min after the trigger comment and
past the measured ~335 s relay. **The verdict body was empty and the findings
were inline** — the shape `CAPABILITIES.md` already warns about.

**Every one of the six was right.** The tally is stated plainly because a
`[survived]` count of zero is the informative outcome here, not an
embarrassment to soften.

1. **`[conceded]` The D2 answer was my inference wearing his authority.** He
   stated a desired estate-wide *outcome*; he did not select a repository, and
   he did not say D2's one-repo acceptance test becomes an all-repo sweep.
   Marking `OQ-FM-D2-TARGET` ✅ recorded a `REASONED` reading as an owner
   decision — **the exact confusion `intent.md`'s provenance labelling exists to
   prevent, committed in the file whose job is to keep them apart.** Reverted in
   four places: the queue entry, the NOW pointer, OD-20's own gloss, and the
   current-state row.
2. **`[conceded]` The "four most-worked repos" ranking was unsupported and
   contradicted by this tree.** I derived it from **last-commit dates**, which
   cannot rank activity. The real 14-day merged-PR order was already recorded:
   `fleet-manager` 99 · `superbot` 64 · `websites` 19 · `couch-legend` 18 ·
   `spider-swing` **2**. My own 7-day sweep this session put `substrate-kit` at
   **0** — and I called it most-worked anyway. Withdrawn.
3. **`[conceded]` "The README back-link is the only channel" is overstated.**
   The satellite's **own** `.claude/` loads — that is in the same measurement I
   cited. So its boot file, `current-state.md` and orientation docs are live
   channels, and I searched **root READMEs only**. The supported claim is that
   the *hub's* apparatus does not auto-load; not that the nine are unreachable.
4. **`[conceded]` Presence cannot size truth work.** § 5's "twelve edits" framing
   invited exactly the mechanical sweep the intent audit's real failures rule
   out. Rewritten to say the file cannot size D2 at all.
5. **`[conceded]` The denominator was unreproducible.** 16 READMEs exist, the
   table had 15, and the method said "each of the 17". The exclusion —
   `fleet-manager`'s own — is now stated.
6. **`[conceded]` Staleness count off by one.** `curious-research` at 08-07 is 16
   days, not over three weeks. Three repos, not four.

## The root cause, which is worth more than the six findings

**[`2026-08-23-active-repo-intent-audit.md`](../docs/findings/2026-08-23-active-repo-intent-audit.md)
was written hours earlier the same day, in this repository, and I never opened
it before drafting a finding on the same question.**

It is strictly better grounded: it ran **D2's actual acceptance test** across all
17 repos (7 pass · 5 unrated · 1 stale · 3 fail · 1 hub), judged from contents
rather than file presence, fixed two failures the same day, and derived D2's
order — `product-forge` → `estate-backups` → the `websites` date stamp. Three of
my six findings would not have existed had I read it: the ranking (it holds the
correct measurement), the sizing (it holds the real failures), and the whole
premise that D2 needed a new target (it had already supplied one).

**The new file is now demoted to a supplement** and opens by pointing at it. Its
one genuinely new contribution is the *direction* of the linking, which that
audit did not measure.

**How this was missed:** I searched `docs/repos/`, the program, the queue and the
boot path, and never listed `docs/findings/` for today's date — while the estate
had merged **19 PRs in the preceding 14 hours**. `TRAP-001` covers a dated
document read as current; this is its neighbour — **a current document not read
at all because the session assumed it knew the corpus.**

## Round 2 — 6 more findings: 5 conceded, 1 partial

It re-reviewed the merge preview (`5a3f0878`) at `23:26:36Z`.

7. **`[conceded]` The withdrawn D2 closure was still in this card**, in present
   tense, in the summary table and the title — while § 64 said the opposite.
   A later session could have recovered the exact false owner decision the
   correction existed to remove. Title and table fixed.
8. **`[conceded]` The laptop thread was filed on the wrong surface.**
   `docs/owner-queue.md` is for decisions and manual actions genuinely waiting on
   him; a permanent entry that says *"not an ask"* reads as a blocker that never
   clears. Moved to
   [`findings/2026-08-23-owner-direction.md`](../docs/findings/2026-08-23-owner-direction.md),
   which is the pattern OD-17/OD-18 already use.
9. **`[conceded]` The back-link conclusion still overreached its own nulls.**
   The result is *nine READMEs do not contain the literal string* — not "point
   nowhere back", which the file's own § 6 already contradicted.
10. **`[conceded]` I misdescribed the primary audit as covering all 17 repos.**
    Its verdict classes name **16**; its headline says *7 pass* while naming 6.
    **`spider-swing` has no verdict at all** — the one repo with a live external
    clock is the unclassified one.
11. **`[conceded]` And I said it fixed two of three failures.** It fixed
    `idea-engine` (a failure) and `sim-lab` (the *stale* row) — so **one** of
    three failures. `product-forge` and `estate-backups` remain open failures,
    which understated the open D2 work.
12. **`[partial]` The bot amendment does not actually reorder the work.**
    Correct, and now recorded with the measurement: `delivery-roadmap.md` puts
    the AI spine in Phase 1, community/safety through Phase 4, and the **game
    testing loop — OD-19's first slice — at Phase 5.** Telling Phase 0 to "size
    for" the review bot leaves the executable order contradicting the owner.
    **Not re-sequenced here**, and the reason is stated in the plan: OD-19 is one
    sentence, "review oriented" is unspecified, and inventing that scope would be
    manufacturing product intent (`intent.md` § 8b). Recorded instead as the
    first thing a GCB session does, with OD-19 named as the winner while they
    disagree.

**Running total across both rounds: 12 findings · 11 conceded · 1 partial · 0
survived.**

## What landed

- **OD-19 and OD-20** in the program's directive table (now 20 rows).
- **The bot plan amended at its head** — scope, cog portability as a Phase 0
  acceptance question, and the separation constraint. GCB-1 untouched; nothing
  here authorises creating the repository.
- **`OQ-FM-D2-TARGET` left OPEN**, with the withdrawal recorded in the entry so
  the next session sees that it was briefly closed and why that was wrong, plus
  the intent audit's order as unblocked work.
- **E1** restated with his reason — it did not slip, he re-ordered it.
- **His laptop-as-AI-workstation thread recorded** in
  [`findings/2026-08-23-owner-direction.md`](../docs/findings/2026-08-23-owner-direction.md)
  § 4, alongside all four quotes verbatim — explicitly not an ask, and
  explicitly not licence to reconfigure his machine. **Not** an owner-queue
  entry: that surface is for decisions actually waiting on him.
- **The back-link audit**, demoted to a supplement, carrying its own withdrawals.

## Verification

- `python3 bootstrap.py check --strict` → **real exit 0**, read directly, never
  after a pipe.
- Telemetry delta committed, not reverted; every appended line parses as JSON.

## The lesson

**A directive can carry a factual claim, and the claim is checkable even when the
directive is not — but checking it does not make my reading of the directive his
decision.** I did the first half well (measuring "each repo needs documentation"
changed what the work was) and then failed the second half in the same commit, by
writing `✅ ANSWERED` over an inference. Verification of the premise and
provenance of the instruction are two different disciplines, and being right
about one bought nothing on the other.

**And the cheaper lesson: list the corpus before claiming to have read it.** A
finding written hours earlier, in this repo, on this question, would have
prevented half of what `@codex` had to catch. `ls docs/findings/ | tail` costs
nothing. The estate's fastest-moving day was the day its records were most worth
checking, and I treated familiarity as coverage.
