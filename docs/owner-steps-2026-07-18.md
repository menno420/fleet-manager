# Owner steps — fleet-wide, 2026-07-18

> **Status:** `audit`
>
> The consolidated fleet-wide step list, **re-sorted to the corrected doctrine**
> (owner #308/#309/#311). Yesterday's version over-routed agent-doable work —
> merges, ready-flips, settings changes, releases, branch-deletes — to the owner.
> Under the corrected model those are **normal agent work**: agents merge, flip,
> change settings, and cut releases directly. The genuine owner-only set is only
> **external accounts, real money, secret VALUES the owner holds, and
> product/intent decisions**. Anything an agent is refused in a given session goes
> to the **hub chat** (the owner-live chat outside Projects, full ability) — a
> venue note, not a capability wall.
>
> Three sections below: **✅ Done by agents** · **→ Handled in the hub chat** ·
> **👤 Genuine owner-only steps**. Every item keeps its exact link and any pasted
> value/price. All items were live-verified 2026-07-18.

---

## ✅ Done by agents (no owner action)

The corrected doctrine in action: these landed as ordinary agent work, not owner
clicks.

- **gba PR #177 — flipped Ready** (auto-lands on green). https://github.com/menno420/gba-homebrew/pull/177
- **gba PR #178 — flipped Ready** (auto-lands on green). https://github.com/menno420/gba-homebrew/pull/178
- **gba PR #165 — merged** — Underroot v1.0 shipped (the owner merged this himself while draining the gba pile 13 → 3). https://github.com/menno420/gba-homebrew/pull/165
- **Doctrine reconciliation — fleet-manager PR #313** — synced `current-state.md` /
  `owner-queue.md` to the #308/#309/#311 wording (agents land their own and sibling
  green PRs directly; merging is normal agent work; living docs never record a
  standing limitation). https://github.com/menno420/fleet-manager/pull/313

The remaining gba drafts (Underroot slices 3–10, Brineward cuts 2–3) are agent
ready-flip / close work, handled in-lane as the seats reach them; #154 and #176
carry merge conflicts and are left for a rebase pass (they merge on their own once
green). Not owner steps.

---

## → Handled in the hub chat (agent-doable, not owner clicks)

Every item here is settings / release / branch work an agent performs directly.
This Projects session's platform layer declined the direct settings and release
calls, so they are **routed to the hub session** (owner-live, full ability) — a
venue-specific note for this run, not a standing limit. The hub session (or the
owner, if he prefers the click) executes each with the target + URL below.

### Settings · rulesets · required checks

- **gba-homebrew — confirm the required-checks set.** Reconcile the ruleset so
  green means "lands": decide the required set (candidates `ROM builds`,
  `nds-rom-build`, `substrate-gate`) against the live check-run names on a recent
  PR. https://github.com/menno420/gba-homebrew/settings/rules ·
  https://github.com/menno420/gba-homebrew/settings/branches
- **pokemon-mod-lab — protect `main` + require `ROM builds`.** The fleet's only
  unprotected default branch. New ruleset targeting `main`, require `ROM builds`
  (keep `substrate-gate`). https://github.com/menno420/pokemon-mod-lab/settings/rules
- **substrate-kit — swap the required checks to `kit-quality`.** Edit the `main`
  ruleset: **remove** `Kit test suite` and `Cold-adoption smoke`, **add**
  `kit-quality`, set "Require branches up to date before merging" **OFF**.
  https://github.com/menno420/substrate-kit/settings/rules
- **superbot-idle — make `pytest` a required check on `main`.** Until it's required
  a green PR isn't actually tested. Branch protection → require status check
  `pytest`. https://github.com/menno420/superbot-idle/settings/branches
- **superbot-next — artifact retention → 400 days.** Restore-verify needs old
  artifacts to still exist. Settings → Actions → Artifact and log retention → 400.
  https://github.com/menno420/superbot-next/settings/actions
- **superbot-next (optional) — kill the update-branch dance.** Enable a merge queue
  or turn **OFF** "Require branches up to date before merging" on the `main`
  ruleset. https://github.com/menno420/superbot-next/settings/rules
- **product-forge — point Pages at GitHub Actions.** The published page 404s because
  Pages has no source. Settings → Pages → Source → **GitHub Actions** → Save.
  https://github.com/menno420/product-forge/settings/pages

### Releases · tags

- **gba — publish Lumen Drift v1.3.** New release, tag `lumen-drift-v1.3` on `main`,
  attach the built `dist/lumen-drift.gba`, Publish. Verify
  https://github.com/menno420/gba-homebrew/releases/tag/lumen-drift-v1.3 loads.
  https://github.com/menno420/gba-homebrew/releases/new
