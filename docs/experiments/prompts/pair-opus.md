# PAIR-OPUS — design-system kit generator (Opus 4.8)

> **Status:** `reference`
>
> Harness-comparison experiment package. Drafted 2026-07-09 per owner design
> (fleet experiment, 3 ideas x 1 model x 2 harnesses). Fairness doctrine:
> fleet-manager `docs/findings/gpt-5-6-report-2026-07-09.md` — native harness
> each arm, fixed wall-clock budget (one overnight turn), artifact-based
> judging only, rubric pre-registered BEFORE launch (this file is that
> pre-registration for PAIR-OPUS).
>
> Model tier (controlled): **Opus 4.8** in both arms.
> Repos (fresh, empty): **harness-exp-opus-u** (ultracode arm) ·
> **harness-exp-opus-p** (Project arm).
> Judged tomorrow from committed artifacts at HEAD of the default branch only.
> Idea provenance: fleet-manager `docs/ideas/design-system-lane-2026-07-09.md`
> (owner-originated, state: captured).

---

## 1. TASK SPEC (identical text for both arms — harness-neutral)

The block between the BEGIN/END markers is the canonical spec. Both wrappers
embed it **verbatim**. It deliberately contains no vocabulary that presumes
either multi-agent orchestration or a single linear session ("the work",
"this repo", never "you should first... then...").

<!-- SPEC-BEGIN -->
### Mission

Build **brandkit**: a generator that turns ONE brand-spec file into a
complete, coherent visual kit. Given a small declarative spec (brand name,
one or two seed colors, a personality/tone field, optional font stack), the
generator produces every visual surface a small product family needs, all
derived from that single source of truth so they visibly belong together.

### Concrete deliverables (all committed to this repo)

1. **Brand-spec format** — a single human-editable file (YAML, TOML, or JSON;
   pick one and document it) that is the ONLY input. A documented schema and
   at least **two** distinct committed example specs (e.g. a playful brand
   and a formal brand) that exercise different corners of the schema.
2. **Palette derivation** — a full color system computed from the seed
   color(s): accent scale, neutral scale, semantic colors (success / warning
   / danger / info), and light + dark surface/text roles. Include a
   machine-checkable accessibility pass: generated text/surface pairings meet
   WCAG AA contrast (>= 4.5:1 normal text), verified by code in this repo,
   not by eye.
3. **SVG logo set** — at least three generated variants per brand (e.g. full
   wordmark, compact mark/monogram, single-color/mono variant), as valid
   standalone SVG files using only colors from the derived palette and no
   external references (no linked images, no webfont URLs).
4. **Discord embed styles** — a generated artifact (JSON and/or a small
   Python module) defining embed styling for a Discord bot: embed accent
   colors per semantic role, emoji/prefix conventions, field layout
   conventions, and at least one worked example embed payload per role.
5. **Web CSS tokens** — a generated `tokens.css` (CSS custom properties) plus
   a machine-readable `tokens.json`, covering color roles (light + dark),
   type scale, spacing scale, and radii, named consistently with the embed
   styles so the same role names appear on both surfaces.
6. **Gallery page** — a generated static HTML page per brand that displays
   the whole kit in one place: logos, palette swatches with contrast
   annotations, token table, and rendered mock Discord embeds (HTML/CSS
   mockups are fine). It must open correctly from the local filesystem with
   zero network requests (all assets inline or relative) and must respect
   light and dark color schemes.
7. **CLI** — one command regenerates everything for a given spec (e.g.
   `python -m brandkit build specs/example.yml -o dist/`). Regeneration is
   deterministic: the same spec produces byte-identical output (any
   randomness must be seeded from the spec).
8. **Tests + docs** — an automated test suite runnable with a single
   documented command, and a README covering: what this is, install/run
   steps, the spec schema, and a description of how outputs stay coherent.
   Commit the generated output for both example specs (e.g. under `dist/`)
   so the results are inspectable without running anything.

### Tech constraints

- Python **3.11**, standard library plus small pure-Python dependencies only
  (e.g. PyYAML, Jinja2, pytest are fine; no headless browsers, no image-
  editing binaries, no node toolchain). Pin any dependency in
  `requirements.txt`.
- SVG and HTML are authored/generated as text — no raster asset pipeline
  required (embedded data-URI rasters are allowed but not required).
- Everything must work fully offline; generated pages and SVGs must not
  reference any remote URL.
