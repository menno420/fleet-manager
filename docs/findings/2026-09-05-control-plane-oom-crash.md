# control-plane OOM crash — the crawler moved from `/orders` to `/queue`

> **Status:** `reference` · 2026-09-05 · owner-directed (*"Review the railway
> logs and find out why the deployment crashed"*).
>
> Certainty tags per
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).
> Everything in §§ 1–4 is `MEASURED` this session (Railway GraphQL over direct
> egress, the Railway crash mails in the owner's inbox, live HTTP probes, and
> the deployed SHA's source) unless tagged otherwise.

## 0 · The answer in five sentences

**`superbot-websites/control-plane` was OOM-killed twice — 2026-09-04 10:57Z
and 2026-09-05 08:25Z** — and Railway mailed the owner both times ("Deploy Ran
Out of Memory!"). The cause is the **same crawler DoS that
[the websites gate decision of 2026-08-20](https://github.com/menno420/websites/blob/main/docs/decisions.md)
— *"Seat-era heavy routes gated IN PLACE behind the owner overlay"* — fixed on
`/orders`, now moved to the one faceted page that fix deliberately left
public**: Meta-range crawlers (`57.141.x`, spoofed desktop UAs, robots.txt
ignored) are enumerating `/queue`'s multi-select filter permutations, an
unbounded URL space against a ~240 KB page that is rebuilt from scratch on
every request. That decision predicted this in writing — *"`/queue` is the other
faceted page — flagged to the owner as the likely next crawler target if the
fleet migrates, gate-ready with one line if he says so"* — and the prediction
came true 15 days later. Memory left a **flat 0.155 GB baseline** at 09-04
08:30Z, reached 1.459 GB by 10:30 and was killed at 10:57; it refilled to
**1.93 GB within two hours** and then sat at that ceiling for **19 hours** with
CPU welded to a full core before the second kill. The service is saturated
end-to-end: `/healthz`, which does no I/O at all, **took 11.97 s** on a live
probe. **No other Railway
service is affected** — the bot worker, spider-bot, shiftlife and the two
sleeping websites are all healthy, and nothing here touches the bot's hard rail.

## 1 · What crashed, and what did not (`MEASURED` 2026-09-05)

**This does not show up as a broken deploy.** Across the account's **four
projects and nine services** (enumerated via
`me { workspaces { team { projects } } }`, then `services` per project), every
service's active deployment reads `SUCCESS`, and the 25 most recent deployments
per project carry **no `FAILED` and no `CRASHED` row**. The crash is a **runtime
OOM kill of a successfully-deployed container** — Railway records it only in the
crash mail and the metrics, never in deployment status. That is precisely why
looking at the deploy list first says "nothing is wrong".

| Project / service | State | Evidence |
|---|---|---|
| `superbot-websites/control-plane` | **CRASHING — OOM ×2** | crash mails 09-04 10:57Z, 09-05 08:25Z; memory cliff in § 2 |
| `superbot-production/worker` (the bot) | healthy | deployed 2026-08-25, still the active deployment; **no restart in the retained log window (09-02 → 09-05)** — no `Starting Container`, no traceback. Logs to 09-05 08:09Z are steady-state BTD6 ingestion + hourly gateway RESUMEs; the only failures are `warn`-level ingestion-source backoffs |
| `spider-bot/worker` | healthy | booted 09-04 19:27Z (`ready as Spider Bot#7153`), memory flat at 86 MB through the latest sample |
| `superbot-websites/dashboard`, `botsite` | healthy | their `Stopping Container` / `Starting Container` cycles are **app-sleep, not crashes** — `sleepApplication: true` on both; `control-plane` has it `false` |
| `shiftlife/shiftlife-api` + both Postgres | healthy / idle | no crash signal; shiftlife stays untouched per `OQ-RAILWAY-SHIFTLIFE-SCOPE` |

Railway service config, control-plane: `healthcheckPath: /healthz`,
`sleepApplication: false`, `restartPolicyType: ON_FAILURE`,
`restartPolicyMaxRetries: 10`.

## 2 · The memory cliff — the timing is unambiguous (`MEASURED`)

Railway `metrics(MEMORY_USAGE_GB)`, 30-minute samples. The deployment
(`aca47b5d`, commit `48b75de8`) went live 09-03 20:49Z and ran **flat at
0.154–0.155 GB for about eleven hours**:

| Time (UTC) | Memory | What it means |
|---|---|---|
| 09-03 21:00 → 09-04 08:00 | **0.154–0.155 GB** | healthy baseline, eleven hours flat |
| 09-04 08:30 | 0.166 GB | onset |
| 09-04 09:00 → 10:30 | 0.195 → 0.622 → 1.166 → 1.459 GB | monotone climb |
| 09-04 11:00 | **0.260 GB** | ← **first OOM kill** (crash mail 10:57:01Z) |
| 09-04 11:30 → 13:00 | 0.797 → 1.077 → 1.895 → **1.931 GB** | refills in 90 minutes |
| 09-04 13:00 → 09-05 07:30 | **1.85–1.93 GB, 19 hours** | pinned at the ceiling |
| 09-05 08:25 | **0.308 GB** → 0.093 GB | ← **second OOM kill** (crash mail 08:25:48Z) |

Over 09-05 06:00–08:20, `CPU_USAGE` sat at **0.89–1.03 — a full core, saturated,
continuously** — then collapsed to 0.14 at the kill.

**The ceiling is inferred from the SECOND kill only** (`REASONED`). At 30-minute
sampling the instantaneous peak before the *first* kill is unknown — the last
sample before it is **1.459 GB at 10:30**, and 1.93 GB is first observed only
after the restart. So the ~2 GB limit reading rests on the 19-hour 1.85–1.93 GB
plateau that preceded the second kill, not on both. I did not read a configured
limit field; if the Railway API exposes one, it should replace this inference.

**Which kill the traffic evidence actually covers (`REASONED` for the first).**
The request sample in § 3 spans **08:25–08:38Z on 09-05** — it is time-correlated
with the **second** kill only. Because the `httpLogs` date window does not bind
(below), traffic from the 09-04 onset cannot be recovered, so the crawler as
cause of the **first** OOM rests on the identical memory shape and the prior
`/orders` precedent — strong, and still an inference. The second kill is
`MEASURED`.

**Timing note (`MEASURED`, method):** the onset above is taken from the metrics
API, not from `httpLogs`. `httpLogs`' `afterDate`/`beforeDate` did **not** bind
on this deployment — three different one-hour windows returned byte-identical
5,001-row results (the `beforeLimit` cap). That is a second instance of the
2026-08-20 ledger entry warning that this endpoint's windowing is unreliable;
treat its date range as advisory and never time an event from it.

## 3 · The traffic — one page, one crawler (`MEASURED`)

Both figures below are **samples of the retained request log, not totals** — the
endpoint caps at `beforeLimit` and its date window does not bind (§ 2). Of the
**5,001 most recent requests** returned (the cap): **4,988 on `/queue`**, **4,998
from `57.141.x`** (Meta), and **4,438 of them HTTP 499** — the crawler hanging up
before the render finishes, while the app keeps paying for the abandoned work. A
separate 530-request sample spanning the second kill (08:25–08:38Z):

- **527 / 530 on `/queue`; 100 % from `57.141.x`.**
- Latency **mean 9,132 ms · p50 5,153 ms · p95 24,992 ms · max 25,014 ms**.
- **88.7 MB egress in ~13 minutes**, mean 167 KB per response.
- Statuses: 383 × 200, **94 × 499**, **53 × 502** (the app already dying).
- User agents: 339 Windows Chrome, 161 macOS Chrome, 26 Linux Chrome, 1
  Firefox — all spoofed desktop — and only **3 genuine `facebookexternalhit`**.

That last row is why the fix must stay **route-scoped and never an IP-range
block**: the real unfurler shares Meta's ranges, and a `57.141.0.0/16` 403 would
break WhatsApp/Messenger/Facebook/Instagram link previews for every shared link.
Decided upstream (2026-08-20 worklist § 3.1 and § 4); not re-litigated here.

Live probes against the running service, ~35 minutes after the second restart —
it is **already saturated again**:

| Probe | Result |
|---|---|
| `GET /healthz` | 200 in **11.97 s** — returns `{"ok":true,"cache_entries":170}`; **does no network I/O at all** |
| `GET /version` | 200 in **6.55 s** — reads an env var |
| `GET /queue` | 200 in **53.43 s**, 241,758 B |

A route that does no I/O taking twelve seconds means the service is **saturated
end-to-end** — and, importantly, that the Railway healthcheck configured on
`/healthz` is itself near failing. It does **not** localise *where* the delay
occurs: queueing behind accepted connections, CPU contention, and proxy
scheduling all fit equally, and no event-loop lag or handler timing was measured
(`REASONED`). The cheap-handler-still-slow observation rules out "the upstream
GitHub calls are slow" as the whole story; it does not by itself name the layer.

## 4 · Why `/queue` specifically — three multipliers (`MEASURED` at the deployed SHA)

Source read at `48b75de8`, the SHA the live `/version` reports.

1. **It is public, and it is faceted.** Only three routes carry the websites
   owner-overlay gate — `/prompts`, `/orders`, `/orders.json`. `/queue` (`app/main.py:531`)
   and `/queue.json` (`:557`) are credential-free. Its `FILTER_SPEC`
   (`app/owner_queue.py`) has **three multi-select dimensions** — `project`
   (derived live from source labels), `kind` (9 values), `age` (4:
   `<24h`/`1-7d`/`>7d`/`undated`) — **× 3 sorts × free-text `q`**, and
   `listfilter`'s `toggle_url` / `sort_url` / `clear_dim_url` render a link for
   every toggle on every page. Each crawled page therefore emits links to more
   permutations: a combinatorial, effectively unbounded URL space. The observed
   query strings are exactly that shape —
   `?project=…&project=…&kind=…&kind=…&age=%3E7d&sort=oldest`.
2. **Every request rebuilds everything.** `owner_queue.overview()` is **not
   memoized**, and neither is the `fleet.overview()` it rides. Only the raw
   GitHub HTTP responses are TTL-cached (`app/github.py`). That cache is keyed on
   the upstream URL, not the request query string, and live `/healthz` reports
   **170 entries** — which rules out *the crawler's filter permutations minting a
   cache entry each*, the obvious hypothesis. It does **not** exonerate the cache:
   170 is a cardinality, not a byte count, and entries are never evicted on
   expiry (only `clear_cache()` removes them). Cached response bytes over time
   were **not** measured, so the cache stays an unruled contributor
   (`UNVERIFIED` — a heap profile or a cache-bytes probe settles it). So per request
   the app re-fans-out `lane_status()` over every lane, re-parses each
   heartbeat, rebuilds `raw_items`, re-dedups into a dict, re-sorts, recomputes
   a uid per item, re-renders the fleet-manager `owner-queue.md` body to HTML,
   then runs `listfilter.apply` for another filtered copy and Jinja-renders
   ~240 KB. Concurrent requests share none of it.
3. **Nothing bounds the concurrency.** The Dockerfile CMD is a bare
   `uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}` — **one worker, no
   `--limit-concurrency`, no request timeout**. Taking both terms from the *same*
   sample (40.6 req/min arrival, 9.13 s mean residence, 08:25–08:38Z), Little's
   law puts **~6 requests in flight** (`REASONED`). An earlier draft of this
   finding said ~36 by pairing that arrival rate with the 53 s single probe taken
   35 minutes later — two different populations, and the mistake inflated the
   figure roughly sixfold; the 53 s probe bounds *one* request's residence under
   load, not the steady-state mean.

**What this section does and does not establish (`REASONED`, and the weakest
link here).** The three multipliers above are each `MEASURED` in the source, and
together they explain why `/queue` is expensive per request and unbounded in URL
space. They do **not** arithmetically account for 1.9 GB: ~6 concurrent requests
would each have to hold on the order of 300 MB, which is not something I
measured. **Per-request allocation was never profiled**, and the 19-hour plateau
does not by itself distinguish (a) a continuously large live request set, (b)
CPython holding freed arenas at the high-water mark, or (c) retention in the
cache or elsewhere — all three fit the same curve. The honest statement is that
the *trigger* is established and the *quantitative memory mechanism is not*; a
heap profile under load, or `tracemalloc` around one `/queue` request, is the
measurement that would close it. Nothing in the recommended fixes depends on
which of (a)–(c) it turns out to be.

The 89 % 499 rate is the amplifier — most of that memory and CPU is spent
rendering pages **no client is still listening for**.

## 5 · What this was, before it was a crash

This is not a new failure mode. The websites gate decision of 2026-08-20 fixed
exactly this attack on `/orders` — same range, same spoofed UAs, same 499 signature, same
ignored robots.txt — and its own verdict names the residual risk:

> *"The next-heaviest pages stay public deliberately: `/fleet` (211 KB) and
> `/queue` (150 KB) are live-tier surfaces, and `/queue` is the other faceted
> page — flagged to the owner as the likely next crawler target if the fleet
> migrates, gate-ready with one line if he says so."*

The flag was raised, correctly, and left as an owner decision. Fifteen days later
the crawler migrated. `/fleet` now redirects to `/repos` (measured at the deployed SHA,
`app/main.py:458`), so `/queue`
was the remaining faceted surface — and it is the one that fell over.

## 6 · Recommended fix — the owner's call, one line either way

Not implemented this session: the ask was to find out why, and the change lands in
`menno420/websites`, not here.

- **A (recommended — that decision's own prepared answer):** add
  `dependencies=[Depends(owner.require_owner_page)]` to `/queue` and
  `/queue.json`, exactly as `/orders` carries it. The gate runs **before** the
  route body, so an anonymous hit costs a <2 KB 401 instead of a 53-second
  render. `/queue` is an owner to-do surface with an already-gated writeback twin
  at `/owner/queue`; it has no anonymous audience. Reversible by deleting the
  clause. `app/nav.py` gated-label registries and `scripts/smoke_crawl.py` need
  the same treatment `/orders` got.
- **B (defense in depth — worth doing regardless, but read the caveat):**
  memoize `overview()` behind the existing TTL so concurrent requests share one
  rebuild — that is the cheap, unambiguous win, and it attacks the per-request
  cost directly. Bounding concurrency is the other half **and needs care**:
  uvicorn's `--limit-concurrency` is **global**, issuing HTTP 503 past the limit
  for *every* route — including `/healthz`, which is this service's configured
  Railway healthcheck. Setting it naively trades an OOM for failed health probes
  and a restart loop. If concurrency is capped, it needs to be route-scoped
  admission control, or reserved capacity for the health path, not a bare global
  flag.
  **B is not optional, because `/queue` is not the last faceted public route.**
  Enumerated at the deployed SHA (`grep listfilter.parse app/*.py`, with
  `/orders` as the positive control): five call sites — `/orders`
  (`main.py:745`, gated), the `/owner` env hub (`owner.py:399`, gated),
  `/queue` + `/queue.json` (`main.py:540,566`, public), and **`/repos`
  (`main.py:432`, public)**. `/repos` carries its own `REPOS_LIST_SPEC`
  (2 multi-select dimensions + sorts, `app/estate.py`) over an
  `estate_service.overview()` that shows **no memoization either**. So gating
  `/queue` alone leaves one public faceted surface of the same shape standing —
  A really can relocate the crawler rather than stop it, and `/repos` should be
  gated or bounded in the same change. (§ 5's "remaining faceted surface" refers
  to the three routes the 2026-08-20 decision weighed; `/repos` postdates it.)
- **Rejected, and stays rejected:** an IP-range block (breaks real link
  unfurling, § 3) and relying on robots.txt — measured ignored on 2026-08-20:
  **0 `/robots.txt` fetches in the 3,001 most recent retained requests** sampled
  that day (a capped sample, the same basis as § 3's counts, not a census of the
  day), and the crawl continues today.

Until one lands, the service will keep OOM-looping: it refilled to the ceiling
within 90 minutes of the first kill, and it was already saturated 35 minutes
after the second.
