# The agent operating environment — the three-phase roadmap

> **Status:** `plan` · 2026-08-08 · owner architecture review, recorded live
>
> **These are the owner's architectural decisions**, taken in the hub chat on
> 2026-08-08 and written down the same session, because the direction otherwise
> lives only in a chat transcript — and *"a document that lives only in a handoff
> prompt is not in the repo"* (`.claude/CLAUDE.md` read path, entry 2b).
>
> Certainty tags per
> [`../findings/2026-08-05-foundation-continuation.md`](../findings/2026-08-05-foundation-continuation.md).
> Everything in § 1 is `OWNER`. Phase 1's measurements are `MEASURED`; the
> Phase 2/3 designs are `OWNER` on intent and `REASONED` on mechanism until
> something is built and tested.

## 1 · The goal, in one paragraph

`OWNER`. Build an agent operating environment where Claude, GPT/Codex, Gemini or
any other capable agent starts from an imperfect owner message, reconstructs the
intended outcome from existing project knowledge, exposes only the consequential
uncertainty, plans correctly, executes with the repo's known methods and traps,
reviews back against the original intent, and leaves better-structured context
for the next agent — **without the owner having to restate how he works.**

**"Model-independent" is the wrong phrase for it, and the precise one is
`provider-aware, model-portable`** (sharpened 2026-08-08 against the owner's
agent roster). **The reasoning and the method must transfer; execution
capabilities do not have to be equalised.** Claude holds the broadest credential
and tooling reach here, so a method that depends on a Claude-specific capability
is **not defective — provided the dependency is declared** rather than hidden.
What must stay portable is the *concepts*: intent resolution, the procedure, the
verification, the record. The target is therefore a **common operating protocol
with provider-specific adapters**, never an identical workflow everywhere.

**The bottleneck is not code quality.** `OWNER`: once a good plan exists,
implementation is usually strong. The recurrent failures happen earlier —
understanding intent, retrieving intent that already exists, selecting the right
procedure, carrying intent through planning → implementation → documentation →
review, and preserving durable lessons so the next agent does not repeat a known
mistake.

**And the owner's messages are high-information but not perfectly ordered.**
`OWNER`: he may still be refining an idea while writing it. **The system must not
require him to produce perfect specifications.** The agent's job is to
consolidate, retrieve existing intent, distinguish what he said from what was
already decided from what the agent inferred, expose consequential gaps, and
structure the goal back to him.

## 2 · Why the phases are ordered this way

`MEASURED` ([`../findings/2026-08-08-why-rules-dont-bind.md`](../findings/2026-08-08-why-rules-dont-bind.md)):
116 committed statements of the verify-first rule across 66 files caught **0** of
16 incidents. Rules bind only when they **arrive** at the moment of action.

`REASONED`, and it is the whole argument for the ordering: **intent resolution is
retrieval, and retrieval is only as good as the corpus it retrieves from.** An
intent layer built over stale routers would confidently reconstruct the wrong
intent — worse than no layer, because it would carry provenance labels that make
the wrong answer look checked.

| Phase | What it establishes | Status |
|---|---|---|
| **1** | Trustworthy retrieval + orientation | this PR |
| **2** | Intent resolution | next |
| **3** | Common operating protocol | after |

## 3 · Phase 1 — trustworthy retrieval and orientation *(this PR)*

Boot file corrected at net-zero words; `session-close` carrying the Layer 2 step
it was decided to carry; one prompt route under a stated admission bar; the
seat-era routers saying which era they describe; this document.

**What Phase 1 explicitly does NOT fix:** intent resolution, procedure selection
beyond one route, documentation governance, review-from-intent, structured traps,
the procedure registry, workspace topology — and *momentum over evidence*, the
worst failure class, which has no mechanical catcher and belongs to the Stop hook
and the owner.

## 4 · Phase 2 — intent architecture

### 4.1 The intent map

`OWNER`. Before planning any non-trivial task, build — from the request **and**
the repo — a map with these parts, and **never collapse them into one confident
paragraph**:

| part | what it holds |
|---|---|
| **EXPLICIT** | what the owner actually said in the current request |
| **ESTABLISHED** | intent, decisions, constraints and non-goals already documented |
| **DERIVED** | conclusions the agent inferred — labelled as inference |
| **OPEN** | outcome-changing questions that cannot safely be derived |
| **GOAL** | one coherent statement of the intended outcome |
| **NON-GOALS** | plausible nearby readings that are *not* intended |
| **SUCCESS** | the result that would make the owner say "yes, that is what I meant" |

The separation is the mechanism: explicit owner intent, existing documented
intent, and agent inference must stay distinguishable, because the failure being
prevented is a fluent paragraph in which all three read alike.

### 4.2 Resolution order

`OWNER`:

```
owner request
  → retrieve existing project intent
  → retrieve relevant decisions / current context
  → build the intent map
  → resolve from evidence wherever possible
  → if HIGH ambiguity remains: ask the minimum sufficient set of questions
  → update the map
  → only then plan
```

**Never ask what the repo already answers.**

**There is no question budget — corrected 2026-08-08, `OWNER`.** This step read
*"ask 1–3 targeted questions"*, and a fixed range is wrong in both directions:
*"there should not be a maximum or minimum amount of questions. It should make
sure that based on the questions, you are able to fully understand the remaining
ambiguous items."* Often the answer is **zero** — a structured restatement is
enough and he corrects it. Sometimes it is ten. **The stopping condition is
§ 4.4's sufficiency test, never a count**, and any number written here would be
optimised toward instead of the thing it stands in for.

### 4.3 Ambiguity classes

`OWNER`:

- **LOW** — implementation detail. The agent decides.
- **MEDIUM** — reversible design choice. The agent decides and flags.
- **HIGH** — changes product intent, scope, ownership, irreversibility, or the
  definition of success. **Ask.**

**A planning agent must not silently resolve HIGH ambiguity.**

Questions should help the owner *recognise and refine* his idea, not demand a
specification — structured alternatives, or a restated interpretation:

> *"My current reading is that X is only an example and the broader goal is Y. Is
> that the correct level, or am I generalising too far?"*

### 4.4 The intent sufficiency test — the seam before planning

`OWNER`. Not a semantic gate; a standard question the planning workflow answers
out loud:

> Can I state the desired outcome, the relevant existing intent, the important
> constraints, the non-goals and the definition of success — **without silently
> resolving any HIGH ambiguity?**

```
INTENT STATUS: RESOLVED
```
or
```
INTENT STATUS: NEEDS OWNER
OPEN HIGH:
  - …
```

**Deliberately categorical, with no numeric confidence score** — a number here
would be fake precision, and the two-state distinction is what review needs to
refer back to later.

### 4.5 Ephemeral maps versus durable intent — keep these apart

`OWNER`, and this is the correction that stops `intent.md` becoming a transcript
of every conversation. **Most intent maps are working state and should stay
ephemeral.** *"Maybe we should move X into Y, although I'm not sure yet…"* may be
mapped perfectly, asked about, and resolved — and none of that intermediate map
belongs permanently in a durable document.

```
messy request → intent map → resolved intent → plan

and ONLY where durable knowledge actually changed:

resolved durable intent → documentation procedure → update canonical intent/decision
```

### 4.6 The durable intent surface — an invariant, not a filename

`OWNER`. **Every actively developed repo must have a discoverable canonical
intent source. Whether that earns a dedicated `intent.md` is repo-specific.**

> **Question:** where is this project's durable intent?
> **Answer:** exactly one discoverable canonical place.

What durable intent holds: purpose · owner outcome · product principles ·
non-goals · decision heuristics. What it does **not** hold: current state,
implementation detail, architecture.

The distinction from Layer 2, which is the reason both exist:

| | answers |
|---|---|
| **Layer 2** (`docs/repos/<name>/`) | what matters **now**, and where the last session left off |
| **project intent** | what should still matter **after** the current tasks change |

This is the `current-state.md` / `goals.md` lesson applied in advance: **do not
create a file merely because the global architecture named one.** For a small
repo the intent may already be perfectly represented in an existing canonical
document. If a dedicated file earns itself, create it.

