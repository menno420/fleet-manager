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

**2026-08-08 — and then it had never fired.** The verification above was real
and it was container-specific. Asked directly whether the hook had fired this
session, the answer was **no, not once**: `/tmp/claude-owner-review/` held the
credential cache and **zero log lines**. Three faults, each hiding the next:

1. **`google.auth` is absent from this container**, so `_review` raised
   `ModuleNotFoundError` at every Stop. The lazy import carried a comment
   reading *"absence of google-auth in some container = silent skip"* — the
   failure was anticipated and answered with silence.
2. **`_log` sat downstream of every failure**, so the header's promise that
   *"silent-skip is still countable"* was false exactly when it mattered. A
   mechanism whose absence is invisible is indistinguishable from a working one
   — the **false guardrail** this estate rates as costlier than a false wall.
3. Replacing google-auth with the `cryptography` package made it **worse**:
   that package's Rust layer raises **`PanicException`, whose MRO is
   `PanicException → BaseException → object`** — *not* an `Exception` — so
   `except Exception` did not catch it and the hook **exited 1**. A Stop hook
   exiting non-zero traps the turn, the one cost this design calls strictly
   worse than no hook.

Fixed: sign the service-account JWT with the **openssl binary** (a missing
binary is a `FileNotFoundError`, not a panic inside our interpreter); catch
`BaseException` **after re-raising `KeyboardInterrupt` and `SystemExit`**, since
deliberate termination is not a defect and fail-open must not mean outliving the
process that owns us; and log **every** exit with a `skip` reason.
Re-verified live 2026-08-08 — exit 0, empty stderr, one telemetry line
(`reply_chars=1804, null=false, out_tokens=154, finish=STOP`), three real
provenance questions on first firing, defect path exit 0 and `SIGINT` exit 1.

**What is actually established about the `openssl` dependency, stated narrowly
because the first version of this paragraph was not.** It was measured in
**one container, once** (`command -v openssl` → `/usr/bin/openssl`). That is not
"reliably present in all target environments", and nothing here establishes
that. Two things make it acceptable anyway: the hook is **scoped to this repo**,
so "all environments" is currently one image; and absence now degrades to a
**logged** `skip=review-failed` rather than to silence — which is the whole
repair, and is true whatever openssl does. Credential *acquisition* is untouched
(env → /tmp cache → Railway), so the key-material question is exactly as
established — or as unestablished — as it was before this change; the Railway
reachability path has never been verified outside this container either.

**2026-08-08, later — the auth chain was never needed.** Asked *"why do we need
Google auth?"*, the measured answer is that we do not. Given the same system
prompt and the same reply, **free-tier `gemini-flash-latest` returned the same
two findings** the Vertex/Pro reviewer had produced on the previous turn — the
`BaseException`-swallows-`SIGINT` defect, and an unfounded *"openssl is present
in all our environments"* claim — in **7.1 s, 70 output tokens, at no cost**.
Pro on the free key 429s, as the convention says it will.

That is § 1 restated: **the system prompt is the load-bearing component, not the
model.** The Railway → service-account → OAuth → JWT → openssl chain was buying
a bigger model for a job the small one does.

**Correction — "the only part that ever broke" was an overstatement, and it made
a working capability sound broken.** Google authentication was never absent; the
`google-auth` *library* was. Verified cold 2026-08-08 with the credential cache
deleted: Railway SA **0.8 s** → self-signed JWT access token **0.1 s** → Vertex
`generateContent` **HTTP 200 in 6.7 s**, **7.5 s end to end**. Of the three
"breakages", one was the missing library (fixed in ten minutes), one was the
uncountable-skip *logging* defect — not auth at all — and one was self-inflicted
by the first repair reaching for `cryptography`. Free-first is right because it
is free, needs one header, and § 8 says the model is not load-bearing — **not**
because the credit-funded path is unreliable. So the routing inverts: **free AI Studio
key first, Vertex underneath for exactly one failure, the requests-per-day
cliff.** Consistent with `docs/conventions/vertex-first-for-gemini.md`, which
reserves the Vertex default for volume/image/video and otherwise says *"free key
unless its daily cap is genuinely in the way"* — one ~1 k-token call per turn is
none of those, and the cap is the one real risk, which is what the fallback is
for. Which route answered is now recorded per firing (`"route":"free"`).
Honest null: n=1 input, one run per model — not a model comparison.

