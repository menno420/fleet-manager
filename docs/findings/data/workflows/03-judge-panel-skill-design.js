export const meta = {
  name: 'ultracode-prep-skill',
  description: 'Design an ultracode fleet-preparation skill from this session measured orchestration telemetry and its six real failures',
  phases: [
    { title: 'Draft', detail: '3 independent skill drafts from different design angles' },
    { title: 'Judge', detail: '3 judges per draft, incl. the acceptance test' },
    { title: 'Synthesize', detail: 'winner plus grafts from runners-up' },
  ],
}

const EVIDENCE = `
## MEASURED TELEMETRY from the run this skill is derived from (fleet-manager, 2026-08-28/29)

Two workflows auditing 4,583 session cards + 1,592 PR review comments across 20 repos.

- **1,063 agent transcripts**, 913,042 output tokens, 17.1 h wall clock.
- **Actual concurrency: peak 4, mean 3.8, median 4.** The documented cap is min(16, CPUs-2);
  this box gave 4. Planning was done assuming 10-16 — wrong by 3-4x.
  Consequence: at concurrency 4 and ~190s mean agent duration, **every agent added costs
  ~48 seconds of wall clock**. 1,063 agents = ~14 h of serialised time.
- **Budget split by lane** (output tokens):
  | lane | agents | out tok | share | mean dur |
  |---|---|---|---|---|
  | verify | 929 | 805,679 | 88% | 189s |
  | harvest:cards | 68 | 52,640 | 5% | 214s |
  | synthesize | 32 | 40,036 | 4% | 358s |
  | census | 20 | 12,400 | 1% | 226s |
  | harvest:codex+owner | 12 | 2,122 | 0% | ~310s |
- **Verification outcome: 925 verdicts → 572 PARTIAL, 293 CONFIRMED, 60 REFUTED.
  Only 7.0% of individual verdicts set refuted=true. Only 7 of 284 patterns died.**
  88% of the budget bought a 97.5% pass rate.
- **815 of 925 verdicts named something in \`already_covered_by\` — and the survival rule
  ignored that field entirely**, keying only on \`refuted\`. The right signal was collected
  and discarded in aggregation.
- External review (Codex) then returned **37 findings across 4 rounds, ALL conceded, zero
  survived** — i.e. essentially all real quality came from outside the workflow's own
  verification stage.

## THE SIX REAL FAILURES the skill must prevent

1. **Unvalidated instrument.** The error-matching regex was compiled with \`re.X\`, which
   silently strips literal spaces inside multi-word alternatives — "was wrong" became
   "waswrong". 6 of 7 phrases were inert. 986 agents ran on it before anyone checked.
   Five known-positive test strings would have caught it in seconds.
2. **Corpus mislabelled.** The finding said "7,214 sections from 4,583 cards". The fetch
   also took findings, retros, audits, program docs; measured after the fact: 89% cards,
   10% other. Scope of the fetch and wording of the claim were written hours apart and
   never reconciled.
3. **Aggregation ignored its own signal** (the 815/925 above); and of three "adversarial"
   lenses only ONE was told to refute, so a lone dissent was always outvoted 2-1.
4. **Stale base.** Nobody re-read \`main\` at the start. Mid-run, one PR merged that FIXED
   the exact defect being measured, and another landed an owner ruling that retired the
   framing of the recommendation. Both were discovered at the end, costing an extra PR.
5. **Inputs discarded.** The extractor kept the resulting document text and threw away the
   authoring input. The audit's own recommended follow-up measurement ("would this route
   have fired on that incident?") is therefore impossible from its own corpus.
6. **Documented values quoted as measured.** The concurrency figure above was taken from
   the tool reference and reported as observed. The journals had the real number all along.

## HOUSE CONSTRAINTS (fleet-manager / substrate-kit estate)
- "Records may grow; instructions may not." A rule that is only stated has never bound
  anything here. Deterministic parts belong in scripts; judgement belongs in skills.
- No fake precision: no invented thresholds, cadences or ratios.
- The owner does not want new walls; a skill advises and prepares, it does not gate.
- Existing sibling skills to match in shape: \`prompt-preflight\`, \`quality-gate\`,
  \`implementation-prompt\`. Read one at /home/user/fleet-manager/.claude/skills/ if present.
`

