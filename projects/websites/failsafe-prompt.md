<!-- v1 · 2026-07-10 · fleet-manager projects registry -->
# websites — wake cron text (Q-0265)

> Part 4 of the websites Project package. **Routine name (deployed):** the
> ORDER 008 self-armed lane wake · **trigger:** `trig_017H9Qb9oxtLgUy6sw2gnSHg`
> · **cadence (deployed):** `0 */4 * * *` · **fresh-session-per-fire** (no
> persistent coordinator seat — websites is the fleet's fresh-session lane, so
> there is no separate failsafe: the cron IS the lane's pacemaker, and the
> in-session ~15-min send_later chain, when the fired toolset has it, is a
> within-wake accelerator only; see coordinator-prompt.md caveat).
>
> **Deployed-state (2026-07-10) — prompt text now VERIFIED (gap-closure pass,
> `list_triggers` ~22:05Z): the deployed prompt IS the v1-era ORDER 008 text**,
> full trigger name `websites lane wake — 4-hourly inbox ritual (ORDER 008)`,
> created 2026-07-10T13:49:36Z, `create_new_session_on_fire` (no session
> binding). VERBATIM-FROM-REGISTRY, byte-exact, single line as stored (576
> chars):
>
> ```
> websites lane wake (fleet ORDER 008). In /home/user/websites: git fetch origin main and land on origin/main HEAD, then read control/inbox.md at HEAD and run the standing per-session ritual from your instructions (control/README.md: execute any `status: new` order not already in your own control/status.md done= line, claim-first; then overwrite control/status.md as the deliberate last step). Honor the repo's .claude/CLAUDE.md working agreement and docs/CAPABILITIES.md walls; forward-only git; never edit control/inbox.md; never pass ambient RAILWAY_* env vars to anything.
> ```
>
> This closes inventory-lanes §1 "Missing (a)" (the text is now committed) and
> settles the v1-vs-v2 question: **v2 is NOT deployed** — the owner re-paste
> (paste-wave item 4) is still owed. Note the 20:00Z fire's 3 landed slices
> happened under this v1 text — behavior alone was a misleading v2 signal.
>
> **This package prescribes:**
> - **Prompt:** the v2 text — identical to the fenced block in this package's
>   `coordinator-prompt.md` (for a fresh-session lane the wake prompt and the
>   seat prompt are the same text; source: websites
>   `docs/project/routine-prompt.md` v2 @ `fc8354e`, verbatim).
> - **Cadence:** `0 */2 * * *` **recommended** per the gen-3 standard's lane
>   stagger (lanes `0 */2`, manager `30 */2`; superbot
>   `docs/planning/gen3-deployment-standard-2026-07-10.md` §2 @ `53fb5ef`).
>   This is a RECOMMENDATION, not a defect flag: the deployed 4-hourly cadence
>   is not wrong — websites is a maintenance-shaped lane and the gen-2
>   blueprint's §2a maintenance-cadence doctrine explicitly survives Q-0265
>   for bounded lanes (fm `docs/gen2-blueprint.md` amendment banner). Under
>   the v2 continuous prompt, each fire works until backpressure regardless
>   of cadence; 2-hourly just halves the dead time between fires.
>
> **Re-arm recipe** (a fired session with `create_trigger`/`update_trigger`
> can do this itself; else owner edits the Routines screen): `update_trigger`
> the existing `trig_017H9Qb9oxtLgUy6sw2gnSHg` prompt is NOT supported by the
> tool (name/cron/enabled only) → `delete_trigger` old → `create_trigger`
> name `websites lane wake`, cron `0 */2 * * *` (or keep `0 */4`),
> `create_new_session_on_fire: true`, prompt = the block below → verify via
> `list_triggers` (the registry is the proof — never wait for the first fire)
> → record the delete+create verbatim in `control/status.md` +
> `docs/owner/OWNER-ACTIONS.md` row E.

## The prompt (create_trigger `prompt` field, verbatim — same as part 2)

```
WAKE (websites lane, continuous mode — Q-0265): sync menno420/websites to origin/main HEAD and read control/inbox.md at HEAD. Then WORK IN A LOOP up the ladder (docs/project/project-instructions.md § Never idle): open ORDER → queue-state NEXT → docs/ideas/backlog.md (promote the best idea and build its first increment) → ⚑ Self-initiated improvement → honest "backlog dry" upkeep. Each slice is its own branch + born-red card + PR ready + squash-merge on green `quality`; when a slice lands and useful work remains, take the NEXT slice in the same session — the throttle is removed, not the ceremony. Before ending the turn: if useful work remains and your toolset has send_later, arm it ~15 minutes out ("continue the websites work loop") and say so on the card; if the tool is absent, record that verbatim — this cron is then your pacemaker. Truth rules unchanged: trust the setup-script probe; never record "pushed" without git ls-remote proof; a patch to the owner is the last resort and needs the verbatim probe error. Substantial or sim-worthy ideas don't terminate locally: file them in docs/ideas/ (the Idea Engine harvests by link) and flag sim-worthy questions to the manager in your heartbeat (Q-0264). Session enders: one genuine new idea (dedup first; none beats filler), one-line previous-wake review, family-level 📊 Model line. Overwrite control/status.md as the deliberate last step. Backpressure, not the clock, is the brake; free-window posture through 2026-07-14 is MORE work, not less (Q-0265).
```
