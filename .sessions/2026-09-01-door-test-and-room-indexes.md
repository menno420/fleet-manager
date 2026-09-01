# 2026-09-01 — the door test, and two rooms that could not describe themselves

> **Status:** `complete` — both room descriptions and the door test are
> pushed, fm #1003 is open and ready, and the strict check ran with its real
> exit code read; its only blocking finding was this card's born-red hold.

- **📊 Model:** withheld · high · docs-only
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_013ME1H7CPbqA1FBxJ61VPC2](https://claude.ai/code/session_013ME1H7CPbqA1FBxJ61VPC2) · "Owner-directed documents review"

💡 Session idea: when the owner offers an analogy, **run it as a test instead
of agreeing with it.** His doors analogy, walked literally against this repo,
found three distinct defects at three levels in four steps — none of which
agreeing with him would have surfaced.

## Mission

Two authorized items plus the question he actually asked.

1. **Authorized:** `docs/README.md` and `owner/intent-workbooks/README.md` —
   the two live directories measured this session as having no room
   description. GitHub renders a folder's `README.md` on open; without one,
   `docs/` presents ~79 sorted names and no orientation.
2. **His question:** *"Do you think my analogy is correct?"* Answer it by
   walking the tree as doors, not by assenting.

## Previous-session review

fm #997 sections · #998 filename claims · #999 the misread measurement · #1000
that page's own overstatement · #1001 the naming rule · #1002 its nested shape.
The through-line: **six corrections, all the same class — a label read as
substance.** This card's door walk is that class stated as a property of the
tree rather than of the reader.

## Shipped

- `docs/README.md` — 15 doors, each described by **that folder's own first
  line**, quoted rather than summarised, so the page cannot drift from what the
  folder says it is. States the 64-loose-files defect rather than hiding it.
- `owner/intent-workbooks/README.md` — the collection's room description.
- `owner/intent-workbooks/successor/the-door-test.md` — the analogy as a
  repeatable acceptance test, with its first run recorded.
- `owner/intent-workbooks.md` — count 72 → 74.

## The walk — measured, four doors

| Level | Seen | Defect |
|---|---|---|
| root | 10 doors | 3 are dead rooms with live names: `control/`, `projects/`, `telemetry/` are seat-era history per `.claude/CLAUDE.md` |
| `docs/` | 15 doors + **64 loose files** | the floor must be checked before the doors can be trusted |
| `docs/repos/` | 10 repo doors + 2 files | clean |
| `docs/repos/spider-swing/` | 5 files named by **type** | **no door says "current"** — the thing sought is not a door |

The leaf defect is the one his `goals/{current,future,historical,superseded}`
scheme fixes outright.

## The amendment worth recording

He wrote that the analogy would work differently for an agent, *"since you can
probably see the whole structure at once."* It binds **harder**, not softer:
`ls` yields door *names* only, exactly as for him — and where a human opens a
wrong door, sees an unfamiliar room and backs out, this session opened wrong
doors and confidently described them, three times today.

## Verification

- `python3 bootstrap.py check --strict` → **exit 1, read directly, not after a
  pipe**. Sole blocking finding: this card's designed born-red hold.
- **Every door description in `docs/README.md` was taken from that folder's own
  `head -1`, not written here.** All 15 subdirectories were enumerated and each
  one's README opened for its title line; none was described from its name.
  That is the precise failure this session made six times, so the page that
  fixes it must not commit it.
- **The proposal this replaces was tested and rejected on evidence.** I had
  proposed building `docs/README.md` from `MAP.md`'s content, having never
  opened `MAP.md`. Opening it shows it is the **repo-wide** router — its rows
  cover `.claude/`, `.sessions/`, `.github/`, `scripts/`, `tools/`,
  `bootstrap.py`, `../` and root-level files — so copying it into `docs/` would
  have put root-level areas behind a `docs/` path and created the second source
  of truth `intent.md` § 5 names as a non-goal.
- Live-API confirmation of the gap before fixing it: GitHub's per-directory
  readme endpoint returned `Not Found` for `docs` and `owner/intent-workbooks`,
  and `README.md` for `docs/repos` and `owner`.
- Count corrected 72 → 74 in `owner/intent-workbooks.md`, cross-checked against
  `tools/gen_workbook_progress.py` rather than hand-counted.
- New worksheet at **54 lines**, exactly the collection's stated norm.

## What this does NOT establish

The walk is one question against one repo. It shows three defects exist; it
does not measure how often a walker hits them, and `docs/repos/` walked clean.
`REASONED`, not measured: that the leaf-level defect is the costliest of the
three. Nobody has walked the proposed layout, so the comparison stays a
counterfactual.

No Codex round, per the owner's 2026-08-29 cadence correction.

Capability delta: null. Owner ask: null — three questions live in the door-test
worksheet.
