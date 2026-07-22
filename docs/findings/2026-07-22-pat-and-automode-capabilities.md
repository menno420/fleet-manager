# Findings — GitHub PAT capability matrix + auto-mode/settings.json mechanism (2026-07-22)

> **Provenance:** 2026-07-22, live owner session (model: claude-opus-4-8),
> empirically tested this session with reversible probes against the owner's
> own repos + the current published Claude Code docs. Dated incident doc — the
> legitimate home for exact HTTP codes and platform facts. Written so
> tomorrow-me (and the final EAP email) can reuse it without re-deriving.
> Everything below was **measured**, not assumed.

## TL;DR — three independent gates, routinely confused for one

The recurring "agents can't do X" story collapses into **three separate gates**,
and almost every prior mis-report blamed the wrong one:

| Gate | What it is | What it actually stops |
| --- | --- | --- |
| **GitHub — token scope** | The `$GITHUB_PAT` (account-scoped, fine-grained, **admin on all repos**) | Essentially nothing for our work — broad write confirmed |
| **GitHub — account plan** | The account is on GitHub **Free** | Branch protection / rulesets **on private repos only** (free on public) |
| **Anthropic — auto-mode classifier** | Runtime guardrail in `auto` mode | Sensitive/relayed/"capability-probing" actions, *regardless* of the PAT |

