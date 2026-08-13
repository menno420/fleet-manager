# 2026-08-13 · hub — run the fresh-SCORER half of roadmap § 4.8

> **Status:** `in-progress`

- **📊 Model:** fable-5 · high · review/verify — run the fresh-scorer half of
  roadmap § 4.8: scorer subagents that have seen neither this conversation nor
  any adjudication re-score the five committed fresh-agent maps against the
  pre-registered rubric; deliver the divergence comparison against fm #851's
  § 3 scoring; land the finding and the surface updates it obligates

Time: 2026-08-13 · venue: continuation session (owner prompt, decisions carried
from fm #851's session) · branch `claude/fresh-scorer-roadmap-4-8-e5s1xv`
(started at `51703ca` = `origin/main` after fm #851 merged; 0 open PRs
confirmed at start)

## Previous-session review

⟲ fm #851 (card `.sessions/2026-08-12-intent-map-fresh-agent-test.md`,
`complete`) ran § 4.8's producer half: five fresh maps, pre-registered rubric,
scored by the running session, verdict PARTIAL — checked against `main`: the
finding, the evidence folder (5 maps · 4 TSVs · checker · prompts) and every
claimed surface update are in `51703ca`; its two deliberately-deferred items
(the intake one-liner, finding § 4 point 4; the fresh-scorer half, § 1.5/§ 5)
are exactly this session's scope. Nothing to repair.

## What is about to happen

1. **The task:** the one named-outstanding item on the owner's current plan
   (OD-13 → roadmap Phase 2). The recorded § 4.8 bar is a fresh agent that
   produces **and scores** (replay finding § 4; fm #830 disposition). fm #851
   discharged the producer half; the scorer half runs here. The deliverable is
   a **comparison, not just a re-score**: fresh-scorer verdicts beside the
   committed § 3 scoring, divergences named — divergence measures the prior
   (outcome-aware) scorer's bias, and "the prior scoring was wrong" is a valid
   result.

2. **Scorer structure (design call, stated before launch):** **two independent
   fresh scorer subagents, each scoring all five maps.** Structure-matched to
   the committed condition (§ 3 was one scorer over all five maps) so the only
   varied factor is outcome-knowledge; two of them so fresh↔fresh agreement
   bounds scoring noise when reading fresh↔prior divergence — if S1 and S2
   disagree with each other as much as with § 3, the divergence is noise, not
   bias, and the finding must say so. Same model family as producers and prior
   scorer (kept deliberately; recorded as a null).

3. **Scorer isolation — inputs, redactions, probes (mirrors § 1.3 of the
   producer finding, upgraded for a tree that now contains the outcomes):**
   - **Inputs, per scorer, in a hermetic scratchpad sandbox** (outside the
     repo checkout): the five raw maps verbatim (`agent-A1..A3, B1, B2`); the
     two producer ask-prompts verbatim (`prompt-A.md`, `prompt-B.md` — the
     maps are unscorable without the handed ask and procedure text, and they
     carry no adjudications); the finding's §§ 1–2 design-and-rubric text with
     the redactions below; both pinned snapshot trees rebuilt from the
     committed pins (`git archive 7fbc065` / `f53d7ea`, finding § 6);
     `verify_citations.py` verbatim (reusable per the fm #851 decision —
     scorers build their **own** rows). Nothing else.
   - **Redacted out of §§ 1–2:** § 1.5 entirely (it frames the prior scoring
     and states the observed error direction), replaced by a neutral scorer
     charge; the two Codex-round parentheticals (§ 1.3's pin-A cell, § 2's
     unscored-note sentence) — each records what "the agents had right", i.e.
     outcome data. No text anywhere tells the scorers a prior scoring exists.
   - **Forbidden and physically absent from the sandbox:** finding §§ 3–6,
     the evidence README (all adjudications), the prior `citations-*.tsv`
     (they encode the prior scorer's needle choices and known enumeration
     gaps), the replay walkthrough, handoff-fidelity's prompt/verdict columns,
     every fm #851 summary surface.
   - **Leak probes before launch:** (a) mechanical — grep the assembled
     sandbox for outcome needles (verdict words, tally numbers, review-round
     vocabulary, `fm #851`, dates ≥ 2026-08-12), adjudicate every hit by eye;
     (b) empirical — a no-tool probe subagent reports verbatim anything its
     *injected* context says about § 4.8 / fm #851 / intent-map outcomes,
     because subagents auto-load the live boot file, whose entry 1b names the
     producer verdict; (c) if (b) leaks, neutralize that boot-file line in the
     **working tree only** for the spawn window, re-probe, launch, restore
     immediately after both scorers have spawned (claudeMd is injected at
     spawn; never committed — no commits happen while the tree is
     neutralized); (d) route-doc audit — every `doc-routes.json` target
     checked for § 4.8 outcomes: none carries any (`docs/CAPABILITIES.md`
     last touched fm #846, pre-#851), so `PreToolUse` injections cannot leak
     the answer key and the hooks stay live.
   - **Containment residual:** instructed + self-attested (each scorer's
     report must list any path touched outside its sandbox), not fully
     audited — the producer finding's § 5 null inherited, and sharper now
     because the live tree holds the answers. The mitigations above narrow
     it; the finding will state what remains.

4. **The OPEN design call, decided:** scorers score the **pre-registered § 2
   rubric only**. The OPEN-column-discipline criterion was added post-hoc in
   fm #851's Codex round 1 — handing it to fresh scorers would import the
   prior scorer's needle choice, the same class the prior TSVs are excluded
   for. Scorers get a free OBSERVATIONS section (anything the rubric does not
   score, kept outside the scored tally); whether a fresh eye independently
   finds the OPEN-parking is itself divergence data. In the comparison table
   that row is labelled post-hoc / prior-only.

5. **Deliverable:** `docs/findings/2026-08-13-intent-map-fresh-scorer.md` —
   per-scorer tallies, fresh↔fresh agreement, the divergence table against
   committed § 3, honest nulls — plus an evidence folder (handed rubric
   verbatim, scorer prompt template, both raw reports, their TSVs, the probe
   record). Where a divergence is mechanically checkable I adjudicate against
   the pinned tree and **label that layer outcome-aware**; fresh verdicts
   stand as data either way.

6. **Bundled:** the intake one-liner deferred in finding § 4 point 4 (decided
   LOW/MEDIUM items report under DECISIONS FLAGGED, never OPEN) · the
   spider-swing `records.md:8` OD-6→OD-3 citation fix (surfaced by agent B2's
   map, verified live at HEAD).

7. **Surfaces updated to the result:** roadmap § 2 table + § 4.8 + § 8 nulls ·
   boot file entry 1b · `docs/current-state.md` · program § 7 row ·
   `intake` SKILL.md replay note · `docs/findings/README.md` index ·
   `docs/SKILLS-local.md` re-apply row.

8. **Landing:** this card born-red first → PR READY immediately →
   work batched → `@codex review` before the flip (inline comments, two-round
   cap) → `python3 bootstrap.py check --strict` exit 0 → flip `complete` last
   → merge on green.

## Close-out

*(fills at close: shipped · verify tails · ⚑/💡/⟲ · PR terminal state ·
Layer-2 handoff line · capability delta)*
