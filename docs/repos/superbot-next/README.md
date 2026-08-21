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
