# 2026-08-29 — the Codex trigger corrected in all five places, and the model slot dated

> **Status:** `complete` — the wrong `@codex` trigger claim is corrected in
> every live copy (five, not just the boot file), and the date the `📊 Model:`
> slot started reading `withheld` is measured from the card corpus rather than
> recalled. **Two Codex rounds, 7 findings, all 7 `[conceded]`, zero
> `[survived]`** — 5 then 2, converging. **Flip exemption, declared:** the last
> reviewed SHA is `e15ea41`; after it come the two round-2 fixes, the
> path-asymmetry caveat, and this flip. Both fixes only *weaken* claims — a
> hedge and one integer — so nothing unreviewed asserts anything new.

- **📊 Model:** withheld · max · docs-only
- **⚑ Model-slot note:** this session's harness policy forbids a model
  identifier in any pushed artifact. See § *When the model slot changed* — this
  card is both an instance of that policy and the measurement of when it began.
- **📍 Venue:** cloud-container

## Mission

Two owner asks, both live:

1. *"Yes you can fix that thing about codex."* — the trigger claim flagged by
   [the previous card](2026-08-29-session-card-pr-test.md) (fm #974).
2. *"Review some other recent session cards; yesterday all sessions were still
   able to write down their model."* — establish when the change actually
   started, against the corpus rather than from memory.

## 1 · The Codex trigger — wrong in five live places, not one

**Owner, live, 2026-08-29:** *"Codex only reviews if you ask it to."*

The estate recorded the opposite. `.claude/CLAUDE.md` said *"Trigger: PR open,
draft→ready, or the literal comment `@codex review`"*, and it had said so since
2026-08-07. **fm #974 paid for it that day:** the session opened its PR READY on
the strength of that line and polled three API surfaces for a verdict that was
never coming.

The boot file was **one of five live copies**, and correcting only it would have
been this estate's own TRAP-008 — *a correction that leaves its own copies
standing* — committed by the session that had just read the trap:

| file | what it said |
|---|---|
| `.claude/CLAUDE.md` | *"Trigger: PR open, draft→ready, or the literal comment"* |
| `docs/CAPABILITIES.md` | *"Reviews trigger on PR open, draft→ready, and the literal comment"* |
| `docs/repos/spider-swing/capabilities.md` | *"Trigger: PR open, draft→ready, or the literal comment"* |
| `docs/repos/spider-swing/working-here.md` | *"reviews this repo's PRs on open, draft→ready, or the literal comment"* |
| `docs/prompts/chatgpt-couch-legend-project-instructions.md` | *"Codex reviews this repo (on PR open, draft→ready, or a literal comment)"* |

Four now say the same thing: **always post the `@codex review` comment; treat
the advertised auto-triggers as unreliable.** Session cards were left alone —
record tier, and a card records what a session believed on its date.

**`docs/CAPABILITIES.md` is the fifth and it is handled differently, because
editing it in place was wrong.** That file's § 5 states *"Re-verifications
APPEND, never edit"*, and its own 2026-08-23 row demonstrates the pattern —
marked as superseded with a ⚠ pointer, explicitly *"marked rather than
rewritten, per § 5's append-never-edit rule."* The first version of this PR
inserted 2026-08-29 evidence straight into the 2026-08-07 row while leaving its
`LAST-VERIFIED: 2026-08-07` untouched, which makes the ledger's own provenance
false — **the append-only rule broken inside the file that states it.** Caught
by Codex (P2), `[conceded]`. Now: the 2026-08-07 row is restored verbatim and
its trigger sentence carries a ⚠ supersession marker, and the correction lives
in a **new dated 2026-08-29 append entry**.

**A restoration re-creates what it restores.** Putting the old row back put the
wrong sentence back, and the copy check caught it on re-run — which is why the
marker exists rather than the row simply being reverted and forgotten.

### The correction was itself corrected, mid-session, by the reviewer

The first version of this edit asserted flatly that *"opening a PR does not
start a review, nor does draft→ready."* Then Codex's own summary comment landed
on this very PR and said the opposite, in its own about-box:

> Reviews are triggered when you — Open a pull request for review · Mark a draft
> as ready · Comment "@codex review" or "@codex security review".

So the vendor's configuration lists the two triggers the owner's statement
denies. **Rather than pick a side, this session measured the thing neither
source settles.** `MEASURED` 2026-08-29, all three read surfaces, with fm #967
as the positive control (2 reviews + 2 issue comments, so the query form works):

| PR | open window | Codex activity |
|---|---|---|
| fm #974 | **422 s** (READY `19:35:24Z` → merged `19:42:26Z`) | **0** — reviews, inline, issue comments all zero |
| fm #975 | 86 s | 0 — shorter than the relay, proves nothing |
| fm #977 | open, + `@codex review` | review **Running** within seconds, self-logged `Review trigger: Manual request` |

**Read the margin honestly: 422 s is only 87 s past the ~335 s relay.** That is
suggestive, not a clean null — a queued auto-review would plausibly be abandoned
when the PR merged, so #974 does not prove the auto-trigger is dead.

**The sharper measurement is #977's own timeline**, found only after the first
three were written, and it does not depend on relay latency at all:

```
19:57:21Z  PR #977 created, draft=false (READY)
19:58:08Z  manual "@codex review"            (+47 s)
19:58:23Z  Codex summary comment CREATED     (+15 s after the request)
```

A trigger produces the `Running` summary in **~15 s** — the review itself takes
~335 s, but the summary does not. The PR sat open and ready for **47 s** with no
summary comment in existence. An auto-trigger at open should have posted one by
about `19:57:36Z`. (n=1 on the 15 s figure, from this session's own request.)

**And the instrument that looked like evidence was not one.** The review-summary
comment is **edited in place** — one comment object, updated per review — and
its own header says it shows the *latest* activity. Reading three
`Manual request` rows across three heads therefore says nothing about what else
fired; an auto-triggered row would simply have been overwritten. The `created_at`
comparison above is the reading that survives.

**Two figures this session got wrong before getting right**, both the same
mistake — a window measured against the wrong clock. First, fm #974's session
polled **90 seconds** against a 335 s relay and correctly recorded that it had
established nothing. Then this card claimed **26 minutes** of silence on #974 —
but the PR was only *open* for 422 s of that; the remaining ~19 minutes it spent
merged, where no reviewer had any reason to look. Caught by the session's own
review hook before the card landed.

**One sub-finding worth more than the fix.** `spider-swing/capabilities.md`
carried the trigger list under a `MEASURED 2026-08-07` banner. The latency
(~335 s) and the inline-comment shape *were* measured — on a review someone had
**requested**. The trigger list was never measured by anything; it inherited the
banner by sitting under it. That is noted in place, because the same shape will
happen again.

## 2 · When the model slot changed — measured, not recalled

**Population: all 441 dated cards in `.sessions/`** as the committed tree holds
them — **including this card**, which is itself `withheld` and `cloud-container`.
Enumerated whole, not sampled (the directory README is not a card).
Fleet-manager only; other repositories keep their own cards, not visible here.

**Both corrections here came from the reviewer, and the second is the
interesting one.** The first draft counted 440/8 — a pre-card snapshot, a
whole-directory claim that excluded the file making it. The second: it reported
`cloud-container` as **12 named**, when the answer was **13 all along**. One
card's venue line reads `cloud-container, owner PRESENT`, and the counting
script split on whitespace without stripping the comma, bucketing that card
under `cloud-container,` as if it were a different venue. **The card was
mis-binned before this session's card existed** — so that figure was wrong for a
reason having nothing to do with the snapshot, and two independent errors
happened to live in one number.

**9 of 441 carry a `withheld` model segment**, and they are two unrelated groups:

- **3 older, different cause** — `2026-07-10` ×2 and `2026-08-11`, reading
  *"withheld per session policy (Fable-5 review wave…)"*. One of them **names
  Fable-5 in its own parenthetical**, so that was a review-wave convention, not
  a harness restriction.
- **6 consecutive and current**, the group that matters — the five below plus
  this card.

Ordered by **commit time** rather than filename date — which matters, because
the first one is *dated* 08-28 and was *committed* on 08-29:

| committed (UTC) | card | model segment |
|---|---|---|
| 2026-08-28 20:02 | `substrate-kit-od24-session4` | `opus-5` |
| 2026-08-28 21:39 | `claim-guards-reach-bash-authoring` | `opus-5` |
| **2026-08-28 22:00** | **`owner-intent-elicitation`** | **`opus-5` ← last named** |
| **2026-08-29 12:22** | **`estate-agent-error-audit`** | **`withheld` ← first** |
| 2026-08-29 13:14 | `audit-od26-reconcile` | `withheld` |
| 2026-08-29 13:19 | `audit-banner-counts` | `withheld` |
| 2026-08-29 15:42 | `fleet-orchestration-retro` | `withheld` |
| 2026-08-29 19:42 | `session-card-pr-test` | `withheld` |

**The transition window is 2026-08-28 22:00Z → 2026-08-29 12:22Z — about 14¼
hours, overnight.** Every card committed before it names a model; every card
committed after it withholds. Nothing in between.

**Venue does not explain it.** Cross-tabulated over the whole corpus with the
venue token normalised: `cloud-container` cards split **13 named / 6 withheld**,
so it is not a cloud-versus-laptop effect. Time is the only variable that
separates the groups — and note the conclusion was unchanged by the corrected
figures, which is exactly why the error survived a first reading.

**Count discipline:** these are **cards, not sessions** — one session can land
two, so **6 withheld cards in the current group is an upper bound on 6
sessions**, not a session count. (That denominator read `5` until Codex caught
it in round 2 — left behind by the very recount that fixed the totals above.
The count discipline this card preaches, failed by this card, in the paragraph
stating it.)

**What this does NOT establish.** Nothing here says *why*, and no dated
Anthropic documentation was found that mentions the restriction — checked
against the Claude Code changelog and Anthropic-controlled domains, with a
positive control confirming the same queries do return matches for the
attribution-trailer entries that exist. The web material that does describe an
"undercover mode" is third-party commentary on a leaked source, describes a
different scope (Anthropic-internal information, employee-gated), and is not
documentation.

## 3 · The instruction contradicts itself, and the squash hides it

The same harness that forbids a model identifier in a pushed artifact also
instructs: *end git commit messages with `Co-Authored-By: Claude <family> …`*.
That trailer **is** a model identifier.

`MEASURED` on fm #974/#975: the trailer reached
`origin/claude/session-card-pr-p8k89p` and is still readable there. It did
**not** reach `main`, because this repo's squash merge discards the commit body
— the landed commits carry only `<title> (#N)` and a `Head-ref:` line. **The
restriction held by accident of the merge strategy, not because the session
honoured it.** A repo that merges without squashing would carry the identifier
on `main` today.

The route around it is unchanged and costs nothing: `get_session` reports
`session_context.model` and `external_metadata.last_served_model`, and the
answer goes in the chat reply where it is allowed.

## What the two review rounds cost, and what they bought

**Round 1 on `aa17ccc`: 5 findings (3 P2, 2 P3), all `[conceded]`, zero
`[survived]`.** The sharpest was the append-only violation — this session edited
a dated entry in `docs/CAPABILITIES.md` in place, which its own § 5 forbids, in
the file that states the rule. Second sharpest: the `cloud-container` figure was
`12` and the answer was `13`, wrong for **two independent reasons** — a pre-card
snapshot, and a venue token reading `cloud-container, owner PRESENT` that the
counting script bucketed separately for want of a comma strip. Neither error
changed the conclusion the number supports, which is why both survived a first
reading.

**Round 2 on `e15ea41`: 2 findings (1 P2, 1 P3), both `[conceded]`.** The P2 is
the better one and it is a scope error this card kept making in miniature:
every copy claimed *both* advertised auto-triggers "did not fire", while both
observed PRs were **created** ready — `draft=false`, zero `ready_for_review`
events on either (`/issues/{n}/events`). **PR-open was probed; draft→ready was
never exercised.** All copies now say `UNMEASURED` for that path rather than
refuted. The P3 was the stale `5` denominator above.

**Landed at the two-round cap with the fixes applied but unreviewed.** The last
reviewed SHA is `e15ea41`; after it come the two round-2 fixes, the
path-asymmetry caveat below, and this flip. Both fixes are strictly
*weakening* — they replace claims with hedges and correct one integer — so they
add no assertion a reviewer has not seen.

**The caveat, owed before Codex asked and recorded here because it is the
weakest joint in the whole finding:** the ~15 s summary-creation latency is
`n=1` **and comes from the manual path only**. No observation exists of the
automatic path posting a summary. So "47 s of silence beats a 15 s post time"
assumes both paths post at the same speed — unverified, and the argument leans
on it.

## Verify

- `python3 bootstrap.py check --strict` → real exit code, read directly, no pipe.
- Corpus figures from a whole-directory enumeration of `.sessions/*.md` with the
  same `📊 Model:` regex the kit's own parser uses, and commit times from
  `git log --diff-filter=A` per file — not from filename dates, which is what
  moves `estate-agent-error-audit` across the boundary.
- Post-edit copy check. **The first version of this line claimed the re-grep
  left "only one hit", which was false** — `draft→ready` legitimately appears in
  8 live files, four of them the ones edited here (the corrected text names the
  trigger in order to qualify it) and four unrelated, where it means an agent
  flipping a PR out of draft. A bare phrase grep cannot separate those, so the
  copy check that actually ran was `grep -rn` for the *claim* phrasings
  (`Trigger: PR open`, `reviews trigger on`, `reviews this repo (on PR open`)
  and reading each hit.

## Layer-2 handoff

Layer-2 handoff: docs/repos/spider-swing/ — two files corrected
(`capabilities.md`, `working-here.md`), **no thread advanced**. The edit was an
estate-wide fact correction that happened to have copies there; spider-swing's
own threads (core feel & difficulty, the Play release) are untouched and stay
where the last session left them.

## ⟲ Previous-session review

Previous card:
[`2026-08-29-session-card-pr-test.md`](2026-08-29-session-card-pr-test.md)
(fm #974, merged).

**Held up on substance, and its flagged item is what this session executed.** It
declined to fix the boot-file line because its PR was scoped to one file, named
the contradiction instead, and the owner then authorised the fix — the flag
worked as a flag is supposed to.

**What it got wrong, corrected in chat but never written down:** it reported the
CI-failure event as having arrived *after* the flip push. Measured afterwards,
the event queued at `19:36:14Z` and the flip commit is dated `19:40:47Z` — the
event came **four and a half minutes earlier**, and the session had inferred an
ordering from its own reading order instead of comparing two timestamps it could
read. The card's own conclusions are unaffected; the habit is not.

**What it under-scoped:** it treated the boot-file line as *the* copy. There
were five. A card that flags a wrong claim should count the claim's copies
before calling the flag complete.

## 💡 Session idea

**This estate has a checker for false walls and none for stale duplicates.**
`tools/check_no_false_walls.py` is a required gate lane; TRAP-008 — *a
correction that leaves its own copies standing* — has now been recorded at least
three times (the audit banner counters on 08-29, this session's five Codex
copies, and the audit's own §9), and has no instrument at all.

The mechanical core is small and does not need to understand prose: when a diff
**removes** a distinctive phrase from one file, grep the tree for that same
phrase and print every other file still carrying it. No judgement about whether
those copies are wrong — just the list, so a session cannot fail to see them.
It is the same shape as the doc-route hook: silent when nothing matches, never
blocking.

**Why an idea and not an action:** OD-24 §3 says an agent does not add a gate
lane on its own initiative and OD-26 §13 puts mechanisms behind the revised
plan. It also wants measuring against the corpus first — how many of this
repo's past corrections would it have caught, and how many false positives does
a phrase-level match produce on a repo this quote-heavy?