**The first one exists: [`../intent.md`](../intent.md), 2026-08-08.** It earned a
dedicated file because the corpus answered almost none of it — twelve OD rows,
three `[D-NNNN]` entries and a PL register all record *what was decided*, while
**20 of the 21 intent questions were genuinely unanswered** anywhere. The
exception matters and is measured in § 4.8: the *purpose* question was partially
answered by two existing records, and the filtering pass missed it. So the honest
claim is **not** that nothing recorded what this repo is for — it is that the
record was scattered, partial, and silent on what would count as working. It was
produced by **asking**, not by deriving from the decision record, and two of the
21 answers immediately amended standing directives (OD-3, OD-6) — which is the
argument for the surface: intent that is never asked for drifts out of agreement
with the rules written under it, silently, because nothing compares them.

### 4.7 Intent-time routing

`OWNER` on the intent classes, `REASONED` on the mechanism. A **small** set of
high-value owner intents — review/audit · document/record · plan/design ·
implement/fix · continue/handoff · research/compare · Drive/files ·
recording/video · capability/blocked · Gemini/delegate — reached by distinctive
multi-word patterns and, eventually, a procedure classifier rather than keywords.

**The hook injects the method, never an interpretation.** *"Resolve existing
project intent and current owner intent before planning; label inference as
inference"* is a method. *"The owner means X"* is a guess the session will act on.

No broad generic keyword routes: the admission bar is committed in
[`../../.claude/hooks/doc-routes.json`](../../.claude/hooks/doc-routes.json)
§ PROMPT ROUTES, and it exists because a common word fires at prompt 1 of nearly
every session and the once-per-session dedup then burns the route before the
moment it was written for.

### 4.8 How Phase 2 gets tested

`OWNER`: against **real, messy, historical owner messages** from the committed
record — not synthetic examples. A fresh agent's map is scored on whether it puts
each claim in the right column (explicit / established / derived / open), and on
whether it left any HIGH ambiguity silently resolved.

**First live run, 2026-08-08 — the interview half, not the map half.** A 21-question
intent batch was put to the owner and fully answered. Three results worth carrying
into the design: (1) the questions were filtered against the repo first, and **20
of 21 were genuinely unanswered** — the *"never ask what the repo answers"* rule
cost almost nothing here because the corpus had no intent layer. **The exception
is the instructive part:** the purpose question *was* partially answered — two
records already called this repo *"hub + records custodian"* — and the filtering
pass missed it, which is a **`MEASURED` false-negative rate of 1 in 21 for
human-eye filtering** and the argument for making the ESTABLISHED column a
retrieval step rather than a recall step;
(2) **two answers contradicted standing directives**, so the interview's output is
not additive-only and needs a reconciliation step, which Phase 2's procedure must
name; (3) his own verdict on the format — a large lettered batch was right *"for
this task"* because the subject was the method itself, and the per-task version
should instead be sized to *"the remaining ambiguous items"*, with **no minimum or
maximum**.

**A fourth result, and it is about the interviewer rather than the interview.**
The session recorded a *"question 22, begun and left blank"* as an open item, in
three documents. **There was no question 22** — the batch had 21, and a trailing
`22.` in the answer list was read as an abandoned question (owner-corrected the
same day). Nothing was lost, but an **invented OPEN item is a distinct failure
mode from a missed one**: a missing question leaves a gap that the next
conversation closes, while a fabricated one sends future sessions hunting for
intent that never existed, and it carries the same provenance labelling as the
real entries. **So the OPEN column needs the same discipline as the others** —
an entry there is a claim that the owner left something unresolved, and it
requires the same evidence as a claim about what he said.

## 5 · Phase 3 — the common operating protocol

### 5.1 `/documentation`

`OWNER`. A procedure governing creation or material modification of durable docs.
Before writing, determine: document type · what it is authoritative for · what it
is explicitly **not** authoritative for · the canonical source the claim derives
from · whether another document already owns the information · whether this
should be a pointer instead of a copy · what owner intent and rationale must
survive · which alternatives were rejected and why · how future sessions discover
it · what makes it stale · how it is verified.

Eventually a `PreToolUse` hook detects durable doc writes and injects the
procedure — **complementing, not replacing,
[`read_before_write.py`](../../.claude/hooks/read_before_write.py)**.

