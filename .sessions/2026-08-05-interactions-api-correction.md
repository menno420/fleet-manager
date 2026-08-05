# 2026-08-05 · hub — repudiate a false wall I wrote three hours ago

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: I trusted a **machine-readable API discovery document** over the
repo's own measured record, and concluded an endpoint did not exist because the
spec did not list it. A spec feels more authoritative than prose, which made it
more dangerous than prose — the same failure as every other one today, wearing
better clothes.

## Previous-session review

Hours earlier this session added **step 0** to the DISCOVERY RULE: an owner
statement about provisioning is verified evidence, act on it. The owner then
said a previous session had used the Interactions API successfully. Step 0
should have ended the matter instantly. Instead the wall was already written.
**The rule I authored today did not bind me today.**

## What landed

- `docs/CAPABILITIES.md` — a repudiation of tonight's own entry, with the
  working recipe.
- `docs/findings/2026-08-05-foundation-continuation.md` — § 7 honest null
  corrected; it claimed the API "could not be used".

## Measured — it works, on a free key, exactly as documented

`POST https://generativelanguage.googleapis.com/v1beta/interactions?key=$GEMINI_API_KEY`

```json
{"model": "gemini-3.1-flash-lite", "input": "…",
 "previous_interaction_id": "<id from the prior turn>"}
```

A/B, this session, `gemini-3.1-flash-lite`:

| Turn | Result |
|---|---|
| 1 — "Remember 8891" | `noted.` · id `v1_ChcwN1Z6YXZlNEpl…` |
| 2 **with** `previous_interaction_id` | **`8891`** |
| 2 **without** it (control) | *"You haven't asked me to remember a number yet."* |

Response text is at **`steps[] → type == "model_output" → content[].text`**, not
`outputs[]`. Fields are **snake_case**; the object reports `"object":
"interaction"`.

## Why the probe missed it

Four things, and each one was individually reasonable:

1. **Wrong surface.** I searched Vertex first, per the Vertex-first directive.
   Vertex *does* expose `interactions:create` under
   `projects/{p}/locations/{loc}/` and it returns `RESOURCE_PROJECT_INVALID` for
   this project — a real result that made "preview allowlist" feel settled.
2. **Wrong shape.** The AI Studio endpoint is a **flat collection** —
   `POST /v1beta/interactions` — with flat `model`/`input`, not Vertex's nested
   `interaction.stringContent` + `modelInteraction.model`.
3. **The discovery document omits it.** I fetched
   `generativelanguage.googleapis.com/$discovery/rest` at `v1beta` **and**
   `v1alpha`, both HTTP 200, and searched every method name and path for
   "interaction". **Zero hits.** The endpoint exists anyway. The spec is
   incomplete, and I read absence-from-spec as absence.
4. **I never read `docs/providers/gemini.md`.** It has said since this morning:
   *"`POST /v1beta/interactions` is reachable on a free key and accepts
   `previous_interaction_id`"* — with its own A/B using the number 4712, which
   is the same test I then reinvented with 8891.

## Verification

- `python3 tools/check_no_false_walls.py --strict` → **exit 0**.
- `python3 bootstrap.py check --strict` → **exit 0**, run **post-commit**.
- The A/B above is reproducible and costs nothing: free key, `flash-lite`,
  three calls.

**Honest nulls.** Retention (**1 day free / 55 paid**) is `MEASURED-PRIOR` from
`providers/gemini.md`, not re-checked here. Whether Vertex's
`RESOURCE_PROJECT_INVALID` is genuinely an allowlist stays **unproven** — it is
now simply irrelevant, because the working path is elsewhere. Free-tier RPD is
the real constraint: **20/day** on `gemini-3.6-flash`, 500 on flash-lite.

## ⟲ Previous-session review

See above — the rule this session wrote is the rule this session broke, twice
now (the dependabot landing rule earlier, step 0 here). Both times the rule was
correct, recent, and authored by me. **A rule does not bind its author any more
than it binds a stranger**, which is the strongest argument yet that the estate's
prose-versus-mechanism split is the thing that matters.

## ⚠ Correction, appended later the same day — this card names the wrong root cause

The owner read the account above and pointed out what it misses. The four
reasons below are all true and all **second-order**. The first-order failure is
not in the list:

> *"That one of my requests or statements should not be seen as only plausible
> but as source truth. You broke that rule by writing down the wall about the
> Interactions API without searching for any documents about it."*

**He had already told me it works — in the task message that started the
work:** *"the new 'createinteraction/interaction API' works fully turn based and
stored session history for a short time."* The wall was written after that, and
it contradicted him directly. The doc I skipped would have caught it, but I
should not have needed the doc.

Reason 4 below — *"I never read `docs/providers/gemini.md`"* — is therefore the
**recovery** that failed, not the cause. The cause is that a probe of one
surface was allowed to overturn a statement from the person who built the
estate. And the version of step 0 written earlier that same day is what
permitted it: it scoped his authority to *provisioning*, so *"the Interactions
API keeps turn-based history"* filed as a behaviour claim, and behaviour claims
looked overturnable by measurement.

Fixed 2026-08-05 in `docs/CAPABILITIES.md` § THE DISCOVERY RULE step 0 and in
`.claude/CLAUDE.md`: the boundary is **not** provisioning-versus-behaviour. A
probe establishes only what that one call did; **a failure means you took the
wrong path, not that he was wrong.** The `recording-a-wall` route in
`.claude/hooks/doc-routes.json` now fires on any edit that writes limitation-
shaped prose, carrying this example with it.

## 💡 Session idea

**Grep the estate before probing an API.** Every failed probe tonight was
preceded by a document in this repo that already had the answer — and the
delegation tooling exists precisely to make that search cheap. A one-line
pre-probe habit — `grep -rn "<endpoint or feature>" docs/` — would have replaced
forty minutes of Vertex archaeology with one hit on `providers/gemini.md:151`.
Worth promoting into `capability-probe` as step 0 of that skill, mirroring the
step 0 added to the DISCOVERY RULE today: **check what the estate already
measured before you measure it again.**
