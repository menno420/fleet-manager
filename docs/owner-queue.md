# Owner queue

> **Status:** `living-ledger` — the ONE deduplicated queue of things waiting on the owner.
> The manager adds/removes items; asks stay valid until acted on (playbook R11).
> Every item below must carry WHAT/WHERE/HOW/WHY/UNBLOCKS + proof it's owner-only (R17).

Rewritten 2026-07-10 (morning, after the gen-2 overnight launch) — every item
re-verified against live GitHub at HEAD. Superseded/stale items removed:
venture-lab repo exists (seeded + 9 PRs); kit #26/#49 and games #5 are MERGED
(00:07/00:12/00:00Z); the fleet environments exist (gen-2 lanes booted in them
overnight); the gen-1 wind-down, merge-session, and launch click-lists are DONE.
Full launch context: [`planning/gen2-launch-record-2026-07-10.md`](planning/gen2-launch-record-2026-07-10.md).

> **Amended 2026-07-10 (midday, round-3 brief §1c).** The pure DECISION items
> below (1 · 4 · 6 · 8, plus the concept/playtest picks in 3) are now
> **consolidated — with recommendations and defaults — in the owner decision
> sheet: superbot `docs/planning/round3-launch-pack-2026-07-10.md` §4**. Answer
> them THERE (one sitting, ten numbered calls); the entries below are kept as
> stubs so nothing dangles, and are no longer the full text — the §4 sheet is.
> New item 0 added: create the Idea Engine Project (standing autonomous core).

## Active queue (HOT first)

0. **Create the Idea Engine Project (superbot repo) — standing autonomous core.**
   - WHAT: create ONE new claude.ai Project on the **superbot** repo (not
     substrate-kit — the ideas pipeline `docs/ideas/` + router + grooming
     doctrine live in superbot) whose mission is: generate + groom ideas into
     `docs/ideas/`, promote the best into plans, and propose routing ORDERs to
     the manager for lane repos. It is one of the FOUR permanently-running
     Projects in the owner's standing-autonomous-core design (manager · Idea
     Engine · superbot-next builder · Product Forge), each on a ~2-hourly
     routine, looping without the owner.
   - WHERE/HOW: claude.ai → new Project on menno420/superbot; then paste the
     **routine text from superbot `docs/planning/round3-launch-pack-2026-07-10.md`
     §5** (the "Arm a recurring routine for this Project yourself…" block) as
     its first message — the Project arms its own routine via the verified
     recipe (`create_trigger`, cron every 2 hours; `capabilities.md` CAN
     entry); owner routine click only if that seat is walled.
   - NOTE: Product Forge seat: candidate TBD per corrected round3-launch-pack
     §5 (owner retracted venture-lab pairing, 2026-07-10); default fallback =
     seed a dedicated `product-forge` repo born-right with a required check.
     venture-lab keeps its own venture mission unchanged.
   - WHY owner-only: creating claude.ai Projects has no agent API surface
     (verified wall, `capabilities.md`).
   - UNBLOCKS: the standing autonomous core's idea-generation loop — the
     fleet generating its own work between owner sessions.

1. **🔥 HOT — kit F-5 one-letter ruling (A or B).** → **decision sheet §4.1**
   (superbot `docs/planning/round3-launch-pack-2026-07-10.md`; recommendation
   there: the stricter Reading A). Stub retained: reply "A" or "B" in any
   channel; kit-lab's dispatch is paused on it. Full context:
   substrate-kit `docs/ideas/rubric-f5-none-regressing-wording-2026-07-09.md`.

