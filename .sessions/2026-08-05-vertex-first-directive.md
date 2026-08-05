# 2026-08-05 · hub — the credit was there the whole time

> **Status:** `complete`

- **📊 Model:** opus-5 · high · research

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/swingy-spider-play-submission-wno3nb`

💡 Session idea: **a documented funding rule that nobody has to act on is just a
fact; it becomes a default only when the route is verified and written where the
next session boots.** `providers/gemini.md` already said the $300 credit excludes
AI Studio and reaches Gemini through Vertex. This session read that page at boot,
then spent 21 calls on the AI Studio key anyway — because the credential in the
environment was the AI Studio one, and the Vertex service account was somewhere
else. Knowing the rule did not change the behaviour; the path of least resistance
did. The fix is not a stronger warning, it is making the credit-funded route
reachable and putting it in the boot file.

## previous-session review

`2026-08-05-play-closed-test-and-gemini-benchmark.md` (PR #745, merged) recorded
the Gemini URL-accuracy benchmark. The owner then challenged the funding
assumption behind those calls, supplied console screenshots resolving a
documented null, and directed that every session default to Vertex.

## What landed

- `docs/conventions/vertex-first-for-gemini.md` — the binding directive plus the
  full verified route, Railway IDs, the `googleSearch` camelCase gotcha, and the
  service-account-to-credit billing chain.
- `.claude/CLAUDE.md` — the directive in the boot file, so a session meets it
  before it reaches for a key rather than after.
- `docs/providers/gemini.md` — banner at the top; the "which funding source
  pays" null replaced with the owner's measured figures.

## Measured

**The funding split, from the owner's console** (console-UI-only data no session
can read — he supplied screenshots, which is what closed the null):

| | |
|---|---|
| Credit remaining | **€251.37 of €256.52** |
| Credit consumed this month | €5.15 — Vertex (Veo, image generation) |
| **Real money this month** | **€0.49** — AI Studio API |
| Forecast end-of-month | €0.00 |

€256.52 is the $300 welcome credit in EUR. The split fell **exactly** along the
documented line: the credit excludes "Gemini API in AI Studio" and does not
exclude Vertex. Attribution caveat kept honest — €0.49 is month-to-date across
the project, and earlier sessions also spent on the AI Studio key (the recorded
image-generation probe alone was ≈$0.086), so this session caused *part* of it,
not provably all.

**The route, every hop exercised** from a container holding no Google credential
(`GEMINI_VERTEX_SA_JSON`, `GOOGLE_APPLICATION_CREDENTIALS`, `GCP_SA_JSON`,
`GOOGLE_CLOUD_PROJECT` all confirmed absent; `$RAILWAY_API_KEY` present):

| Hop | Result |
|---|---|
| Railway GraphQL auth | 200 — `me` resolves to the owner |
| `projects` at top level | **empty** — they hang off `me { workspaces { team { projects } } }`. The one non-obvious step. |
| `variables(...)` on `reliable-grace`/`worker`/`production` | 35 vars; `GEMINI_VERTEX_SA_JSON` 2,420 chars |
| `pip install google-auth cffi` | required — neither present |
| OAuth refresh | token obtained |
| `gemini-3.1-pro-preview` on Vertex | **200** |
| Grounding via `googleSearch` | **200, 5 grounding chunks** |
| `billingInfo` | account `01161F-0357D6-33069D`, "My Billing Account", EUR, open |

**Two things worth carrying forward.** On Vertex the grounding tool is
**`googleSearch`, camelCase** — `google_search` is the AI Studio spelling. And
the Vertex-grounded answer to the tester question returned **12 / 14 consecutive
days**, matching hand-verified ground truth — the same fact `url_context` on the
AI Studio path got wrong (20) earlier today.

**The behavioural finding, which is the real one.** This session read
`providers/gemini.md` at boot. That page already documented the credit
exclusion. It then made 21 Pro calls on the AI Studio key regardless, because
that was the credential sitting in the environment and Vertex needed a service
account from somewhere else. A documented rule with an unreachable path loses to
the path of least resistance every time. So the fix is not a stronger warning —
it is the verified route plus the directive in `.claude/CLAUDE.md`, where a
session meets it *before* choosing a credential.

## Verification

- `python3 tools/check_no_false_walls.py --strict` → **exit 0**, CLEAN across 5
  living/binding docs. Real exit code, not `$?` after a pipe.
- `python3 bootstrap.py check --strict` → **exit 0** once this card flips.
- Every Vertex claim above is a live HTTP response from this session, not a
  reading of a prior doc.
- **No credential committed.** The SA JSON was written outside the repository at
  mode 600, never printed, and deleted; `git status` clean of it throughout.

**Honest nulls:** cost and credit *amounts* remain unreadable from a session —
the Cloud Billing API exposes structure only, with no cost or credit-balance
endpoint, so the figures above are the owner's screenshots and will go stale.
Attribution of the €0.49 to this session specifically is partial, not exact. The
directive is scoped "at least this month" and a later session must re-ask rather
than silently revert.
