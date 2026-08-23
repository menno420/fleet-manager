# The EAP evidence pack — what the projects created, measured 2026-08-23

> **Status:** `reference` · measured for program step **E1** (the final EAP
> review mail). Certainty tags per
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).
>
> **What this is:** the numbers the mail can cite, each with the command that
> produced it, measured on 2026-08-23 — not recalled from July. Owner directive,
> live: *"only after we have properly looked at everything the projects created
> and have a good batch of information to send them with."*
>
> **What this is NOT:** a draft of the mail. E1 is **owner-reserved** by his own
> ruling (`OQ-E1-FINAL-EAP-EMAIL`) — no session drafts, sends or restarts it.
> This is the evidence he writes *from*. The structure follows the six net-new
> sections named in
> [`../owner-reflection-2026-07-21.md`](../owner-reflection-2026-07-21.md)
> § "The vendor final-review email", so a section here maps to a section there.

## 0 · Read this first — the method, because the obvious one is wrong

`MEASURED` 2026-08-23. **Do not measure this account with `search/issues` or
`search/code`.** The search index covers a minority of these repositories, and an
unindexed repository returns **0**, which is indistinguishable from a genuine
zero ([TRAP-003](../traps.md)).

- First sweep, via `search/issues`: **2,783** PRs all-time. **False.**
  `superbot` returned 0 with a newest PR of **#2450**.
