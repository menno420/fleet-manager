# Owner steps — fleet-wide, 2026-07-18

> **Status:** `audit`
>
> Every open owner-only step across the fleet, grouped so you can knock out a
> batch in one sitting. Ordered by payoff. Links open to the exact page. Every
> item is: **what** it is → **why** it matters / what it unblocks → **steps**
> (every click) → **links** → **verify**. Where a value or price is needed, it
> is pasted inline. File links use `/blob/main/` so they open in the browser.
> All items were live-verified 2026-07-18. Where a queued item was already done,
> it is listed in the Appendix and dropped from the batches.

---

## BATCH 1 — 5-minute unblocks (mostly one click)

The highest payoff-per-second in the whole list. Each is a single click or one
short reply, and each one unsticks work that is otherwise finished and waiting.

### 1.1 — Merge the finished GBA Underroot v1.0 PR
- **What:** Merge the completed Underroot v1.0 pull request.
- **Why / unblocks:** It is ready with no conflict — only the agent-can't-merge wall holds it. Merging ships Underroot v1.0.
- **Steps:**
  1. Open https://github.com/menno420/gba-homebrew/pull/165
  2. Click **Merge pull request**.
  3. Click **Confirm merge**.
- **Links:** https://github.com/menno420/gba-homebrew/pull/165
- **Verify:** the PR header shows **Merged**.

### 1.2 — Ready-flip or close the 10 GBA draft PRs
- **What:** Move 10 draft PRs (Underroot slices 3–10, Brineward cuts 2–3) out of draft.
- **Why / unblocks:** Drafts never auto-land. Flipping each to "Ready for review" lets it merge on green; closing clears the queue. Either way the backlog stops looking stuck.
- **Steps (for each PR below):**
  1. Open the PR.
  2. Click **Ready for review** (it auto-lands on green) — or click **Close pull request** if it should not ship.
- **Links (one per PR):**
  - https://github.com/menno420/gba-homebrew/pull/157
  - https://github.com/menno420/gba-homebrew/pull/158
  - https://github.com/menno420/gba-homebrew/pull/159
  - https://github.com/menno420/gba-homebrew/pull/160
  - https://github.com/menno420/gba-homebrew/pull/161
  - https://github.com/menno420/gba-homebrew/pull/162
  - https://github.com/menno420/gba-homebrew/pull/163
  - https://github.com/menno420/gba-homebrew/pull/164
  - https://github.com/menno420/gba-homebrew/pull/177
  - https://github.com/menno420/gba-homebrew/pull/178
- **Do NOT touch:** #154 and #176 have merge conflicts — leave them alone. A session will rebase them and they will merge on their own. You do not need to fix those.
- **Verify:** each of the 10 shows **Ready** (green check pending/landing) or **Closed**.

### 1.3 — Answer the curious-research slicer question (one word)
- **What:** Tell the repo which slicer you use.
- **Why / unblocks:** The slicer guides can't be written until they know your tool.
- **Steps:**
  1. Open https://github.com/menno420/curious-research/pull/4
  2. Add a comment with exactly one of: `Cura`, `PrusaSlicer`, `OrcaSlicer`, or `Bambu Studio`.
- **Links:** https://github.com/menno420/curious-research/pull/4
- **Verify:** your one-word comment appears on the PR.

### 1.4 — Publish the GBA Lumen Drift release
- **What:** Cut the Lumen Drift v1.3 release with the built ROM attached.
- **Why / unblocks:** Agents can't push tags here (the release page is currently 404). This publishes the playable build.
- **Steps:**
  1. Open https://github.com/menno420/gba-homebrew/releases/new
  2. Tag: type `lumen-drift-v1.3`, target **main**.
  3. Attach the built `dist/lumen-drift.gba` file.
  4. Click **Publish release**.
- **Links:** https://github.com/menno420/gba-homebrew/releases/new
- **Verify:** https://github.com/menno420/gba-homebrew/releases/tag/lumen-drift-v1.3 loads (no longer 404).

### 1.5 — Point product-forge Pages at GitHub Actions
- **What:** Switch the Pages source so the site builds.
- **Why / unblocks:** The published page is currently 404 because Pages has no source.
- **Steps:**
  1. Open https://github.com/menno420/product-forge/settings/pages
  2. Under **Source**, select **GitHub Actions**.
  3. Click **Save**.
