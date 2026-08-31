# 2026-08-31 — owner intent workbooks moved into Fleet Manager

> **Status:** `in-progress` — place the complete owner intent workbook inside
> Fleet Manager, make it discoverable through the generated owner index, verify
> the repository gates, review the exact PR head, and merge the result.

- **📊 Model:** GPT-5 family · high · docs-only
- **📍 Venue:** other
- **🔗 Session:** unavailable — Codex desktop does not expose a Claude session id

💡 Session idea: a durable owner workbook needs a tested intake route, not only
a sensible folder. If the generated owner index scans direct siblings while the
workbook lives below them, the collection must be surfaced explicitly or it can
be present and still effectively lost.

## Mission

Move the 51-file `estate-owner-workbook` preparation pack from its separate
local staging folder into Fleet Manager's existing owner-facing area. Preserve
the five current workbooks, use the repository's `OWNER` / `DERIVED` provenance
language, teach the generated index to surface the nested collection, and leave
the new material clearly marked as successor preparation rather than current
policy.

The owner explicitly directed this session not to pause until the pull request
is merged. That authorizes the branch publication, ready PR, review loop, merge,
and post-merge verification required by this repository's landing procedure.

## Previous-session review

Read the three newest cards on `main`:

- `2026-08-31-sessionstart-orientation-hook.md` shows why a file's mere presence
  is insufficient: the route that injects or surfaces it is part of the feature.
- `2026-08-30-structure-sketch-consults.md` establishes the successor's
  role-named tree, archive-search exclusion, and the rule that mirrors must not
  double the live search surface.
- `2026-08-30-independent-fresh-start-review.md` created the current five owner
  workbooks and made `owner/README.md` generated rather than hand-maintained.

This work extends that owner-facing surface. It does not create `estate`, move
current truth out of Fleet Manager, or change the agreed cutover boundary.

## What the next session needs to know

The work is intentionally held born-red. The workbook was already validated as
51 Markdown files, 47 answerable worksheets, 28 repository drafts, no file over
58 lines, and no broken internal links. Those checks must be repeated after the
files are adapted and placed under `owner/intent-workbooks/`.

