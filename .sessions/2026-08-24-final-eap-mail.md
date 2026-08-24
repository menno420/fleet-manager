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
   raw material. And Part 2 ran ~1,700 words against the plan's one-page cap
  (1,851 by round 4 — it grew with every round; see the round-4 entry):
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

## Adversarial review — round 4, 9 findings, 8 conceded + 1 already fixed

`@codex` at `059bfcd`, 20:11:59Z. **8 conceded, 1 stale (the 61→67 route count,
already fixed at `5e53541` before the review ran). Four-round tally: 39 conceded
/ 0 survived.**

**The dominant failure mode is now unambiguous and it is mine, not the
reviewer's.** Findings 1 and 2 are *again* "the mail was corrected and the source
sweep was not" — **in the round whose commit message claimed to fix at the
source.** What actually happened: round 3's own findings were propagated, and the
new edits made in that same commit were not. So the strategy was applied to the
backlog and not to the work in hand, which is the same shape one level down.

**The structural fix, applied from this round on: every claim change ends with a
search for the claim across `docs/`, and the commit does not go until that
returns only the corrected form.**

**The first run of that fix was itself broken, and it is worth more than the fix.**
The command was a single `grep -rn` with five alternatives, one of which was
`never got\nan answer` — **`grep` reads `\n` in a basic pattern as a literal
backslash-n, so that alternative could not match a line break and therefore could
not fail.** It returned clean and was reported as a passing propagation check.
That is the session's **fifth** false-absence instance, and the first one inside
the instrument built in direct response to the previous four. Replaced with a
per-claim multiline `re.finditer` sweep that names each pattern and prints
`CLEAN` or the residual sites — a check that can distinguish "nothing there" from
"nothing could have matched". Seven patterns, all CLEAN at `dc7ed7d`.

**The transferable rule, since "write a better grep" is not one:** a check whose
failure mode is silence must be shown to fail at least once before its silence
means anything. None of the five false-absence instruments in this session was
ever tested against a case it should have caught. Recorded here because "be more careful" is the
non-fix this estate's own N3 finding exists to reject.

Two findings worth keeping beyond the fix:

- **A false fact was seeded into the owner's own prose.** The Part 1 fact table
  read *"promised 2026-07-21; sent 2026-08-24"* — a **send date for a mail that
  has not been sent**, in the one section he is meant to write from. If he sends
  tomorrow, the table hands him a false correspondence date about his own mail.
  Now explicitly "do not pre-fill".
- **The literal-cap option was arithmetic nobody did.** § 2 call 5 offered
  "keep findings 1–3, drop 4 and 5, keep asks 1–5 → ~700 words". Measured: that
  cut leaves **1,227**, because the good-parts block, the standing offer, the
  links and the framing all survive it. The option is now costed honestly and
  says what else would have to go.

Also: the tool-call-only conclusion survived in Finding 3 after ask 1 was
broadened; "never got an answer" claimed every channel where only the mailbox was
searched; and the Codex yield (13 findings / 5 rounds) was attributed to fm #812
alone when it is #812 and #813 combined — only the 335 s latency is #812's.

## The uniqueness claim, withdrawn — and the one absence claim that holds

**Withdrawn.** The sweep's § 4 was headed *"why nobody else can send it"* and
opened *"this estate is the only one that kept the entire output and spent the
following month auditing it."* **There is no basis for either.** This estate has
no visibility into what other EAP participants retained or did afterwards, and
none was sought — the vendor's own *"that's how we identified you as a power
user in providing ample feedback"* is about **feedback volume**, not about what
anyone kept. The claim was load-bearing: it was the stated justification for the
mail's entire structure, in § 4's heading and in the draft's decision table.
**It never reached the copy block**, so nothing false was heading to the vendor —
but a reason that does not hold is still the wrong reason, and the structure it
justified survives on a supportable one: the fortnight is already in their inbox
across four mails and the month after is not.

**And the contrast worth keeping, because it is the session's own standard
applied to itself.** Five absence-checks here returned confident wrong answers.
**The Gmail absence claim is the one that meets the bar those five failed**, and
the difference is exactly the rule this card records: *a check whose failure mode
is silence must be shown to fire before its silence means anything.*

