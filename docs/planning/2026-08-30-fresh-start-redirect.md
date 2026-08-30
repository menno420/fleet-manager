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
doc-routing table, and a map that exists because 64 top-level files cannot be
scanned by eye — arise because the tree fails; in a right-shaped repo they
shrink or become generated views, which is why he has had to say *"go look in
section X"* to agents who then found no section X. **The required reading
order is NOT in this class** — corrected 2026-08-30, owner-live: *"There
should be a required reading order."* An entry point is orientation, not
compensation; see § *The acceptance test* for the restatement and [D-0032]. **Practice gates** — born-red, verification before
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

**Restated 2026-08-30 (owner-live) — the earlier wording said the opposite of
what he meant.** It read *"a cold agent given no map and no mandatory read list
orients from the tree and filenames alone"*, and § structure-first named *"the
six-read order"* among the compensation rules expected to dissolve. Taken
together those would have told a future session to delete the reading order.
His correction, verbatim: *"There should be a required reading order. What I
meant is that when an agent does its reading/orientation, it automatically
notices which other files except for the reading order are also worth reading
into or at least being made in such a way that if I later mention something,
that the agent knows that certain things are written in logical places, making
it faster for me and the agents to navigate."*

So the required reading order **stays**, and the test measures **findability**,
in two directions:

- **Retrieval (the scored half).** Name a topic the owner would plausibly
  mention in chat — the Gemini notebook route, the archive rule, what
  `spider-swing` is for, the Codex review cadence — and a cold agent resolves
  each to one folder **before** searching. This is the direction that costs him
  time daily, and it had never been tested.
- **Placement (the secondary check).** Given a new document, the agent files it
  where it belongs. Tested 2026-08-30 on the tree-only cold read: 2 pass, 1
  fail.

Both blind-scored by an independent agent, per the §4.8 producer + scorer
method — a self-scored run does not meet this bar, which the 2026-08-30
tree-only read notes about itself. The owner's browsing test is the human half:
he finds a named document without opening an index.

**What is compensation, stated narrowly** so this is not over-read again: a map
that exists because 64 top-level files cannot be scanned by eye; a routing hook
that fires because a session would not otherwise find the provider doc; his
having to say *"go look in section X"* because the filename did not say it. An
entry point is not compensation.

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

## Answered — the 2026-08-30 morning sitting (his words, verbatim)

The § Open items below and the addendum's four questions were put to the owner
one topic at a time on the morning of 2026-08-30. What he settled:

**The hard cutover — agreed, and split in two.** The session proposed
separating the *write cutover* (the day the new hub passes acceptance, all new
work goes there — absolute, no exceptions) from the *GitHub archive flag* (a
mechanical step that may lag by days without creating coexistence, since
coexistence is about where work happens, not about a flag). Owner: **"Agreed."**
The reasoning behind the split is that his own EAP account names the fake
"done" as what killed the last cutover, not the coexistence itself —
coexistence was the symptom of a replacement that never worked.

**The carry-cut — agreed, with the separation stated as a principle.** His
words: *"Yes, I think we should be very strict about how historical records or
finished work should be documented. I don't think it's a good idea to leave
historical and current work in the same files like you said is now true in
owner-queue."* So the proposed three verbs stand — **carry whole** (copied
as-is, outbound relative links rewritten to archive URLs) · **distill**
(rewritten fresh in the new hub, the long-form original archived and linked) ·
**archive only** (stays put, reachable by link, nothing copied) — and the
middle verb is the one his principle requires: `owner-queue.md` and
`CAPABILITIES.md` are live *and* historical in the same file, which is exactly
what he does not want carried forward.

**Seeding scope, his words:** *"Seeding comes mostly from fleet-manager and
superbot, tho some of the newer repos will have to add something aswell but
mainly for the router/summary sections."* So the baseline audit is not
estate-wide-equal: fleet-manager and `superbot` are the substantive sources;
the newer repos contribute to the router and summary layers only.

