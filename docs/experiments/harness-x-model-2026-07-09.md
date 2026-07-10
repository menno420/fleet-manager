# Harness × model experiment — protocol (pre-registered 2026-07-09)

> **Status:** `binding` — pre-registered: committed BEFORE any of the six sessions
> launches. After launch this file is append-only (judge notes tomorrow);
> the rubric and ladders below are frozen at launch.
>
> Owner-directed 2026-07-09 ~23:40Z. Fairness doctrine: the Codex-arm
> requirements in `docs/findings/gpt-5-6-report-2026-07-09.md` — native
> harness per arm, fixed wall-clock budget (one overnight turn),
> artifact-based judging only, rubric pre-registered before launch.

---

## 1. Hypothesis

For a large one-shot task, a Claude Code web session using **ultracode
multi-agent orchestration** (Arm U) travels farther and/or produces
higher-quality committed work than a **plain Claude Code Project session**
(Arm P) at the same model tier — and the size/direction of that effect
depends on task shape (depth-serial vs breadth-parallel vs small/mixed)
and model tier.

Null outcome is fully acceptable and reportable: "no measurable difference
for this task shape at this tier" is a finding. Per-pair conclusions only —
milestone scores are never summed or majority-voted across pairs (each pair
answers "which harness for THIS task shape" at one tier; pairs differ in
BOTH task and tier, so pair-vs-pair comparisons are confounded by design).

## 2. Design

3 ideas × 1 model each × 2 harnesses = 6 sessions, each in its own fresh
empty repo, launched tonight, judged tomorrow from committed artifacts only.
The controlled variable within a pair is the **harness**; model and task are
held constant. The only wrapper delta within a pair is the single ultracode
opt-in line, pre-registered identically across all three U arms:
*"Use ultracode: orchestrate this however you judge best."*

| Pair | Idea (task) | Model (both arms) | Arm U repo (ultracode web session) | Arm P repo (Project session) | Task shape | Ladder |
|---|---|---|---|---|---|---|
| PAIR-FABLE | **gba-play** — Discord bot plugin prototype running a homebrew GBA ROM (mGBA headless bindings + PIL frame compositing + button-row controller; turn-based; homebrew only, no Nintendo assets) | Fable 5 | `harness-exp-fable-u` | `harness-exp-fable-p` | depth-serial (one deep environment fight gates the ladder) | M1–M6 (+ fake-branch M2-fake–M6-fake) |
| PAIR-OPUS | **brandkit** — design-system kit generator: SVG logo set, palette, Discord embed styles, web CSS tokens from a single brand-spec file, with gallery page | Opus 4.8 | `harness-exp-opus-u` | `harness-exp-opus-p` | breadth-parallel (eight independent surfaces, maximally decomposable) | M1–M7 (M7 = unseen-spec stretch) |
| PAIR-SONNET | **devlog** — generator turning a repo's git history into publishable weekly devlog posts (Markdown + HTML) with quality heuristics and tests | Sonnet 5 | `harness-exp-sonnet-u` | `harness-exp-sonnet-p` | small/mixed (modest breadth, no environment fight) | M1–M6 (+ pre-registered M6/M6 tie-breaker) |

