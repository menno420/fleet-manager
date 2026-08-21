# 2026-08-21 — game-community Discord bot plan

> **Status:** `complete`

- **📊 Model:** gpt-5.6 · high · planning/architecture
- **Venue:** ChatGPT Work, owner-live request
- **Branch:** `codex/game-community-bot-plan-2026-08-21`
- **Pull request:** [fm #882](https://github.com/menno420/fleet-manager/pull/882)
- **Scope:** Review `fleet-manager`, `superbot`, and `superbot-next`; create the authoritative pre-repo plan for a new AI-first Discord bot focused on game testing and a general game community. The production bot and both source repositories were evidence only and remain untouched.

## Previous-session review

⟲ fm #878 established the current Layer-2 entry points for both bot repositories and left their direction as an owner-gated fork. This session re-verified both repositories and resolved that planning fork from the owner's live direction.

## 💡 Session idea

Make AI autonomy a typed, risk-scored tool policy from the first vertical slice, so giving the AI more freedom does not create a second ungoverned mutation path.

## Outcome

- Added the indexed eight-file plan at
  `docs/planning/2026-08-21-game-community-bot/`: intent, pinned source
  comparison, product/UX, architecture, dependency-ordered roadmap, safe
  migration/rollout, and verification/operations.
- Chose a clean multi-game repository as the reversible planning default:
  `superbot` is the behavior/operator-UX oracle, `superbot-next` is the
  layered-kernel/workflow/AI pattern donor, and neither is the build target.
- Defined a Game Testing server profile, real opt-in/install/launch tester
  funnel, builds/playtests, Forum-based feedback-to-fix/retest, moderation
  appeals, guild removal/reinstall, and deterministic fallbacks.
- Defined AI Observe/Assist/Act with provider-neutral adapters, durable scoped
  memory, purpose-limited service principals, state-bound confirmations,
  privacy/spend gates, component budgets, audit, verification, and kill
  switches.
- Reconciled the planning index, both Layer-2 handoffs, the canonical
  consolidation program (OD-16; OD-1/R4/R7 superseded), and `docs/ESTATE.md`.
- Created no repository, Discord application, secret, guild, Railway service,
  data migration, source-bot change, or production cutover. GCB-1..GCB-6 remain
  explicit owner gates with recommended defaults.

## Source baseline

- `fleet-manager` main reviewed at `9f8eb079effd6af2c6475665ffc16af736d1ce99`
- `superbot` main reviewed at `5e3a667b2a55bae98a7863dd66492f477dd19546`
- `superbot-next` main reviewed at `d5f66dc27768d49b2755f368c6a2d0ecca66a1af`

## Verification and review

- Plan links were resolved from the nested directory and corrected; all local
  plan files passed scans for tabs, trailing whitespace, unresolved
  TODO/TBD/FIXME/checkbox placeholders, and superseded phrases.
- GitHub substrate run `32530290191` at pre-close head `c380ade4f3`:
  repository checkers reported **54 routes · 28 docs routed · 0 errors ·
  0 notes**. Its only gate failure was the designed born-red
  `session-card-hold` for this card's former `in-progress` status.
- Codex round 1 reviewed `395f26ad5f`: **17 findings**. Sixteen substantive
  findings were conceded, fixed, replied to, and resolved; the close-card
  finding was deliberately held for this final flip.
- Codex round 2 reviewed `802b5e3343`: **2 findings**, both conceded, fixed,
  replied to, and resolved.
- Codex final re-review reviewed `677220e0dc`: **4 findings**, all conceded,
  fixed, replied to, and resolved. The configured two-re-review cap is reached;
  the transparent post-review delta is those four dependency/gate fixes plus
  this close-out flip.
- Review total: **23 findings · 23 conceded/fixed · 0 survived · 0 unresolved
  after this card thread closes**.

## Handoff

Next executable step: owner confirms GCB-1 (recommended repository name
`superbot-community`), then Phase 0 creates the isolated canonical repository
and transplants/reconciles this plan. GCB-2..GCB-6 are answered only at their
named irreversible/enabling gates.

Layer-2 handoff: `docs/repos/superbot/README.md` and
`docs/repos/superbot-next/README.md` now point to the resolved clean-repo,
server-first direction and preserve both source repos as read-only evidence.
