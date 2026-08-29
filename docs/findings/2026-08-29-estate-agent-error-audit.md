# The estate-wide agent-error harvest — OD-24 §6 step 1, extended

> **Status:** `living-ledger` · opened 2026-08-29 · **PARTIAL — §4 pending**
> (the session-card corpus is still in adversarial verification; §§1–3 are
> complete and independently verified).
>
> **What this is:** the drift-incident corpus OD-24 §6 step 1 asked for, taken
> at estate scale. The [genesis dig](2026-08-28-substrate-kit-genesis-dig.md)
> executed step 1 **fleet-manager-side only**, over the August window, and its
> §9 names the remainder as skipped: the eighteen satellite repositories, the
> June/July bulk, and superbot's PR review threads. This is that remainder.
>
> Certainty tags per
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).

## 0 · The corpus

`MEASURED` 2026-08-28/29. Two deliberately independent halves — session cards
are **self-reported**, review comments are **externally caught after the agent
declared the work done**.

| source | volume | span |
|---|---|---|
| Session cards, 20 repositories | **4,583 cards** → 7,214 error-bearing sections → 68 shards | 2026-05-29 → 2026-08-28 |
| PR review comments, 12 repositories | **1,592** (1,431 from the external reviewer) | 2026-06-17 → 2026-08-28 |
| Per-repo instruction surfaces | **20 of 20** censused | at HEAD |

Re-derivable: `census.py` → `fetch.sh` → `extract.py` → `shard.py` →
`reviews.py`, preserved with the harvest in this PR's `.audit-recovery/`.

---

## 1 · The identity collision — the owner has no distinguishable voice on GitHub

**This is the finding with the widest blast radius, and no record in this
estate names it.**

`MEASURED` 2026-08-29, two endpoints, with positive controls:

| population | attributed to `menno420` | agent-authored |
|---|---|---|
| PR **review** comments (12 repos) | **155** | **135 (87 %)** by literal marker; the remaining 20 read identically (judged, not marker-matched) |
| **Issue** comments (6 busiest repos) | **564** | **499** by literal marker · **55** more by agent operational voice · **10 residue, every one read in full** |

**The 10-comment residue is enumerated rather than sampled** — an earlier cut of
this section characterised 65 comments from reading 14, which is TRAP-004 inside
the document whose §3 lists this session's errors. Read in full: five are
`spider-swing` landing reports (*"Phase 0 implementation merged in PR #6 as
`e5ec3c5`"*), two are structured `## Plan addendum` bodies, one opens
**_"Roadmap review decisions from owner:"_** — an agent relaying his decisions
**in the third person, under his account** — and two (a 2026-05-20 triage note, a
2026-06-14 duplicate-supersede) are too short to attribute from text either way.

**Scope, exactly:** of 564, **562 are attributable to agents and 2 are
indeterminate; none is identifiably the owner's first-person voice.** The
sharpest single line in the residue is an agent writing *"Menno also confirmed
the PR #8 Reel and DEBUG controls now work on Android"* — referring to the owner
in the third person from the owner's own account.

**Positive control:** the same marker regex over the 1,437 external-reviewer
comments returns **0** Claude Code footers and **1** disposition token, so the
markers discriminate rather than matching everything.

**Author distribution across those 6 repos:** `menno420` 564 · the reviewer bot
198 · dependabot 35 · code-scanning 1. **There is no separate identity for the
owner anywhere in it.**

The cause is mundane and was never written down: **agents authenticate with
`$GITHUB_PAT`, which is the owner's own credential**, so every comment, review
reply and PR body an agent posts is authored by `menno420`. The estate records
the PAT's *capabilities* in several places
(`docs/execution-surfaces.md`, `docs/providers/claude.md`) and its *attribution
consequence* in none — a grep for any record of agents posting under the owner's
identity returns nothing, against a positive control confirming the grep style
finds PAT records.

**Why it matters more than an attribution nit:**

1. **The `OWNER` certainty tag is unfalsifiable from GitHub.** The legend reads
   *"The owner stated it… Act on it. Do not probe first."* — the estate's
   strongest instruction, and on GitHub nothing distinguishes his statement from
   an agent's paraphrase of one.
2. **It is the mechanism behind a defect already observed independently.** The
   review corpus surfaced *"Inference filed as the owner's words"* (n=5, high)
   and two clean owner-authority fabrications: **OD-6 cited as capping landings
   per session when its text explicitly refuses to**, and **`spider-swing`
   promoted from an agent's own recommendation to a settled roadmap decision**.
   Both landed in artifacts whose job is to brief the next session. TRAP-005's
   mirror image: not failing to believe the owner, but manufacturing him.
3. **It contradicts an assumption the owner-comments apparatus rests on.**
   `docs/owner-comments/` exists to carry the owner's wording durably; its
   records are trusted as his. Nothing in the contract establishes authorship,
   because on the surface it draws from, authorship cannot be established.

**What it does NOT mean:** the owner's *chat* statements are unaffected — those
arrive through a channel agents cannot author. This is specific to GitHub-hosted
text. `REASONED`: the same collision applies to any surface reached with his
credentials (Railway, releases, gists), untested here.

**Consequence for this audit, stated because it cost a claim:** this session
told the owner the 155 comments were "his own voice — the highest-signal source
in the estate," and built a whole workflow lane on it. **Zero of them are.** One
harvest lane refused the premise, measured it, and reported an honest null
rather than filling the field — the correct behaviour, and it is what surfaced
this section.

---

## 2 · The enforcement census — 328 prose-only rules across 20 repositories

`MEASURED` 2026-08-29, one reader lane per repository over its `CLAUDE.md`,
`.claude/`, hooks, settings, checkers and recent cards.

| | |
|---|---|
| Rules stated with **no mechanism** delivering or checking them | **328** |
| Enforcement mechanisms found | **216** — 78 checker · 55 CI · 39 hook · 25 prose-only · 19 none |
| Repositories with kit divergences an upgrade would silently revert | **20 of 20** (2–10 each) |

This is OD-24 §6 step 2's taxonomy filled in with a number: the dominant class
is **stated but undelivered**, exactly as the genesis dig predicted from a much
smaller sample.

The per-repo gaps are concrete, not atmospheric — `superbot-games` and
`superbot-idle` have **no `.claude/` directory at all** while carrying 18–24
stated instructions each; `spider-bot`'s landing path (push to main deploys to
production, CI informational) **defeats every mechanism the repo has**;
`substrate-kit`'s own flagship doctrine is the one thing it ships no mechanism
for. `fleet-manager`'s biggest gap is the moment *before* the first tool call.

