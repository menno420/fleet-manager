# PAIR-FABLE — harness-comparison package (gba-play)

> Fleet harness experiment, owner-directed 2026-07-09.
> Model tier: **Fable 5** (held constant across both arms — the controlled
> variable is the harness, per the Codex-arm fairness doctrine in
> fleet-manager `docs/findings/gpt-5-6-report-2026-07-09.md`).
> Arm U: Claude Code web session with ultracode multi-agent orchestration →
> repo **harness-exp-fable-u**.
> Arm P: plain Claude Code Project session → repo **harness-exp-fable-p**.
> Budget: one overnight turn, fixed wall-clock, both arms launched tonight.
> Judging: tomorrow, from committed repo artifacts only, at **HEAD of the
> default branch** at the single shared snapshot timestamp recorded for all
> six experiment repos (commits after it do not count), against the
> pre-registered milestone ladder below (registered BEFORE launch).

---

## 1. TASK SPEC (identical core task text for both sessions)

> The text between the SPEC-START and SPEC-END markers is the canonical spec.
> It is inserted verbatim into both wrappers. It is written harness-neutrally:
> it never says "you/your subagents", "orchestrate", "delegate", "in this
> session", or "step by step" — only what must exist in the repo when the
> work ends.

<!-- SPEC-START -->
**Mission — gba-play: a Discord bot plugin prototype that lets a Discord
channel play a homebrew Game Boy Advance ROM, turn-based, through message
components.**

This repo starts empty. When the work ends, the repo must contain a working,
tested, documented prototype of the following system:

**What the system does**

1. An emulator core runs a **homebrew** GBA ROM headlessly via the mGBA
   Python bindings: load ROM → advance frames → read the current video frame
   → inject button input (A, B, Start, Select, L, R, D-pad) → advance again.
   No display, no audio, no real-time loop — the model is **turn-based**: one
   input (or "wait") per turn, run a fixed number of frames, then snapshot.
2. A frame-rendering layer turns raw emulator frames into share-ready PNG
   images using PIL: integer upscaling of the native 240×160 frame, plus a
   composited status strip (e.g., turn number, last input, ROM name).
3. A Discord plugin layer (discord.py or equivalent) exposes this as a bot
   extension: a command starts a play session in a channel; the bot posts the
   current frame as an image attachment with a **button-row controller**
   (message components for the GBA buttons); pressing a button plays that
   input as the next turn and the bot posts/edits the updated frame. Sessions
   have an owner or open-play mode, an inactivity timeout, and a stop command.
   The plugin must be fully exercisable **without any Discord token or live
   connection**: all Discord-facing logic is tested against fakes/mocks, and
   the core loop is additionally drivable by a local, non-Discord driver
   (CLI or script) that produces the same composited frames.

**Concrete deliverables (all committed to the repo)**

- D1. Python package with a clean separation: emulator core / frame
  compositor / session state machine / Discord plugin adapter.
- D2. A homebrew GBA ROM committed to the repo — either built from source in
  the repo (devkitARM or `binutils-arm-none-eabi`-class toolchain) or a
  vendored open-licence homebrew ROM — with a `ROM_PROVENANCE.md` stating
  exactly where it came from and its licence. The ROM must visibly react to
  input (a moving sprite/menu is enough; it does not need to be a fun game).
- D3. A local driver: one documented command that, without Discord and
  without a display, plays a scripted input sequence against the ROM and
  writes the resulting composited PNG frames to `artifacts/demo/`.
- D4. Committed evidence in `artifacts/`: at least the demo frame sequence
  from D3, produced by the committed code, showing the frame changing in
  response to input.
- D5. Tests (pytest): unit tests for the session state machine and
  compositor; integration tests covering emulator boot, frame capture, and
  input causing observable frame change; Discord-adapter tests against
  fakes. One documented command runs the whole suite.
- D6. `scripts/env-setup.sh`: installs everything the repo needs (apt +
  pip), always exits 0, never assumes cwd, guards every install step. The
  README's quickstart must work on a fresh machine after running it.
