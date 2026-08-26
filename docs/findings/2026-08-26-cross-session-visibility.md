# 2026-08-26 — how much of a local session's work a cloud session can actually see

> **Status:** `reference` · certainty labels per the
> [legend](2026-08-05-foundation-continuation.md).
>
> **The question, his words:** *"how is the cross session coordination going?
> What I mean by that is, how well does a cloud session understand what the
> local sessions have been doing?"* — owner, 2026-08-26, hub chat.
>
> **The answer in one line: `MEASURED` — barely, and the failure is structural
> rather than a matter of anyone forgetting.** A cloud session booted in
> fleet-manager sees this repository's session cards and nothing else. The fix
> built the same day is [`../activity/`](../activity/README.md).

## 1 · What a cloud session could see, before this

`MEASURED` 2026-08-26, all figures from the live account over the direct-PAT
path (`GET /user/repos`, `GET /repos/{o}/{r}/contents/.sessions`).

| channel | what it carries | what it misses |
|---|---|---|
| `fleet-manager/.sessions/` — **418 dated cards** (the directory README is not one) | every session that ran **in this repo** | every session that ran anywhere else |
| `docs/current-state.md` | hub state, hand-maintained | only what a hub session chose to write |
| `docs/repos/<name>/` (Layer 2) | per-repo handoff threads | updated by the session that worked the repo, **if** it ran the step |
| `docs/ESTATE.md` | every repository, one line | **was missing `creator-kit` entirely** |
| git history | **the 52 commits present in this container's clone, which is shallow** (`.git/shallow` exists; `main` has 966) — one author and one committer across all 52, `Menno van Hattum` / `GitHub`, every one squash-merged | nothing distinguishes a local push from a container push. **Scoped to the sample**: the first version of this row said "50 commits" as though it described the repository, which a shallow clone cannot support (`@codex`, fm #947). The conclusion is unchanged — a squash merge carries no trace of the machine either way |

**In the seven calendar days to 2026-08-26 the estate wrote 74 session cards
across six non-archived repositories. A fleet-manager cloud session could reach
54 of them** — the ones in its own tree. **The other 20 could not be reached
from here by any path a session would take unprompted**: `websites` 9,
`couch-legend` 7, `product-forge` 2, `sim-lab` 1, `idea-engine` 1.

*(An earlier version of this paragraph said 43 and 31. Those were written from a
hand count, not from the generated table sitting in the same commit, and
`@codex` caught the arithmetic against the artefact. Every figure here now comes
from [`../activity/estate-log.md`](../activity/estate-log.md), which is
regenerated rather than remembered — the only fix that has ever worked here.)*

## 2 · Three separate gaps, and they need three different fixes

**Gap 1 — no aggregation.** Every kit repository keeps excellent per-session
records; nothing ever reads them together. The cards were not missing, they were
**unreachable from the router whose job is routing**.