const DRAFT = {
  type: 'object',
  properties: {
    name: { type: 'string' },
    description: { type: 'string', description: 'the SKILL.md frontmatter description — when it should fire' },
    angle: { type: 'string', description: 'the design angle this draft took' },
    body_markdown: { type: 'string', description: 'the full SKILL.md body, ready to commit' },
    catches: { type: 'array', items: { type: 'string' }, description: 'which of the six failures it catches, and by what step' },
    misses: { type: 'array', items: { type: 'string' }, description: 'which it does NOT catch, stated honestly' },
    why_this_shape: { type: 'string' },
  },
  required: ['name','description','angle','body_markdown','catches','misses'],
}

const ANGLES = [
  { key: 'preflight', ask: `Design it as a PREFLIGHT CHECKLIST run before the first agent spawns — the sibling of the estate's existing \`prompt-preflight\`. Its output is a short written plan the session commits or states before fanning out: what the instrument is and how it was validated, what the corpus actually contains, what the base state is, what gets retained, and the wall-clock estimate from measured concurrency. Bias toward steps that produce an artifact, not steps that produce a feeling.` },
  { key: 'budget', ask: `Design it around the BUDGET AND SHAPE decision — the measured finding is that 88% of spend bought a 97.5% pass rate. Make the skill force an explicit allocation between discovery and judgement BEFORE launch, with the aggregation rule written down and tested on paper against a case that should fail. Include the wall-clock arithmetic (agents x mean duration / measured concurrency) so scale is chosen rather than stumbled into.` },
  { key: 'contract', ask: `Design it as a set of CONTRACTS each stage must satisfy, checked in order: the instrument contract (validated against known positives AND known negatives before the fleet runs), the corpus contract (what is in it, stated in the same breath as the number), the retention contract (what raw inputs are kept so downstream measurement is possible), the base contract (what HEAD was at launch), the aggregation contract (which field decides, and one case that must die). A stage cannot start until its contract is written.` },
]

phase('Draft')
log('3 independent drafts from different design angles')
const drafts = await parallel(ANGLES.map(a => () =>
  agent(
    `Write a Claude Code skill that prepares a well-organised multi-agent fan-out ("ultracode fleet") BEFORE it launches.

**This is not a skill about how to invoke ultracode** — the harness already covers that. It is about the preparation that makes a large fan-out produce trustworthy output instead of expensive noise. It is derived from one real run, and it must be derived from that run's MEASURED evidence rather than from general advice.

${EVIDENCE}

YOUR DESIGN ANGLE — ${a.key}: ${a.ask}

REQUIREMENTS:
- The body must be a complete, committable SKILL.md body in markdown. Concrete steps, not principles.
- Every number you cite must come from the telemetry above. Invent none.
- Say plainly which of the six failures each step would have caught, and which it would not.
- Keep it short enough to be read at the moment of use. A skill nobody finishes is not delivered.
- It advises and prepares; it never gates or blocks.`,
    { label: `draft:${a.key}`, phase: 'Draft', schema: DRAFT, effort: 'high' }
  )
))

const ok = drafts.filter(Boolean)
log(`${ok.length} drafts; judging each on 3 lenses`)

const SCORE = {
  type: 'object',
  properties: {
    lens: { type: 'string' },
    score: { type: 'number', description: '0-10' },
    catches_count: { type: 'number', description: 'how many of the six failures it genuinely catches, by your own reading not the draft self-report' },
    verdict: { type: 'string', enum: ['STRONG','USABLE','WEAK'] },
    strongest_element: { type: 'string', description: 'the one step worth grafting into any winner' },
    fatal_flaws: { type: 'array', items: { type: 'string' } },
    reasoning: { type: 'string' },
  },
  required: ['lens','score','catches_count','verdict','strongest_element','reasoning'],
}