- **codetool-lab-sonnet5 — cfgdiff v0.1.1** and **codetool-lab-fable5 — envdrift
  v0.1.0 + v0.2.0** are release work, but **parked on the delete-vs-archive
  decision** (§ owner-only below) — do them once that call lands.
  https://github.com/menno420/codetool-lab-sonnet5/blob/main/control/status.md ·
  https://github.com/menno420/codetool-lab-fable5/blob/main/control/status.md

### Stale-branch deletes (fleet-wide)

- **Delete stale branches** across the fleet: websites ×4, gba
  `claude/brineward-wind`, pokemon-mod-lab ×3, fleet-manager
  `claude/consolidation-plan-v34`, curious-research, codetool-opus
  `claude/status-heartbeat-001`. Each repo's `/branches` page, e.g.
  https://github.com/menno420/fleet-manager/branches

---

## 👤 Genuine owner-only steps

The real owner-only set: external accounts, real money, secret VALUES the owner
holds, and product/intent decisions. Exact URLs and paste-blocks preserved.

### External accounts + real money

- **venture Gumroad — publish the 10 digital kits.** Finished kits waiting on a
  storefront. Prices: Membership-Site Boilerplate **$49** · Agent Fleet Field
  Manual **$39** · AI Novella Kit **$29** · GitHub Webhook Test Kit **$29** ·
  Multi-Agent Control-Plane **$29** · Template Pack **$19** (pay-what-you-want) ·
  Owner-Click Queue **$19** · Merge-Wall Cookbook **$19** · Kill-Rule Intake
  **$15** · False-Green Test Trap **$15**. Paste-ready per-kit runs in the queue.
  https://github.com/menno420/venture-lab/blob/main/docs/publishing/OWNER-QUEUE.md
- **venture Amazon KDP — account + publish.** Create the account, finish the
  **tax and bank interview** (it gates every ~19-book run), then publish using the
  paste-ready runs. The **Ship-It Bundle ($59)** is gated on membership-kit +
  template-packs being live first — do it last. https://kdp.amazon.com ·
  https://github.com/menno420/venture-lab/blob/main/docs/publishing/OWNER-QUEUE.md
- **venture Stripe TEST keys.** In `candidates/membership-kit/server/.env` (local
  only — never commit) add `STRIPE_SECRET_KEY=sk_test_…` and
  `STRIPE_WEBHOOK_SECRET=whsec_…` from your test-mode dashboard.
  https://github.com/menno420/venture-lab/blob/main/candidates/membership-kit/server/.env.example
- **venture money-decisions (real-money commitments).** D13 / D14 / D16
  illustration commissions (**$1,200–$5,600**): seat recommends **Park** all three.
  D10 / D11 photo-packs: decide storefront + price. Hand off the full-res photo
  originals (V-PHOTO, off-repo). Arrange a native Dutch proofread (V-PROOF, ~10 NL
  titles). https://github.com/menno420/venture-lab/blob/main/docs/publishing/OWNER-QUEUE.md
- **venture SWTK T+14 kill check** (deadline **2026-07-26**). Needs ≥1 organic sale
  or one qualified inbound, else delist. Record the kill/keep decision in the log.
  https://github.com/menno420/venture-lab/blob/main/docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md
- **websites PayPal Payouts (real outbound-money rail).** Start early — approval
  takes days. Business account → Live app (Client ID + Secret) → enable Payouts →
  set `PAYPAL_CLIENT_ID` + `PAYPAL_CLIENT_SECRET` on the **botsite** service in
  Railway, leave `TESTING_AUTOPAY_ENABLED` **OFF**. https://developer.paypal.com ·
  https://www.paypal.com

### Secret VALUES the owner holds (names only — never in a repo)

- **websites fine-grained PAT (one covers three needs).** Mint a fine-grained PAT
  for `menno420/websites` (Contents = R/W, Pull requests = R/W). Set Railway var
  `GITHUB_TOKEN` on **both** control-plane and botsite; add Actions secret
  `BAKE_PAT` with the same token. Unblocks owner-console git writeback + the nightly
  bake self-merge. https://github.com/settings/personal-access-tokens/new ·
  https://github.com/menno420/websites/settings/secrets/actions
- **websites Railway — Postgres + site password.** Add PostgreSQL, copy
  `DATABASE_URL` into the **botsite** service, set `SITE_PASSWORD` on **botsite**,
  delete the orphan `SITE_PASSWORD` on **dashboard**. https://railway.app (project
  `superbot-websites`)
- **superbot-mineverse env vars (host, names only).** Snapshot ingest first
  (`MINING_SNAPSHOT_RELAY_SHARED_SECRET`, `MINING_SNAPSHOT_PATH` — flips the site
  from sample to live data); then write relay (`MINING_WRITE_ENDPOINT`,
  `MINING_WRITE_SHARED_SECRET`); confirm the 4 Discord OAuth vars.
  https://github.com/menno420/superbot-mineverse/blob/main/docs/NEXT-TASKS.md
