# superbot-next — the entry point

> **Status:** `living-ledger` · true as of **2026-08-21**
>
> **What this is:** fleet-manager's entry point for `menno420/superbot-next` —
> where the last session left off and where the next one should look.
> **Canonical for nothing.** The repo's own `docs/current-state.md` wins on its
> state, `docs/PROJECT-CLOSEOUT.md` on the handover, `docs/AGENT_ORIENTATION.md`
> on the binding contracts, and the live tree wins over all of them. Depth
> files are **not yet written** — created by the 2026-08-21 fleet review
> (the Tier-1 pair row was "cleared to build" since 2026-08-08) and carries
> only the entry point so far.
>
> Certainty tags per
> [`../../findings/2026-08-05-foundation-continuation.md`](../../findings/2026-08-05-foundation-continuation.md).

## The one-paragraph answer

`superbot-next` is the **ground-up rebuild** of the production Discord bot
("SuperBot 2.0"): Python 3.11, layered plugin architecture, 49 subsystems +
kernel, 3,660 tests, validated against the frozen `superbot` as behavioral
oracle — **golden parity full-corpus green, 533/533**. It closed
complete-parked with the program on 2026-07-21; the only activity since is the
kit lane (#602 → v1.20.1, 2026-08-05; #606 → v1.21.0, 2026-08-13, the last
push). `MEASURED` 2026-08-21: **0 open PRs** — the closeout's two carried PRs
are both resolved (**#602 MERGED 2026-08-05, #576 closed 2026-07-21**; a
record still citing the "#602 owner hold" is describing July).

**The one caveat that governs everything here:** *golden-parity green must not
be read as "ported".* The 2026-08-05 owner-live audit
([`../../findings/2026-08-05-superbot-next-live-audit.md`](../../findings/2026-08-05-superbot-next-live-audit.md))
found **capture-world literals** — values the old bot computed shipping as
constants transcribed from the capture corpus — and the help navigation graph
unported (60 of 66 help panels button-less), alongside real strengths (1,327
dispatch targets, real handlers, real DB writes — "not a shell").

## Threads

### Thread: the headless boot — **gap 1 closed in part; three runtime defects on record, at the pin `d5f66dc2`** (2026-09-04, later the same day)

The rebuild package's verdict said every dynamic claim in it was read from
source because neither bot had been booted. fm #1040 booted this repo at the
pin — the composition root end to end against a throwaway local Postgres, the
gateway connect stubbed, Discord's HTTP faked in-process — and drove `/help`,
the setup flow, the join launcher and all 27 slash commands through the real
spine and the **production** presenter, clicking every rendered control.
Record: [`planning/2026-09-04-superbot-rebuild/run/boot-observation.md`](../../planning/2026-09-04-superbot-rebuild/run/boot-observation.md);
instrument: `run/headless_drive.py` beside it. What a session working this
repo needs from it (`MEASURED` at the pin, headless — no Discord surface
observed):

- **The primary setup entry never posts its card.** `/setup`, the launcher's
  *Start Setup*, `/setup-advanced` and `/setup-status` render into the
  workspace through `service.post_panel_to_channel`, whose request has no
  interaction origin; `DiscordPanelPresenter` has no channel-send branch for
  that shape (the parity `ParityPresenter` does — `record_send`), so the
  render is dropped and the reply links to message id `0`. The 13-panel
  essential flow is unreachable through the shipped adapter.
