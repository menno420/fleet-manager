# 2026-09-17 — the self-critical tally in fm #1047 counted the owner's sentence as one of mine

> **Status:** `complete` — both records now read **second** instance, with the
> correction stated in place rather than appended silently. The mail is
> untouched: `--count` 2,286 before and after. Records-only, no Codex round
> ([D-0019]); verified directly by the figure checker, `--verify`, and the
> strict gate with this card. Landed on green.

- **📊 Model:** Opus 5 · max · docs-only
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01PrzQkc44A9Q3JyA94rnX1n](https://claude.ai/code/session_01PrzQkc44A9Q3JyA94rnX1n) · "Email draft review"
- **⚑ Third PR from this session**, stated exception under [D-0024]: fm #1047
  is merged, so a correction to it cannot ride that branch; this one restarts
  the designated branch from `main` per the merged-PR rule.

## What is wrong

`docs/planning/2026-08-24-final-eap-email-draft.md` § 2 (▶ 2026-09-17,
*interviews*) and `.sessions/2026-09-17-eap-mail-owner-edits.md` § Review
rounds both read **"third instance of one defect shape"**, and the draft names
the three as the *not-faulty* clause, the 533/533 parity figure and the
research-interviews channel. The shape those sentences define is *an
unverified attribution replaced by a more specific unverified attribution*.

- The **533/533 parity figure** fits: it replaced the owner's clause with a
  figure taken from a doc-route summary that the file refutes.
- The **research-interviews channel** fits: it replaced *"You asked him that"*
  with a venue the source never names.
- The ***not-faulty* clause does not fit, on two counts.** It is **the owner's
  own sentence**, written by him in fm #1019 and carried forward under the
  rule that reserves Part 1 to him; no session authored it. And it is a
  different defect — a code-quality claim contradicted by later measurement,
  not an attribution swapped for a narrower one.

So a self-critical count was inflated by one, and it absorbed the owner's
prose into a session's error tally. An overstated confession is still an
inaccurate record, and this one misattributes authorship.

## 💡 Session idea

**A confession is a claim, and nothing checks it.** Every guard in this estate
points at claims that flatter the session: false walls, overstated counts,
false-dones. This defect ran the other way — a tally of the session's own
mistakes, inflated by one, which no checker looks at and which a reader has no
reason to doubt because it costs the author something. It also quietly
reassigned the owner's prose to a session's error list, which is the part that
actually misleads. The general form: **self-critical counts need the same
N-of-M discipline as flattering ones** (TRAP-004 makes no exception for
humility), and an error attributed to "this session" needs the same authorship
check as a credit. Cheap to adopt: when writing "Nth instance", enumerate the
N and name who authored each.

## ⟲ Previous-session review

`.sessions/2026-09-17-eap-mail-owner-edits.md` (fm #1047) did the substantive
work right: six owner-accepted edits applied, every guarded figure moved, the
draft restaged and diffed against its stored bytes twice, and five Codex
findings dispositioned. Its miss is the sentence this card corrects, and the
shape is worth naming: it wrote a self-critical tally, got the count wrong in
the direction that sounds more honest, and folded the owner's own sentence into
it. The owner-review round caught it by asking what the number rested on — the
same mechanism that caught the 533/533 figure and the invented interview
channel, and the third time today that opening the cited thing was the whole
fix.

## Close-out

- **Shipped** (fm #1048, branch `claude/email-draft-review-eweeef` restarted
  from `main` at `4efd805` because its previous PR, fm #1046, is merged):
  `3efef76` the born-red card, then the two corrections and this flip.
- **Changed:** `docs/planning/2026-08-24-final-eap-email-draft.md` § 2
  (▶ 2026-09-17, *interviews*) and `.sessions/2026-09-17-eap-mail-owner-edits.md`
  § Review rounds — "third" to "second", each with the correction stated in
  place and the reason.
- **Not changed:** the mail. `--count` 2,286 before and after; the Gmail draft
  needs no restage.
- **Program:** E1 unchanged and still his. No queue change, no capability
  delta, no wall.
- **Layer-2 handoff:** null (fleet-manager itself)
- **PR:** #1048, terminal state probed after the flip.
