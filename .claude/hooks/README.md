# Hooks — the doc-routing net

> **Status:** `reference` · added 2026-08-05

## What this is

A `PreToolUse` hook that watches for a session about to probe something the
estate has already documented, and injects the doc path plus one sentence of
what it says.

It exists because prose failed. On 2026-08-05 a session wanted a multi-turn
Gemini conversation, fetched `generativelanguage`'s discovery document, found no
`interactions` endpoint, and wrote *"unavailable"* into `docs/CAPABILITIES.md` —
while [`docs/providers/gemini.md`](../../docs/providers/gemini.md) carried the
working recipe. The same session had authored the rule against exactly that,
**three hours earlier**. A rule does not bind its author any more than a
stranger, so the fix had to be a mechanism.

| File | Role |
|---|---|
| [`doc-routes.json`](doc-routes.json) | the route table — trigger patterns → docs → one sentence |
| [`route_docs.py`](route_docs.py) | the matcher; advisory, silent by default, never blocks |
| [`../../tools/check_doc_routes.py`](../../tools/check_doc_routes.py) | validates the table; `--strict` exits 1 on a real defect |
| [`../../tools/install_root_hooks.py`](../../tools/install_root_hooks.py) | installs into whichever directory is actually the session root |

## Design rules, and why each one

1. **It never blocks.** Advisory only, exit 0 on every path including a crash.
   A hook that can stop work eventually stops the right work.
2. **Silence is the default.** A route fires only when it matches, *and* its doc
   exists, *and* it has not already fired this session, *and* the session is not
   already opening that doc. An agent tries to satisfy whatever appears in its
   feedback channel, so a channel that is usually empty is the only kind worth
   writing to. See
   [`docs/findings/2026-08-05-foundation-continuation.md`](../../docs/findings/2026-08-05-foundation-continuation.md)
   § 5 — the estate's `--strict` runs already emit ~45 advisories that are
   explicitly never exit-affecting, which is the noise field this must not join.
3. **It writes nothing to the repo.** Session state lives under
   `/tmp/claude-doc-routes/<session-id>.json`, so the hook never dirties the
   tree a session is trying to keep clean.
4. **Every route points at a doc that genuinely covers its trigger** — enforced,
   not assumed. See below.

## Adding a route

Append to `routes` in `doc-routes.json`:

```json
{
  "id": "short-slug",
  "when": ["regex", "another\\.host\\.com"],
  "docs": ["docs/path/to/doc.md"],
  "says": "One sentence a session can act on without opening the doc."
}
```

The bar for a new route: **a session that skipped this doc would probe blind and
could plausibly conclude "unavailable" about something that works.** That is the
whole population worth catching. A route that merely adds background reading is
noise, and noise is what makes the useful ones invisible.

### Two kinds of route

| | fires on | matched against | suppression |
|---|---|---|---|
| **probe route** (default) | `Bash` `WebFetch` `Read` `Glob` `Grep` | command, url, path, pattern | silent if the session is already opening that doc |
| **content route** (`"tools": ["Edit","Write"]`) | only the tools it names | **what is being written** — `new_string` / `content` | none — firing on an edit to its own doc is the point |

`recording-a-wall` is the content route: it fires when limitation-shaped prose
enters any doc and asks the two questions that would have prevented the
2026-08-05 Interactions-API wall — *did the owner already say otherwise*, and
*has the estate already measured this*. Declaring `tools` is what keeps content
routes off ordinary tool calls; without it a route joins the probe set.

**Known false-positive class:** writing *about* a wall is wall-shaped, so
documenting this mechanism trips it. One advisory line, once per session, never
blocking — cheap enough to accept rather than weaken the pattern.

Then:

```bash
python3 tools/check_doc_routes.py --strict   # must exit 0
```

## The coverage check is the point

A route table decays in one specific way: the doc gets rewritten, moved or
narrowed, the route keeps pointing at it, and the hook confidently sends a
session to a page that no longer covers what it triggered on. **That is worse
than no hook**, because the session stops looking.

So the validator requires that **at least one of a route's `when` patterns
actually occurs in at least one of its docs.** A doc that stops covering its
trigger fails the check instead of misrouting a session.

It earned this immediately: the first thing it caught was `docs/CAPABILITIES.md`
carrying the discovery rule **twice** — the canonical numbered version near the
top starting at step 1, and a second copy 1,200 lines below where step 0 had
been written. The boot file pointed at "§ DISCOVERY RULE step 0" as though those
were one place, so a session reading top-down never met step 0.

The validator also prints `NOTE unrouted:` lines for capability and method docs
that no route and no boot file mentions. Those are **informational and never
fatal** — whether a doc deserves a route is a judgement, and a judgement wired
to a hard gate produces an agent inventing routes to make a number go green.

## Where this gets installed — root is not always the repo