- **Two unhandled `AttributeError`s:** `sb/domain/ticket/setup_panel.py:159`
  and `:191` read `result.ok` off a `WorkflowResult` that has no such field
  (the *Enable tickets* / *Auto-create log channel* buttons answer *"Something
  went wrong on our end"*); `sb/domain/platform/guild_snapshot.py:243` reads
  `.name` off a `ResourceRequirement` (every setup recommender read logs the
  exception and falls back).
- **A guild owner locks themself out with one click** on the Command Access
  panel — a mode or a per-channel role-set — because `owner_override_holds`
  is the platform owner's, not the guild owner's; the reply tells them to
  fix it in `!settings`, which is prefix-only and dead without the message
  intent. Three of the ten setup commands (`setup-describe`, `setup-skip`,
  `setup-unskip`) cannot work on the slash surface at all: commands register
  parameterless.
- **The help tree is navigable and leads nowhere:** 57 of 66 help panels
  from `/help`, depth up to 5, 48 of them with nothing but a Back button, and
  not one click out of the help tree.

Next step in this repo: **none** — it stays parked and read-only. The
findings belong to the successor plan (gap 1's residue is the gateway leg,
`OQ-SUPERBOT-NEXT-GATEWAY-LEG` in `docs/owner-queue.md`). If the owner ever
wants these fixed *here*, the four bullets above are the ticket.

### Thread: the rebuild review — **its failure is now diagnosed, at the pin `d5f66dc2`** (2026-09-04)

The 2026-09-04 comparative review
([`docs/planning/2026-09-04-superbot-rebuild/`](../../planning/2026-09-04-superbot-rebuild/00-README.md))
treated this repo's outcome as its primary research subject. **Read
[`04-root-cause.md`](../../planning/2026-09-04-superbot-rebuild/04-root-cause.md)
before forming any view about why 533/533 parity shipped nothing.** Four
findings change what the entry point above says, each measured at this pin:

- **The 533 goldens do not test the shipping bot.** Every "actual" wire byte
  comes from `rendered_panel_payload()` in `sb/adapters/parity/transport.py`, a
  serializer used by nothing but the parity adapter; production installs
  `DiscordPanelPresenter` (`sb/app/panel_host.py:66`), which **no CI job
  exercises** — the required gate installs only `pytest pyyaml`, so its four
  tests skip.
- **This composition root publishes no slash-command set.**
  `sb/app/main.py:616` hardcodes `sync_remote(bot, committed, enabled=False)`,
  and the only other sync leg is gated on `SB_DATA_PLANE=test`. Whether the
  audit's *"27 slash commands survive"* still holds from an earlier registration
  is **unmeasured** — but the repo's own justification for degrading rather than
  refusing to boot rests on that survivor set, and this root never creates it.
- **The clean layer DAG is a measurement artifact.** 296 cross-subsystem
  `sb.domain` imports, **268 of them (90.5 %) inside function bodies**, where
  all 8 mutual subsystem pairs live and where the module-level census never
  looked.
- **Its real donation is not the panel/manifest/parity layer.** It is authority,
  audit, send-egress and member-data erasure as **required fields and
  registry-derived walks** — the half a successor would be foolish to
  re-derive.

Next step: none in this repo. It stays parked and read-only; the review
changed nothing here.

### Thread: game-community successor direction — **resolved for planning** (2026-08-21)

The owner's current request resolves the former two-plan fork in favor of a
server-first, game-testing/community bot with substantially stronger AI. The
[authoritative pre-repository plan](../../planning/2026-08-21-game-community-bot/README.md)
chooses a **clean multi-game repository**, not a cut-down or deployed
`superbot-next`: this repo donates its layered kernel, registries, workflow,
audit, provider-neutral AI, and scope-narrowing patterns; live `superbot`
donates proven behavior and operator UX. The 49-subsystem/golden-parity target,
BTD6 tools, and captured-state panels are explicitly rejected.

This is planning truth, not a modification order for this parked repo. Next
step is plan GCB-1/Phase 0: owner confirms the new repository name, then the plan
moves there and implementation starts from a minimal substrate. `superbot-next`
remains untouched and never becomes a test deployment merely because it is the
architecture donor.

## Before you attach / modify — the traps, measured

- **Seven required checks on `main`**: code-quality · manifest-validate ·
  architecture · sim-gate · golden-parity (gate job) · check_compat_frozen ·
  pip-audit. `substrate-gate` is **NOT required here and reds** on a
  pre-existing break (`test_parse_message_shapes` under CPython 3.14.6) — so
  the born-red card holds nothing closed, and the regen "fix" was
  Codex-refuted 7/7 and reverted (program §7 rows, 2026-08-13). Do not "fix"
  it by suppression.
- **The closeout's "permanently read-only on 2026-07-22" is false at face
  value** — it meant the EAP *Project*; the repo merged PRs in August.
- **`control/` cannot be naively deleted**: the gate workflow reads
  `control/status.md` + `control/claims`; removal is the owner-sequenced D6
  plan.
- **Auto-merge enabler arms at PR open AND synchronize** — same trap as
  superbot's, wider trigger set.
- Config-accessor seam is machine-enforced (no `os.getenv` outside
  `sb/kernel/config/**`, plus one ledgered parity-boot exception — sb
  D-0028); the plugin lockfile pins `superbot-idle-plugin` and
  `superbot-plugin-hello` by manifest hash — a plugin-side manifest edit is a
  two-repo change.
- Kit v1.21.0, full config. Verify: the closeout's canonical pytest run
  (its § 2 — the bare `python3 -m pytest` does NOT exclude `examples/` by
  itself) + the seven checks; deploy shape (`railway.json`,
  `python3 -m sb`) has **never fired in production** — CUT-3 unfired.

## External workspaces

Pointers, never copies (the § 5.7 shape) — all **null today**: no Drive
folder, ChatGPT workspace, or Gemini notebook is mapped to `superbot-next` in
any record this review read. Add the pointer here when one exists.
