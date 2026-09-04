# The architecture-pattern matrix

> **Status:** `plan` — authoritative for the **disposition of every engineering
> pattern** in `superbot` and `superbot-next`: which repository each pattern
> should be taken from, which is replaced, and which the successor does not build
> at all. Product capabilities are [`02-product-matrix.md`](02-product-matrix.md);
> why the two repos failed differently is [`04-root-cause.md`](04-root-cause.md);
> the successor's own design is [`06-architecture.md`](06-architecture.md).

## 0 · How to read this

**Verdict vocabulary**, five values, used strictly:

| verdict | means |
|---|---|
| **preserve from superbot** | the shipped bot's mechanism is the donor; the successor's version starts from it |
| **preserve from superbot-next** | the rebuild's mechanism is the donor |
| **merge ideas** | both repos hold a structural half the other lacks; neither alone is sufficient |
| **replace both** | both answers are wrong or absent; the successor designs this |
| **omit** | build nothing here until a named condition is met |

A parenthetical after a verdict (**"contract replaced"**, **"simplified"**)
qualifies *what* is taken, and never converts one verdict into another.

**Evidence marking.** Every number this session re-derived against the pinned
clones is stated bare and carries its `I-` id
([`run/independent-findings.md`](run/independent-findings.md)). Every number
carried from a fleet lane without re-derivation is marked **`lane-claimed`**
inline, at the number, with its row id
([`run/evidence-digest.md`](run/evidence-digest.md)). The rule and the reason:
[I-17](run/independent-findings.md), [I-18](run/independent-findings.md).

**Three corrections move rows in this matrix**, and each is worked in § 2 rather
than argued in a table cell:

1. **Attribution reversals** (§ 2.1). The 2026-08-21 plan named `superbot-next`
   the *"architecture donor"* and opened its preserve list with **"explicit
   layers and import-direction guards"** and **"provider-neutral AI contracts…
   behind one gateway."** Both belong to `superbot` (I-3, I-4, I-21). Three rows
   below therefore point at the repo the prior plan told an implementer to
   ignore.
2. **The clean DAG is a measurement artifact** (§ 2.3). `superbot-next`'s
   layering is real only where a module-level census can see it: 268 of 296
   cross-subsystem `sb.domain` imports (90.5 %) sit in function bodies, and all
   8 mutual subsystem pairs live there — 0 at module level (I-22).
3. **The population defect** (§ 2.5, and [`08-verification.md`](08-verification.md)
   § 1). Several patterns below are green in CI over an empty set. A pattern is
   dispositioned on what it *does*, never on what its gate reports.

---

## 1 · The matrix

### A · Composition and extension

