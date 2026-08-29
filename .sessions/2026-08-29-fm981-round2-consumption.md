# 2026-08-29 — consuming the fm #981 review round that landed after the flip

> **Status:** `in-progress` — born-red. fm #981's full Codex review (six
> inline findings, reviewed commit `0181391`) landed at `21:49:31Z` — three
> minutes after the 21:46 issue comment this session had taken as the whole
> verdict — and the PR merged before they were read. This PR consumes them:
> every finding measured against merged `main`, the confirmed ones fixed.

- **📊 Model:** withheld · max · runtime bugfix
- **⚑ Model-slot note:** harness policy forbids a model identifier in a pushed
  artifact; effort and task class are exact.
- **📍 Venue:** cloud-container (owner-live)

## Mission

Same conversation as fm #978/#981. The capture PR merged on a partial read of
its own review: the 21:46 comment was Codex's *delivery-status* half (its
sandbox had no remote, so it described two findings in prose), and the review
object with six inline findings arrived at 21:49 on the same head. Findings 1
and 2 were already fixed by `73f0396` before the merge; the other four name
surfaces that commit never touched. This session measured all six against
merged `main` and fixes what held.

## Dispositions, measured before fixed

| # | finding (file) | measured | disposition |
|---|---|---|---|
| F3 | D-0019's "single round lands on the head that flips" cannot hold when the round's own findings force fixes (decisions.md) | real tension — both fm #978 and #981 flipped on the answered verdict + Gemini-verified fixes | **[partial]** — the worked rule exists but is unrecorded; put to the owner in chat (his directive to amend, not mine) |
| F4 | live delivery surfaces still inject the retired route | CONFIRMED ×3: `doc-routes.json` gemini `says` ("Vertex for volume, image and video"); `owner_review.py` `_review` falls through to Vertex on free-tier failure — with the credit gone that would bill the card; boot file §decisions "the Vertex-first convention still decides the *route*" | **[conceded]** — all three fixed; the hook now fails open on free-tier failure (no enrichment that turn; the fixed question still fires) |
| F5 | D-0011's own amendments still prescribe Vertex routing | CONFIRMED at decisions.md (2026-08-11 and 2026-08-28 amendment blocks) | **[conceded]** — dated 2026-08-29 amendment added: route halves superseded by D-0020, spend authorisation untouched |
| F6 | "**Use Vertex.**" survives as an unqualified imperative under the marked heading | CONFIRMED — the sentence itself is the greppable string | **[conceded]** — inline marker on the sentence |
| F7 | provider body still says "prefer Vertex" (L274) and "still Vertex-first" (L304-306) | half-CONFIRMED: L304-306 was already fixed by `73f0396` (Codex reviewed the pre-fix head); L274 stood | **[partial]** — L274 marked credit-era; PNG-vs-JPEG fact kept, with the honest null that no surviving route is measured for PNG |
| F9 | "the `gemini-2.5-*` ids 404" generalizes one probed id to a class | CONFIRMED — only `gemini-2.5-flash` was probed; TRAP-004's exact shape | **[conceded]** — narrowed on all five surfaces (CAPABILITIES gets a ⚠ marker per its append-never-edit rule, not a rewrite) |
| F8 | the #981 card's previous-session review was same-conversation | CONFIRMED — the card says so itself | **[partial]** — deliberate and labelled, but the contract wants cross-session review; this card reviews a genuinely previous session below |

**Left deliberately:** `docs/audits/2026-08-10-full-read/raw/adjudication.jsonl`
still carries the old "Use Vertex" sentence — raw audit evidence quoting what
the doc said on 2026-08-10; record tier, editing it would corrupt the audit.
The copy-check hook flagged it; this line is the disposition.

## Verify

- `python3 -m py_compile .claude/hooks/owner_review.py` → compiles; no live
  references to the retired Vertex helpers remain (grep).
- `python3 bootstrap.py check --strict` → real exit code, no pipe; born-red on
  this card until the flip.
- Fix diff verified on the free-key Gemini route per D-0019 before the flip.

## ⟲ Previous-session review

Previous card:
[`2026-08-29-codex-trigger-and-model-slot.md`](2026-08-29-codex-trigger-and-model-slot.md)
(a genuinely different conversation — read whole). **Held up:** its five-copy
sweep is exactly the discipline this PR needed tonight (the retired route
survived in a hook, a routing table, and a boot-file line the first fix
missed); its "the summary comment is edited in place — not an instrument"
finding directly explains tonight's trap, where the first Codex surface to
arrive read as the whole verdict. **What it left open that bit tonight:** it
measured *when* Codex answers but not that the answer arrives in **two parts**
(issue comment ≠ review object) — the gap this card's session idea names.

## 💡 Session idea

**A Codex verdict is two surfaces, and the first to arrive is not the
verdict.** Tonight the delivery-status issue comment (21:46) read as the whole
answer; the review object with six inline findings landed at 21:49 — same
head, three minutes later — and the PR merged before they were read. The boot
file already warns "a summary that looks empty is not an empty review"; the
sharper rule is *wait for the review object (or the 👍 reaction) before
treating any comment as the verdict, and read `/pulls/{n}/comments` after it
exists*. Candidate for the boot file's @codex bullet once the owner confirms
the cadence question this session put to him (F3).