Claude Code loads `<root>/.claude/settings.json`, where root is the session's
working directory. Measured in this container on 2026-08-05:

| Boot | Root | What loads from a repo's `.claude/` |
|---|---|---|
| single source | `/home/user/fleet-manager` — the repo | everything |
| multiple sources | `/home/user` — the bare clone parent | **nothing** |

`/home/user` holds all four clones, is not a git repo, and has no `.claude/`
directory. So a multi-repo session loses every repo's settings, hooks, skills
and auto-loaded `CLAUDE.md` **at once, with no error** — superbot's seven hooks
including its hard-fail `Stop` gate simply are not there.

The owner boots one source per session precisely because of this, and source
selection at boot is his to make, not a session's. Two things follow for a
session:

- **`add_repo` mid-session is safe.** Root is fixed at boot and does not move —
  measured: `substrate-kit`, `superbot` and `superbot-next` were all added to
  `/home/user/` during 2026-08-05 sessions and root stayed on the repo.
- **If you ever find root above the repos, install the hooks yourself:**

  ```bash
  ls /root/.claude/projects/          # a bare `-home-user` entry = root moved
  python3 tools/install_root_hooks.py --apply
  ```

  That path is outside any repo, so the file is not version controlled and dies
  with the container — re-run it once per session.

The repo-local `.claude/settings.json` already carries the registration for the
ordinary single-source case, so nothing is needed there.

## Verifying the hook end to end

```bash
# 1 · pipe-test the matcher directly
echo '{"session_id":"T","tool_name":"Bash","tool_input":{"command":"curl https://generativelanguage.googleapis.com/v1beta/models"}}' \
  | python3 .claude/hooks/route_docs.py

# 2 · schema-validate the registration
jq -e '.hooks.PreToolUse[] | select(.matcher == "Bash|WebFetch|Read|Glob|Grep")
       | .hooks[] | select(.type == "command") | .command' .claude/settings.json

# 3 · prove it fires — run any command mentioning a trigger, then:
cat /tmp/claude-doc-routes/*.json     # the route id appears once it has fired
```

**A firing consumes that route for the session.** If you need to re-test the
same route, delete the state file first — and note the ordering: the hook runs
*before* the command, so a command that itself deletes the state directory will
look like the dedupe failed when it did not.

## The owner-review Stop hook — `owner_review.py`

> added 2026-08-07 · design record:
> [`docs/findings/2026-08-06-provenance-mechanism-measured.md`](../../docs/findings/2026-08-06-provenance-mechanism-measured.md)

The second hook here, and a different species: it fires at `Stop` (turn end),
reads the final reply from the transcript, sends it to the owner-stand-in
reviewer on Vertex, and — only when the reviewer returns questions — blocks
**once** so the agent addresses them in the reply the owner actually reads.
`stop_hook_active` guards the second pass: one round per turn, ever.

Everything load-bearing in it is measured, not designed:

- **The system prompt is the mechanism.** The same model, unframed, endorsed a
  known-wrong design and praised its specific defect (findings § 1). The
  owner-stand-in framing is committed verbatim in findings § 7 and inlined here.
- **`Stop` is the only viable event** — at `UserPromptSubmit` no claim exists
  yet to ask about (findings § 2).
- **The hook runs the review itself** — run 4's untried path, named by the
  reviewer: no skill invocation, no agent initiative anywhere in the loop
  (findings § 1 addendum).
- **The null path is normal.** The reviewer outputs `NO QUESTIONS` and the turn
  ends untouched. A review that must always find something is ritual.
- **Fail-open is a hard contract.** Any defect — creds, network, parse, timeout
  — exits 0 silently, and the firing (or its absence) is countable at
  `/tmp/claude-owner-review/log.jsonl`.

Verified 2026-08-07: guards by pipe-test (`stop_hook_active`, missing
transcript, sub-400-char reply — all exit 0, empty); the full cold chain
(Railway → service account → OAuth → Vertex → verdict) live at ~12 s, ~7 s
warm. Its first verdict re-caught the previous day's real rulesets false wall
from a synthetic reproduction — *"did you try the classic Branch Protection
API, or did you stop at Rulesets?"* — which is the acceptance shape: the
untried path, named. One transport quirk is load-bearing: Railway's edge 403s
the default Python-urllib User-Agent; any explicit UA passes.

Scope: **this repo only** until a week of telemetry says otherwise — the
no-fleet-rollout decision stands.

```bash
# guards (exit 0, no output)
echo '{"stop_hook_active":true}' | python3 .claude/hooks/owner_review.py
# full chain against a claim-bearing transcript
echo '{"session_id":"t","transcript_path":"<some .jsonl>"}' | python3 .claude/hooks/owner_review.py
# registration
jq -e '.hooks.Stop[].hooks[].command' .claude/settings.json
```