| pattern | superbot | superbot-next | VERDICT | why (one line) |
|---|---|---|---|---|
| **cogs** — the feature module unit | 59 `INITIAL_EXTENSIONS`, each loaded in its own `try/except`, failure recorded and the subsystem demoted to INTERNAL rather than crashing the process (`disbot/bot1.py:721-745`, R3-S1); runtime load/unload/reload audited with a `_PROTECTED_COGS` guard (`cogs/admin/cog_manager.py:191-200`, R3-S2); **cog→cog imports are unconstrained** — `layers.yaml:57-60` lists `cogs` in `cogs.may_import`, and **128** module-level `from cogs.<x>` statements across 51 files sit inside `cogs/` (I-17; R3 reported 134, `lane-claimed`) | no cog concept; 49 manifests auto-discovered by `pkgutil` with no hand-maintained list (`sb/app/main.py:91-104`, R3-S6); any single plugin violation aborts the whole boot (`main.py:365-367`, R3-D6); no deploy-time subset — all 49 load unconditionally (R3-D7); the Cog Manager ported as a dead end wired to `pending_handler` (`sb/domain/admin/cogmgr.py:43-49`, R3-D8) | **merge ideas** | take `superbot`'s per-module fault isolation and in-Discord unload lever, `superbot-next`'s auto-discovery, and add the module→module coupling rule neither has |
| **manifests** — declarative feature declaration | none; the equivalent is **13** hand-coordinated touch-points enumerated by `scripts/new_subsystem.py` (R3-S10, `lane-claimed`) that nothing ever sweeps — no `--all` mode, one key per invocation (R3-D11) | 49 manifests compiled to a committed snapshot, recompiled **in-process at boot** with divergence = `FAILED_STARTUP` (`sb/app/boot_gate.py:74-79`, M9-S04); fired both ways — one changed description string reds `manifest_compile.py` and `check_runtime_smoke.py` (M8-S02, `lane-claimed`); but 107 of 237 grammar fields are never given a non-default value (M9-D08, `lane-claimed`) and three P6 semantic predicates key on fields **0 of 3,552** walked objects carry (M9-D02/D03, `lane-claimed`) | **preserve from superbot-next** (grammar cut) | one declaration per feature is the fix for § 1.2 of the root cause; ship only fields with a live consumer and a predicate with a non-empty population |
| **plugins** — out-of-tree extension | none (B-S11) | entry-point discovery, hash-pinned `plugins.lock.json`, joint compile with in-tree manifests; pinning proven both ways — zeroing a hash and deleting a pin each red (M8-S07, `lane-claimed`); **but `HOST_ONLY_FACETS = (stores, data_invariants, wizard_sections)` makes 29 of its own 49 subsystems ineligible** (I-10, `sb/app/plugin_host.py:76-83`) | **preserve from superbot-next** (contract replaced) | the pinning and joint-compile discipline is right and the facet fence must go: an out-of-tree module that cannot own data serves the stateless two-fifths, and precisely not the class OD-19 names |
| **registries** | `SUBSYSTEMS` validated, deep-frozen and raising typed `RegistryValidationError` subclasses at boot (`utils/subsystem_registry.py:1308-1318`, A-S07); but 43 real keys against 59 cog modules with `starboard` absent (R3-D10/R3-D1), the parent link stored twice across two registries, and `interaction_router.register()` logs *"Overwriting existing handler for prefix"* and silently replaces — over **280** hand-written `custom_id=` literals in 86 files (`interaction_router.py:89-93`, B-D09, `lane-claimed`) | one static `custom_id` table minted at registration with a **raising** collision fence (`PanelCompileError('custom_id_collision')`), 863 entries and 0 collisions over all 314 panels (`sb/kernel/panels/registry.py:77-95`, M9-S02/B-S08, `lane-claimed`); but registries are process-global mutable dicts with **92** `clear_*_for_tests` / `reset_*_for_tests` functions (E-D6, `lane-claimed`) — the mechanism that emptied the navigation golden (I-2, `registry.py:177-180`) | **merge ideas** | mint ids once with a raising fence (next) behind a boot-time validate-and-freeze (superbot), and no registry may be a process global a fixture can empty |
| **services** — the domain layer | 190 flat modules in `disbot/services/`, 86,749 LOC = 35.6 % of `disbot` (E-D10, `lane-claimed`), and **acyclic** — 148 edges among 93 modules, 0 mutual pairs (E-S6, `lane-claimed`, and the load-bearing half of I-22's correction); one canonical mutation owner per domain in `mutation_owners.yaml` | 48 domain packages whose `{handlers,ops,service,store}.py` combination takes **9 distinct shapes** (E-D7, `lane-claimed`); 268 of 296 cross-subsystem imports in function bodies, all 8 mutual pairs there (I-22) | **replace both** | one canonical file role per feature package, plus a cycle-failing whole-AST import guard — `superbot` has the acyclic result without the convention, `superbot-next` has neither |

### B · Mutation, data and the write path

| pattern | superbot | superbot-next | VERDICT | why (one line) |
|---|---|---|---|---|
| **workflow engine** — the typed operation | no equivalent; mutation services plus a remembered audit call — `emit_audit_action(` at **49 sites in 27 files** (I-18, re-derived; the lane said 28 files) | one mutation seam for 32 of 49 domains (`sb/kernel/workflow/engine.py`, M9-S07, `lane-claimed`); `audit_verb: str` is a **required no-default field** on a frozen dataclass, 175/175 ops carry one (`spec.py:121-131`, B-S01, `lane-claimed`); authority resolved as leg 0 before any leg runs (`engine.py:124-136`, B-S02); but **0 of 175** carry a `ConfirmationSpec` (B-D05) and **0** are `DURABLE_ONCE`, so the dedup branch is dead code (B-D03), over 173 DB legs / 12 effect legs / 0 irreversible (B-D11) — all `lane-claimed` | **preserve from superbot-next** (simplified) | this is exactly [the 2026-09-04 AI-authority decision](run/in-flight-direction.md)'s *typed operation* and the most expensive seam to re-derive; the saga/compensator layer is omitted until a second leg kind exists |
| **event bus** | `core/events` with services emitting real payloads asserted in tests (M2-S7); no declared event graph | `KNOWN_EVENTS` names events and `check_runtime_smoke` asserts every armed subscriber names a known event bound to a real callable — a one-character typo (`bus.on("xp.level_upp")`) reds it (M8-S05, `lane-claimed`); but `SUBSCRIBE_ROSTER` is a hand-maintained 6-entry tuple whose completeness nothing enforces (M8-D05) and **all 23** `EventSpec`s declare `expected_subscribers=()`, so the compiler's delivery fence iterates an empty tuple every time (M9-D07) — both `lane-claimed` | **merge ideas** | keep next's boot-time subscriber resolution (it fires on an injected typo), derive the roster instead of typing it, and require a declared subscriber set to be non-empty — the population rule applied to the event graph |
| **authority / permissions** | authority lives on the **surface**: 166 decorators in `cogs/`, 3 in `views/`, **0 in `services/`** while 190 service modules hold the mutations; 19 of 93 service-importing view modules carry any authority token (B-D07, `lane-claimed`); governance installed at exactly one seam (`bot1.py:646-652`) that discord.py applies to prefix commands only — 31 app_commands never reach it (M5-D01); 35 of 43 subsystems fail **open** when the gate throws (M5-D06). Genuinely strong: the bootstrap lockout escape hatch (`command_access.py:351-358`, M1-S01), the two-tier typed `setup_access` surface (M1-S03), and hub views re-checking the floor **live per interaction** rather than locking to the invoker (M1-S04) | authority is a property of the **mutation**: 175/175 ops carry `authority_ref`, resolved before any leg (B-S02, `lane-claimed`); but `''` is always valid and means the administrator floor, so a missing declaration is indistinguishable from a deliberate one — 29 of 175 carry it (`sb/spec/authority.py:134-156`, B-D12); and the `AIScope` lattice is never fed from real Discord authority (M10-D3) | **merge ideas** | authority belongs on the operation (next) with `superbot`'s live re-check and bootstrap escape hatch kept, and an empty authority declaration must be a compile error |
| **config** | env reads are ungoverned; no counterpart to next's config checker exists (I-8) | one typed `CONFIG_FIELDS` registry plus an AST fence banning `os.getenv`/`os.environ` outside `sb/kernel/config/` with 2 ledgered allowlist entries; injected positives in both `sb/kernel/` and `sb/domain/` returned EXIT=1 with a per-line message (`tools/check_config_usage.py:17-26`, M8-S03/M10-S1) | **preserve from superbot-next** | a single typed accessor with a firing AST fence is the cheapest structural seam in either repo, and it is one of the few `superbot-next` guards measured firing on an injected positive |
| **DB access** | `try_debit_coins` is a single conditional `UPDATE … WHERE coins >= $3 … RETURNING` with no read-then-write window, reused by 7 service modules (`utils/db/economy.py:39-61`, M6-S3/M3-S1) — **and not universal**: `economy_service.transfer()`, the live `$pay` path, reintroduces the exact race (M6-D2), as do both reward-cooldown gates (M3-D1); the raw-SQL ban has **zero recall** for the multi-line `.execute(\n """…""")` style, reproduced empirically (`scripts/check_architecture.py:270-276`, M6-D1) | store mutators take `conn` as a parameter, so they cannot be called outside a transaction the engine owns (`sb/domain/economy/store.py:138-168`, B-S12); the parallel textual rule ("raw `conn.execute` banned outside `sb/kernel/db`") is enforced by nothing, with 11 files already outside it calling `pool`/`conn` execute (M10-D2, `lane-claimed`) | **merge ideas** | next's `conn`-parameter shape makes the rule structural instead of checked, and superbot's conditional-UPDATE debit primitive is production-proven and must be universal rather than 7-of-8 |
| **migrations** | 104 migrations; the runner raises before executing anything on a duplicate version or malformed filename, serialises concurrent instances with a real Postgres advisory lock, and pairs each migration's transaction with its ledger row (`utils/db/migrations.py:87-92,158-159,178-186`, M6-S1); no checksum or immutability check anywhere (I-8) | 57 migrations with checksum integrity enforced **twice independently** — `tools/check_migrations.py` in CI (sha256 byte-identity + contiguous numbering) and `verify_applied_checksums()` re-hashing every applied migration at boot (`sb/kernel/db/migrations.py:192-198`, M10-S2, `lane-claimed`) | **merge ideas** | superbot's runner discipline plus next's immutability manifest; and the successor needs what neither has — a namespaced per-plugin migration lane, without which cog portability fails for 59 % of the feature classes (I-10) |
| **audit** | a convention: 49 call sites in 27 files (I-18), policed by `check_audit_seam` which is wired `continue-on-error: true` and can never block a merge (`code-quality.yml:234-237`, R6-D03), and which clears 85 of 193 in-scope functions by transitive **function-name** match — `ModerationCog.ban` cleared by the name `ban` (M5-D02, `lane-claimed`); AI configuration mutations are outside the log entirely, 1 of 24 `ai_*` services emitting (M4-D5). The read side is the strength: Discord's own audit-log gateway event mirrored into the log channel with the actor named, for **any** actor including humans in the web client (`cogs/logging_cog.py:249-266`, D-S09) | audit is a property of the engine, not a call authors remember: **one** call site (`emit_central_audit(` → 1 site / 1 file, I-18) writing one row inside the mutation's own transaction (`sb/kernel/workflow/audit.py:94-105`, M9-S03); but there is **no way to read the audit log from Discord** — the only `SELECT` against it in the tree is the engine's own dedup lookup (D-D09), and only 3 of 533 goldens ever assert an audit row exists (F-D02) — both `lane-claimed` | **merge ideas** | take next's engine-owned write spine (1 site against 49) and superbot's operator read surface: a bot that writes 175 operations' audit rows and cannot show one has built half an audit system |
| **outbox** | none | 763 LOC across `enqueue`/`store`/`relay`/`metrics` plus an `event_outbox` table, dedup keys, a relay lane and an in-transaction name guard — serving exactly **one** event: 24 of 25 `KNOWN_EVENTS` are `BEST_EFFORT`, 1 is `AT_LEAST_ONCE` (`sb/kernel/outbox/enqueue.py:43-45`, M9-D06, `lane-claimed`) | **omit** | the design is right and its population is one; build it when a second at-least-once consumer exists, and record the trigger rather than the machinery |

### C · Surface and interaction

| pattern | superbot | superbot-next | VERDICT | why (one line) |
|---|---|---|---|---|
| **panels / views** | 64,872 LOC across 250 files backing 280 View classes ≈ 232 LOC per surface (E-S5, `lane-claimed`); `panel_recovery.restore_parent_or_send_fresh` centralises return-to-parent with explicit branching on `NotFound` vs `Forbidden`, replacing a bare `except Exception: pass` (M6-S7); persistent anchored panels restored across restart (M1-S04) | declarative `PanelSpec`: 23,802 LOC across 41 files backing 314 panels ≈ 76 LOC per surface — a genuine ~3× reduction (E-S5, `lane-claimed`); the escape hatch cannot be taken silently, 218 of 218 overriding panels carry a compiler-forced justification (E-S3) — **but 218 of 314 panels (69 %) take it** (I-18, re-derived), and the required `NO EXPIRY` ratchet that should count them counts a tier-3 marker occurring **0** times in a 2.27 MB snapshot against a baseline of `{"per_subsystem":{},"total":0}` (I-16, I-18) | **preserve from superbot-next** (hatch capped) | the declarative spec is the real per-surface saving; the hatch must be counted with a ceiling and a scan that matches the tree's actual shape — `sb/domain/*/ui/*.py` globs 0 files across 49 directories (I-16) |
| **navigation** | the shared child-discovery seam is **19 for 19**; hand-rolling is **8 for 15**; 27 of 34 declared hub children have a button on their parent hub, and `ModPanelView`'s seven buttons are every one an action and none a route (I-14). Setup is reachable only through an ephemeral out-of-graph launcher message with no route back — `"setup"` is not one of the 43 `SUBSYSTEMS` keys, so the Help dropdown can never list it (I-13) | navigation is injected by the renderer, not by panel authors — one block in `render_panel` appends Help/Home/Back (`sb/kernel/panels/render.py:606-613`, M9-S01), a structural improvement over an opt-in helper. **The graph it decorates was never connected**: 314 panels wired by **200** downward edges where a tree needs ≥313; from `help.*` roots max depth is **zero**; `setup` is 39 of 40 panels unreachable; adding Back/Home up-links raises edges to 278 and reachability by **zero** panels (I-13) | **merge ideas** (graph replaced) | keep next's engine-injected default and superbot's rendered-artifact hub assertion (I-6), and replace the route graph outright — both bots fail the same first-run journey by two different mechanisms |
| **state / session** | `runtime_sessions` enforces one active panel per `(user, channel, subsystem)` with a real Postgres `UNIQUE`, resolves races with a single `INSERT … ON CONFLICT … RETURNING`, and cascades state rows (`migrations/007_runtime_sessions.sql:12-30`, M6-S2); one generic restart-safe `game_state` checkpoint table with the invariant in a DB constraint plus a GC sweep (M3-S3); `scope_locks` per-scope lock manager with a three-path cleanup contract and 11 consumers (`core/runtime/scope_locks.py:5-16`, R6-S08) | `session_lifecycle` on 223 of 314 panels and an invoker lock on 238 of 314 enforced at 2 call sites (D-S05, `lane-claimed`), but the session is gone after a restart and the lock then opens; no DB-backed session identity | **preserve from superbot** | a session invariant held by a database constraint survives the restart that destroys an in-memory one, and `superbot-next` has no equivalent to port |
| **scheduled work** | every background task goes through one managed-task supervisor holding a strong reference, logging with traceback and incrementing an outcome counter (`core/runtime/tasks.py:1-27`), enforced by an AST guard over all 883 files with a count-pinned allowlist — **fired on an injected positive and clean on the control** (A-S03); but deferred timers are in-memory `asyncio.sleep` with no persisted deadline: the raid-lockdown gap is allowlisted with its own caveat (M2-D2/M2-S6) and `!remind` has no DB row at all (M2-D4) | `sb/kernel/scheduler/due_queue.py` makes a timer fire **one scheduler-owned transaction** — deterministic `once()` key (`task_id:fire_epoch`), audited `run_ref`, `mark_fired`/`advance` committing together, *"no crash window in either direction"* (B-S10, `lane-claimed`) | **merge ideas** | superbot's supervisor answers *"did the task survive the process"* and next's due-queue answers *"did the timer survive the restart"*; they are different halves and neither repo has both |

### D · AI

| pattern | superbot | superbot-next | VERDICT | why (one line) |
|---|---|---|---|---|
| **AI gateway** | **the origin.** Provider-neutral, never-raises, eight ordered steps; callers are genuinely provider-independent — 2 of 883 production files import a vendor SDK, both adapters, behind an AST guard whose allowlist is now empty (M4-S1); redaction applied at the single provider boundary and to every tool result re-entering context, via `dataclasses.replace` so a new request field cannot be silently dropped (`core/runtime/ai/gateway.py:253-263`, M4-S7); the tool-loop budget lives once in `providers/base.py:54-62` (M4-S12); four feature flags layer strictly, each defaulting safe (M4-S9) | a port that says so: `sb/kernel/ai/gateway.py:1-6` — *"Ported from shipped `disbot/core/runtime/ai/gateway.py` @7f7628e1"* — and **24 of 30** files in `sb/kernel/ai/` name a `disbot/` source in their first 12 lines (I-4, I-18). Two genuine additions: `socket_guard.deny_sockets()` patching the transport so the eval suite structurally cannot reach the network, absent from `superbot` (0 grep hits) (M10-S4), and a guarded `_observe()` wrapper isolating metrics faults (M10-S5); the "only `providers/` may import LLM SDKs" boundary is enforced by nothing there (M10-D1) | **preserve from superbot** | this is the first attribution reversal: the design, the pipeline order and the provider set are `superbot`'s, and the port's only novel contributions are the socket fence and the metrics guard — take those two with it |
| **AI tool registry** | a closed `CATALOGUE` of **36** tools, 35 read-only and exactly **one** write — `open_support_ticket`, which emits a request so a human clicks the button while the row is written by the audited mutation seam (`disbot/services/ai_tools.py:2416-2427`, I-11/M4-S3). Grounding allowlists are derived from catalogue metadata rather than hand-mirrored (M4-S8). **No per-cog registration hook exists** — `register_tool`/`add_tool`/`ToolProvider` return zero matches repo-wide, so every tool is hardcoded into a central 2,719-line module (M4-D6) | the closed dict replaced by an open registry with `min_scope` authority that can only narrow and derived grounding allowlists — a better abstraction — with **one** `register_tool(` call site in all of `sb/` (`sb/domain/ai/tools.py:185`) registering **8** rows, every one a BTD6 factual read at `AIScope.USER`, **zero write-capable** (I-11); the one audited write seam did not survive the port | **merge ideas** | next's open registry is the cog-portability answer superbot structurally lacks, and superbot's read-only-plus-one-audited-write contract is [the 2026-09-04 AI-authority decision](run/in-flight-direction.md) already shipped — take both, with a committed `FLOOR` on the registry so *the mechanism improved and the population collapsed* is a red diff |
| **AI memory** | ported forward into `sb/kernel/ai/memory.py` along with conversation state (M4-D12's file list); decision audit stores **no raw message content** and rejects an unknown decision string at the seam rather than writing a corrupt row (`services/ai_decision_audit_service.py`, M4-S10) | inherits the same design; the one measured property is a defect of the harness rather than the layer — replay results depend on case **order** because the conversation buffer rides across cases in process memory (R5-D12, `lane-claimed`) | **preserve from superbot** (thin evidence — stated) | the design is superbot's like the rest of the AI kernel, **and this is the row with the least evidence in the matrix**: no lane measured either bot's memory retention or erasure behaviour, so the successor declares it under next's store-lifecycle contract (B-S04) and the product question of how long the bot remembers routes to [`12-owner-decisions.md`](12-owner-decisions.md) OD-F |

### E · Operations and proof

| pattern | superbot | superbot-next | VERDICT | why (one line) |
|---|---|---|---|---|
| **observability** | per-request `uuid4` correlation ids (not a per-process boot id), structured JSON logging, Prometheus command latency/outcome metrics and a slow-path ring buffer, wired through the **real** dispatch path (`disbot/bot1.py:374-419,501-506`, M7-S3); typed failure-mode counters written on every path in `server_logging` and **read back** by an operator-facing diagnostics surface (M7-S5) | a metric-cardinality budget checker with no `superbot` counterpart (I-8) and the gateway's `_observe()` fault isolation (M10-S5); against that, the degrade notice **has no sink** — `record_operator_finding` appends to a module-level `deque(maxlen=256)` and `OperatorAlertSink` has zero consumers outside tests (`sb/kernel/observability/findings.py:45-71`, R4-D02); the FATAL promotion is dead code, since no severity outside `("info","warning","error","critical")` can survive coercion (R4-D08); and 28 operator diagnostic cards are frozen literals of the **old bot's** runtime (R1-D1, `lane-claimed`) | **merge ideas** | superbot's telemetry is wired to the real dispatch path and read back; take it, plus next's cardinality budget — and a finding that reaches no sink is this review's own defect class wearing an observability label |
| **health / readiness** | real liveness/readiness endpoints tied to an explicit lifecycle-phase state machine (`healthserver.py:1-18`, M7-S4); a health-server bind failure is a boot abort with a dedicated webhook and `SystemExit(1)` (R4-S04); the deterministic startup-outcome summary is posted **before** `bot.start()`, so a boot that dies before READY still produces an out-of-band artifact (R4-S03); but `/ready` is gateway-and-phase only, not DB-aware (R4-S08), and `db.init()` runs before any notification channel exists (R4-D06) | readiness is a decision table with a named reason per row and it is DB-aware — RUNNING + DB down → 503 `db_unavailable`, STARTING → 503 `still_starting` (`sb/adapters/http/health.py:85-96`, R4-S08); but readiness flips green **before** the degrade is evaluated (R4-D09), and *"online"* does not mean a reachable command surface: `sb/app/main.py:616` hardcodes `sync_remote(..., enabled=False)`, so this composition root publishes **no slash command at all** while `/ready` answers 200 (I-19) | **merge ideas** | next's reason-per-row DB-aware table plus superbot's pre-connect ops summary and abort-on-bind-failure — and "online" must mean a **counted, named, reachable** command surface asserted against a committed floor at boot (I-19) |
| **deployment** | Railway; the close-driver releases the runtime instance lock **before** the slow drain, with the ~85 s production downtime it fixes named in the comment (M5-S07); SIGTERM and `!restart` both only record intent, one watchdog is the sole executor with a 20 s bounded timeout falling through to `os._exit(1)`, and exit code 42 is documented against a live incident dated 2026-06-10 (M5-S06); the live worker service has **no deploy watch-path filter** in a 4-service monorepo and has already cost ~293 unnecessary restarts, root cause unfixed (M7-D4) | a weekly restore-verify workflow — which **cannot fail**: `restore-verify.yml:124` runs `python3 -m sb.app.verify_boot` **piped into** `tee verify-report.json`, with **0** occurrences of `pipefail` and **0** `shell:` keys across all 8 workflow files, so the step's exit status is `tee`'s (I-19); and `verify_boot` executes 3 of `main.py`'s 18 boot steps, reaching "readiness" by calling the lifecycle setter itself (M8-D02, `lane-claimed`) | **preserve from superbot** | the lifecycle, drain and restart machinery is incident-derived and production-proven; next's weekly restorability proof is the right **idea** and its implementation is this review's subject twice over — a parallel re-implementation, behind a pipe that swallows the exit code |
| **testing** | **the enforcement locus is pytest, not the workflow.** 45 `scripts/check_*.py`; **44** are driven by an asserting test and **15** appear in any workflow — confirmed on three independent instruments, the third an AST pass that cannot be fooled by a comment (23 imported · 21 driven by a path string · 0 comment-only) (I-21). 14 AST write-boundary invariant guards, one mutation domain each (M7-S2); guards fired on injected positives with clean controls (A-S03, A-S04). Against that: zero coverage measurement anywhere in CI or tooling (M7-D2); the sole required check goes green with pytest, ruff, mypy and both strict checkers **skipped** on a docs-only classification (`code-quality.yml:71-77`, A-D01); and the suite cannot even be collected without discord.py — 5,402 collected with 632 errors, EXIT=2 (B-D10) | 3,648 tests pass with neither discord.py nor asyncpg installed (M9-S06/M11-S08) — a real substitutability property; against that, **two required CI legs are green over zero executed tests**: `pytest tests/integration -q` → `14 skipped`, EXIT=0 and `pytest tests/e2e -q` → `11 skipped`, EXIT=0, in the one job provisioned with Postgres precisely so they could not skip (I-16); `run_app`'s 624 lines are never executed, with 9 assertions over `inspect.getsource()` substrings standing in (M8-D03/F-D07, `lane-claimed`) | **merge ideas** | superbot donates the locus — a checker is a library behind a blocking asserting test — and next donates port isolation, a suite that runs without the vendor SDK; and every tier asserts a **collected-count floor**, which is the population contract expressed in the test runner |
| **architectural checks** | **the estate's only working import-direction gate**: `architecture_rules/layers.yaml` declares the allowed directions and `check_architecture.py --mode strict` runs at `code-quality.yml:221-223` with no `continue-on-error`, inside the **sole** required status check on `main` (A-S02, A-S10); measured EXIT=0 with 1 `views→cogs` warning (I-18). Its two holes: 55 `known_violations` with no stale-entry detection (R6-D05, `lane-claimed`), and lazy imports invisible by default — CI never passes `--report-lazy-imports`, which raises findings from 1 to 137 (R3-D2, `lane-claimed`; the strict figure of 1 is re-derived, I-18) | **27** `tools/check_*.py`, all enumerated and read by their own docstrings, and **none** is an import-direction or layer guard; there is no `tests/architecture/` directory, and the required job is literally named `architecture` (I-3, I-8). Lane counts of this fleet range 24–35 (M11-D11, R3-D9, R2 — all `lane-claimed`); 27 is the session's. What it *does* own is a checker set with **no superbot counterpart at all**: config seam, migration checksums, namespace and symbol shadowing, egress fence, money-race and settle-once, data/credential lifecycle and rotation, cost posture, metric cardinality, the slash budget, schema growth, resolving doc citations (I-8) — while three flagship required `NO EXPIRY` gates are green over empty populations (I-16, I-21) | **merge ideas** | the second attribution reversal: `superbot` donates the **guard architecture** and the import-direction gate, `superbot-next` donates the **invariant checker set** — the two repos hold different halves of one discipline and neither has both |
| **agent / repo navigation** | `docs/AGENT_ORIENTATION.md`, created **2026-05-24** — six weeks before the EAP — carrying the tier vocabulary this estate's own boot file descends from (I-9); 855 of 863 docs carry a valid machine-readable Status badge and the badge layer is gated on every PR, with 176 files (39,605 lines) already badged `historical`/`archive` and exempted by the gate itself (A-S06/A-D05, `lane-claimed`); against that, the orientation doc misstates its own `docs/` count by ~8.6× and the checker built for that class cannot see the instance (M7-D3), and `docs/planning` is 292 files in one flat directory (A-D04) | 92 docs (R6-D10, `lane-claimed`); `check_doc_cites` verifies that `file:line` citations in tracked markdown actually resolve — a mechanism `superbot` has no counterpart for (I-8); against that, `sb/manifest/__init__.py`'s docstring tells the first reader the package is *empty* while it holds 49 modules and 5,545 LOC (M9-D12) | **merge ideas** | superbot's badge taxonomy and tiered orientation doc are the owner's own named quality baseline (I-9), next's resolving-citation checker is the mechanism that keeps a router honest — and every count a router states carries a staleness assertion, which is the same rule as § E's floor |

---

## 2 · The rows the corrections move

### 2.1 · The attribution reversals — three rows point at `superbot`

The 2026-08-21 plan's operative recommendation is *"use `superbot-next` as an
architecture and kernel-pattern donor."* Three of the patterns above reverse it,
and all three are measured rather than argued:

| the prior plan's claim | what is measured | matrix row |
|---|---|---|
| "Preserve from `superbot-next`: explicit layers **and import-direction guards**" | `superbot-next` has the property and **no mechanism**: 0 module-level `sb.kernel → sb.domain` imports against 234 the other way, and none of its 27 checkers guards import direction (I-3). `superbot` has `layers.yaml` + `check_architecture --mode strict` inside its required check (I-3, A-S10) | **architectural checks** |
| "Preserve from `superbot-next`: provider-neutral AI contracts and adapters behind one gateway" | `sb/kernel/ai/gateway.py:1-6` says it is a port of `disbot/core/runtime/ai/gateway.py`; 24 of 30 files in `sb/kernel/ai/` name a `disbot/` source in their first 12 lines (I-4, I-18) | **AI gateway** |
| `superbot-next` as the disciplined-verification repo | `superbot`'s enforcement locus is pytest — 44 of 45 checkers driven by asserting tests against 15 in workflows, on three instruments (I-21) — while three of next's required `NO EXPIRY` gates are green over empty populations (I-16) | **testing** |

**Why this is operative and not pedantic.** An implementer told to read
`superbot-next` for the layer guard will find a folder shape and no guard, and
will conclude the guard was not needed. The reading that survives measurement is
sharper: **the two repos donate different halves of one discipline** — `superbot`
guards the *rendered product* (reachability, actionability, back-button, hub
coverage, size ceiling), `superbot-next` guards the *invariants of the system*
(config seam, migration checksums, namespace, egress, lifecycle, cost,
cardinality, slash budget). That is why seven rows above are **merge ideas** and
why merging is a design requirement rather than a compromise.

### 2.2 · One lane disagreement left open, because the verdict does not turn on it

`superbot`'s navigation injection is reported two ways and both are
`lane-claimed`: E-S1 measures a **base-class constructor** reaching 217 of 280
View descendants (77.5 %) by transitive base closure; R6-S07 describes
`attach_standard_nav` as an **opt-in helper with 17 call sites across 9 files**.
This session re-derived neither. They may both be true of different mechanisms in
the same repo, or one may be wrong.

**It is recorded rather than resolved because no verdict depends on it.** Both
lanes agree `superbot-next` made injected navigation structural rather than
optional, and the navigation row takes it from `superbot-next` on that ground.
Anyone who needs the number should measure it before quoting it.

Two smaller spreads in the same class: `superbot-next`'s declared config-field
count is reported as **38** (M8-S03), **44** (M10-S1) and **53** (B-S09) by three
lanes, none re-derived here — the *mechanism* is what the config row preserves,
not the count; and its checker fleet is counted as 24, 27, 28, 34 and 35 across
lanes, against **27** enumerated by this session (I-3, I-8).

### 2.3 · The DAG artifact — what the successor's import guard must do

I-22 corrects this session's own earlier finding, and it is the sharpest
constraint the matrix produces:

```
cross-subsystem sb.domain imports: 296
  module-level  :  28  ( 9.5 %)
  FUNCTION-BODY : 268  (90.5 %)
mutual subsystem pairs — union graph: 8   |   module-level only: 0
```

Nine of every ten cross-subsystem edges are inside function bodies, and **every
cycle is there**. At module level the graph is acyclic — which is exactly the
number both this session's first pass and lane M8 published, because a
module-level census cannot see anywhere else.

Three consequences, and the third is the buildable one:

1. **The clean layer DAG is a property of the measurement, not of the design.**
   Moving an import into a function body removes it from the census and changes
   nothing about the coupling.
2. **The comparison inverts on actual coupling.** `superbot` is acyclic in both
   its 59-cog layer and its 190-module services layer (0 cycles over 148 edges,
   E-S6, `lane-claimed`) — the three-years-later bot is cleaner than its
   ground-up replacement on the one graph property that decides whether a module
   can be lifted out.
3. **A layer rule that sees only module-level imports has a documented bypass and
   both repos took it.** `superbot`'s own checker knows this — it ships
   `--report-lazy-imports`, raising findings from 1 to 137 — **and CI never
   passes the flag** (R3-D2, `lane-claimed`; the strict-mode 1 is re-derived,
   I-18).

**So the successor's import guard walks the whole AST, counts a function-body
import as a real edge, and fails on cycles.** Anything less means *"clean
architecture"* is a synonym for *"we moved the imports."* This is a hard
requirement on the **architectural checks** and **services** rows, and it is the
reason **services** is the matrix's only `replace both`.

### 2.4 · Cog portability — the requirement neither repo meets, and the proof it is achievable

OD-19 is a constraint, not a preference: *"I should be able to add exiting cogs
to it on demand, or be able to slightly alter an existing cog so that it works
with this bot."* Four measurements bound the design space:

- **`superbot-next`'s plugin contract cannot host 29 of its own 49 subsystems**
  (I-10). `HOST_ONLY_FACETS = (stores, data_invariants, wizard_sections)` fences
  out every stateful feature — economy, moderation, roles, setup, xp, settings,
  ticket, starboard, btd6, mining, fishing. The eligible 20 are the stateless
  ones. The docstring names the reason: migrations and the setup registry *"have
  no out-of-tree lane yet."*
- **`superbot`'s modularity is coarser but broader** — any cog, data-owning or
  not, can be dropped from `INITIAL_EXTENSIONS` or `!cog unload`-ed, because it
  is in-tree (I-10, R3-S1/S2). Its cost is the shared floor: the intersection of
  all 58 non-trivial cog closures is 148 modules / 30,925 LOC spanning seven
  top-level packages (A-S08/A-D03, `lane-claimed`).
- **Portability has already happened, 54 times.** 54 `disbot`↔`sb` file pairs
  score above 0.55 similarity, 8 at ≥0.90, and one is **byte-identical** —
  `disbot/utils/mining/capacity.py` and `sb/domain/mining/capacity.py` share md5
  `64f1665a9fb83a940d95eca5b9492bf2`, verified by this session (I-21). A domain
  module already moved between these two architectures unchanged.
- **The one gate behind the requirement returns `[]` when its population is
  absent** — `plugin_boot_problems` is verbatim commented *"nothing to prove"*
  when no exemplar is present in the checkout, and nothing outside that function
  asserts the exemplars exist (F-D08, `lane-claimed`; the same shape R2/I-16
  measured in `check_escape_hatches`).

**The hard requirement this puts on the plugins, migrations and manifests rows:**
an out-of-tree module must be able to **own data** — ship its own migrations into
a namespaced schema, declare its invariants, and contribute a setup section — and
the gate proving it must assert its exemplar population against a floor rather
than passing when the population is missing.

### 2.5 · The population defect, applied as a matrix rule

Several patterns above would score differently if their gates were taken at face
value. They are not, and the rule is uniform:

> **A pattern is dispositioned on what it does, never on what its gate reports.**

Applied, in this file, to five rows:

| row | the green report | the population |
|---|---|---|
| panels / views | `check_escape_hatches` → `clean`, EXIT=0, required, `NO EXPIRY` | counts a tier-3 `"view:` marker occurring **0** times in the snapshot; its `sb/domain/*/ui/*.py` sweep globs **0** files across 49 directories (I-16) |
| navigation | the navigation-completeness golden asserts `report.ok` | an inventory its own `autouse` conftest clears before **and** after every test in the directory (`tests/unit/navigation_golden/conftest.py:16-25` → `clear_panels_for_tests`, which is `_PANELS.clear(); _STATIC_TABLE.clear(); _HUBS.clear()` at `sb/kernel/panels/registry.py:177-180`), **and** a root set empty even in a booted process — `register_hub` has exactly one occurrence in all of `sb/`, its own definition at `registry.py:88`, against 3 in `tests/` (I-2, I-16; re-confirmed at the pin while writing this file) |
| testing | two required CI legs pass | `14 skipped` and `11 skipped`, EXIT=0 (I-16) |
| architectural checks | `check_verified_live` → `OK — 50 subsystems (0 verified), 0 records` | `records: []` — the V1/V2/V3 loops have never iterated (I-21) |
| deployment | the weekly restorability workflow is green | a pipe into `tee` with no `pipefail` — the step's status is `tee`'s (I-19) |

And the counterweight, because a matrix that only indicts is not usable: **the
same two repositories already built eleven working anti-vacuity mechanisms** —
the denominator assert, the live-population negative control, the shrink-only
ratchet with a staleness proof, excuse-row expiry, the guard that guards the
guards, plus `db_delta` effect capture, composition-root reachability boot, the
single-entry-seam fence, the frozen compat pin, GAP-on-unmodeled-effect and
symmetric dispositions. Every one stayed in the file where it was born.
[`08-verification.md`](08-verification.md) §§ 3 and 3b carry them and are the
authority; this matrix simply refuses to credit a pattern for a gate that is one
of the counterexamples.

---

## 3 · Adjacent patterns this matrix does not own

Recorded so they do not vanish between files:

- **The invocation surface** (prefix vs slash) is the single highest-leverage
  product decision the evidence surfaces and it is not an engineering-pattern
  row: `superbot-next` compiles 413 commands of which **386 are prefix-only** and
  27 are reachable by slash (C-D01, `lane-claimed`), and `superbot` is 243 prefix
  commands against 30 app commands with zero hybrids (D-D08, `lane-claimed`).
  Both bots are prefix-first in a slash-first Discord, and `superbot` already
  shipped the escape once — `cogs/btd6/_unified.py` collapses five prefix groups
  into one `/btd6` tree budgeted against Discord's caps (C-S05). It belongs to
  [`05-product-definition.md`](05-product-definition.md) and
  [`06-architecture.md`](06-architecture.md).
- **The acceptance oracle** — byte parity, its harness and its six reusable
  primitives — is [`08-verification.md`](08-verification.md) § 3b, including the
  finding that the oracle never runs the shipping renderer.
- **Content mass** (BTD6 at 36,410 LOC, `ux_lab` at ~5,016) is a product scope
  question with an owner fork, not an architecture verdict (A-D02, M3-D7 — both
  `lane-claimed`); it belongs to [`02-product-matrix.md`](02-product-matrix.md)
  and OD-D.

## 4 · What this matrix routes to the owner

Nothing in §§ 1–2 is an owner question — every row is settled by measurement, and
`docs/intent.md` § 6 makes a reversible implementation choice *"decide and flag"*
rather than owner homework. Two threads touch existing rows in
[`12-owner-decisions.md`](12-owner-decisions.md) and are named here so the
dependency is visible rather than implied:

- **OD-D (which features are core)** determines how hard the **plugins**,
  **migrations** and **manifests** rows are loaded. If the middle set (`xp`,
  `karma`, `leaderboard`, `counting`, `starboard`, `ticket`, …) is optional
  rather than core, the data-owning plugin lane in § 2.4 carries the whole
  product, not an edge case — which is the argument for building it in slice one.
- **OD-F (how much authority the AI holds)** determines whether the **AI tool
  registry** row ships superbot's one-audited-write contract as the permanent
  ceiling or as a starting point. The registry shape is the same either way; the
  floor on write-capable tools is not.

**One thing the evidence cannot settle and this file will not invent:** how long
the successor's AI remembers a conversation, and what a member may ask it to
forget. No lane measured either bot's memory retention or erasure behaviour, and
the **AI memory** row says so in its own cell rather than in a footnote. The
*mechanism* is settled — it is declared under `superbot-next`'s per-store
retention and erasure contract (B-S04, `lane-claimed`: 81 registered stores, 52
carrying member data, all 52 with both a retention and an erasure reference) —
and the *policy* is OD-F's neighbour, not a derivable fact.
