# 2026-08-05 · hub — establish what is actually true across fleet-manager, superbot and superbot-next

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: the previous session's every failure came from the same move —
reading code and inferring, while skipping both repositories' required boot
files. This session inverts it: read the documents first, trust them until they
contradict the tree, and run the one-command check whenever one exists.

## Previous-session review

PR #760 corrected the menu-parity claim and established that **the navigation
graph is the product**, not the command list — 60 of 66 `help` panels in
superbot-next have zero buttons. PR #759 recorded the live audit and the
`CAPTURE-WORLD LITERAL` finding. Both left explicit honest nulls (§ 9 of the
live-audit doc): the literal sweep was never run, and the two-tap reachability
property was never measured. This session picks up from those nulls.

## Scope

Three phases, strictly ordered — reading first, verifying second:

1. **fleet-manager** — the estate's history and terminal states, completely.
2. **superbot** — docs, a fair share of the 967 session cards, then the CODE:
   the help system, cog construction, helper files, how it fits together.
   Separate files that are sound from files that need work (server-relevant only).
3. **superbot-next** — same treatment, comparative: which parts are genuinely
   better built.

Deliberate non-scope: no bot code written; game subsystems noted but not
depth-read; the disband decision is the owner's; the rebuild plan is a later
session's job. This is the foundation, not the plan.

## What landed

- `docs/findings/2026-08-05-three-repo-state-audit.md` — the audit: fleet-manager's
  confirmed state and two drifts, superbot's navigation graph as a built system,
  superbot-next's genuinely-better parts, the corrected help diagnosis, and four
  corrections to the record (one of them this session's own).
- `docs/findings/README.md` — index row.
- `docs/findings/2026-08-05-playtest-discord-and-superbot-value.md` — superseded
  banner on § 6, the recommendation the owner overrode.
- `docs/planning/2026-07-26-consolidation-program.md` — §7 ledger rows closing
  the 07-26 → 08-05 gap; NOW pointer confirmed unchanged.
- `docs/CAPABILITIES.md` — two verified capability entries.
- `tools/gemini_delegate.py` — a Vertex path, so the binding Vertex-first
  directive holds for delegated corpus reads.

## Measured

**superbot already has the acceptance test the rebuild doc proposed inventing.**
`scripts/check_command_reachability.py`, built 2026-06-23, run at HEAD in a
python3.10 venv, **exit 0**: `242 prefix commands (95 reachable, 147 exempt,
0 GAP) — all member-tier commands are reachable ✓`. Never ported.

The graph is held up by three things: 43 per-cog `build_help_menu_view` hooks
returning **live curated launchers** (Role Hub = 7 buttons, not one per
command), `attach_standard_nav` in the base view's `__init__` — *"any panel
reachable by any command stays one click from Help and its hub"* — and one
`help_projection` seam replacing five divergent filters.

**The "photograph" reading of superbot-next's help is wrong.** Its command data
is computed from the manifest, and the manifest **is** the dispatch table
(`CommandSpec(route=HandlerRef(…))`). The transcribed part is the category
topology alone, deliberately, ledgered in that repo's decision register. The
missing thing is **curation, not buttons**: `COMMANDS_PER_PAGE = 24` against
Discord's 25-component cap means one-button-per-command cannot work, and no
manifest facet carries the judgement those 43 hooks encode.

Re-measured by building the panel tree: 66 help panels = 6 editor (buttons) +
10 with a working select (home + 9 categories) + **50 `help.sub_*` with
neither**. Two taps reach a page; there is no third tap. Repo-wide the true
dead-end rate is **115/314 = 37%**, not 48%.

Corpus: 967 + 334 session cards read via Vertex, 2.48M input tokens on credit,
82 findings verified / 6 rejected — all six rejects were claims emitted with no
citation at all.

## Verification

- `python3 tools/check_no_false_walls.py --strict` → **exit 0**.
- `python3 bootstrap.py check --strict` → **exit 0**, run **post-commit**.
- Both bot repos cloned read-only and built in-container (superbot python3.10 +
  `requirements.txt`; superbot-next python3.11 + `requirements.lock`
  hash-pinned). No bot was connected to Discord and no bot code was written.
- The Railway-held service account was written mode-600 outside any repository
  and the variables dump shredded; nothing secret entered the tree.

**Honest nulls** (carried into § 7 of the finding): the `CAPTURE-WORLD LITERAL`
sweep was **not** run and stays open; nothing was driven live in a guild; the
37% figure counts declared components, so it is a floor; curated-launcher
quality was checked on 5 of 43 hooks, not all 43; the delegated read verifies
that citations exist, not that claims follow from them; no game subsystem was
depth-read, by scope.

## ⟲ Previous-session review

PR #759/#760 did the hard, honest thing — booting the bot, then correcting its
own wrong claim about menu-parity the same day — and its § 7 list of five errors
is why this session started from the boot files instead of the code. What it
missed is that it never looked for prior art: it proposed a two-tap reachability
acceptance test as something to invent, while superbot has shipped exactly that
checker since June, with an allowlist and a gaps audit. The improvement that
follows is a habit, not a tool: **before proposing a mechanism, grep the oracle
for it.** superbot holds 244k lines of solved problems, and the rebuild's job is
to port the solutions, not re-derive them.

## 💡 Session idea

**Give the manifest a `featured_actions` facet.** The whole navigation defect
reduces to one missing piece of schema. superbot encodes "which six of this
subsystem's twenty commands deserve a button" in 43 hand-written methods —
irreproducible by any generator, because it is a judgement, not data.
superbot-next's manifest can express a command, its route, its aliases and its
tier, but not its *prominence*. So its help can only render everything, and
everything does not fit behind buttons.

One optional field — an ordered tuple of the handful of routes that are a
subsystem's front door — turns the auto-generated leaf page from a text list
into a launcher, mechanically, for all 49 subsystems at once. It also gives the
reachability guard something to check: a subsystem with no featured actions is
one nobody can reach by clicking. That is the smallest change that converts the
rebuild's biggest weakness into its structural advantage — because the thing
superbot pays 43 hand-written methods for, the manifest would get once.
