# 2026-08-05 · hub — sync the queue to the decided name

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/swingy-spider-play-submission-wno3nb`

💡 Session idea: **the queue was still asking a question the owner had already
answered.** `OQ-SWINGY-NAME` read as open, and `OQ-PLAY-APP-ID` still recommended
`com.menno420.swingyspider` — an identifier derived from a name ruled out hours
earlier for being taken. The owner is about to type a **permanent** package name
into Play Console, so a stale recommendation in the one document he consults for
owner-only steps was not a tidiness problem.

## previous-session review

PR #749 corrected the Gemini benchmark. Since then the naming work landed across
spider-swing #164–#167: "Swingy Spider" ruled out, "Slingy Spider" decided, and
the provenance recorded. The hub's queue had not caught up.

## What landed

- `docs/owner-queue.md` — `OQ-SWINGY-NAME` resolved to **Slingy Spider** with the
  evidence and the one remaining open item (trademark: BOIP + EUIPO, Nice 9/41).
- `docs/owner-queue.md` — `OQ-PLAY-APP-ID` corrected to
  **`com.menno420.slingyspider`**, with the note that newer Play Console asks for
  the package name on the *Create app* form rather than at first upload, so it is
  fixed at creation alongside the equally permanent free-vs-paid choice.

## Measured

**The drift, found by grep rather than by memory:** two live references to
`com.menno420.swingyspider` in the owner queue, plus an `OQ-SWINGY-NAME` entry
still phrased as an open question. The same sweep in spider-swing found two more
in the closed-test runbook, fixed in that repo's PR.

A stale identifier is a different class of error from a stale note. The owner was
mid-way through the Play Console **Create app** form when this was caught, and
the package name on that form is permanent and non-reusable. A recommendation
carrying the ruled-out name would have been typed into the one field that cannot
be undone.

## Verification

- `python3 tools/check_no_false_walls.py --strict` → **exit 0**.
- `python3 bootstrap.py check --strict` → **exit 0**, run **post-commit**.
- Drift located by `grep -rn "swingyspider"` across both repositories rather than
  by recalling where the name had been written.

**Honest null:** the trademark step (BOIP, EUIPO, Nice 9/41) is untouched and
remains the only open item on the name.
