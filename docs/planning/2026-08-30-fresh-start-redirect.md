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
fresh start whose records never move breaks nothing: **the old fleet-manager
becomes the archive** — read-only, permanently linkable, every card and
finding exactly where every citation expects it — and the new hub starts
with only the distilled living core, born in the intended structure. The
owner's archive ask and his fresh-repo ask solve each other.

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

## Open — owner to confirm; not yet his verbatim

- **The hard-cutover rule:** this repo archives (read-only on GitHub —
  platform behavior to verify at execution time, not assumed) the day the
  new hub passes acceptance; no coexistence window. His account implies it
  (cutover failed before because the replacement never worked; this one
  cannot ship unverified) — recorded as intent pending his explicit yes.
- **The carry-cut:** proposed tier-based — living ledgers (decisions,
  capabilities, owner-queue) and still-binding conventions carry whole;
  cards, findings, audits and seat-era apparatus stay archived, reachable by
  link. He mentioned seeding *"from fleet-manager and the other repos"* —
  wider than this repo; the baseline audit scopes it.
- **The name.**