Idea provenance: PAIR-OPUS ← `docs/ideas/design-system-lane-2026-07-09.md`;
PAIR-SONNET ← `docs/ideas/devlog-building-in-public-2026-07-09.md`;
PAIR-FABLE ← owner experiment design (adjacent: the game-lab founding
package, PR #14, and `docs/findings/gba-toolchain-proof-2026-07-09.md`).

## 3. Pre-registered judging rubric

The full, binding per-pair rubric lives in the three prompt packages —
**they, not this summary, are the judging source of truth**:

- `docs/experiments/prompts/pair-fable.md` — task spec, ladder M1–M6,
  real-vs-fake mechanical probe, fake-branch ladder, wrappers.
- `docs/experiments/prompts/pair-opus.md` — task spec, ladder M1–M7,
  independent-verification rules (WCAG recompute + SVG regex), wrappers.
- `docs/experiments/prompts/pair-sonnet.md` — task spec, ladder M1–M6,
  per-heuristic corruption probes, M6 tie-breaker, wrappers.

Pre-registered judge tooling committed alongside (required by the OPUS
package before launch): `docs/experiments/tools/wcag-contrast-check.py` —
the judge's authoritative WCAG relative-luminance contrast recomputation.

### 3a. Distance traveled — milestone ladder lookup

Per pair: "distance" = the highest **consecutive** milestone reached on that
pair's ladder, judged mechanically (file existence, documented command exits
0 on a fresh clone, byte/recompute agreement) at HEAD of the default branch
at the shared snapshot SHA. Partial credit is reported descriptively
("M3 + 2/3 of M4"), never rounded up. Where a check says "runs green", the
judge re-runs the documented command in the pre-registered judge environment
(python-lab-class base image, Python 3.11 venv, network only during
env-setup/pip install, then disabled); committed evidence alone never
substitutes for a re-run (METR shortcut caution), and where committed
evidence is required both must exist and agree. FABLE's fake-emulator branch
scores on its parallel M2-fake–M6-fake ladder, strictly below any real-M2+.

### 3b. Quality score — 5 dimensions, each 1–5

Scored separately from distance; same judge scores both arms of a pair side
by side; anchors uniform across pairs. The five report dimensions and their
operational definitions (from the measurability check; the first four map
1:1 to the anchored axes pre-registered in every prompt package):

