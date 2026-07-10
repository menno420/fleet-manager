# codetool-lab-sonnet5 — package meta

> **Status: ARCHIVE.** Project CLOSED (fleet-manager `control/status.md` @ `0eaa668`:
> "codetool ×3 — Projects CLOSED; repos retained"; disposition in
> `docs/planning/gen2-launch-record-2026-07-10.md` @ `0eaa668`). Repo retained and
> **NOT platform-archived** — `"archived": false` API-verified 2026-07-10 ~15:12Z;
> archive toggle parked as a paired DECISION (fleet-manager `docs/owner-queue.md` @
> `0eaa668` § Parked: "wait, then archive" — archiving breaks the succession pack's
> write rituals AND would block the pending v0.1.1 tag push below). Repo HEAD at build
> time: `66c3dfc79735` ("wind-down complete — ready for archive + fresh session", PR #16).

No live package artifacts (nothing deployed; no Project). This meta indexes the
successor-seed material and the repo's terminal state.

## Succession material (would seed any gen-3 successor)

All at `66c3dfc`, **entirely under `docs/succession/`** — including the setup script
(⚠ non-standard location: this repo has **no `environments/` dir**; a gen-3 reviver
must know to look here):

- `docs/succession/README.md` — the pack index + queue state at wind-down
  (DONE / IN-FLIGHT / NEXT).
- `docs/succession/NEXT-BOOT.md` — future-seat boot prompt (read order, walking-skeleton
  check with READY-never-draft callout, §3 known walls). Gen-2 discrete-session model.
- `docs/succession/PROPOSED-CUSTOM-INSTRUCTIONS.md` — table-form KEEP/DROP/ADD with a
  per-row gen2-blueprint alignment column (the most blueprint-integrated of the three
  codetool proposals). Proposal only — the deployed gen-1 CI text was never committed.
- `docs/succession/ENVIRONMENT.md` + `docs/succession/GEN2-FEEDBACK.md`.
- Setup script: **`docs/succession/setup-universal.sh`** — fleet-canonical defensive
  template adapted (pyproject editable + `[dev]` extra; always exits 0).
- Whole-life retro: `docs/retro/winddown-review-2026-07-09.md` (full PR ledger, every
  failure with exact error text; headline lesson: a differential oracle vs python-dotenv
  found 3 real parser bugs behind 114 green tests).

## Release state — cfgdiff v0.1.1 PENDING (2 owner clicks)

Product: **cfgdiff 0.1.1 on main, unreleased** (bugfix PR #11, tag target `0b1eb60`;
165 tests + 4 deliberate xfails; installable via
`pipx install git+https://github.com/menno420/codetool-lab-sonnet5`). Zero remote tags
(verified `ls-remote --tags` at build time); `release.yml` has **never fired**. The two
owner clicks (`control/status.md` ⚑1–2 @ `66c3dfc`; mirrored in fleet-manager
`docs/owner-queue.md` @ `0eaa668` § Parked):

1. Register the PyPI trusted publisher — pypi.org → Publishing → pending publisher:
   owner `menno420`, repo `codetool-lab-sonnet5`, workflow `release.yml`, environment
   `pypi` (steps: `docs/retro/project-review-2026-07-09.md` §(e)3).
2. `git tag -a v0.1.1 0b1eb60 -m "cfgdiff 0.1.1" && git push origin v0.1.1` — runs the
   test gate, builds sdist+wheel, cuts the GitHub Release with the CHANGELOG body, and
   (if click 1 done first) publishes to PyPI. Do **NOT** tag v0.1.0 at `0260aae` — it
   predates release.yml and fires nothing.

WHY owner-only: tag push is a **credential-layer 403** on agent seats (not a
classifier denial — this half of the wall is NOT seat-dependent; see below).

## The seat-dependent release-wall lesson (recorded at fable5 `a6cf1a9`)

fable5 `docs/succession/PLATFORM-LIMITS.md` item 4 correction: **classifier-denial**
walls (Actions `workflow_dispatch` release route) are SEAT-DEPENDENT — opus4.8's seat
published two live Releases via the route fable5's seat was denied; a successor probes
once per seat. **Credential-layer 403s** (direct tag push, Releases API, ref-create) held
on every seat tested — which is why this repo's release automation was built
tag-triggered-by-owner instead. Any successor package inherits probe-once-per-seat for
classifier walls and treats the credential 403s as real until the credential layer
changes.

## Branches — one stale

- `test/push-check` — empty probe branch, leftover; agent branch-delete 403s, owner
  click queued (`control/status.md` ⚑3 @ `66c3dfc`; fleet-manager `docs/owner-queue.md`
  @ `0eaa668` § housekeeping, ~10s).

## Gen-3 note

**Any successor seat starts from the gen-3 born-continuous standard, not these gen-2
texts**: superbot `docs/planning/gen3-deployment-standard-2026-07-10.md` @ `dc19b1e8`
(Q-0265-amended) + `round3-dispatch-part4-brief-2026-07-10.md` §2b. The succession pack
here is pre-Q-0265 raw material (discrete-wake NEXT-BOOT, gen-2 CI proposal); re-base
per the Q-0262.6 hold before any deployment. If the owner archives the repo first
(paired decision), the tag-push release click must happen **before** the archive toggle.
