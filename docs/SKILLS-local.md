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
| `intake` | kit, **fm-extended 2026-08-09** | Turn a fragmented owner ask into a provenance-separated **intent map** — what he said · what the repo already decided · what you inferred · what is genuinely open — plus goal, non-goals, success test and an `INTENT STATUS` verdict, before planning. The old single "fuller picture" paragraph is gone: fusing those four is the failure it now prevents. |
| `owner-brief` | local | The owner's status brief on demand — what landed, what needs his eyes, what happens next — plain language, zero technical vocabulary, decisions as one-letter choices. |
| `parallax-prompt` | local | Parallax background layers and wall/rail materials — one layer per call, far layer opaque, mid/near on chroma, tiling only where the renderer needs it. Loads on top of `image-prompt`. |
| `prep-owner-steps` | kit, **fm-amended** | Hand the owner finished steps, not directions — deep links, paste-ready blobs, his path walked once, one batched sitting, payoff + verification stated. |
| `prompt-preflight` | local | The checks to run before writing **any** session prompt — verify state at HEAD, split repo-held from chat-held, read the target surface's constraints. |
| `quality-gate` | kit, **fm-amended** | Run the project's full verification before pushing and report what must be fixed. |
| `question` | kit | Answer a direct question concisely from memory and source; make no changes. |
| `rationalize` | kit | The checkpoint at natural pauses — should this action also be executed? does this lesson deserve a permanent home shippable NOW? |
| `release` | kit, **fm-amended** | Cut + publish a substrate-kit release — version bump PR, `workflow_dispatch` publish, three-way asset verification, adopter distribution wave. |
| `repo-health` | kit | Audit doc + session-log hygiene (bootstrap check) and summarize drift. |
| `review` | kit | Review the branch diff against the binding contracts; comment with a verdict and fixes, no edits. |
| `scope-backlog-item` | kit, **fm-amended** | Turn a raw backlog item into a turnkey recipe or an owner ask — chase its origin, classify buildable/owner-gated/dead, write the sized recipe with acceptance + traps. |
| `session-close` | kit, **fm-amended** | Land the session — claim, born-red card first, READY PR, batched work, close-out docs, flip complete last; land on green. |
| `sprite-prompt` | local | A character/object sprite that must slot into an existing set — canonical camera and layout, enumerated body parts, chroma field, runtime dimensions. Loads on top of `image-prompt`. |
| `upgrade-distribution` | kit, **fm-amended** | Roll a kit release out to one adopter repo — download, sha256 three-way, banked rollback, carve-out scan, born-red PR, tree-verified merge. |

### What this roster fixed — `MEASURED` 2026-08-08

The count was the symptom; three separate defects were the cause. All were
found by listing `.claude/skills/` and diffing it against both indexes.

1. **`rationalize` and `scope-backlog-item` appeared in NO index** — installed,
   invocable, and undiscoverable except by listing the directory.
2. **`chase-references` and `prep-owner-steps` were indexed as living somewhere
   else.** `SKILLS.md` carried a "Fleet seed skills — pointer (not kit-shipped
   yet)" section saying their bodies live in **superbot**. They are installed
   *here*, and that section was stale — it predates the kit shipping them.
   *(Corrected by hand 2026-08-11. This bullet used to say "it is generated, so
   it is not corrected by hand; it will clear at the next adopt/upgrade" — the
   2026-08-09 upgrade then ran and cleared nothing, because `SKILLS.md` is
   `consumer-edited` and `apply_doc_improvements()` writes only
   consumer-untouched docs — the mechanism §"Generated-file corrections" below
   already stated while this line promised the opposite. A defect parked on an
   event that can never fire waits forever; hand-fixing was always the path.)*
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
by the same copy.** **SEVEN kit-named skills now carry fleet-manager amendments,
and all seven are reverted by that loop** — so **re-apply them after every
upgrade** and diff before assuming the install was clean. *(This table named two
of the seven until 2026-08-11 — the full-read audit's headline finding 5: a
session following it after an upgrade re-applied two, silently reverted five,
and reported a clean install. The set below is derived by diffing every
installed skill against its staged copy — re-derive it the same way rather than
trusting this prose:
`for d in .substrate/skills/*/; do n=$(basename "$d"); diff -q ".claude/skills/$n/SKILL.md" "$d/SKILL.md" >/dev/null || echo "$n"; done`.)*

