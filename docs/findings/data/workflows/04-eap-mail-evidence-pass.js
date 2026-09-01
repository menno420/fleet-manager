export const meta = {
  name: 'eap-mail-evidence-pass',
  description: 'Map every recent audit, the raw 284-pattern catalogue and the prior mails into verified, novelty-checked evidence for the final EAP review mail, then propose and judge three spines for the widened brief',
  phases: [
    { title: 'Read', detail: '20 document readers · 12 pattern-shard readers · 1 census reader · 6 prior-mail readers' },
    { title: 'Merge', detail: 'audit candidates · pattern candidates · owner words · dedupe into one ranked list' },
    { title: 'Verify', detail: 'two refuting lenses per candidate (holds? new-and-fit?); survival rule' },
    { title: 'Spine', detail: '3 proposals from different angles · 3 judges, own counts · completeness critic' },
  ],
}

// ---- aggregation contract (fleet-preflight § 1) — asserted before any agent spawns
const dies = (a, b) => (a.refuted || b.refuted) || (Boolean(a.already_covered_by) && Boolean(b.already_covered_by))
const FIX = [
  [{ refuted: true,  already_covered_by: '' }, { refuted: false, already_covered_by: '' }, true ],
  [{ refuted: false, already_covered_by: 'mail-4' }, { refuted: false, already_covered_by: 'draft' }, true ],
  [{ refuted: false, already_covered_by: '' }, { refuted: false, already_covered_by: '' }, false ],
]
for (const [a, b, exp] of FIX) { if (dies(a, b) !== exp) throw new Error('aggregation fixture failed') }
log('aggregation fixtures: 2 kill, 1 survive — pass; fields read: refuted, already_covered_by')

// Paths come in via args so the script runs from any clone on any machine:
//   args.fm  = the fresh fleet-manager clone (Git Bash form, e.g. /c/dev/fleet-manager-night)
//   args.sb  = a folder holding superbot's docs/eap files (fetch them with gh api; see the README beside this script)
//   args.pat = the folder of pattern shards produced by shard_patterns.py beside this script
const FM = (typeof args === 'object' && args && args.fm) || '/c/dev/fleet-manager-eap-20260901'
const SB = (typeof args === 'object' && args && args.sb) || 'C:/Users/menno/AppData/Local/Temp/claude/C--Users-menno-OneDrive/9ee7d362-2383-4a0b-9e4e-7449213f0321/scratchpad/superbot-eap'
const PAT = (typeof args === 'object' && args && args.pat) || 'C:/Users/menno/AppData/Local/Temp/claude/C--Users-menno-OneDrive/9ee7d362-2383-4a0b-9e4e-7449213f0321/scratchpad/patterns'
const JUDGE_MODEL = (typeof args === 'object' && args && args.judgeModel) || undefined
log(`paths: fm=${FM} sb=${SB} pat=${PAT} · judge/verify/merge model=${JUDGE_MODEL || 'session default'}`)

const LEDGER = `TOPICS ALREADY ARGUED IN THE FOUR JULY MAILS (the final mail may reference each in ONE pointer line, never re-argue):
1 scoped owner-set pre-authorization (allow and deny, per repo/branch/action) · 2 coordinator-to-worker relayed authority treated as untrusted (dated regression, changelog-traced) · 3 nondeterministic denials · 4 documenting the walls is itself denied · 5 settings.json inert in auto mode · 6 server-side merge automation as a workaround, draft-default defeating it · 7 cross-project overview / "blocked on you" one level up · 8 routine/model attribution disagrees across surfaces · 9 scheduler unreliability, no tombstones, runs not inspectable · 10 branch deletion 403s · 11 proxy blocks api.github.com, gh missing · 12 GitHub MCP staleness, auto_merge absent, rulesets (now readable - correct, do not repeat) · 13 agents cannot see their own usage/cost · 14 agents cannot answer "what can I do?" (deferred tools invisible) · 15 the good parts: shared memory / auto-injected working agreement, worker-tier autonomy, born-red cards, honest negative results, the team's responsiveness.
NEVER SENT, so free to use: the 07-18 follow-up draft (the guard is venue-scoped: denied inside a Project, unrestricted in a plain chat with the same authority; one invented wall propagated through shared memory and a CI check now reds undated walls; stale stored text outranking a live instruction; trigger tools forcing an interactive approval with no off-switch) and the capability self-knowledge pack.
THE CURRENT DRAFT (2026-08-24, revised 08-25; Part 2 is 1,686 words) already carries: the scale figures (27 repos, 19 created in the fortnight, ~8,000 PRs, ~4,560 session records); Finding 1 FORGETTING and FALSE-DONE; Finding 2 the appended-correction-that-does-not-retract mechanism (101-defect full-read audit); Finding 3 "116 statements caught 0 of 16 incidents, everything that caught one arrived at a moment"; the other-vendor adversarial review that caught false-dones (335 s; 13 findings over 5 rounds); asks 1-5 (rules that arrive at the moment of action; agents that retract; a durable queryable record of what a session changed; a done-ness signal an owner can trust; usage/cost telemetry visible to agents); the good-parts block; the standing test-harness offer. CUT from it on 2026-08-25 to meet a one-page cap, still drafted: N4 drift on the most visible surface (0 of 7 live pages said the program ended, 33 days later); N5 cost not agent-legible (a 949 MB store with 925 MB ingestion history found only because the owner questioned a bill); N7 a blind-scored eval of agent comprehension; a finding 6 (five confident false "nothing there" answers in one session).
THE OWNER'S WIDENED BRIEF (2026-08-28, his words): "all the audits I'm doing right now will provide valuable information, not only about the EAP itself but generally about how agents work, which would be a valuable addition to the mail". So findings about how agents work IN GENERAL count, not only EAP-fortnight findings. He wants the mail valuable to Anthropic, not repetitive, made with visible effort; he hopes to be selected for a future early-access program. His rules: Part 1 is his own voice and is never drafted for him; Part 2 is Claude's; every ask is one "what we would like to see, because <one line>" line; nothing already argued is re-argued; a fresh thread; short.`

