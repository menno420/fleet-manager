# 2026-08-14 · hub — Railway consolidation executed: churn stopped, duplicates retired, W1 done

> **Status:** `in-progress`

- **📊 Model:** fable-5 · high · feature build — the owner's live go on fm #861's
  recommendation: *"You can execute the recommended plan, retire the restarts
  etc and remove the duplicate websites in superbot."* Execute W1 (retire the
  three `reliable-grace` duplicate sites, reclaim the old names), stop the
  bot-restart churn (refresh schedule + worker watch filter), reduce backup
  cadence (verified first), App Sleep on the quiet keep sites, and investigate
  control-plane's egress. HARD RAIL unchanged, stated at its real scope
  (cutover plan, Step 3): never **stop, scale, disconnect, or delete**
  `worker` or either protected Postgres — the worker's watch-filter is a
  config-only `serviceInstanceUpdate` under the owner's explicit restart-fix
  directive, outside that prohibited class; `postgres-botsite` is NOT
  deleted (needs an explicit owner amendment — asked, not assumed).

Time: 2026-08-14 · venue: owner-live hub chat (remote session) · branch
`claude/railway-websites-audit-gp7nc7` restarted from `main` @ `76642e2`
(fm #861 merged; same-name branch per the merged-PR rule)

## Previous-session review

⟲ fm #861 (card `.sessions/2026-08-14-railway-websites-audit.md`, complete,
merged `76642e2`): the audit this session executes. Checked at `main`: §7 row
present, OQ-RAILWAY-PROJECT-SPLIT carries the packet, 12/12 Codex findings
conceded in the merged text. Nothing to repair.

## 💡 Session idea

Execute fm #861 § 5 with the owner's explicit go, in measured-impact order,
each mutation verified live after it lands, every Railway call by exact
service id, never project-level.

## Close-out

**Shipped (every mutation verified live after it landed):**
- **Worker watch filter** `['disbot/**', 'requirements.txt', 'requirements-dev.txt', 'pyproject.toml', 'Procfile']` — readback exact; first live test same hour: sb #2446's workflows-only merge → worker deployment `SKIPPED`, no bot restart.
- **superbot #2446** (auto-merged): `dashboard-data-refresh` schedule retired (workflow_dispatch kept, OD-3), backups daily → weekly (verified first — artifacts 171–180 MB gz/dump ≈ 1.5–2.2 GB on the wire).
- **W1 executed**: `review-f027` + old botsite + old dashboard **deleted** (per exact id; probes: f027 404 / keeps 200); `superbot-app` + `superbot-dashboard` **reclaimed** onto the canonical services (titles verified; redirects intact); `reliable-grace` = worker + 2 Postgres only.
- **App Sleep** on review-fc91 / dashboard / botsite (readback true ×3; all 200).
- **Egress root cause measured**: Meta-range crawlers (57.141.2.x, spoofed UAs) on control-plane's 620 KB `/orders`; robots.txt 404'd → **websites #501** adds Disallow-all robots.txt to the three ops surfaces (botsite stays crawlable); its `quality` red was the repo's own nav/clarity registries wanting the new route classified — five registry entries added, all six affected test files green locally (26 passed).
- Records: audit finding § 7 (execution record) · §7 W1-EXECUTED ledger row · `OQ-RAILWAY-PROJECT-SPLIT` marked executed · new `OQ-RG-POSTGRES-BOTSITE` one-letter ask · CAPABILITIES entry (httpLogs / FQDN domain trap / mutation-timeout pattern / bucketed-usage trap).

**Deliberately NOT done:** `postgres-botsite` untouched (hard-rail protected; the blanket go is not the per-service amendment — asked as `OQ-RG-POSTGRES-BOTSITE`); `OQ-WEBSITES-PAT` stays owner-side (console mint; wiring the full account PAT into a public service would violate the env-grant blast-radius rule); no change to control-plane's public/auth posture ([D-0011] stands).

**Verify:** each mutation's readback + live probe inline above; strict gate run pre-flip with real exit code (recorded at flip).

**⚑ decide-and-flag:**
- `OQ-RG-POSTGRES-BOTSITE` — A) dump-to-artifact then delete (recommended) · B) leave running (~$0.30/cycle). One letter.
- If the Sep 13 receipt still shows heavy control-plane egress, the spoofed-UA share ignored robots.txt → next levers are app-side IP/UA limits or gating the seat-era `/orders` page (a W2 purpose question).

**💡 idea:** the smoke-crawl/healthcheck workflows could log per-service `txBytes` from `httpLogs` weekly — a one-query early-warning line the bake could append to the control-plane board (folds into the W3 usage-snapshot idea from fm #861).

**⟲ previous-session review:** in the header above.

**Layer-2 handoff:** null (no `docs/repos/` folder exists for `websites` or `superbot` — Tier 2 on-demand; both repos' changes are recorded in their own PRs and this repo's finding § 7).

**PR:** fm #863 — <terminal state at flip>. Companions: sb #2446 **MERGED** · websites #501 **MERGED**, and the deployed effect verified live — `/robots.txt` probed 200 with `Disallow: /` on all three ops services at 12:47Z after the redeploy.