- **Links:** https://github.com/menno420/product-forge/settings/pages
- **Verify:** the page redeploys and stops returning 404.

### 1.6 — Make `pytest` a required check on superbot-idle
- **What:** Add `pytest` to the required status checks on `main`.
- **Why / unblocks:** Until it's required, a green PR isn't actually tested — the tests can be skipped.
- **Steps:**
  1. Open https://github.com/menno420/superbot-idle/settings/branches
  2. Edit the `main` branch protection rule.
  3. Under **Require status checks to pass**, add `pytest`.
  4. **Save changes**.
- **Links:** https://github.com/menno420/superbot-idle/settings/branches
- **Verify:** `pytest` appears in the required-checks list for `main`.

---

## BATCH 2 — GitHub settings sitting (rulesets / required checks)

All in GitHub settings, no external accounts. Knock these out together — you're
already logged in.

### 2.1 — gba-homebrew: confirm the required-checks set
- **What:** Line up the required checks so PRs auto-land as intended.
- **Why / unblocks:** This is why born-red PRs there look stuck — `substrate-gate` is currently **not** required, and the real gate is the ROM-build checks. Reconciling the set makes green mean "lands".
- **Steps:**
  1. Open https://github.com/menno420/gba-homebrew/settings/rules
  2. Also check https://github.com/menno420/gba-homebrew/settings/branches
  3. Decide the required set (candidates: `ROM builds`, `nds-rom-build`, `substrate-gate`) and reconcile the exact context names against the live check-run names on a recent PR.
  4. Save the ruleset.
- **Links:** https://github.com/menno420/gba-homebrew/settings/rules · https://github.com/menno420/gba-homebrew/settings/branches
- **Verify:** a green PR now shows all-required-passed and auto-merges.

### 2.2 — pokemon-mod-lab: protect main + require `ROM builds`
- **What:** Add a ruleset on `main` and require the ROM build.
- **Why / unblocks:** This is the fleet's only unprotected default branch — anything can land unchecked.
- **Steps:**
  1. Open https://github.com/menno420/pokemon-mod-lab/settings/rules
  2. **New ruleset** targeting `main`.
  3. Require status check: `ROM builds` (and keep `substrate-gate`).
  4. Save.
- **Links:** https://github.com/menno420/pokemon-mod-lab/settings/rules
- **Verify:** `main` shows the ruleset and required checks.

### 2.3 — substrate-kit: swap the required checks
- **What:** Update which checks are required on `main`.
- **Why / unblocks:** The required list names checks that no longer exist, so nothing can go green.
- **Steps:**
  1. Open https://github.com/menno420/substrate-kit/settings/rules
  2. Edit the `main` ruleset.
  3. **Remove** required checks `Kit test suite` and `Cold-adoption smoke`.
  4. **Add** required check `kit-quality`.
  5. Set **Require branches to be up to date before merging** to **OFF**.
  6. Save.
- **Links:** https://github.com/menno420/substrate-kit/settings/rules
- **Verify:** the ruleset lists `kit-quality` and no longer lists the two removed checks.

### 2.4 — superbot-next: set artifact retention to 400 days
- **What:** Raise Actions artifact retention.
- **Why / unblocks:** Restore-verify needs old artifacts to still exist.
- **Steps:**
  1. Open https://github.com/menno420/superbot-next/settings/actions
  2. Under **Artifact and log retention**, set **400** days.
  3. Save.
- **Links:** https://github.com/menno420/superbot-next/settings/actions
- **Verify:** retention shows 400 days.

### 2.5 — superbot-next (optional): kill the update-branch dance
- **What:** Enable a merge queue, or drop "require up to date" on the main ruleset.
- **Why / unblocks:** Removes the repeated "update branch" step before merges.
- **Steps:**
  1. Open https://github.com/menno420/superbot-next/settings/rules
  2. Either enable a **merge queue**, or turn **OFF** "Require branches to be up to date before merging".
  3. Save.
- **Links:** https://github.com/menno420/superbot-next/settings/rules
- **Verify:** PRs no longer require a branch update immediately before merge.

---

## BATCH 3 — Secrets & tokens (one PAT session + Railway)

Do the token minting in one sitting. Secrets are host/Actions values only —
never commit them to a repo.

