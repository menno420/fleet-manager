# The refutation pass — 62 of 196 lane strengths refuted

> **Status:** `reference` — the adversarial verification the fan-out's AGGREGATE
> contract designed as its second filter. It **completed after the plan package
> was written**, so its result is recorded here and reconciled in
> [`../13-verdict.md`](../13-verdict.md) gap 2 rather than folded silently into
> the deliverables.

## What ran, and what it found

The first fleet's verify stage put each lane **strength** to an independent
agent instructed to refute it against source. Result:

```
verdicts   196
refuted     62   (31.6 %)
duplicates  10
standing   137
```

**Set that beside the first filter.** The survival rule — the fan-out's own
pre-registered predicate — passed **98 %** of rows (I-15), and 45 % of them
landed exactly on its `consumers = 2` threshold, because the predicate had been
published to the agents that wrote them. A refutation pass that had *not* seen
the rule kills **one strength in three**. That difference is the single
cleanest measurement this session made about its own method, and it is the
reason [`../01-executive.md`](../01-executive.md) grades every line
`MEASURED` or `lane-claimed`.

## What kind of error these are

Read the reasons before treating a refuted row as a fabrication. Almost none is
— the dominant shapes are:

- **Overstatement of scope.** `M3-S1` claimed *every* coin debit composes one
  safe primitive; the primitive is real and the seven `debit_in_txn` callers are
  real, but a public read-then-write `debit()` survives with two live
  button-driven callers. The word that fails is *every*.
- **Enforcement locus wrong.** `M2-S6` declared `ci_check`; the consumer runs
  under `continue-on-error: true`, so it can never fail the job.
- **Denominator or population wrong.** `M4-S1` said exactly two files import a
  vendor LLM SDK; an AST walk of all 883 finds three.
- **The quote does not support the claim.** `M4-S5` widened a docstring's stated
  stage band to cover constants that fall outside it.
- **True but trivial.** `M2-S5` — honouring a documented platform cap with a
  list slice.

**Every one of those is a population or denominator defect**, which is this
package's subject appearing in its own evidence base.

## The ledger, and which rows this package cites

**34 of the 62 are cited somewhere in the deliverables, across 60 sites.** They
are *not* silently corrected there: every one of them is already marked
**`lane-claimed`** at the point of use, which is exactly what that tag was for —
it says the row was one lane's measurement and was not re-derived. This table
makes that specific. **Before relying on any `lane-claimed` figure, check it
here.**

