# 2026-07-11 — P2 QUEUE GENERATION: owner-queue candidate feed + merged-PR checker + OQ slugs

> **Status:** `complete`

📊 Model: Claude (Fable family, fable-5) · start 2026-07-11T~19:40Z · lane
worker dispatched by coordinator cse_012o8pySy5K3AV6JWoPKryZL

## Declared at open (born-red)

Scope: **phase P2 (QUEUE GENERATION) of the fleet centralization plan**
(superbot `docs/planning/fleet-centralization-plan-2026-07-11.md` §3b/§5,
owner-directed, Option A custodian-primary in force). Kills the
"already-satisfied ask" + "stale pending-merge" drift class (items 1–3 and 13
of the queue would all have fired today). Deliverables this PR:

1. **Candidate feed** — extend `scripts/gen_roster.py` status parsing to
   extract each lane heartbeat's `⚑ needs-owner` / `OWNER-ACTION` blocks into
   a GENERATED `docs/owner-queue-candidates.md` (marked NOT SOURCE OF TRUTH;
   the manager curates `docs/owner-queue.md` from it). Wired into the same
   regen path (manual invocation + `.github/workflows/roster-regen.yml`) so
   it refreshes headlessly.
2. **`scripts/check_owner_queue.py`** — at each wake/regen, for every
   owner-queue item citing a PR with a MERGE action or
   "RESOLVED-PENDING-MERGE of PR #N", query live PR state and FLAG
   already-merged/closed citations. Q-0105 provenance header; known-bad +
   known-good fixtures shipped AND run (verbatim output in this card);
   report-only (never merge-blocking) in the regen workflow.
3. **Stable slug IDs** — every `docs/owner-queue.md` item gets
   `id: OQ-<slug>` (content-derived, never positional — today's renumbering
   by fm PR #75 broke a cross-reference); queue migrated IN PLACE (ordering/
   groups untouched); checker + candidate feed key on slugs.
4. Heartbeat as the deliberate last content commit; card flip last.

Landing path: born-red card+claim first → PR open immediately → build →
heartbeat → card flip `complete` → substrate-gate green on final head → ONE
REST squash-merge attempt (park verbatim on denial; auto-merge arming is a
known wall in this repo — not attempted).

## Shipped (close-out)

