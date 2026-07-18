# Session — fm-no-false-walls-guard

> **Status:** `complete`

**Branch:** `claude/fm-no-false-walls-guard-0718`

📊 Model: Opus 4.8 · medium · feature build

**About to do:** Build `tools/check_no_false_walls.py` — an advisory stdlib doc
linter that bans present-tense standing agent-capability-denial claims (#309's
new doctrine) in the repo's living/binding docs, and fix the CONSTITUTION
branch-delete "genuine wall (403)" line it should catch. This card held the PR
red (HOLD) until the checker landed, was run against the real docs + `--selftest`,
the sibling checkers + strict gate stayed green, and the enders were filled —
then flips `complete` last.

**Did:**
- **Built `tools/check_no_false_walls.py`** (stdlib-only, sibling-parity with the
  S3/S5/S9 advisory checkers `check_fleet_triage_staleness` /
  `check_docs_links` / `check_capabilities_wall_age`): kit provenance +
  reliability + kill-switch header, `--selftest` (inline fixtures), `--list`
  (scan set), `--root PATH` (fixture-tree testability), `--strict` (exit 1 on
  findings; default advisory exit 0). It enforces #309's ban on **present-tense
  standing agent-capability-denial claims** in the repo's living/binding prose —
  statements that an agent *cannot* merge / flip / delete a branch, framed as a
  permanent limit — while leaving the DATED/QUOTED incident row (the legitimate,
  S9-aged home for a transient wall observation) untouched.
- **Detection = seed-term + core-capability context + present-tense shape − exemptions.**
  A line flags only when it carries a WALL signal (`wall`/`walled`, `blocked`,
  `owner-only`, `classifier-denied`, `agents cannot/can't`, `must not merge/flip`,
  `not allowed to`, or a present-tense `is|stays|verified … 403/409` framing)
  **AND** names a core capability #309 declares NORMAL (merge / draft→ready flip
  / branch·ref deletion / auto-merge arm). This context gate is the false-positive
  firebreak: it lets **genuine** constraints — `tag-push is 403-walled`,
  `api.github.com` 403, secrets/rulesets owner-only, protected-main 409 — pass
  untouched (they are not in the core-normal set).
- **Exemptions (any → clean):** a **block** carrying a `YYYY-MM-DD` / `LAST-VERIFIED`
  date (dated incident); a **quoted** verbatim refusal (`"…"`, `verbatim`,
  `Reason:`); a **negated / anti-wall** line (`not a wall`, `never a … wall`,
  `≠ … wall`, `no longer`, negation within the ~48-char lead before the signal);
  a **meta / discovery-discipline** line (`declare`, `cite`, `mint`, `document(s)`,
  `record`, `re-verify`, `false wall`, `doc-wall`, `check_no_false_walls`); and
  **non-capability** nouns (`blocked branch`, `firewall`, `paywall`, `stonewall`,
  `hub`). **Self-exclusion (meta-risk):** the guard's own file + its inline
  fixtures carry every seed term and are excluded structurally (fixed allowlist)
  and by explicit basename skip.
- **Allowlist (narrow, living/binding only):** `CONSTITUTION.md`,
  `docs/current-state.md`, `docs/owner-queue.md`, `.claude/CLAUDE.md`, and the
  **active region** of `docs/CAPABILITIES.md` (top of file down to `## Append log`).
  It does NOT scan `.sessions/**`, `CAPABILITIES-verified-*.md` snapshots, the
  CAPABILITIES dated append-log/mirrored/folded region, `bootstrap.py`,
  `.substrate/**`, or fixtures — the false-positive-flood surfaces the task warned
  against.
