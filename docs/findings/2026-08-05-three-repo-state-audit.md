# What is true across fleet-manager, superbot and superbot-next

> **Status:** `reference`
>
> Written 2026-08-05 as the foundation for a later planning session that will
> rebuild a **server-first Discord bot with no game features**. It is not that
> plan. It establishes what is actually true first, because the previous two
> sessions' failures all came from the same move — reading code and inferring,
> while skipping both repositories' required boot files.
>
> **Method.** Documents first, trusted until they contradict the tree; anything
> unsure verified by running it. Both bot repositories were cloned at HEAD, and
> both were made executable in-container (`superbot` on python3.10 +
> `requirements.txt`, `superbot-next` on python3.11 + `requirements.lock`) so
> that measurements come from imports and checkers rather than from greps. The
> 967 + 334 session cards were read by a delegated Gemini pass on Vertex with
> every citation machine-verified against the tree. Where a number here came
> from a grep or an estimate, it says so.
>
> **This document corrects four claims in the record, including one of its own
> author's.** They are collected in § 6 rather than scattered.

## 0. The finding in one paragraph

superbot's navigation graph is not an emergent property of a well-liked bot —
it is a **built system with a mechanical guard**, and that guard is green at
HEAD: `242 prefix commands · 95 reachable · 147 exempt · 0 GAP`. Three
mechanisms hold it up: a per-cog `build_help_menu_view` hook that returns a
**live curated launcher** (the Role Hub is seven buttons, not one per command),
an `attach_standard_nav` call in the base view's `__init__` that makes every
panel one click from Help, and a single `help_projection` seam that replaced
five divergent visibility filters. superbot-next ported none of the three. But
the reason its help tree is dead is **not** the one previously recorded: its
command data is computed live from the manifest, which is itself the dispatch
table. What is missing is **curation** — the manifest has no way to say *these
six actions matter*, so the help tree can only auto-list every command as text.
That is a smaller and much better-defined problem than "it is a photograph",
and it is the single most important correction in this document.

## 1. fleet-manager — state confirmed, and the drift found

Verified against HEAD via the direct-PAT path, 2026-08-05.

| Claim | Verdict |
|---|---|
| `main` @ `4b6fc99` | ✅ confirmed (`commits/main`) |
| Nothing open | ✅ confirmed — 0 open PRs |
| "Eight PRs merged 2026-08-05" | ⚠️ **19** merged that day — 11 substantive + 8 roster-regen |
| `claude/swingy-spider-…` fully merged | ✅ tree SHA `e0e79fd4f0` **identical** to main's; the "3 ahead" is squash-merge graph noise |
| superbot / superbot-next public, `archived=false` | ✅ both |
| Corpus scale 967+861 / 334+92 | ✅ exact at HEAD |

Two drifts not in the brief, both worth carrying:

- **The local git proxy serves a stale `origin/main`** — `92c0909`
  (2026-08-04, PR #734), 26 commits behind. `git fetch origin main` returns
  exit 0 and changes nothing. Any session that trusts `git log origin/main`
  here is reading yesterday. Use the direct API for state.
- **The consolidation program's §7 progress ledger stops at 2026-07-26.** None
  of the 08-01 → 08-05 work has a row: the Vertex directive, the two Gemini
  benchmarks, the Play submission requirements, the superbot-next live audit,
  the navigation-graph correction. The NOW pointer still reads **E1**, which is
  owner-reserved and explicitly not available to pick up. A session looking for
  work from the program alone would find a pointer it must not act on and no
  record of the last five days.

Also: `docs/findings/2026-08-05-playtest-discord-and-superbot-value.md` § 6
still recommends *"Use the live `superbot`. Do not deploy `superbot-next`"* —
the recommendation the owner overrode the same day. The file carries no
superseded note.

## 2. superbot — the navigation graph is a built system

### 2.1 Shape

883 Python files · 243,961 lines under `disbot/`. Layered
`utils/` → `utils/db/` (asyncpg only) → `core/` → `services/` → `governance/`
→ `views/` → `cogs/`, with `services/ → views/` carrying **zero tolerance for
new violations**. **59** entries in `config.INITIAL_EXTENSIONS` (AST-counted at
HEAD; the playtest doc's "61" is stale), loaded in order by `bot1._load_cogs`,
with `cogs.bootstrap_access_cog` pinned first so the command-access guard is
installed before anything can be admitted.

### 2.2 The three mechanisms that make the graph hold

**One — the per-cog launcher hook.** 43 cogs implement

```python
async def build_help_menu_view(self, interaction) -> tuple[discord.Embed, discord.ui.View]
```

It returns a **live View**, so the panel is constructed at click time by the
subsystem that owns it. The Role Hub returns seven buttons — 📝 Create ·
🗂️ Manage · ⏱️ Time Roles · ⚡ XP Roles · 💬 Reaction Roles · 🔧 Diagnostics ·
🚫 Exemptions — for a subsystem with far more than seven commands. **These are
curated feature launchers, not a rendering of the command list.** That
distinction is the whole ballgame; see § 4.3.

**Two — "never stranded".** `views/navigation.attach_standard_nav` runs in the
base view's `__init__`, so it cannot be forgotten:

> *"every panel that declares a `SUBSYSTEM` gets, on construction, a **📚 Help**
> button and — when the subsystem has a `parent_hub` — a **↩ \<hub\>** button…
> any panel reachable by *any* command stays one click from Help and its hub."*

Because it runs on construction, the controls survive the `edit_in_place`
redraw idiom that used to drop them. `HubChildButton` complements it with the
shared open-child-in-place logic, including a **click-time governance recheck**
so a user who lost a tier between renders gets the current state.

**Three — one visibility seam.** `services/help_projection.py` (662 lines)
replaced five different filter sets across five render paths with one
reason-coded model: `shown · display_hidden · governance_hidden · routed_off ·
command_locked · unavailable · orphaned_override`. Only the first two hide.
Help **deliberately advertises locked features** — execution is denied by the
owning policy with its own copy.

### 2.3 The guard, run at HEAD

`scripts/check_command_reachability.py` is a per-command help-reachability
checker built 2026-06-23 with an allowlist (`architecture_rules/
command_reachability_exceptions.yml`) whose entries each carry a source-cited
reason. Run in-container on python3.10, **real exit code 0**:

```
check_command_reachability — 242 prefix commands  (95 reachable, 147 exempt, 0 GAP)
  all member-tier commands are reachable ✓
```

This matters more than any other single fact in this document. The live-audit
doc proposed, as the acceptance test the golden harness could never express,
*"from `!help`, every shipped feature is reachable by clicking… a property of
the route table, checkable mechanically."* **It already exists, it has existed
since June, and it is green.** It was not ported.

Its own history is the argument for it: the 2026-06-22 regrouping simulation
found **8 orphan subsystems** — *"fishing, creature, welcome, counters,
security, channel, ai, ux_lab"* — reachable only through the paginated
"Advanced" list. Four of those are server subsystems. The fix homed them under
hubs and **deleted** the "All Commands / Advanced" text browser
(`HelpPanelView`, PR #1294) as redundant. superbot's help tree ends in
launchers because the text browser was deliberately removed from it.

### 2.4 Which server-relevant files are sound, and which need work

The decomposition rule is explicit: past ~400 LOC a cog **must** be split into
`cogs/<name>/` (pure domain) + `views/<name>/` (UI). Measured at HEAD:

**Sound — inside the rule, decomposed, or small enough not to need it**

`help` (444 + `cogs/help/` ×4 + `views/help/` ×3 — the route/panels/schemas
split is clean) · `moderation` (340 + 2 + 3) · `settings` (236 + 1 +
**16** view modules) · `welcome` (189 + 2) · `automod` (149 + 3) ·
`image_moderation` (145 + 3) · `security` (142 + 2) · `server_management`
(101 + 3) · `community` (78 + 2) · `counters` (258 + 2) · `diagnostic`
(266 + 6 + 6) · `logging` (447 + 6) · `starboard` (329 + 2) · `karma` (269 + 2).

**Needs work — over the threshold, and two have no supporting package at all**

| Cog | LOC | State |
|---|---|---|
| `cleanup_cog.py` | 798 | decomposed (3 + 2) but the entry file is still double the rule |
| `setup_cog.py` | 795 | decomposed (4 + **15**); the largest legitimate surface here |
| `role_cog.py` | 786 | decomposed (2), hosts the 7-button PersistentView (Pattern A) |
| `admin_cog.py` | 782 | decomposed (3); hosts `!cog` and 15 buttons |
| `channel_cog.py` | **750** | **no `cogs/channel/`, no `views/channel/`** — undecomposed |
| `utility_cog.py` | **725** | **no `cogs/utility/`, no `views/utility/`** — undecomposed |

`channel` and `utility` are the two clearest targets. Both are Tier-1 for a
server bot (`utility` carries `!remind` and `!poll`, the two subsystems the
playtest mapping named as directly serving tester retention and feedback), and
both are the pattern the architecture doc names as the thing to fix.

**Debt is not marked inline.** Across 243,961 lines there are exactly **2**
`TODO`/`FIXME`/`XXX`/`HACK` markers. The debt ledger is
`architecture_rules/*.yml` — known-violation allowlists with reasons, which is
a materially better convention than scattered comments and is worth carrying
into any rebuild.

### 2.5 Recurring defect classes, from the 967-card corpus

Delegated read, every citation machine-verified (60 verified · 4 rejected — all
four rejects were claims emitted with no citation at all, correctly dropped):

- **Command-name collisions crash the boot.** *"This is the **second** such
  outage (the first was the `give` collision)"* — now guarded by a boot smoke
  test. A single flat command namespace is the hazard.
- **Unaudited mutation bypasses.** The save-fixes bug class; the invariant only
  scanned `channel_cog`, so bypasses elsewhere slipped through. Fixed with an
  AST audit-seam guard.
- **Attachment stranding on view transitions** (BUG-0025) — three instances.
- **Ledger drift** — merged PRs left marked pending, repeatedly.
- **Pinned-in-three-places drift** — tool versions, twice.
- **Wall-clock / subprocess tests race under parallel pytest** — two bugs, same
  shape.

Every one of these was converted into a checker or a test. That reflex — the
friction→guard law — is the most valuable thing in the repository and is not a
code asset at all.

### 2.6 The real gap, and it is in both codebases

Cog routing is stored, mutated with audit, given named batch profiles, shown in
the setup wizard and projected into the Access Map — and **never consulted when
a command runs**. Every caller of `is_cog_enabled` is a read. superbot-next
reaches the same state and says so. Two independent codebases, same hole. What
*is* enforced is `command_access` (`all_channels` / `selected_channels` /
`disabled_except_bootstrap`), which is a blunter instrument that gates *where*
commands work rather than *which*.

## 3. superbot-next — what is genuinely better built

Not a consolation list. These are things the rebuild does better than the
original, and a rebuild-of-the-rebuild should keep them.

**1 — The layered architecture with mechanical import guards.** `sb/spec` +
`sb/namespace` are stdlib-only grammar leaves; `sb/kernel` never imports
`domain`; `sb/domain/<key>` sits behind audited seams; `sb/app` is the
composition root. The direction is enforced by `tools/check_namespace.py`,
`check_symbol_shadowing.py`, `check_no_skip.py`, `check_config_usage.py`.
superbot's equivalent rules exist but carry tracked pre-existing violations;
superbot-next's are clean by construction. 634 files / 150,328 lines against
superbot's 883 / 243,961 for a comparable surface.

**2 — The manifest is the dispatch table.** This is the finding that overturns
the "photograph" reading. `sb/manifest/role.py` declares

```python
_cmd("roleinfo", HandlerRef("role.roleinfo"), aliases=("ri",), …)
```

— every `CommandSpec` carries the `HandlerRef` that actually routes. So when
`sb/domain/help/service.command_inventory()` walks
`pkgutil.iter_modules(sb.manifest)` reading `manifest.commands`, it is reading
**the live routing table**, and its docstring's claim — *"generated from EVERY
sb.manifest declaration (the single source; help can never drift)"* — is
structurally true, not aspirational. superbot cannot say this: its help tree
and its command registration are separate surfaces held in agreement by a
five-way identity contract and a startup validator.

**3 — Anti-drift by construction in the help rosters.** `category_rosters()`
computes membership from the live inventory, and a subsystem the category map
does not know **falls into an OTHER category instead of disappearing**. That is
the right failure direction, and superbot's orphan incident is exactly what it
prevents.

**4 — The verification and reconciliation discipline.**
`docs/status/completeness-table-2026-07-18.md` is the best status artifact in
either repository: every row hand-verified by reading *both* the oracle and
HEAD, cited `file:line`, with verdicts split into DONE / NOT-A-GAP / OPEN and
each OPEN carrying a **mintability** call. It marks itself point-in-time and
says to regenerate rather than amend. It also correctly distinguishes
"superbot-next ships a stub" from "superbot ships a stub and superbot-next
reproduced it byte-faithfully" — a distinction the golden harness makes easy to
lose.

**5 — Honest refusals over silent partials.** `cleanup`'s history-read leg
returns a declared BLOCKED refusal rather than performing a partial sweep. The
70 "not armed" terminals read as failure in aggregate but each one is a
deliberate choice to fail loudly.

**6 — Boot verification as a first-class gate.** `SB_VERIFY_BOOT=true` →
`{"verified": true}`, exit 0, without Discord. superbot has no equivalent
offline boot proof.

## 4. The help tree — the corrected diagnosis

### 4.1 What was measured, by importing and building at HEAD

`sb/domain/help/service.build_help_panels()` and `sb.app.main.load_live_manifests()`,
run in-container on python3.11, exit 0:

| Panel class | Count | Buttons | Selectors | Navigable? |
|---|---|---|---|---|
| `help.editor_*` | 6 | 2–6 | 0–1 | yes |
| `help.home` + `help.cat_*` | 10 | **0** | **1** | **yes — a working dropdown** |
| `help.sub_*` | **50** | **0** | **0** | **no — nothing to press** |
| **total** | **66** | | | |

Repo-wide, across 49 manifests: **314 panels · 153 with zero buttons · 115 with
neither buttons nor selectors.**

### 4.2 Two corrections that follow

**The true dead-end rate is 37% (115/314), not 48%.** The 48% figure counted a
panel with a working dropdown as a dead end. And the help tree's shape is
sharper than "60 of 66 have no buttons": the home and the nine category panels
navigate perfectly well by select. **The dead ends are exactly the 50
`help.sub_*` leaves** — and all 50 of them are dead.

So the navigation is `home (select) → category (select) → subsystem page`, and
the subsystem page is where it stops. **Two taps reach the page; there is no
third tap.** That answers the open question the brief carried forward: the
two-tap property holds for *reaching a page* and fails completely for
*activating a feature*.

An honest qualification, and it is the reviewer's point, not mine: to a user, a
dropdown that only goes deeper is a hallway, not an action. The 37% figure is
more precise than 48% and it does not make the bot better. The user-facing
truth is the last column of that table.

### 4.3 Why it is dead — and it is not transcription

Two providers render the text, and neither emits a component:

- `_ensure_category_provider` (service.py:180) space-joins the roster into one
  field per subsystem: `names = " ".join(f"`{n}`" for n, _ in …)`.
- `_ensure_commands_provider` (service.py:216) — **the leaf** — builds one
  embed field per command: `rows = [(f"`{name}`", summary or "No description.")]`.

Both read `_inventory`, which is computed from the manifest. **The content is
live and correct. Only the rendering is text.**

But "just buttonize the leaf" does not survive contact:

- `COMMANDS_PER_PAGE = 24`, and `_subsystem_panels` injects up to three
  `NavRouteSpec` routes ("More ▶", parent, home). Discord caps a message at 25
  components. 24 + 3 does not fit.
- And a button must *do* something. One-button-per-command means routing
  arguments, permissions and context through a component interaction for every
  command in the bot.

**The missing thing is curation, not buttons.** superbot's answer is 43
hand-written `build_help_menu_view` hooks, each choosing roughly seven
meaningful launchers out of a subsystem's full command set. The manifest has no
facet that can carry that judgment — no "featured actions", no primary/secondary
split. superbot-next's help is *more* automated than superbot's and *less*
useful for exactly that reason: auto-generating from a complete command list can
only ever produce a complete list.

That reframes milestone zero. It is not "add buttons to the help panels." It is
**"give the manifest a way to declare a subsystem's handful of front-door
actions, then render those as the launcher."** Contained, schema-shaped, and it
makes the rest of the navigation tree fall out.

### 4.4 Two more differences, from superbot-next's own 334 cards

Delegated read, citations machine-verified (22 verified · 2 rejected):

- **Navigation sends a new message; superbot swaps in place.** *"navigation
  sends a NEW message (the #295 precedent)"*. superbot's `HelpCategoryView`
  *"swaps the message in place to that hub's panel"* with a "↩ Back to Help"
  appended. A menu that replaces itself feels like one surface; a menu that
  posts a new message every hop fills the channel and loses the back-chain. This
  is small in code and large in feel, and it is worth deciding deliberately
  rather than inheriting.
- **The 25-option cap has already bitten the rebuild.** *"The cog-routing cog
  picker re-meets the oracle's #1040 bug class."* Discord's component and option
  ceilings are a recurring hazard in **both** codebases, which is the concrete
  reason § 4.3's "just add buttons" is not a plan.

## 5. Where superbot-next's `CAPTURE-WORLD LITERAL` problem actually lives

The four labelled files remain the known instances, and the sweep the brief
carries as open — *every module-level literal in `sb/domain/` that should be a
runtime read* — was **not run here**; it stays open. What this pass adds is a
boundary: the help tree, which the record placed inside that defect class, is
**outside** it. Its rosters are computed. The transcribed part of help is the
category topology only, and that is deliberate, ledgered as D-0055, and
explicitly parked pending the owner's hub-arrangement ratification.

The Cog Manager remains the genuine case and the worst one: 58 hardcoded
`superbot` module filenames in a tuple, status glyphs baked into the f-string,
and a legend advising `!cog` — which superbot has (`admin_cog.py:99`, owner-
gated, deliberately carrying **no** critical-cog protection because it is the
operator's escape hatch when the panel will not open) and superbot-next never
ported.

## 6. Corrections to the record

| Claim | Where | Reality |
|---|---|---|
| "The help pages render a **transcribed list** of command names — the captured *text* of the old bot's help output" | live-audit § 4b | **Wrong.** Computed live from the manifest, which is the dispatch table. The transcribed part is the category topology (D-0055, deliberate). |
| "153 of 314 panels — 48%" dead ends | live-audit § 4b | Counted panels with a working dropdown as dead ends. True neither-buttons-nor-selectors rate: **115/314 = 37%**. The 50 `help.sub_*` leaves are the real dead ends. |
| "61 extensions loaded (`config.py:111`)" | playtest § 2 | **59** at HEAD, AST-counted. |
| "Use the live superbot; do not deploy superbot-next" | playtest § 6 | Overridden by the owner the same day; the file carries no superseded note. |
| *This session's own:* "the defect is one line, `names = " ".join(…)`, so buttonizing is contained" | draft of § 4.3 | **Wrong on both halves.** That line is the *category* provider, not the leaf; the leaf is `_ensure_commands_provider`. And buttonizing 1:1 breaks Discord's 25-component cap at `COMMANDS_PER_PAGE = 24`. Caught by an adversarial Gemini review before it reached this document. |

The last row is the method working, and it is worth stating plainly: the
reassuring claim was the wrong one, and it was wrong in a way that a second
reading of my own citation would have caught.

## 7. Honest nulls

- **The `CAPTURE-WORLD LITERAL` sweep was not run.** Still open, still the
  right next audit, still cannot be settled by grepping a label.
- **Nothing was driven live in a guild this session.** superbot's reachability
  guard is static and says so; it cannot see hand-wired panel buttons, which is
  why five of its allowlist entries carry "verified by reading the cog".
- **The 37% figure counts declared components, not working ones.** A panel whose
  buttons all route to "not armed" still counts as having buttons. It is a
  floor.
- **superbot's per-cog panel quality was not assessed one by one.** 43 hooks
  exist; that they return curated launchers was verified on `role`, `moderation`,
  `utility`, `admin` and `starboard`, not on all 43.
- **The 967-card read is a delegated extraction.** Citations are verified to
  exist; that each claim follows from its quote is my judgement, and the
  categories were mine, so absence of a finding is not evidence of absence.
- **No game subsystem was depth-read**, by scope.
- **Whether superbot-next should be disbanded is not answered here.** § 3 is the
  evidence for keeping parts of it; § 4 is the evidence for what it would cost
  to finish. The call is the owner's.
