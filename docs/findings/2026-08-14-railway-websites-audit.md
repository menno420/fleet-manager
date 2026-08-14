# Railway websites audit — what is live, what it costs, why the bill is €30

> **Status:** `reference` · 2026-08-14 · owner-directed ("find out which are live
> and what they do, if there are any duplicates and how we can consolidate…
> I received a 30 euro railway bill and I think thats a little high")
>
> Certainty tags per
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).
> Everything in §§ 1–4 is `MEASURED` this session (Railway GraphQL over direct
> egress + the Gmail receipts + live `/healthz` probes) unless tagged otherwise.
> Costs are computed from Railway's own receipt unit prices; arithmetic
> cross-foots against the receipt totals in § 3.

## 0 · The answer in five sentences

The August 13 bill is **$30.73 (~€30), all of it usage**: the billed cycle
(Jul 13 → Aug 13) was the **first cycle with (nearly) the whole EAP-era
estate running 24/7** — 12 of the 14 services predate the cycle start, while
the new botsite Postgres (07-19) and both shiftlife services (07-25) joined
mid-cycle, so the full-estate run-rate is slightly *above* $30.73, where the
June cycle ($7.75) had only ~half the estate for part of the month. The per-service
attribution (§ 3) shows it is **not** "many small websites": **two services
carry 75 % of the bill** — the websites **`control-plane`** ($11.62: 92 % of
all vCPU plus **149 GB of egress** serving its readiness board, half of that
in the final week alone and still running at that rate) and the **bot's
Postgres** ($11.35: **831 MB resident RAM** around the clock plus **~59 GB of
egress that matches the daily off-platform `pg_dump` backup**). The three
duplicate/old sites the cutover plan already retires cost **~$1.6/cycle** —
worth retiring, but hygiene rather than the main lever. A separate
**operational** defect found on the way: the unfiltered `worker` service was
rebuilt and **the LIVE Discord bot restarted 344 times in the cycle
(~11×/day)** by pushes to the frozen `superbot` repo — ~293 of them the
2-hourly `dashboard-data-refresh` commits (the dashboard-filter-matched
subset), the rest other pushes. Nearly free in dollars (the worker totals
$1.03), but it bounces the production bot mostly for the sake of a site that
is itself a retire target. Fixes in § 5, ordered by
measured impact; at control-plane's current rate the **next bill will not be
smaller without action**.

## 1 · What is live on Railway — the full inventory (`MEASURED` 2026-08-14)

One workspace, **4 projects, 14 services**, all with a `SUCCESS` latest
deployment, **none using App Sleep** (`sleepApplication: false` on all 14).
Nine answer HTTP (all probed live this session); five are infrastructure.

| Project | Service | Serves | What it is |
|---|---|---|---|
| `reliable-grace` (created 05-13) | **worker** | *(no domain)* | **The LIVE production Discord bot** (`menno420/superbot`, `disbot/bot1.py`). HARD RAIL: never touch. |
| | **Postgres** | *(internal)* | The bot's production database. Never touch. |
| | **botsite** | `superbot-app.up.railway.app` | **OLD** SuperBot site ("SuperBot — interactive prototype", title fetched live), deploys `menno420/superbot` — superseded by the new botsite. Retire target. |
| | **dashboard** | `superbot-dashboard.up.railway.app` | **OLD** developer dashboard ("SuperBot — developer dashboard", fetched live), deploys `menno420/superbot` — superseded. Retire target. |
| | **review** | `review-production-f027.up.railway.app` | **DUPLICATE** of the new review site — Railway reports the same source repo (`menno420/websites`) for both, and both serve the identical "Program Review" page (titles fetched live). Retire target. |
| | **postgres-botsite** | *(internal)* | Postgres serving ONLY the old botsite (`DATABASE_URL` host verified = `postgres-botsite.railway.internal`). It is one of the **two `reliable-grace` Postgres DBs W1's hard rail protects** — it merely becomes *functionally* orphaned once the old botsite retires; any disposition is an explicit owner amendment to that rail (§ 5.5). |
| `superbot-websites` (created 07-09) | **control-plane** | `control-plane-production-abb0…` | Fleet readiness board + journal browser over the estate's repos, live from the GitHub API. |
| | **botsite** | `botsite-production-cfd7…` | **Canonical** SuperBot marketing/reference site + `/submit` idea intake + `/testing` tester program (Postgres-backed). |
| | **dashboard** | `dashboard-production-a91b…` | **Canonical** read-only bot-inventory dashboard (+ Discord-gated `/admin`). |
| | **review** | `review-production-fc91…` | **Canonical** EAP program-review site (built for Anthropic reviewers; audience concluded 07-21). |
| | **Postgres** | *(internal)* | The new botsite's database (`/submit`, `/testing`). |
| `superbot-mineverse` (created 07-12) | **web** | `web-production-97636…` | The mineverse staged web app (read-only degraded; live mode still blocked on env-var secrets). |
| `shiftlife` (created 07-25) | **shiftlife-api** | `shiftlife-api-production…` | The ShiftLife app's sync/share server. |
| | **Postgres** | *(internal)* | ShiftLife's database. |