### 5.2 The three hook moments

`OWNER`:

| event | layer | maturity |
|---|---|---|
| `UserPromptSubmit` | **INTENT** | least complete — Phase 2's job |
| `PreToolUse` | **ACTION** | strong examples: `route_docs`, `read_before_write`, `git_state_guard` |
| `Stop` | **CLAIM** | comparatively mature |

### 5.3 Inheritance, not copying

`OWNER`:

```
substrate universal method
  + repo-specific method additions
  + repo intent
  + current task intent
  = the working environment for any agent
```

**substrate-kit** owns the universal procedures — intent resolution, planning,
documentation, implementation handoff, review, verification, session close.
**Each repo** defines only its specialisation — project intent, repo-specific
planning requirements, repo-specific verification, known traps, architecture and
current state. The universal method is never copied into every repo.

### 5.4 Known mistakes as executable knowledge

`OWNER`. Each repo exposes its recurring traps in a structured form — **TRAP ·
TRIGGER · WHY · REQUIRED PREVENTION · VERIFY · ORIGIN** — with the lifecycle:

```
mistake → documented trap → hook/procedure reminder → deterministic checker where possible
```

### 5.5 Review traces backwards from intent

`OWNER`. The current review skill is too implementation-centric. The standard
method becomes: **1** intent fidelity · **2** plan fidelity · **3** repo-method
compliance · **4** implementation correctness · **5** known-trap check · **6**
verification quality · **7** residual uncertainty · **8** verdict.

**A clean implementation can still be wrong if the plan misunderstood the owner**,
which is why intent fidelity sits above code correctness.

### 5.6 The procedure registry — the architectural destination

`OWNER` on the need, `REASONED` on the shape. One way to answer: *"this request
is X — what exact procedure governs X, which docs/skills/tools are required, what
output shape is required, and what proves the procedure was followed?"*

**Do not simply move the existing guides into one directory and duplicate them.**
The distinctions are load-bearing: **provider/capability docs = facts ·
conventions/contracts = policy · skills/tools = execution · procedure registry =
orchestration.**

A record would carry: `id · purpose · trigger · status · canonical_policy ·
required_reads · preconditions · ordered_steps · tooling · output_contract ·
verification · failure_routes · owner_boundary · enforcement · last_verified` —
enough for deterministic validation that referenced docs, skills and tools exist,
that output contracts are present, that verification is defined, and that routes
point at real procedures.

### 5.7 External workspace topology

`OWNER`. The system includes non-GitHub context, and the roles stay distinct:

| surface | role |
|---|---|
| target GitHub repo | canonical technical/project truth |
| **fleet-manager** | global router + continuation/project topology |
| **substrate-kit** | universal agent operating method |
| **Google Drive** | persistent **non-code supporting material** — recordings, screenshots, images, audio, PDFs, external research, documents, datasets, store/publication assets, exports and deliverables |
| ChatGPT Projects | human-facing domain workspaces — **not canonical truth** |
| Gemini Notebook / NotebookLM | curated corpus / research interface |
| Claude + implementation agents | execution |
| Codex + review agents | independent verification |

fleet-manager eventually **points at** these locations for important repos rather
than copying their contents.

**The mapping is optional and many-to-many — never implicitly 1:1 with repos**,
because the surfaces have genuinely different boundaries: Drive folders map
cleanly to repos (storage benefits from deterministic names), ChatGPT Projects
are *mental* workspace boundaries that may span or subdivide repos, and a Gemini
notebook is created when a corpus merits one, not automatically per repo:

```yaml
drive:
  folder: <deterministic per repo, or absent>
chatgpt:
  workspaces:
    - AI Fleet / Control Room      # may span several repos, or be absent
gemini:
  notebooks: []                    # empty until a corpus earns one
```

Null and multiple values are both normal. Forcing symmetry would make the
topology tidy and untrue.

**Why the owner is building the Drive half by hand, in his words** (`OWNER`,
2026-08-08). He is creating a **Drive folder per repo** and making them public so
an agent can open them on request, then filling them with images, recordings and
documents. Three reasons, and the second is a concrete constraint no document
here had recorded:

1. **Persistent storage deliberately unrelated to GitHub** — the material is
   supporting context, not technical truth, so it does not belong in a repo.
2. **It routes around the five-attachments-per-message limit.** Uploading to a
   folder lets him hand over a whole set at once instead of dribbling files
   across messages.
3. **Labelling is the point, not tidiness:** *"preferably properly labeled so
   Claude and any other AI with Drive access can easily discover and use the
   relevant files."* A folder an agent cannot navigate unaided fails its purpose.

He also treats **cleaning up the noise** — the Drive layout, the ChatGPT
projects — as the highest-value thing he can personally do right now, which is
the same judgement that produced the OD-3 cleanup amendment: **noise reduction is
a feature, not tidying.**

Reading recipe for the folder, already measured and committed:
[`../conventions/owner-drive-folder.md`](../conventions/owner-drive-folder.md).

### 5.8 One instrument defect still open — and one already fixed

`MEASURED` in this session, `REASONED` on the fix.

**Still open — a lost read-set reads exactly like "you never read this."** The
usage-limit pause rotated the session id, `/tmp/claude-read-set/<id>.json`
started empty, and `read_before_write` warned about files that had been read in
full. The estate already holds the governing principle and the hook does not
implement it: **absence of telemetry must not masquerade as negative evidence.**
The fix is not necessarily persistence — it is that the hook must be able to say
*"I have no record for this session"* differently from *"I have a record and this
path is not in it."*

**Already fixed, and this entry was wrong to list it — corrected 2026-08-08
after Codex.** The closed-vocabulary check scoping by artifact type
(`in-progress` being a valid session-card Status and an invalid documentation
badge) **is implemented**: `.claude/hooks/read_before_write.py:142` guards the
badge check with `"/.sessions/" not in target`, landed in Phase 1 with the
measurement in its own comment. It was recorded here as unbuilt because a
parallel ChatGPT session described the **pre-fix** recording and that description
was folded in without opening the file — the same compose-instead-of-transcribe
error the finding names, committed while writing the roadmap that names it.
**A second agent's observation is dated evidence about the moment it was made,
not a statement about the tree now.**

**Only the open one belongs to the promotion rule below** — observed, recorded,
and not built into anything until it has earned it. The scoping fix is *shipped*,
and this sentence said "both" until Codex caught it: a correction that fixes the
body and leaves its own conclusion standing is the same defect one paragraph
down.

## 6 · The promotion rule that governs all of it

`OWNER`, and it is the guard against this roadmap becoming the thing it is trying
to fix:

```
observe failure → prototype procedure → test against real cases → measure → promote only if useful
```

**not**

```
good idea → mandatory infrastructure everywhere
```

The worked example is in this PR: the close-time telemetry snapshot was demoted
from a permanent `session-close` step to an experiment, to be adopted only if
about three sessions show the data is actually used. The estate's standing
tendency is to turn every useful observation into permanent apparatus; measuring
first is the correction.

## 7 · Who owns what

| | owns |
|---|---|
| **fleet-manager** | prototypes and estate-specific orchestration · global routing · Layer 2 · workspace topology |
| **substrate-kit** | generalised intent resolution · documentation · review · universal procedure mechanics · the eventual registry |
| **each repo** | its actual project intent · its own traps · its method additions and verification |

This is what keeps fleet-manager from becoming the universal implementation of
everything: it is where new estate-level methods are **proven**, and substrate-kit
is where proven methods become **reusable infrastructure**.

## 8 · Honest nulls

- **Phases 2 and 3 are unbuilt and uncosted.** Nothing here has been tested; the
  mechanism claims are `REASONED` until something runs.
- **Phase 1's own effect is measured on n=1 session** and only against the
  orientation failure class. It cannot move the classes the landed injection
  mechanisms already cover, and the roadmap should not be read as claiming it does.
- **The intent-map schema has never been run against a real owner message.** Its
  first test is its first use, and the test corpus (real historical messages)
  exists but has not been assembled.
- **Whether a durable intent surface stays distinct from Layer 2 in practice is
  unverified** — the two could collapse into each other under normal maintenance,
  which is the specific drift to watch for when the first one is written.
