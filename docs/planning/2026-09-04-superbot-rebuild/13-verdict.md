# Readiness verdict

> **Status:** `plan` — authoritative for whether a future session may begin
> implementing, and for exactly what it may begin with.

## The verdict

# `PARTIAL — EVIDENCE GAPS`

**And the qualifier matters more than the label: the gaps do not block the first
slice.** They block *design-lock* — freezing the whole architecture — and they
block any claim about replacing production. A session may begin slice one
tomorrow under the stated assumptions.

## Why not `READY_TO_DESIGN-LOCK`

Four gaps, each named with what would close it. None is a matter of needing more
thinking; each needs an observation this session could not make.

### 1 · Neither bot was booted — every dynamic claim is static

By contract, both product repositories were read-only and the production Railway
worker, its Postgres and every Discord surface were untouched. So **every
reachability, effect and degraded-state finding in this package is read from
source, from the compiled manifest, or from the 2026-08-05 live audit** — never
from a running process.

This is not a formality. It means:

- The reachability figures (I-13) are **declared-graph** figures. 463 of 640
  actions carry a `handler:` ref that could render a panel without declaring a
  panel edge, so the true runtime number lies between this and better.
- The 2026-08-05 audit's own honest nulls are **inherited, not closed**: no
  click-through census, and the "two taps" property measured as a graph rather
  than driven.
- The one figure this session moved — the audit's *"27 slash commands survive"* —
  shows both halves of that at once. `main.py:616`'s hardcoded `enabled=False`
  establishes that **this composition root publishes no command set** (I-19); it
  does **not** establish that no commands are reachable, because an application
  retains what an earlier sync registered. External review caught that overreach
  in this very package, and the corrected claim is narrower and still damaging:
  the degrade rationale rests on a surface this root never creates. **Reading
  the application's remote command set is a one-call measurement that this
  contract forbade**, which is gap 1 in one sentence.

**Closed by:** a boot of `superbot-next` in a test guild with a test app, driving
the help tree and the setup flow. About an hour, per the audit's own recipe.

### 2 · The fan-out's adversarial verification did not run before this landed

`run/CONTRACTS.md`'s AGGREGATE contract designed a refutation pass as the second
filter. It had not completed when this package was committed, and — worse — I-15
established that the **first** filter was not filtering: the survival rule passed
**108 of 110 strengths and 125 of 127 defects (98 %)**, because the predicate was
published to the agents that wrote the rows, and 45 % of them landed on
`consumers = 2`, the threshold itself.

So the package rests on a narrower base than the lane count suggests: **the 22
findings this session re-derived itself** (`run/independent-findings.md`), plus
the lane rows marked `lane-claimed` inline. The re-derivation ledger's score is
the honest summary — **9 exact, 3 differing denominators, 0 flipped
conclusions** — and it also records two of the session's own over-corrections and
one finding (I-22) where a challenge lane refuted the session's headline claim.

**Closed by:** running the refutation pass over the retained rows in
`run/raw/lane-results.json`, which is committed precisely so it can be done
without re-running the fleet.

### 3 · One owner decision materially changes the architecture

`12-owner-decisions.md` **OD-A** — is the successor one server's tool, or a
product for many servers? Both readings are consistent with every owner statement
on record; the 2026-09-04 spider-bot purpose decision
([`run/in-flight-direction.md`](run/in-flight-direction.md)) narrows *spider-bot*
and is explicit that it does not narrow
the successor. The recommended default (many servers, one guild at a time) is
chosen on asymmetric cost, not on a guess about ambition: per-guild scoping is
cheap to build in and expensive to retrofit.

If he answers *one server*, roughly the whole 40-panel `setup` surface leaves the
plan — the largest single simplification available anywhere in this package.

**Closed by:** one sentence from him. Everything else in `12-owner-decisions.md`
has a default the plan can proceed under.

### 4 · The successor would be the third start-fresh attempt, and the second failed

Recorded here rather than only in the risk register, because it is the reason the
verdict is not stronger. `superbot-next` reached **533/533 golden parity, 3,648
green tests and 7 required checks** and was parked as a donor. Every mechanism
this package proposes is cheap to install in the first commits and unaddable
later — which is exactly what was true last time.

**Closed by:** nothing this session can do. It is closed by the first slice
shipping with its population contract already in place, or not at all.

## What IS established well enough to build on

Stated positively, because a `PARTIAL` verdict is not a recommendation to wait:

- **The first slice is a finding, not a choice.** Navigation and first-run
  access, because both bots independently lose the setup journey to the
  navigation graph by unrelated mechanisms (I-13: `superbot-next` reaches 39 of
  40 setup panels from nowhere; `superbot` reaches setup only through an
  ephemeral out-of-graph launcher with no route back).
- **The root cause is measured, not theorised** — three source-read instances of
  a guard over an empty, modelled or shrunken population, plus the estate's own
  false-done ledger.
- **The proof system is not invented here.** Both repos already built eleven
  anti-vacuity mechanisms and generalised none of them
  (`08-verification.md` §§ 3, 3b). The successor's advantage is wiring them to
  the shipping artifact from commit one.
- **The donor roles are corrected.** Three attribution reversals against the
  2026-08-21 plan (import-direction guard, AI gateway, enforcement locus), plus
  I-22 turning its layering premise into a measurement artifact. `superbot` is
  the donor for guards and product behaviour; `superbot-next` for authority,
  audit, egress and erasure as **required fields rather than convention**
  (CHALLENGE B).
- **Domain logic is demonstrably reusable across the two trees** — 54
  `disbot`↔`sb` file pairs above 0.55 similarity, 8 at ≥0.90, one byte-identical.
  **This is NOT a demonstration of cog portability, and an earlier draft of this
  file said it was** (caught by external review): a helper can be copied verbatim
  while the cog around it is rewritten by hand and remains uninstallable through
  any extension boundary. OD-19's requirement is that an existing cog can be
  *added on demand*, and proving that needs a cog actually loaded and exercised
  through the proposed contract — which is slice two's job, not a finding this
  review can claim. What the similarity does establish is that the port is not
  starting from nothing.

## What a future session may do on this verdict

**May:** build slice one under `12-owner-decisions.md`'s stated defaults; run the
refutation pass over the retained rows; boot `superbot-next` in a test guild to
close gap 1.

**May not:** claim design-lock; promise or perform a production cutover; treat any
`lane-claimed` number as measured; or begin a second slice before slice one's
population contract and reachability gate are in place and demonstrated.

**Must not, under any reading:** modify `superbot`, its Railway worker, its
Postgres, or any Discord surface. That rail is unchanged by anything in this
package.
