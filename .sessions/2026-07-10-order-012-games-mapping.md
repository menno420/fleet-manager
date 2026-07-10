# 2026-07-10 — ORDER 012: games-program mapping proposal (Q-0259 r5)

> **Status:** `complete`

📊 Model: fable family (worker seat, family-level per Q-0262.4) · start 2026-07-10T21:42Z (`date -u`)

## Declared at open (born-red)

Owner-dispatch execution (2026-07-10 ~21:4xZ) for the coordinator: the GAMES-PROGRAM
MAPPING proposal Q-0259 r.5 requires before any founding package ships. Planned, in
this PR:

1. **`control/inbox.md`** — ORDER 012 appended near-verbatim from the owner dispatch
   (this commit), flipped ✅ DONE at close (proposal committed; owner review pending).
2. **`docs/proposals/games-program-mapping-2026-07-10.md`** — the mapping: 3 repos →
   3 Projects, the versioned read-only data API placed + sequenced (grounded in what
   superbot PR #1920's dashboard-data-contract pattern actually is — verified at
   superbot origin/main, not assumed), games-web phase-2 edge, superbot-games
   disposition, in-bot cogs vs superbot-next band-6 relationship. Decide-and-flag:
   one proposed mapping, alternatives one line each. **FOUNDING PACKAGES DEFERRED**
   until the owner reacts.
3. **`control/status.md`** — heartbeat with a prominent **⚑ OWNER-REVIEW** flag
   ("games-program mapping proposal awaits your reaction — founding packages held").
4. This card, flipped `complete` as the deliberate last step.

Sequencing note: PR #39 (projects/ registry) merged 21:33:19Z while this session was
in research; this branch is based on the post-#39 HEAD (`3d105d9`), so
`projects/games-program/{meta,expected-seed}.md` is the committed baseline this
proposal supersedes.

## Done (close-out) · end 2026-07-10T21:58Z (`date -u`)

All four declared items landed in PR #41 (3 commits):

1. **ORDER 012** appended near-verbatim (`control/inbox.md`), flipped ✅ DONE with the
   close-out block citing this PR — review pending, founding packages HELD.
2. **`docs/proposals/games-program-mapping-2026-07-10.md`** committed. The mapping:
   pokemon-mod-lab (QoL+, Q-0262.7) · gba-homebrew (Lumen Drift release-prep + concept
   options) · **superbot-games becomes Project 3** (engine+content; resolves the
   meta.md open question) · games-web stays a forge product (data edge only) · in-bot
   cogs stay superbot-owned, band-6 port stays superbot-next's. **API placement:
   superbot lane** — contracted committed-JSON feed per #1920's *verified* pattern
   (superbot origin/main `655e0fea`: contract + stdlib repo-static producer +
   fail-closed checker + raw.githubusercontent consumption; NOT a live service; the
   games feed needs one NEW DB-reading producer — refresh path decided in the
   implementing superbot PR). Sequence: feed slice now · boots parallel post-reaction ·
   phase-2/stats on feed live (owner's "highest-leverage" read validated, refined to
   parallel-not-gating).
3. **`control/status.md`** heartbeat: prominent ⚑ OWNER-REVIEW block right under
   `blockers:` + phase-line marker.
4. This card flipped `complete` as the deliberate last step.

Evidence honesty notes: websites has NO stats/explorer backlog entry yet
(grep-verified @ `44a9fa6`) — the need is the dispatch's stated intent, flagged in the
proposal §2 with a file-the-entry routing note. superbot-games "121 tests" claim
grep-verified at HEAD `4493292`. PR #39 merged 21:33:19Z mid-research; this branch
based on post-merge HEAD `3d105d9` per the dispatch's sequencing instruction.

💡 Session idea: the games feed's first family should be produced TO games-web's
already-committed consumer contract (`games-web.character-sheet`) rather than minting
a producer-side shape first — consumer-defined contracts invert #1920's flow and would
have caught the BUG-0022 class at design time; worth naming as a pattern variant in
the kit's contract doctrine when the feed ships.

⟲ Previous-session review: the package-centralization slice (PR #39) shipped a clean
18-dir registry but opened its PR based on a stale main (`0eaa668` while #38 was
merging) — it landed fine via GitHub's merge, but basing on a polled fresh HEAD (as
this dispatch explicitly instructed for #39 itself) is the cheaper habit; the
dispatch-side fix (sequencing instructions naming the in-flight PR) already exists —
keep writing them into dispatches.

📊 Model: fable family (family-level per Q-0262.4).
