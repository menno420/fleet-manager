# Owner queue

> **Status:** `living-ledger` — the ONE deduplicated queue of things waiting on the owner.
> The manager adds/removes items; asks stay valid until acted on (playbook R11).
> Every item below must carry WHAT/WHERE/HOW/WHY/UNBLOCKS + proof it's owner-only (R17).

Rewritten 2026-07-09 from the retro synthesis (deduplicated). Fast wins first-ish.

## Active queue

1. **Paste the env setup scripts (trading + kit)** — ~2 min each.
   - WHAT: create claude.ai environments for trading-strategy and substrate-kit.
   - WHERE: **claude.ai/code → Environments → New environment**, then attach to
     the Project.
   - HOW: paste the setup script into the Setup-script field —
     `environments/templates/setup-universal.sh` is the proven default shim;
     trading's and kit's exact scripts are in the retro-synthesis pack
     (menno420/superbot `docs/eap/`) until their per-repo specs are filed here.
     Variable NAMES per `environments/templates/env-vars.md` (values only in the
     claude.ai panel — never in the repo).
   - WHY owner-only: agents cannot create/edit environments (verified wall).
   - UNBLOCKS: dependency-green boots in both Projects.
2. **kit P10 required-check swap.**
   - WHAT: swap substrate-kit main's required status check — remove the stale
     context, require the current gate.
   - WHERE: github.com/menno420/substrate-kit → Settings → Branches/Rulesets →
     main → required status checks.
   - HOW: exact contexts to remove/add are listed in the kit's retro
     project-review ⚑ owner-actions (`docs/retro/project-review-2026-07-09.md`).
   - WHY owner-only: branch-protection edits 403 at the agent credential layer.
   - UNBLOCKS: kit PRs stop waiting on a check that never reports.
3. **Mining merge authorization — ONE sentence.**
   - WHAT: type in the mining session chat: "You may mark ready, arm auto-merge,
     and merge superbot-games PRs #9 and #5." (Or click yourself: merge **#9**,
     then mark **#5** ready and merge; #4 is already closed as redundant.)
   - WHERE: the mining Project session (or github.com/menno420/superbot-games
     PRs #9, #5).
   - WHY owner-only: self-approval classifier blocks the lane from merging its
     own PRs; one sentence collapses the 3 clicks.
   - UNBLOCKS: mining retro + the 18-module pure-domain port land on main.
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
14. **Pick the gen-2 pilot mission** — the retro synthesis is in; blueprint
    starts on your pick.

## Parked (valid, no rush)

- **codetool-lab-opus4.8 v0.1.0 tag + Release** — tag-push is walled (403);
  owner click at github.com/menno420/codetool-lab-opus4.8 → Releases → Draft.
- **Paper-doll PNG pack for mining** — art asset, whenever.
- **SuperBot 2.0 test-guild hand-verification** — folds into item 10's band flow
  when the bands reach owner-eyes demos.

## Resolved since last rewrite

- **D&D bounded-authority sign-off** — adopted under decide-and-flag
  (superbot-games #8, D-0007); vetoable until the P3→P4 ship gate, no click owed.
