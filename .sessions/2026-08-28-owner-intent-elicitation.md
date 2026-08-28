# 2026-08-28 — the owner intent elicitation sitting

> **Status:** `in-progress` — born red, and it stayed red for the whole sitting
> **by design**: he was answering live, and the hold is what kept this PR from
> merging mid-conversation. Flipped only at his explicit close (*"I'd like you
> to properly end the session for now, I'm about to go to sleep"*). The
> questions he has not yet answered are **committed**, not carried in this chat,
> so tomorrow starts from the repo.

- **📊 Model:** opus-5 · high · owner-live interview
- **📍 Venue:** cloud-container, owner PRESENT

## Mission

His ask, verbatim: *"I'd like you to ask me some questions about certain things
that are not yet clear about my intent … My goal is to make sure that enough
owner intent is present in the repo(s) to ensure that the plan we are creating
has a good foundation."* Plus: review the intent already recorded for staleness,
surface **conflicts between his own statements** so he can adjudicate, and end
with per-repo records carrying **his own words** — *"I feel like a lot of my
original intent got lost along the way or hasn't been properly documented."*

He also asked to have the request improved with what he did not think to ask
for. Added, and each accepted or answered by him since: a **fixed template** so
28 records stay comparable · **triage before depth** · a **staleness rule** ·
**the layer above the repos** (the estate's own why) · **kill criteria**, which
the estate records nowhere.

`intake` invoked per the routing table; its RETRIEVE step ran before any
question was put to him (`intent.md`, the OD table, `decisions.md`, `ESTATE.md`,
`owner-profile.md`, the Layer-2 folders).

## Shipped

**The record — his words, kept apart from mine.**
[The elicitation record](../docs/findings/2026-08-28-owner-intent-elicitation.md)
— `OWNER` separated from `DERIVED` throughout, every answer written **as it
arrived** rather than at the close, because answers living only in chat are the
loss mode the whole sitting exists to correct.

- **Seven conflicts between his own past statements, resolved by him:** money
  (hobby stands; the commercial structures are not goals) · autonomy · reader
  (agent-first — **not** stale) · repo count (**deferred, not closed** — the
  estate had hardened it into a permanent closure) · the kit vs the
  maintenance non-goal (**not exempt** — time-boxed instead) · shiftlife
  (paused, he intends to return) · record shape.
- **His acceptance criterion, which the estate had never captured:** the
  **one-word test**. *"I literally started a fresh session, wrote only 'chicken
  farm' and the session created exactly what I had in mind."* **Both examples
  verified in the frozen repo** — superbot **#1328** (41 min, +1,668/29 files)
  and **#1332** (57 min, +2,131/37 files), **both 2026-06-22**, which lands on
  the exact peak the genesis dig measured independently. The PR bodies carry the
  mechanism: the two-word prompt is preserved verbatim in #1328; #1332 shows
  *five* design questions answered by documented defaults rather than by asking
  him; and #1328 applied an owner caution **nobody put in the prompt**. **The
  one-word test is a test of the repository, not of the agent.**
- **The end state for the bots, in his words:** `spider-bot` + `superbot-next`
  converge into **one** bot with **no architectural debt**, *"planned and
  connected from the start so it remains manageable and able to grow
  indefinitely"*. His *"already documented"* was **verified true** — and three
  parts of it are recorded nowhere, including that **`superbot-next` must be
  remade**, which contradicts `ESTATE.md`'s *"complete-parked architecture
  donor — 533/533 golden parity green"*.
- **The estate's first defect baseline:** ~7 agent claims corrected per session,
  14 the highest counted, recorded as a **floor** because his own hedges say
  counting started partway.
- **A new owner-originated want:** a **repo-creation skill** *"so all repos get
  created in the same way"*. Queued, not built.
- **Three intent drafts staged** for his rewrite — `substrate-kit`,
  `spider-swing`, `spider-bot` — each labelled slot-by-slot, with guiding
  questions only where the draft is guessing. The pattern they exposed: the
  same two slots are empty for every repo — **"what would make me stop"** and
  **"why it exists"** — and the worst case is `spider-swing`, the repo with more
  recorded state than any other and **no statement anywhere of why he made it**.
- **The questions he has not answered are committed**, not stranded in chat:
  [`../docs/planning/2026-08-28-owner-intent-questions.md`](../docs/planning/2026-08-28-owner-intent-questions.md),
  routed from the planning index, the record, and a new `OQ-INTENT-WRITE-UP`.

**A mechanism fix he ratified in-sitting, and it is the session's sharpest
result.** The shallow-clone error this session made was **not** unwritten
knowledge: TRAP-004 registered it, `doc-routes.json` routed it at exactly the
right tool, and its text is the missing step verbatim. It still did not arrive —
because the route was **one-shot**, and this session's *first* tool call spent it
on harmless orientation nine hours earlier. Put to him (hooks are owner-gated by
superbot:Q-0194's ladder), he ruled: **a route guarding a KIND of command is
never spent.** Applying it found the policy **already written in
`route_docs.py:505-515`** — reference pointer vs action guard, three measured
incidents behind it — with **one opt-in across 71 routes**; and found fm #938
had named **two** spent routes and given the flag to **one**. `repeat: true`
applied to the **9 action guards**; reference/repo routes deliberately excluded
per the implementation's own *"blanket repetition would nag"* warning, and that
narrowing flagged as `DERIVED` for him to widen if he wants.

## Verify

- `python3 bootstrap.py check --strict` on **real exit codes, no pipes**
  (redirect-then-read; TRAP-002 honoured). Final pre-flip run: the only finding
  is the designed born-red hold naming this card.
- **The route fix verified live, not asserted:** JSON re-parsed after the edit ·
  `repeat` routes **1 → 10** · `python3 tools/test_doc_route_patterns.py`
  **exit 0**, *"17 case(s) — CLEAN"*. Then the real proof — **both newly
  repeated routes fired on the very next Bash command**, having already been
  spent earlier in this session.
- **A hedged owner claim verified rather than accepted** (verify the hedged, act
  on the unhedged): the kit's outside-adopter framing is **substantially as he
  said** — MIT `LICENSE`, a one-step adopt recipe, three modes that pace
  adoption — with two exceptions that land on the charter rewrite he ordered.
- **Both one-word-test PRs verified** at `menno420/superbot` via the API, with
  timestamps and diff sizes; superbot never cloned, never written.
- **A dating claim measured, published, refuted and re-measured.** Its first
  form was inference; its second was `MEASURED` **on a shallow clone** and
  wrong; `git fetch --unshallow` (64 → 995 commits) restored the truth and
  vindicated the inference. The false version is struck through in place, not
  deleted.

⚑ Owner decisions needed: the standing intent questions (his to write, whenever
— `OQ-INTENT-WRITE-UP`) · whether the route-repeat policy should widen to the
reference routes · `OQ-KIT-RENAME` still needs one word from him.

💡 **Session idea:** every mechanism failure this evening had the same shape and
**none involved missing knowledge** — a routed rule that arrived too early, a
policy written inside its own implementation and applied once, a fix that named
two defects and repaired one. That suggests the estate's next instrument is not
another guard but a **guard census**: for each registered trap, does a route
exist, does it repeat, and has it ever fired at the moment it was written for?
`.substrate/guard-fires.jsonl` already records every fire, so the census is
readable from the tree today — it needs no new apparatus, which is exactly the
kind of fix his own cost function ranks highest.

## ⟲ previous-session review

The OD-24 sitting immediately before this one (fm #964) established the method
this one reuses: record each answer **as it arrives**, keep `OWNER` and
`DERIVED` apart, and verify a claim before writing it down as his. Two carried
forward and one corrected:

1. **Carried:** putting his own prior statements to him as conflicts worked
   again — seven resolved here, and in two cases (repo count, the kit non-goal)
   the estate had hardened his words into something stronger than he said.
2. **Carried:** the "state your interpretation back" form his profile
   prescribes produced the sitting's best result again — he rejected a proposed
   autonomy map outright, which no menu would have surfaced.
3. **Corrected in flight:** fm #964's § 1.2 recorded an autonomy **area map** as
   the highest-value follow-up. His next answer dissolved the premise. The entry
   was left standing with the correction attached rather than edited away,
   because a session reaching for a permissions artefact within minutes of him
   naming an initiative problem is the useful part.
