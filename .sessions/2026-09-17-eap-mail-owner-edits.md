# 2026-09-17 — the owner read the final EAP mail and took the review's changes

> **Status:** `in-progress` — he came back from a week away, read the mail, and
> said *"you can apply the changes."* What is about to happen: apply the six
> edits the 2026-09-09 review proposed, update every guarded figure the change
> moves, restage the Gmail draft with the new text and the settled subject, hand
> him the clean-link document, and record the one recommendation this review
> **withdrew** before it shipped. **Nothing is sent** — the links route and the
> recipients are his.

- **📊 Model:** Opus 5 · max · docs-only
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01PrzQkc44A9Q3JyA94rnX1n](https://claude.ai/code/session_01PrzQkc44A9Q3JyA94rnX1n) · "Email draft review"
- **⚑ Second PR from this session** — the stated exception under [D-0024]: fm
  #1046 was records-only and merged on 2026-09-09; this PR edits the mail itself
  on his word eight days later, and is independently revertable from it.

## What this session is about

Program step **E1**. fm #1046 found the draft and reviewed it, listing six
changes as calls for him. He read the mail on 2026-09-17 and took all six. This
card carries what changed, the figures it moved, and the near-miss.

## The near-miss, recorded first because it is the useful part

Correcting Part 1's *"the code itself was not faulty"*, this session first
proposed replacing it with *"and it passed every one of its own parity
tests"*, citing superbot-next's 533/533 golden parity. That figure came from a
**doc-route summary line**, not from the file. Opening the file:
`docs/repos/superbot-next/README.md`:90–92 — ***"The 533 goldens do not test the
shipping bot.** Every "actual" wire byte comes from `rendered_panel_payload()`
in `sb/adapters/parity/transport.py`, a serializer used by nothing but the
parity adapter; production installs [another]"*.

So the proposed fix would have put a **second** checkable-wrong claim into a
vendor mail, in the exact place the first was being removed, about a public
repository, in a mail whose thesis is that verification is the deciding line.
It was caught by the owner-review round before it reached him as anything but
a recommendation, and withdrawn; the clause was deleted instead.

**This is TRAP-008 committed inside the document that reports the defect
class** — the same shape as the 2026-09-01 instances, and the first one on
record caught before the artifact left the estate. It is also the reason the
sending gate's base rate is what it is: 5 of 5 prior rounds changed this
document, and this is the sixth.

## Review rounds

**Round 1** on `b7afac2946` (requested 14:46Z, review 14:52:13Z — 335 s):
**2 findings, both P1 — 1 conceded, 1 partial.**
- *Avoid attributing the question to a research interview* — **conceded**, and
  it was this session's own third instance of one shape. The fix for the
  addendum's "You asked him that" had invented a channel; the source records
  only his recollection, with no venue (`docs/findings/2026-09-02-owner-direction.md`
  :230–236, and the only two "interview" mentions in that file, :513 and :564,
  tie nothing to this question). Now *"This is a question he remembers being
  asked, and the one he most wanted to answer well"*. Fixed in `2f97d93`.
- *Complete the session card before landing* — **partial**. The
  `in-progress` badge is the merge hold (TRAP-006/007); flipping it early is
  the documented failure. What was genuinely caught: `docs/current-state.md`
  described the work in the perfect tense in the same push where the card
  still read "about to happen". The flip commit reconciles them.

**Round 2** on `2f97d9387f` (requested 14:54Z, review 15:01:03Z — ~7 min):
**3 findings — 1 P1 put to the owner, 2 P2 conceded and fixed.**
- *Hedge the remaining direct attribution in Part 1* (P1) — **put to the
  owner, not applied.** Part 1 says *"to answer your question about what would
  make me choose a Project over a session"*, and the reviewer is right that
  the record establishes only his recollection. But the two cases are not the
  same kind: the addendum was **the agents** asserting to the recipients that
  they asked, and Part 1 is **him**, in his own voice, addressing the people
  he remembers asking. His sentences are reserved to him, so this is his call
  and it is in § 2 as *your-question*.
- *Update the addendum subtotal after deleting its asks* (P2) — **conceded.**
  Recomputed independently with the renderer's own block splitter and word
  method: the addendum body is **474**, matching the reviewer's figure; the
  queue carried 488, which is the 2026-09-03 text's. Corrected, with the old
  pair dated rather than overwritten.
- *Reconcile the queue heading with the completed read* (P2) — **conceded.**
  The entry's WHAT line said he had read and edited while its own heading
  still said *"what is left is his: read, edit, add the recipients, send"*.
  Heading now reads READ, EDITED AND RESTAGED.

**Tally: 5 findings across 2 rounds — 3 conceded and fixed, 1 partial, 1 put
to the owner.** No third round: the two round-2 fixes are records-only, the
COPY block is byte-identical to the head round 2 reviewed, and both were
verified directly (the 474 recomputed from source, the heading re-read).
[D-0019]'s cadence reserves Codex for the flip-readiness of real changes.

## Close-out

*(filled at the flip)*