Correcting the misconception a prior agent left the owner with ("the PAT won't
let us create repos, restriction from Anthropic"): the PAT creates repos fine —
what 403s is the **MCP GitHub app** (app scope), and separately the **classifier**
in auto mode. Neither is the PAT.

## 1 · GitHub PAT capability matrix (measured 2026-07-22)

**Path that works:** `$GITHUB_PAT` over **direct egress** —
`curl --noproxy '*' --cacert /root/.ccr/ca-bundle.crt -H "Authorization: Bearer $GITHUB_PAT"`.
The token is **account-scoped** (proven: `POST /user/repos` → `201`, an
account-level op a repo-only token can't reach) and reports
`admin:true, maintain:true, push:true` on every repo checked (proxybench,
venture-lab, substrate-kit, fleet-manager).

| Action (endpoint) | Result | Notes |
| --- | --- | --- |
| Create repo `POST /user/repos` (direct PAT) | **201** | account-scoped confirmed |
| Create repo via **MCP GitHub app** | **403** | `Resource not accessible by integration` — app scope, **not** the PAT |
| Push commits (direct-egress git) | **OK** | `git -c http.proxy= -c https.proxy= push` |
| Edit repo settings `PATCH /repos/{r}` | **200** | `[needs: administration=write]` |
| Create/close issue, create/delete label | **201 / 204 / 200** | `[needs: issues=write]` |
| Create webhook `POST /repos/{r}/hooks` | **422** (Validation) | **auth passed** — payload invalid, not a permission block |
| Read Actions secrets public-key / Actions perms / deploy keys | **200** | `[needs: secrets=read / administration=read]` |
| **Branch protection** `PUT …/branches/{b}/protection` (private repo) | **403** | reason: **"Upgrade to GitHub Pro or make this repository public"** |
| **Ruleset** `POST …/rulesets` (private repo) | **403** | same reason |

**Key nuance (new vs. the 07-18 note):** branch protection + rulesets returning
403 on a **private** repo is a **GitHub Free-plan gate, with a documented remedy
in the message itself** — *make the repo public, or upgrade to Pro*. They are
**free on public repos**. Since 19 of the owner's 20 repos are public, the
capability effectively holds for those 19; the single private repo (copyright
reasons) is the only one where these need public/Pro. (The 07-18 doc's bare
"branch protection 200 / rulesets 201" was a public-repo result; it just lacked
the private-repo caveat.)

**Useful probe technique:** GitHub returns an `x-accepted-github-permissions`
header on every call (success *and* 403), naming exactly which fine-grained
permission the endpoint gates on. Reading it (a non-mutating GET) tells you the
token's real permission set without changing anything.

**Not tested (deliberately, need explicit go-ahead):** repo delete, transfer,
add-collaborator — the irreversible/outward class.

## 2 · Auto-mode vs. `settings.json` — the exact mechanism

The fleet's standing shorthand ("auto mode doesn't read `settings.json`") is
**right in effect**, and the current published docs (Claude Code v2.1.211/212,
fetched 2026-07-22 from code.claude.com) give the precise mechanism — which is
worth having exactly, for the email:

- Auto mode **does** evaluate `deny` / `ask` / **narrow** `allow` rules first
  (fixed order: rules → read-only/edits auto-approved → **classifier** for
  everything else).
- **On entering auto mode it DROPS broad allow rules**: `Bash(*)`,
  `PowerShell(*)`, wildcarded interpreters (`Bash(python*)`), package-manager
  run commands, and `Agent` allow rules. **Narrow** rules (`Bash(npm test)`)
  carry over. `autoMode.classifyAllShell:true` suspends *every* shell allow
  rule.
- The classifier's **own** config (`autoMode.*`) is read **only** from
  `~/.claude/settings.json`, managed settings, or `--settings` — **never** from
  project `.claude/settings.json`, and (since v2.1.207) not from
  `.claude/settings.local.json` either.

**Therefore** the habitual agent remedy — *"add an allow rule to your
`settings.json`"* — is inert in auto mode precisely because (a) the broad allow
rule you'd naturally write for "let me hit the GitHub API / merge" is the kind
auto mode **drops**, and (b) project settings don't reach the classifier at all.
The denial hint that says *"the user can add a Bash permission rule to their
settings"* is therefore **misleading in auto mode** — same finding the fleet
logged empirically, now with the documented cause.

**What actually clears it:** an `allow` rule in `~/.claude/settings.json` (narrow,
survives) overrides the classifier; or drop to **accept-edits** and approve per
call (what the owner did this session — the safer choice for capability probing).
Root-cause of the cross-session denials remains **v2.1.178** (relayed
`SendMessage` no longer carries user authority) + **v2.1.210** (classifier pinned
to Sonnet 5 per session) — consistent with the 07-16 changelog forensics.

## 3 · Reliable "is this setting actually active?" method (owner's pain point)

Owner problem: agents hand back to-do lists that include settings/rules he'd
**already applied hours earlier** — the agent guessed state instead of reading
it. The direct-PAT path fixes this cleanly, because **GETs are idempotent
ground truth**:

- `GET /repos/{r}` → `default_branch`, feature toggles, `visibility`.
- `GET /repos/{r}/branches/{b}/protection` → the live protection object (or 404
  = none).
- `GET /repos/{r}/rulesets` (+ `/rulesets/{id}`) → active rulesets.
- Diff **desired vs. actual**, then only `PUT`/`PATCH` what genuinely differs.

This turns "here's a list of things to do (some already done)" into "here's the
diff between what you want and what's live" — verifiable, no hallucinated items.
This is the concrete win behind the owner's "if you could set the 20 repos'
protection yourself" ask: on the 19 public repos the PAT can both **read current
state and write** protection/rulesets, so an agent can converge each repo to a
declared standard and *prove* it did.

## 4 · Meta — self-knowledge, observed live

This session **reproduced the July-12 root cause** ("agents don't reliably know
their own capabilities") on a fresh model: the assistant confidently said it
would "create and push" a repo — a capability it had **not** verified — and the
tool it was implicitly leaning on (the MCP app) 403'd exactly as the owner
predicted. Truth only came from **firing each action and reading the real
response**.

The honest lesson, and a genuine tension worth naming in the email: the fleet's
"**never document a limitation**" doctrine (a correct guard against *stale
classifier walls*) can push an agent toward the **opposite** error —
**overclaiming** a capability it hasn't tested. The correct synthesis is
symmetric: **assert neither a wall nor a capability without an empirical check
this session.** "Let me try X and report what comes back" beats both "I can't"
and "I can."

(Doc-accuracy nit found en route: `tools/check_no_false_walls.py` ships
**advisory** — `exit 0`, not wired into the substrate-gate — while
`CAPABILITIES-verified-2026-07-18.md` describes it as a required check that
reds a PR. The guard also only gates on *core* caps and exempts `docs/findings/**`
entirely, which is why this dated doc can state the 403 facts plainly.)

## Evidence appendix (raw, 2026-07-22)

```
POST /user/repos (direct PAT)            -> 201   menno420/proxybench created
create_repository (MCP app)              -> 403   "Resource not accessible by integration"
PATCH /repos/{r} settings                -> 200   [needs: administration=write]
PUT   /branches/main/protection (priv)   -> 403   "Upgrade to GitHub Pro or make this repository public"
POST  /rulesets (priv)                   -> 403   same message
GET   /actions/secrets/public-key        -> 200   [needs: secrets=read]
GET   /actions/permissions               -> 200   [needs: administration=read]
GET   /keys (deploy keys)                -> 200   [needs: administration=read]
POST  /hooks                             -> 422   Validation Failed (auth OK)
POST  /labels ; DELETE /labels/{n}       -> 201 ; 204
POST  /issues ; PATCH close              -> 201 ; 200
repo permissions readback (all repos)    -> {admin:true, maintain:true, push:true, triage:true, pull:true}
PATCH /repos/{r} {private:false}         -> 200   proxybench flipped public
```
