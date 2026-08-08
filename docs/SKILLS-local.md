# fleet-manager — skills: the complete installed set

> **Status:** `living-ledger`
>
> **The one place that answers "what can I do here" without loading 27 files.**
> Two halves with different owners: skills **written in this repo**, detailed
> below, and skills **shipped by the kit**, whose generated index is
> [`SKILLS.md`](SKILLS.md). That file regenerates from the kit's own list at
> every adopt/upgrade and must never be hand-edited — a row added there
> disappears at the next upgrade. The local ones do not, because the kit never
> writes a live `.claude/` tree.
>
> The roster immediately below spans **both** halves, because a session reading
> either file alone gets part of the answer and cannot tell that it is part.

## All 27 — the roster

`MEASURED` 2026-08-08 against `.claude/skills/` (the live, invocable tree).
**Invoke as `/<name>`.** The one-liners are each skill's own `description`
frontmatter — the same text a session matches against when deciding whether a
skill applies. For the local skills, the fuller "when to reach for it" entries
are further down; for the kit skills, [`SKILLS.md`](SKILLS.md) adds declared
capabilities and exact grounds commands.

| skill | body | what it does |
|---|---|---|
| `analysis` | kit | Read-only deep-dive: investigate and report findings without changing anything. |
| `asset-pipeline` | local | A delivered generated image → engine-ready asset: key by corner sample, despill at full resolution, downscale to the contract size, three-scale fringe audit, source-record entry. |
| `audio-prompt` | local | Any audio ask — SFX, loops, music stems — by either route, against the committed contract: mono 44.1 kHz 16-bit WAV, sub-0 dBFS with edge fades, manifested, loops mathematically continuous. |
| `capability-probe` | local | Test what a session can do and record it correctly — before declaring anything impossible, and after discovering something works. Produces a well-formed `CAPABILITIES.md` entry with venue token and verbatim evidence. |
| `chase-references` | kit | Resolve every reference in the ask before acting — inventory, resolve or search each one, report unfindables explicitly, state the assembled picture back. |
| `continuation-prompt` | local | Carry a planning or working session into a fresh one — harvest this chat's decisions, verify state at HEAD, commit what should be committed, emit a paste-ready prompt. |
| `cover-art-prompt` | local | Cover art, key art, app icons, banners, store assets — full-bleed, no chroma, silhouette read, short in-image text allowed and tested. Loads on top of `image-prompt`. |
| `decision-capture` | local | Turn decisions that exist only in a conversation into a committed record, so the next prompt points at them instead of carrying them. |
| `deep-research` | kit | Fan out web research, adversarially verify sources, synthesize a cited report. |
| `delegate-read` | local | Hand a read-heavy job to Gemini instead of burning session context, and get back claims citation-verified against the repo before you read them. |
| `image-prompt` | local | The shared method for **any** image-generation prompt — eight sections, anchored to an existing asset, one asset per call, chroma-keyed, function criterion, acceptance question. Routes to the three type skills. |
| `implementation-prompt` | local | Direct a session to build a defined thing — scope and non-scope, the contract, where the patterns live, the verify command, landing discipline, the traps that actually bit. |
| `intake` | kit | Turn a fragmented owner ask into main ideas, a restated fuller picture, a skill-index map, and structured-choice owner questions — before building. |
| `owner-brief` | local | The owner's status brief on demand — what landed, what needs his eyes, what happens next — plain language, zero technical vocabulary, decisions as one-letter choices. |
| `parallax-prompt` | local | Parallax background layers and wall/rail materials — one layer per call, far layer opaque, mid/near on chroma, tiling only where the renderer needs it. Loads on top of `image-prompt`. |
| `prep-owner-steps` | kit | Hand the owner finished steps, not directions — deep links, paste-ready blobs, his path walked once, one batched sitting, payoff + verification stated. |
| `prompt-preflight` | local | The checks to run before writing **any** session prompt — verify state at HEAD, split repo-held from chat-held, read the target surface's constraints. |
| `quality-gate` | kit | Run the project's full verification before pushing and report what must be fixed. |
| `question` | kit | Answer a direct question concisely from memory and source; make no changes. |
| `rationalize` | kit | The checkpoint at natural pauses — should this action also be executed? does this lesson deserve a permanent home shippable NOW? |
| `release` | kit | Cut + publish a substrate-kit release — version bump PR, `workflow_dispatch` publish, three-way asset verification, adopter distribution wave. |
| `repo-health` | kit | Audit doc + session-log hygiene (bootstrap check) and summarize drift. |
| `review` | kit | Review the branch diff against the binding contracts; comment with a verdict and fixes, no edits. |
| `scope-backlog-item` | kit | Turn a raw backlog item into a turnkey recipe or an owner ask — chase its origin, classify buildable/owner-gated/dead, write the sized recipe with acceptance + traps. |
| `session-close` | kit | Land the session — claim, born-red card first, READY PR, batched work, close-out docs, flip complete last; land on green. |
| `sprite-prompt` | local | A character/object sprite that must slot into an existing set — canonical camera and layout, enumerated body parts, chroma field, runtime dimensions. Loads on top of `image-prompt`. |
| `upgrade-distribution` | kit | Roll a kit release out to one adopter repo — download, sha256 three-way, banked rollback, carve-out scan, born-red PR, tree-verified merge. |

### What this roster fixed — `MEASURED` 2026-08-08

The count was the symptom; three separate defects were the cause. All were
found by listing `.claude/skills/` and diffing it against both indexes.

1. **`rationalize` and `scope-backlog-item` appeared in NO index** — installed,
   invocable, and undiscoverable except by listing the directory.
2. **`chase-references` and `prep-owner-steps` were indexed as living somewhere
   else.** `SKILLS.md` carries a "Fleet seed skills — pointer (not kit-shipped
   yet)" section saying their bodies live in **superbot**. They are installed
   *here*, and that section is stale — it predates the kit shipping them. It is
   generated, so **it is not corrected by hand**; it will clear at the next
   adopt/upgrade, and this roster is the true list until then.
3. **Neither file stated its own scope**, so a session reading one had no signal
   that the other half existed. Both headers now say so.

The general shape is worth more than the instance: **an index that does not
state what it covers reads as complete.** Same failure as a wall that reads as
measured — the fix is a scope line, not a longer list.

## Why the local half exists at all

Two facts, both verified 2026-08-03:

1. **The kit stages skills; it does not install them.** `bootstrap.py skills
   --build` writes `.substrate/skills/<name>/SKILL.md` and, in its own words,
   *"never writes a live `.claude/` tree"*. The host installs them. Until
   2026-08-03 nobody had, so `.claude/skills/` did not exist and **none of the
   fourteen kit skills was invocable as `/<name>`** — they were documented,
   staged, and unreachable. That is the likeliest mechanical reason skills were
   used less than they should have been.
2. **Because the kit never touches `.claude/skills/`, hand-authored skills there
   are safe.** They survive upgrade. They are simply invisible to the generated
   index, which is what this file fixes.

Installing the staged set is a copy:

```bash
python3 bootstrap.py skills --build          # refresh the staged tree
mkdir -p .claude/skills
for d in .substrate/skills/*/; do
  n=$(basename "$d"); mkdir -p ".claude/skills/$n"
  cp "$d/SKILL.md" ".claude/skills/$n/SKILL.md"
done
```

Re-run it after a kit upgrade. It only overwrites kit-named skills; the local
ones below are untouched.

⚠ **That cuts both ways: local amendments to a kit-named skill are overwritten
by the same copy.** `session-close` carries fleet-manager-specific steps — the
live-venue rewrite (2026-08-04, owner-ratified 2026-08-05) and the Layer 2
handoff line (2026-08-08) — so **re-apply them after every upgrade** and check
the diff before assuming the install was clean. The durable fix is upstream:
propose the generalisable half to the kit so it ships to every adopter instead
of living as a local patch that each upgrade silently reverts.

## The local skills

| Skill | When to reach for it |
|---|---|
| `prompt-preflight` | Before writing **any** session prompt — verify state at HEAD, split repo-held from chat-held, read the target surface's constraints, define done. Invoked by the two below; run directly when hand-writing a prompt. |
| `continuation-prompt` | A planning or working session is ending and the work continues in a fresh one. Harvests this chat's decisions, verifies state, offers to commit first, emits a paste-ready prompt. |
| `implementation-prompt` | The shape of the work is already agreed and a session needs to build it. Contract, non-scope, the pattern to follow, acceptance, landing discipline, real traps. |
| `decision-capture` | Decisions exist only in a conversation. Lands them in the repo so handoffs become pointers instead of payload. |
| `image-prompt` | The **shared method** for any image-generation prompt (eight sections, hard rules, measured pipeline facts) and the router to the three type skills below. Reverse-derived from the sessions that made spider-swing's art: [`findings/2026-08-04-generated-art-pipeline.md`](findings/2026-08-04-generated-art-pipeline.md). |
| `sprite-prompt` | A character/object sprite that must slot into an existing set — set contract first, anchor + identity exclusion, enumerated layout with a checkable total, neutral stance, chroma by palette. |
| `parallax-prompt` | Parallax background layers and wall/rail materials — one layer per call, far layer opaque, mid/near on chroma, tiling only where the renderer needs it (measured: spider-swing mirrors alternate backdrop tiles), centre stays open. |
| `cover-art-prompt` | Key art, app icons, banners, store assets — full-bleed, no chroma, composition brief, silhouette read at thumbnail size, one short in-image word allowed as the calibration signal, icon margin rule. |
| `asset-pipeline` | The post-generation half: key by corner sample (never the requested hex), despill at full resolution, downscale to the contract size, three-scale fringe audit (bar: zero), source-record entry, in-engine proxy check. Runnable snippets included; measured basis: `tools/chroma_spill_probe.py`. |
| `audio-prompt` | Any audio ask, either route (procedural generator or AI generation), delivered against spider-swing's committed contract: mono 44.1kHz 16-bit WAV, sub-0dBFS + 3ms fades, mathematically continuous loops, manifested provenance. Honest about what is measured (the contract) vs transferred (the method) vs unmeasured (every AI audio provider). |
| `capability-probe` | The discovery rule as an executable method: ledger → environment → attempt once → verbatim evidence → same-session append with venue token. Fires at the moment of thinking "I can't", not at commit time. |
| `delegate-read` | A read-heavy sweep (every session card, every bench result, a whole doc tree) handed to free-tier Gemini via `tools/gemini_delegate.py`, with every returned claim citation-verified against the repo before it is read. Delegates the reading, never the record. |
| `owner-brief` | The owner's status view on demand: LANDED / YOUR EYES / NEXT, plain language only, decisions as one-letter choices with bolded recommendations, under a minute to read. |

## The idea they share

> **A prompt carries what is not in the repo. The repo carries the rest.**

Pointers stay true when the repo moves; inlined copies rot and then outrank the
file they were copied from. So the only things that belong inline are the ones a
fresh session genuinely cannot recover — the decisions made, the options rejected
and why, the constraint the owner said out loud and nobody wrote down.

That is also why `decision-capture` exists: when the inline payload grows, the
right fix is usually not a longer prompt but a commit, after which the prompt
shrinks to a pointer and the decisions outlive it.

## Promoting one upstream

A local skill that proves itself here is a candidate for the kit's `SKILLS` list,
which would reach every adopter. That is a change in the kit repo, not here.
Until then it lives in this file and in `.claude/skills/`, which is enough to use
it and enough to find it.

## Adding one

1. Write `.claude/skills/<name>/SKILL.md` with frontmatter (`name`,
   `description`) and a body: what it does, numbered instructions, traps.
2. Add a row to **both** tables above — the 27-skill roster (so it is
   discoverable) and the local table (so its "when to reach for it" is
   recorded). A skill in only one of them is the defect this file just fixed.
3. Keep the description one line and concrete — it is what a session matches
   against when deciding whether the skill applies.

Skills earn their place by being invoked. One that never fires is a document with
extra steps; fold it into the doc it should have been.
