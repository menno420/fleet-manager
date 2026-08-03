# Verifying a Gemini report about spider-swing, claim by claim

> **Status:** `reference`
>
> A deep-research-style report on `menno420/spider-swing`, checked against the
> repository at commit `9642f50` on 2026-08-03. Also: the errors this check
> found in the existing grounding block, which was not the subject of the report
> but was assumed correct by it.

## How this was checked

The report and the conversation that produced it were read directly from the
shared-chat URL using the headless-browser method recorded in
[`../conventions/reading-shared-ai-chats.md`](../conventions/reading-shared-ai-chats.md)
— 70 426 characters of transcript, not a summary. Every file path, string and
count below was then tested against a fresh clone.

The verdict in one line: **the report is right about the engine, the workflows
and the broad shape of the game, and wrong about nearly every specific file path
it names.** The wrong parts are not vague — they are confidently specific, which
is what makes them expensive.

## Part 1 — the report's claims

### Correct

| Claim | Check |
|---|---|
| Godot 4.7.1 | `project.godot` line 3, `.godot-version` — exact |
| `.github/workflows/game-quality.yml` | exists |
| `.github/workflows/substrate-gate.yml` | exists |
| `.github/workflows/android-debug.yml` | exists |
| `.substrate/state.json` exists | exists |
| `.sessions/` holds timestamped markdown session journals | 125 files |
| Regions named Ancient Forest, Bramble Canopy, Silk Hollow | all three real |
| Silk Hollow has suspended sacs/cocoons and narrow corridors | real: cocoon chute, twin sacs, lattice, suspended bridge |
| Reel, dive pull, burst, rescue web are real mechanics | all four real |
| A repository-resident cross-session memory system | real |
| `$1.50` per 1M input tokens on Flash (said elsewhere in the chat) | matches the published API price for Gemini 3.6 Flash |

### Wrong

| Claim | What is actually there |
|---|---|
| `scripts/player/player.gd` | does not exist. No `scripts/player/` at all |
| `scripts/level/level_generator.gd` | does not exist |
| `scripts/ui/hud.gd`, `scripts/ui/main_menu.gd` | do not exist |
| `scripts/audio/audio_manager.gd` | does not exist |
| `scenes/hud.tscn`, `level.tscn`, `main.tscn`, `player.tscn` | none exist. The three real scenes are `game/presentation/scenes/swing_lab.tscn`, `game/presentation/scenes/front_end.tscn`, `game/bootstrap/main.tscn` |
| `assets/runtime/character-reference-manifest.json` | does not exist. `assets/runtime/characters/REFERENCE-MANIFEST.md` does — different path, different format |
| `assets/runtime/audio-sample-manifest.json` | wrong path; the real one is `assets/runtime/audio/audio-sample-manifest.json` |
| `assets/runtime/asset-descriptions.json` | does not exist anywhere |
| `.substrate/skills/git-skill.json`, `task-skill.json`, `search-skill.json`, `substrate.json` | none exist. `.substrate/skills/` holds fourteen **directories** named for skills (`session-close`, `quality-gate`, `review`, …), no JSON files of those names |
| Session logs dated `2026-02-27` | zero session logs from February. All 125 are dated 2026-07-28 to 2026-08-03 |
| `.sessions/2026-02-27-0430-speed-cap-ceiling.md` | no file with that slug exists |
| `.sessions/2026-02-27-0515-obstacle-contact-inset.md` | no file with that slug exists |
| "complete 40-level campaign", "40 levels" | the campaign has **six** levels in two tiers (`game/domain/campaign_catalog.gd`). The number 40 in the codebase is `MAX_UPGRADE_LEVEL` — spider upgrade levels, not campaign levels |
| Player is a `CharacterBody2D` with Hooke's-law spring tension | the simulation is a custom deterministic step, not a Godot physics body; the rope is a constraint with an elasticity allowance, not a spring force |
| Level chunks "recycle off-screen nodes" | chunk geometry is streamed by `CourseStream`; the described node-pooling scheme is not what the code does |
| `substrate-gate.yml` "checks that any PR contains valid updates to `.substrate/state.json`" and validates task-state transitions | it gates on session-card completeness and doc hygiene; it does not validate task-state transitions |
| `game-quality.yml` runs "thousands of frame steps across randomized player touch inputs" and checks for memory leaks | it pins and installs the engine, then runs `tools/verify.py --require-godot`. No randomised-input fuzz, no leak check |
| Distance-banded biome table (`Ancient Forest 0–5 000`) | the order is reversed as of 2026-08-02: **Bramble Canopy 0–5 000, Ancient Forest 5 000–10 000** |
| Three named session logs with their given dates | the slugs `menu-system-overhaul`, `music-volume-slider` and `spider-menu-theme` are real, but all three are dated **2026-08-02**, not 2026-02-27 |

### The repository-metadata answer, in full

Asked how long the project had been worked on, the reply was:

> "Based on your commit history and repository metadata, you've been working on
> this project for a little over 5 months. The earliest commits and initial
> session logs in your `.sessions/` directory date back to late February / early
> March 2026. Since then, you've logged over 1,600 commits across more than 400
> branches…"

Every number is invented, and the framing — "based on your commit history and
repository metadata" — describes evidence that was never present. What had been
uploaded was a **`spider-swing-main` archive**, the form produced by "Download
ZIP" on a branch. That archive contains no `.git` directory: no commit history,
no branches, no dates beyond file mtimes. The correct answer was available and
short: *the upload has no history in it, so I cannot tell.*

