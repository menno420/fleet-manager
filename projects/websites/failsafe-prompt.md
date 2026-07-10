# websites — wake cron text (Q-0265)

> Part 4 of the websites Project package. **Routine name (deployed):** the
> ORDER 008 self-armed lane wake · **trigger:** `trig_017H9Qb9oxtLgUy6sw2gnSHg`
> · **cadence (deployed):** `0 */4 * * *` · **fresh-session-per-fire** (no
> persistent coordinator seat — websites is the fleet's fresh-session lane, so
> there is no separate failsafe: the cron IS the lane's pacemaker, and the
> in-session ~15-min send_later chain, when the fired toolset has it, is a
> within-wake accelerator only; see coordinator-prompt.md caveat).
>
> **Deployed-state (2026-07-10) — prompt text UNVERIFIED:** the trigger was
> created 2026-07-10T13:49:36Z with the OLD v1-era delegating prompt — recorded
> only as paraphrase, "prompt = the standing inbox ritual" (websites
> `docs/owner/OWNER-ACTIONS.md` row E @ `fc8354e`; first fire confirmed
> 2026-07-10T16:01:32Z via `list_triggers`). The verbatim deployed text is NOT
> committed anywhere (inventory-lanes §1 "Missing (a)"). The repo's
> `docs/project/routine-prompt.md` v2 (Q-0265 continuous) is marked "the one
> to paste" — the owner MAY have re-pasted it into the Routines screen since,
> but no paste record exists, so treat the deployed prompt as **v1-era until a
> fired session's behavior proves otherwise** (a wake that works the loop and
> mentions Q-0265/send_later is running v2; a wake that ships exactly one
> bounded slice off "the standing inbox ritual" is still v1).
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
