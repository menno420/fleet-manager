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
is a write to a satellite repo with its own required checks and its own born-red
card — `spider-swing`'s `main` gates on **both** `substrate-gate` and
`game-quality` — so none of them can ride this PR; each is its own landing in its
own repo regardless of who does it.

**The boundary is not an OD-6 head-count, and saying so would misread it.**
OD-6 (`../docs/planning/2026-07-26-consolidation-program.md:31`) is *"one thing
at a time and do it properly from start to finish"* and is explicitly **not a
reason to stop short of a finished job** — it sets no per-session limit on
landings. The boundary here is that **classification is the one thing, and it is
finished**: verdict, re-rank, brief. The evidence that it is a genuine unit
rather than a truncated one is that it **changed what two of the four fixes have
to be** — `spider-swing` was not in the order at all, and `product-forge`'s fix
is its README before its ledger. Had classification left the fixes unchanged,
this boundary would have been stopping short.

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

**§ 1 — `spider-swing` judged, FAIL.** Four defects — **a mix of live reads and
ledger statements, and the card has to say which** (`@codex`, fm #940 round 2, on
an earlier line claiming all four were live). Live: the tree byte-count, the
greps, the merge timestamps, issue #2's date. From spider-swing's own ledger:
that `android-release.yml` has run through vc66, and the whole Play-track state.
Every defect is nonetheless a **README-vs-its-own-ledger** contradiction, so none
of them needs a surface this session cannot reach:

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
dead), 22 slice cards through 2026-08-20, its own README 18,456 bytes.

**And the bus it routes to is not empty — it is contradicted**, which I learned
only after an owner-review round asked what "empty inbox" was based on. It was
based on the README's fallback sentence; I had never opened the file.
`control/inbox.md` carries **four ORDERs, all `status: new`**, two of them
**P1** (001 = *"Build `products/games-web/`"*, 2026-07-10), while
`control/status.md` reports `acked=001,002,003,004 done=001,002,003,004`. The
file forbids anyone but the manager seat from editing it, and that seat retired
2026-07-21, so the stale markers are structural rather than neglect.

**Filling in `current-state.md` would have closed the recorded finding and left
the repo still failing the test — and so would fixing `README.md` alone**, since
its route still lands on a queue advertising two unexecuted P1s.

**§ 5 — re-measured live; the starved reading needed re-checking, and the two
tables turn out not to reconcile at all.**
`spider-swing` reads **5** in the 2026-08-24 window, not 2. The three new ones are
#177/#178/#179 — all Play-release work — merged `19:29:40Z`, `19:52:39Z`,
`20:17:00Z` on 2026-08-23, while this audit landed in fm #928 at **`17:19:21Z`**
the same day: two to three hours *after* the measurement. The two windows are not
interchangeable. `superbot`'s 64 → 53 matches an 11-merge day dropping out, but
**`fleet-manager`'s 99 → 103 reconciles at no cutoff at all** — swept 595 merged
PRs (oldest 2026-07-18, so the window is fully covered) and tested every 14-day
window ending on 2026-08-23 from `00:00Z` to fm #928's own merge at `17:19:21Z`:
the range is **83–93**, never 99. The two tables came from different methods and
**no arithmetic bridges them**; cite one or the other and do not try. Ordering
survives; using "2 merges" as evidence of *dormancy* does not, and neither does a
merge count as evidence of which threads are live — Layer 2 marks core feel &
difficulty active at `:55`.

**§ 6 — re-ranked, PROVISIONAL discharged.** `spider-swing` → `product-forge` →
`estate-backups` → the `websites` date stamp. **Settled among the rated only:**
five repos stay `unrated` (one read each), and any could carry a contradicting
front door that displaces this. The ranking rule is now stated explicitly —
contradicting beats empty, and among contradicting, the one with a running clock
goes first — because **both** `spider-swing` and `product-forge` are the
contradicting class; an earlier draft wrongly called `product-forge`'s front door
blank, contradicting § 1 one section above.