const READ_RULES = `READING RULES (non-negotiable):
- Read the WHOLE file in slices: sed -n '1,220p' FILE, then '221,440p', and so on until past the last line. Never rely on head, grep -l, or a listing to characterise content (a label is not its contents).
- Copy every number verbatim with its stated method, date and unit. Never round, never recompute, never generalise beyond the population the source names.
- If the source later corrects or retracts a claim (look for "corrected", "withdrawn", "an earlier version said", strikethrough), report the CORRECTED version and say it was corrected.
- Owner quotes must be exact text, never paraphrased; carry the date and citation.
- Certainty: report the tag the source itself uses (MEASURED / MEASURED-PRIOR / OWNER / REASONED / REVIEWED / UNVERIFIED / DERIVED) or "unstated".
- Citations are FILE:LINE-RANGE of what you actually read. Do not cite anything you did not open.
- Do not write, create or modify any file. Read only. Your final message must be the structured output only.`

const READER = { type: 'object', required: ['source', 'date', 'method', 'findings', 'owner_quotes', 'self_stated_limits'], properties: {
  source: { type: 'string' }, date: { type: 'string' }, method: { type: 'string' },
  findings: { type: 'array', items: { type: 'object', required: ['claim', 'evidence', 'citation', 'numbers', 'certainty', 'scope', 'novelty'], properties: {
    claim: { type: 'string' }, evidence: { type: 'string' }, citation: { type: 'string' }, numbers: { type: 'string' }, certainty: { type: 'string' },
    scope: { type: 'string', enum: ['eap', 'general', 'both'] },
    novelty: { type: 'string', enum: ['new', 'partly', 'already-argued', 'in-current-draft', 'unknown'] } } } },
  owner_quotes: { type: 'array', items: { type: 'object', required: ['quote', 'date', 'citation'], properties: { quote: { type: 'string' }, date: { type: 'string' }, citation: { type: 'string' } } } },
  self_stated_limits: { type: 'array', items: { type: 'string' } } } }

const MAIL = { type: 'object', required: ['file', 'status', 'date', 'topics', 'asks', 'good_parts'], properties: {
  file: { type: 'string' }, status: { type: 'string' }, date: { type: 'string' },
  topics: { type: 'array', items: { type: 'object', required: ['topic', 'one_line', 'citation'], properties: { topic: { type: 'string' }, one_line: { type: 'string' }, citation: { type: 'string' } } } },
  asks: { type: 'array', items: { type: 'string' } }, good_parts: { type: 'array', items: { type: 'string' } } } }

const PATTERNS = { type: 'object', required: ['shard', 'rows_read', 'selected'], properties: {
  shard: { type: 'string' }, rows_read: { type: 'integer' },
  selected: { type: 'array', items: { type: 'object', required: ['name', 'one_line', 'why_anthropic_cares', 'instances_quoted', 'repo_count', 'severity', 'fix_family', 'already_covered_positive', 'maps_to_existing_trap', 'product_ask'], properties: {
    name: { type: 'string' }, one_line: { type: 'string' }, why_anthropic_cares: { type: 'string' },
    instances_quoted: { type: 'array', items: { type: 'string' } }, repo_count: { type: 'integer' }, severity: { type: 'string' }, fix_family: { type: 'string' },
    already_covered_positive: { type: 'boolean' }, maps_to_existing_trap: { type: 'string' }, product_ask: { type: 'string' } } } } } }

const CANDS = { type: 'object', required: ['candidates'], properties: { candidates: { type: 'array', items: { type: 'object',
  required: ['id', 'claim', 'why_anthropic_cares', 'evidence', 'citations', 'scope', 'novelty', 'mail_role'], properties: {
  id: { type: 'string' }, claim: { type: 'string' }, why_anthropic_cares: { type: 'string' }, evidence: { type: 'string' },
  citations: { type: 'array', items: { type: 'string' } }, scope: { type: 'string', enum: ['eap', 'general', 'both'] }, novelty: { type: 'string' },
  mail_role: { type: 'string', enum: ['finding', 'ask', 'good-part', 'pointer', 'drop'] } } } } } }

