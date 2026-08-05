# 2026-08-05 · hub — boot superbot-next and measure what the harness could not see

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/swingy-spider-play-submission-wno3nb`

💡 Session idea: the owner said "boot up the bot yourself" after three of this
session's claims about it turned out to be wrong. Booting it settled every one
of them in minutes, and then surfaced the thing no amount of reading had —
a panel that reports 58 modules healthy from a hardcoded tuple.

## Previous-session review

PR #757 landed the playtest-Discord research and recommended *against*
deploying superbot-next. The owner overrode that with a reason: superbot carries
architectural debt and superbot-next was meant to be a clean functional clone.
Testing that claim is what this session did.

## What landed

- `docs/findings/2026-08-05-superbot-next-live-audit.md` — the measurements, the
  `CAPTURE-WORLD LITERAL` finding, the harness diagnosis, the server-first
  subsystem shortlist for milestone one, a reproduction recipe, and a section
  recording this session's own five wrong claims.
- `docs/findings/README.md` — index row.

## Measured

**The named convention.** `CAPTURE-WORLD LITERAL` is a formal term in
superbot-next carrying trap numbers and precedents. Its own words:
*"both goldens pin the one value, so the line ships as the pinned literal;
the live … count is the honest successor read."* A value the old bot **computed**
ships as a constant because the capture corpus observed it once.

The Cog Manager is the complete case: 58 hardcoded `superbot` module filenames
in a tuple, status glyphs inside the f-string with no check
(`lines.append(f"✅ 🟢  \`{name}\`…")`), Unload observed `blocked` in the live
trace, and a legend telling the operator to run `!cog unload` — one of the three
commands never ported.

**Scope, with its limit stated:** 4 labelled files, not the 34 mentioning
"capture world" (most are legitimately-static game data). Unlabelled instances
are invisible to the method used.

**Why the harness certified it:** a polite refusal replays byte-identically, a
photograph *is* the captured bytes, and an absence emits no output to compare.
`533/533 · 49/49 · zero unmapped` is true and compatible with panels that do
nothing.

**By running it:** boots `verified: true` exit 0; gateway READY, 3 guilds;
1,327 dispatch targets; 314 panels / 640 buttons; 49/49 manifests load with no
filter parameter; zero runtime load/unload; 17 of 368 command names absent, 3
of them real; menu-vs-text 17% against superbot's ~21% — **inherited**.

## Verification

- `python3 tools/check_no_false_walls.py --strict` → **exit 0**.
- `python3 bootstrap.py check --strict` → **exit 0**, run **post-commit**.
- Both bot repositories cloned and read-only; a local PostgreSQL 16 cluster and
  a venv on `requirements.lock` built in-container; the bot connected to Discord
  on the **test** token and was shut down with SIGTERM → `lifecycle STOPPED —
  clean exit`. Postgres stopped after.

**Honest nulls** (carried into the finding's § 9): the literal audit is not
exhaustive — labelling is not guaranteed complete; superbot's ~21% is an AST
estimate while superbot-next's 17% is exact; the 70 terminals figure is a grep
of refusal copy, not a click census; 46 of 49 subsystems were never opened live.

## 💡 Session idea

**Three claims died the moment the thing was run, and the owner had to say "boot
it yourself" before that happened.** Reading produced: superbot can't disable
cogs (it can), the boot gate blocks a subset (it doesn't), and the environment's
token is production (it is the test app — the repo's own testing ledger says so
in the file the working agreement lists as required reading). Each was minutes
of execution away.

The deeper pattern is the one the finding is about, and this session enacted it
in miniature. superbot-next's harness compares output bytes and cannot see the
difference between a working panel and a photograph of one. This session
compared *source text* against *expectations* and could not see the difference
between a documented decision and a documented decision that was wrong. Both are
the same error: **taking a faithful reproduction of a description as evidence
about the thing described.** The correction in both cases is identical — run it,
and see whether anything happens.