- **Ran against the real repo — flagged exactly 3 genuine false walls, then CLEAN
  after the fixes.** Before: `CONSTITUTION.md:85` ("Ref/branch deletion stays a
  genuine wall (403)…"), `docs/owner-queue.md:426` and `:431`
  ("agent branch-delete is a verified 403"). **Fixed all three to #309's verified
  reality:** branch deletion is normal agent work — 204 via the direct-token path,
  only the proxied path 403s, so agents delete branches directly. After:
  `check_no_false_walls` CLEAN (advisory EXIT=0 **and** `--strict` EXIT=0).
- **Two false-positive classes caught + fixed during the build** (the reason the
  guard is trustworthy, not just green): (1) the date regex `\b\d{4}-\d{2}-\d{2}\b`
  missed timestamp dates like `2026-07-17T09:…` (digit→`T` is not a word boundary),
  so a dated incident row (`owner-queue.md:251`) leaked as a finding → dropped the
  trailing `\b`; (2) the negation contraction `n'?t\b` matched the bare `nt` inside
  `age**nt**`, falsely exempting the two genuine `owner-queue` branch-delete walls
  → required the apostrophe (`n't`). Also added a **prev-line context window** for
  the meta/quote/anti-wall exemptions so a qualifier that markdown hard-wrapped onto
  the previous line (`…a PR that documents an\n agent-capability wall…` in
  `.claude/CLAUDE.md`) is seen, while the negation lead stays bounded to 48 chars so
  an earlier `never` in the same bullet cannot over-exempt a real standing wall.
- **`--selftest` PASS (EXIT=0), 6 invariants:** a present-tense standing wall line →
  flagged; a dated+quoted historical incident line → not; a non-capability
  `blocked branch` line → not; a negated / anti-wall line → not; a genuine non-core
  constraint (`tag-push 403`) → not; a meta line describing the guard → not; plus a
  `LAST-VERIFIED` dated-BLOCK exemption case.
- **Severity + wiring:** sibling-parity — default advisory (exit 0), `--strict`
  reds on findings. Ships **standalone, NOT wired into `bootstrap.py check`**, so it
  can never jam the substrate-gate — advisory-first per the task; PR body documents
  the semantics for owner ratification and promotion to a required check once proven
  clean.
- **Checks green:** `check_no_false_walls` CLEAN EXIT=0 (advisory + strict);
  `--selftest` PASS EXIT=0; `check_owner_queue.py` EXIT=0; `check_docs_links.py`
  CLEAN (256 files); `bootstrap.py check --strict` EXIT=0 after this flip — the
  only red was this card's born-red HOLD (guard-fire delta committed, not reverted).
  The pre-existing `seat-digest-stale` advisory is explicitly "never exit-affecting"
  and out of this session's scope.

⚑ Self-initiated: None — directed deliverable (the coordinator's task: build the
`tools/check_no_false_walls.py` guard #309 named as required but was never created,
fix the flagged living-doc lines, land born-red). No autonomous idea promotion; no
trigger created, modified, fired, or deleted.

💡 Session idea: **Fleet-wide false-wall sweep** — extend `check_no_false_walls` with
a `--fleet` mode that reads each sibling repo's living docs (`CONSTITUTION.md` /
`.claude/CLAUDE.md` / the active `CAPABILITIES.md` region) over
`raw.githubusercontent.com` (standing read-auth, no `add_repo`) and reports false-wall
lines per repo. The drift this session found — #315 corrected the doctrine in
`owner-steps-2026-07-18.md` but left contradicting `agent branch-delete is a verified
403` claims in `owner-queue.md` **and** `CONSTITUTION.md` — almost certainly exists in
the other ~19 repos, which all carry the same doctrine language propagated by the kit.
A read-only hub sweep would surface the whole fleet's stale walls in one pass and feed
the per-repo fix as routed items, turning a single-repo guard into a fleet-hygiene
instrument. (Dedup-checked `docs/ideas/` — no existing false-wall / fleet-sweep /
promote-to-required idea; distinct from the S9 wall-age and S3 triage-staleness
flaggers, which age *dated* findings rather than catching *undated standing prose*.)

⟲ Previous-session review: **PR #315 (fm-owner-steps-revise — revised
`owner-steps-2026-07-18.md` to the corrected #308/#309/#311 doctrine)** did the core
thing right and boldly: it recognised yesterday's list over-routed agent-doable work
(merges, flips, settings, releases, branch-deletes) to the owner and restructured into
✅ Done / → hub-chat / 👤 genuine-owner-only, landing the doctrine correction cleanly
(merged server-side by `github-actions[bot]`). What it **missed**, and this session had
to clean up: the same false-wall claim it corrected in `owner-steps.md` was left
standing in **two other living docs** — `owner-queue.md:426/:431` and `CONSTITUTION.md:85`
still asserted branch deletion is a 403 wall. That is exactly the *doc-to-doc drift*
class (a doctrine fix applied in one file but not its siblings) — a good session-level
lesson: a doctrine correction should sweep **every** living doc that repeats the claim,
not just the doc in front of you. **System improvement it surfaces (and this session
shipped):** that drift is now *mechanically caught* — `check_no_false_walls` would have
reddened (advisory) on #315's un-swept siblings the same session. The natural next step
is the fleet-wide `--fleet` extension (the session idea above), so the "fix it in one
doc, forget the other twelve" failure is caught across the whole fleet, not just this
repo. No filler: this is a real, concrete gap the guard closes.
