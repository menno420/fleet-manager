# Railway "keep bot-only" worklist — the owner's 2026-08-20 direction, decided and sliced

> **Status:** `plan` · 2026-08-20 · owner-directed, decisions harvested from the
> live hub chat the same day. Certainty tags per
> [`../findings/2026-08-05-foundation-continuation.md`](../findings/2026-08-05-foundation-continuation.md).
> Execution context: the audit + consolidation record is
> [`../findings/2026-08-14-railway-websites-audit.md`](../findings/2026-08-14-railway-websites-audit.md)
> (§§ 1–4 pre-execution snapshot · § 7 what already changed on 08-14/16).

## 0 · The owner's words (2026-08-20, hub chat)

`OWNER`: *"Use the continuation prompt skills so the next session can execute
the reccomended steps. It should also remove the mineverse from railway, the
only things we should keep is the things that are actually related to the bot
etc"* — given immediately after the status review that found the crawler
problem below.

## 1 · New measurements this direction was given against (`MEASURED` 2026-08-20)

- **The crawler fleet ignored robots.txt and is now effectively DoS-ing
  control-plane.** Fresh `httpLogs` on the live deployment: 5,001 requests in a
  40-minute window, **100 % from Meta's 57.141.x range**, 4,938 of them on the
  ~620 KB seat-era `/orders` page (~295 MB / 40 min ≈ $0.4+/day egress at that
  rate); UA breakdown of the most recent 3,001 requests: 2,986+ spoofed desktop
  browser UAs, **zero `/robots.txt` fetches**, and exactly 4 hits from the
  genuine `facebookexternalhit` unfurler (all on `/`). Meanwhile
  `GET /healthz` from outside timed out **3 × 30 s consecutively** — a route
  that answered in milliseconds on 08-14. The board is intermittently
  unreachable for humans while it serves bots.
- **Everything else from the 08-14 consolidation is holding**: `worker` on one
  deployment since 08-14 11:13 (zero restarts in six days; was ~11/day);
  `review` observed in `SLEEPING` state; `dashboard`/`botsite` sleep-enabled;
  10 services total, exactly the keep-set of the audit.
- The multi-day per-service usage average for the new cycle was still queued
  behind Railway's usage-API concurrency limit when this was written
  (`UNVERIFIED` — the pool stayed saturated ~50 min); nothing below depends on
  it, and the executing session can re-pull it cheaply.

## 2 · The keep-criterion, applied service by service

`OWNER` intent (“actually related to the bot etc”), application `DERIVED` and
flagged where it is a judgement:

| Service | Verdict | Basis |
|---|---|---|
| `reliable-grace/worker` + `Postgres` | **KEEP** | The bot itself. Hard rail unchanged (never stop/scale/disconnect/delete). |
| `superbot-websites/botsite` (+ `superbot-app` name) + its `Postgres` | **KEEP** | The bot's public site + its `/submit` data. |
| `superbot-websites/dashboard` (+ `superbot-dashboard` name) | **KEEP** | The bot's inventory viewer. |
| `superbot-websites/control-plane` | **KEEP** (fix, not retire) | Estate/bot oversight board — the owner's visibility surface. |
| `superbot-websites/review` | **RETIRE after static export** | EAP program-review site; audience concluded 07-21 — not bot-related. Was already recommendation #3; the keep-criterion confirms it. |
| `superbot-mineverse/web` | **REMOVE — owner-named** | *"remove the mineverse from railway."* Stateless (deploys `menno420/superbot-mineverse`, no DB in the project, billed-cycle disk usage 0). The **repo stays** — only the Railway surface goes. |
| `shiftlife/shiftlife-api` + `Postgres` | **DO NOT TOUCH — HIGH, ask first** | His live app's production sync server + real data. Reading *"etc"* as covering it would be a silent HIGH resolution; the question is posed in § 5. |

## 3 · Decided (do not re-litigate)

1. **Crawler fix is route-scoped, never an IP-range block** — the genuine
   `facebookexternalhit` unfurler shares Meta's ranges, so a 57.141.0.0/16 403
   would break WhatsApp/Messenger/Facebook/Instagram link-preview cards for
   every shared link. Gate or remove the heavy seat-era pages instead
   (`/orders` first; it is RECORD-tier history — the old ORDER browser), behind
   the existing owner login or deleted outright, tiny public response.
2. **Mineverse leaves Railway; the repo is untouched.** Owner-named.
3. **Review retires via static export** (its content already lives committed in
   the websites repo — `review/data/` mirrors + generators), then the service
   is deleted and the daily `review-bake` schedule retired with it (OD-3
   pattern: keep `workflow_dispatch`).