- Repo layout, code quality, and commit hygiene are part of the judged work.

### Hard rails

- **No external publishing**: nothing is deployed, uploaded, or posted
  anywhere outside this repo. No new external accounts or services.
- **No spend**: no paid APIs, no purchases of any kind.
- **No secrets**: no tokens, keys, or credentials anywhere in the repo or
  its history.
- Use only assets you generate or that are unambiguously license-free; do
  not copy any existing brand's logo, name, or trade dress. Example brands
  must be fictional.
<!-- SPEC-END -->

---

## 2. MILESTONE LADDER M1–M7 (pre-registered; artifact-lookup only)

Judged tomorrow strictly from HEAD of the default branch of each repo. Each
milestone is a set of mechanical checks — file existence, a command exiting
0, a byte comparison — so "how far did it get" is a lookup, not a judgment
call. A milestone counts only if **all** its checks pass; the score is the
highest milestone whose entire ladder below it also passes (no skipping).
Judge environment: clean python3.11 venv, `pip install -r requirements.txt`
if that file exists, network disabled during checks. One snapshot SHA per
repo is recorded at the single shared timestamp used for all six experiment
repos; commits after it do not count.

**Independent verification (pre-registered):** in-repo checks must exist
AND agree with the judge's independent recomputation — the independent
result is authoritative (a tautological in-repo checker, e.g. `assert
True`, fails the milestone regardless of its exit code). Contrast: the
judge recomputes WCAG relative-luminance contrast on every text/surface
pairing in `tokens.json` using the 15-line reference script committed to
the fleet-manager experiment folder before launch. SVG palette membership:
the judge extracts colors with the pre-registered fill/stroke regex
`(?:fill|stroke)\s*[:=]\s*["']?(#[0-9a-fA-F]{3,8}|rgb\([^)]*\))` and checks
membership against `tokens.json`.

**M1 — Walking skeleton.**
- README.md exists and names an entry command.
- At least one brand-spec example file is committed.
- The documented command runs against that spec and exits 0, producing at
  least one output file (or the committed `dist/` already contains at least
  one generated file and the command reproduces it).

**M2 — Palette + tokens core.**
- Running the CLI on an example spec emits `tokens.css` AND `tokens.json`.
- `tokens.json` contains accent + neutral scales, the four semantic roles,
  and both light and dark surface/text roles (key presence check).
- A contrast check exists in-repo (script or test) and exits 0, asserting
  >= 4.5:1 for every generated normal-text/surface pairing.

**M3 — Logo set.**
- >= 3 SVG files generated per brand; each parses as XML (`xml.etree`), has
  an `<svg>` root, and contains no `http://`/`https://` reference.
- Every fill/stroke color used in the SVGs appears in that brand's
  `tokens.json` palette (checkable by string/regex sweep; a committed script
  or test in the repo performs this check and exits 0).

**M4 — Multi-surface + gallery.**
- Discord embed styles artifact exists (JSON or Python module) with per-role
  accent colors matching palette values, and >= 1 example embed payload per
  semantic role.
- Gallery HTML generated per brand; contains zero `http(s)://` references;
  references only files that exist in the output tree; inlines or
  relatively references EVERY committed logo SVG for the brand; contains
  >= 1 element per palette role whose style value equals that role's
  `tokens.json` color; and contains >= 4 embed mock blocks (one per
  semantic role).
- Role names appearing in the embed artifact also appear in `tokens.json`
  (cross-surface naming coherence, mechanical string check).

**M5 — Two brands + determinism.**
- Two distinct example specs committed, with committed generated output for
  both, and the two outputs differ (different palettes/logos — byte-level
  inequality of tokens.json suffices).
- Determinism: running the CLI twice into fresh output dirs produces
  byte-identical trees (`diff -r` clean); rerunning also reproduces the
  committed `dist/` byte-identically.
- The spec schema is documented (README section or docs file) and both
  example specs validate against it via an in-repo validator that exits 0
  on the examples and nonzero on a committed known-bad fixture (or a test
  asserting rejection).

**M6 — Polished, tested, documented.**
- Full test suite: single documented command (e.g. `python3.11 -m pytest`)
  exits 0 with >= 15 test functions collected, covering at minimum: palette
  derivation, contrast, SVG validity, determinism, and spec validation.