**The name — leaning `estate`, not yet confirmed.** His words: *"I think
'estate' might be a good call, I was personally considering calling it
'structure' but I feel like that name would make it a bit ambiguous to
discuss."* His rejection reason is worth keeping: a repo named `structure`
cannot be discussed without collision ("the structure of `structure`").
`estate` is already his own vocabulary (`docs/ESTATE.md`) and names the thing
rather than a mechanism — which is how `fleet-manager` went stale, naming a
seat architecture retired 2026-07-21. **Recorded as leaning; the confirming
word is still owed.**

**Stubs inside the new hub — agreed, with the precondition made mechanical.**
No per-file stubs, contingent on an inbound-reference rewrite pass; and the
pass is a **tool, not a discipline** — `tools/archive_move.py` scans the repo
for inbound references, rewrites every one, then moves the file. Moving a file
any other way is out of contract. A stub remains only where the reference is
external and cannot be rewritten. (The owner asked for this in plainer
language and agreed on the restatement; the reason it must be a tool is the
estate's own record that prose-demanded practices die.)

**"An active project uses it" — his definition replaces the mechanical one,
and changes what the rule is for.** His words: *"I think it should mean that
the value the file holds is gone. So a file could sit untouched for 2 months
and still not be archived as long as there are still certain things in there
that are required for something that we plan on doing. But to prevent things
from sitting around too long, there should probably be a script that surfaces
these kinds of files that have been unused for a while."*

This supersedes the session's proposed rule, which **decided** archive
eligibility from a reference test. His splits the mechanism in two: a script
**surfaces** candidates on a cheap mechanical proxy (untouched for N days —
**N = 30** as his starting figure: *"30 days is probably a good start"*), and a
person or session **judges** whether the value is gone. It also dissolves the
reference-lock deadlock more cleanly than the proposed rule did: a file held by
a stale plan reference simply appears on the candidate list and someone says
the plan is dead — the reference is context, never a veto. Convergent with the
already-decided flag-don't-move rule. Design note added by the session: the
candidate list must carry *why* each file surfaced (days untouched, what still
links to it), or the judgement costs an investigation and gets skipped.

**How the pin is expressed — his words:** *"I think maybe a bit of both, one
list that names them all, automatically arranged by a scrip that fetches the
info from the files."* So: the marker lives in each file's header, the roster
is generated from the markers, nobody hand-edits the roster. Same shape as
`docs/owner-comments/*/README.md` and `docs/planning/idea-backlog.md`, the two
generated indexes this estate already relies on.

**When the check runs — open; he asked for a suggestion.** His words: *"Not
entirely sure. what do you suggest?"* The session's suggestion, awaiting his
word: neither a cron nor on-demand, but **as one more detector inside the
initiative loop's end-of-session hook** (slice S2 of the initiative-loop
design — *not yet built*).
Three reasons: it is the same shape (mechanical detector → surfaced candidate →
agent disposition), it fires at the one moment an agent with loaded context is
present to make the value judgement his definition requires, and it keeps one
surfacing mechanism rather than two.

**Session cards — archived on a clock, and read more than they are now.** His
words: *"Yes, these cards should be consistently archived. But also, there
should be more effort spend reading them. Maybe each new session should read
the last 3 session cards each time, and the session cards should be written in
such a way that they hold valuable information in a concise way. So it doesn't
take too much context or time for an agent to read them, but would help an
agent understand what the current work has been."*