- D7. Documentation: `README.md` (what it is, quickstart, how to run tests,
  how to run the demo, how a real bot would mount the plugin) and a short
  `docs/architecture.md` (layers, turn-based model, known limits).

**Tech constraints**

- Python 3.11 (container default). Emulator: `mgba==0.10.2` (pinned) via
  pip; apt packages `mgba-sdl` and `binutils-arm-none-eabi` are known-good;
  devkitARM, if needed for the ROM build, is obtainable via the leseratte10
  mirror. Treat setup friction as solvable, not as a reason to stub the
  emulator. If the pinned `mgba==0.10.2` wheel is unavailable or fails to
  install in the environment, building the mGBA Python bindings from source
  still counts as a real emulator (not the fake fallback).
- Imaging: PIL/Pillow. Discord layer: discord.py (or an equivalent
  actively-maintained library), imported only by the adapter layer.
- If the real emulator genuinely cannot run in the environment, the fallback
  is a fake emulator behind the same interface **plus** a committed note in
  the README's "Status" section saying exactly that — a silently-stubbed
  emulator presented as working counts as failure.

**Hard rails**

- **Homebrew ROMs only.** No Nintendo-owned ROMs, BIOS files, assets,
  trademarks, or links to them — anywhere in the repo, including tests and
  docs. Licence and origin of any vendored ROM must be recorded (D2).
- **No external publishing and no spend.** No Discord token, no live bot
  connection, no deploys, no paid APIs, no publishing packages or pages.
  Free downloads of open-source tools/ROMs are fine.
- Everything of value must be **committed and pushed** to this repo. Work
  that exists only in a sandbox, a chat log, or an unpushed branch does not
  exist for judging purposes.
<!-- SPEC-END -->

---

## 2. MILESTONE LADDER M1–M6 (pre-registered; artifact-lookup only)

Each milestone is a conjunction of checks that a judge performs on the repo
at HEAD **without reading chat logs or asking the session anything**. A
milestone counts only if all its checks pass; "distance traveled" = highest
consecutive milestone reached (report partials as e.g. "M3 + 2/3 of M4").
Where a check says "runs green", the judge re-runs the documented command on
a fresh clone after `scripts/env-setup.sh` — committed evidence alone does
not substitute for a re-runnable command (METR shortcut caution), but
committed evidence IS required where listed, so both must exist and agree.

**M1 — Walking skeleton.**
- Repo has `README.md` naming the project and a quickstart section;
  a Python package directory that imports cleanly; `requirements.txt` or
  `pyproject.toml`; `scripts/env-setup.sh` present and exiting 0 on a fresh
  clone; at least one pytest test collected and passing via the documented
  test command.

**M2 — Emulator proof: headless boot + frame capture.**
- A homebrew ROM file is committed with `ROM_PROVENANCE.md` (origin +
  licence). A documented command loads the ROM through the mGBA bindings
  headlessly, advances ≥60 frames, and writes ≥1 PNG of the actual emulator
  output; at least one such PNG is committed under `artifacts/` and is not
  a uniform/blank image. An integration test covering boot+capture passes.
- **Real-vs-fake probe (mechanical):** (a) the demo driver's import path
  must reach the actual mgba binding — the judge greps that the core module
  imports `mgba` and that no monkeypatch/env-flag substitutes a fake in the
  demo path; (b) with `mgba` uninstalled in the judge venv (`pip uninstall
  mgba`), the documented demo command must FAIL loudly, not silently
  produce frames; (c) use of the fake-fallback clause requires the README
  "Status" note. Absence of the note plus a passing (b) = real M2; any
  other combination = M2-fake.
- **Fake-branch ladder (pre-registered):** if the fallback fake-emulator
  clause was honestly used, the arm is scored on a parallel ladder
  M2-fake … M6-fake — every check in M2–M6 identical except run against
  the fake core. Any Mn-fake result ranks strictly below any real-M2 (or
  higher) result, but distance WITHIN the fallback branch stays fully
  measurable (M5-fake beats M2-fake).