const QUOTES = { type: 'object', required: ['quotes', 'roster', 'rules_for_the_mail'], properties: {
  quotes: { type: 'array', items: { type: 'object', required: ['quote', 'date', 'citation', 'about'], properties: { quote: { type: 'string' }, date: { type: 'string' }, citation: { type: 'string' }, about: { type: 'string' } } } },
  roster: { type: 'string' }, rules_for_the_mail: { type: 'array', items: { type: 'string' } } } }

const VERDICT = { type: 'object', required: ['refuted', 'already_covered_by', 'what_i_opened', 'discrepancies', 'corrected_claim'], properties: {
  refuted: { type: 'boolean' }, already_covered_by: { type: 'string' }, what_i_opened: { type: 'array', items: { type: 'string' } },
  discrepancies: { type: 'array', items: { type: 'string' } }, corrected_claim: { type: 'string' } } }

const SPINE = { type: 'object', required: ['title', 'target_length_words', 'structure', 'which_candidates_used', 'what_it_drops_and_why', 'risk'], properties: {
  title: { type: 'string' }, target_length_words: { type: 'integer' },
  structure: { type: 'array', items: { type: 'object', required: ['section', 'purpose', 'content_summary', 'word_budget'], properties: { section: { type: 'string' }, purpose: { type: 'string' }, content_summary: { type: 'string' }, word_budget: { type: 'integer' } } } },
  which_candidates_used: { type: 'array', items: { type: 'string' } }, what_it_drops_and_why: { type: 'string' }, risk: { type: 'string' } } }

const JUDGE = { type: 'object', required: ['scores', 'winner_index', 'graft_from_others', 'rationale'], properties: {
  scores: { type: 'array', items: { type: 'object', required: ['spine_index', 'valuable_to_anthropic', 'not_repetitive', 'honest_and_cited', 'respects_owner_rules', 'criteria_met_own_count', 'total'], properties: {
    spine_index: { type: 'integer' }, valuable_to_anthropic: { type: 'integer' }, not_repetitive: { type: 'integer' }, honest_and_cited: { type: 'integer' }, respects_owner_rules: { type: 'integer' }, criteria_met_own_count: { type: 'integer' }, total: { type: 'integer' } } } },
  winner_index: { type: 'integer' }, graft_from_others: { type: 'array', items: { type: 'string' } }, rationale: { type: 'string' } } }

const CRITIC = { type: 'object', required: ['missing_sources', 'unverified_claims', 'overlap_unchecked', 'other_gaps'], properties: {
  missing_sources: { type: 'array', items: { type: 'string' } }, unverified_claims: { type: 'array', items: { type: 'string' } },
  overlap_unchecked: { type: 'array', items: { type: 'string' } }, other_gaps: { type: 'array', items: { type: 'string' } } } }

function readerPrompt(paths, note) {
  return `You are one reader in a multi-agent evidence pass for Menno's final review mail to Anthropic's Claude Code Projects team (the EAP he took part in, July 2026). Your source(s): ${paths.join(' ; ')}. ${note}
${LEDGER}
Extract the findings in the source that could matter to Anthropic: what the source measured, the exact numbers, the mechanism it names, and whether it is about the EAP fortnight or about how agents work in general. Mark novelty against the July ledger and the current draft above. Collect verbatim owner quotes about agents, the EAP, or how he wants to work (at most 8, the sharpest). List the limits the source states about itself.
SIZE DISCIPLINE: at most 12 findings, ranked by value to Anthropic; claim at most 30 words; evidence at most 60 words; numbers as a compact list. A downstream merge reads fifteen of these outputs at once, so a long extraction crowds out the others.
${READ_RULES}`
}

function ownerPrompt(paths, note) {
  return `You are one reader in a multi-agent evidence pass for Menno's final review mail to Anthropic. Your source(s) hold THE OWNER'S OWN WORDS: ${paths.join(' ; ')}. ${note}
Collect every verbatim quote where he describes how agents work, fail, or should work; what the EAP taught him; what he wants from the platform; how he wants the mail written. Exact text only, with date and FILE:LINE. Also state, from these sources, his agent roster (which AI does what) and every rule he has stated about the mail itself. Skip DERIVED or agent-written prose entirely; only lines the source marks as his (OWNER, "his words", quoted replies) count.
${READ_RULES}`
}

function mailPrompt(path, status) {
  return `You are one reader in a multi-agent evidence pass for Menno's final review mail to Anthropic's Claude Code Projects team. Your ONE source is a PRIOR MAIL or its archived draft: ${path} — its status as far as the estate records: ${status}. Extract, so later verifiers can check whether a new claim was already argued: the status and date, every topic it argued (one line each, with FILE:LINE citation), every ask it made, and every good part it praised. For the CURRENT DRAFT file, read only the text between "## COPY FROM HERE" and "## COPY TO HERE".
${READ_RULES}`
}

