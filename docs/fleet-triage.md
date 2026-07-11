# Fleet triage register — keep / replace / archive / delete

> **Status:** `living-ledger`
>
> The standing, re-reviewable **"should it exist?"** ledger for every fleet
> repo — distinct from `roster.md` (freshness now) and the product catalog
> (what each thing is). **Canonical home: fleet-manager** (centralization plan
> §4 — cross-repo/fleet state lives here), ported 2026-07-11 (P3, fm PR #86)
> from the seed review. Re-verdict rows as reality moves; a verdict is a
> dated judgment, not a decree — cite evidence when you change one.
>
> **Seed provenance:** superbot
> [`docs/planning/fleet-review-2026-07-11.md`](https://github.com/menno420/superbot/blob/main/docs/planning/fleet-review-2026-07-11.md)
> §1 — the owner-directed 2026-07-11 verified full-fleet review (19-agent
> fan-out, every load-bearing claim source-verified, Q-0120). That doc stays
> as the frozen program-narrative snapshot; THIS file is the living register.

## Verdict legend

**KEEP** (active, earns its place) · **KEEP-SEQUENCE** (keep, mid-build,
defined next step) · **KEEP-PARKED** (keep the asset, park the loop) ·
**ARCHIVE** (finished, make read-only, lose nothing) · **SEED** (empty, one
action to activate) · **DELETE** (none).

## Register (verdicts as of 2026-07-11; seed = the fleet review §1, verified)

| Repo | Health | Verdict | One-line rationale | The single next action |
|---|---|---|---|---|
| **superbot** (hub / prod bot) | 🟢 | KEEP | The oracle + the live product; the whole program's substrate | Normal live-verify of merges; fix the Rule-6 false-green checker (review §3) |
| **superbot-next** (rebuild) | 🟡 | KEEP-SEQUENCE | Flagship build, 37/49 ported, boots on real PG; 2 money races to fix pre-cutover | Fix F-001/F-002 wallet races + F-003 parity false-green, then continue ports |
| **substrate-kit** (fleet foundation) | 🟡 | KEEP | 7 adopters run on it; gate false-green shipped in v1.12.0; #228 was an empty fix | Land the *real* gate fix, cut a patch release *(post-seed: fixes landed via kit #228 successor work — re-verify at next sweep)* |
| **websites** (oversight/control-plane) | 🟢 | KEEP | 4 real services, 3 live; the fleet's visual control plane; backlog drained | Owner: merge #141 + create the `review` Railway service |
| **venture-lab** (first revenue) | 🟡 | KEEP | 3 real built products; **critical Stripe fail-open** before publish | 🔴 Fail-closed on partial Stripe config, then publish |
| **superbot-mineverse** (web game) | 🟡 | KEEP | Real read-only demo; login-CSRF + pytest-not-required before secrets | Bind OAuth state to browser + schema-validate; make pytest required |
| **superbot-games** (game engines) | 🟢 | KEEP | Pure-domain, green, DM-clamp verified; parked on plugin contract (correct) | ~~Owner merge #49 then #50~~ *(post-seed: #49 merged `5d38593` 17:22Z)*; refresh stale status |
| **superbot-idle** (idle engine) | 🟡 | KEEP-SEQUENCE | 827 tests, 12 themes; **self-parked on a blocker that's already resolved** | Lift PLUG-001 (contract EXISTS in superbot-next), build the adapter; land SIM-001 |
| **product-forge** (web-product forge) | 🟢 | KEEP | Real games-web, 22 PRs, foundational infra ("home to homeless projects") | Owner: enable GitHub Pages (one toggle — `OQ-FORGE-PAGES`) |
| **gba-homebrew** (GBA game) | 🟢 | KEEP | Playable committed ROM, reproducible CI build; low-maintenance | Owner: create the Lumen Drift v1.3 Release (`OQ-GBA-LUMEN-RELEASE`) |
| **pokemon-mod-lab** (private ROM mod) | 🟢 | KEEP-PARKED | Real 16-patch mod, private, copyright-safe; idle ~18 sessions, all owner-gated | **Pause/slow the hourly wake**; owner playtest verdict unblocks it (`OQ-SITTING-0714-DECISIONS`) |
| **trading-strategy** (quant research) | 🟢 | KEEP-PARKED | Honestly complete (holdout spent, 0/13 cleared); paper lane in warm-up | Leave parked until the 2026-07-17 grading |
| **sim-lab** (evidence/lie-detector) | 🟢 | KEEP | 10 verdicts, self-checks caught a real bug; idle-by-design not stuck | ~~Owner: enable Codex (OA-002)~~ *(post-seed: resolved — Codex envs exist for all 12 active repos, ORDER 014)* |
| **idea-engine** (ideation) | 🟢 | KEEP | 193 PRs, reports verify true; surfaced a real superbot false-green | Split the 25KB status.md; lift the ≤07-13 owner decision out of the bloat |
| **fleet-manager** (coordination substrate) | 🟢 | KEEP | The de-facto SSOT; roster/queue/inbox real | *(post-seed: the seed's "ledgers drift + stubs unfilled" 🟡 is CLOSED by P1–P3, fm #81–#86)* Keep the custodian loop green |
| **superbot-plugin-hello** | ⚪ empty | **SEED** | Empty repo gating two finished engines (idle + games) | 🟢 One word: "push the plugin seed" (`OQ-PLUGIN-SEED-WORD`) |
| **codetool-lab-fable5** (envdrift) | ⚫ parked | **ARCHIVE** | Finished CLI, wound-down, no mission | Archive after gen-3 succession settles; pending tag/Release clicks |
| **codetool-lab-opus4.8** (mdverify) | ⚫ parked | **ARCHIVE** | Finished CLI, releases live, wound-down, no mission | Archive after gen-3 succession settles |
| **codetool-lab-sonnet5** (cfgdiff) | ⚫ parked | **ARCHIVE** | Finished CLI, wound-down, no mission | Archive after gen-3 succession settles; pending v0.1.1 tag |

**19 repos · 15 active (all KEEP-family) · 3 ARCHIVE · 1 SEED · 0 DELETE**
(seed tally, unchanged at port time).

## How to re-verdict

1. Verify against live source (Q-0120 — never against report text).
2. Edit the row: new verdict + dated one-line evidence citation (SHA / PR).
3. Cross-check the owner-queue: a verdict whose "next action" is an owner
   click must have (or get) an `OQ-` item; cite the slug.
4. Wholesale re-reviews land as a new dated seed note here, not a fork file.
