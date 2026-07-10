# PAIR-SONNET — devlog generator (Sonnet 5)

> Harness-comparison experiment package, drafted 2026-07-09.
> Two sessions, same model (Sonnet 5), same task, same budget:
> **Arm U** = Claude Code web session with ultracode multi-agent orchestration → repo `harness-exp-sonnet-u`
> **Arm P** = plain Claude Code Project session → repo `harness-exp-sonnet-p`
> Each repo starts fresh and empty. Judged tomorrow from committed artifacts only,
> against the pre-registered milestone ladder below (registered BEFORE launch, per
> fleet fairness doctrine: native harness each, fixed wall-clock = one overnight
> turn, artifact-based judging only).

---

## 1. TASK SPEC (identical core text for both arms — harness-neutral)

```
MISSION — devlog generator

Build "devlog": a tool that turns a git repository's commit history into
publishable weekly devlog posts — the story of what shipped, what changed,
and what it means — in both Markdown and HTML, with quality heuristics
and an automated test suite.

CONCRETE DELIVERABLES
1. A Python package `devlog/` with a CLI entry point, invocable as:
       python -m devlog generate --repo <path> [--since <date>] [--weeks N] --out <dir>
   It must read real git history (commits: hash, author, date, message,
   changed files, insertions/deletions) from any local repository path and
   group it into ISO-week buckets.
2. Post generation: for each week with activity, emit one post as BOTH
   `out/<year>-W<week>.md` and `out/<year>-W<week>.html`. A post contains,
   at minimum: a title, a date range, a narrative summary section, a
   "shipped" section (grouped notable changes), stats (commit count, files
   touched, +/- lines), and a footer identifying the generator. HTML output
   must be self-contained (inline CSS, no external assets) and render the
   same content as the Markdown.
3. An index page `out/index.md` and `out/index.html` linking all generated
   posts, newest first.
4. Quality heuristics module `devlog/quality.py`: score each generated post
   0–100 with named checks — at minimum: substance (not just a raw commit
   dump; narrative sentences present), specificity (references real files/
   components from the history), completeness (all required sections
   present), length bounds, and dedup (no near-duplicate bullets). The CLI
   must support `python -m devlog check --posts <dir>` printing per-post
   scores and failing (nonzero exit) below a documented threshold. Scores
   must also be embedded in each post's front-matter/metadata.
5. Tests under `tests/`, runnable with `python -m pytest -q`, that build at
   least one synthetic fixture git repository at test time (create a temp
   repo, make scripted commits) and assert on: week bucketing, post
   structure, HTML/Markdown content parity, heuristic scoring behavior
   (including a deliberately bad post scoring low), and CLI exit codes.
6. Real-output proof: run the tool on THIS repository's own git history at
   the end of the session and commit the generated posts under
   `examples/self/` so the judged repo contains real output.
7. Documentation: `README.md` (what it is, install/run, CLI reference,
   example output snippet, how scoring works, known limitations) and a
   short `DESIGN.md` (architecture, key decisions, what you would do next).

TECH CONSTRAINTS
- Python 3.11, standard library strongly preferred. Allowed third-party
  deps: pytest (tests only) and, if genuinely needed, up to two small pure-
  Python libraries, pinned in requirements.txt with a one-line justification
  each in DESIGN.md. No heavyweight frameworks.
- Read git history via `git` subprocess calls or pure-Python parsing — no
  GitPython-style heavy deps required.
- Narrative text must be produced deterministically by the tool itself
  (templating/summarization logic over commit data). The tool must NOT call
  any LLM or network API at runtime; generation runs fully offline.
- No secrets, no tokens, no env-var configuration containing credentials.

HARD RAILS
- No external publishing: do not post output anywhere (no GitHub Pages
  enablement, no gists, no social/blog platforms, no external services).
  Generated posts live only as committed files in this repository.
- No spend: no paid APIs, no new services, no network calls at runtime.
- Work only inside this repository.

WORKING RULES
- Commit early and often with meaningful messages; push everything before
  finishing. The repository is the only judged artifact — anything not
  committed and pushed does not exist.
- Budget: one work session (a single overnight turn). Work until the turn's
  natural end; leave the repo in a clean, honest state (tests green or
  failures documented in README "Known limitations").
```

