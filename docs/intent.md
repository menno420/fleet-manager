# fleet-manager — intent

> **Status:** `living-ledger`
>
> **What this file is for:** the durable half of *why*. Every other record in
> this repo says what was decided; this one says what the repo is **for**, what
> would make the owner call it working, and how a session should decide when he
> is not there. It is the thing a rule is checked against when the rule and the
> situation disagree.
>
> **What it is NOT:** current state (`current-state.md`), architecture
> (`architecture.md`), the step ledger (the program), or per-repo truth (each
> repo's own docs, indexed at `docs/repos/<name>/`). If this file starts
> describing what is true *now*, it has drifted into the wrong job.
>
> **Provenance is labelled per entry and never merged.** `OWNER` = his words,
> quoted or closely paraphrased, from the intent interview of **2026-08-09**
> (21 questions, all answered). `DERIVED` = my inference from those answers —
> revisable, and explicitly not his statement. Certainty legend:
> [`findings/2026-08-05-foundation-continuation.md`](findings/2026-08-05-foundation-continuation.md).

## 1 · What this repo is for

`OWNER`. **The estate's router and records home.** Orientation, continuity, and
where the per-repo handoffs live. **Product truth stays in each repo** — this
one links and points, it does not restate.

`OWNER`, and it narrows the boundary usefully: fleet-manager **should**
reasonably explain *what each repo is for* and *what kind of skills and
capabilities are generally required there*. That is not the same as explaining a
repo in depth, and the second is what it must not do. So the line is:

| fleet-manager carries | each repo carries |
|---|---|
| what the repo is for · which skills and capabilities working there needs · where the last session left off · whether to attach it at all | its architecture, its internal state, its own capability ledger, how to work inside it |

`OWNER`. **The primary reader is the next agent session, not the owner.** Where
the two conflict, write for the agent — a small named set of surfaces
(`owner-queue.md`, the briefs) is his, and the rest is not.

`DERIVED`. Method-prototyping happens here because the estate's methods are
exercised here first — but it is a **side effect of being the hub, not a second
mission**. When a method proves out, its home is substrate-kit, which is what
every adopter actually loads. If you want the intent layer to stay fm-resident,
that overrides this line.

## 2 · Success — what "working" means

`OWNER`, three of five offered, and the third was not on my list of guesses:

1. **A fresh session orients and takes a correct first action without being
   steered.**
2. **The same class of mistake is never corrected twice** — a correction becomes
   a mechanism, not a memory.
3. **Sessions stop asking things the repo already answers.**

He did **not** pick "you can see estate state without asking an agent" or "small
enough that you could read it" as success criteria — size is governed separately
(§ 4), and the visibility surface is not what this repo is measured on.

## 3 · The failure costs, in his order

`OWNER`:

1. **A session acting on stale or wrong recorded state.**
2. **A session never finding the right doc.**
3. *(partly)* A session asking what is already written down — and the
   qualification matters more than the rank:

> *"I'd rather have an agent ask me something so I can clarify than that they
> misunderstand the goal."*

**So asking is cheap and misunderstanding is not.** The estate's older framing —
owner attention as the scarcest resource, minimise asks — is real but subordinate
to this: a question that prevents a misread goal is a good trade, and the thing
to minimise is *unnecessary* asks, never asks as such.

`OWNER`, on scope: a session doing good work on a slightly different scope is a
**small** problem —

> *"as long as the work is done in a way that's beneficial an agent should have
> some freedom to decide its own scope."*

## 4 · Growth — the rule that governs this whole repo

`OWNER`. **Records may grow. Instructions may not** — instructions grow only
with a good reason, because:

> *"it's more important that we implement and test the right
> enforcement/reminders, so the right instructions enter at the right moment."*

That is the injection thesis stated as intent rather than as a finding: the
answer to "sessions do not follow rule X" is a mechanism that delivers X at the
moment X applies, **not** another statement of X. See
[`findings/2026-08-08-why-rules-dont-bind.md`](findings/2026-08-08-why-rules-dont-bind.md)
for the measurement behind it (116 statements, 0 catches).

## 5 · Non-goals

`OWNER` (three of four offered; the fourth is qualified in § 1):

- **A second source of truth for anything a repo owns.**
- **A growing archive nobody reads.**
- **An apparatus that needs maintenance sessions of its own.**

## 6 · Decision heuristics — how to decide without him

`OWNER` throughout.

**When a plan or directive exists, keep going.** *"If any work has a proper plan
or clear directive, an agent can always continue as long as the decisions are
already made or can be fully derived with logic."* With nothing assigned: improve
orientation/apparatus, take the next program step, or stop and report — inventing
work is not required.

**Reversible and 50/50 → decide and flag.** Ask when undoing it would cost more
than a session.

**When his live word conflicts with a written record, the live word wins — and
you say so.** *"Always explain what is conflicting and which side you suggest to
follow through on. It could be possible that I personally misunderstood something
and gave the wrong orders, though this is not likely."* Never resolve the
conflict silently in either direction.

**Interrupting him.** *"Don't interrupt work unless absolutely necessary."* He is
mostly away during implementation — those run for hours and he checks in roughly
every 30 minutes. So: **ask immediately when a genuine fork appears, but do not
stop working for it.** Stop only when there is truly no next step available
without the answer. If another approved step exists, take it and collect the
answer on his next check-in.

**Question form.** State your interpretation back and let him correct it —
*"most of the time by stating back your perceived intent I will see if you
understood and will correct you if you are wrong."* Structured options are for
genuine forks. There is no target number of questions: enough to resolve the
ambiguity that remains, and no more.

## 7 · Who does what — the agent roster

`OWNER`, 2026-08-09, and nothing in this repo recorded it before.

| Agent | Role in this estate |
|---|---|
| **Claude** | The main agent. Planning, implementation, GitHub settings/Actions, documentation — *"Claude does everything"*. It holds the full credential set, so it has the widest capability and the most freedom. Preferred for important documentation work. |
| **ChatGPT** (the *Work* environment) | Real implementation, currently doing a lot of it in `spider-swing`. Comparable to Claude Code, installs the same kinds of packages, and **has proven very reliable**. Documentation work there is worth a deliberate test — untried, and the owner wants to know if it understands the method. |
| **Gemini** · **Grok** | Routed to **extra review, brainstorming and planning**. Implementation is not their lane in this estate. |
| **Codex** | Independent PR review (the GitHub relay, ~5.5 min). |

`OWNER` on portability: **do not assume every method works on every agent.**
Claude has the deepest native GitHub integration, so expecting parity is not
reasonable — but **write for the fact that more than one agent works these
repos, mainly ChatGPT**, and what exists today already carries over decently.
Surface differences that change how a prompt must be written:
[`execution-surfaces.md`](execution-surfaces.md).

## 8 · Structural answers that were open

`OWNER`, 2026-08-09, closing the three questions the spider-swing folder left
open plus the workspace question:

- **The Layer-2 folder shape replicates as built** — README + `capabilities.md` +
  `records.md` + `working-here.md`, with `current-state.md` and `goals.md`
  deferred. `working-here.md` earns its place as a distinct file.
- **Coverage: the four Tier-1 repos now, the rest on demand.**
- **fleet-manager points at the external workspaces per repo** — Drive folder,
  ChatGPT workspace, Gemini notebook — as pointers, never copies.

Detail and the rejected alternatives:
[`repos/README.md`](repos/README.md) ·
[`planning/2026-08-08-fleet-manager-as-index.md`](planning/2026-08-08-fleet-manager-as-index.md).

## 9 · Still open

- **Where the durable intent surface lives for *other* repos** — this file is
  fleet-manager's. The roadmap deliberately requires *one discoverable canonical
  intent source* per active repo rather than a file of this name everywhere.
- **Whether ChatGPT can carry documentation work to this standard** — the owner
  wants it tested; nothing has been run.
- The owner began a question 22 and left it empty. Whatever it was, it is not
  captured here.

## How to use this file

Read it when a rule and the situation disagree, when you are about to ask him
something, or when you are deciding what belongs in this repo versus another. It
does not need re-reading every session — but it is the thing a plan is checked
against, and Phase 3's review ladder starts at intent fidelity, not at code.
