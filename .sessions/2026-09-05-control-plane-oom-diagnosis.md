# 2026-09-05 — why the Railway deployment crashed: control-plane OOM, and the crawler that moved to `/queue`

> **Status:** `complete` — a diagnosis, not a fix. **One Codex round at the
> flip head: 10 findings, 10 conceded** (3 P1), two of them factual errors in
> my own numbers; all corrected, and one of them overturned in my favour by
> enumerating rather than asserting. The owner asked *"Review the
> railway logs and find out why the deployment crashed"*; the answer is
> `superbot-websites/control-plane`, OOM-killed twice (2026-09-04 10:57Z and
> 2026-09-05 08:25Z), and the finding is
> [`docs/findings/2026-09-05-control-plane-oom-crash.md`](../docs/findings/2026-09-05-control-plane-oom-crash.md).
> **The fix is deliberately not in this PR:** it lands in `menno420/websites`,
> not here, and choosing between the two options is the owner's call — option A
> was already prepared and flagged to him by the 2026-08-20 gate decision.
> Landed on green.

- **📊 Model:** withheld · xhigh · research
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01JbCfvTw9YnPtg4ig8LoS6m](https://claude.ai/code/session_01JbCfvTw9YnPtg4ig8LoS6m) · "Railway deployment crash"

💡 Session idea: **a crash that leaves no crash status is the one that survives
a status check.** Every deployment on the account reads `SUCCESS`, in all four
projects — the deploy list says nothing is wrong. A container that is OOM-killed
at runtime and restarted keeps its `SUCCESS` deployment status; the only places
the event exists are the crash mail Railway sends the owner and the memory
metric. Reading deployment status first, and stopping there, would have produced
a confident "nothing crashed" — which is what the first pass through the logs
actually produced, before the mail was checked.

## previous-session review

**None — this is a fresh owner-directed ask, not a continuation.** The branch
was created for it and carried no prior work; `origin/main` was 15 commits
ahead of the stale local ref at boot, and after `git fetch origin main` the
branch sits exactly at `main` (`4121b4b`) with nothing of its own. Checked
rather than assumed, because the first `check --strict` run gated on
`.sessions/2026-09-04-couch-legend-glass-and-garden.md` — another session's
card — which is exactly what a stale `origin/main` looks like from the
added-card lane, and would have read as a real finding against this work.

The nearest prior thread is not a session but a decision: the websites gate of
2026-08-20, which fixed this same crawler on `/orders` and named `/queue` as
the likely next target. That prediction is the finding's § 5.

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
3. **The memory metric times it.** Flat at 0.154–0.155 GB for eleven hours, then
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
   `uvicorn` with no `--limit-concurrency` and no request timeout.
   **That establishes the trigger and the per-request cost — it does NOT explain
   the 1.9 GB.** Per-request allocation was never profiled and handler lifetimes
   were never measured, so the quantitative memory mechanism is open; the
   finding's § 4 names the measurement (a heap profile or `tracemalloc` around
   one `/queue` request) that would close it. Do not carry "concurrency ×
   rebuild = 1.9 GB" forward: it was withdrawn under review.

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

## Adversarial round — Codex, 10 findings, 10 conceded

One round at the flip head (`48ca8b1d`), 3 P1 / 6 P2 / 1 P3. **Every one was
correct**, and two were factual errors in my own numbers, not phrasing:

