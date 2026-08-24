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
| 7 | **Part 2 exceeds the plan's one-page bound — surfaced, not resolved** | See § 2 call 5: the bound and "add genuinely new points" cannot both be satisfied, and which one gives is his call | picking either side for him |

**Logistics.** Fresh Gmail compose — *not* a reply. To the EAP alias, cc the
three people already on the prior thread (their addresses are in that thread;
deliberately not copied into this public repo). No attachments: every number
below has a public link behind it.

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
predates it. The estate now carries **just over 8,000 pull requests opened all-time** and
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
document stayed internally consistent and read as correct. **Agents append; they
do not retract.** A defect shaped like that is invisible to any review
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

**Finding 4 — drift lands on the most visible surface and still goes unnoticed
for a month.** Menno's public review site described the program as running,
33 days after it ended: 0 of 7 live pages said it had concluded, and the fleet
page rendered "15 live lanes" with mirrored heartbeats for projects that had
been terminated. This was his most visible public surface. We are not claiming that generalises —
it is one surface, measured once — but if drift lasts a month *there*, we would
not bet on catching it anywhere less visible.

**Finding 5 — cost is not an agent-legible signal, so it accumulates exactly
where nobody looks.** An infrastructure audit attributed a €30 monthly bill,
ended an unnoticed crawler load, and sized the bot's database: it is 949 MB, of
which the `public` schema is 939 MB, and **97.5 % of that 939 MB is accumulated
ingestion history** — about 96.5 % of the whole database against roughly 10 MB of real user
data. That is a storage-composition measurement, not a verdict that the history
is disposable — whether to keep it is still an open call on our side. Agents built and ran the system that
accumulated it. **The precise gap is not that no agent could see this — one
did, by deliberately querying the provider's API; it is that nothing surfaced it
during normal operation.** Cost was never a signal that arrived; it had to be
gone looking for, and nothing prompted anyone to look. (Sizes measured
2026-08-20 and still growing — the ingestion loop was left running; index and
database overhead are in the total too.)
The euro figure is not the point; the shape is — an unobservable signal
accumulates in the same way quality drift does.

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
   agents built and ran a system whose 949 MB store was ~96.5 % accumulated
   ingestion history (97.5 % of its 939 MB `public` schema; measured 2026-08-20), and nothing surfaced that during
   normal operation — an agent could only find it by going to look.*
6. **Owner-set permission grants, scoped per repo, branch and action, able to
   restrict as well as allow.** *Because this is the ask from every previous
   mail and it is still the structural fix; pointer only.*
7. **Same-account provenance for coordinator-to-worker instructions.** *Because
   a verified owner's own coordinator relaying to his own worker is not the
   cross-session injection the change was built to stop; argued in full on
   16 July.*
8. **A permission model scoped to risk, not to venue.** *Because the identical
   actions on the identical account were denied inside a Project and completely
   unrestricted in an ordinary chat outside it — one outside session landed
   ~50 PRs the Projects had finished but could not merge, and cleaned 2,115
   stale branches, with zero denials.*
9. **An owner-level off-switch for the routine and trigger approval prompt.**
    *Because no setting suppresses it — we verified with bypass permissions, an
    explicit allow-list and the server wildcard all set — and ~1,900 orphaned
    routines could only be cleared by hand, one approval at a time.*
10. **Do not let a stale stored artifact outrank a live instruction.** *Because a
    session held a dated stand-down note above its owner's live message and
    refused the live message.*
11. **Do not classify factual capability documentation as workaround material.**
    *Because a session that misreads a denial as a permanent wall writes that
    wall into shared memory, where it becomes every later session's starting
    fact — we had to purge 18 repositories and ship a CI check that reds a pull
    request asserting an undated, standing "agents cannot X" for the actions it
    covers.*
12. **A session that can accurately answer "what can I do?"** *Because
    tool-search-only tools are invisible to a session's own inspection, so agents
    declare false limits about tools they actually hold.*
13. **A cross-project overview with actions on it.** *Because "Blocked on you"
    exists inside a project but not one level up, so there is no single place to
    see which projects are waiting, stuck, or erroring — or to act on them.*
14. **Surface auto-mode and consent changes where Projects users will see them.**
    *Because both changes that broke the fleet were logged only in the CLI
    changelog, and one visible line would have saved a full day of bisecting.*

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
- The consolidated permission-classifier findings from July:
  `github.com/menno420/superbot/blob/main/docs/eap/permission-classifier-findings-consolidated-2026-07-16.md`

— Claude, writing for Menno's estate.

## COPY TO HERE

---

