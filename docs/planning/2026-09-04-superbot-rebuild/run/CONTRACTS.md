# CONTRACTS — SuperBot rebuild comparative review fan-out

> **Run:** fm session `claude/superbot-rebuild-review-20f9hq`, 2026-09-04.
> Written **before** the first review agent spawned, per
> [`.claude/skills/fleet-preflight/SKILL.md`](../../../../.claude/skills/fleet-preflight/SKILL.md).
> Quoted verbatim in the published plan. Scripts beside this file.

```
AGGREGATE   : STRENGTH dies_if not(  (not refuted)
                    and (evidence_class in {PRODUCTION-PROVEN,LIVE-TESTED,SOURCE-ENFORCED,OWNER-VALUED}
                         or (evidence_class == TEST-PROVEN and effect_asserted))
                    and (enforcement_locus not in {documentation_only,none})
                    and (consumers >= 2 or prevents_failure != ''))
              DEFECT   dies_if not(  (not refuted)
                    and (evidence_class in {PRODUCTION-PROVEN,LIVE-TESTED,SOURCE-ENFORCED,
                                            TEST-PROVEN,OWNER-VALUED,MEASURED})
                    and (failure_scenario != ''))
              · unread fields 0 (exit 0, survival_rule.py; REPORT_ONLY is PER RULE —
                enforcement_locus decides for a strength and describes for a defect)
              · fixture kill 4/6 · fixture survive 2/6 (exit 0)
              · refute authority 3/3 — every verifier lens carries the refute instruction
              · already_covered_by is READ by the merge step (raises corroboration on the
                named id), never discarded — the 815/925 defect of the 2026-08-29 estate run
INSTRUMENT  : capture_literal_scan.py · positives 5/5, negatives 6/6, exit 0
              · real-slice: D1 (name-shaped module-level literal) 12 hits in sb/domain,
                ALL 12 READ BY HAND → 1 true positive (_COGS, already labelled), 11 false
                (identity strings `_SUBSYSTEM="ai"`, boot flags `_installed=False`, empty
                runtime registries `_tables={}`, BTD6 power constants).
                **D1 PRECISION 1/12 — RETIRED as a decisive instrument.** The unlabelled-
                instance hunt the 2026-08-05 audit named in its § 6 is NOT mechanizable by
                name; it is routed to a semantic agent lane instead.
              · D2' (the convention's own vocabulary, not just its formal label) IS kept as
                a SELECTION instrument: `capture.world|honest successor|successor read|
                shipped verbatim|golden.pinned|pinned literal|the oracle carried|goldens pin`
                → 137 of 634 sb/ files · 116 of 382 sb/domain files (30%), against the
                audit's 4 formally-labelled. It selects candidates; it does NOT classify
                them. Classification is the agent's job, one sampled slice, read by hand.
PILOT       : lane P (superbot navigation reachability) × 2 agents, run first
              · 2 transcripts read whole (raw/pilot-journal.jsonl) before the remaining
                lanes committed
              · CHANGED, five things, all from what the pilot exposed:
                1. SIZE was wrong by 2.6x. Planned ~420s/agent; measured 997s and 1,241s
                   (95 and 130 tool calls, 219k and 284k tokens). Fleet cut from ~52 agents
                   to 33 and re-floored at ~5.0 h. The 420s was a guess wearing a number.
                2. The pilot's two agents CONTRADICTED each other and the contradiction was
                   the single most valuable output (P1: reachability is CI-enforced with a
                   teeth test, max 2 clicks, 0 orphans · P2: that guard checks a MODEL of
                   the UI, and the Moderation hub declares 6 children while its rendered
                   panel has none). Every fleet prompt now carries an explicit instruction
                   to name contradictions with prior audits and sibling lanes rather than
                   smoothing them.
                3. Added the highest-yield question the pilot found by accident, now asked
                   of every guard in both repos: WHAT POPULATION DOES THIS GUARD RUN OVER,
                   AND CAN THAT POPULATION BE EMPTY? (Found independently by this session
                   in superbot-next's navigation golden; the pilot found its twin in
                   superbot's help-reachability sim.)
                4. Row budget raised 10 -> 12 per class. P2 dropped a verified finding
                   explicitly "because the row budget was full, not because it is refuted".
                5. discord.py and asyncpg are NOT installed in this container, so the repos'
                   own checkers cannot be run directly. The pilot solved it by writing stub
                   modules and setting PYTHONPATH; that recipe is now in the shared prompt,
                   because without it a lane reports "could not run" where a real exit code
                   was available (P1 got check_command_reachability.py to REAL_EXIT=0 that
                   way).
CORPUS      : superbot 883 runtime .py / 243,961 LOC (59 cog modules, 24 cog packages,
                190 services, 250 view .py, 41 core/runtime, 16 governance, 192 utils,
                104 migrations) + 1,060 test files / 244,805 LOC + 863 docs .md +
                970 session cards + 18 workflows
              superbot-next 634 sb/ .py / 150,328 LOC (kernel 20,486 · domain 111,929 ·
                adapters 6,375 · app 1,821 · manifest 5,545 · spec 22 files) +
                48 domain subsystems + 273 test files / 78,171 LOC + 57 migrations +
                551 parity golden files + 92 docs .md + 335 session cards + 8 workflows +
                a 2.2 MB manifest.snapshot.json
              spider-bot 27 runtime .py / 3,172 LOC + 15 test files + 4 docs .md
                (BOUNDED — read only for the four questions § 2 of the brief names)
              from working clones at /home/user/{superbot,superbot-next,spider-bot}
                at 2026-09-04T11:52:55Z
RETAIN      : per finding — repo · file · line_span · verbatim quote · evidence_class ·
              enforcement_locus · consumers · prevents_failure · effect_asserted ·
              new_failure_class · already_covered_by · per-lens refute verdicts (not the
              tally) · the lane prompt that selected it.
              Raw agent JSON retained under run/raw/.
              Follow-up this fleet is expected to recommend — "for capability X, does the
              successor's proposed gate actually assert an effect?" — answerable: YES
              (effect_asserted + failure_scenario are carried per row).
              Second follow-up — "which unlabelled capture literals exist?" — answerable:
              PARTIALLY. D2' gives the candidate set and its size; exhaustiveness is NOT
              establishable by this run and is written into the report as an honest null.
BASE        : fleet-manager @ caa6cd2ab6591794258b68b3c385a8378a55c8d3 (SHALLOW clone,
                58 of N commits — no history claim is made from it)
              superbot @ 5e3a667b2a55bae98a7863dd66492f477dd19546 (6,391 commits, full)
              superbot-next @ d5f66dc27768d49b2755f368c6a2d0ecca66a1af (653 commits, full)
              spider-bot @ bf4d75278a74147aaf9c7f19e2da2c7abb1939cb (20 commits, full)
              at t0 = 2026-09-04T11:52:55Z
              open PRs — superbot #2453 #2451 #2447 #2402 #2401 #2400 #2399 #2398
                (ALL 8 dependabot; D-0017 parks them; zero product changes pending)
              superbot-next 0 · spider-bot 0
              NOTE: superbot and superbot-next are at the EXACT pins the 2026-08-21 GCB
                plan reviewed (5e3a667b / d5f66dc2). Neither product tree has moved in
                14 days. spider-bot HAS moved (e0d8909 → bf4d7527).
              re-read <sha>..origin/main for all four repos immediately before writing
SIZE        : limit 2 — MEASURED by DEMAND TEST 2026-09-04T11:54Z, not quoted.
              6 probes dispatched at one instant on a 4-CPU box; peak overlap 2, mean(busy)
              1.5, mean duration 8s. Starts track slot-frees (ends 7.5/7.8s → starts
              11.5/11.6s; end 19.0s → start 23.0s; end 23.6s → start 28.2s) and within-wave
              provisioning is 0.9s, so this is SLOT-limiting, not provisioning-limiting.
              Dispatch→first-assistant gap flat at 1.7–2.3s across a 28s queue span (one
              7.0s outlier), so first timestamps mark execution, not dispatch — the
              discriminator applies. Documented cap min(16, CPUs−2) = 2 agrees, but the
              number here is measured.
              REVISED AFTER PILOT: 33 agents × ~1,100s ÷ 2 ≈ 5.0 h floor.
              (Pre-pilot estimate was 52 × 420s ÷ 2 ≈ 3.0 h — wrong on both terms.)
EXTERNAL    : @codex on the plan PR — HARD CAP 3 rounds (D-0039, enforced by
              .claude/hooks/codex_round_guard.py). Mid-run verification of intermediate
              fixes goes to the free-key Gemini route (gemini-3.6-flash), not to Codex
              (D-0019 as amended 2026-08-29). The fleet's own adversarial lanes do NOT
              substitute for the external round.
MODELS      : readers/mappers/census/inventory → sonnet
              · judges, verify, root-cause, product-value, architecture → opus
              · challengers A–F → opus · final critic (last look) → opus
              · fable: none — the owner has not asked for Fable on this run, and
                D-0040 as amended 2026-09-02 makes Fable his call, never the session's.
UNCONTRACTED: (1) Neither bot is BOOTED in this session. Every reachability, effect and
              dynamic-state claim is read from source, the compiled manifest snapshot, or
              the 2026-08-05 live audit — never from a running process. The live audit's
              own honest nulls (click-through census not run; two-tap property not
              measured) are therefore INHERITED by this review, not closed by it.
              (2) The superbot production Discord guild, its Postgres and its Railway
              service are untouched by contract; no live-guild measurement is available
              to this run at all.
```
