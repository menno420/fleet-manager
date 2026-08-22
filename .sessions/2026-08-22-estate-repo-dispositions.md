# 2026-08-22 — OD-18: every repo gets a disposition, and only one of them is a start-fresh

> **Status:** `in-progress` — branch `claude/estate-repo-dispositions-spa3i0`,
> started from `origin/main` at `8212720` (#905). Flips to `complete` only
> after `python3 bootstrap.py check --strict` returns a real exit 0 on this
> tree, read directly and never after a pipe.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

OD-18 asks for the thing the R-track never produced: **a verdict per
repository**, not a policy. Keep / archive / delete, and for every keep, whether
the way forward is reworking what exists or starting fresh — each with a stated
reason, so the owner can disagree with one row without re-reading the estate.

The deliverable is [`docs/planning/2026-08-22-repo-dispositions.md`](../docs/planning/2026-08-22-repo-dispositions.md).
Executing any archive or delete is **out of scope** — the list is his and he has
not answered.

## Previous-session review

The session before this one landed fourteen PRs (#892–#905) and finished **R3**
— cfgdiff v0.1.1 and envdrift v0.1.0/v0.2.0 released, because archiving freezes
tag push and two finished CLIs sat at zero releases. Its card
([`2026-08-22-r3-releases-before-archive.md`](2026-08-22-r3-releases-before-archive.md))
also corrected its own framing: that urgency was real but its stated reason
("freezes tag-push **forever**") was false, because archiving is reversible.
That correction is load-bearing here — it is why this table can recommend
archiving twelve repositories without treating any of them as a one-way door.

It left the archive list itself open, on record as five repos. This session
re-derives it from every repo's own state rather than inheriting it, and lands
at twelve.

Two of its notes are carried and closed here: the account-wide dependency check
it called too narrow to justify a deletion has now **run** (§ 3 of the table),
and its branch `claude/project-status-next-steps-hlj7p3` is spent — this one
starts from `origin/main`, not on top of it.

## What this card will carry when it flips

- the table, its counts, and the disposition of the four owner-only rows
- the pre-archive write list (writes must happen *before* the archive, sourced)
- what was measured live vs what is reasoned
- the verify line with its real exit code