Eight web surfaces returned 200 on `/healthz`; mineverse has no `/healthz`
route and returned its app with 200 on `/` — nine reachable, eight of them
via health checks. The gba-homebrew arcade is GitHub Pages —
free, not part of this bill.

**The duplicates, precisely:** `review` ×2 (identical `menno420/websites`
code, both live), `botsite` ×2 and `dashboard` ×2 (old `superbot`-repo
implementations vs their `websites`-repo replacements). This is exactly the
duplication `OQ-RAILWAY-PROJECT-SPLIT` records and websites PR #407 mapped:
**canonical = `superbot-websites`, duplicates/old = `reliable-grace`.** The
old constraint that kept `f027` reachable (the Anthropic email linked it)
**lapsed 07-21, verified 07-26** (consolidation program, W1).

## 2 · The bill, from the receipts (`MEASURED` — Gmail, Stripe receipts)

| | Jun 13 → Jul 13 (#2465-9407) | **Jul 13 → Aug 13 (#2694-7229)** |
|---|---|---|
| Memory | $5.84 (25.2M MB-min ≈ 0.56 GB avg) | **$15.43** (66.7M MB-min ≈ **1.49 GB avg, 24/7**) |
| Network egress | $1.49 (~30 GB) | **$11.74** (~**234 GB**) |
| vCPU | $0.15 | **$3.29** (≈ 0.16 vCPU continuous) |
| Disk | $0.07 | $0.27 |
| Agent usage | $0.20 | $0.00 |
| Hobby base − included usage | $5 − $5 | $5 − $5 |
| **Total** | **$7.75** | **$30.73** |

The bill is **pure usage** — the $5 subscription is fully offset by the $5
included-usage credit. The Aug 7 usage-alert email ($15.08 at 25 days into
the cycle) implies the final week ran ~$2.6/day vs ~$0.60/day before — the
estate's cost was still **accelerating** at cycle close. § 3's bucketed data
attributes the acceleration: control-plane's egress and CPU roughly tripled
in early August and were still at that rate when this audit ran.

Why the 4× jump from June's cycle: `superbot-websites` (4 of its 5 services)
was created 07-09, `superbot-mineverse` 07-12, the second review copy 07-12 —
so the June cycle billed a half-built estate for part of a month, while the
July cycle billed 12 of the 14 services for the whole month. Two joined
mid-cycle (the new botsite Postgres 07-19, both `shiftlife` services 07-25),
which means **the €30 slightly understates the full-estate run-rate — it is
the run-rate of the estate as built, not a one-off spike.**

## 3 · Where it goes, per service (`MEASURED` — Railway usage API, billed cycle)

Method: `usage(workspaceId, measurements, groupBy: [SERVICE_ID])` for
2026-07-13 → 2026-08-13, **summing** the API's time-bucketed rows per service
(a first pass that dict-assigned instead of summing kept only each service's
last bucket and under-reported 4× — kept here as the trap it is). Dollars
computed at Railway's receipt unit prices ($10/GB-mo memory ·
$20/vCPU-mo · $0.05/GB egress). **Cross-foot against the receipt: memory
$14.99 vs $15.43 (97 %) · vCPU $3.06 vs $3.29 (93 %) · egress 212 GB vs
~234 GB (~91 % — ~22 GB / ~$1.10 unattributed)**; the residue is
window-boundary (midnight-UTC query bounds vs the receipt's mid-day cycle
boundary) plus rounding, two deleted services report zero, and the egress gap
is the largest single uncertainty this attribution carries.

