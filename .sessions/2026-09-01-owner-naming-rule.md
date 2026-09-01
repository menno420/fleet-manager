# 2026-09-01 — the owner's naming rule, and the folder scheme he already has

> **Status:** `in-progress` — born red; flips last.

- **📊 Model:** withheld · high · docs-only
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_013ME1H7CPbqA1FBxJ61VPC2](https://claude.ai/code/session_013ME1H7CPbqA1FBxJ61VPC2) · "Owner-directed documents review"

💡 Session idea: when the owner proposes a structure, check whether the estate
already adopted it before designing it. `docs/repos/<name>/` with fixed
filenames was adopted 2026-08-08 and is **3-of-10 populated**. The rebuild's
real work is filling a scheme, not choosing one.

## Mission

The owner, live: *"create more folders and shorter but more specific files…
the filename tells you exactly what the file contains. And the folder name
should tell you exactly which types of files are there. And I want to make sure
that whenever an agent opens a file, it reads it whole."*

Capture it against evidence before it exists only in chat — he pauses every AI
subscription for about a week from ~2026-09-10.

**Fifth PR this session** (D-0024 asks one, extras with a stated reason). The
reason: this is new owner design intent for the successor, and chat is the one
surface that does not survive his offline week.

## Previous-session review

fm #997 (sections + convention) · #998 (filename claims) · #999 (the misread
measurement) · #1000 (that page's own overstatement). This card continues the
same thread and adds the first measurement that **redirects** the rebuild
rather than describing a failure.

## Shipped

- `owner/intent-workbooks/successor/naming-and-file-size.md` — his rule quoted,
  scored against this session's three misses (**it catches 2 of 3; my
  line-length lint caught 1**), plus the population measurement and one
  argued refinement.
- `owner/intent-workbooks/successor/README.md` · `owner/intent-workbooks.md`
  (72 → 73, cross-checked against the generator).

## The measurements

- `docs/repos/` — the folder-per-repo scheme with fixed filenames
  (`README.md`, `intent.md`, `capabilities.md`, `records.md`,
  `working-here.md`), adopted 2026-08-08: **10 of 28** repositories have a
  folder; **3 of 10** have anything beyond `README.md`; **1 of 10**
  (`spider-swing`) has the full set.
- `docs/repos/superbot-next/README.md` states its depth files are *"not yet
  written"* in its own header — which is why the hook's one-line summary was
  all that stood between me and the misread it caused.

## A correction this card carries

I told the owner `spider-bot` was "the clean repo that did ship" as an option
for his superbot rebuild. **Wrong, and found by opening the file I had been
citing through a hook summary.** `docs/repos/spider-bot/README.md`: Spider Bot
is the **Slingy Spider** Discord community bot, a different-purpose repo — not
a superbot rebuild. `superbot-next` is the only prior, and
`docs/repos/superbot-next/README.md` states golden-parity green *"must not be
read as ported."* Fifth instance of reading a summary instead of the source.

## Verification

(filled at close)
