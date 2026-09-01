# Complete estate and repository intent workbooks

> **Status:** `owner-guidance` — preparation draft for Menno, 2026-08-31.
>
> These pages are not yet policy and are not a second source of truth. They
> make the agents' current interpretation visible so you can correct it before
> the successor `estate` repository is created.

## How I see it

`VERIFIED`: Fleet Manager already had five short workbooks for archive shape,
folder structure, migration order, repository-purpose coverage, and idea
triage. It also had three dedicated per-repository intent drafts. Most
repository purposes and the proposed folder contracts were still only gaps or
questions.

`DERIVED`: keeping the fuller workbook outside Fleet Manager would recreate the
findability failure it is meant to fix. This collection therefore lives here,
inside the existing owner-facing area, until the tested cutover to `estate`.

## What I suggest

`PROPOSED`: open whichever filename interests you. Answer one question,
rewrite a whole page, or leave it alone. There is no required order and “I
don't know yet” is a useful answer.

The pages use four labels:

- `VERIFIED` — checked against the live GitHub account or Fleet Manager's
  current branch on 2026-08-31.
- `DERIVED` — an agent's best reading of your intent, deliberately revisable.
- `PROPOSED` — an agent's design recommendation, not your decision.
- `OWNER` — space for your words.

When an answer becomes settled, an agent should preserve your words, move the
durable result to its one canonical home, and leave a pointer from the workbook
instead of silently turning an old inference into policy.

## Start here

- [`intent-workbooks/HOW-TO-ANSWER.md`](intent-workbooks/HOW-TO-ANSWER.md) —
  two minutes, and the one convention that makes your answers findable
  afterwards. Read it before the first page you answer.
- [`intent-workbooks/PROGRESS.md`](intent-workbooks/PROGRESS.md) — generated:
  which worksheets already carry your words. Never hand-ticked.
- [`intent-workbooks/WHEN-I-AM-BACK.md`](intent-workbooks/WHEN-I-AM-BACK.md) —
  what the first session after your offline week should do with the answers,
  written now rather than improvised then.

## Open the collection

- [`estate/`](intent-workbooks/estate/README.md) — why the whole collection
  exists and how you want it run.
- [`you/`](intent-workbooks/you/README.md) — how you work, decide, and want to
  be talked to. Added 2026-09-01; the collection had 47 questions about the
  estate and almost none about you.
- [`agents/`](intent-workbooks/agents/README.md) — the working contract: what
  agents may do unasked, when to stop, what "done" means, which AI does what.
- [`products/`](intent-workbooks/products/README.md) — the things you are
  building, as products rather than as repositories.
- [`successor/`](intent-workbooks/successor/README.md) — the four decisions the
  fresh-hub cutover needs from you.
- [`folders/`](intent-workbooks/folders/README.md) — one proposed contract for
  every main folder in the successor hub.
- [`repositories/`](intent-workbooks/repositories/README.md) — one prefilled
  intent draft for each of the 28 repositories visible on GitHub.

The collection contains **72 answerable worksheets** (`MEASURED` 2026-09-01 by
`tools/gen_workbook_progress.py`, which enumerates the whole tree) plus the
section indexes and the three pages above. `MEASURED` 2026-09-01: the longest
**unanswered** worksheet is 54 lines and the median is well under 40 — short on
purpose. Answered ones grow, correctly: yours is 67. (The collection previously
claimed "no worksheet is longer than 44 lines"; that was inherited and untrue
the day it was written — two worksheets shipped at 46 and 47.) It remains
successor preparation: current Fleet Manager records still
win until the cutover, and product repositories remain canonical for their own
implementation truth.

## One guiding question

`DERIVED`: which page would be most damaging for an agent to misunderstand
tomorrow?

## Your note

`OWNER`:

