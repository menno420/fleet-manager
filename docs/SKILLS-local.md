# fleet-manager — locally-authored skills

> **Status:** `living-ledger`
>
> Skills written in this repo rather than shipped by the kit. Kept separate
> because [`SKILLS.md`](SKILLS.md) regenerates from the kit's own list at every
> adopt/upgrade and must never be hand-edited — a row added there disappears at
> the next upgrade. These do not, because the kit never writes a live `.claude/`
> tree.

## Why this file exists at all

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
2. Add a row above.
3. Keep the description one line and concrete — it is what a session matches
   against when deciding whether the skill applies.

Skills earn their place by being invoked. One that never fires is a document with
extra steps; fold it into the doc it should have been.