function patternPrompt(shard) {
  return `You are one reader of the raw catalogue behind the 2026-08-29 estate-wide agent-error audit: 284 candidate recurring agent-error patterns harvested by 80 reader lanes over 4,583 session cards and 1,592 PR review comments across 20 repositories, then never read by a human. Your shard: ${PAT}/${shard} (a JSON array; read it WHOLE — it is large, read it in slices with sed -n and keep going to the end; count the rows you read into rows_read). Reading guide: ${FM}/docs/findings/data/README.md (read it first; it explains that instance_count is a claimed tally, only the instances array is checkable, that refuter_count 0 means unchallenged not confirmed, and that owner_flagged is void).
Select at most 6 patterns from your shard that Anthropic's Claude Code Projects team should hear about — patterns that say something general about how agents fail, that span several repositories, whose cited instances are concrete, and that suggest a platform-level answer (a hook moment, a signal the agent tier lacks, a default that misleads). Prefer patterns NOT already covered by the traps the current mail draws on (TRAP-001 dated doc read as current, TRAP-002 exit code after a pipe, TRAP-003 absence as evidence, TRAP-004 claim wider than sample, TRAP-006/007 card flipped early, TRAP-008 label read as contents) unless the pattern adds breadth evidence the mail lacks. For each: quote 2–3 instances verbatim from the instances array (repo · path:line — text), copy repo_count and severity, and write the one-sentence product ask it implies.
${LEDGER}
Read only; never write. Final message: the structured output only.`
}

function verifyA(c) {
  return `You are an adversarial verifier. Your job is to REFUTE this candidate finding for a mail to Anthropic if it does not hold. Default to refuted=true when you cannot confirm it from the cited lines.
CANDIDATE: ${JSON.stringify(c)}
Open EVERY citation. Citations under fleet-manager are FILE:LINE under ${FM} (use sed -n 'A,Bp'). Citations of the form "repo · path:line — text" point into other repositories on github.com/menno420/<repo>: fetch with gh api repos/menno420/<repo>/contents/<path> --jq .content | base64 -d, or curl -sL https://raw.githubusercontent.com/menno420/<repo>/main/<path>, then read around the cited line (files may have moved since the harvest; if a cite cannot be resolved, say so in discrepancies and judge the candidate on the citations that do resolve — an unresolvable cite is "not re-verifiable", never proof of falsity). Check: does the text say what the claim says, with these exact numbers, and without a downstream qualifier that reverses it (read to the end of the paragraph, cell or section)? Is the certainty tag right? Is the claim wider than the population the source measured? Did the source later correct or withdraw it? If the claim is essentially right but a number or a scope word is wrong, set refuted=false and put the exact fix in corrected_claim. Leave already_covered_by as an empty string unless you personally found the same substance argued in a July mail or the current draft (then name the file). Read only; never write. Final message: the structured output only.`
}

function verifyB(c, argued) {
  return `You are an adversarial verifier with the NOVELTY and FIT lens. Refute the candidate (refuted=true) if it would make the mail repetitive or unfit: (1) already argued in the July mails — the topics extracted from every prior mail are below, and the files are under ${SB} (email-2 sent 07-12, email-3 send-ready 07-13, email-4 SENT 07-16, gen1 wrap-up candidate, the NOT-sent 07-18 follow-up, the permission-classifier consolidated doc) — open the specific mail if the topic list suggests overlap; (2) already in the current draft — check the COPY block of ${FM}/docs/planning/2026-08-24-final-eap-email-draft.md; (3) not about the EAP nor about how agents work in general; (4) an anecdote with n=1 where the mail already has a measured finding of the same shape; (5) a claim about the vendor's product that the estate could not have measured. If the substance IS already argued in a SENT mail or the current draft, put that file name in already_covered_by (that turns it into a pointer line, not a finding). Material from the NOT-sent 07-18 draft or the unsent capability pack is free to use — do not mark it covered. List every file you opened in what_i_opened. If the candidate holds and is new, refuted=false, already_covered_by="".
CANDIDATE: ${JSON.stringify(c)}
TOPICS ARGUED IN EACH PRIOR MAIL (extracted by readers): ${JSON.stringify(argued)}
${LEDGER}
Read only; never write. Final message: the structured output only.`
}