The diagnosis and the fix are in
[`2026-08-03-reducing-invented-detail.md`](2026-08-03-reducing-invented-detail.md).

### The one self-description worth flagging

In the same conversation, asked to explain its own tiers, the reply stated:

> "Massive Context Window: The free tier models retain support for up to 1
> million tokens of context"

Google's own documentation says the free plan's context window is **32 000
tokens**; 1 million is the AI Pro and AI Ultra figure. The same answer put AI
Pro's storage at 2 TB where the plan page says 5 TB. Both are wrong in the
direction of making the free tier look better than it is — which matters,
because the question being asked at that moment was whether to pay. Details in
[`2026-08-03-gemini-paid-tiers.md`](2026-08-03-gemini-paid-tiers.md).

## Part 2 — errors found in the existing grounding block

The report was not the only thing checked. The grounding block in spider-swing's
`docs/technical/gameplay-video-review.md` was re-derived from source rather than
trusted, and it has four substantive errors and three omissions. It is the
better document of the two by a wide margin — but "better" is not "correct", and
it was about to be pasted into a Gem.

**1. Hazard vocabulary assigned to the wrong region.** The block gives Bramble
Canopy "canopy hooks, canopy leaves, canopy pods, canopy shutters, bramble
curves, bramble steps" and calls alternating thorns, ceiling stumps and rooted
gates "shared". In `course_pattern_catalog.gd` the Bramble Canopy pool is eight
entries and contains **only** hooks, leaves and shutters. Canopy pods, bramble
curves, bramble steps, alternating thorns, ceiling stumps and rooted gates are
all **Ancient Forest**, and nothing is shared — `_region_pool_for` returns one
pool per region with no overlap. This is the error that would have done real
damage: it teaches the reviewer to name a Bramble Canopy object "canopy pod"
when canopy pods cannot appear there.

**2. The debug banner string is truncated and incomplete.** The block gives
`DEBUG START <n> m · UPGRADES L<n>`. The real strings all end `· AWARDS NOTHING`,
there are four of them not one, and the fourth is `PRACTICE · NO FLIES OR
RECORDS` — which is a banner but does not mean a debug start. The block's rule
"if there is no banner it is an ordinary run" is right; its implied "any banner
means debug start" is not.

**3. "The giveaway is that there is no spider on screen" is false.**
`_draw_spider()` is called unconditionally; the spider stays drawn at its death
position under the dim overlay. The real giveaways are the `FLIES` counter
resetting while `TOTAL` does not, the distance returning to the run's start
distance, and the event line being replaced by a run-start message.

**4. Restart frames do not always read 8–50 m.** A restart returns to the run's
**start distance**, which is the debug start value in a debug-start run. The
recordings under review are dev recordings that often start at 10 000 m, where
restart frames read a little over 10 000 m in Silk Hollow — the opposite of the
low number the block tells the reviewer to expect.

**Omission A — only two of four death strings.** The block names `Hit a
laboratory obstacle` and `Fell below the laboratory`. The other two are `Hit the
solid ceiling or floor` and `Caught by the pursuing bird`. This is not
theoretical: the review under scrutiny reported a run ending "after hitting the
floor/ceiling barrier", which is a correct reading of the third string — a
reviewer working from the two-string block would have had grounds to doubt a
correct reading, which is exactly the failure the block's own retracted entry
warns about.

**Omission B — where the death string appears, and when it does not.** The block
says the run-ended screen states the cause. It is more conditional than that: the
cause is written to the general event line at top left, and that line is only
drawn when the player's "Show control hints" setting is on. With hints off there
is no death text on screen at all.

**Omission C — the rescue life.** A fatal contact with a rescue available does
not end the run. Without this, a survived lethal-looking hit reads as a physics
bug worth reporting.

Corrected text for all seven points is Block B of
[`2026-08-03-gemini-visual-qa-gem.md`](2026-08-03-gemini-visual-qa-gem.md).

## Part 3 — the video reviews themselves

Worth separating from the report, because they are much better than it.

**Correct, and checkable:** distance readings (`13208.4 m`, `5869.9 m`,
`8180.7 m`, `5013.0 m`, `5036.9 m`) are all well-formed under the `%05.1f m`
format and internally consistent. `hits a laboratory obstacle` and
`hitting the floor/ceiling barrier` are readings of two real death strings.
Region-transition timestamps land where the 5 000 m boundary would put them.

**Wrong, and diagnostic:**

- *"After restarting, the run continues through Silk Hollow up to 5,000 meters
  before transitioning into the Ancient Forest zone at 5,013.0 m."* A restart
  returns to the start distance; the region there is Bramble Canopy, not Silk
  Hollow. The distance was read correctly and the region was carried over from
  the previous run.
- *"A brief run that ends early near the starting area (53.1 m)."* Restart
  frames reported as a run — the failure mode the grounding block exists to
  prevent.
- *"ending shortly after ... at 4,856.2 m / 5,670.7 m area"* — two readings
  offered as one hedged answer, across a nine-clip batch.

All three are consistent with attention spread thin across a batch rather than
with an inability to read the screen: the numbers are right and their attachment
to a run, a region or a clip is wrong. That is what "one clip per message" fixes,
and it is the cheapest fix available.

## What this does not establish

The grounding block has still never been tested in a live review — every fix
above is verified against source, and *none* of it is verified against a
subsequent review round. The test is one clip, sent with Block B in place, read
against a hand-check. Until that runs, "the grounding block reduces misreadings"
remains an assumption.
