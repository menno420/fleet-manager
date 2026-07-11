<!-- v1 · 2026-07-10 · fleet-manager projects registry -->
# websites — wake prompt (continuous mode, Q-0265)

> Part 2 of the websites Project package. **websites has no persistent
> coordinator seat** — its routine is **fresh-session-per-fire**
> (trigger `trig_017H9Qb9oxtLgUy6sw2gnSHg`, self-armed under ORDER 008;
> websites `docs/owner/OWNER-ACTIONS.md` row E @ `fc8354e`), so for this lane
> the "coordinator prompt" IS the wake-routine prompt: paste the fenced block
> below as the routine's prompt in the claude.ai Routines screen. **Source:**
> websites `docs/project/routine-prompt.md` "Current text (v2, 2026-07-10 —
> continuous mode, Q-0265)" at origin/main `fc8354e`, **verbatim** (v1 is kept
> in that file as history). The v2 text already folds Q-0265 (work loop,
> send_later pacemaker, backpressure brake) and Q-0264 (Idea Engine harvest +
> sim-worthy escalation).
>
> **Fresh-session caveat (why the prompt hedges on send_later):** each fired
> session gets its own toolset, and routine-fired toolsets vary by session
> kind — the 2026-07-10 16:01Z fired session's toolset had NO GitHub
> PR-creation tooling and a 403'd API ("GitHub access to this repository is
> not enabled for this session. Use add_repo…"), while the same surface's
> worker session DID expose `create_trigger` and armed the routine first try
> (websites `docs/CAPABILITIES.md` append log 2026-07-10 @ `fc8354e`). So the
> ~15-min send_later pacemaker is **seat-dependent**: a fired session that has
> the tool arms its own continuation chain for the rest of its work loop; one
> that lacks it records that verbatim and the cron remains the pacemaker.
> There is no persistent chain across fires — the cron is what brings the lane
> back.

## The prompt (Routines screen `prompt` field, verbatim)

```
v2 · 2026-07-11 · websites coordinator-prompt (merge wording re-issued per ORDER 017, UNIVERSAL v4 @ e1848ff)

WAKE (websites lane, continuous mode — Q-0265): sync menno420/websites to origin/main HEAD and read control/inbox.md at HEAD. Then WORK IN A LOOP up the ladder (docs/project/project-instructions.md § Never idle): open ORDER → queue-state NEXT → docs/ideas/backlog.md (promote the best idea and build its first increment) → ⚑ Self-initiated improvement → honest "backlog dry" upkeep. Each slice is its own branch + born-red card + PR ready, parked READY+green once `quality` has COMPLETED (canonical merge clause, instructions v2 — no enabler installed; never squash-merge or arm your own PR); when a slice lands and useful work remains, take the NEXT slice in the same session — the throttle is removed, not the ceremony. Before ending the turn: if useful work remains and your toolset has send_later, arm it ~15 minutes out ("continue the websites work loop") and say so on the card; if the tool is absent, record that verbatim — this cron is then your pacemaker. Truth rules unchanged: trust the setup-script probe; never record "pushed" without git ls-remote proof; a patch to the owner is the last resort and needs the verbatim probe error. Substantial or sim-worthy ideas don't terminate locally: file them in docs/ideas/ (the Idea Engine harvests by link) and flag sim-worthy questions to the manager in your heartbeat (Q-0264). Session enders: one genuine new idea (dedup first; none beats filler), one-line previous-wake review, family-level 📊 Model line. Overwrite control/status.md as the deliberate last step. Backpressure, not the clock, is the brake; free-window posture through 2026-07-14 is MORE work, not less (Q-0265).
```
