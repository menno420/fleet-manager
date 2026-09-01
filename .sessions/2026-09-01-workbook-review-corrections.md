# 2026-09-01 — owner-review corrections to the new workbooks

> **Status:** `complete` — the settled-name page is corrected, the four
> overlapping worksheets are cross-linked, and preflight is green on every lane
> except this card's own born-red hold.

- **📊 Model:** withheld · high · docs-only
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_013ME1H7CPbqA1FBxJ61VPC2](https://claude.ai/code/session_013ME1H7CPbqA1FBxJ61VPC2) · "Owner-directed documents review"

💡 Session idea: the review hook asked what a claim was measured against, and
the answer for three claims was "the file's title". Two of the three were
wrong. **Reading eight filenames is not reading eight files** — and the failure
is invisible from the inside, because a title plus this estate's conventions
produces a confident and entirely plausible sentence.

## Why a second PR (D-0024 exception reason)

fm #997 merged on green before the owner-review round surfaced these defects.
A merged pull request cannot carry the correction, so this lands as its own
change on a branch restarted from `origin/main`.

**And a second defect, in the restart itself, worth its own trap-shaped note.**
The first attempt at that restart ran `git checkout -B <branch> origin/main`
**without fetching first**. `origin/main` was a stale remote-tracking ref
pointing at `23a6b56` — the commit before fm #997's own squash-merge landed as
`fd33e7b`. So the branch was rebuilt on the *pre-merge* main and carried fm
#997's three original unsquashed commits again. GitHub then saw both sides
adding the same 30-odd files by different SHAs and marked fm #998 `dirty`:
5 commits, 39 changed files, for a change that touches 7. The owner spotted it
before the polling loop did — the loop was waiting on check-runs that never
registered, because a conflicted PR does not run them, and it read that as
"checks pending" rather than as a symptom.

**The rule this cost:** after a squash-merge, `git fetch origin <base>` is part
of restarting a branch, not an optimisation. A remote-tracking ref is a cache,
and `checkout -B` from a cache silently resurrects merged history. The tell is
in the PR's own numbers — changed-files far exceeding what the change touches
— and `git merge-base --is-ancestor origin/main HEAD` answers it in one
command. Fixed by rebuilding from the fetched `fd33e7b` and force-pushing;
`git diff --name-only fd33e7b HEAD` now returns exactly the 7 intended files.

## Previous-session review

- `2026-09-01-owner-workbook-expansion.md` — this session's own earlier card,
  landed as fm #997. Its verification section claims the collection was
  extended correctly; this card records the three claims in it that rested on
  filenames rather than files.
- `2026-08-31-first-owner-intent-answer.md` — the rule this correction protects:
  completed workbooks stay verbatim owner evidence until an explicit synthesis
  pass. A worksheet that asks an already-answered question corrupts that from
  the other end, by inviting an answer the record already holds.
- `2026-08-31-owner-intent-workbooks.md` — created the collection whose eight
  estate worksheets this session had read the titles of and not the bodies.

## Mission

Fix three defects in the workbooks added by fm #997, all of the same shape — a
claim resting on a filename rather than on the file.

1. **`successor/what-the-new-hub-is-called.md` asked a question the repository
   already answers.** `MEASURED`: `docs/planning/2026-08-30-fresh-start-redirect.md`
   line 271 records the owner's own words settling the name as `estate`, with
   his rejection of `structure` and the reason; line 424 marks it
   `✅ SETTLED`. The worksheet told him no record said he had chosen it. That
   is precisely the failure `docs/intent.md` § 2 counts against this estate —
   *sessions stop asking things the repo already answers* — committed inside a
   document written to prevent it.
2. **Three new worksheets duplicate questions the existing eight already ask.**
   `MEASURED` by opening the five estate worksheets this session had only read
   the titles of: `how-agents-should-work-with-you.md` Q1 is the annoying-small-
   things question and Q5 is the disagreement question;
   `risk-and-owner-authority.md` Q1 is the spending threshold. During an offline
   week with no agent watching, that means answering the same question twice in
   different files and neither knowing about the other.
3. **"Almost none of the collection is about you" was a title-level claim** over
   eight files, three of which this session had opened. Two of the eight face
   him directly.

## Shipped

- `owner/intent-workbooks/successor/what-the-new-hub-is-called.md` — rewritten
  from an open question to a **settled** record carrying his own quote and the
  reason he rejected `structure`, with the two things genuinely still open
  (does the name still hold a day later; public or private on day one). The
  page keeps a visible note that it was drafted wrong, rather than being
  silently replaced — an unmarked correction teaches the next session nothing.
- `owner/intent-workbooks/successor/README.md` — the row now says settled.
- `you/what-frustrates-you.md`, `agents/when-an-agent-disagrees-with-you.md`,
  `agents/what-agents-may-do-without-asking.md`, `you/time-money-and-limits.md`
  — each carries a short overlap note naming the existing estate worksheet it
  duplicates, so answering either one counts. **The duplication is not removed,
  deliberately:** the wider pages ask the question better, the narrower ones
  are already in his hands, and deleting either would decide for him which
  framing he prefers.

## Verification

- The five estate worksheets this session had only read the *titles* of were
  opened in full. That is what surfaced defects 2 and 3.
- `docs/planning/2026-08-30-fresh-start-redirect.md` read at lines 268–280 and
  424 — the settled name, his verbatim words, and the `✅ SETTLED` ledger row.
  **TRAP-003 positive control run first**: the same grep form was made to find
  `D-0025`, a record known to be present, before any absence was claimed.
- `python3 scripts/preflight.py` → exit 1, and the **only** failing lane is this
  card's designed born-red hold; the previous card's lane now passes. Every
  other lane exit 0, `workbook progress drift` included.

**What this session got wrong, stated plainly:** three claims in a reply to the
owner rested on filenames rather than files, and two of them were false. The
estate's boot file carries the rule verbatim — *do not write about a file you
have not opened* — and it did not bind, because a title plus this estate's
conventions produces a sentence that reads exactly like a checked one. The
review hook caught it; nothing in the gate would have.

Capability delta: null. Owner ask: null.
