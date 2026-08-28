# The OD-24 round's open questions — the discussion agenda

> **Status:** `living-ledger` · assembled 2026-08-28, after the round's three
> audits landed (fm #956 · #959 · #960; kit #587 · #588)
>
> **What this is:** the input to the review-and-discussion sitting the owner
> asked for — *"the next session can review everything that these 3 audits have
> produced, and then helps me to discuss and answer the open questions"*
> (live, 2026-08-28, after session 3 merged). One row per question that is
> genuinely his, each phrased so he can answer it in a sentence.
>
> **What it is NOT:** a work plan, a decisions ledger, or a second owner-queue.
> Answers given in the sitting come back to
> [`../owner-queue.md`](../owner-queue.md) as entry updates and to the program
> as directives; this file feeds those, it does not replace them. It also does
> not carry the estate's product letters — those live in the queue and are
> pointed at in § 3.
>
> **How it was built, so its verdicts can be checked:** seven reader lanes over
> the three audits, the owner-queue, both 2026-08-27→28 owner-direction
> records, the Layer-2 round thread, the v1.21.0 worklist and the program +
> roadmap; 68 candidate questions harvested; each of 26 then put through an
> **adversarial verifier** told to refute that it is a live owner question, to
> re-classify owner-only vs agent-derivable, and to phrase the survivor in
> plain language. Coverage and its limits: § 7.

## 0 · The headline — the round asked you for things your own record already answers

**Five of the questions this round queued for you are already answered in the
committed record; two more are narrower than they were posed; and one a first
cut called answered turned out to still be yours.** The round is an audit of
unrouted knowledge; its own output turned out to carry the same defect. Read
§ 4 before the sitting — it is what keeps the conversation short.
*(These counts were wrong twice before Codex review forced them to be computed
from § 4's own rows rather than asserted. § 4 now holds eight rows: five
answered, two narrowed-but-still-asked — the confirmation doctrine as § 2 · B2
and the spend window as § 2 · H — and one struck through and restored to the
agenda as § 2 · E2. That this file's own audit arithmetic needed three passes
is itself a datum about hand-carried counts.)*

The sharpest instance: session 2 queued `OQ-KIT-PROMPT-DOCTRINE` asking which
of your rules governs a kit-planted brake, citing superbot:Q-0128 from
**2026-06-13**. But `.claude/hooks/README.md:483-486` carries a **later** you,
verbatim, from **2026-08-09**:

> *"Delete triggers are the only thing that gives me an approval prompt in
> automode, this will stall your session untill I get back. Always prevent
> using them."*

That is the same subject two months on, and it is narrower than the June line:
you named the one call that actually raises a prompt and asked for it to be
prevented — not for all confirmation to be abolished. **It sharpens the letter
without settling it**, because it says nothing about whether a *send* or a
*delete* may still ask first — so the fork is on the agenda as § 2 · B2 rather
than closed. *(An earlier cut of this paragraph called it "mostly answered" and
folded the residue into § 2 · B, which is a different subject entirely —
waiting for review, not interrupting you. Codex review caught it; the
correction is the kind of thing this round exists to make.)*

**And the second headline, which is not your fault and not quite ours
either: the three letters this round has been waiting on for three sessions
were never in the queue you read.** Move 1's GO, the journal question and the
§10 disposition confirmations have been recorded in every session card and
Layer-2 thread since 2026-08-28 as *"unanswered"* — but `MEASURED` at
`origin/main` today, `docs/owner-queue.md` carries **134 `OQ-` references and
not one entry for any of the three** (the only *journal* hits are the OneDrive
hub's `journal.md`, unrelated). They lived in audit findings, which are
`RECORD`-tier documents you have no reason to open. So *"the letters remain
unanswered"* — a line three sessions repeated — was true and misleading: the
asking never actually happened in the place asking happens. **This file is
the first surface that carries all three where you look**, and the queue now
points at it.

## ✅ THE SITTING RAN — 2026-08-28, owner-live. This file is now a RECORD, not an agenda.

**Every § 2 and § 2b row was put to him and answered, plus two of § 3's three.**
Verbatim answers, `OWNER` separated from `DERIVED`, and the reasoning behind each
derived consequence: [the sitting record](../findings/2026-08-28-od24-sitting-answers.md). Answers were routed the
same session to [`../owner-queue.md`](../owner-queue.md) (7 entries updated, 1
added), [`../decisions.md`](../decisions.md) (`[D-0011]` reconciled) and the
program's OD table.

| row | his answer | where it landed |
|---|---|---|
| **§ 2 · 0** which ways it doesn't work | **one root cause** — *"agents don't take enough initiative to leave the repos in a better shape"* | re-ranks the round; § 4 of the record |
| **§ 2 · A** June rules | *"Some of them might not be relevant anymore, but most of it still stands"* — a **fourth** option, none of the three offered | § 1 |
| **§ 2 · B** blocking | **never block; guarantee pickup** | § 2 |
| **§ 2 · B2** brakes prompting | **presence decides** — never while away, freely when present | `OQ-KIT-PROMPT-DOCTRINE` ✅ |
| **§ 2 · C** Move 1 | **HELD** — and § 13 makes it a *stage* with an exit condition | `OQ-KIT-MOVE1-GO` ⏸ |
| **§ 2 · D** the interview | **something asks, and filters** — not him | § 8 |
| **§ 2 · E** AGENTS.md | **hand-write per repo** | § 6 |
| **§ 2 · E2** the journal | **delegated**, with a function named → decided: keep, re-scope, route | `OQ-KIT-JOURNAL-SURVIVES` ✅ |
| **§ 2 · F** leftovers | **a standing surface he reads** — scheduled unattended draining **refused** | § 10 |
| **§ 2 · G** card deletion | **not asked** — its own minimum answer was *nothing today*, pending the report-only census | unchanged |
| **§ 2 · H** spend caps | *"There hasn't really been much API use lately, so this is currently not relevant"* | `OQ-EAP-SPEND-WINDOW-MOOT` ✅ |
| **§ 2b** kit charter | **rewrite it to say initiative** | § 9 |
| **§ 2b** provider mix | his to work out, sequenced **after** the plan — and he named the **method** | § 16 |
| **§ 2b** kit name | **change it**, but he picks the name later | `OQ-KIT-RENAME` (new) |
| **§ 2b** next release | **cut when the next fix batch lands**; adopter half still open | `OQ-KIT-V1-21-RELEASE` ◐ |
| **§ 3** D2's target | **`spider-swing`** — the measured order ratified | `OQ-FM-D2-TARGET` ✅ |
| **§ 3** the EAP mail | *"leave it"* → **revised minutes later to "soon"**, with a widened brief | `OQ-E1-FINAL-EAP-EMAIL` ▶ |
| **§ 3** the BTD6 loop | **not asked** — a product question for its own sitting | unchanged |

**And one thing he said that was on no agenda**, which reframes all of the above:
*"I am currently running 3 parrallel ultracode session to map most of all the
repos, once this mapping is all done we should use this information to come up
with a revised pan. Only after that will we move to execution of the 'GO'"* —
so this round's output is **an input to a revised plan**, not a work queue. § 13
of the record.

**The headline measurement.** His list and ours **converge on one cause**, and the
divergence is one of *altitude*: we ranked twelve gap classes; he named a single
root cause they are all downstream of. The round had already found it — dig § 6.1
called the missing initiative half *"the central drift … and the review round's
real charter"* — and then organised itself around the gap table anyway. **The
round reproduced, on itself, the unrouted-knowledge defect it was auditing.**

## 1 · How to use this in the sitting

- **§ 2 is the agenda.** Eleven questions, ordered by dependency, not by size —
  start at § 2 · 0, which is the one nobody ever asked you. Each carries: the
  ask in plain language · the options · what it unblocks · what the minimum
  answer is. **§ 2b adds four short ones** the audits never phrased as
  questions at all.
- **Read § 4 first if the sitting is short.** It removes five things you might
  otherwise be asked.
- **§ 5 is not for you.** It is what a session should simply decide, recorded
  here so the sitting does not spend your attention on it. Your own rule
  governs: *"unnecessary asks are the waste, but a question that prevents a
  misread goal is a good trade"* ([`../intent.md`](../intent.md) § 3).
- **Silence is not consent in this file.** Every row is here precisely because
  no session may derive it.

## 2 · The agenda — in dependency order

### 0 · Which ways does the kit still not work? — the question nobody asked you

**✅ ANSWERED 2026-08-28 — one root cause, not a list:** *"they are all related to the same root cause, which is mostly that agents don't take enough initiative to leave the repos in a better shape"*. See § 4 of [the sitting record](../findings/2026-08-28-od24-sitting-answers.md) for why this re-ranks the round's own output.

**The ask.** When you ordered this round you said, of stepping back to see how
agents cope with the substrate-kit: *"in some ways it actually goes well, but
in a lot of ways it still doesn't."* **No session has ever asked you which
ways.** Three audit sessions then reconstructed a failure list from the
committed record — twelve classified gaps, a doc-surface census, a router
re-read — and that list is an inference from traces. Yours is first-hand.

**Why it goes first.** If your list and ours agree, the round's priorities are
confirmed and everything below is well-aimed. If they diverge, the divergence
is the single most valuable measurement this round could produce — it tells us
exactly where reading the record fails to see what you see.

**Minimum answer:** two or three things that annoyed you, in any order, in
your own words. Not a structured list — the structuring is ours.

**Evidence:** [OD-24 § 5](../findings/2026-08-28-owner-direction-agent-autonomy.md)
(line 185, verbatim) · the reconstructed list is dig § 7.

### A · Do your June rules still stand by default, or are they history?

**✅ ANSWERED 2026-08-28 — and with a FOURTH option, not one of the three offered:** *"Some of them might not be relevant anymore, but most of it still stands."* Standing is the default; the obsolescence exception is real but is **his** to apply, so a session flags a rule for retirement and keeps obeying it meanwhile. § 1 of [the sitting record](../findings/2026-08-28-od24-sitting-answers.md).

**The ask.** Through June and July you told the agents a lot of things —
*never show me a confirmation prompt again* · *if I asked for it personally,
merge it immediately, don't hold it for review* · *when you hand me steps,
mark each one safe / undoable / permanent*. The router band re-read found
**five of those absent from every live fleet-manager document**, carried only
in frozen or seat-era surfaces. So: do they still bind?

**Options.** (a) They stand until you retire one — agents should treat the
router's June rulings as live estate law. · (b) They are archaeology: only
what has been re-stated since the program closed binds. · (c) Case by case —
and then the two that actually collide with this round's work are the ones to
settle now (they are B and the merge-fast pair below).

**Why it is first.** It governs the two questions after it. If June's
*merge-immediately-when-I-asked-for-it* still binds, that constrains any gate
this round builds; if it does not, the gate is free.

**Minimum answer:** one sentence choosing (a), (b) or (c). Explicitly **not**
needed: walking the thirteen census entries rule by rule — that would consume
the whole sitting.

**Evidence:** [the router band re-read](../findings/2026-08-28-router-band-reread.md) § 2.

### B · May anything ever block a session from calling its work "done"?

**✅ ANSWERED 2026-08-28 — NO. Never block; guarantee pickup.** Confirms his own June design (Q-0180 + Q-0174). Build the consumption loop, build **no** gate. § 2 of [the sitting record](../findings/2026-08-28-od24-sitting-answers.md).

**The ask.** A session is supposed to wait for the second opinion before it
calls a piece of work finished, and it keeps not waiting — measured five times
in one day with the rule written down and a reminder firing at the exact
moment. There are two ways to handle that, and only one of them needs you:
either something is allowed to **block** the finish until the review lands, or
nothing blocks and we instead guarantee the findings get **picked up** by the
next session.

**Why you and not us.** You have said twice that agents over-add walls, and
you once retired a review gate yourself because it was unused friction. A
blocking gate is exactly the class you dislike. We will not build one on our
own judgement.

**Options.** (a) Yes — something may block "done" until review answers. ·
(b) No — never block; just guarantee consumption. · (c) Yes, but work you
personally directed is exempt (this is the June rule from A).

**Minimum answer:** one sentence, plus that exemption clause if (a) or (c).

**What we do either way, without asking:** build the consumption loop — the
next session fixes what the reviewer flagged first. That adds no restriction
and needs no GO.

**Evidence:** dig § 7 gap #7 · re-read § 3 (superbot:Q-0180 + Q-0174 accepted
the race *because* a consumption loop existed) · OD-24 § 3.

### B2 · May a brake ever stop and ask you — and for what?

**✅ ANSWERED 2026-08-28 — PRESENCE DECIDES:** *"Never while I'm away; freely when I'm present."* The conflict was real; he resolved it by drawing a line neither rule drew — **presence** — so Q-0128 is **superseded**, not reinterpreted (corrected on Codex fm #964). `delete_trigger` stays prevented in every venue. `OQ-KIT-PROMPT-DOCTRINE` closed. § 3 of [the sitting record](../findings/2026-08-28-od24-sitting-answers.md).

**The ask.** Separate from B, and it stayed open after a first pass wrongly
folded it into B (caught on review). B is about *waiting for review before
calling work done*. This one is about **interruption**: may a kit-planted brake
ever surface a prompt that waits for you?

Two of your own rules point opposite ways. June: *"I never want to see such a
prompt asking me for my confirmation ever again, no matter what it is for."*
This month (OD-24 § 3), the re-ratified line keeps **confirm before sending or
deleting**. Your 2026-08-09 words narrow the gap but do not close it — you
named `delete_trigger` as the one call whose prompt stalls a session and asked
for it to be prevented, which says nothing about whether a *send* or a *delete*
may ask first.

**Why it cannot be derived.** Left unresolved, a session either skips a
confirmation you require or introduces a prompt you banned — and which of those
it does is currently luck.

**Carved out of every option, because you already settled it:**
`delete_trigger` is never prompted for — it is prevented, per your 2026-08-09
instruction. No answer below re-authorises it.

**Options.** (a) Never prompt — brakes refuse or proceed, never wait. ·
(b) Prompt only before something leaves the estate or destroys data (sends,
deletes, `delete_trigger` still excluded) — the OD-24 line, which means
accepting the occasional wait. · (c) Never prompt while you are away; prompt
freely when you are present.

**Minimum answer:** one sentence choosing (a), (b) or (c).

**Evidence:** `OQ-KIT-PROMPT-DOCTRINE` (narrowed, still open) ·
superbot:Q-0128 · OD-24 § 3 · `.claude/hooks/README.md:483-486`.

### C · Move 1 — GO or hold, and how far does the GO reach?

**⏸ ANSWERED 2026-08-28 — HELD, and it is a STAGE not a deferral.** He chose hold over three GO shapes, then gave the exit condition unprompted (mapping → revised plan → execution). **Do not re-put this until that condition is met**, and build nothing Move-1-shaped under another name. § 7 + § 13 of [the sitting record](../findings/2026-08-28-od24-sitting-answers.md).

**The ask.** When a session finishes, nothing asks it what it left behind for
the next one — and that is precisely the habit that stopped working when you
stepped back. Move 1 is one line every session must fill before it can close:
*did I leave an idea, a note in the running journal, both, or nothing?* It is
designed, evidenced and **held** — you said *"no execution yet, because I
still have more to plan"* on 2026-08-28, and nothing since lifts that.

**Options if GO.** (a) fleet-manager only, as a prototype we measure ·
(b) prototype **plus** a kit release · (c) the whole chain, including the
adopter hops.

**Minimum answer:** one word — **GO or hold** — and if GO, one letter for how
far. Everything else about it is ours to sequence.

**Depends on B:** whether that line may *block* the close is B's answer, not
this one.

**Evidence:** dig § 11 item 3 · OD-23 (the hold) · OD-24 § 7.

### D · The end-of-session questions — do you ask them again, or does something ask for you?

**✅ ANSWERED 2026-08-28 — something asks, and shows him only what is worth showing.** The questioner is **not him**. **This is NOT a GO for § 2 · C** — reading it as one would be the inference-as-owner-decision failure recorded twice in this estate. § 8 of [the sitting record](../findings/2026-08-28-od24-sitting-answers.md).

**The ask.** In June you used to ask each session a few questions when it
finished — what did you learn, what should change — and you decided which
answers became standing rules. That interview is the single practice that
stopped when you stepped back; everything with a switch behind it survived.
The mining half still ships in the kit (it collects the ideas); the **asking**
half and the **you-ratify-it** half are what went missing.

**Options.** (a) You ask them again, yourself, when you feel like it. ·
(b) Something asks on your behalf and shows you only what it finds worth
showing. · (c) Leave it — the loop stays one-directional.

**Minimum answer:** one sentence naming the questioner. The routing is ours;
the ratification rule is already yours and is not re-asked here.

**Evidence:** dig § 4 (the reflection interview row) · § 5.

### E · AGENTS.md — what should the nineteen files actually say?

**✅ ANSWERED 2026-08-28 — hand-write per repo.** PKT-B4's recorded position is confirmed by him, shown the trade and choosing it anyway; the kit does **not** plant or maintain them. Closes the fork in both places this file carried it. Execution stays behind the packet hold. § 6 of [the sitting record](../findings/2026-08-28-od24-sitting-answers.md).

**The ask — and it is the MECHANISM, which two earlier cuts of this file
wrongly moved off your plate.** You already decided every repo gets a small
*start here* note, and that public is fine. What is still yours is **how the
nineteen get made and kept fresh**: does the substrate-kit **plant and
maintain** them, so upgrade waves keep all nineteen current — or are they
**hand-written once per repo**, as PKT-B4 records?

**Why it is yours, on the record's own say-so.** Your own direction record
names this exact fork as reserved for this sitting:
[`../findings/2026-08-28-owner-direction.md`](../findings/2026-08-28-owner-direction.md)
`:147-150` — *"The kit questions are open for the kit sitting, including one
his AGENTS.md yes reopens … whether the kit should plant/maintain `AGENTS.md`
so upgrade waves keep 19 files fresh, versus PKT-B4's recorded
hand-write-per-repo."* *(A verifier here judged it agent-derivable and this
file removed it; Codex review on fm #961 produced the line above and it wins —
the record beats an inference about the record.)*

**The evidence you may want, since it cuts against planting:** you once ruled
that *"generating 24 stubs that then rot would be worse than the current gap"*,
and the kit's planted journals were measured **byte-identical to their template
in 11 of 14 repos** — planting is exactly what rotted last time. Against that:
hand-writing nineteen files has no maintenance story at all.

**Options.** (a) The kit plants and maintains them. · (b) Hand-write per repo,
as PKT-B4 has it. · (c) Plant a minimal pointer the kit maintains, hand-write
anything beyond it.

**Minimum answer:** one sentence, (a) / (b) / (c).

**What is NOT asked here:** the *content* — PKT-B4 already specifies the
one-line purpose plus pointers, so there is no content fork to spend the
sitting on. Execution of the nineteen still sits behind the packet hold.

### E2 · Does the per-repo journal survive at all?

**✅ ANSWERED 2026-08-28 — DELEGATED, with a function named:** *"Your call … But I think the session journals would definitely add some value so we can easily find out what went wrong each session."* **Decided under that delegation: keep it, re-scoped to that function, and route it before enforcing it.** His conditional is answered on **lifecycle, not scope**: a trap register admits what is already recurring and preventable; he asked for what went wrong *each session*. *(The first cut's "estate-scoped" leg was refuted at source by Codex fm #964 — roadmap § 5.3–5.4, `OWNER`, makes per-repo traps the intended design.)* § 5 of [the sitting record](../findings/2026-08-28-od24-sitting-answers.md).

**The ask.** Every repo carries a planted `.session-journal.md` — a running
notebook a session is supposed to add to. **The dig measured** that no checker
references it, that it is absent from every boot list, and (with OD-21's
census) that it stayed byte-identical to its planted template in 11 of 14
repos; those are its findings, cited here rather than re-measured. So it was
never adopted by mechanism alone. Two ways forward, and the audits say this one is yours: does
the journal **survive** as a per-repo surface worth enforcing, or is it
**superseded** by routed records of the `traps.md` kind — the structured
recurring-trap lifecycle your own roadmap § 5.4 specifies?

**Why it is yours.** The genesis dig's gap table states it directly: *"separately
decide whether the journal should survive as a per-repo surface or be
superseded by traps.md-style routed records — **a round question for the
owner**"*. *(An earlier cut of this file closed it on the grounds that roadmap
§ 5.4 already specified the surface. Codex review established that § 5.4 never
mentions `.session-journal.md` — grep, zero hits — so it is one side of the
fork, not its answer.)*

**Options.** (a) Keep the journal and enforce it. · (b) Retire it; routed
trap/idea records carry the function instead. · (c) Keep it, unenforced, and
stop pretending it is a contract.

**Minimum answer:** one sentence.

**Evidence:** dig § 4 + gap #2 · the roadmap's § 5.4.

**Evidence:** `OQ-FM-AGENTS-BOOT` (answered yes, estate-wide) · OD-23 § 6 ·
OD-24 § 7 (plant-vs-hand-write parked *for this round*).

### F · Who works the leftovers pile — you, or a schedule?

**✅ ANSWERED 2026-08-28 — a standing surface he reads.** And a **negative worth recording**: two options offered scheduled unattended draining and he took neither, so that is **not** sanctioned. Fix family for gap #6 is **route**, not build-procedure. § 10 of [the sitting record](../findings/2026-08-28-od24-sitting-answers.md).

**The ask.** There is a pile of small jobs nobody comes back to: fixes the kit
itself needs, ideas from old sessions, write-ups we said we would do. The only
thing that has ever drained it is you asking, as you did this week — three
items moved and the rest sat. Two things here are genuinely yours: whether you
want a **standing surface pointed at you** (that is a commitment of your
attention, and nobody can derive what you will actually read), and whether
**scheduled unattended agent sessions** are sanctioned to drain it (that
spends money while you are away, which your own safety line reserves for you).

**Options.** (a) A standing surface you read. · (b) Scheduled sessions that
drain it unattended. · (c) Both — name which leads. · (d) Neither; leftovers
wait for you to ask.

**Minimum answer:** one sentence. **Not** needed: any cadence or number — your
own no-fake-precision rule sends that to prototype time.

**Evidence:** dig § 7 gap #6 · re-read § 3 (superbot:Q-0124, Q-0153) ·
the v1.21.0 worklist's standing rows.

### G · May old session cards ever actually be deleted?

**◻ NOT ASKED 2026-08-28 — deliberately.** This row's own minimum answer is *nothing today*; the report-only census is its prerequisite and has not run. Unchanged and still his, once there are real numbers.

**The ask.** Every session leaves a written note. There are now **343** in the
toolbox repo and **431** here, and nothing has ever tidied them — even though
the kit *ships* a tidy-up that deletes an old note and leaves a one-line
receipt behind, with the full text still recoverable from history. You picked
that posture yourself in July (superbot:Q-0214, *"delete with tombstones"*);
it shipped in v1.0.0 and has never once been switched on, on any corpus.

**Read this with OD-25, which landed while this agenda was being assembled.**
In a parallel sitting (fm #962) you were offered the ~150k cold-boot context as
an optimization target and **declined it**: *"this booting context does not seem
weird to me nor bothers me … the memory my agents have … is the most valuable
thing we have now"*, with the rule that **token count is not a defect;
duplicated, stale or mechanically derivable context is**. So this question is
**not** "may we cut for size" — that framing is already answered, no. It is
narrower: whether *spent* cards may be pruned once a census shows which are
genuinely dead weight, with the full text still recoverable.

**The order matters.** A session will first run the **report-only** census —
declare what would be pruned, delete nothing — because that needs no
permission and turns this from a preference into a number. Your answer is only
needed **after** that: with the real numbers in front of you, may cards
actually be deleted with a tombstone, or do we keep everything forever?

**Minimum answer:** nothing today. One sentence once the census lands.

**Evidence:** [the truth pass](../findings/2026-08-28-kit-tree-truth-pass.md)
§ 3 + § 5's carved-out last row.

### H · Spend caps — the ten-second one

**✅ ANSWERED 2026-08-28 — not currently relevant:** *"There hasn't really been much API use lately."* A dismissal on relevance, **not** a no-ceiling-forever ruling; no cap adopted, **no meter ordered** (that option was offered and not taken). Its prerequisite was discharged first — `[D-0011]`'s self-contradiction is reconciled. § 17 of [the sitting record](../findings/2026-08-28-od24-sitting-answers.md).

**The ask.** In early July you said the AI bills were not really a problem and
you would rather watch a couple of months and decide from the average. That
window lands about now — but **no meter ever ran** (the telemetry feed carried
no cost and stopped 2026-07-13), so there is no average to look at.

**One thing to fix before you answer, and it is ours not yours** *(two review
rounds landed on this; the second was right)*: the ledger contradicts itself.
`[D-0011]` is titled *"capped at its balance"* and justifies itself by a **€10
prepay with auto-reload off**, while its own 2026-08-11 amendment says the same
variable, `GEMINI_API_KEY_PAID`, **bills your card** on `generativelanguage`
(measured €0.49 → €7.88 month-to-date). Those cannot both be the current
picture, and a session must reconcile them against the live billing surfaces
**before** the sitting — otherwise *"leave it"* could be read as ratifying a €10
ceiling that no longer exists.

**Then the question, which is genuinely yours:** for AI spend going forward, do
you want any ceiling at all, or do you keep deciding by watching?

**Minimum answer:** one sentence — *no ceiling*, or *a ceiling* plus a rough
number and what it covers.

**Prior, so you can answer in a breath:** your own recorded position is
*"budget so far is not really a problem"* and *"we spend way too much time on
safety … this is just a hobby project"*. The one thing that changed since: the
paid key now bills your card directly, which was not true in July.

**Evidence:** kit `docs/program/rulings.md` **PL-005** (Q-0249 is already
program law, not a dangling obligation — see § 4) · `[D-0011]`.

## 2b · Four more the audits never turned into questions

Surfaced by the completeness pass, each verified at source this session. They
are shorter than § 2's rows and mostly answerable in a breath.

- **The kit's charter never mentioned the thing you built it for.** You said
  the kit exists *"so agents become more autonomous and think more for
  themselves and take more initiative"* (OD-24 § 2) — and the word
  **initiative appears nowhere** in the kit's README, its closeout, or its
  program-law register (grep, zero hits, re-run this session). So: should the
  kit's stated purpose be rewritten to say that, or is the charter fine as
  built and the initiative duty lives in the estate's rules instead?
  *One sentence.*
- **OD-13 named two prerequisites before product work; only one has been
  worked.** Verbatim: *"further improve the methods and the rule enforcement"*
  **and** *"further define the right mix of AI agents across different
  providers"*. Everything since — the roadmap, this round — is the first.
  The provider mix has had no session. Does it get one, and is that before or
  after the round's remaining work? *One sentence.*
- **The kit's published name is still a placeholder, by its own README.**
  `README.md:9` reads *"`substrate-kit` is a placeholder name"* and defers the
  published name to you. It has shipped 21 releases under it. Keep the name,
  or change it now while the adopter list is still short? *One word.*
- **The kit's own fixes are finished and unreleased — when does the next cut
  happen, and who gets it?** kit #587 and #588 both ride `main` unreleased, and
  `OQ-KIT-V1-21-RELEASE` still has an open half: which remaining adopters take
  the v1.21.0 hop (`pokemon-mod-lab` is owner-held, `superbot-games` was "no
  adopter yet", `trading-strategy` is archived now). Releases are owner-paced by
  your own standing call, so this is a genuine ask rather than a queued job.
  *Cut now, cut when the next fix batch lands, or leave it — plus any adopter
  you want moved.* *(Promoted here from the unverified residue on review: it is
  source-verified in the queue and in the worklist's tail, and leaving it in a
  "do not ask this" section would have parked the round's own output
  indefinitely.)*

## 3 · Also yours, but not this round's

The owner-queue carries the estate's open product letters, and they are
**not** on this agenda — they belong to their own repos and sittings. Three
were verified still-open in this pass and are worth naming in case the sitting
has room: **D2's next target repository** (ratify the measured order —
spider-swing first — or name another), **the final EAP mail's shape** (you
called one page; what is assembled is about three, and one page IS reachable
by restructuring), and **the bot's BTD6 history pile** (97 % of the bot's
database; should the collection loop keep running, and may the history be
pruned). Everything else: [`../owner-queue.md`](../owner-queue.md).