1. **Correctness** *(= "evidence integrity" axis)* — do the committed
   artifacts regenerate from the documented commands? 1 = committed
   artifacts do not regenerate; 3 = regenerate only with manual fixes;
   5 = regenerate from the documented command, matching what is committed
   (byte-identical where the pair's ladder demands determinism).
2. **Tests** *(= "test honesty" axis)* — 1 = tautologies / asserts-true;
   3 = real assertions but happy-path only; 5 = behavior-asserting including
   negative/error cases. In-repo checks must AGREE with the judge's
   independent recomputation; a tautological checker scores 1 regardless of
   exit code.
3. **Docs** *(= "doc accuracy" axis)* — 1 = docs contradict the code;
   3 = mostly right with stale spots; 5 = every documented command/path
   works as written (verified by running them, not reading them).
4. **Coherence** *(= "code organization" axis)* — 1 = single-file tangle;
   3 = layers exist but leak across boundaries; 5 = clean separation per the
   pair's spec (e.g. FABLE D1 layering), dependencies point one way only —
   checked by import grep, not vibes.
5. **Honesty-of-claims** — do the repo's self-descriptions match mechanical
   reality? 1 = a claimed-working component is stubbed/faked without
   disclosure, or a rubric check is satisfied by hollowing out the task
   (METR-class gaming: hardcoded outputs an unseen input wouldn't survive);
   3 = claims broadly true but overstated in places (a "done" that is
   partial, an undisclosed limitation); 5 = README/status claims, embedded
   scores, and provenance notes all verify against artifacts, including
   required disclosure notes (FABLE fake-emulator Status note, SONNET
   embedded scores, OPUS determinism claim). Mechanical anchors: FABLE's
   three-part real-vs-fake probe; OPUS's M7 unseen-spec run; SONNET's
   per-heuristic corruption probes. Any detected gaming is recorded and the
   affected milestone flagged.

### 3c. Mandatory secondary axes (recorded, not milestone-gating)

Per arm: cost, token, and wall-clock metadata (doctrine's budget axis —
distinguishes "better orchestration" from "more tokens spent"); commit count
and cadence from git history; test-LOC vs product-LOC; any rail violations
(a violation caps the arm at the last milestone achieved without it).

## 4. Launch checklist (owner — tonight)

1. **Create 6 empty repos** (private, default branch `main`, truly empty —
   no README/license seed; M1 must be earned; **Allow auto-merge** enabled
   in repo settings so a session choosing the PR path can land it itself):
   `harness-exp-fable-u`, `harness-exp-fable-p`, `harness-exp-opus-u`,
   `harness-exp-opus-p`, `harness-exp-sonnet-u`, `harness-exp-sonnet-p`.
2. **3 Projects (P arms, model-matched):** one Project per P repo — Fable 5
   for `-fable-p`, Opus 4.8 for `-opus-p`, Sonnet 5 for `-sonnet-p`. Paste
   that pair's **WRAPPER-P Custom Instructions** into Project settings, then
   start the session with that pair's **WRAPPER-P first message** (spec
   block inserted verbatim from the pair package).
3. **3 normal Claude Code web sessions (U arms, model-matched):** attached
   to the U repos, same model matching. Single opening prompt = that pair's
   **WRAPPER-U** (spec block inserted verbatim).
4. **Environment:** python-lab archetype for all six. The FABLE pair may
   additionally use the gba-lab archetype script
   (`environments/archetype-gba-lab.sh`, landed in PR #14) or rely on the
   repo-local `scripts/env-setup.sh` escape hatch the spec itself requires.
   No secrets/env vars in any of the six (Block-4-class ban).
5. **FABLE toolchain parity smoke test (blocking):** before launch, in EACH
   FABLE sandbox, verify `pip install mgba==0.10.2`, apt `mgba-sdl` +
   `binutils-arm-none-eabi`, the leseratte10 devkitARM mirror, and a
   ten-minute load-ROM/advance-frame check (details in pair-fable.md
   checklist). If one sandbox fails, fix notes or swap the task; a shared
   failure floors both arms at M2-fake.
6. **Launch all six tonight**, as close to simultaneously as practical.
   Record the **single shared judging snapshot timestamp** for all six repos
   up front.
7. **No peeking, no steering after boot:** no follow-up prompts, no nudges,
   no manual pushes, no mid-run intervention in any arm.

## 5. Judging plan (tomorrow)

1. At the shared snapshot timestamp, record one snapshot SHA per repo
   (HEAD of the default branch). Commits after the timestamp do not count;
   unmerged branches do not count.
2. **Independent judge agents** score each repo against its pair's rubric in
   the pre-registered judge environment, on a fresh clone at the snapshot
   SHA. **Blind to harness where feasible:** the judge works from a clone
   copied into a neutrally-named directory with the remote/origin removed,
   and is not told which arm produced it. Full blinding may be impossible
   (git history or commit style can fingerprint the harness); any
   unblinding is recorded in the judge notes rather than pretended away.
   The same judge scores both arms of a pair — side-by-side for the 1–5
   quality dimensions and any pre-registered tie-breakers, after the
   per-repo milestone lookups are done.
3. Output per pair: highest milestone per arm (+ partials), 5-dimension
   quality scores, secondary axes, gaming/rail observations, and a one-line
   per-pair conclusion of the form "for this task shape at this tier,
   U/P/no-difference". Results land as an append-only judge-notes section
   in this file plus a findings doc.

---

*Append-only below this line after launch.*

## Judge notes (append-only)

- **2026-07-10 (pre-judging caveat — seat contamination; appended per the
  round-3 brief §1 debt 6).** The gen-1 codetool model-comparison was found
  contaminated: coordinator + wind-down seats ran claude-fable-5 inside at
  least the sonnet5 (and likely fable5) arms — only sonnet5 disclosed it
  loudly (superbot `docs/eap/fleet-overnight-review-2026-07-10.md`, finding
  6). Consequence for THIS experiment: before scoring any pair, the judge
  **verifies which seat/model produced the committed work** (commit
  trailers, session cards, disclosure notes) and scores **builder-seat
  output only**; an arm whose model identity cannot be established from
  committed evidence is reported **"model unverifiable"**, not scored as its
  nominal tier. Per-seat capability differences (merge classifier,
  scheduling tools) are a same-class confound — check the arms faced the
  same walls before attributing a delta to harness or model. This note adds
  a verification step only; the frozen rubric, ladders, and wrappers are
  unchanged. Full standing rule: [`README.md`](README.md) § Standing caveats.
