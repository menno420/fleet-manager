# 2026-08-22 — OD-18: every repo gets a disposition, and only one of them is a start-fresh

> **Status:** `complete` — branch `claude/estate-repo-dispositions-spa3i0`,
> started from `origin/main` at `8212720` (#905), landed as fm **#906**.
> Flipped after `python3 bootstrap.py check --strict` returned a real exit 0 on
> this tree, read directly and never after a pipe.

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

## What landed

[`docs/planning/2026-08-22-repo-dispositions.md`](../docs/planning/2026-08-22-repo-dispositions.md)
— **keep 14 · archive 12 · delete 0**, every row with a stated reason, wired into
the program (OD-18 row, R5's input, §7, the NOW block), `ESTATE.md` and
`owner-queue.md` (`OQ-ESTATE-ARCHIVE-LIST`).

**The answer to the axis OD-18 added:** 13 of the 14 keeps are **reworks**; the
fourteenth (`superbot`) is neither — frozen, with a fresh successor. The estate
has exactly two start-overs and both were already decided: fresh **code** for the
bot (OD-16), and a fresh **home** for phone-controller (R2). Keeping those two
senses apart is most of what makes the table usable.

## Five claims checked rather than inherited

Index rows are pointers; each of these was read at source, and each moved a row.

| claim | what it turned out to be |
|---|---|
| `Substrate-kit-app` has no dependents | **Established account-wide** — 5 code-search hits, all in fleet-manager, none in the other 25. The check the prior note called too narrow has now run. |
| `superbot-plugin-hello` must never be archived | **False, and for a better reason than first written.** `superbot-next` vendors the plugin in-tree at `examples/superbot-plugin-hello/`; the host never reaches the standalone repo. |
| `superbot-idle` is quietly parked | **Not quiet.** Its cron has 40 scheduled runs across 40 distinct days with no gap, 32 of them after the repo's last commit. |
| the `superbot-mineverse` baton | **Wrong twice** — it directs a trigger deletion this estate forbids, against a trigger that no longer exists on the account. |
| merging superbot's dependabot PRs restarts the bot | **Three of the eight cannot** — they touch only `botsite/`, `dashboard/`, or a workflow. Smaller owner ask than the one on record. |

## The trap this pass found

**R3's lesson is not about releases, it is about writes.** Archiving makes a repo
read-only, so anything a repo still needs written has to be written first — and
GitHub's own archiving docs recommend the same order for issues, PRs and the
README. The sharp case is `superbot-mineverse`: archive it as-is and a forbidden
instruction is sealed, read-only, into the document the whole SuperBot-World
family routes to. That is § 4 of the table.

Guard recipe for a later session: the pre-archive write list is checkable, not
just documented — a script over the twelve rows asserting *no open issues · a
README line dated after the last release · no `delete.*trigger` string in any
`docs/current-state.md`* would red before R5 rather than after. Anchors:
`scripts/check_estate_index.py` (already walks the same twelve names),
`docs/planning/2026-08-22-repo-dispositions.md` § 4.

## Adversarial review

**Owner-review hook — 3 questions, 1 `[survived]` · 2 `[conceded]`.** It asked
what established "a hash doesn't fetch" for `superbot-plugin-hello`; the honest
answer was the lockfile *format*, not the resolution path, so I read the
resolution path and found the in-tree vendored copy — same verdict, verified
mechanism. It also caught the GitHub-docs citation being stretched from what the
quote covers (issues/PRs, README) to items the docs never mention; that split is
now explicit. The dependabot measurement `[survived]` with its provenance stated:
file lists measured here, filter semantics inherited from the Layer-2 record.

**Codex round 1 — 6 findings, 6 `[conceded]`**, fixed in `8be279a`: the OD-18 row
still said "every keep a rework"; *"exactly one window"* contradicted this PR's
own reversibility argument; the owner-queue stated archive safety above its
evidence; the cron claim generalised from a five-day sample (fixed by measuring
the full history, which also exposed a 1,185-run figure that was the repo's
all-workflow total, not this cron's); "skip the archive-bound" for D2
contradicted the archives-preserve-reads rationale; and — the most consequential
— the execution-facing archive list lacked the GCB-1 gate its canonical row
carries, so a single owner yes could have archived the architecture donor early.

## What did NOT happen, deliberately

No repository was archived, deleted, renamed or modified. No trigger was deleted
or disabled. The twelve-row list is the owner's call, queued as
`OQ-ESTATE-ARCHIVE-LIST`; the two letters (`OQ-GBA-NEXT-PICKS`,
`OQ-PML-EMERALD-LETTER`) stay his.

## Verify

`python3 bootstrap.py check --strict` → **exit 0**, read directly. Through the
session it returned 1 on the designed born-red HOLD only; the sixteen
`substrate-gate` failures the PR collected are that same hold on each pushed SHA
(`[session-card-hold] … designed hold, not a defect`, read from the job log),
not a defect and not a flake.