- **superbot-next production env (host, names only).** Secrets:
  `DISCORD_BOT_TOKEN_PRODUCTION`, `DATABASE_URL`, `DATABASE_PUBLIC_URL`. Variables:
  `SB_DATA_PLANE=prod`, `SB_PROD_ATTEST`, `BACKUP_ENABLED=true`.
  https://github.com/menno420/superbot-next/settings/secrets/actions ·
  https://github.com/menno420/superbot-next/settings/variables/actions
- **fleet-manager `ROSTER_READ_TOKEN` (conditional).** Only if you keep roster
  autogen: a read-only PAT for `menno420/pokemon-mod-lab`, saved as Actions secret
  `ROSTER_READ_TOKEN`. https://github.com/settings/personal-access-tokens/new ·
  https://github.com/menno420/fleet-manager/settings/secrets/actions

### Product / intent decisions

- **Delete-vs-archive** (gates the parked releases above). Answer **A** or **B**;
  recommendation **A** (harvest → archive, delete nothing).
  https://github.com/menno420/fleet-manager/blob/main/docs/owner-queue.md
- **Approve the apparatus-sizing recommendation** (OQ-FM-APPARATUS-SIZING). Keep
  merge-on-green / substrate-gate / roster-freshness + the S3/S5/S9 checkers; slow
  `roster-regen.yml` from every-2h to daily.
  https://github.com/menno420/fleet-manager/blob/main/docs/owner-queue.md
- **substrate-kit — three rulings.** (a) public-flip the repo or provide a read-only
  PAT; (b) kit-lab daily cron arm-or-retire (rec **A**, arm `0 6 * * *`); (c)
  self-pin version ruling (rec **A**).
  https://github.com/menno420/substrate-kit/blob/main/control/status.md
- **superbot-games — four reversible design calls.** audit-grants ratify · rung-3
  packaging · persistence format · transfer-policy.
  https://github.com/menno420/superbot-games/blob/main/control/status.md
- **venture D1–D19** storefront-default decisions (mostly one-word "agree").
  https://github.com/menno420/venture-lab/blob/main/docs/publishing/OWNER-QUEUE.md
- **trading-strategy — go or defer** (no rush; grader is a no-op until ~August).
  Reply "per-seat go" or "defer".
- **idea-engine — review the phone-controller plan (PR #481).**
  https://github.com/menno420/idea-engine/pull/481
- **curious-research — drybox design** (one line; recommendation **A**).
  https://github.com/menno420/curious-research/blob/main/docs/eap-closeout-walkthrough-2026-07-14.md
- **curious-research — slicer question** (one word: `Cura` / `PrusaSlicer` /
  `OrcaSlicer` / `Bambu Studio`). https://github.com/menno420/curious-research/pull/4
- **websites bot-control decision** (gates the armed-control chain). Answer Q-0004
  (where live bot control lives); ASK-0002 / ASK-0003 follow.
  https://github.com/menno420/websites/blob/main/docs/question-router.md

### Time-gated (after EAP goes read-only, Tue 2026-07-21 17:00 PT)

- **websites Railway consolidation** (reliable-grace vs superbot-websites): do NOT
  move or rename before 2026-07-21 — the Anthropic email links the reliable-grace
  URLs.
- **superbot-next merge-flow / autonomy teardown** (owner-sequenced; do the
  kit-config migration first).
- **Recreate the Projects fresh.**

### Optional / cosmetic (whenever)

- **Veto passes:** 6 overnight menus (~266 proposals, all already on main; **no
  action = all build**). Strike ids only to veto. Example:
  https://github.com/menno420/fleet-manager/blob/main/docs/planning/overnight-menu-2026-07-17.md
- **superbot-next:** review/delete 3 account triggers pending a decision.
- **codetool-opus:** optional PyPI `mdverify` publish; optional Claude GitHub App
  connect.

---

## APPENDIX — Verified done, removed from the list

These were on earlier queues and are now confirmed resolved — no longer owner steps:

- **This session (2026-07-18):** gba #177 / #178 flipped Ready (auto-land on green);
  gba #165 merged (Underroot v1.0); fleet-manager #313 doctrine reconciliation. All
  now in the ✅ section above.
- **owner-actions-2026-07-17 §1–§3** — all 11 PRs merged/closed: websites #380, games
  #151, gba #153, idle #145, pokemon #94 / #87, next #503 / #499 / #500, games #149.
- Both **veto-menu draft PRs** (#94 / #171).
- **OQ-FM-WAKE-CHAIN-ARM** (agent-resolved).
- **SWTK** published & live (Gumroad returns 200).
- **websites Decided rows A–N.**
- **superbot** seed-data.
- **superbot-idle** OA-001 / OA-002.
- **codetool-opus** releases live.
- **sim-lab** OA-005.
- **superbot-next** Postgres wall (non-reproducing in the default env).
- **gba #176** card (already complete).
- Stale **baton triggers** (already absent).
