# The fresh-start redirect — the plan's execution target becomes a new hub; this repo becomes the archive

> **Status:** `plan` — owner-settled direction from the live 2026-08-29/30
> sitting, captured as **plan input** ([D-0025]; the one-PR guideline decided
> the same night is [D-0024]). Nothing is created or moved by this document:
> no new repository exists, no file migrates, and forward-only placement
> discipline governs the meantime. The target tree, the distillation
> checklist and the cutover checklist belong to the dedicated planning
> sessions this document feeds.

## The directive, his words

*"The plan that we are planning should be redirected towards a fresh start."*
And the trigger, from his own fresh-eyes test — he cloned this repo into
VSCode, browsed, and could not follow it: *"no matter how good your map is,
if you always have to read it before being able to navigate the repo that
means something is very wrong."* Measured the same hour: `docs/audits/`
holds 2 audits while 7 audit-named documents sit in `docs/findings/`;
`docs/` has 80 top-level entries; and `docs/_merge_verification_2026-07-15.md`
— whose own text says *"it can be deleted once verified"* — sat at top level
for six weeks after its purpose ended (deleted in the PR that lands this
document). His design criterion, which becomes the acceptance test below:
*"I'm fairly certain that with a good folder and file structure, an agent
would be able to understand what's going on globally just by looking through
the folders and reading the filenames."*

## Why a fresh start and not a reorganization in place