| Service | avg RAM | mem $ | vCPU-min | cpu $ | egress GB | net $ | **total $** |
|---|--:|--:|--:|--:|--:|--:|--:|
| **superbot-websites/control-plane** | 134 MB | 1.36 | **6,068** | 2.81 | **149.1** | 7.46 | **11.62** |
| **reliable-grace/Postgres** (bot DB) | **831 MB** | 8.39 | 41 | 0.02 | **58.8** | 2.94 | **11.35** |
| reliable-grace/worker (the bot) | 99 MB | 1.00 | 56 | 0.03 | 0.3 | 0.01 | 1.03 |
| superbot-websites/botsite | 63 MB | 0.63 | 78 | 0.04 | 1.2 | 0.06 | 0.73 |
| superbot-websites/dashboard | 53 MB | 0.53 | 68 | 0.03 | 0.8 | 0.04 | 0.61 |
| superbot-websites/review | 48 MB | 0.48 | 72 | 0.03 | 1.2 | 0.06 | 0.58 |
| reliable-grace/botsite (old) | 54 MB | 0.54 | 59 | 0.03 | 0.0 | 0.00 | 0.57 |
| reliable-grace/review (dup) | 46 MB | 0.46 | 71 | 0.03 | 1.0 | 0.05 | 0.55 |
| reliable-grace/dashboard (old) | 46 MB | 0.46 | 61 | 0.03 | 0.0 | 0.00 | 0.49 |
| reliable-grace/postgres-botsite | 29 MB | 0.29 | 14 | 0.01 | 0.0 | 0.00 | 0.30 |
| superbot-websites/Postgres | 26 MB | 0.26 | 21 | 0.01 | 0.0 | 0.00 | 0.27 |
| shiftlife/Postgres | 25 MB | 0.26 | 5 | 0.00 | 0.0 | 0.00 | 0.26 |
| superbot-mineverse/web | 19 MB | 0.19 | 5 | 0.00 | 0.0 | 0.00 | 0.19 |
| shiftlife/shiftlife-api | 13 MB | 0.13 | 0 | 0.00 | 0.0 | 0.00 | 0.13 |
| **TOTAL (recovered)** | | **14.99** | | **3.06** | **212.4** | **10.62** | **28.68** |

What the numbers say:

- **`control-plane` is the single biggest cost** and it is *working*, not
  idle: 6,068 vCPU-min is 92 % of the estate's CPU (its GitHub-polling
  readiness cache — still on the anonymous 60 req/h tier, `OQ-WEBSITES-PAT`
  never done), and 149 GB is 70 % of all egress. The bucketed data shows
  **~77 GB of that egress and ~2,885 of those vCPU-min in the final week
  alone** — its load roughly tripled in early August and the new cycle's
  projection (`estimatedUsage`: 169 GB, ~8,000 vCPU-min) says it is still
  running at the elevated rate. *What* pulls ~5 GB/day from a readiness board
  is not determinable from the usage API — Railway's HTTP logs are the next
  step (crawler traffic and the cross-service fleet-nav fetches are the
  candidates).
- **The bot's Postgres transmitted 58.8 GB; attributing it to the daily
  02:00 `pg_dump` backup is `REASONED`, not measured** — the usage API groups
  egress by service, not by request, so the near-exact fit (~59 GB ÷ 31 days
  ≈ 1.9 GB/day against a daily dump over the public proxy, the only route a
  GitHub runner can reach) is strong but inferential. One observation closes
  it: the backup workflow's artifact/transfer size for a single run. Its
  831 MB resident RAM is the estate's largest memory line either way.
