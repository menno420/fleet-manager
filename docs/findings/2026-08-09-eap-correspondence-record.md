# The EAP correspondence — what was sent, what came back, and what is still owed

> **Status:** `reference` · 2026-08-09
>
> **Why this file exists:** the facts below existed only in a chat transcript and
> cost roughly 300k characters of mailbox reading to derive. Program step **E1**
> (the final EAP email) cannot be written without them, and E1 has been the NOW
> pointer since 2026-07-26. A fact that lives only in a handoff prompt is not in
> the repo — [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md)
> makes that point about a document, and it is truer of a mailbox.
>
> Certainty tags per that file's legend. Everything marked `MEASURED` was
> re-queried against Gmail **on 2026-08-09 by this session**, not carried from
> the handoff that supplied it.
>
> **Confidentiality method — read this before adding to the file.** The program
> is covered by a confidentiality agreement, and the owner personally answered a
> reminder of it with *"the confidentiality is safe with me."* This repo is
> **public**. So this file follows the most careful precedent already in the
> tree ([`../pre-reboot-review-2026-07-15.md`](../pre-reboot-review-2026-07-15.md)
> § EAP extension): **reference metadata only for the vendor's messages — dates,
> subjects, message ids, and their substance in our own words — with bodies
> unreproduced.** The owner's *own* words are quoted verbatim: they are his, and
> [`../owner-reflection-2026-07-21.md`](../owner-reflection-2026-07-21.md)
> § Confidentiality is explicit that his ideas are not the confidential part.
> The gift-code redemption link is a personal credential and is **not recorded
> here at all**.

## 1 · The shape of the correspondence

`MEASURED` 2026-08-09. Two threads carry everything that matters.

**Thread A — "Claude Code Projects Review"** (`19f41cd2e5380bb3`). Five messages:
four substantive owner reviews and **one** vendor reply.

| # | when (UTC) | from | what it is |
|---|---|---|---|
| 1 | 2026-07-08 15:06:39 | owner | the introduction review — two-part human/agent, the permission-probe table, and four direct questions |
| 2 | 2026-07-12 13:24:40 | owner | the scale-up report (1 → 15 repos) |
| 3 | 2026-07-14 00:57:48 | vendor team alias | the only reply in this thread — a thank-you, signed with a first name |
| 4 | 2026-07-16 01:52:08 | owner | the classifier-crisis report |
| 5 | 2026-07-16 21:12:02 | owner | the follow-up, both models tested, same result |

**Thread B — the power-user thread** (`19f85d35fa344225`), 2026-07-21. Five
messages, and unlike thread A it is a genuine back-and-forth: vendor 17:57:18 →
owner 18:28:47 → vendor 18:35:25 → owner 20:07:32 → vendor 20:28:07.

**Also on the record**, metadata only: a UX-research interview invitation on
2026-07-10 21:14:08 (`19f4de1a02874f58`) and **a second one** on 2026-07-21
18:53:34 (`19f8606e24dab896`); program announcements on 07-09, 07-14 and 07-16;
and the program-ending notice on 2026-07-21 16:33:12 (`19f85865fa17b54d`).

## 2 · The finding: four direct questions, none answered

`MEASURED`. The 07-08 review closed with four numbered questions under the
heading *"A few questions back to you — we'd rather calibrate than assume"*.
Restated compactly, they asked:

1. whether the destructive-git wall and the absence of a scoped pre-authorization are **intentional** — explicitly offering to design around it permanently if so;
2. whether there are **settings or workarounds already shipping** that the owner had not found;
3. **which scenarios the vendor would most like stress-tested**, offering a ~1,700-PR autonomous project as a harness and verbatim results;
4. whether the **Contents-API-vs-git-push asymmetry** is a sanctioned bootstrap surface or a gap.

**None of the four was answered, then or since.** The single reply in thread A
is **205 characters** of body — a thank-you for the time and feedback, with no
technical content. That number is the finding, and it is measured rather than
characterised: 205 characters against four reviews.

**Question 3 is the one worth carrying into E1.** It is a standing offer of free,
structured testing capacity from an unusually instrumented harness, and it was
never taken up. The E1 plan's § 3 already flags the standing test-harness offer
as net-new material; this is the evidence that it was made and left open.

## 3 · The outstanding commitment — his words, twice

`MEASURED`, verbatim, both in thread B on 2026-07-21. This is the reason E1
exists as a program step at all.

At 18:28:47 —

> I am planning to send one final feedback email to properly explain everything
> of importance in my own words. I would highly appreciate it if you could give
> me a short list of the things you would most like to know from me, so I can
> direct my time on that.

At 20:07:32 —

> I've just completed Matt's interview and will still send my final review later
> on like I said

