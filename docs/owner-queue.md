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

> **Amended 2026-07-10 (afternoon, launch-readiness sweep).** Items 9–12 added
> from the 5-worker Q-0261 launch-readiness research (full classified checklist
> with citations: [`launch-readiness-2026-07-10.md`](launch-readiness-2026-07-10.md));
> codetool archive/release clicks added to Parked; flag-13 moved from Parked
> into item 12 (it is seat-3 finalize-first debt under Q-0261). No prior item
> removed.

> **Amended 2026-07-10 (night, package-centralization).** Items 13–14 added:
> the consolidated **Project package paste wave** (the "re-base + deploy in one
> sitting" that item 8's resolution promised — the re-based packages now live in
> [`../projects/`](../projects/README.md)) and the trading-strategy PR #37 merge
> click. Kit OA8 (item 11) is now a subitem of the paste wave. Parked
> codetool tag mislabel corrected with provenance (the un-released tags are
> **fable5**'s, not opus4.8's).

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
   - **⚑ LIKELY ALREADY DONE (evidence, 18:31Z wake — confirm & retire):**
     live `list_triggers` shows an **"idea-engine 2-hourly standing wake"**
     (`trig_01KBoHPaq…`, cron `0 */2 * * *`, enabled, last fired
     2026-07-10T18:05:20Z) — a firing in-Project routine strongly implies
     the Project exists and self-armed. Kept open only pending a heartbeat/
     repo trace from that seat; the ~20:31Z wake confirms and retires this.

1. ~~🔥 HOT — kit F-5 one-letter ruling (A or B).~~ **✅ RESOLVED 2026-07-10
   (Q-0262.1): Reading A** — routed as substrate-kit **ORDER 011** and already
   **EXECUTED by the kit lane** (kit PRs #127/#128; family headline re-scored
   **1 PASS / 3 FAIL** under Reading A; B-benches unpaused, B1 run-5 free to
   fire; record: kit `bench/results/cold-start/f5-ruling-order-011.md`; kit
   status @ 18:22Z confirms acked+done). Also listed in Resolved below.

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

4. **Concept picks — game-lab tracks.** Track A **✅ RESOLVED 2026-07-10
   (Q-0262.7): pokemon concept = QoL+** — effective **when the games program
   boots post-core** (not an immediate dispatch; the lane stays PARKED till
   then). **Track B still open** → decision sheet §4.4 (recommendation:
   order Lumen Drift release-prep so you can PLAY it before any new
   concept). Any signal works (inbox order or PR comment). Full context:
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

6. ~~trading P5 holdout unlock (decision, 1 line).~~ **✅ RESOLVED 2026-07-10
   (Q-0262.2): GRANTED** — routed as trading-strategy **ORDER 008 @ fd5e9fe**
   (protocol `docs/p5-holdout-protocol.md` binding). Lane has **ACKED** it
   (trading status @ 16:21:48Z: "acked=001–008"); execution deliberately
   waits for a FRESH dedicated session per protocol §7, sequenced after the
   now-done ORDER 007 significance bar. Holdout verified still SEALED at ack.
   Also listed in Resolved below.

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

8. ~~The 8 undeployed instruction packages (decision).~~ **✅ RESOLVED
   2026-07-10 (Q-0262 / ORDER 008 policy 3): they STAY undeployed until the
   gen-3 blueprint delta lands, then re-base + deploy in one sitting** —
   now standing doctrine at blueprint §4 (folded by the 18:31Z wake). No
   owner click until the manager's gen-3 report lands; the future deploy
   sitting will be a fresh, dated queue item. Reference:
   `docs/proposals/instructions/` — 2 of 10 DEPLOYED fitted (websites,
   trading-strategy); 8 PROPOSED, none binding until pasted.