// ---------------- Phase 1: readers ----------------
phase('Read')
const DOCS = [
  { paths: [`${FM}/docs/findings/2026-08-29-estate-agent-error-audit.md`], note: 'This is the ~1,000-agent estate-wide error audit (986 agents) the owner refers to; the single most important synthesis source.' },
  { paths: [`${FM}/docs/findings/2026-08-28-kit-tree-truth-pass.md`], note: 'A long audit of the shared method kit; extract only what says something about how agents work or fail.' },
  { paths: [`${FM}/docs/findings/2026-08-28-substrate-kit-genesis-dig.md`], note: 'The genesis dig: how the kit and its rules came to be, and what drifted. Extract what it shows about agents.' },
  { paths: [`${FM}/docs/findings/2026-08-28-router-band-reread.md`], note: 'A re-read of settled owner rulings that later sessions re-derived. The re-derivation pattern is the point.' },
  { paths: [`${FM}/docs/findings/2026-08-28-skill-and-rule-reuse-map.md`], note: 'Which skills and rules were actually reused, and which were written and never invoked.' },
  { paths: [`${FM}/docs/findings/2026-08-28-context-budget-and-orientation-cost.md`], note: 'What orientation costs a session in context, measured.' },
  { paths: [`${FM}/docs/findings/2026-08-29-fleet-orchestration-retrospective.md`, `${FM}/docs/findings/2026-08-29-fleet-preflight-dissection.md`], note: 'Two records of running a ~1,000-agent fleet and what its verification actually did. Lessons about multi-agent work itself.' },
  { paths: [`${FM}/docs/findings/2026-08-08-why-rules-dont-bind.md`, `${FM}/docs/findings/2026-08-09-error-to-mechanism.md`], note: 'The measurement behind "116 statements caught 0 of 16" and the scoring of 13 errors against "could a machine have caught this at the moment?".' },
  { paths: [`${FM}/docs/traps.md`], note: 'The trap register: eight recurring execution mistakes with dated instances and their delivery mechanisms.' },
  { paths: [`${FM}/docs/findings/2026-08-30-tree-only-cold-read.md`, `${FM}/docs/findings/2026-09-01-label-read-as-substance.md`, `${FM}/docs/planning/2026-08-30-fresh-start-redirect.md`], note: 'Two findability measurements, and (in the redirect, read its first ~120 lines and the section "What killed the last rebuild") the owner\'s own account of why the EAP superbot rebuild failed: coordinator relay, minimal steering, unverifiable done claims.' },
  { paths: [`${FM}/docs/findings/2026-08-23-eap-evidence-pack.md`], note: 'The numbers behind the current draft and the commands that produced them.' },
  { paths: [`${FM}/docs/findings/2026-08-24-e1-source-sweep.md`], note: 'What the prior mails argued, what was never sent, the seven month-after findings (N1–N7, N6 withdrawn), and the scale re-measured.' },
  { paths: [`${FM}/docs/findings/2026-08-26-cross-session-visibility.md`, `${FM}/docs/findings/2026-08-21-fleet-estate-review.md`], note: 'What one session can see of the others across machines and repositories.' },
  { paths: [`${FM}/docs/findings/2026-08-23-active-repo-intent-audit.md`], note: 'Whether each active repository states its own purpose; the acceptance test and its failures.' },
  { paths: [`${FM}/docs/findings/2026-08-09-eap-correspondence-record.md`, `${FM}/docs/planning/2026-07-26-final-eap-email-plan.md`], note: 'What was sent, what came back, the four unanswered questions, the two promises, and the plan for this mail.' },
]
const OWNER_DOCS = [
  { paths: [`${FM}/docs/findings/2026-08-28-od24-sitting-answers.md`], note: 'His 2026-08-28 discussion sitting: twenty answers, verbatim.' },
  { paths: [`${FM}/docs/findings/2026-08-28-owner-intent-elicitation.md`], note: 'His intent answers as they arrived, 2026-08-28.' },
  { paths: [`${FM}/docs/findings/2026-08-22-owner-direction.md`, `${FM}/docs/findings/2026-08-23-owner-direction.md`, `${FM}/docs/findings/2026-08-26-owner-direction.md`, `${FM}/docs/findings/2026-08-28-owner-direction.md`, `${FM}/docs/findings/2026-08-28-owner-direction-agent-autonomy.md`], note: 'Five owner-direction records, August 2026.' },
  { paths: [`${FM}/docs/owner-reflection-2026-07-21.md`, `${FM}/docs/eap-retrospective.md`], note: 'His reflection written for this very mail (its section "The vendor final-review email") and the EAP retrospective harvest fields.' },
  { paths: [`${FM}/owner/intent-workbooks/estate/why-this-estate-exists.md`, `${FM}/docs/intent.md`], note: 'His 2026-08-31 answers on why the estate exists, and the intent file with his 2026-08-08 interview answers and agent roster.' },
]
const MAILS = [
  { path: `${SB}/anthropic-email-4-classifier-regression-sent-2026-07-16.md`, status: 'SENT 2026-07-16 21:12Z (archived record)' },
  { path: `${SB}/anthropic-email-2-draft-2026-07-11.md`, status: 'send-candidate; the 07-12 scale-up report was sent from it (body no longer in the mailbox)' },
  { path: `${SB}/anthropic-email-3-draft-2026-07-13.md`, status: 'send-ready draft 07-13; whether it was sent is unverified' },
  { path: `${SB}/gen1-wrapup-email-final-candidate.md`, status: 'send-candidate 07-10; the 07-08 introduction review preceded it and its body is lost' },
  { path: `${SB}/2026-07-18-followup-email-draft.md`, status: 'NOT SENT — free material' },
  { path: `${FM}/docs/planning/2026-08-24-final-eap-email-draft.md`, status: 'THE CURRENT DRAFT, 2026-08-24 revised 08-25, unsent; read only the COPY block' },
]
const SHARDS = Array.from({ length: 12 }, (_, i) => `shard-${String(i + 1).padStart(2, '0')}.json`)

