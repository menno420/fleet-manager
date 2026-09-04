# The migration and disposition manifest

> **Status:** `plan` — authoritative for **what moves out of `superbot` and
> `superbot-next` into the successor, in what form, who owns it there, how the
> move is proved, and in which slice it lands** — and for **the disposition of
> every class of production data**. It is authoritative for nothing else: what
> the product contains is [`02-product-matrix.md`](02-product-matrix.md), which
> repo a pattern is taken from is
> [`03-architecture-matrix.md`](03-architecture-matrix.md), how the successor is
> arranged is [`06-architecture.md`](06-architecture.md), and what proves a slice
> is [`08-verification.md`](08-verification.md). Where a row here and one of those
> disagree, **they win on their own subject and this file is the defect.**
>
> **It authorises nothing.** No repository is created, no code is copied, no
> database is read or written. The live Postgres behind `superbot` is a
> **protected surface and was not read by this review** — every data claim below
> is derived from committed migrations and source, never from production rows.

---

## 0 · How to read this, and the one rule that governs it

### 0.1 · The rule: never default to copying an implementation

A capability moves as a **contract** — the behaviour, the tier, the typed seam —
re-derived against the successor's ports. The implementation is carried only
where a measurement says the artifact itself is transferable. Three measurements
draw that boundary, and they draw it in both directions:

- **Copying is right where the module is pure logic.** The one byte-identical
  `disbot`↔`sb` pair is `disbot/utils/mining/capacity.py` ↔
  `sb/domain/mining/capacity.py`, md5 `64f1665a9fb83a940d95eca5b9492bf2`, 137
  lines — **re-verified here** (**`§10 measured`**), and it is the file class
  [`06-architecture.md`](06-architecture.md) § 1 calls `logic.py`: no framework
  import, no Discord, no DB. The 54 pairs above 0.55 similarity and 8 at ≥ 0.90
  are R6's and stay **`lane-claimed`** (via I-21).
- **Copying is wrong where the artifact encodes its old venue.** I-5 measured the
  capture-world vocabulary — `capture world`, `shipped verbatim`, `golden-pinned`,
  `goldens pin`, `pinned literal` — in **116 of 382 `sb/domain` files (30 %)**.
  Copying `sb/domain/*` carries the transcription habit into a repository whose
  whole premise is that the habit is the defect.
- **And a port can keep the mechanism while losing the contract.** I-11 is the
  measured case: `superbot`'s closed catalogue of **36** AI tools with exactly one
  audited write became an *open, better-designed* registry holding **8 read-only
  rows from one call site** (`sb/domain/ai/tools.py:185`). Nothing was copied
  badly. The contract simply was not part of what moved.

So **every row's deliverable is a contract plus its committed floor**, never a
file. A row that cannot state its floor has not been migrated; it has been
mentioned.

### 0.2 · The approach vocabulary

| token | means | when it is allowed |
|---|---|---|
| `LIFT-VERBATIM` | the mechanism's code shape is carried essentially as-is | **only** for § 4's list: stdlib-only, framework-agnostic, no product knowledge — and each still carries a mandatory repoint |
| `PORT-LOGIC` | pure functions carried unchanged; everything around them re-derived | the source has a `logic.py`-shaped core with no framework, Discord or DB import |
| `PORT-CONTRACT` | the interface / tier / typed seam is re-implemented against the successor's ports; the old implementation is **read**, not copied | the default for anything with a proven behaviour |
| `RE-DERIVE` | the behaviour is rebuilt from the feature declaration; the old code is a spec source only | the old shape is the defect, or the capability does not exist yet |
| `DECLARE-ONLY` | nothing is ported: the capability becomes rows in `manifest.py` and every registry is generated from them | anything that is today a hand-maintained second copy |
| `DROP` | not carried; the reason is in § 5 | measured dead code, or a capability OD-16/OD-D excludes |

`LIFT-VERBATIM` appears **eleven times in this document and nowhere else**. If a
future session finds itself reaching for a twelfth, that is the signal to stop
and read § 0.1 again.

### 0.3 · The other columns

- **New owner** names a seam from [`06-architecture.md`](06-architecture.md) — the
  four rings `app/` · `core/` · `adapters/` · `modules/<name>` — not a file. `06`
  is authoritative for the final names.
- **Verification** names the proof layer from
  [`08-verification.md`](08-verification.md) § 3c **and its population and
  floor**, because a layer without a population is the defect this package is
  about ([`04-root-cause.md`](04-root-cause.md) § 2.4).
- **Phase** keys to [`09-roadmap.md`](09-roadmap.md)'s stable slice ids `S1`…`S6`.
- **Evidence.** A figure this session re-derived against the pinned clones is
  stated bare with its `I-` id from
  [`run/independent-findings.md`](run/independent-findings.md). A figure carried
  from a review lane without re-derivation is marked **`lane-claimed`** inline, at
  the number, with its row id from
  [`run/evidence-digest.md`](run/evidence-digest.md). Measurements made **while
  writing this file** are marked **`§10 measured`** and carry their command in
  § 10.

---

## 1 · Product capability migrations — Group A · access, orientation and operation (S1)

