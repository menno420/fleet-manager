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

### Shipped

- `tools/check_no_false_walls.py` scopes its bounded negation exemption to the
  wall's own clause and pins the bare-wall, unrelated-negation, direct-negation,
  and hard-wrap directions in the offline self-test.
- `tools/ab_kit_scan.py` now runs all seven recorded kit defects — six scanner
  cases plus the fresh-adopter `skills --build` command/template contract — and
  preserves semantic `want=` controls alongside old/new counts.
- `.claude/hooks/trigger_tools_guard.py` plus
  `tools/test_trigger_tools_guard.py` cover two literal direct-API forms and two
  executing-heredoc forms the 52-case baseline missed. Codex landing review
  added command-position controls for `eval|source`, and re-review extended the
  same rule to all known interpreters and shell prefixes; the suite is 66 cases.
  The tool-name denial remains exact and command-text matching remains advisory.
- `docs/findings/2026-08-09-independent-guard-review.md` is the requested claim →
  command → verdict record. Canonical boot/current-state/decision/hook docs and
  both reviewed session records carry the corrections rather than leaving stale
  counts or operational advice behind.
- Substantive GitHub commit: `d4aac5d5890b96d8f5f8f690fb4b4104bd40de8a`.

### Verdict

- Kit classifications: **five v1.20.2 behaviour changes** (defects 1, 2, 4, 6,
  7) and **two long-standing defects** (3, 5). Defect 2's old red is right for
  the wrong reason because v1.20.1 rejects its valid quote-only control too.
- The local negation cliff is confirmed: token-end distances 44/45 clear while
  46/47/48 flag in the old source. After the fix, the bare wall and the same
  wall behind `does not reproduce because` both exit 1; a direct negation exits
  0.
- No baseline trigger-suite case required the opposite expectation. The passing
  52-case suite instead had coverage and contract-assertion gaps. Literal forms
  now warn; a data-flow form such as a variable holding `DELETE` remains silent
  by design because that regex leg is not enforcement.

### Verify

- Untouched `main`: the five owner-requested commands exited **0 / 0 / 0 / 0 /
  0** independently.
- Pre-flip head: `python3 bootstrap.py check --strict` exits **1** with exactly
  one exit-affecting finding — this card's designed born-red hold.
- Pre-flip standalone gates: doc routes **0** (`24 routes · 19 docs routed · 0
  errors · 0 notes`); local false-wall strict check **0**; change guard **0**
  (`16/16`); trigger guard **0** (`66/66` after review fixes).
- Targeted: Python compilation **0**; `git diff --check` **0**; local false-wall
  self-test **0**; seven-defect A/B instrument **0**.
- Final all-green exits and the reviewed SHA are recorded in the flip commit;
  the review request happens after this close-out is published and before that
  flip.

### Review

- Codex reviewed `6388db4c1fec89e7ae84be80ad6e883ee38b225d` and returned two
  threads: P2 causal `since` remained jointly attached to the earlier negation;
  P3 inert `source.md` / `eval.md` writes were mistaken for executors. Direct
  probes reproduced both, so both are `[conceded]` and fixed with controls.
- The P2 correction also covers `given that`, while a `not as if …` control
  prevents over-broadening bare `as`. The P3 correction recognizes
  `eval|source` only at shell command positions and keeps a separator execution
  case red.
- Those are reviewable code changes, so the corrected head receives one
  re-review round before this card flips.
- Re-review of `0027cb0e24185cf1bf4b7543055eb14961ec497e` returned four P2s:
  variable whitespace/hard-wraps in `not as if`; causal `as`; direct
  `not (a) given that`; and assignment/builtin/indent prefixes before heredoc
  executors. Direct probes reproduced all four, so all are `[conceded]`.
- Boundary attachment now distinguishes causal `as` from `as if/though` and
  causal `given that` from an immediately negated complement. One shell-command
  matcher covers prefixes plus all known interpreters; `python3.md` and
  `bash.md` silence controls prevent the filename regression moving sideways.
- This correction receives the second and final re-review round permitted by
  `session-close`; any remaining finding is dispositioned, not allowed to make
  the loop unbounded.

### Handoff and backlog

- Capability delta: none — this session measured repository code behaviour, not
  a new platform capability. No owner decision or owner-queue mutation is needed.
- Residual: the local second-assertion-after-a-repudiated-quote hole remains
  recorded; it is separate from the owner's line-284 acceptance. Substrate-kit
  v1.21.0 remains its own owner-gated release session.
- Groomed `review-queue-drainer-2026-07-10.md` to historical/rejected because
  live `session-close` now owns pre-merge review. Captured
  `checker-contract-bank-2026-08-09.md` for the later kit session; not approved
  or implemented here.
- Layer-2 handoff: null (fleet-manager itself).
- PR: #835, READY and held born-red pending Codex review.
