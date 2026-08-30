# Tree-only cold read — fleet-manager

> **Status:** `audit` · captured 2026-08-30 · reader: ChatGPT Work
>
> This is the first test here that measured the **tree itself**: folder and file
> names only, with no document opened. The observation was frozen before the
> repository reading began.

## Question

Can a cold reader infer four facts from names alone: what this repository is
for, what era it is in, what is being worked on, and what happens next? Can the
same reader place three invented documents without opening a guide?

## Method

- Timestamp: `2026-08-30T12:51:36Z`.
- Pinned tree: `main` at `45076b1`.
- Input: recursive paths only. No file content, commit message, PR text, or
  repository description was shown.
- The reader wrote its interpretation and three placements before opening any
  document.
- Afterward the reader followed README's complete numbered six-read route, then
  read the fresh-start redirect, the latest eleven decision entries, both earlier cold
  reads, `.claude/CLAUDE.md`, the three newest session cards, and the deeper
  sources they routed to.

This follows the controlled shape of the 2026-08-22 boot-trim read—frozen input,
explicit questions, recorded absence—but changes the tested object from a
document bundle to a tree.

## Frozen first impression

The reader inferred that fleet-manager was an estate control hub: a router and
records home for many repositories, owner intent and decisions, shared checks,
prompts, environments, and operating tools. It appeared mature but overgrown,
built rapidly through July and August 2026 and entering a redesign or migration
era. The reader believed the current work was to settle a replacement hub's
structure and migration rules, then prepare a controlled cutover. It could not
tell from the tree whether that direction was already decided, who held current
authority, or the exact next action.

Blind placements:

| Invented document | Cold placement | Confidence |
|---|---|---|
| Dated finding | `docs/findings/2026-08-30-tree-only-cold-read.md` | high |
| Per-repository intent note | `docs/repos/<repository>/intent.md` | high |
| One-off owner checklist | `owner/2026-08-30-<topic>-checklist.md` | medium |

The third placement was an inference: `owner/` did not exist on the pinned
`main` tree. It existed only on the live planning branch.

## Score against the later read

| Test | Verdict | Delta |
|---|---|---|
| Purpose | **Pass** | The later read confirms a cross-repository control and records hub. |
| Era | **Partial** | Redesign was visible, but the tree did not establish the settled fresh-start/archive direction. |
| Current work | **Partial** | Structure and migration were correctly inferred; the settled name `estate` and the exact folder-naming sitting were not recoverable. |
| Next step | **Fail** | “Prepare a controlled cutover” is directionally sound but not the plan's immediate next action: choose the role-named folder tree and its contracts. |
| Finding placement | **Pass** | It matches the repository convention. |
| Intent placement | **Pass** | It matches the three existing per-repo intent files. |
| Owner checklist placement | **Fail on the pinned tree** | The guess is correct on the planning branch, but no filename on pinned `main` could prove it. |

Strict score: **3 pass, 2 partial, 2 fail.** On the acceptance test as written,
this tree does **not** pass: broad purpose is discoverable; authoritative live
state and exact next action are not.

## What the delta means

The test exposed two separate properties that should not be combined:

1. **Placement findability:** can a reader choose the right home from names?
2. **Truth accuracy:** can a reader identify the authoritative current fact?

Fleet-manager did reasonably well at the first and poorly at the second. A new
hub needs both. A tidy category tree can still fail if branch state or stale
“current” files disagree.

The ref is also part of the test fixture. On this date, `main` at `45076b1` did
not contain `owner/` or the latest settled answers; the planning branch did.
Scoring an unnamed “current tree” would confuse branch drift with navigation.

## Suggested acceptance test for `estate`

1. Pin one commit SHA and record it before the reader starts.
2. Give only the path list and the five fixed tasks above.
3. Require the reader to name the file it believes is authoritative for each
   answer, even though it cannot open it.
4. Pre-register exact scoring: purpose, era, current work, exact next action,
   and three placements. “Directionally close” is partial, not pass.
5. Score placement and truth accuracy separately.
6. Run at least one owner read and one agent read. The owner is testing whether
   names make sense; the agent is testing whether routing is deterministic.
7. Re-run after cutover at the exact cutover SHA. A test against a planning
   branch is evidence about that branch, not about the new default branch.

## Position for the owner

**How I see it:** the recent repairs improved the front door, but the strict
tree-only promise is not yet met. The tree tells a good story and an incomplete
instruction.

**What I suggest:** keep the acceptance test, tighten it as above, and require
an exact-next-step route in the root filenames rather than relying on a reader
to discover the newest dated plan.

**Guiding question:** when the owner opens the new hub after a month away, which
single filename should he trust for “what is true now and what needs me next”?
