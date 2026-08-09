# fleet-manager as the index — the two-layer restructure

> **Status:** `plan` · 2026-08-08 · owner-live design session
>
> **These are decisions, not proposals.** Taken by the owner across one
> conversation, each one restated back to him and confirmed. Where a decision
> reversed an earlier agent proposal, the reversal is recorded with its reason —
> the reasons are the part that stops the next session re-litigating.
>
> Certainty tags per
> [`../findings/2026-08-05-foundation-continuation.md`](../findings/2026-08-05-foundation-continuation.md).

## The premise

`OWNER`. **fleet-manager is always the boot repo, and is never the repo the
session is about** — the sole exception being work on fleet-manager itself.

The working model, in order:

1. Session boots on fleet-manager (single source, so its `.claude/` actually
   loads — boot triad case 1).
2. It **orients** from fleet-manager's own docs.
3. It **attaches** the working repo (`add_repo`).
4. It works there.
5. At close, it **updates that repo's folder here** so the next boot starts
   informed.

Consequence worth stating plainly, because it removes a whole class of
difficulty: **there is no cross-repo write.** The session is always inside
fleet-manager when it updates the folder. No untried capability is involved.

## The two layers

### Layer 1 — general, and it stays light

The required reading order carries what applies **regardless of which repo is
being worked on**:

- general skills and capabilities
- documentation rules — how things get written and filed *here*
- a short line per repo: what it is and why it exists (orientation, not depth)
- the rest of what a session normally does

**Constraint: light.** It must carry the most important information about
everything a session normally does, and it is not where any single repo gets
explained properly.

### Layer 2 — one folder per repo

`OWNER`, and this **reverses an agent proposal**: a single file per repo was
proposed and rejected as *"too condensed"*. Each repo gets a folder holding a
**compacted orientation that stands on its own**.

> **The test that defines "enough": a session must be able to answer basic
> questions about the repo WITHOUT the repo attached** — and must be able to
> decide *whether* to attach it.

```
docs/repos/<name>/
  README.md         what it is · why it exists · the per-repo boot path
  current-state.md  what is true now
  capabilities.md   what is verified there
  goals.md          current objectives
  records.md        index into fleet-manager's own dated files about it
```

**`README.md` is the entry and stands alone.** One read answers the basic
questions; the other four are depth, opened when the question is deeper. This is
the record/instruction split applied one level down — the thing read *in the
moment* must fit working attention, the depth may grow. The doc-route for a repo
points at `README.md`, never at the folder.

## Tiering — depth follows where work actually happens

`OWNER`.

| tier | repos | treatment |
|---|---|---|
| **1** | `spider-swing` · `superbot` + `superbot-next` (paired) · `substrate-kit` · `venture-lab` | full folder, filled |
| **2** | the remaining ~19 | ~~present as orientation points; `README.md` only, honestly stubbed~~ **SUPERSEDED — see below**; depth **deferred, not skipped** |

Tier 2 repos are *"still important but less so for actually working on"*. A
session must be able to find them and know what they are.

> **⚑ Tier 2 SUPERSEDED — owner, 2026-08-08 intent interview (answer 17).**
> **Do not pre-stub the remaining ~19.** Folders are built **on demand**, when
> work actually goes to that repo; the four Tier-1 folders are cleared to build
> now. Both this row and the replacement are `OWNER`, and the later statement
> wins — recorded here rather than only in the newer document, because a session
> arriving at this table by grep or by the read path would otherwise follow a
> superseded directive that still reads as current and carries the same
> provenance label.
>
> The reason is the one this design already argued for Layer 2 generally: **a
> stub that is never filled is precisely what the coverage table exists to make
> visible**, and 19 of them would make absence invisible by making it uniform.
> Live decision and its provenance: [`../intent.md`](../intent.md) § 8 ·
> coverage state: [`../repos/README.md`](../repos/README.md).

**fleet-manager gets its own folder too.** Today's work on it is otherwise a
standing exception, and an exception that recurs is a rule with a gap.

## What each folder IS — a handoff, not an encyclopedia

`REASONED`, accepted by the owner. The folder is **not documentation about the
repo** — that would compete with the repo's own docs and drift. It is **where
the last session left off and where the next one should look**: a short summary
plus pointers to the files that matter, each with one line on what it is.

That makes it a **persistent continuation prompt** for that repo, and the shape
is already defined by the [`continuation-prompt`](../../.claude/skills/continuation-prompt/SKILL.md)
skill: where things stand · decided · open · first step.

Being dated is then its *nature*, not its decay.

### Three tiers of ownership — conflating any two is the drift risk

`MEASURED` (spider-swing ships `AGENT_ORIENTATION.md`, `CAPABILITIES.md`,
`architecture.md`, `SKILLS.md` and more of its own):