**M3 — Input changes the world.**
- The core exposes a turn API (input → advance N frames → frame out). An
  integration test proves input causes an observable frame difference
  (e.g., pixel/hash inequality between a no-input run and an input run at
  the same frame count) and passes. The button set covers at minimum
  D-pad + A + B + Start.

**M4 — Session state machine + compositor, unit-tested.**
- A session state machine exists as its own module (states at minimum:
  idle → active → ended; inactivity timeout; single-session-per-channel
  rule) with passing unit tests that do not require the emulator.
- The PIL compositor exists as its own module: upscaled 240×160 frame +
  status strip (turn number, last input); passing unit tests; ≥1 composited
  PNG committed under `artifacts/`.

**M5 — End-to-end offline demo + Discord adapter.**
- The D3 local driver runs green from a fresh clone and regenerates a
  multi-frame composited sequence matching the committed
  `artifacts/demo/` frames in count and shape.
- A Discord adapter module exists (command to start/stop, button-row
  controller wiring, posts/edits frame attachments) with passing tests
  against fakes/mocks and **zero** requirement for a token; no cross-layer
  leakage (emulator core does not import the Discord library).

**M6 — Polished, tested, documented.**
- Full test suite green via one documented command; lint (ruff or
  equivalent) configured and green; `docs/architecture.md` present and
  accurate to the code — "accurate" operationalized as exactly two
  mechanical checks, nothing more: (1) every module/path it names exists
  in the repo; (2) no layering claim it makes is contradicted by an import
  grep. README covers quickstart, demo, tests, and real-bot mounting
  instructions; error paths handled and tested (bad ROM path, input after
  session end, double session start).
- ROM legitimacy, operationalized: `ROM_PROVENANCE.md` contains a
  resolvable source URL + licence name; the judge confirms the URL is a
  homebrew source and the committed file matches it (size, or hash if the
  source publishes one). Plus a case-insensitive sweep of the full git
  history: zero hits for "nintendo", "bios", "gba_bios" outside
  provenance/docs context, and no tokens/secrets anywhere in history.

**Quality axes (judged separately from distance; scale and anchors uniform
across all three pairs; the same judge scores both arms of a pair side by
side — the OPUS protocol, generalized).** Each axis scored 1–5:
- **Code organization vs. D1** — 1 = single-file tangle; 3 = layers exist
  but leak across boundaries; 5 = clean D1 separation, dependencies point
  one way only.
- **Test honesty** — 1 = tautologies / asserts-true; 3 = real assertions
  but happy-path only; 5 = behavior-asserting including negative/error
  cases.
- **Evidence integrity** — 1 = committed artifacts do not regenerate; 3 =
  regenerate only with manual fixes; 5 = regenerate from the documented
  command, matching what is committed.
- **Doc accuracy** — 1 = docs contradict the code; 3 = mostly right with
  stale spots; 5 = every documented command/path works as written.

**Judge environment (pre-registered):** the judge runs in the same base
container image as the session sandboxes (python-lab-class), Python 3.11.
Network is allowed only while running `scripts/env-setup.sh` and
`pip install`, then disabled for all milestone checks. One snapshot SHA per
repo is recorded at the single shared timestamp for all six experiment
repos; judging target is HEAD of the default branch at that snapshot —
commits after it do not count.

**Cross-pair protocol (pre-registered; identical text in all three
packages):**
- One shared judging snapshot timestamp for all six repos; commits after it
  do not count.
- No mid-run intervention in either arm of any pair: no follow-up prompts,
  no nudges, no manual pushes.
- Budget framing (doctrine reconciliation): budget = each harness's native
  natural end of one overnight turn; endurance and parallel token spend are
  part of the treatment. To keep "better orchestration" distinguishable
  from "more tokens spent", per-arm **cost, token, and wall-clock
  metadata are recorded as mandatory secondary axes** in every pair, and
  the shared snapshot timestamp acts as the hard wall-clock cutoff.
