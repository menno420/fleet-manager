# estate-backups — the entry point

> **Status:** `living-ledger` · true as of **2026-08-21**
>
> **What this is:** fleet-manager's entry point for
> `menno420/estate-backups` — where the last session left off and where the
> next one should look. **Canonical for nothing**; the repo's own tree wins.
> Depth files are **not yet written** — created on demand (the keep-bot-only
> close) and carries only the entry point so far.
>
> Certainty tags per
> [`../../findings/2026-08-05-foundation-continuation.md`](../../findings/2026-08-05-foundation-continuation.md).

## The one-paragraph answer

`estate-backups` is the **PRIVATE Actions venue** for work the session
container's 80/443-only egress cannot do directly against Railway
Postgres: its workflows run on GitHub's runners, which CAN reach a
database's public proxy. Two workflows exist, each a one-shot with its own
sealed secret — `dump.yml` (fm #867: the **one-shot, restore-verified
pre-deletion archive of `postgres-botsite`**, secret `PGB_DSN`; the proxy,
credential and source service were deleted minutes after its 2026-08-16
run) and `sizing.yml` (`c1439ab`, 2026-08-20: read-only catalog SELECTs +
`COUNT(*)` + min/max of date columns over secret `BOT_DB_DSN` — size
metadata, never row contents). **The recurring bot backup does NOT live
here** — it is a `superbot` workflow, daily → weekly since sb #2446. The
credential pattern is the venue's whole point: a **one-shot sealed-box
secret** (PUT via the API without the value ever printing → dispatch →
read the log → DELETE the secret), so nothing durable holds a DSN. Work
here is read-only unless the owner directs otherwise — the worker/Postgres
hard rail applies to everything this venue touches.

## Threads

### Thread: bot-DB sizing — **landed**, 2026-08-20

Where it stands: the sizing run answered the ~2 GB-dump question — 949 MB
database, 97.5 % of it three `btd6_*` ingestion tables; full results and
the prune proposal live in the fm audit
[§ 8 addendum](../../findings/2026-08-14-railway-websites-audit.md), and
the owner ask is `OQ-BOT-DB-BTD6-PRUNE`. If the owner answers "P N", the
executing session runs a fm #867-style restore-verified dump FIRST, then
the prune — from this venue.

## External workspaces

Pointers, never copies (the § 5.7 shape) — all **null today**: no Drive
folder, ChatGPT workspace, or Gemini notebook is mapped to
`estate-backups` in any record this session read. Add the pointer here
when one exists.
