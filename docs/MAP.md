# The map — every part of this repo, one line each

> **Status:** `living-ledger`
>
> The router the front door promises: `README.md` → this map → any area → any
> file, three links or fewer. One line per area — what it is, its **tier**, and
> where its own README is. Depth lives behind the links, never here.
> Design and the owner's directive: [the navigation plan](planning/2026-08-10-repo-navigation-plan.md).

## The three tiers

| tier | meaning | your obligation |
|---|---|---|
| **CORE** | mandatory orientation | read on every cold start — the numbered order in [`README.md`](../README.md) |
| **TASK** | live surfaces | read when your task touches them; routed from here and the boot table |
| **RECORD** | the estate's memory | never required for orientation; preserved and dated — provenance, **not certified accuracy** (this audit found record-tier claims false when written) |

A `RECORD` area is not unimportant — it is why the estate can prove what
happened. It is simply never the answer to "what should I do now?", and a claim
inside one is evidence *about* its date, to verify like any other claim.

## Root files

| file | tier | what it is |
|---|---|---|
| [`README.md`](../README.md) | **CORE** | The front door: the story, the mandatory reading order, this map. |
| [`CONSTITUTION.md`](../CONSTITUTION.md) | TASK | The working agreement: act-vs-ask rails, owner-only classes, how rules change. |
| [`MISSION.md`](../MISSION.md) | RECORD | The seat-era mission (era-bannered 2026-08-08); the program's NOW pointer replaced it. |
| [`bootstrap.py`](../bootstrap.py) | TASK | The vendored substrate-kit engine (GENERATED — never edit). `python3 bootstrap.py check --strict` is the one local gate. |
| `substrate.config.json` · `project.index.json` | TASK | Kit host configuration (version, docs root, badge vocabulary, cadences) and the kit's context-pack index. |
| `.session-journal.md` | RECORD | The kit's cross-session process-memory template — still unfilled placeholders. |

## Top-level areas