### 3.1 — One websites fine-grained PAT covers three needs
- **What:** Mint a single fine-grained personal access token for `menno420/websites` and wire it into two places.
- **Why / unblocks:** Unblocks the owner-console git writeback **and** the nightly bake self-merge.
- **Steps:**
  1. Open https://github.com/settings/personal-access-tokens/new
  2. **Resource owner:** menno420. **Repository access:** Only select repositories → `menno420/websites`.
  3. **Permissions:** Contents = **Read and write**; Pull requests = **Read and write**.
  4. **Generate token** and copy it.
  5. In Railway (websites project), set the var `GITHUB_TOKEN` to that token on **both** the control-plane and botsite services.
  6. In GitHub, open https://github.com/menno420/websites/settings/secrets/actions and add an Actions secret `BAKE_PAT` with the same token.
- **Links:** https://github.com/settings/personal-access-tokens/new · https://github.com/menno420/websites/settings/secrets/actions
- **Verify:** owner-console writeback works and the nightly bake self-merges.

### 3.2 — websites Railway: Postgres + site password
- **What:** Add a database and set the tester password; remove a stray one.
- **Why / unblocks:** `DATABASE_URL` powers the app; `SITE_PASSWORD` on botsite opens the tester owner queue.
- **Steps:**
  1. Open the Railway console → project `superbot-websites` (https://railway.app).
  2. **Add PostgreSQL** to the project; copy its `DATABASE_URL` into the **botsite** service variables.
  3. Set `SITE_PASSWORD` on the **botsite** service.
  4. Delete the orphan `SITE_PASSWORD` variable on the **dashboard** service.
- **Links:** https://railway.app (project `superbot-websites`)
- **Verify:** botsite boots against Postgres and the tester owner queue is reachable.

### 3.3 — websites PayPal Payouts (real outbound money rail)
- **What:** Set up a live PayPal Payouts app and wire its keys.
- **Why / unblocks:** This is the real outbound-money rail. **Start early — approval takes days.**
- **Steps:**
  1. Ensure a PayPal **business** account at https://www.paypal.com
  2. At https://developer.paypal.com create a **Live** app; copy its **Client ID** and **Secret**.
  3. Request/enable **Payouts** on the app (approval can take several days).
  4. Set `PAYPAL_CLIENT_ID` and `PAYPAL_CLIENT_SECRET` on the **botsite** service in Railway.
  5. Leave `TESTING_AUTOPAY_ENABLED` **OFF**.
- **Links:** https://developer.paypal.com · https://www.paypal.com
- **Verify:** the app shows Payouts enabled; the two vars are set on botsite; autopay stays off.

### 3.4 — superbot-mineverse env vars (host, names only)
- **What:** Set the ingest, write-relay, and OAuth env vars on the host.
- **Why / unblocks:** The snapshot **ingest** pair is the #1 unblock — it flips the site from the committed sample to live data.
- **Steps (set in Railway, names only — never in the repo):**
  1. Snapshot ingest (do first): `MINING_SNAPSHOT_RELAY_SHARED_SECRET` and `MINING_SNAPSHOT_PATH`.
  2. Write relay: `MINING_WRITE_ENDPOINT` and `MINING_WRITE_SHARED_SECRET`.
  3. Confirm the 4 Discord OAuth vars are set: `DISCORD_OAUTH_CLIENT_ID`, `DISCORD_OAUTH_CLIENT_SECRET`, `OAUTH_REDIRECT_URI`, `WEB_SESSION_SIGNING_KEY`.
- **Links:** https://github.com/menno420/superbot-mineverse/blob/main/docs/NEXT-TASKS.md
- **Verify:** the site serves live snapshot data (not the sample) and sign-in works.

### 3.5 — superbot-next production env (host, names only)
- **What:** Set the production data-plane and backup vars.
- **Why / unblocks:** Brings up the production bot and turns on backups.
- **Steps:**
  1. Secrets (https://github.com/menno420/superbot-next/settings/secrets/actions): `DISCORD_BOT_TOKEN_PRODUCTION`, `DATABASE_URL`, and backup secret `DATABASE_PUBLIC_URL`.
  2. Variables (https://github.com/menno420/superbot-next/settings/variables/actions): `SB_DATA_PLANE=prod`, `SB_PROD_ATTEST`, `BACKUP_ENABLED=true`.
- **Links:** https://github.com/menno420/superbot-next/settings/secrets/actions · https://github.com/menno420/superbot-next/settings/variables/actions
- **Verify:** production boots on the prod data plane and a backup run succeeds.

### 3.6 — fleet-manager `ROSTER_READ_TOKEN` (conditional)
- **What:** A read-only PAT for pokemon-mod-lab.
- **Why / unblocks:** Only needed **if** you keep roster autogeneration (pokemon-mod-lab is private, so the roster job can't read it without a token).
- **Steps:**
  1. Open https://github.com/settings/personal-access-tokens/new
  2. Repository access: Only `menno420/pokemon-mod-lab`; Permissions: Contents = **Read-only**.
  3. Generate and copy.
  4. Save it as Actions secret `ROSTER_READ_TOKEN` at https://github.com/menno420/fleet-manager/settings/secrets/actions
- **Links:** https://github.com/settings/personal-access-tokens/new · https://github.com/menno420/fleet-manager/settings/secrets/actions
- **Verify:** the roster-regen job reads pokemon-mod-lab without a 404.

---

## BATCH 4 — Money / publish / external accounts (decisions + real money)

These involve external accounts and, in some cases, real money. Read the WHY on
each before acting.

### 4.1 — venture Stripe TEST keys
- **What:** Paste test-mode Stripe keys into the local env file.
- **Why / unblocks:** Turns on the payment path for the membership kit.
- **Steps:**
  1. In `candidates/membership-kit/server/.env` (local only — **never commit**), add:
     ```
     STRIPE_SECRET_KEY=sk_test_…
     STRIPE_WEBHOOK_SECRET=whsec_…
     ```
  2. Use your **test-mode** keys from the Stripe dashboard.
- **Links:** https://github.com/menno420/venture-lab/blob/main/candidates/membership-kit/server/.env.example
- **Verify:** the membership-kit server accepts a test payment locally.

### 4.2 — venture Gumroad: publish the 10 digital kits
- **What:** Create and publish 10 Gumroad products.
- **Why / unblocks:** These are finished kits waiting on a storefront. Prices:
  - Membership-Site Boilerplate — **$49**
  - Agent Fleet Field Manual — **$39**
  - AI Novella Kit — **$29**
  - GitHub Webhook Test Kit — **$29**
  - Multi-Agent Control-Plane — **$29**
  - Template Pack — **$19** (pay-what-you-want)
  - Owner-Click Queue — **$19**
  - Merge-Wall Cookbook — **$19**
  - Kill-Rule Intake — **$15**
  - False-Green Test Trap — **$15**
- **Steps:**
  1. Open the paste-ready per-kit run for each product at the queue below.
  2. For each: create a Gumroad product, paste the provided title/description/price, upload the file, publish.
- **Links:** https://github.com/menno420/venture-lab/blob/main/docs/publishing/OWNER-QUEUE.md
- **Verify:** each product returns HTTP 200 on its Gumroad URL.

### 4.3 — venture Amazon KDP: account + publish
- **What:** Create a KDP account, finish the tax/bank interview, then publish the books.
- **Why / unblocks:** The tax/bank interview is the first row of every ~19-book run and gates all of them.
- **Steps:**
  1. Open https://kdp.amazon.com and create an account.
  2. Complete the **tax and bank interview**.
  3. Publish the books using the paste-ready runs in the queue.
  4. Note: the **Ship-It Bundle ($59)** is gated on membership-kit + template-packs being live first — do that one last.
- **Links:** https://kdp.amazon.com · https://github.com/menno420/venture-lab/blob/main/docs/publishing/OWNER-QUEUE.md
- **Verify:** the tax interview shows complete; books appear as published.

### 4.4 — venture money-decisions (the real-money commitments)
- **What:** Decide the paid commissions and hand off the off-repo assets.
- **Why / unblocks:** These are the only real-money commitments in venture; the seat's recommendation is to **Park** the three commissions.
- **Steps:**
  1. **D13 / D14 / D16** illustration commissions (**$1,200–$5,600**): recommended **Park** all three.
  2. **D10 / D11** photo-packs: decide storefront + price (gated).
  3. Hand off the **full-res photo originals** (V-PHOTO, off-repo) for the photo packs.
  4. Arrange a **native Dutch proofread** (V-PROOF, ~10 NL titles).
- **Links:** https://github.com/menno420/venture-lab/blob/main/docs/publishing/OWNER-QUEUE.md
- **Verify:** each decision is recorded (park/go) in the queue.

### 4.5 — venture SWTK T+14 kill check
- **What:** Check the GitHub Webhook Test Kit against its kill rule.
- **Why / unblocks:** Deadline **2026-07-26** — needs ≥1 organic sale or one qualified inbound, else delist.
- **Steps:**
  1. On or before 2026-07-26, open the launch log.
  2. Check for ≥1 organic sale or qualified inbound.
  3. If none: delist the product.
- **Links:** https://github.com/menno420/venture-lab/blob/main/docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md
- **Verify:** the log records the kill/keep decision by 2026-07-26.

### 4.6 — websites bot-control decision (gates the armed-control chain)
- **What:** Answer where live bot control should live.
- **Why / unblocks:** This is the gate for the whole armed-control chain — ASK-0002 and ASK-0003 follow from it.
- **Steps:**
  1. Answer Q-0004 (where live bot control lives) in the question router.
  2. Then set up ASK-0002 (a Discord OAuth app) and ASK-0003 (a scoped token / armed service).
- **Links:** https://github.com/menno420/websites/blob/main/docs/question-router.md
- **Verify:** Q-0004 has an answer recorded; ASK-0002/ASK-0003 can proceed.

---

## BATCH 5 — Standing decisions (one letter / one word)

These unblock downstream work with a single short answer. No building, just a
choice.

### 5.1 — Delete-vs-archive (gates Batch 6)
- **What:** Choose how retired repos/assets are disposed.
- **Why / unblocks:** Gates the Batch 6 gated releases.
- **Steps:** Answer **A** or **B** in the owner queue. Recommendation: **A** (harvest → archive, delete nothing).
- **Links:** https://github.com/menno420/fleet-manager/blob/main/docs/owner-queue.md
- **Verify:** the delete-vs-archive item shows your answer.

### 5.2 — Approve the apparatus-sizing recommendation
- **What:** Approve the keep/slow-down recommendation for fleet-manager's own automation.
- **Why / unblocks:** Right-sizes the apparatus without deleting anything.
- **Steps:** Approve the recommendation: keep merge-on-green / substrate-gate / roster-freshness + the S3/S5/S9 checkers; slow `roster-regen.yml` from every-2h to daily. Reply on the queue item.
- **Links:** https://github.com/menno420/fleet-manager/blob/main/docs/owner-queue.md (OQ-FM-APPARATUS-SIZING)
- **Verify:** OQ-FM-APPARATUS-SIZING shows approved.

### 5.3 — substrate-kit: three rulings
- **What:** Three small kit decisions.
- **Why / unblocks:** Clears the kit's standing questions.
- **Steps:**
  1. (a) Public-flip the repo **or** provide a read-only PAT.
  2. (b) Kit-lab daily cron: **arm or retire** — recommendation **A**, arm `0 6 * * *`.
  3. (c) Self-pin version ruling — recommendation **A**.
- **Links:** https://github.com/menno420/substrate-kit/blob/main/control/status.md
- **Verify:** all three are recorded in the status doc.

### 5.4 — superbot-games: four reversible design decisions
- **What:** Ratify four design calls.
- **Why / unblocks:** Unsticks the games build.
- **Steps:** Decide: audit-grants ratify · rung-3 packaging · persistence format · transfer-policy.
- **Links:** https://github.com/menno420/superbot-games/blob/main/control/status.md
- **Verify:** the four decisions are recorded in the status doc.

### 5.5 — venture D1–D19
- **What:** Clear the storefront-default decisions.
- **Why / unblocks:** Mostly one-word "agree" clears Gumroad storefront defaults.
- **Steps:** Read D1–D19 in the queue; answer each (mostly "agree").
- **Links:** https://github.com/menno420/venture-lab/blob/main/docs/publishing/OWNER-QUEUE.md
- **Verify:** D1–D19 all show a decision.

### 5.6 — trading-strategy: go or defer
- **What:** Per-seat go/defer call.
- **Why / unblocks:** No rush — the grader is a no-op until ~August.
- **Steps:** Reply "per-seat go" or "defer".
- **Verify:** the call is recorded.

### 5.7 — idea-engine: review the phone-controller plan
- **What:** Review the phone-as-Bluetooth-controller plan.
- **Why / unblocks:** Lets that build proceed or park.
- **Steps:** Review and comment on the PR.
- **Links:** https://github.com/menno420/idea-engine/pull/481
- **Verify:** your review is on PR #481.

### 5.8 — curious-research: drybox design (one line)
- **What:** Approve the drybox design direction.
- **Why / unblocks:** Lets the drybox guide be written.
- **Steps:** Add a one-line answer. Recommendation: **A**.
- **Links:** https://github.com/menno420/curious-research/blob/main/docs/eap-closeout-walkthrough-2026-07-14.md
- **Verify:** the drybox item shows your one-line answer.

---

## BATCH 6 — Gated releases (only after Batch-5 #5.1 = A)

Do these **after** you've answered delete-vs-archive as **A** in Batch 5.

### 6.1 — codetool-lab-sonnet5: cfgdiff v0.1.1
- **What:** Publish cfgdiff 0.1.1 to PyPI + tag it.
- **Why / unblocks:** Ships the tool release.
- **Steps:**
  1. On https://pypi.org register a **trusted publisher** for the project.
  2. Tag and push:
     ```
     git tag -a v0.1.1 0b1eb60 -m "cfgdiff 0.1.1"
     git push origin v0.1.1
     ```
- **Links:** https://github.com/menno420/codetool-lab-sonnet5/blob/main/control/status.md
- **Verify:** the release publishes to PyPI and the tag exists.

### 6.2 — codetool-lab-fable5: envdrift releases
- **What:** Tag + GitHub Release for envdrift v0.1.0 and v0.2.0.
- **Why / unblocks:** Ships both envdrift versions.
- **Steps:**
  1. Tag v0.1.0 at commit `73ef38d` and create its GitHub Release.
  2. Tag v0.2.0 at commit `13a84e5` and create its GitHub Release.
- **Links:** https://github.com/menno420/codetool-lab-fable5/blob/main/control/status.md
- **Verify:** both releases appear on the repo's Releases page.

### 6.3 — product-forge: archive (or keep)
- **What:** Archive the repo, per the disposition.
- **Why / unblocks:** Closes out a retired repo.
- **Steps:** Open https://github.com/menno420/product-forge/settings and scroll to the bottom → **Archive this repository** (or keep it, per your disposition).
- **Links:** https://github.com/menno420/product-forge/settings
- **Verify:** the repo shows **Archived** (if you chose to archive).

### 6.4 — sim-lab: deploy the review site
- **What:** Deploy the VERDICT-011 review site (+ optional tag).
- **Why / unblocks:** Publishes the review site (no URL yet).
- **Steps:**
  1. Deploy the VERDICT-011 review site.
  2. Optionally tag `harness-v0.1.0`.
- **Links:** https://github.com/menno420/sim-lab/blob/main/docs/current-state.md
- **Verify:** the review site has a live URL.

---

## BATCH 7 — Optional / cosmetic (whenever)

Nothing depends on these; do them when it feels tidy.

- **Delete stale branches** (agents are 403-walled from deleting): websites ×4, gba `claude/brineward-wind`, pokemon-mod-lab ×3, fleet-manager `claude/consolidation-plan-v34`, curious-research, codetool-opus `claude/status-heartbeat-001`. Each repo's `/branches` page (e.g. https://github.com/menno420/fleet-manager/branches).
- **Veto passes:** 6 overnight menus (~266 proposals, all already on main; **no action = all build**). Only strike ids in the menu docs if you want to veto. Example: https://github.com/menno420/fleet-manager/blob/main/docs/planning/overnight-menu-2026-07-17.md
- **superbot-next:** review/delete 3 account triggers pending a decision.
- **codetool-opus:** optional PyPI `mdverify` publish; optional Claude GitHub App connect.

---

## BATCH 8 — Time-gated (after EAP goes read-only, Tue 2026-07-21 17:00 PT)

Do **not** start these before the EAP read-only cutover.

- **websites Railway consolidation** (reliable-grace vs superbot-websites): do **NOT** move or rename before 2026-07-21 — the Anthropic email links the reliable-grace URLs.
- **superbot-next** merge-flow / autonomy teardown (owner-sequenced; do the kit-config migration first).
- **Recreate the Projects fresh.**

---

## APPENDIX — Verified done, removed from the list

These were on earlier queues and are now confirmed resolved — no longer owner steps:

- **owner-actions-2026-07-17 §1–§3** — all 11 PRs merged/closed: websites #380, games #151, gba #153, idle #145, pokemon #94 / #87, next #503 / #499 / #500, games #149.
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