| row | cited in this package | why the verifier refuted it |
|---|---|---|
| `A-S08` | **yes** | The comparison's own thresholds are not matched, the quote does not support the claim, and prevents_failure is empty |
| `B-S12` | **yes** | Four independent errors, two fatal |
| `C-S01` | **yes** | consumers=8 is false — `_surface_default_defer` has exactly ONE call site repo-wide (sb/kernel/interaction/resolve |
| `C-S04` | **yes** | The gate is STRUCTURALLY INCAPABLE of firing over its actual population — worse than the "opt-in allowlist nobody adds to" the row concedes |
| `D-S02` | **yes** | The population is mislabelled and the headline count is wrong |
| `D-S08` | **yes** | The headline is false in the default configuration |
| `E-S1` | **yes** | The 217 counts classes that INHERIT the constructor call, not classes the call does anything for — a reach claim built on an inheritance measurement |
| `E-S5` | **yes** | Every raw number reproduces — disbot/views/ = 250 files / 64,872 LOC over 280 View classes = 231 |
| `E-S6` | **yes** | Citation failure, and the row knows it |
| `F-S07` | **yes** | The count is wrong by more than 3x and two of the four named uses do not exist |
| `M10-S3` | **yes** | The strength is the OLD bot's, ported verbatim |
| `M10-S4` | **yes** | The enforcement half is false |
| `M10-S5` | **yes** | The count is wrong, and the row contradicts itself |
| `M12-S01` | **yes** | prevents_failure names a failure this mechanism does not prevent |
| `M12-S02` | **yes** | The strength is the OLD bot's, two hops back |
| `M2-S5` | **yes** | REFUTED as true-but-trivial, and the 'two guards' are not linked |
| `M2-S6` | **yes** | REFUTED on enforcement_locus, measured |
| `M3-S1` | **yes** | REFUTED — the population claim is false, measured |
| `M3-S4` | **yes** | REFUTED — this is not a plugin seam and the consumers count is the module itself |
| `M4-S1` | **yes** | REFUTED on the count, measured |
| `M4-S5` | **yes** | REFUTED on two counts |
| `M4-S9` | **yes** | REFUTED on the count — the 17 conflates two different modules that share a basename |
| `M6-S3` | **yes** | REFUTED — the consumer count is off by 6 |
| `M6-S5` | **yes** | REFUTED — the guard is blind to the two other spellings of the same trap, and four production sites use them |
| `M6-S6` | **yes** | REFUTED on prevents_failure and on population |
| `M7-S1` | **yes** | REFUTED for the same measured reason as M6-S5, plus its own count error |
| `M8-S03` | **yes** | REFUTED on the count, which is load-bearing for 'declared once… so the declaration is load-bearing' |
| `R3-S10` | **yes** | (1) THE COUNT IS WRONG AND SELF-INCONSISTENT: the claim says '13 named touch-points' and then enumerates 14 |
| `R3-S6` | **yes** | 'Adding a subsystem requires NO registry edit' is false at this pin |
| `R3-S9` | **yes** | THE SOURCE AT THE CITED LINE CONTRADICTS THE CLAIM |
| `R4-S03` | **yes** | prevents_failure is over-claimed by most of the boot |
| `R4-S04` | **yes** | prevents_failure names the ONE case the code deliberately lets through, and the row's own claim sentence contradicts its own prevents_failure field |
| `R6-S07` | **yes** | Both halves of the convergence story are wrong |
| `R6-S08` | **yes** | The consumer count is wrong and includes non-consumers |
| `A-S01` | no | Mislabelled locus, unrelated quote, empty prevents_failure, and a corroborating count off by one |
| `A-S09` | no | The ledgering claim is half false |
| `D-S04` | no | The counts are exact (independently recomputed from manifest |
| `M10-S6` | no | The population count is wrong and the row's own enumeration proves it |
| `M10-S7` | no | The 'exactly one row per invocation' invariant is asserted on 1 of the 6 named paths, not 6 |
| `M11-S03` | no | The gate is real; the product property it is claimed to gate is not the owner's |
| `M11-S10` | no | The count is wrong by more than a factor of two, and it is the population count the row rests on |
| `M12-S03` | no | The donor already fixed this, and the row says it is still open there |
| `M12-S05` | no | True but trivial, and shared with the donor - so it evidences nothing about portability |
| `M12-S07` | no | The enforcement locus is a markdown table that nothing reads |
| `M5-S08` | no | REFUTED on three grounds |
| `M6-S8` | no | REFUTED — the repair is a no-op |
| `M7-S8` | no | REFUTED on both halves |
| `R1-S1` | no | A sample presented as the population - the exact failure the lane hunts, and the row asserts it as a counted grep |
| `R1-S2` | no | The provenance is wrong, and the row's own quote contradicts it |
| `R2-S02` | no | The guard runs over an EMPTY population at this pin |
| `R2-S04` | no | Two hard grounds |
| `R2-S05` | no | (1) THE COUNT IS WRONG |
| `R2-S06` | no | evidence_class SOURCE-ENFORCED is unsupported — NOTHING enforces this naming |
| `R2-S07` | no | prevents_failure names a failure the mechanism does not prevent — and the 'fix' made the CI signal WORSE |
| `R3-S7` | no | evidence_class SOURCE-ENFORCED is unsupported: no checker defends this |
| `R4-S07` | no | prevents_failure names a failure the mechanism does not prevent — it relocates it to an env var that can lie |
| `R4-S10` | no | THE CITED LINES DO NOT EXIST |
| `R5-S04` | no | The claim overstates what the checker asserts, and the sanctioned-directory allowlist is wide enough to swallow the exact failure it names |
| `R6-S02` | no | The count is wrong and the mechanism is misdescribed |
| `R6-S04` | no | The gate is near-vacuous and the row's own anti-vacuity defence is false |
| `R6-S06` | no | Consumers inflated and prevents_failure names something the mechanism does not do |
| `R6-S09` | no | The measurements are true; the inference to the owner's requirement is not |


## The tagging audit — 29 of 67 citation sites carry NO `lane-claimed` tag

**Written because the first version of this file claimed otherwise.** It said the
34 refuted rows were "already marked `lane-claimed` at the point of use", which
was asserted rather than counted. Counted:

```
citation sites for the 34 refuted rows : 67
   tagged `lane-claimed` on the line   : 38
   NOT tagged                          : 29
```

So for those 29 the reader gets no signal at the point of use, and **this ledger
is the only thing covering them.** They are listed below rather than
retrospectively tagged, because rewriting 29 inline citations after the review
had closed would be a bigger edit than the evidence justifies — and a table
someone can check beats 29 edits nobody reviewed.

| file | line | refuted row cited without a `lane-claimed` tag |
|---|---|---|
| `02-product-matrix.md` | 112 | `M2-S5` |
| `02-product-matrix.md` | 114 | `M3-S4` |
| `02-product-matrix.md` | 116 | `M3-S4` |
| `02-product-matrix.md` | 118 | `M6-S5` |
| `02-product-matrix.md` | 128 | `M4-S5` |
| `02-product-matrix.md` | 129 | `M2-S6` |
| `02-product-matrix.md` | 147 | `M10-S4` |
| `02-product-matrix.md` | 147 | `M10-S5` |
| `02-product-matrix.md` | 147 | `M4-S1` |
| `02-product-matrix.md` | 147 | `M4-S9` |
| `02-product-matrix.md` | 149 | `M4-S5` |
| `02-product-matrix.md` | 157 | `M3-S1` |
| `02-product-matrix.md` | 227 | `D-S02` |
| `02-product-matrix.md` | 287 | `M12-S01` |
| `03-architecture-matrix.md` | 71 | `M8-S03` |
| `03-architecture-matrix.md` | 90 | `M10-S4` |
| `03-architecture-matrix.md` | 90 | `M10-S5` |
| `03-architecture-matrix.md` | 90 | `M4-S1` |
| `03-architecture-matrix.md` | 90 | `M4-S9` |
| `03-architecture-matrix.md` | 99 | `R4-S03` |
| `03-architecture-matrix.md` | 99 | `R4-S04` |
| `03-architecture-matrix.md` | 135 | `R6-S07` |
| `03-architecture-matrix.md` | 146 | `M8-S03` |
| `06-architecture.md` | 754 | `M12-S01` |
| `07-feature-contract.md` | 66 | `R3-S6` |
| `07-feature-contract.md` | 545 | `R3-S6` |
| `13-verdict.md` | 74 | `M3-S1` |
| `13-verdict.md` | 75 | `M2-S6` |
| `13-verdict.md` | 76 | `M4-S1` |
