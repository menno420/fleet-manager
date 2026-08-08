# spider-swing — the entry point

> **Status:** `living-ledger` · true as of **2026-08-08**
>
> **What this is:** fleet-manager's entry point for `menno420/spider-swing` —
> where the last session left off and where the next one should look.
> **Canonical for nothing.** The repo's own `docs/current-state.md` wins on its
> state, its `docs/architecture.md` wins on its design, and the live tree wins
> over both. This file summarises and points; when it disagrees with the repo,
> the repo is right and this file is stale.
>
> Certainty tags per
> [`../../findings/2026-08-05-foundation-continuation.md`](../../findings/2026-08-05-foundation-continuation.md).

## The one-paragraph answer

**Slingy Spider** is an Android-first 2D physics swing game in Godot 4.7.1 /
GDScript — a spider swings by attaching silk to anchors, and a pursuing bird
enforces pace. `MEASURED` 2026-08-08 against the GitHub API: `menno420/spider-swing`,
**public**, default branch `main`, created 2026-07-28, last pushed 2026-08-07,
~47 MB, 1 open PR (a Dependabot bump) and 1 open issue (#2, the Phase-0 Swing
Laboratory). `spider-swing` is the **repo** name and internal codename; **Slingy
Spider** is the publishing name, decided 2026-08-05.

**Why it gets Tier 1 depth:** it is the only asset in the estate with a **live
external signal** — returning players and unprompted difficulty feedback — and
`OWNER`, per the consolidation program, every owner evening since 2026-07-26 has
gone to it. Program step E1 is deferred *because of* this repo, and the program
records that as triage, not neglect.

## Where it stands right now

**The main point of importance: the game is not yet fun enough to test, and the
test has a three-week floor.** Those two facts are in tension and they are what
any new session is walking into.

The owner's north star (`OWNER`, 2026-08-02, quoted from the repo's own
`docs/current-state.md`) is to *"tune core feel, difficulty and upgrade impact
until excellent play can meaningfully reach 25 k+"* — and the game is still
*"too difficult and moves too quickly"* for that to feel achievable. Unlock
systems, expanded Campaign trees and deeper monetisation are **deferred by
directive** until the core loop is right.

Meanwhile the Play release path cannot be compressed: a personal developer
account created after 2023-11-13 must run a **closed test with 12 testers opted
in for 14 continuous days** before it may even *apply* for production, then wait
~7 days for review. Finished code does not shorten it.

## Threads

### Thread: core feel & difficulty — **active**, updated 2026-08-02 (owner directive)

Where it stands: build `0.44.0-run-evidence` is current. Continuous drive is
zero; release, swing control, Reel and pull timing earn speed; the former left
kill line is now a visible pursuing bird. The simulation bot still cannot tune
the bird — model v4 pumps but sustains far below the reference pace in the band
where the owner actually plays — so Test Run owns three session-only chase
controls as a stopgap.

Pointers (all in spider-swing):
- `docs/current-state.md` — the north star and the stability baseline. **Start here.**
- `docs/game-design/earned-speed-and-the-bird.md` — the earned-speed specification.
- `docs/planning/next-session-brief-2026-08-01-mechanics.md` — the measured design and its seams.
- `docs/product/player-preference-research-2026-08-02.md` — the evidence, the hard monetisation boundaries, and the parked work.
- `docs/product/upgrade-and-difficulty-research-2026-08-02.md` — external benchmarks + the verified zone audit.

Next step: this is a **tuning** thread, not a building one. The run-evidence
system below now exists precisely to make it measurable, and nothing has yet
used it for a tuning pass. That is the obvious first move.

### Thread: Google Play release — **active, owner-gated**, updated 2026-08-05

