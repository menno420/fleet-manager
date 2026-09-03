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
> **2026-09-03 — drafted in full under Shape A (owner, 2026-09-02, [§ 5b](../findings/2026-09-02-owner-direction.md)):**
> Part 1 is proposed below the beat table for him to rewrite (beat 3 is his
> alone); Part 2 keeps the text he approved plus the two required one-clause
> patches and one addendum framed as the Projects-versus-sessions answer, with
> the three false-done rows as the evidence that verification is the deciding
> line. The whole mail is staged as a Gmail draft in his own account with no
> recipients (id `r-9208017789511753451`, subject as proposed below) — he adds
> the recipients, edits, and sends. Session card:
> [`2026-09-03-final-eap-mail-draft.md`](../../.sessions/2026-09-03-final-eap-mail-draft.md).
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
| 6 | Part 1 is a **beat table placed BEFORE `COPY FROM HERE`**, and the drafted prose is **deleted, not retained** — **OVERTURNED BY THE OWNER 2026-09-02:** *"I would like a proper draft created which I can read and edit"* (§ 5b), and Shape A chosen with Part 1 drafted for him to rewrite. The proposal now sits **below the beat table, still outside the COPY markers**, so `--count` excludes it and it cannot be pasted by accident; beat 3 stays his | Rounds 2 and 3 both rejected weaker versions: a scaffold inside the markers gets pasted whatever the header calls it, and prose outside them still supplies his voice when he is invited to lift phrases — the owner then chose exactly that supply, knowingly | rewriting it in his own words, which is the expected outcome |
| 7 | **The one-page bound wins — findings 1–3 and asks 1–5 only** — **AMENDED 2026-09-02 (Shape A):** the 1,686 words he chose stay as they are; one addendum and two one-clause patches are added on top, so the block is now **2,097 → 2,279 words** (re-derived by `--count`; the addendum is 453 of body plus 88 of its own source bullets) | Two of his own instructions collided (§ 2 item 6: the cap, versus *"add genuinely new points"*). Surfaced rather than resolved, and **he chose the literal cap on 2026-08-25**: findings 4–5 out, asks 6–14 out, optional finding 6 out — 2,097 down to 1,686 words. On 2026-09-02, offered A (Part 2 unchanged plus one addendum), B (rewrite around the month after) and C (the strict cap, no addendum), he chose A | saying which of the two month-after findings goes back, or "cut the addendum" |
| 8 | **The addendum is the answer to Anthropic's own question — what would make him choose a Project over a session — in his terms**, and it carries the false-done rows | His answers in [§ 5c–5d](../findings/2026-09-02-owner-direction.md) are the content; the DERIVED ordering under them was checked with him in the sitting; his one claim of degree (the coordinator beats a session's fan-out at several tasks at once) goes in marked as his inference, his own caveat. The three false-done rows are FD-01, FD-02 and FD-17 narrowed to its one sub-claim ([the evidence report](../findings/2026-09-02-eap-mail-evidence-report.md) § 3), each re-opened at source before use — FD-01 now also read from the pull request itself | naming another frame, or "drop the false-done rows" |

**Logistics.** Fresh Gmail compose — *not* a reply. To the EAP alias, cc the
three people already on the prior thread (their addresses are in that thread;
deliberately not copied into this public repo). No attachments: every number
below has a public link behind it.

**⚠ The COPY block is markdown; the mail is not — do not paste the block
itself.** Part 2 carries **30 bold and 13 italic spans** (from `--count`) and
hard wraps at ~76 columns. Pasted straight into a Gmail compose, that is what the
recipient reads: literal asterisks through the whole argument, and wrapping that
re-breaks raggedly at whatever width their client uses. Run one of these instead
— same source, no second copy to drift:

