# 2026-08-07 · hub — the boot source decides how capable a session is

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-07 · venue: owner-live hub chat (fleet-manager boot, curious-research
attached mid-session) · branch `claude/fleet-manager-orientation-env9da`

💡 Session idea: the previous session's two flattering inferences were not a knowledge
gap — **it was booted somewhere that could not load the things that catch them.** The
skill whose entire job is writing a capability entry correctly (`capability-probe`) was
not loadable in the session that wrote three of them.

## What the session did

Walked the full boot read path (all 8 entries plus `CAPABILITIES.md` end to end),
verified the previous session's claims against the live surface rather than reading
them, merged fm #809, and corrected four things in the records.

## The finding, owner-stated and then measured

The owner, live: *"the previous session booted directly on curious-research and that
caused a few problems; it didn't fully understand the way I work directly. Which is why
I normally boot a session always from the fleet-manager."*

That session's own card corroborates it verbatim — venue *"curious-research session,
fleet-manager attached mid-session"*.

Measured both trees this session:

| | fleet-manager | curious-research |
|---|---|---|
| skills in `.claude/skills/` | **27** | **1** (`visual-explainers`) |
| `.claude/hooks/` | `route_docs.py`, 19 routes | **none** |
| estate read path | the 8-entry path | absent |

`.claude/CLAUDE.md` already covered *several* sources at boot (root falls back to
`/home/user`, everything goes quiet). It never covered **one source that is not the
hub** — where root is that repo, its own `.claude/` loads normally, and the estate's
apparatus is absent **with no error and no gap the session can feel**. That is worse
than the documented case, because the documented case at least leaves the session
naked in a way it might notice.

And the boot file's reassurance that *"`add_repo` mid-session is safe"* is true and
reads as complete when it is not: root is fixed at boot, so attaching the hub later
hands you this file to **read** and loads none of the hooks or skills it routes to.
The routing table's own law — a skill you didn't load can't bind you (PL-013) — is
exactly what applied.

## The four corrections

1. **`.claude/CLAUDE.md` boot triad §2** — three cases now, not two, with the
   satellite-boot case named and measured, and the `add_repo` line corrected to
   "attaches files, not apparatus".
2. **`docs/CAPABILITIES.md` — new entry** recording the above. Filed as a
   **capability**, not a wall: it is a configuration with a silent failure mode, and
   the fix is a boot choice, not a limitation.
3. **`docs/CAPABILITIES.md` — the roster-regen entry, two overstatements** merged
   hours earlier in #809. *"every PR in this repo carries a red `freshness` check"* is
   scoped to `claude/*` branches only (`roster-freshness.yml` runs `--advisory` and
   exits 0 elsewhere; #808 gets no checks at all, so it is blank not red), and
   *"~20 consecutive cron fires"* is **16**. Also strengthened what was right:
   ruled out the branch-filter explanation (`substrate-gate.yml` triggers on bare
   `pull_request`), and confirmed `ROUTINE_PAT` absent — the secrets list is empty —
   which closes the one gap that entry honestly flagged as unconfirmed.
4. **`docs/CAPABILITIES.md` — the step-0 boundary contradicted itself.** The top of
   the file says the boundary is *"not provisioning versus behaviour — that version
   was written here on 2026-08-05 and it licensed a violation within hours."* The
   rationale section at the bottom still read *"He is authoritative on
   **provisioning**"* under a heading claiming to state *"the whole boundary"*. The
   2026-08-05 fix moved step 0 up and left behind the sentence it was made to retire.
   Corrected in place, marked, with the reason kept visible.

Plus `OQ-CR-SLICER-ANSWER` closed — open ~23 days, answered by hardware recorded in
another repo (Bambu A1 mini + A1 AMS Lite → Bambu Studio), with `guides/bambu-studio/`
already shipped. The queue-hygiene lesson is the reusable part: an owner ask can be
resolved by work that never looks at the queue.

## Verified, not read

Everything load-bearing in #809 was checked against the live surface before merging:
PR #808's `total_count: 0`; the rulesets API (`substrate-gate` sole required check, so
the PR was never actually blocked — its own comment hedged on this and one read would
have settled it); `roster-regen` run history; the empty secrets list; curious-research's
41,478-deletion commit, zero `push`-event `pages` runs, both named Pages-enablement run
ids, and the live site returning 200. The curious-research findings held; the
fleet-manager-side entry is what overstated.

## ⟲ Previous-session review

The newest card (`2026-08-07-curious-research-handover`) names its own shape well: the
inference that flatters the asserting party is the one that slips through. It then asks
whether that bias shows up anywhere the asserting party does *not* benefit.

One datapoint toward an answer, from its own diff. The overstatement I corrected —
"every PR in this repo" for what is one branch lane — does not flatter that session at
all. It **enlarges the problem**, which makes the finding more important and the
session that found it more useful. Same direction, different mechanism: not "my work
was necessary" but "what I found matters more than it does". Both inflate; neither is
a knowledge gap; both were available to check in one call.

So the bias may be less about flattery specifically and more about **whichever
direction makes the session's own output load-bearing.** Worth watching under that
wider framing.

## Open, flagged not fixed

- **The roster deadlock is untouched** and is an owner architecture fork, correctly
  routed rather than decided. Recommendation on file: **(d)** retire the roster and its
  freshness gate — it measures a fleet of seats that no longer exists, and OD-9 wants
  one required check per repo. Nothing is blocked meanwhile.
- **The boot read path is growing by accretion** — 8 entries, two of them
  "this exists because a session skipped the last one" patches. It works; I oriented in
  one pass. But the pattern is worth a D2 look rather than a ninth patch.

## Left running

curious-research is attached with push access and cloned. Its `pages` schedule safety
net (`17 */2 * * *`, added in its PR #65) has **never fired** — 7 runs, all
`workflow_dispatch`, zero `schedule` — with its first window not yet reached, so it is
unverified rather than broken. The owner is sending the twelve deep-research documents
next.
