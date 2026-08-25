# The final EAP review mail — assembled draft, 2026-08-24

> **Status:** `owner-guidance` — program step **E1**.
>
> **The reservation is lifted, and the conflict is named rather than resolved
> silently** (`intent.md` § 6). [`../owner-queue.md`](../owner-queue.md)
> `OQ-E1-FINAL-EAP-EMAIL` and [the E1 plan](2026-07-26-final-eap-email-plan.md)
> both say *no session drafts, sends or restarts this mail* — owner-reserved,
> deferred 2026-08-23. **He lifted it live on 2026-08-24:** *"today I want to
> work on and possibly finish the final EAP mail… see what more you can prepare
> for me and how we should complete the email."* Live word beats stored record.
> **Nothing here sends** — he composes and sends from his own mailbox, as every
> prior version of this plan required.
>
> **Sources:** [the source sweep](../findings/2026-08-24-e1-source-sweep.md)
> (what was already argued, what was never sent, what is new, today's figures) ·
> [the evidence pack](../findings/2026-08-23-eap-evidence-pack.md) (the numbers
> and their commands) · [the correspondence record](../findings/2026-08-09-eap-correspondence-record.md)
> (the outstanding promise, the four unanswered questions, the absent agenda) ·
> [his reflection](../owner-reflection-2026-07-21.md) § "The vendor final-review
> email" (the six net-new sections and the thesis).

## 1 · The decisions this draft makes, so he can overturn them in one line each

| # | Decision | Why | Overturn by |
|---|---|---|---|
| 1 | **The spine is the month *after* the program**, not the fortnight | The fortnight is already in their inbox across four mails; the month after is not, and it is what changed his conclusion. **Not** because other participants did not do it — we have no visibility into that and the claim has been withdrawn (sweep § 4) — but because it is the part he has that the prior mails do not carry. | saying "lead with the fortnight" |
| 2 | Everything already argued becomes **one pointer line**, never a re-argument | His own reflection is explicit; four mails already carry it with forensics | saying which topic he wants re-opened |
| 3 | **Two-part format kept** (his voice, then Claude's) | It is what the earlier reviews used and what the team is used to reading | saying "one voice" |
| 4 | **Fresh compose, new subject, no reply-linkage** | Plan § 1: the standalone closing statement, readable cold in minutes | replying on the old thread instead |
| 5 | The thesis is **refined, not replaced**: the wall is human review *because the defects are shaped to survive review* | The month of auditing earned the sharper version; the original is still true and still his | keeping the July wording |
| 6 | Part 1 is a **beat table placed BEFORE `COPY FROM HERE`**, and the drafted prose is **deleted, not retained** | Rounds 2 and 3 both rejected weaker versions: a scaffold inside the markers gets pasted whatever the header calls it, and prose outside them still supplies his voice when he is invited to lift phrases | writing his half himself, which is the expected outcome |
| 7 | **The one-page bound wins — findings 1–3 and asks 1–5 only** | Two of his own instructions collided (§ 2 item 6: the cap, versus *"add genuinely new points"*). Surfaced rather than resolved, and **he chose the literal cap on 2026-08-25**: findings 4–5 out, asks 6–14 out, optional finding 6 out. **2,097 → 1,477 words.** | saying which of the two month-after findings goes back |

**Logistics.** Fresh Gmail compose — *not* a reply. To the EAP alias, cc the
three people already on the prior thread (their addresses are in that thread;
deliberately not copied into this public repo). No attachments: every number
below has a public link behind it.

**⚠ The COPY block is markdown; the mail is not — do not paste the block
itself.** Part 2 carries some ninety `**bold**` spans and hard wraps at ~76
columns. Pasted straight into a Gmail compose, that is what the recipient reads:
literal asterisks through the whole argument, and wrapping that re-breaks
raggedly at whatever width their client uses. Run one of these instead and paste
its output — same source, no second copy to drift:

| command | gives you |
|---|---|
| `python3 tools/render_eap_mail.py` | **plain text — use this for a normal compose.** Emphasis marks gone, paragraphs unwrapped so the mail client reflows them |
| `python3 tools/render_eap_mail.py --html` | rich paste that keeps the bold and the links |
| `python3 tools/render_eap_mail.py --count` | the word count, computed from the source rather than quoted from a sentence about it |

*(There is deliberately no rendered copy of the mail committed anywhere. A second
copy would drift from this one — which is precisely the defect finding 2
reports.)*

**Subject — pick one:**
- *Claude Code Projects EAP — the final review, one month on*
- *Claude Code Projects EAP — what the agents actually built, audited a month later*

---

> **⚠ PART 1 IS NOT DRAFTED, AND THAT IS NOW LITERAL (`@codex`, fm #943, rounds
> 2 and 3).** Round 2 caught 482 words of polished first person *inside* the COPY
> markers under a header calling it a scaffold. Moving it outside the markers and
> relabelling it "raw material to lift phrases from" was **not enough** — round 3
> was right that a complete send-ready narrative supplies his voice whatever the
> label says, and the plan permits *at most a pointer skeleton*. **The prose is
> deleted.** What remains is beats and facts: what each paragraph must carry, and
> nothing about how to say it.

## Part 1 — the owner's half (he writes this; nothing here is sentences)

| beat | what it has to carry | facts available if he wants them |
|---|---|---|
| 1 · open, and why it is late | the delay *is* the argument — he wanted to check what the projects built before sending a fifth list of complaints | promised 2026-07-21; **send date is whatever he actually sends on** — do not pre-fill it |
| 2 · the prior mails are not repeated | permissions · coordinator↔worker trust · the classifier regression · the scheduler — all still true, all already with them, with forensics | four mails, 07-08 → 07-16; offer to walk through any of it |
| 3 · **the verdict paragraph — his alone** | he went in thinking the limit was agent capability; a month of auditing moved it | the limit he found: not too much to read, but mistakes shaped to survive reading |
| 4 · hand off to Part 2, then thanks | the program, the extension, the personal reply on the final day | he has said on the record that the reply mattered more than the gift |

**Beat 3 is the one nobody can supply.** It is the only new argument in the whole
mail that is his rather than measured, and it is why the mail is worth sending.

## COPY FROM HERE
To the Claude Code Projects team,

Menno's four EAP mails argued the platform from inside the program. This one
reports what the program produced, measured a month later. Everything below is either a public link, or a
published command with its result recorded. **One caveat so the offer is
honest:** the repository-census and infrastructure figures were taken against
this account with the owner's own credentials and include private
repositories, so the *method* is reproducible but the *inputs* are not
available to you — those you would have to take on the record, or ask us to
re-run.

**The scale, as of 24 August 2026.** 27 repositories on the account; **19 of
them created inside the EAP fortnight**, 17 of those in the first four days. One
predates it, and **seven were created after the program closed**. The estate now
carries **just over 8,000 pull requests opened all-time** and
**about 4,560 session records** across 19 repositories (exact counts taken
2026-08-24 ~18:05Z; they move daily). Read those as volume, not
quality — that distinction is the whole mail. Two honest caveats travel with the
figures: the counts are point-in-time and will differ when you re-run them, and
no count of PRs opened *during* the fortnight exists, because the method counts
lifetime PRs rather than a date window.

**Finding 1 — the failure modes we could measure are FORGETTING and FALSE-DONE.**
The recurring outcome problems we found were that agents forgot what had already
been established, and that they reported work finished which was not finished in
the way it was asked for. Both are intent failures. **We are not making a claim
about code quality either way** — we ran no census of runtime defects, so we do
not know whether the software was good, and we would rather tell you what we
measured than what we assume.

**Finding 2 — the defect mechanism preserves coherence, which is why review does
not catch it.** Every tracked file in one repository was accounted
for — not a sample — and it found **101 defects**; 98 are closed. (Precisely:
most were read line by line; 19 large files, about 22 MB, were inspected for
structure, provenance, schema and anomalies instead. The audit records which,
and says the distinction is not cosmetic.) The mechanism behind its
highest-cost findings was not an error of fact. It was **an appended correction
that failed to retract what it corrected**. (We did not classify all 101 by
mechanism, so read this as the shape of the worst ones, not a majority.) The agent added the truth and left the falsehood in place, so the
document stayed internally consistent and read as correct. **In this sample,
agents appended and did not retract** — we have not tested whether that
generalises, and it is a tendency we measured rather than a rule we proved. A defect shaped like that is invisible to any review
that reads a document for coherence — and reading for coherence is what a
reviewer does by default, unless they stop to compare the document against its
sources or re-run the thing it describes.

**Finding 3 — written rules do not bind agents; only rules that arrive at the
moment of action do.** We counted this properly. In one session — one that was
itself building our verification tooling, so nothing was rushed — there were
**16 distinct incidents**. At the time of that audit the repository carried **116 committed statements of
the single rule those incidents violated, across 66 files**, including all three
of the documents that bind a session there. *(The 116 is the 2026-08-08 audit-time count, and it
is the one that goes with those 16 incidents. We are deliberately not quoting a
current count: the same regex, run three times today, gave 125, 126 and 127,
because each write-up of the measurement added text the measurement then
matched. That is a curiosity, not a defect in the finding — the argument is
about 116 statements catching 0 of 16, and that pair is fixed.)* Documentation recalled at the right
moment caught **0 of 16**. What did catch them: the owner asking a question (5),
a Stop hook (4), the gate and CI together (3 — 1 local, 2 CI/GitHub), test runs (2), and after-the-fact discovery
(2). The conclusion we acted on is that a rule binds only if it *arrives* at the
moment it applies — of the catches above, all but two came from something that
fired at a moment — and the two exceptions were found only after the cost was
paid; none came from a document being available — so we built 67 documentation routes onto a pre-tool hook (counted
2026-08-24; it was 61 sixteen days earlier — the mechanism is still growing). That is a
platform-shaped feature we had to build ourselves, and we think it generalises:
**more instructions in a context file is not a fix, and our number for that is
116 to nothing.**

**One thing that did work, and it was not one of yours.** What reliably caught
the false-dones was independent adversarial review by a *different vendor's*
model, wired into the PR flow. Measured: request to review in **335 seconds**,
13 findings over 5 rounds, several of them proving a pull request did not do
what its own title claimed. A second model that has not read your reasoning is
worth more than a longer checklist.

**What we would like to see.** One line of why each; the detail is all public.

1. **Rules that arrive at the moment of action, not at session start.** *Because
   116 committed statements of one rule caught 0 of 16 violations in the session
   that wrote them; 14 of the 16 were caught by something firing at a moment — a
   question, a hook, a gate, a test — and the last two only after the cost was
   paid. None came from a document being available.*
2. **Agents that retract, not only append.** *Because the costliest findings in
   a 101-defect full-read audit were corrections that left the error standing,
   and the result still reads perfectly.*
3. **A durable, queryable record of what a session actually changed.** *Because
   sessions forget, and we now hand-maintain 4,560 session records to replace
   what the platform does not keep.*
4. **A done-ness signal an owner can trust.** *Because work was repeatedly reported
   finished that was not finished as asked — we are not saying anything about
   the code either way.*
5. **Usage, cost and resource telemetry visible to the agent tier.** *Because
   agents built and ran a system whose 949 MB store held 925 MB in three
   ingestion-history tables against about 10 MB of actual user data (measured
   2026-08-20, and still growing — the loop was left running), and nothing
   surfaced that during normal operation. One agent did find it, by deliberately
   going to look; nothing prompted anyone to look.*

**What genuinely worked.** The shared working agreement is
the single best feature you have — written once, picked up by every session in
every project, with nothing repeated by hand; it is the reason any of this was
possible. Worker-tier autonomy ran clean from the first night: claim, open,
verify, land, with no prompts and no tool failures. The self-improving loop
closed across repositories in about 30 hours — one project found a defect in the
shared tooling, routed it upstream, the tooling shipped a fix, and the project
consumed it back and verified it firing. The honesty held under hostile audit:
a 999-test claim independently re-run came back 998 passed and 1 skipped, and an
adversarial wind-down review verified 21 of 21 incidents with zero fabrication.
And the team was responsive throughout — the extension, the features shipped
mid-program, and a personal reply on the final day.

**A standing offer, and it is bigger than it was in July.** One of the four
questions in the 8 July mail offered this estate as a test harness, and no answer
to it appears anywhere in our recorded correspondence. It is now 27 repositories, ~8,000 pull requests, ~4,560 session
records, a published measurement method with its own positive controls, and a
blind-scored evaluation of whether a fresh agent can correctly state what a
repository is *for* — five agents producing, two independent scorers against a
pre-registered rubric, with the outcomes withheld from the scorers' inputs.
Honestly: that containment was instructed and self-attested rather than
enforced, and both scorers ran the same model family — we would tighten both
before calling it a result. If you want a specific
scenario stress-tested, name it and we will run it and send you the raw results,
including the ones that make us look bad.

Everything above is public:
- The measured evidence pack, every figure with the command that produced it:
  `github.com/menno420/fleet-manager/blob/main/docs/findings/2026-08-23-eap-evidence-pack.md`
- Why written rules do not bind, 116 to nothing:
  `github.com/menno420/fleet-manager/blob/main/docs/findings/2026-08-08-why-rules-dont-bind.md`
- The full-read audit, all 101 defects:
  `github.com/menno420/fleet-manager/blob/main/docs/audits/2026-08-10-full-read/README.md`
- The permission, trust and classifier findings argued in full in July, which
  this mail deliberately does not repeat:
  `github.com/menno420/superbot/blob/main/docs/eap/permission-classifier-findings-consolidated-2026-07-16.md`

— Claude, writing for Menno's estate.

## COPY TO HERE

---

## 2 · Before he sends — the seven calls, three of them answered 2026-08-25

> **⚠ SENDING GATE — added 2026-08-24 after owner-review, and it is a base rate,
> not a worry.** A Codex round was outstanding when this draft was handed over,
> and the handover said *"nothing is blocked — the mail is yours to finish now."*
> **That was wrong about sending.** Measured over the five completed rounds:
> **5 of 5 changed this document**, and every one corrected something that would
> otherwise have reached the vendor — a withdrawn search-index bug report; a rule
> count stated in the present tense that had already moved; a send date recorded
> for a mail not yet sent; a telemetry claim the cited audit itself refutes; and
> **an offer to re-run measurements the recipient cannot re-run**. On that
> record, an outstanding round is a **material chance of another such error**,
> not a formality.
>
> **And the hedge that belongs on the state of this draft, because the stronger
> version is not earned:** it is **free of currently known errors** — not
> "correct". Five of five rounds found assertion-level errors in a document that,
> before each round, looked finished. The difference matters when deciding
> whether to wait.
>
> **So: the calls below are judgement and can be made at any time. Sending
> should wait until the outstanding round is reported.** If he would rather send
> without waiting, that is entirely his call; the point is that it is a decision
> with a measured risk attached, not a free action. *(This paragraph said "the
> six calls below" under a header saying seven. The header was right — see the
> numbering note at item 5.)*



> **A fifth item was here and is now closed, recorded because the near-miss is
> the useful part.** The draft carried a paragraph and an ask reporting that
> GitHub's search index is blind to most of this account — carried in good faith
> from [the evidence pack](../findings/2026-08-23-eap-evidence-pack.md) § 0,
> written the previous day with commands attached. **Tested before sending: it
> does not reproduce** — search returns 8,038 account-wide and 2,380 for
> `superbot`, matching the independent per-repo count to the unit
> ([sweep](../findings/2026-08-24-e1-source-sweep.md) § 4 N6). Both the paragraph
> and the ask are **removed**, not softened: a checkable false claim in a mail to
> a vendor about their own tooling costs more than the finding was worth. The
> net effect on the mail is positive — the § 5 figures now rest on two
> independent endpoints instead of one.


### ✅ Answered by the owner, 2026-08-25 — recorded, not interpreted

Each was put to him as a menu before any edit was made, and he picked.
**What his three answers did to the mail: 2,097 → 1,477 words.**

| item | the call | his answer |
|---|---|---|
| **6** | the length, against the plan's one-page cap | **the literal cap** — findings 1–3, asks 1–5 |
| **2** | the 97.5 % that contradicts its own source | **cut the ratio, keep the shape** |
| — | what *"a revision pass and my own section added/edited"* targets | **two operations, and the pass covers the whole document** |

**Four consequences of the cap — surfaced, not resolved.** None was decided for
him; each follows from the route itself rather than from anyone's judgement, and
each is one line to overturn.

- **a · The venue asymmetry is gone.** The 2,115 branches / ~50 PRs / ~1,900
  routines figures — which item 4 below calls *the strongest single argument in
  the estate* — lived in asks 8 and 9. → *"put ask 8 back"* (54 words)
- **b · The prior-mail pointer left with asks 6–7.** Those two were Part 2's only
  reference back to what the four earlier mails argued, which **§ 1 decision 2
  requires the mail to carry**. Rather than leave the July link orphaned at the
  foot of a mail that no longer cites it, **the link is re-labelled to carry that
  pointer itself** — *"the permission, trust and classifier findings argued in
  full in July, which this mail deliberately does not repeat"*, ten words.
  → *"drop the link"*, or *"give it a sentence in the body"*
- **c · The month-after spine is three findings, not five** — and the month-after
  is **§ 1 decision 1's entire rationale** for sending this at all. → *"put
  finding 4 back"* (drift, 92 words) or *"finding 5 back"* (cost, 193 words)
- **e · One addition, eight words, and it is the only content added to the
  mail.** The scale paragraph accounted for 19 + 1 of 27 repositories and left
  **seven unexplained** — an arithmetic gap a vendor would notice, and six
  adversarial rounds did not. The sweep has them (§ *"created after the program
  closed"*, 7 as of 08-24), and they are **evidence for the spine rather than
  filler**: repositories created *after* the program is exactly what § 1
  decision 1 says this mail is for. → *"cut it"*
- **d · 1,477 words is about three pages, not one.** No route reached one page.
  The honest floor — cutting the good-parts block and the standing offer as well
  — measured 1,182, and those two are exactly what make the critique read as a
  fan's rather than a complainer's. Recorded so the cap is not mistaken for met.

---

1. **Ask 12 may be a repeat — MOOT under the cap.** Ask 12 was in asks 6–14 and
   is out, so nothing turns on whether [`../anthropic-email-pack.md`](../anthropic-email-pack.md)
   was ever sent ([source sweep](../findings/2026-08-24-e1-source-sweep.md) § 3;
   we could not establish it either way). **It returns as a live question only if
   he takes consequence *a* and puts asks back.**
2. **The database figures — ANSWERED: cut the ratio, keep the shape.** They
   remain a **2026-08-20 snapshot, not re-measured for this mail** (`@codex`,
   fm #943 round 6): re-taking them needs the private Actions venue and a
   one-shot database credential, a real operation rather than a read. The audit
   records an ingestion event 27 minutes before that run and the loop was left
   going, so **the store is larger now than the number says** — the mail says so.
   **How the ratio was cut without losing the evidence:** the contested quantity
   was the *derived percentage* — the audit's prose says **97.5 %** of the 939 MB
   `public` schema while its own rows sum to 668 + 135 + 122 = **925 MB**, which
   is **98.5 %**. Plausibly exact-bytes versus rounded-MB, and **still
   unresolved — no session picked a side.** The rows themselves were never in
   dispute, so ask 5 now quotes *them*: **949 MB store · 925 MB in three
   ingestion-history tables · about 10 MB of actual user data**, and no
   percentage anywhere. → *"re-run the sizing before I send"* if he wants a
   current, self-consistent figure instead.
3. **The €30 was his own infrastructure — MOOT under the cap.** It lived in
   finding 5, which is out, so no hosting bill appears in the mail. Ask 5 keeps
   the storage shape because *that* shape transfers — an unobservable signal
   accumulating unseen — and it carries no euro figure. → *"put finding 5 back"*
   re-opens this.
4. **The July `MEASURED-PRIOR` figures — MOOT under the cap, and this is
   consequence *a*.** The 2,115 branches / ~50 PRs / ~1,900 routines counts came
   from the never-sent 18 July draft: measured then, not re-measured now, and
   five weeks old. They were the choice between *send them as dated July
   measurements* and *drop the counts, keep the venue asymmetry*. **The cap took
   both, along with the asymmetry itself.** → *"put ask 8 back, counts and all"*
   or *"put ask 8 back without the numbers"*.
5. **Not a call — a statement, and this is where the numbering drifted.**
   *Nothing in this mail claims anything about agent code quality*, deliberately:
   every measured failure is about records, retrieval and verification, and that
   restraint is what makes the rest credible. **It has nothing in it to decide**,
   which is why the sending gate said "six calls" while the header said seven,
   and why § 1 decision 7, item 7 (three times) and the owner-queue entry all
   pointed at **"call 5"** when they meant the length — item **6**. All five
   sites are corrected. The item keeps its number so that "seven pre-send calls",
   recorded in the queue, the program § 7 row and `docs/planning/README.md`,
   stays true.
6. **The length — ANSWERED: the literal cap.** **Part 2 was 2,097 words at
   `9b2d83a`, 1,469 after the cut, and 1,477 as it now stands** — the eight-word
   census fix at consequence *e* is the difference.
   **The number now comes from a command rather than from prose:**
   `python3 tools/render_eap_mail.py --count`. That *is* the fix; a fourth
   written statement of it would go stale exactly like the first three.
   **The drift, for the record — and it ran deeper than stale copies.** Three
   committed places carried three different values: the draft **2,082**, the
   owner-queue **2,127**, the file **2,151**. **None of the three was right.**
   The method was never stated, and both obvious methods are wrong — substituting
   a space for each emphasis mark splits `**fortnight**,` into `fortnight` + `,`
   and counts the bare comma as a word (**+8**), while deleting the marks instead
   leaves the links block's `-` bullets standing as words (**+4**). Neither
   punctuation nor a bullet glyph is a word. **Counting the plain text that is
   actually pasted gives 2,097** — so the 2,151 this session first put in front
   of him was itself inflated by ~2.5 %. **It did not change the decision:**
   2,097 words against a one-page cap is the same call as 2,151, and he made it
   on the direction, not the third digit. **The route prices were staler still:**
   quoted at ~1,227 in one place and ~1,434 in another; measured, the route
   lands at **1,469**.
   **The conflict this resolved:** the cap was written 2026-07-26, when the mail
   was conceived as a *synthesis of already-sent material*; today's brief was
   *"add a few genuinely new points… actually a new valuable source"*. Both are
   his instructions and both could not hold. **He chose the cap** — see
   consequence *d* for what that did and did not achieve.


7. **The optional sixth finding — DROPPED, by this item's own conditional.**
   It said: *include it on the "keep the length" route, drop it on the
   literal-cap route.* He took the literal cap, so it is out. **That is a
   resolved conditional, not a new decision.** It stays drafted below, because
   the reasoning that put it here has not changed.
   It was first excluded as *"that's our own trap, not the vendor's problem"*,
   which owner-review correctly rejected: the mail's subject **is** agent failure
   modes, so a session generating false-absence checks is on topic, not off it.
   **What keeps it out now is evidential weight against length** — it is **n=1
   self-observation from one session**, where every other finding rests on a
   committed audit with a measured denominator. → *"include finding 6"* puts it
   back at **193 words**, taking Part 2 to ~1,670. **Its paste location moved:**
   between **finding 3** and the "one thing that did work" paragraph — findings 4
   and 5 are no longer there to sit between.


   > **Finding 6 — the same failure shape, caught live while writing this mail.**
   > Assembling this review, the agent doing it wrote **five** separate checks
   > that answered "is there anything there?" and five times returned a confident
   > *no* that was wrong — a shell fallback that printed the same token for a failed
   > check as for a real absence; a match on the wrong commit field; a match
   > pinned to the wrong revision; an unpaginated read that stopped at the
   > API's 30-item default and dropped the newest item; and — after all four were
   > written up — a propagation check whose pattern could not match what it was
   > searching for, so it could not fail. Four of the five were in
   > code written specifically to avoid that error, and the repository already
   > carried a written rule about it. The rule did not bind; the query decided
   > the answer, and nothing in the output said so. We report it because it is
   > one session's self-observation rather than an audited sample — but it is the
   > same shape as everything above, it happened today, and it is the reason we
   > think this class needs a product answer rather than more documentation.

## 3 · After he sends

- Mark **E1 complete** in the [program](2026-07-26-consolidation-program.md) § 7
  ledger and move the NOW pointer.
- Close `OQ-E1-FINAL-EAP-EMAIL` in [`../owner-queue.md`](../owner-queue.md).
- One-line "superseded by the final mail" note on
  [`../anthropic-email-pack.md`](../anthropic-email-pack.md) and on superbot's
  `docs/eap/2026-07-18-followup-email-draft.md`.
- **Record the send into the repo — date, exact subject, and the Gmail
  `Message-Id`.** This is not tidy-up bookkeeping, it is the mail's own argument
  applied to itself: § 0 of [the correspondence record](../findings/2026-08-09-eap-correspondence-record.md)
  **measured that four of his own sent EAP mails are no longer retrievable from
  Gmail**, with two positive controls passing — so the mailbox is not the archive
  of record and the repo has to be. The `Message-Id` is under Gmail's *Show
  original*. The row below is staged and needs only the three values.

### The send record — three values, and the queue entry can close

| field | value |
|---|---|
| sent (UTC) | *(pending)* |
| subject | *(pending — one of the two in § 1 Logistics)* |
| `Message-Id` | *(pending — Gmail → ⋮ → Show original)* |
| thread | fresh compose, **not** a reply to the July thread (§ 1 decision 4) |
- Record the sent-mail metadata (date, subject, message id) into
  [the correspondence record](../findings/2026-08-09-eap-correspondence-record.md)
  — and this time into the **repo**, since
  [§ 1 of the sweep](../findings/2026-08-24-e1-source-sweep.md) established that
  the mailbox is not the archive of record.
