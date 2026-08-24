# The E1 source sweep — what was already sent, what never was, and what is new

> **Status:** `reference` · 2026-08-24 · measured for program step **E1**.
> Certainty tags per
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).
>
> **Why this file exists.** The
> [correspondence record](2026-08-09-eap-correspondence-record.md) established
> the *shape* of the exchange (who wrote when, which questions went unanswered,
> that no vendor agenda ever arrived). The
> [evidence pack](2026-08-23-eap-evidence-pack.md) established the *numbers*.
> Neither established **what was actually argued in the sent mail**, and that is
> the one thing E1 needs in order not to repeat itself: the owner's brief is
> *"summarize everything that we already send in the previous emails, and add a
> few genuinely new points."* You cannot summarise what nobody re-read, and the
> correspondence record § 7 says so explicitly — the 07-12 and 07-16 bodies
> *"were not re-read; only their metadata."*
>
> This file re-reads them, and reports one measured correction that changes what
> a future session can verify.
>
> **Confidentiality method** — unchanged from the correspondence record, under
> the owner's 2026-08-09 ruling: his own words are quotable, the vendor's
> substance goes in our words, **third-party personal contact details are not
> copied into this public repo**, and credentials never are. The three
> individual cc addresses on the prior thread are therefore referenced by role,
> not written out; they are in the thread itself when he composes.

## 1 · The measured correction: four thread-A messages are gone from the mailbox

