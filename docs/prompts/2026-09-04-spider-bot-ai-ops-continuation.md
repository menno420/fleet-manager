# Continuation prompt — Spider Bot AI operations, review and continue

> **Status:** `reference` · **CONSUMED 2026-09-04, ~1 h after it was written.**
> Kept verbatim as the record; do not paste it at a fresh session — its subject
> is finished. `session_01XtUDb1BxPVdjkGryVWCKVu` (Claude Fable 5.1) acted on it
> at 18:32Z, pushing `8937191c`, and **the owner merged spider-bot#3 at 18:42Z
> as `5a7f8a2`**; the deployment is verified in that repo's session card.
>
> **What it was for, and what it actually bought.** Everything in its DECIDED and
> REJECTED sections was carried so it would not be re-litigated, and none of it
> was. The line that produced new truth was the one admitting ignorance — the
> `preserve()` question marked *NEW, and in no document yet* — which a different
> model went and measured, finding that the IaC would have deleted the rollout
> switches. A handoff's value is in naming what it does not know.
>
> Written at the close of the AI-operations tranche. The copy below is
> byte-identical to the one handed to the owner in chat (fm #1030's lesson);
> the state annotations dated `8937191c` were added in fm #1038, before it
> merged.

```text
CONTINUE: spider-bot#3 is built, green and open, deliberately unmerged. Review
it, get the owner's decision, and take Spider Bot's AI-operations work forward.

BEFORE YOUR FIRST TOOL CALL — state the task back, inline in this same reply,
in four labelled lines (never one fused paragraph, never a question):
  HE SAID — the ask in your own words, one or two sentences.
  ALREADY SETTLED — what the repo already decided about it, naming the file,
                    or "nothing found yet".
  I INFER — the specs, constraints and scope the ask implies, and the follow-on
            the owner probably wants but did not spell out. Labelled inference.
  LEAST SURE — the one reading you are least sure of; he corrects it in a word.
Then begin. This is the owner's one cheap chance to correct your aim; a first
reply that only announces your first action spends it.

WHERE YOU OPEN
Boot in fleet-manager, then `add_repo menno420/spider-bot`. spider-bot has NO
`.claude/` directory — booting there loads no hooks, no skills and no estate
read path, silently. Measured 2026-09-04 with `git ls-tree`.

WHERE THINGS STAND (all verified 2026-09-04, late; re-check anyway)
- spider-bot#3 OPEN, mergeable_state `clean`, head `8937191c`. 24 commits, 59
  files. CI check `quality` completed/success at that head. `d3a66bb` was the
  head when this prompt was written; a review pass pushed one commit on top of
  it at 18:32Z, and the three items below carry what it changed.
- All 40 Codex review threads are RESOLVED. Each was fixed in code first; the
  three round tables in the PR's issue comments record which fix answered which.
- spider-bot `main` is `bf4d7527`, untouched since 2026-08-25. Merging #3 is the
  first production change to this bot since then.
- THE LIVE WORKER IS NOT RUNNING `main`. Railway has `bc4f9985` deployed; the
  `bf4d7527` deployment is SKIPPED, because that commit touched only
  `.railway/railway.ts` and the build watch patterns are `spiderbot/**`,
  `requirements.txt`, `.python-version`. That is correct behaviour, not a fault
  — but it means "verify meta.commitHash == HEAD" would have compared against a
  hash that was never live. #3 changes 33 files under `spiderbot/`, so merging
  it WILL deploy.
- The worker carries exactly three application variables: `ANTHROPIC_API_KEY`,
  `DISCORD_TOKEN`, `GUILD_ID` (names read, never values). Every switch #3 adds
  is unset, so everything arrives off — measured, not inferred from the code.
- spider-swing#181 MERGED. The support feed is live; it was fetched from
  raw.githubusercontent.com and parsed end-to-end (source=feed, live=True).
- fleet-manager#1021 and #1029 MERGED. fleet-manager `main` was `2561874`.
- 669 tests pass, exit 0 (at `d3a66bb` and again at `8937191c`). 55 invariants
  in `CLAUDE.md`.

READ FIRST — a floor, not a boundary
1. `spider-bot/docs/rollout.md` — BINDING, and it wins over every other
   document about what turns on, when, and on what evidence. It also carries
   the owner's six manual steps and the questions that are his to answer, so do
   not re-derive either. Verified at `d3a66bb`; step 3 and the watch-pattern
   line were corrected at `8937191c`.
2. `spider-bot/docs/what-changed.md` — the same thing in plain language, which
   is the version to talk to him from. Verified at `d3a66bb`; its
   *Moderation cases* row said `#mod-cases` where the bot resolves
   `#case-state`, corrected at `8937191c`.
3. `spider-bot/.sessions/2026-09-04-ai-operations-tranche-1.md` — the build's
   own card, including *Deployment outcome*, which says the deployment is NOT
   verified rather than pretending. Verified at `d3a66bb`, watch-pattern line
   corrected at `8937191c`.
4. `fleet-manager/docs/repos/spider-bot/README.md` and `intent.md` — Layer 2;
   the purpose is ANSWERED there, not DRAFT. Verified at fm `origin/main`.
Then: the five issue comments on spider-bot#3 ARE the review record — three
round tables and a standing-down comment naming the residue. Read them instead
of re-deriving what was already found.

DECIDED (do not re-litigate)
- The owner merges, not a session — the bot is live in a real Discord server and
  `main` deploys straight to production with no gate, so what #3 needs next is
  his decisions rather than more code.
- Nothing new enforces on arrival — `MOD_MODE=off`, ceiling `flag_for_review`,
  GitHub projection fail-closed — because a false positive on a tester being
  rude about a hard game is the failure this server is most exposed to.
- The AI supplies judgement; deterministic code supplies authority. Enforced by
  `tests/test_moderation_layering.py` parsing the import graph, so it cannot
  decay into something someone has to remember.
- Publication needs a named human running `/publish`; the privacy classifier is
  a pre-sort, not a gate — an adversarial review reproduced four ways a keyword
  classifier lets a complaint about a named member through, including every
  report written in Dutch.
- `kick` and `ban` are not on the ceiling ladder at all, so raising the ceiling
  cannot reach them; they stay a human action through `/modact`.
- Codex is spent for this PR at three rounds — the hard cap, and the free-key
  Gemini route is where mid-session verification goes instead. Both are
  standing decisions; read them at their home in `fleet-manager/docs/decisions.md`
  rather than from this prompt.

REJECTED, AND WHY
- Auto-publishing "public-safe" reports → the classifier let a named-member
  complaint through four ways. A person is the gate.
- A stricter `quote_floor` than `min(40, max(8, n // 8))` → a rejected verdict
  produces no action AND no case, so over-strictness loses moderation silently
  instead of failing loudly.
- Merging #3 once CI went green → production safety; see DECIDED.
- Connecting a second bot instance to test against Discord → the standing rule
  that two instances must never both be connected. Nothing in this work has
  ever been run against the gateway.
- Filing Gemini's three wrong findings as defects → an unverified reviewer's
  finding is a hypothesis; they are recorded as wrong, with what each was
  checked against.
- Buying a green `substrate-gate` on spider-swing by declaring `high` effort
  when the session ran `xhigh` → the real effort went in a comment instead. A
  green gate bought with a false assertion is worth less than a red one.

OPEN — his to answer. All but the last are already written up in
`spider-bot/docs/rollout.md`; bring them to him, do not re-derive them.
- The six owner-only setup steps: the fine-grained PAT, the `from-spider-bot`
  label, the two private staff channels, the bot's permission set, Discord
  AutoMod rules, and `known_issues` in the support feed.
- Automatic vs reporter-confirmed publication of a public-safe report (one
  field); which repository gets a report about the BOT rather than the game;
  whether tester ideas belong on spider-swing's tracker at all (it holds one
  real issue against 179 pull requests); whether `#intake-state` needs
  splitting; who counts as staff for the panel, which reads `manage_guild`
  alone today.
- ~~NEW: whether an IaC apply would drop a dashboard-set `GITHUB_TOKEN` or
  `MOD_*`.~~ **ANSWERED and FIXED at `8937191c`, so do not re-investigate it.**
  It would have: Railway IaC is omit-means-delete, and a read-only
  `railway config plan` with one existing variable removed from the file
  previewed `Delete variable worker.GUILD_ID`. All six rollout switches are now
  declared `preserve()`; a plan with them added and none of them set reports
  "already up to date", so the lines are inert until each is. Set each switch in
  the dashboard when its step comes, never in the file.

YOUR FIRST STEP
Do not trust the state above — it ages. Re-verify it, then report what moved:
  curl -sS --noproxy '*' -H "Authorization: Bearer $GITHUB_PAT" \
    https://api.github.com/repos/menno420/spider-bot/pulls/3 \
    | python3 -c "import json,sys; p=json.load(sys.stdin); \
print(p['state'], p['merged'], p['mergeable_state'], p['head']['sha'][:8])"
and the deployed hash (urllib gets a Cloudflare 1010 here — use curl):
  curl -sS --noproxy '*' -X POST https://backboard.railway.com/graphql/v2 \
    -H "Authorization: Bearer $RAILWAY_API_KEY" -H "Content-Type: application/json" \
    -d '{"query":"query($id:String!){project(id:$id){deployments(first:3){edges{node{status createdAt meta}}}}}","variables":{"id":"f519761e-a71d-4f4b-8cf6-1dbce06ececf"}}'

DONE WHEN — it branches on his answer, so ask early
- He says merge → merged; the deployment verified by `meta.commitHash == HEAD`,
  NOT by Railway reporting SUCCESS; the real hash written into
  `.sessions/2026-09-04-ai-operations-tranche-1.md` under *Deployment outcome*,
  replacing the line that says it is unverified; and rollout step 1's evidence
  checked (`ready` lists the resolved channels, `/home` opens, `/tester count`
  answers, the AI still replies on mention).
- He wants something changed first → it lands on the same branch and #3 stays
  one PR. Gate before every push: `ruff check .`, `python -m pytest`,
  `python -m compileall -q spiderbot` (what CI runs) AND `python docs/journeys.py`
  (which CI does NOT run). Read the real exit code, never `$?` after a pipe.

OUT OF SCOPE
Do not merge #3 without his word. Do not connect a second bot instance while
the Railway worker is live. Do not touch Discord application identity, server
permissions, Railway secrets, GitHub credentials or provider configuration. Do
not alter gameplay or tuning in spider-swing. Do not add an economy, games
inside the bot, XP, a casino, a web dashboard, arbitrary AI shell or database
tools, or a second source of Slingy Spider product truth. Do not turn Spider
Bot into SuperBot. Never put a Discord user id, private username, private
channel link or raw moderation context into a public GitHub issue; if
sensitivity is unclear, default private.

LESSONS FROM THIS SESSION
- Four of the five worst findings were protections the code DOCUMENTED and did
  not have. A docstring asserting a property is the cheapest possible way to
  stop looking for its absence; every one was caught by executing the claim,
  never by reading it.
- Three of Codex round 3's findings were caused by round 2's fixes, and two of
  Gemini's four by round 3's. A fix moves a problem rather than removing it,
  and nobody has looked at where it moved to.
- I pushed once with ruff red, and wrote two commit messages carrying counts I
  had not read. Everything after that was read from the run's own output first
  — which is also how the stale `22 commits` in the fleet-manager card was
  caught while writing this prompt.

CLOSE WITH
fleet-manager's `session-close` skill, and `python3 bootstrap.py check --strict`
as the one local gate — read its real exit code. spider-bot has no
`bootstrap.py`; its gate is the four commands under DONE WHEN. If spider-bot#3
merges, drive it to terminal state and update both cards before flipping
anything to `complete`.
```
