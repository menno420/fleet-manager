# fleet-preflight contract sheet — the estate truth baseline run (2026-09-04)

> **Status:** `reference` · tier **RECORD** — evidence for
> [`../../2026-09-04-estate-truth-baseline.md`](../../2026-09-04-estate-truth-baseline.md):
> the run's fleet-preflight contract sheet, filled before the first audit agent spawned and quoted verbatim in the finding.

Filled before the first audit agent spawned, per
[`.claude/skills/fleet-preflight/SKILL.md`](../../../../.claude/skills/fleet-preflight/SKILL.md).
Quoted verbatim in the finding.

```
AGGREGATE   : dies_if  refuted or not source_path or not verification_point
                       or certainty == 'UNVERIFIED'
                       or (contradicted_by and contradiction_resolution == 'unresolved')
                       or (stale_on_copy and disposition == 'carry')
                       or (canonical_owner not in ('hub','owner') and disposition == 'carry')
                       or (only_source_is_hub_summary and certainty != 'OWNER')
              · unread fields 0, undefined 0 (exit 0, tools/estate_baseline/seed_rule.py audit,
                parsed from the rule SOURCE not a retyped copy)
              · fixture kill 8/12, survival 4/12 (exit 0) — expected outcome written per case first
              · refute authority 3/3 — every lens in the refute stage carries the refute
                instruction and returns its own verdict; the tally is never the record
INSTRUMENT  : tools/estate_baseline/delta.py — the UNCHANGED/CHANGED decision
              · unit positives 7/7, negatives (the branch that must not fire: a moved repo
                reading UNCHANGED) 0 occurrences, exit 0
              · real-slice 11/11 controls correct over all 28 rows: 4 known-moved
                (fleet-manager 23 commits, couch-legend 5, substrate-kit 3, websites 2)
                and 7 known-still (pokemon-mod-lab, shiftlife, gba-homebrew, curious-research,
                venture-lab, superbot-next, superbot-plugin-hello) — read by hand against
                each repository's own last-commit date
              · KNOWN LIMIT, stated rather than hidden: the script decides MOVEMENT only.
                WEAK_OR_INCOMPLETE and NEW are judgements about the prior EVIDENCE and are
                set in anchors.tsv, never computed — a script must not launder a judgement
                into a measurement. creator-kit is the live demonstration: mechanically
                UNCHANGED, actually NEW.
PILOT       : delta lane × all 28 rows first (it is cheap and total) · 28 rows read whole
              before any audit agent launched · changed: three things — the archive-notice
              commits made the 9 archived rows read CHANGED until the archived flag was
              given precedence; the anchor had to be the START of the measurement day, not
              its end, or a same-day audit absorbs commits it never saw; and
              creator-kit/estate-backups/product-forge exposed the judgement-overlay gap above.
              Repository lane × 2 agents (spider-swing, creator-kit — one contradicting front
              door, one no-baseline) read whole before committing the remaining 14.
CORPUS      : TWO corpora, censused separately.
              (A) the estate = 28 repositories — 19 non-archived / 9 archived, 3 private
                  (estate-backups, pokemon-mod-lab, shiftlife) — from
                  GET /user/repos?affiliation=owner at 2026-09-04T11:34Z, reconciled against
                  docs/ESTATE.md: 28 rows, 0 live-not-in-index, 0 index-not-live.
              (B) fleet-manager's own candidate live truth = 1,284 tracked files, of which
                  the audited candidate set is 411 — composition from `git ls-files`:
                  owner/ 93 · docs/(loose) 65 · docs/planning 39 · .claude/ 40 · tools/ 37 ·
                  docs/owner-comments 32 · scripts/ 26 · docs/ideas 19 · docs/repos 18 ·
                  docs/providers 11 · docs/conventions 7 · .github 4 · .codex 4 ·
                  docs/activity 3 · templates 2 · root 11.
                  The 873 not in the candidate set are archive-only by construction:
                  .sessions/ 483 · docs/findings 127 · projects/ 77 · .substrate/ 53 ·
                  docs/prompts 52 · docs/proposals 17 · docs/research 16 · environments/ 14 ·
                  docs/audits 9 · docs/experiments 6 · control/ 5 · telemetry/ 4 ·
                  registry/ 3 · docs/succession 3 · docs/retro 3 · docs/(other) 1.
              from /home/user/fleet-manager at caa6cd2 + the live GitHub API, 2026-09-04T11:34Z.
RETAIN      : per repository — repo · default branch · live SHA · fetch instant · every path
              opened (raw URL + the SHA it was fetched at) · the verbatim span quoted for each
              claim · the anchor row that selected it · the instrument version.
              Per seed candidate — all 17 schema fields including the four dissent fields.
              Both the INPUT (the fetched file text) and the OUTPUT (the derived claim) are
              kept, which is the flat rule the 2026-08-29 fleet broke.
              follow-up "at seed time, which of these rows moved since this baseline?"
              answerable: YES — delta.py re-runs against the same anchors.tsv and reports the
              new commits_since; the seed manifest carries a source SHA per row.
              follow-up "would this claim have survived a stricter rule?" answerable: YES —
              killed rows are published with the branch that fired, not dropped.
BASE        : all 28 repos pinned at 2026-09-04T11:34Z; the per-repo table is
              launch-shas.json. fleet-manager@caa6cd2ab659 · substrate-kit@ff06fb902c69 ·
              websites@48b75de8fd30 · spider-swing@fc64a3fbb25f · superbot@5e3a667b2a55.
              open PRs at launch (state=open, per_page=100 — not a default page size):
              substrate-kit #590 (K1–K5, the CONCURRENT session — out of scope) ·
              spider-swing #180 (dependabot) · superbot #2398–#2453 (8, all dependabot) ·
              fleet-manager 0 before this session's own #1020. Every other repo: 0.
              re-read <sha>..main for ALL 28 immediately before writing the finding.
SIZE        : limit 2 via PROBE (demand test: 8 barrier agents dispatched at one instant,
              each held alive 45s by a fixed wait) at 2026-09-04T11:36:05→11:39:35Z.
              Peak 2, mean(busy) 1.88, four clean waves of 2. Discriminator: within-wave
              starts 1.1–3.6s apart (provisioning is fast) while each new wave began
              5.2–11.7s after a slot freed — fast provisioning + starts tracking slot-frees
              is slot-limiting, not provisioning-limiting. The documented min(16, CPUs−2)
              is 8× the measured figure and is NOT used.
              ~46 agents × ~200s ÷ 2 ≈ 4,600s ≈ 1.3 h floor.
EXTERNAL    : @codex at flip-readiness, HARD CAP 3 rounds (decision 39 in `docs/decisions.md`,
              .claude/hooks/codex_round_guard.py DENIES the fourth). Mid-run verification of
              intermediate fixes goes to the free-key Gemini route, not to Codex (decision 19 in `docs/decisions.md`
              as amended 2026-08-29). Budgeted BEFORE the internal lanes were sized: the
              2026-08-29 run's entire yield was its external round.
MODELS      : census/anchor-discovery → sonnet · repository readers → sonnet ·
              fleet-manager area enumerators → sonnet · cold-session answerers → sonnet ·
              contradiction adjudication → opus · seed-disposition judges → opus ·
              refute lenses → opus · blind scorer → opus · final critic → opus
              reasons: adjudication, disposition and refutation each decide what survives.
              reviews last: the final critic, on opus.
              fable: none — decision 40 in `docs/decisions.md` as amended live 2026-09-02 ("Fable should only be used
              when I explicitly request it"). He has not asked for it for this run, so the
              last look runs on opus.
UNCONTRACTED: none.
```

