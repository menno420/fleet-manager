# superbot — the entry point

> **Status:** `living-ledger` · true as of **2026-08-21**
>
> **What this is:** fleet-manager's entry point for `menno420/superbot` —
> where the last session left off and where the next one should look.
> **Canonical for nothing.** The repo's own `docs/operations/` runbooks win
> on what runs where; the live tree wins over everything. Depth files are
> **not yet written** — created on demand (the keep-bot-only close; the
> Tier-1 row was "cleared to build" since 2026-08-08) and carries only the
> entry point so far.
>
> Certainty tags per
> [`../../findings/2026-08-05-foundation-continuation.md`](../../findings/2026-08-05-foundation-continuation.md).

## The one-paragraph answer

`superbot` is the **FROZEN** repo behind the LIVE production Discord bot:
the `reliable-grace` Railway `worker` service deploys it (`disbot/bot1.py`),
and the estate's hardest rail protects that service and its Postgres —
never stop, scale, disconnect, delete, or change config without the owner's
explicit directive. **Rebuild behavior changed 2026-08-14**: before W1 the
worker had `watchPatterns: []`, so EVERY push rebuilt it (344 production-bot
restarts measured in one billing cycle); W1 installed the watch filter
`['disbot/**', 'requirements.txt', 'requirements-dev.txt', 'pyproject.toml',
'Procfile']`, live-tested the same hour — sb #2446's workflows-only merge
produced a **SKIPPED** worker deployment, the bot did not restart. So
workflow/runbook-only maintenance is now rebuild-safe; a push touching
`disbot/**` or a root build input still restarts the bot. Schedule
retirements remain the recurring work class (they burn Actions runs, not
the bot). A clean game-community successor is now the planned direction; `superbot-next`
is its architecture donor rather than the deployment target
([paired Tier-1 folder](../superbot-next/README.md)). The authoritative
pre-repository plan is
[`docs/planning/2026-08-21-game-community-bot/`](../../planning/2026-08-21-game-community-bot/README.md).

Three facts a fresh session needs that the repo will not volunteer
(`MEASURED` 2026-08-21, fm #878 review):

- **There is no root README.** The repo's real entry is
  `docs/AGENT_ORIENTATION.md` (its own reading router), then
  `docs/current-state.md`. "The live tree wins" starts there.
- **8 open PRs are all dependabot, parked by doctrine** — D‑0017 explicitly
  exempts third-party automation (`../../decisions.md` § D‑0017); do not start
  dispositioning them as abandoned session work.
- **Working contract:** required check on `main` is `Code Quality`; the kit
  gate (`python3 bootstrap.py check --strict`) runs **honestly red at 2**
  (orientation-budget, enforcement-unwired) — expected, never "fixed" by
  suppression; kit updates go vendor-dist + bump-pin, never `adopt`/`upgrade`
  (both over-correct here — program §7, 2026-08-13). And its own
  `docs/current-state.md` still records seat-era 403 walls (ref deletion,
  tag-push, raw api.github.com) that the estate has since refuted — in this
  one repo, "the tree wins" carries the caveat *except its recorded walls*,
  which are dated venue records, 11 of them deliberately allowlisted.

## Threads

### Thread: the rebuild review — **plan written, one owner question open** (2026-09-04)

A full comparative review of this repo against `superbot-next` ran on
2026-09-04 and produced the successor plan:
[`docs/planning/2026-09-04-superbot-rebuild/`](../../planning/2026-09-04-superbot-rebuild/00-README.md).
**It supersedes the comparative and architectural halves of the 2026-08-21 plan
below**, which stays authoritative for nothing it does not still uniquely carry.

Three things it changes about how this repo is read, each re-derived against
the pin `5e3a667b` rather than carried from a prior document:

- **This repo is the donor for guards over the rendered product** —
  reachability, hub actionability, the back-button rule, the always-answer
  fallback at `disbot/bot1.py:540-546`. The 2026-08-21 plan attributed the
  import-direction guard and the provider-neutral AI gateway to
  `superbot-next`; both are **this repo's**, and `sb/kernel/ai/gateway.py:1-6`
  says so in its own header.
- **Its real enforcement locus is `tests/`, not the workflow file.** 44 of 45
  `check_*.py` are driven from `tests/` as libraries behind blocking invariant
  tests; a reviewer reading only the CI workflow will understate this repo
  badly.
- **Three years in it is not the tangle its docs imply** — 0.69 % of lines
  unreachable from the composition root, one `TODO` marker in the whole tree.

Next step: none in this repo. **The review changes nothing here and authorizes
nothing here** — `superbot`, its Railway worker and its Postgres were read-only
throughout and remain the protected surface they were. The open item is one
owner question (`OQ-SUPERBOT-SUCCESSOR-SCOPE`), and the work it unblocks starts
in a new repository, not this one.

### Thread: game-community successor plan — **written, owner confirmation gates remain** (2026-08-21)

The owner asked for a basic game-testing/general game-server bot that keeps the
best of both bots and gives AI more freedom from the start. The resulting
[authoritative pre-repository plan](../../planning/2026-08-21-game-community-bot/README.md)
chooses a clean multi-game repository: this live bot is the behavior/UX oracle,
`superbot-next` is the kernel-pattern donor, and neither existing bot is changed
or used as the development deployment. The server/playtest core comes first;
casino/economy/BTD6 and unrelated content do not transfer.

Next step: confirm the new repository name and create the isolated canonical
home (plan GCB-1/Phase 0). Until then, this thread is only a cross-repo handoff;
the plan owns the pre-build decision and this file owns no product architecture.

### Thread: scheduled-workflow retirement — **landed through #2450**, 2026-08-20

Where it stands: the two frozen-repo pollers are retired — sb **#2446**
(the 2-hourly `dashboard-data-refresh` bake, the ~293-restarts/cycle
source) set the pattern (cron out, `workflow_dispatch` kept, a header note
saying why), and sb **#2450** (`5e3a667b`) applied it to
`ci-rerun-watchdog` (`*/12`) and `pr-conflict-guard` (30-min sweep) —
~170 no-op runs/day gone; runbook rows in `docs/operations/` trued in the
same PR.

**Traps, measured on #2450:** the repo's **auto-merge enabler arms at PR
open** — disable it first or green CI merges before a requested review
answers (it would have, by ~10 minutes); and the runbook tables in
`docs/operations/ci-what-runs-where.md` go stale silently — #2446 left one
of its own rows wrong, found and fixed by #2450's review round.

Next step: none queued. Any remaining scheduled workflow that produces
against a concluded audience is the same class — enumerate before
retiring one at a time (the fm execution card's 💡 idea).

## External workspaces

Pointers, never copies (the § 5.7 shape) — all **null today**: no Drive
folder, ChatGPT workspace, or Gemini notebook is mapped to `superbot` in
any record this session read. Add the pointer here when one exists.