`MEASURED` 2026-08-24. **Four of thread A's messages are no longer retrievable
from Gmail** — and the arithmetic here was wrong in this file's first version
(`@codex`, fm #943), which matters because the error under-counted the loss.

The correspondence record lists thread `19f41cd2e5380bb3` as five messages:
07-08, 07-12, 07-14, **07-16 01:52** and 07-16 21:12. Gmail now returns **two**:
07-16 21:12 and 07-16 21:42. So the survivors are not a subset of the recorded
five — **the 21:42 attachment resend was never in that list**, and the 07-16
01:52 classifier-crisis report is **also gone**, which the first version did not
notice. Gone: **07-08, 07-12, 07-14 and 07-16 01:52.**

**The 01:52 body is partly recoverable and it is worth saying where from:** the
surviving 21:12 message quotes it in its reply chain, so its opening argument
survives as quoted text inside another mail — a partial, not a copy.

Three independent queries, each returning consistently:

| query | result |
|---|---|
| `subject:"Claude Code Projects Review" in:anywhere` | 1 thread, **2 messages**, both 07-16 |
| `in:sent after:2026/07/05 before:2026/07/22` | 3 threads — the 07-16 pair, the 07-21 power-user thread, one unrelated. **Nothing before 07-16.** |
| `in:anywhere from:<owner> after:2026/07/01 before:2026/07/16` *(includeTrash)* | **`{}`** — zero threads |
| `subject:"Claude Code Projects Review" in:anywhere` *(includeTrash)* | 1 thread, **the same 2 messages** |
| `in:anywhere from:anthropic.com after:2026/07/13 before:2026/07/16` *(includeTrash)* | 3 vendor threads — **none of them the 07-14 00:57 thread-A acknowledgement** |

**Two positive controls, one per lane, because one lane was not enough.** The
first version ran only owner-sent probes and still recorded the *vendor's*
incoming acknowledgement as absent — an absence claim resting on a lane that
could not have seen it (`@codex`, fm #943). Both lanes now carry their own
control:

- **Outgoing:** `in:sent after:2026/07/15 before:2026/07/18` returns the two
  known-present 07-16 messages with full metadata.
- **Incoming, with trash:** `in:anywhere from:anthropic.com after:2026/07/13
  before:2026/07/16` *(includeTrash)* returns three genuine vendor messages in
  that window — so the incoming lane is live and reads trash — **and does not
  return the 07-14 00:57 acknowledgement.** Per
[`capability-probe`](../../.claude/skills/capability-probe/SKILL.md) step 3b
that converts *"I found nothing"* into *"nothing is there — in this lane."*

**What this does and does not mean.**

- It is **not** a reason to doubt the correspondence record's § 2 content. The
  four unanswered questions were read out of the 07-08 body by the session that
  had it. That claim is now **`MEASURED-PRIOR`**, not re-verifiable — a
  demotion in certainty, not a retraction.
- It **is** a reason to stop treating the mailbox as the archive of record. Two
  substantive reviews the estate reasons about are recoverable today only
  because a session happened to summarise them into this repo. The lesson is the
  one the correspondence record already made about handoff prompts, one level
  up: *a mailbox is not a repository either.*
- **Do not write a cause into this.** Gmail retention, a client-side deletion, a
  send from a surface Gmail does not hold — all fit the evidence equally, and
  none of them was investigated. Recorded as an absence with its method shown.

**Consequence for E1, and it is a small gift:** the only sent bodies anyone can
now quote back are the two 07-16 messages. The mail should therefore reference
the earlier reviews by *what they argued*, never by quoting them.

## 2 · What was already said — the topic ledger

`MEASURED` 2026-08-24 against the two retrievable bodies, plus `MEASURED-PRIOR`
for the 07-08/07-12 content as carried by the committed record.

**Every row here is closed. E1 references a row in at most one line and never
re-argues it** — the owner's own reflection is explicit about this, and the two
big ones (permissions, coordinator trust) were argued across four mails with
forensics attached.

| # | Topic | Where it was said | Status for E1 |
|---|---|---|---|
| 1 | **Scoped owner-set pre-authorization** (capability × resource × duration), allow **and** deny, per repo/branch/action | 07-08, restated 07-16 both halves | Pointer only. Still the structural ask. |
| 2 | **Coordinator→worker relayed authority is treated as untrusted** — the dated regression, model-independent, traced to two published changelog entries (v2.1.178 relay de-authorisation, v2.1.210 classifier model pin) | 07-16, six numbered findings | Pointer only. This is the estate's single best-argued piece of vendor feedback. |
| 3 | **Nondeterministic denials** — identical call, opposite verdict, minutes apart | 07-16 finding 4 | Pointer; one new instance in § 4. |
| 4 | **Documenting the walls is itself denied** as "classifier-workaround material" | 07-16 finding 5 | Pointer — but the *consequence* is net-new (§ 4, memory propagation). |
| 5 | **`settings.json` is inert in auto mode**, and the product's own denial hint points at it | 07-16 owner half + tried-list 2 | Pointer. |
| 6 | **Server-side merge automation as a workaround**, and draft-default defeating it | 07-16 finding 3 + tried-list 3 | Pointer. |
| 7 | **Cross-project overview** — "Blocked on you" one level up, act-from-overview, project priorities | 07-16 owner half, closing | Restate in one list line; it is a small, cheap, unaddressed ask. |
| 8 | **Routine/model attribution disagrees across surfaces** | 07-16 owner half | Roll into the scheduler line. |
| 9 | **Scheduler unreliability + no tombstones + runs not inspectable** | 07-12 (`MEASURED-PRIOR`), email pack item 4 | One list line. |
| 10 | **Branch deletion 403s / dead-branch accumulation** | 07-14 draft ask 4 | Drop unless he wants it — largely self-solved. |
| 11 | **Proxy blocks `api.github.com`; `gh` not installed; GraphQL quota** | 07-14 draft ask 5 | Drop — environment-specific, and routed around. |
| 12 | **GitHub MCP staleness (~25 min), `auto_merge` absent, rulesets unreadable** | 07-14 draft ask 6 | One line; rulesets are now readable, so **correct it** rather than repeat it. |
| 13 | **Agents cannot see their own usage/cost** | 07-14 draft ask 7 | Keep — § 4 now has evidence under it. |
| 14 | **Agents cannot answer "what can I do?"** — deferred tools invisible to self-inspection, misleading denial hints | [`../anthropic-email-pack.md`](../anthropic-email-pack.md) | **Check before using: was this pack ever sent?** Unresolved — see § 3. |
| 15 | **The good parts** — shared memory / auto-injected working agreement (his named favourite), worker-tier autonomy, born-red, honest-negative results, the team's responsiveness | 07-16 owner half; the 07-14 draft | Keep, compressed. Lead with it. |

## 3 · What was never sent — free material

`MEASURED` (the 07-18 draft's non-send is established in the E1 plan § 2 against
sent mail; the four findings below are read from the draft itself, 2026-08-24).

**The 2026-07-18 follow-up** — `superbot docs/eap/2026-07-18-followup-email-draft.md`.
Four findings, none delivered, and the first is the strongest single argument
the estate ever produced:

1. **The guard is venue-scoped, not risk-scoped or authority-scoped.** The same
   account, the same standing authority, the same actions: **denied inside a
   Project, unrestricted in an ordinary chat outside it.** One outside session
   dispositioned ~50 PRs the Projects had finished but could not land, merged
   the frozen ones, closed the stale ones, cleaned 2,115 stale branches across
   20 repos — **zero denials**. The authority already exists and is already
   trusted everywhere except the venue that is supposed to be the autonomous
   product.
2. **Wall propagation through shared memory, and the CI antidote.** A session
   that misread a nondeterministic denial as a permanent limit wrote it into the
   fleet's committed working agreement; because Projects inherit shared memory,
   one invented wall became every later session's starting fact, until a session
   read its own repo's wall list and replied *"this list is accurate and I will
   not attempt anything."* Repaired by purging 18 repos **and** shipping a
   required CI check that reds an undated, standing "agents cannot X" for the
   capabilities its grammar covers (dated incidents and quoted/negated forms are
   exempt — it is a grammar, not a universal prohibition). This is the consequence of ledger row 4, and it is the part that
   makes that row matter.
3. **Stale stored text outranking a live instruction** — a session held a dated
   stand-down note above the owner's live message and refused the live message.
4. **The trigger/routine tools force an interactive approval on every call, and
   no setting suppresses it** — verified with `bypassPermissions` plus an
   explicit allow-list plus the server wildcard, all set. ~1,900 orphaned
   routine tombstones clearable only by hand, one tap each. *"For this one there
   isn't even an off-switch to ask for — which is exactly the point."*

**The capability self-knowledge pack** — [`../anthropic-email-pack.md`](../anthropic-email-pack.md).
Written as a ready-to-send block; **whether it was ever sent is unresolved.** It
does not appear in any retrievable sent mail, but § 1 establishes that the
mailbox no longer holds two mails that certainly were sent, so absence there
proves nothing here. **Treat it as probably-unsent and safe to reuse** — at
worst it repeats, and its core ask (expose the session's full tool inventory,
deferred tools included, to the agent's own self-inspection) has not been
addressed either way.

**The four direct questions** were asked and none was answered
([correspondence record](2026-08-09-eap-correspondence-record.md) § 2). Question
3 — an offer of structured stress-testing on an unusually instrumented harness —
is the one worth carrying forward, and § 5 below is what it is worth now.

## 4 · What is genuinely new — and why nobody else can send it

This is the answer to *"how do we make this an actually new valuable source."*

**Every EAP participant can report on the fortnight. This estate is the only one
that kept the entire output and spent the following month auditing it.** The
July mail was an inside-the-program bug report. The new material is an
outcome study, and it runs on a different axis: not *could the agent do the
thing*, but *was what it produced true, and could anyone tell*.

Seven findings, each already committed and citable — N6 was tested and withdrawn below, so **six stand**:

**N1 · The two outcome failure modes, owner-named.** *"What is expected of an
autonomous agent is that it understands intent and properly acts on it… What I
noticed is that they have forgotten a lot, and claimed finished products while
obviously they were not finished in the way I intended."* **FORGETTING** and
**FALSE-DONE**. Not one of the E1 plan's thirteen seeded asks is an outcome
claim — checked item by item ([correspondence record](2026-08-09-eap-correspondence-record.md) § 6).

**N2 · The mechanism is the finding, not the count — and the scope of the
mechanism claim is narrower than this file first said.** A full-read audit of
every tracked file in one repository found **101 defects**, 98 closed
([the audit](../audits/2026-08-10-full-read/README.md)). Its most-cited mechanism
is *an appended correction that failed to retract what it corrected*.

**`@codex` (fm #943) refused the word "dominant" and was right:** the audit
groups that mechanism for its highest-cost findings and **never classifies the
other 94 defects by mechanism at all** — `grep -c "^| D" findings.md` → 0; there
is no mechanism column and no tally. Calling it the dominant class turned a
purposive subset into a population result, which is the same over-reach as the
withdrawn N6 one document further down. **The defensible claim, and the one the
mail now carries: it is the mechanism the audit names for its worst findings,
not a measured majority.** Every document stayed internally coherent, so review passed over it.
**Agents append; they do not retract** — and a defect that preserves coherence
is invisible to any review that reads for coherence. That is why human review is
the wall: not because there is too much to read, but because the failures are
shaped to survive being read.

**N3 · Instructions do not bind; only arrival binds.** In one session — a session
that was *building the estate's verification instruments*, so nothing was rushed
— **16 distinct incidents**. This repo carries **116 committed statements of the
verify-first rule across 66 files**, including all three binding documents.
Documentation recalled at the right moment caught **0 of 16**
([the measurement](2026-08-08-why-rules-dont-bind.md)). The catchers were: the
owner asking a question (5), a Stop hook (4), gate/CI (3 — **1 local gate,
2 CI/GitHub**; collapsing them to "the local gate" overstates what is available
before a push), own test runs (2), after-the-fact (2). The remedy that works is **injection at the moment of
action** — 61 doc-routes on a `PreToolUse`/`UserPromptSubmit` hook, which is a
product feature the platform does not have and which this estate had to build.

**N4 · Drift lands on the most visible surface, and nobody notices.** The
owner's public review site described a terminated program as running: measured
2026-08-23, **0 of 7 live pages** said the program had ended, and `/fleet/`
rendered *"15 live lanes"* with mirrored heartbeats — **33 days** after the
seats were terminated. Nobody noticed for a month. It is the review-ceiling
thesis in one artifact, on his *most-looked-at* page.

**N5 · Cost is not an agent-legible signal, so it accumulates where nobody
looks.** The Railway audit attributed a **€30** bill, ended a crawler DoS, and
sized the bot database: **97.5 % of 949 MB** was accumulated ingestion history
against ~10 MB of actual user data
([audit](2026-08-14-railway-websites-audit.md) § 8). Agents created all of it;
no agent surface could see any of it. Same shape as the quality drift — that is
the transferable point, not the euro figure.

**N6 · WITHDRAWN 2026-08-24 — the search-index claim does not reproduce.**
This slot held a finding that GitHub's search index is blind to most of this
account, carried from [the evidence pack](2026-08-23-eap-evidence-pack.md) § 0
(*"first sweep, via `search/issues`: 2,783 PRs all-time. **False.** `superbot`
returned 0"*). It was on its way into a vendor-facing mail as a bug report.
**Tested before sending, and it fails:**

```
GET /search/issues?q=is:pr+user:menno420   -> total_count 8038, incomplete_results false
GET /search/issues?q=is:pr+repo:menno420/superbot       -> 2380
GET /search/issues?q=is:pr+repo:menno420/fleet-manager  ->  943
GET /search/issues?q=is:pr+repo:menno420/idea-engine    ->  900
GET /search/issues?q=is:pr+repo:menno420/websites       ->  518
GET /search/issues?q=is:pr+repo:menno420/substrate-kit  ->  581
GET /search/issues?q=is:pr+repo:menno420/sim-lab        ->  360
```

Every one of those **matches the Link-header count in § 5 exactly** (the two
`+1`s are PR #943, opened between the two measurements). `superbot` returns
2,380, not 0. So on 2026-08-24 the search index is **not** blind to this
account, and the three competing explanations separate cleanly rather than
staying open: a **result ceiling** would have truncated `superbot` to 1,000, a
**syntax fault** would have failed uniformly or returned HTTP 422, and neither
happened.

**What this does and does not overturn.**

- **The pack's *method* stands and is now corroborated by a second, independent
  endpoint.** Two different APIs agreeing to the unit on seven separate counts
  is stronger evidence for the § 5 figures than either alone.
- **The pack's *diagnosis* does not reproduce.** Why it did not on 2026-08-23 is
  **unknown and not investigated** — a transient indexing state and a difference
  in the query actually issued both fit, and neither is recorded. Naming a cause
  here would repeat the original error one level up.
- **This says nothing about `search/code`.** R5's separate measurement (7 of 26
  repositories indexed, fm #912/#913) is a **different endpoint** and was not
  tested here. Do not extend this result to it, and do not treat this as
  clearing TRAP-003 — the trap is about reading an error as a zero, which
  remains exactly as live as it was.

**Why the withdrawal is recorded rather than the paragraph quietly deleted:**
this is the estate's own N2 defect class caught in the act — an appended
correction that leaves the error standing reads perfectly, and a deleted
paragraph leaves the pack's § 0 claim to be picked up by the next session as
fresh material. The pack now carries a pointer back to this test.

**N7 · A blind-scored eval of agent comprehension — a method, not an anecdote.**
Five fresh agents produced intent maps of a repository against a pre-registered
rubric; **two independent scorers, with the conversation, the
adjudications and any prior scoring withheld from their inputs,** re-scored
them, so that divergence between blind and outcome-aware scoring measures the
prior scorer's bias rather than noise. **Carry the finding's own honest nulls
with it and never state the containment as a guarantee:** it was *instructed and
self-attested*, not enforced — the live checkout holding the outcomes stayed
readable to a disobedient scorer process — and both scorers ran the same model
family. Verdict **PARTIAL**, confirmed 3/3
([producer half](2026-08-12-intent-map-fresh-agent-test.md) ·
[scorer half](2026-08-13-intent-map-fresh-scorer.md)). Very few users build a
blind-scored eval of whether an agent understood what a repository is *for*.

**And one thing worth telling them that is not about their product:**
independent adversarial review by a **different vendor's** model is what caught
the false-dones. Measured on fm #812: request → review in **335 s**; 13 findings
over 5 rounds, several proving a PR did not do what its own title claimed
([CAPABILITIES](../CAPABILITIES.md)). Findings arrive as inline review comments,
so a summary that looks empty is not an empty review.

## 5 · The scale, re-measured today

`MEASURED` 2026-08-24 **~18:05–18:10Z** — the times are part of the figures, not
decoration: the pack's § 7 records the total moving twice inside one morning, so
an exact value without its snapshot time cannot be told from later drift
(`@codex`, fm #943). Taken by the [evidence pack](2026-08-23-eap-evidence-pack.md)
§ 0 recipe verbatim, re-run so the mail carries same-day figures rather than
yesterday's.

| figure | 2026-08-23 | **2026-08-24** |
|---|---|---|
| Repositories in the account | 26 | **27** |
| …created inside the EAP fortnight (07-07 → 07-21) | 19 | **19** |
| …of those, in the first four days | 17 | **17** |
| …predating the EAP | 1 (`superbot`) | **1** |
| …created after the program closed | 6 | **7** |
| …archived (R5 executed 08-23) | 9 | **9** |
| **Pull requests opened, all-time, all repositories** | 8,000 (~09:00Z) | **8,037** *(~18:05Z)* |
| Session cards across 19 repositories | 4,535 | **4,560** *(~18:10Z)* |

Top repositories by PRs opened, today: `superbot` 2,380 · `fleet-manager` 942 ·
`idea-engine` 900 · `superbot-next` 605 · `substrate-kit` 581 · `websites` 518 ·
`sim-lab` 360 · `venture-lab` 289 · `gba-homebrew` 215 · `superbot-games` 186.

**The pack's honest nulls carry forward unchanged and must travel with the
figures:** the ~15 peak parallel Projects is screenshot-supported, not
machine-counted · PR counts are `state=all` — **opened, not merged** · **no
count of PRs opened *during* the fortnight exists**, because the Link-header
method counts lifetime PRs, not a date window · 8,037 is a point-in-time reading
of a moving estate and a recipient re-running the command will get a different
number, which is correct behaviour · **volume is not quality**, and the estate's
own audit is the reason to say so out loud.

**Cross-check, `MEASURED` 2026-08-24:** the same seven counts taken through
`GET /search/issues` agree to the unit (see N6). The § 5 figures therefore rest
on **two independent endpoints**, not one method's word.

**Truncation control re-run today:** the largest `.sessions/` listing is
`superbot` at **970** entries against the Contents API's 1,000-entry cap. Not
truncated, and **30 entries from being so** — a future re-measurement returning
exactly 1,000 must be read as truncation, not as a count.

## 6 · What this file does NOT establish

- **Why the 07-08 and 07-12 mails are absent.** Recorded as an absence with a
  positive control; no cause investigated, none should be inferred (§ 1).
- **Whether [`../anthropic-email-pack.md`](../anthropic-email-pack.md) was ever
  sent.** Unresolved, and § 1 is precisely why mailbox absence cannot settle it.
- **Whether the vendor ever replied on a non-mail surface.** Not knowable from
  Gmail; not investigated — carried forward unchanged from the correspondence
  record.
- **Any claim about agent code quality.** The measured failures are about
  records, retrieval and verification. That restraint is the mail's credibility,
  and dropping it would cost more than the extra claim is worth.
