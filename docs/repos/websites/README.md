# websites — the entry point

> **Status:** `living-ledger` · true as of **2026-08-21**
>
> **What this is:** fleet-manager's entry point for `menno420/websites` —
> where the last session left off and where the next one should look.
> **Canonical for nothing.** The repo's own `docs/decisions.md` wins on its
> decisions (the two 2026-08-20 entries — the route gate and the export
> losses — are this era's; ids stamped in the audit § 8 addendum), its
> `.sessions/` cards on session history, and the live tree wins over both. Depth files are **not
> yet written** — this folder was created on demand (the keep-bot-only
> execution session's close) and carries only the entry point so far.
>
> Certainty tags per
> [`../../findings/2026-08-05-foundation-continuation.md`](../../findings/2026-08-05-foundation-continuation.md).

## The one-paragraph answer

`websites` is the estate's four-service web repo: **control-plane** (the
owner's readiness board + journal browser), **botsite** (the SuperBot
marketing/testing site), **dashboard** (read-only bot inventory) — all three
on Railway in the `superbot-websites` project — and **review** (the EAP
program-review record), which since the **2026-08-20/21 cutover is a GitHub
Pages static export** at <https://menno420.github.io/websites/> with **no
Railway service behind it** (`MEASURED`: the venue was created + probed
serving 08-20, the consumers repointed and the service deleted 08-21; the
old `review-production-fc91` URL 404s). One committed data
layer (`app/data/*.json`) feeds the owner surfaces; the repo's own
`bootstrap.py check --strict` + the four pytest suites are the local gate,
and `quality` (with the born-red session-card hold) is the required CI
check. Codex reviews every PR on the bare literal `@codex review`.

## Threads

### Thread: keep-bot-only execution — **LANDED**, 2026-08-20/21

The owner's "keep only bot things" direction, executed in three PRs
(fleet-manager card:
[`.sessions/2026-08-20-railway-keep-bot-only-execute.md`](../../../.sessions/2026-08-20-railway-keep-bot-only-execute.md);
evidence table:
[audit § 8 addendum](../../findings/2026-08-14-railway-websites-audit.md)):

- **#508** (`74410ff`) — the crawler DoS ended at the route layer:
  `/orders` + `/orders.json` + `/prompts` gated in place behind the
  [D-0012] owner overlay (websites' decisions ledger carries the entry);
  route-scoped, never an IP-range 403 (facebookexternalhit shares Meta's
  ranges).
- **#509** (`b596b70`) — the static-export mechanism: `review/gen_static.py`
  (TestClient walk, pretty URLs, base-path + idempotent host-root rewrite),
  `review-pages.yml` deploy workflow, `review-bake` schedule retired; the
  export-losses decision in websites' ledger names what dies with the
  process (the live `/ask/api` AI path; seeded answers survive as static
  pages).
- **#510** (`f0e5bd3`) — the consumer cutover: nav strips ×4 → Pages, both
  registries shed the mineverse group and the last duplicate rows,
  dashboard `/reviews` → the Pages index, and the retirement semantics
  (`retired`/`static-venue` states in `app/envdrift.py`/`app/envhub.py`)
  keep `/owner/environments` and the hub honest about a deleted service
  whose CODE still documents its env reads. Then the `serviceDelete`.

**Traps this work measured, worth knowing before touching the repo:**
pushes/merges attributed to `GITHUB_TOKEN` fire **no** push-event workflows
on this repo (zero push-event runs exist on main) — the Pages rebuild after
a merge needs an explicit `review-pages.yml` dispatch; the exporter's
"exit 0" proves all routes rendered 200, **not** link integrity (the
double-prefix P1 shipped through it — grep the tree, don't trust the exit);
and the owner-gate throttle (`app/owner.py`, 10/60 s) leaks across test
files run back-to-back — the envhub-family files carry the autouse
`reset_rate_limits` fixture for exactly that.

**One satellite-side staleness to carry** (`MEASURED` 2026-08-21): websites'
own `docs/current-state.md` — a declared readpath doc there — still asserts
the pre-cutover world (review live on Railway, scheduled bake, kit v1.20.1).
A session booting in websites (boot-triad case two, where this entry never
loads) or trusting that ledger gets the dead URL; the tree and this entry are
right, and a restamp there is a next-touch item.

### Thread: open follow-ups — **PAUSED (owner-gated or next-touch)**

- `/queue` (150 KB, the other faceted page) is left public deliberately —
  likeliest next crawler target; the gate is one line behind
  `require_owner_page` on the owner's word.
- `/owner/environments` honestly reports **48 documented-with-defaults
  names unset live + 1 undocumented live name** across the three Railway
  services (`MEASURED` 2026-08-21, post-cutover; the drift computation's
  inputs were proven unchanged by the cutover). Old config debt the page
  exists to surface — an owner read, not a defect.
- **Three dead links on the live control-plane — `smoke-crawl` has been
  reporting them and the run reads as noise** (`MEASURED` 2026-08-22, both by
  the crawler and by an independent fetch). `smoke-crawl` is **not broken**;
  it is red *because these are real*, and its last runs are 2 failures / 0
  successes. Unrelated to any archiving — nothing in the estate is archived.
  - `/journal/product-forge` → **404**
  - `/projects/_inventory` → **404**
  - the `/fleet` page links to `pokemon-mod-lab/blob/main/docs/current-state.md`,
    which returns **403** to an unauthenticated visitor because that repo is
    **private**. The crawler logs this one as 404; the independent fetch says
    403, so its status codes are not verbatim reliable — the brokenness is.
  **Why this is a follow-up and not a fix already:** the first two are content
  calls (create the page, or remove the link?) and the third is a design call
  (should the public fleet page link into private repos at all?). Recorded here
  rather than only in the program's §7 row, because §7 is append-only history
  and this repo has already measured that a commitment left in RECORD tier is
  read as history and never actioned.
- `OQ-WEBSITES-PAT` (fleet-manager owner queue): the **rate-limit token**
  for control-plane's readiness polling — Tier 1 recommended: public-repo
  **read-only, zero permission boxes** (Tier 2's actions:write is optional
  and only for the `/owner` re-run button). Still waits on the owner's UI
  mint (mint is UI-only, `MEASURED` 2026-08-16); wire-on-paste stands.

## External workspaces

Pointers, never copies (the § 5.7 shape) — all **null today**: no Drive
folder, ChatGPT workspace, or Gemini notebook is mapped to `websites` in
any record this session read. A deliberate null, so the next session can
tell it from an incomplete handoff; add the pointer here when one exists.
