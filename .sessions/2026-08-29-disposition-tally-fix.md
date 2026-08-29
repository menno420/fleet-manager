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

## Guard recipe (deferred) — and the defect found by testing it by hand

**The obvious recipe does not work, and finding that out is half the value.**
"Count `` `[conceded]` `` / `` `[partial]` `` / `` `[survived]` `` tokens in the
card's round tables and compare to the banner" was the first draft. Run against
the two merged cards it reports **10 conceded** where the truth is 19 — because
**9 of the 20 round-table rows carry no token at all**: both round-2 tables put
the disposition in the section heading ("*6 findings, all `[conceded]`*") and
omit the per-row column. A hook shipping that predicate would fire a *false*
mismatch on every card written that way, which is the worst possible failure for
an advisory checker: it teaches sessions to ignore it.

So the recipe is **two predicates, in order**, and the first is the one that
makes the second possible:

1. **Grammar** — every numbered row in a `## Codex round N` table carries
   exactly one disposition token. Fires on a row without one. This is what makes
   the tally countable; without it nothing downstream is well-defined.
2. **Tally** — sum the tokens and compare to any `N [conceded]`-shaped claim in
   the Status banner or a round heading. Fires on mismatch.

**This PR makes both cards satisfy predicate 1** — the nine untokenised rows now
carry an explicit `` `[conceded]` `` and their tables gained the column — so the
recipe ships with a working fixture rather than a hypothesis. `MEASURED` after
the change: fm #973 counts (13, 0, 0) from rows alone, fm #976 counts (6, 1, 0),
zero untokenised rows, and every table is well-formed (header, separator and
every row at 5 pipes).

Anchors: the Status-badge parse already exists (`check_log` / `missing_markers`
in `bootstrap.py`); the disposition vocabulary is fixed by
`docs/conventions/adversarial-review.md`. Advisory lane only — a card with no
round table must stay silent, and an honest `[partial]` must never red.

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

## Verify

```
python3 bootstrap.py check --strict
```
