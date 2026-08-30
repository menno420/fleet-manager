# 2026-08-30 — independent fresh-start structure review

> **Status:** `in-progress` — Claude Code's cross-vendor review arrived after
> the first close. The card is reopened while its provenance correction,
> navigation-policy correction, workbook clarity line, folder-boundary rules,
> and independent-scorer requirement are folded in and re-verified.

- **📊 Model:** gpt-5.6 · high · docs-only
- **📍 Venue:** chatgpt-work
- **🔗 Session:** unavailable — ChatGPT Work does not expose a Claude session id

💡 Session idea: a tree-only orientation test must pin the exact ref whose tree
was shown. `main` and a live planning branch can truthfully present different
eras on the same day; scoring the reader without naming the ref confuses branch
drift with navigation quality.

## Mission

Give the owner an independent second opinion on fleet-manager's whole structure
and the fresh-start redirect. Preserve a timestamped tree-only cold read before
opening documents; score it after the mandatory six-read path; propose a
role-named tree and archive design for the future `estate` hub; add short,
editable owner documents beside the generated index; and draft shared
`AGENTS.md` plus Codex-only `codex.md`. Planning and records only: do not create
`estate`, reorganize fleet-manager, edit generated `owner/README.md`, or touch
the Claude branch/PR directly.

## Previous-session review

Read the three 2026-08-30 cards that form the immediate redirect chain:
`fresh-start-redirect-capture`, `structure-sketch-consults`, and
`fresh-start-structure-sitting`. The first two are complete and show that the
redirect, no-stub precondition, search-pollution protection, and archival
questions were deliberately reviewed. The structure sitting remains
`in-progress` on the branch this work builds from; that is consistent with the
prompt's stated born-red hold and is not repaired here. Its most important
handoff is that the owner settled the name `estate`, approved the generated
owner index, and made the folder-naming pass the next planning sitting.

## What the next session needs to know

- The cold tree was captured from `main` at `45076b1` before any document was
  opened; the planning branch had advanced from the prompt's `6b9582b` to
  `e4447b7` by checkout.
- The strict cold score is 3 pass · 2 partial · 2 fail. Purpose and the finding
  and intent placements passed; exact next action and owner placement on pinned
  `main` failed. Future tests must pin a commit and score placement separately
  from truth accuracy.
- The independent review recommends a role-named live tree, rejects a literal
  same-shaped archive mirror in favour of a frozen role-first archive plus
  generated move manifest, and moves thin seed/cold-test ahead of the full
  operating-apparatus build.
- Five editable owner workbooks now cover folder names, archive shape, migration
  order, 28-repository purpose coverage, and the four currently measurable
  ungroomed ideas. The generated index discovers the siblings automatically.
- `owner/README.md` is generated and must only be refreshed through
  `tools/gen_owner_index.py` if its source inputs require it. The generator was
  extended rather than the index hand-edited.

## Cold-read baseline

Timestamp: `2026-08-30T12:51:36Z`. Evidence source: recursive path listing only
for `main` tree `45076b1`; no document content had been opened.

Initial reading: this is an estate control hub that routes agents, tracks many
repositories, records owner intent and decisions, and supplies shared checks,
prompts, environments, and operating tools. It appears to be a mature but
overgrown system built rapidly from July into August 2026 and now entering a
redesign or migration era. The strongest filename signals were the
fresh-start redirect and structure consult, recent agent-error audits, and the
growing owner-facing surface. I inferred that the active work was to settle a
replacement hub's structure and migration rules, then prepare a controlled
cutover; the tree did not establish that this direction was already decided,
who owned it, or the exact next action.

Blind placements:

- dated finding → `docs/findings/2026-08-30-tree-only-cold-read.md`
- per-repository intent note → `docs/repos/<repository>/intent.md`
- one-off owner checklist → `owner/2026-08-30-<topic>-checklist.md`

The first two felt strongly signposted. The third was only moderately clear
because `owner/` was absent from the `main` tree used for the cold read; it
exists on the planning branch.

## Verification

- [x] Cold-read delta scored against the repository truth
- [x] Owner index regenerated only through its generator
- [x] `python3 bootstrap.py check --strict` read from its real exit code: `1`.
  First run found eight defects in this session's drafts plus the inherited
  hold; all eight were corrected. Second run reported only the inherited
  `fresh-start-structure-sitting` in-progress card, the branch's deliberate
  born-red hold named in the task. It is not repaired here.
- [x] Claude Code review requested on PR #989 before the final card flip. No
  review reply was present at close; the request and six review questions are
  preserved in the PR conversation for that running planning session.
- [x] Remote diff checked after publication. The first connector transfer
  truncated `.substrate/guard-fires.jsonl` and appeared to delete 34,347 lines.
  Its generated telemetry delta is preserved in local commit `e92059e`; the PR
  restores the file to the base branch's exact blob rather than publishing a
  damaged ledger.
- [x] Claude Code review read at PR #989 comment `5469261901`. Disposition:
  F1 provenance quote — conceded; F2 mandatory read ladder — conceded; F3
  workbook clarity — conceded. Its folder-collision and blind-scorer additions
  are also adopted. The confirmed stale-map/index defects remain #988's scope.
- [x] Review fixes rebuilt on merged `main` rather than the superseded planning
  branch. `python3 tools/gen_owner_index.py --check` reports current. A new
  `python3 bootstrap.py check --strict` returned real exit code `1` for this
  card's own `in-progress` born-red hold only: one selected card, no draft defect.
- [ ] Card flipped to `complete` as the deliberate last commit after review fixes
