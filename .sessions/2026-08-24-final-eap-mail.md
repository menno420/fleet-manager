# 2026-08-24 — E1: the source sweep and the assembled final EAP mail

> **Status:** `in-progress` — branch `claude/final-eap-mail-x2s9kx`, cut from
> `origin/main` at `27b81a4` (fm #942). Born red on purpose; flips only after
> `python3 bootstrap.py check --strict` returns a real exit 0 read directly.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

E1 has been owner-reserved since 2026-08-01 and deferred four times. The owner
lifted the reservation live on 2026-08-24: *"today I want to work on and
possibly finish the final EAP mail."* The reservation was a stored instruction;
the live word wins, and the conflict is named rather than resolved silently.

The work is the half the evidence pack deliberately did not do: sweep **what was
already sent**, so the mail repeats nothing, and assemble the draft. The sweep
found one measured correction to the committed correspondence record and one
genuinely new spine for the mail — the estate spent the month **after** the
program auditing what the fortnight produced, and no other EAP participant can
send that.

## previous-session review

fm #942 (spider-bot registration) landed the ESTATE row and Layer-2 folder. It
left the repo clean at `27b81a4`; nothing about it blocks or feeds this session.

## Adversarial review — round 1, 10 findings, all conceded

`@codex` at `39753f5`: **10 inline findings, 9×P2 + 1×P3, every one accepted.**
Disposition `[conceded] ×10`, `[survived] ×0` — the tally is countable per
[`../docs/conventions/adversarial-review.md`](../docs/conventions/adversarial-review.md).
Four of them are the same species: **a bounded measurement restated at a wider
scope.** The mechanism behind the audit's worst findings became "the dominant
class of all 101"; a self-attested containment became "no access to the
answers"; a storage-composition measurement became "waste"; a grammar covering
undated standing walls became "reds any PR documenting a limitation". Each was
heading into a mail to a third party.

**A defect in the watching instrument, and a causal claim about it that had to
be withdrawn within the hour.** The poll loop interpolated curl output into a
`python3 -c` heredoc with `|| echo NO` as its fallback, so **any failure of the
check printed the same token as a genuine absence** — TRAP-003 committed by the
instrument built to detect it, with `docs/CAPABILITIES.md` already recording a
session losing 24 minutes to the same shape.

**The defect is real. The story first told about it was not.** This card, and
the reply to the owner, first said the loop *"reported no verdict for 11
iterations while a review and ten comments were already on the PR."*
`MEASURED` afterwards: `submitted_at` is **2026-08-24T19:29:21Z** and all ten
inline comments carry 19:29:21–22Z, whereas the loop's ~11 × 28 s ran before
that and a clean status-checked probe *preceding* it returned a genuine
`entries=0`. **So the review was absent for most of the loop, and the defect
cannot be shown to have hidden anything.**

**And the replacement story was wrong too, on the third telling.** *"Codex
answered at ~35 min"* was eyeballed off the polling, not computed. `MEASURED`
from the API: PR `created_at` **19:10:05Z**, review `submitted_at` **19:29:21Z**
= **19.3 min** open→review; the explicit `@codex review` at **19:21:07Z** was
answered in **8.2 min**. So the relay ran close to its recorded ~335 s once
*explicitly* triggered, and what actually underperformed was the **open**
trigger. That is a different fact from "Codex is slow", and the difference is
the whole diagnostic value.

Recorded because of *when* it happened — the over-claim was written into the
reply that was itself reporting four Codex findings of exactly this shape, a
bounded fact restated wider. The lesson the session already had in hand did not
bind the sentence it was writing, which is N3 measured on itself twice in one
session.

*(Two of the ten comments carry `commit_id f4e81600c3` rather than `39753f5` —
not a second round, and now measured rather than reasoned: both carry
`original_commit_id 39753f5f04` with `created_at` 19:29:2xZ. GitHub re-anchors a
still-applicable review comment to the newer head and keeps `original_commit_id`
as the record, so **matching on `commit_id` alone reads them as fresh
findings** — a sibling of the TRAP-007 note about matching verdicts per
surface.)*

## Adversarial review — round 2, 7 findings, all conceded

`@codex` at `f4e8160`, 19:42:57Z. **7 findings, all P2, `[conceded] ×7`,
`[survived] ×0`.** Running tally **17 conceded / 0 survived over two rounds.**

Three classes, and the middle one is the one worth keeping:

1. **Two round-1 fixes were partial.** The code-quality negative was removed from
   Finding 1 and left standing in an ask, in Part 1, and in the pre-send
   checklist that *asserted* the mail made no such claim. The thread-A
   correction was applied to the sweep and not to the correspondence record's
   own banner, which went on saying the 07-16 messages all re-verify.
2. **The N6 withdrawal was itself an append-without-retract.** The banner said
   the diagnosis does not reproduce; the paragraph under it still asserted it,
   and **three further live records** — `current-state.md`, the active-repo
   intent audit, and the program's own E1-prep row — carried it as fact where a
   cold session would meet it first. **The correction to the estate's flagship
   defect was committed in the shape of that defect**, twice: banner-over-claim,
   then no downstream sweep. Now struck in place in all four, with the
   `search/code` half and TRAP-003 explicitly preserved.
3. **Two owner boundaries were being quietly overrun.** Part 1 sat *inside* the
   COPY markers as 482 words of polished first person, labelled a scaffold in a
   header — but a header does not change what gets pasted, and the plan says his
   half is never ghost-written. Moved out of the block entirely; a pointer
   skeleton takes its place and the prose survives as explicitly-not-for-sending
   raw material. And Part 2 runs ~1,700 words against the plan's one-page cap:
   **surfaced as an owner call with two costed options, not resolved by a
   session** — the cap and *"add genuinely new points"* are both his, and they
   cannot both be met.

Two smaller ones, both wider-than-measured restatements: the catcher tally read
`local gate (3)` where the source says gate 1 + CI/GitHub 2, and the 116-statement
scope read *"every document the session was required to read"* where the source
says *"all three binding documents"*.

## Retraction shape is per-document, and the first pass got one wrong

Owner-review, 2026-08-24: *"did you think through the consequences of leaving
struck-through text in a prep document meant for a cold session?"* **No — the
first pass applied one shape to four documents.** The correct rule is that the
shape follows the document's job:

| document | shape | why |
|---|---|---|
| [the evidence pack](../docs/findings/2026-08-23-eap-evidence-pack.md) | **strike in place** | a dated record of what was measured on 08-23; deleting it would erase that the claim was ever made and let a future session re-derive it from the same source |
| [the intent audit](../docs/findings/2026-08-23-active-repo-intent-audit.md) | **strike in place** | same — a dated finding |
| [the program's E1-prep row](../docs/planning/2026-07-26-consolidation-program.md) | **strike in place** | the § 7 ledger is an append-only history of what each step did; a row that silently changes is a falsified history |
| [`current-state.md`](../docs/current-state.md) | **DELETE, leave a pointer** | it is a `living-ledger` answering *what is true now*. A struck paragraph there is dead weight on a read path, and its retraction has a home elsewhere. Corrected after the first pass struck it like the others. |

**The distinction, stated so it is reusable: strike a record, delete from a
ledger.** A dated document's value is that it says what was believed then, so
the strike *is* the content; a living ledger's value is that everything in it is
current, so a struck claim is the one thing it must not carry. Both obey the
same underlying rule — the retraction lands at the site — and they differ only
in whether the site is history or state.

## Adversarial review — round 3, 13 findings, all conceded

`@codex` at `94b8b0b`, 20:00:24Z. **13 findings, all P2. Tally over three rounds:
30 conceded / 0 survived.**

**The count went UP (10 → 7 → 13) and the reason is diagnostic, not alarming.**
Six of the thirteen exist *because of how round 2 was fixed*: findings 1, 2, 3
and 9 are all *"you corrected the mail and left the source sweep saying the old
thing"*, and 6 and 8 are stale cross-references created by that same editing
(ask numbers, decision counts). **Patching the outbound document without
propagating to its source manufactures the next round's findings** — which is
the append-without-retract mechanism again, one level up: the correction landed
somewhere, just not everywhere the claim lived. This round fixes at the source
and propagates outward.

**One is a straight refutation of a number that was in the mail.** The
116-statements-across-66-files figure does not reproduce: re-running the audit's
own published regex against this tree gives **125 across 72 files**. The 116 is
the 2026-08-08 audit-time count and belongs with the 16 incidents it was measured
against; the mail said it in the present tense under an as-of-24-August heading.
Now dated explicitly.

**And the Part 1 fix from round 2 was still not enough.** Moving the drafted
prose outside the COPY markers and calling it *"raw material to lift phrases
from"* still supplies his voice — the plan permits **at most a pointer
skeleton**. The prose is now **deleted**; Part 1 is a beat table of what each
paragraph must carry, with no sentences at all. Beat 3 is flagged as the one
nobody can supply for him.

Four more wider-than-measured claims removed from the mail: *"most of it
works"* (no denominator) · *"drift survives indefinitely everywhere else"* (one
surface, measured once) · *"agents created every byte"* (the audit measures
storage composition, not authorship of every byte) · *"only hooks firing at the
tool call caught anything"* (the table credits the owner 5, Stop hook 4, gate/CI
3, tests 2 — and the Stop hook is post-turn, not tool-call).

