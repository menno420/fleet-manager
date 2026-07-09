# claude.ai fleet-visibility findings — two screen recordings (2026-07-09)

> **Status:** `reference`
>
> Distilled 2026-07-09 (evening) from two frame-by-frame analyses of the
> owner's screen recordings (Samsung browser, ~12 tabs, one per Project). The
> owner's complaint under test: *"everything looks dormant while the fleet is
> working."* Verdict in one line: **session-level activity signals are good;
> project-level rollup is zero; some timestamps and Working states actively
> mislead.**

## Recording 1 — chat-view tab sweep (15.3s, 31 frames)

A ~1.2s-per-tab sweep across 10 Project tabs, each open on a session
*conversation* view.

- **The Projects sidebar exposes zero activity state** — active and dormant
  Projects are pixel-identical (icon + name + chevron; no spinner, badge, dot,
  unread marker, timestamp, or preview on any row).
- The **browser tab strip is useless**: 12 tabs all titled "Claude Code" with
  identical favicons.
- **Delegated/child-session work is invisible:** Trading Strategy, Mining,
  Exploration, fable5, and sonnet5 all *textually claimed* live background
  work ("successor is live", "is now actively building", "build take 2"), but
  each coordinator chat showed a completed static turn. The greyed "Started
  session…" chips are historical links, not liveness indicators.
- **Timestamps actively mislead:** "8 minutes ago" / "31 minutes ago" stamp
  the last message in the *open* chat while a spawned worker runs right now.
- The only activity indicator anywhere: the in-conversation **"Claude is
  working" pulsing dot** — visible in 1 of 10 tabs (Project Manager), only
  while that session's own turn streams.
- "Needs-human" states (e.g. "Needs you: one click" PR-merge asks, a "Failed
  to message session" error) also have **no UI badge** — same visibility gap.
- **Conclusion:** the owner's "all dormant" perception is a faithful reading
  of the UI, not a mistake — with the fleet's coordinator→child pattern, 9 of
  10 working Projects showed no working state anywhere.

## Recording 2 — session-list tab tour (18.6s, 28 frames, 16:48–16:49)

Same device, but each tab open on a Project's *session list* instead of a chat.

- **Within a project's session list the signal is good:** sessions bucket
  under "Needs input / Working / Ready for review / Idle / Pinned" headers
  with count badges; Working rows carry an animated-ellipsis icon, a step
  progress counter (6/8, 3/9, …), live preview text, PR badges ("15 merged /
  #60"), and timestamps that tick to "Just now." Genuinely live: one row's
  timestamp flipped 2m-ago → Just-now on camera, and the Project Manager
  coordinator visibly moved Working → Idle mid-recording.
- **Across projects: nothing.** The sidebar shows no indicator on any Project
  entry regardless of Working sessions inside (a project with a
  Working-Just-now session renders identically to one that is 100% Idle). The
  owner must open each project — hence the 12-tab workaround being filmed.
- **Reliability caveat: "Working" can be stale.** A hung/abandoned session
  (sonnet5 take-1) sat in Working with a 50m-old timestamp next to its take-2
  successor. "Working" means "session not terminated," not "making progress."
  The trustworthy liveness signals are the step counter + Just-now timestamp.
- The Routines sidebar section, by contrast, does show colored dots.

## Workflow implications

1. **Any fleet-visibility fix has to live outside this UI** — claude.ai
   surfaces liveness only inside an opened project (session list) or an
   actively-streaming chat. This is exactly the niche of the control-plane
   heartbeats + the websites dashboard (/fleet, /queue, /environments).
2. Recording 2 confirms the practical owner ritual: open the **session list**
   (not the chat) per project — chat views are the misleading surface.
3. The stale-Working caveat validates the retro synthesis's heartbeat/liveness
   cross-patterns (`retro-synthesis-2026-07-09.md` §3.5): the platform itself
   cannot distinguish a hung session from a working one.
4. Owner-blocked states ("Needs input", failed messages) are just as invisible
   at the project level as activity — the owner-queue doc + status ⚑ lines
   remain the only reliable needs-owner surface.
