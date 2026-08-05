# 2026-08-05 · hub — the credit was there the whole time

> **Status:** `in-progress`

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

[[fill: measured]]

## Verification

[[fill: verification]]
