# Independent second opinion — the `estate` structure and fresh-start plan

> **Status:** `plan` · independent review · ChatGPT Work · 2026-08-30
>
> This is an independent read, not an amendment to the decided direction. It
> accepts the fresh `estate` hub, absolute write cutover, link rewriting before
> moves, human archive judgment, session-card clock, and non-blocking idea cap.
> Where it disagrees, it says so once and leaves the decision with the owner.

## Bottom line

The fresh start is the right decision. Fleet-manager contains useful truth, but
its live state, history, operating machinery, experiments, and owner material
have grown into one crowded namespace. Reorganizing it in place would preserve
neither citations nor confidence.

My two changes to the working plan are:

1. Do **not** build a literal same-shaped archive mirror. Freeze archived files
   under their original role and record every move in a generated manifest.
2. Do **not** finish the whole new operating apparatus before any real material
   enters the new tree. Build the minimum safety gates at birth, seed a thin
   truthful hub, cold-test it, cut over, then promote deeper mechanisms from
   measured use.

## 1 · My read of fleet-manager's present structure

Measured on the planning branch: 25 top-level entries; 79 immediate entries
inside `docs/` (64 files and 15 folders); 454 session cards; 28 repositories
enumerated by the owner-comments checker; 10 Layer-2 repository folders; and
three dedicated per-repository intent files. `owner/` had one generated index
and no editable sibling before this review.

The strong parts should survive the move:

- the numbered read route makes deliberate orientation possible;
- the decision register preserves provenance instead of rewriting history;
- generated indexes are better than hand-maintained attention summaries;
- dated evidence usually states method, certainty, and what it could not prove;
- the born-red session card makes unfinished work visible;
- the per-repository intent shape asks the right human questions.

The structural problem is that those good systems compensate for a tree whose
top-level roles are not stable. Current state, old state, plans, findings,
prompts, owner material, operating code, and seat-era history all meet under
`docs/`. A reader can follow a prescribed route, but cannot reliably orient from
names alone. The cold read proves the difference.

**How I see it:** this is not a bad repository. It is a successful records
system that accumulated several eras without retiring their front doors.

**What I suggest:** preserve the provenance, generators, gates, and intent
shape; replace the namespace and the duplicated current-state summaries.

**Guiding question:** which parts help because they hold truth, and which parts
exist only because the present tree cannot make that truth findable?

## 2 · The proposed folder tree

```text
estate/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── codex.md
├── gemini.md
├── grok.md
├── owner/
├── repositories/
├── state/
├── plans/
├── decisions/
├── ideas/
├── evidence/
├── practices/
├── tools/
├── sessions/
└── archive/
```

Tool-required root exceptions such as `.github/`, `.codex/`, `bootstrap.py`,
and kit configuration may also live at root. They are runtime addresses, not
content categories. `sessions/` should be visible rather than hidden; if the kit
still requires `.sessions/`, change that contract before the new hub is born,
while a rename is still cheap.

Every role folder gets a one-screen README with the same contract headings:
**belongs here**, **does not belong here**, **source of truth**, **filename
rule**, **when it leaves**, and **generated outputs**. Those contracts should be
checked mechanically where possible.

Three boundaries need explicit handoff rules in both sibling READMEs:
`evidence/` establishes facts while `state/` summarizes only what is currently
true; an `idea/` moves to `plans/` when work is actually promised; a practice
states the rule while `tools/` contains its executable implementation.

| Folder | Belongs here | Does not belong here |
|---|---|---|
| `owner/` | Generated attention index and short files awaiting the owner's words, choice, or triage | Technical status, hidden agent work, or a second copy of source truth |
| `repositories/` | One folder per external repository: purpose, route, last handoff, and pointers to product truth | Product implementation or copied product plans |
| `state/` | The small set of facts true now: hub state, cutover state, active work, current risks | Dated proof belongs in `evidence/`; state links to it rather than absorbing it |
| `plans/` | Future work with an explicit draft/approved/completed state and owner | Unpromised possibilities stay in `ideas/`; findings and completed history stay elsewhere |
| `decisions/` | One decision register and decision evidence pointers | Open questions or repeated decision prose |
| `ideas/` | Uncommitted possibilities and their triage outcome | Once work is promised it moves to `plans/`; owner decisions belong in `decisions/` |
| `evidence/` | Dated findings, audits, experiments, and research with method and conclusion | Current summaries belong in `state/`, even when evidence established them |
| `practices/` | Estate-specific ways of working, review rules, and traps | Executable implementations belong in `tools/`; universal kit rules and vendor limits stay elsewhere |
| `tools/` | Checks, generators, importers, and move/link-rewrite tools | The rule a tool enforces belongs in `practices/`; this folder holds implementation only |
| `sessions/` | In-progress and recent handoffs on the fixed clock | Permanent decisions, evidence, or a lifetime archive |
| `archive/` | Frozen material moved by the archive tool and its generated manifest | Anything still authoritative or used by active work |

**How I see it:** the most durable distinction is not document format but the
role a fact plays: now, next, settled, possible, observed, or historical.

**What I suggest:** approve these role names before creating `estate`, then
write the folder contracts before importing a single legacy file. Avoid a
generic `docs/`; it recreates today's ambiguity one level down.

**Guiding question:** can the owner choose between `state/`, `plans/`,
`decisions/`, `ideas/`, and `evidence/` without learning an internal vocabulary?

## 3 · Archive design

I disagree with a literal same-shaped mirror of the live tree. It promises
symmetry that the plan deliberately refuses to maintain after archival. It also
doubles search results and makes people wonder which copy is current.

Use this shape instead:

```text
archive/
├── README.md
├── manifest.csv              # generated, owner-readable
└── <original-role>/
    └── <YYYY-MM>/
        └── <remaining-original-path>
```

The move tool should write one manifest row with: original path, archived path,
archive date, reason, replacement if any, commit SHA, inbound links rewritten,
and external-reference stub if one was required. Search ignores `archive/` by
default; deliberate archive search opts in. An archived file never moves merely
because its live counterpart or role is renamed. The manifest, not symmetry,
is the lookup bridge.

The machine definition behind “no active project uses this” should be narrow:

- older than the chosen activity window;
- no inbound links from declared active roots;
- absent from active repository manifests and current state;
- not cited by an open plan, owner item, or recent session card.

Passing those checks means **candidate**, never “value gone.” The human still
answers whether the file's value is exhausted.

**How I see it:** search pollution is mechanical; value is judgment. One tool
should solve the first without pretending to solve the second.

**What I suggest:** freeze archive paths, exclude them from default search, and
generate a complete move manifest. Do not track later live-tree renames.

**Guiding question:** when looking for old evidence, would the owner rather
remember where it used to live or ask one manifest where it went?

## 4 · Carry, distill, or leave

### Carry whole

- unconsumed owner comments and their provenance;
- the three existing per-repository intent drafts;
- the owner-index generator and its explicit source contract;
- small current schemas and checks that the new tree needs on day one;
- kit-owned bootstrap files, with local changes recorded rather than copied
  silently.

### Distill into new truth

- root purpose and routing;
- one current-state document;
- the active owner-attention queue;
- decisions still governing the new hub;
- the repository list and each repository's purpose coverage;
- measured capabilities that remain current;
- the approved fresh-start plan and migration manifest.

Each distilled item should link to its fleet-manager evidence and state when it
was last verified. Distillation is a new summary, not a disguised file move.

### Leave in fleet-manager's archive

- old session cards and seat-era control/telemetry;
- completed plans, audits, findings, research, and proposals;
- old prompts and provider histories;
- shipped logs and historical environment records;
- any apparatus whose only job was compensating for fleet-manager's layout.

Start the new session history with one cutover card linking the last three old
cards; do not copy 454 cards into the live hub.

**How I see it:** “useful” is not the same as “must be live.” Most of this
repository remains useful as evidence and harmful as current navigation.

**What I suggest:** require a migration manifest with exactly one disposition
per candidate: `carry`, `distill`, or `archive`, plus destination, source,
certainty, and verifier.

**Guiding question:** if a carried file disappeared tomorrow, would current
work stop—or would only historical explanation become harder to find?

## 5 · Sequence

Recommended order:

1. Approve role names, folder contracts, and the scored acceptance rubric.
2. Create the minimum skeleton later: routes, search exclusions, session hold,
   link checker, and manifest validator.
3. Build the migration manifest for only the proposed live seed.
4. Distill and seed the smallest truthful current hub.
5. Give the pinned tree and pre-registered rubric to a separate cold agent for
   blind scoring, then run the document-open test, owner browse, link-rewrite
   rehearsal, and strict gate. The producer's self-score is evidence, not the
   cutover verdict.
6. Perform the absolute write cutover.
7. Add deeper skills, hooks, and consolidation only when the live hub shows
   their need; promote stable pieces to the kit from measured use.

This keeps the plan's practice gates. It changes only when the larger apparatus
is built. Designing every mechanism against an empty tree risks reproducing
fleet-manager's abstractions before the new structure has been tested with real
material.

**How I see it:** structure and minimum safety are birth requirements; a full
operating system is not.

**What I suggest:** move “seed and cold-test” ahead of full Phase 3 build-out,
while retaining the born-red session gate, link checks, and no-stale-current
checks from the first commit.

**Guiding question:** what is the smallest seed that proves the structure works
without making the old repository writable again?

## 6 · Instruction-file drift

Use one shared `AGENTS.md` and one delta file per vendor. Give every vendor file
the same small template: **how context loads**, **available access**, **surface
limits**, **fallback**, and **last verified**. A checker can flag identical
normalized paragraphs in two vendor files and require shared rule identifiers
to exist only in `AGENTS.md`. It cannot prove two differently worded paragraphs
mean the same thing; review remains necessary.

Generate a comparison report showing each vendor file's headings and
last-verified dates. Do not generate the vendor files themselves: their
surface-specific claims need deliberate verification.

**How I see it:** drift starts when shared policy is copied, not when a vendor
has a genuine difference.

**What I suggest:** make duplicate shared prose a check failure and stale
capability dates an advisory. Require a human or second agent to review semantic
overlap during instruction changes.

**Guiding question:** if a rule vanished from one vendor file, would that vendor
behave differently for a real reason? If not, the rule belongs in `AGENTS.md`.

## 7 · Current-repository findings that affect the move

These are not reasons to repair fleet-manager in place. They are warnings about
what not to distill without checking:

- `docs/current-state.md` still names an older kit-records action rather than
  the fresh-start folder sitting.
- `docs/planning/README.md` describes the hard cut, carry set, and hub name as
  open after later records settled them.
- an earlier decision entry's open paragraph is superseded by the later hub-name
  decision and the redirect's answered section.
- `docs/MAP.md` does not route to `owner/` and still presents an older planning
  front door.

**How I see it:** the problem is not merely too many folders. Several polished
front doors can each be internally plausible and jointly stale.

**What I suggest:** choose one generated current-state source in `estate` and
make every other front door link to it instead of restating it.

**Guiding question:** which one file is allowed to answer “what is happening
now,” and which check proves every other summary points there?
