<!-- v1 · 2026-07-10 · fleet-manager projects registry -->
# Product Forge — failsafe cron text (part 4 of 4)

> Routine name: **`product-forge failsafe wake`** · cron: **`0 */2 * * *`** (even hours
> :00 — the manager reads at :30; fleet stagger per gen3-deployment-standard §2).
>
> **Deployment state — two conflicting records, repo wins:**
> - Dispatch premise (this build order + part4-brief §2 item 0): seat booted ~19:05Z
>   **pre-Q-0265-merge** → marked **NOT-YET-ARMED-BY-SEAT**; the live chat still owed the
>   §2b continuous-mode amendment paste (part-4 brief item 0).
> - **Repo ground truth (newer)**: `control/status.md` @ product-forge origin/main
>   `7f05aa8` (updated 2026-07-10T20:41Z) records **"Continuous mode (Q-0265): Active.
>   Chain alive (~15-min send_later continuation ticks) + failsafe cron
>   `trig_012EvztCrHHg7s4mBsKT3VKs` 'product-forge failsafe wake' (`0 */2 * * *`),
>   enabled."** — i.e. the seat cut over and ARMED the failsafe after the dispatch
>   snapshot. Text-equality caveat RESOLVED 2026-07-10 ~22:05Z (gap-closure pass,
>   `list_triggers`): the armed trigger's stored prompt is **NOT** the canonical block
>   below — it is the generic §2b failsafe template, VERBATIM-FROM-REGISTRY (263 chars,
>   single line as stored):
>
>   ```
>   FAILSAFE WAKE (product-forge, Q-0265): if your send_later continuation chain is alive, verify that in one line and end. If it stalled, resume the work loop (sync HEAD → inbox → slice after slice, each merged-on-green) and re-arm the chain (~15 min) before ending.
>   ```
>
>   The mismatch is functional-benign (chain-alive check + resume + re-arm are all
>   present) but the seat-specific rails (product ORDER ladder, money-step brake) exist
>   only in the canonical block below — re-arm with the canonical text at the seat's
>   next cutover to close the gap.
>
> Source of the exact text: superbot
> `docs/planning/round3-founding-package-product-forge-2026-07-10.md` §2 step 5
> @ superbot origin/main `dc19b1e` (the natively-continuous rewrite). Quoted verbatim:

```
FAILSAFE WAKE (product forge, Q-0265 continuous mode): if your send_later
continuation chain is alive (a pending continuation exists), verify that in
one line and end. If it stalled, RESUME THE WORK LOOP: sync
menno420/product-forge to origin/main HEAD; read control/inbox.md at HEAD;
advance the current product ORDER (scaffold → core → tests → README →
artifact) slice after slice, each merged-on-green; if the inbox is empty,
polish the newest product's roughest edge and flag 'inbox empty' to the
manager. Money steps are never executed — they become conservative owner
plans (Q-0259 r.4). Re-arm the continuation chain (~15 min) before ending
the turn; overwrite control/status.md as each turn's last step. If this
trigger is one-shot rather than recurring, re-arm it for +120 minutes.
```

Arming recipe (founding package §2 step 5): `create_trigger` with name
`"product-forge failsafe wake"`, cron `"0 */2 * * *"`, firing into the coordinator's
persistent session, prompt EXACTLY as above → verify via `list_triggers` (never wait for
the first fire as proof — runs aren't inspectable owner-side; the registry is) → record
the exact call + outcome verbatim in `control/status.md`. If the call is walled: record
the verbatim denial in status and hand the owner this block (name + cadence + prompt)
for manual creation in the claude.ai Routines screen.
