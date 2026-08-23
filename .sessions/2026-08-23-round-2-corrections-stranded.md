# 2026-08-23 — The round-2 corrections that #937 merged without

> **Status:** `in-progress` — branch `claude/active-projects-overview-kiftou`,
> restarted from `origin/main` at `5a3f087` (fm #937, merged) because the
> previous PR on this branch was already merged. Born red on purpose: the card is
> the merge hold (TRAP-006), and this session exists **because that hold was
> released too early on #937.** It flips only after
> `python3 bootstrap.py check --strict` returns a real exit 0, read from a
> redirect and never after a pipe — **and after `@codex` has answered.**

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

fm #937 captured OD-19/OD-20 and took two rounds of `@codex` review. **Round 1's
corrections merged. Round 2's did not** — the PR auto-merged at `775f1c8` while
round 2 was still being written, so `main` currently carries five known-wrong
statements and one unrecorded conflict.

This lands them.

## What is about to happen

Re-applied onto the new base, unchanged from the stranded commits:

- the laptop thread **moved off `owner-queue.md`** into
  `findings/2026-08-23-owner-direction.md` — the queue is for asks
- the back-link claim **narrowed** to *nine READMEs do not contain the literal
  string*, matching its own nulls
- the primary audit **correctly described**: its verdicts name **16** repos, not
  17, and **`spider-swing` carries none**
- **one** of three failures fixed, not two — `product-forge` and
  `estate-backups` are still open failures
- the withdrawn D2 closure **removed from this session's card title and table**
- the `delivery-roadmap.md` conflict **recorded**: OD-19's first slice sits at
  **Phase 5**, behind the AI spine and community core

## The trap this session is evidence for

**TRAP-006 covers flipping a card to `complete` before the branch is pushed.
This is its neighbour and it is not covered: flipping to `complete` while a
review is still outstanding.**

The card is the merge hold. On #937 I flipped it after the gate went green and
after round 1 was addressed — which was correct by every written rule — then
requested a re-review and pushed further commits. The lander does not know a
re-review was requested: it saw a complete card and a green gate, and merged the
**earlier** head. Round 2's six findings landed against a PR that no longer
existed.

**Measured:** PR #937 merged at head `775f1c8`; commits `4a80bf6` and `4ea3962`
were pushed to the same branch afterwards and reached `main` in **neither** —
`git show origin/main:docs/findings/2026-08-23-owner-direction.md` returned
missing, and the superseded queue entry was still present on `main`, count 1.

**The rule that would have prevented it:** do not flip the card while a review
you asked for is unanswered — or apply `do-not-automerge` when re-requesting
one. The flip should track *review answered*, not just *gate green*.

**Registered, not just described** — because a lesson that lives only in a card
is the estate's statement #117, and the 2026-08-20 railway card already recorded
this exact shape (*"`merge-on-green` landed #871 before the round-2 review I had
requested could answer"*) **and produced no register entry**, which is why it
happened again:

- **`docs/traps.md` TRAP-007** — full entry with trigger, prevention, verify and
  the measured origin.
- **Both existing card routes now carry it** — `card-flip-before-push` (fires on
  `git push`) and `card-status-write` (fires on any `.sessions/*.md` edit), so
  the warning arrives at the flip *and* at the push. `check_doc_routes.py` → exit
  0, 64 routes, 0 errors.
- **No checker, and the reason is stated in the register:** a check would have to
  know a review was *requested*, which is PR state, not tree state. That is an
  honest null, not an omission.
