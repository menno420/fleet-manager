# meta — Builder seat (superbot-next)

| Field | Value |
|---|---|
| Seat | **Builder** (Q-0261 core seat 3, "SuperBot 2.0" rebuild) — **LIVE**, booted 2026-07-10; the most Q-0265-current deployed seat (continuous-mode cutover executed + recorded verbatim on-repo) |
| Cadence | Continuation chain = one-shot `create_trigger` links ~15 min apart into `session_01HRfuSKiQSnGHXKne3yzadg` (pacemaker); cron `trig_01L5JBefGSCM1fUdwm4SRQnY` "Builder failsafe wake" **`0 */2 * * *`** (dead-man failsafe only, Q-0265) |
| Env archetype | `bot-prod` — fleet-manager `environments/archetype-bot-prod.sh` verbatim (founding package §3); env named `superbot-next`, single repo, python3.11 (CI parity), hash-pinned `requirements.lock` install; the only archetype allowed prod-pointing var NAMES. Fail-fast trio: `DISCORD_BOT_TOKEN_PRODUCTION` (TEST bot's token — never the live bot's) · `DATABASE_URL` (test-plane DSN) · `SB_DATA_PLANE=test`. `SB_TEST_DB_HOSTS` never set/asked (Q-0263.1, ORDER 011 done). NEVER in this env: Railway trio, `SB_PROD_ATTEST`, prod DSN, live-bot token (founding §3 4th-rail rule) |
| Grants | Write: **menno420/superbot-next only** (Q-0260 single-writable-repo; founding §1: "Your writable repo is superbot-next ONLY"). Read: **menno420/superbot via public raw — the ORACLE, never attached, never a write target** (founding §1/§3: "the old bot … is public and read-only to you"). **superbot-plugin-hello: pending owner creation** (status ⚑ OWNER-ACTION 2; integration token gets 403 on repo-create — evidence in docs/retro/project-review-2026-07-09.md §2 item 2; gates ORDER 002 done-when). Live-drive grants LIVE-VERIFIED at HEAD (#109): token present, intents flagged, prefix conflict resolved, guild id set |
| Codex | **ENABLED (owner, 2026-07-11; already YES before — fleet-wide enablement confirmed via fm inbox ORDER 014).** Evidence: `chatgpt-codex-connector[bot]` auto-review on **PR #103** (comment 4937122146, 2026-07-10T15:55:59Z, "Codex Review: Didn't find any major issues", reviewed commit `5fe336ad59`); further replies on #111 (comment 4938542412) per control/status.md notes. Standing @codex rule: inbox ORDER 010 / Q-0259 r.3, encoded in docs/collaboration-model.md § Standing @codex review. Quota refusals are RETRY-LATER, never a wall (fm `projects/README.md` § Codex fleet-wide enablement) |
| Ruleset | 6 required checks (named-gates.yml jobs): `code-quality` · `manifest-validate` · `architecture` · `sim-gate` · `golden-parity` · `check_compat_frozen`. `report` (golden-parity.yml) red-by-design, NEVER required. Direct-to-main blocked — branch + READY PR + **REST squash merge** is the fast lane (`enable_pr_auto_merge` declines on all-green PRs, R21). Require-up-to-date: owner-confirmed unchecked (founding §0.2 ☑ DONE) though status OWNER-ACTION 3 (merge dance) still stands pending behavior-verify at the first behind-PR |

## Deployed-state per part

| Part | Deployed state |
|---|---|
| `instructions.md` | **NEW DRAFT** — no Custom-Instructions paste file existed for this seat anywhere (inventory-lanes.md: "NO custom-instructions paste file at all"); the live seat runs on the founding-package §1 paste (historical, pre-Q-0265) + the owner-pasted §2b amendment. This draft folds Q-0265/Q-0266 + ORDER 010 + band-6 position in |
| `coordinator-prompt.md` | **NEW DRAFT (Q-0265-rewritten)** — supersedes founding §2 brief (banner-amended, body historical "one bounded slice"); provenance-stamped. The live chat received the §2b amendment paste; this canonizes the continuous work-loop prompt (inventory gap: "continuous work-loop prompt not canonized") |
| `setup-script.sh` | **DERIVED DRAFT** — from archetype-bot-prod.sh (deployed pattern, tested) + the repo's actual manifests at HEAD (requirements.lock/txt, pyproject requires-python >=3.11) + status.md env facts (HEALTH_HOST, live-drive vars) + Q-0263 silence rule. The deployed env runs the archetype verbatim |
| `failsafe-prompt.md` | **DEPLOYED + VERIFIED** — the committed verbatim text from control/status.md; trigger in registry (`list_triggers`-verified per the cutover record). This seat is the fleet's reference instance |
| `meta.md` | this file |

## Sources (all read this build, 2026-07-10)

- superbot @ origin/main `dc19b1e8`: `docs/planning/round3-founding-package-builder-2026-07-10.md` (banner-amended) · `docs/planning/gen3-deployment-standard-2026-07-10.md` §2 (Q-0265/Q-0266 folds) · `docs/planning/round3-dispatch-part4-brief-2026-07-10.md` §2b (amendment template) · router Q-0259 (r.3 @codex; r.4 family model names via Q-0262.4) · Q-0260 · Q-0263 (never-ask) · Q-0264 (sim-lab escalation) · Q-0265 · Q-0266
- superbot-next @ origin/main `9757755c61034edad4b5dee5ab715783da18f1a6`: `control/status.md` (Q-0265 cutover record, verbatim source) · `control/inbox.md` ORDERs 001–011 (009 flag-13, 010 @codex, 011 SB_TEST_DB_HOSTS) · `control/README.md` (protocol, claiming, OWNER-ACTION format) · `docs/collaboration-model.md` (§ @codex, § Continuous mode) · `docs/retro/project-review-2026-07-09.md` §3 CONTINUATION (band ladder) · `parity/README.md` (goldens integrity) · `.github/workflows/{ci,named-gates,golden-parity}.yml` (check names; report red-by-design) · `requirements.txt` / `pyproject.toml` (deps) · PR #103 + its codex comment
- fleet-manager @ main: `environments/archetype-bot-prod.sh` (setup pattern)
- inventory: `launch-packages/inventory-lanes.md` §5 (superbot-next rows) · `inventory-hub.md` (round-3 package rows)

**Last-verified:** 2026-07-10 (superbot-next HEAD `9757755`; superbot HEAD `dc19b1e8`). Family-level model names only throughout.
