# 2026-07-10 — ultracode verification: verdict record + env archetype updates

> **Status:** `complete`

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

## Done (close-out)

- **PR #16** opened READY right after the born-red card push
  (<https://github.com/menno420/fleet-manager/pull/16>).
- **Findings record** — `docs/findings/ultracode-verification-2026-07-10.md`:
  owner exec summary; the three verdict tables **verbatim** (superbot #1911:
  18 verified / 1 refuted / 1 unverifiable; fm #15: 13/2/2; superbot #1913:
  17/1/1); PR-disposition table; six ⚑ flags (queued merges, ultracode
  feature-name confirmation before the experiment launch, the
  starboard/paragon parity-row correction, the ping-test websites-row error
  in this repo, the venture-lab add_repo wall, the `undefined`
  template-rendering bug). Findings README index row added.
- **Env archetypes** — both updated scripts copied over after an R19 re-read
  of HEAD (`ce8e984`; no other writer had touched them): pinned-research
  (setup-env.sh hook recognition — websites' committed name; git-state
  triage; GITHUB_TOKEN presence; python3 version boot log; THREE-deaths
  header fix) and bot-prod (per-repo CI interpreter pins superbot→3.10 /
  superbot-next→3.11; report-only workspace-residue advisory with the
  `git checkout main && git pull --ff-only` recovery hint; fail-fast trio
  cited to `sb/spec/config.py`; YOUTUBE_API_KEY presence). `bash -n` clean;
  both smoke-ran exit 0 in an empty dir; R15 contract intact (unconditional
  `exit 0`, names-only env reporting). `archetypes.md` bot-prod row updated
  to match.
- **Disposition executed** — verification comment posted on superbot #1913
  (17/1/1 result, the sonnet5 shell-script refutation, rebase-then-merge
  recommendation): #1913 state = commented / blocked on conflicts.
- **Not done here (queued for the owner):** every merge — this session is
  permission-walled from merge tools. fleet-manager #16 lands via REST
  merge-on-green after this flip; superbot #1913 needs a rebase + one-line
  correction first.

## 💡 Session idea

**Verbatim-embed verdicts by reference, not by copy:** this session pasted
three full verdict tables (≈300 lines) into one findings file because the
worker outputs lived only in a session scratchpad. If verification workers
committed each verdict as its own `docs/findings/verdicts/<key>.md` in their
own PR lane, the aggregating session would link rows instead of duplicating
whole tables — no drift risk when a verdict gets corrected later, and the
findings index stays scannable. Cheap convention, one README line to
establish.

## ⟲ Previous-session review

The harness-experiment session (PR #15) shipped an unusually careful
pre-registered protocol, but this session's verification of it surfaced a
process gap worth fixing: its PR body claimed "new files only" while the diff
also edited `docs/AGENT_ORIENTATION.md` — exactly the class of letter-level
drift R2 exists to catch, in the repo that *wrote* R2. Concrete improvement:
the PR-body template for routine lanes should carry a one-line
`files: <n> new / <n> modified` stanza generated from `git diff --stat`
rather than typed from memory — a 30-second discipline that would have made
both of tonight's "new files only" misstatements impossible.
