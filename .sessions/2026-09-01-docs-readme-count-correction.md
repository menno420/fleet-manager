# 2026-09-01 — the room description's own count, wrong on arrival

> **Status:** `complete` — pushed, fm #1007 open and ready, strict check run
> with its real exit code read; only blocking finding was this card's own
> born-red hold.

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

- `python3 bootstrap.py check --strict` → **exit read after a redirect, not a
  pipe**. Sole blocking finding: this card's designed born-red hold.
- **The corrected numbers are asserted against the directory, not eyeballed:**
  a check enumerated `docs/` (65 files total, 64 excluding `README.md`) and
  asserted the exact sentence `"**The 64 other files at this level** — 65
  counting this README"` appears in the file. Both halves match the tree.
- The error was found by **re-measuring a claim in my own reply** — `ls -p
  docs/ | grep -vc /` → 65 against `docs/README.md:40` → 64 — rather than
  restating the number a third time.

## The pattern, now twice since it was registered

TRAP-008 instance 4 is *a count restated without re-testing it*. Since the
register entry landed in fm #1005 it has recurred twice: the register's own
summary line ("seven entries") went stale inside #1005, and this count went
stale inside fm #1003. Both were self-inflicted by the same change that made
them wrong.

`REASONED`, not measured: the sub-pattern is narrower than TRAP-008 as written
— **not "I read the label" but "I did not re-read after changing the thing."**
Two instances is the register's stated bar, so this is a candidate for its own
entry or a sharpened ORIGIN on TRAP-008. It is **not** filed as either here:
that is a register edit, this card is a one-line content fix, and conflating
them is how a small correction becomes an unreviewed policy change.

No Codex round, per the owner's 2026-08-29 cadence correction.

Capability delta: null. Owner ask: null.
