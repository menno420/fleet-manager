<!-- v1 · 2026-07-10 · fleet-manager projects registry -->
# substrate-kit — failsafe cron text (Q-0265)

> Part 4 of the substrate-kit Project package. **Routine name:**
> `substrate-kit failsafe wake` · **cadence:** `0 */2 * * *` (even hours :00 —
> the core-seat stagger: lanes `0 */2`, manager `30 */2`; gen-3 deployment
> standard §2) · fires into the persistent coordinator session.
>
> **Deployed-state note (2026-07-10):** the trigger currently live in the
> registry is `trig_016EfUawz6KxEYqUM6f1BqDw` **"substrate-kit 2-hourly
> standing wake"**, cron `0 */2 * * *`, created 2026-07-10T15:53:36Z, bound to
> coordinator session `session_01YMJrUDpcarFsqPZ2BeeiVB` (kit
> `control/status.md` § ROUTINE STATE @ `7e600c6`). That is the OLD pre-Q-0265
> standing-wake wording — its **actual stored prompt is committed verbatim
> below** (§ "Deployed prompt", VERBATIM-FROM-REGISTRY, extracted via
> `list_triggers` 2026-07-10 ~22:05Z by the gap-closure pass; it confirms the
> earlier reconstruction: the founding package §2 step-3 "ONE bounded pass"
> text, superbot
> `docs/planning/round3-founding-package-substrate-kit-2026-07-10.md`).
> **The § "Replacement prompt" block is the text for the seat's next
> self-re-arm** per the part-4 brief §2b recipe: `delete_trigger` the old
> standing wake → `create_trigger` with the name/cron/prompt below → verify
> both via `list_triggers` (the registry is the proof — never wait for the
> first fire) → record the delete+create calls verbatim in
> `control/status.md`.
>
> Template provenance: part-4 brief §2b failsafe template (superbot
> `docs/planning/round3-dispatch-part4-brief-2026-07-10.md`), adapted for the
> kit seat.

## Deployed prompt — VERBATIM-FROM-REGISTRY (extracted 2026-07-10 ~22:05Z via `list_triggers`)

The stored `prompt` field of live trigger `trig_016EfUawz6KxEYqUM6f1BqDw`,
byte-exact, single line as stored (655 chars):

```
2-HOURLY WAKE (substrate-kit): sync menno420/substrate-kit to origin/main HEAD; read control/inbox.md at HEAD; then ONE bounded pass — exactly one of: advance one §6 centralization item | run one distribution wave for a pending kit release | one kit development/bench slice. Lane-repo writes are DISTRIBUTION ONLY (Q-0261.3) — never lane domain work, never their control/ files. Ship merged-on-green per the target repo's conventions; decide-and-flag; no excessive work — one real slice per wake. Overwrite control/status.md as the deliberate last step. If this trigger is one-shot rather than recurring, re-arm it for +120 minutes before ending the turn.
```

## Replacement prompt (create_trigger `prompt` field for the next self-re-arm, verbatim)

```
FAILSAFE WAKE (substrate-kit, Q-0265): if your send_later continuation chain
is alive, verify that in one line and end. If it stalled, resume the work
loop (sync menno420/substrate-kit to origin/main HEAD → control/inbox.md at
HEAD → slice after slice, each its own merged-on-green PR — kit development,
release, and distribution per your standing brief; lane-repo writes are KIT
DISTRIBUTION ONLY, Q-0261.3) and re-arm the chain (~15 min) before ending.
Overwrite control/status.md as the deliberate last step.
```

## create_trigger args (recipe)

- `name`: `substrate-kit failsafe wake`
- `cron_expression`: `0 */2 * * *`
- target: this (persistent coordinator) session — default self-bind; do NOT
  set `create_new_session_on_fire`
- `prompt`: the fenced block above, verbatim