const docReads = parallel(DOCS.map(d => () => agent(readerPrompt(d.paths, d.note), { label: `read: ${d.paths[0].split('/').pop()}`, phase: 'Read', schema: READER })))
const ownerReads = parallel(OWNER_DOCS.map(d => () => agent(ownerPrompt(d.paths, d.note), { label: `owner: ${d.paths[0].split('/').pop()}`, phase: 'Read', schema: QUOTES })))
const mailReads = parallel(MAILS.map(m => () => agent(mailPrompt(m.path, m.status), { label: `mail: ${m.path.split('/').pop()}`, phase: 'Read', schema: MAIL })))
const shardReads = parallel(SHARDS.map(s => () => agent(patternPrompt(s), { label: `patterns: ${s}`, phase: 'Read', schema: PATTERNS })))
const censusRead = agent(`You are one reader in a multi-agent evidence pass for Menno's final review mail to Anthropic. Your source: ${PAT}/census-20-repos.json — 20 rows, one per repository, each a single lane's first-pass census of that repo's agent-instruction surface (what it instructs, what enforcement exists, prose-only rules, divergences from the shared kit, biggest gap, portable lesson). Read the guide first: ${FM}/docs/findings/data/README.md, section "The census rows have their own limits" — one reader per repo, unverified, some lanes saw a filtered snapshot. Extract: the portable lessons and biggest gaps that recur across repositories (name the repos), the pattern of prose-only rules versus mechanical enforcement, and anything that says something general about how agents work. Never aggregate the rows into an estate-wide count; report N repos of 20 where you counted.
${LEDGER}
${READ_RULES}`, { label: 'census: 20 repos', phase: 'Read', schema: READER })

const [docs, owners, mails, shards, census] = await Promise.all([docReads, ownerReads, mailReads, shardReads, censusRead])
const docOut = docs.filter(Boolean), ownerOut = owners.filter(Boolean), mailOut = mails.filter(Boolean), shardOut = shards.filter(Boolean)
log(`readers: docs ${docOut.length}/${DOCS.length} · owner ${ownerOut.length}/${OWNER_DOCS.length} · mails ${mailOut.length}/${MAILS.length} · shards ${shardOut.length}/${SHARDS.length} (${shardOut.reduce((n, s) => n + s.rows_read, 0)} rows read, ${shardOut.reduce((n, s) => n + s.selected.length, 0)} selected) · census ${census ? 'ok' : 'NULL'}`)
if (docOut.length < DOCS.length) log(`DROPPED readers (returned null): ${DOCS.filter((d, i) => !docs[i]).map(d => d.paths[0].split('/').pop()).join(', ')}`)
if (shardOut.length < SHARDS.length) log(`DROPPED shards: ${SHARDS.filter((s, i) => !shards[i]).join(', ')}`)

// ---------------- Phase 2: merge (barrier is correct: dedupe across all readers) ----------------
phase('Merge')
const mergeRules = `Rules: one candidate per distinct mechanism; merge overlapping ones and keep all their citations; copy numbers verbatim from the reader extractions; scope = eap / general / both; novelty against the ledger and the current draft; mail_role = finding (a measured claim worth a paragraph), ask (a "what we would like to see, because…" line), good-part, pointer (already argued — one line), or drop. Prefer what the current draft does NOT already carry, and prefer general-about-agents findings with a measured denominator over EAP anecdotes.
WORDING DISCIPLINE (the pilot's verifiers rejected every candidate's wording for these four reasons — do not repeat them): (1) keep the source's population scope inside the claim — "on the surfaces measured", "in the 12 repositories that have any", never "on every surface" or "always"; (2) keep a MEASURED count and a REASONED mechanism in separate sentences — "155 of 155 were agent-authored" is measured, "because agents post with his credential" is the source's reasoning, say which is which; (3) never assert how the vendor's product works ("Claude Code acts under the user's identity") — the estate measured its own repositories, not the product; state what was measured and let the product team draw the inference; (4) no superlatives or directional words the source does not use ("only ever", "the cheapest of all", "never") — quote the source's own qualifier instead. A candidate that pads its evidence with an n=1 anecdote or an unrelated pattern loses at verification; cite only what supports the exact claim.
Do not open files; work only from the extractions. Final message: the structured output only.`
const docGroups = [docOut.slice(0, 5), docOut.slice(5, 10), docOut.slice(10)].filter(g => g.length)
const mergeAparts = (await parallel(docGroups.map((g, gi) => () =>
  agent(`You merge reader extractions into candidate findings for Menno's final EAP mail to Anthropic. Produce at most 10 candidates (ids A${gi + 1}-1..A${gi + 1}-10) from these audit and record extractions (group ${gi + 1} of ${docGroups.length}).
${LEDGER}
${mergeRules}
EXTRACTIONS:
${JSON.stringify(g)}`, { label: `merge A${gi + 1}: audits → candidates`, phase: 'Merge', schema: CANDS, model: JUDGE_MODEL })))).filter(Boolean)
const mergeA = { candidates: mergeAparts.flatMap(m => m.candidates || []) }
const [mergeB, ownerMerge] = await Promise.all([
  agent(`You merge pattern selections from the raw 284-pattern catalogue, plus the 20-repository census, into candidate findings for Menno's final EAP mail to Anthropic. Produce at most 14 candidates (ids B1..B14). A pattern candidate's evidence must quote its instances verbatim (repo · path:line — text) and its repo_count; never quote instance_count. Group patterns that are one mechanism into one candidate.
${LEDGER}
${mergeRules}
PATTERN SELECTIONS:
${JSON.stringify(shardOut)}
CENSUS EXTRACTION:
${JSON.stringify(census)}`, { label: 'merge B: patterns → candidates', phase: 'Merge', schema: CANDS, model: JUDGE_MODEL }),
  agent(`You consolidate the owner's verbatim words from five reader extractions into one list for the people writing Menno's final EAP mail. Keep at most 25 quotes: the ones that best show how he thinks about agents, what the EAP taught him, what he wants from the platform, and every rule he stated about the mail. Exact text only, dated, cited. Deduplicate identical quotes. State his agent roster in one paragraph, and list every rule for the mail as one line each. Do not open files. Final message: the structured output only.
EXTRACTIONS:
${JSON.stringify(ownerOut)}`, { label: 'merge C: owner words', phase: 'Merge', schema: QUOTES }),
])
const pool = [...(mergeA && mergeA.candidates ? mergeA.candidates : []), ...(mergeB && mergeB.candidates ? mergeB.candidates : [])]
log(`merge: A ${mergeA ? mergeA.candidates.length : 0} · B ${mergeB ? mergeB.candidates.length : 0} · owner quotes ${ownerMerge ? ownerMerge.quotes.length : 0}`)
const dedup = await agent(`You deduplicate and rank candidate findings for Menno's final EAP mail to Anthropic. Two merges produced overlapping lists (A from the synthesis audits, B from the raw pattern catalogue). Return one ranked list of at most 16 candidates: merge any two that describe the same mechanism (keep both id sets in the id field, like "A3+B7", and all citations), rank by value to Anthropic's product team × strength of evidence × novelty against the July mails and the current draft. Keep mail_role. Drop nothing silently: a candidate you leave out must appear with mail_role "drop" and a one-line reason in its evidence field, at the end of the list, beyond the 16.
${LEDGER}
POOL:
${JSON.stringify(pool)}
Do not open files. Final message: the structured output only.`, { label: 'dedupe + rank', phase: 'Merge', schema: CANDS, model: JUDGE_MODEL })
const ranked = (dedup && dedup.candidates ? dedup.candidates : []).filter(Boolean)
const toVerify = ranked.filter(c => c.mail_role !== 'drop').slice(0, 16)
log(`ranked ${ranked.length}; verifying ${toVerify.length}; dropped by dedupe: ${ranked.filter(c => c.mail_role === 'drop').length}`)

