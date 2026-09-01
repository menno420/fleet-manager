# The `estate` structure — proposal for approval (2026-09-01)

> **Status:** `plan` · plan input under OD-26 § 13 — nothing here is built. Written 2026-09-01 by the first Fable 5.1 session on the owner's laptop from a fresh clone at `cb3fc9a`; the owner chose all six defaults the same evening (A–F, see [`../../findings/2026-09-01-owner-direction.md`](../../findings/2026-09-01-owner-direction.md) § 7; four decisions in `docs/decisions.md` dated 2026-09-01). The laptop-hub copy of this folder is `OneDrive\Hub
ecords6-09-01 estate-successor-planning\`.
>

> **What is already decided and not reopened here:** the fresh start
> decision 25 in docs/decisions.md, the name `estate` decision 26 in docs/decisions.md, the generated `owner/` index decision 27 in docs/decisions.md,
> the findability contract — required reading order kept, one question per
> file, no file outside a folder decision 32 in docs/decisions.md — the eleven role names (agreed
> 2026-08-30 "as long as there are no renames along the way"), the three
> carry verbs, the hard write cutover, one `AGENTS.md` plus per-vendor delta
> files. Sources: `docs/planning/2026-08-30-fresh-start-redirect.md`, the
> ChatGPT Work review of the same day, `owner/intent-workbooks/folders/`.
>
> **What this adds:** the second level inside each role folder, designed from
> what fleet-manager actually holds and from the failure record; the boot
> path with a token budget; the file rules a check can enforce; the standard
> door-test walks. Your naming rule from today governs it: *nested, not
> sibling* — `superbot/goals/{completed,in-progress,planned}`.

## The tree

```text
estate/
├── README.md                     the door list (generated) + the reading order
├── AGENTS.md                     every rule that applies to all agents
├── CLAUDE.md · codex.md · gemini.md · grok.md      deltas only: how it loads, what it can reach
├── bootstrap.py · substrate.config.json · .github/ · .claude/ · .substrate/    tool-required roots
│
├── owner/                        your workbench — everything that needs you
│   ├── README.md                 GENERATED · decide · answer · do · triage
│   ├── decisions-needed/{open,answered}/     one question per file, your answer inside
│   ├── actions-needed/{open,done}/           clicks only you can do, deep links inside
│   ├── intent-workbooks/         carried whole: estate/ you/ agents/ products/ repositories/ successor/ folders/
│   └── briefs/                   GENERATED · what landed · what needs you · what is next
│
├── repositories/                 one folder per repo on the account, all 28
│   ├── README.md                 GENERATED estate index — one line per repo, at most 120 characters
│   └── <repo>/
│       ├── README.md             what it is · state word · where its own truth lives (at most 60 lines)
│       ├── intent.md             your words, then DERIVED; one page
│       ├── working-here.md       venue, gates, skills needed, what not to touch
│       ├── goals/{planned,in-progress,completed}/     one goal per file
│       ├── problems/{open,resolved}/                  one problem per file, subsystem tag in the header
│       └── owner-comments/{unconsumed,consumed}/      carried whole, same tool
│
├── state/                        what is true now, each file dated and sourced
│   ├── estate/                   now.md (GENERATED from goals/in-progress + your holds) · cutover.md · risks.md
│   ├── services/                 one live external thing per file: railway-reliable-grace.md · play-store-slingy-spider.md
│   └── capabilities/             one surface per file: claude-code-cloud.md · claude-code-laptop.md · chatgpt-work.md · codex-review.md · gemini.md · github-pat.md
│
├── plans/{active,completed,superseded}/     a file, or a folder for a multi-part plan
│   └── active/estate-successor/  structure.md · migration-manifest.csv · acceptance-test.md · cutover-checklist.md
│
├── decisions/
│   ├── README.md                 GENERATED ledger view with status
│   ├── owner/                    OD-NN-<slug>.md — your directives, your words
│   └── estate/                   D-NNNN-<slug>.md — session-made and flagged
│
├── ideas/{open,promoted,retired}/           one idea per file; the cap of 50 counts open/
│
├── evidence/                     dated measurements; a closed topic set, README declares it
│   ├── agent-errors/ · repo-structure/ · capabilities/ · owner-sittings/ · products/ · other/
│   └── <topic>/YYYY-MM-DD-<slug>.md
│
├── practices/                    how we work here — settled rules only
│   ├── how-we-work-here.md       the one page in the reading order
│   ├── traps/TRAP-NNN-<slug>.md  one trap per file; its route patterns live in its header
│   ├── conventions/<one-rule>.md
│   ├── writing/                  one-question-per-file.md · naming.md · certainty-tags.md · owner-marker.md
│   └── sessions/                 session-start.md · session-card.md · session-close.md
│
├── tools/
│   ├── README.md                 plain-language catalogue: the human problem each tool solves
│   └── checks/ · generators/ · moves/
│
├── sessions/                     visible, not hidden
│   ├── README.md                 GENERATED · the last three cards per repo, top blocks only
│   ├── YYYY-MM-DD-<slug>.md      top block first: "what the next session needs to know", 3 to 5 lines
│   └── off-repo/                 laptop, ChatGPT and Codex work that lands no commit here
│
└── archive/                      frozen; moved only by tools/moves/archive_move.py
    ├── README.md · manifest.csv  GENERATED: old path · new path · date · reason · replacement · commit
    └── <role>/<YYYY-MM>/<original path>            (question A)