## Two owner-review challenges to round 3's fixes — both checked, both held

**1 · Was the 125/72 re-count inflated by artifacts, untracked files, or this
session's own writing?** Fair question: the audit's published block filters only
`node_modules` and `.git/`, so it would happily count anything else lying in the
tree. Decomposed three ways, `MEASURED`:

| variant | files / statements |
|---|---|
| the published block, verbatim | **72 / 125** |
| restricted to `git ls-files '*.md'` | **72 / 125** |
| tracked, minus the three files this session created | **72 / 125** |
| *(audit-time, 2026-08-08)* | *66 / 116* |

**Untracked contribution 0; this session's contribution 0** — the three new files
do not match the pattern at all. So the +6 files / +9 statements is genuine
corpus growth between 08-08 and 08-24, not self-inflation. `[survived]`, and now
decomposed rather than asserted.

**2 · Was "the audit measures storage composition, not authorship" read, or
assumed?** **Assumed** — it was taken from the reviewer's wording, and a claim
about what a document says was written without opening it, which is the estate's
own *"do not write about a file you have not opened."* Now read:
[`2026-08-14-railway-websites-audit.md`](../docs/findings/2026-08-14-railway-websites-audit.md)
§ 8 reports relation sizes with **separate table / index / TOAST columns**
(`btd6_source_snapshots` 668 MB total = 245 MB table + 22 MB index + **401 MB
TOAST**), states that the date columns show only *"the last observed ingestion
event; liveness at probe time is not"* established, and records that **nothing
was deleted and the ingestion loop was left running** with `OQ-BOT-DB-BTD6-PRUNE`
open. **No authorship claim anywhere in it.** `[survived]` — and the reading
strengthens the fix rather than merely confirming it: with 401 MB of one table
being TOAST, *"agents created every byte"* was wrong about the storage as well as
about the authorship.