// ---------------- Phase 3: verify (pipelined; two refuting lenses per candidate) ----------------
phase('Verify')
const argued = mailOut.map(m => ({ file: m.file, status: m.status, topics: m.topics.map(t => t.topic) }))
const verified = await pipeline(toVerify,
  c => parallel([() => agent(verifyA(c), { label: `A holds? ${c.id}`, phase: 'Verify', schema: VERDICT, effort: 'high', model: JUDGE_MODEL }),
                 () => agent(verifyB(c, argued), { label: `B new? ${c.id}`, phase: 'Verify', schema: VERDICT, effort: 'high', model: JUDGE_MODEL })]),
  (vs, c) => {
    const [a, b] = vs
    if (!a || !b) return { candidate: c, a, b, survives: false, reason: 'a verifier returned null' }
    const d = dies(a, b)
    return { candidate: c, a, b, survives: !d, reason: d ? (a.refuted || b.refuted ? 'refuted' : 'already covered per both lenses') : 'survives' }
  })
const results = verified.filter(Boolean)
const survivors = results.filter(r => r.survives)
log(`verify: ${survivors.length}/${results.length} survive · refuted ${results.filter(r => r.reason === 'refuted').length} · covered ${results.filter(r => r.reason.startsWith('already')).length}`)

// ---------------- Phase 4: spine proposals, judges, critic ----------------
phase('Spine')
const survivorBrief = survivors.map(r => ({ id: r.candidate.id, claim: r.a.corrected_claim || r.candidate.claim, why: r.candidate.why_anthropic_cares, evidence: r.candidate.evidence, scope: r.candidate.scope, role: r.candidate.mail_role, citations: r.candidate.citations, lensB_note: (r.b.discrepancies || []).join(' | ') }))
const coveredBrief = results.filter(r => !r.survives).map(r => ({ id: r.candidate.id, claim: r.candidate.claim, reason: r.reason, covered_by: [r.a.already_covered_by, r.b.already_covered_by].filter(Boolean).join(' / '), discrepancies: [...(r.a.discrepancies || []), ...(r.b.discrepancies || [])] }))
const ANGLES = [
  { key: 'one-page', angle: 'ONE PAGE (about 650 words for Part 2). The owner said "much shorter than before" and chose a literal one-page cap on 2026-08-25 — but then widened the brief on 08-28. Design the shortest Part 2 that carries the widened brief: a thesis, at most four findings each with one number, five asks, the good parts, the offer, the links. Say what a one-pager must sacrifice.' },
  { key: 'two-part-two-page', angle: 'TWO SECTIONS (about 1,300 words for Part 2): "what the program produced, a month later" (the EAP half, tightened from the current draft) and "what a summer of auditing agents shows about how agents work in general" (the new half from the audits and the pattern catalogue), each with its own numbered asks. Design it so the second half is the reason to read.' },
  { key: 'keep-plus-addendum', angle: 'KEEP THE CURRENT PART 2 (1,686 words, six adversarial rounds already spent on it) and add one addendum section of at most 450 words carrying only what the audits add about agents in general, plus at most three new asks. Design the addendum and say exactly which sentences of the current draft must change to stay true.' },
]
const spines = (await parallel(ANGLES.map(a => () => agent(`You design ONE spine (structure, not prose) for Part 2 of Menno's final review mail to Anthropic's Claude Code Projects team, from this angle: ${a.angle}
Constraints that bind every spine: Part 1 is the owner's voice and is never drafted; Part 2 is Claude's; every ask is one line "what we would like to see — because <one line>"; nothing already argued in the July mails is re-argued (one pointer line at most); every number carries its method and date and has a public link; the mail must be valuable to a product team, not repetitive, honest about limits, and read as coming from a fan, not a complainer (keep the good parts and the standing offer). Read the current COPY block at ${FM}/docs/planning/2026-08-24-final-eap-email-draft.md (between "## COPY FROM HERE" and "## COPY TO HERE") so you build on it rather than beside it.
${LEDGER}
VERIFIED SURVIVING CANDIDATES (use their ids in which_candidates_used): ${JSON.stringify(survivorBrief)}
CANDIDATES THAT DID NOT SURVIVE (already covered or refuted — may only be pointers): ${JSON.stringify(coveredBrief)}
Read only; never write. Final message: the structured output only.`, { label: `spine: ${a.key}`, phase: 'Spine', schema: SPINE })))).filter(Boolean)

