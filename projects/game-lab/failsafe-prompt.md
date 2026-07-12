<!-- v1 · 2026-07-11 · fleet-manager projects registry -->
# Game Lab — failsafe cron text (Q-0265)

> Part 4 of the Game Lab Project package. **Routine name:**
> `game-lab failsafe wake` · **cadence:** `50 */2 * * *` (even hours :50 —
> inherits the retired superbot-retro slot in the gen-3 lane stagger; manager
> reads at :30) · fires into the persistent coordinator session (default
> self-bind). **Provenance:** v1 · 2026-07-11, owner restructure directive
> 2026-07-11 — replaces the slice-1 v0 placeholder; authored from the retired
> superbot-retro seat's failsafe + child-wake pattern (packages @ `1dea86d`).
> Per registry doctrine the trigger prompt block below is deliberately NOT
> version-stamped in-band (byte-checkable against `list_triggers`).
>
> **Deployed state (2026-07-11): NOT ARMED for this seat.** The retired
> superbot-retro seat's triggers are still armed against these repos (last
> committed registry state — re-verify via `list_triggers` before acting):
> - retro failsafe: `trig_01Y99uDKNtKTz2EtRYPWZkGY` (`50 */2 * * *`)
> - gba hourly child wake: `trig_0137SkvhXEJvwepX8aVNkcSn` (`0 * * * *`)
> - pokemon hourly child wake: `trig_01BTJjkMVMKtWPjuYe7643Hi` (`30 * * * *`)
>
> **Cutover recipe (rides the merged seat's boot — coordinator-prompt.md
> BOOT step 2, rebind-then-delete):** create THIS trigger first, verify via
> `list_triggers` (the registry is the proof — never wait for the first
> fire), THEN delete all three old triggers and verify them absent — the
> merged seat replaces the retro parent+children pattern with one seat + one
> failsafe. Record every call + outcome verbatim in the gba-homebrew
> heartbeat. If the seat's surface walls the calls: record the verbatim
> denial and hand the owner this block (name + cadence + prompt) via the
> owner-queue.

## The prompt (create_trigger `prompt` field, verbatim)

```
FAILSAFE WAKE (game-lab, Q-0265): if your send_later continuation chain is
alive, verify that in one line and end. If it stalled, resume the work
loop: sync menno420/gba-homebrew + pokemon-mod-lab to origin/main HEAD →
read each control/inbox.md at HEAD → run the R22 visibility check (pokemon
public → STOP, flag) → slice after slice, each its own PR (strict track
isolation: nothing from the private Track A ever reaches a public surface;
headless in-game proof before "done"; no SuperBot repos, ever) — and
re-arm the chain (~15 min) before ending. Overwrite gba-homebrew
control/status.md as the deliberate last step.
```

## create_trigger args (recipe)

- `name`: `game-lab failsafe wake`
- `cron_expression`: `50 */2 * * *`
- target: this (persistent coordinator) session — default self-bind; do NOT
  set `create_new_session_on_fire`
- `prompt`: the fenced block above, verbatim
- After creating: verify via `list_triggers`, then retire the three
  superbot-retro triggers (delete + verify absent) and record all calls
  verbatim in the heartbeat.
