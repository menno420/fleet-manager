# 2026-07-11 — P1 FRESHNESS: triggers snapshot + automated roster regen + freshness checker

> **Status:** `complete`

📊 Model: Claude (Fable family, fable-5) · start 2026-07-11T~19:00Z · lane
worker dispatched by coordinator cse_012o8pySy5K3AV6JWoPKryZL

## Declared at open (born-red)

Scope: **phase P1 (FRESHNESS) of the fleet centralization plan** (superbot
`docs/planning/fleet-centralization-plan-2026-07-11.md` §3a/§5, owner-directed,
Option A custodian-primary in force). Kills the single-point-of-freshness that
let the roster go ~13h stale and the silent-dark class that gen #6 caught
(NINE lane failsafes auto-disabled `ended_reason=auto_disabled_env_deleted`,
14:45–16:16Z today). Deliverables this PR:

1. **`telemetry/triggers-snapshot.json`** — full `list_triggers` export
   committed at each manager wake (first snapshot produced live this session;
   stable-sorted by trigger id; gives `gen_roster.py` a headless source + a
   git-visible registry history).
2. **`.github/workflows/roster-regen.yml`** — Actions cron `40 */2 * * *`
   (offset from lane heartbeats): regenerates `docs/roster.md` from the
   committed snapshot + live heartbeat re-fetch, commits on change.
3. **`scripts/check_roster_freshness.py`** — reds LOUDLY when the roster's
   generated-at stamp is older than 2× cadence (~4h); wired into CI via a
   separate workflow (substrate-gate.yml is kit-owned, never hand-edited);
   Q-0105 provenance header; verified against known-bad + known-good fixtures.
4. **Docs**: snapshot dump documented as a REQUIRED verified wake step in
   `projects/fleet-manager/coordinator-prompt.md` § work loop + the
   `gen_roster.py` regen recipe; CCR create_trigger alternative recorded as
   fallback.

Landing path: heartbeat LAST → flip this card `complete` → bootstrap check
--strict green → one REST squash-merge attempt on green (park verbatim on
denial; no auto-merge arming — known wall in this repo).

## Shipped (close-out)

- **`telemetry/triggers-snapshot.json`** — first committed full `list_triggers`
  export: **702 unique records** (8 pages, 100×7+2, zero duplicate ids),
  stable-sorted by trigger id; 21 enabled (7 standing crons + 2 poke-only +
  12 one-shots); 11 records carry `ended_reason=auto_disabled_env_deleted`
  (incl. the gen #6 nine-failsafe incident). **One deliberate deviation from
  "commit verbatim": `api_token_hint` (a credential-shaped redacted token
  prefix) stripped from 1 record** — the no-secrets bar wins. Headless path
  live-verified: `gen_roster.py --triggers telemetry/triggers-snapshot.json`
  produced a valid generation #7 to stdout (deliberately NOT committed — the
  roster was 0.3h fresh; regen cadence belongs to the workflow/manager).
  Context-wall note for future dumps: each `list_triggers` page >~25k tokens
  is auto-saved by the harness to a tool-results file — copy those files to
  the merge dir instead of transcribing; only a tiny final page ever needs
  hand-transcription.
- **`.github/workflows/roster-regen.yml`** — cron `40 */2 * * *`, offset from
  lane heartbeats: checkout → `gen_roster.py` against the committed snapshot
  (heartbeats re-fetched live over plain https — Actions runners have normal
  internet; the agent git-proxy stale-pack caveat does not apply; verified
  against gen_roster source: it needs only the snapshot + git + stdlib;
  private repos like pokemon-mod-lab degrade honestly to NOT MEASURED) →
  blocking freshness self-check → commit-on-change. ⚑ Decide-and-flag:
  **direct GITHUB_TOKEN push to main** — PR path is structurally broken for a
  bot here (no auto-merge-enabler installed + GITHUB_TOKEN PRs never trigger
  workflows → a bot PR parks forever); a protection-rejected push reds the
  run, which is itself the loud signal. Snapshot->24h advisory warning; CCR
  `create_trigger` fallback recipe in the header.
- **`scripts/check_roster_freshness.py`** — RED nonzero when the roster's
  generated-at stamp is >4h old (2× regen cadence); future-stamp guard (the
  product-forge class); Q-0105 provenance header with the gen #6 incident.
  Fixture verification (Q-0120): known-bad fabricated 2026-07-10T06:00Z stamp
  → "ROSTER FRESHNESS: RED — ... 37.1h old (threshold 4h ...)" exit=1;
  known-good fresh stamp → "ROSTER FRESHNESS: OK — ... 0.0h old" exit=0;
  live committed roster → 0.3h exit=0; --advisory on known-bad → exit=0.
- **`.github/workflows/roster-freshness.yml`** — PR gate. ⚑ Decide-and-flag
  (plan doc leaves severity unstated): **BLOCKING on claude/* (manager-
  authored) branches, ADVISORY elsewhere** — the manager's own PRs red until
  regen happens; lane/owner PRs are never jammed. Separate workflow file
  because substrate-gate.yml is kit-owned (its own header says so).
- **Required verified wake step** — `projects/fleet-manager/
  coordinator-prompt.md` v2 § work loop (a) (dump + regen + green freshness
  check at every registry-touching wake; `list_triggers` is MCP-only so the
  dump is inherently a CCR-wake step), `gen_roster.py` docstring § SNAPSHOT
  CONVENTION, and new `telemetry/README.md` (full dump recipe).
- **Heartbeat**: minimal append-style `control/status.md` update (new
  `updated:` stamp + P1 slice record appended; giant `phase:` line untouched).

## 💡 Session idea

The snapshot now gives the registry a git history, but nothing DIFFS it:
teach the roster-regen workflow (or a tiny `scripts/diff_snapshot.py`) to
emit a one-line summary of trigger-registry deltas between the last two
committed snapshots (new/deleted/disabled trigger ids, ended_reason changes)
into the commit message or a job summary — the gen #6 nine-failsafe incident
would then be a readable commit line ("9 standing crons -> auto_disabled")
instead of a hand-derived headline. Cheap: the data is two committed files.

## ⟲ Previous-session review

The roster-gen-6 session (PR #80) set the bar this session built on: its
hand-derived nine-failsafe headline is exactly the incident class P1
mechanizes, and its card's honest "UNVERIFIED header stays (2 runs; criteria
say several)" discipline made trusting gen_roster.py for the headless path an
easy, evidenced call. What it could have done better: it exported 690 records
but threw the export away (tmp-triggers.json, gitignored) — had it committed
the export, this session's snapshot would have a day-earlier baseline and the
auto-disable incident would already be a git diff. Concrete improvement
shipped here: the snapshot is now committed BY RULE (required wake step), so
no future export is ever discarded.

## Verification

- `python3 scripts/gen_roster.py --selfcheck` → PASS (0 failures).
- Headless regen from the committed snapshot → valid gen #7 to stdout,
  "702-record export, 21 enabled", all repos converged first fetch.
- Freshness checker fixtures: bad → exit 1 RED, good → exit 0, live → exit 0,
  advisory-on-bad → exit 0 (verbatim outputs in the PR conversation record).
- `python3 bootstrap.py check --strict` green on the final head (run before
  the flip push).