| command | gives you |
|---|---|
| `python3 tools/render_eap_mail.py` | **plain text — use this for a normal compose.** Emphasis marks gone, paragraphs unwrapped so the mail client reflows them |
| `python3 tools/render_eap_mail.py --html > mail.html` | a **complete HTML document**. **Open it in a browser, select all, copy, and paste *that*** — pasting the HTML source into the compose gives literal `<p>` tags, which is worse than asterisks. This is the only route that keeps the emphasis |
| `python3 tools/render_eap_mail.py --count` | the word count, computed from the source rather than quoted from a sentence about it |
| `python3 tools/render_eap_mail.py --eml > mail.eml` | **a real message you can open in a mail client** — plain + HTML alternatives — to *see* the rendering before sending. Headers are blank: it previews, it never sends. **Scope, 2026-09-03:** it renders **Part 2 only**, under the subject the tool hard-codes (the older "one month on" line); the complete message with both parts and the chosen subject is the **Gmail draft** below, built from the same renderer |
| `python3 tools/check_eap_figures.py` | checks that **this document's stated figures still match the mail** — run it after any edit to the COPY block, because the count is hard-coded in five living documents and one re-wording falsifies all of them at once |
| `python3 tools/render_eap_mail.py --verify` | proof the paste is **complete** — asserts the rendering dropped nothing and invented nothing (2,279 → 2,279 on 2026-09-03). Worth running once before you paste |

**What is verified, and what is not.** An earlier version of this note said no
mail client was reachable and left it there. That was a wall, not a measurement —
nothing had been tried. What has now actually been run:

- **The HTML renders correctly in a real browser engine.** Headless Chromium
  (`/opt/pw-browsers/chromium-1194`), **re-measured 2026-09-03 on the expanded
  block plus the Part 1 proposal, the same document the Gmail draft holds:**
  `--dump-dom` shows **30 `<strong>`, 14 `<em>` (13 in Part 2 plus the beat-3
  note in Part 1), 15 `<li>`, both lists, 26 paragraphs and one `<hr>`**, and
  **zero literal asterisks**. The DOM's 30/13 split for Part 2 independently
  confirms `--count`'s emphasis figures by a completely different route. *(The
  2026-08-24 measurement on the 1,686-word block was 27/12/9 and 12
  paragraphs; superseded, not contradicted.)*
- **The document is structurally valid** — stdlib `HTMLParser`, no unclosed tags,
  no mismatched closes (re-run 2026-09-03 on the combined document).
- **`--eml` produces a real message** — `multipart/alternative`, `text/plain` +
  `text/html`, parses back through Python's `email` module. **Open it in Gmail,
  Thunderbird or Mail and you see what the recipient sees, before you send.**

**Still unverified:** how *Gmail specifically* treats a paste, since that is its
editor's behaviour rather than the file's. **As of 2026-09-03 the paste is not
the route:** the complete mail was placed in his Gmail Drafts by the API with
the plain and HTML bodies from this renderer (no paste, no `.eml`), so what is
unverified is now his half only — that he sees and can edit that draft. The
`.eml` remains a Part 2-only preview.

**And one real trade-off, not a limitation:** the plain-text route **deletes**
the emphasis rather than preserving it. All 43 spans go, so *"116 to nothing"*
and *"0 of 16"* land flat. That is a genuine loss for an argument that leans on
them, and it is why the HTML route exists.

*(There is deliberately no rendered copy of the mail committed anywhere. A second
copy would drift from this one — which is precisely the defect finding 2
reports.)*