---

## 2. MILESTONE LADDER M1–M6 (pre-registered; judged from repo artifacts only)

Each milestone is a boolean lookup against **HEAD of the default branch** at
the pre-registered snapshot time — one shared timestamp for all six
experiment repos, recorded up front; commits after it do not count, and an
unmerged branch does not count. A milestone counts only if all its checks
pass; "distance traveled" = highest consecutive milestone reached (plus note
any skipped-then-satisfied ones).

**Judge environment (pre-registered):** the same base container image the
sessions run in (python-lab-class), clean python3.11 venv, fresh clone at
the recorded snapshot SHA; network allowed only for `pip install -r
requirements.txt` (if present), then disabled for all checks.

- **M1 — Walking skeleton.**
  `devlog/` package exists with `__main__.py`; `python -m devlog generate
  --repo . --out /tmp/x` exits 0 on a clone of the repo itself and writes at
  least one `.md` file containing a title and at least one commit-derived
  fact (hash prefix, filename, or message fragment verifiable against
  `git log`). README.md exists with a run command that works as written.

- **M2 — Correct week bucketing + full Markdown post structure.**
  Posts are named `<year>-W<week>.md`; spot-check: every commit date in
  `git log` of the input repo falls in the ISO week of exactly one emitted
  post claiming it (verifiable by recomputing ISO weeks). Each post contains
  all required sections (title, date range, narrative summary, shipped,
  stats, footer). Stats in at least one post match `git log --numstat`
  recomputation within exact equality — **under the tool's documented
  counting convention**: README or DESIGN.md must state how merge commits
  are handled (counted or skipped), how binary files (`numstat` "-"
  entries) are counted, how renames are handled, and which date field
  (author vs committer) buckets a commit into a week. The judge recomputes
  UNDER THE DOCUMENTED CONVENTION; an undocumented convention fails M2.

- **M3 — HTML output + index, content parity.**
  For every `.md` post an `.html` twin exists, self-contained (no external
  `http(s)://` asset references in the HTML), containing the same title,
  sections, and stats values. `index.md` + `index.html` exist and link every
  post, newest first.

- **M4 — Quality heuristics wired end-to-end.**
  `devlog/quality.py` exists implementing the five named checks;
  `python -m devlog check --posts <dir>` exits 0 on the repo's own generated
  posts and prints per-post numeric scores; each post file embeds its score
  in metadata; the failure threshold is documented. **Per-heuristic probes
  (pre-registered — one corruption per check, each of which must move the
  printed score or flip the exit code):** (1) dedup — duplicate a
  shipped-section bullet 3x; (2) specificity — strip all file/component
  names from the narrative; (3) length — truncate the post to 3 lines;
  (4) substance — delete the narrative section of the NEWEST post in
  `examples/self/` (the previous probe, now pinned to a specific file);
  (5) completeness — remove the stats section. Acceptance alternative
  (named now): in-repo tests demonstrating each check discriminates (a
  passing and a failing input per check) satisfy the same requirement.

