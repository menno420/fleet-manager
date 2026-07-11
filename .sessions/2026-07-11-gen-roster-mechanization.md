# 2026-07-11 — gen_roster.py mechanization (work-ladder item 8)

> **Status:** `complete`

📊 Model: Claude (Fable family, fable-5) · start 2026-07-11T~05:2xZ · lane
worker dispatched by successor coordinator cse_012o8pySy5K3AV6JWoPKryZL

## Declared at open (born-red)

Scope: mechanize the R25 roster regeneration as **`scripts/gen_roster.py`**
(the owed follow-up from ORDER 009 / roster gens #1–#4, handoff §7 ladder
item 8): ingest a `list_triggers` JSON export (`--triggers triggers.json`,
documented schema, loud fail on mismatch), fetch each lane repo's
`control/status*.md` heartbeat over git transport with the MANDATORY
ls-remote verify loop (stale-clone-pack doctrine), regenerate `docs/roster.md`
in the established gen-N format + a `--check` drift mode. Stdlib + git
subprocess only. Verify against the real gen #4 before landing; the
deliverable is the TOOL — a machine gen #5 ships only if the diff is clean
and meaningful. Heartbeat `control/status.md` as the batch's last step; flip
this card `complete` as the final commit; REST squash-merge on green (R21).

## Shipped (close-out)

- **`scripts/gen_roster.py`** (stdlib + git subprocess; Q-0105 provenance +
  unverified + kill-switch header). Three modes: generate (attribution/date
  from CLI args, generation auto-bump from the committed roster), `--check`
  (unified diff vs `docs/roster.md`, exit 2 on drift), `--selfcheck` (offline
  logic assertions — the repo gate has no pytest harness, documented in the
  header). Expected `list_triggers` export shape documented in the docstring
  from a real 2026-07-11 record; schema mismatch = nonzero exit naming the
  failing record. Every repo read loops fetch → `FETCH_HEAD == ls-remote` →
  re-fetch (gen-#3 stale-proxy-pack doctrine); unreadable repos degrade to
  `NOT MEASURED (wall: <reason>)`. Verdict ladder codified: FRESH ≤2× wake
  cadence (parsed from the matched cron) · STALE ≤24h · DARK >24h · DEAD =
  not measurable · STALE-BY-DESIGN for archived lanes.
- **Verified against ground truth before landing:** fresh 263-record /
  31-enabled live trigger export (3 pages, ~02:40Z) + a real full
  regeneration (18 repo fetches, all converged first attempt, pokemon
  private repo read fine). All 15 standing trigger id·cron pairs agree
  EXACTLY with hand gen #4 (set-diff empty both ways). `--check` vs gen #4:
  exit 2, 150 diff lines — all classified (format-class: machine format is a
  documented subset of the hand prose; world drift: 10 HEADs moved since
  01:58Z). **Three first-run bugs found and fixed with regression
  selfchecks:** git `%cI` tz-offset truncation (future-dated ages);
  named-trigger prompt-body mis-attribution (sim-lab failsafe → idea-engine);
  bullet-form heartbeat headers parsed empty (venture-lab/pokemon style).
- **NO gen #5 committed** — the dispatch bar (clean and meaningful diff) is
  not met by format; `docs/roster.md` stays at hand gen #4. Next R25 pass
  runs the script and may append coordinator prose before committing.
- `.gitignore` += `tmp-triggers.json` (the documented export filename can
  never be committed by accident). Raw export NOT committed, per dispatch.
- Heartbeat slice record in `control/status.md` with the six ⚑ self-decided
  design decisions (path `scripts/` vs proposal's `tools/` — dispatch won;
  in-script LANES registry; verdict thresholds; `--check` reproducibility
  via `--date`; deltas stay human; gitignore guard).

## 💡 Session idea

`gen_roster.py`'s LANES registry is now the second place a seat birth must be
recorded by hand (after the trigger itself). The registry already knows every
seat: standing-cron trigger names are near-canonical lane names. Idea: a
`--audit-lanes` mode that diffs enabled standing crons against the LANES
tokens and exits nonzero when a trigger matches NO lane (a born seat the
script doesn't know) or a live lane matches NO trigger — turning the one
hand-maintained input into a self-checking one. ~20 lines, closes the exact
drift class that killed the hand manifest.

## ⟲ Previous-session review

The review-queue-verify session (PR #61) set a high evidence bar — two
independent CI-log anchors for the pokemon sha1 chain, and its
closed-by-design verdict quoted the workflow's own in-file comment rather
than inferring intent. One gap it left: its heartbeat verdicts live only in
prose — neither row's verify method (chain-link sha1 equality) was banked as
a reusable check, so the next verifier re-derives the procedure from prose.
Improvement this session applies in kind: verification logic that a session
invents (here: the ls-remote loop, the schema gate, the verdict ladder) got
encoded as executable, regression-tested code rather than session prose —
which is the whole point of the mechanization ladder item.