- R5 measured the same defect for `search/code`: **7 of 26** repositories indexed
  (fm #912/#913).

**The method that works, with its positive control built in:**

```bash
# per repo: count PRs by the Link header's rel="last" page number
curl -sSD - -o /dev/null --noproxy '*' \
  -H "Authorization: Bearer $GITHUB_PAT" \
  "https://api.github.com/repos/menno420/<repo>/pulls?state=all&per_page=1"
```

Controls: `superbot` → **2,378** against a max PR number of 2,450 (the gap is
issues sharing the numbering) · `websites` → **512**, which is the PR opened the
same hour. Both reproduce, so the method sees what the index cannot.

## 1 · The scale, and the shape of it

`MEASURED` 2026-08-23, all 26 repositories, method above.

| figure | value |
|---|---|
| Repositories in the account | **26** |
| **Pull requests opened, all-time, all repositories** | **8,000** |
| Repositories created **inside** the EAP window (2026-07-07 → 07-21) | **19 of 26** |
| …of which created in the five days 07-07 → 07-13 | **17** |
| Repositories predating the EAP | **1** (`superbot`, 2025-08-10, 2,378 PRs) |
| Repositories created after the program closed | **6** |
| PRs in EAP-created repositories | **5,368** |

**The one-sentence version, and it is the mail's opening fact:** one person, not
a coder, went from a single repository to **nineteen new ones in a fortnight**
and **8,000 pull requests**, then spent the next month finding out how much of it
he could actually verify.

Top repositories by PRs opened: `superbot` 2,378 · `fleet-manager` 918 ·
`idea-engine` 900 · `superbot-next` 605 · `substrate-kit` 581 · `websites` 512 ·
`sim-lab` 359 · `venture-lab` 289 · `gba-homebrew` 215.

## 2 · The consolidation number — now closed, not intended

This is the section his reflection names as *"the consolidation number… puts a
hard figure on the oversight gap."* Until 2026-08-23 it could only be stated as a
plan. It is now executed.

| stage | figure | source |
|---|---|---|
| Peak parallel Projects | **~15** | screenshot-supported, *not* machine-counted — the `~` is deliberate |
| Consolidated to | **8 seats** | decided 2026-07-11, canonicalised 2026-07-12T03:15Z (commit-verified) |
| Program closed | **2026-07-21** | seats terminated; OD-5 |
| Repositories reviewed for disposition | **26** | [the disposition table](../planning/2026-08-22-repo-dispositions.md), fm #906 |
| Verdict | **keep 14 · archive 12 · delete 0** | 13 of 14 keeps are *reworks* |
| **Executed 2026-08-23** | **9 archived, 0 deleted** | R5, fm #912 — confirmed by fresh `GET /user/repos`, not by the API's 200 |
| Still gated | **3** | `superbot-next` + `superbot-plugin-hello` on GCB-1; `product-forge` on R2 |

**The honest framing:** he did not archive nine repositories because they failed.
He archived them because **he could not review them**, and unreviewed shipping
volume is not finished work. That is the same thesis the mail opens on, with a
number under it.

## 3 · "What I had to build myself" — the teardown, measured

His reflection calls this *"unique, roadmap-grade, and nobody else can give it."*
It is also the section the [review site](https://menno420.github.io/websites/)
makes demonstrable rather than asserted.

| what he had to build | measured today |
|---|---|
| **Session cards** — durable per-session memory | **4,550 across 19 repositories** (`superbot` 970 · `idea-engine` 504 · `fleet-manager` 393 · `substrate-kit` 342 · `superbot-next` 335) |
| **Moment-of-action injection** — rules that arrive when they apply | **59 doc-routes** in one repo's `PreToolUse`/`UserPromptSubmit` hook |
| **Lifecycle hooks** | **6** in fleet-manager alone |
| **Executable procedures** (skills) | **27** |
| **Repo-side checkers/generators** | **30** |
| **A trap register with deterministic checkers** | **5 traps**, 1 with a checker in the required gate — built 2026-08-23 |
| **Dated findings** (the estate's own research) | **52** in fleet-manager |

**Why this is roadmap-grade rather than a brag:** every item is a product gap he
paid for in his own time. The session card exists because sessions forgot. The
routes exist because **116 committed statements of one rule across 66 files
caught 0 of 16 incidents** ([the measurement](2026-08-08-why-rules-dont-bind.md))
— a rule binds only if it *arrives* at the moment of action. The born-red card
exists because auto-merge landed a partial PR. Each is a feature the platform
did not have.

## 4 · The verification wall — the thesis, with evidence under it

The mail's spine, his words: *"I scaled it until I found the wall; the wall is
human review, not agent capability."* What the estate can now put under it:

- **116 statements → 0 catches / 16 incidents.** Documentation recalled at the
  right moment caught **zero**; the catchers were the owner (5), the Stop hook
  (4), gate/CI (3), tests (2), after-the-fact (2).
  [Source](2026-08-08-why-rules-dont-bind.md).
- **A full-read audit of one repository found 101 defects** — every tracked file,
  not a sample ([the audit](../audits/2026-08-10-full-read/README.md)). 98 closed.
  The defect class was *not* bad code: it was **an appended correction failing to
  retract what it corrected**, so every document stayed internally coherent and
  review passed over it.
- **The public review site described a terminated program as running.** Measured
  2026-08-23: **0 of 7 live pages** said the program had ended, and `/fleet/`
  rendered *"15 live lanes"* with mirrored heartbeats — 33 days after the seats
  were terminated (websites #512 fixes it). **Nobody noticed for a month**, which
  is the thesis in one artifact: the drift was on his most visible surface.

## 5 · Economics

`MEASURED` and owner-executed: the Railway estate audit attributed a **€30**
bill, ended a crawler DoS, took the estate to **3 projects / 8 services**,
retired the pollers, and sized the bot database — where **97.5 %** of 949 MB
turned out to be accumulated BTD6 ingestion history against ~10 MB of actual user
data ([audit](2026-08-14-railway-websites-audit.md) § 8).

**The transferable point for the mail:** none of that cost was visible to the
agents that created it. Cost is not an agent-legible signal, so it accumulates
exactly where nobody looks — the same shape as the quality drift.

## 6 · Capability evaluations owed, and the standing offer

- **The capability-evaluation debt** he acknowledged mid-program is still the
  freshest unpaid content; the source list is
  [the E1 plan](../planning/2026-07-26-final-eap-email-plan.md) § 3.
- **The unsent 2026-07-18 follow-up** holds four findings never delivered: the
  venue-scoped guard, agent-memory wall propagation + the CI antidote,
  stale-text-outranks-live-instruction, and the trigger-tool forced-approval
  finding. `superbot docs/eap/2026-07-18-followup-email-draft.md`.
- **Four direct questions were asked and none answered**; two verbatim promises
  of a final review are on the record, and **no vendor agenda ever arrived** — so
  the content is entirely his call
  ([correspondence record](2026-08-09-eap-correspondence-record.md)).
- **The standing offer** has more behind it than in July: 26 repositories, 8,000
  PRs and 4,550 session cards is an unusually good structured-probe harness.

## 7 · Honest nulls — what this pack does NOT establish

- **The ~15 peak is screenshot-supported, not machine-counted.** Do not harden it.
- **8,000 PRs is a volume figure, not a quality figure**, and the estate's own
  audit is the reason to say so out loud. Roughly 60 of `superbot`'s recent PRs
  were an automated dashboard-refresh loop (retired 2026-08-14) — volume counts
  include machine churn.
- **PR counts are `state=all`** — opened, not merged. Merged counts were not
  re-derived by the reliable method; the search-derived merge figures are
  unusable for the reason in § 0.
- **No claim here is made about agent code quality.** The measured failures are
  about *records, retrieval and verification*, which is the mail's actual point.
- **Session-card counts are per-repository directory listings**, so a repo that
  archives older cards elsewhere reads low. `fleet-manager` 393 is current-window
  only.
