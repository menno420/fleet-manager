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

## Close-out

*(filled at the flip)*