## Round 3 was 14 findings, not 13 — the fourteenth was hidden by pagination

`MEASURED` 2026-08-24. `GET /pulls/943/comments` **defaults to 30 items per
page**. The PR had accumulated 10 + 7 + 14 = **31** inline comments, so the
unpaginated read returned exactly 30 and silently dropped the newest one. It
surfaced only because the webhook delivered it separately.

The lost finding was real and is now fixed: the mail, the sweep and the evidence
pack all said **61 doc-routes**; `.claude/hooks/doc-routes.json` holds **67**
(`len(json.load(...)['routes'])` → 67). The mail and sweep now carry 67 with the
measurement date; the pack keeps 61 as its own 2026-08-23 snapshot, marked as a
moving count.

**This is the fourth distinct instance in one session of a truncated or
over-narrow read reporting a false absence** — after `|| echo NO` swallowing a
failed check, matching round 2 on `commit_id` instead of `original_commit_id`,
and matching round 3 only at the current head. Each had a different mechanism and
the same shape: **the query decided the answer, and nothing said so.** Written
here rather than in the mail because it is the estate's own TRAP-003, not the
vendor's problem — but it is also the most honest illustration this session
produced of why the mail's central claim is true.

**The standing fix, in one line: always page, always check the status, never let
a filter be the only thing standing between a read and "nothing is there."**

**Correction to this section's own reasoning, owner-review 2026-08-24.** It
first said the pagination miss was kept out of the mail because it is *"this
estate's own TRAP-003, not the vendor's problem."* **That reason does not hold.**
The mail's subject *is* agent failure modes; a session building four different
false-absence checks — three of them inside instruments built to catch exactly
that — is squarely on topic, is measured, and is the most current evidence in the
whole document. The real trade-off is different and is the owner's: it is **n=1
self-observation** against the committed audits' measured n, and the mail is
already over its length cap. So it is now offered to him as a costed option
rather than silently excluded.

**And the CI/local comparison in the reply was overstated.** It claimed the hold
was *"verified by running the identical preflight locally against this exact
tree."* Neither half survives inspection: the CI job was for `059bfcd` and the
local run for `5e53541` — **different trees** — and the outputs are **not
identical**. CI reports **2 findings** (`[preflight-script]` +
`[session-card-hold]`); the local gate reports **1** (`[preflight-script]`) plus
a separate un-numbered *"session log … is missing: a completed Status"* line.
**Same root cause, different presentation.** The conclusion — no real defect,
every line in both outputs names the in-progress card and nothing else — is
established by reading both outputs, which is what should have been said instead
of asserting they were identical.

## What landed

- `docs/findings/2026-08-24-e1-source-sweep.md` — what was already sent, topic by
  topic; what was never sent; the mailbox correction; today's re-measured figures.
- `docs/planning/2026-08-24-final-eap-email-draft.md` — the assembled mail.