Two design notes from the session. First, this **strengthens an existing
contract rather than adding a rule**: `.sessions/README.md` already requires a
*Previous-session review* marker on every card; his version raises one to
three. Second, concision needs structure, not exhortation — the proposal is a
required short block near the top of every card (*"What the next session needs
to know"*, 3–5 lines, written for someone who was not there) with the
long-form record below it, so reading three cards costs about fifteen lines.
That also fixes a mismatch his ask exposes: cards today are written as records
*of* a session, not briefings *for* the next one. **This card is the first
written to that shape.** Card volume, measured 2026-08-30:
`ls -1 .sessions/*.md | wc -l` = **453** — the largest single document class in
the repo, which is why they age on a fixed clock rather than on the
reference test.

**Per-vendor instruction files — his direction, superseding the session's
fold-into-`AGENTS.md` proposal.** His words: *"I'm not entirely sure, all I
know is that I think it's important that we have a way to separate the
instructions for the different types of agents. So we should also have a
grok.md and gemini.md, tho gemini itself does not see a repo as you or the
other AIs would. so for that I have another solution. We can add this repo to a
notebook or to google Drive, which does make it an extra part we need to
maintain, but I think this will not be that hard since it can be as easy as
just completely re-cloning the repo into there each time I intend to talk to
gemini about it etc."*

The session had argued for folding `codex.md` into `AGENTS.md`; his reason for
separation generalises past Codex to Grok and Gemini, which that proposal had
no answer for, so separation wins. The risk it introduces is split-brain —
four vendor files each drifting into their own version of a shared rule — and
the design answer is a strict division of labour: **`AGENTS.md` carries every
rule that applies to all agents** (single source of truth, vendor-neutral),
and **`CLAUDE.md` / `codex.md` / `grok.md` / `gemini.md` carry only the delta**
(how that agent loads context, what access it has, what its surface cannot do).
The rule that keeps it honest: a statement appearing in two vendor files
belongs in `AGENTS.md` — checkable by duplicate-paragraph detection across the
four, flag-only.

**What the Gemini half already has here, and the constraint it comes with.**
His Drive/notebook solution is largely built: `tools/build_notebook_bundle.py`
(added 2026-08-23, hardened against nine `@codex` findings on fm #934)
enumerates tracked files only, converts what a notebook cannot ingest,
flattens paths into filenames because the filename is the citation label, and
partitions rather than merges; `docs/providers/gemini-notebook.md` carries the
convention, and `OQ-GEMINI-NOTEBOOKS` is his own standing queue entry. Its
recorded caps: **50 sources per notebook** (`MEASURED`, Google's FAQ) and
**300 on PRO** (`OWNER`, read off the Dutch splash, not on the fetched FAQ
page and not established for the standalone surface). Its § built table records
`curious-research` at 110 sources → 1 notebook and `idea-engine` at 779 → 3
notebooks split 300/292/190, so a corpus over the cap **partitions cleanly
rather than failing**. Two design consequences: the archive must be excluded
from the bundle (the `CORPORA` table at `tools/build_notebook_bundle.py:81`
takes `exclude_exact` paths only, so a subtree exclusion needs a small code
addition, not just config); and `gemini.md` is two documents, since Gemini
reads a flat pile with no tree, no git and no dates — instructions to *us* on
preparing its context, and **an orientation source that goes into the notebook
as source #1** saying what the snapshot is, when it was taken, and that
anything later is invisible to it.

**Mirror drift — frozen, and the real fix is upstream.** His words: *"Yes I
kinda agree, tho I also think we should make sure that there don't have to be
any renames along the way."* Both halves are adopted. The archive mirrors the
tree **as it was at archive time** and does not track later renames — tracking
them would rewrite archive paths and destroy the one property the archive
exists to provide. And his upstream point becomes a design requirement: folders
are **named by role, with the set of roles exhaustive**, so every document has
one obvious home and nothing forces a rename later. The failure this repo
already demonstrates is `docs/audits/` vs `docs/findings/` — neither name
wrong, the taxonomy simply never closed, so material landed by feel. Because
the archive freezes, a post-cutover rename is expensive; the naming decision is
therefore free only now, during planning, which argues for a dedicated pass on
the folder tree before anything is created.

**The review-cadence amendment — confirmed.** His words: *"Yes,
agreed."* Written into the cadence entry — stamped in [`docs/decisions.md`](../decisions.md), whose citing home is
`conventions/vertex-first-for-gemini.md` — in the same PR as this section.

## Still open after this sitting

- ~~**The new hub's name**~~ — **✅ SETTLED: `estate`**, later the same day;
  stamped in [`docs/decisions.md`](../decisions.md), cited from `owner-queue.md`.
- ~~**When the archive-candidate check runs**~~ — **✅ SETTLED** ([D-0029]): a
  detector inside the initiative loop's S2 end-of-session hook, not a cron and
  not on-demand.
- **The idea-queue cap** — **✅ RECORDED** in the decision register (50
  provisional; it
  triggers a review, never blocks recording; it counts undisposed ideas).
  His proposal, verbatim: *"the ideas that agents
  should create at the end of a session. These shouldn't stack too much either,
  we should have a maximum amount, maybe 50 ideas at most at any time. If there
  are more than 50 there has to be a dedicated session discussing them with me
  and deciding which ones to keep, which ones to discard and which ones we
  could possibly execute immediately. Tho preferably these ideas should be
  discussed even sooner, or at least be made visible in a more efficient way."*
  The session's response, with him: the cap should **trigger a review, never
  block recording** (a hard stop at 50 makes an agent at #51 either suppress a
  good idea or discard one without judgement); the cap must count **undisposed**
  ideas, not harvested ones, since the backlog is generated and regenerates
  (the initiative-loop decision's item 5 provides the durable retirement
  source that makes that countable);
  and *"discussed even sooner"* is the more valuable half, best served by a
  sharper trigger than raw count — an idea surfaced in three consecutive
  sessions without disposition is more informative than the pile reaching an
  arbitrary size.
  **The measurement problem, `MEASURED` 2026-08-30:** the count does not
  currently exist. `docs/planning/idea-backlog.md` reports *"57 idea block(s)
  across 350 card(s) · 4 ungroomed"*, `generated-at 2026-08-11T18:01:58Z`, and
  its own header states the harvest is *"the BULLET form only"*, that *"the
  majority conventions … are NOT harvested"*, and that the figure is *"a floor
  over one formatting style, never a measurement of the corpus"* — against 453
  cards today. The initiative-loop design's slice **S1** is the fix
  ([`2026-08-29-initiative-loop-design.md`](2026-08-29-initiative-loop-design.md)
  § Implementation slices). Whether the undisposed count
  is near 50 is unknown, and the one weak signal available (4 of 57 ungroomed,
  ~7%, via a groom-detector the header itself tags unverified) argues **against**
  an immediate breach rather than for one.
- **A dedicated folder-naming pass** — **✅ AGREED as the next sitting**, on the
  C2 reasoning above: the archive freezes, so a post-cutover rename is
  expensive and the naming decision is free only during planning. Nothing is
  designed for it yet; the session that takes it should arrive with a proposed
  set of role-named folders and what each folder's README would declare, for
  him to cut and correct rather than invent.

## What he asked for that this sitting built

**A folder directed at him** — his words: *"We should create a folder directed
at me, so I can see everything that needs my attention at once."* Built as the
generated `owner/README.md` ([D-0027]), swept from the owner queue, the intent
documents' ❓ markers, the owner-guidance documents, the idea backlog and the
unconsumed owner comments. It is a **carry whole** item when `estate` is seeded.

**The documents he could not find** were `docs/repos/<repo>/intent.md` —
`spider-bot`, `spider-swing` and `substrate-kit`, all three written 2026-08-28,
all `Status: owner-guidance`, carrying 10 ❓ questions addressed to him — plus
`docs/intent.md` for fleet-manager itself, against the 28 repositories the
owner-comments checker enumerates. The prepared prompts are
`docs/planning/2026-08-28-owner-intent-questions.md` (167 lines, 12 sections),
tracked as `OQ-INTENT-WRITE-UP`. **Why he could not find them, `MEASURED`
2026-08-30:** grepping the per-repo intent path across `README.md`,
`docs/MAP.md`, `.claude/CLAUDE.md`, `docs/repos/README.md` and
`docs/current-state.md` returns **zero** hits — including `docs/repos/README.md`,
the index of the very folder they live in. The only pointer in the tree is
inside `docs/owner-queue.md`.


## Answered — the 2026-08-30 afternoon sitting (his words, verbatim)

Continuing the same day. Four packages settled, each recorded here because the
mechanisms they describe are not yet built and the [D-0022] hold governs.

### Session-card grammar and the idea marker

His observation, and the correction the measurement made to it: he recalled
*"some where marked with an emoji and some marked by text."* Measured across
all 453 cards — **452 carry the 💡 marker and 0 are text-only**. The
inconsistency is the *shape around* the marker: bullet (59) · heading (198) ·
paragraph-start (206), counts overlapping. And the damage is larger than the
inconsistency: `scripts/gen_idea_backlog.py:70` harvests
`BULLET_RE = ^- (?:\*\*)?💡` only. Counted as **blocks**, which is what S1
has to recover: **59 bullet blocks are harvested and 409 structural blocks are
invisible** — 197 heading blocks plus 212 paragraph-start blocks. (Corrected
after Codex review on fm #988: an earlier draft said 391, which counted
*cards* rather than blocks — five cards carry several paragraph-start ideas —
and included one H1 title in `2026-07-19-fm-evening-groom.md` that mentions 💡
without being an idea heading. Sizing S1 on 391 understates the recovery by
18.) By card, 59 of 452 are harvested; just 2 cards carry an inline mention
alone.

His mechanism: *"a hook triggers at the end if session which prompts a skill
that tells each session exactly what to write down in the session cards etc."*
Agreed, with the split the estate's own record requires:

- **Not a second hook** — extend [D-0021]'s slice **S2** (the initiative skill
  and its non-blocking end-of-session hook). Two hooks at the same moment
  compete for one session's attention.
- **Form goes in a checker, not the skill.** `scripts/preflight.py` already
  enforces [D-0023]'s `🔗 Session:` line on added cards, locally and in CI;
  the idea marker extends that lane. A skill can be skipped; a gate cannot.
- **Substance goes in the skill** — what is worth writing down is judgement no
  checker can score.
- **Canonical form: the bullet** `- 💡`. One line, one idea, unambiguous
  boundary; the heading and paragraph forms have no end delimiter, which is
  why a machine cannot find where they stop.
- **No backfill.** [D-0021]'s slice **S1** teaches the harvester all three
  forms — that is what recovers the 391 — and the 452 existing cards stay as
  they are, per [D-0023]'s record-tier precedent.
- **Required with an honest null**, the [D-0023] shape, his call: *"Yes I think
  I agree with those suggestions."*

### The honest null does work: retire, don't vote

His proposal: *"if there is no idea then a session should possibly give another
idea a +1 to move it up the queue or something."* Argued against and he
accepted the alternative. Three reasons a raw +1 fails: it makes the null
expensive, so fabricating a throwaway idea becomes the cheaper path; agent
votes are not independent (one model, one repo, one list order — forty votes
are one opinion sampled forty times, and top entries get read most so they
stay top); and a tally is a script-computable proxy standing in for exactly the
judgement he reserved for humans in the archive rule.

What replaces it, in preference order — **a new idea** · **a retirement with a
stated reason** · **`nothing this session`**, the third staying free so no
session is pushed into fabricating either an idea or a kill. The null points at
the cap rather than the ordering: with the queue heading from 57 toward ~450
once S1 lands, ranking is hopeless and pruning is the only thing that helps.
[D-0021] item 5 already permits any session to retire an idea with a stated
reason, and the retired entry stays *displayed* — so a wrong kill is one line
to reverse.

His addition, verbatim: *"when a session retired an idea it should state it
clearly in the chat and in the session card."* Three places, and they are not
redundant — **the chat** (which is what makes his *"he spot-checks kills"* in
[D-0021] item 5 possible at all), **the session card** (which session killed
it, beside what else it did), and **the durable disposition source**. The third
is load-bearing and does not yet exist: `gen_idea_backlog.py` reads only
`.sessions/*.md` and `docs/planning/*.md`, and contains no disposition concept,
so a retirement written only in a card leaves the idea **re-harvested from that
same card on every regeneration**. Building that source is S1's job.

### One question per file

His rule: *"each folder should be split into multiple sub folders, so instead
of reading a 500 line file, you see for example 10 50 line files."* The evidence
is a failure in this session: asked whether ChatGPT Work could open a PR, the
answer sat at `docs/execution-surfaces.md:137` and again at 203–206; the file
was opened, the grep pattern matched those lines, and `head -50` discarded
**56% of a 114-line result** that contained the answer, which was then reported
as unverifiable. His reading of why structure beats instruction: *"even tho not
all rules get followed even if they are currently in an agents context. I do
know that you are programmed to investigate, and if you have the obvious names
in front of you that match a certain task, I'm pretty sure that will make it a
lot easier for you to search efficiently."*

Measured across `docs/` + root: **371 files, median 132 lines, and 75 files
over 300 lines holding 57% of all prose** — more than half the words sit in the
fifth of files nobody reads whole, `owner-queue.md` (2,161) and
`CAPABILITIES.md` (2,136) at the top.

The rule, with the constraint that keeps it from backfiring: **split by
question, not by size.** Sections answering different questions split; sections
that are instances of one question stay together, because splitting a
comparison destroys it — `execution-surfaces.md` is a comparison between
surfaces and must not become five files. **Append logs split by subject, never
by date**: chronology lives in git history, the same principle as the archive
manifest. And `fleet-triage.md`, whose 52 sections are dated sweeps rather than
per-repo entries, is not a split candidate at all — it is seat-era history and
archives whole.

### Naming, folder READMEs, and what actually leaks

His rule: *"Each file should have a proper name that defines what the purpose
is in as little tokens as possible. And the readme of the main folders should
explain in a little more depth what everything is supposed to do, and same
thing, better to have more small readmes than one large one."*

Measured, and the surprise is that **both halves are already implemented here**:
median filename is **2 words**, and **62 of 68** subfolders under `docs/`
carry a README — **6 uncovered**. (Corrected after Codex review on fm #988:
an earlier draft said 62 of 65, a denominator that silently dropped three
tracked directories for containing no Markdown — `docs/audits/2026-08-10-full-read/raw`,
`docs/experiments/tools`, `docs/prompts/v3/tools` — even though the folder
contract applies to them too. 62 of 68 with six uncovered is materially weaker
evidence that the rule is "already implemented" than 62 of 65 was.) So neither is the missing piece, and two refinements
matter more than the rules themselves:

- **Short is not the goal; answering a question is.** `traps.md`,
  `ownership.md`, `q-index.md` and `fence-index.md` are all short and none is
  retrievable. The rule is *as few tokens as possible **while still naming a
  question a reader would ask*** — `capabilities/chatgpt-work.md` beats
  `CAPABILITIES.md` by being longer. (25% of names carry a `YYYY-MM-DD` prefix:
  earned in evidence and record folders where recency is the question, a token
  cost in live folders where the topic is.)
- **The top-level map must be GENERATED from the folder READMEs.** Ten
  contracts plus a hand-maintained index states the same fact twice and drifts —
  measured this session: `owner/` was created and `docs/MAP.md` never learned
  of it, because the map is written by hand.

And the addition neither rule covers: **no file outside a folder.** `docs/` has
**64 loose top-level files**, which are in no folder and therefore governed by
no README — the one place the per-folder contract does not reach, and where the
largest files live. Checkable: count files at a level no README governs.

**Scoped honestly.** An earlier draft of this argued that every failure in this
session was a top-level file. That is false — of eight, four were foldered
(`docs/providers/gemini-notebook.md`, `docs/planning/idea-backlog.md`,
`docs/planning/README.md`, `scripts/gen_idea_backlog.py`). Foldering did not
protect them because in each the session read *a document describing the thing*
rather than the thing. So this rule addresses about half the observed failures;
the short-file rule covers most of the rest, and neither cures reading a
description instead of a source.