- **M5 — Test suite with synthetic fixture repo, green.**
  `python -m pytest -q` exits 0 in a fresh clone (after
  `pip install -r requirements.txt` if present); tests construct at least
  one temp git repo with scripted commits (visible in test source — not
  checked-in fixtures only); tests cover bucketing, post structure, MD/HTML
  parity, a low-scoring bad post, and CLI exit codes. Zero skipped tests,
  or skips only for reasons on the pre-registered whitelist ("git
  executable unavailable"); any other skip fails M5.

- **M6 — Polished, self-applied, documented.**
  All of M1–M5, plus: `examples/self/` contains committed real output
  generated from the repo's own history (posts + index, scores embedded, and
  the content demonstrably corresponds to the repo's actual commits);
  README is complete (install/run, CLI reference, example snippet, scoring
  explanation, known limitations); DESIGN.md exists with architecture +
  decisions + next steps. Tree hygiene (mechanical): zero files matching
  the pre-registered scratch pattern list (`*.tmp`, `scratch*`, `*.bak`,
  `notes.txt` at repo root); every module under `devlog/` reachable from
  the CLI entry point or imported by tests (grep/import sweep);
  `grep -rE 'TODO|FIXME' devlog/` hit count == 0. History hygiene
  (mechanical): >= 8 commits; no single commit introducing > 50% of final
  product LOC; no commit message matching `^(wip|fix|update)$`.

**M6 tie-breaker (pre-registered — ceiling risk):** devlog is small enough
that both arms may reach M6, so an M6/M6 result is decided by: (a) a blind
side-by-side quality comparison of the two arms' `examples/self/` posts
(narrative quality, specificity, honesty of embedded scores), same judge,
both arms together; (b) depth checks — do the M4 per-heuristic corruptions
all discriminate (not just the substance probe), and do the heuristics
resist false positives on a judge-supplied pathological history (e.g. a
fixture repo of 100 identical one-line commits)?

Judge also records (secondary, not milestone-gating): commit count and
timestamps (distance/pace), lines of test code vs product code, **per-arm
cost, token, and wall-clock metadata (mandatory — doctrine's budget axis;
distinguishes "better orchestration" from "more tokens spent")**, and any
rail violations (network at runtime, publishing) — a rail violation caps
the arm's result at the last milestone achieved without it.

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
  regenerate only with manual fixes; 5 = regenerate from the documented
  command, matching what is committed.
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
- Each pair answers "which harness for THIS task shape" only. PAIR-SONNET's
  shape is **small/mixed** (modest breadth, no environment fight).
  Milestone scores are never summed or majority-voted across pairs; report
  per-pair conclusions only, task shape named alongside each.
- The ultracode opt-in sentence is identical in all three U arms:
  "Use ultracode: orchestrate this however you judge best."

---

## 3. WRAPPER-U — ultracode session prompt (repo: `harness-exp-sonnet-u`)

```
Use ultracode: orchestrate this however you judge best.

You are working in the fresh empty repository `harness-exp-sonnet-u` (this
repo). Commit and push everything; the repo is the only judged artifact —
anything not committed and pushed does not exist. Commit early and often so
progress is preserved even if the turn ends abruptly. Direct-to-main
commits or a PR you open AND merge yourself are both fine, but nothing may
be left unmerged/unpushed at the end. You have one work session (a single
overnight turn); work until the turn's natural end.

<TASK SPEC — insert Section 1 verbatim>
```

---

## 4. WRAPPER-P — Project boot (repo: `harness-exp-sonnet-p`)

**Custom Instructions (Project settings):**

```
Repo conventions for harness-exp-sonnet-p:
- Commit early and often with meaningful messages; push everything before
  finishing, so progress is preserved even if the turn ends abruptly.
- Open READY (non-draft) PRs or commit directly to main — both are fine;
  if you open a PR, merge it yourself before finishing. Leave nothing
  unmerged or unpushed at the end.
- Everything is judged from the repository contents only (HEAD of the
  default branch); anything not committed and pushed does not exist.
```

**First message (verbatim):**

```
You are working in the fresh empty repository `harness-exp-sonnet-p` (this
repo). Commit and push everything; the repo is the only judged artifact —
anything not committed and pushed does not exist. Commit early and often so
progress is preserved even if the turn ends abruptly. You have one work
session (a single overnight turn); work until the turn's natural end.

<TASK SPEC — insert Section 1 verbatim>
```

**Information-equivalence note:** both wrappers carry the identical task spec,
identical budget sentence, identical "repo is the only judged artifact" rule,
identical abrupt-end/checkpointing sentence, identical "merge any PR yourself;
leave nothing unmerged/unpushed" rule, and identical repo-name framing (in Arm
P the PR/merge rule lives in Custom Instructions — Project-surface plumbing —
so the union of Custom Instructions + first message equals the U wrapper's
content). The only asymmetry is Arm U's single ultracode opt-in line, using
the discretionary wording pre-registered identically across all three pairs'
U arms. The task spec itself never mentions subagents,
orchestration, planning phases, or "work step by step" — it states deliverables
and rails only, so neither harness's working style is presumed.