| # | capability | old source (read at the pin) | contract to preserve | new owner | approach | verification (layer · POP · FLOOR) | phase |
|---|---|---|---|---|---|---|---|
| A1 | **Lockout escape hatch** | `superbot` `disbot/core/runtime/command_access.py:351-358` — `is_bootstrap_command(...) and (ctx.is_guild_operator or ctx.is_bot_owner)` returns `BOOTSTRAP_BYPASS` **before** the per-guild policy row is read (read at the pin; M1-S01's 6 consumers `lane-claimed`) | no per-guild policy can lock the owner or a guild operator out of the bootstrap set, and the bypass is resolved in **one** place, before policy | `core/governance` | `PORT-CONTRACT` — **with one change**: the bootstrap set is *derived from the route graph* (routes flagged `bootstrap`), not a hand list. M1-D05 (`lane-claimed`) measured the Server Management hub absent from the bypass on both surfaces, which is what a hand list produces | contract (3) · POP = every bootstrap-flagged route × every policy mode · FLOOR = both counts non-empty · negative control: a deny-everything policy must still admit the set | S1 |
| A2 | **Two-tier setup permission** | `superbot` `disbot/services/setup_access.py` — `is_setup_admin` (`:61`) and `can_view_setup` (`:84`) may view, `can_run_readiness` (`:92`), `can_apply_setup` (`:105`) may write (function map read at the pin; M1-S03 `lane-claimed`) | view and apply are different tiers resolved in one typed surface, never per-surface | `core/ops` — the tier lives on the operation's `authority_ref` | `PORT-CONTRACT` | contract (3) + journey (4) · POP = every surface routing to the op · FLOOR = that count · negative control: each tier below must refuse | S1 |
| A3 | **First-run entry with named fallbacks** | `superbot` `disbot/cogs/setup_cog.py:613-641` — `on_guild_join` creates a private setup channel, posts the launcher with an owner ping, degrades to safest channel then DM (D-S06, `lane-claimed`) | first run reaches the owner through a **named** fallback chain ending in a DM; every fallback is stated, none is silent | `modules/setup` + `adapters/discord` | `RE-DERIVE` — the behaviour is kept and the launcher stops being the **only** door. I-13: `superbot` reaches setup only through this ephemeral out-of-graph message, and `_repost_launcher` is the tell | journey (4) · POP = the first-run path · FLOOR = 1 · the R4 drive deletes the message and reaches setup from the root | S1 |
| A4 | **Wizard resume / recovery** | `superbot` `disbot/views/setup/recovery.py` — 4-field structured embed (What happened / Why / Recommended / If skipped) + Continue / Retry / Skip (M1-S07, `lane-claimed`) | an abandoned wizard resumes with a stated reason, and every mutating button re-checks authority against a fresh snapshot | `modules/setup` | `PORT-CONTRACT` | journey (4) · POP = the wizard's sections · FLOOR = its own size · the R4 drive abandons and resumes once | S1 |
| A5 | **Live authority re-check on persistent panels** | `superbot` `ServerManagementHubView` re-evaluates the administrator floor **live on every interaction** rather than binding the panel to its invoker (M1-S04, `lane-claimed`) | a persistent panel is never bound to its invoker; authority is resolved per interaction | `core/ops` + `adapters/discord` | `PORT-CONTRACT` | contract (3) · POP = every persistent component id · FLOOR = the mint table's size | S1 |
| A6 | **Settings declared once, rendered with no UI code** | **merge**: `superbot`'s `SubsystemSchema`, 19 consumers (R3-S3, `lane-claimed`) + `superbot-next`'s activation grammar `sb/spec/settings.py:63-69` — `ON_BY_DEFAULT` / `ON_WHEN_BOUND` / `ON_WHEN_KEYED` / `OFF_UNTIL_OPT_IN`, grammar enforced at `:306-321` (read at the pin) | a setting is declared once and renders itself; a bool **must** declare an activation; anything with `external_side_effects` is forced to `OFF_UNTIL_OPT_IN` — a privacy policy expressed as grammar that cannot compile if forgotten | `core/settings` | `DECLARE-ONLY` | contract (3) · POP = every declared setting · FLOOR = its own size · **plus**: every activation state is asserted against the wiring it depends on — the measured failure is `superbot-next`'s `welcome` greeting reading ✅ with no `on_member_join` listener anywhere in `sb/` (05 § 5) | S1 |
| A7 | **Hub child rendering by construction** | `superbot` `disbot/views/hub_children.py` — the one discovery seam, an unfiltered comprehension over `SUBSYSTEMS` filtered on `parent_hub`, plus `HubChildButton` (read at the pin; I-14: the seam is **19 for 19**, hand-rolling **8 for 15**) | every declared child the viewer is permitted to see renders — a property of the framework, not of the hub author | `core/route-graph` — children are edges; there is no hub author | `RE-DERIVE` | reachability (5) over the **rendered** view · POP = the composition root's route graph · FLOOR = routes ≥ committed floor · the gate models per-guild visibility (I-14) or it scores a correctly-hidden module as an orphan | S1 |
| A8 | **Framework-injected Back / Home / Help** | `superbot-next` `sb/kernel/panels/render.py:606-613` — one render block injects the nav frame (M9-S01, `lane-claimed`) | nav affordances are injected by the engine, never authored per panel | `adapters/discord` renderer | `PORT-CONTRACT` | rendering stability (demoted, 08 § 0) + reachability (5) · **and the caveat**: I-13 measured that up-links add 78 edges and **zero** reachability, so this is a usability contract, never a reachability one | S1 |
| A9 | **`custom_id` collision fence** | `superbot-next` `sb/kernel/panels/registry.py:79-87` — `_mint` raises `PanelCompileError("custom_id_collision")` when a `custom_id` is rebound to a different binding (read at the pin) | component identity is minted once, centrally, and a collision raises at **compile** time | `core/mint` | `LIFT-VERBATIM` (§ 4 · row 12 is not this — see § 4's note on scope) → in practice `PORT-CONTRACT`, since the mint table is the successor's own | contract (3) · POP = every minted id · FLOOR = its own size · negative control: mint a duplicate, the fence must raise | S1 |
| A10 | **Typed config with an `os.getenv` fence** | `superbot-next` `CONFIG_FIELDS` + `tools/check_config_usage.py` — one typed accessor, no ambient env read outside `sb/kernel/config/` (I-8; `superbot` has no counterpart) | there is exactly one place a process value enters the program | `core/config` | `PORT-CONTRACT` | structural (1) · POP = every module in the shipped package · FLOOR = module count == profile · whole-AST including function bodies and `importlib` by name | S1 |
| A11 | **A refusal names its reason, twice** | `superbot` — both admission gates surface the resolver's own user-facing reason before returning False and log a structured deny line carrying guild / channel / user / command / reason / source / mode (M1-S08, `lane-claimed`) | a denial is legible to the person **and** to the operator reading logs | `core/ops` + observability | `PORT-CONTRACT` | journey (4) · POP = every authority tier below the op's · FLOOR = that count | S1 |
| A12 | **No silent resource creation** | `superbot` `tests/unit/invariants/test_no_silent_auto_create.py` — AST scan of all 883 production files under `disbot/` for `guild.create_text_channel` / `create_role` outside the declared provisioning path (M1-S02, `lane-claimed`) | the bot never creates a Discord resource except inside a declared, audited provisioning operation | `core/checks` | `LIFT-VERBATIM` (§ 4 family — same shape, new population) | structural (1) · POP = every module in the shipped package · FLOOR = that count | S1 |
| A13 | **Boot-time profile selection** | **merge**: `superbot`'s `INITIAL_EXTENSIONS`, 59 entries each in its own `try/except` with the subsystem demoted rather than the process crashed (R3-S1, `lane-claimed`) vs `superbot-next`'s unconditional `pkgutil` import of all 49 manifests with no subset lever (R3-D7, `lane-claimed`) | *which modules exist in this deployment* is a named profile, and one bad module degrades itself, not the boot | `app/` boot step 1 | `PORT-CONTRACT` from `superbot`, discovery from `superbot-next` | boot step 8's surface floor — isolation without a floor is how a bot of broken modules reports healthy (06 § 4.3) | S1 mechanism · S6 second profile |

---

## 2 · Group B · the extension boundary and data-owning modules (S2)

| # | capability | old source | contract to preserve | new owner | approach | verification | phase |
|---|---|---|---|---|---|---|---|
| B1 | **Out-of-tree discovery, hash-pinned** | `superbot-next` `sb/app/plugin_host.py` — `sb.plugins` entry points, `plugins.lock.json`, one joint compile pass with in-tree manifests; pinning fires both ways, zeroing a hash and deleting a pin each EXIT=1 (M8-S07, `lane-claimed`) | an installed distribution is discovered, hash-pinned and compiled in the **same pass** as in-tree modules | `app/` loader | `PORT-CONTRACT`, **fence removed** — `ALLOWED_FACETS` / `HOST_ONLY_FACETS` at `:78-83` (read at the pin) makes 29 of its own 49 subsystems ineligible (I-10) | portability gate · POP = **all** modules, in-tree included · FLOOR = all · negative control: a module needing a host-side edit fails the gate | S2 |
| B2 | **Migration immutability + checksum manifest** | `superbot-next` `tools/check_migrations.py:4-16` (read at the pin) + `migrations/checksums.json`; **57 `.sql` files plus the manifest** (**`§10 measured`**) | an applied migration file is byte-frozen; CI and boot both verify the same manifest | `core/db`, **per module** | `PORT-CONTRACT` with **contiguity re-scoped**: the checker requires versions *"unique AND contiguous from 0001"* across one global directory, which is the exact structural cause of the facet fence (06 § 4.1). Immutability + checksums migrate; global contiguity does not | migration gate · POP = every module's ladder · FLOOR = its own length · negative control: a cross-schema DDL statement in a module migration is rejected **before it runs** | S2 |
| B3 | **A ladder that refuses to start** | `superbot` migration runner — raises `MigrationError` before executing anything on a duplicate leading version or a malformed filename, and serialises concurrent instances on a real Postgres advisory lock (M6-S1, `lane-claimed`) | a malformed ladder is a pre-execution abort, and two instances cannot apply concurrently | `core/db` | `PORT-CONTRACT` | boot gate · POP = every migration file · FLOOR = its own count | S2 |
| B4 | **Erasure as a structural walk** | `superbot-next` `sb/kernel/privacy/erasure.py:1-25` — *"Completeness is STRUCTURAL, not audited by inspection"*, enumerating the registered `StoreSpec` inventory filtered on `data_class != NONE` (read at the pin) | the walk enumerates the registry; a new store is covered with **no edit** to the walk | `core/store-registry` | `PORT-CONTRACT` **plus the missing assertion** — B-D01 (`lane-claimed`) reports 52 stores declared, **0 of 48** `erasure_ref` names registered as op keys and 6 not resolving at all. *This session could not re-derive those figures*: a literal-only scan finds **75** `register_store(` call sites in `sb/` and **1** distinct `erasure_ref` string literal, so the instrument does not resolve the constructor's shape and B-D01 stays `lane-claimed` and unverified (**`§10 measured`**, per I-18's rule that an unvalidated instrument is not a re-derivation) | erasure gate · POP = the store registry · FLOOR = its own size · assertion: **every `erasure_ref` resolves to a registered operation** | S2 |
| B5 | **Teardown that keeps the forensic trail** | `superbot` `disbot/guild_lifecycle.py` — live bindings dropped, `binding_audit_log` retained (M1-S06, `lane-claimed`) | leaving a guild purges live state and **retains** the audit trail, by declaration | `core/store-registry` | `RE-DERIVE` from the registry — the measured reason: `disbot/guild_lifecycle.py` defines **31** `_teardown_*` helpers against **74 of 90** matched `CREATE TABLE` statements carrying a `guild_id` column (**`§10 measured`**; this reconciles two conflicting lane figures — see § 10), and `setup_draft_operations` (created at `disbot/migrations/035_setup_draft_operations.sql:78`, indexed on `(guild_id, seq)` at `:134`) is named **0 times** in that file, so staged wizard drafts survive a guild leaving and are re-read on re-invite (M1-D01 reproduces, **`§10 measured`**) | teardown gate · POP = every guild-scoped store in the registry · FLOOR = its own size · negative control: add a fourth table without declaring it; the completeness assert must red | S2 |
| B6 | **`data_class` / retention / `erasure_ref` per store** | `superbot-next` store specs + `check_data_lifecycle` (I-8) | no member-data store can exist outside the erasure walk, because a store without the three fields does not compile | `core/store-registry` | `DECLARE-ONLY` | structural (1) · POP = every declared store · FLOOR = its own size | S2 |
| B7 | **The cog → module port itself** | `superbot`'s cog layer generally; the worked case is `starboard` — a live cog with 3 tables, 2 migrations and its own config panel that is **absent from `SUBSYSTEMS` entirely** (R3-D1, `lane-claimed`) | OD-19's *"slightly alter an existing cog"*, made concrete: [`06-architecture.md`](06-architecture.md) § 4.4's eight steps, of which **1, 2, 3, 5, 6 and 8 are mechanical, step 4 is the port, and step 7 is an improvement the old cog never had** | `modules/<name>` | `PORT-LOGIC` for the pure core; `PORT-CONTRACT` for everything else. **Not cheap, stated so nobody plans around a fiction:** a cog importing another cog at module level — **128** such statements across 51 files (I-17) — must have that edge resolved first | `check_module_portability` · POP = all modules · FLOOR = all · plus the module's own journey at R4 | S2 |
| B8 | **A module owns its schema** | neither — `CREATE SCHEMA` appears **0 times** across `superbot-next`'s 57 migrations and `superbot`'s 104, and **0** `.sql` file in either mentions `search_path` (**`§10 measured`**; the only `search_path` hit in either tree is `tools/manifest_compile.py:267-268`, a Python `__path__` variable, not a Postgres one) | an out-of-tree module ships migrations into `mod_<name>` with `search_path` set by the host — the decision that dissolves the facet fence | `core/db` + `modules/<name>` | `RE-DERIVE` (new on both sides) | migration gate + effect (6) · the module's op changes **its own** tables and no others, asserted as a row-level diff | S2 |

---

## 3 · Group C · the mutation spine (S3), the AI (S4), operations (S5), scope (S6)

### 3.1 · S3 — the mutation spine and the record a human can read

| # | capability | old source | contract to preserve | new owner | approach | verification | phase |
|---|---|---|---|---|---|---|---|
| C1 | **The typed operation** | `superbot-next` `sb/kernel/workflow/spec.py:121-131` — the *"required (no default)"* block of `CompoundOpSpec`: `op_key`, `domain`, `lane`, `authority_ref`, `legs`, `idempotency`, `dedup_key`, `audit_verb` (read at the pin) | every mutation is a declared operation naming its authority tier and its audit verb, **with no default** | `core/ops` | `PORT-CONTRACT`, **grammar cut** — 06 § 13 cut the unused half on measurement: `ConfirmationSpec` carried by 0 of 175 ops, 0 irreversible legs of 185, `DURABLE_ONCE` on 0 of 175 (all `lane-claimed`) | effect (6) · POP = every registered op · FLOOR = its own size · AST gate: every `store.py` function takes a `conn` the engine owns | S3 |
| C2 | **One audit writer, inside the transaction** | `superbot-next`'s central spine — **1 call site / 1 file** — against `superbot`'s **49 sites / 27 files** (I-18, re-derived; the lane said 28 files) | the audit row and the state change commit together or neither happens | `core/audit` | `PORT-CONTRACT` from `superbot-next` (the *mechanism*), with `superbot`'s coverage as the floor | effect (6) · negative control: suppress the audit write, the test must red | S3 |
| C3 | **The case record and its read surface** | **neither.** `superbot-next` writes an audit row for every one of its 175 ops and the only `SELECT` against `audit_log` in the tree is the workflow engine's dedup lookup (D-D09, `lane-claimed`) | a human can read back, in Discord, what happened, who did it and why — at 02:00, from the root route | `core/audit` + `modules/moderation` | `RE-DERIVE` (new) | journey (4) · POP = cases created by the test · FLOOR = 1 · rendered by the **shipping** renderer, never a twin (08 § 3b) | S3 |
| C4 | **Audit-log mirror of every administrative action** | `superbot` — subscribes `on_audit_log_entry_create` and mirrors **every** administrative action by **any** actor, humans in the web client and other bots included, actor named (02 § A, `lane-claimed`) | actions taken outside the bot are still visible, with the actor named | `modules/logging` | `PORT-CONTRACT` | journey (4) + effect (6) · POP = the mirrored event kinds · FLOOR = that count | S3 |
| C5 | **Moderation DM to the moderated member** | `superbot`'s moderation service — DM names action, server and reason, templated with plain token replacement, with explicit failure handling (02 § C, `lane-claimed`) | the person affected is told what happened and why; a failed DM is recorded, never swallowed | `modules/moderation` | `PORT-CONTRACT` | journey (4) · POP = every moderation op · FLOOR = its own size | S3 |
| C6 | **Severity-routed logging with a fallback chain** | `superbot` `resolve_log_channel` — own binding → mod-log fallback for debug/info/warning/error/audit, tested end-to-end against the **real** function with only the DB binding layer mocked (M2-S3, `lane-claimed`, 11 consumers) | a log line always lands somewhere, deterministically | `modules/logging` | `PORT-LOGIC` (the resolution is pure) | contract (3) · POP = every severity × binding state · FLOOR = that product | S3 |
| C7 | **Typed failure-mode counters an operator can read** | `superbot` — typed counters written on every code path in the server-logging service, surfaced to an operator (M7-S5, `lane-claimed`) | every failure path increments a typed counter that a human can read **in Discord** | observability | `PORT-CONTRACT` + a metric-cardinality budget (I-8) | operational · POP = every declared failure mode · FLOOR = its own size | S3 |
| C8 | **The conditional-write primitive** | `superbot` `disbot/utils/db/economy.py:39-61` — `try_debit_coins`, one `UPDATE xp SET coins = xp.coins - $3 WHERE user_id=$1 AND guild_id=$2 AND coins >= $3 RETURNING coins`, transaction-aware via an optional `conn` (read at the pin; M6-S3/M3-S1's 7 reuse sites `lane-claimed`) | affordability and write are **one statement**; there is no read-then-write window | `core/db` | `PORT-LOGIC` — **and note the shape of this row**: the economy *capability* is `DROP` (OD-16), and the *primitive* is preserved for every conditional write the successor does have (claim-once, quota, rate budget). A dropped capability can still donate a pattern | effect (6) · POP = every conditional write · FLOOR = its own count · negative control: a concurrent double-spend must fail | S3 |

### 3.2 · S4 — judgement without authority

| # | capability | old source | contract to preserve | new owner | approach | verification | phase |
|---|---|---|---|---|---|---|---|
| D1 | **Provider-neutral, never-raises AI gateway** | **`superbot`** `disbot/core/runtime/ai/gateway.py` — the origin. Its successor's own header says *"Ported from shipped `disbot/core/runtime/ai/gateway.py` @7f7628e1"*, and **24 of 30** files in `sb/kernel/ai/` name a `disbot/` source in their first 12 lines (I-4, I-18) | eight ordered steps — admission/flags → safety → redaction → routing → provider call under `wait_for` → metrics → parse → degraded-never-raises — with a **deterministic** provider in the same set as the vendors | `core/ai` port + `adapters/llm` | `PORT-CONTRACT` **from `superbot`**. This is one of the three attribution reversals (I-3, I-4, I-21): the 2026-08-21 plan credited this to `superbot-next` | structural (1) · POP = every module · vendor SDK imports appear only under `adapters/llm/`, whole-AST including function bodies and `importlib` by name (M10-D1 measured the absence of any such checker, `lane-claimed`) | S4 |
| D2 | **A tool catalogue that is read-only plus exactly one audited write** | `superbot` `disbot/services/ai_tool_catalogue.py:50-53` — the source comment, read at the pin: *"Support tickets — the one action toolset. `open_support_ticket` writes (it opens a ticket through the audited mutation seam), unlike every other catalogued tool, which is read-only."* 36 tools (I-11) | the model reads freely; the one write goes through **the same audited operation a button uses** | `core/ai` tool registry | `PORT-CONTRACT` **with the floor**. `superbot-next`'s open registry is the better mechanism and it is exactly what collapsed to 8 read-only rows (I-11) — so the registry ships **with `FLOOR`** from its first commit | registry floor · POP = registered tools · FLOOR = committed · **write-capable count == declared** · negative control: unregister one and the gate reds | S4 |
| D3 | **Untrusted-text containment + a scope lattice that only narrows** | **merge**: `superbot`'s containment delimiters around untrusted text (02 § D, `lane-claimed`) + `superbot-next`'s scope lattice, which is real and tested and **never fed from a live user's Discord permissions** — every production call site sits at the USER floor (M10-D3, `lane-claimed`) | model input is fenced, and the model's authority is the tier resolved at pipeline step 3 — it can only narrow | `core/ai` | `PORT-CONTRACT` with the fix: the lattice is fed from the resolved tier | contract (3) · POP = every AI-initiated op · FLOOR = its own size · assertion: no AI path widens authority | S4 |
| D4 | **Correction logged only against an answer the bot gave** | `superbot` `ai_review_cog` — recovers the original Q&A from the answer registry so a 👎 or correction-reply can only attach to a message the bot actually answered (02 § D, `lane-claimed`) | feedback is anchored to a real answer, not to arbitrary text | `modules/ai` | `PORT-CONTRACT` | journey (4) · POP = answered messages · FLOOR = 1 | S4 |
| D5 | **A decision audit holding no raw message content** | `superbot-next` — the AI decision audit stores no raw content and rejects an unknown decision shape (03 § D, `lane-claimed`) | the decision log is auditable without retaining message text | `core/audit` | `PORT-CONTRACT` | effect (6) · POP = every AI decision · FLOOR = its own count | S4 |
| D6 | **Classify externally, act through the moderation service** | `superbot`'s image moderation — 02 calls it *"the cleanest instance of [the 2026-09-04 AI-authority decision](run/in-flight-direction.md) already in production"* (`lane-claimed`): the classifier is external, any action routes through `services/moderation_service`, so escalation and audit stay one authority | judgement is external; authority is the same typed operation a human uses | `modules/moderation` + `core/ai` | `PORT-CONTRACT` **plus the fix for its measured gap**: when the provider is unavailable it silently no-ops per message with only a `logger.warning` and no diagnostics surface (M2-D3, `lane-claimed`) | effect (6) + degradation · POP = provider states {available, missing key, missing SDK, quota} · FLOOR = 4 · each must produce a stated degradation reaching a durable sink | S4 |
| D7 | **Durable-first report intake** | neither ([the 2026-09-04 AI-authority decision](run/in-flight-direction.md), adopted verbatim) | the record exists with a stable id **before** any external projection; invalid model output means no automatic action | `modules/reports` | `RE-DERIVE` (new) | journey (4) + effect (6) · POP = the four invalid-output modes {invalid, incomplete, timed-out, degraded} · FLOOR = 4 | S4 |

### 3.3 · S5 — time, degradation, restart

| # | capability | old source | contract to preserve | new owner | approach | verification | phase |
|---|---|---|---|---|---|---|---|
| E1 | **Managed background tasks** | `superbot` `disbot/core/runtime/tasks.py:1-15` — read at the pin: a strong reference held until completion (the GC trap), unhandled exceptions logged with full traceback at ERROR, `task_outcome_total{name, outcome}` incremented on every completion, `cancel_all()` for cooperative shutdown (M6-S5 / M7-S1, 14–15 consumers, `lane-claimed`) | no bare `create_task` anywhere; every background task is referenced, logged and counted | `core/scheduler` | `LIFT-VERBATIM` (§ 4 family) | structural (1) · POP = every module in the shipped package · FLOOR = module count · the gate bans bare `asyncio.create_task` | S5 |
| E2 | **Durable timers** | **neither.** `superbot`'s `!remind` is `tasks.spawn(asyncio.sleep(delay))` then a channel send — no DB row, no boot reconcile (M2-D4, `lane-claimed`); the raid-lockdown auto-restore is the same shape (M2-D2, `lane-claimed`) | a deadline survives a restart and fires exactly once | `core/scheduler` due queue | `RE-DERIVE` (new) | scheduler gate · POP = every declared job · FLOOR = its own size · the R5 drive restarts twice inside the window and asserts one firing | S5 |
| E3 | **Session identity as a database constraint** | `superbot` `runtime_sessions` — a real Postgres `UNIQUE` on (user, channel, subsystem) with `INSERT … ON CONFLICT … RETURNING` resolving the race (M6-S2, `lane-claimed`; `superbot-next` has no equivalent to port) | one active panel per (user, channel, module), enforced by the database rather than a process dict | `core/store-registry` | `PORT-CONTRACT` | restart-restore · POP = every persistent component id · FLOOR = the mint table's size | S5 |
| E4 | **Lifecycle: record intent, one watchdog executes** | `superbot` — SIGTERM and `!restart` only *record* intent; one watchdog task is the sole executor with a bounded timeout falling through to a hard exit (M5-S06); the close driver releases the runtime instance lock **before** the slow drain, with the ~85 s production downtime it fixes named in the comment (M5-S07) — both `PRODUCTION-PROVEN`, both `lane-claimed` | shutdown has exactly one executor and the instance lock is not held across the drain | `app/` | `PORT-CONTRACT` — **incident-derived, so the shape is the evidence** | deployment-readiness verdict, run **in the host environment** (08 § 5) | S5 |
| E5 | **Readiness as a decision table** | `superbot` `healthserver.py:1-18` — liveness/readiness tied to an explicit lifecycle-phase state machine; a health-server bind failure is a boot abort with a diagnostic (M7-S4, `lane-claimed`) | readiness has a named reason per row, is DB-aware, and cannot flip green before the surface floor passed | `app/` + observability | `PORT-CONTRACT` + boot step 8 (06 § 2) | boot gate · POP = the readiness rows · FLOOR = its own size · **and step 7's read-back**: `sb/app/main.py:616` hardcodes `sync_remote(..., enabled=False)` while `/ready` answers 200 (I-19) | S5 |
| E6 | **Correlation ids and structured logging** | `superbot` — per-request `uuid4` request ids (not a per-process boot id), structured JSON logging, Prometheus command latency/outcome metrics, a slow-path ring buffer (M7-S3, `lane-claimed`) | every interaction is traceable end to end by an id that changes per request | observability | `PORT-CONTRACT` + cardinality budget | operational | S5 |
| E7 | **Cleanup provider registry** | `superbot` `cleanup_registry.py` — decouples the GC scheduler from feature-owned cleanup/refund semantics via register/run_all (M6-S6, `lane-claimed`) | the scheduler does not know what cleanup means for a feature | `core/scheduler` | `PORT-CONTRACT` | scheduler gate · POP = registered cleanup providers · FLOOR = its own size | S5 |
| E8 | **A restore proof that can fail** | `superbot-next` `.github/workflows/restore-verify.yml:124` — **the counter-example**: `python3 -m sb.app.verify_boot \| tee verify-report.json`, with **0 occurrences of `pipefail`** and **0 `shell:` keys** across all 8 workflow files, so the step's status is `tee`'s; and `sb/app/verify_boot.py:100` is `sys.exit(main())`, so there was a real non-zero being swallowed (I-19) | the weekly proof that the bot can be restored must be **able to red** | CI | `RE-DERIVE` (inverted) — no pipe, or `pipefail` above it | demonstrated by **making it fail** (09 § 6 exit criterion 4) | S5 |
| E9 | **Deploy watch-path filter** | absent in `superbot` — a 4-service monorepo whose live `worker` service has no path filter, which already caused ~293 unnecessary production restarts with the root cause unfixed (M7-D4, `lane-claimed`) | a service redeploys only on changes to its own paths | deploy config | `RE-DERIVE` (new) | deployment-readiness verdict | S5 |

### 3.4 · S6 — per-guild scope

| # | capability | old source | contract to preserve | new owner | approach | verification | phase |
|---|---|---|---|---|---|---|---|
| F1 | **Per-guild visibility resolver** | `superbot` `disbot/governance/resolver.py` and `governance/__init__.py:59,152-197` — visibility resolved per guild with role-scoped overrides, a cache and an events channel (inspected in 05 § 5) | a module a server did not want is **genuinely absent** there, not merely unlisted | `core/governance` — one record read by the router, the renderer **and** the scheduler (06 § 4.5) | `PORT-CONTRACT` — **and its measured gap is the reason it moves to one seam**: `superbot` installs governance at exactly one `@bot.before_invoke` hook, which discord.py applies only to prefix commands, leaving 31 app_commands across 19 cog files ungoverned (M5-D01, `lane-claimed`), and 35 of 43 subsystems fail **open** when the gate throws (M5-D06, `lane-claimed`) | per-profile reachability (5) + a cross-guild leakage query · POP = every store · FLOOR = its own size · assertion: no query returns another guild's rows | S6 |

### 3.5 · Group G · the optional modules (OD-D), phase = after S2, order = his

[`12-owner-decisions.md`](12-owner-decisions.md) **OD-D** decides which of `xp`,
`karma`, `leaderboard`, `counting`, `starboard`, `community_spotlight`, `ticket`,
`polls` and `reminders` are core, optional or gone; the recommended default is
that **none is core** and each is an optional module the extension contract must
carry. Each migrates through **B7's recipe**, and each carries one named contract
worth preserving rather than a file worth copying:

| module | the contract worth preserving | approach | note |
|---|---|---|---|
| `karma` | the anti-abuse orchestration — self-give guard, per-recipient cooldown, daily cap, disabled check — tested by calling the **real** function with only the DB/bus boundary mocked (M2-S4, `lane-claimed`) | `PORT-LOGIC` | the orchestration is pure; the storage is not |
| `counting` | the persistence write rides the managed-task seam, so a failure is logged and metered rather than silently swallowed (M2-S2, `lane-claimed`) | `PORT-CONTRACT` | second consumer of E1 |
| `starboard` | every one of the 5 config-mutation entry points calls a shared `_emit` helper recording an audited mutation (M2-S1, `lane-claimed`) | `PORT-CONTRACT` | the reference port for S2 (09 § 3); its defect (absent from `SUBSYSTEMS`) is fixed by B7 step 7 |
| `ticket` | open/claim orchestration asserted against the real `tm.open_ticket`, including the emitted bus payload and that the audit call fired (M2-S7, `lane-claimed`) | `PORT-CONTRACT` | and the gap: no DB-layer test at all, unlike moderation and roles (M2-D7, `lane-claimed`) |
| `roles` | the role-menu view **names and enforces** Discord's 25-option select cap and the 25-component view cap rather than truncating at render (M2-S5, `disbot/views/roles/role_menu_view.py:36-38,270-272`, `lane-claimed`) | `PORT-CONTRACT` | a platform limit stated in code is worth more than the code |
| `leaderboard` | `RankProvider` ABC + registry read by exactly 2 host surfaces, with **7** independently registered providers (M3-S4, `lane-claimed`) — a plugin seam that actually works | `PORT-CONTRACT` | the successor's version is a capability ref resolved by the compiler |
| `xp` | the passive chat award riding the real message pipeline (M3-S4, `lane-claimed`) | `PORT-CONTRACT` | one of `superbot-next`'s three genuinely armed message-feed consumers |
| `welcome` | `superbot`'s real `on_member_join`, live in 4 cogs — greeting, autorole, raid screening, join logging (02 § B, `lane-claimed`) | `PORT-CONTRACT` | the counter-example is A6's: a toggle reading ✅ that can never fire |
| `security` / raid | the honest allowlist entry — the known restart gap is triaged, allowlisted with a named reason, and the entry itself states the residual user-visible caveat in plain language (M2-S6, `lane-claimed`) | `PORT-CONTRACT` for the *disclosure habit*; `RE-DERIVE` the timer onto E2 | the gap it discloses (M2-D2) is fixed by E2, which is why the disclosure is the transferable half |
| `polls`, `reminders` | nothing — both are measured as zero-persistence toys (M2-D5, M2-D4, `lane-claimed`) | `RE-DERIVE` on E2's due queue | the capability is wanted; neither implementation is |

---

## 4 · The artifacts worth lifting verbatim — the eleven anti-vacuity mechanisms

These are the only rows in this document permitted `LIFT-VERBATIM`, and the
reason is stated in [`08-verification.md`](08-verification.md) § 3: **both
repositories already built working anti-vacuity mechanisms, each after a real
incident, and not one was generalised to the guards beside it.** The successor's
requirement is not a better idea; it is a framework in which these are the
default shape of a check and opting out is what takes effort.

**Every path below was opened and read at the pin by this session.** Each row
carries a **mandatory repoint**, because several of these mechanisms are correct
instruments aimed at the wrong population — which is the whole subject of this
package.

| # | mechanism | source path (verified at the pin) | what it gives | new home | the mandatory repoint | phase |
|---|---|---|---|---|---|---|
| 1 | **denominator assertion** | `superbot-next` `tools/run_golden_parity.py:162-170` — the comment read at the pin: *"the gate could false-green with fewer cases replayed than goldens on disk. Assert the two counts match per ported subsystem"* | two independently derived counts compared in the same run | `core/checks` — **every** gate | it stayed in one file. It becomes an argument of check registration, so a check that cannot state its two counts cannot register | S1 |
| 2 | **live-population negative control** | `superbot` `tests/unit/invariants/test_help_reachability.py:61-80` — docstring read at the pin: *"a vacuous check is worse than none"*; it mutates the **live** scheme and `pytest.fail()`s when the target is absent, so the control itself fails on an empty population | a guard that proves it has teeth on the real set | `core/checks` — every population-walking guard | **the target is wrong.** It mutates `scheme_live()`, a model of the hub registry. Repoint it at the **rendered** view — the replacement already exists in the same repo, `tests/unit/views/test_games_hub_view.py`, applied to 2 of 8 hubs (I-6) | S1 |
| 3 | **shrink-only ratchet with a staleness proof** | `superbot` `tests/unit/invariants/test_command_reachability.py:96-104` — `test_baseline_has_no_stale_entries`, read at the pin: *"the recorded debt only ever shrinks"*; its baseline is currently `frozenset()`, which is what a finished ratchet looks like | recorded debt cannot go stale, and the list cannot grow | `core/checks` | its sibling ratchet in the same repo has no such test (08 § 3.3). In the successor **every** baseline/allowlist carries a paired staleness assertion; a list without one is a build error | S1 |
| 4 | **excuse-row expiry** | `superbot-next` `tools/check_settle_once.py:629-637` and `tools/check_money_race.py:610-616` — both read at the pin, both emitting `STALE-ROW … never let an excuse outlive the code it excused` | an allowlist row matching nothing is **itself** a finding | `core/checks` template | 2 of the 10 checkers that carry exemptions do this (08 § 3.4's corrected count). It goes in the template, so it is present by construction — and it is the direct answer to `superbot`'s five exception files plus a 55-entry `known_violations` ledger | S1 |
| 5 | **the guard that guards the guards** | `superbot` `tests/unit/scripts/test_workflow_script_flags.py:1-30` — provenance header read at the pin: PR #1770 invoked a checker with a `--strict` it does not define, *"argparse exited 2, so the (advisory) checker never ran at all"* | a silently-dead checker is caught | `core/checks` | it is scoped to one workflow file and marked *"disposable … delete this test if it proves unreliable."* In the successor checkers **self-register their argparse surface** and CI derives invocations from that registry, so the guard's population cannot drift | S1 |
| 6 | **`db_delta` effect capture** | `superbot-next` `parity/harness/dbsnap.py:1-18` — read at the pin: `TRUNCATE … RESTART IDENTITY` per case, fixture rows applied, a full before/after dump, a row-level diff, volatile values normalised | R5 calls it *"the only assertion in either repo that proves a write happened"* | `core/checks` effect layer (08 § 3c layer 6) | it lives inside the parity harness, which cannot boot (§ 7). Lift the **snapshot/diff/scrub** mechanism out of the harness and point it at the successor's own transactions | S1 (mechanism) · S2–S3 (load) |
| 7 | **the F-003 denominator assert** | same file as row 1 | — | — | **the overlap is real and is stated rather than padded**: [`08-verification.md`](08-verification.md) lists this mechanism in both § 3 and § 3b, so the eleven slots hold **ten distinct artifacts**. Counting it twice would be this document committing the defect it is cataloguing | — |
| 8 | **composition-root reachability boot** | `superbot-next` `tools/check_runtime_smoke.py:1-14` — read at the pin: *"Static checks pass while WIRING breaks slip through"*; boots the real root headlessly, **no token, no guild, no DB, no network**, and resolves every manifest ref and armed subscriber, riding *"the SAME composition-root code paths as `sb.app.main`, never a parallel re-implementation"* | the reachability layer, cheap | `core/checks` reachability layer (layer 5) | it is missing one assertion — that every registered `custom_id` resolves to a handler, which is R5's 165-never-clicked hole (`lane-claimed`). Add it, and walk the **route graph the composition root built**, not a registry a fixture can empty (I-2) | S1 |
| 9 | **the single-entry-seam fence** | `superbot-next` `tools/check_no_skip.py:1-14` — read at the pin: *"there is NO path from a Discord surface to a handler except through `resolve()`"*, plus discord-import containment | **the cog-portability enabler** — one entry seam is what makes an out-of-tree module safe to load | `core/checks` structural layer | two changes: widen its root to wherever ported modules live, and **pair it with the positive direction** — every registered command *is* reachable from `resolve()`. Also close the dynamic hole: M8-D09 (`lane-claimed`) measured it stricter on the three static import forms and EXIT=0 on `importlib` | S1 · widened S2 |
| 10 | **the frozen compat pin** | `superbot-next` `compat/compat-frozen.json` — re-derived here: **413 command rows across 46 groups, 265 `legacy_custom_ids`, 49 `subsystem_keys`, 23 `event_payloads`, 17 `legacy_ai_task_ids`** (**`§10 measured`** — R5's figures reproduce exactly), CODEOWNERS-routed | R5 calls it *"the highest-value artifact in either repo for the owner's stated goal"*: the executable form of a compatibility contract | `core/checks` + CODEOWNERS | **lift the form, not the content.** The pinned identifiers are the **old bot's** surface, and under OD-B's default the successor makes no replacement promise, so it owes that surface nothing. The successor's compat file starts **empty** and grows as it ships surfaces. *If the owner answers OD-B "commit to replacement", this file's content becomes a migration input rather than a template* | S1 (form) · OD-B (content) |
| 11 | **GAP-on-unmodeled-effect** | `superbot-next` `sb/adapters/parity/transport.py:13-14` — read at the pin: *"Unknown/unmodeled effects are recorded as GAPS (the capture-integrity honesty rule: a golden must never silently drop an outbound effect)"* | R5: *"an unmodeled effect is a RED, never a skip — the single discipline that separates this harness from a screenshot differ"* | `core/checks`, all layers | generalise it past the harness into the rule 08 § 5 states independently: **a skipped test in a required gate is a red gate.** The measured original is `pytest tests/integration -q` → `14 skipped`, EXIT=0 inside a job that provisions Postgres precisely so it cannot skip (I-16) | S1 |

**Two hygiene patterns ride along** and are named separately because 08 § 3b does
not count them among the six: **symmetric disposition transforms** (an accepted
difference is applied to *both* sides, so it cannot become a one-sided blind
spot) and a **closed reason-class vocabulary** for exemptions (12 declared
classes, *"never a bare flaky"* — `lane-claimed`, R5). Both migrate into the
checker template, the second with the addition row 4 supplies: **an expiry per
class, so *time-driven* cannot mean *forever*.**

---

## 5 · What is explicitly not migrated

Each absence is a decision with a measurement behind it, recorded here so a
future session does not re-open it by accident.

| not migrated | why | evidence |
|---|---|---|
| the 533-golden corpus and the parity harness | the oracle never runs the shipping renderer: the actual side is `rendered_panel_payload()` (`sb/adapters/parity/transport.py:242`, called at `:531`), production installs `DiscordPanelPresenter` (`sb/app/panel_host.py:66`), and the two are never compared to each other | 08 § 3b · and § 7 below: the corpus is not reproducible from that repository at all |
| `rendered_panel_payload()` and every renderer twin | 06 § 3's single most consequential rule — **one renderer, no twin** | 08 § 3b |
| the capture-world literals | transcribing a value made a golden green where computing it made it red — *"the gate selected for the photograph"* | 04 § 2.3 · I-5's 116 of 382 `sb/domain` files |
| `superbot`'s five exception files + the 55-entry `known_violations` ledger | an allowlist that can only grow is a rule being retired in slow motion; § 4 row 4 is the mechanism that replaces them | 04 § 1.2 · 09 § 2's stop rule |
| the **global contiguous** migration ladder | it is the structural cause of the facet fence; immutability and checksums migrate (B2), contiguity is re-scoped to the module | `tools/check_migrations.py:4-16` read at the pin · I-10 |
| the setup provisioning preview/confirm panels | 450 lines with **zero** production callers, and the confirmation gate is bypassed at 3 of 3 call sites with `confirmed=True` hardcoded | M1-D03, M1-D02, both `lane-claimed` |
| `check_deferred_recovery` | its real candidate population is **two** functions in an 883-file tree, and both are the two bugs it was written from; it decides recovery by regexing raw source text including comments | M5-D03, M5-D12, both `lane-claimed` |
| `check_settings_reachability` as shaped | it certifies from a **source literal**, so a schema module never registered still counts reachable — the population defect in a guard | M1-D04, `lane-claimed` |
| the outbox | 763 LOC across enqueue/store/relay/metrics plus a table, serving exactly **one** at-least-once event of 25 | 06 § 13, `lane-claimed` |
| saga compensators · `DURABLE_ONCE` · `ConfirmationSpec` grammar · the fuzzy-typo rung · an open renderer escape hatch · 107 of 237 unused declaration fields | each measured unused; each names its own re-entry trigger in 06 § 13 | all `lane-claimed` |
| `SUBSCRIBE_ROSTER` | a 6-entry hand-maintained tuple whose completeness is enforced by nothing; a 7th subscriber omitted from it passes every gate | M8-D05, `lane-claimed` · replaced by 06 § 7's derived-registry rule |
| `ux_lab` | an admin-only gallery of fake Discord UI patterns whose own docstring says it performs zero writes, at 4,937 lines across 13 files | M3-D6, `lane-claimed` |
| BTD6, Project Moon, economy / casino / blackjack / inventory / treasury, mining / fishing / farm / creature | OD-16; and one AI-content vertical alone is 30,923 of 59,744 measured lines of the games surface | M3-D7, `lane-claimed` · 02 § 3 |
| `bet_and_settle`, `fishing_workflow.fish()` | dead seams named as live API in their own docstrings, with zero production callers | M3-D3, M3-D4, both `lane-claimed` |
| the EAP documentation tranche | 183 surviving doc files added to `superbot` in fourteen days against 2 runtime files; the successor's documentation is its declaration and its record | I-9 · 09 § 8 |

**One artifact is neither migrated nor dropped, and it earns the exception.**
`superbot`'s `docs/AGENT_ORIENTATION.md`, created **2026-05-24 — six weeks before
the EAP** — carries the tier vocabulary this estate's own boot file descends from,
and it is the dated artifact behind the owner's *"pre-EAP docs are the quality
baseline"* claim (I-9). Its disposition is `PRESERVE_PATTERN` **with the defect
removed**: it misstates the size of its own tree (M7-D3, `lane-claimed`), which is
what a hand-written orientation doc does. The successor's equivalent is
**generated from the declaration**, so it cannot misstate what is in the tree.

---

## 6 · Data disposition

### 6.1 · The standing rails, before any classification

1. **The live Postgres behind `superbot` is a protected surface and was not read
   by this review.** Nothing below is measured against production rows; every
   figure comes from committed migrations and source.
2. **This plan authorises no data migration of any kind.**
   [`12-owner-decisions.md`](12-owner-decisions.md) **OD-E**'s recommended default
   is **import nothing; start fresh** — because under **OD-B**'s default the
   successor is not promised as a replacement, so there is nothing to be
   continuous with, and *every migration that does not happen is a class of risk
   that does not exist.*
3. **If any data does carry forward it is owner-approved, dry-run first,
   reversible, measured and independently verified** — § 6.4 is that protocol,
   written so a later session does not have to invent it under pressure.

### 6.2 · The size of the thing, measured from committed files only

| fact | value | source |
|---|---|---|
| `superbot` migrations | **104** `.sql` files, numbered `001`…`104` | **`§10 measured`** |
| `superbot` DB access modules | **45** `.py` files under `disbot/utils/db/`, one of which is `__init__.py` | **`§10 measured`** |
| `CREATE TABLE` statements in those migrations | **92** occurrences; **90** matched by the § 10 regex, of which **74 declare a `guild_id` column** | **`§10 measured`** |
| hand-written teardown helpers | **31** `def _teardown_*` in `disbot/guild_lifecycle.py` | **`§10 measured`** |
| domains with a declared canonical write path | **14** in `architecture_rules/mutation_owners.yaml`, plus **6** `known_raw_write_violations` | **`§10 measured`** |
| `superbot-next` migrations | **57** `.sql` files plus `checksums.json` | **`§10 measured`** |
| namespacing in either repo | `CREATE SCHEMA` **0 times**; `search_path` in **0** `.sql` files. Every table is in `public` | **`§10 measured`** |

**The last row is the migration-relevant one.** Neither predecessor namespaced
anything, so there is no schema boundary to migrate *along*. Any production
import lands in a successor whose modules own `mod_<name>` schemas (B8) — which
means a data migration is a **re-homing**, not a schema copy, and its mapping is
per-store, declared, and reviewable.

### 6.3 · The four classes

The governing rule is one line and it disposes of most of the 104:
**data cannot migrate to a capability that does not exist.** Every `DROP` row in
[`02-product-matrix.md`](02-product-matrix.md) is automatically **start fresh**
here, with no further argument needed.

| class | what is in it | why |
|---|---|---|
| **MUST MIGRATE** | **nothing.** Under OD-E's and OD-B's defaults this class is empty, and the emptiness is the decision, not an omission | there is no replacement promise, so there is no continuity obligation. This class becomes non-empty only if the owner answers OD-B *commit to replacement* — at which point the migration map's data column changes and a rehearsal becomes a phase rather than a contingency (12 § OD-B) |
| **MAY MIGRATE** — owner-named, **server-visible surfaces only** | on the evidence, the plausible candidates are **member XP / levels**, **karma**, and **open tickets**; `starboard` entries are a fourth if OD-D makes it core | OD-E asks him to name *surfaces the server's members would notice losing*, **not a table list** — a table list is a schema port wearing a product's clothes. Each named surface then becomes one scoped, rehearsable exercise under § 6.4 |
| **START FRESH** | per-guild settings and activation state · governance/visibility records · bindings · panel/session rows (`runtime_sessions` is a runtime cache by construction) · the audit spine (the successor writes its own from op 1) · AI conversation state and memory · **and every table belonging to a dropped capability**: economy, casino, blackjack, inventory, treasury, mining, fishing, farm, creature, BTD6, Project Moon, `ux_lab` | settings and governance are re-declared by the successor in a different grammar (A6), so importing them would import a vocabulary the successor does not speak; the dropped-capability tables have no destination at all |
| **HISTORICAL ONLY** — read-only, never imported | `binding_audit_log` and the rest of the forensic trail `superbot`'s teardown deliberately retains (M1-S06, `lane-claimed`) · moderation case history · the migration ledger itself · `setup_draft_operations` (whose survival across a guild leave is a *defect* in the source, not a feature to carry — § 2 B5) | these are records **about** the old bot. Their value is answering "what happened", which a read-only export serves; importing them into a new audit spine would mix two systems' provenance in one table, and the successor's audit row records a resolved authority tier that the old rows do not carry |

### 6.4 · The protocol, if and only if the owner answers OD-E

Seven gates, in order. **Each is a stop, not a checkpoint.** No step may be
skipped because the previous one looked green — that reflex is the subject of
this entire package.

| gate | what it requires |
|---|---|
| **P0 · owner approval, in surfaces** | he names the **server-visible surfaces** that must survive, not tables. Nothing starts without this, and the naming is the scope |
| **P1 · inventory against a restored copy** | the source is a **restored backup**, never the live database. The inventory is read-only, and it produces a declared population: rows per surface, per guild, with counts committed to the repository before anything is written |
| **P2 · the migration is a typed operation** | it is written in the successor as a module operation with an `authority_ref` and an `audit_verb` (C1), inside its module's own ladder — **not** a `psql` script and not a one-off notebook. If it cannot be expressed as an op, the destination model is wrong and the answer is to fix the model |
| **P3 · dry run, with an effect assertion** | run against the restored copy. The assertion is a row-level `db_delta` (§ 4 row 6), source → target, with the P1 counts as the committed floor: `assert migrated >= FLOOR` beside `assert ok`. A run that migrates fewer rows than the inventory declared is a **red**, not a partial success — this is the population contract applied to data |
| **P4 · reversibility, demonstrated** | the target is `mod_<name>`, so the whole rehearsal is `DROP SCHEMA`-able; the source is opened read-only and is never written. Reversal is **rehearsed at least once** and its exit code read, not inferred |
| **P5 · measurement, published** | counts per surface per guild, plus a sampled row-by-row equality check, both written into the record. A count with no sample proves the rows arrived, not that they arrived intact |
| **P6 · independent verification** | a second session re-derives the source count with its own instrument — and per I-18, **with a positive control**: find the symbol before counting the symbol. Then a **human** confirms one real member's data in Discord, which is R4 on the ladder and cannot be signed by the session that wrote the migration (08 § 4) |
| **P7 · the cutover is separate** | moving data is not handing over a journey. That is **C4** on 09 § 9's ladder — one journey, per-guild, reversible by one setting flip, with its own 14-day observation window |

**And the rail that outranks all seven:** nothing in this package modifies
`superbot`, its Railway worker, its Postgres, or any Discord surface it serves.

---

## 7 · The golden corpus is not reproducible from `superbot-next` alone

**Measured, at the pin** (**`§10 measured`**):

```
superbot-next/parity/harness/boot.py:33   _DISBOT = _REPO_ROOT / "disbot"
superbot-next/parity/harness/boot.py:41   if str(_DISBOT) not in sys.path:
                                :42           sys.path.insert(0, str(_DISBOT))

$ ls -d /home/user/superbot-next/disbot
ls: cannot access 'disbot': No such file or directory
```

The oracle harness boots the **real old bot in-process** to produce the expected
side of every golden diff — and it does that by putting a sibling `disbot/`
directory on `sys.path` that **does not exist in that repository.** Three
consequences, and the third is a rule the successor inherits:

1. **No migration row in this document may be verified "against the goldens."**
   No such verification is executable from the repository that owns them. Any row
   phrased that way would be a claim nobody can check, which is precisely what
   § 0.1 forbids.
2. **This is why R5's corpus figures stay `lane-claimed`** — 38 of 533 goldens
   asserting nothing after dispositions, 165 of 183 component ids never clicked,
   36 of 533 pinning a refusal, `check_parity_depth` over a denominator of 83.
   Reproducing them requires checking `superbot` out at `5e3a667b` into
   `superbot-next/disbot/` and running the harness with Postgres available, and
   **this session did not do it.** A later session that wants those numbers now
   knows the exact prerequisite. (One adjacent figure *was* re-derived and
   matches: 62 of 533 goldens carry an empty `db_delta`.)
3. **The successor's rule, stated as a migration requirement rather than an
   aesthetic:** *an acceptance artifact that needs a second repository on
   `sys.path` is not an acceptance artifact the successor may build.* Its
   acceptance corpus is reproducible from one repository, from the **shipping**
   renderer, or it is not the acceptance corpus. This is the same sentence as
   06 § 3's *one renderer, no twin*, arriving from the reproducibility side.

**And the honest credit, because it belongs in the same section.** The parity
gate is the one instrument in either repo that **refuses to be vacuous**: run on
a machine with no Postgres it prints `gate: RED — 50 subsystem(s) are flipped
'ported' but no replay is possible`, names the reason, and exits **1** (I-20).
Whatever else is wrong with what it compares, it does not lie about whether it
ran — which is exactly the property § 4 rows 1, 6 and 11 exist to generalise.

---

## 8 · The manifest by phase

Reading of the tables above, so a session opening
[`09-roadmap.md`](09-roadmap.md) at a slice can see what that slice owes.

| slice | migrates in | count |
|---|---|---|
| **S1** — front door and first run | A1–A13, plus **all eleven** § 4 mechanisms (they are the shape of the first check written, not a slice — 09 § 0.4) | 13 capability rows + 10 distinct artifacts |
| **S2** — the ported module that owns data | B1–B8, plus B7's recipe applied once to OD-D's pick | 8 |
| **S3** — the mutation spine | C1–C8 | 8 |
| **S4** — judgement without authority | D1–D7 | 7 |
| **S5** — time, degradation, restart | E1–E9 | 9 |
| **S6** — the second configuration | F1 | 1 |
| **after S2, order = OD-D** | Group G's ten optional modules | 10 |
| **never** | § 5's fourteen classes | — |
| **only on OD-E** | § 6.4's seven gates | — |

**The sequencing constraint that is not negotiable**, repeated from
[`04-root-cause.md`](04-root-cause.md) § 3 and
[`09-roadmap.md`](09-roadmap.md) § 0.4 because this file is where it would be
easiest to lose: § 4's mechanisms are **cheap in the first commits and unaddable
later.** A migration plan that schedules them after the features it migrates has
already failed, in the same way and for the same reason as last time.

---

## 9 · What this file could not settle

Routed, not invented, per [`12-owner-decisions.md`](12-owner-decisions.md):

| row | what it moves here |
|---|---|
| **OD-A** — one server or many | whether **F1** exists at all, and the size of the setup surface A3/A4 migrate into |
| **OD-B** — is replacement ever promised | the **MUST MIGRATE** class in § 6.3 (empty under the default, non-empty under a replacement promise) and § 4 row 10's content-versus-form call on `compat-frozen.json` |
| **OD-C** — third repository or `spider-bot` grown | if `spider-bot` is the seed, every row's *phase* is unchanged but its *venue* becomes a live production bot, and § 6.4's "restored copy" posture has to be built around a running service |
| **OD-D** — which community features are core | which module B7 ports first, and the whole of Group G's ordering |
| **OD-E** — does production data carry forward | § 6.3's second class, and whether § 6.4 is ever executed |
| **OD-F** — how much authority the AI holds | D2's write-capable floor (exactly one under the default) and D3's tier boundaries. **The pipeline order in [the 2026-09-04 AI-authority decision](run/in-flight-direction.md) is identical under every answer** |

Two package-level gaps also bear on this file and are not its to close
([`13-verdict.md`](13-verdict.md)): **neither bot was booted**, so every
reachability figure a row here cites is a declared-graph figure; and **the
fan-out's adversarial refutation pass had not run**, which is why every lane
number above carries its `lane-claimed` mark inline rather than in a footnote.

---

## 10 · Measurements made while writing this file

Every command was run against the pinned read-only clones — `superbot` @
`5e3a667b`, `superbot-next` @ `d5f66dc2` — and nothing was modified.

| # | claim | command | result |
|---|---|---|---|
| 1 | the byte-identical pair | `md5sum superbot/disbot/utils/mining/capacity.py superbot-next/sb/domain/mining/capacity.py` | both `64f1665a9fb83a940d95eca5b9492bf2`; 137 lines. I-21 reproduces |
| 2 | teardown coverage | `grep -rn "def _teardown_" disbot/` · a regex census of `CREATE TABLE … ( … );` bodies over `disbot/migrations/*.sql` | **31** helper definitions, all in `disbot/guild_lifecycle.py`; **90** `CREATE TABLE` statements matched of **92** occurrences; **74** declare a `guild_id` column. **This reconciles two conflicting lane figures** — 06 § 8 carries *"31 helpers against 84 guild-scoped columns"* and M1-D06 carries *"23 `_teardown_*` against 74 tables"*; the measured pair is **31 helpers / 74 tables**, and the 2-statement regex shortfall is stated rather than hidden |
| 3 | the staged-draft leak | `grep -rn "setup_draft_operations"` · `grep -c "setup_draft" disbot/guild_lifecycle.py` | the table is created at `disbot/migrations/035_setup_draft_operations.sql:78` and indexed on `(guild_id, seq)` at `:134`; `guild_lifecycle.py` names it **0** times. M1-D01 reproduces |
| 4 | ladder and DB-module sizes | `ls disbot/migrations/*.sql \| wc -l` · `ls disbot/utils/db/*.py \| wc -l` | **104** migrations (`001`…`104`); **45** `.py` files, one being `__init__.py` |
| 5 | mutation ownership | parse `architecture_rules/mutation_owners.yaml` | **14** domains, **6** `known_raw_write_violations` |
| 6 | `superbot-next`'s ladder | `ls migrations/*.sql \| wc -l` · `ls migrations/checksums.json` | **57** `.sql` files plus the manifest |
| 7 | namespacing | `grep -ril "create schema"` over both migration sets · `grep -rl "search_path"` over both trees | `CREATE SCHEMA` **0**; `search_path` in **0** `.sql` files. The only tree hit is `superbot-next/tools/manifest_compile.py:267-268`, `pkgutil` package paths — not a Postgres `search_path` |
| 8 | the frozen compat pin | parse `compat/compat-frozen.json` | **413** command rows across **46** groups · **265** `legacy_custom_ids` · **49** `subsystem_keys` · **23** `event_payloads` · **17** `legacy_ai_task_ids`. R5's figures reproduce exactly |
| 9 | the harness's missing repository | `sed -n '33p;41,42p' parity/harness/boot.py` · `ls -d disbot` | `_DISBOT = _REPO_ROOT / "disbot"`, inserted on `sys.path`; the directory does not exist |
| 10 | **a probe that failed, recorded as a failure** | `grep -rn "register_store(" sb/ \| wc -l` · a regex for `erasure_ref="…"` literals | **75** call sites and **1** distinct literal, against B-D01's 52 stores and 48 distinct `erasure_ref` names. The instrument does not resolve the constructor's shape, so it settles nothing and **B-D01 stays `lane-claimed`**. Per I-18: a re-derivation with an unvalidated instrument is not a re-derivation, and publishing this as a correction would be the ledger's own bad row repeated |

Rows 1–9 are stated bare in the tables above under the **`§10 measured`** mark.
Row 10 is the reason one figure in § 2 stays unverified, and it is here rather
than dropped because a failed probe that is recorded costs one line and a failed
probe that is quietly dropped costs the next reader a day.
