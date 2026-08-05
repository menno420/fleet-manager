# 2026-08-05 · hub — a mechanism instead of a fourth rule

> **Status:** `complete`

- **📊 Model:** opus-5 · max · docs + tooling

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: the owner asked for **a hook that makes a session find the doc**,
after catching me for the second time skipping one. His instinct was right and
it is the whole point: three rules were written today, all three by me, and
**all three were broken by me within hours.** Prose was never going to fix this.

## What the owner asked

> *"Another time I caught you not reading an important document, can we implement
> a hook that prompts you to find and read the documents that explain your
> capabilities and certain methods to use for these types of requests?
> Ultimately we should then also make sure that … all the right documents are
> correct and relevant"*

Two halves. The mechanism, and then the corpus it points at.

## What landed

| File | Role |
|---|---|
| `.claude/hooks/route_docs.py` | `PreToolUse` matcher — advisory, silent by default, never blocks |
| `.claude/hooks/doc-routes.json` | 19 routes: trigger patterns → docs → one actionable sentence |
| `.claude/hooks/README.md` | design rules, how to add a route, the root caveat |
| `tools/check_doc_routes.py` | validator; `--strict` fails on a real defect |
| `tools/install_root_hooks.py` | installs into whichever directory is *actually* the session root |
| `.claude/settings.json` | the registration (this repo had **no `hooks` key at all** before) |
| `.claude/CLAUDE.md` | boot triad #2 now covers what loaded and why; capability bullet for the hook |
| `docs/CAPABILITIES.md` | step 0 hoisted into the canonical rule; three new append-log entries |

## Verified, with real exit codes

- Pipe-tested raw across six cases before wiring: fires · dedupes · silent on
  harmless input · silent when already opening the doc · exit 0 on malformed
  stdin · exit 0 on empty stdin.
- `jq -e` on the installed matcher → **exit 0**, and `permissions.allow` still
  holds its 12 entries (merged, not replaced).
- **Proved live**: a `Bash` call mentioning `ai.meta.com` produced the injected
  block naming `docs/providers/meta-llama.md`. Dedupe verified silent on the
  third mention. It then fired **organically**, unprompted, on a real
  `api.github.com` call later in the session.
- `python3 tools/check_doc_routes.py --strict` → **exit 0** (19 routes, 0 errors).
- `python3 tools/check_no_false_walls.py --strict` → **exit 0**.
- `python3 bootstrap.py check --strict` → run post-commit, recorded below.

## The validator caught the first defect within a minute

`docs/CAPABILITIES.md` carried the discovery rule **twice** — the canonical
numbered version near the top starting at step 1, and a second copy 1,200 lines
below, which is where step 0 was added earlier today. The boot file pointed at
*"§ DISCOVERY RULE step 0"* as though those were one place. **A session reading
top-down met steps 1–5 and never saw step 0.**

Step 0 now lives in the canonical rule; the duplicate is a pointer plus the
long-form rationale, which was always the part worth keeping separate. Nothing
deleted (OD-6).

## The root finding — and it is bigger than the hook

The owner asked which repo the session's hooks came from. **None of them.**

`/root/.claude/launcher-settings.json` — the harness, not the estate —
registers the only two: `SessionStart` → `session-start-git-identity.sh` and
`Stop` → `stop-hook-git-check.sh`. Measured: **34 `SessionStart` firings** across
today's 17 diag logs, zero of any other event.

He then supplied the mechanism from his own experience, and the disk confirms it:

| Boot | Root | Loads from a repo's `.claude/` |
|---|---|---|
| single source | `/home/user/fleet-manager` — the repo | everything |
| multiple sources | `/home/user` — bare clone parent | **nothing** |

`/home/user` holds all four clones, is **not** a git repo, and has no `.claude/`.
So a multi-repo session loses settings, hooks, skills and the auto-loaded
`CLAUDE.md` of every repo **at once, with no error.** superbot's seven hooks —
including its **hard-fail `Stop` gate** — are among the casualties. The owner
already boots one source per session for exactly this reason, which is why
nobody has been paying that cost; boot-source selection is his, not a session's.

Two things a session *can* act on:

- **`add_repo` mid-session is safe.** Root is fixed at boot and does not move —
  measured: three sibling clones were added to `/home/user/` today and root
  never left the repo.
- A bare `-home-user` entry in `/root/.claude/projects/` is the signature that
  root moved. Then: `python3 tools/install_root_hooks.py --apply`.

This is the § 2 false-negative shape from the foundation doc, exactly: **nothing
fails loudly, the gates are simply absent.**

## Design constraint I held to, and why

The adversarial review's objection to wiring everything to a gate governed this:
*"'Advisory by design' is a human concept — if an agent sees a warning, its
default behavior is to try and fix it."* So the hook is **silent unless a route
matches, its doc exists, it has not fired this session, and the session is not
already opening that doc.** The estate's `--strict` runs already emit ~45
never-exit-affecting advisories; a channel that is usually empty is the only
kind worth writing to.

Same reason the validator splits tiers: deterministic defects are `--strict`
fatal; *"should this doc have a route?"* prints as a note and never fails,
because a judgement call wired to a hard gate produces an agent inventing routes
to make a number go green.

## Honest nulls

- **The hook is a net, not a cure.** It fires only on triggers someone thought
  to add. The failure class it cannot catch is the one nobody has met yet.
- **Whether it changes behaviour is unmeasured** — it fired correctly three
  times today; whether a session that receives the block actually reads the doc
  is one session's worth of evidence, none of it adversarial.
- **The kit's four staged hooks remain uninstalled** in this repo. That is a
  decision to make deliberately, not an oversight to fix blindly — the kit's
  `PreToolUse` uses matcher `"*"` and would run on every call.
- **The multi-repo root claim is owner-observed**, not reproduced here: this
  container has only ever booted single-source. The `-home-user` project-dir
  signature would settle it in one command.

## ⟲ Previous-session review

The card before this one ended: *"a rule does not bind its author any more than
it binds a stranger, which is the strongest argument yet that the estate's
prose-versus-mechanism split is the thing that matters."* The owner read that and
asked for the mechanism. This session is that sentence being acted on rather
than restated — which is the first time today a lesson survived contact with the
next hour.