All three deliverables landed on PR #85; `python3 bootstrap.py check
--strict` green at the flip except this card's designed born-red hold.

- **Candidate feed** — `gen_roster.py` grew `parse_owner_flags`
  (line-start-anchored `⚑`/`OWNER-ACTION` starts; `needs-owner: none`
  skipped; blocks dedup'd, 25-line cap, code fences ignored),
  `suggest_slug`, `load_queue_pr_index`, `render_candidates`; every regen
  now writes `docs/owner-queue-candidates.md` beside the roster. **First
  committed generation: 65 verbatim blocks across 14 lanes** (gen #8, live
  git-transport run, all repos converged first fetch, no walls) — including
  superbot-next OWNER-ACTIONs 2–6 (six-field blocks), substrate-kit's 13-item
  ladder, websites' seven-ask list, venture-lab ⚑A–⚑F, trading's ⚑(b)–(f).
  Selfcheck extended (extraction ×6, slug ×2, sanitization ×3, queue-index):
  `gen_roster.py --selfcheck` → `selfcheck: PASS (0 failure(s))`.
- **`scripts/check_owner_queue.py`** — merge-actionable detection
  (MERGE / RESOLVED-PENDING-MERGE / HOW-merge), PR citations from URLs (bare
  `PR #N` attributed only when the item cites exactly one repo — never
  guessed), slug presence+uniqueness, positional-ref lint over living config
  surfaces. **Fixture run 1 verbatim** (offline `--selftest`, stub-pinned
  states):

  ```text
  selftest: PASS (0 failure(s))
  --- known-bad fixture output ---
  FLAG [merged-citation] OQ-FIXTURE-GAMES-PR34-MERGE: cited superbot-games#34 is MERGED (2026-07-11T13:40:40Z) — the ask is (at least partially) satisfied; re-verify and sweep
  FLAG [resolved-not-swept] OQ-FIXTURE-UNIVERSAL-CLAUSE: cited fleet-manager#76 is MERGED (2026-07-11T15:26:47Z) (item already self-declares ✅ RESOLVED — sweep it to the Resolved section)
  --- known-good fixture output ---
  (clean)
  ```

  **Live runs** (session transport = github.com HTML fallback, see walls):
  known-bad → same 2 flags, exit 1; known-good → `CLEAN — no merged/closed
  citations, slugs intact`, exit 0. **Live queue at HEAD → 8 FLAGS:**
  `OQ-GAMES-PR27-MERGE`, `OQ-GAMES-PR32-MERGE`, `OQ-GAMES-PR38-MERGE`
  (games #27/#32/#38 owner-merged 14:56:05/17/26Z), `OQ-KIT-PR181-RATIFY`
  (kit #181 owner-merged 14:56:40Z) — **the whole A-section is satisfied** —
  plus `OQ-UNIVERSAL-MERGE-CLAUSE` ×4 (self-declared ✅ RESOLVED, cited fm
  #76/#77/#68/#47 all merged; needs its sweep to Resolved). Deliberately NOT
  swept this slice: the sweep is the manager's curation move, and the un-swept
  queue is the checker's live validation. The owner's acceptance bar ("items
  that cited PRs merged earlier today must fire") is met on both the
  historical fixture AND the real queue.
- **Slug migration** — 33 active items got `id: OQ-<slug>` lines in place
  (script-inserted after the full wrapped title, before the first field
  bullet; ordering/groups byte-untouched otherwise) + a header convention
  note. Old-number→slug table in the PR #85 body.
- **Workflow wiring** — `roster-regen.yml`: regen step + commit path now
  carry `docs/owner-queue-candidates.md`; new REPORT-ONLY probe step
  (`check_owner_queue.py --advisory`, exit 0 always, flags as `::warning::`);
  its own "item 33" positional refs migrated to
  `OQ-FM-ACTIONS-PR-PERMISSION`.

### Walls hit (verbatim)

- **api.github.com is proxy-403 in agent sessions** — `HTTP Error 403:
  Forbidden` on `GET https://api.github.com/repos/menno420/fleet-manager/pulls/76`,
  with AND without `Authorization: Bearer $GITHUB_TOKEN` (curl + urllib
  both; the proxy README's "403 from the proxy = egress policy, do not
  route around" class). **Fallback shipped:** github.com (the allowed
  git-transport host) PR pages embed exactly one `"state":"OPEN|CLOSED|MERGED"`
  marker — verified on open #85 + merged #76 pages; Actions runners keep the
  API path (P1 proof: machine-merged roster gen #7, commit `ad8659a`).
- **Kit gate vocabulary** — `[badge] owner-queue-candidates.md: invalid
  badge token \`generated\`` → feed badges `living-ledger` (roster
  precedent); `[stamp] … D-0005 cited from 2 docs` → feed quotations swap
  decision-id hyphens to U+2011 (checker-inert, documented in-script as the
  one verbatim deviation, same class as P1's api_token_hint strip).
- **Future-stamp near-miss (caught in-session):** the heartbeat was first
  written `updated: 20:25:00Z` against real `20:00:49Z` — corrected to
  `20:00:00Z` before commit (the product-forge future-stamp class; `date -u`
  first, always).

### ⌛ Fixture-rot note (Q-0105 honesty)

The known-good fixture cites fm PR #85 (open at authoring). `--selftest`
pins its state and never rots; a LIVE run of that fixture flags once #85
merges — that is the checker working. First draft cited substrate-kit #181
as the "stays-open" PR; the owner ratified it mid-session (14:56:40Z) —
in this fleet every healthy citation eventually merges, so live fixture
runs are time-stamped evidence, not standing tests.

💡 **Session idea:** `check_owner_queue.py` proves PR-state probing is cheap
(one HTTPS GET per citation, HTML fallback needs no token). The same probe
belongs in the CANDIDATE feed: `render_candidates` could annotate each
extracted block whose text cites an already-merged PR (e.g. superbot-games'
"FIVE PRs need one merge click" block — all five merged) with
`stale-evidence?: <repo>#<n> merged <date>`, so the manager sees intake
items that are pre-satisfied BEFORE curating them into the queue. Cheap:
reuse `fetch_pr_state` from `check_owner_queue` (import or subprocess),
cache across blocks. Guard recipe: extend `render_candidates` in
`scripts/gen_roster.py`, add a `--probe-candidates` opt-in flag first (regen
runtime grows by ~1 request/cited PR), selfcheck with a stubbed fetch.
Dedup-checked: nothing in the feed, queue, or this repo's docs/ideas
surfaces proposes it.

⟲ **Previous-session review:** the P1 session (PR #81, + its #82/#83
same-day correction slices) is a model of honest live-testing — it shipped
a direct-push commit path, watched the real run fail (GH013), corrected to
the PR path, watched THAT fail (createPullRequest permission), and
converted the residue into owner-queue item 33 with verbatim walls. Two
improvements it hands forward: (1) it committed the wall knowledge only in
workflow comments + the owner queue — this session still had to rediscover
the *session-side* api.github.com 403 live because no CAPABILITIES-style
ledger in this repo records per-surface transport walls (fleet-manager has
no docs/CAPABILITIES.md; worth planting at the next docs slice); (2) its
positional reference "owner-queue item 33" inside roster-regen.yml became
drift the moment P2 renamed items — living config should have cited a
stable id from the start, which is precisely the P2 slug lesson,
now enforced by the new positional-ref lint.

## Documentation audit (close)

Everything from this session lives in its durable home: the three
deliverables in `scripts/` + `docs/` + the workflow; decisions/deviations in
the heartbeat slice record (control/status.md) + the PR #85 body; walls
verbatim in this card + the checker's own header; the 8-flag live finding in
the heartbeat for the manager's next sweep. Nothing chat-only. Claim file
deleted at close per `control/claims/README.md`.
