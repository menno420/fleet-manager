# Q-index — repo-qualified owner-decision register (INDEX)

> **Status:** `living-ledger`
>
> **INDEX, not a copy** (central-docs-plan C6, class C source-of-truth rule):
> the canonical write surface is superbot
> [`docs/owner/maintainer-question-router.md`](https://github.com/menno420/superbot/blob/main/docs/owner/maintainer-question-router.md)
> (Q-0001…Q-0274 at seed time, ~9.9k lines, append-only). This file is fm's
> repo-qualified Q→pointer table for the Q-numbers that are cited **across
> repos** — it exists to kill the ID-mislabel class (a shared Q-NNNN grammar
> across ~19 repos with no central lookup). Never restate ruling bodies here
> (a copy is drift by construction); one line + a pointer, nothing more.
>
> Seeded 2026-07-14 (Slice 0 item 5) against superbot @ `3477594`; every
> entry below was grep-verified against the router at that SHA. Grow it as
> new Q-numbers earn cross-repo citation.

## Citation grammar

- **Repo-qualified, always:** `superbot:Q-0262`, never bare `Q-0262` in a
  cross-repo doc — other repos mint their own Q-numbers from the kit grammar,
  so a bare ID is ambiguous by construction (plan §6, ID-namespace risk).
- **Sub-rulings:** `superbot:Q-0262.7` means **numbered item 7 inside the
  Q-0262 block** (the router writes multi-part directives as numbered lists,
  not standalone headings) — cite the parent Q + the item number, and expect
  a grep for the literal string "Q-0262.7" in the router to find nothing.
- Anchors into a ~9.9k-line append-only file are not stable; link the file
  and grep the Q-ID.

## Cross-repo-cited Q-numbers (grep-verified @ superbot `3477594`)

| Repo-qualified ID | One line (pointer, not the ruling) |
|---|---|
| `superbot:Q-0240` | Agent decision authority — decide-and-flag over route-up; reversible-until-gate decisions are the agent's. |
| `superbot:Q-0242` | CCR settings.json allowlist entries exist but still prompt — recovery duties must run Routine-spawned, never rely on settings.json grants. |
| `superbot:Q-0254` | Understand-and-reflect — restate the fuller picture before substantive work; graduated to kit doctrine same day. |
| `superbot:Q-0262` | Blanket application of the round-3 recommended answers (numbered applied rulings — see sub-ruling grammar above). |
| `superbot:Q-0262.4` | Model-line policy: family-level names ONLY, everywhere (feeds the 📊 Model card line + fm model matrix). |
| `superbot:Q-0262.7` | Pokemon concept pick = QoL+ (the lane's own recommendation; effective when the games program boots post-core). |
| `superbot:Q-0262.8` | Core seat 6 = superbot hub — **SUPERSEDED by Q-0264.2** (sim-lab took seat 6; the flagged veto arrived). |
| `superbot:Q-0263` | Never-ask posture — derivable values never route to the owner; asks must be paste-ready (kit ORDER 008 class). |
| `superbot:Q-0264` | Idea-pipeline redesign — own-repo idea-engine + sim-lab as core seat 6; evidence-gated routing through the manager. |
| `superbot:Q-0265` | Continuous mode for ALL six core seats — the routine is a failsafe, not the pacemaker. |
| `superbot:Q-0266` | Volume-first founding doctrine — maximize output at creation, consolidate later. |
| `superbot:Q-0269` | Live sessions merge finished PRs themselves — never park green PRs on the owner's queue. |
| `superbot:Q-0270` | Boot triad — every session establishes model · venue · ability envelope before directing work. |
| `superbot:Q-0272` | Standing cross-repo read authorization + the multi-repo reading path in boot orientation. |
| `superbot:Q-0274` | The fleet-grounding file — one living doc any session reads to understand the projects (owner-directed home: superbot; move is Phase 5, propose-only). |

## Known mislabels (the class this index exists to kill)

| Where | Wrote | Verbatim router truth |
|---|---|---|
| fm `docs/findings/manifest-parallel-run-2026-07-11.md` (pokemon row) | "Q-0266 pick = Emerald QoL+" | The QoL+ concept pick is `superbot:Q-0262.7`; Q-0266 is the volume-first founding doctrine. Corrected in place 2026-07-14 (bracketed note — dated findings are never silently rewritten). |

## Graduation candidates (superbot-next candidate 3, plan C6)

Cross-repo-cited Q-numbers proposed for promotion into kit program-law (PL)
entries, so lanes cite a PL-ID instead of reaching into superbot's router:
`superbot:Q-0265`, `superbot:Q-0269`, `superbot:Q-0270`, `superbot:Q-0240`.
Routing: kit-lab ORDER (program law is kit-owned, D-0002) — a later phase,
recorded here so the nomination isn't lost.
