# 2026-08-09 · hub — independently review the day's guards, then close the false-wall hole

> **Status:** in-progress

- **📊 Model:** GPT-5 · ChatGPT Work · adversarial review plus one narrow checker fix

Time: 2026-08-09 · venue: ChatGPT Work · branch
`agent/fix-false-wall-negation-scope` (from `0ab4d07` = `origin/main`)

💡 Session idea: **a passing suite is evidence about the assertions it made, not
about whether those assertions describe the intended behaviour.** This review
starts from the three places the previous work was most likely to encode its own
bug as the expected answer: the kit A/B bank, the fixed-distance negation
lookback, and the trigger guard's 52 asserted outcomes.

Layer-2 handoff: null (fleet-manager itself)

## Previous-session review

⟲ fm #833 upgraded the vendored kit to v1.20.2 and left a reproducible seven-case
upstream defect record; fm #834 added the trigger-deletion guard and its 52-case
suite. The owner's continuation asks this fresh surface to distrust the claims,
rerun the instruments offline, record a claim-by-claim verdict, and repair the
fleet-manager-local false-wall checker only if the 48-character negation cliff is
real.

The untouched-main baseline was checked before this card: `HEAD` and
`origin/main` were both `0ab4d07edd7ad989ed2614b34584d2f933777c28`; the
connected GitHub repository query returned zero open PRs; and each of the five
requested commands exited 0. `bootstrap.py check --strict` appended 49 telemetry
records and created one probe-bank artifact; both are being inspected rather than
silently discarded.

## What is about to happen

1. Run `tools/ab_kit_scan.py`, inspect its case bank and both vendored scanner
   implementations, and classify every row from observed old/new behaviour plus
   the semantic `want=` contract.
2. Sweep the local checker's negation distance around its 48-character boundary
   with a positive control, then reduce the confirmed failure to a permanent
   regression test.
3. Audit the trigger suite's assertions against the guard's stated contract and
   exercise additional boundary/traffic cases where the existing suite leaves a
   plausible blind spot.
4. If confirmed, scope negation to the clause that contains the wall signal so a
   negation belonging to an earlier predicate cannot clear it.
5. Commit the review as evidence, run all five gates, obtain review while this
   card remains born-red, then flip this badge to `complete` as the last step.

## Acceptance

- A bare present-tense capability wall still makes
  `tools/check_no_false_walls.py --strict` exit 1.
- The same wall after `does not reproduce because` also exits 1.
- Valid prose that directly negates the wall remains clear.
- The seven kit cases and the trigger suite each have a written claim → command →
  verdict record, including any corrected classification or expectation.
- All five requested gates return exit 0 after the fix.

## Close-out

*(to be completed before the Status flips)*