- Lint clean: `ruff check .` exits 0. Judge protocol (pre-registered): use
  the repo's pinned ruff version if one is pinned; otherwise the single
  pre-registered judge version **ruff 0.14.0** installed in the judge venv
  — never whatever happens to be on the judge machine.
- Gallery honors light and dark (`prefers-color-scheme` media query or an
  explicit theme toggle present in the generated HTML).
- README additionally documents the spec schema — "in full" operationalized
  as: every key used in the two example specs appears in the README schema
  section (string sweep) — plus architecture in brief and a coherence
  rationale (how outputs stay in sync); CHANGELOG or equivalent progress
  record exists.
- Placeholder sweep of generated `dist/` artifacts: zero case-insensitive
  hits for the fixed grep list `TODO`, `FIXME`, `XXX`, `PLACEHOLDER`,
  `lorem`, `changeme`.

**M7 — Stretch: unseen third spec (scored; ceiling breaker).**
- The judge writes a third, previously-unseen brand spec exercising
  documented schema corners (this promotes the METR third-spec gaming
  check from footnote to a scored ladder rung). M7 passes iff: the CLI
  runs green on the judge's spec; the contrast, SVG-color-membership, and
  gallery checks (M2–M4, judge-recomputed) all pass on its output; AND at
  least one extra surface beyond the eight named deliverables exists and
  regenerates for it (e.g. a favicon/OG-image SVG set, or a second gallery
  theme).

**Secondary axes recorded alongside the milestone score (not part of it):**
commit count and cadence, total LOC vs test LOC, **per-arm cost, token, and
wall-clock metadata (mandatory — doctrine's budget axis; distinguishes
"better orchestration" from "more tokens spent")**, judge's blind 1–5
aesthetic rating of each gallery (same judge, both arms, side by side), and
any rail/rubric-gaming observations (METR caution: a check satisfied by
hollowing out the task — e.g. hardcoded outputs that a fresh spec wouldn't
survive — is noted and the milestone flagged; the third-spec check is now
the scored M7).

**Quality axes (judged separately from distance; scale and anchors uniform
across all three pairs; same judge scores both arms side by side).** Each
axis scored 1–5:
- **Code organization** — 1 = single-file tangle; 3 = layers exist but
  leak across boundaries; 5 = clean separation, dependencies point one way
  only.
- **Test honesty** — 1 = tautologies / asserts-true; 3 = real assertions
  but happy-path only; 5 = behavior-asserting including negative/error
  cases.
- **Evidence integrity** — 1 = committed artifacts do not regenerate; 3 =
  regenerate only with manual fixes; 5 = regenerate byte-identically from
  the documented command.
- **Doc accuracy** — 1 = docs contradict the code; 3 = mostly right with
  stale spots; 5 = every documented command/path works as written.

**Cross-pair protocol (pre-registered; identical text in all three
packages):**
- One shared judging snapshot timestamp for all six repos; commits after it
  do not count.
- No mid-run intervention in either arm of any pair: no follow-up prompts,
  no nudges, no manual pushes.
- Budget framing (doctrine reconciliation): budget = each harness's native
  natural end of one overnight turn; endurance and parallel token spend are
  part of the treatment. To keep "better orchestration" distinguishable
  from "more tokens spent", per-arm **cost, token, and wall-clock metadata
  are recorded as mandatory secondary axes** in every pair, and the shared
  snapshot timestamp acts as the hard wall-clock cutoff.
- Each pair answers "which harness for THIS task shape" only. PAIR-OPUS's
  shape is **breadth-parallel** (eight independent surfaces, maximally
  decomposable). Milestone scores are never summed or majority-voted
  across pairs; report per-pair conclusions only, task shape named
  alongside each.
- The ultracode opt-in sentence is identical in all three U arms:
  "Use ultracode: orchestrate this however you judge best."

---

## 3. WRAPPER-U — ultracode session prompt (repo: harness-exp-opus-u)

Send as the opening message of a Claude Code web session attached to the
fresh empty repo `harness-exp-opus-u`, model Opus 4.8:

```
Use ultracode: orchestrate this however you judge best.

Repo: harness-exp-opus-u (fresh and empty — you are building it from
scratch on the default branch).

[TASK SPEC — paste section 1 between SPEC-BEGIN/SPEC-END verbatim]

Budget: this single turn, running to its natural end — plan for an
overnight, unattended run with no follow-up prompts.

Commit and push everything; the repo is the only judged artifact. Anything
not committed and pushed does not exist. Commit early and often so progress
is preserved even if the turn ends abruptly; direct-to-main commits or a PR
you open AND merge yourself are both fine, but nothing may be left
unmerged/unpushed at the end.
```

