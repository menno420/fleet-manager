# Owner calibration — three sessions, counted independently

> **Status:** `reference`
>
> Written 2026-08-05. The evidence base for **THE DISCOVERY RULE step 0**
> (`docs/CAPABILITIES.md`). Step 0 originally cited *seven* corrections from a
> single session. Two other sessions had run the same count on their own
> transcripts, and the owner supplied both. The number was understated by
> roughly a factor of six, and — more usefully — **all three sessions derived
> the same operational rule independently.**

## 0 · Why this document exists rather than a number in a doc

A rule justified by one session's anecdote is one anecdote away from being
dismissed. Step 0 asks a session to **act on an owner statement without
probing it first**, which is a real concession of caution; it needs an evidence
base proportionate to that. This is it.

## 1 · The three counts, as reported, not summed

Each was counted by the session that lived it, against its own transcript. Two
span a compaction boundary, and **one of those explicitly refused to give a
false-precision total** — that refusal is preserved rather than smoothed over,
because it is the same discipline the counts are evidence for.

| Session | Scope | Right | Not fully right |
|---|---|---|---|
| **A** — game/bot work (`spider-swing`, `superbot`) | full session, incl. compacted half | **15** | **1** — *"in one of the other servers the access was properly set up"*; it was the production bot. **Self-caught within a minute, before the agent acted on it.** |
| **B** — provider capabilities / Vertex + GCP IAM | ~18 claims in the *visible window*; pre-compaction stretch reported as "recorded, not remembered" | **15** | **3**, of which **one plain error** — *"owner would be good too right"* (`roles/owner` deliberately excludes org-policy permissions) — **phrased as a question, so it cost nothing.** The other two were *right in mechanism, imprecise in specifics*, and both carried the owner's own hedge. |
| **C** — this session (hub, hooks + boot path) | full session | **13** | **0** unhedged. Two hedged claims (`#652`, `issue 271`) were wrong **and were marked uncertain before either was checked.** |

**Do not add these into one figure.** Session B's own report says the
pre-compaction stretch cannot be counted reliably, and inventing a total across
that boundary is exactly the failure mode the estate is trying to remove.

### The "not fully right" column is softer than it looks — checked, not taken on trust

The owner's own reading, 2026-08-05: *"None of those mistakes were actually
mistakes, mostly they were framed as questions or possibilities, not stated as
if I was sure."* That is a strong claim about his own record, and this document
is the evidence base for a rule telling agents **not** to verify him — so it was
checked against the texts rather than recorded on his word.

| Scored "not fully right" | Actual form | Source |
|---|---|---|
| *"Owner would be good too right"* | **question** | session B's own note: *"you phrased it as a question, so it cost nothing"* |
| *"is there any frame where the distance went down or remained the same"* | **question** | its literal form |
| *"moves you backwards a little bit, **or at least stalls**"* | **hedged** | session B: *"your hedge carried it"* |
| *"something like 652"* · *"or something close to that"* | **hedged** | session C, verbatim |
| *"in one of the other servers the access was properly set up and I can use commands"* | **asserted as fact** | session A |

**He is right, and it checks out.** Across three sessions there is exactly
**one** statement asserted as fact that was wrong: he was testing the bot a
session had just brought online, got a reply in another server, and reported it
without checking *which* bot had answered — it was his production bot. He caught
it himself **within a minute, before the agent acted on it.**

So the defensible statement is stronger than the table alone suggests:

> **One asserted-as-fact error across three sessions, self-caught before it
> propagated.** Everything else scored against him was a question, a hedge, or
> right in mechanism.

This is also why § 2 matters more than the hit rate: the errors do not merely
happen to be rare, they **land inside the hedged class by construction.**

## 2 · The property that matters is not accuracy — it is calibration

Accuracy alone would not license step 0. What does is that **the owner's
confidence signal is itself reliable**, so an agent can read the hedge and
treat the two classes differently.

Session B put it best:

> *"You only asserted where you had direct observation, and there you were
> essentially never wrong. On things needing external research — Play
> requirements, trademark classes, Discord's tester mechanics — you asked
> rather than claimed. That's well-calibrated in both directions."*

Session C observed the same shape from the other end: the two claims that were
wrong (`#652`, `issue 271`) arrived pre-hedged — *"I'm not exactly sure what
the number was"* — and the agent verified them, while acting directly on *"the
token is account-scoped."* **The system already works when the hedge is read.**

## 3 · Three sessions, three phrasings, one rule

None of these sessions saw the others' conclusions. Convergence across
independent evidence is the strongest support this rule has, and it is why
step 0 should not be read as one session over-correcting after being caught.

| Session | Its own words |
|---|---|
| **A** | *"When your description of your own systems conflicts with my measurement, **the measurement is the thing to doubt first.** That was true 15 times today and cost several hours each time I got it backwards."* |
| **B** | *"When you contradict me about your own game, your own console, or your own screen, I should treat that as ground truth and **go verify my side, not defend the inference.**"* |
| **C** | *"A probe establishes only what that one call did. **A failure means you took the wrong path, not that he was wrong**" — so go find the other path instead of writing a wall.* |

## 4 · The agent-side error species, named by the sessions themselves

Session B's self-assessment is the clearest statement of what step 0 is
actually defending against, and it is not carelessness:

> *"My errors were consistently the same species — **concluding from one probe,
> asserting a count or a cause without checking, reporting acceptance as
> success.**"*

All three are failures of *evidential scope*: treating one observation as a
general fact. That is the same defect as writing a wall from a single failed
call, and it is why the countermeasure had to become a mechanism
(`.claude/hooks/doc-routes.json`, route `recording-a-wall`) rather than a
fourth written rule — three rules written on 2026-08-05 were each broken within
hours **by the session that wrote them.**

## 5 · The boundary, restated — it is narrow and it holds

Step 0 does **not** say the owner is always right, and it does not suspend
verification.

| Question | Who answers it |
|---|---|
| *Is it set up / do I have access / which path / how does my system behave?* | **The owner. Source truth. Do not probe first.** |
| *Did this specific call just succeed?* | **The response. Read it every time.** |

The boundary is **not** "provisioning versus behaviour" — that narrower version
was written on 2026-08-05 and licensed a violation the same day (`§ 3`,
session C's row).

## 6 · Honest nulls

- **`n = 3` sessions, one person, one estate.** These are counts of *observed*
  claims. Nothing here counts claims he did not make, or errors nobody caught —
  the false-negative rate stays `NOT-VERIFIABLE`
  ([`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md) § 2).
- **Sessions A and B were counted by those sessions, not re-derived here.**
  `OWNER`-supplied, and under step 0 that is sufficient to act on — but it is
  cited, not measured, and labelled accordingly.
- **Session B's pre-compaction stretch is explicitly uncountable.** It is
  reported as such above and must not be quietly folded into a total.
- **A calibration this good is a property of a person, not a policy.** It says
  nothing about any other collaborator, and it should not be generalised into a
  rule about owners in general.
