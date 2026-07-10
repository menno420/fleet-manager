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

## Active queue (HOT first)

1. **🔥 HOT — kit F-5 one-letter ruling (A or B).**
   - WHAT: read two short paragraphs and reply with one letter — which reading
     of the benchmark pass/fail rule is intended. Reading A (strict
     none-regressing) vs Reading B (7k-budget-purposive) produce OPPOSITE
     verdicts on the same evidence; the B1 bench's whole 1-PASS/2-FAIL headline
     hangs on it.
   - WHERE: substrate-kit `docs/ideas/rubric-f5-none-regressing-wording-2026-07-09.md`.
   - HOW: reply "A" or "B" in any channel (or an inbox order).
   - WHY owner-only: bench/rubric is a pin path; the idea file reserves the
     call ("Agents do not resolve this one") — it's product judgment on what
     the rubric MEANS.
   - UNBLOCKS: run-2/run-3 verdicts un-disputed; run-4 lands under a ruled
     reading; honest KF-5 release notes.

2. **venture-lab ⚑A–D — the revenue clicks (zips are ON MAIN, upload-ready).**
   PR #9 merged 05:11:50Z: both buyer zips are committed —
   `candidates/membership-kit/dist/membership-kit-v0.2.zip` and
   `candidates/template-packs/dist/template-packs-v0.1.zip`.
   - **⚑A — Stripe TEST keys:** free Stripe account → Developers → API keys →
     copy `sk_test_…` into `STRIPE_SECRET_KEY` and the webhook `whsec_…` into
     `STRIPE_WEBHOOK_SECRET` in `candidates/membership-kit/server/.env` (from
     `.env.example`). Test mode only; no real money. UNBLOCKS the live
     test-mode purchase→webhook→grant E2E.
   - **⚑B — publish membership-kit at $49:** Gumroad or Lemon Squeezy → new
     product → paste `candidates/membership-kit/LISTING.md` → upload the
     committed membership-kit-v0.2.zip → Publish.
   - **⚑C — (optional) Supabase + Discord accounts** for the hosted
     production stack (URL/key + invite URL into `server/.env`).
   - **⚑D — publish template-packs at $19 PWYW:** same marketplace → paste
     `candidates/template-packs/LISTING.md` → upload the committed
     template-packs-v0.1.zip → Publish. (The $59 `candidates/BUNDLE-LISTING.md`
     goes live after ⚑B+⚑D — it needs their live URLs.)
   - Rider (repo settings, 1 min): give venture-lab a self-landable path —
     either make `substrate-gate` a REQUIRED check on `main`, or accept the
     lane filing a merge-on-green workflow. The classifier walled agent
     self-merge there twice (verbatim denials in venture-lab
     `control/status.md`); without one of these, every overnight venture PR
     waits for a click.
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
     (PRIVATE — never publish); PRs #4–#7.
   - HOW: one play session; drop reactions as a PR comment or inbox order —
     "keep/tune/drop" per patch is enough.
   - WHY owner-only: game-feel is taste; the headless harness proves the
     patches work, not that they feel right.
   - UNBLOCKS: which QoL patches lock in before deeper mod work.

4. **Concept picks — BOTH game-lab tracks (one message covers both).**
   - WHAT: Track B — pick 1 of 3 committed concepts (Lumen Drift / Clockwork
     Courier / Shoal); Lumen Drift is scope-complete with polish, so the pick
     decides continue-polish vs transfer, not sunk work. Track A — pick from
     its 3 committed mod concepts (ORDER 001 reserves both picks to you).
   - WHERE: gba-homebrew `docs/concepts/session-1-concepts.md`;
     pokemon-mod-lab's concepts doc.
   - HOW: any signal (inbox order or PR comment), e.g. "Track B: Lumen Drift;
     Track A: concept 2".
   - UNBLOCKS: locks the target for the remaining game-lab sessions.

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

6. **trading P5 holdout unlock — the last roadmap step (decision, 1 line).**
   - WHAT: authorize the one-shot holdout evaluation. Everything is
     pre-registered (13 subjects, frozen params, verdict rules fixed before
     any holdout number exists) in `docs/p5-holdout-protocol.md`; §7 requires
     an explicit owner ORDER — no session may start it on less.
   - WHERE/HOW: append an order to trading-strategy `control/inbox.md` naming
     the protocol binding (the manager can draft it — you say "unlock").
     Recommendation (decide-and-flag): unlock now; the protocol is one-shot
     and ties/ambiguity already resolve against the strategy.
   - UNBLOCKS: the final ranked report's §Holdout — the lab's terminal
     deliverable.

7. **Wake-routine arming — recorded as PLATFORM GAP, no click possible.**
   - WHAT: routine/trigger creation is walled on BOTH sides — agents
     (self-arm attempts failed fleet-wide with recorded errors, capabilities.md)
     AND this owner account (the console lacks the option — verified at the
     2026-07-10 paste session). There is nothing to click today.
   - INTERIM: lanes run **self-terminal** (every session leaves work safe with
     no future wake needed — already founding law in the gen-2 texts); the
     wake substitute is timed watch workers + **a morning "continue" message
     per Project** (one paste each, any order).
   - UNBLOCKS (when the platform ships the surface): the fleet running on
     orders without manual wake-ups — re-promote to a click item then.

8. **Review the 10 PROPOSED instruction packages.**
   - WHAT: `docs/proposals/instructions/` — 10 gen-2 founding packages.
     TWO are now DEPLOYED in fitted ≤7,500-char form (websites,
     trading-strategy — the exact live texts are recorded in each file's
     "Deployed fitted version" section); 8 remain PROPOSED, none binding
     until pasted.
   - WHERE: the README index + per-file §2 blocks; paste-time delta-8
     checklist in the README.
   - HOW: read at leisure; veto/edit by comment; paste order recommendation
     is in the README.
   - UNBLOCKS: relaunch texts for the remaining lanes when their turns come.

## Parked (valid, no rush)

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

- Fleet environments created — gen-2 lanes booted in them overnight (item 1 retired).
- venture-lab + game-lab launch click-lists executed (items 14/17 retired);
  gen-1 wind-down pasted and completed fleet-wide (item 15 retired).
- Merge session done: kit #26 + #49 MERGED ~00:10Z (ratifications live),
  games #5 MERGED 00:00:58Z (items 3/6/8/16 retired); kit #22 retro-ratify
  comment superseded by the #26 ratification lane closing.
- Gen-1 wind-down prompt, external ChatGPT campaign, and Anthropic-email
  items consolidated (campaign closed with gen-1; email pack parked above).