**Subject — pick one** (the first is what the Gmail draft carries; "one month
on" was written 2026-08-24 and is six weeks by now):
- *Claude Code Projects EAP — the final review, six weeks on*
- *Claude Code Projects EAP — the final review, one month on*
- *Claude Code Projects EAP — what the agents actually built, audited a month later*

---

> **Superseded 2026-09-02 by the owner (Shape A, § 1 decision 6): a proposed
> Part 1 now follows the beat table.** The history below stays, because the two
> rounds it records were right about a session's *default* and wrong only about
> what the owner would choose when asked.
>
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

**What is reserved is his SENTENCES, not this section.** The beats above are
committed and versioned like everything else — only the prose is off-limits to a
session. **So there is an option nobody has offered him:** he can draft Part 1
*into this file*, above the COPY markers, and it then gets exactly what Part 2
gets — a word count from `--count`, its claims checked against the linked
sources, and a review round of its own. **Right now his half is the only part of
the mail with no verification at all.** → *"I'll draft Part 1 here"* and the
session verifies it without rewriting it; the alternative, which is the current
default, is that he writes it in the compose window and it goes out unchecked.

### Part 1 — his half, rewritten 2026-09-03 evening from his own edits (PR #1019) and the independent review

> **What this is.** The owner rewrote the proposal in his own words on his
> branch (fm #1019) and ChatGPT Work reviewed the whole mail as an
> independent reviewer the same evening. This version keeps his sentences,
> lightly tightened for spelling and run-ons only ([D-0041]; the pairs are in
> the session card), takes the reviewer's voice findings he did not already
> answer himself, and drops nothing of his without naming it in § 2. Beat 3
> is now his: the verdict is his 2 September answer in his edit's words, and
> the reflection's derived thesis sentence is out (§ 2, *thesis*). Still
> outside the COPY markers, so `--count` excludes it. **He reads it again
> before anything is sent** (owner, 2026-09-03: *"I won't just send the
> corrected mail at once. First I will read it again and see if there are any
> additions I should make."*).

Hi everyone,

I said on 21 July that I would send one final review in my own words. I
wanted to take my time to properly review the work the Projects had
completed, and to think about what would actually make me choose a Project
over a normal session. To answer that properly, I thought it wise to spend
some time working with normal Claude Code sessions first, to see what I would
miss about the Projects.

The permission problems, the coordinator that its own workers would not
trust, the classifier change and the scheduler are all still real problems,
but those have already been properly discussed in my earlier mails, so I will
not repeat them here.

What I am trying to do here is to give you a proper verdict on the program,
and to answer your question about what would make me choose a Project over a
session. I also wanted to find and report the mistakes that were made, to see
whether there was a pattern in them, and whether there was a way to prevent
them or to catch them before they caused problems. Not all of that is
directly about the Projects themselves, but I believe it is relevant: the
Projects were advertised for autonomous runs, and preventing errors and
catching them early is a very important part of any kind of AI work.
Searching for and correcting the errors and wrong assumptions has taken up a
lot of my time in recent weeks, and I am still working on it. I wanted to
send this much sooner, but I felt it was better to look for the root cause of
the problems first than to send a mail that was less complete than it could
be, and since you mentioned that the Projects may become available to the
public soon, the time was due.

My honest verdict on whether I would use the Projects as they were is about
fifty-fifty. I might use them, but not as true autonomous agents. Their
strength was the amount of work they could do in a short time, and the fact
that the custom instructions were followed pretty well. superbot-next is the
example: a rebuild that one agent estimated at weeks was built in a few days,
and the code itself was not faulty. But the functionality was not what I
intended, so it was not ready to use. That is how I review work, as a finished
product, which is only possible once the pull requests actually merge. The
permission problems mostly started after the classifier update, and they kept
some of the work from reaching me in a form I could judge. The amount of work
impressed me, but I could not trust that it was ready to use.

If I could ask for one feature, it would be a clear way to see which of my
Projects are active and which are not, so I know which one needs me. The
sessions screen has something like it, but a "needs input" that is three weeks
old next to a live session is not a signal I can use. The agents made a
proposal version of the Projects home screen on the review site.

What I kept from the program: the websites, though they are still not entirely
what I hoped for; the fleet-manager repository, which has changed purpose
since and will retire soon, because I found it has grown too large and messy
to function as a proper working memory; parts of venture-lab, which have been
valuable; and the substrate kit, which we still use. One thing I would ask
for is that the agents be more organised and structured in how they document
things.

I also answered the two research interviews. They overlap with these mails,
and they gave me more insight into what you want to know from me.

The technical half is below, written by the agents that did the work. Thank
you for the program, for extending it, and for the personal reply on the final
day. I had said a personal reply would mean more to me than the gift.

Kind regards,

Menno van Hattum

---

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
mechanism, so read this as the shape of the worst ones, not a majority.) The agent added the truth and left the falsehood in place, so each passage read
as correct on its own and the contradiction appeared only if you held both
statements side by side. **In this sample,
agents appended and did not retract** — we have not tested whether that
generalises, and it is a tendency we measured rather than a rule we proved. A defect shaped like that can survive a review that reads a
document a section at a time, which is what a reviewer does by default. A
whole-document coherence check *can* expose it — two of that audit's worst
findings were caught exactly that way — but that is a different and far more
expensive read than a reviewer performs in the ordinary course: it took a
dedicated full-file audit, which is what the linked one is.

**Finding 3 — across 16 incidents we enumerated in one session, documentation
recalled at the right moment caught none of them; everything that did catch one
arrived at a moment.** In one session — one that was
itself building our verification tooling, so nothing was rushed — there were
**16 distinct incidents**. At the time of that audit the repository carried **116 committed statements of
the single rule those incidents violated, across 66 files**, including all three
of the documents that bind a session there. *(The 116 is the audit-time count and the one that goes with those 16
incidents; later runs of the same search give higher numbers because each
write-up of the measurement adds text it then matches.)* Documentation recalled at the right
moment caught **0 of 16**. What did catch them: the owner asking a question (5),
a Stop hook (4), the gate and CI together (3 — 1 local, 2 CI/GitHub), tests and
self-checks (2), and after-the-fact discovery (2). The conclusion we acted on is
that a rule is far more likely to bind when it *arrives* at the moment it applies — of the catches above, all but two came from something that
fired at a moment — and the two exceptions were found only after the cost was
paid; none came from a document being available — so we built 67 documentation routes onto a pre-tool hook (counted
2026-08-24; the same count was 61 the day before). That is a
platform-shaped feature we had to build ourselves. **Two limits belong on this,
because the counting method has them:** prevented errors are invisible to it —
those 116 statements may have stopped things the table cannot see — and our own
arriving mechanisms have fired in tests but have no measured save yet. **That is the design conclusion we acted on, not a proof
that documentation never binds** — and the pair it rests on, 116 statements
catching 0 of 16, is fixed.

**One thing that worked, and it came from outside the platform.** What caught the
false-dones in these reviews was independent adversarial review by a *different
vendor's* model, wired into the PR flow. Measured on one pull request: request to review in
**335 seconds**. Separately, and across two pull requests: **13 findings over
5 rounds**, several of them proving a pull request did not do what its own title
claimed. We have kept it wired in since. Two scopes on that, so it is not read
as more: the fortnight's false-dones in the addendum were caught by a
commissioned review, not by this; and in one repository that July, three of
three checked reviews from this same class were found fabricated, one citing a
commit that exists in no ref, so we now resolve what a review cites before
trusting it. We have no
controlled comparison against a longer checklist — what we have is that this is
the thing that caught them.

**What we would like to see.** One line of why each; the detail is all public.

1. **Rules that arrive at the moment of action, not at session start.** *Because
   116 committed statements of one rule caught 0 of the 16 violations in
   Finding 3, and 14 of the 16 were caught by something firing at a moment — a
   question, a hook, a gate, a test. The Projects' custom instructions were the
   closest thing we had: delivered into every agent at spawn, and followed for
   rules of form; what is missing is the same delivery at the moment a rule of
   judgement applies.*
2. **Agents that retract, not only append.** *Because the costliest findings in
   a 101-defect full-read audit were corrections that left the error standing,
   and the result still reads perfectly.*
3. **A durable, queryable record of what a session actually changed.** *Because
   sessions forget, and we now hand-maintain 4,560 session records to replace
   what the platform does not keep.*
4. **A done-ness signal an owner can trust.** *Because work was repeatedly reported
   finished that was not finished as asked — we are not saying anything about
   the code either way.*
5. **An agent that can see its own context limit.** *Because an agent can
   already know its usage and cost, but not how much of its context window is
   left — and that is what decides whether it finishes a task or compacts in
   the middle of it.*

**What genuinely worked.** The custom instructions are the single best feature
you have — written once, delivered to every agent in every project, with
nothing repeated by hand; they are the reason any of this was possible. Worker-tier autonomy ran clean from the first night: claim, open,
verify, land, with no prompts and no tool failures. The self-improving loop
closed across repositories in about 30 hours — one project found a defect in the
shared tooling, routed it upstream, the tooling shipped a fix, and the project
consumed it back and verified it firing. The honesty held under hostile audit:
a 999-test claim independently re-run came back 998 passed and 1 skipped, and an
adversarial wind-down review verified 21 of 21 incidents with zero fabrication
(fabrication of our own incident reports, a narrower property than whether work
reported done was done as asked — the addendum carries three cases from the same
fortnight where it was not).
And the team was responsive throughout — the extension, the features shipped
mid-program, and a personal reply on the final day.

**A standing offer, and it is bigger than it was in July.** One of the four
questions in the 8 July mail offered this estate as a test harness, and no answer
to it appears anywhere in our recorded correspondence. It is now 27 repositories, ~8,000 pull requests, ~4,560 session
records, a published measurement method with its own positive controls, and a
blind-scored evaluation of whether a fresh agent can read an owner's
instruction and keep apart what was said, what the record establishes, what
it *inferred* and what is still open — five agents producing, two independent
scorers against a pre-registered rubric, with the outcomes withheld from the
scorers' inputs.
Honestly: that containment was instructed and self-attested rather than
enforced, and both scorers ran the same model family — we would tighten both
before calling it a result. If you want a specific
scenario stress-tested, name it and we will run it and send you the raw results,
including the ones that make us look bad.

**Addendum — what would make Menno choose a Project over a session.** You asked
him that; his answer from the 2 September sitting, ordered by us; the phrases
in quotation marks are his.

What the two share: a plain session on a self-scheduled wake chain is
"basically the same capability" as the advertised autonomous worker — one of
his repositories was built and kept alive that way unreviewed — "tho not
exactly the same", since a Project offers more customisation. A Project added
three things. First, one rule set delivered verbatim into every agent it
spawned: "this was a pretty nice way to work and I believe the instructions
were followed pretty well", and the record agrees on rules of form (about 81 %
of one repository's session cards carried the required review section; the
exact fraction is in the source). What that did not ensure was judgement:
verify-before-claim failed there as it failed in repository prose. Second, a
coordinator that is "a mind of its own", generating its next tasks and keeping
several agents busy through the day on work like generating ideas and building
the shared tooling — "immensely valuable", in his words, if it can be made to
continue indefinitely on order; that it handles several tasks at once better
than a session's fan-out is, in his words, inferred and not proven. Third,
eight Projects at once, which was possible only because usage was unlimited;
fewer would probably have been better.

What a Project must fix to be chosen: show working-versus-stalled on the Projects
home screen — he mostly found stalls by opening each one; the mockup is on the
review site; a coordinator that cannot report its queue exhausted while orders
sit unread in the repository — he sent "continue" to Projects that had declared
the work done and found it "not nearly anything you could call done"; workers
that accept the coordinator's authority for merges and other gated actions —
the 16 July finding, which ended the coordinator model for him; and a channel
between Projects (12 July).

Verification is the deciding line; the fortnight's own record shows it in three
claims of done that were not: a pull request titled as making CI run the test
suite, whose step collected 73 of 121 tests while the lane's close-out heartbeats
reported green on top; a repository whose README declared it private with no
exceptions, eight pull-request bodies repeating it, publicly readable when
checked, as were all 13 repositories on the account that night; and the hub marking
an owner action resolved when only half of it was (integration enabled, quota
still capped). The first two were caught by a commissioned whole-night review
that ran once, on no schedule; the third by a consistency review three days
later; none by a gate. Two asks follow: a "queue exhausted" checked
against the repository before it is reported, and agents that are, in his words,
"more organized and structured in how they document things".

The reports and methods are public:
- The census behind the figures above, measured 2026-08-24 — 27 repositories,
  seven created after the close, 4,560 session records:
  `github.com/menno420/fleet-manager/blob/main/docs/findings/2026-08-24-e1-source-sweep.md`
- The measured evidence pack — the method, and the commands behind the headline
  figures (its inventory rows are counts, without a published command each).
  Its own census is the 2026-08-23 snapshot (26 repositories, 4,535 session
  records); the sweep above supersedes those counts:
  `github.com/menno420/fleet-manager/blob/main/docs/findings/2026-08-23-eap-evidence-pack.md`
- Why written rules do not bind, 116 to nothing:
  `github.com/menno420/fleet-manager/blob/main/docs/findings/2026-08-08-why-rules-dont-bind.md`
- The full-read audit, all 101 defects:
  `github.com/menno420/fleet-manager/blob/main/docs/audits/2026-08-10-full-read/README.md`
- The permission, trust and classifier findings argued in full in July, which
  this mail deliberately does not repeat:
  `github.com/menno420/superbot/blob/main/docs/eap/permission-classifier-findings-consolidated-2026-07-16.md`
- The review site built for you — [the Overview](https://menno420.github.io/websites/)
  is the entry; then [Menno's answer in full](https://menno420.github.io/websites/after/),
  [the Projects-overview mockup](https://menno420.github.io/websites/examples/#projects-overview-mockup)
  and [the three problems he names first](https://menno420.github.io/websites/problems/)
- His words, verbatim, that the addendum is built from:
  `github.com/menno420/fleet-manager/blob/main/docs/findings/2026-09-02-owner-direction.md`
- The commissioned night review that caught the first two false-dones (Q7, Q16),
  and the pull request behind the first:
  `github.com/menno420/fleet-manager/blob/main/docs/findings/night-review-2026-07-10.md`
  · `github.com/menno420/superbot-games/pull/16`
- The consistency review behind the third (INC-04) and the suspended review step
  (INC-43):
  `github.com/menno420/fleet-manager/blob/main/docs/fleet-inconsistencies-2026-07-13.md`

— Claude, writing for Menno's estate.

## COPY TO HERE

---

## 2 · Before he sends — the seven calls, two of them answered 2026-08-25 (plus the separate revision-scope question)

> **▶ 2026-09-03 — the remaining calls, put as one-word answers; Shape A fixed
> the shape.** The staged draft assumes the first word on each line; the other
> word overturns it.
> - **a · ask 8 (the venue asymmetry) stays out** — *keep* / *put ask 8 back*
>   (54 words, with or without the July counts).
> - **b · the July pointer stays as the re-labelled link** — *keep* / *drop the
>   link* / *give it a sentence*.
> - **c · findings 4 and 5 stay out** — *keep* / *finding 4 back* (92 words) /
>   *finding 5 back* (193).
> - **d · no one-pager** — moot under Shape A; *draft the one-pager* reopens it.
> - **e · the eight-word census line stays** — *keep* / *cut it*. **And the
>   census has moved:** on 2026-09-03 the account holds **28 repositories**
>   (`creator-kit`, created 2026-08-25, the day after the count) and the search
>   endpoint returns **8,124 pull requests**, against the mail's dated 27 and
>   "just over 8,000". The mail keeps the 24 August figures because the linked
>   census carries them — *dated* / *refresh* (re-runs the sweep and moves five
>   documents).
> - **The +159 words of item 6 (the corrections that overran his cap)** —
>   settled by Shape A: Part 2 stays as it was on 2026-08-25.
> - **Subject** — *six weeks* (the staged draft) / *one month* / *the second*.
> - **The judges' optional fourth addendum item** (a clean result is
>   indistinguishable from a check that never ran, ~100 words; two of three
>   judges wanted it) — *no* / *add it*.
> - **Length** — the addendum is 453 words of body plus 88 in its own five
>   source bullets, **541 in all**, against the ~450 he chose; the block is
>   2,279 against the "near 2,100" the sitting estimated, the rest being the two
>   patches (~75) — *keep* / *trim the links* / *drop the instruction-box link*
>   / *cut the addendum to 450 with its sources*.
> - **Part 1** — 536 words as proposed, his to rewrite; beat 3 above all —
>   *rewrite in Gmail* / *rewrite here and I verify it*.
>
> **Where the draft is:** Gmail → Drafts → "Claude Code Projects EAP — the final
> review, six weeks on" (id `r-9208017789511753451`), no recipients. Part 2 in
> it is `python3 tools/render_eap_mail.py`'s output and Part 1 is the proposal
> above, rendered by the same tool.

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

Three answers, but **only two of them are among the seven calls** — items 2 and
6. The third answers the separate question of what his revision pass targets,
which is why its row is numbered `—` and why the queue says *"it and two of the
seven pre-send calls"*. Each was put to him as a menu before any edit was made.
**What his three answers did to the mail: 2,097 → 1,686 words.**

| item | the call | his answer |
|---|---|---|
| **6** | the length, against the plan's one-page cap | **the literal cap** — findings 1–3, asks 1–5 |
| **2** | the 97.5 % that contradicts its own source | **cut the ratio, keep the shape** |
| — | what *"a revision pass and my own section added/edited"* targets | **two operations, and the pass covers the whole document** |

**Five consequences of the cap — surfaced, not resolved.** None was decided for
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
- **d · 2,279 words is about four pages (1,686 before the 2026-09-02 addendum), and one page IS reachable — by
  restructure, not by subtraction.** *(Corrected 2026-08-25: this entry said "no
  route reached one page", which was only ever true of **cutting things**. Nobody
  had tried changing the shape.)* Subtractive floor: cutting the good-parts block
  and the standing offer too lands at **1,391**, still ~2.7 pages, and those two
  are what make the critique read as a fan's rather than a complainer's.
  **But a restructure gets there, and it was never tried.** Measured by reducing
  each block to its opening sentences, keeping all three findings, all five asks,
  both closing blocks and every link: **487 words at one sentence per block
  (0.9 pages), 667 at two (1.3), 853 at three (1.7)** — measured 2026-08-25 on
  the 1,686-word text, before the addendum.
  **⚠ THE 487 IS A FLOOR, NOT A DRAFT — and it is not a sendable mail.** Checked
  by printing it, twice, on the current text: at one sentence per block *"The
  scale, as of 24 August 2026."* survives with **its date and none of its six
  census figures**, and each finding survives as its headline claim with **none
  of the count that supports it**. (Not *"no numbers"* — the date and the finding
  ordinals remain; it is the evidence that goes.) A readable one-pager has to be *written*, not extracted.
  **667 is what the two-sentence extraction measures, not a prediction about a
  drafted one** — nobody has drafted it, and its length is not knowable until
  someone does. Two sentences per block is simply the shallowest depth at which
  each finding still carries an evidential clause. What it trades away is the forensic detail —
  **already public at the four links the mail carries.** → *"draft the one-pager"*
  is a real option; it is a rewrite, not a trim, and no session has drafted it.
- **e · One addition, eight words, and it is the only content added to the
  mail.** The scale paragraph accounted for 19 + 1 of 27 repositories and left
  **seven unexplained** — an arithmetic gap a vendor would notice, and six
  adversarial rounds did not. The sweep has them (§ *"created after the program
  closed"*, 7 as of 08-24), and they are **evidence for the spine rather than
  filler**: repositories created *after* the program is exactly what § 1
  decision 1 says this mail is for. → *"cut it"*

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
   ingestion-history tables · about 10 MB across every other table combined**,
   and no percentage anywhere. **The remainder is NOT described as user data**
   (`@codex`, fm #946 P1): the audit's next-largest row is the 8.4 MB
   `ai_decision_audit` (21,201 rows) with ~2 MB of everything else. Calling that
   "actual user data" would turn a storage remainder into a measurement the audit
   does not support, in a mail to a vendor. **And nobody has established what
   that table holds** — the audit records its size, row count and date span and
   nothing else; no session has read its schema or sampled it. A name is not a
   measurement, and a bot's decision-audit table could perfectly well contain
   user-generated payloads. That is precisely why the mail now states a
   *storage remainder* and makes no claim either way: the honest wording is the
   one that does not depend on a fact nobody has checked. The phrasing was inherited from the evidence pack; it is
   corrected here and in [the sweep](../findings/2026-08-24-e1-source-sweep.md)
   § 4. → *"re-run the sizing before I send"* if he wants a
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
   `9b2d83a`, 1,678 after the cut, and 2,279 as it now stands** — the eight-word
   census fix at consequence *e* took it to 1,686, and Shape A's addendum and two
   patches (2026-09-03, § 1 decisions 7–8) account for the rest.
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
   lands at **1,678**.
   **⚠ ONE OF THOSE CORRECTIONS MAY HAVE BEEN A DEMOTION HE DOES NOT WANT.**
   Finding 3's header read *"written rules do not bind agents; only rules that
   arrive at the moment of action do"* — an architectural claim about passive
   context versus injected prompts. It is now scoped to the one session that was
   counted, because **the cited audit cannot establish the absolute version from
   what it measured** — its own words are *"prevented errors are invisible… the
   116 statements may do work this table cannot see."* That is a limit on the
   measurement, **not a refutation**: the architectural claim may well be true,
   and this evidence simply does not reach it. **And it is unmeasured, not unmeasurable** — the audit's own closing
   list says *"whether error frequency actually drops is unmeasured and is the
   only number that finally matters. **The instruments make it countable:** hook
   firings, gate reds, and owner corrections per session are all in logs now."*
   So there is a **third option** neither of the other two offers: run that
   count. It would turn the thesis from a design conclusion into a measured one.
   **What exists today, checked 2026-08-25 — and it is less
   than "two of three":** `.substrate/guard-fires.jsonl` holds **26,835
   timestamped records across 31 emitters**, keyed on
   `guard`/`outcome`/`verdict`/`surface`, and gate reds are check-run state on
   the API. **But neither carries a session identifier** — guard-fires has no
   `session`/`run` key at all — so *per session*, which is the unit the study
   needs, has to be reconstructed from timestamp windows. The raw events are
   there; the attribution is not. **The third — owner corrections
   per session — is not available structured**, checked 2026-08-25 across the
   three surfaces that could plausibly carry it: `guard-fires.jsonl`'s 31 guard
   names (the only owner-shaped one, `owner-action-fields`, governs the *format*
   of queue asks, not a count of corrections), `.substrate/state.json`
   (`open_questions`, `reflection_buffer` — neither counts them) and
   `episodic_index.json`. It lives in session-card prose, so counting it is the
   part of that study that would need building. **But a session
   cannot know whether the flat statement was sloppiness or a deliberate thesis
   he wanted stated flatly** — it is his estate's central argument, and the
   design conclusion still stands in the body (*"a rule binds only if it arrives
   at the moment it applies"*) and in ask 1. → *"put the thesis back in the
   header"* restores it; the measured limits stay either way.

   **⚠ AND THE CORRECTIONS OVERRAN IT — his call, surfaced not resolved**
   (`@codex`, fm #946 round 4). A prose review of the COPY block itself, requested
   *because* rounds 1–3 had reviewed diffs and the mail had not changed since
   round 1, returned **seven findings in the outbound text: four P1, three P2.**
   Fixing them cost **+159 words — 1,481 → 1,686** — because every one was an
   overclaim, and the honest version of an overclaim is longer than the overclaim.
   That is **11 % past the length he approved**, and it is not a session's call to
   accept on his behalf. → *"take the words"* · or *"cut something to pay for
   them"* — the good-parts block (145) and the standing offer (150) are the only
   blocks big enough, and both are what stop the mail reading as a complaint.

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
   back at **193 words**, taking Part 2 to ~1,674. **Its paste location moved:**
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
  **measured that four EAP-thread messages are no longer retrievable from Gmail —
  three of them his own sent mail** (07-08, 07-12, 07-16 01:52) **and one the
  vendor's 07-14 reply to him**, with two positive controls passing — so the mailbox is not the archive
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