- **The bot itself is cheap** ($1.03) — the 344-restart churn (§ 4) is an
  operational defect, not a cost driver.
- The three retire-target sites total **$1.61**; beyond control-plane, the
  three canonical site services total $1.92 and all keep web services
  (+ mineverse + shiftlife-api) $2.24; every idle Postgres runs ~$0.26–0.30.

## 4 · The churn defect: the frozen repo redeploys the production bot 11×/day

`MEASURED` from Railway's deployments API, billed cycle Jul 13 → Aug 13.
"Real" excludes `SKIPPED` records (watch-path filtered): a `REMOVED` status is
a deployment that built, went live, and was later replaced — i.e. a restart.

| Service | Real deployments in cycle | Since Aug 1 | Watch filter |
|---|---|---|---|
| reliable-grace/**worker** (the live bot) | **344** — every push; **~293 of them refresh-driven** (the dashboard-filter-matched subset below), the rest other pushes to the frozen repo | 148 (~11/day, ongoing) | **none** (`watchPatterns: []` — rebuilds on every push) |
| reliable-grace/dashboard (old) | 293 (+50 skipped) | 135 | `dashboard/**` — matched by every 2-hourly data-refresh commit |
| reliable-grace/botsite (old) | 17 (+326 skipped) | 6 | `botsite/**` — its filter works; not churning |
| reliable-grace/review (dup) | 253 | 15 | none — rebuilds on every `websites` push |
| superbot-websites/control-plane | 254 | 15 | rebuilds on every `websites` push |

The mechanism: `superbot` (frozen as the behavioral oracle 07-17, "no new
feature work") still runs `dashboard-data-refresh.yml` every 2 hours, which
lands an auto-merged data PR on `main`. The old dashboard rebuilds because its
watch filter (`dashboard/**`) matches the refreshed JSON — that is by design.
**The production bot rebuilds because its service has NO watch filter**
(`watchPatterns: []`), so every push to the frozen repo — including a
data-only JSON refresh — rebuilds and restarts the live bot. The old
botsite's `botsite/**` filter correctly skips these pushes, which proves the
filter mechanism works and `worker` simply never got one. The websites side had the same shape during the EAP tail (253 deploys
in the cycle) but is now calm (~1/day — the nightly `review-bake`, which
rebuilds all four `superbot-websites` services **and** the duplicate `f027`
review daily).

The dollar cost is small — § 3 puts the worker's whole cycle at $1.03, so
build/deploy churn is not what drives the bill. The issue is operational:
**the live bot's process is being bounced ~11 times a day by a cron that
exists to freshen a website that is itself a retire target.** Nothing in the
frozen repo's docs records this as intended behavior.

## 5 · Consolidation — the recommendation

The cutover plan already exists and its prerequisites are closed
(websites `docs/plans/site-consolidation-cutover.md`, ground truth corrected
by websites #407; program track W1, OD-8). What this audit adds is the
measured attribution — which reorders the work. By impact:

1. **Chase control-plane's 149 GB/mo egress + 92 %-of-estate CPU**
   (worth ~$10/cycle and growing — its load tripled in early August).
   First step is Railway's HTTP logs for the service: if it is crawler
   traffic, robots.txt + response caching / Railway's CDN caching are the
   levers; if it is the cross-service fleet-nav or an external poller,
   cache the readiness JSON with a real TTL. Separately, its GitHub polling
   still runs on the anonymous 60 req/h tier — `OQ-WEBSITES-PAT` (wiring a
   read-only PAT) would cut the retry churn that anonymous rate-limiting
   produces. This is investigation-then-fix, one session.
2. **Tame the bot-DB backup egress** (~$2.9/cycle if the `REASONED`
   attribution in § 3 holds): the bot's Postgres transmitted 58.8 GB, a
   near-exact fit to the daily 02:00 `pg_dump` at ~1.9 GB/day. **Verify
   before weakening dailies** — read one backup run's transfer/artifact size
   from the workflow logs; if it confirms, daily → weekly full (keep the
   monthly long-retention tier) ≈ −$2.5/cycle. The durable fix is asking why
   a Discord bot's dataset dumps at ~2 GB and pruning what grew (server
   logging / XP history are the candidates). The 831 MB resident RAM
   ($8.39/cycle) follows the dataset — pruning shrinks both.
3. **Stop the bot-restart churn** (operational, ~free in dollars). Two
   independent, reversible levers: (a) disable `dashboard-data-refresh.yml`
   in `superbot` — its only consumer is the old dashboard site, a retire
   target; (b) give `worker` a watch filter via `serviceInstanceUpdate` —
   the mechanism the old botsite already uses successfully — **covering
   every build/runtime input, not just the source directory**: at minimum
   `disbot/**` plus the root deployment inputs the build consumes
   (`requirements*.txt`, the Dockerfile/build config — enumerate from the
   repo root before setting it). A source-only filter would let a dependency
   bump merge while the live bot silently keeps its old environment. Doing
   both is cheap and correct.
4. **Execute W1 as the cutover plan writes it** (−$1.61/cycle + the drift
   hazard gone) — the full three-step sequence per service, not delete
   alone: **Step 1 repoint references** (old → keep domains, including the
   `superbot` repo/bot-config audit the plan names) → **Step 2 reclaim the
   freed pretty names onto the keep services** (OD-8: the new services
   replace the old sites **under the old names** — `superbot-app` /
   `superbot-dashboard` should end up serving the canonical replacements,
   not go dead) → **Step 3 stop → watch → owner's explicit per-service go →
   delete**, in the order `review-f027` → `superbot-app` →
   `superbot-dashboard`. The `f027` EAP-link constraint has lapsed. Never
   touch `worker` or either `reliable-grace` Postgres (the plan's hard
   rail; operate by exact service id, never project-level).
5. **`postgres-botsite` — an owner amendment, not cleanup** (−$0.30/cycle
   if taken). It is one of the two Postgres DBs W1's hard rail explicitly
   protects; what this audit adds is the wiring fact that its only consumer
   is the old botsite, so after W1 it is protected-but-functionally-orphaned.
   Any disposition (dump to a backup artifact then stop/delete, or keep it
   stopped so the old `/submit` data stays warm) requires the owner to
   explicitly amend the rail for this one service. Flagged, not decided.
6. **Enable App Sleep on the low-traffic keep sites** (review-fc91,
   dashboard, botsite ≈ $1.9/cycle combined runtime; savings scale with how
   sporadic their traffic really is). Cold-start of ~seconds on first hit;
   the 6-hourly healthcheck/smoke-crawl crons wake them briefly, which is
   compatible. Control-plane will NOT sleep while its background GitHub
   polling runs — fix item 1 first.
7. **W2 candidate beyond the plan:** the review site's audience (EAP
   reviewers) concluded 07-21. It is server-rendered from committed data
   mirrors and could become a static export on GitHub Pages (like the gba
   arcade) — retiring BOTH review services eventually. A product decision
   (W2's per-site purpose review), not part of W1.

**What the estate would cost after items 1–6** (from § 3's measured
numbers): the mechanical items alone — W1's three services, the orphan DB,
weekly backups, sleep on three sites — remove **~$5–6/cycle**. The dominant
lever is item 1: control-plane's egress+CPU is ~$10 and *rising*, so the
landing zone is **roughly $12–18/cycle** depending on what its HTTP logs
show and how far the fix goes, with the remaining floor set by the bot DB's
831 MB working set (item 2's pruning is what moves that). Doing everything
except item 1 leaves the next bill at or above this one.

## 6 · What this session did NOT do

No Railway mutation of any kind was made — no service stopped, no variable
touched, no trigger changed. The bot, both its databases, and all nine web
surfaces are exactly as found. Retirement remains owner-gated per the
cutover plan's execution gate, and W1 execution is its own session.
