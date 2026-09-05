# 2026-09-05 — why the Railway deployment crashed: control-plane OOM, and the crawler that moved to `/queue`

> **Status:** `in-progress` — a diagnosis, not a fix. The owner asked *"Review the
> railway logs and find out why the deployment crashed"*; the answer is
> `superbot-websites/control-plane`, OOM-killed twice (2026-09-04 10:57Z and
> 2026-09-05 08:25Z), and the finding is
> [`docs/findings/2026-09-05-control-plane-oom-crash.md`](../docs/findings/2026-09-05-control-plane-oom-crash.md).
> **The fix is deliberately not in this PR:** it lands in `menno420/websites`,
> not here, and choosing between the two options is the owner's call — option A
> was already prepared and flagged to him by the 2026-08-20 gate decision.
> Landed on green.

- **📊 Model:** withheld · high · research
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01JbCfvTw9YnPtg4ig8LoS6m](https://claude.ai/code/session_01JbCfvTw9YnPtg4ig8LoS6m)

💡 Session idea: **a crash that leaves no crash status is the one that survives
a status check.** Every deployment on the account reads `SUCCESS`, in all four
projects — the deploy list says nothing is wrong. A container that is OOM-killed
at runtime and restarted keeps its `SUCCESS` deployment status; the only places
the event exists are the crash mail Railway sends the owner and the memory
metric. Reading deployment status first, and stopping there, would have produced
a confident "nothing crashed" — which is what the first pass through the logs
actually produced, before the mail was checked.

## What this covers

An investigation only. No product code changed; the only files here are the
finding, this card, and the mechanical index/telemetry deltas.

## The chain, as measured

1. **Railway status is clean everywhere.** Four projects, nine services; every
   active deployment `SUCCESS`, no `FAILED` or `CRASHED` row in the 25 most
   recent deployments per project. The dashboard/botsite
   `Stopping`/`Starting Container` cycles are `sleepApplication: true`, not
   crashes — a decoy worth naming, because they look exactly like restarts.
2. **The crash mails name it.** `hello@notify.railway.app`, *"Deploy Ran Out of
   Memory!"* for `control-plane` in `superbot-websites` — 2026-09-04 10:57:01Z
   (×3) and 2026-09-05 08:25:48Z.
3. **The memory metric times it.** Flat at 0.154–0.155 GB for twelve hours, then
   0.195 → 0.622 → 1.166 → 1.459 GB across 09-04 09:00–10:30, kill; refill to
   1.93 GB in 90 minutes; **19 hours pinned at the ceiling** with CPU at a
   saturated full core; second kill 09-05 08:25Z.
4. **The traffic identifies it.** Of the 5,001 most recent requests, 4,988 on
   `/queue` and 4,998 from `57.141.x` (Meta), 4,438 of them HTTP 499. Mean
   latency 9.1 s, p95 25 s, 167 KB per response, all spoofed desktop UAs bar
   three genuine `facebookexternalhit`.
5. **The source explains it.** At the deployed SHA `48b75de8`: `/queue` is
   public and faceted (3 multi-select dimensions × 3 sorts × free text —
   unbounded URL space, with the filter widget emitting a link per toggle);
   `owner_queue.overview()` and `fleet.overview()` are **not memoized**, so every
   request rebuilds the whole graph; and the Dockerfile runs a bare single
   `uvicorn` with no `--limit-concurrency` and no request timeout. Concurrency ×
   per-request rebuild is the 1.9 GB.

## Traps this session hit, and what caught them

- **`httpLogs`' date window does not bind.** Three different one-hour windows
  returned byte-identical 5,001-row results. I had already started reading them
  as three measurements of the crawl over time; they were one sample three
  times. The onset timing in the finding comes from the metrics API instead,
  which did honour its range. This is a second instance of the 2026-08-20
  ledger entry about this endpoint — recorded there as empty-window unreliability,
  extended here to the window being ignored outright.
- **Two counts written as censuses.** "5,001 requests" and "no FAILED deployment
  anywhere" both went into the draft without their denominators; TRAP-004's
  route caught both, and the finding now carries the cap and the enumeration
  basis in the same sentence.
- **Foreign decision ids.** The draft cited `D-0036`/`D-0038`/`D-0012` bare in a
  fleet-manager doc, where those numbers name *different* fleet-manager
  decisions (its own D-0012 is a Gemini budget ruling). The stamp checker
  flagged the duplication; the fix — naming them as the websites decisions they
  are, with a link — was the more accurate wording anyway.

## What is NOT done, and why

The fix. Two options are in the finding's § 6: **A** gate `/queue` +
`/queue.json` exactly as `/orders` is gated (one clause each, already prepared
and flagged to the owner on 2026-08-20), and **B** bound the blast radius
(`--limit-concurrency`, memoize `overview()`), which is the durable half —
A moves this crawler to the next page, B stops any faceted route converting
traffic into an OOM. Both land in `menno420/websites`. A is his call because
gating a surface changes who can see it; B is uncontroversial but belongs in the
same change. Until one lands the service keeps OOM-looping: it refilled to the
ceiling within 90 minutes of the first kill and was already saturated 35 minutes
after the second.