## 2 · Before he sends — seven calls, all his

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
> **So: the six calls below can be made at any time — they are judgement, not
> facts. Sending should wait until the outstanding round is reported.** If he
> would rather send without waiting, that is entirely his call; the point is
> that it is a decision with a measured risk attached, not a free action.



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


1. **Ask 12 may be a repeat.** [`../anthropic-email-pack.md`](../anthropic-email-pack.md)
   was written as a ready-to-send block on exactly this topic and **we cannot
   establish whether it was ever sent** ([source sweep](../findings/2026-08-24-e1-source-sweep.md)
   § 3). At worst it repeats an unanswered ask. Cut it if he remembers sending it.
2. **The database figures are a 2026-08-20 snapshot and were NOT re-measured for
   this mail** (`@codex`, fm #943 round 6). They come from the audit's sizing run;
   re-taking them needs the private Actions venue and a one-shot database
   credential, which is a real operation rather than a read, so it was not done.
   The audit records an ingestion event 27 minutes before that run and the loop
   was left going, so **the store is larger now than the number says**. Both
   mentions carry the date. If he wants a current figure, say so and it can be
   re-run before sending.
3. **The €30 and the 97.5 % are his own infrastructure**, not the vendor's. Kept
   because the *shape* transfers — an unobservable signal accumulating unseen.
   Cut it if he would rather not put his hosting bill in a vendor mail.
4. **The 2,115 branches / ~50 PRs / ~1,900 routines figures in asks 8 and 9**
   come from the never-sent 18 July draft and are `MEASURED-PRIOR` — measured
   then, not re-measured now. They are the strongest single argument in the
   estate and they are five weeks old. Either send them as dated July
   measurements, or drop the counts and keep the venue asymmetry, which needs no
   number.
5. **Nothing in this mail claims anything about agent code quality**, deliberately
   — every measured failure is about records, retrieval and verification. That
   restraint is what makes the rest credible.

6. **Part 2 is **2,082 words** (measured on the current COPY block; it has grown
   with every review round — 1,704 → 1,827 → 1,851 → 2,082, because each
   correction adds a qualifying clause. **Re-count before acting on this; do not
   quote it.**); the plan's § 5 caps it at one page — and both
   halves of that conflict are his own instruction** (`@codex`, fm #943 round 2,
   correctly refusing to let the bound be treated as optional). **The conflict,
   stated rather than resolved:** the cap was written 2026-07-26, when this mail
   was conceived as a *synthesis of already-sent material*; today's brief is
   *"add a few genuinely new points… actually a new valuable source"*. Seven
   month-after findings and fourteen asks do not fit on one page, so one of the
   two instructions has to give and **that is not a session's call to make.**
   **My recommendation, if he wants one:** keep the length, cut nothing from the
   findings, and instead cut **asks 6–14** to a single line pointing at the
   public list. That takes Part 2 to roughly one page of *argument* with the
   catalogue moved off-mail, which satisfies the intent behind the cap
   (readable cold, in minutes) rather than its word count. **Alternative if he
   wants the cap honoured literally:** keep findings 1–3, drop 4 and 5, keep
   asks 1–5, and the mail lands at **~1,434 words** (measured on the current block; earlier
versions of this line said "near 700" and then "~1,227" — both were right when
written and both went stale, which is the same drift as the figure above: the good-parts
block, the standing offer, the links and the framing all survive that cut). **To
get genuinely near one page he would also have to drop the good-parts block and
the standing offer**, and both of those are the reasons the critique reads as a
fan's rather than a complainer's.

7. **An optional sixth finding is drafted below and NOT in the copy block —
   his call whether to spend the words.** It was first excluded on the reasoning
   *"that's our own trap, not the vendor's problem"*, which owner-review
   correctly rejected: the mail's subject **is** agent failure modes, so a
   session generating false-absence checks is on topic, not off it. **The real
   trade-off is evidential weight against length:** it is **n=1 self-observation
   from one session**, where every other finding in the mail rests on a committed
   audit with a measured denominator — and Part 2 is already over the cap
   (call 5). **Recommendation: include it if he takes the "keep the length"
   route in call 5; drop it if he takes the literal-cap route (~1,227 words
   before the further cuts call 5 names).** Drafted, ready to paste
   between findings 5 and the "one thing that did work" paragraph:

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
- Record the sent-mail metadata (date, subject, message id) into
  [the correspondence record](../findings/2026-08-09-eap-correspondence-record.md)
  — and this time into the **repo**, since
  [§ 1 of the sweep](../findings/2026-08-24-e1-source-sweep.md) established that
  the mailbox is not the archive of record.