## 4 · NOT open — what the round already answered

Do not re-open these in the sitting; each is settled in the committed record,
and three of them were queued *for you* by the round before anyone checked.

| the round asked | the answer, and where it already lives |
|---|---|
| **`OQ-KIT-PROMPT-DOCTRINE`** — which rule governs a kit-planted brake | **NARROWED, NOT ANSWERED — and this row said "answered" until review caught it.** Your 2026-08-09 words (`.claude/hooks/README.md:483-486`) name `delete_trigger` as the one call whose prompt stalls a session, which sharpens the question but does not settle whether a *send* or *delete* may ask first. An earlier cut folded the residue into § 2 · B; B is a different subject (waiting for review, not interrupting you), so the fork is restored as its own agenda row, **§ 2 · B2**. |
| **`OQ-EAP-SPEND-WINDOW-MOOT`** — a dangling dated obligation? | **Not dangling — it is program law.** kit `docs/program/rulings.md` **PL-005 "Observe-first budgets"** (2026-07-07) carries your full quote and the method: caps *deferred, not adopted*; instrument, then decide from the measured average. The genuine residue is that **no meter ever ran**, which is why § 2 · H exists in its place. |
| ~~**The journal letter**~~ — **RE-OPENED, see § 2 · E2** | An earlier cut closed this on the grounds that roadmap § 5.4 already specified the surface. **Codex review refuted it:** § 5.4 defines a recurring-*trap* lifecycle and never mentions `.session-journal.md` (grep, zero hits, re-run here), so it is one side of the fork rather than its answer — and the dig calls the disposition *"a round question for the owner"* in as many words. Restored to the agenda. |
| **The `control/claims/` disposition** — contested, rule separately | **Closed 2026-08-11** as audit finding **D46** (fm #849). The dig deferred to a ruling that had already been made. |
| **Who corrects the Q-0241 provenance mislabel** | **Agent work, already labelled so** — the truth pass's own § 5 preamble marks every row but the last agent-executable and not owner-gated. |
| **Q-0214's unshipped remainder** | **Answered by session 3** and annotated in place at both claim sites (re-read § 1.4, dig § 4/§ 8). |
| **The ~2026-09-09 trading gate as an owner obligation** | The *"approve now"* text is the **recommendation column of an agent-written checklist**, not your ruling. There is no owner obligation to moot; a session extracts the line to the queue and moves on. |
| **House style vs program law (D-7)** | Misread: D-7 is *hardcoded vs configurable*, not *enforced vs optional*. Its verbatim fork is in the kit's founding plan. |

## 5 · What a session should just decide — no letter needed

Recorded here so the sitting does not spend attention on them, and so the next
session knows it is authorised to act. Each is agent-derivable from the
committed record.

- **The AGENTS.md mechanism** (kit-plants vs hand-write ×19) — decide, record
  it as a decision, amend the packet row. Only the *content* question (§ 2 · E)
  is yours.
- **The consumption loop for gap #7** — build and measure it; it adds no
  restriction, so it needs no GO. First re-measure whether the defect has even
  recurred since the routes hardened on 2026-08-24; an unused gate is the
  failure mode you delete.
- **The § 10 disposition table** — execute it: extract the dated gate line to
  the queue, move the five superseded EAP records to an archive path with the
  stated reason. Nothing is deleted.
- **The truth pass's § 5 sweep** — the 23-file wrong-action set: era banners,
  conveyor frontmatter flips, the standing-walls corrections, the roster's five
  missing adopters. Records-only, one session.
- **The report-only economy census** (§ 2 · G's prerequisite) — declare classes,
  report, delete nothing.
- **The Q-0241 provenance correction** — fix the attribution at its source slot
  and re-render the two derived copies.
- **Pin PL-002's scope sentence** — a *different* item from the mislabel above,
  and it was mapped to this section before it actually appeared here (Codex,
  fm #961). The truth pass found the scope clause protected only by the
  register's append-only grammar and two header pins, with no test asserting the
  sentence itself; a session adds that assertion so the rebuild-only scope
  cannot be silently dropped.
- **Reconcile `[D-0011]`'s two budget statements** against the live billing
  surfaces — the entry is titled *capped at its balance* while its own
  amendment says the same key bills the card. Prerequisite to § 2 · H, and
  agent work.
- **What becomes NOW after the sitting** — *not his to pick, and an earlier cut
  wrongly put it to him* (caught on review). The program's own ledger rule is
  explicit: *"only ONE step is NOW at a time — the owner (**or the session, if
  he hasn't said**) picks the next NOW from the top of any track."* So a
  session selects it from the sitting's outcomes and flags the choice; it asks
  him only if he overrides. The four candidate queues (the program's D2, the
  kit build rows, this agenda's outcomes, the held packets) are inputs to that
  choice, not a fork for him.

## 6 · Raised but not adversarially verified

Named rather than dropped, because the verify pass was capped at 26 of 66
deduplicated candidates. These are round-relevant, plausible, and unchecked —
treat them as candidates for a later pass, not as findings:

whether the **NOW pointer** moves off D2 now that the round has output · what
counts as *"further along"* for OD-13's methods-before-product gate · whether
this round is the roadmap's Phase 3 or a track beside it · whether the
**provenance mandate** gets a session · whether the **intent map** graduates
into the kit · whether new red-gate conditions need your ratification · the
**session-hygiene prototype**'s start and whether its closer blocks or warns ·
how the **cross-session chain** gets enforced · **PKT-B3** and the hub-side
wiring.

## 7 · Method, coverage, and what this pass cannot claim

- **Harvest:** 7 lanes, whole-document reads, over the three audits, the
  owner-queue (all ~1,900 lines), both owner-direction records, the round
  thread, the v1.21.0 worklist, the program, current-state and the roadmap.
  68 candidates.
- **Dedup:** mechanical, keyed on slug-or-title — **it under-merges**. AGENTS.md
  surfaced in five lanes under four titles and deduped to four rows, not one.
  66 groups resulted; the semantic merge is the one done by hand in § 2.
- **Verify:** 26 adversarial verifiers, each told to refute. As returned:
  **13 open, 13 closed.** The narrowings are the pass's real product — nearly
  every survivor lost an agent-derivable half the harvest had wrongly routed to
  the owner.
- **After Codex review overturned three of those closures**, the standing split
  is **16 open / 10 closed at candidate level**, and the ten map exhaustively:
  **7** are § 4's answered rows · **1** is *"pinning PL-002's scope sentence"*,
  closed as not-a-question and now actually present in § 5 as agent work
  (it was mapped here before it existed — Codex caught that too) · **2** are
  estate-queue product items outside this round (`pokemon-mod-lab`'s v1.21.0
  hop, the review-bot's scope), which stay in the queue.
- **The three overturned closures**, each restored because the record said so
  rather than because a reviewer insisted: the confirmation doctrine and its
  second-lane duplicate → one row, § 2 · B2 · the journal disposition → § 2 · E2.
  A fourth verdict was corrected without changing the count: the AGENTS.md
  mechanism stayed open but was re-classified agent-derivable, and the owner's
  own direction record reserves it for this sitting, so § 2 · E asks it.
- **One closed-as-partial candidate is named rather than dropped:** whether
  superbot:Q-0132's untrusted-input trust criterion still binds the provider
  mix. It is round-adjacent and belongs with § 2b's OD-13 provider-mix row.
- **Completeness pass:** a critic re-read the surfaces the harvest lanes did
  not own, asking what the audits never turned into a question. It returned
  nine; the five strongest are § 2 · 0 and § 2b, each **verified at source by
  this session before being written here** (the OD-24 § 5 quote at line 185;
  OD-13's two-prerequisite sentence; `initiative` returning zero hits across
  the kit's README, closeout and register; the kit README's own
  placeholder-name line). The other four overlapped rows already present.
- **Not claimed:** that the 40 unverified candidates hold nothing. § 6 names the
  round-relevant ones; the rest were estate-queue product letters (which belong
  to the queue) or semantic duplicates of verified rows.
- **Counts re-derived at this branch head**, not carried from the audits: kit
  `.sessions/` **343** cards, fleet-manager **431** — both including the cards
  the round's own sessions added, which is why the truth pass's `342` (at kit
  `a9acc41`) and this file's `343` (at kit `7f58f0e`) are both correct.