4. **Frozen-repo pollers retire**: `ci-rerun-watchdog` (*/12 min) and
   `pr-conflict-guard` (*/30 min) schedules out of `menno420/superbot`,
   `workflow_dispatch` kept — ~170 no-op runs/day on a repo with no
   development. (Precedent: the dashboard-refresh retirement, sb #2446.)
5. **Bot-DB pruning is investigate-then-propose** — read-only sizing of what
   makes the dataset dump at ~2 GB (server-logging / XP history are the
   suspects, `REASONED`); any deletion needs the owner's explicit approval of
   the specific tables/rows.
6. **The PAT stays owner-gated**: mint is UI-only (`MEASURED`, ledger 2026-08-16);
   Tier-1 recipe in `OQ-WEBSITES-PAT`; wire-up on paste.

## 4 · Rejected, and why

- **robots.txt as the fix** — shipped 08-14, measured ignored 08-20 (zero
  robots fetches in 3,001 requests). Keep the files; they cost nothing and
  govern compliant crawlers.
- **Blanket 403 of Meta's /16** — breaks link unfurling (above).
- **Waiting for the multi-day usage average before acting** — the burst rate
  plus the measured unavailability already justify the route fix; the average
  only refines the € number.
- **Deleting the mineverse REPO** — the owner named Railway only.

## 5 · Open (genuinely undecided)

- **`OQ-RAILWAY-SHIFTLIFE-SCOPE` (HIGH — one letter):** does *"only keep things
  actually related to the bot etc"* also mean removing the **shiftlife**
  project (his app's live API + database, real sync data)? **A)** keep
  shiftlife (recommended — it is a product, not bot-web estate; removal would
  take the app's sync offline and needs a data plan) · **B)** remove it too,
  after a verified dump to `menno420/estate-backups` (the fm #867 pattern).
  Until answered: do not touch shiftlife.
- Static-export destination for review: GitHub Pages on the websites repo is
  the default (`DERIVED`, decide-and-flag); skip-export-and-delete only if the
  owner says the content needs no live home.
- `OQ-WEBSITES-PAT`: waiting on the owner's mint.

## 6 · Execution slices, in order (one landing each, estate discipline per repo)

1. **websites PR — unblock the board**: move `/orders` (and any sibling
   seat-era heavy route found by size audit) behind the existing owner login
   with a tiny public 403/redirect; keep `facebookexternalhit` unfurl targets
   (`/`, page roots) public. Verify: healthz answers <1 s from outside under
   load; `/orders` public response is small; nav/clarity registries updated
   (the #501 pattern: classify new/changed routes). Expected effect: the DoS
   ends and the dominant egress line collapses.
2. **Railway — remove mineverse**: `serviceDelete` of `superbot-mineverse/web`
   (id `5cabd73c-3edf-49ef-b204-e8adfe49bc4c`, project `d6e6dc20…`, env
   `99d4ec0a…`), then the empty project (`projectDelete` if the API allows;
   else the service alone and note it). Stateless — no dump needed (verify
   no volume exists before deleting; expected none, disk metered 0).
3. **websites — review to static + retire**: export the review site's rendered
   pages to GitHub Pages (content is committed data; generators in
   `review/gen_*.py`), verify the Pages URL serves, then `serviceDelete`
   the `review` service (id `511fd9eb…`) and retire the `review-bake` schedule
   (keep `workflow_dispatch`). Update the fleet-nav strip if it links review.
4. **superbot PR — retire the pollers**: schedules out of
   `ci-rerun-watchdog.yml` + `pr-conflict-guard.yml`, `workflow_dispatch` kept,
   header notes per the sb #2446 pattern.
5. **Bot-DB sizing (read-only)**: table/relation sizes via a one-shot Actions
   job (this container cannot reach the DB — egress is web-ports-only,
   ledger 2026-08-16) or the existing backup artifact; propose the prune list
   to the owner; execute only what he approves.
6. **If the owner pastes the PAT**: `variableUpsert` on control-plane +
   redeploy + verify the poller's authenticated rate.
7. **Records**: §7 rows per landed slice; OQ updates
   (`OQ-RAILWAY-SHIFTLIFE-SCOPE` answered or still open); the audit finding
   gets a § 8 execution addendum mirroring § 7's evidence style.

## 7 · Out of scope, explicitly

- **shiftlife** (both services) until `OQ-RAILWAY-SHIFTLIFE-SCOPE` is answered.
- **`worker` and the bot's `Postgres`**: the operation-scoped hard rail stands
  (never stop/scale/disconnect/delete; config-only changes need an explicit
  owner directive).
- The mineverse **repo**, the superbot repo's code (workflow triggers only),
  and any change to control-plane's public/auth posture beyond gating the
  named seat-era routes ([D-0011] stands).
- E1 and everything else owner-reserved in the program.
