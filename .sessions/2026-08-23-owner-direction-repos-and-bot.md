# 2026-08-23 — Owner direction: the bot's shape, the no-cut repo policy, and D2's answer

> **Status:** `in-progress` — branch `claude/active-projects-overview-kiftou`,
> cut from `origin/main` at `a8e0988` (fm #936). Born red on purpose: the card is
> the merge hold (TRAP-006). It flips only after
> `python3 bootstrap.py check --strict` returns a real exit 0 on this tree, read
> directly and never after a pipe.

- **📊 Model:** opus-5 · high · records

## 💡 Session idea

The owner asked for oversight into the active projects, and in answering gave
**four pieces of direction that exist only in the chat transcript** — the exact
loss mode this repo's boot file records as entry 1b, where a plan set live on
2026-08-08 reached neither `CLAUDE.md` nor `README.md`, and a later session
walking the read path met a two-week-old plan instead.

This session records them, measures the one that makes a claim about the tree,
and answers a standing owner question his message resolves in passing.

## previous-session review

⟲ fm #936 (`a8e0988`, HEAD): the `idea-engine` notebook corpus and its
seam-count correction. Checked at `main` — present, and this branch was cut from
exactly `origin/main`. Nothing to repair.

Its closing lesson is the one this session had to apply first: *"an inference
that explains a real finding is still an inference."* The owner's directive here
carries an embedded claim about the tree — that the repos need documentation —
and the temptation was to accept it and start writing. **Measuring it first
changed the size of the work by an order of magnitude** (§ below), which is the
same move #936 wished it had made.

## What the owner said, and what was recorded

| His direction | Recorded as |
|---|---|
| The next bot: **review-oriented and small first**, cog-portable, **bots stay separated**; the two `superbot` repos consolidate into one new **repository** eventually | **OD-19**, plus an amendment at the head of the [pre-repository plan](../docs/planning/2026-08-21-game-community-bot/README.md) so a GCB session meets it before the headline |
| **Every repo earns its place**; the remedy is documentation + hub linking, not cuts | **OD-20**, which bounds OD-17 and closes OD-18's execution arc |
| *"so I will send the email tomorrow"*, deferred deliberately behind his setup work | **E1** status block, above the older 2026-08-01 note kept for provenance |
| The laptop as an AI-integrated workstation — his current priority | **`OQ-LAPTOP-AI-WORKSTATION`**, filed as a thread, **not** an ask |

**`OQ-FM-D2-TARGET` is answered by OD-20**, after 13 days open. D2 stops waiting
on a named repository: the target is the property he stated, held across the
active set. The NOW pointer is retargeted accordingly.

## The measurement that changed the work

`MEASURED` — all 17 non-archived repos, live default-branch trees via the
direct-PAT path. Full method and per-repo table:
[the audit](../docs/findings/2026-08-23-front-door-audit.md).

| | |
|---|---|
| carry a root `README.md` | **16 of 17** |
| carry `docs/current-state.md` | **15 of 17** |
| **READMEs that name this hub** | **6 of 15** |

**Read as a documentation programme, OD-20 is a 17-repo sweep. Measured, it is
three content holes plus nine one-line back-links.**

The three holes: **`superbot` has no root README at all** — the repo behind the
LIVE production bot, entered via an internal orientation file; `estate-backups`
is a 130-byte stub with no state file; `superbot-plugin-hello` has no state file.

**And the back-links are the load-bearing half, not the cosmetic one.** The boot
triad already records (`MEASURED` 2026-08-07, `curious-research`) that a session
booting in a satellite loads that repo's `.claude/` and **none** of the hub's —
no read path, no doc-routing, no skills. PL-013: the routing table cannot bind a
session that never loaded it. So for those nine repositories the README
back-link is the **only** surviving channel that can say the hub exists. Four of
the nine are the most-worked repos in the estate.

## What landed

- **OD-19 and OD-20** in the program's directive table (now 20 rows).
- **The bot plan amended at its head** — scope, the cog-portability requirement
  as a Phase 0 acceptance question, and the separation constraint. GCB-1
  untouched; nothing here authorises creating the repository.
- **`OQ-FM-D2-TARGET` answered**; the NOW pointer retargeted with the measured
  scope inline, so the next session reads the size rather than the slogan.
- **E1** restated with his reason — it did not slip, he re-ordered it.
- **`OQ-LAPTOP-AI-WORKSTATION`** filed, with the explicit note that it is not an
  ask and is not licence to reconfigure his machine.
- **The front-door audit**, with its method, its nulls, and its own correction.

## Verification

- `python3 bootstrap.py check --strict` → **real exit 0**, read directly, never
  after a pipe.
- The audit's numbers are reproducible from the recorded calls; the script is
  scratch, the calls are named in the finding.

## Corrections made in-session

- **The audit's first draft listed `superbot-next` as archived.** It is not —
  it is active and gated on GCB-1, and it is inside the 17 the audit counts.
  Caught on re-read before the file was committed; the bullet now names the
  actually-archived reference repos and states the error.
- **The finding was born with badge `finding`**, which is not in the allowed
  vocabulary. The gate caught it (`[badge]`); it is `audit`.

## The lesson

**A directive can carry a factual claim, and the claim is checkable even when the
directive is not.** OD-20 is his call and is not up for verification. *"Each repo
needs proper documentation"* is a statement about the tree — and measuring it
turned a 17-repo sweep into twelve small edits. The estate's habit is to verify
records and inferences; this is the same discipline applied one level up, to the
premise inside an instruction, without touching the instruction's authority.
