# 2026-07-10 — ORDER 013: conformed games mapping (Q-0267 owner-shaped frame)

> **Status:** `complete`

📊 Model: fable family (worker, coordinator-dispatched) · start 2026-07-10T22:3xZ (`date -u`)

## Declared at open (born-red)

Worker for the coordinator's round-3 part-4e dispatch. The games mapping is now
OWNER-SHAPED (superbot router Q-0267): Seat A = one Project on `superbot-games`
(whole world ecosystem, gen-2 relaunch), Seat B = new repo + Project for the idle
game (egg farm = first THEME of a template-first idle engine), website-first
onboarding, core/skin split. About to land, in this PR:

1. **ORDER 013 appended to `control/inbox.md`** (dispatch near-verbatim) and
   flipped ✅ DONE.
2. **`docs/proposals/games-program-mapping-conformed-2026-07-10.md`** — the
   CONFORMED mapping filling in the four details still ours to place: data-API
   reconciliation (stay/move/split) · theme-manifest contract home · new repo
   name · first-shippable sequencing per seat.
3. **Supersedes banner** on `docs/proposals/games-program-mapping-2026-07-10.md`
   (one-line edit pointing at the conformed doc — superseded AS A SHAPE by
   Q-0267).
4. **`control/status.md` heartbeat** — ⚑ OWNER-QUEUE flag refreshed to the
   conformed doc ("Q-0267 frame, details filled: API/contract/name/sequence"),
   other flags kept.
5. **`docs/owner-queue.md`** — games-mapping review item refreshed to point at
   the CONFORMED doc.

Evidence base read at pinned refs before writing: superbot origin/main
`9624c539` (router Q-0267 block + `docs/ideas/games-theme-engine-website-first-
2026-07-10.md`), superbot-next origin/main `4a32f61` (D-0056 +
`docs/game-plugin-contract.md`), fm PR #41 proposal, `menno420/
superbot-plugin-hello` existence probe (list_repos: EXISTS, public, pushed
2026-07-10T16:03:04Z; raw main/master both 404 → EMPTY shell, seeded package
not yet pushed).

## Close-out

Landed exactly the five items declared above, one PR.

The four placements (full grounding in the conformed doc):

1. **Data API → SPLIT.** Game-state read feed stays the superbot-lane
   committed-JSON contract feed (#1920 pattern, unchanged — superbot owns the
   Postgres). Theme/feature manifests are different data: committed files in
   the game-seat repos + superbot-next's plugin registry, raw-fetched by
   websites. New write path (provisioning manifest) = plugin-contract family,
   phase-1 setup-code.
2. **Theme-manifest contract → Seat B repo drafts v1** (engine owns its schema;
   theme-gate CI co-locates), flagged for promotion into superbot-next's
   plugin-contract family when a second game consumes it. Websites renders the
   gallery by raw-fetching schema + `themes/*.yaml`.
3. **Repo name → `superbot-idle`** (sibling symmetry with `superbot-games`;
   distribution inside follows the plugin naming). Alternates:
   `superbot-plugin-idle`, `idle-engine`.
4. **Sequencing** — dependency-honest: plugin-hello validation push (unblocked
   NOW, repo exists but EMPTY) ∥ Seat A relaunch (CI-gap fix → fishing on
   mining's substrate) ∥ superbot game-state feed slice → Seat B skeleton
   (core → schema+CI → egg-farm theme) → websites selector LAST-shippable
   (needs committed themes to render; website-first is the user flow, not the
   build order).

💡 **Session idea** (dedup-grepped `docs/`): a `tools/check_supersedes.py`-style
proposal-freshness rule — any `docs/proposals/*.md` with `Status: plan` older
than N days without a supersedes/decision banner gets flagged on the manager
wake, so owner-shaped rulings (like Q-0267 today) can't leave a stale "awaiting
react" proposal looking live. Cheap grep, catches exactly today's drift class.

⟲ **Previous-session review:** the #43 universal-pointer worker shipped a clean
paste-same-everywhere block and its card declared scope precisely — good. Miss
worth one line: it did not stamp `projects/games-program/meta.md` (pre-birth
archive) with a pointer to the then-live #41 proposal, which this session now
had to chase across three docs; improvement adopted here — the conformed doc
carries explicit supersedes/carry-forward lines for every predecessor artifact
it touches.

· end 2026-07-10T22:55Z