| | lives | canonical for |
|---|---|---|
| the repo's own docs | its repo | **its internal state** — architecture, its capabilities, how to work in it |
| fleet-manager's dated records | here (`docs/`, `.sessions/`) | **what happened in sessions run from here** |
| the Layer 2 folder | here | **nothing** — it is an entry point and a handoff |

The link-never-copy rule survives **only** under a stamp: each file states what
it summarises, which doc is canonical, and the date it was true. The rule exists
to stop *silent* drift, not to forbid summaries — the estate's own
`evidence-index.md` carries exactly this header pattern. **The moment a folder
file starts explaining the repo's architecture it has become a copy and will
drift**, so the rule belongs written on the page.

## Threads — the unit of replacement

`REASONED`, and this **corrects an earlier agent rule**. "Each session replaces
the pointer list" was proposed to stop the list becoming a changelog; it assumed
one active thread per repo and would have silently wiped paused or parallel work.

Corrected: **the folder holds one block per active thread**, and a session
replaces *its own* block only.

```
## Thread: <name> — active, updated YYYY-MM-DD
   where it stands · pointers · next step
## Thread: <name> — paused YYYY-MM-DD
   where it stopped · pointers · what would resume it
```

Three properties this buys: parallel and paused work survives a session that
never touched it; staleness becomes **visible** rather than silent; and threads
are **closed explicitly** by the session that finishes them, so the file keeps
answering "what matters now" without growing into a changelog.

## Maintenance — a session-close step, and deliberately NOT a gate

`REASONED`. A gate checking "attached a repo ⇒ touched its folder" was proposed
and **withdrawn before implementation**. It reproduces the exact defect that
killed the provenance gate one day earlier: a session attaching a repo for a
read-only lookup or a typo fix would be forced to write a meaningless update or
go red on legitimate work — *gate-every-card, reddening work that never touched
a decision surface*.

Nor does it narrow cleanly. *"Did the session attach a repo"* is a fact;
*"did the handoff state change"* is a **judgement**, and a trivial fix is
indistinguishable from a direction change to a script. Mechanise facts, never
meaning.

**So: a step in `session-close`, with an explicit null** — *"if nothing about
the handoff changed, record that and move on."* Same null-path discipline as the
owner-review hook, which is what stops a check becoming ritual.

## Acceptance tests — write them down, then run them

Two, both owner-stated, and they are the definition of done rather than a
nice-to-have:

1. **The single-repo boot.** Boot fleet-manager, say *"this session is for
   spider-swing"* → the session finds that repo's objectives, capabilities and
   where to look, **before attaching it**.
2. **The survey.** Boot fleet-manager, ask *"what are the current open
   projects"* → the session reviews the repo folders and, for each, states the
   current main point of importance plus a short suggestion for how to
   start or continue — so the owner can **choose** which repo to work on.

Test 2 is the stronger one: it exercises every folder at once and fails loudly
if any is empty, stale or unreadable.

## Layer 1's own gaps — measured 2026-08-08, and both are owner goals

`MEASURED`:

- **`docs/SKILLS-local.md` names 13 of 27 installed skills.** Absent:
  `session-close`, `release`, `review`, `intake`, `quality-gate`,
  `deep-research`, `rationalize`, `repo-health`, `analysis`, `question`,
  `chase-references`, `prep-owner-steps`, `scope-backlog-item`,
  `upgrade-distribution`. A session reading it to answer *"what can I do"* gets
  half and cannot tell that it is half. Owner requirement: **know which skills
  exist and what they do without loading them all.**
- **`@codex` appears 0 times in `.claude/CLAUDE.md`** and 5 times inside
  1,200-line `docs/CAPABILITIES.md`. Owner requirement: fleet-manager's own
  orientation should carry the abilities a session actually uses — talking to
  Gemini, the `@codex` PR mention (measured working, ~335 s latency, fm#813).

## Retrieval — the routing gap that makes Layer 1 light

`MEASURED`. `route_docs.py` is registered `PreToolUse` and reads **tool input
only** (`FIELDS`, line 45): a Bash command, URL, file path, Glob/Grep pattern,
Write/Edit content. **It never sees the owner's message.** So *"this session is
for spider-swing"* fires nothing until the session itself greps or reads that
string.

**Registering `route_docs.py` on `UserPromptSubmit` as well** closes this, and it
is what makes Layer 1 able to stay light: Layer 1 need not describe each repo
deeply, because naming a repo pulls its Layer 2 `README.md` in automatically.

## Working style for the build

`OWNER`: **not rushed. One repo at a time.** The session verifies which files
are genuinely valuable for that repo and which to defer — and **records why**
something was deferred rather than silently omitting it.
