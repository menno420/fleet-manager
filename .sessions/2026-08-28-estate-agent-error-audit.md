# 2026-08-28 — the estate-wide agent-error harvest (OD-24 §6 step 1, extended)

> **Status:** `complete` — both corpora harvested, verified and synthesized;
> [the finding](../docs/findings/2026-08-29-estate-agent-error-audit.md) is
> landed and indexed. Nothing is registered or built: every proposal is
> owner-gated under the roadmap's §6 promotion rule.

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
- **1,592 pull-request review comments** across 12 repositories — **1,431**
  external reviewer findings and **155 written by the owner himself**, the
  highest-signal source in the estate.
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
   **no routing at all** while already owning a four-event hook channel in every
   adopter.
3. **Seven patterns converge across two independent corpora** (§5), earning five
   proposed traps.
4. **The era question is answered in kind and refused in rate** (§6) — the
   owner's drift hypothesis is not visible; what did worsen is rules broken by
   the session that wrote them, whose cause is delivery, not motivation.

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

No finding is written yet, no trap is registered, and nothing is proposed to
the kit. Those land when the audit completes.
