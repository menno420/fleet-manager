# 2026-08-23 — The card-census recipe prints rows but never sums them

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

Codex raised this on fm #919 and I filed it "accepted open" while landing. That
was the wrong call, and **fm #920 is why**: that PR's whole argument is that the
evidence pack's credibility rests on *"every figure carries the command that
produced it."* Leaving a recipe that cannot emit its own headline figure
contradicts the PR I had just merged.

**MEASURED against `origin/main`:** the session-card census block ends in
`echo "$r $n"` inside the loop. It prints one `repo count` row per repository and
**never sums them, nor counts the non-zero repositories** — so running it verbatim
produces neither **4,551** nor **19 of 26**. Both are stated in the prose directly
beneath it as though the block derived them.

A recipient of this pack — the vendor — running the published command and getting
26 unlabelled rows instead of the two figures they were told it produces is
exactly the failure mode the pack claims to have designed out.

## Previous-session review

⟲ fm **#920** (`6376999`), fm **#919** (`e2fe0bb`), websites **#512** (`478cb13`)
— all merged. Checked at `main`: the pack carries the point-in-time stamp on the
PR total, the creation-date partition reads 19 / 17 / 19 across three rows and its
recipe reproduces `26 / 19 / 17 / 19`. The live review site is verified at
7 of 7 pages stating the program concluded. Nothing to repair; this card closes
one item those three left open.

**Carried lesson, and it bit twice today:** fm #915 and fm #920 both merged in
under a minute with **zero reviews** because the card was flipped to `complete`
before the branch was pushed — TRAP-006, which I registered this morning. This
card is committed and pushed **red, as its own commit, before any content work**,
which is the discipline the trap exists to enforce.

## What is about to happen

Add the aggregation to the published block so it emits both figures, and verify by
running the committed version verbatim.

## Adversarial review — `@codex`, 3 rounds, 8 findings

**`[conceded]` × 8 · `[survived]` × 0.** Rounds: 3 · 1 · 4 (two of round 3's and
two of round 2's were stale re-anchors of fixes already in the tree — verified at
`:204` and `:194` rather than assumed).

**The headline figure was wrong from the start, and not by drift.**
`.sessions/README.md` is the session *protocol*, not a card, and every repository
with a `.sessions/` directory carries one — so the count was inflated by exactly
**19**. Measured both ways: **4,554** counting every `.md`, **4,535** excluding
READMEs. So `4,551` was never right and `4,554` was not either.

**Two reasons the number moved, deliberately kept apart** — collapsing them would
hide that the original measurement was defective:

| | | |
|---|---|---|
| 4,551 → 4,554 | **drift** | this session's own three cards |
| 4,554 → 4,535 | **definition correction** | −19 protocol READMEs |

**Three times a fix I added to close a TRAP-003 gap contained a smaller TRAP-003
of its own.** The census mapped every error to `0`; the replacement checked only
the per-repo calls and not the enumeration; the enumeration preflight then
validated the outer list but not its entries, so `[{"name":"ok"},{}]` passed and
raised `KeyError` where bash discards it. The pattern worth naming: *"I added
error handling"* feels like completion, and only a probe distinguishes handling
**some** errors from handling **the** error.

**And a ceiling that genuinely could bite, measured rather than assumed:** the
Contents API caps a directory listing at **1,000** entries. `MEASURED` — not hit;
`superbot` is the largest at **970**, thirty short, and returned 970 rather than a
suspicious round 1,000. The doc now carries the check to run before trusting any
future re-measurement.

## Verify

- **The published recipe executed verbatim, end to end:** preflight exit 0 (26
  repos) → census exit 0 → **`26 / 19 / 4535`**, matching the pack.
- Preflight probed against four inputs: malformed entry **rejected**, well-formed
  accepted, empty list **rejected**, non-list **rejected**.
- All five per-repository examples cross-checked against the census: `superbot`
  969 · `idea-engine` 503 · `fleet-manager` 394 · `substrate-kit` 341 ·
  `superbot-next` 334.
- The corrected figure propagated to the three surfaces that had copied it —
  `current-state.md`, the `OQ-E1-FINAL-EAP-EMAIL` entry, the § 7 ledger row —
  and an estate-wide grep confirms no surface carries a stale one.
- `python3 bootstrap.py check --strict` → **exit 0** at the flip (real exit code,
  redirected never piped — TRAP-002); `tools/check_doc_routes.py --strict` → exit 0.

## Landing discipline — the point of this card

**Pushed red as its own commit before any content work**, and the hold armed:
`mergeable_state: blocked`, `substrate-gate` red, still open minutes later. fm
#915 and fm #920 both merged in under a minute with **zero reviews** because the
card was flipped before the push. Same trap, twice, on the day it was registered —
and this card is what it looks like when the discipline is actually followed.

## Layer-2 handoff

`null` — fleet-manager itself; no satellite repo attached.
