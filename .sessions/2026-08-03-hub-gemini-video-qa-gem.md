# 2026-08-03 · hub — Gemini visual-QA Gem: tier research, verified grounding block, hallucination protocol, share-link capability

> **Status:** `complete`

- **📊 Model:** opus-5 · high · research + docs

Time: 2026-08-03 · venue: owner-live hub chat · branch
`claude/gemini-video-qa-gem-jehvhh` · PR fm #696

💡 Session idea: **a handoff should carry a negative inventory — what the
evidence excludes — and nothing in this estate currently does.** The sharpest
finding of the session is that one session read four in-game strings correctly
off a HUD and, in the same conversation, invented 1 600 commits across 400
branches for a five-day-old repository. The difference is not care, model
quality or prompting: video was in the room and git history was not, and
**nothing told it the archive it had been given contained no history**. A
"Download ZIP" export looks, from the inside, exactly like a repository. The
substrate is built entirely out of positive claims — what is known, what
happened, what was verified. It has no slot for *what a given piece of evidence
cannot answer*, so every reader has to rediscover each absence, and a reader
that fails to notice one fills it fluently instead. Concretely: session cards
and handoff docs could carry a one-line "not in here:" alongside the verify
command. Cheap to write, and it targets the one failure mode that is invisible
in the output — because a fabricated answer and a sound one read identically
when the missing evidence was never named.

## previous-session review

`2026-08-01-e1-owner-reserved.md` recorded that E1 is owner-reserved rather than
stalled, and named the reason: every evening since 07-26 has gone to
spider-swing, the one asset with a live external signal. This session is that
same triage continuing — owner-directed spider-swing work, not a program step.
E1 was not touched, and the NOW pointer still reads E1 with its owner-reserved
annotation intact.

That card also did something worth copying: it stated the truth in the place a
future session will actually read, rather than in the place it logically
belonged. Applied here by putting the corrected grounding facts in a paste block
next to the instructions that use them, not in a prose section about them.

## Scope (owner ask, four parts + one verification)

1. Is a paid Gemini tier worth it, on the owner's narrow criterion (capability,
   not quota)? Cited, with this-session-verified separated from training data.
2. Paste-ready Gem: system instructions + knowledge file, every game fact
   re-verified against `menno420/spider-swing` source.
3. Hallucination diagnosis + a concrete prompting protocol with a
   verified/inferred marking convention.
4. The share-link read method verified and recorded as a durable capability —
   Gemini **and** ChatGPT.
5. Claim-by-claim verification of a deep-research report the owner supplied.

## What landed

- **`docs/research/2026-08-03-gemini-paid-tiers.md`** — the context window is the
  only paid difference that is capability rather than quota: 32k free / 128k AI
  Plus / 1M AI Pro+Ultra. At the documented ≈300 tokens per second of video that
  is **under two minutes of footage** on free, for the whole conversation. Ten
  clips were sent in one message. The recommendation is conditional on a test the
  owner has not run yet, and says so.
- **`docs/research/2026-08-03-gemini-visual-qa-gem.md`** — three paste blocks
  (instructions · knowledge file · per-clip message), an acceptance test whose
  fourth point is the one that matters, and the six source files to regenerate
  the knowledge block from.
- **`docs/research/2026-08-03-gemini-report-verification.md`** — the report is
  right about the engine, the three workflows and the shape of the game, and
  wrong about **every** file path it names. Plus seven errors in the pre-existing
  grounding block.
- **`docs/research/2026-08-03-reducing-invented-detail.md`** — four mechanisms,
  five rules, and the `[SEEN]` / `[INFERRED]` / `[UNSURE]` convention, each rule
  mapped to the mechanism it targets.
- **`docs/conventions/reading-shared-ai-chats.md`** + **`tools/read_shared_chat.py`**
  — the method, the three fixes, and what each failure looks like if you skip one.
- **`docs/CAPABILITIES.md`** — two entries appended.
- **`docs/owner-queue.md`** — `OQ-GEMINI-TIER` added.

## The thing worth carrying forward

The pre-existing grounding block was written from source and was still wrong in
four places. The worst was the hazard vocabulary: it gave Bramble Canopy "canopy
pods, bramble curves, bramble steps", and `course_pattern_catalog.gd` puts all
three in **Ancient Forest**. Bramble Canopy's entire pool is eight entries —
hooks, leaves, shutters. Pasted as-is, that block would have taught the reviewer
to name a Bramble Canopy object something that cannot appear there, and the
resulting misreadings would have looked like reviewer error.

That document already carried one correction where a previous session called a
real in-game string invented. Two corrections in opposite directions on the same
page is the argument: **the direction of the error is not predictable, so
re-derivation is not optional and re-reading is not re-derivation.**

## Guard recipe — regenerating the knowledge block

When spider-swing's regions, HUD or pattern catalogue change, Block B of the Gem
doc goes stale silently — nothing fails, the reviewer just starts being
confidently wrong. Anchors: `CourseRegionCatalog.REGIONS`
(`game/domain/course_region_catalog.gd`), `_draw_hud` and `_run_access_status`
(`game/presentation/scripts/swing_lab.gd`), the four `DEATH_REQUESTED` sites
(`game/simulation/simulation_world.gd`), and the per-region pools +
`_region_pool_for` (`game/application/course_pattern_catalog.gd`). Six files,
about fifteen minutes.

## Honest nulls

- **ChatGPT share-link extraction is not verified.** Transport, TLS through the
  imported NSS store, hydration and route-specific text extraction from
  `chatgpt.com` all confirmed; no valid public share id was available to test a
  real transcript against. Recorded as partial rather than claimed.
- **The grounding block still has not been tested in a live review.** Every fix
  is verified against source; none is verified against a subsequent review round.
- **Whether lifting the context ceiling fixes the batch failure is an
  inference.** Consistent with the evidence, not measured. The test is
  `OQ-GEMINI-TIER` and it is one evening.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
python3 tools/read_shared_chat.py --setup
python3 tools/read_shared_chat.py "https://share.gemini.google/3MvaF0QMFGFn" -o /tmp/out.txt
```

Last run this session: gate red **only** on this card's own designed hold;
false-walls guard `CLEAN`; share read returned 70 426 characters.
