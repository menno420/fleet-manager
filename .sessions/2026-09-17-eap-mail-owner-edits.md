# 2026-09-17 — the owner read the final EAP mail and took the review's changes

> **Status:** `complete` — he read the mail after a week away and said *"you
> can apply the changes"*; all six are applied, the draft is restaged and
> verified against its stored bytes, and two review rounds are dispositioned.
> **Nothing was sent** — the links route, the recipients and the send are his,
> and one round-2 finding is a call in his hands (§ 2, *your-question*).
> Codex: two rounds, 5 findings — 3 conceded and fixed, 1 partial, 1 put to
> him; no third round, and § Review rounds says why. **Reviewed SHA
> `2f97d9387f` (round 2). After it:** `ecfc4ec` (the two records-only P2 fixes,
> verified directly — the 474 recomputed from source, the heading re-read —
> with the COPY block byte-identical) and this flip commit, the badge and the
> close-out text. Landed on green.

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

## 💡 Session idea

**A staging step that diffs what was STORED, not what was sent.** This session
restaged the mail twice and both times read the draft back as raw MIME and
diffed it against the renderer's output; both times every difference was a
Gmail link wrapper and nothing else, which is the only reason the second
restage could be asserted rather than hoped. The 2026-09-03 session read its
staging back as a snippet and wrote *"the body in Gmail is the reviewed head's
text"* — true of every word and false of every link. The check is twenty
lines and belongs in the render tool: fetch `RAW`, decode the parts, diff the
plain part against `to_text`, count `google.com/url` in the HTML, fail the
staging on any hunk that is not a wrapper. It generalises past mail: the
surface that matters is the stored artifact, and a snippet of it is a label
read as substance (TRAP-008). Deduped against `docs/owner-queue.md` and the
2026-09-0x idea slots: the 2026-09-09 card names the same defect, and this is
its shippable form rather than a second statement of it.

## ⟲ Previous-session review

`.sessions/2026-09-09-final-eap-mail-review.md` (fm #1046) found the draft,
proved the mailbox copy equalled the repo word for word, and measured the link
wrapping that no read-back had caught in six days. Every one of its six calls
survived contact with the owner: he took all six. Its miss is the one this
session paid for twice. It reported the *not-faulty* clause correctly and then
offered a replacement — superbot-next's 533/533 parity — taken from a doc-route
summary rather than the file, which
`docs/repos/superbot-next/README.md`:90–92 refutes outright; and the fix it
proposed for the addendum's attribution invented a research interview the
source never names. Both were caught before they shipped, by the owner-review
round and by Codex. The lesson is not new and that is the point: the card that
reports a defect class is not exempt from it, and the only thing that actually
stopped it twice was a reader who opened the cited file.

## Close-out

- **Shipped** (fm #1047, branch `claude/eap-mail-owner-edits-2026-09-17`):
  `add4208` the born-red card · `b7afac2` the six edits plus the five guarded
  consumers they moved · `2f97d93` the round-1 P1 fix and its eight consumers ·
  `ecfc4ec` the round-2 P2 fixes and the review record · this flip.
- **The mail now:** Part 1 **726** words, Part 2 **2,286** by `--count`,
  addendum body **474**. Subject settled as *"Claude Code Projects EAP — the
  final review"*, no week-count.
- **Gmail:** draft `r-9208017789511753451` restaged twice, the second time at
  the corrected text; read back as `RAW` and diffed against the renderer both
  times — 13 differing hunks, every one a `google.com/url` wrapper, no
  recipients. Message id `1a0afe058ae19bac`.
- **Handed to him in chat:** the combined clean-link document, twice, the
  second replacing the first; the review of the current state; and the
  *your-question* call.
- **Program:** E1 stays NOW and stays his. No §7 row — the step is not
  complete until he sends. `docs/owner-queue.md`'s heading, WHAT line and
  figures reconciled; `docs/current-state.md` likewise.
- **Capability delta:** none new. The Gmail link-wrapping line landed with
  fm #1046 on 2026-09-09 and needed no revision; this session exercised it
  twice and it held. No wall written.
- **Layer-2 handoff:** null (fleet-manager itself; superbot-next was read only
  as a source at `docs/repos/superbot-next/README.md`, no repo attached)
- **PR:** #1047, terminal state probed against the API after the flip, not
  read from a stale response.
