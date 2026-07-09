# Owner queue

> **Status:** `living-ledger` — the ONE deduplicated queue of things waiting on the owner.
> The manager adds/removes items; asks stay valid until acted on (playbook R11).
> Every item below must carry WHAT/WHERE/HOW/WHY/UNBLOCKS + proof it's owner-only (R17).

Rewritten 2026-07-09 from the retro synthesis (deduplicated). Fast wins first-ish.

## Active queue

1. **Create the ≤4 fleet environments (trading first)** — ~3 min each; this
   ONE item replaces every earlier scattered environment ask (the old
   "trading + kit paste" item and the per-lane spec asks). Everything you
   paste lives in [`../environments/archetypes.md`](../environments/archetypes.md)
   (mapping + var names) and the four `environments/archetype-*.sh` scripts —
   all tested in-container 2026-07-09, incl. the exact two-source layout that
   killed the trading sessions (transcripts in PR #10).
   - WHAT: four claude.ai environments, one per archetype, covering every
     current + planned Project.
   - WHERE: **claude.ai/code → Environments → New environment** (steps 1–3);
     **edit the existing `multi-repo` env** (step 4). Then each Project →
     settings → Environment → select its archetype env.
   - HOW (in this order — trading first):
     1. **`pinned-research`** *(fixes the dead trading lane)*: New environment
        → name `pinned-research` → add repos `menno420/trading-strategy` +
        `menno420/substrate-kit` (+ `menno420/websites` if you want one shared
        env) → Setup script: paste the full contents of
        `environments/archetype-pinned-research.sh` → env vars: none for
        trading; add `GITHUB_PAT`, `RAILWAY_API_KEY`, `SITE_PASSWORD`,
        `DATABASE_URL` (websites' own app DB value) only if websites attaches
        here. **Never** add `RAILWAY_PROJECT_ID` / `RAILWAY_SERVICE_ID` /
        `RAILWAY_ENVIRONMENT_ID` to this env (production-pointing). Attach to
        the trading-strategy (and optionally websites) Project.
     2. **`python-lab`**: New environment → name `python-lab` → add repos
        `substrate-kit`, `codetool-lab-fable5`, `codetool-lab-opus4.8`,
        `codetool-lab-sonnet5`, `superbot-games`, `fleet-manager` (add
        `venture-lab` after its launch) → Setup script: paste
        `environments/archetype-python-lab.sh` → env vars: **none**. Attach to
        the lab/games/kit/manager Projects.
     3. **`bot-prod`**: New environment → name `bot-prod` → add repos
        `superbot-next` (+ `superbot` if the legacy lane needs it) → Setup
        script: paste `environments/archetype-bot-prod.sh` → env vars: copy
        the NAMES from the superbot-next row of `environments/archetypes.md`
        (values from your existing superbot env panel / Railway). This is the
        ONLY env allowed the production-pointing vars.
     4. **`multi-repo` (edit, don't create)**: open the existing multi-repo
        environment → replace its Setup script with
        `environments/archetype-coordinator.sh` → leave repos + vars as they
        are. (Fixes the superbot 3.10-vs-3.11 pip wrinkle automatically.)
   - WHY owner-only: agents cannot create/edit environments (verified wall,
     `environments/README.md`).
   - UNBLOCKS: dependency-green boots in every Project; retires the
     provision-death failure class (4+ lanes) fleet-wide; trading's gen-2
     relaunch.
2. **kit P10 required-check swap.**
   - WHAT: swap substrate-kit main's required status check — remove the stale
     context, require the current gate.
   - WHERE: github.com/menno420/substrate-kit → Settings → Branches/Rulesets →
     main → required status checks.
   - HOW: exact contexts to remove/add are listed in the kit's retro
     project-review ⚑ owner-actions (`docs/retro/project-review-2026-07-09.md`).
   - WHY owner-only: branch-protection edits 403 at the agent credential layer.
   - UNBLOCKS: kit PRs stop waiting on a check that never reports.
3. **Mining PR #5 — mark ready + merge (half done: you merged #9 at 19:02Z ✅).**
   - WHAT: superbot-games PR **#5** (the 18-module pure-domain port) is still
     open and DRAFT. Click "Ready for review", then "Squash & merge" →
     Confirm. (#9 merged 2026-07-09 19:02Z; #4 closed as redundant — verified
     at HEAD.) Or type in the mining session chat: "You may mark ready, arm
     auto-merge, and merge superbot-games PR #5."
   - WHERE: github.com/menno420/superbot-games/pull/5.
   - WHY owner-only: self-approval classifier blocks the lane from
     marking-ready/merging its own PR (verbatim denials in the mining retro).
   - UNBLOCKS: the mining port (18 modules, 62 tests) lands on main; the lane
     proceeds to workflow seam + host adapter with a clean base.
4. **PyPI trusted-publishing registration** — ~2 min.
   - WHAT: register a pending trusted publisher for the kit package.
   - WHERE: pypi.org → your account → Publishing → "Add a new pending publisher".
   - HOW: per-arm values (owner/repo/workflow/environment) as listed in the
     kit's publishing owner-action note (retro project-review ⚑ list).
   - WHY owner-only: PyPI account action; no agent credential.
   - UNBLOCKS: token-less automated kit releases.
5. **Archive the dead trading session.**
   - WHAT/WHERE/HOW: claude.ai session list → ⋮ on the dead trading session →
     **Archive**.
   - WHY owner-only: session management is claude.ai UI.
   - UNBLOCKS: clean wake-ups; no stale session competing for the lane.
6. **Ratify kit #26 (PL-011).**
   - WHAT: merge substrate-kit PR #26 — makes "adoption isn't done until
     ENGAGED" binding program law.
   - WHERE: github.com/menno420/substrate-kit/pull/26 (do-not-automerge by
     design; merge = ratification, comment on the thread to veto).
7. **kit #22 — PL-010 retro-ratify comment.**
   - WHAT: leave the one-line ratification comment on kit PR #22 per PL-010's
     retro-ratification path.
   - WHERE: github.com/menno420/substrate-kit/pull/22 thread.
8. **Merge kit #49.**
   - WHAT: merge the pin-path seed fix (make_seed `yield`-keyword bug).
   - WHERE: github.com/menno420/substrate-kit/pull/49 (do-not-automerge by
     design — pin-path integrity law: the lab never merges its own oracle change).
   - UNBLOCKS: bench **B1 run-3**.
9. **websites product questions.**
   - WHAT: domains · /submit Postgres · /admin OAuth+home · restyle
     keep/preserve · cutover · deploy hook · health URL.
   - WHERE: menno420/websites `docs/owner/OWNER-ACTIONS.md` (each with options +
     a recommended default).
   - WHY owner-only: product/intent calls.
   - UNBLOCKS: websites Q4/Q5 roadmap lanes.
10. **superbot-next grants.**
    - WHAT: confirm intents toggles done? · sacrificial Discord account ·
      capped API key for band 7 · flag-13 ruling.
    - WHERE: superbot-next `control/status.md` ⚑ + the testing ledger
      (`docs/status/testing-report-2026-07-09.md`).
    - UNBLOCKS: live-testing bands proceed without improvisation.
11. **Arm per-Project self-poll routines** — the highest-value click in the
    program.
    - WHAT: a routine per Project: "read control/inbox.md and act on new
      orders", hourly or daily.
    - WHERE: each claude.ai Project → routines/schedule UI.
    - WHY owner-only: routine creation has no agent API surface.
    - UNBLOCKS: the fleet runs on orders without manual wake-ups.
12. **Review + send the Anthropic email** — addendum findings 1–10 are complete;
    the pack is ready for your read + send.
13. **Run the external ChatGPT review campaign** — pack live (sb#1903;
    next#57/#78): paste per pack instructions, feed replies back to any session.
14. **Launch venture-lab — the gen-2 born-right pilot** (~10 min of clicks,
    in order; supersedes the old "pick the gen-2 pilot mission" ask — the
    blueprint finalized venture-lab as the pilot under decide-and-flag; veto
    = say so and the next candidate gets the same package).
    - WHAT: create the venture-lab lane end-to-end — repo, ruleset, Project,
      environment, wake routine. The founding Custom Instructions are
      finalized and paste-ready in `docs/prompts/venture-lab-draft.md`
      (§ "Founding instruction text").
    - WHERE/HOW (click-level, in this order):
      1. **Repo:** github.com/new → name `venture-lab`, private, tick "Add a
         README". Then Settings → General → Pull Requests: tick **"Allow
         auto-merge"** + **"Automatically delete head branches"**.
      2. **Ruleset:** Settings → Rules → Rulesets → "New branch ruleset" →
         name `main`, target the `main` branch, enable "Require a pull
         request before merging". Do NOT restrict push; do NOT require
         up-to-date branches. (Add the required status check
         `substrate-gate` only AFTER the lane's first CI PR has reported it
         — a required check that never reports jams auto-merge forever.)
      3. **Project:** claude.ai → New Project `venture-lab` → paste the
         Custom Instructions block from `docs/prompts/venture-lab-draft.md`
         **verbatim** → set the model (your pick; default: same tier as the
         current fleet coordinators).
      4. **Environment:** attach the **`python-lab`** archetype environment
         (queue item 1.2 — or create it now: paste
         `environments/archetype-python-lab.sh` as the setup script); no
         extra env vars at launch. Attach it to the Project.
      5. **Routine:** the Project's routines/schedule UI → **hourly** wake
         (gen2-blueprint §2a, Class A): "Read control/inbox.md at HEAD and
         run the standing ritual from your instructions." This is the
         highest-value click — the ping test measured 7/9 unwoken lanes
         never picking an order up.
      6. **Boot message:** "Boot: walking skeleton through the full merge
         path, then ORDER 001." (The manager will have ORDER 001 + the
         venture shortlist corpus queued in control/inbox.md; step 6 can
         also confirm the ruleset check reports on the skeleton PR.)
    - WHY owner-only: repo creation + settings, Project / environment /
      routine creation are GitHub-settings and claude.ai UI surfaces — no
      agent API for any of them (verified walls, docs/capabilities.md; R17:
      attempted-or-exact-wall evidence on file for environments/routines,
      repo-settings 403s in the kit retro).
    - UNBLOCKS: phase-2 — the first born-right lane, which is both a revenue
      probe and the live test of the gen-2 seed standard the whole next
      generation launches from.

15. **Paste the gen-1 wind-down prompt into each gen-1 Project** — the
    fleet-wide gen-1 → gen-2 refresh (one identical paste ×9 chats).
    - WHAT: send ONE universal wind-down message to every gen-1 Project's
      chat, so each lane finishes/parks its open work and commits its own
      succession package (retro, next-boot doc, proposed Custom Instructions,
      tested environment spec, gen-2 feedback, "wind-down complete" status
      marker) in its own repo — the raw material for each lane's fresh gen-2
      relaunch.
    - WHERE: each gen-1 claude.ai Project — superbot-next, substrate-kit,
      websites, trading-strategy, codetool-lab-fable5, codetool-lab-opus4.8,
      codetool-lab-sonnet5, superbot-games (mining), superbot-games
      (exploration).
    - HOW: open
      https://raw.githubusercontent.com/menno420/fleet-manager/main/docs/prompts/gen1-winddown-universal.md
      → copy everything inside the code fence (from "WIND-DOWN:" to "…keep
      going.") → paste it as ONE message into each Project's chat. Same text
      everywhere — each lane adapts it to its own repo.
    - WHY owner-only: sending a message into a Project's chat is a claude.ai
      UI action; agents have no surface to message other Projects' sessions
      (same verified wall class as environments/routines,
      `docs/capabilities.md`).
    - UNBLOCKS: per-lane succession packages on each repo's main; the manager
      tracks completion via each lane's `control/status.md` "wind-down
      complete" marker, then queues the per-lane gen-2 relaunch clicks (fresh
      Project + new instructions + new environment per blueprint §3).

16. **Run the merge session — one doc, all clicks.**
    - WHAT: work through [`merge-queue-2026-07-09.md`](merge-queue-2026-07-09.md)
      top to bottom — every open PR in the fleet, each re-verified at live
      HEAD (2026-07-09 22:41Z) with a pre-chewed disposition and any
      pre-merge step. 4 one-click merges, 1 needs a conflict fix first
      (superbot-next #95 — the doc has the exact message to send that lane),
      1 waits on another.
    - WHERE: the PR links are in the doc; work in its row order.
    - WHY owner-only: the still-open PRs are gen-1 owner-gated carve-outs
      (kit pin-path/program-law ratification, mining's explicit owner gate)
      — merge = your ratification.
    - UNBLOCKS: kit bench B1 run-3, the mining port + wind-down landing,
      superbot-next band-5 fixes.
    - NOTE: this absorbs the *clicking* half of items 3 (mining #5), 6
      (kit #26), and 8 (kit #49) — the doc is the current source of truth on
      their live state; those items stay listed for their context only.

17. **Launch game-lab — the two-track GBA venture you decided tonight**
    (~10 min of clicks, in order; decision 2026-07-09 night, both tracks;
    toolchain fully proven in-container the same night —
    [`findings/gba-toolchain-proof-2026-07-09.md`](findings/gba-toolchain-proof-2026-07-09.md)).
    - WHAT: create the game-lab lane end-to-end — TWO repos (one private,
      one public), ONE Project, the gba-lab environment, an hourly wake
      routine. The founding Custom Instructions are finalized and
      paste-ready in
      [`prompts/game-lab-founding.md`](prompts/game-lab-founding.md).
    - WHERE/HOW (click-level, in this order):
      1. **Repo 1 (public):** github.com/new → name `gba-homebrew`,
         **public**, tick "Add a README". Then Settings → General → Pull
         Requests: tick **"Allow auto-merge"** + **"Automatically delete
         head branches"**.
      2. **Repo 2 (PRIVATE):** github.com/new → name `pokemon-mod-lab`,
         **private** (this one holds Nintendo-copyrighted decomp material —
         it must NEVER be public), leave it **empty apart from the README**
         (agents mirror pret/pokeemerald in themselves). Same Settings →
         General → Pull Requests ticks: **"Allow auto-merge"** +
         **"Automatically delete head branches"**.
      3. **Project:** claude.ai → New Project `game-lab` → paste the Custom
         Instructions block from `docs/prompts/game-lab-founding.md`
         **verbatim** → set the model (your pick; default: same tier as the
         current fleet coordinators) → add BOTH repos to the Project.
      4. **Environment:** claude.ai/code → Environments → New environment →
         name `gba-lab` → add repos `menno420/gba-homebrew` +
         `menno420/pokemon-mod-lab` → Setup script: paste the full contents
         of `environments/archetype-gba-lab.sh` → env vars: **none**.
         Attach it to the game-lab Project.
      5. **Routine:** the Project's routines/schedule UI → **hourly** wake
         (gen2-blueprint §2a, Class A — new lane at launch): "Read
         control/inbox.md at HEAD and run the standing ritual from your
         instructions."
      6. **Boot message:** "Boot: walking skeleton on both tracks (build +
         headless screenshot through the full merge path), then ORDER 001."
         (The manager queues ORDER 001 — scout-loop reproduction + 3 mod
         concepts / 3 game concepts with scope estimates — in each repo's
         control/inbox.md at seed.)
    - WHY owner-only: repo creation + settings, Project / environment /
      routine creation are GitHub-settings and claude.ai UI surfaces — no
      agent API for any of them (verified walls, `docs/capabilities.md`;
      same wall class R17-evidenced on the venture-lab item above).
    - UNBLOCKS: the second gen-2 born-right lane; the first *playable*
      fleet artifact (a modded Emerald in your hands + an original homebrew
      ROM that is publish-safe); live reuse of the scout session's proven
      toolchain before it goes stale.

## Parked (valid, no rush)

- **codetool-lab-opus4.8 v0.1.0 tag + Release** — tag-push is walled (403);
  owner click at github.com/menno420/codetool-lab-opus4.8 → Releases → Draft.
- **Paper-doll PNG pack for mining** — art asset, whenever.
- **SuperBot 2.0 test-guild hand-verification** — folds into item 10's band flow
  when the bands reach owner-eyes demos.

## Resolved since last rewrite

- **D&D bounded-authority sign-off** — adopted under decide-and-flag
  (superbot-games #8, D-0007); vetoable until the P3→P4 ship gate, no click owed.