**§ 7 — new: a turnkey fix brief per repo**, including the `websites` item, which
is more than a stamp: its `docs/current-state.md` reads `last updated
2026-07-21` and still describes the EAP wind-down as upcoming, so it predates the
whole keep-bot-only cutover § 3 measures.

**Truth left accurate:** the program's NOW pointer, its §7 ledger row,
`docs/current-state.md` and `docs/owner-queue.md` all carry the settled order.
`OQ-FM-D2-TARGET` is untouched and still open — this is the audit's measured
order, not a repository chosen on the owner's behalf.

## What did NOT happen, deliberately

**No satellite repo was edited.** Each fix is a landing in a different repo with
different required checks and its own born-red card — `spider-swing`'s `main`
gates on **both** `substrate-gate` and `game-quality` — so none could have ridden
this PR anyway. **Not an OD-6 head-count:** OD-6 forbids stopping short, and sets
no per-session landing limit. The argument for spending a session on
classification alone is that it **changed what two of the four fixes have to
be** — `spider-swing` was not in the order at all, and `product-forge`'s fix is
its README before its ledger. That is what makes classification a finished thing
rather than a truncated one.

## What this session got wrong, and the shape it kept taking

**Six** claims were corrected under review — two by `@codex`, four by
owner-review. Listing them because the **rate** is the finding, not any one fix:

| the claim | what it was really based on | caught by |
|---|---|---|
| signed vc64 is on Play's internal track | spider-swing's ledger — a document | owner-review |
| `phone-controller` is the *only living asset* | session-card **filenames** | owner-review |
| all four defects were *checked against a live surface* | a blanket over a mixed set | `@codex` r2 |
| the earlier window's cutoff *cannot be recovered* | **one** method tried, then generalised | owner-review |
| `product-forge`'s inbox is *empty*, so a session stalls | the README's fallback sentence; **the file was never opened** | owner-review |
| three `substrate-gate` reds are *the same born-red hold* | **one** job log read, then generalised to three | owner-review |

**They are one shape, not five.** Every one is a claim about a surface there was
a *cheap* way to check — one API call, one `curl` — and the check was skipped
because the inference felt like knowledge. None came from bad reasoning; each
came from not noticing that a reasoning step had happened at all.

**And the certainty legend did not stop any of them.** This audit carries
`MEASURED` tags throughout, and four of the five sat inside or beside one. The
tag was applied to *the sentence as written* rather than to *the check actually
run* — which is [TRAP-001](../docs/traps.md)'s exact failure mode, in the
document whose § 3 reports TRAP-001, for the second time in two sessions. The
register entry does not need rewriting; this is another instance of it, and the
instance count is the useful part.

**The one that cost the most was the cheapest to check.** Opening
`control/inbox.md` — 4,751 bytes, one fetch — falsified a ranking argument that
had already survived a `@codex` round and been written into four files.

**And the sixth is the one that matters, because it happened AFTER this table was
written.** Having just tabled five instances of *skipped a cheap check*, the next
message dismissed three CI failures as the born-red hold on the strength of one
job log read earlier. **Writing the pattern down did not prevent the next
instance of it** — which is this estate's own thesis
([`why-rules-dont-bind`](../docs/findings/2026-08-08-why-rules-dont-bind.md))
demonstrated on the document written to record it, within one message.

**A second-order defect came out with it, and it is the more useful one.** The
local checks that "confirmed" the hold were run as
`grep -E "^check: (HOLD|session log)"` — a filter shaped to match what was
expected, so a **new** finding of any other shape would have been invisible to
the check meant to catch it. Re-run unfiltered, the local gate reports **1**
finding where CI reports **2**: CI adds `[session-card-hold]` because it runs the
added-card lane against the merge-base diff, which no local run reproduces. Every
earlier "only the born-red hold" statement here was true, and none of them had
read the count. Verified on all four heads — `5e7d4c1`, `3993da8`, `6dae308`,
`2a08475` — each `check: 2 finding(s)`, both the hold, no third finding.

**What this does NOT license:** treating the table as the fix. Nothing here
delivers the check at the moment it is skipped, and the estate has measured that
a stated rule catches nothing. This is an instance count, not a mechanism.

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