| kit-named skill | local amendment at risk | added |
|---|---|---|
| `session-close` | the live-venue rewrite (2026-08-04, owner-ratified 08-05), the Layer 2 handoff line (2026-08-08), and the `adversarial-review.md` link depth fix (2026-08-10 — `../../` resolved to `.claude/docs/`, one level short; **until 2026-08-11 no checker covered `.claude/`**, so the revert was undetectable — `scripts/check_docs_links.py` now scans it, advisory and standalone, so a hand run catches a reverted broken link though nothing in CI runs it) | — |
| **`intake`** | **the entire Phase 2 intent map** — the seven-part provenance separation, the retrieval step, the LOW/MEDIUM/HIGH classes and `INTENT STATUS` — **plus the § 4.8 fresh-agent test result note in the replay section (2026-08-12, fm #851)**. The staged copy at `.substrate/skills/intake/SKILL.md` still contains the superseded `FULLER PICTURE` body, **verified 2026-08-09**, so the copy loop reverts Phase 2 in one command | 2026-08-09 |
| `prep-owner-steps` | the 10-line **Venue note** (`control/` is seat-era historical here; card + PR description are the live venues; owner-ratified 2026-08-05) | 2026-08-04 |
| `release` | the same 10-line Venue note | 2026-08-04 |
| `scope-backlog-item` | the same 10-line Venue note, **plus** step 5's baton retarget to the live venues (2026-08-11 — the staged step writes the baton into retired `control/status.md` and calls that the whole output) | 2026-08-04 |
| `quality-gate` | step 1/2 split corrected (staged copy names `bootstrap.py check --strict` twice and never mentions the false-wall guard) **plus** the 2026-08-11 coverage note — reverting deletes the skill's only pointer to `tools/check_no_false_walls.py` | — |
| `upgrade-distribution` | step 7 verifies `tools/check_no_false_walls.py --strict` explicitly beside the gate (staged copy names the gate twice) | — |

⚠⚠ **This bites on the very next session**, because the owner's live decision is
*upgrade the kit first*. Anyone running that upgrade must re-apply `intake`
afterwards, or the roadmap and both ledgers will go on claiming a procedure the
tree no longer contains.

**Amended 2026-08-09 (fm #833) — right in substance, wrong about the trigger.**
The upgrade ran, and `intake` **survived it byte-for-byte**. `upgrade` only
re-stages `.substrate/skills/` (14 skills, `intake` among them); **no kit command
writes `.claude/skills/` at all** — `skills --build` also only stages, per
`cmd_skills`' docstring. **The destroying action is the `cp` loop above, run by
hand.** So the warning stands and its urgency is unchanged — the staged body
carries **0** of the Phase-2 markers against **8** in the live one — but it fires
on *running the loop*, not on *running the upgrade*. A session that upgrades and
then re-applies `intake` "to be safe" is re-applying over an unchanged file and
reporting a fix that fixed nothing.

## Generated-file corrections to re-apply (kit-owned, clobbered at upgrade)

These live in files the kit regenerates, so they are lost at the next upgrade
and belong on this list beside the skills above.

| file | correction | why |
|---|---|---|
| `.github/workflows/substrate-gate.yml` | the `repo checkers` step · the `--session-log` sentinel on the verify-suite step · the `env:` block on the claims-only guard | `bootstrap.py:20048` rewrites this file unconditionally. Without the first, neither checker runs in CI; without the second, a `main` push can select a historical `in-progress` card by mtime and go falsely red; without the third, a PR-author-chosen branch name is interpolated into shell and can `exit 0` past the guard (all three: Codex, fm #833) |
| `docs/CAPABILITIES.md` (inside the `capability-seed` fence) | the three **RETRACTED** wall rows — tag push/release create, branch deletion, `api.github.com` (2026-08-11, the audit's headline finding 2) | the rows sit **inside** the kit-owned seed fence, which "refreshes at upgrade between the fence markers" per the fence's own note — an upgrade may restore the false walls the append log at `:775`/`:888` refutes. If restored: re-strike them, or verify the kit seed itself was fixed (the durable fix, filed for v1.21.0). `docs/seat-digest.md`'s walls digest is a derived render of the same rows — regenerated 2026-08-11 from the corrected ledger, so it carries the retractions; if an upgrade reverts the seed rows, a `seat-digest` regen re-propagates the stale rows there too, so re-check both |

**`docs/SKILLS.md` is NOT on this list, and the reason corrects an error of
mine.** A first version of this table listed it as upgrade-clobbered, reasoning
from the file's own header (*"Generated by substrate-kit … regenerates at
adopt/upgrade, so it cannot hand-drift"*). **The engine does not behave that
way.** Planted docs are classified first: `classify_planted_docs()` marks a
touched file `consumer-edited`, and `apply_doc_improvements()` writes only
`consumer-untouched` ones. This upgrade's own report says so in one line —
`.substrate/upgrade-report.md:23`: *"docs/SKILLS.md | consumer-edited | template
unchanged — consumer-owned, nothing to apply"*. **Only the workflow is rewritten
unconditionally**, because `:20048` is the *workflow* writer, not the planted-doc
path, and conflating the two is what put SKILLS.md here.

**Listing it would have manufactured a false-done** — a future session
"re-applying" a correction that was never lost, then reporting it done. Caught by
Codex (fm #833, P2), inside the very table built to prevent that class.

**The durable fix for the workflow rows is upstream in the kit**, not here —
filed for the v1.21.0 session.

**How this was found is the argument for the warning existing at all:** Codex
caught it on fm #830 (P1). This section's author had read this very paragraph
while adding a section 60 lines above it, and still shipped a kit-named skill
amendment without adding it here. *A warning in the file you are editing is not
self-applying.*

The durable fix is upstream: propose the generalisable half to the kit so it
ships to every adopter instead of living as a local patch that each upgrade
silently reverts. For `intake` that is explicitly roadmap § 7's allocation —
substrate-kit owns *generalised intent resolution*, so the map belongs there once
it has earned promotion.

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

## Where these 27 are visible — and where they are not

**The owner asked why the skills we built here do not appear in the claude.ai
Skills settings list** (2026-08-09, with a screenshot showing only `morning` and
`skill-creator`, both Anthropic-authored). The answer is that there are **two
registries**, and committing a skill to a repo does not upload anything.

| scope | where it lives | what reads it |
|---|---|---|
| **project** — all 27 of these | `<repo>/.claude/skills/<name>/SKILL.md`, in git | Claude Code sessions whose **root** is that repo, and cloud sessions on the cloned repo |
| **personal** | `~/.claude/skills/<name>/SKILL.md` on one machine | that machine's Claude Code, all projects |
| **account** | uploaded to the claude.ai account | claude.ai chat, Cowork (interactive **and** scheduled), Routines — and this is the list the settings page shows |

Scope rows are from
[the skills doc](https://code.claude.com/docs/en/skills); the rest of this
section is `MEASURED` on this container, 2026-08-09.

**What is actually here.** `CLAUDE_CODE_SYNC_SKILLS=1` syncs the account set into
`/root/.claude/skills/`, which holds **8** entries whose `manifest.json` tags
each `"source": "anthropic"` or `"anthropic-example"` — the two `-example` ones
are exactly the two rows on his settings page. Probed directly: `intake`,
`capability-probe`, `session-close`, `owner-brief` and `image-prompt` are all
**absent** from that tree. They are not hidden or filtered; they were never
uploaded.

**This is the boot triad's case two wearing different clothes.** The boot file
already records that a session rooted on a satellite repo gets *1 skill instead
of 27* — same cause, different venue. The account registry is simply a third
place the project-scope boundary shows.

### Three routes, and what each one costs

1. **Upload per skill to the account** — **Customize → Skills → `Add`**, taking a
   ZIP whose root is the skill folder: `<name>.zip` → `<name>/` → `skill.md`
   ([owner-supplied support article](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills),
   2026-08-09). Reaches claude.ai, Cowork and Routines. Supported on all plans
   and requires code execution enabled.

   **The blocker is the description length, and it is measured.** Uploads cap
   `name` at 64 characters and `description` at **200**. All 27 use only `name`
   and `description` — inside the six fields uploads accept (`name`,
   `description`, `license`, `compatibility`, `metadata`, `allowed-tools`), where
   a seventh field is a hard error rather than a warning — but **15 of the 27
   descriptions are over 200 characters** (`MEASURED` 2026-08-09; worst:
   `delegate-read` 384, `owner-brief` 300, `capability-probe` 300). Names are all
   within 64.

   *(An earlier version of this section said no frontmatter work was needed. That
   checked which **fields** were present and inferred eligibility without
   checking the limits on their **values** — a conclusion drawn one step past the
   measurement, which is the class this repo keeps cataloguing. Corrected the
   same day.)*

   **Do not shorten the sources to fit.** The description is what a session
   matches against when deciding whether a skill applies, and Claude Code imposes
   no limit — trimming 15 of them would degrade the surface that works today for
   one that has not been adopted yet. If route 1 is taken, the shortening belongs
   in a packaging step that emits an upload-safe variant. `UNVERIFIED`: whether
   `package_skill.py` does this itself or simply rejects, and whether the
   uploader accepts our `SKILL.md` where the article writes `skill.md`.

   Cost of the route overall: a manual copy that drifts from git the moment
   either side changes, and an account-level skill competes for match in **every**
   session everywhere.
2. **The Skills API / `package_skill.py`** from `anthropics/skills` — the
   scriptable form of route 1. Not attempted here; no Anthropic API key is
   present in this container (`ANTHROPIC_BASE_URL` is set, no key), so the
   credential path is `UNVERIFIED` rather than known-absent.
3. **Ship them in a plugin declared in each repo's `.claude/settings.json`** —
   the docs state repo-declared plugins install at session start, while plugins
   enabled only in user settings do not transfer. Git-native, versioned,
   reviewable, no manual drift.

### The recommendation, and what is still the owner's call

**Not all 27 should travel.** An account-level skill loads everywhere, so the
repo-coupled ones would misfire: `session-close` drives this repo's §7 ledger and
NOW pointer, `release` and `upgrade-distribution` are substrate-kit procedures,
`repo-health` runs this bootstrap. The portable ones are the *method* skills that
describe how to work rather than where — and five of the eight need an
upload-safe description before they can go anywhere:

| portable candidate | description chars | upload-ready? |
|---|---|---|
| `chase-references` | 174 | ✅ |
| `prep-owner-steps` | 171 | ✅ |
| `rationalize` | 158 | ✅ |
| `decision-capture` | 226 | ✂ needs trim |
| `intake` | 262 | ✂ needs trim |
| `prompt-preflight` | 286 | ✂ needs trim |
| `capability-probe` | 300 | ✂ needs trim |
| `delegate-read` | 384 | ✂ needs trim |

**Route 3 is the one that fixes the estate's actual defect**, because case two is
about satellite *repos*, not about claude.ai — and a plugin declared in a
satellite's settings is the only one of the three that follows the repo. Route 1
is the right answer to the narrower question he asked, and the two are not
exclusive.

**Open, and his to decide:** whether to build the plugin, and which skills go in
it. Recorded rather than built — a plugin is new apparatus, and § 5 of
[`intent.md`](intent.md) names "an apparatus that needs maintenance sessions of
its own" as a non-goal, so this one needs a yes rather than an inference.

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
