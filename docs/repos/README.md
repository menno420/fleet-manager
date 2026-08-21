# `docs/repos/` — Layer 2, one folder per repo

> **Status:** `living-ledger`
>
> The estate's per-repo entry points. Layer 1 (the boot file and the read path)
> carries what is true **regardless of which repo a session is working on**;
> this directory carries the part that is specific to one.
>
> Design and the reasons behind every decision here:
> [`../planning/2026-08-08-fleet-manager-as-index.md`](../planning/2026-08-08-fleet-manager-as-index.md).
> Certainty tags per
> [`../findings/2026-08-05-foundation-continuation.md`](../findings/2026-08-05-foundation-continuation.md).

## The working model this exists to serve

fleet-manager is **always the boot repo and never the subject repo** — the sole
exception being work on fleet-manager itself. So a session:

1. boots here (single source, so this repo's `.claude/` actually loads),
2. **orients from the repo's folder below — before attaching anything**,
3. attaches the working repo (`add_repo`),
4. works there,
5. at close, updates that repo's folder here.

Because step 5 happens while the session is still inside fleet-manager, **no
cross-repo write is involved anywhere in this loop.**

## What a folder IS — a handoff, not an encyclopedia

The test that defines "enough": **a session must be able to answer basic
questions about the repo without the repo attached, and decide whether to attach
it at all.**

A folder is *where the last session left off and where the next one should
look* — a persistent continuation prompt for that repo. It is deliberately
**not** documentation about the repo, because that would compete with the
repo's own docs and lose.

### Three tiers of ownership — conflating any two is the drift risk

| | lives | canonical for |
|---|---|---|
| the repo's own docs | in that repo | **its internal state** — architecture, its capabilities, how to work in it |
| fleet-manager's dated records | here (`docs/`, `.sessions/`) | **what happened in sessions run from here** |
| a Layer 2 folder | here | **nothing** — it is an entry point and a handoff |

A folder file summarises and points; it never becomes the source. The rule
survives only under a stamp, so **every file here states what it summarises,
which document is canonical, and the date it was true.** The moment a file
starts explaining the repo's architecture it has become a copy and will drift.

## Threads — the unit of replacement

A folder holds **one block per active thread**, and a session replaces *its
own* block only — never the whole file. That is what keeps paused and parallel
work alive across a session that never touched it.

```
## Thread: <name> — active, updated YYYY-MM-DD
   where it stands · pointers · next step
## Thread: <name> — paused YYYY-MM-DD
   where it stopped · pointers · what would resume it
```

Threads are **closed explicitly** by the session that finishes them, so the file
keeps answering "what matters now" instead of growing into a changelog. Being
dated is the folder's nature, not its decay: staleness is meant to be *visible*.

## The files, and how a repo earns them

`README.md` is the entry and **stands alone** — one read answers the basic
questions and carries the thread blocks. Everything else is depth, opened when
the question is deeper. A doc-route for a repo points at `README.md`, never at
the folder — and **a built folder ships with its doc-route pair in the same
PR** (`<id>` for tool events + `<id>-prompt` for UserPromptSubmit): the
product-forge folder went routeless for a week because the route was treated
as a separate chore (measured, fleet review 2026-08-21), which silently
falsified the boot file's "naming a repo pulls its README in".

The design named `current-state` / `capabilities` / `goals` / `records` as a
**starting shape** and asked the first folder to earn its files. That question is
**now settled** (owner, 2026-08-08): the earned set — `README.md` +
`capabilities.md` + `records.md` + `working-here.md`, with `current-state.md` and
`goals.md` deferred — **is the shape every folder replicates.** Start from it
rather than re-deriving it.

What survives from "each repo earns its files" is narrower and still true: **a
folder may add a file its repo genuinely needs, and any departure from the shape
is recorded with its reason** — silently omitting or adding one is what makes the
next session re-derive a decision that has already been made.

See [`spider-swing/README.md`](spider-swing/README.md) § "Why this folder has
the files it has" for the worked example the shape came from.

## Coverage — honest, and mostly not yet built

| tier | repos | state |
|---|---|---|
| **1** | `spider-swing` | ✅ **built** 2026-08-08 — the reference shape, **ratified 2026-08-08** |
| **1** | `superbot` | ◐ **entry point built** 2026-08-21 (on-demand, the keep-bot-only close) — `README.md` only; depth files not yet written, reasons in its header. Carries the § 5.7 section (all null) |
| **1** | `superbot-next` (superbot's pair) | ◐ **entry point built** 2026-08-21 (the fleet review, fm #878) — `README.md` only; depth files not yet written, reasons in its header. Carries the § 5.7 section (all null) |
| **1** | `substrate-kit` | ◐ **entry point built** 2026-08-21 (same review) — `README.md` only; carries the FM-resident 22-row worklist pointer. § 5.7 section all null |
| **1** | `venture-lab` | ◐ **entry point built** 2026-08-21 (same review) — `README.md` only; carries the OD-11 supersession the repo's own docs lack. § 5.7 section all null |
| **1** | `fleet-manager` (itself — today's work is otherwise a standing exception) | ⬜ not built — outside the owner-ratified build-now set; its intent already lives at [`../intent.md`](../intent.md) |
| **2** | `product-forge` | ◐ **entry point built** 2026-08-14 (on-demand, the Slice-18 session) — `README.md` only; `capabilities.md` / `records.md` / `working-here.md` deliberately not yet written, reasons in its header. Carries the § 5.7 external-workspaces section (all null today) |
| **2** | `couch-legend` | ◐ **entry point built** 2026-08-20 (on-demand, the adoption session) — `README.md` only; depth files not yet written, reasons in its header. Carries the § 5.7 section (Grok provenance pointers live; ChatGPT: the owner's "Couch Legend" project, 2026-08-21, instructions at [`../prompts/chatgpt-couch-legend-project-instructions.md`](../prompts/chatgpt-couch-legend-project-instructions.md); Drive/Gemini null) |
| **2** | `websites` | ◐ **entry point built** 2026-08-21 (on-demand, the keep-bot-only close) — `README.md` only; depth files not yet written, reasons in its header. Carries the § 5.7 section (all null) |
| **2** | `estate-backups` | ◐ **entry point built** 2026-08-21 (on-demand, same close) — `README.md` only; the private Actions venue for bot-DB work. Carries the § 5.7 section (all null) |
| **2** | all other repos | ⬜ **on demand** — built when work goes there, not pre-stubbed (owner, 2026-08-08). **Every repo without a folder has a routing row in [`../ESTATE.md`](../ESTATE.md)** — the estate index (one line per repository: what it is, state, aliases, canonical entry), added 2026-08-21 so "no folder" never again means "invisible" |

**The shape is settled — owner, 2026-08-08.** The three questions the spider-swing
folder left open are answered: it replicates **as built** (`README.md` +
`capabilities.md` + `records.md` + `working-here.md`); `working-here.md` **earns
its place as a distinct file** because gates, verify commands and traps are what a
session needs *before* attaching, and they are neither state nor goals;
`current-state.md` and `goals.md` **stay deferred**. Coverage is **the named
Tier-1 build-now set above; all other repos are on demand** — deliberately not a
prebuilt folder for every repo, because a stub that is never filled is the
failure mode this directory's own coverage table exists to make visible.
Provenance: [`../intent.md`](../intent.md) § 8.

**One addition to the shape — first carried 2026-08-14:** a folder should point
at the repo's **external workspaces** — its Drive folder, its ChatGPT workspace,
its Gemini notebook — as pointers, never copies (owner, 2026-08-08). Design:
[`../planning/2026-08-08-agent-operating-environment-roadmap.md`](../planning/2026-08-08-agent-operating-environment-roadmap.md)
§ 5.7. `product-forge/README.md` carries it (with honest nulls — the mapping is
optional and many-to-many); spider-swing's gets it retroactively.

**A blank row above means "not written yet", never "nothing is happening
there."** Until a row is built, that repo's truth lives where it always did:
in its own `docs/current-state.md` and `docs/PROJECT-CLOSEOUT.md`, plus this
repo's dated records. Tier 2 repos are still important — a session must be able
to find them and know what they are — they are simply not where work happens
most weeks.

## This is not `projects/`

`../../projects/<name>/` is **seat-era apparatus and historical record**: the
console package (Custom Instructions, startup prompts) for the autonomous
Projects that closed 2026-07-21, generated from `docs/prompts/v3/`. It is
per-*seat*, not per-*repo*, several of its dirs are merged-source pointer stubs,
and it is not on any boot read path.

`docs/repos/` is per-repo, current, and hand-written. The two do not overlap and
neither supersedes the other. If you are looking for what a repo is doing now,
you are in the right directory.

## Maintenance — a session-close step, deliberately NOT a gate

A gate on *"attached a repo ⇒ touched its folder"* was proposed and **withdrawn
before implementation**. `Did the session attach a repo` is a fact; **`did the
handoff state change` is a judgement**, and a typo fix is indistinguishable from
a direction change to a script. Mechanise facts, never meaning — a gate here
would redden legitimate read-only work, which is the same defect that killed the
provenance gate a day earlier.

So it is a step in `session-close`, **with an explicit null**: if nothing about
the handoff changed, record that and move on. The null path is what stops the
check becoming ritual.
