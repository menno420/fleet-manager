# Owner direction, 2026-08-26 — verbatim, with what is and is not a directive

> **Status:** `reference` · 2026-08-26 · `OWNER` throughout unless marked.
>
> **What this is:** his words from the hub chat, kept verbatim so the directives
> that derive from them can be checked against the source. Same job as
> [`2026-08-22-owner-direction.md`](2026-08-22-owner-direction.md) and
> [`2026-08-23-owner-direction.md`](2026-08-23-owner-direction.md).
>
> **What it is NOT:** a queue. The only owner-gated item here is already filed;
> everything else is direction or correction.

## 1 · The local-work section — his design, which differs from what was built

He opened the day asking how well a cloud session understands what his local
sessions have been doing. [`../activity/`](../activity/README.md) was built that
morning (fm #947). He then described the shape he actually wanted, and it is
**not** the shape that was built:

> *"Just create a seperate section in fleet-manager for the local work, just
> like how each repo is mentioned with some explanation, the one drive should
> get the same treatment. If things have only been done locally, so on the
> laptop or any of my accounts unrelated to direct repo work. That should be
> clearly explained in fleet manager, but if the local sessions do repo work,
> that should just be documented in the repo they worked at, tho with some
> extra explanation that they worked as a local session."*

> *"The main goal of this is to make sure that any agent has the ability to find
> out the same things. The local agents can all view my github, so the main
> problem is to make the local agents known to the cloud agents. Which could be
> helpfull if I have done certain preparations on my laptop and want to continue
> in the cloud."*

**What matched what was built:** the split rule exactly — local-only work
explained in fleet-manager, repo work documented in its own repo carrying an
extra marker saying a local session did it. That is `off-repo-log.md` plus the
`📍 Venue:` token, both landed in fm #947.

**What did not match, and is still to do.** `DERIVED` from his *"just like how
each repo is mentioned"*: he is describing the **`docs/repos/` shape — a page
per surface, explaining what it is and where it got to** — and what exists is a
**chronological log**. A log answers *"what happened Tuesday"*; his shape answers
*"what is the state of the laptop right now, before I continue in the cloud."*
His stated use case needs the second. Planned pages: the laptop · OneDrive ·
Google Drive · other accounts as they matter, each carrying *what it is · what
is on it · current state · what to know before continuing · last checked*.

**He is executing this himself, locally, later** — stated 2026-08-26. A session
should not pre-empt it; this entry exists so his execution has a written target
rather than a chat message. **Clarified 2026-08-27→28, and the current word
lives there:** *"himself"* meant *via local sessions* (*"they have the full
ability to work on both sides and see everything"*), the pages carry a lean
history as well as state, and execution waits on his explicit GO —
[`2026-08-28-owner-direction.md`](2026-08-28-owner-direction.md) §§ 2–4. This
paragraph stays as the record of what he said on 2026-08-26.

### 1b · Two drives, and both were already in the tree

`MEASURED` 2026-08-26 — the answer to *"which drive did he mean"* turned out to
be **both**, and the repo already knew about each:

| surface | what it is | where the repo already records it |
|---|---|---|
| **OneDrive** | his **laptop hub**. `Hub/journal.md` on it *"carries the build-session narrative"* | [`../repos/spider-bot/README.md`](../repos/spider-bot/README.md) line 107 |
| **Google Drive** | the media dropbox sessions already read — gameplay captures, cover art; exists because images pasted into chat never become real files | [`../conventions/owner-drive-folder.md`](../conventions/owner-drive-folder.md) |

**`Hub/journal.md` is the sharp end.** A record of his local work already
exists, on his machine, and no cloud agent can read it. **Open question, his to
answer:** whether a local session copies it into fleet-manager, or the OneDrive
folder is shared the way the Google one is. *(Settled differently
2026-08-27→28: hub-local sessions keep a lean account in fleet-manager's local
section, so neither copy nor share is the path —
[`2026-08-28-owner-direction.md`](2026-08-28-owner-direction.md) §§ 2–3, and
`OQ-ONEDRIVE-HUB` is rescoped to housekeeping.)*

## 2 · The website as his review surface — became OD-21

> *"my idea for this is mostly the website, allowing me to leave a comment
> wherever I feel like the agents did not understand my intent or their tasks
> properly etc. And it gives me an easy way to look at what I think is important
> in each repo while the agent works, so I can also have visual confirmation
> about what I believe to be true."*

> *"Ideally every repo should be featured and have multiple subsections under
> it, so I can see things like the claude.md, the reading order, summaries of
> certain files etc. I do not want this to be a direct clone of a repo, because
> it needs to be easy for me to see and review aswell as easy to leave comments
> or make edits."*

> *"once this is all more orderly, I intend to have more in depth conversations
> with multiple claude sessions to really take my time and map out the proper
> intent and goals of each repo."*

Recorded as **OD-21**; the design derived from it is
[the legibility plan](../planning/2026-08-26-legibility-and-intent-plan.md), and
**the design is `DERIVED`, not his** — which OD-21 states explicitly after
`@codex` caught an earlier version attributing it to him.

## 3 · Codex does NOT boot blind — an owner correction, and this session proves it

He corrected a claim made in this chat, and the correction stands:

> *"One small note I want to make about codex, you say it boots blind, but thats
> not true. And I should probably even mention that codex/chatgpt probably reads
> the documents better than claude does at this moment."*

> *"Tho I can't say this for sure, since I still use claude for most of the
> things, I did notice that recently chatGPT has been very reliable whether it's
> execution work or documentation."*

> *"Tho a dedicated agents.md is still probably a good idea."*

**Read the hedge, per [`../CAPABILITIES.md`](../CAPABILITIES.md) § step 0.** The
**unhedged** half is the correction — *"you say it boots blind, that's not
true"* — and it is source truth. The **hedged** half is the comparison with
Claude (*"probably"*, *"I can't say this for sure"*), which is an impression
worth checking rather than a measurement.

**`MEASURED` in this session's own PR reviews, and it settles the unhedged
half.** Across five rounds on fm #947 and one on fm #949, `@codex` cited files
**nothing routed it to**:

- `docs/repos/substrate-kit/README.md` lines 49 and 51 — to contradict a
  kit-version census, naming `pokemon-mod-lab` and `sim-lab` at v1.15.0;
- the consolidation program's **2026-08-24** row, to show that its own
  **2026-08-23** traffic figures had been retracted;
- `bootstrap.py`'s `ensure_draft` / `_hook_stopcheck`, to show the kit
  auto-drafts a missing session card — which broke a causal claim;
- `.sessions/2026-07-23-hub-forge-slice4-handoff.md` **and** `-landed.md`, to
  show one session can land two cards.

**A session that reads the program's correcting row, the kit engine's internals
and a two-year-old card pair is not blind.** *No auto-loaded boot file* and
*blind* are different claims, and this estate had been writing the second while
measuring only the first.

**Corrected in place:** [`../execution-surfaces.md`](../execution-surfaces.md)
§ 4b said *"boots BLIND in this repo"*.

**`AGENTS.md` is still wanted** — his words, and the gap is estate-wide:
`MEASURED` 2026-08-26, **0 of 19** non-archived repositories carry one. Filed as
`OQ-FM-AGENTS-BOOT`, whose scope this widens from fleet-manager to the estate.
**Answered 2026-08-28: yes, everywhere**
([`2026-08-28-owner-direction.md`](2026-08-28-owner-direction.md) § 5).

## 4 · Two process notes he gave, worth keeping

**On the review relay** — after five `@codex` rounds on fm #947:

> *"Do you think it's really necessary to have an infinite loop of AIs
> correcting each other? Isn't there already a documented limit for these
> things?"*

There is, in the boot file: *stop when a bot's findings stop converging.* Round 3
had already tripped it (4 of 8 findings were re-emissions of fixes already in the
tree) and the session ran to five. **His question was the enforcement the rule
did not provide** — the same lesson the legibility plan reaches independently.

**On seeing what he sees** — he sent a screen recording of the chat on his phone
rather than describing it:

> *"I know you see this chat a lot differently than I do, so here is what I can
> see."*

`MEASURED` from it: a blocked `owner_review.py` draft **and** its amended reply
both render in full in his chat, so the hook's own instruction — *"answer in the
reply the owner reads"* — rests on a premise that does not hold on that surface.
**He judged it not worth recording as a defect** (*"today is the first time I'm
seeing it"*), so it is noted here and not filed. The agent-side fix needs no
mechanism: answer a block with **only what changed**.

## 5 · The evening correction — boot venues, the hub, and initiative (became OD-22)

Given while rejecting the first draft of
[the execution packets](../planning/2026-08-26-estate-execution-packets.md),
and it corrected that draft's frame in three places. Verbatim:

> *"you and the other session made a few claims that aren't true or at least
> unverified or badly worded. Like that a satellite can't read fleet-manager,
> which is not true. They just don't load the skills automatically, but if I
> would ask any session to execute a skill in any repo, they can do that
> perfectly. Tho they will have to be directed by me to find out about that."*

> *"But I always start all my session on fleet-manager, or when I now boot a
> local session it boots inside the onedrive or my local disk, which already
> has a copy of the skills. The local sessions are alreasy told to review
> fleet-manager first. Tho this might also need some work."*

> *"the other repos will never be used as boot repo, so they are out of the
> picture, which is why it is so important to have proper links and summaries
> of each repo inside the fleet-manager."*

> *"And the onedrive should basically be considered a repo of it's own. Which
> is kinda like the local version of fleet-manager, which is why right now I
> want to come up with a way that centralises this better."*

> *"I think the root cause/fix is to make sure agents take initiative to do
> their own research inside and outside the repos they work in, to help solve
> the problems they encountered for the next sessions. That's basically the
> main purpose of the substrate-kit and right now it's obviously not working
> as intended, which is why I believe this current plan is very connected to
> the substrate-kit, this is basically all one large connected web of repos
> and files that should all agree on most things and make it easy for any
> agent to navigate."*

**And on accepting the revised plan, the same evening:**

> *"I accepted it, and I think it's pretty good. Tho I have not read every word
> yet, it's getting late and I will continue with this tomorrow. Your task now
> is to properly document this plan and start with some preparations that make
> it easier for me to work on this with a local session tomorrow."*

**What is directive and what is not.** The boot-venue model, the hub's status
and the wanted centralisation are **OD-22** (the program's table). The
plan-acceptance is provisional by his own words — *"not read every word yet"* —
so tomorrow's session should expect line-level corrections, not treat the
packet doc as ratified prose. `MEASURED` the same session, settling the access
half of his correction: fleet-manager is **public** — an unauthenticated raw
fetch of `README.md` returns HTTP 200 — so any session anywhere can read it;
what a satellite boot lacks is auto-loaded apparatus and routing, which is a
discovery gap. The claims his correction retired are listed in the packet
plan's § 3 claims audit.
