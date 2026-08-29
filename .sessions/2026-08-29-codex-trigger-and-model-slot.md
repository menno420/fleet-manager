# 2026-08-29 — the Codex trigger corrected in all five places, and the model slot dated

> **Status:** `in-progress` — born red. **What is about to happen:** the wrong
> `@codex` trigger claim is corrected in every live copy (not just the boot
> file), and the date the `📊 Model:` slot started reading `withheld` is
> measured from the card corpus rather than recalled.

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

All five now say the same thing: **always post the `@codex review` comment;
treat the advertised auto-triggers as unreliable.** Session cards were left
alone — they are record tier, and a card records what a session believed on its
date.

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

| PR | how it was opened | Codex activity |
|---|---|---|
| fm #974 | **READY**, 19:35:24Z | **0** after 26 minutes — reviews, inline, issue comments all zero |
| fm #975 | READY, 19:44:20Z | 0 (merged after 86 s — too short to count) |
| fm #977 | READY + `@codex review` | review **Running** within seconds, self-logged `Review trigger: Manual request` |

26 minutes against a ~335 s relay is not a window effect. **The advertised
auto-trigger did not fire; the manual one did.** The owner was right about
behaviour, the boot file was right about configuration, and the useful rule is
neither of those: *ask, and you never have to know which.*

**Note what the earlier evidence was worth.** fm #974's session polled 90
seconds and stopped — that established nothing, and the card said so. The
26-minute figure is a genuine measurement only because the PR sat there long
after everyone stopped watching it.

**One sub-finding worth more than the fix.** `spider-swing/capabilities.md`
carried the trigger list under a `MEASURED 2026-08-07` banner. The latency
(~335 s) and the inline-comment shape *were* measured — on a review someone had
**requested**. The trigger list was never measured by anything; it inherited the
banner by sitting under it. That is noted in place, because the same shape will
happen again.

## 2 · When the model slot changed — measured, not recalled

**Population: all 440 dated cards in `.sessions/`**, enumerated whole, not
sampled (the directory README is not a card). Fleet-manager only — other
repositories keep their own cards and are not visible from here.

**8 of 440 carry a `withheld` model segment**, and they are two unrelated groups:

- **3 older, different cause** — `2026-07-10` ×2 and `2026-08-11`, reading
  *"withheld per session policy (Fable-5 review wave…)"*. One of them **names
  Fable-5 in its own parenthetical**, so that was a review-wave convention, not
  a harness restriction.
- **5 consecutive and current**, the group that matters.

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

**Venue does not explain it.** Cross-tabulated over the whole corpus:
`cloud-container` cards split **12 named / 5 withheld**, so it is not a
cloud-versus-laptop effect. Time is the only variable that separates the groups.

**Count discipline:** these are **cards, not sessions** — one session can land
two, so 5 withheld cards is an upper bound on 5 sessions and not a session
count.

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

## Verify

- `python3 bootstrap.py check --strict` → real exit code, read directly, no pipe.
- Corpus figures from a whole-directory enumeration of `.sessions/*.md` with the
  same `📊 Model:` regex the kit's own parser uses, and commit times from
  `git log --diff-filter=A` per file — not from filename dates, which is what
  moves `estate-agent-error-audit` across the boundary.
- Post-edit re-grep for `draft→ready` across all live `.md`: the only remaining
  hit is the new text stating that draft→ready does *not* trigger a review.

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