| # | Finding | Disposition |
|---|---|---|
| P1 | Concurrency figure mixed populations — a 9.13 s mean from one sample with a 53 s probe 35 min later | `[conceded]` — Little's law on matched terms gives **~6**, not 36; ~6× inflation |
| P1 | 170 cache entries is cardinality, not bytes — cannot exonerate the cache | `[conceded]` — restated: rules out permutation-keyed growth only; cache stays unruled |
| P1 | `--limit-concurrency` is global and 503s `/healthz`, the configured healthcheck | `[conceded]` — my own fix B would have traded an OOM for a restart loop |
| P2 | "A only moves the crawler" asserted with no remaining route shown | `[conceded]`, then **overturned in my favour** — see below |
| P2 | First OOM has no traffic evidence (the window did not bind) | `[conceded]` — first kill downgraded to `REASONED`, second stays `MEASURED` |
| P2 | 12 s probe = end-to-end delay, not localised event-loop starvation | `[conceded]` |
| P2 | robots count restated as a census of the day | `[conceded]` — sampling basis restored |
| P2 | Allocator explanation for the plateau is untested | `[conceded]` — now one of three named candidates |
| P2 | "peak before each kill ~1.93 GB" contradicted by my own table | `[conceded]` — 1.459 GB before the first; ceiling inferred from the second only |
| P3 | "twelve hours" flat baseline is eleven | `[conceded]` |

**The one that moved past Codex.** Its P2 on the fix ranking said: do not claim
gating relocates the incident unless a specific remaining route reproduces the
cost. Fair — I had asserted it from a partial read. Enumerating instead of
asserting (`grep listfilter.parse app/*.py`, with `/orders` as the positive
control) found **five faceted call sites, and `/repos` is public** with its own
spec over an unmemoized `estate_service.overview()`. So the claim was right and
my basis for it was not; the finding now names the route. Without the TRAP-003
route firing on my *corrected* sentence — a negative claim I was about to commit
— I would have shipped Codex's version, which is wrong in the other direction.

### Round 2 — 6 findings, 6 conceded, and the lesson is where they were

Round 2 at `6506b8c` found **the fixes had not propagated**: three of its six
were against **this card**, not the finding — the card still carried "concurrency
× rebuild is the 1.9 GB", still said twelve hours, and — the P1 — **still told a
next session to use `--limit-concurrency`**, the exact unsafe flag round 1 had
just made me withdraw from the finding. A handoff is read *instead of* the long
document, so a stale summary is not a cosmetic lag; it is the version that gets
implemented. Corrected here, and worth generalising: **when review changes a
claim, grep every surface that repeats it before calling the fix done.**

Its other three, all conceded: the replacement ~6 concurrency figure is also
unsupportable (the durations are proxy timings spanning the restart, and 89 % are
499s recording *client* disconnect — which my own § 4 argues is not when the
handler stopped), so the finding now offers **no** concurrency number; `/repos`
shares `/queue`'s *structure* but its cost was never compared, so it is "check
this next", not "the next victim"; and the causal attribution is `REASONED` for
**both** kills, not just the first — the 08:25–08:38 sample overlaps the second
kill but mostly covers the restarted service.

**What the round cost the finding's core:** nothing. The trigger (crawler on
`/queue`) survived every challenge. What did not survive is the *quantitative*
memory mechanism — ~6 concurrent requests do not obviously hold 1.9 GB, per-request
allocation was never profiled, and the finding now says so in its own § 4 rather
than implying the arithmetic closes.

## What is NOT done, and why

The fix. Two options are in the finding's § 6, and **§ 6 is the authority — this
paragraph is a pointer, not a spec**:

- **A** — gate `/queue` + `/queue.json` exactly as `/orders` is gated (one clause
  each, prepared and flagged to the owner on 2026-08-20). His call, because
  gating a surface changes who can see it.
- **B** — **memoize `overview()`** so concurrent requests share one rebuild:
  that is the unambiguous half. **If concurrency is also capped it must be
  route-scoped admission control or reserved health capacity — NOT a bare
  `--limit-concurrency`**, which is global and would return 503 for `/healthz`,
  this service's own configured Railway healthcheck, trading the OOM for a
  restart loop. An earlier draft of this card recommended exactly that flag;
  it was withdrawn under review, and a session acting on the old wording would
  have shipped the unsafe fix.

`/repos` (`main.py:432`) is the other public faceted route and shares `/queue`'s
structure — unbounded filter URL space over an unmemoized overview. **Its cost
was not measured**, so treat it as the next thing to check, not as a proven
second victim.

Both land in `menno420/websites`. Until one lands the service keeps OOM-looping:
it refilled to the ceiling within two hours of the first kill and was already
saturated 35 minutes after the second.