---

## Launch checklist (operator)

1. Create empty repos `harness-exp-sonnet-u` and `harness-exp-sonnet-p`
   (private, default branch main, no template files — truly empty except the
   Project arm's Custom Instructions which live in Project settings, not the
   repo).
2. Register this file (ladder included) BEFORE either session starts.
3. Launch both tonight on Sonnet 5, one turn each, no mid-run intervention
   in either arm (no follow-up prompts, nudges, or manual pushes).
4. Judge tomorrow strictly per Section 2, from HEAD of the default branch at
   the single shared snapshot timestamp recorded up front for all six
   experiment repos (record one snapshot SHA per repo; commits after the
   timestamp do not count), in the pre-registered judge environment; record
   the mandatory secondary axes (cost, tokens, wall-clock) per arm.

---

## Fairness revisions

Applied 2026-07-09 (pre-launch), from the confirmed fairness critiques. Doctrine
(fleet-manager `docs/findings/gpt-5-6-report-2026-07-09.md`) wins on conflicts.

1. **[must-fix] Unmerged-PR trap closed.** P-arm Custom Instructions now
   require "merge it yourself before finishing; leave nothing unmerged or
   unpushed", the U wrapper mirrors the same sentence for symmetry, and
   judging is defined as HEAD of the default branch at the pre-registered
   snapshot time (unmerged branches do not count) — the OPUS clause,
   generalized.
2. **[must-fix] M6 subjective terms replaced with mechanical checks.** "Clean
   tree / stray files / dead stubs / meaningful history" replaced by: zero
   files matching a pre-registered scratch pattern list (*.tmp, scratch*,
   *.bak, notes.txt at root); every devlog/ module reachable from the CLI or
   imported by tests; grep TODO|FIXME count == 0 in devlog/; >= 8 commits; no
   single commit introducing > 50% of final product LOC; no commit message
   matching ^(wip|fix|update)$.
3. **[should-fix] M6 ceiling tie-breaker pre-registered.** Blind side-by-side
   comparison of the two arms' examples/self/ posts (narrative quality,
   specificity, honesty of scores) plus depth checks (all M4 corruptions
   discriminate; false-positive resistance on a judge-supplied pathological
   history).
4. **[should-fix] M2 counting convention pinned.** The tool must document its
   convention (merges, binaries, renames, author-vs-committer date); the
   judge recomputes under the documented convention; undocumented convention
   fails M2.
5. **[should-fix] M4 per-heuristic probes pre-registered.** One corruption per
   check (dedup/specificity/length/substance/completeness), each must move
   the score or flip the exit code; substance probe pinned to the newest
   examples/self post; in-repo discriminating tests named as the acceptance
   alternative.
6. **[should-fix] M5 skip rule tightened.** Zero skips, or whitelist-only
   ("git executable unavailable"); any other skip fails M5.
7. **[should-fix, cross-pair] Abrupt-end checkpointing sentence** added
   identically to both arms' wrappers.
8. **[cross-pair] Judge environment pre-registered** (python-lab-class base,
   python3.11 venv, network off after pip install, snapshot SHA per repo);
   shared snapshot timestamp + no-mid-run-intervention rule made explicit.
9. **[cross-pair] Budget/token axis restored (doctrine).** Per-arm
   cost/token/wall-clock metadata mandatory secondary axes; snapshot
   timestamp is the hard commit-timestamp cutoff.
10. **[cross-pair] No cross-pair aggregation.** Per-pair conclusions only;
    PAIR-SONNET named small/mixed; uniform 1-5 quality axes with anchors
    added; U-arm opt-in normalized to the exact shared sentence "Use
    ultracode: orchestrate this however you judge best."

Also fixed in passing: a stray trailing code fence at end of file.
