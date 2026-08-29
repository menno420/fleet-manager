# 2026-08-29 — capture of two live owner directives: review cadence and the Gemini route

> **Status:** `complete` — the records half of directives given live in the
> audits-review session (same conversation as fm #978), landed as its own
> small PR under the owner's mid-planning carve-out: small, ready, and not a
> surface the plan is deliberating. Flipped after the flip-readiness Codex
> round answered and both its findings were fixed and Gemini-verified —
> [D-0019]'s cadence worked end to end on the PR that records it.

- **📊 Model:** withheld · max · docs-only
- **⚑ Model-slot note:** harness policy forbids a model identifier in a pushed
  artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container (owner-live)

## Mission

Two directives existed only in chat — the loss mode this estate keeps writing
findings about (gap #8, owner-words capture):

1. **Review cadence:** Codex reserved for flip-readiness and real important
   changes; mid-session verification on the free-key Gemini route. →
   **[D-0019]**.
2. **Gemini route:** *"the paid/vertex route does not work anymore since the
   free credits timed out a few days ago"* — the free `GEMINI_API_KEY` is the
   route. → **[D-0020]**, taken as source truth, not probed.

Plus one measurement made while executing directive 1 for the first time: the
free key's working model id is `gemini-3.6-flash`; the `gemini-2.5-*` ids are
listed by `/models` but refuse new users on `generateContent`.

## Shipped

- `docs/decisions.md` — **[D-0019]** and **[D-0020]**, his words verbatim,
  authority-labelled, each with its rules-out.
- `docs/conventions/vertex-first-for-gemini.md` — supersession header carrying
  the current rule; the credit-era record kept whole below it (its own §Scope
  exit clause — *"if credit runs out … re-read this page and ask"* — is the
  clause his directive answers).
- `docs/providers/gemini.md` — banner rewritten to the current route + the
  measured model-id fact.
- `.claude/CLAUDE.md` — the Gemini bullet rewritten; the @codex bullet gains
  the cadence paragraph.
- `docs/CAPABILITIES.md` — one append-log entry (the model-id measurement,
  `owner-live` venue, verbatim evidence).

## Verify

- The Gemini call evidence is this session's own run (200/STOP/8504 tokens on
  the fm #978 round-2 fix review; the 2.5 404 body quoted verbatim).
- `python3 bootstrap.py check --strict` → real exit code, no pipe; born-red on
  this card until the flip.

## ⟲ Previous-session review

Previous card:
[`2026-08-29-audits-review-fleet-preflight-dissection.md`](2026-08-29-audits-review-fleet-preflight-dissection.md)
(fm #978, merged this hour — same conversation, so this is a same-session
review at arm's length). **Held up:** its two Codex rounds and the Gemini
mid-check are accurately recorded, and its numbers were re-derived before
each disposition. **What it left implicit, which this card makes explicit:**
the cadence it executed under ("owner directive, applied from round 2
onward") existed in no committed record — exactly the class this PR closes.

## ⚖ Flip-readiness review (Codex on 0181391, per [D-0019])

Requested 21:42:06Z, answered 21:46Z as an issue comment (its sandbox had no
remote or token, so its prepared diff stayed there — findings only):

1. **Live-sounding Vertex imperatives survived in the credit-era record**
   (*"For volume, image or video work, Vertex"*; *"## The rule — Use
   Vertex"*). Measured: both present as cited. **[conceded]** — inline
   supersession markers added at both spots, plus one on the §Scope exit
   clause the header quotes.
2. **[D-0020] over-revoked [D-0011]**: my *"anything else needs his say-so"*
   contradicted D-0011's verdict — *"spend without asking … no approval
   step"* — which the 2026-08-28 amendment explicitly kept standing. The
   owner's words retire a **route**, not that authorization. Measured against
   the verdict text. **[conceded]** — reconciled on all four surfaces
   (decisions rules-out, conventions header, boot file, provider banner +
   body): free key first; paid key when the free key cannot serve, no
   ask-gate, disclosure in the card.
3. Codex could not verify the [D-0019] quotation (the chat behind it is not
   in the PR context). **[survived]** — the transcript is the source and this
   session its witness; owner-verbatim is the strongest provenance a live
   directive has.

Fix diff verified on the free-key route (`gemini-3.6-flash`, 200/STOP):
both findings **RESOLVED**, no new issues, four surfaces confirmed aligned.

## 💡 Session idea

**A supersession header should quote the exit clause it exercises.** The
Vertex-first doc anticipated its own retirement condition in §Scope; tonight's
supersession quotes that clause as its authority, which made the correction
uncontestable. Candidate convention for any `binding` doc: name the condition
under which it stops binding, so the session that meets the condition can
retire it by citation instead of by argument. (An idea for the revised plan's
records track, not an action — and it fits the demand-structure discussion:
a rule that names its own red is the falsifiable form.)
