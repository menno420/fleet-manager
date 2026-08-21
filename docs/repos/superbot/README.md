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
explicit directive. The repo is frozen as a codebase but its **workflows
still matter**: pushes to it rebuild the worker (the audit measured 344
production-bot restarts in one billing cycle from exactly this), so
schedule retirements — not code changes — are the recurring work class.
The successor codebase is `superbot-next` (paired Tier-1 row).

## Threads

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
