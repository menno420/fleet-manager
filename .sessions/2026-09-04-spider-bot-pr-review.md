# 2026-09-04 — spider-bot#3 reviewed against the tree and the live Railway project; the merge is his

> **Status:** `in-progress` — branch `claude/spider-bot-pr-review-bye9ni`, born red.
> Flips `complete` only after the owner's answer on spider-bot#3 has been acted
> on and both cards carry the outcome.

- **📊 Model:** fable-5 · xhigh · review/verify
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01XtUDb1BxPVdjkGryVWCKVu](https://claude.ai/code/session_01XtUDb1BxPVdjkGryVWCKVu) · "Spider Bot PR review and merge"

**What is about to happen.** Review [spider-bot#3](https://github.com/menno420/spider-bot/pull/3)
as it stands, land what the review finds on the same branch, put the merge
decision and the rollout questions to the owner, and act on his word.

## Live state re-read at session start — `MEASURED` 2026-09-04T18:2xZ, nothing had moved

| surface | value |
|---|---|
| spider-bot#3 | open · unmerged · `clean` · head `d3a66bb` · 23 commits · 58 files · +14,395/−125 |
| spider-bot `main` | `bf4d7527` (2026-08-25T22:42:55Z) |
| Railway `worker` | `bc4f9985` SUCCESS · `bf4d7527` SKIPPED (IaC-only commit, watch patterns) |
| worker variables (names) | `ANTHROPIC_API_KEY`, `DISCORD_TOKEN`, `GUILD_ID` + the seven `RAILWAY_*` Railway injects |
| gate at `d3a66bb`, local 3.11 | ruff 0 · pytest 0 (669 passed) · compileall 0 · `docs/journeys.py` 0 |

## What the review found — three doc defects and one IaC gap, none in the 48 findings' territory

All by reading the docs against the tree and the live project, not the code the
four review sources had already covered:

1. **`docs/what-changed.md` told the owner to create `#mod-cases`.** The bot
   resolves `#case-state` (`spiderbot/config.py`, `ch_case_state`). Following
   the owner page as written leaves moderation silently off — invariant 4's
   deliberate behaviour for a *missing* channel, delivered by a wrong
   instruction on the one page written for him.
2. **`.railway/railway.ts` declared `preserve()` for exactly the three live
   variables.** Railway IaC is *omit means delete*. `MEASURED` read-only with
   `railway config plan` on spider-bot's project: removing one existing
   variable from the file plans `Delete variable worker.GUILD_ID` as a
   destructive change; adding `preserve()` for six variables that do not exist
   yet plans "already up to date". So a `GITHUB_TOKEN` or `MOD_*` set in the
   dashboard at rollout step 3–5 would have been removed by the owner's next
   apply — and PR #1/#2's bodies show he runs the apply flow himself. The six
   rollout switches are now declared `preserve()`, inert until set.
3. **Four documents said `railway.json` holds the watch patterns** (the repo's
   `CLAUDE.md`, `docs/rollout.md`, its session card, and this repo's Layer-2
   entry). The tree has held only `.railway/railway.ts` since spider-bot#1/#2
   on 2026-08-25, and `railway.json` is not among the patterns. `README.md`
   also still said NIXPACKS where the IaC says RAILPACK.
4. **Gemini's four unreviewed fixes** (`204227d`: the edit cooldown, the
   null-aware required-field check, the skipped redundant draft write, the
   withheld-count flush loop) — read line by line, one pair of eyes, no defect
   found. That is a reading, not a test; recorded as such.

Landed as spider-bot `8937191` on the PR's own branch (one PR, D-0024). Gate
before the push: ruff 0 · pytest 0 (669) · compileall 0 · journeys 0, each read
from its own exit code. CI `quality` at `8937191`: completed/success on both
runs (push + PR).

## The trap the measurement itself found — TRAP-011

The first `railway config plan` ran **against `superbot-production`**: this
container's environment carries `RAILWAY_PROJECT_ID`, `RAILWAY_ENVIRONMENT_ID`
and `RAILWAY_SERVICE_ID` for that project, and the CLI honours them over
`railway link` — the link wrote the right ids to its config and `railway status`
still answered superbot. The plan previewed **24 variable deletions plus the
Postgres** on the wrong bot. A plan, nothing applied; an `apply --yes
--confirm-destructive` would have been the end of the live SuperBot. Overriding
the three ids on the command line fixed it, and the `Project` line of every
subsequent run was read before its output was believed. Recorded in
`docs/traps.md` TRAP-011, `docs/CAPABILITIES.md` (the CLI recipe), and a new
`railway-cli-project` doc route that fired on this session's own next command.

## Owner decision — put to him, not taken

The merge is his (DECIDED in the handoff). What he gets: merge now or change
first; the six setup steps and the open rollout questions as `docs/rollout.md`
already carries them; and the IaC answer above, which closes the one question
no document held.

## Deployment outcome

*(written after his answer)*

## Layer-2 handoff

Layer-2 handoff: docs/repos/spider-bot/README.md — *AI operations build* thread updated (review state, live worker hash, IaC finding)

## 💡 Session idea

*(at close)*

## ⟲ Previous-session review

The build session's own residue statement on the PR was honest and complete
about the **code** — and every defect this session found was in a **document
or a config file**: the owner page, the IaC declaration, four copies of a
filename that had been wrong for ten days. A review budget spent entirely on
`spiderbot/` reads exactly what the 48 findings read, and the next defect is
wherever nobody has pointed a reviewer yet. The cheap check that would have
caught three of the four: grep every filename a doc names against `git
ls-files`.