- Each pair answers "which harness for THIS task shape" only. PAIR-FABLE's
  shape is **depth-serial** (one deep environment fight gates the ladder).
  Milestone scores are never summed or majority-voted across pairs; report
  per-pair conclusions only, task shape named alongside each.
- The ultracode opt-in sentence is identical in all three U arms:
  "Use ultracode: orchestrate this however you judge best."

---

## 3. WRAPPER-U — ultracode session prompt (repo: `harness-exp-fable-u`)

> Paste as the single opening prompt of the Claude Code web session attached
> to the empty repo `harness-exp-fable-u`.

```
Use ultracode: orchestrate this however you judge best.

You are working in the repo harness-exp-fable-u (currently empty; you have
push access). Budget: this single turn, running overnight — work until the
turn's natural end. Commit and push everything; the repo is the only judged
artifact — anything not pushed does not exist. Commit early and often so
progress is preserved even if the turn ends abruptly. Direct-to-main
commits or a PR you open AND merge yourself are both fine, but nothing may
be left unmerged/unpushed at the end.

[TASK SPEC — insert the SPEC-START…SPEC-END block verbatim]
```

## 4. WRAPPER-P — Project boot (repo: `harness-exp-fable-p`)

> Project Custom Instructions (set before launch), then the first message.

**Custom Instructions (verbatim):**

```
Repo conventions for harness-exp-fable-p:
- Commit early and often; push as you go, so progress is preserved even if
  the turn ends abruptly. Direct-to-main commits or a PR you open AND merge
  yourself before finishing are both allowed — nothing may be left
  unmerged/unpushed at the end.
- Everything is judged from the repo contents only (HEAD of the default
  branch) — anything not pushed does not exist.
```

**First message (verbatim):**

```
You are working in the repo harness-exp-fable-p (currently empty; you have
push access). Budget: this single turn, running overnight — work until the
turn's natural end. Commit and push everything; the repo is the only judged
artifact — anything not pushed does not exist. Commit early and often so
progress is preserved even if the turn ends abruptly.

[TASK SPEC — insert the SPEC-START…SPEC-END block verbatim]
```

