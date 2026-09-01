# 2026-09-01 — owner workbook expansion for the offline writing week

> **Status:** `complete` — the four new sections, the answer convention and the
> generated progress page are pushed; fm #997 is open and ready; the strict
> check ran with its real exit code read and its only blocking finding was this
> card's own born-red hold.

- **📊 Model:** withheld · high · docs-only
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_013ME1H7CPbqA1FBxJ61VPC2](https://claude.ai/code/session_013ME1H7CPbqA1FBxJ61VPC2) · "Owner-directed documents review"

💡 Session idea: a workbook collection the owner fills in **without any agent
present** has a requirement the current one does not meet — the answers must be
machine-findable afterwards without a session having to re-read 74 files by
hand. The answer marker is the feature; the questions are only the prompt.

## Mission

The owner asked for three things in one message:

1. **Review** the new owner-directed documents (`owner/intent-workbooks/`, 47
   worksheets + 4 indexes, landed fm #994), one of which he has now fully
   answered (`estate/why-this-estate-exists.md`, landed fm #995).
2. **Create more of them** — his stated purpose is to have a large amount of
   material to read and write against **next week, with every AI subscription
   paused**, restarting them gradually once the answers are in.
3. **Say what I think of that plan and how to improve it and the files.**

Point 3 is not commentary: the plan has one structural gap (answers written
offline with no agent present are not detectable afterwards) and one sequencing
gap (nothing tells the first session back what to do with a week of answers).
Both are fixable inside this change.

## Previous-session review

- `2026-08-31-owner-intent-workbooks.md` — created the collection; its own
  session idea is that presence is not surfacing, and the generated index had
  to be taught about the nested tree.
- `2026-08-31-first-owner-intent-answer.md` — landed the first answered
  worksheet **verbatim**, and established the rule this session builds on:
  completed workbooks stay owner evidence until an explicit synthesis pass
  promotes them. It also recorded the owner's live correction that a Codex
  review is discretionary, not mandatory, on small owner-document landings.
- `2026-08-31-remove-superbot-combination-inference.md` — most recent on `main`.

## Shipped

**The collection grows from 47 to 71 answerable worksheets** (`MEASURED`
2026-09-01 by `tools/gen_workbook_progress.py`, which enumerates the whole
tree — not a sample).

- `owner/intent-workbooks/you/` (7 + index) — how he works, decides, wants to
  be talked to, what frustrates him, his own vocabulary, time and budget. The
  collection asked 47 questions about repositories and folders and almost none
  about him, which is backwards for a collection whose stated purpose is that
  agents understand how he works.
- `owner/intent-workbooks/agents/` (9 + index) — the working contract: what
  agents may do unasked, when to stop, how to ask, how to report, what "done"
  means, which AI does which work, and what to do when an agent thinks he is
  wrong.
- `owner/intent-workbooks/products/` (4 + index) — the products as products
  rather than as git repositories: the game, money, audience, and the
  deliberately unconstrained one.
- `owner/intent-workbooks/successor/` (4 + index) — the four decisions
  `[D-0025]`'s fresh-hub cutover needs from him and has never asked.
- `owner/intent-workbooks/HOW-TO-ANSWER.md` — one answer marker, matching the
  `(Owner reply <date>: …)` form he already used unprompted, so he changes
  nothing about how he writes.
- `owner/intent-workbooks/PROGRESS.md` + `tools/gen_workbook_progress.py` —
  generated from the worksheets, drift-checked in `scripts/preflight.py`.
- `owner/intent-workbooks/WHEN-I-AM-BACK.md` — the paste-ready prompt for the
  first session after the break.
- `tools/gen_owner_index.py` — a `## Write` section so the nested collection is
  surfaced on `owner/README.md` itself rather than one hop behind its own index
  page. It imports the detector rather than restating it, so there is one
  definition of "the owner has written here".

## The design decision worth recording

The progress page is **generated, never hand-ticked**, and that is load-bearing
rather than stylistic. A hand-kept checklist goes wrong the first time he
answers a page without updating it — and during the offline week he cannot run
the generator to correct it, so the drift would survive the entire period the
page exists to serve. Reading the worksheets themselves cannot disagree with
them.

## Verification

- `python3 bootstrap.py check --strict` → **exit read directly, not after a
  pipe** (TRAP-002). One blocking finding: this card's own designed born-red
  hold. Every other lane exit 0, including the new `workbook progress drift`
  lane. Telemetry committed.
- **Detector positive control on real data** (TRAP-003 — an empty result would
  otherwise prove only that the query ran): it flags exactly
  `estate/why-this-estate-exists.md`, the one worksheet he has answered, and
  none of the other 70.
- **Detector negative control, asserted on every run**: the bare `` `OWNER`: ``
  template tail that every unanswered worksheet ends with must not read as an
  answer. Without that assertion the tool would report the collection complete
  and nobody would notice.
- **Drift check negative-controlled three ways**: clean tree → exit 0; injected
  drift in the generated page → exit 1; a genuine new answer appended to a
  worksheet → count flips 1→2 and the check reds. Tree restored after each.

**No Codex round.** Per the owner's live cadence correction of 2026-08-29 —
reserve Codex for flip-readiness and genuinely important changes rather than
after every push — and the precedent set on the immediately preceding owner
workbook landing, which recorded the same correction. This is additive
owner-facing prose that he will read himself, page by page, during the week it
was written for.

Capability delta: null. Owner ask: null — he asked for these directly, and
`WHEN-I-AM-BACK.md` carries the four questions this change raised rather than
adding an `OQ-` entry for them.