2. **venture-lab ⚑A–D — the revenue clicks (zips are ON MAIN, upload-ready).**
   PR #9 merged 05:11:50Z: both buyer zips are committed —
   `candidates/membership-kit/dist/membership-kit-v0.2.zip` and
   `candidates/template-packs/dist/template-packs-v0.1.zip`.
   - **⚑A — Stripe TEST keys:** free Stripe account → Developers → API keys →
     copy `sk_test_…` into `STRIPE_SECRET_KEY` and the webhook `whsec_…` into
     `STRIPE_WEBHOOK_SECRET` in `candidates/membership-kit/server/.env` (from
     `.env.example`). Test mode only; no real money. UNBLOCKS the live
     test-mode purchase→webhook→grant E2E.
   - **⚑B — publish membership-kit at $49:** ❄️ **FROZEN 2026-07-10: D1 Stripe
     defect (headline paid path never executed; customer_email null on live
     events + invalid {CHECKOUT_EMAIL} success-URL placeholder) — unfreezes
     when venture-lab's fix ORDER lands with a real-path test.** Do NOT
     publish until then. (When unfrozen: Gumroad or Lemon Squeezy → new
     product → paste `candidates/membership-kit/LISTING.md` → upload the
     committed membership-kit-v0.2.zip → Publish.)
   - **⚑C — (optional) Supabase + Discord accounts** for the hosted
     production stack (URL/key + invite URL into `server/.env`).
   - **⚑D — publish template-packs at $19 PWYW:** ❄️ **FROZEN 2026-07-10: D1
     Stripe defect (headline paid path never executed; customer_email null on
     live events + invalid {CHECKOUT_EMAIL} success-URL placeholder) —
     unfreezes when venture-lab's fix ORDER lands with a real-path test.**
     (When unfrozen: same marketplace → paste
     `candidates/template-packs/LISTING.md` → upload the committed
     template-packs-v0.1.zip → Publish. The $59 `candidates/BUNDLE-LISTING.md`
     goes live after ⚑B+⚑D — it needs their live URLs.)
   - Rider (repo settings, 1 min): give venture-lab a self-landable path —
     either make `substrate-gate` a REQUIRED check on `main`, or accept the
     lane filing a merge-on-green workflow. The classifier walled agent
     self-merge there twice (verbatim denials in venture-lab
     `control/status.md`); without one of these, every overnight venture PR
     waits for a click. This rider is part of the **§4.9 repo-settings sweep**
     on the decision sheet. Product Forge seat: candidate TBD per corrected
     round3-launch-pack §5 (owner retracted venture-lab pairing, 2026-07-10);
     default fallback = seed a dedicated `product-forge` repo born-right with
     a required check. venture-lab keeps its own venture mission unchanged.
   - WHY owner-only: marketplace/payment accounts and repo settings are
     owner surfaces (agents: no accounts, no money, no external publish —
     hard rail).
   - UNBLOCKS: first-revenue path for both products.

