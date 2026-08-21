# 2026-08-20 — Railway keep-bot-only worklist EXECUTED (slices 1–5)

> **Status:** `in-progress` — branch `claude/railway-keep-bot-only-oxyxa3`.
> Born red; flips `complete` after review at the exact head and the landing
> checks. Executes
> [`docs/planning/2026-08-20-railway-keep-bot-only-worklist.md`](../docs/planning/2026-08-20-railway-keep-bot-only-worklist.md)
> in its § 6 order, one landing at a time.

- **📊 Model:** fable-5 · high · mechanical refactor

## previous-session review

The previous card (2026-08-20, keep-bot-only **plan**, fm #868) handed off a
state block and told this session to verify rather than trust it. Verified:
10 services ✓ (list re-read) · mineverse ids exact ✓ · mineverse project
volumes NONE ✓ · review sleeping ✓ · healthz timeout REPRODUCED (3×30 s,
21:39Z) · crawl re-sampled — and the state had WORSENED: the 17:30–18:00Z
httpLogs sample hit the query cap at 2,001 requests, 1,997 Meta-range, 1,947
on `/orders`, **every one HTTP 499**, with the app's runtime log silent
since 17:47:12Z (~4 h) — the board effectively down. One divergence from the
plan's premises, in the good direction: the Pages-create probe (slice 3
preflight) returned **201 over the direct PAT**, so slice 3 needed no owner
gate. Nothing in the handoff contradicted the tree.

## Shipped (this session, chronological)

- **Slice 1 — websites #508 (merged `74410ff`), the crawler DoS ended at the
  route layer.** `/orders` (~608 KB) + `/orders.json` (775 KB) + `/prompts`
  (513 KB) gated IN PLACE behind the [D-0012] overlay (websites D-0036);
  size audit measured every route live before choosing the set. Codex on the
  exact head `74c4015`: **0 findings**. Live-verified minutes after deploy:
  healthz **5×200, ≤ 0.62 s** (from 3×30 s timeouts) · anonymous `/orders`
  and facet URLs **42 B, ~0.2 s** (from ~620 KB) · owner Basic 200 at
  **620,461 B — the exact audited page size** · `/` and `/queue` publicly
  intact.
- **Slice 2 — mineverse off Railway.**
  `serviceDelete(id: "5cabd73c-3edf-49ef-b204-e8adfe49bc4c")` → `true`,
  then `projectDelete(id: "d6e6dc20-f3a7-45e2-bc01-1ab57f15a31b")` → `true`
  (the emptied project). Re-read:
  **3 projects / 9 services, superbot-mineverse absent**; old URL → 404 in
  0.3 s; the REPO untouched (exists, unarchived — verified).
- **Slice 3a — websites #509 MERGED (`b596b70`): the static-export
  mechanism.** Pages preflight GET 404 → POST (`build_type: workflow`) →
  **201** — venue https://menno420.github.io/websites/ created agent-side.
  `review/gen_static.py` + `review-pages.yml` + `review-bake` schedule
  retired (sb #2446 pattern) + websites D-0037 naming the losses (the live
  `/ask/api` AI path dies with the process; seeded answers survive).
  **Codex two rounds under the cap: R1 6/6 + R2 3/3 conceded and fixed** —
  among them three worth carrying: the bake's GITHUB_TOKEN pushes fire no
  workflows (measured: ZERO push-event runs exist on websites main at all —
  every landing is auto-merge/bot; explicit dispatch added), frozen
  relative ages on static pages (export-anchor banner added), and the
  origin-root robots.txt gap (per-page `noindex, nofollow` in static mode).
  **First deploy dispatched + verified: six route classes 200** (home,
  faceted list, editions, static /ask, Atom feed, the dotted-lane
  directory index). **3b (websites #510, the consumer cutover) opened once
  Pages verifiably served; `serviceDelete` only after it lands.**
- **Slice 4 — superbot #2450 MERGED (`5e3a667b`): the frozen-repo pollers.**
  `ci-rerun-watchdog` cron `*/12` out (dispatch kept) · `pr-conflict-guard`
  30-min sweep cron out (event triggers + pre-existing dispatch kept) —
  ~170 no-op runs/day gone; sb #2446 pattern, notes in headers. The repo's
  enabler armed auto-merge at open; **disabled by this session** so green CI
  could not race the R30 exact-head review — and it would have (all checks
  green ~10 min before Codex answered). Codex R1: 1 P2, [conceded] — three
  stale runbook rows fixed, including one #2446 itself left; R2 at the exact
  head `23f0975`: clean. Post-merge tree read-back: triggers
  `[workflow_dispatch]` and `[push, pull_request, workflow_dispatch]`.
- **Slice 5 — bot-DB sizing, read-only.** `sizing.yml` pushed to
  `menno420/estate-backups` main (`c1439ab`, fm #867 venue pattern):
  catalog SELECTs + COUNT(*) + min/max of date-typed columns only — size
  metadata, never row contents. One-shot `BOT_DB_DSN` sealed-box secret
  created agent-side (PUT 201, value never printed), dispatch 204; secret
  deleted after the log read. Results + prune proposal: § 8 addendum of the
  audit finding.
- **Slice 6 (PAT)**: nothing — `OQ-WEBSITES-PAT` still waits on the owner's
  UI mint; wire-on-paste stands.
- **Records (slice 7)**: this card · program § 7 row · audit finding § 8
  execution addendum · OQ updates (`OQ-RAILWAY-SHIFTLIFE-SCOPE` still OPEN —
  shiftlife untouched, both services verified present and running) ·
  CAPABILITIES ledger entries (Pages-create capability; httpLogs window
  quirk).

## Deliberately not done

- **shiftlife**: untouched (OQ open — one-letter call still pending).
- **worker + bot Postgres**: untouched beyond READ-ONLY catalog queries the
  worklist's slice 5 prescribes (hard rail intact; no stop/scale/
  disconnect/delete/config change).
- The mineverse **repo**, superbot app code, control-plane public posture
  beyond the three named routes.
- `/queue` (150 KB, the service's other faceted page) left public and
  flagged: likeliest next crawler target; the gate is one line if the owner
  wants it.
- reliable-grace's **4 orphan volumes** (postgres-botsite-volume + two
  suffixed strays beside the live postgres-volume) — observed during
  verification, NOT touched (hard-rail adjacency; disk is $0.27/cycle);
  flagged in the § 8 addendum for the owner.

## Verify

- (filled at close: per-slice live probes above; fm gate
  `python3 bootstrap.py check --strict` real exit code; Codex on the exact
  head of this records PR.)

## Session idea

- 💡 The bot's own BTD6 ingestion loop (one run per ~26 s, ~86 days, ~925 MB
  of history) is the same shape as the retired 2-hourly dashboard refresh —
  an EAP-era automation still producing against a concluded audience. The
  worklist's keep-criterion conversation probably wants a standing question:
  *"what does the worker still run on a timer, and who consumes it?"* — a
  one-shot read of the worker's scheduled tasks would enumerate the class
  instead of finding its members one bill at a time.