## 4. WRAPPER-P — Project boot (repo: harness-exp-opus-p)

**Project Custom Instructions** (the entire project config — minimal, repo
conventions only):

```
Repo conventions for harness-exp-opus-p:
- Commit early and often; push everything. Work is judged solely from what
  is committed and pushed to this repo — anything unpushed does not exist.
- Direct-to-main commits are allowed; if you prefer PRs, open them READY
  and merge them yourself before finishing. Leave nothing unmerged.
- Fresh empty repo: create all structure from scratch on the default branch.
```

**First message of the session** (model Opus 4.8):

```
Repo: harness-exp-opus-p (fresh and empty — you are building it from
scratch on the default branch).

[TASK SPEC — paste section 1 between SPEC-BEGIN/SPEC-END verbatim]

Budget: this single turn, running to its natural end — plan for an
overnight, unattended run with no follow-up prompts.

Commit and push everything; the repo is the only judged artifact. Anything
not committed and pushed does not exist. Commit early and often so progress
is preserved even if the turn ends abruptly.
```

**Information-equivalence note (pre-registered):** both arms receive the
identical spec, the identical budget sentence, and the identical
"repo is the only judged artifact / nothing unpushed exists / merge or
direct-to-main" rules. The only intended delta is the single ultracode
opt-in line in WRAPPER-U ("Use ultracode: orchestrate this however you judge
best") — the experimental variable itself. WRAPPER-P splits the shared
conventions between Custom Instructions and the first message (that split is
inherent to the Project harness shape), but their union carries the same
content as WRAPPER-U's closing paragraph.

---

## Fairness revisions

Applied 2026-07-09 (pre-launch), from the confirmed fairness critiques. Doctrine
(fleet-manager `docs/findings/gpt-5-6-report-2026-07-09.md`) wins on conflicts.

1. **[must-fix] Ceiling effect broken with a scored M7 stretch tier.** The
   judge writes a third, previously-unseen spec exercising documented schema
   corners; M7 = CLI green on it + contrast/SVG/gallery checks pass on its
   output + one extra surface (favicon/OG-image SVG set or second gallery
   theme). This also promotes the METR third-spec gaming check from footnote
   to scored ladder rung.
2. **[should-fix] Self-attesting checks closed.** Pre-registered independent
   verification: the judge's recomputation is authoritative (WCAG
   relative-luminance reference script committed to the fleet-manager
   experiment folder before launch; pre-registered fill/stroke extraction
   regex for the SVG sweep). In-repo checks must exist AND agree; a
   tautological checker fails the milestone.
3. **[should-fix] M4/M6 adequacy judgments concretized.** Gallery: must
   inline/relatively reference every committed logo SVG, >= 1 element per
   palette role with the exact tokens.json color, >= 4 embed mock blocks.
   README schema "in full" = every key used in the two example specs appears
   in the README schema section (string sweep). Placeholder sweep grep list
   fixed: TODO, FIXME, XXX, PLACEHOLDER, lorem, changeme.
4. **[should-fix] Ruff version pinned for judging.** Repo's pinned ruff if
   pinned, else pre-registered judge version ruff 0.14.0 in the judge venv.
5. **[should-fix] Wrapper information asymmetry removed.** The abrupt-end
   checkpointing sentence ("anything not committed and pushed does not exist;
   commit early and often so progress is preserved even if the turn ends
   abruptly") now appears in the P-arm first message, matching WRAPPER-U.
6. **[should-fix, cross-pair] Shared snapshot timestamp + no-mid-run-
   intervention rule** pre-registered; snapshot SHA per repo recorded at one
   timestamp for all six repos.
7. **[should-fix, cross-pair] Budget/token axis restored (doctrine).** Per-arm
   cost/token/wall-clock metadata mandatory secondary axes; snapshot
   timestamp is the hard commit-timestamp cutoff.
8. **[should-fix, cross-pair] No cross-pair aggregation.** Per-pair
   conclusions only; PAIR-OPUS named breadth-parallel; opt-in sentence
   pre-registered identical across all three U arms.
9. **[cross-pair] Uniform 1–5 quality axes with anchors** added (identical
   across the three pairs), alongside the existing blind aesthetic rating.
