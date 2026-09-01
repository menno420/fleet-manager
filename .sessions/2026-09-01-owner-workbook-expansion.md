# 2026-09-01 — owner workbook expansion for the offline writing week

> **Status:** `in-progress` — born red. Flips to `complete` only after the
> branch is pushed, the PR is open and ready, and the strict check has been run
> with its real exit code read.

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

(filled at close)

## Verification

(filled at close)
