# Gemini routing — the free key is the route; Vertex retired 2026-08-29

> **Status:** `binding` — this header carries the current rule; everything
> below it is the credit-era record, kept because the recipes and billing
> chain stay true as history and revive if he ever re-funds the credit.
>
> **Owner directive, live, 2026-08-29:** *"the paid/vertex route does not work
> anymore since the free credits timed out a few days ago"* — use the **free**
> `GEMINI_API_KEY`. This supersedes the 2026-08-05 Vertex-first directive
> below by its own exit clause (*"if credit runs out … re-read this page"* —
> §Scope): the credit that made Vertex the free path is gone, so Vertex now
> either fails or would bill differently, and the owner has ruled the route
> off rather than asked for a probe.
>
> **The current rule:** free `GEMINI_API_KEY` for everything it serves —
> including the mid-session review work the same sitting assigned to Gemini
> ([D-0019]). `GEMINI_API_KEY_PAID` still bills **the owner's card**; Deep
> Research remains its one documented exception (below), everything else
> needs his say-so, stated in the session card. **Model ids for this key
> class, `MEASURED` 2026-08-29:** `gemini-3.6-flash` works on
> `generateContent`; the `gemini-2.5-*` ids are still listed by `/models` but
> 404 with *"no longer available to new users — use models/gemini-3.6-flash"*.
> Route decision record: [`../decisions.md`](../decisions.md) [D-0020].

---

## The credit-era record below (2026-08-05 → 2026-08-29)

# Default to Vertex for all Gemini work *(superseded 2026-08-29 — header above)*

> **Owner directive, 2026-08-05: every session defaults to Vertex AI for Gemini
> calls — at least for the rest of this month.** Not a preference. Vertex spends
> a credit balance already paid for that expires unused, while the **paid** AI
> Studio key spends the owner's card. Note "the AI Studio key" is two keys —
> `GEMINI_API_KEY` is free tier and costs nothing; see the next section, which
> exists because this header used to say it in the singular.
>
> The whole route was verified end to end in the session that wrote this, from a
> container with no Google credentials in its environment.

## Two identities, three billing outcomes (corrected 2026-08-06)

This document originally described "two paths" and named only the paid AI Studio
key. The environment carries **two distinct AI Studio keys**, and collapsing them
cost real reach: a session reading either this doc or the boot file learned only
*"AI Studio spends the owner's card"* and avoided the whole surface — **including
the free one.**

**It is two identities, and the paid one has two routes that bill differently.**
That is the part worth internalising — *the route decides who pays, not the key.*

| identity | route | who pays | binding constraint |
|---|---|---|---|
| **`GEMINI_API_KEY`** — free tier | AI Studio (`generativelanguage`) | **nobody** | hard **requests-per-day** caps: ~20/day flagship Flash, 500/day Flash Lite ([`../providers/gemini.md`](../providers/gemini.md)) |
| **the paid GCP project** — SA from Railway | **Vertex** (`aiplatform`) | the **prepaid credit**, €245.23 left (2026-08-06) | no RPD cliff; **no server-side conversation history** |
| **the paid GCP project** — `GEMINI_API_KEY_PAID` | AI Studio (`generativelanguage`) | **the owner's card** | none — and that is the problem |