```

## Why these second levels — one line each

- **Closed sets go in the path, open sets get an index.** `{planned,
  in-progress,completed}`, `{open,resolved}`, `{unconsumed,consumed}`,
  `{active,completed,superseded}` are closed: an agent guesses them right
  forever. Subsystems, topics and repos are open: each has a generated
  README. This is Condition 2 from `successor/naming-and-file-size.md`.
- **State in the path is moved by a tool, never by hand** — the
  `owner-comments` pattern that already reds the build when folder and header
  disagree. Copy the mechanism, not just the names.
- **"Where does spider-swing stand?" is a door, not a paragraph.**
  `repositories/spider-swing/goals/in-progress/` answers it without opening a
  file. Today the answer is a section inside a README you must know to open —
  the door test's level-4 defect.
- **`state/` is generated where it can be.** `now.md` is built from every
  repo's `goals/in-progress/` plus five hand-written owner-hold lines. One
  file answers "what is happening now" and every other front door links to
  it. That is the ChatGPT review's guiding question, answered.
- **Capabilities become one file per surface.** `CAPABILITIES.md` is 2,136
  lines of live facts and ledger history in one file. The facts move to
  `state/capabilities/<surface>.md`, each with a checked date; the history
  archives.
- **Traps carry their own delivery.** A trap file's header declares the
  patterns that should fire it; `doc-routes.json` is generated from those
  headers. "An entry without a route is unfinished work" becomes a checker
  instead of a sentence.
- **Decisions split by who decided.** Your directives (`OD-NN`) and session
  decisions (`D-NNNN`) have different authority; the folder says which.
  Flag: filenames keep the number because the estate cites `[D-NNNN]`
  everywhere; the slug makes the door readable.
- **Evidence splits by the question it answers, not by genre.** The
  audits-versus-findings split never closed and material landed by feel. Six
  topics are declared in the README; `other/` exists so nothing is homeless,
  and a file sitting there is a prompt to name a seventh topic.
- **Every repo gets a folder** (flagged default), archived ones a README
  only, so the path is guessable for all 28 and the generated index marks
  the state word.

## The boot path — six reads, one budget

The required reading order stays decision 32 in docs/decisions.md. It becomes six short files:

| # | Read | Budget |
|---|---|---|
| 1 | `README.md` — what estate is, this list, the doors | at most 60 lines |
| 2 | `AGENTS.md` — the rules for every agent; your vendor file loads itself | at most 80 lines |
| 3 | `state/estate/now.md` — true now, active work, your holds | at most 50 lines |
| 4 | `owner/intent-workbooks/estate/why-this-estate-exists.md` — your words | 67 lines today |
| 5 | `practices/how-we-work-here.md` — act versus ask, verify, one PR, born-red; points onward | at most 80 lines |
| 6 | `sessions/README.md` — the last three cards' top blocks | at most 40 lines |

**Total at most 400 lines, about 5,000 to 6,000 tokens. Today's six reads
cost about 88,000.** The boot file routes; it does not summarise. History
(`fleet-account`) and how you think (`owner-reflection`) move to
`evidence/owner-sittings/` and `owner/intent-workbooks/you/` and are linked as
"read when the task needs it", not mandated.

## The file rules — each one checkable

| Rule | Check | Mistake it targets |
|---|---|---|
| R1 · No file outside a folder, except the root set | preflight counts files at levels no README governs | 65 loose files in `docs/` |
| R2 · Every folder has a README with six headings: belongs · does not · source of truth · filename rule · when it leaves · generated outputs | preflight | the door test's dead rooms |
| R3 · Length: soft 120 lines advised at write time, hard 200 fails preflight; `evidence/`, `archive/` and generated files exempt (question B) | PostToolUse advice + preflight | 27 files over 600 lines; 57 % of prose in the unread fifth |
| R4 · One claim per line: prose wrapped at 100 characters, table cells at most 200 | preflight | TRAP-008 — a 673-character cell whose qualifier sat 400 characters in |
| R5 · `state/` and `evidence/` headers carry `checked · via · certainty`; state older than 30 days renders stale | preflight | TRAP-001 — a dated record read as current |
| R6 · Generated indexes are regenerated in preflight; CI fails if stale | CI | the companion record the diff owes (13 repos) |
| R7 · Filenames are lowercase-kebab topics or questions; dates only in `evidence/`, `sessions/`, `archive/`; no `notes`, `misc`, `temp`, `final`, `v2` | preflight | files nobody can guess |
| R8 · State-in-path moves go through `tools/moves/`, which rewrites the header and the index in one diff | preflight reds folder/header disagreement | a goal finished and never moved: wrong twice |
| R9 · A new folder inside an open set needs its index line the same diff | preflight | rooms with no door label |

## The door test — five standard walks, blind-scored

Pass means: at most four doors, no back-outs, no index opened, scored by an
agent other than the one who built the tree.

| Question | Expected walk |
|---|---|
| What is the current work on spider-swing? | `repositories/` → `spider-swing/` → `goals/` → `in-progress/` |
| May an agent delete a stale file without asking? | `practices/` → `conventions/` → `deleting-and-archiving.md` |
| What did the last session on the laptop do? | `sessions/` → `off-repo/` |
| Is Railway still running the bot? | `state/` → `services/` → `railway-reliable-grace.md` |
| Placement: a new finding about agent errors | `evidence/` → `agent-errors/` → `YYYY-MM-DD-<slug>.md` |

Plus the mechanical half: boot path at most 6,000 tokens; R1 to R9 green.

## What this deliberately does not do

- It does not rename any of the eleven agreed roles.
- It does not decide the archive month layer (A) or the length cap (B).
- It does not create anything. The next step after your letters is
  `05-kit-prerequisites-and-migration.md`.
