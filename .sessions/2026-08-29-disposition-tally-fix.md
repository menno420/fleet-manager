# 2026-08-29 — three defects the merged audit cards carry about themselves

> **Status:** `in-progress`

- **📊 Model:** withheld · high · docs-only
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact. The
  sanctioned token and why it is not a wall: [`.sessions/README.md`](README.md).
- **📍 Venue:** cloud-container

💡 Session idea: the flip banner is written last, from memory of the rounds, and
nothing checks it against the disposition table in the same file. Two of the
three defects below are that gap; the third is a string replacement that left
its tail behind.

## Mission

fm #973 and fm #976 merged carrying twenty Codex findings, all dispositioned.
Reviewing my own summary of that afterwards turned up **three claims the merged
cards make about themselves that are wrong**. All three are in the class the
audit those cards deliver is about, which is why they are fixed in a named PR
rather than quietly.

## The three

**1 · A flip banner contradicted its own table — and it was one of THREE
disagreeing tallies in the same file.** In
`2026-08-29-model-slot-grammar.md`, the Status banner said *"all 7
`[conceded]`"*; the round-1 summary said *"One `[partial]`, three
`[conceded]`"*; and the round-1 **heading** said *"4 P2 findings, all
`[conceded]`"*. Finding 1 of round 1 was `[partial]`, because its values had
already been corrected before the review landed and only the reproducibility
half was new. The true tally is **6 `[conceded]`, 1 `[partial]`, 0
`[survived]`**.

**The third one is the finding.** The first draft of this card named the banner,
fixed it, said "corrected" — and never swept the file for siblings, so the
round-1 heading went on asserting *all conceded* through an entire review round
of a PR whose subject is that exact defect. Codex caught it. The sweep is now
run mechanically over every tally-shaped line in both cards; the rows-derived
tallies (13, 0, 0) and (6, 1, 0) agree with every remaining claim.

**No line numbers are cited above, deliberately.** The first draft cited `:4`
and `line 217`; both had already moved, because the edit that fixed the banner
inserted lines into the very file the citation pointed at. A line number in a
document that edits its own target has a shelf life measured in commits — the
quoted strings are stable and greppable, so they are the pointer.

I then repeated the wrong number to the owner as *"twenty findings, twenty
conceded"* across both PRs. It is **19 conceded, 1 partial**. `MEASURED` by
reading both merged cards' round tables.

**Why it happened, precisely:** the banner is composed at flip time from memory
of how the rounds went, and the disposition table it is summarising is in the
same file, unread at that moment. Nothing reconciles them. A `[survived]` or
`[partial]` is exactly the entry a from-memory summary rounds off, because the
memorable shape of a good round is "everything conceded".

**2 · A superseded claim sits in a round-1 table with no marker.**
The same file's round-1 finding-2 disposition ends: *"The one stable figure —
`origin/main` carries 1 trailer across 62 commits, because the repo
squash-merges — is stated as such."* Round 2 established that this was a
**shallow-clone artifact** (`.git/shallow`, 7 grafted roots at 2026-08-23) and
that the squash-merge mechanism was invented to explain it. The correction is in
§ *Codex round 2 on fm #976*, a hundred lines below; a reader landing on the
round-1 table gets the false version with nothing adjacent to warn them.

Struck through in place rather than deleted — the table is the record of what I
claimed at the time, and deleting it would hide the sequence that makes the
round-2 finding legible.

This is **TRAP-008** (a later fix leaves a stale copy behind) in the file that
names TRAP-008 as its own round-2 pattern.

**3 · A string replacement left its tail attached.**
Flipping `2026-08-29-audit-catalogue-export.md`'s status, I replaced the literal
`> **Status:** \`in-progress\`` and the rest of that line — *"— born-red.
Exporting the 284 candidate patterns…"* — survived, so the merged banner reads
*"…and this flip. — born-red. Exporting the 284…"*. Split onto its own
paragraph. Mechanical, no claim harmed; recorded because it is the third
defect the same flip produced and the count is the point.

## What this is evidence for

Three defects, one flip each, in cards whose subject is claims that outrun their
evidence. None was caught by `bootstrap.py check --strict`, which grades the
Status badge's **presence and value** and never reads the prose beside it. The
gate cannot catch defect 1 without parsing a disposition table it has no schema
for — but the estate has been asking for **card grammar enforced by a hook**
(owner, 2026-08-29), and "the flip banner's tally matches the dispositions
counted in the same file" is a concrete, checkable instance of that ask.