Rows 2 and 3 are the **same billing project**. The credit
[excludes the "Gemini API in AI Studio" SKU](#why--the-paths-are-funded-differently)
and does not exclude Vertex, so the identical project is credit-funded on one
host and card-funded on the other. Owner, 2026-08-06:

> *"Vertex is only available on the paid key, which uses the $300 of free
> credits when routed through Vertex. But uses my own personal credit when
> directly invoking the Gemini API."*

Measured 2026-08-06: the two env vars are genuinely different values (53 vs 39
chars), not one key under two names.

**So `generativelanguage` is not one thing.** Hitting it with
`GEMINI_API_KEY` costs nothing; hitting it with `GEMINI_API_KEY_PAID` bills the
card. Any AI Studio call — the Interactions API included — should carry the
**free** key unless its daily cap is genuinely in the way.

**What this changes in practice.** The free key is not merely "the cheap
option" — it is the only path that serves the **Interactions API**
(`POST /v1beta/interactions` + `previous_interaction_id`, server-side history,
verified on it). Vertex's `interactions:create` returned
`RESOURCE_PROJECT_INVALID` for this project, so Vertex conversations carry their
transcript client-side and resend it every turn — token cost that grows
quadratically with turns.

So for a **long** multi-turn exchange the free key is both cheaper *and* more
token-efficient than Vertex, bounded only by requests-per-day. For **volume,
image or video work**, Vertex, because 20 requests/day is the real ceiling on
the free tier and it is the binding one — not the token meter.

## Why — the paths are funded differently

**Read the console's vocabulary literally** (owner, 2026-08-06): **"cost"
means his actual money. "Credits" means the free-trial balance.** They are
separate lines in the billing view and only one of them is a bill.

Measured from the owner's Cloud console — console-UI-only data no session can
read, recorded because he supplied it. Two dates, because the trend is the
point:

| | 2026-08-05 | 2026-08-06 | delta |
|---|---|---|---|
| **Cost — real money, month to date** | **€0.49** | **€7.88** | **+€7.39 (~16×)** |
| Credit consumed this month | €5.15 | €11.29 | +€6.14 |
| Credit remaining | €251.37 | €245.23 | of €256.52 |
| Forecast end-of-month cost | €0.00 | €0.00 | unchanged |

**The forecast is not reassurance.** It read €0.00 on both days while the
real-money line grew sixteen-fold — it forecasts *additional* cost, not the
total already accrued.

Credit movement is expected: that is Vertex work. Real-money movement can only
be the AI Studio SKU on `GEMINI_API_KEY_PAID`, since Vertex draws credit and
`GEMINI_API_KEY` draws nothing. Attribution by SKU is not readable from a
session — console or a BigQuery billing export only — so a session that suspects
it caused spend should say what it ran, not guess at a figure.

**That +€7.39 was correct spend, not a routing mistake.** Owner, 2026-08-06: it
came from **Deep Research**, which **is not available through Vertex at all and
is not served on the free key either.** So the paid AI Studio key was the only
path in existence for it. Recorded because the obvious inference from a
real-money jump — "a session took the expensive route again" — is wrong here,
and would have a future session hunting a habit that does not exist.

### The documented exception

| task | why the paid key is the only option |
|---|---|
| **Deep Research** | not on Vertex, not on the free tier — owner-verified 2026-08-06 |

The rule below says reach for `GEMINI_API_KEY_PAID` *"only when Vertex has
actually failed."* Deep Research is not a failure case: **Vertex was never an
option.** Use the paid key without hesitation, note it in the session card, and
do not spend a turn looking for a Vertex route that does not exist.

The €256.52 is the $300 Google Cloud welcome credit denominated in EUR. It
**excludes "Gemini API in AI Studio"** — verbatim from the billing dialog — and
does **not** exclude Vertex AI, which serves the identical Gemini models.
Eligibility keys on the SKU, not the model.

So the same prompt, to the same model, is free on one path and billed on the
other. There is no quality trade-off to weigh: **the credit-funded path is also
the one that returns lossless PNG for image work.**

This closes a null that stood in `providers/gemini.md`: *"whether the credit or
the card pays… is inference until read there."* It is now read.

## The rule

**Use Vertex.** Reach for `GEMINI_API_KEY_PAID` only when Vertex has actually
failed for the task in hand, and say so in the session card when you do.

The session that produced this directive spent €0.49-ish of card money on 21
text calls that Vertex would have covered from credit — small in absolute terms,
and exactly the habit worth killing before an image or video batch makes it
expensive.

## The route, verified 2026-08-05

No Google credential exists in the session environment — `GEMINI_VERTEX_SA_JSON`,
`GOOGLE_APPLICATION_CREDENTIALS`, `GCP_SA_JSON` and `GOOGLE_CLOUD_PROJECT` are
all absent. The service account lives in **Railway**, and `$RAILWAY_API_KEY` is
present, so the route is: **Railway → service-account JSON → OAuth → Vertex.**

### 1. Pull the service account from Railway

Railway's GraphQL API at `https://backboard.railway.com/graphql/v2`, over direct
egress. **`projects` at the top level returns an empty list** — the projects hang
off the workspace, which is the one non-obvious step:

```graphql
query { me { workspaces { id name team { projects { edges { node { id name } } } } } } }
```

Then, for `reliable-grace` / `worker` / `production`:

```graphql
query($p:String!,$e:String!,$s:String!){ variables(projectId:$p, environmentId:$e, serviceId:$s) }
```

| | |
|---|---|
| project `reliable-grace` | `285dfbcd-0ba7-42a5-ba87-6d85263a0a37` |
| service `worker` | `eac6b498-6db7-420e-9d0b-a625941c6504` |
| environment `production` | `429efe45-7995-4046-91ce-1886692c33a7` |
| variable | `GEMINI_VERTEX_SA_JSON` (2,420 chars) |

`variables` returns plaintext values. **Never write the JSON anywhere inside a
repository, and never print it.** Hold it in memory, or in a mode-600 file
outside the tree that you delete when finished.

### 2. Authenticate and call

`pip install google-auth cffi` first — neither is present by default, and the
container's system `cryptography` needs `cffi`.

```python
from google.oauth2 import service_account
from google.auth.transport.requests import Request as GRequest
import requests

creds = service_account.Credentials.from_service_account_info(
    info, scopes=["https://www.googleapis.com/auth/cloud-platform"])
sess = requests.Session(); sess.trust_env = False
sess.verify = "/root/.ccr/ca-bundle.crt"      # direct egress, not the proxy
creds.refresh(GRequest(session=sess))

url = (f"https://aiplatform.googleapis.com/v1/projects/{PROJECT}/locations/global/"
       f"publishers/google/models/gemini-3.1-pro-preview:generateContent")
```

API keys are rejected by Vertex (*"API keys are not supported by this API"*) —
it is OAuth or nothing.

### 3. Grounding uses a different key name

**On Vertex the tool is `googleSearch` (camelCase), not `google_search`.**

```json
{"tools": [{"googleSearch": {}}]}
```

Verified: HTTP 200, **5 grounding chunks**, and the answer matched a
hand-verified ground truth (12 testers / 14 consecutive days — the exact fact
that `url_context` on the AI Studio path got wrong an hour earlier; see
[`../findings/2026-08-05-gemini-url-accuracy-benchmark.md`](../findings/2026-08-05-gemini-url-accuracy-benchmark.md)).

### 4. Confirm the money lands on the credit

```
GET https://cloudbilling.googleapis.com/v1/projects/{PROJECT}/billingInfo
```

Verified chain, 2026-08-05:

| | |
|---|---|
| SA | `vertex-sessions-83@project-a8d37219-aa51-4350-90d.iam.gserviceaccount.com` |
| Project | `project-a8d37219-aa51-4350-90d` |
| Billing account | `01161F-0357D6-33069D` — **"My Billing Account"**, EUR, open |

That is the same account carrying the €251.37 credit in the owner's console. The
chain from service account to credit balance is complete and checked, not assumed.

## What is still not readable from a session

**Cost and credit balance.** The Cloud Billing API exposes *structure* — account,
open state, currency, linked projects — and there is **no cost or credit-balance
endpoint**. The figures at the top of this page came from the owner's screenshots.
Any session claim about how much credit remains is inference unless he supplies a
fresh reading or a BigQuery export exists.

## Scope of the directive

The owner said *"at least this month"*. Treat Vertex-first as binding until he
says otherwise; if credit runs out or the month turns, re-read this page and ask
rather than silently reverting to the card.