## What this sheet does not cover

- Whether the question is worth ~46 agents. Sizing gives the price, never the value.
- An instrument that matches correctly and asks the wrong question. The pilot is
  the only cover, and only because its transcripts were read whole.
- Anything landing between the pre-publication re-read and the merge.

---

## Addendum — a CORPUS correction the fleet caught, and where the error actually was

An area agent reported: *"The task brief stated the planning population was 41
files; the actual tracked file count (both `find` and `git ls-files`) is 39."*
It is right, and running the check across every area shows the error is narrower
and more interesting than one stale number.

**The `CORPUS` line above is correct.** It was built with
`git ls-files | awk` and its `docs/planning 39` matches
`git ls-files docs/planning | wc -l` exactly; the sixteen per-area figures sum to
the stated 411.

**The per-area `n` hints handed to the agents were built separately, with a
`glob('**')`, and three of eight disagree with it:**

| area | `n` given to the agent | `git ls-files` | why they differ |
|---|--:|--:|---|
| `planning` | 41 | **39** | the glob counted 3 directories as files |
| `repos-and-owner-comments` | 88 | **50** | directories counted, and an `ls` form that double-listed nested paths |
| `apparatus` | 105 | **147** | the opposite error — `.claude/skills/*/SKILL.md` counts one file per skill and misses everything else in each skill directory, so this one **under**-reported |
| `owner-workbooks` | 93 | 93 | correct |
| the other four | — | — | not re-derived; the same glob built them |

So the defect is **two populations counted two ways in one run**, which is the
composition-versus-count failure § 4 of the skill exists to prevent, reproduced
at a smaller scale inside a run that had already contracted against it. It did
not corrupt any finding — `n` was a hint, every agent enumerated its own
population with `ls`/`find` and reported `files_total` from that — but a reader
comparing the sheet against an agent's `files_total` would have found a
discrepancy with no explanation, which is exactly the thing the sheet exists to
stop.

**The figure to quote is `git ls-files`.** Where an agent's `files_total`
disagrees with the `n` in its own prompt, the agent's number is the measured one.

**Coverage is not the same as population, and is reported per lane rather than
assumed.** `owner-workbooks` opened **17 of 93** and said so; that is a
judgement call about a population that is 74 near-identical unanswered forms,
and it is recorded as `files_examined/files_total` on every area result rather
than smoothed into a claim of full coverage.
