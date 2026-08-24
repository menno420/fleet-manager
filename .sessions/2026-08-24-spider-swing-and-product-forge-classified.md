# 2026-08-24 — the unjudged repo fails, and so does the one we thought we'd sized

> **Status:** `in-progress` — branch `claude/d2-fleet-manager-classify-2srczr`,
> cut from `origin/main` at `68dbe90` (fm #939). Born red on purpose: the card
> is the merge hold, and it stays `in-progress` until a `@codex` verdict covers
> the head this PR is flipped on.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

D2's order has been **PROVISIONAL** since fm #938, for one stated reason:
`spider-swing` was swept but never judged, and it is the estate's only asset
with a live external clock. Until it has a verdict the order below it may be
wrong. This session judges it, judges `product-forge` properly, and settles
the order.

## Scope, and what it deliberately is not

**In:** classification. `spider-swing` gets its first verdict; `product-forge`
gets a re-characterised one; § 5's activity table is re-measured live; § 6 is
re-ranked and the PROVISIONAL marker discharged; each failing repo gets a
turnkey fix brief so the next session executes instead of re-deriving.

**Out — and this is a decision, not an omission:** the *fixes* themselves. Each
is a write to a satellite repo with its own gates, its own born-red card and its
own PR — `spider-swing`'s `main` requires **both** `substrate-gate` and
`game-quality`. Four landings in one session is not OD-6, and the audit's own
rejected note (*presence of a file is not truth of its contents*) is the reason
classifying first was worth a session at all: it changed what the fix has to be.

## previous-session review

⟲ fm **#939** (`68dbe90`) — the immediately preceding work, and it is the reason
this session exists in the shape it does. #938 shipped TRAP-007 stating that a
clean `@codex` pass identifies its head *only* through a `Reviewed commit:` line;
#939 measured a second clean-pass shape that carries no such line and corrected
the rule to *try the line, then match your head among the body's 40-hex strings*.
That correction is load-bearing here — this PR's own flip depends on reading a
verdict correctly, and the narrower rule would have produced a false negative.

⟲ fm **#938** (`9bd48b4`) is the direct predecessor of this session's task: it
found the census defect (16 of 17 swept, `spider-swing` unjudged) and marked § 6
**PROVISIONAL** rather than papering over it. That marker held correctly and is
what this session discharges. Its judgement stands unchanged; nothing in it
needed correcting.

## What landed

**`docs/findings/2026-08-23-active-repo-intent-audit.md`** — amended in place, the
house convention for this file (it already carries three dated in-place
corrections).

**§ 1 — `spider-swing` judged, FAIL.** Four defects, each checked against a live
surface rather than another document:

1. Lines 10–17 still call the name unapproved and *"still open"*. It was settled
   **2026-08-05** as **Slingy Spider**; spider-swing #171 merged `11:27:20Z` that
   day.
2. Line 268: *"No release signing exists."* — `android-release.yml` is in the
   tree at **14,303 bytes** and the repo's ledger records it as having *"run
   successfully through version code 66."*
3. Line 191: *"…store publishing remain absent."* — per spider-swing's ledger
   dated 2026-08-23, signed vc**64** has been on Play's internal track since
   2026-08-05. **Owner-confirmed, not re-verified:** no Play surface is reachable
   from here (`androidpublisher` → 0 hits across `docs/`; no Google credential in
   the environment). The defect is README-vs-ledger and needs no Play read.
4. **The clock is invisible.** `grep -ci` → **0** for `closed test`, `internal
   testing`, `tester`, `Slingy`, `version code`; positive controls on the same
   file → `swing` 17, `Godot` 13, `Reel-In` 3, so the query works, and the file
   was read in full. Both mentions of *"Google Play"* are a scope boundary and a
   prohibition.

**The verdict is a different *kind* of failure, and that is what re-ranked the
order.** `product-forge` and `estate-backups` have *empty* front doors — a cold
session knows it knows nothing and goes looking. `spider-swing`'s is full,
coherent and wrong, so the session does not go looking; it acts on three false
beliefs about the one thread with a deadline. Its ledger is fine and current to
2026-08-23 — README's Documentation table lists ten docs and not
`current-state.md`, whose only pointer is line **340 of 345**.

**§ 1 — `product-forge` re-judged, and the audit had named the smaller defect.**
The 24-line template ledger is real, but the **declared entry point is
`README.md`**, and it is entirely seat-era: `Status: binding`, *"the fleet's
product build seat"*, routing a cold session to wait for an ORDER in
`control/inbox.md` written by a manager seat retired **2026-07-21**, with a
fallback that writes a heartbeat to a coordinator that does not exist. It never
names `phone-controller` — the only subtree committed to in 45 days (`MEASURED`:
`products/phone-controller` 2026-08-20T20:06:39Z vs `products/games-web`
2026-07-10T22:43:14Z; a work-distribution fact, **not** a claim games-web is
dead), 22 slice cards through 2026-08-20, its own README 18,456 bytes. **Filling in `current-state.md` would
have closed the recorded finding and left the repo still failing the test.**

**§ 5 — re-measured live, and the starved reading needed re-checking.**
`spider-swing` reads **5** in the 2026-08-24 window, not 2. The three new ones are
#177/#178/#179 — all Play-release work — merged `19:29:40Z`, `19:52:39Z`,
`20:17:00Z` on 2026-08-23, while this audit landed in fm #928 at **`17:19:21Z`**
the same day: two to three hours *after* the measurement. The two windows are not
interchangeable and the differences are not drift — `superbot` merged **11** PRs
on 2026-08-09, the day the slide dropped, which accounts for 64 → 53 exactly.
Ordering survives; using "2 merges" as evidence of *dormancy* does not.

**§ 6 — re-ranked, PROVISIONAL discharged.** `spider-swing` → `product-forge` →
`estate-backups` → the `websites` date stamp.

**§ 7 — new: a turnkey fix brief per repo**, including the `websites` item, which
is more than a stamp: its `docs/current-state.md` reads `last updated
2026-07-21` and still describes the EAP wind-down as upcoming, so it predates the
whole keep-bot-only cutover § 3 measures.

**Truth left accurate:** the program's NOW pointer, its §7 ledger row,
`docs/current-state.md` and `docs/owner-queue.md` all carry the settled order.
`OQ-FM-D2-TARGET` is untouched and still open — this is the audit's measured
order, not a repository chosen on the owner's behalf.

## What did NOT happen, deliberately

**No satellite repo was edited.** Four fixes across four repos in one session is
not OD-6, and each carries its own gates, born-red card and PR —
`spider-swing`'s `main` requires **both** `substrate-gate` and `game-quality`.
The argument for spending a session on classification alone is that it **changed
what two of the four fixes have to be**: `spider-swing` was not in the order at
all, and `product-forge`'s fix is its README before its ledger.

## Honest limits

- The **five unrated repos** are still unrated. Unchanged by this session.
- `spider-swing`'s verdict is drawn from `README.md` and `docs/current-state.md`
  read in full plus live API reads. Nothing under `game/`, `tests/` or
  `docs/product/` was opened, and none of it bears on a front-door verdict.
- § 7.4's claim that `websites`' **review** is now a Pages export rather than a
  Railway service is carried from the Layer-2 record and is marked `UNVERIFIED
  here` in the brief. It wants the live service list, exactly as § 3 did.

## Verify

`python3 bootstrap.py check --strict` → to be recorded at close, read from a
redirect and never after a pipe.
