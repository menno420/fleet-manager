# Planning — plans and launch records

> **Status:** `living-ledger`
>
> Index of `docs/planning/` — dated plans and launch/follow-up records. Each
> plan is a snapshot of its drafting moment: verify volatile claims (PR
> states, CI colors) at HEAD before acting (playbook R2). Each entry gets a
> link line below when it merges.

| Date | Doc | Scope |
|---|---|---|
| 2026-08-10 | [Repo navigation plan](2026-08-10-repo-navigation-plan.md) | The owner's browsable-repo directive, designed: the mandatory six-read order, the CORE/TASK/RECORD tier labels, `docs/MAP.md`, and the per-area "you are here" contract |
| 2026-08-08 | [**The agent-operating-environment roadmap**](2026-08-08-agent-operating-environment-roadmap.md) | **The owner's CURRENT plan** (OD-13 puts its Phases 2–3 ahead of the lettered product steps): three phases — retrieval + orientation (landed, fm #826) · intent resolution (first slice landed, fm #830) · the common operating protocol (not started) |
| 2026-08-08 | [fleet-manager as the index — two-layer restructure](2026-08-08-fleet-manager-as-index.md) | Owner-live design decisions for Layer 1 (general, light) + Layer 2 (`docs/repos/<name>/`, per-repo handoff folders); the boot file cites it as canonical for the Layer 2 decisions |
| 2026-07-26 | [Final EAP email — writing-session plan](2026-07-26-final-eap-email-plan.md) | Program step **E1** — **OWNER-RESERVED, deferred since 2026-08-01; not the NOW**: the owner's requirements for the standalone closing review mail (fresh thread · short · Part 1 owner / Part 2 Claude · numbered wish list + the good parts), the source map in priority order, a pre-harvested candidate list, the method, and the boundaries (never re-argue the already-reported cases; Part 1 is never ghost-written) |
| 2026-07-26 | [**The consolidation program**](2026-07-26-consolidation-program.md) | **THE working plan (living-ledger).** Owner directives OD-1..OD-9 · the 7-section target · four step-ledger tracks (D docs-first · W websites · R repos · C CI-to-one-check) with a NOW pointer · the session protocol. Written after the owner's definitive framing (Projects terminated; slow pace; docs+websites first; sessions as the venue). Supersedes plan v2 |
| 2026-07-26 | [Fleet plan v2 — verification-led consolidation (SUPERSEDED)](2026-07-26-consolidation-plan-v2.md) | *(superseded same day by the program above; analysis carried forward)* Reframes the target from repo count to **review surfaces** (the owner's own ceiling: "~10 projects, even 8 was heavy"): 22 repos → **6 review surfaces**. Generalizes shiftlife's proven `plan-conformance.md` into a per-repo "contains vs claims" pass, and sequences **review-and-fold** — verify a repo, surface what's wrong, then merge or archive it — one at a time, highest claim-risk first. Supersedes v1; resolves `OQ-CONSOLIDATION-DELETE-VS-ARCHIVE` = A |
| 2026-07-26 | [CI consolidation](2026-07-26-ci-consolidation.md) | Companion to the fleet consolidation plan: 97 workflow files / 397 runs-per-24h measured live, of which ~44% is autonomous-agent merge plumbing for a program that ended 2026-07-22 and ~175 daily cron runs serve dormant repos. Target **3 uniform checks per active repo** (`test`/`build`/`deploy`) + a short specialist list; ~two-thirds of the cleanup falls out free when the repo archive step lands |
| 2026-07-26 | [Fleet consolidation plan (product topology) — v1, SUPERSEDED](2026-07-26-fleet-consolidation-plan.md) | *(superseded same day by v2 above; census evidence still sound and reused)* Owner-directed 22 → 9 consolidation, organized by **product** instead of agent seat: target structure, the legal/release constraints that cannot be traded away, and 7 sequenced workstreams (W1 graduate phone-controller · W2 consolidate the bot into superbot-next · W3 owner-gated live-test + cutover · W4–W7 CLIs, archive, retire apparatus). Records owner decisions OD-1/2/3. **Supersedes the 2026-07-12 seat-based plan** |
| 2026-07-24 | [App plan — Life Admin platform / ShiftLife first](2026-07-24-app-plan-life-admin.md) | Owner-requested product plan from the 2026-07-24 pasted market research: build a Personal Operations Core narrowly and ship **ShiftLife** (household shift-calendar, free-forever core + one-time Pro) as app #1; free-vs-paid charter, architecture, phased roadmap, GTM, kill criteria; `OQ-APP-PLAN-GO` **RESOLVED same day — owner GO, defaults D1–D5; `menno420/shiftlife` created and phase-0 pushed** (row corrected 2026-08-11, audit D77) |
| 2026-07-19 | [Session-card idea backlog (GENERATED)](idea-backlog.md) | Machine-harvested index of `.sessions/*.md` card 💡 ideas **in the bullet form only** (`- 💡`; the majority heading/paragraph forms are NOT harvested — audit D36, 2026-08-11, so this is a floor, not the corpus) — regenerate with `python3 scripts/gen_idea_backlog.py`; a grooming pass starts here AND still hand-greps the unharvested forms |
| 2026-07-19 | [Next executable slices — night-shift idea groom](2026-07-19-next-slices.md) | Ranked queue of next fm-seat slices groomed from the ~8 night-shift session-card 💡 ideas (top 3: lane-liveness checker · regen-window skip detector · I8 provenance remedy); dropped/routed ideas recorded with reasons |
| 2026-07-14 | [Fleet docs centralization plan](2026-07-14-central-docs-plan.md) | The 19-repo review's actionable plan making fm the single source of truth for fleet docs — 47 enumerated items in 5 classes, Slice 0 + Phases 1–5; landed here per its own §1 Self-application (moved from `docs/central-docs-plan.md`, permanent stub left) |
| 2026-07-12 | [Repo consolidation plan (phase B)](2026-07-12-repo-consolidation-plan.md) | Owner-facing consolidation plan: 19 → 16 unarchived repos / 8 seats; Phase 1 agent migration ORDERs, Phase 2 one-letter owner decisions (incl. cron trims + the ≤2026-07-13 bundle), Phase 3 owner clicks; reconciles census PR #119 with proposal PR #121 (supersedes it and owner-queue E#37) |
| 2026-07-17 | [Overnight planning menu](overnight-menu-2026-07-17.md) | 25 veto-ready fleet-manager seat proposals from the 2026-07-16 overnight run (seat-era record) |
| 2026-07-11 | [ORDER 016 follow-ups](order-016-followups-2026-07-11.md) | Ready-to-file draft ORDER text from the ORDER 016 now-scope session (coordinator files them into `control/inbox.md`) |
| 2026-07-10 | [Gen-2 launch record](gen2-launch-record-2026-07-10.md) | Record of the gen-2 fleet launch (overnight 2026-07-09/10) + morning-consolidation verification |

## Provenance — the frozen superbot centralization seeds

The 2026-07-14 central-docs plan supersedes the two superbot planning docs
that seeded fm's mission and triage register (plan §1 Self-application).
They stay superbot-side as **frozen provenance seeds** (verified present at
superbot `3477594`, 2026-07-14), each due a supersession banner pointing at
the plan above (routed via inbox ORDER — superbot is outside fm write
scope):

- [superbot `docs/planning/fleet-centralization-plan-2026-07-11.md`](https://github.com/menno420/superbot/blob/34775943da081dd0a1dc7cf858efc0889726fcf6/docs/planning/fleet-centralization-plan-2026-07-11.md)
  — Option A custodian-primary (the owner decision that made fm the records
  custodian); seeded fm's P1–P3 toolchain.
- [superbot `docs/planning/fleet-review-2026-07-11.md`](https://github.com/menno420/superbot/blob/34775943da081dd0a1dc7cf858efc0889726fcf6/docs/planning/fleet-review-2026-07-11.md)
  — the 2026-07-11 fleet review; seeded fm's fleet-triage register.