| lane | the probe | its control | control result |
|---|---|---|---|
| outgoing | `in:sent 07-05→07-22`; `in:anywhere from:<owner> 07-01→07-16` *(+trash)* | `in:sent 07-15→07-18` | **fired** — returns the known 07-16 pair |
| incoming | `subject:"Claude Code Projects Review" in:anywhere` *(+trash)* | `in:anywhere from:anthropic.com 07-13→07-16` *(+trash)* | **fired** — returns 3 genuine vendor messages, not the acknowledgement |
| direct | `get_thread(19f41cd2e5380bb3)` — fetch by id, not a search | — | 2 messages |

**Both controls were demonstrated to fire on something they should catch.** None
of the five broken checks ever was. **Still not done, and stated rather than
buried:** no exact `rfc822msgid:` lookup, because the record carries the thread id
but no per-message ids for the four absent mails — that is the one retrieval path
left open, and if those ids ever surface it could overturn this.

## Adversarial review — round 5, 13 findings, all conceded

`@codex` at `0dc2f32`, 20:31:46Z. **13 findings, all P2, all conceded.
Five-round tally: 52 conceded / 0 survived.**

**This round is the answer to the sending-gate question, and it answers it the
uncomfortable way.** The gate was added on a base rate — *4 of 4 rounds changed
this document, 3 corrected errors that would have reached the vendor.* Round 5
then found **five more vendor-facing errors**, three of them in claims this
session had already "fixed" once:

- **WITHDRAWN — "a full read of every tracked file".** The audit records 19
  files (~22 MB) inspected for **structure**, not line by line, and says the
  distinction is not cosmetic. The mail claimed exhaustive content inspection to
  a third party.
- **WITHDRAWN — "no agent surface could see any of it".** False, and the audit
  is the refutation: it measured those costs **agent-side**, over Railway
  GraphQL and the usage API. The replacement is narrower and better — *nothing
  surfaced it during normal operation; cost had to be gone looking for.*
- **WITHDRAWN — "which is every review a human actually performs".** A universal
  about all human review, from a sample of several sessions missing seven
  defects.
- **The 949 MB / 97.5 % figures** were 2026-08-20 measurements stated in the
  present tense on 08-24, against a store still ingesting.
- **The re-run promise** — the mail invited the recipient to re-run the
  published commands. They enumerate the account through `/user/repos` with the
  owner's PAT and include private repositories: **the method is reproducible,
  the inputs are not.**

**And one that refutes this session's own measurement.** The regex recount is
**126 across 73 files**, not 125/72 — because `.sessions/2026-08-24-final-eap-mail.md`
now matches on *"do not write about a file you have not opened"*, a phrase this
card added while recording that very rule. The decomposition that said "this
session's contribution: 0" was true when run and false by the time it was
quoted. **The act of writing up the measurement changed the measurement** — and then did
it twice more: 125 when first run, 126 when Codex ran it, **127** when re-run
during the owner-review of the reply reporting 126. Each write-up added a phrase
the regex matches. **Resolution: the mail no longer quotes a current count at
all.** The argument needs only the fixed pair — *116 statements, 0 of 16 caught*
— and that does not move. A number that changes because you described it is not
evidence you can hand to anyone.

## The propagation check is now a committed tool, not a claim

Round 5's sharpest finding: the "structural fix" announced in round 4 existed
**only as prose in this card** — no script, no patterns, no fixture, no way for
anyone to run it or show it could fail. An unrunnable check is the thing this
session keeps being caught by, described rather than built.

Now [`tools/check_claim_propagation.py`](../tools/check_claim_propagation.py),
12 patterns, and its `--selftest` has **two** halves because the first alone
would have been the next mistake:

- **A — every pattern must match its fixture.** A pattern that cannot fire is a
  dead pattern, not a clean repo. This is precisely where round 4's
  `never got\nan answer` grep failed.
- **B — the retraction filter must not swallow a live claim.** Silencing false
  positives by widening the filter is the obvious next error: widen it far
  enough and the sweep can never fail again. So each fixture is also run through
  the filter alone and must still be reported.

`--selftest` → 12 fire, none swallowed. Sweep → **0 residual**.

## "Precision" was the wrong word — a commitment and a factual claim changed

Owner-review, on the framing *"the substance has been stable for three rounds;
what keeps changing is precision"*: **that is not true of round 5, and the
distinction decides whether further review is worth running.**

