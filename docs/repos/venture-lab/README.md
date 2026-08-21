# venture-lab — the entry point

> **Status:** `living-ledger` · true as of **2026-08-21**
>
> **What this is:** fleet-manager's entry point for `menno420/venture-lab` —
> where the last session left off and where the next one should look.
> **Canonical for nothing.** The repo's own `docs/PROJECT-CLOSEOUT.md` wins on
> the handover, `docs/current-state.md` on its state (with the two staleness
> caveats below), `docs/conventions.md` on how work ships, and the live tree
> wins over all of them. Depth files are **not yet written** — created by the
> 2026-08-21 fleet review (Tier-1, "cleared to build" since 2026-08-08) and
> carries only the entry point so far.
>
> Certainty tags per
> [`../../findings/2026-08-05-foundation-continuation.md`](../../findings/2026-08-05-foundation-continuation.md).

## The one-paragraph answer

`venture-lab` is the estate's commerce lane ("Venture"): find and validate the
cheapest credible path to first revenue — **agents build, the owner clicks**.
What it holds now: **1 LIVE $29 Gumroad SKU** (Stripe Webhook Test Kit,
launched 2026-07-12, 0 organic sales measured), 19 publish-READY SKUs, 3
hard-gated bundles + photo packs, and **12 finished books** (The Night Kiln ×6,
Lull/DREAMLINE ×3, Ultramarine ×3) with 7 KDP-ready packages. Last merge:
#289, kit v1.20.1 → **v1.21.0** (2026-08-13, distribution wave). Last product
work: 2026-07-20/21 (closeout).

**The governing fact a session must carry in: OD-11 supersedes the repo's own
top threads.** The owner ruled 2026-07-26: *"let it sit"* — no kill-clock
action, no delist, no publish wave; he works the sellable-products angle
himself, at his own pace. The repo has **zero awareness of OD-11**
(`MEASURED` 2026-08-21: no hits in its docs): its `PROJECT-CLOSEOUT.md` § 3
and `launch/kill-clock-decision-packet.md` still present the (expired
2026-07-26) T+14 delist call and the publish wave as live top threads. **Do
not action delist/publish/kill-clock work from the repo's docs alone.**

## Threads

### Thread: product/publishing — **paused by OD-11** (owner-paced, indefinitely)

Where it stands: the catalog is built and waiting
(`docs/launch/CATALOG.md`); 19 OWNER-QUEUE rows are hard-gated on the
owner-only NL proofread; the publish clicks (`OQ-VENTURE-PUBLISH-CLICKS` —
note SWTK is already live), Stripe test keys (`OQ-VENTURE-STRIPE-KEYS`) and
the gotcha article (`OQ-VENTURE-GOTCHA-ARTICLE`) all wait in
[`../../owner-queue.md`](../../owner-queue.md) under OD-11's blanket hold.
What would resume it: the owner's word, nothing else.

### Thread: repo hygiene — **open at next touch** (small)

The repo's own `docs/current-state.md:64` still claims kit **v1.20.1**; the
tree is **v1.21.0** (`substrate.config.json`, #289 touched only kit files —
no restamp). A session doing any work here should restamp that line in
passing. The D2 truth pass also has venture-lab queued late in its order.

## Before you attach / modify — the traps, measured

- **Hard rails:** NO spend, account creation, publishing, or payment flows
  without explicit owner action (`README.md` § rails). NL proofread is
  owner-only.
- **The auto-merge enabler is ACTIVE** — a green READY `claude/*` PR
  squash-merges itself; opt out with a `do-not-automerge` label set at open.
- **`docs/publishing/OWNER-QUEUE.md` is GENERATED — never hand-edit**;
  regenerate via `scripts/derive_owner_queue.py`.
- The repo README is frozen in seat-era lane framing ("ORDER 001 in
  control/inbox.md") — the real front door is `docs/PROJECT-CLOSEOUT.md` § 5.
- Verify: `python3 bootstrap.py check --strict` + `python3 -m pytest
  scripts/test_*.py`; required on `main`: PR + exactly one check,
  `substrate-gate` (already the OD-9 one-check model). No deploy — merging
  is not publishing here.

## External workspaces

Pointers, never copies (the § 5.7 shape) — all **null today**: no Drive
folder, ChatGPT workspace, or Gemini notebook is mapped to `venture-lab` in
any record this review read. (Gumroad hosts the live SKU; its metrics are
owner-dashboard-only.) Add the pointer here when one exists.