**Two promises to a named person, 19 days old as of this file.** The second also
confirms he completed the second research interview. A third quote from the same
thread sets the tone the reply came back in — he asked, in the 18:28 message,
for *"a personal reply that shows me you've really taken the time to review my
feedback,"* saying he would be happier with that than with the gift.

## 4 · There is no vendor-supplied agenda — content is his call

`MEASURED`. The agenda request sits inside the 18:28 message above. The reply at
18:35:25 answered the *other* half — it confirmed, personally and by name, that
the engineering team had been reading his feedback and that this is how he was
identified as a power user — **and supplied no list.** No later message supplies
one either.

**So the "short list of things you'd most like to know" never arrived, and E1's
content is entirely the owner's choice.** That is a genuine finding for the
writing session: there is nothing to wait for, and no external agenda to satisfy.

**It also corrects the record in the vendor's favour.** The 18:35 reply *is* a
substantive, personal response, and it directly answered the thing he said he
wanted most. Any characterisation of the correspondence as "one 205-character
thank-you and nothing else" is true of thread A and false of the whole.

## 5 · Four corrections to the relayed fact list

The handoff that commissioned this file supplied these facts as settled. They
were derived by a prior session and **relayed through a prompt** — a provenance
this estate has already been burned by (fm #830 error #7 called agent-quoted
fragments "owner messages"). Re-querying found most of them exact and four
wrong. Recorded because the corrections are cheap here and expensive in a sent
email.

| # | the relayed claim | what the mailbox says |
|---|---|---|
| 1 | the 07-14 reply came from the product-operations manager's own address | it came from the **team alias**, signed with her first name. The person is right; the address is not |
| 2 | *"Anthropic's ONLY substantive reply"* was the 205-character thank-you | true **of thread A only**. The 07-21 18:35 reply is a second substantive personal reply — see § 4 |
| 3 | one UX-research interview invitation, on 07-21 | **two** — 2026-07-10 and 2026-07-21. The 07-21 one is explicitly *"again"* and references the earlier round |
| 4 | on 07-22 he reported the platform still fully live ~11h past the announced cutoff, and got a reply saying access would be turned off shortly | **not corroborated in Gmail** — see below |

**Correction 4 in full, because an absence needs its method shown.**
`in:sent after:2026/07/21 before:2026/07/24` returns exactly two threads: the
power-user thread (last owner message 07-21 20:07:32) and an unrelated one.
**No owner-sent mail exists on 07-22 or 07-23.** A query for the reply's
reported phrasing across 07-20 → 07-28 also returns nothing matching.

**Positive control passed:** the same `in:sent` query correctly returns the
known-present 07-21 sent messages, so the query works and the window is right.
Per `capability-probe` step 3b, that is what converts *"I found nothing"* into
*"nothing is there"* — **in this lane.** It is recorded as **uncorroborated,
not as disproved**: the exchange may have happened on a surface Gmail does not
hold (in-product feedback, a session transcript, another channel). The claim
should not be repeated as fact in E1 without a source, and it should not be
called invented either.

## 6 · What this changes for E1 — the net-new axis

The owner stated a new frame for the final email on 2026-08-09, and it does not
appear anywhere in the E1 plan:

> once we are finished with improving the fleet-manager, we should focus on
> finding the errors that have been introduced in the repos, and mostly what a
> project has created based on my input.

and, on what autonomous agents actually did versus what was expected:

> What is expected of an autonomous agent is that it understands intent and
> properly acts on it, while some of that is true. What I noticed is that they
> have forgotten a lot, and claimed finished products while obviously they were
> not finished in the way I intended.

**Two named failure modes: FORGETTING and FALSE-DONE.** Both are *outcome* claims
about what the program produced, and the E1 plan's § 4 seeded list is **entirely
platform asks** — permissions, scheduling, oversight, primitives. Checked item by
item: none of its thirteen entries is an outcome claim. So this axis is genuinely
net-new material for the mail, not a re-cut of what is already listed.

**It also sets up the reconciliation.** He has said the repo-by-repo sweep *is*
the evidence base for the email — the errors and the false-dones are what a
final review would be reporting. That sweep is a program of its own and needs
him to scope it; this file is only the correspondence half of the foundation.

## 7 · What is not verified here

Kept explicit so the next session does not inherit this file's silences as
completions.

- **The bodies of the owner's 07-12 and 07-16 reviews** were not re-read; only their metadata and position in the thread. The four questions in § 2 come from the 07-08 body, which **was** read in full.
- **Correction 4's underlying event** — uncorroborated, not disproved. See § 5.
- **Whether the vendor ever replied on any non-mail surface** is not knowable from Gmail and was not investigated.
- **Nothing here has been checked against the unsent 2026-07-18 follow-up draft** (superbot `docs/eap/2026-07-18-followup-email-draft.md`), which the E1 plan § 2 lists as unused material. That repo was not attached.