**Load-bearing caveat:** each census is one lane's single read, and several
lanes wrote scope caveats into a schema field rather than the body, so the
counts are a **first pass, not a verified inventory**. The 328 should be read as
*"this order of magnitude, per this method"*, not as a countable register.

---

## 3 · Method, and where it under-performed

Two workflows: 68 harvest lanes over the card shards, 12 over the review shards,
20 census lanes, then per-class synthesis and a three-lens adversarial panel
(refute · already-covered · buildable).

**The panel did not discriminate, and that is a finding about the method rather
than about the estate.** On the review corpus it returned **140 survivors from
141 candidates — a 99.3 % pass rate**. A panel that refutes 1 in 141 is not
evidence that 140 patterns are real; it is evidence the bar was set where
nothing fails it. The survival rule (`refuters < 2` of 3 lenses) let a single
dissent be outvoted by two lenses answering *different questions* — only one of
the three was actually asked to refute. **The 140 are candidates. They are not
findings, and this document does not present them as any.**

`REASONED`, for the next pass: make all three lenses refute, from different
angles, and require the refuter to open the cited artifact.

### This session's own errors, recorded as corpus

Four, and three compress to one sentence — **a conclusion drawn from an absence
that the circumstance already explains**:

1. An extraction returned **564** sections instead of 7,214; Python's `glob`
   does not match dot-directories, so `.sessions/` was never scanned.
2. `merge-on-green` written into a published PR comment as *"already passing"*;
   it had no result on that head at all.
3. *"The session volume does not survive a container"* — inferred from no file
   predating the boot, which was the session's **first** container, so nothing
   older could exist. Disproved at 23:48:12Z when the container **was** replaced
   and the 47M corpus and both journals survived intact.
4. *"The census came back empty"* — the task output nests everything under
   `result` and the query read the top level. Caught in the same command by a
   fallback that went to the journal.

The fourth is the same class again and was caught **because a positive control
was built into the query rather than run afterwards** — which is the practical
form of the fix, and cheaper than the trap it prevents.

---

## 4 · The cross-corpus convergence — PENDING

The session-card corpus is still in adversarial verification. The analysis this
section will carry — **which patterns appear in BOTH the self-reported cards and
the externally-caught reviews**, the strongest signal this estate can produce —
is not written yet, and no trap is registered until it is.

**Nothing is proposed to the kit in this revision.** Under the roadmap's §6
promotion rule and the owner's own § 3 freedom doctrine, a review round that
emitted infrastructure before measuring would recreate the wall-accretion he is
correcting.
