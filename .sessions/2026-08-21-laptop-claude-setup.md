# 2026-08-21 — laptop setup: Claude Desktop + Claude Code on the Galaxy Book6 Pro

> **Status:** `complete` — branch `claude/desktop-app-setup-cu3ivl`. Born red;
> flipped after `python3 bootstrap.py check --strict` returned a real exit 0 on
> this tree. The gate earned its keep: it caught an invalid badge token and an
> orphaned doc, both fixed before the flip.

- **📊 Model:** opus-5 · owner-ask research + records

## What happened

The owner asked, live from a **new Galaxy Book6 Pro**, how to properly install
the desktop app, enable Claude Code locally, and what a local Claude could do
for him that the remote sessions cannot.

Answered from the vendor docs read in full rather than from memory —
`code.claude.com/docs/en/setup` and `code.claude.com/docs/en/desktop` (both
fetched 2026-08-21) — plus a spec check on the machine itself, which decides
the installer: the **Galaxy Book6 Pro runs an Intel Core Ultra X7 358H
(Panther Lake)**, so it is **x64, not ARM64**. The ARM installer is the wrong
one for this laptop and that is the single most likely way the install goes
sideways unhelped.

The payoff half is grounded in this estate rather than in vendor marketing:
`docs/ESTATE.md` and the two Layer-2 entry points
(`docs/repos/spider-swing/README.md`, `docs/repos/couch-legend/README.md`) were
read to name what specifically becomes reachable on a local machine — playing
the games, a USB-connected phone, the Godot editor.

## Shipped here (this PR)

- `docs/owner-steps-2026-08-21-laptop-setup.md` — the click-level install
  sitting (4 steps, deep-linked, every command in its own paste block), the
  verification commands, and the grounded "what local unlocks" section with its
  honest limits (native-Windows sandboxing, plan gates, CLI-only features).
- `docs/MAP.md` — one TASK row linking the guide, so it is reachable from a
  read-path doc rather than orphaned.

## ⚑ decide-and-flag (hub-side)

- **Native Windows does not support sandboxing** (vendor setup docs, platform
  table): sandboxed command execution requires WSL 2. Recorded because it is a
  real trade against the estate's habit of running agents at high autonomy —
  on this laptop that autonomy is unsandboxed unless he works inside WSL.
- **Computer use and Dispatch are Pro/Max only** — explicitly *not* available on
  Team or Enterprise plans. If the account ever moves to a Team seat, those two
  capabilities disappear; worth knowing before any plan change.

## 💡 Session idea

`docs/CAPABILITIES.md` records what an *agent session* can do. Nothing records
what the **owner's own machines** can do — and the answer now differs per
machine (the laptop reaches a USB phone and the Godot editor; a remote container
does not). A short `docs/owner-machines.md` would stop the next session guessing
whether a "just run it and see" instruction is even executable for him.

## ⟲ previous-session review

fm #881 (the couch-legend life-story hub close-out): verified live at boot —
its `docs/ESTATE.md` couch-legend row and the Layer-2 thread both matched the
tree, and its "Android shell NEXT" pointer is the thread this session's answer
leans on when it explains what a local machine unlocks for that repo. No drift
found; nothing corrected.
