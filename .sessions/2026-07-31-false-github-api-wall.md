# 2026-07-31 · Correct the false `api.github.com` wall — and the false guardrail behind it

> **Status:** `complete`

About to happen (declared born-red): a records-only correction carried over
from an owner-live spider-swing session. That session found the seeded wall row
"`api.github.com` direct HTTP: blocked → GitHub access is MCP-tools-only"
(LAST-VERIFIED 2026-07-10) to be false as written, corrected it in
menno420/spider-swing (PR #59), and observed the identical stale row here.
Payload: re-measure the claim in THIS container rather than importing the other
repo's numbers, append a dated `capability` row to `## Append log`, correct the
two places where `tools/check_no_false_walls.py` cites the same stale framing as
an example of a *genuine* constraint, regenerate `docs/seat-digest.md`, and
report honestly on what the correction does NOT reach. No code, no behaviour
change, no gameplay or fleet-state change.

- **📊 Model:** opus-5 · high · docs-only — capability-ledger correction

- **⟲ Previous-session review (the owner-live spider-swing thread, same day):**
  strong on evidence discipline — it measured the proxied-vs-direct split
  instead of asserting it, and it corrected the sibling ledger the same session
  it found the fault. Two misses worth naming. First, it reached the media-
  extraction answer by probing the shell from scratch when both this repo's
  ledger and spider-swing's already documented the recipe; the boot file's
  read-the-ledger-first rule existed and went unused, and the owner has had to
  supply that reminder by hand more than once. Second, it treated the
  `[capability-entry-stale]` advisories as noise all day because they are not
  exit-affecting — and the entry they were pointing at is the one that turned
  out to be false. It also stopped at the sibling repo rather than carrying the
  correction here, which is what this card closes.

## What shipped

- `docs/CAPABILITIES.md` — one dated `capability` row at the top of the
  newest-first append log recording the measurement and its stakes. The
  kit-owned seed row is left untouched (the fence rule says findings go below
  it); the dated row is the correction of record.
- `tools/check_no_false_walls.py` — comment-only fix in two places. The guard
  that exists to catch false walls was itself citing `api.github.com` 403 as an
  example of a **genuine** constraint, in its module docstring and again above
  `CORE_CAP_RES`. Both now say the *proxied* path, with a dated pointer to the
  ledger row. No logic touched; `--selftest` still PASSes.
- `docs/seat-digest.md` — regenerated; byte-identical (see the honest null).
- `.claude/CLAUDE.md` — corrected a false claim the ledger work exposed (below).

## The bigger finding: a false guardrail

Pulling the same thread went somewhere unplanned. `bootstrap.py check` emits a
standing NOTE that whether `substrate-gate` is a required check "is owner-UI
state this gate cannot read (rules API; 403-walled to agents)" — the same false
wall, now deferring an answerable question to the owner. It is answerable: the
rules API returns 200 on the direct path. Reading it showed `main` carries
exactly one ruleset (`main-branch-protection`, active) with a `pull_request`
rule and **no required status checks**, and no classic protection either (404).

That made a boot-file claim checkable, and it was wrong. `.claude/CLAUDE.md`
stated "CI enforces this (`check_no_false_walls`, required): a PR documenting an
agent-capability wall cannot merge." The guard appears in **no workflow** —
`grep -rn check_no_false_walls .github/workflows/` returns nothing — and no
required check exists to carry it. Corrected to say the discipline is
self-enforced, with the guard named so a session can run it.

Real enforcement does exist, but workflow-side: `merge-on-green.yml` verifies
every check run on the head SHA is completed+success before merging. So the
automated path is gated; a direct merge is not.

This is the inverse of a false wall and the costlier of the two. A false wall
makes a session do less than it can. A false guardrail makes it trust a net that
is not there — which is how the `api.github.com` row sat unchallenged for 21
days in the one file whose entire job is to be true.

**Not done, deliberately:** wiring the guard into CI. It currently runs CLEAN
and its own header says to promote it once it stays clean, but adding a check
changes merge behaviour for every future PR — a gate change, not a records fix,
and this repo's style is one small step per session. Flagged here rather than
taken unilaterally.

## What was measured (this container, this session)

Same URLs back to back, one flag apart:

| path | proxied | direct | direct + `$GITHUB_PAT` |
|---|---|---|---|
| `repos/menno420/spider-swing` | 403 | 200 | 200 |
| `user` | — | 403 | 200 |
| `repos/menno420/spider-swing/rulesets` | 403 | — | 200 |
| `repos/menno420/spider-swing/actions/workflows` | 403 | — | 200 |
| `repos/menno420/spider-swing/branches/main/protection` | 403 | — | **404** |

Three things follow. The `/user` pair (403 unauthenticated vs 200 with the
token) proves the token genuinely authenticates on the direct path rather than
the endpoint merely serving public reads. The `rulesets` and `actions/workflows`
rows refute this file's own "still walled EVEN in the rescue venue" note for the
read paths. And the `branches/main/protection` row is the sharpest: direct
returns **404** — the true answer, no classic protection configured on that repo
— while the proxy returns 403. The proxy converts a factual "not configured"
into what reads as a permission refusal, which is precisely how a path quirk
gets recorded as a capability wall.

## Honest null

The correction does not reach the surface that matters most for future sessions.
`docs/seat-digest.md` is a derived render of the seed fence only, so
`bootstrap.py seat-digest` regenerated it byte-identical and its line 44 still
reads "blocked → GitHub access is MCP-tools-only". Fixing that needs either a
kit-side seed refresh or a digest that also reads append-log corrections;
`bootstrap.py` and the digest are both generated, so neither is hand-editable
here. Flagged rather than quietly left.

## Verification

Real exit codes, no pipes:

- `python3 bootstrap.py check --strict` → **exit 0**, "all checks passed".
- `python3 tools/check_no_false_walls.py --selftest` → **PASS (0 failures)**.
- `python3 tools/check_no_false_walls.py --strict` → **exit 0**, CLEAN across
  5 living/binding docs.
- `python3 scripts/check_capabilities_grammar.py --strict` → **exit 0**, CLEAN.
- `python3 bootstrap.py seat-digest` → exit 0, no diff.

## Open owner questions

One, and it is not blocking — the correction stands on its own either way.

**Should `check_no_false_walls.py` become a real CI check?** Right now the
never-write-down-a-limitation rule is doctrine with nothing behind it. Three
options, cheapest first: leave it self-enforced and the boot file now says so
honestly; add it to CI as an advisory step (visible, never blocks); or promote
it to a required status check, which needs the ruleset changed as well as the
workflow, since `main` has no required checks at all today. The guard runs CLEAN
and its own header sanctions promotion — but it also admits its detection is
best-effort text heuristics, so making it blocking could red a PR over a
false flag. Advisory-in-CI is the honest middle and my recommendation.

## 💡 Idea

The gate emitted 23 `[stale-wall]` advisories against this file, all
last-verified 2026-07-14 and all non-exit-affecting. That is the same failure
shape the correction itself came from: the spider-swing session skipped
identical advisories as background noise all day, and the one they pointed at
turned out to be false rather than merely stale. Advisories that can only ever
be skipped stop being read. A cheap fix with no gate change: a session that
relies on any capability re-verifies the specific row it relied on and stamps
it — one row per session keeps the ledger honest without ceremony, and the rows
that never get relied upon are exactly the ones whose staleness costs nothing.
