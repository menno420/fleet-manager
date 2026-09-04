# 2026-09-04 — Spider Bot becomes the AI operations bot of the Slingy Spider test server

> **Status:** `in-progress` — branch `claude/spider-bot-ai-ops-sthix0`, born red.
> Flipped to `complete` as the deliberate LAST step, after the spider-bot PR is
> green and the estate records are reconciled.

- **📊 Model:** opus-5 · xhigh · feature build
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01YCXH5D4omEgguaPYHwVz6d](https://claude.ai/code/session_01YCXH5D4omEgguaPYHwVz6d) · "Spider Bot AI operations bot"

**What this session is about:** the owner gave Spider Bot its purpose, and it is
newer than every record in this repo. Spider Bot exists to **manage the Slingy
Spider server and help during testing of the game** — a reliable automoderator
with heavy AI integration, that people can talk to naturally for guidance,
complaints, bugs, feedback and improvement ideas, whose reports become durable
and easy for the developer to find and act on, preferably through GitHub. That
answers the question [`docs/repos/spider-bot/intent.md`](../docs/repos/spider-bot/intent.md)
has carried as *"DRAFT, awaiting his words"* since 2026-08-28, and it narrows
the [game-community-bot plan](../docs/planning/2026-08-21-game-community-bot/README.md)'s
multi-game breadth rather than extending it.

This card covers the fleet-manager half. The implementation half lands in
`menno420/spider-bot` on the same branch name, with its own card.

## Live state read at session start — `MEASURED` 2026-09-04T12:08:06Z

| repo | main | open PRs |
|---|---|---|
| `menno420/spider-bot` | `bf4d75278a74` (2026-08-25) | 0 |
| `menno420/spider-swing` | `fc64a3fbb25f` (2026-08-23) | #180 (dependabot) |
| `menno420/fleet-manager` | `caa6cd2ab659` (2026-09-03) | #1020 |

Three counts in this repo's own records were re-derived and are wrong:
spider-bot has **20 commits, not 5**; **246 tests, not 78** (the Layer-2 entry
point) and **not 116** (the repo's own README); and the `/home` panel, route
registry, closed-test clock and membership memory that the entry point lists as
*"candidates on the table"* all **shipped 2026-08-24/25**.

## What was done

**Three PRs, one purpose.**

| PR | What |
|---|---|
| [fleet-manager#1021](https://github.com/menno420/fleet-manager/pull/1021) | The records: `intent.md` answered, `[D-0042]`, `OQ-GCB-REVIEW-SCOPE` closed, the Layer-2 entry point re-derived |
| [spider-bot#3](https://github.com/menno420/spider-bot/pull/3) | The build: 19 commits, +13,190 lines, 246 → 647 tests |
| [spider-swing#181](https://github.com/menno420/spider-swing/pull/181) | The producer half of the support feed: a versioned, fail-closed cross-repo contract |

**The build, in dependency order.** Shared foundations (stable ids, a storage
seam, a GitHub client, typed AI verdict contracts, a policy layer, correlation)
→ the developer feedback loop (one intake service behind every entry point,
conversational filing, privacy classification, store-first, idempotent GitHub
projection) → the AI moderation foundation (event logging, classifier,
deterministic policy evaluator, shadow mode, one case model, a staff review
surface) → the game-knowledge seam → run-evidence import. Nothing new enforces
on arrival: moderation ships `off`, the autonomy ceiling ships at
`flag_for_review`, the GitHub path is fail-closed until a credential exists.

**The adversarial review is most of what this session actually was.**

- **8 lanes** (`fleet-preflight` run first; concurrency measured at 2, so the
  fleet was spent on design and review rather than parallel implementation) plus
  a synthesis pass: **41 findings**, every one reproduced here before it was
  touched, every fix carrying a test verified to fail when the fix is removed.
- **1 Codex round** at flip-readiness: **15 more** (5 P1, 10 P2), all fifteen
  reproduced and fixed. That is the number that matters: Codex found fifteen
  things eight independent Opus lanes had missed.
- The four worst, and they are the same shape: **`classifier.SYSTEM` reached
  the model on no call ever made** (a mode-dispatch bug routed moderation down
  the chat path); **the human publication gate approved by report id** so it
  swapped a classifier publishing unseen content for a person publishing unseen
  content; **a masked markdown link — and then an HTML anchor — passed both
  escapers** into a public issue under the bot's name; and **two members filing
  at the same instant could leave a report durably stored and invisible to
  every read path**, after its reporter had been told it was saved.

**What the whole review is about, stated once:** of the five sharpest findings,
four were *documented* protections — a docstring asserting a property is the
cheapest possible way to stop looking for its absence.

**Records reconciled here:** `docs/repos/spider-bot/intent.md` (ANSWERED, all
four ❓ closed beside their questions), `[D-0042]`, `OQ-GCB-REVIEW-SCOPE`
CLOSED and mapped honestly onto its own A–D menu (B and D in his answer, two
things the menu never offered added, A and C **not mentioned** — absence, not
refusal), the GCB plan NARROWED, the Layer-2 entry point re-derived with the
correction kept visible, `docs/current-state.md`, and `owner/README.md`
regenerated.

**Two count slips in my own commit messages**, recorded because the rule is that
a number in a message is a claim: one said 513 where the run was 539, one said
553 where it was 552. Both were written before reading the run's own output.
Every count from the third commit onwards was read first.

## 💡 Session idea

**The estate's checkers verify code. Nothing verifies that a docstring's claim
is true.** Four of the five worst findings in this review were properties the
code *asserted about itself* in prose — "the one defence that does not rely on
the model cooperating", "the scanned set is the published set", "never raises",
"what stops a retry loop hammering a 404 forever" — while the behaviour had
drifted or had never been wired. Each was found by someone executing the claim,
never by reading it.

The cheap version of a fix: a convention that a docstring making a checkable
claim names the test that checks it. `read_before_write.py` already catches
writing about a file you have not opened; this is the same defect one level in —
writing about behaviour you have not run.

## ⟲ Previous-session review

The 2026-08-24 registration session's Layer-2 entry point froze that day's
numbers into prose and was never re-derived: by today it was wrong about the
commit count, the test count, and — worst — still listed as a *candidate* a
feature that had shipped eleven days earlier. Its own dated header was supposed
to be the honesty mechanism. **A dated header is not one if nothing re-reads
it.** The correction is kept visible in the file rather than quietly applied,
because the correction is the useful part.
