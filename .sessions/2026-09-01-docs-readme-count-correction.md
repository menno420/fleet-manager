# 2026-09-01 — the room description's own count, wrong on arrival

> **Status:** `in-progress` — born red; flips last.

- **📊 Model:** withheld · high · docs-only
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_013ME1H7CPbqA1FBxJ61VPC2](https://claude.ai/code/session_013ME1H7CPbqA1FBxJ61VPC2) · "Owner-directed documents review"

💡 Session idea: **a count is a claim about the present, and writing a file
changes the present.** `docs/README.md` said "the 64 files sitting loose at
this level" — measured before the README existed, written into the README, and
therefore false the moment it was saved. Adding a file to a directory
invalidates any count of that directory taken beforehand, including counts
inside the file being added.

## Mission

Correct a number I wrote today and then repeated to the owner. Found by
re-measuring a claim in my own reply rather than restating it: `ls -p docs/ |
grep -vc /` returns **65**, and `docs/README.md:40` said **64**.

## Previous-session review

fm #1005 added TRAP-008 (a label read as its contents) with six named
instances, one of which — instance 4 — is *a count restated without re-testing
it*. This is the second occurrence of that specific instance class since, after
the register's own summary line went stale in #1005 itself. The pattern is not
"I read the wrong thing"; it is **"I did not re-read after changing the thing."**

## Shipped

- `docs/README.md` — the count corrected to *"the 64 other files at this level
  — 65 counting this README"*, dated `MEASURED`, with a bracketed note naming
  the trap it fell into. Phrased so the README is excluded **explicitly**
  rather than silently, which is what made the original ambiguous enough to get
  wrong.

## Why phrasing, not just the digit

Writing "65" would have been correct and equally fragile: the next file added
to `docs/` breaks it again, silently. Naming both numbers and what separates
them ("64 other … 65 counting this README") makes a future reader able to
*check* it against `ls` in one step instead of trusting it. The estate's
preference for a generated count does not reach here — one number in one
sentence does not earn a generator, and saying so is the honest version of
that judgement rather than an unstated omission.

## Verification

(filled at close)