**Gap 2 — no venue on any card.** `MEASURED` at `39c9d6e`, the commit this work
branched from: **0 of 418** dated cards in this repo carry a venue
(`git grep -l "📍 Venue" HEAD~2 -- .sessions/` → 0), and 0 of the 74 in the
estate-wide window do either. **418, not 419**: the directory's own `README.md`
is not a session card, and counting it inflated the baseline by one
(`@codex`, fm #947). The
card grammar has a `📊 Model:` line with a kit-validated three-segment taxonomy
(`model · effort · task-class`) and no fourth axis for *where*. So even a card a
session **can** read cannot answer the owner's question. A `GPT-5` card and an
`opus-5` card tell you the model, not the laptop.

**Gap 3 — work outside every repository leaves nothing at all.** This is the
largest one and the one his message is really about. The estate's whole memory
is git-shaped. Laptop setup, a ChatGPT sitting, a Gemini notebook, a Drive
reorganisation, an install — none of it produces a commit, so none of it exists
in the record. `docs/planning/2026-08-08-agent-operating-environment-roadmap.md`
§ 5.7 already names Drive, ChatGPT Projects and Gemini notebooks as parts of the
system's topology; **the table has no row for the owner's own machine**, which
is where he has spent the last several days.

## 3 · The proof case: `creator-kit`

`MEASURED`. `menno420/creator-kit` was created **2026-08-25T21:14:50Z** and
pushed once, two minutes later: *"Seed creator-kit: existing FreeCAD/Godot
tooling + substrate-kit 1.21.0"*. 111 files.

On 2026-08-26 it was **absent from `docs/ESTATE.md`** — the file whose header
says it names *"every repository the account holds"* and whose baseline reads
*"all 27 repositories verified against the live account"*. The account held 28.

The tree says where it was built. `Verify Creator Kit.cmd`, `freecad/Open
FreeCAD Library.cmd`, `godot/Open Creator Workbench.cmd` — Windows launchers and
a FreeCAD parts library. `REASONED`, not measured: a Linux container does not
produce those, and the owner has been setting up a Windows laptop in exactly
these days. Its `docs/current-state.md` is still the **unrendered kit
template**, every `${...}` slot unfilled — so the repository cannot answer for
itself either.

Nothing was done wrong here. A session did good work on the owner's machine and
there was **no surface to record it on**. That is the finding.

## 4 · What was built, and what deliberately was not

Built (fm #947): [`../activity/`](../activity/README.md) — a derived lane that
rolls every repository's cards into one index automatically, a hand-written lane
for the off-repo residue, a `📍 Venue:` token on the card protocol, and
`tools/estate_activity.py` to drive both. The generator's own "invisible work"
section is the part with teeth: it names every repository that **moved without
leaving a card**, which is how `creator-kit` surfaces at all.

**Not built, deliberately:**

- **No scheduled refresh.** A daily bot commit to `main` is the churn class the
  estate has been retiring (superbot #2450 retired the frozen-repo pollers). The
  refresh is on demand; scheduling it is the owner's call, not a default.
- **No venue enforcement.** The token is self-reported and nothing verifies it,
  because nothing **can** — a squash-merged commit carries no trace of the
  machine that produced it. The generator prints the stated-vs-total count so
  the coverage of the convention is visible instead of assumed. It began at
  **0 of 74**, and an honest null beats a guessed venue.
- **No backfill. The off-repo lane opens empty.** It was seeded with one
  reconstructed `creator-kit` entry and that entry was removed the same day
  (`@codex`, fm #947): it recorded a **commit**, which the lane's own contract
  sends to the repository lane, and `creator-kit` already appears in the
  generated invisible-work section. The reconstruction survives in § 3 above,
  where it is evidence rather than a ledger entry. Nothing earlier is invented,
  because a reconstructed diary reads exactly like a remembered one.

## 5 · What this does not solve

`MEASURED` where stated, otherwise structural.

- **A local session that never pushes stays invisible.** The derived lane reads
  pushed cards. That is a property of git, not a defect of this design.
- **Four non-archived repositories have no card protocol**, so no session in
  them can ever appear in the derived lane: `curious-research`,
  `estate-backups`, `spider-bot`, `superbot-plugin-hello`. **Every count in this
  finding and in the generated log is non-archived-only** — nine repositories
  were archived on 2026-08-23 and some carry cards from that very wave, so these
  are not totals for the estate's whole history (`@codex`, fm #947). `spider-bot` is the notable one — it is
  **live in production** and took 8 commits in the two days to 2026-08-25 with
  no `.sessions/` directory to record any of them.
- **Card discipline is uneven where it exists.** `superbot` and `spider-swing`
  both moved inside the window and neither left a card dated inside it.
- **The desktop app cannot list cloud sessions.** Recorded independently at
  [`../owner-steps-2026-08-21-laptop-setup.md`](../owner-steps-2026-08-21-laptop-setup.md)
  § The honest limits, from the vendor docs: a session in the app lists only
  other desktop sessions. This area routes around that through the repository
  rather than through the app, which is the only channel both surfaces share.
