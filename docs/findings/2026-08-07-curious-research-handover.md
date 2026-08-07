# curious-research is now a gift being handed to its reader — what changed and why

> **Status:** `reference`
>
> Written 2026-08-07 by the session that did the work. This repo's registry
> entry (`projects/curious-research/`) still describes a kit-run seat with a
> heartbeat in `control/status.md`. **That is no longer true** — see § 3.
>
> Certainty here is plain: everything in § 1–4 was done and verified this
> session (PRs #53–#65, all merged). § 5 is in flight. § 6 is opinion, marked
> as such.

## 0 · Why this file exists

`curious-research` was seat 9 of the autonomous fleet — the teaching-and-research
seat, and the only one that was never a lab. It is **a gift for a person**: the
owner's weekend foster-father, a Dutch hobby maker.

Today it stopped being a repo the fleet maintains and became a repo *he* is about
to be handed, together with a Claude subscription and an introduction email. That
transition changed what the repo is for, and therefore what belongs in it. The
fleet's records should say so, because the registry copy still describes the old
shape.

## 1 · Who it is actually for

This matters more than any technical decision here, and getting it wrong is the
main failure mode. From his own words this week, relayed by the owner:

- **He is not new to Claude.** He uses it weekly already — Arduino code, 3D-printing
  tips, Fusion 360. The repo had been quietly built around *showing him what an AI
  can do*. He knows. He is new to **GitHub**, not to Claude.
- **What he does not have is persistence.** Every good answer he gets dies with the
  chat window. That is the repo's actual pitch and the only part that is news to him.
- **His hardware, confirmed:** a Bambu Lab **A1 mini** and an **A1 with AMS Lite**
  (so: Bambu Studio); **Fusion 360** free licence for *everything* — 2D for **laser
  cutting and CNC milling**, 3D for the printers; a busy Arduino bench; and a 6-DOF
  arm on **6 × MG996R** servos that is **already built, wired and moving under
  program control**.
- **He asked for something specific**, unprompted: how to load a Python program into
  Fusion 360. That is now `guides/fusion-python/`.
- **Low coding skill, high everything else.** He assembled the arm from a kit and
  solved its power supply correctly before the repo mentioned power at all.

### The failure mode, named twice

Twice today a session — this one — wrote an inference as a fact, and both times the
inference **flattered the repo at his expense**:

1. Assumed the arm kit shipped without a controller or PSU, and planned a "how to
   power your arm" guide. Video showed a proper enclosed switching supply and a
   distribution board. He had solved it months ago.
2. Shipped copy to the live site saying *"voordat de arm ook maar één keer
   beweegt"* and *"de software weigert elke beweging"*. His arm moves. What was
   true is only that **this repo's** tool refuses to start without a calibration
   file.

Both were caught by the owner, not by the session. `curious-research/CLAUDE.md` §0
now carries this as a standing rule with the example. **Any fleet doc that describes
a person's setup should assume the same trap exists.** The inference that makes your
work look more necessary is the one to check hardest.

## 2 · What was removed

The autonomous-fleet machinery, in full: `bootstrap.py`, `.substrate/`, the 37
`.sessions/` cards, `control/` with its ORDER/PROPOSAL protocol, `scripts/`,
`CONSTITUTION.md`, `LICENSE-substrate-kit`, `project.index.json`,
`substrate.config.json`, `.ignore`, `.gitattributes`, and sixteen generated `docs/`
files. **−41,399 lines.**

**The ordering mattered and is worth recording as kit-adopter guidance.**
`.claude/settings.json` had four hooks shelling out to `bootstrap.py`, one with a
`PreToolUse` matcher of `*`. A previous session deleted `bootstrap.py` with those
still wired, and every subsequent tool call in that session errored and was blocked —
it could not even read a file to diagnose itself, and was abandoned. **Un-wire the
hooks and commit that alone, before deleting anything.** That was done here as commit
`4210642`, ahead of every deletion.

`substrate-gate` was kept, workflow name and job id byte-identical, because a branch
ruleset on `main` requires that exact status-check context and a required check that
never reports leaves every PR pending forever. Its contents are now a relative-link
checker — the failure this repo actually suffers from. It caught two dead links on
its first run.

## 3 · What the registry entry now gets wrong

`projects/curious-research/meta.md` says the archetype is a *"kit-run coordinator
loop (substrate-kit ≥ v1.15.0, guided mode); heartbeat home `control/status.md` in
curious-research."*

None of that exists any more. There is no kit, no control lane, no heartbeat, no
seat. The generated prompt copies in the same directory (`coordinator-prompt.md`,
`failsafe-prompt.md`, `instructions.md`) describe a coordinator seat with a failsafe
cron; they are historical, like the rest of the seat-era apparatus that
`.claude/CLAUDE.md` already classes as record rather than truth.

**Not fixed here on purpose.** Those three are marked GENERATED COPY with a
regeneration path (`docs/prompts/v3/`), and editing generated files in place is how
drift gets baked in. Whoever runs consolidation step D4 should either regenerate them
or retire the entry; this file is the note that says the underlying repo moved first.

## 4 · What the repo is now

- **15 guides** in `guides/`, each an animated `index.html` plus a step-by-step
  `guide.md`. New ones are written in Dutch; the nine older English ones stay and get
  summarised in Dutch on demand.
- **5 buildable projects**, including one added today: `arm-soepele-beweging/`, which
  fixes the burst motion the owner spotted in video of the arm. `servo.write()` has no
  speed input, so smoothness has to be generated in software — stream nearby targets at
  50 Hz, give every joint one shared duration, and ease in and out with `3t²−2t³`.
- **A live website**, https://menno420.github.io/curious-research/ — plain HTML/CSS,
  no build step, deliberately readable on a phone with no account and no subscription.
  It carries a shelf of every guide and a `kennis.html` reference with topic tabs,
  collapsible sections, short cards, and a **confidence badge per card**
  (ZEKER / MEESTAL / BETWIST) with a source link.
- **`research/deep-research-prompts.md`** — six self-contained deep-research prompts
  with a fixed output contract: cards of ≤120 words, a real number each, a source URL,
  a confidence mark, and a mandatory *"myths and outdated advice"* section.

### Two findings other repos in this estate can use

**GitHub Pages cannot be enabled by a workflow.** `actions/configure-pages@v5` with
`enablement: true` fails with *"Create Pages site failed. Error: Resource not
accessible by integration"*. A workflow's `GITHUB_TOKEN` can **deploy** to an existing
Pages site but cannot **create** one, even with `pages: write` — creation needs
repo-admin rights. The one-time switch really is a human action. Do not burn runs
rediscovering this.

**Auto-merge with `GITHUB_TOKEN` silently suppresses downstream workflows.** Five PRs
merged in a row here and the `pages` workflow ran **zero** times. Every check was
green and the live site sat half a day stale, including a correction that was the
whole point of the PR before it. Cause: GitHub suppresses workflow runs for events
triggered by `GITHUB_TOKEN`, and `auto-merge-enabler.yml` falls back to it when no
`ROUTINE_PAT` secret exists. Confirmed from run history — `substrate-gate` has
push-triggered runs on `main` from July, when merges were manual, and none since.
**Any repo in this estate using the kit's auto-merge enabler without `ROUTINE_PAT`
has the same hole.** Mitigated there with a two-hourly `schedule`; the real fix is the
secret.

## 5 · In flight

Twelve deep-research runs are out — the six prompts, sent to both ChatGPT deep
research and Gemini deep research. Results land in `research/dossiers/` in English
(agent-facing), then get **cut**, not translated, into Dutch cards on the site.
`lasersnijden` and `frezen` are currently visible, deliberately empty tabs — an
honest blank beats plausible filler on topics involving fumes and spinning cutters.

Then an introduction email from the owner, with a Claude subscription.

## 6 · One opinion, marked as opinion

`docs/CAPABILITIES.md` here treats a proxy 403 as a false wall to route around with
`curl --noproxy '*'`. That framing is right about **GitHub's** permissions — the PAT
genuinely has the scope — and wrong about what the proxy is. The proxy is not
misreporting a GitHub boundary; it is correctly reporting its own, and it belongs to
the session runtime rather than to this estate. A session that declines to bypass it
currently finds no documented alternative in these docs and may conclude it is stuck.
It is not: the GitHub MCP tools handled every operation needed today — merging,
dispatching workflows, reading job logs, opening PRs — through a sanctioned channel.

Two suggestions, take or leave:

1. **Separate the two failure classes.** A proxy 403 and a GitHub
   `Resource not accessible by integration` look alike and mean opposite things. The
   second is a real boundary and should be recordable as one — as § 4 above shows, the
   estate hit a genuine one today.
2. **Document the MCP path as the sanctioned fallback**, so declining `--noproxy` is a
   route rather than a dead end.
