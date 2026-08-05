# 2026-08-05 · hub — the tool decided, not the model

> **Status:** `complete`

- **📊 Model:** opus-5 · high · research + build — closed-test path, Gemini benchmark

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/swingy-spider-play-submission-wno3nb`

💡 Session idea: **the same model, the same key, the same day, gave opposite
answers to the same question — and the difference was which tool it used.**
Asked how many testers Play requires, `google_search` grounding said **12** and
volunteered that it had been reduced from 20. `url_context`, pointed at the very
page that says 12, failed to retrieve it, answered **20** from training data, and
prefaced it with *"Based on the Google Play support page."* Nothing in the prose
marked the difference. The retrieval-status field did.

## previous-session review

`2026-08-05-play-submission-requirements.md` (PR #743, merged) recorded the Play
requirements with fetched sources and filed six `OQ-PLAY-*` items. The owner then
supplied three corrections that reshaped the plan: the developer account is
already created and paid; the game **does** retain run data; and leaderboards will
eventually send data off device. He also directed this benchmark.

## What landed

- `docs/findings/2026-08-05-gemini-url-accuracy-benchmark.md` — the ten-URL
  measurement, scored against pages fetched by hand first.
- `docs/providers/gemini.md` — `url_context` row corrected: it is host-dependent.
- `docs/owner-queue.md` — `OQ-PLAY-ACCOUNT` closed; `OQ-PLAY-LISTING` promoted to
  the critical path; `OQ-PLAY-CLOSED-TEST` corrected on two counts.
- `menno420/spider-swing` PR #163 — privacy policy draft, Console answer sheet,
  listing copy, closed-test runbook, upload-key script.

## Measured

**The benchmark**, ten URLs, ground truth established by hand first:

| | |
|---|---|
| `url_context` retrieval, `support.google.com` | **0 / 8** |
| `url_context` retrieval, `developer.android.com` | **2 / 2** |
| Correct **and** retrieved | 2 |
| Correct from memory after a failed fetch | 3 |
| False negatives ("NOT ON PAGE" when the page states it) | 2 |
| **Materially wrong** | **2** |
| Blocked calls that admitted being blocked | **1 of 8** |

The two wrong ones: **"at least 20 testers"** where the page says 12, and the
upload-key page scored *"NOT ON PAGE"* for a key size it states (RSA ≥2048) plus
an outdated reset route (*"contact Google Play support"* — it is self-serve in
Console now).

**The same question, two tools, same model and key, one hour apart:**

| Tool | Answer | Correct |
|---|---|---|
| `google_search` grounding | 12, *and* volunteered the 20→12 history | ✅ |
| `url_context`, retrieval failed | 20 | ❌ |

That is the finding. Not "Gemini is unreliable" — on the two pages it could
actually read it was accurate and complete, and the search-grounded pass was
right on everything later confirmed by hand. The failure is mechanical and
host-shaped, and it is invisible in the prose.

**Two instruments, both cheap, both caught real errors on first use:**
`urlContextMetadata.urlMetadata[].urlRetrievalStatus` for `url_context`, and
`groundingMetadata.groundingChunks` for search grounding — an empty chunk list
marked exactly the two answers earlier that day that were memory rather than
search.

**Three owner corrections, each of which changed an artefact:**

1. The developer account exists — `OQ-PLAY-ACCOUNT` closed, and the critical
   path moves to the listing.
2. The game retains run data — but `game/` has **no** network API of any kind and
   every write goes to `user://`, and Google defines *collect* as transmitting
   **off** the device. So the Data safety answer is "no data collected" and the
   owner's statement is also true. Different questions.
3. Leaderboards will eventually transmit — so the accurate declaration ships now
   and the leaderboard release carries a hard gate, rather than pre-declaring
   collection that would itself be false today.

## Verification

- `python3 tools/check_no_false_walls.py --strict` → **exit 0**, CLEAN across 5
  living/binding docs. Real exit code, not `$?` after a pipe.
- `python3 bootstrap.py check --strict` → **exit 0** with the born-red hold
  cleared by this commit.
- Benchmark scoring is against pages **this session fetched itself before**
  asking Gemini, so ground truth was not itself model output.
- spider-swing PR #163 carries the buildable half; its gates are recorded on its
  own card.

**Honest nulls:** sample is ten URLs, one model, one day — no broader claim about
the provider is warranted. Tester opt-in/opt-out mechanics beyond the URL format
remain unverified. Whether a published store name can be freely changed is
believed yes and unconfirmed. Everything about Play Games Services is still
unresearched, and `android-release.yml` still has never run end to end.
