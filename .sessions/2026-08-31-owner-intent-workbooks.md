# 2026-08-31 — owner intent workbooks moved into Fleet Manager

> **Status:** `complete` — the complete owner intent workbook is inside Fleet
> Manager, surfaced by the generated owner index, verified, and reviewed on the
> exact pre-flip head with no findings. PR #994 is eligible to merge.

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

The work began intentionally held born-red. The workbook was already validated as
51 Markdown files, 47 answerable worksheets, 28 repository drafts, no file over
58 lines, and no broken internal links. Those checks were repeated after the
files were adapted and placed under `owner/intent-workbooks/`.

## Shipped

- `owner/intent-workbooks.md` — the direct owner-facing entry point, discovered
  automatically by the generated `owner/README.md`.
- `owner/intent-workbooks/` — 47 short answerable worksheets plus three nested
  indexes: eight estate-wide intent pages, eleven successor-folder contracts,
  and one prefilled intent draft for every live GitHub repository.
- `owner/README.md` — regenerated through `tools/gen_owner_index.py`; the
  collection appears as the sixth short workbook without hand-maintaining the
  generated page.
- Local cleanup — at the owner's request, the earlier 51-file staging copy at
  `C:\dev\estate-owner-workbook` was sent to the Windows Recycle Bin. It never
  existed in OneDrive. Fleet Manager is now the only active copy.

All agent interpretations use `DERIVED`, recommendations use `PROPOSED`, and
owner answer areas remain blank `OWNER` fields. The collection is explicitly
successor preparation; it does not override Fleet Manager's current records or
product-repository truth.

## Verification

- Collection count: 51 Markdown files.
- Worksheet shape: 47 of 47 carry `Questions for you` and an `OWNER` answer
  field; maximum worksheet length is 44 lines.
- Repository coverage: live GitHub list 28, repository drafts 28, exact match.
- Relative-link scan: every Markdown link in the collection resolves.
- Provenance scan: zero `INFERRED` labels remain after alignment with the
  repository's `OWNER` / `DERIVED` contract.
- `python tools/gen_owner_index.py --check` → current.
- `python bootstrap.py check --strict` → real exit 1 before the flip, with one
  finding only: this card's designed born-red `in-progress` hold. Nine
  guard-fire writes were reported by the command; the resulting telemetry
  ledger delta is committed with the session.

## Review and landing

Codex review completed on exact head `59145f9e242df948d140fcb9c0a5ed52f4d0cb2d`
with no major issues and zero inline comments. This final commit changes only
the session card's status and close-out text, so it takes the documented flip
exemption: no reviewable workbook content follows the reviewed SHA.

Layer-2 handoff: null (Fleet Manager itself; no satellite repository attached).

Capability delta: null. Owner ask: null. The owner's live instruction to carry
the PR through merge is fulfilled by this session's landing sequence.
