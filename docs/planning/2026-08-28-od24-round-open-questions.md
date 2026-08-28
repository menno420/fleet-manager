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
committed record, and one is answered by your own later words.** The round is
an audit of unrouted knowledge; its own output turned out to carry the same
defect. Read § 4 before the sitting — it is what keeps the conversation short.

The sharpest instance: session 2 queued `OQ-KIT-PROMPT-DOCTRINE` asking which
of your rules governs a kit-planted brake, citing superbot:Q-0128 from
**2026-06-13**. But `.claude/hooks/README.md:483-486` carries a **later** you,
verbatim, from **2026-08-09**:

> *"Delete triggers are the only thing that gives me an approval prompt in
> automode, this will stall your session untill I get back. Always prevent
> using them."*

That is the same subject two months on, and it is narrower than the June line:
you named the one call that actually raises a prompt and asked for it to be
prevented — not for all confirmation to be abolished. The letter as queued is
therefore mostly answered; what survives of it is folded into § 2 · B.

## 1 · How to use this in the sitting

- **§ 2 is the agenda.** Eight questions, ordered by dependency, not by size.
  Each carries: the ask in plain language · the options · what it unblocks ·
  what the minimum answer is.
- **Read § 4 first if the sitting is short.** It removes five things you might
  otherwise be asked.
- **§ 5 is not for you.** It is what a session should simply decide, recorded
  here so the sitting does not spend your attention on it. Your own rule
  governs: *"unnecessary asks are the waste, but a question that prevents a
  misread goal is a good trade"* ([`../intent.md`](../intent.md) § 3).
- **Silence is not consent in this file.** Every row is here precisely because
  no session may derive it.

## 2 · The agenda — eight questions, in dependency order

### A · Do your June rules still stand by default, or are they history?

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

### C · Move 1 — GO or hold, and how far does the GO reach?

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

**The ask.** You already decided every repo gets a small *start here* note for
non-Claude agents, and that public is fine. **We are not asking how they get
made** — your own past ruling (generating stubs that then rot is worse than
the gap) plus the measurement that the kit's planted journals stayed
byte-identical in 11 of 14 repos settles the mechanism, and § 5 records what a
session will decide. What we cannot derive is **content**: should each file be
pointers only (read path, hub back-link, where the records are), or pointers
**plus a few lines of yours** about what that repo is actually for?

**Options.** (a) Pointers only. · (b) Pointers plus your own purpose lines —
and then: do you dictate them, or do we draft from each repo's docs for you to
correct?

**Minimum answer:** one sentence. If (b), the follow-on in the same breath.

**Note:** execution of the nineteen still sits behind the packet hold (C's
sibling); this decides what they say when they are written.

**Evidence:** `OQ-FM-AGENTS-BOOT` (answered yes, estate-wide) · OD-23 § 6 ·
OD-24 § 7 (plant-vs-hand-write parked *for this round*).

### F · Who works the leftovers pile — you, or a schedule?

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

**The ask.** Every session leaves a written note. There are now **343** in the
toolbox repo and **431** here, and nothing has ever tidied them — even though
the kit *ships* a tidy-up that deletes an old note and leaves a one-line
receipt behind, with the full text still recoverable from history. You picked
that posture yourself in July (superbot:Q-0214, *"delete with tombstones"*);
it shipped in v1.0.0 and has never once been switched on, on any corpus.

**The order matters.** A session will first run the **report-only** census —
declare what would be pruned, delete nothing — because that needs no
permission and turns this from a preference into a number. Your answer is only
needed **after** that: with the real numbers in front of you, may cards
actually be deleted with a tombstone, or do we keep everything forever?

**Minimum answer:** nothing today. One sentence once the census lands.

**Evidence:** [the truth pass](../findings/2026-08-28-kit-tree-truth-pass.md)
§ 3 + § 5's carved-out last row.

### H · Spend caps — the ten-second one

**The ask.** In early July you said the AI bills were not really a problem and
you would rather watch a couple of months and decide from the average. That
window lands about now — but **no meter ever ran** (the telemetry feed carried
no cost and stopped 2026-07-13), so there is no average to look at. The
question is just: leave it uncapped, or set a cap?

**Minimum answer:** one word — *no cap*, or *cap it* plus a rough number.

**Prior, so you can answer in a breath:** your own recorded position is
*"budget so far is not really a problem"* and *"we spend way too much time on
safety … this is just a hobby project"*. The one thing that changed since: the
paid key now bills your card directly, which was not true in July.

**Evidence:** kit `docs/program/rulings.md` **PL-005** (Q-0249 is already
program law, not a dangling obligation — see § 4) · `[D-0011]`.

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
| **`OQ-KIT-PROMPT-DOCTRINE`** — which rule governs a kit-planted brake | **Largely answered by your own later words.** `.claude/hooks/README.md:483-486`, owner-live **2026-08-09**: *"Delete triggers are the only thing that gives me an approval prompt in automode … Always prevent using them."* Two months after the June line the round cited, and narrower: you named the one call that raises a prompt. What survives is folded into § 2 · B; **the queue entry is narrowed accordingly, not left as posed.** |
| **`OQ-EAP-SPEND-WINDOW-MOOT`** — a dangling dated obligation? | **Not dangling — it is program law.** kit `docs/program/rulings.md` **PL-005 "Observe-first budgets"** (2026-07-07) carries your full quote and the method: caps *deferred, not adopted*; instrument, then decide from the measured average. The genuine residue is that **no meter ever ran**, which is why § 2 · H exists in its place. |
| **The journal letter** — does the per-repo journal survive? | **You already specified this surface**, in your own roadmap: `planning/2026-08-08-agent-operating-environment-roadmap.md` § 5.4 *"Known mistakes as executable knowledge"*, marked `OWNER` — and the round never cited it. The letter as posed asks you to re-decide something you decided; what remains is design, not a letter. |
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

## 6 · Raised but not adversarially verified

Named rather than dropped, because the verify pass was capped at 26 of 66
deduplicated candidates. These are round-relevant, plausible, and unchecked —
treat them as candidates for a later pass, not as findings:

whether the **NOW pointer** moves off D2 now that the round has output · what
counts as *"further along"* for OD-13's methods-before-product gate · whether
this round is the roadmap's Phase 3 or a track beside it · whether the
**provenance mandate** gets a session · whether the **intent map** graduates
into the kit · when the next **kit release** is cut and which adopters take it
· whether new red-gate conditions need your ratification · the
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
- **Verify:** 26 adversarial verifiers, each told to refute. **13 survived as
  open** (some narrowed), **13 were closed** as already-answered, not-questions,
  or misreads — the § 4 table is that half. The narrowings are the pass's real
  product: nearly every survivor lost an agent-derivable half that the harvest
  had wrongly routed to the owner.
- **Not claimed:** that the 40 unverified candidates hold nothing. § 6 names the
  round-relevant ones; the rest were estate-queue product letters (which belong
  to the queue) or semantic duplicates of verified rows.
- **Counts re-derived at this branch head**, not carried from the audits: kit
  `.sessions/` **343** cards, fleet-manager **431** — both including the cards
  the round's own sessions added, which is why the truth pass's `342` (at kit
  `a9acc41`) and this file's `343` (at kit `7f58f0e`) are both correct.