3. **pokemon-mod-lab playtest — 4 game-feel patches, ONE pass.**
   - WHAT: play the modded Emerald ROM once and react to the four QoL+
     increments shipped overnight: (1) instant text + running indoors,
     (2) reusable TMs + modern Exp. Share, (3) repel re-prompt + auto-run,
     (4) faster HP bars + battle messages.
   - WHERE: build artifacts / instructions in menno420/pokemon-mod-lab
     (now PRIVATE — flipped by the owner 2026-07-10, API-verified; the
     lane's rail says PRIVATE, never publish); PRs #4–#7.
   - HOW: one play session; drop reactions as a PR comment or inbox order —
     "keep/tune/drop" per patch is enough.
   - WHY owner-only: game-feel is taste; the headless harness proves the
     patches work, not that they feel right.
   - UNBLOCKS: which QoL patches lock in before deeper mod work.

4. **Concept picks — BOTH game-lab tracks.** → **decision sheet §4.3 + §4.4**
   (recommendations there: Track A QoL+ — better, play the 12 patches first;
   Track B order Lumen Drift release-prep so you can PLAY it before any new
   concept). Stub retained: any signal works (inbox order or PR comment),
   e.g. "Track B: Lumen Drift; Track A: QoL+". Full context:
   gba-homebrew `docs/concepts/session-1-concepts.md` + pokemon-mod-lab's
   concepts doc.

5. **kit P10 required-check swap + P4 daily-loop schedule.**
   - P10 (2 min): substrate-kit → Settings → Rules → `main` ruleset →
     required status checks: REMOVE "Kit test suite" and "Cold-adoption smoke
     (adopt + check --strict)", ADD `kit-quality` (GitHub Actions), and set
     "Require branches to be up to date" OFF (a green PR sat `behind` 10+ min
     overnight purely on that toggle). WHY owner-only: rulesets 403 on every
     agent path. UNBLOCKS: deleting the legacy alias jobs; ends the
     ~35-min queue-stall class.
   - P4: arm the daily lab loop — kit's ask is Console → kit environment →
     Schedules → New schedule, prompt from `docs/operations/lab-loop.md`
     § Arming, cron `0 6 * * *`. **PLATFORM-GAP caveat (item 7):** if the
     Schedules/routine pane is missing on your console too (it was at the
     2026-07-10 paste attempt), this collapses into item 7's interim: a
     morning "continue" message to the kit Project is the loop until the
     platform ships the surface.

6. **trading P5 holdout unlock (decision, 1 line).** → **decision sheet §4.2**
   (recommendation there: grant it — the protocol `docs/p5-holdout-protocol.md`
   is pre-registered, code-enforced, one-shot; the lab is otherwise done and
   idle). Stub retained: you say "unlock", the manager drafts the ORDER into
   trading-strategy `control/inbox.md` naming the protocol as binding.

7. **Wake-routine arming — self-arm rollout DISPATCHED (nothing to click unless a lane fails).**
   - WHAT: the "walled on BOTH sides" reading was corrected 2026-07-10
     (~morning, owner-verified): Project sessions CAN create their own
     in-Project routines (capabilities.md carries the correction; the walls
     stand for coordinator/worker surfaces and cross-session binding).
     **Self-arm rollout dispatched (ORDERs queued to all active lanes)** —
     venture-lab, substrate-kit, pokemon-mod-lab, gba-homebrew hourly
     (Class A); websites, trading-strategy 4-hourly (Class B), per
     blueprint §2a. **Recipe now VERIFIED (2026-07-10 ~11:01Z):** the
     claude-code-remote scheduling tools (`create_trigger` / `send_later`
     family), seat-dependent — two lanes are ALREADY armed and firing
     ("Created by Claude": trading-strategy 4-hourly, kit-lab hourly; owner
     recordings 11:01Z/11:04Z). Those two need nothing from you.
   - **Owner fallback ONLY if a lane's attempt fails with a recorded error**
     — then that lane's routine (or the morning-"continue" interim) becomes
     a click again; otherwise nothing to do here.
   - UNBLOCKS: the fleet running on orders without manual wake-ups.

8. **The 8 undeployed instruction packages.** → **decision sheet §4.8**
   (recommendation there: **don't paste any today** — several were written
   blueprint-blind; re-base them on the gen-3 blueprint delta and deploy in
   one sitting when the manager's gen-3 report lands). Stub retained:
   `docs/proposals/instructions/` — 2 of 10 DEPLOYED fitted (websites,
   trading-strategy, exact live texts in each file's "Deployed fitted
   version"); 8 PROPOSED, none binding until pasted.

## Parked (valid, no rush)

- **Account-wide visibility review** (carried over from the resolved
  pokemon-mod-lab URGENT item's second ask) — at your next settings pass:
  all 13 repos in the account were public at the 2026-07-10 night review;
  pokemon-mod-lab is now private, the rest — including fleet-manager (this
  owner queue is on the open internet) — remain public. Decide per-repo
  public/private; pairs with the decision sheet's §4.9 repo-settings sweep.
- **superbot-next grants** — intents toggles · sacrificial Discord account ·
  capped API key (band 7) · flag-13 ruling; folds into the band flow
  (superbot-next `control/status.md` ⚑). Lane stays gen-1 mid-mission.
- **websites product questions** — domains · /submit Postgres · /admin
  OAuth+home · restyle · cutover (websites `docs/owner/OWNER-ACTIONS.md`,
  each with a recommended default).
- **Anthropic email pack** — review + send; follow-up to the 07-09 22:29Z
  extension mail before the 2026-07-14 window close.
- **PyPI trusted-publishing registration** (~2 min) — token-less kit releases.
- **codetool-lab-opus4.8 v0.1.0 tag + Release** — tag-push 403; owner click
  at Releases → Draft. (Codetool Projects are CLOSED; repos stay.)
- **Archive the dead trading session** — claude.ai session list → ⋮ →
  Archive (still listed active).
- **Paper-doll PNG pack for mining** — art asset, whenever.

## Resolved since the last rewrite (2026-07-09 → this morning)

- **🚨→✅ pokemon-mod-lab flipped to PRIVATE (URGENT item, night-review Q16) —
  DONE by the owner, re-verified 2026-07-10 via the GitHub API
  (`repo.private` = true, `visibility: private`). The lane's "no exceptions"
  PRIVATE hard rail is now true; R22 verification unblocked. The second ask
  (account-wide visibility review) moved to Parked above as a normal item.**
- Fleet environments created — gen-2 lanes booted in them overnight (item 1 retired).
- venture-lab + game-lab launch click-lists executed (items 14/17 retired);
  gen-1 wind-down pasted and completed fleet-wide (item 15 retired).
- Merge session done: kit #26 + #49 MERGED ~00:10Z (ratifications live),
  games #5 MERGED 00:00:58Z (items 3/6/8/16 retired); kit #22 retro-ratify
  comment superseded by the #26 ratification lane closing.
- Gen-1 wind-down prompt, external ChatGPT campaign, and Anthropic-email
  items consolidated (campaign closed with gen-1; email pack parked above).