**2026-08-08, final — the model is not the mechanism.** Owner: *"for the hook we
don't even need gemini at all right? The hook itself should ask 'what made you
draw this conclusion?' and that does not require gemini."* Correct, and the
findings already said so — § 8 measured both questions **content-independent**
(he composed Q1 before the output existed, pre-committed to firing it regardless
of content, screenshotted the pre-commitment; it landed anyway), and rated the
options: *"fixed-and-always-on and blended-into-conversation both avoid the
test-signal; **selective firing is the worst of the three**."* A reviewer that
returns `NO QUESTIONS` on some turns **is** selective firing. The hook had been
built as the worst of the three, on top of the only component that could break.

So it inverts: **the fixed question IS the hook** — no model, no network, no
credentials, no quota, no failure mode. The model is strictly **additive
enrichment** appended under *"And specifically:"* when it happens to answer.
Question 2 stays explicitly conditional on question 1 surfacing something, per
§ 8's ordering — it has no referent otherwise, and the pair is a check, not a
quota.

Measured both ways 2026-08-08: with `GEMINI_API_KEY` and `RAILWAY_API_KEY`
stripped from the environment it still blocks (`route:null, enriched:false`,
exit 0); with the free key present it blocks with two real specifics appended
(`route:"free", enriched:true, out_tokens:76`).

**And the answer to why Vertex ever needed Google auth**, since it is structural
rather than a choice we made: Vertex refuses API keys outright —
`401 UNAUTHENTICATED: "API keys are not supported by this API. Expected OAuth2
access token or other authentication credentials"` (measured directly against
`aiplatform.googleapis.com`). Credit-funded ⇒ Vertex ⇒ OAuth ⇒ service account ⇒
Railway ⇒ signed JWT. Every link forced; the only exit was not using Vertex on
the critical path, which is what this change does.

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

---

## `read_before_write.py` — prose about a file nobody opened

`PreToolUse`, advisory, fail-open. Records the paths a session actually fetches
(read-tool inputs), and when the session writes prose *describing* a path it
never fetched, says so.

**Why it exists — MEASURED 2026-08-08 on this repo's own transcript.** A session
built `docs/repos/spider-swing/` and wrote a boot-path table glossing eight of
that repo's files in one line each. Split by whether it had fetched the file
before writing the line:

| | wrong |
|---|---|
| fetched first (3 files) | **0 / 3** |
| not fetched (5 files) | **3 / 5** |

The three errors were plausible and none was catchable downstream:
`AGENT_ORIENTATION.md` called an instruction set when it is a reading-*router*,
`decisions.md` called an ADR log when it cites `[D-NNNN]` ids, and
`architecture.md` listed as ordinary reference when its badge is `binding` — so
a later session would have been told there was one binding contract where there
are two. **An unread description reads exactly like a read one**, which is why
this is a mechanism rather than a line of advice.

**What it checks, and the boundary that matters.** It checks a *fact* — was this
path named in a read tool's input before the prose was written. It does **not**
check whether the file was understood; that is a judgement, and this estate has
twice withdrawn a gate that tried to mechanise meaning (the provenance gate, and
"attached a repo ⇒ touched its folder"). So it never blocks, and a **quiet hook
is not evidence of anything** — only a firing one carries information.

Deliberately narrow, to keep the channel worth reading: a path counts as
*described* only when prose follows it on the same line (a table cell, an
em-dash gloss, a colon). Bare links, imports and paths inside commands are
pointers and are ignored. Reported once per path per session, capped at 5.

Two behaviours found by testing it against real files rather than fixtures:
markdown-link table rows (`[`docs/x.md`](../docs/x.md) | what it is`) hid the
path from the first version, so links are collapsed to their label before
matching — it had gone silent on 25 described paths, and for an advisory a
silent miss is the worst outcome available. And a *directory listing* must not
count as having read a file: matching on returned text let `ls` output launder
a filename into "read", which is why only tool **inputs** are recorded.

```bash
# fires: describing files never opened
echo '{"session_id":"t","hook_event_name":"PreToolUse","tool_name":"Write","tool_input":{"file_path":"r.md","content":"| `docs/decisions.md` | the decision ledger (ADRs) |"}}' | python3 .claude/hooks/read_before_write.py
# quiet: a pure link list is a pointer, not a description
echo '{"session_id":"u","hook_event_name":"PreToolUse","tool_name":"Write","tool_input":{"file_path":"x.md","content":"See [a](docs/a.md) and [b](docs/b.md)."}}' | python3 .claude/hooks/read_before_write.py
# registration (both hooks, all events)
python3 tools/install_root_hooks.py
```