**Equivalence note (pre-registered):** both wrappers carry the identical
spec block, the identical budget sentence ("this single turn, running
overnight — work until the turn's natural end"), the identical
repo-is-the-artifact rule, the identical abrupt-end/checkpointing sentence,
and the identical "merge any PR yourself; nothing unmerged/unpushed at the
end" rule (in WRAPPER-P the merge rule lives in Custom Instructions — the
Project surface's native place for conventions — so the union of Custom
Instructions + first message equals WRAPPER-U's content). The only delta is
WRAPPER-U's one-line ultracode opt-in, which uses the discretionary wording
pre-registered identically across all three pairs' U arms ("Use ultracode:
orchestrate this however you judge best") — it neither compels a fan-out
strategy nor imposes a plan-then-execute phase structure. Neither wrapper
mentions subagents beyond the opt-in line.

---

## Launch checklist (operator)

1. Create both repos empty (no README seed — M1 must be earned), private,
   under the experiment org/account. python-lab-class environment; the
   repo's own `scripts/env-setup.sh` is the sanctioned escape hatch for GBA
   deps (no secrets, no env vars needed — Block-4-class ban applies).
2. This file is the pre-registered rubric: commit it to the fleet-manager
   experiment folder BEFORE either session launches; do not edit after
   launch (append-only judge notes tomorrow).
3. **Toolchain parity smoke test (blocking — do not launch unverified):**
   before launch, in EACH harness's actual sandbox, verify that
   `pip install mgba==0.10.2`, `apt install mgba-sdl
   binutils-arm-none-eabi`, and the leseratte10 devkitARM mirror all work,
   and run a ten-minute load-a-ROM / advance-a-frame check. Record the
   parity result in this package. If either sandbox fails, fix the spec's
   known-good notes or swap the task — an environment asymmetry here would
   measure network policy, not orchestration; a shared failure floors both
   arms at M2-fake.
4. Launch both arms tonight, as close to simultaneously as practical, same
   model (Fable 5), native harness each. No mid-run intervention in either
   arm (no follow-up prompts, nudges, or manual pushes).
5. Record the single shared judging snapshot timestamp (all six experiment
   repos) up front; commits after it do not count.
6. Tomorrow: judge each repo at the recorded snapshot SHA of **HEAD of the
   default branch**, on a fresh clone in the pre-registered judge
   environment (§2), against §2; record highest milestone + 1–5 quality
   axes + the mandatory secondary axes (cost, tokens, wall-clock,
   commit-timeline metadata from git history).

---

## Fairness revisions

Applied 2026-07-09 (pre-launch), from the confirmed fairness critiques. Doctrine
(fleet-manager `docs/findings/gpt-5-6-report-2026-07-09.md`) wins on conflicts.

1. **[must-fix] Opt-in normalized.** WRAPPER-U's directive line ("plan and
   execute with your full multi-agent orchestration") replaced with the
   discretionary wording used by the other pairs: "Use ultracode: orchestrate
   this however you judge best." Pre-registered as identical across all three
   U arms (§2 cross-pair protocol + equivalence note).
2. **[must-fix] Unmerged-PR trap closed.** Both wrappers now carry the
   OPUS-style clause (direct-to-main, or a PR opened AND merged by the session;
   nothing unmerged/unpushed at the end); judging language changed to "HEAD of
   the default branch" throughout (header, Custom Instructions, checklist).
3. **[must-fix] Environment-capability parity.** Launch checklist now has a
   blocking pre-launch smoke test of pip pin + apt packages + mirror + a
   load-ROM/advance-frame check in EACH harness sandbox; the spec's unverified
   "proven feasible" claim was removed and the pin softened (source-built mGBA
   bindings count as a real emulator).
4. **[must-fix] M2-fake cap replaced with a fake-branch ladder.** M2-fake …
   M6-fake pre-registered (identical checks against the fake core), ranked
   strictly below any real-M2 result, so distance stays measurable in the
   fallback branch.
5. **[must-fix] Real-vs-fake made mechanical.** M2 now has the three-part
   probe: import-path grep, loud failure with mgba uninstalled in the judge
   venv, and the README Status-note rule (note-absent + loud-fail = real;
   anything else = M2-fake).
6. **[must-fix] M6 operationalized.** architecture.md "accurate" = exactly two
   mechanical checks (named paths exist; no layering claim contradicted by
   import grep). ROM legitimacy = resolvable URL + licence in
   ROM_PROVENANCE.md, size/hash match, case-insensitive history sweep for
   nintendo/bios/gba_bios outside provenance docs.
7. **[must-fix] Judge environment pre-registered** (§2): python-lab-class base
   image, Python 3.11, network only for env-setup/pip then disabled, snapshot
   SHA per repo at the shared timestamp.
8. **[should-fix] Budget/token axis restored (doctrine).** Cross-pair protocol
   pre-registers the reframing AND makes per-arm cost/token/wall-clock
   mandatory secondary axes, with the shared snapshot timestamp as the hard
   commit-timestamp cutoff.
9. **[should-fix] No cross-pair aggregation.** Pre-registered: per-pair
   conclusions only ("which harness for THIS task shape"); FABLE named
   depth-serial; no summing/majority-voting across pairs.
10. **[should-fix] Abrupt-end checkpointing sentence** added identically to
    both arms (U wrapper; P Custom Instructions + first message).
11. **[should-fix] Quality axes anchored.** Uniform 1–5 scale with one-line
    anchors per axis, identical across all three pairs; same judge scores both
    arms side by side.
12. **[should-fix] Shared snapshot timestamp + no-mid-run-intervention rule**
    added to the launch checklist and §2.
