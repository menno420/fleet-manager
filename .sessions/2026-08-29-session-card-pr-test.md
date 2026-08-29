# 2026-08-29 — a session card PR, as a test of the landing path

> **Status:** `in-progress` — born red. **What is about to happen:** this card is
> committed alone, pushed, and opened as a READY PR carrying nothing else; the
> strict gate is then run and the badge flipped last. The card *is* the
> deliverable, so the landing path is the thing under test rather than the
> vehicle for something else.

- **📊 Model:** withheld · max · docs-only
- **⚑ Model-slot note:** this session's harness policy forbids a model
  identifier in any pushed artifact, so segment 1 is honestly withheld rather
  than guessed; effort and PL-004 task class are exact. Same slot, same reason,
  as [the previous card](2026-08-29-fleet-orchestration-retro.md).
- **📍 Venue:** cloud-container

## Mission

Owner, live: *"small test task: create a PR with only your session card."*

Taken literally. The PR's diff is one added file — this one — and no other path
is touched. That is the whole scope, and the interesting part is what a
card-only PR exercises on the way through.

## What a card-only PR actually tests

Four things, and none of them is normally observable on its own, because a card
always rides in with real work:

1. **Cold orientation** — the six-read order in `README.md`, run before writing
   anything. It produced the four facts it promises: router-and-records-home ·
   post-close owner-directed era · OD-13 methods-before-product with OD-26's
   *map → revise → execute* at stage one · NOW = the OD-24 round's session 5
   (kit records work), with D2's target now answered as `spider-swing`.
2. **The born-red gate on its own card** — `scripts/preflight.py` step 1 grades
   every card ADDED in the diff against `origin/main`. Here the added-card set is
   exactly one, so the lane's verdict is unambiguous rather than inferred from a
   mixed diff.
3. **The `📊 Model:` grammar** — three exit-affecting checks (R13 task class,
   R14 exact-model-ID, R15 effort tier) all read this one line, and `max` is a
   taxonomy tier that has been valid since it was declared but is rare on the
   cards here.
4. **The base the diff is measured against.** On arrival `origin/main` was
   **five commits stale** (`5d10b95`) while the working tree already held
   `3606b4f`; the diff vs the tracking ref therefore showed **58 files and
   14,223 insertions** that were in fact already merged. One `git fetch origin
   main` collapsed it to `0 0`. Had the card been committed before that fetch,
   the added-card lane would have graded a phantom batch of merged cards as this
   PR's own.

## What went wrong in this session, recorded rather than tidied

**TRAP-002, committed on the fourth command of the session.** The fetch was run
as `git fetch origin main 2>&1 | tail -3; echo "exit=$?"` — which reports
`tail`'s exit code, not the fetch's. The doc-routing hook fired the trap the
moment the command ran, which is the mechanism working exactly as designed. The
result happened to be independently verifiable (`git rev-parse origin/main`
moved to `3606b4f`), so nothing was recorded on a false pass; the point is that
the *check* was worthless and the estate's own register had already named the
failure. `docs/traps.md` TRAP-002.

## Verify

- `python3 bootstrap.py check --strict` → real exit code, read directly, no pipe.
- The PR diff is confirmed to be one added path via `git diff --name-only
  origin/main...HEAD` before the flip, not asserted from intent.

## Layer-2 handoff

Layer-2 handoff: null (no repo attached; fleet-manager itself)

## ⟲ Previous-session review

Previous card:
[`2026-08-29-fleet-orchestration-retro.md`](2026-08-29-fleet-orchestration-retro.md)
(fm #971, merged `7d99f7d`).

**Held up, and it is the strongest card in the recent run.** It opened by paying
a debt the previous turn had conceded — the concurrency figure reported to the
owner as observed had been read from a tool reference — and the measurement
overturned it by 3–4× (peak 4, not 10–16). It then let the same pass overturn its
*own* framing: verification was not under-provisioned, it was 88 % of output
tokens with a broken decision rule. A card that corrects the thing it came in
believing is doing the job.

**What it could not close, and this card does not either:** its own flip
exemption declares `fe184ccb` as the last reviewed SHA with three commits after
it. That is the documented exemption and it was declared properly — but it means
the merged head of fm #971 carries commits no reviewer saw, which is the same
shape as the risk `session-close` § 6c exists to prevent. The exemption is
load-bearing and undated; nothing in the repo counts how often it is taken.

## 💡 Session idea

**The gate can already tell a session that its base is stale, and it doesn't.**
This session's `origin/main` was five commits behind the tree it was standing on,
and the only reason that surfaced was a hand-run `git rev-parse` comparison
prompted by an odd `git log` result. Nothing would have said so — and the whole
added-card lane, the estate's one exit-affecting card gate, is defined as *the
cards added in the diff versus that ref*.

One line in `scripts/preflight.py`, before it computes `added_cards()`: compare
`origin/main` against the remote head and print the delta. It needs no network
call it does not already have available, changes no verdict, and turns a silent
mis-measurement into a printed number. It is the same class as TRAP-004's
shallow-clone warning — a derived figure whose base is quietly wrong — and the
estate has now been bitten by that class twice in four days.

**Why an idea and not an action:** OD-26 §13 puts mechanisms behind the revised
plan, and this PR is scoped to one file by the owner's own instruction. Adding a
gate lane inside a test of the gate would be the wrong place to learn whether it
is right.