## Guard recipe (deferred) — third draft, because the first two did not work

**Two drafts of this recipe have now failed on the corpus they were written for.**
That sequence is the finding; the recipe is just where it happened.

**Draft 1 — "count disposition tokens in the round tables, compare to the
banner."** Reports **10 conceded where the truth is 19**: 9 of the 20 rows carry
no token, because both round-2 tables put the disposition in the section heading
and omit the per-row column. Found by hand-testing before review; Codex found it
independently in the same window.

**Draft 2 — same, after giving every row a token.** Still broken, and this time
by *quotation*. A row that **discusses** a disposition contains the word:
`2026-08-29-disposition-tally-fix.md:139` — a row of this card's own round-1
table — reads `| 3 | A round-1 heading still said "4 P2 findings, all
`[conceded]`" | `[conceded]` | … |`, so a token count sees **two** and the
"exactly one per row" predicate fires on the card proposing it. The banner has
the same problem in the other direction: fm #976's Status block deliberately
retains *"all 7 `[conceded]`"* inside a correction note, so a regex reading the
banner finds the live tally **and** the dead quoted one. Found by Codex.

**Draft 3 — parse structure, never prose.** Both failures are the same mistake:
matching a *token* where the meaning lives in a *position*.

1. **Grammar** — locate the round table by its `| # | finding | disposition |
   fix |` header, and read the **disposition column by index**. Fires when that
   column's cell is not exactly one of the three vocabulary values. Tokens
   anywhere else in the row are prose and are ignored.
2. **Tally** — sum that column, and compare against **one canonical field**, not
   against tally-shaped prose. The field does not exist yet; adding it is part of
   the work (a `⚖ Dispositions:` line beside `📊 Model:`, or a fenced block the
   checker owns). Free-text banners and headings stay human prose and are never
   parsed — which is what makes a deliberately-quoted historical tally safe.

**Anchors** (`.sessions/README.md:7` wants function + file + test target — the
first two drafts named only the first two):

| what | where |
|---|---|
| implement | `tools/check_card_disposition_tally.py`, shaped like `tools/check_doc_routes.py` |
| **test target** | `tools/test_card_disposition_tally.py`, shaped like `tools/test_doc_route_patterns.py` |
| fixtures | the three cards of this session — two clean, and **this card's own row 3 as the known-negative** that draft 2 failed on |
| wire | `scripts/repo_checks.sh` beside `check_doc_routes.py`, which `substrate-gate.yml:152` runs |
| vocabulary | fixed by `docs/conventions/adversarial-review.md` |

Advisory lane only. A card with no round table stays silent; an honest
`[partial]` never reds.

**Do not implement draft 3 without running it against these three cards first.**
Both earlier drafts read as obviously correct and both were wrong on contact
with the corpus — which is the same finding as everything else in this PR, in
the one place where it would have shipped as executable code.

## Previous-session review

Follow-on to fm #973 and fm #976, both merged today. Same session, defects found
while summarising them.

## Codex round 1 on fm #979 — 3 P2 findings, 2 `[conceded]`, 1 `[conceded]`-already-fixed

Reviewed `3d17dc5a`, one commit behind the head at the time.

| # | finding | disposition | fix |
|---|---|---|---|
| 1 | The recipe cannot count tokens the round-2 tables do not have | `[conceded]` | **Independently identical to the finding I reached in `a228db4d`, testing the recipe by hand.** The two ran *concurrently*, not sequentially — see the timeline below. The recipe is now two ordered predicates and both cards satisfy the first. |
| 2 | The card's line citations had already moved | `[conceded]` | `:4` and `line 217` were stale — the edit that fixed the banner inserted lines into the file the citation pointed at. **All line numbers removed** in favour of the quoted strings, which are stable and greppable. |
| 3 | A round-1 *heading* still said "4 P2 findings, all `[conceded]`" | `[conceded]` | The third disagreeing tally in that file. I fixed the banner Codex's earlier round named, wrote "corrected", and never swept for siblings — so the heading asserted *all conceded* through a full review round of the PR whose entire subject is that defect. |

### Finding 3 is the session's shape in one line

Fix the instance you were told about; do not sweep for its siblings; report it
corrected. That is the same move as counting the bolded cards and reporting the
population, and as measuring one clone and reporting the repository.

The sweep is now mechanical rather than remembered — every tally-shaped line in
both cards, checked against the rows-derived count:

| card | rows-derived | remaining tally claims | all consistent |
|---|---|---|---|
| fm #973 | (13, 0, 0) | 3 | yes |
| fm #976 | (6, 1, 0) | 2 (one deliberately quoting the old wrong text) | yes |

**Finding 1 is the more interesting data point — and I got its timeline wrong
first.** I wrote that I had found it "twenty minutes earlier". `MEASURED` from
commit timestamps and the review summary:

| event | time (UTC) |
|---|---|
| `3d17dc5a` — PR opened, review requested | 20:28:59 |
| Codex begins reviewing `3d17dc5a` | 20:29:54 |
| `a228db4d` — my hand-test lands the same fix | **20:32:02** |
| Codex completes, reporting the defect | 20:33:22 |

So the two overlapped by **2 min 08 s**: Codex was already reading the commit
when I pushed the fix, and finished 80 seconds after. Not twenty minutes, and
not sequential — genuinely concurrent, which is a *stronger* form of
independence than the version I invented, since neither could have seen the
other's result.

That still makes it the first convergence of the day: everywhere else the review
found what I had not looked for. It is weak evidence that the recipe defect was
real and obvious rather than a reviewer artefact — worth something given how
much of today's output rests on one reviewer's judgement.

**And the interval itself is a fifth instance of the pattern.** "Twenty minutes"
was not measured; it was a plausible-feeling number attached to a real event,
which is exactly the shallow-clone squash-merge failure in miniature. I put it
in this card and in a public comment before checking two timestamps.

## Codex round 2 on fm #979 — 5 findings (4×P2, 1×P3), all `[conceded]`

Reviewed `c48b2bff`. **Two of the five I had already fixed independently in
`935f5c90`, minutes before the review landed** — the invented twenty-minute
interval and the `fm #978` reference — both caught by re-deriving my own
disposition comment rather than by review. They are recorded as conceded because
they were real, not because the review found them first.

| # | finding | disposition | fix |
|---|---|---|---|
| 1 | The twenty-minute separation contradicts the commit timestamps | `[conceded]` | Already fixed in `935f5c90`. Measured: a 2 min 08 s **overlap**, not a separation. |
| 2 | **The grammar predicate cannot tell a quoted disposition from a live one** | `[conceded]` | The substantive one — see below. |
| 3 | The correction note attributes the repair to fm #978 | `[conceded]` | Already fixed in `935f5c90`; the PR is #979. |
| 4 (P3) | The recipe names no test target, which `.sessions/README.md:7` requires | `[conceded]` | The first two drafts named function and file and stopped. Draft 3 carries an anchors table with the test module, its shape-model, the fixtures and the wiring line. |
| 5 | The post-review coverage sentences became false when this PR edited the cards | `[conceded]` | Both Status blocks said only the round-2 fixes and the flip follow the last reviewed SHA. fm #979 then added more. Both now name what came after and say it carries its own review round. |

### Finding 2 killed the second draft of the recipe

**A row that *discusses* a disposition contains the word.** This card's own
round-1 row 3 reads `| 3 | A round-1 heading still said "4 P2 findings, all
`[conceded]`" | `[conceded]` | … |` — two tokens, so "exactly one per row" fires
on the card proposing it. The banner fails the same way in reverse: fm #976's
Status deliberately retains *"all 7 `[conceded]`"* inside a correction note, so a
regex reading the banner finds the live tally and the dead quoted one.

So **two drafts, both obviously correct on inspection, both wrong on contact with
the corpus.** Draft 1 counted tokens the cards did not have; draft 2 counted
tokens that were quotations. Both are the same mistake: **matching a token where
the meaning lives in a position.**

Draft 3 parses the disposition **column by index** and compares against one
canonical field rather than any tally-shaped prose. `MEASURED` against all three
cards of this session, including the row that broke draft 2 as a known-negative:
(13, 0, 0), (6, 1, 0), (3, 0, 0) — all correct.

### Why this stops here

Round 1 found 3, round 2 found 5 — but 2 of those 5 were already fixed, so the
new-defect count is flat at 3 while severity fell (round 2 carries this PR's
first P3). More to the point, **the two things that were converging are the two
that matter**: the recipe has moved from unimplementable → implementable-but-
wrong → tested against its own known-negative, and the tally is now derivable
from structure rather than from any sentence.

Draft 3 has been **tested, not reviewed** — and the recipe says so in its own
last line: do not implement it without first running it against these three
cards. Given that both earlier drafts read as correct and were not, that
instruction is the load-bearing part of the recipe, not the predicate.

## Verify

```
python3 bootstrap.py check --strict
```
