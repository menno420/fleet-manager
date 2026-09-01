# 2026-09-01 — the owner's nested folder shape, and the two conditions on it

> **Status:** `complete` — pushed, fm #1002 open and ready, strict check run
> with its real exit code read; only blocking finding was this card's own
> born-red hold.

- **📊 Model:** withheld · high · docs-only
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_013ME1H7CPbqA1FBxJ61VPC2](https://claude.ai/code/session_013ME1H7CPbqA1FBxJ61VPC2) · "Owner-directed documents review"

💡 Session idea: when the owner proposes a structure, look for it already
running somewhere in the estate before warning about it from theory. His
state-in-path scheme has a real failure mode **and** a working local
implementation that solves it — `docs/owner-comments/`. The useful reply was
the precedent, not the caution.

## Mission

The owner corrected my reading of his naming rule: **nested**, not sibling —
`superbot/goals/{completed,in-progress,planned}`,
`superbot/problems/{cogs,API,railway}`. Update the captured page to his actual
shape and state the conditions the evidence supports.

**Sixth PR this session** (D-0024 asks one, extras with a stated reason). The
reason: fm #1001 landed his rule in the wrong shape, so the page he reads
during his offline week currently argues against a proposal he did not make.

## Previous-session review

fm #997 sections + convention · #998 filename claims · #999 the misread
measurement · #1000 that page's own overstatement · #1001 the naming rule,
captured as sibling folders. This card fixes #1001's misreading of the shape.

## Shipped

- `owner/intent-workbooks/successor/naming-and-file-size.md` — rewritten to his
  nested shape, with the two conditions and the population census. Held to 53
  lines, inside the collection's 54-line norm.

## The measurements

- **The precedent.** `docs/owner-comments/<repo>/{unconsumed,consumed}/` is
  state-in-path running in production here. `tools/owner_comments.py`
  `consume()` (line 2567) renames the record into `consumed/`, sets
  `state = "consumed"` **inside the JSON as well**, and rewrites the index —
  one diff. `scripts/preflight.py:146` runs `owner_comments.py check` as a gate
  lane, so a record whose folder and contents disagree reds the build.
- **Empty-directory risk is not the failure mode here:** `find docs -type d
  -empty` returns **0 of 70**. The measured risk is thin folders, not empty
  ones — 3 of 10 repo folders hold anything past a README.

## The distinction this card adds

`DERIVED`, from his own two examples: **closed category sets are safe in a
path, open ones are not.** `{completed,in-progress,planned}` is closed and
stays guessable forever. `{cogs,API,railway}` is open — the next subsystem
invents a folder nobody can guess, which defeats the purpose of putting it in
the path. Open sets need an index one level up; closed sets do not.

## Verification

- `python3 bootstrap.py check --strict` → **exit 1, read directly, not after a
  pipe**. Sole blocking finding: this card's designed born-red hold.
- **The precedent was read in source, not assumed from the folder names.**
  `tools/owner_comments.py:2567` `consume()` — the rename, the in-file `state`
  write and the reindex are all in that one method; `scripts/preflight.py:146`
  wires its `check` into the gate. Both cited by line because a claim about a
  mechanism is worth nothing without one.
- Page held to **53 lines**, inside the collection's stated 54-line norm — the
  norm this session had to correct once already.
- Both generated pages `--check` current; no worksheet count change (edit, not
  addition).

## What this does NOT establish

That his nested scheme is *better* than the flat one. It establishes that its
one known failure mode has a working local solution, and that his two examples
differ in a way that changes the answer. Nobody has run a session against the
proposed layout; the comparison remains a counterfactual.

No Codex round, per the owner's 2026-08-29 cadence correction.

Capability delta: null. Owner ask: null — four questions live in the worksheet.
