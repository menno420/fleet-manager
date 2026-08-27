# Activity — what every session did, wherever it ran

> **Status:** `living-ledger` · tier **TASK**
>
> **What this area is for:** so a session working **fleet-manager** — from the
> owner's laptop, a cloud container, Codex or ChatGPT Work — can find out what
> sessions in *other* repositories and on *other* machines have been doing.
>
> **The promise is scoped on purpose.** A session booted in a satellite
> repository loads that repo's `.claude/`, not this one's
> ([`../../.claude/CLAUDE.md`](../../.claude/CLAUDE.md), boot triad case two), so
> the prompt route and the map entry that point here **do not exist for it**.
> Reaching this area from a satellite still takes someone naming fleet-manager.
> Propagating a pointer into the satellites is real follow-up work and is not
> done here (`@codex`, fm #947) — claiming otherwise would be the "delivered by
> a mechanism" story told about a mechanism that is absent. Built 2026-08-26 on the owner's
> ask: *"how well does a cloud session understand what the local sessions have
> been doing? … we should make a dedicated section in the fleet manager where
> my local AIs keep track of what they have been doing."*
>
> **What it is NOT:** canonical for any repository's work. Per-repo truth stays
> in that repository's own `.sessions/` card and its `docs/current-state.md`
> (`intent.md` § 1 — this repo points, it does not copy). This area is an
> **index of where the work happened**, not a second copy of it.

## The answer to the question that produced this area

Measured 2026-08-26 and written up in
[`../findings/2026-08-26-cross-session-visibility.md`](../findings/2026-08-26-cross-session-visibility.md):
a cloud session booted in fleet-manager could see **this repository's** session
cards and nothing else. In the seven calendar days to that date the estate wrote
**74 cards across six non-archived repositories**; this session could reach
**54** and **20 were unreachable** — `websites` 9, `couch-legend` 7,
`product-forge` 2, `sim-lab` 1, `idea-engine` 1. A whole repository
(`creator-kit`) had been created and was absent from the estate index. And no
card anywhere — **418 dated cards in this repo alone** — recorded **which
machine ran it**, so even a visible card could not tell you whether it was local
or cloud.

## The two lanes

The split is the design, and it is a split by *what can be derived*:

| lane | file | written by | covers |
|---|---|---|---|
| **derived** | [`estate-log.md`](estate-log.md) | `python3 tools/estate_activity.py refresh` | every session card in every **non-archived** repository inside a rolling window — on the default branch **and on open PR branches**, so a born-red card in flight is visible before it merges — **automatically**, because the card already exists |
| **hand-written** | [`off-repo-log.md`](off-repo-log.md) | `python3 tools/estate_activity.py log …` | work that touches no repository and therefore cannot be derived: laptop setup, a ChatGPT or Gemini sitting, a Drive reorganisation, an install |

Nothing has to be remembered for the derived lane, which is why it carries the
bulk. The hand-written lane exists only for the residue — and it is one
command, not a procedure, because
[`intent.md`](../intent.md) § 4 rules that **the fix for an unfollowed rule is
a mechanism that delivers it at the right moment, never another statement of
the rule.**

## The venue token — how a card says which machine ran it

Every session card in the estate may carry one line directly under its
`📊 Model:` line:

```
- **📍 Venue:** local-desktop
```

The closed set, and it answers *which machine*, not *which model* — the Model
line already answers that:

| token | means |
|---|---|
| `local-desktop` | the owner's laptop — Claude Desktop's Code tab |
| `local-cli` | the owner's laptop — `claude` in a terminal |
| `cloud-container` | Claude Code on the web / a remote container |
| `codex-cloud` | ChatGPT Codex cloud |
| `chatgpt-work` | ChatGPT Work |
| `other` | anything else — say what in the card body |

**Absence is reported as `unstated`, never guessed.** The generator prints the
stated-vs-total count in its header, so the coverage of this convention is
visible rather than assumed. It started at **0 of 74**.

The line is deliberately **not** part of the Model line: that line has a
kit-validated three-segment taxonomy (`model · effort · task-class`) and
overloading it would put a local convention inside a gated grammar.

## Planned: a page per surface, not only a log — the owner's shape

**`OWNER`, 2026-08-26, after this area was built**, and it is a different shape
from what is here:

> *"Just create a seperate section in fleet-manager for the local work, just
> like how each repo is mentioned with some explanation, the one drive should
> get the same treatment."*

**What exists is a log; what he described is a place.** `off-repo-log.md`
answers *"what happened Tuesday"*. His shape — the
[`../repos/`](../repos/README.md) shape, one page per surface — answers *"what
is the state of the laptop right now, before I continue in the cloud"*, which is
the use case he gave. **Sharpened 2026-08-27→28
([owner direction](../findings/2026-08-28-owner-direction.md) §§ 1–3): the
acceptance test is venue handoff** — a device-bound task started locally must
be continuable by a fresh cloud session — and the pages carry **state AND a
lean account of the main things that happened** (*"lean, but not that it should
exclude all feature work"*), at capability/work level only: nothing personal,
no paths or security-relevant detail, because these pages are public. Planned
pages, each carrying **what it is · what is on it · current state · what to
know before continuing · last checked**:

| page | what it covers | already in the tree |
|---|---|---|
| `laptop.md` | the machine, what is installed, what has been prepared there | [`../owner-steps-2026-08-21-laptop-setup.md`](../owner-steps-2026-08-21-laptop-setup.md) |
| `onedrive.md` | **his laptop hub** — `Hub/journal.md` on it carries the build-session narrative, and no cloud agent can read it | [`../repos/spider-bot/README.md`](../repos/spider-bot/README.md) line 107 |
| `google-drive.md` | the media dropbox sessions already read | [`../conventions/owner-drive-folder.md`](../conventions/owner-drive-folder.md) |

**Hub-local sessions execute this, owner-directed** — clarified 2026-08-27→28:
his 2026-08-26 *"himself"* meant *via local sessions*, *"because they have the
full ability to work on both sides and see everything"* — and **execution
awaits his GO** (*"no execution yet"*, same sitting). This section exists so
that work has a written target instead of a chat message. The dated log stays
underneath as history, and the scope rule that feeds all of this is now
owner-stated: repo work in the repo's own card (scoped to that repo),
estate-level work here, machine/personal in the hub with these pages as its
lean cloud-readable account
([owner direction](../findings/2026-08-28-owner-direction.md) § 3).

**`OQ-ONEDRIVE-HUB` is rescoped (2026-08-27→28) — no longer a sync question.**
It asked how the hub and this repo centralise (private git repo · read-only
share · `journal.md` copied per sitting) so the cloud could see the laptop;
the owner answered the visibility need differently — the cloud reads this
section's pages — so the a/b/c choice shrinks to unhurried hub housekeeping
(whether the hub wants git versioning for its own sake), blocks nothing, and
the old recommendation **(a)** no longer stands as a sync path. **The pages
give sight, not file access** (`@codex`, fm #954): work meant to continue in
the cloud lands in a repo before the handoff, and if a genuine handoff ever
depends on hub-only artifacts, the a/b/c options are the recorded transfer
candidates and the question re-opens. Records:
[`../findings/2026-08-26-owner-direction.md`](../findings/2026-08-26-owner-direction.md)
§§ 1, 5 (origin) ·
[`../findings/2026-08-28-owner-direction.md`](../findings/2026-08-28-owner-direction.md)
§ 7 (rescope).

## Refreshing the derived lane

```bash
python3 tools/estate_activity.py refresh            # last 7 days
python3 tools/estate_activity.py refresh --days 30  # a wider window
python3 tools/estate_activity.py refresh --stdout   # look without writing
```

It works from either GitHub path — `$GITHUB_PAT` over direct egress in a
container, or the `gh` CLI on the laptop — so the same command is correct in
both places.

**On demand, not on a schedule.** A cron that commits a regenerated file to
`main` every day is exactly the churn class the estate has been retiring
(superbot #2450). Refresh it when you want the picture: at session close, or
when a session asks "what happened while I was away". If the owner later wants
it scheduled, that is a one-file workflow and a deliberate choice, not a
default.

## What this area still does not solve

Honest limits, so the next session does not assume more than is here:

- **A local session that never pushes leaves nothing.** The derived lane reads
  pushed cards, on `main` or on an open PR branch. Work still on the laptop's
  disk is invisible until it is pushed, and that is a property of git, not a
  defect to fix here.
- **Archived repositories are excluded**, so every count is non-archived-only
  and none of them is a total for the estate's whole history. Nine repositories
  were archived on 2026-08-23 and some carry cards from that wave.
- **Repositories with no card protocol can never appear in the derived lane.**
  The generator names them in their own section rather than passing over them.
  As of the first run: `curious-research`, `estate-backups`, `spider-bot`,
  `superbot-plugin-hello`.
- **The venue token is self-reported.** Nothing verifies it, and nothing can:
  a squash-merged commit carries no trace of the machine that produced it.
- **This is a log, not a lock.** It tells a session what happened; it does not
  stop two sessions colliding. The in-flight claim is still the born-red card
  plus the open PR, per [`session-close`](../../.claude/skills/session-close/SKILL.md).
