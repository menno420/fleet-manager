# 2026-08-28 — the estate-wide agent-error harvest (OD-24 §6 step 1, extended)

> **Status:** `complete` — both corpora harvested, verified and synthesized;
> [the finding](../docs/findings/2026-08-29-estate-agent-error-audit.md) is
> landed and indexed. Nothing is registered or built: every proposal is
> owner-gated under the roadmap's §6 promotion rule.

- **📊 Model:** withheld · high · review/verify
- **⚑ Model-slot note:** the harness policy for this session forbids putting a
  model identifier into any artifact pushed to a repository, which collides with
  this field's family-level-model convention. Recorded as a collision rather
  than resolved either way; the effort and PL-004 task-class halves are exact.
- **📍 Venue:** cloud-container

## Mission

Owner ask, live: find what has already been audited today and what still needs
attention, then fan out across repositories to gather what would improve
`substrate-kit` and its skills — focused on **common agent errors across
sessions and repos**.

That resolves to **OD-24 §6 step 1, extended**. The genesis dig (fm #956)
executed step 1 **fleet-manager-side only**, over the August stepped-back
window, and its §9 names the remainder as skipped: the eighteen satellite
repositories, the June/July bulk, and superbot's PR review threads. This
session sweeps that declared remainder.

## Corpus (measured, not sampled)

- **4,583 session cards** across 20 repositories, 2026-05-29 → 2026-08-28,
  fetched as API tarballs → **7,214 error-bearing sections** → 68 shards.
- **1,592 pull-request review comments** across 12 repositories — 1,437 not
  attributed to the owner's account (1,431 Codex + 6 code-scanning) and **155
  attributed to it**. This card originally called those 155 *"written by the
  owner himself, the highest-signal source in the estate"*. **That is false and
  the audit's §1 is the correction:** agents authenticate with his credential,
  so all 155 are agent-authored. Corrected here rather than only in the finding,
  because a session card is a durable briefing artifact and would otherwise
  propagate exactly the false `OWNER` provenance this audit warns about (Codex,
  fm #967).
- Two independent corpora deliberately: session cards are **self-reported**,
  review comments are **externally caught after the agent declared done**.
  Patterns present in both are the strongest available signal.

## Shipped

- **[The finding](../docs/findings/2026-08-29-estate-agent-error-audit.md)** —
  eight sections, indexed in `docs/findings/README.md`.
- The audit ran as **two workflows, 986 subagents, 73.2M subagent tokens,
  17,444 tool calls, 0 agent errors**, paused mid-run for a usage-limit reset
  and resumed from cache on a bound trigger.
- `.audit-recovery/` — created as insurance during the pause, **deleted in this
  PR** as its README promised. The measurement that motivated it turned out to
  be backwards (see Verify), which is recorded rather than quietly dropped.

## The four findings

1. **The owner has no distinguishable voice on GitHub** (§1) — agents
   authenticate with his credential, so 562 of 564 issue comments and all 155
   review comments attributed to him are agent-authored. No estate record names
   this, and it makes the `OWNER` certainty tag unfalsifiable from GitHub.
2. **The delivery layer cannot reach the errors** (§4) — of 71 doc-routes, 8
   fire on `Edit`/`Write`, 42 on `Bash`, **0 on both**, 1 repeats; the kit ships
   **no routing at all**, and 19 of 20 repositories have no `.claude/hooks/` file
   at all — while the kit's four-event hook channel is installed in **18 of 20**
   (`superbot` and `spider-bot` excepted). Measured at `8a3a13d`; fm #963 has
   since closed the Edit/Write disjointness on `main`.
3. **Seven patterns converge across two independent corpora** (§5), earning five
   proposed traps.
4. **The era question is answered in kind, refused in rate, and the drift
   hypothesis is UNTESTED** (§6) — the extraction filters out the mission and
   scope sections that would answer it. A distinct August cluster is observed
   (rules broken by the session that wrote them); whether it represents a real
   increase is unanswerable here, and delivery is a candidate explanation, not
   a demonstrated cause. Both stronger claims were withdrawn on review.

## Verify

- Corpus counts are re-derivable: the five scripts in the recovery tarball
  rebuild everything from the GitHub API.
- Resume-from-cache **verified, not assumed** (2026-08-28 23:48Z): after the
  pause both journals gained **2** `started` entries each, not 68, and their
  105 and 121 results replayed unchanged. The documented behaviour holds.
- Three in-flight self-corrections worth inheriting, all one class:

  1. The first extraction returned **564** sections rather than 7,214, because
     Python's `glob` does not match dot-directories and `.sessions/` was never
     scanned — a null produced by the query, not the world.
  2. `merge-on-green` was written into a published PR comment as *"already
     passing"* without being read. It has no result on this head at all.
  3. **The container-persistence claim was backwards.** This session measured
     that no scratchpad file predated the 18:28:55 boot and concluded the
     storage does not survive a container. The absence was explained by the
     circumstance — it was the session's *first* container, so nothing older
     could exist — and proved nothing about persistence. **Measured decisively
     at 23:48:12Z**: the container was replaced (`uptime -s` = 23:48:12, up 0
     minutes) and the 47M corpus, both workflow journals and the scripts were
     all intact. The session volume **does** survive container replacement
     within a session. Scope: one replacement, same session; nothing here says
     it survives session end.

  All three are the same failure — **a conclusion drawn from an absence that
  the circumstance already explains** — which is TRAP-003's shape reaching
  beyond search results into environment inference. Recorded because the audit
  this card belongs to is harvesting exactly this.

## Not done here

**No trap is registered and nothing is proposed to the kit.** The five trap
candidates (TRAP-008..012) are written up as proposals in the finding's §5 and
deliberately not added to `docs/traps.md`; no doc-route, checker or skill is
edited. Under the roadmap's §6 promotion rule and OD-24 §3's freedom doctrine,
emitting estate-wide mechanism before the owner has seen the measurement would
recreate the wall-accretion he is correcting.

The finding itself **is** written and indexed —
[`docs/findings/2026-08-29-estate-agent-error-audit.md`](../docs/findings/2026-08-29-estate-agent-error-audit.md).


## ⟲ Previous-session review

Previous card:
[`2026-08-28-od24-round-open-questions-agenda.md`](2026-08-28-od24-round-open-questions-agenda.md)
(fm #961) — the OD-24 round's discussion agenda.

**Held up.** Its §5 *"what a session should just decide"* is what authorised this
session to run a large sweep without a letter, and its §0 headline — *the round
asked him for things his own record already answers* — set the standard this
audit tried to meet by measuring before proposing.

**One thing it could not have known, and this session owes it a correction.**
The agenda's §2 · E2 restored the journal question to the owner partly on the
strength of what the round's records said. This audit's §1 finds that **no
GitHub-sourced statement in this estate can be attributed to the owner at all**,
because agents post under his credential. That does not overturn any agenda row
— every row this session checked traces to chat or to a committed record, not to
a PR comment — but it means the agenda's provenance method has an untested
assumption under it, and any future row sourced from a GitHub comment is
unsafe. Flagged, not fixed: re-auditing the agenda's eleven rows is the
discussion sitting's work, not this session's.

**Not reviewed:** the three audits the agenda summarises were read as corpus
inputs, not audited for correctness. This session verified the structural claims
it repeats (the 71/8/1 route counts, the kit's missing routing) in the live tree
rather than citing them.

## 💡 Session idea

**Give the kit's four already-installed hook events something to carry.**

The kit wires `PreToolUse`, `SessionStart`, `PostToolUse` and `Stop` to
`bootstrap.py hook …` in **every adopter** via
`.substrate/hooks/settings.template.json`, and ships **no routing** through them
(`grep -c -E "route_docs|doc-routes" bootstrap.py` → 0, positive control 203).
Meanwhile fleet-manager's routing layer reaches `Edit`/`Write` on 8 of 71 routes
and repeats on 1.

So the cheapest real improvement is not another checker: it is **moving the
routing layer into a channel that already exists in all twenty repositories**,
and it is measurable against this audit's own corpus — every incident is dated
and cited, so *"would this route have fired on that instance"* is answerable
rather than asserted. That measurement is the promotion evidence the roadmap's
§6 requires, and it can be run before anything is made mandatory.

**Why it is an idea and not an action:** it changes what every adopter loads at
boot, which is exactly the kind of estate-wide mechanism OD-24 §3 says an agent
does not introduce on its own initiative.