| area | tier | what it is |
|---|---|---|
| [`.claude/`](../.claude/CLAUDE.md) | TASK | What a Claude Code session loads at boot: the boot file, six hooks ([hook README](../.claude/hooks/README.md)), 27 skills. |
| [`docs/`](#docs-areas) | mixed | The records home — every subdirectory mapped below. |
| [`.sessions/`](../.sessions/README.md) | TASK | The live session-card protocol — your born-red card is the in-flight claim parallel sessions see, and it flips complete last. Completed cards are records. |
| [`.substrate/`](../.substrate/hooks/README.md) | TASK | Kit state, staged skill copies, the guard-fire telemetry ledger, banked rollback dists. Kit-owned. |
| [`scripts/`](../scripts/README.md) | TASK | Repo-side checkers and generators; `scripts/preflight.py` is what CI's gate actually runs. |
| [`tools/`](../tools/README.md) | TASK | Estate tooling: the false-wall and doc-route checkers (required-check inputs), gemini delegation, guard tests. |
| [`.github/workflows/`](../.github/workflows) | TASK | Four workflows; `substrate-gate.yml` is THE required check; the roster pair is retired (banners inside). |
| [`control/`](../control/README.md) | RECORD ·mixed | The retired seat-era ORDER/status bus — **except [`control/claims/`](../control/claims/README.md)**, which the kit still wires (`claims_dir`, `check_claims`, a gate fast-lane) and whose README is badged `binding`; contested — see the audit's control/claims finding. The claim signal sessions actually use is the born-red card + open PR. |
| [`telemetry/`](../telemetry/README.md) | RECORD | Committed trigger snapshots for the retired roster machinery. |
| [`projects/`](../projects/README.md) | RECORD | Console packages (instructions/prompts) for the terminated autonomous seats. |
| [`registry/`](../registry/README.md) | RECORD | Generated lane registry, frozen at generation #430 (2026-08-06). |
| [`environments/`](../environments/README.md) | TASK ·mixed | The environment registry (no-secret-values hard rule) — `setup-base.sh` + specs live, routed from [`execution-surfaces.md`](execution-surfaces.md); per-seat scripts are records. |
| [`templates/`](../templates/README.md) | RECORD | The seat-era worker preamble template. |

## docs/ areas

| area | tier | what it is |
|---|---|---|
| [`intent.md`](intent.md) · [`current-state.md`](current-state.md) · [the program](planning/2026-07-26-consolidation-program.md) · [`fleet-account-2026-07-26.md`](fleet-account-2026-07-26.md) · [`owner-reflection-2026-07-21.md`](owner-reflection-2026-07-21.md) | **CORE** | The mandatory reads — see [`README.md`](../README.md) for the order and what each gives you. |
| [`current-state-shipped-log.md`](current-state-shipped-log.md) | RECORD | The hub's merged-work log plus the seat-era sections lifted off the boot path (OD-17, 2026-08-22). Provenance, never orientation — `current-state.md` keeps the recent window. |
| [`owner-queue.md`](owner-queue.md) | TASK | The consolidated queue of genuinely owner-only asks (`OQ-` slugs). |
| [`owner-steps-2026-08-21-laptop-setup.md`](owner-steps-2026-08-21-laptop-setup.md) | TASK | The owner's local-machine setup: installing Claude Desktop + Claude Code on his Windows laptop (x64), and what a local session reaches that a cloud container cannot. |
| [`decisions.md`](decisions.md) | TASK | The `[D-NNNN]` decision ledger (append-only). |
| [`CAPABILITIES.md`](CAPABILITIES.md) | TASK | The verified capability/wall ledger + THE DISCOVERY RULE. Append-only below the seed fence. |
| [`SKILLS-local.md`](SKILLS-local.md) · [`SKILLS.md`](SKILLS.md) | TASK | The 27-skill roster and the ⚠ re-apply table for kit upgrades. |
| [`ESTATE.md`](ESTATE.md) | TASK | The estate index — every repository the account holds, one line each: what it is, state, aliases, canonical entry, Layer-2 link. The "which repo owns this?" router. |
| [`repos/`](repos/README.md) | TASK | Layer 2 — per-repo entry points and handoffs (coverage table inside; unbuilt repos are on demand, each with an ESTATE.md row). |
| [`providers/`](providers/README.md) | TASK | Per-provider capability references (Claude, ChatGPT, Gemini, Grok, …). |
| [`conventions/`](conventions/README.md) | TASK | Working conventions: adversarial review, Vertex-first Gemini routing, outbox rollover. |
| [`planning/`](planning/README.md) | TASK | Plans, the program, the roadmap, this map's design. Index inside distinguishes live from superseded. |
| [`audits/`](audits/README.md) | RECORD ·mixed | Dated audits — except the [full-read audit](audits/2026-08-10-full-read/README.md)'s `findings.md`, which is **TASK**: the live edit-pass worklist. |
| [`findings/`](findings/README.md) | RECORD ·mixed | Dated findings — except the two ★ read-path entries (foundation-continuation, checker-classification), which are **TASK**: read before acting on the program's next-actions. |
| [`ideas/`](ideas/README.md) | TASK | The idea backlog and its lifecycle. |
| [`prompts/`](prompts/README.md) | RECORD ·mixed | The retired seat-prompt corpus — except [`chatgpt-project-instructions.md`](prompts/chatgpt-project-instructions.md) (live standing instructions, rewritten 2026-08-10), [`chatgpt-couch-legend-project-instructions.md`](prompts/chatgpt-couch-legend-project-instructions.md) (the same for the Couch Legend project, 2026-08-21) and the [curious-research review prompt](prompts/2026-08-07-curious-research-external-review.md) (usable owner deliverable), all **TASK**. |
| [`experiments/`](experiments/README.md) · [`research/`](research/README.md) · [`proposals/`](proposals/README.md) · [`retro/`](retro/README.md) · [`succession/`](succession/README.md) | RECORD | Pre-registered experiments · 2026-07-12 research corpus · seat-era proposals · retros · handoffs. |
| `eap-*` · `handoff-*` · `owner-actions-*` · other dated root files | RECORD | Dated snapshots of the EAP era; each carries (or is gaining) its era banner. |

## If you are lost

You are in a **records home**: most of what you can see is memory, and the small
live core is the numbered list in [`README.md`](../README.md). When a document
here contradicts a live surface, the live surface wins; when two records
disagree, the later date wins; when it matters, the committed tree beats both.
