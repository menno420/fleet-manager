---
state: captured
origin: owner
shipped_pr: null
shipped_repo: null
merged_date: null
outcome: open
---

# GBA play-through-Discord — emulator behind a Discord bot

> **Status:** `ideas`
>
> Captured 2026-07-10 (morning consolidation session, from the owner's
> morning coordination). State: **captured** — not approved, not scheduled.

## The idea

Put a GBA emulator behind Discord: an **mGBA headless** core renders
frames, **PIL** composes them into posted images, and a **button-row
controller** (Discord UI components mapped to GBA buttons) drives input.
Players press buttons under the message; the bot advances the emulator N
frames and posts the next screenshot.

## Why it works (and what it's for)

- **Turn-based genres fit the medium**: Pokémon-likes, tactics, RPGs,
  puzzle games — a frame-per-interaction loop is native to how they play.
  Real-time genres don't fit; don't force them.
- **Rides the PROVEN scout loop**: the in-container mGBA headless
  boot→run-N-frames→PNG pipeline runs at ~290 fps with scripted button
  injection ([`../findings/gba-toolchain-proof-2026-07-09.md`](../findings/gba-toolchain-proof-2026-07-09.md)) —
  the hard technical half already exists and is verified.
- **Natural superbot-next plugin**: the rebuild's adapter/domain seam
  (component feeds, panel model) is exactly the shape this needs —
  a game session is a panel with a button row and a state store.

## Publication rails (hard)

- **Homebrew ROMs** (gba-homebrew's own games, e.g. Lumen Drift):
  publishable **publicly** — original code, no rights issues; this is
  also a distribution channel for game-lab Track B output.
- **Commercial ROMs** (incl. the pokemon-mod-lab builds): **private-guild
  only, never public** — same rail as the pokemon-mod-lab repo itself.

## Next destination

Route: structured plan when picked up — natural home is a
superbot-next plugin band (or a games-plugins lane order) once the
games-plugins gen-2 lane is running; the emulator loop can be prototyped
against gba-homebrew's committed ROMs with zero new toolchain work.