9. **Create the `product-forge` repo + Product Forge Project (core seat 5, PRE-BIRTH).**
   - WHAT: (1) create a **public, empty** repo `product-forge` (default branch
     `main`); (2) create the Product Forge Project in claude.ai/code, attach
     the repo, paste the founding package (superbot
     `docs/planning/round3-founding-package-product-forge-2026-07-10.md` —
     branch-only until superbot PR #1948 merges); (3) after the forge's seed PR
     adds CI: tick *Allow auto-merge* + make the substrate gate / smoke check
     **required** (ORDER 000's report names the exact check and asks once).
   - WHERE/HOW: github.com/new; claude.ai → New Project; repo Settings after
     the seed PR.
   - WHY owner-only: repo creation is a verified agent 403 wall; Project
     creation has no agent API surface; required-check settings are
     agent-unreadable/unwritable.
   - UNBLOCKS: core seat 5 of the Q-0261 standing six — the products loop.
     Everything else (ORDER 000 walking skeleton, routine, control seed,
     environments-registry spec) is agent work riding its boot.

10. ~~Name the sixth core seat (DECISION, Q-0261.1).~~ **✅ RESOLVED
    2026-07-10 (Q-0262 / ORDER 008 policy 4): core seat 6 = the superbot hub
    Project** (games/maintenance — the recommended pick, adopted wholesale;
    **owner may veto** by striking this). Next agent step: the manager
    drafts the hub founding package; the owner click that remains (create
    the hub Project) rides that package. Also listed in Resolved below.

11. **kit OA8 — setup-script paste (🔥 gates the NEXT boot, seat 2).**
    *(Folded into paste-wave item 13(a) — do it there; kept as a stub so
    nothing dangles. The registry copy `projects/substrate-kit/setup-script.sh`
    supersedes the bare `docs/gen2/setup.sh` pointer below — read the
    package's meta first.)*
    - WHAT: paste substrate-kit `docs/gen2/setup.sh` verbatim into the kit
      environment's Setup script field.
    - WHERE: Claude console → kit environment settings → Setup script.
    - WHY owner-only: agents cannot read or write the settings dialog; the
      current script killed a session AT PROVISIONING (kit PR #47 casualty).
    - UNBLOCKS: reliable session starts for the relaunched kit Project — the
      one item that can kill seat 2's fresh boot itself. Do BEFORE its first
      session (if already pasted, say so and the ask is withdrawn — agents
      can't confirm).

12. **Settings-sweep additions (fold into the §4.9 sitting): superbot-next
    finalize-first set.**
    - WHAT: (a) create the **`superbot-plugin-hello`** repo (public, empty, no
      template) — Builder ORDER 002's gate; (b) **relax superbot-next's
      require-up-to-date merge rule** (or enable merge queue) — every session
      loses time to the update-branch dance (#86/#87 stranded), which directly
      degrades an unattended 2-hourly Builder loop. ~~(c) flag-13 corpus-red
      disposition~~ **✅ (c) RESOLVED 2026-07-10 (Q-0262.3): ACCEPTED** —
      routed as superbot-next **ORDER 009**, applied by the lane in next
      **#105** (decision record: superbot-next
      `docs/parity/flag-13-disposition-2026-07-10.md`; lane status confirms
      "OWNER-ACTION 1 (flag-13 corpus-red ruling) is CLEARED"). (a)+(b)
      remain the open clicks.
    - WHERE: github.com/new; superbot-next Settings → Rulesets.
    - WHY owner-only: repo creation + rulesets are agent 403 walls.
    - UNBLOCKS: Builder ORDER 002 done-when, unattended Builder wrap-ups,
      every parity pending→ported flip + the `report` CI leg.

13. **Project package paste wave (registry: [`projects/`](../projects/README.md)) —
    ONE sitting, ~6 clicks.** The centralized, gen-3/Q-0265-re-based console
    packages are committed (one dir per Project: instructions ·
    coordinator-prompt · setup-script · failsafe text · meta). This is the
    "re-base + deploy in one sitting" item 8's resolution promised. Source of
    truth = the repo files; after any future edit, re-paste. Read each
    package's `meta.md` first. The clicks (full detail: `projects/README.md`
    § Paste wave):
    - (a) **substrate-kit** — §2b continuous-mode amendment paste into the
      live kit coordinator chat + **OA8** (= item 11): paste
      `projects/substrate-kit/setup-script.sh` into the kit environment's
      Setup-script field.
    - (b) **product-forge** — §2b amendment paste into its live coordinator
      chat (belt-and-braces: the seat already operates continuous per its
      status @ `7f05aa8`, but the chat may still hold pre-Q-0265 §2 text).
    - (c) **sim-lab** — arm the failsafe **via the Routines screen** with the
      verbatim text in `projects/sim-lab/failsafe-prompt.md`, cron
      `0 1-23/2 * * *` (odd hours — keep the idea-engine pair stagger). WHY
      owner-only: the seat verifiably lacks `create_trigger`/`send_later`
      (OA-003, "tool not present in session toolset") — the lane has NO clock
      until this.
    - (d) **websites** — re-paste the v2 wake prompt
      (`projects/websites/coordinator-prompt.md`) into trigger
      `trig_017H9Qb9oxtLgUy6sw2gnSHg` (last committed record: v1-era text) +
      re-paste `projects/websites/instructions.md` (deployed text is the
      older pre-Q-0265 fitted version). Optional: retune `0 */4` → `0 */2`.
    - (e) **trading-strategy** — re-paste
      `projects/trading-strategy/instructions.md` (deployed CI is pre-Q-0265
      and pre-completion; the lane is parked green, so low rush).
    - (f) **superbot (optional)** — `projects/superbot/instructions.md` only
      if you host superbot sessions in a Project with an empty console field
      (`.claude/CLAUDE.md` auto-loads in-repo either way).
    - NOT in the wave (ride their seats' own boots — no click): fleet-manager,
      superbot-next, idea-engine (live seats current/equivalent); venture-lab,
      superbot-games, pokemon-mod-lab, gba-homebrew (parts ride their next
      boot); archives/pre-birth (nothing to paste).
    - WHY owner-only: console fields, Project chats, and trigger prompts have
      no agent write surface (verified walls).
    - UNBLOCKS: every live seat running on committed, current text — closes
      the chat-only/console-only drift class fleet-wide.

14. **trading-strategy PR #37 — owner merge click (final P5 report).**
    - WHAT: merge https://github.com/menno420/trading-strategy/pull/37 — the
      FINAL P5 holdout report. The holdout is **SPENT** (one-shot, run stamps
      2026-07-10T16:47Z) and the report is FINAL; the PR is
      **agent-unlandable behind a terminal classifier refusal** (no agent
      retries it — probe-once-per-seat doctrine).
    - WHERE/HOW: the PR's Merge button, ~10 s.
    - WHY owner-only: merge authorization classifier-denied on the lane's
      seat; terminal, not transient.
    - UNBLOCKS: the trading program's terminal state landing on main (verdict:
      0/13 clears significance; primary = RULE-PASS candidate, not a finding).

## Parked (valid, no rush)

- **Account-wide visibility review** (carried over from the resolved
  pokemon-mod-lab URGENT item's second ask) — at your next settings pass:
  all 13 repos in the account were public at the 2026-07-10 night review;
  pokemon-mod-lab is now private, the rest — including fleet-manager (this
  owner queue is on the open internet) — remain public. Decide per-repo
  public/private; pairs with the decision sheet's §4.9 repo-settings sweep.
- **superbot-next grants** — intents toggles · sacrificial Discord account ·
  capped API key (band 7); folds into the band flow (superbot-next
  `control/status.md` ⚑). Lane stays gen-1 mid-mission. (The flag-13 ruling
  MOVED to active item 12 — it is seat-3 finalize-first debt under Q-0261.)
- **websites product questions** — domains · /submit Postgres · /admin
  OAuth+home · restyle · cutover (websites `docs/owner/OWNER-ACTIONS.md`,
  each with a recommended default).
- **Anthropic email pack** — review + send; follow-up to the 07-09 22:29Z
  extension mail before the 2026-07-14 window close. Include the four routines
  platform bugs: (1) completed runs not inspectable from the Routines screen;
  (2) Runs panel vs Routines screen disagreement; (3) the arming
  seat-inconsistency; (4) **model attribution inconsistent across Routines
  screen / chat header / session self-report — no authoritative surface**
  (appended 2026-07-10: Routines menu shows fable-5 for all project-created
  routines while the websites fired session's chat header + own card said
  claude-sonnet-5 — websites PR #59, squash 2c89e96; evidence + probe:
  `capabilities.md` § routine self-arm rider).
- **PyPI trusted-publishing registration** (~2 min) — token-less kit releases.
- **codetool-lab-fable5 (envdrift) v0.1.0 + v0.2.0 tags + Releases** —
  tag-push 403; owner click at Releases → Draft: v0.1.0 @ `73ef38d`, v0.2.0 @
  `13a84e5`. (Codetool Projects are CLOSED; repos stay.) *Corrected
  2026-07-10 (package-centralization): this line previously said
  "codetool-lab-**opus4.8** v0.1.0" — a mislabel. opus4.8's (mdverify)
  v0.1.0/v0.2.0 Releases are **LIVE** (published 2026-07-09T16:56:21Z /
  17:57:53Z by `github-actions[bot]`; attested by its `control/status.md` @
  `80f6cd1` and the fable5 correction commit `a6cf1a9`). The repo with
  never-pushed tags is **fable5** — zero tags on its remote, verified
  `ls-remote --tags` at package build; owner-manual steps in its
  `docs/retro/project-review-2026-07-09.md` §(e). Provenance:
  `projects/codetool-lab-{fable5,opus4.8}/meta.md`.*
- **codetool archive toggles ×3 (paired DECISION).** All three codetool repos
  report `"archived": false` (API-verified 2026-07-10 ~15:12Z) while the
  ruling describes them as archived — unarchived public repos remain writable
  surfaces. WHERE: each repo Settings → Danger Zone → "Archive this
  repository" (~1 min each). PAIRED DECISION: archive now vs after the gen-3
  succession question settles — recommendation: **wait, then archive**
  (archiving makes the repos read-only and would break the NEXT-BOOT write
  rituals the succession packs expect).
- **cfgdiff v0.1.1 release — two clicks (codetool-lab-sonnet5).** (1) register
  the PyPI trusted publisher (pypi.org → Publishing → pending publisher: owner
  `menno420`, repo `codetool-lab-sonnet5`, workflow `release.yml`, environment
  `pypi`, ~2 min); (2) `git tag -a v0.1.1 0b1eb60 -m "cfgdiff 0.1.1" && git
  push origin v0.1.1` — do NOT tag v0.1.0 at `0260aae` (predates release.yml,
  fires nothing). cfgdiff 0.1.1 sits on main unreleased; release.yml has never
  fired. WHY owner-only: tag push is a credential-layer 403 on that seat.
- **Paper-doll PNG pack for mining** — art asset, whenever.

### Safe to delete / archive (housekeeping, consolidated 2026-07-10 · 18:31Z wake)

Everything here is verified spent — deleting/archiving loses nothing (all
state is committed in the repos). Do in one sitting whenever convenient.

- **Spent chats (archive in claude.ai):**
  - **OLD kit-lab coordinator chat** — **cutover VERIFIED**: its old hourly
    trigger `trig_01FnqnAQjLU2T8d16iHwWQ2h` is DELETED from the trigger
    registry and the fresh seat is live (new 2-hourly trigger fired
    16:02:43Z; fresh-seat heartbeat 16:17:12Z; F-1 rebind-then-delete
    executed). Archiving it can no longer kill anything.
  - **Dead trading gen-1 "ORDER 001 successor" session** — died at
    provision, still lists as active (carried ask; trading status ⚑(d)).
  - **Wound-down gen-1 lane chats generally** — every gen-1 lane committed
    its succession package on main; chat context is spent by design.
- **Stale branches (delete at each repo's branches page; agent
  branch-delete is a verified 403):**
  - codetool ×2 — `claude/status-heartbeat-001` (opus4.8) and
    `test/push-check` (sonnet5), ~10 s each.
  - superbot-games ×2 (per launch-readiness) — `mining/adopt-substrate-kit`
    (closed-unmerged-deliberate) and `mining/grid-encounters` (**verify tip
    is merged before deleting** — tip ≠ merged head at the survey).
- **NOT yet safe:** codetool repo archive toggles ×3 (paired decision above
  — wait until the gen-3 succession question settles); anything holding an
  open READY PR.

## Resolved 2026-07-10 (Q-0262 owner-rulings batch, reconciled by the 18:31Z wake)

The owner answered the round-3 decision sheet **wholesale** (superbot router
Q-0262; routed by the dispatch session as inbox ORDER 008 + lane orders):

- **kit F-5 ruling = Reading A** (Q-0262.1) — routed as kit ORDER 011,
  **executed** (kit #127/#128; headline 1 PASS / 3 FAIL; B1 run-5 unblocked).
- **trading P5 holdout unlock = GRANTED** (Q-0262.2) — routed as trading
  ORDER 008 @ fd5e9fe; lane acked; runs in a fresh dedicated session per the
  binding protocol.
- **superbot-next flag-13 disposition = ACCEPTED** (Q-0262.3) — routed as
  next ORDER 009, **applied** in next #105
  (`docs/parity/flag-13-disposition-2026-07-10.md`).
- **Core seat 6 = the superbot hub Project** (ORDER 008 policy 4) — owner
  may veto; manager drafts the founding package next.
- **pokemon concept = QoL+** (Q-0262.7) — effective when the games program
  boots post-core.
- **The 8 undeployed instruction packages stay undeployed** until the gen-3
  blueprint delta lands, then re-base + deploy in one sitting (policy 3 —
  now doctrine at blueprint §4).
- Fleet policies folded into doctrine same day (fleet-manager PR #33):
  family-level model names ONLY (blueprint §1); kit OWNER-ACTION grammar
  wins by definition, venture-lab conforms at next kit upgrade (playbook
  R17 rider).

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