const LENSES = [
  'You are the PRODUCT TEAM lens: score what an Anthropic Claude Code Projects PM or engineer would actually learn and act on. Penalise anything they already heard in the July mails.',
  'You are the EVIDENCE lens: score whether every finding in the spine can be backed by a verified candidate with a number, a method and a date, and whether limits are stated. Penalise any claim about the product the estate could not have measured.',
  'You are the OWNER-RULES lens: score fidelity to Menno\'s rules (Part 1 his, one-line asks, no re-arguing, fresh thread, short, fan-not-complainer, visible effort) and to his widened brief (general agent findings, not only EAP). Penalise length that is not earning its place.',
]
const judges = (await parallel(LENSES.map((lens, i) => () => agent(`${lens}
Score each of the three spines below on four criteria, 1–5 each (valuable_to_anthropic, not_repetitive, honest_and_cited, respects_owner_rules), and give criteria_met_own_count = YOUR OWN count of how many of these 12 binding constraints the spine satisfies — count them yourself from the spine's structure, never from its self-description: (1) Part 1 undrafted, (2) one-line asks with a because, (3) no re-argued July topic, (4) every finding maps to a verified candidate id, (5) numbers with method and date, (6) public link per number, (7) good parts kept, (8) standing offer kept, (9) general-agent findings present, (10) EAP-month-after findings present, (11) total length stated and justified, (12) what it drops is stated. total = sum of the four criteria. Name the winner and the specific elements to graft from the other two.
${LEDGER}
SPINES: ${JSON.stringify(spines)}
SURVIVING CANDIDATE IDS: ${JSON.stringify(survivorBrief.map(s => s.id))}
Do not open files. Final message: the structured output only.`, { label: `judge ${i + 1}`, phase: 'Spine', schema: JUDGE, effort: 'high', model: JUDGE_MODEL })))).filter(Boolean)

const critic = await agent(`You are the completeness critic for a multi-agent evidence pass that fed Menno's final EAP review mail. Below is what was read, what survived verification, and the spines proposed. Say what is MISSING: sources in fleet-manager@cb3fc9a or superbot docs/eap that should have been read and were not (check ${FM}/docs/findings/README.md and ls ${FM}/docs/findings ${FM}/docs/planning ${SB}); surviving claims whose verification looks thin (a verifier that opened nothing, or a corrected_claim that changes the meaning); overlaps with the prior mails nobody checked; and any other gap. Be concrete and short.
READ: ${JSON.stringify({ docs: DOCS.map(d => d.paths), owner: OWNER_DOCS.map(d => d.paths), mails: MAILS.map(m => m.path), shards: SHARDS, census: true })}
SURVIVORS: ${JSON.stringify(survivorBrief)}
NON-SURVIVORS: ${JSON.stringify(coveredBrief)}
SPINES: ${JSON.stringify(spines.map(s => ({ title: s.title, words: s.target_length_words, used: s.which_candidates_used })))}
Read only; never write. Final message: the structured output only.`, { label: 'completeness critic', phase: 'Spine', schema: CRITIC, effort: 'high', model: JUDGE_MODEL })

return {
  contract: 'see CONTRACTS.md beside this script',
  counts: { docs: docOut.length, owner: ownerOut.length, mails: mailOut.length, shards: shardOut.length, rows_read: shardOut.reduce((n, s) => n + s.rows_read, 0), pool: pool.length, ranked: ranked.length, verified: results.length, survivors: survivors.length },
  readers: { docs: docOut, census },
  patterns: shardOut,
  owner_words: ownerMerge,
  prior_mails: mailOut,
  ranked,
  verified: results,
  spines,
  judges,
  critic,
}
