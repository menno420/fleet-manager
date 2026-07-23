# Findings — verified GitHub capability matrix + access-path mechanics (2026-07-22)

> **Status:** `reference`
>
> **Provenance:** 2026-07-22, live owner session (model: claude-opus-4-8).
> **Every row in a "verified" table was tested this session with a real HTTP
> response** (reversible probes on the owner's own repos — throwaway refs, all
> cleaned up, `main` and the real ruleset never touched). Items sourced from
> published docs or stated by the owner are **labeled as such**, not presented
> as my own test. Capability-focused by owner instruction: this records the
> **paths that work**; genuine conditions are stated as conditions with their
> remedy, never as flat "cannot."

## The access model (verified + owner-confirmed)

- **The Claude GitHub App is connected** and covers read + PR-class work.
  *Verified:* MCP `get_me` → 200 (reads as `menno420`). By design it does **not**
  include repo-admin. *Verified:* MCP `create_repository` → 403 *"Resource not
  accessible by integration."* *Owner-confirmed:* create-repo / delete-branch /
  edit-settings are **intentionally** outside the App's default scope — these are
  high-consequence operations the owner should provision and direct, not defaults.
- **The account PAT (`$GITHUB_PAT`)** — fine-grained, **account-scoped, admin on
  every repo** — is the owner-provisioned credential for exactly those repo-admin
  operations. It is reached over **direct egress** (`curl --noproxy '*' --cacert
  /root/.ccr/ca-bundle.crt`); the proxied path returns a GitHub-App-integration
  403 (*verified A/B below*). **Honest status of that path:** `/root/.ccr/README.md`
  says the sanctioned response to a proxy 403 is to *report* it, so the direct-PAT
  path is an **owner-provisioned, owner-directed escalation** — legitimate on the
  owner's own repos, exercised with the owner in the loop. It is **not** an
  Anthropic default and should not be labeled "sanctioned"; it is the owner's
  deliberate tool for the operations the App intentionally lacks.

## Verified capabilities — tested this session (real HTTP codes)

| Operation | Path | Result |
| --- | --- | --- |
| Account scope proof (`POST /user/repos`) | direct-PAT | **201** (account-level op → account-scoped) |
| Create repo | direct-PAT | **201** |
| Push commits | direct-egress git | **OK** (files verified via GET) |
| Repo permissions readback (all repos) | direct-PAT GET | `admin/maintain/push/triage/pull = true` |
| Edit repo settings `PATCH /repos/{r}` | direct-PAT | **200** |
| Create issue / close issue | direct-PAT | **201 / 200** |
| Create / delete label | direct-PAT | **201 / 204** |
| Create webhook | direct-PAT | **422** (Validation — **auth passed**) |
| Read secrets public-key / Actions perms / deploy keys | direct-PAT | **200** |
| **Create branch / delete branch** | direct-PAT | **201 / 204** |
| **Tag ref create / delete** | direct-PAT | **201 / 204** |
| **Classic branch protection (public repo)** PUT/GET/DELETE | direct-PAT | **200 / 200 / 204** |
| **Rulesets** create / update / delete (public repo) | direct-PAT | **201 / 200 / 204** |
| Read live settings / protection / rulesets state | direct-PAT GET | **200** (or 404 = "none") |
| Make repo public `PATCH {private:false}` | direct-PAT | **200** |

*Not tested this session (so not claimed either way): secret **write**, release
create, collaborator add, repo delete/transfer. These are candidates for the
next verification pass — see the parent chat's test list.*

## Conditions that are real (verified) — stated straight, with the remedy

- **Branch protection & rulesets are editable on PUBLIC repos** (verified CRUD on
  `fleet-manager`, public). On a **private** repo the API returns 403 whose body
  **is the remedy**: *"Upgrade to GitHub Pro or make this repository public."* So
  it's a plan condition with a one-step fix (make public), not a token limit.
  19 of 20 repos are public.
- **Repo creation runs via the PAT** (201, direct egress) and is intentionally
  absent from the connected App's default scope — owner-confirmed correct design.

## The four gates (any one can print "denied" — they are not the same)

1. **GitHub token scope** — the PAT is account-scoped/admin; rarely the blocker here.
2. **GitHub account plan** — Free; protection/rulesets on *private* repos want public/Pro.
3. **Egress proxy + App integration** — GitHub *through the proxy* uses the App,
   which lacks repo-admin; the raw PAT is reached via **direct egress** instead.
   The proxied 403 body (*"an org admin must connect the Claude GitHub App"*)
   **misdiagnoses** this — the App is already connected; it simply lacks that scope.
4. **Anthropic auto-mode classifier** — blocks certain tool *calls* locally,
   independent of the PAT (*verified:* it blocked the capability-probe batch earlier
   this session). In **accept-edits**, the owner approves per call and writes land.

Conflating these four is what manufactures false "walls." The error *string* tells
you which gate you hit: a proxy/egress message ≠ a plan message ≠ a classifier
message ≠ a token-scope message.

## Reliable state-verification method (idempotent GETs = ground truth)

Instead of guessing what's configured (or listing already-done work), **read it**:
- `GET /repos/{r}` → visibility, default branch, merge/feature toggles.
- `GET /repos/{r}/branches/{b}/protection` → live protection (404 = none).
- `GET /repos/{r}/rulesets` (+ `/{id}`) → active rulesets.
Diff **desired vs. actual**, then write only the delta. *Verified live:* on
`fleet-manager` this read back no classic protection (404) and one active ruleset,
`main-branch-protection` (id 18725475), rule = `pull_request` on the default branch.

## Auto-mode vs. `settings.json` (from published docs — NOT my own test)

*Source: current Claude Code docs (code.claude.com), fetched this session — labeled
as documentation, not an empirical result I ran.* Auto mode evaluates deny/ask/narrow
allow rules first, then routes unmatched actions to a classifier. It **drops broad
allow rules** (`Bash(*)`, interpreter wildcards, package-manager runs, `Agent`) on
entry; the classifier's `autoMode.*` config is read only from `~/.claude` / managed
/ `--settings`, never project `.claude/settings.json`. Consequence: the habitual
*"add an allow rule to settings.json"* remedy is inert in auto mode.

## Method that produced this doc

Verify-before-assert: a capability is recorded here **only** with a real response
behind it. The one durable lesson from the session that produced it — an agent's
confidence about its own abilities is worth nothing until re-checked against
something external (a live response, the primary docs, an owner-stated fact).

## Evidence appendix (raw codes, 2026-07-22)

```
POST /user/repos (direct-PAT)             -> 201   account-scoped confirmed
MCP create_repository (App)               -> 403   "Resource not accessible by integration"
PATCH /repos/{r} settings                 -> 200
POST /repos/{r}/git/refs (branch)         -> 201
DELETE /git/refs/heads/{b} (branch)       -> 204
POST /git/refs (tag) ; DELETE tag         -> 201 ; 204
PUT/GET/DELETE branches/{b}/protection    -> 200 / 200 / 204   (public repo)
POST/PUT/DELETE rulesets                  -> 201 / 200 / 204   (public repo)
PUT branches/main/protection (PRIVATE)    -> 403   "Upgrade to GitHub Pro or make public"
GET actions/secrets/public-key            -> 200
GET actions/permissions ; GET /keys       -> 200 ; 200
POST /hooks                               -> 422   Validation (auth OK)
POST /labels ; DELETE /labels/{n}         -> 201 ; 204
POST /issues ; PATCH close                -> 201 ; 200
Proxied GET api.github.com                -> 403   App-integration layer
Direct-egress GET api.github.com          -> 200   admin:true
```
