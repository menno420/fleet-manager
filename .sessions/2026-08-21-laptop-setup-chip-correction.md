# 2026-08-21 — laptop guide: owner chip correction + what Git actually does

> **Status:** `complete` — branch `claude/desktop-app-setup-cu3ivl`, restarted
> from `main` after fm #883 merged. Born red; flipped after
> `python3 bootstrap.py check --strict` returned a real exit 0 on this tree.
> Flipping this badge is what arms `merge-on-green` — see decide-and-flag.

- **📊 Model:** opus-5 · owner-correction follow-up

## What happened

Two owner inputs on the guide that landed in fm #883.

**1 · The chip was wrong.** The guide named an **Intel Core Ultra X7 358H**,
which I had inferred from a spec search on the model name — not read off the
machine. The owner: *"my laptop is with intel 5 not 7."* Per the estate's
source-truth rule his statement about his own hardware is acted on, not probed.

The correction does **not** move the conclusion: every Intel chip is x64, so the
x64 installer was and remains right. Recorded because it is a clean example of
the failure mode this file's own flagging caught in advance — the reply that
shipped the SKU also told him it was inferred and gave him the command to check.
The guide now states the durable reason (Intel ⇒ x64) instead of a SKU, so the
same correction cannot invalidate it twice.

**2 · "What does the git do exactly?"** The guide said Git was required and
never said what it *is*. For a non-coder owner that is a hole, not a nicety.

## Shipped here (this PR)

- `docs/owner-steps-2026-08-21-laptop-setup.md`:
  - chip claim replaced with **Intel ⇒ x64** reasoning + the owner's Core Ultra 5,
    with the superseded SKU kept visible as a provenance note rather than erased;
  - the `echo $env:PROCESSOR_ARCHITECTURE` check promoted **into the doc** (it
    had only ever been said in chat), including the trap that **`AMD64` does not
    mean an AMD processor** — the single likeliest way that check misleads him;
  - a plain-language **what Git actually is** section + the three concrete things
    it does for Claude Code on Windows (Code tab hard requirement · worktree
    session isolation · Git Bash for the Bash tool), and the honest note that the
    CLI docs call Git optional while the desktop docs call it required — both
    true, different surfaces.

## ⚑ decide-and-flag (hub-side)

- **The merge-on-green card flip is the merge trigger, and that is worth stating
  plainly somewhere a session will meet it.** fm #883 landed 8 s after its sweep
  read `status=complete` off its in-diff card (run `32528596869`). A session that
  flips a card believing it is only bookkeeping has already pressed merge. The
  real hold levers are the `do-not-automerge` / `owner-held` labels, re-read
  fresh per sweep — **not** declining to merge by hand.

## 💡 Session idea

Both owner inputs this round were *corrections to claims about his own
environment* (his chip, his tooling knowledge). Nothing in the estate records
the owner's machines or what he already knows, so every session re-derives both
— usually by guessing. The `docs/owner-machines.md` idea from the previous card
now has a second instance behind it.

## ⟲ previous-session review

The immediately previous card (`2026-08-21-laptop-claude-setup.md`, fm #883):
its claims held up under the owner-review hook across two rounds — the desktop
UI and computer-use citations were verbatim and survived. The one thing it got
wrong is the one thing it had explicitly flagged as inferred (the SKU), which is
the flagging working as designed rather than a defect. Its "merged by
github-actions[bot]" line was true but under-explained; this card's
decide-and-flag closes that.
