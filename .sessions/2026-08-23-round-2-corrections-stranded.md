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

## Round 3 — 8 findings (1 × P1), all 8 addressed IN THIS SESSION

The P1 is the one that matters: **the first attempt to register TRAP-007
delivered nothing at all.**

1. **`[conceded]` P1 — the routes never fired at the claimed moment.**
   `route_docs.py` spends a route on first match, so `card-status-write` was
   consumed **writing the born-red card** and `card-flip-before-push` on the
   **first red push** — leaving the flip and the final push silent. Reproduced
   here on the real sequence (write → push → flip → push): **steps 3 and 4 both
   SILENT.** So extending the two `says` strings was a null change dressed as a
   mechanism — the precise failure the estate calls statement #117, committed
   inside the commit that claimed to fix it.
   **Fixed two ways, then re-measured.** An opt-in **`repeat`** flag —
   an ACTION guard is never spent, a REFERENCE pointer still speaks once — now
   set on `card-flip-before-push`; plus a new **`card-flip-to-complete`** route
   matching the completion transition itself. Post-fix on the same sequence:
   **1 fires · 2 fires · 3 fires · 4 fires**, and every later push fires.
   *The alternative (dedicated IDs alone) was evaluated and is insufficient: the
   hook sees only tool input, so it cannot tell a final push from the first, and
   any new any-`git push` route is consumed exactly as the old one was.*
2. **`[conceded]` TRAP-007 misdiagnosed itself.**
   `session-close/SKILL.md:116-129` — `MEASURED` on fm #827 — already states the
   loop, including *"flip only when the outstanding review covers the head you
   are flipping."* The claim that the flip was *"correct by every written rule"*
   was **false**; the rule existed and had not been read. Rewritten as a
   **compliance/delivery failure of an existing rule**, which is the more useful
   record: it is this estate's own thesis demonstrated on itself.
3. **`[conceded]` Recovery ordering.** `do-not-automerge` must be applied
   **before pushing the completed card** — the push, not the request, is what
   makes the PR mergeable, so a label applied afterwards loses the same race.
4. **`[conceded]` Register totals.** `docs/traps.md` said *"six entries, five
   delivered"* and `docs/MAP.md` *"five of its six"* — both current-state
   summaries, both stale the moment TRAP-007 landed. Now **seven / six**.
5. **`[conceded]` The primary audit's census was wrong AT SOURCE.** Annotating it
   in the supplement left the misinformation where readers are sent first.
   `2026-08-23-active-repo-intent-audit.md` now says **16 of 17**, **6 pass**
   (it listed six while claiming seven), and names **`spider-swing` as carrying
   no verdict**. The NOW pointer's "all 17" is corrected too.
6. **`[conceded]` The review-bot scope question had no queue entry.** Filed as
   **`OQ-GCB-REVIEW-SCOPE`** (`bf94e29`) with four candidate scopes.
7. **`[conceded]` Phase 5 was asserted to BE OD-19's first slice.** That assumes
   the review bot *is* the game-testing loop, which his one sentence does not say.
   Now recorded as a **possible** sequencing conflict, gated on the scope answer.
8. **`[conceded]` E1 "did not slip" was a false schedule history.** 08-22's
   *"today or tomorrow"* meant no later than 08-23; this sets 08-24. It is an
   **intentional deferral by one day**. Reason kept, date corrected.

**Running total across three rounds: 20 findings · 19 conceded · 1 partial ·
0 survived.**

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
