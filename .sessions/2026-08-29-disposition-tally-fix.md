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

**1 · A flip banner contradicts its own table, two hundred lines apart.**
`2026-08-29-model-slot-grammar.md:4` said *"all 7 `[conceded]`"*. Line 217 of
the same file says *"One `[partial]`, three `[conceded]`"* — finding 1 of round 1
was `[partial]`, because its values were already corrected before the review
landed and only the reproducibility half was new. The true tally is **6
`[conceded]`, 1 `[partial]`, 0 `[survived]`**.

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

## Verify

```
python3 bootstrap.py check --strict
```
