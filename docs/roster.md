# Fleet roster — GENERATED

> **Status:** `living-ledger`
>
> **GENERATED — do not hand-edit; regenerated each manager wake (`scripts/gen_roster.py`, R25).**
>
> **Generation #23** · generated-at **2026-07-13T04:10Z** · by roster-regen workflow (GitHub Actions, headless), dispatched by cron 40 */2 * * * (.github/workflows/roster-regen.yml, fleet-manager PR #81) · machine generation (`scripts/gen_roster.py`)
>
> **Source of truth = the lane heartbeats** (each repo's `control/status*.md` at an ls-remote-verified HEAD over git transport) + the live trigger registry (`list_triggers` export). This file is a derived snapshot. **Kill-switch: if this file's generated-at goes stale >24h, trust the heartbeats directly** — do not act on a stale roster row.
>
> **Transport verification:** every repo HEAD below was fetched shallow and re-fetched until FETCH_HEAD == a fresh `git ls-remote` (stale-proxy-pack doctrine, roster gen #3); all repos converged on the first fetch. Repos that could not be read are marked NOT MEASURED with the verbatim wall reason and verdict UNREADABLE (transport/auth) — a measurement artifact, never guessed and never printed as lane death.
>
> **Trigger evidence:** 1078-record export, **35 enabled**: 12 standing crons + 1 poke-only + 22 one-shots.
>
> **Sub-rows (P3, plan §3c):** a `↳` row is an EXTRA heartbeat file in the same repo (all `control/status*.md` are enumerated; `substrate.config.json heartbeat_files` ordering honored) — judged on its own `updated:` stamp; wake triggers live on the parent lane row. Evidence homes per lane: `docs/evidence-index.md` (generated with this file).
>
> **Trigger health (ORDER 020):** evaluated at **2026-07-13T02:28Z** (basis: snapshot captured_at) · grace 15min. Fleet-wide: **2 WEDGED cron(s) · 9 DROPPED-or-QUEUED one-shot(s) · 2 DEAD chain(s)** — detail section below the verdicts; wake-time enforcement: `scripts/check_trigger_health.py`.

| Lane | Heartbeat `updated:` | Age | Verdict | Phase (machine-truncated) | Orders | Kit | Wake state (trigger · cron · last fire) | Trigger health | Evidence (repo @ HEAD) |
|---|---|---|---|---|---|---|---|---|---|
| superbot (hub) | 2026-07-11T19:45:00Z | ~32h25m | DARK | STEADY — hub coordination surface (docs/ledger/recon + fleet relay); product runtime work is lane-side (superbot-next rebuild at 37/49 ports per #1996) | acked=001-002 done=001-002 (001 done at #1977; 002 done at #2003 — record: docs/retro/self-review-2… | — | poke-only `suberbot docs reconciliation` | OK | `5262fe4` 2026-07-13T04:04:18 |
| superbot-next | 2026-07-13T02:47Z | ~1h23m | FRESH | SEAT OPEN — coordinator session_01KhzyfUk76YB9Bj2TPF6h5z active; night run executing ORDER 017 (owner night-run mandate, inbox@HEAD, landed verbatim by #323). … | acked=001–017 done=002–016; ORDER 017 executing (night run); ORDER 001 open — band-1 live-drive req… | v1.15.0 | **NONE** | — (no attributed triggers) | `a4d51b6` 2026-07-13T04:06:50 |
| substrate-kit | 2026-07-13T02:11:22Z | ~1h59m | FRESH | NIGHT RUN (ORDER 016) — items 1–3 shipped, item 4 green-parked for ratification, item 5 + tally due by 06:00Z | acked=001–016 · done=001–015 · 016 IN PROGRESS (night run) | v1.15.0 · check: green · engaged: yes | **kit-lab loop** `trig_01Jm57GAjNCFrYJn1oLMiYGE` · `0 6 * * *` · last 2026-07-12T10:28:21 · next 2026-07-13T06:08 | OK | `917261b` 2026-07-13T02:13:18 |
| ↳ substrate-kit — `control/status-gba-homebrew-trackb.md` | 2026-07-10T05:06:52Z | ~3.0d | DARK | visit COMPLETE with this build PR's merge — both gate-template sentinel fixes shipped upstream (claim #105 → this build PR, per the claim ritual); the lane ret… | none for this lane (no inbox order; defect-fix visit under the adopter-findings precedent, cf. #83 … | adopter-side v1.6.0 (menno420/gba-homeb… | (triggers on the parent lane row) | (parent row) | `917261b` 2026-07-13T02:13:18 |
| ↳ substrate-kit — `control/status-superbot-coordinator.md` | 2026-07-10T13:47:02Z | ~2.6d | DARK | session close-out complete — gen-1 coordinator lane archived, handoff committed. The lane's final doc is docs/succession/close-out-2026-07-10-superbot-coordina… | wind-down done, close-out done — no orders remain for this lane; the successor lane claims its own | v1.7.0 (repo) · check: green (strict + … | (triggers on the parent lane row) | (parent row) | `917261b` 2026-07-13T02:13:18 |
| websites | 2026-07-13T02:51:21Z | ~1h19m | FRESH | NIGHT RUN 2026-07-13 ACTIVE — ORDER 022 progress ledger at this write: item 1 clarity bar DONE across live pages (#229 control-plane, #231 botsite+dashboard; a… | acked=001-022 done=001-019 (020 IN PROGRESS — filing #183 + build #189 merged, remaining = the owne… | v1.15.0 · check: green · engaged: yes | **Websites failsafe wake** `trig_019cGrUpfHSMv4qLk5tn2hgr` · `45 */2 * * *` · last 2026-07-13T02:10:03 · next 2026-07-13T02:45; **Websites review-bake bridge** `trig_01WA3ewRinYv6sN9Sm4CGx3b` · `33 5 * * *` · last never · next 2026-07-13T05:33 | OK | `1a411d1` 2026-07-13T04:05:46 |
| trading-strategy | 2026-07-12T21:02:36Z | ~7h08m | STALE | — | — | substrate-kit v1.15.0 (vendored bootstr… | **trading-strategy weekly paper-lane grading** `trig_01FRG4uUxPh5ZGncZGfRgF2F` · `0 9 * * 5` · last never · next 2026-07-17T09:06; +1 one-shot(s), next 2026-07-17T09:00 | OK | `5bc063d` 2026-07-13T03:58:24 |
| venture-lab | 2026-07-13T01:49:05Z | ~2h21m | FRESH | — | — | — | **Venture Lab failsafe wake** `trig_01HCLdpcX9QNUz4Y33efgt57` · `45 1-23/2 * * *` · last 2026-07-13T01:45:14 · next 2026-07-13T03:45 | OK | `2c039e3` 2026-07-13T04:00:37 |
| superbot-games · Seat A | 2026-07-12T10:16:22Z | ~17h54m | STALE | docs-correction — landed a docs-only PR correcting stale "plugin contract in flight" claims; no feature-code change. Close-out/archive-prep from the prior wake… | acked=001,002,003,004,005 done=001,002,003,005 | — | **NONE** | — (no attributed triggers) | `5aec110` 2026-07-13T02:46:23 |
| ↳ superbot-games · Seat A — `control/status-exploration.md` | 2026-07-09T20:09Z | ~3.3d | DARK | WIND-DOWN COMPLETE — ready for archive + fresh (gen-2) session | acked=001,002,003,004,005 done=001,002,003,004,005 | substrate-kit v1.7.1 — adopted (D‑0002)… | (triggers on the parent lane row) | (parent row) | `5aec110` 2026-07-13T02:46:23 |
| ↳ superbot-games · Seat A — `control/status-mining.md` | 2026-07-11T19:36Z (archive-prep VERIFY + TOP-UP; verified a… | ~32h34m | DARK | gen-1 mining complete — ARCHIVE-READY. Pure domain + grid-encounters first slice shipped to main. Gen-1 lane is closed and archived; gen-2 boots only from what… | — | substrate-kit v1.7.1 — adopted on main … | (triggers on the parent lane row) | (parent row) | `5aec110` 2026-07-13T02:46:23 |
| superbot-idle (Seat B) | 2026-07-12T10:17Z | ~17h53m | STALE | RESUMED for ORDER 003 (pytest CI) — a P1 order landed in control/inbox.md (2026-07-12T08:30Z), waking the lane from ARCHIVED-READY; addressed by PR #74. Meanwh… | acked=000-003 done=000-002 (003 in-flight: PR #74 READY+green, awaiting owner required-check + merg… | v1.7.1 · check: green | **NONE** | — (no attributed triggers) | `c735075` 2026-07-13T01:50:23 |
| superbot-mineverse | 2026-07-12T23:41:43Z | ~4h29m | STALE | heartbeat — backlog wave shipped (#47–#53), kit finding routed to kit-lab (branch claude/heartbeat-2314). COORDINATOR-DELEGATED heartbeat write — the coordinat… | acked=001,002,003 done=001,002,003 | v1.8.0 | **NONE** | — (no attributed triggers) | `79a4018` 2026-07-13T02:21:33 |
| retro-games coordinator (no repo) | n/a — registry-only seat (no repo) | n/a | n/a (registry-only seat) | — | — | — | **NONE** | — (no attributed triggers) | trigger registry only |
| game-lab (no repo) | n/a — registry-only seat (no repo) | n/a | n/a (registry-only seat) | — | — | — | **NONE** | — (no attributed triggers) | trigger registry only |
| pokemon-mod-lab | NOT MEASURED (wall: fatal: could not read Username for 'https://github.com': terminal prompts disabled — priv…) | n/a | UNREADABLE (transport/auth) | — | — | — | **NONE** | — (no attributed triggers) | NOT MEASURED (wall: fatal: could not read Username for 'https://github.com': terminal prompts disabled — priv…) |
| gba-homebrew | 2026-07-12T16:20:12Z | ~11h50m | STALE | WORK LOOP cycle 5 (merged seat v1) — idle on owner clicks, both next slices pre-built | — | — | **NONE** | — (no attributed triggers) | `d87f9ad` 2026-07-13T01:45:05 |
| product-forge | 2026-07-11T19:39:50Z | ~32h30m | DARK | close-out / archived-ready | acked=001,002,003,004 done=001,002,003,004 | — | **NONE** | — (no attributed triggers) | `4fdfa8a` 2026-07-11T19:49:47 |
| idea-engine | 2026-07-12T23:44:55Z (real wall-clock via date -u, per the … | ~4h25m | STALE | SESSION 2 ACTIVE — governing order: owner ORDER 003 (continuous idea pipeline, P1 standing; landed verbatim via PR #274 → 1bfcde6); the pipeline is RUNNING (cy… | acked=001-003 done=002 (001 standing — its per-session rule re-satisfied this session: the session … | v1.10.0 · check: green · engaged: yes | **NONE** | — (no attributed triggers) | `15d1802` 2026-07-13T03:56:09 |
| sim-lab | 2026-07-12T23:32:28Z | ~4h38m | STALE | ACTIVE — under the merged Ideas Lab seat (Q-0264; idea-engine + sim-lab, one seat), coordinator session 2 (booted 2026-07-12 ~20:45Z; owner ORDER 003 standing … | acked=ORDER-001 ORDER-002 ORDER-003 done=ORDER-001 ORDER-002 ORDER-003 (ORDER-001 model-attribution… | v1.7.0 · check: green (bootstrap.py che… | **NONE** | — (no attributed triggers) | `6c7e278` 2026-07-13T03:47:22 |
| codetool-lab-fable5 | 2026-07-09T20:06Z | ~3.3d | STALE-BY-DESIGN | wind-down complete — ready for archive + fresh session | acked=001,002,003,004 done=001,002,003,004 | — | **NONE** | — (no attributed triggers) | `a6cf1a9` 2026-07-10T12:07:20 |
| codetool-lab-opus4.8 | 2026-07-09T20:11:35Z | ~3.3d | STALE-BY-DESIGN | wind-down complete — ready for archive + fresh session | acked=001,002,003,004 done=001,002,003,004 | — | **NONE** | — (no attributed triggers) | `80f6cd1` 2026-07-09T20:13:54 |
| codetool-lab-sonnet5 | 2026-07-09T20:02:14Z | ~3.3d | STALE-BY-DESIGN | wind-down complete — ready for archive + fresh session | acked=001,002,003,004 done=001,002,003,004 | — | **NONE** | — (no attributed triggers) | `66c3dfc` 2026-07-09T20:09:52 |
| fleet-manager (this repo) | 2026-07-13T03:05Z — coordinator seat ACTIVE (continuous ope… | ~1h05m | FRESH | oversight steady-state; consolidation Phase 1 ORDERs routed; owner goal ORDERs 030–036 dispatched. | — | v1.7.0 · check: green · engaged: yes | **Fleet Manager failsafe wake** `trig_01UQTZFvknBosXVo4YKKfazZ` · `30 */2 * * *` · last 2026-07-13T00:37:55 · next 2026-07-13T02:37 | OK | `02cb4df` 2026-07-13T02:45:51 |

## Staleness verdicts (generation #23)

- **DARK:** superbot (hub), ↳ substrate-kit — `control/status-gba-homebrew-trackb.md`, ↳ substrate-kit — `control/status-superbot-coordinator.md`, ↳ superbot-games · Seat A — `control/status-exploration.md`, ↳ superbot-games · Seat A — `control/status-mining.md`, product-forge
- **UNREADABLE (transport/auth):** pokemon-mod-lab
- **STALE:** trading-strategy, superbot-games · Seat A, superbot-idle (Seat B), superbot-mineverse, gba-homebrew, idea-engine, sim-lab
- **FRESH:** superbot-next, substrate-kit, websites, venture-lab, fleet-manager (this repo)
- **STALE-BY-DESIGN:** codetool-lab-fable5, codetool-lab-opus4.8, codetool-lab-sonnet5
- **n/a (registry-only seat):** retro-games coordinator (no repo), game-lab (no repo)

## Trigger health (generation #23)

> ORDER 020 (per-wake trigger-health; canonical spec: superbot `docs/owner/trigger-health-order-2026-07-12.md`). Evaluated at **2026-07-13T02:28Z** (basis: snapshot captured_at); grace 15min. A QUEUED tick (bound to a busy session — delivers when the turn goes idle, sound by design) is indistinguishable from a LOST one on the registry, so BOTH are flagged. Recovery for a DEAD chain / dark seat: `send_message` that seat's session (the manager's only working cross-session revival path — fire/update/create_trigger on another session are org-refused; do NOT re-edit .claude/settings.json for the prompts, Q-0242). This section rides the Actions regen substrate so the watchdog's record survives a CCR scheduler outage.

- **WEDGED cron(s): 2** — enabled with `next_run_at` frozen in the past:
  - `trig_01Kz3j5ECTZ29hNZCHukgCA1` Ideas Lab failsafe wake · `30 1-23/2 * * *` · next frozen 2026-07-13T01:38Z · lane: (unattributed)
  - `trig_01TuQrpMVpDCXB3K3VbjQUoA` SuperBot 2.0 failsafe wake · `0 1-23/2 * * *` · next frozen 2026-07-13T01:07Z · lane: (unattributed)
- **DROPPED-or-QUEUED one-shot(s): 9** — enabled past `run_once_at` (never delivered), by seat session:
  - `session_015xJBwRogy1ByzZmeWC38qW`: 1 dropped, oldest due 2026-07-13T01:08Z · lane: (unattributed)
  - `session_01CXEh5TBKBNTDGgsDstfcjc`: 1 dropped, oldest due 2026-07-13T01:27Z · lane: (unattributed)
  - `session_01K3A7v82YxTxzaFztpbgEY2`: 1 dropped, oldest due 2026-07-13T01:39Z · lane: (unattributed)
  - `session_01KhzyfUk76YB9Bj2TPF6h5z`: 2 dropped, oldest due 2026-07-13T01:37Z · lane: (unattributed)
  - `session_01Kn5PjZR5EDJL75BeELkUfr`: 1 dropped, oldest due 2026-07-13T01:55Z · lane: (unattributed)
  - `session_01MSze9jQLdxByyv2j6rm29c`: 1 dropped, oldest due 2026-07-13T01:49Z · lane: (unattributed)
  - `session_01N9QvWRsgjhunTTPJU3UoZA`: 1 dropped, oldest due 2026-07-13T01:39Z · lane: (unattributed)
  - `session_01Q5sGKgKCngGa7jgfzEGeEQ`: 1 dropped, oldest due 2026-07-13T01:39Z · lane: (unattributed)
- **DEAD chain(s): 2** — dropped tick + NO future tick armed on the session (recover via `send_message`):
  - `session_01KhzyfUk76YB9Bj2TPF6h5z` · 2 dropped, no future tick · lane: (unattributed)
  - `session_01N9QvWRsgjhunTTPJU3UoZA` · 1 dropped, no future tick · lane: (unattributed)

> Machine generation: the hand generations' "Deltas vs generation #N-1" narrative is coordinator judgment and is NOT auto-derived — read `git diff` on this file, or append prose below before committing.
