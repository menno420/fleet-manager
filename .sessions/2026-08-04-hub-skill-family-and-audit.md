# 2026-08-04 · hub — fresh-eyes audit + the image-prompt skill family

> **Status:** `complete`

- **📊 Model:** fable-5 · max · docs-only — session-output audit, skill review, three-skill family

Time: 2026-08-04 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1` (restarted from main post-#719)

💡 Session idea: **a day of corrections leaves the corrected claims consistent
and the summaries of them stale.** Each of today's three correction waves fixed
the section it targeted; none re-read the document's own recap. The recipe list
at the bottom of the art finding still said "never a batch" and "audit after
downscaling" — both superseded hours earlier in the sections above it. A
summary inside a document is a copy, and copies drift exactly the way the
cite-never-copy rule predicts; the fix is the same as the register's: summaries
should carry the least restatement that still reads, and corrections should
grep the whole file, not the section they came to fix.

## previous-session review

`2026-08-04-hub-chroma-spill-measured.md` (PR #719, merged) replaced a quoted
mechanism with a measured one and updated the skill's hard rule — but not the
finding's own recipe recap, which is precisely the drift described above. Its
honest null "conversation images arrive as inline vision, not files" was left
on the card only; it is a venue-scoped surface fact and belongs in the
capabilities ledger, where this session puts it.

## Scope

Owner-directed, on a model/effort change (opus-5 high → fable-5 max) taken for
fresh eyes: audit today's output for undocumented value and internal drift;
review all skills and judge fitness; split image generation into a family —
sprites, parallax backgrounds, cover/icon/banner — each carrying the measured
standard so recurring art tasks stop depending on session memory. Not a program
step; NOW (E1) untouched.

## What landed

- **The skill family.** `image-prompt` rewritten as the shared method + router;
  three new type skills — `sprite-prompt` (set contract, anchor + exclusion,
  enumerated layout, neutral stance), `parallax-prompt` (one layer per call,
  far-opaque / mid-near-chroma split, tiling only where the renderer needs it,
  centre-open composition), `cover-art-prompt` (full-bleed, composition brief,
  thumbnail silhouette test, icon margin rule, the one-word text calibration).
  Every rule in them is traceable to today's measurements or spider-swing's
  committed records. `SKILLS-local.md` indexed.
- **Drift fixes from the fresh-eyes audit.** The art finding's recipe recap
  still carried two superseded rules ("never a batch", "audit after
  downscaling") — corrected to cite the sections that supersede them, with a
  "the skills are the living copy" precedence line.
- **A real bug in three kit-shipped skills**, found by the review agent and
  verified before fixing: `quality-gate`, `session-close` and
  `upgrade-distribution` all ran `bootstrap.py check --strict` TWICE as if two
  gates; the lost second command is unambiguous in this repo
  (`tools/check_no_false_walls.py --strict` — the boot file's own pair). Fixed
  in the live copies; **upstream template unfixed** — flag for the next kit
  touch, since a future `skills --build` + install could reintroduce it.
- **`docs/CAPABILITIES.md`** — the inline-image surface fact promoted from a
  session card to a ledger entry (images = vision-only, videos/docs = files;
  workaround: repo, URL, or wrap in a file format that uploads as a file).

## Routed to the owner (found, deliberately not fixed here)

- **`control/` live-vs-historical conflict:** the boot file rules `control/`
  seat-era historical; four kit-shipped skills (`session-close` claims,
  `scope-backlog-item` baton, `release` status record, `prep-owner-steps`
  contract pointer) treat it as live. One side is stale and picking one
  changes how sessions close — owner call, flagged in chat.
- **Four stub skills** (`analysis`, `question`, `deep-research`, `review`)
  are thin to the point of adding little; boundaries between the three
  read-only ones are undefined anywhere. Recommend fold-or-flesh — owner call
  because two are kit-shipped.

## Honest nulls

- **None of the three new skills has fired yet.** By `SKILLS-local.md`'s own
  rule they earn their place by invocation; `image-prompt` (1 fire, usable
  output ×3 surfaces) is the only proven member.
- **The skill-set review is one agent's read**, spot-verified by me only where
  I acted on it (the duplicate-command bug, the control/ conflict, the CARRY
  drift). The per-skill verdicts for the untouched skills are its, not mine.
- **Gap list is identified, not built:** post-generation asset pipeline skill
  (key→despill→downscale→audit→source-record), audio prompts, a
  capability-probe skill for the ledger's own format, owner status brief.
  Routed to the owner in chat with a recommendation rather than built
  unilaterally — four new skills in one PR is already the largest skill
  change this repo has taken.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
