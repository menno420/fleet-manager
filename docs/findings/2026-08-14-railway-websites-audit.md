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

## 0 · The answer in four sentences

The August 13 bill is **$30.73 (~€30), all of it usage**: the billed cycle
(Jul 13 → Aug 13) was the **first full month the whole EAP-era estate ran
24/7** — 14 always-on services across 4 projects, where the June cycle
($7.75) had only ~half of them for part of the month. Half the bill is
**memory for services that duplicate each other or serve a concluded
purpose** (three of the nine websites are old copies the cutover plan already
retires); more than a third is **network egress** (~234 GB) concentrated in
the `superbot-websites` project. A separate defect found on the way: the
frozen `superbot` repo's 2-hourly `dashboard-data-refresh` workflow pushed to
`main` **~344 times in the billed cycle, rebuilding and restarting the LIVE
Discord bot ~11×/day** — churn that serves only the old dashboard site that is
itself a retire target. Executing the already-written cutover plan (websites
`docs/plans/site-consolidation-cutover.md`, prerequisites cleared) plus
disabling that one workflow removes the duplicates, stops the bot restarts,
and cuts the run-rate roughly in half; App Sleep on the low-traffic keep
sites cuts most of the remainder.

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
| | **postgres-botsite** | *(internal)* | Postgres serving ONLY the old botsite (`DATABASE_URL` host verified = `postgres-botsite.railway.internal`). Orphan once old botsite retires. |
| `superbot-websites` (created 07-09) | **control-plane** | `control-plane-production-abb0…` | Fleet readiness board + journal browser over the estate's repos, live from the GitHub API. |
| | **botsite** | `botsite-production-cfd7…` | **Canonical** SuperBot marketing/reference site + `/submit` idea intake + `/testing` tester program (Postgres-backed). |
| | **dashboard** | `dashboard-production-a91b…` | **Canonical** read-only bot-inventory dashboard (+ Discord-gated `/admin`). |
| | **review** | `review-production-fc91…` | **Canonical** EAP program-review site (built for Anthropic reviewers; audience concluded 07-21). |
| | **Postgres** | *(internal)* | The new botsite's database (`/submit`, `/testing`). |
| `superbot-mineverse` (created 07-12) | **web** | `web-production-97636…` | The mineverse staged web app (read-only degraded; live mode still blocked on env-var secrets). |
| `shiftlife` (created 07-25) | **shiftlife-api** | `shiftlife-api-production…` | The ShiftLife app's sync/share server. |
| | **Postgres** | *(internal)* | ShiftLife's database. |

All nine web surfaces returned 200 on `/healthz` (mineverse serves its app on
`/`; it has no `/healthz` route). The gba-homebrew arcade is GitHub Pages —
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
the cycle) implies the final week ran ~$2.6/day vs ~$0.60/day before —
the estate's cost was still **accelerating** at cycle close, consistent with
the v1.21.0 rollout week's deploy volume and rising site traffic.

Why the 4× jump from June's cycle: `superbot-websites` (5 services) was
created 07-09, `superbot-mineverse` 07-12, the second review copy 07-12, the
new botsite Postgres 07-19, and `shiftlife` 07-25 — the June cycle billed a
half-built estate for part of a month; the July cycle billed all 14 services
for a full month. **The €30 is the run-rate of the estate as built, not a
one-off spike.**

## 3 · Where it goes, per service (`MEASURED` — Railway usage API, billed cycle)

<!-- PER-SERVICE-TABLE -->

## 4 · The churn defect: the frozen repo redeploys the production bot 11×/day

`MEASURED` from Railway's deployments API, billed cycle Jul 13 → Aug 13.
"Real" excludes `SKIPPED` records (watch-path filtered): a `REMOVED` status is
a deployment that built, went live, and was later replaced — i.e. a restart.

| Service | Real deployments in cycle | Since Aug 1 | Watch filter |
|---|---|---|---|
| reliable-grace/**worker** (the live bot) | **344** | 148 (~11/day, ongoing) | **none** (`watchPatterns: []` — rebuilds on every push) |
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

This costs money (builds + deploy churn), but the bigger issue is
operational: **the live bot's process is being bounced ~11 times a day by a
cron that exists to freshen a website that is itself a retire target.**
Nothing in the frozen repo's docs records this as intended behavior.

## 5 · Consolidation — the recommendation

The cutover plan already exists and its prerequisites are closed
(websites `docs/plans/site-consolidation-cutover.md`, ground truth corrected
by websites #407; program track W1, OD-8). What this audit adds is the cost
attribution and two items the plan predates. Recommended order:

1. **Stop the bot-restart churn.** Two independent levers, both reversible:
   (a) **disable `dashboard-data-refresh.yml` in `superbot`** (one workflow
   edit) — its only consumer is the old dashboard site, a retire target;
   (b) **give `worker` a watch filter** (`watchPatterns: ['disbot/**']` via
   `serviceInstanceUpdate`) so pushes that don't touch bot code stop
   restarting the bot — the same mechanism the old botsite already uses
   successfully. Lever (a) alone stops ~330 builds/month of dashboard+worker;
   lever (b) alone protects the bot from ANY future push noise in the frozen
   repo. Doing both is cheap and correct.
2. **Execute W1 as written** — per service, stop → watch → owner's explicit
   go → delete: `review-f027`, then `superbot-app` (old botsite), then
   `superbot-dashboard` (old dashboard). The `f027` EAP-link constraint has
   lapsed. Never touch `worker` or the bot's `Postgres` (per plan; operate
   by exact service id, never project-level).
3. **Decide `postgres-botsite`** (this audit's addition — the plan's
   "never retire the two Postgres databases" protected the bot's infra; this
   third DB serves only the old botsite). After the old botsite is gone:
   dump it to a backup artifact, then stop/delete — or keep it stopped if
   the old `/submit` data should stay warm. Owner call, flagged not decided.
4. **Enable App Sleep on the low-traffic keep sites** (review-fc91,
   dashboard; consider botsite). They serve sporadic traffic; sleep stops
   the 24/7 memory meter between requests at the cost of a cold-start
   (~seconds) on first hit. Caveat: control-plane's background GitHub
   polling and any steady crawler traffic will keep a service awake —
   verify per service after enabling. The 6-hourly healthcheck/smoke-crawl
   crons wake them briefly; that is compatible.
5. **Check the egress driver on `superbot-websites`** (per § 3's numbers) —
   if it is crawler/bot traffic on the public sites, robots.txt +
   rate-limiting (or Railway's CDN caching, shipped July) are the levers;
   if it is the arcade's game downloads, cache headers do most of it. The
   daily `pg_dump` backup of the bot DB crosses Railway's public proxy
   uncompressed — if § 3 shows the bot Postgres transmitting GB/day, switch
   the backup cadence (daily → weekly + monthly, or prune the DB) before
   touching anything else.
6. **W2 candidate beyond the plan:** the review site's audience (EAP
   reviewers) concluded 07-21. It is server-rendered from committed data and
   could become a static export on GitHub Pages (like the gba arcade) —
   retiring BOTH review services eventually. That is a product decision
   (W2's per-site purpose review), not part of W1.

**What the estate costs after steps 1–4** (from § 3's measured per-service
numbers): <!-- POST-CUTOVER-ESTIMATE -->

## 6 · What this session did NOT do

No Railway mutation of any kind was made — no service stopped, no variable
touched, no trigger changed. The bot, both its databases, and all nine web
surfaces are exactly as found. Retirement remains owner-gated per the
cutover plan's execution gate, and W1 execution is its own session.
