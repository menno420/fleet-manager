# What the substrate caught, and what only the owner could — one session, counted

> **Status:** `reference`
>
> Written 2026-08-07 at the owner's prompting. He observed that he can correct
> this estate's sessions without fail because he holds months of context, and
> that he built the enforcing checks precisely so he would **not** have to.
>
> This is that claim turned into a number. One session, both repos, everything
> enumerated so the count can be **checked rather than trusted** — which matters
> here, because the same session got three counts wrong by pattern-matching
> instead of reading.

## 0 · The owner's claim

> *"I know exactly what you can or can't do, and the list of what you honestly
> can't do is extremely small. Which is why I made sure there are so many
> enforcing checks all around to help me make sure that you notice certain things
> without the need for me to correct you all the time."*
>
> *"A known failure of claude is stating things as facts without properly trying
> it in multiple ways, but if you read the right documents etc which explain the
> right methods, you are usually very good at your job."*

Both halves are testable against a single session's record. Here they are.

## 1 · Caught by the machinery, with no owner involvement

Enumerated, not summarised:

| # | Instrument | What it caught |
|---|---|---|
| 1 | orphan checker (`check --strict`) | the external-review prompt was **unreachable from any read-path doc** — the exact failure the session had spent the morning fixing, landing on its own file |
| 2 | `route_docs.py` hook | fired on a `CAPABILITIES.md` edit; checked, and the entry passed |
| 3 | `route_docs.py` hook | stopped *"Codex isn't available"* being written from assumption — sent the session to `docs/providers/chatgpt.md` |
| 4 | CI session-card grammar | `records correction` is off-taxonomy for PL-004. **A local run structurally cannot catch this** — the leg fires only for cards newly added by the PR diff |
| 5 | `check_links.py` (curious-research) | Gemini's `start_span`/`end_span` citation artifacts, on first contact with the dossiers |
| 6 | `r30_merge_check.py` | returned `REVIEW` and refused to bless a workflow merge |
| 7 | `regen_b_files.py --check` | a notice pushed Custom Instructions **600 chars over its 8,000 hard cap** |
| 8 | `regen_b_files.py --check` | the same edit displaced the `DRIFT CHECK` stamp off line 1 |
| 9 | born-red session gate | held two PRs red until their cards flipped |
| 10 | Codex round 1 (fm #812) | 4 findings, incl. *the retirement did not retire anything* |
| 11 | Codex rounds 2–5 (fm #813) | 9 further findings, incl. **two live bugs** — a queued check wrongly exempted in the lander, and a BOOT step that would exit 1 by design on every fresh paste |

**Count: 11 instrument catches, 13 of them Codex findings.**

## 2 · Caught by the owner: one

**`@codex review` works.** The session waited 150 seconds, wrote *"no review
appeared in 150 seconds"* into a public PR comment **as if it were evidence about
the relay**, and merged the PR three minutes after requesting the review. The
review arrived at 335 seconds with four real findings, one of which proved that
PR did not do what its own title claimed.

The owner: *"What do you mean exactly about codex? If you mention @codex in a PR
codex will review it and answer."* He was right.

## 3 · The split is the finding, and it is not new — it is confirmed

**No checker could have caught the one he did.** No gate reports *"you did not
wait long enough."* No linter flags *"you asked for a review and merged three
minutes later."* Every structural error the session made was caught by the
machinery; the single thing that got past all of it was a **judgement call at a
decision point**.

That is [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md)
§ 2, restated with a ratio:

> **This estate instruments execution. It does not instrument judgement.**

And it matches the owner's own presence model (`owner-profile.md` § Presence
model): *"once a plan is made and the working method is locked in, I can easily
step away… but when it comes to planning and trying certain things, I still need
to pay attention."* Eleven execution catches without him; one judgement catch
that needed him.

## 4 · The boundary of the gate approach, measured

**Three counting errors passed every checker in this repo.** The roster banner
said `21 DARK / 3 UNREADABLE`, then `18 DARK / 10 n/a / zero UNREADABLE`; the
truth — read from the roster's **own generated verdict summary** — is
`18 DARK · 7 n/a · 3 STALE-BY-DESIGN · 1 STALE · 1 PRIVATE · 1 UNREADABLE · 0 LIVE`.
A fourth, the same day, mis-read the research dossiers as uniformly `SOLID` by
grepping for `LIKELY|CONTESTED` when the taxonomy was `COMMON|DISPUTED`.

Every one was **well-formed**. A checker validates form; all four wrong numbers
had impeccable form. Only **Codex** — a reviewer, not a checker — caught them,
and only because the owner said the relay existed.

`REASONED`: this is the practical ceiling of deterministic gates. They cover the
class where wrongness has a shape. A wrong number computed confidently has no
shape, which is why the estate's answer to it is adversarial review rather than
another checker.

**The generalisable error**, since it fired four times in one day: *searching for
a list of values you expect, then reporting the result as the whole
distribution.* The fix is not care. It is **enumerate what is present before
counting it** — and, in the roster's case, the artifact already stated its own
answer and was never read.

## 5 · The documents worked, and one shows their limit

`OWNER`'s second claim held. Three times a document turned a probable failure
into a non-event:

- `conventions/owner-drive-folder.md` — the Drive folder read first try, no
  Drive API, no probing, because the recipe was written down.
- `CAPABILITIES.md` — `cffi` breakage already recorded as *"repaired, not a
  wall"*; cost nothing.
- `providers/chatgpt.md` — settled the Codex-cloud surface question by reading
  rather than guessing.

**And the limit, from the same session.** It wrote the step-0 correction into
`CAPABILITIES.md` that morning — *a failed probe means you took the wrong path,
not that the owner was wrong* — quoted that rule back to him during the day, and
then declared a working tool unavailable eight hours later.

> **Knowing the rule, having just written the rule, and citing the rule did not
> prevent breaking the rule.**

A document only helps when something makes a session *reach* for it. That is why
the hooks exist, and why the hook that fired on Codex (#3 above) was worth more
than the ledger entry it pointed at. `REASONED`: the ratio in § 1 is not evidence
that documents work; it is evidence that **documents plus a trigger** work.

## 6 · Honest nulls

- **The classification is mine and is arguable.** Item 2 is a hook firing on
  something that turned out fine — counted as a catch because it forced a check
  that would otherwise not have happened. Remove it and the ratio is 10:1.
- **The denominator is unknown.** This counts errors that were *caught*. Errors
  neither the machinery nor the owner caught are unmeasurable by construction —
  the same `NOT-VERIFIABLE` false-negative rate as
  `2026-08-05-foundation-continuation.md` § 2. **The ratio says nothing about
  what got through.**
- **One session is one session.** A different task mix would move this. The
  direction is more defensible than the number.
- **The owner's own count is the stronger evidence** and is not in this file:
  across 2026-08-05 to 2026-08-07 he has flagged problems in agent output
  repeatedly, and the record shows **zero false positives**.
