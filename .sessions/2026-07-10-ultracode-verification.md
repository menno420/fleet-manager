# 2026-07-10 — ultracode verification: verdict record + env archetype updates

> **Status:** `in-progress`

📊 Model: unrecorded-by-policy · adversarial-verification worker · night (~01:00Z)

## Declared at open (born-red)

Adversarial verification worker session (playbook R2: verify against repos at
HEAD, never against reports). About to land, in this one PR:

1. `docs/findings/ultracode-verification-2026-07-10.md` — the verification
   record for tonight's three ultracode-class outputs (superbot #1911 Fable
   gen-1 grand review; fleet-manager #15 harness × model experiment; superbot
   #1913 wind-down audit): owner executive summary, the three verdict tables
   verbatim, PR dispositions, ⚑ flags.
2. `environments/archetype-pinned-research.sh` — updated (setup-env.sh escape
   hatch, git-state triage, GITHUB_TOKEN presence line, THREE-deaths header
   correction) — re-verified against HEAD before copy (R19).
3. `environments/archetype-bot-prod.sh` — updated (per-repo CI interpreter
   pins incl. superbot-next → python3.11, non-mutating residue advisory,
   fail-fast-trio + YOUTUBE_API_KEY presence lines) + `archetypes.md` row.

Landing: born-red card holds the gate red; flips `complete` last. **This
session is permission-blocked from merging (session wall) — the owner (or a
permitted session) performs the REST merge-on-green (R21).** No auto-merge
arm attempt (born-red repo, R21 shape a).