const LENSES = [
  `ACCEPTANCE TEST — the only lens that matters most. Walk each of the six real failures and decide, concretely, whether following this draft would have PREVENTED it. Do not credit a step that merely mentions the topic; credit it only if a session following the text would have produced a different action. Report catches_count as your own count, not the draft's.`,
  `USABILITY — would a session actually follow this at the moment of launch, when it is impatient and the task looks obvious? Length, ordering, and whether each step produces a checkable artifact. A step that says "consider whether..." is a step that will be skipped. Penalise anything that reads as principles rather than actions.`,
  `HOUSE FIT — judge against the estate's own doctrine: instructions may not grow, deterministic parts belong in scripts not prose, no fake precision, no new walls, and it must not duplicate what prompt-preflight/quality-gate already do. Read /home/user/fleet-manager/.claude/skills/ if present. Penalise invented thresholds hardest.`,
]

phase('Judge')
const scored = await pipeline(
  ok,
  (d) => parallel(LENSES.map((ask, i) => () =>
    agent(
      `Judge this candidate skill draft.\n\nDRAFT (angle: ${d.angle}):\n${JSON.stringify({name:d.name, description:d.description, body:d.body_markdown, self_reported_catches:d.catches, self_reported_misses:d.misses}, null, 1).slice(0,120000)}\n\n${EVIDENCE}\n\nYOUR LENS: ${ask}`,
      { label: `judge:${i}:${(d.angle||'').slice(0,16)}`, phase: 'Judge', schema: SCORE, effort: 'high' }
    )
  )).then(v => {
    const vs = v.filter(Boolean)
    const mean = vs.reduce((s,x)=>s+(x.score||0),0)/Math.max(vs.length,1)
    const catches = vs.reduce((s,x)=>s+(x.catches_count||0),0)/Math.max(vs.length,1)
    return { draft: d, scores: vs, mean, catches }
  })
)

const ranked = scored.filter(Boolean).sort((a,b)=> (b.mean+b.catches) - (a.mean+a.catches))
log(ranked.map(r=>`${r.draft.angle}: score ${r.mean.toFixed(1)}, catches ${r.catches.toFixed(1)}/6`).join(' · '))

phase('Synthesize')
const final = await agent(
  `Synthesize the FINAL skill from a judged panel of ${ranked.length} drafts.

WINNER (highest combined score + acceptance-test catches):
${JSON.stringify({angle: ranked[0].draft.angle, name: ranked[0].draft.name, description: ranked[0].draft.description, body: ranked[0].draft.body_markdown}, null, 1).slice(0,90000)}

JUDGE VERDICTS ON THE WINNER:
${JSON.stringify(ranked[0].scores.map(s=>({lens:s.lens, score:s.score, catches:s.catches_count, flaws:s.fatal_flaws, strongest:s.strongest_element})), null, 1).slice(0,20000)}

RUNNERS-UP — graft their strongest elements, named by the judges:
${JSON.stringify(ranked.slice(1).map(r=>({angle:r.draft.angle, mean:r.mean, body:r.draft.body_markdown.slice(0,14000), strongest:r.scores.map(s=>s.strongest_element), flaws:r.scores.map(s=>s.fatal_flaws)})), null, 1).slice(0,90000)}

${EVIDENCE}

Produce the final committable SKILL.md — frontmatter description plus body. Fix every fatal flaw the judges named. Graft the runner-up elements they singled out. Cite only measured numbers. End the body with an explicit, honest statement of which of the six failures the skill does NOT catch and why, because this estate treats undisclosed limits as the real defect.

Return the complete file content as your final text, starting with the YAML frontmatter.`,
  { label: 'synthesize', phase: 'Synthesize', effort: 'high' }
)

return {
  ranking: ranked.map(r => ({ angle: r.draft.angle, mean: +r.mean.toFixed(2), catches: +r.catches.toFixed(2),
    verdicts: r.scores.map(s=>s.verdict), flaws: r.scores.flatMap(s=>s.fatal_flaws||[]) })),
  final_skill: final,
}