| round-5 change | what kind of change it actually is |
|---|---|
| *"a published command you can re-run"* → the method is reproducible, the inputs are not | **A COMMITMENT.** The mail offered the recipient something this estate cannot give them: **3 of 27 repositories are private** (`estate-backups`, `pokemon-mod-lab`, `shiftlife`, `MEASURED` from the census JSON), so no third party re-running the recipe reaches the same total. Withdrawing an unhonourable offer is not precision. |
| *"no agent surface could see any of it"* → nothing surfaced it during normal operation | **A FACTUAL CLAIM THAT WAS FALSE**, refuted by the very audit cited for it — that audit measured the costs agent-side over Railway GraphQL and the usage API. **Ask 5's justification moved from "impossible" to "not proactively legible"**, which is a weaker and true reason for the same ask. |
| *"a full read of every tracked file"* | **A SCOPE CLAIM** — 19 files (~22 MB) were structural reads, and the audit says the distinction is not cosmetic. |

**What has genuinely been stable is the thesis** — the wall is human review
because the defects are shaped to survive it — and the five findings' identity.
**What changed is what the mail asserts and what it promises.** Calling that
precision made stopping look cheap; it is not, and the base rate (5/5 rounds
finding vendor-facing changes) is the reason the stopping criterion is *"a round
that changes nothing outbound"* rather than a round count.

**One phrasing of my own, corrected here rather than left standing:** I told the
owner Anthropic *"cannot actually re-run"* the measurements. Measured basis: 3 of
27 repositories are private. What follows is narrower — **they cannot reproduce
the same total**; they could run the method over the public subset, and could run
it in full if the owner granted access. The mail's own wording was already the
accurate one; the reply summarising it was not.

## Adversarial review — round 6, 11 findings, 10 conceded + 1 stale

`@codex` at `74a1905`, 20:50:27Z. **10 conceded, 1 already fixed** (the sending
gate's 4-of-4 figures, corrected at `0793ec4` after the review ran).
**Six-round tally: 62 conceded / 0 survived.**

**The stopping criterion said: stop when a round changes nothing outbound. Round
6 changed five outbound things**, including a wrong denominator, so it does not
stop here.

**An arithmetic error that was heading to the vendor.** The audit says the
database is 949 MB, **939 MB of it `public`**, and 97.5 % of *that 939 MB* is the
three ingestion tables. The mail applied 97.5 % to the **whole 949 MB**. Correct:
97.5 % of the public schema, or **~96.5 %** of the database. Wrong denominator,
in a figure offered as a measurement.

Also outbound: *"most-looked-at page"* was an unmeasured superlative (nothing
records page views) → *"most visible public surface"*; the ask still said every
catch came from something firing when **two of sixteen were after-the-fact
only**; the paragraph explaining why a count was withdrawn **introduced a new
unsupported count** ("re-run four times" against three recorded runs); and the
length figures were stale again — **2,082 words**, not 1,851, with the
literal-cap cut at **1,434**, not 1,227.

## The checker had the same defect it exists to prevent — one level deeper

Round 6's sharpest finding: **`--selftest` part B did not run the production
path.** It tested each bare fixture against the filter, while `sweep()` applied
the filter to the whole enclosing block. **So a live claim sharing a block with
an unrelated retraction was swallowed in production while the test passed** —
a check that cannot fail, in the file written to stop checks that cannot fail.

Two changes, and the second is the one that makes the first believable:

1. **The marker must belong to the claim, not the block.** A bounded window
   (`NEAR_BEFORE=320`, `NEAR_AFTER=160`) replaces "anywhere in the paragraph".
2. **Part B now embeds each fixture in a hostile block** — a live claim, filler,
   then an unrelated *"another claim was corrected"* — and asserts the live claim
   is still reported.

**Demonstrated, not asserted:** restoring the old whole-block window makes
part B report `SWALLOWED BY FILTER` on **all 12** patterns and exit 1. The test
fails when the thing it guards regresses. That is the property the previous two
versions of this check claimed and could not show.

*(One P3 accepted: the header said grep reads `\n` as a literal backslash-n.
GNU grep 3.11 actually matches `never gotnan answer`, and the standard calls a
backslash before an ordinary character unspecified. The conclusion held; the
mechanism was wrong.)*

## What landed

- `docs/findings/2026-08-24-e1-source-sweep.md` — what was already sent, topic by
  topic; what was never sent; the mailbox correction; today's re-measured figures.
- `docs/planning/2026-08-24-final-eap-email-draft.md` — the assembled mail.