Where it stands: the buildable half is done and the calendar is the blocker.
The repository targets API 36 (Play requires it from 2026-08-31, so this is
satisfied), release signing was repaired after the first real build failed
(#169), the closed-test runbook, privacy policy, Console answer sheet and
listing copy are drafted (#163), and the tester-recruiting route was corrected
from fetched sources (#170).

What is genuinely waiting on the owner — these are **his**, tracked with stable
slugs in [`../../owner-queue.md`](../../owner-queue.md), and a session should
not try to route around them:
- `OQ-PLAY-APP-ID` — the application ID, recommended `com.menno420.slingyspider`.
  Permanent and non-reusable; set on the Play Console *Create app* form.
- `OQ-PLAY-UPLOAD-KEY` — generate the upload keystore and store it as secrets.
- `OQ-PLAY-LISTING` — **promoted to the critical path**: a release cannot roll
  out to a closed track until the listing, App content and pricing are complete,
  so the icon, feature graphic and screenshots gate the 12-tester clock rather
  than following it. Copy is drafted; the **screenshots must be real capture**
  (the `android-debug` workflow builds an installable APK on every push to
  `main`), because generated imagery invents UI and physics.

Also open, and not blocking: the trademark search (BOIP + EUIPO, Nice classes 9
and 41) is the only unresolved part of the name.

Pointers: the requirements with every URL fetched first-hand are in this repo at
[`../../findings/2026-08-05-google-play-submission-requirements.md`](../../findings/2026-08-05-google-play-submission-requirements.md);
the runbook, listing copy and answer sheet live in spider-swing under
`docs/product/`.

Next step: nothing in this thread is agent-executable until the owner completes
`OQ-PLAY-APP-ID` and `OQ-PLAY-UPLOAD-KEY`. A session that wants to help this
thread should produce **real device captures** for the listing, which is the one
part it can do.

### Thread: run evidence — **closed 2026-08-06** (spider-swing #172, #173)

Closed deliberately and recorded because it is what makes the difficulty thread
measurable. Shipped a schema-1 `RunRecord` + `RunRecordLedger` (newest 100 full
records, plus lifetime totals and per-difficulty bests), a pure
`RunMetricsAccumulator` shared by live play and `tools/simulate.gd`, a
mobile-readable Run History destination, and a manual JSON export — with **no
analytics, identity, upload or leaderboard logic**, by explicit scope guard.

Why that scope guard matters downstream: the Play *Data safety* declaration is
"no data collected" because Google defines *collect* as transmitting **off** the
device, and `game/` has no network API at all. The owner's separate statement
that the game retains run data is also true — they are different questions. A
future leaderboard release changes this answer and carries a hard gate.

### Thread: generated art pipeline — **paused**, last active 2026-08-04

Where it stopped: the art is in good shape and the *method* has been extracted.
33 audited zone assets and 5 spider sprites ship with **zero chroma fringe
pixels on 32 of 33** runtime assets (the exception, `silk-hollow-floor-wall`,
carries 46).

What would resume it: a new zone, a new spider, or store art for the listing
(the feature graphic may be generated; screenshots may not).

Read before generating anything for this repo — the discipline is non-obvious
and was measured here:
[`../../findings/2026-08-04-generated-art-pipeline.md`](../../findings/2026-08-04-generated-art-pipeline.md),
and its executable form is the `image-prompt` skill family. Two traps in
particular: **despill at full resolution** (downscaling does not introduce
chroma — the fringe was always there, resize only changes its proportion), and
**key by sampling a corner pixel, never by matching the hex you asked for**
(measured fields sat near `#22C022` and `#3E8E3E`, none within tolerance 40 of
`#00FF00`).

## Before you attach it

The repo is **public**, so read-only questions do not need `add_repo` at all —
raw fetch answers them:
`https://raw.githubusercontent.com/menno420/spider-swing/main/<path>`.
Attach when you intend to **write**, or when the job needs a real tree (running
`tools/verify.py`, the Godot engine, a build, or a wide grep). At ~47 MB with
142 session cards, it is not a cheap attach for a lookup.

## Once attached — the per-repo boot path

spider-swing ships its own orientation, and it is better than anything this
folder could restate. Read in this order:

**It is a substrate-kit adopter with the standard doc set** — every file below
carries the kit's generated header, so the shape is the same one you already know
from this repo. Badges below are each file's own `Status:`, checked 2026-08-08.

| file (in spider-swing) | badge | what it is |
|---|---|---|
| `CONSTITUTION.md` | `binding` | the working agreement + autonomy rails |
| `docs/architecture.md` | `binding` | layering, invariants and decomposition rules — **the second binding contract, and easy to miss** |
| `docs/current-state.md` | `living-ledger` | north star, stability baseline, current build. **Start here** |
| `docs/AGENT_ORIENTATION.md` | `reference` | the **task reading-router** — start here to find which docs a given task needs. It routes; it is not itself the instruction set |
| `docs/repo-navigation-map.md` | `reference` | where things live; where new code goes |
| `docs/decisions.md` | `living-ledger` | append-only decision ledger; rule docs cite entries as bare **`[D-NNNN]`** ids, superseded never deleted |
| `docs/CAPABILITIES.md` | `living-ledger` | **its** capability ledger — different file, different scope from ours |
| `docs/reading-path.md` | `reference` | its cross-repo read rules — note its standing rule that **writes stay in that repo** |

For how to work *on* it — gates, verify commands, the traps — see
[`working-here.md`](working-here.md) in this folder, which is the part you want
**before** attaching.

## How much of the repo this was built from — `MEASURED` 2026-08-08

Stated because a handoff that hides its own basis invites over-trust, and
because the answer is **"very little of the repo, most of the records."**

spider-swing is **732 files** — 305 markdown (2.12 MB), 120 under `game/`, 76
GDScript, 207 assets, 142 session cards. This folder was built from:

- **Three files, partially read** (~180 lines total): `docs/current-state.md`,
  `docs/reading-path.md`, and the newest session card
  `.sessions/2026-08-06-run-evidence.md`.
- **Structural metadata, complete**: the full tree, both directory listings,
  every workflow, the rulesets and effective branch rules, open issues and PRs,
  the last 12 merged PRs, and repo metadata — all live from the API.
- **28 files in fleet-manager**, read properly. That is where most of the
  narrative here comes from, and it is the half this repo is canonical for.

**What that means for how to read this folder.** The *state* claims are
strong — they come from spider-swing's own ledger and from live API reads. The
*pointer* claims were checked for existence and badge, but *"what it is"* for a
file this session did not open is a one-line inference from its header. Three
were wrong on first writing and were corrected on 2026-08-08 after checking:
`AGENT_ORIENTATION.md` is a reading-*router* rather than an instruction set,
`docs/decisions.md` cites `[D-NNNN]` ids rather than ADRs, and
**`docs/architecture.md` is a second `binding` contract** that the first draft
listed as ordinary reference.

Nothing under `game/`, `assets/`, `tests/`, `tools/` or `docs/product/` has been
read from here. **The repo always wins** — that is the rule at the top of this
file, and this section is what makes it concrete rather than polite.

## Why this folder has the files it has

The design named `current-state` / `capabilities` / `goals` / `records` as a
starting shape and asked each repo to earn its files. For spider-swing:

| file | verdict |
|---|---|
| `README.md` | **kept** — the standalone entry, and it carries the thread blocks |
| [`capabilities.md`](capabilities.md) | **kept** — spider-swing-specific measurements are scattered across a 1,638-line ledger, `execution-surfaces.md` and a dozen session cards; consolidating them is real value and is *not* a copy of the repo's own `CAPABILITIES.md` (that one is about working *in* it; this one is about reaching it from here) |
| [`records.md`](records.md) | **kept** — 28 dated files in this repo mention spider-swing and nothing indexed them. This is the one thing fleet-manager is genuinely canonical for |
| [`working-here.md`](working-here.md) | **kept — ratified 2026-08-08.** Gates, verify commands and conventions are what a session needs *before* attaching, and they are neither state nor goals. Proposed here as a new shape; the owner kept it distinct, so it is part of what every folder replicates |
| `current-state.md` | **DEFERRED** — it would duplicate the thread blocks above, and two files answering "what is true now" is exactly how drift starts. The threads *are* the current state; if a repo ever has state that is not thread-shaped, add it then |
| `goals.md` | **DEFERRED** — the north star lives one line from the top of this file and the owner-gated asks have stable `OQ-` slugs in `owner-queue.md`, which is where the owner already looks. A third copy of an objective is a third thing to keep in sync |

Both deferrals are **recorded, not silent** — the next session inherits the
reasoning instead of re-deriving it, and either file can be added the moment a
repo genuinely needs it.