Reorganizing in place breaks citations at scale (this repo is
citation-dense; the estate's own convention for moves is permanent stubs). A
fresh start whose records never move breaks no **inbound** citation: **the
old fleet-manager becomes the archive** — read-only, permanently linkable,
every card and finding exactly where every existing link expects it — and
the new hub starts with only the distilled living core, born in the
intended structure. The one link class that does break is the carried
documents' own **outbound** relative links (`docs/CAPABILITIES.md` and
`docs/owner-queue.md`, for example, link relatively into `findings/`,
`audits/` and `planning/` — copied whole, those would resolve inside the
new hub where the targets don't exist), and the carry step owns it: at seed
time every relative link in a carried document is rewritten to a permanent
archive URL, or the entry is distilled rather than copied. Mechanical and
enumerable, and named in the carry-cut below. The owner's archive ask and
his fresh-repo ask solve each other.

**And the counterweight, his too** (same sitting): *"some parts of the fleet
manager repo are pretty well organized after all."* True, and load-bearing
for the design: the areas that grew against a declared contract stayed
navigable — `.sessions/` (dated cards, a grammar README), `docs/repos/<name>/`
(one folder per repo, an entry-point contract), `docs/planning/` (dated docs,
an indexed README), `docs/owner-comments/<repo>/` (a schema and a lifecycle)
— while the areas without one sprawled (`docs/` top level, the audit/finding
split). The fresh tree therefore does not start from zero: it generalizes
the contract-per-folder pattern that demonstrably worked here, and the
well-organized areas are the first carry candidates.

## What killed the last rebuild, in his words — and what is different now

His account of the EAP superbot rebuild (2026-08-30, verbatim): *"the
sessions working on it have all been subsessions of the Project coordinator
chat … the coordinator then relays that back to its subagents in it's own
words, the subagent does not think it's own coordinator is a trustworthy
source and starts questioning everything … I ran these projects with as
little steering as possible too … the occasional 'continue' after the
sessions claimed that the work was 'completely done, the executable work
queue is exhausted' and when I then went to look what was done it was not
nearly anything you could call done at all. The fact that the rebuild
coexisted was because the rebuild was claimed as done but did not even come
close to functioning like the original, which is why it was never possible
to make the switch."*

The estate's record corroborates the done-claim half with the mechanism
measured (`repos/superbot-next/README.md`): golden parity read **533/533
green** while capture-world literals shipped as constants and 60 of 66 help
panels had no buttons — *"golden-parity green must not be read as ported."*
The instrument said done; the thing was not.

| what killed it then | what answers it now |
|---|---|
| coordinator-relay indirection (owner → coordinator → subagents, re-worded; trust decayed at each hop) | the relay no longer exists — the autonomous-Projects program closed 2026-07-21; everything runs as direct owner-live sessions |
| minimal steering ("continue" against a boot prompt) | the owner will personally watch and manage this rebuild (his stated intent), and the turn-based planning sittings are already that |
| "done" claims no instrument could falsify | a falsifiable acceptance test gates the cutover (below), and nothing seeds the new hub without a certainty tag |

## His sequence (verbatim intent, ordered)

1. **Finish the plan as well as possible** (the current planning sittings).
2. **Establish a baseline of trustworthy information** from fleet-manager
   and the other repos — *"we need to perform multiple audits again, but
   only if the information has changed so far"* — re-audit only where state
   moved since the 2026-08 audit wave; carry certainty tags per the
   `MEASURED/OWNER/…` legend on every seeded claim, or the claim does not
   seed.
3. **Build the right skills, hooks and gates** (the common operating
   protocol — the roadmap's Phase 3 — plus this sitting's designs).
4. **Seed the new repo's working context** from that baseline; possibly a
   new name (open).
5. **Active consolidation passes from birth** — *"we had those in superbot
   aswell and they were really helpfull"* — periodic planned sessions, fed
   by the initiative queue, not ad-hoc.

## Structure first, gates kept — the sequencing he argued and this doc adopts

His challenge, granted: *"it would be foolish to create detailed skills and
forced working methods while doing all that inside a repo that doesn't have
any structure at all."* The refined split this direction rests on: the
estate's rules are of two kinds. **Navigation-compensation rules** — the
six-read order, the doc-routing table, the map itself — exist because the
tree fails; in a right-shaped repo most of them shrink or become generated
views, which is why he has had to say *"go look in section X"* to agents who
then found no section X. **Practice gates** — born-red, verification before
fold, review-before-flip — exist because prose-demanded practices died even
when well-organized (the genesis measurement; the never-run fleet-preflight
skill was well-written). The new hub is born with the kit and its gates in
the first commits, and with the intended tree making most of the
compensation layer unnecessary. Neither substitutes for the other.

## Birth rules (decided this sitting; retrofits here become defaults there)

The initiative loop (the 2026-08-29 design: detectors → dispositions → one
queue with durable retirements), the required session-identity line (the
2026-08-29 grammar decision), the one-main-PR-per-session guideline
([D-0024]), placement contracts per folder
with write-time delivery and an advisory placement checker, and the
name-your-red-at-birth rule for everything tier-(c) auto-built. The
apparatus migrates via the kit plus the local-delta manifest the estate
already maintains (`SKILLS-local.md`'s ⚠ re-apply table).

## The acceptance test (gates the cutover)

The new hub is ready when a **cold agent given no map and no mandatory read
list** orients from the tree and filenames alone: states the repo's purpose,
era, current work and next step, and correctly places three test documents
into the folders where they belong — blind-scored, the §4.8 fresh-agent
method (producer + independent scorer). The owner's browsing test is the
human half: he finds a named document without opening an index.

## Addendum — the owner's structure sketch (2026-08-30, pre-sleep), with the consults he invited

His words before sleep, captured so tomorrow starts from them: root-minimal —
*"Eventually I don't thing there should be any files at root level, with a few
minor exceptions"*; an `AGENTS.md` at root *"which gives some basic rules and
routes claude to claude.md and chatGPT to a codex.md"*; *"a clear README.md
and a repo map, this time one that can just clearly point at well structured
and properly used folders"*; *"Each folder gets it's own README.md which
explains what the use of that folder is and which things there should or
shouldn't be"*; and the archive — *"a comprehensive archive system that
accounts for project scope and time, so if it's been weeks since something
was written and there is currently no active project using it, something
should move to an archive folder, the archive folder should basically be a
clone of the repo with the same folders inside it, but all of them archived,
so if you look for an archived file it's still just as easy to find."*
Urgency, revised by his own second look: *"it's not as urgent as I imagined
… the logical entrypoints and root directories are the worst looking."*

**Session analysis.** Root exceptions in practice: README, AGENTS.md,
license-class, and tool-required roots (the kit's `bootstrap.py` sits at
root today — whether the new hub can nest it is a kit question for the
plan). On routing: `AGENTS.md` is the emerging cross-vendor convention that
Codex-class tools read natively, so the sketch's `codex.md` may be one hop
more than needed — `AGENTS.md` itself can carry the Codex-facing content,
with one line routing Claude readers to `CLAUDE.md` (which Claude Code
auto-loads regardless; the routing line serves readers, not loaders). A
separate `codex.md` earns its place only if Codex-specific content should
not live in the vendor-neutral file. Per-folder READMEs are the placement
contracts of layer 1 above — convergent, and the old repo's evidence backs
them. The archive mirror is the **new hub's immune system** against becoming
this repo: the old repo stays the frozen archive of the past; the new hub's
`archive/` is the rolling archive of its own aging material. The move rule
(weeks-old + no active plan references it) is mechanizable as a **flagging**
checker feeding the initiative queue — never an auto-move.

**The Gemini consult** (free-key route, adversarial, run the same night at
his invitation). Its findings worth designing against:

1. **Search pollution** — a same-structure `archive/` doubles every
   glob/grep hit and feeds stale records into agent context. The Codex
   round sharpened the fix: the exclusion must live in the search tools'
   **actual ignore configuration** (`.rgignore`/`.ignore` — never
   `.gitignore`, since archived files must stay tracked), with the opt-in
   for deliberate archive searches documented in `AGENTS.md`; a convention
   written only in `AGENTS.md` asks cooperative agents to remember and
   changes no tool's default.
2. **Stub accumulation defeats the cleanup it serves** — per-file stubs are
   the clutter, one generation later. Candidate, with the precondition the
   Codex round added: no per-file stubs inside the new hub **contingent on
   the mover running a repository-wide inbound-reference check and
   rewriting every link it finds** (the same mechanical pass the carry-cut
   already owns — a derivable archive path helps only readers who already
   know the move happened; it repairs no link). A stub remains only where
   a reference cannot be rewritten (external citations).
3. **Mirror drift** — renaming or splitting an active folder breaks the
   mirror's symmetry; the design must say whether `archive/` reflects the
   tree-at-archive-time or tracks renames.
4. **Reference-lock deadlock** — *"no active project uses it"* needs a
   machine-readable definition, or one stale plan reference locks a file
   active forever and the lifecycle engine freezes.
5. **Per-folder README cost** — dozens of metadata files burned into agent
   context on recursive tasks; keep each to one screen and generate the map
   *from* them.
6. **Routing split-brain** — multi-hop `AGENTS.md → codex.md` indirection
   risks per-vendor divergence; converges with the analysis above (flatten
   to `AGENTS.md` + `CLAUDE.md`).

Down-weighted, with reasons: its merge-conflict worry (the one-PR guideline
and flag-don't-move keep archive moves in deliberate single sessions) and
its provenance worry (git history carries the timeline; the mirror only
relocates the working view).

**Open for his morning, from the sketch + consult:** stub-or-no-stub inside
the new hub · the machine definition of "an active project uses it" ·
whether session cards — born as records — skip the aging rule or are born
archive-tier · `codex.md` folded into `AGENTS.md` or kept separate.

## Open — owner to confirm; not yet his verbatim

- **The hard-cutover rule:** this repo archives (read-only on GitHub —
  platform behavior to verify at execution time, not assumed) the day the
  new hub passes acceptance; no coexistence window. His account implies it
  (cutover failed before because the replacement never worked; this one
  cannot ship unverified) — recorded as intent pending his explicit yes.
- **The carry-cut:** proposed tier-based — living ledgers (decisions,
  capabilities, owner-queue) and still-binding conventions carry whole
  **with their outbound relative links rewritten to permanent archive URLs
  at seed time** (the link-rewrite pass above); cards, findings, audits and
  seat-era apparatus stay archived, reachable by link. He mentioned seeding
  *"from fleet-manager and the other repos"* — wider than this repo; the
  baseline audit scopes it.
- **The name.**
