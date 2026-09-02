export const meta = {
  name: 'eap-false-done-ledger',
  description: 'Read the EAP fortnight corpus (superbot docs/eap + fleet-manager EAP docs) and build the false-done ledger: every claim of done/complete/shipped, matched against what was later found true',
  phases: [
    { title: 'Read', detail: 'one reader per file (48: 32 superbot docs/eap, 16 fleet-manager EAP docs), split any file over 400 lines by line range' },
    { title: 'Merge', detail: 'correlate claims against corrections across all readers into ledger rows' },
    { title: 'Verify', detail: 'two refuting lenses per row (holds? real false-done, not just plan evolution or already-known?); same survival rule as Fleet A' },
    { title: 'Critic', detail: 'completeness critic — what was not read, what looks thin' },
  ],
}

// ---- aggregation contract (fleet-preflight § 1) — asserted before any agent spawns, same rule as Fleet A (04-eap-mail-evidence-pass.js)
// FIXED (Codex review, fm #1010): the READER prompt tells verifiers to leave already_covered_by
// an empty string when nothing is covered, but a verifier that instead writes negative prose
// ("none — ...", "not covered by ...") is not caught by a bare truthiness check — both lenses
// doing this would wrongly kill a surviving row via the coverage branch. Normalize first.
// FIXED (Codex review round 2, fm #1010): "n/a — ..." is another negative form real verifier
// output actually used ("n/a — neither ..."), not caught by the round-1 regex. Broadened.
const isNegativeCoverage = (s) => !s || /^\s*(none|n\/a|not\s+covered|no\b)/i.test(s)
const dies = (a, b) => (a.refuted || b.refuted) || (!isNegativeCoverage(a.already_covered_by) && !isNegativeCoverage(b.already_covered_by))
const FIX = [
  [{ refuted: true,  already_covered_by: '' }, { refuted: false, already_covered_by: '' }, true ],
  [{ refuted: false, already_covered_by: 'traps.md TRAP-006' }, { refuted: false, already_covered_by: 'redirect doc' }, true ],
  [{ refuted: false, already_covered_by: '' }, { refuted: false, already_covered_by: '' }, false ],
  [{ refuted: false, already_covered_by: 'none — not docs/traps.md, nearest is TRAP-003' }, { refuted: false, already_covered_by: 'n/a — neither file names this pattern' }, false ],
]
for (const [a, b, exp] of FIX) { if (dies(a, b) !== exp) throw new Error('aggregation fixture failed') }
log('aggregation fixtures: 2 kill, 2 survive — pass; fields read: refuted, already_covered_by (negative-prose normalized, incl. n/a)')

const FM = (typeof args === 'object' && args && args.fm) || '/home/user/fleet-manager'
const SB = (typeof args === 'object' && args && args.sb) || '/tmp/eap-night/superbot-eap'
const JUDGE_MODEL = (typeof args === 'object' && args && args.judgeModel) || undefined
const PILOT_ONLY = Boolean(typeof args === 'object' && args && args.pilotOnly)
const SKIP_SATELLITE = Boolean(typeof args === 'object' && args && args.skipSatellite)
log(`paths: fm=${FM} sb=${SB} · verify/critic model=${JUDGE_MODEL || 'session default'} · pilotOnly=${PILOT_ONLY} · skipSatellite=${SKIP_SATELLITE}`)

const TASK = `You are one reader in a multi-agent pass building a FALSE-DONE LEDGER for Menno's estate: a table of every claim of "done" / "complete" / "shipped" / "working" / "finished" / "landed" made during the EAP fortnight (July 2026, the Anthropic Early Access Program on the /superbot production Discord bot), matched against what was later found to actually be true. This is not the mail-evidence pass (a sibling fleet handles that) — this fleet's ONLY product is the ledger. The owner's own words about this: "I noticed that much of the work that was claimed to be complete was in fact not complete at all." Turn that sentence into countable rows.`

const READ_RULES = `READING RULES (non-negotiable):
- Read the WHOLE file (or your assigned line range) in slices: sed -n '1,220p' FILE, then '221,440p', and so on until past the last line (or the end of your assigned range). Never rely on head, grep -l, or a listing to characterise content.
- Copy every claim and every correction VERBATIM or near-verbatim with its exact citation. Never paraphrase away the specific words ("done", "complete", "shipped", "working", "fixed", "resolved", "landed", "ready") that make it a done-claim.
- Copy every number verbatim with its stated method, date and unit. Never round, never recompute.
- Certainty: report the tag the source itself uses (MEASURED / MEASURED-PRIOR / OWNER / REASONED / REVIEWED / UNVERIFIED / DERIVED) or "unstated".
- Citations are FILE:LINE-RANGE of what you actually read. Do not cite anything you did not open.
- Do not write, create or modify any file. Read only. Your final message must be the structured output only.`

const READER_B = { type: 'object', required: ['source', 'date', 'method', 'claims', 'corrections', 'self_stated_limits'], properties: {
  source: { type: 'string' }, date: { type: 'string' }, method: { type: 'string' },
  claims: { type: 'array', items: { type: 'object', required: ['statement', 'citation', 'date_stated', 'certainty'], properties: {
    statement: { type: 'string' }, citation: { type: 'string' }, date_stated: { type: 'string' }, certainty: { type: 'string' },
    topic: { type: 'string' } } } },
  corrections: { type: 'array', items: { type: 'object', required: ['statement', 'citation', 'date_stated', 'certainty', 'refers_to'], properties: {
    statement: { type: 'string' }, citation: { type: 'string' }, date_stated: { type: 'string' }, certainty: { type: 'string' },
    refers_to: { type: 'string' }, topic: { type: 'string' } } } },
  self_stated_limits: { type: 'array', items: { type: 'string' } } } }

const ROW = { type: 'object', required: ['id', 'claim', 'claimed_where', 'claimed_when', 'actually', 'found_when', 'found_by', 'citation_claim', 'citation_found'], properties: {
  id: { type: 'string' }, claim: { type: 'string' }, claimed_where: { type: 'string' }, claimed_when: { type: 'string' },
  actually: { type: 'string' }, found_when: { type: 'string' }, found_by: { type: 'string' },
  citation_claim: { type: 'string' }, citation_found: { type: 'string' }, certainty: { type: 'string' } } }

const ROWS = { type: 'object', required: ['rows', 'orphaned_corrections'], properties: {
  rows: { type: 'array', items: ROW },
  orphaned_corrections: { type: 'array', items: { type: 'object', required: ['statement', 'citation', 'reason'], properties: {
    statement: { type: 'string' }, citation: { type: 'string' }, reason: { type: 'string' } } } } } }

const VERDICT = { type: 'object', required: ['refuted', 'already_covered_by', 'what_i_opened', 'discrepancies', 'corrected_claim'], properties: {
  refuted: { type: 'boolean' }, already_covered_by: { type: 'string' }, what_i_opened: { type: 'array', items: { type: 'string' } },
  discrepancies: { type: 'array', items: { type: 'string' } }, corrected_claim: { type: 'string' } } }

const CRITIC = { type: 'object', required: ['missing_sources', 'unverified_claims', 'overlap_unchecked', 'other_gaps'], properties: {
  missing_sources: { type: 'array', items: { type: 'string' } }, unverified_claims: { type: 'array', items: { type: 'string' } },
  overlap_unchecked: { type: 'array', items: { type: 'string' } }, other_gaps: { type: 'array', items: { type: 'string' } } } }

function readerPrompt(path, range, note) {
  const rangeNote = range ? ` Read ONLY lines ${range[0]}-${range[1]} (this file is split across two readers; a sibling reads the rest) — read that slice in full with sed -n.` : ' Read the whole file.'
  return `${TASK}
Your source: ${path}.${rangeNote} ${note || ''}
Extract two things, separately:
1. CLAIMS — every place the source asserts something is done / complete / shipped / working / finished / landed / resolved / ready, **made ON OR BEFORE 2026-07-21 (the EAP fortnight's close) — this ledger is about false-dones made DURING the EAP fortnight, not the estate's later history.** A retrospective written after 07-21 that quotes or restates an in-window claim still counts (extract the claim with its original in-window date, not the retrospective's date); a NEW claim first asserted after 07-21 does not belong in this pool at all — skip it, it is not this ledger's subject. For each in-window claim: the exact statement, its citation, the date it was made (from the file's own date or header if the line has none), and topic (one or two words, e.g. "automerger", "watch-filter", "classifier").
2. CORRECTIONS — every place the source says something was actually still broken/incomplete/wrong, retracts or corrects an earlier claim, or reports something "found later" / "turned out" / "still not" / "actually" — **no date restriction on corrections**, since a correction found weeks or months after the fortnight is exactly the pattern this ledger measures. With the exact statement, citation, date, topic, and refers_to (in your own words, what earlier claim this corrects, if the source says or implies it — otherwise "unstated").
A single file may contain BOTH a claim and its own later correction (a retrospective often does). Extract every instance of each, do not summarise them together.
${READ_RULES}`
}

// ---------------- Phase 1: readers — one per file, split files over 400 lines ----------------
phase('Read')
const SB_FILES = [
  { path: `${SB}/fleet-manifest.md` }, { path: `${SB}/gen1-wrapup-email-part1-questions-2026-07-09.md` },
  { path: `${SB}/NEXT-SESSION-finalize-email.md` }, { path: `${SB}/codex-review-round-verification-2026-07-10.md` },
  { path: `${SB}/2026-07-18-dewall-capabilities-evidence.md` }, { path: `${SB}/anthropic-email-4-classifier-regression-sent-2026-07-16.md` },
  { path: `${SB}/2026-07-18-followup-email-draft.md` }, { path: `${SB}/fleet-overnight-review-2026-07-10.md` },
  { path: `${SB}/session-handoff-2026-07-11-fleet-management.md` }, { path: `${SB}/gen1-wrapup-email-draft-v2-2026-07-09.md` },
  { path: `${SB}/superbot-next-runtime-review-2026-07-10.md` }, { path: `${SB}/README.md` },
  { path: `${SB}/anthropic-email-3-draft-2026-07-13.md` }, { path: `${SB}/night-review-2026-07-12.md` },
  { path: `${SB}/eap-program-review-2026-07-10.md` }, { path: `${SB}/campaign-self-audit-2026-07-08.md` },
  { path: `${SB}/fleet-winddown-audit-2026-07-09.md` }, { path: `${SB}/night-review-2026-07-11.md` },
  { path: `${SB}/fleet-review-2026-07-09.md` }, { path: `${SB}/email-attachment-set-2026-07-12.md` },
  { path: `${SB}/fleet-cleanup-audit-2026-07-13.md` }, { path: `${SB}/hostile-audit-checking-the-checkers-2026-07-10.md` },
  { path: `${SB}/fleet-quality-review-2026-07-09.md` }, { path: `${SB}/night-review-2026-07-13.md` },
  { path: `${SB}/permission-classifier-findings-consolidated-2026-07-16.md` }, { path: `${SB}/gen1-gen2-doctrine-review-2026-07-10.md` },
  { path: `${SB}/gen1-grand-review-2026-07-09.md` }, { path: `${SB}/external-review-pack-2026-07-09.md` },
  { path: `${SB}/gen1-wrapup-email-final-candidate.md`, split: [[1, 220], [221, 425]] },
  { path: `${SB}/anthropic-email-2-draft-2026-07-11.md`, split: [[1, 310], [311, 608]] },
]
const FM_FILES = [
  { path: `${FM}/docs/eap-audit-collection.md` }, { path: `${FM}/docs/eap-final-recon-2026-07-14.md` },
  { path: `${FM}/docs/fleet-inconsistencies-2026-07-13.md` }, { path: `${FM}/docs/pr-landing-audit-2026-07-16.md` },
  { path: `${FM}/docs/audits/eap-project-audit-2026-07-14.md` }, { path: `${FM}/docs/fleet-account-2026-07-26.md` },
  { path: `${FM}/docs/eap-story.md`, split: [[1, 300], [301, 580]] },
  { path: `${FM}/docs/eap-retrospective.md`, split: [[1, 220], [221, 427]] },
  { path: `${FM}/docs/launch-readiness-2026-07-10.md`, split: [[1, 360], [361, 710]] },
  { path: `${FM}/docs/dispatch-log.md`, split: [[1, 340], [341, 671]] },
  { path: `${FM}/docs/PROJECT-CLOSEOUT.md`, split: [[1, 210], [211, 414]] },
]

function expand(files, tag) {
  const out = []
  for (const f of files) {
    if (f.split) f.split.forEach((r, i) => out.push({ path: f.path, range: r, label: `${tag}:${f.path.split('/').pop()}[${r[0]}-${r[1]}]` }))
    else out.push({ path: f.path, range: null, label: `${tag}:${f.path.split('/').pop()}` })
  }
  return out
}
let SB_UNITS = expand(SB_FILES, 'sb')
let FM_UNITS = expand(FM_FILES, 'fm')
if (PILOT_ONLY) {
  // pilot: one fleet-manager split-file half, one superbot split-file half, chosen to pilot the split-by-line-range mechanic itself (05-CONTRACTS-night.md PILOT line)
  FM_UNITS = FM_UNITS.filter(u => u.label === 'fm:eap-story.md[1-300]' || u.label === 'fm:PROJECT-CLOSEOUT.md[1-210]')
  SB_UNITS = SB_UNITS.filter(u => u.label === 'sb:anthropic-email-2-draft-2026-07-11.md[1-310]')
} else if (SKIP_SATELLITE) {
  SB_UNITS = []
}
log(`reader units: superbot ${SB_UNITS.length} (from ${SB_FILES.length} files) · fleet-manager ${FM_UNITS.length} (from ${FM_FILES.length} files)`)

const fmReads = parallel(FM_UNITS.map(u => () => agent(readerPrompt(u.path, u.range, 'This is a fleet-manager estate record about the EAP fortnight.'), { label: u.label, phase: 'Read', schema: READER_B })))
const sbReads = parallel(SB_UNITS.map(u => () => agent(readerPrompt(u.path, u.range, 'This is a superbot docs/eap record, written live during the EAP fortnight.'), { label: u.label, phase: 'Read', schema: READER_B })))
const [fmOutRaw, sbOutRaw] = await Promise.all([fmReads, sbReads])
const fmOut = fmOutRaw.filter(Boolean), sbOut = sbOutRaw.filter(Boolean)
log(`readers: fleet-manager ${fmOut.length}/${FM_UNITS.length} · superbot ${sbOut.length}/${SB_UNITS.length}`)
if (fmOut.length < FM_UNITS.length) log(`DROPPED fm units: ${FM_UNITS.filter((u, i) => !fmOutRaw[i]).map(u => u.label).join(', ')}`)
if (sbOut.length < SB_UNITS.length) log(`DROPPED sb units: ${SB_UNITS.filter((u, i) => !sbOutRaw[i]).map(u => u.label).join(', ')}`)
// FIXED (Codex review round 2, fm #1010): the deterministic FM_UNITS/SB_UNITS labels (which
// carry the split range, e.g. "fm:eap-story.md[301-580]"), index-aligned to the raw results,
// not the model-authored `source` field a reader can render as a bare path missing its range.
const fmOkLabels = FM_UNITS.filter((u, i) => fmOutRaw[i]).map(u => u.label)
const sbOkLabels = SB_UNITS.filter((u, i) => sbOutRaw[i]).map(u => u.label)
const allReaders = [...fmOut, ...sbOut]
const totalClaims = allReaders.reduce((n, r) => n + r.claims.length, 0)
const totalCorrections = allReaders.reduce((n, r) => n + r.corrections.length, 0)
log(`extracted: ${totalClaims} claims, ${totalCorrections} corrections across ${allReaders.length} reader units`)

// ---------------- Phase 2: merge (barrier is correct: correlate claims × corrections across ALL readers) ----------------
phase('Merge')
const mergeRules = `Rules: a ledger ROW requires BOTH a claim (something asserted done/complete/shipped) AND a correction that reverses or qualifies it (found still broken, incomplete, wrong, or retracted) — from the same topic, even if from different files or different dates. Match by topic and by what the statements are actually about, not just by shared keywords. claimed_where/claimed_when/citation_claim come from the claim; actually/found_when/found_by/citation_found come from the correction (found_by = who/what found it — a named audit, a named session, the owner, a specific review round — copy from the correction's context, or "unstated" if the source does not say). Copy statements close to verbatim; do not soften "done" into "attempted" or invent a false-done where the source only shows normal iteration (a plan that was always described as in-progress, then finished, is NOT a false-done). A claim with no correction anywhere in the pool is NOT a row — do not manufacture one. A correction with no matching claim anywhere in the pool goes into orphaned_corrections with a reason (e.g. "no earlier done-claim found in this corpus for this topic"). Do not open files; work only from the extractions. Final message: the structured output only.`
const claimPool = allReaders.flatMap(r => r.claims.map(c => ({ ...c, source: r.source })))
const correctionPool = allReaders.flatMap(r => r.corrections.map(c => ({ ...c, source: r.source })))
log(`pool: ${claimPool.length} claims, ${correctionPool.length} corrections`)

// split correction pool into groups; each merge group gets the FULL claim pool (it must search across all claims) plus its own slice of corrections
const CHUNK = 40
const corrGroups = []
for (let i = 0; i < correctionPool.length; i += CHUNK) corrGroups.push(correctionPool.slice(i, i + CHUNK))
if (corrGroups.length === 0) corrGroups.push([])
log(`merge groups: ${corrGroups.length} × up to ${CHUNK} corrections, each searched against all ${claimPool.length} claims`)

const mergePartsRaw = await parallel(corrGroups.map((g, gi) => () =>
  agent(`${TASK}
You build ledger ROWS for group ${gi + 1} of ${corrGroups.length} of the corrections pool below, by finding each one's matching earlier claim in the FULL claims pool. Produce up to ${CHUNK} rows, one per correction in this group that has a matching claim (ids R${gi + 1}-1..R${gi + 1}-${CHUNK}) — every correction in this group that matches a claim gets a row; do not drop a genuine match to stay under a smaller count.
${mergeRules}
CORRECTIONS (this group): ${JSON.stringify(g)}
FULL CLAIMS POOL (search this for matches): ${JSON.stringify(claimPool)}`,
    { label: `merge R${gi + 1}: corrections → rows`, phase: 'Merge', schema: ROWS, model: JUDGE_MODEL })))
// FIXED (Codex review round 3, fm #1010): a plain filter(Boolean) here silently dropped a whole
// group's up-to-CHUNK corrections (never in ledger rows, never in orphaned_corrections, never
// logged) if its merge agent errored. Keep index alignment so a failed group is named and its
// raw corrections are preserved for the critic instead of vanishing.
const mergeParts = mergePartsRaw.filter(Boolean)
const failedGroups = corrGroups.filter((g, i) => !mergePartsRaw[i])
const unprocessedCorrections = corrGroups.flatMap((g, i) => mergePartsRaw[i] ? [] : g)
if (failedGroups.length) log(`MERGE GROUP FAILURES: ${failedGroups.length}/${corrGroups.length} groups returned null — ${unprocessedCorrections.length} corrections never became rows or orphans, preserved in unprocessedCorrections`)

const mergedRows = mergeParts.flatMap(m => m.rows || [])
const orphaned = mergeParts.flatMap(m => m.orphaned_corrections || [])
log(`merged: ${mergedRows.length} candidate rows, ${orphaned.length} orphaned corrections${failedGroups.length ? `, ${unprocessedCorrections.length} unprocessed (${failedGroups.length} failed groups)` : ''}`)

// KNOWN LIMIT (Codex review, fm #1010, not fully fixed): with 150 input rows the model can only
// surface ~30-45 total in one call — rows beyond that cap vanish with no "dropped" marker at all,
// which is different from (and worse than) the rows this prompt DOES mark dropped. A real fix is to
// batch this stage like the merge stage above; not done here for time. Disclosed, not silently shipped.
const dedup = await agent(`${TASK}
Deduplicate and rank the candidate ledger rows below (produced by ${corrGroups.length} parallel merge groups, so the same false-done may appear more than once from different angles). Return one ranked list of at most 45 rows: merge any two describing the same underlying false-done (keep both citations), rank by how clearly it shows a "claimed done, actually not" pattern with a solid citation on both sides. Drop nothing silently within your budget — a row you drop must still appear, marked with certainty "dropped" and the reason in the actually field; if you must omit a row entirely for space, prefer omitting near-duplicates of a row you kept over omitting a row describing a distinct mechanism.
ROWS: ${JSON.stringify(mergedRows)}
Do not open files. Final message: the structured output only.`, { label: 'dedupe + rank rows', phase: 'Merge', schema: ROWS, model: JUDGE_MODEL })
// FIXED (Codex review round 4, fm #1010): if this single dedup agent call fails, the old
// `[]` fallback discarded ALL 150 merged rows silently -- verify and the critic got nothing,
// the run "succeeded," and the return showed ranked:0 with no trace of what was lost. Fall
// back to the pre-dedup mergedRows (undeduplicated, unranked, but not lost) and say so.
const dedupFailed = !(dedup && dedup.rows)
if (dedupFailed) log(`DEDUPE FAILED: falling back to ${mergedRows.length} undeduplicated merged rows (near-duplicates likely present, none lost)`)
const ranked = (dedupFailed ? mergedRows : dedup.rows).filter(Boolean)
const toVerify = ranked.filter(r => r.certainty !== 'dropped').slice(0, 30)
const rankedButUnverified = ranked.filter(r => r.certainty !== 'dropped').slice(30)
log(`ranked ${ranked.length}; verifying ${toVerify.length}; ranked-but-unverified (slice cap) ${rankedButUnverified.length}; marked dropped by dedupe ${ranked.filter(r => r.certainty === 'dropped').length}; NOTE: rows the dedupe agent omitted entirely (150 merged -> at most 45 returned) never reach this log at all — known limit, see the comment above the dedupe call`)

// ---------------- Phase 3: verify (pipelined; two refuting lenses per row, same rule as Fleet A) ----------------
phase('Verify')
function verifyHolds(r) {
  return `You are an adversarial verifier for a false-done ledger row. Your job is to REFUTE this row if it does not hold. Default to refuted=true when you cannot confirm it from the cited lines.
ROW: ${JSON.stringify(r)}
Open BOTH citations (citation_claim and citation_found) under ${FM} or ${SB} with sed -n. Check: does citation_claim actually assert the thing was done/complete/shipped, in those words or unmistakably that meaning? Does citation_found actually show it was NOT true, contradicting or correcting the claim? Read to the end of the paragraph or section for a qualifier that reverses the read. Are the dates right (claimed_when before found_when)? If the row is essentially right but a date, a citation line, or a word is off, set refuted=false and put the exact fix in corrected_claim. Leave already_covered_by empty unless you personally find this exact false-done already named in docs/traps.md (TRAP-006, TRAP-007) or docs/planning/2026-08-30-fresh-start-redirect.md's "what killed the last rebuild" section — then name it. Read only; never write. Final message: the structured output only.`
}
function verifyFit(r) {
  return `You are an adversarial verifier for a false-done ledger row, with the FIT lens: refute (refuted=true) if this is NOT actually a false-done — e.g. it is normal iterative design (a plan always described as in-progress that later finished on schedule), the "claim" was already hedged/scoped honestly at the time, the "correction" is a routine follow-on rather than a retraction, or the dates don't support claimed-before-found. Also check: is this the SAME pattern already named in docs/traps.md or the fresh-start-redirect doc's account of the failed rebuild? If so put that file in already_covered_by (it still belongs in the ledger, but marked as already-known plumbing, not a fresh finding). List every file you opened in what_i_opened.
ROW: ${JSON.stringify(r)}
Read only; never write. Final message: the structured output only.`
}
const verified = await pipeline(toVerify,
  r => parallel([() => agent(verifyHolds(r), { label: `holds? ${r.id}`, phase: 'Verify', schema: VERDICT, effort: 'high', model: JUDGE_MODEL }),
                 () => agent(verifyFit(r), { label: `fit? ${r.id}`, phase: 'Verify', schema: VERDICT, effort: 'high', model: JUDGE_MODEL })]),
  (vs, r) => {
    const [a, b] = vs
    if (!a || !b) return { row: r, a, b, survives: false, reason: 'a verifier returned null' }
    const d = dies(a, b)
    return { row: r, a, b, survives: !d, reason: d ? (a.refuted || b.refuted ? 'refuted' : 'already covered per both lenses') : 'survives' }
  })
const results = verified.filter(Boolean)
const survivors = results.filter(r => r.survives)
log(`verify: ${survivors.length}/${results.length} survive · refuted ${results.filter(r => r.reason === 'refuted').length} · covered ${results.filter(r => r.reason.startsWith('already')).length}`)

// ---------------- Phase 4: completeness critic ----------------
phase('Critic')
// FIXED (Codex review, fm #1010): this prompt used to pass the PLANNED file lists (FM_FILES/SB_FILES)
// as "READ" regardless of skipSatellite/pilotOnly, so a critic on a skipSatellite run wrongly concluded
// the full superbot corpus was read. Use the ACTUAL executed reader sources instead. Also pass each
// survivor/non-survivor's full verifier records (both lenses' what_i_opened/discrepancies/corrected_claim/
// already_covered_by), not just id/claim/actually/reason — the critic could not previously audit
// thin verification or a meaning-changing correction without them.
const critic = await agent(`You are the completeness critic for a multi-agent pass building the EAP false-done ledger. Below is what was ACTUALLY read (not the planned corpus — some lanes may have been cut for time), what survived verification with both lenses' full records, and what was dropped. Say what is MISSING: sources under ${FM}/docs (EAP-related) or ${SB} that should have been read and were not; surviving rows whose verification looks thin (a verifier that opened nothing, or a corrected_claim that changes the row's meaning — check each survivor's a/b corrected_claim against its row's claim/actually for exactly this); orphaned corrections that plausibly DO have a matching claim somewhere the merge missed; and any other gap. Be concrete and short.
READ: fleet-manager ${JSON.stringify(fmOkLabels)} (${fmOut.length}/${FM_UNITS.length} units) · superbot ${JSON.stringify(sbOkLabels)} (${sbOut.length}/${SB_UNITS.length} units) — labels carry the split range where one applies; a file with only one of its two range-labels present here had its other half fail or get cut
SURVIVORS (with full verifier records): ${JSON.stringify(survivors.map(r => ({ id: r.row.id, claim: r.row.claim, actually: r.row.actually, lens_holds: r.a, lens_fit: r.b })))}
NON-SURVIVORS: ${JSON.stringify(results.filter(r => !r.survives).map(r => ({ id: r.row.id, claim: r.row.claim, reason: r.reason, lens_holds: r.a, lens_fit: r.b })))}
ORPHANED CORRECTIONS: ${JSON.stringify(orphaned)}
MARKED DROPPED BY DEDUPE (with a stated reason): ${JSON.stringify(ranked.filter(r => r.certainty === 'dropped'))}
RANKED BUT NEVER VERIFIED (slice(0,30) cap on the verify stage, not marked dropped): ${JSON.stringify(rankedButUnverified)}
UNPROCESSED CORRECTIONS (their merge group's agent errored — never became rows or orphans): ${JSON.stringify(unprocessedCorrections)}
Read only; never write. Final message: the structured output only.`, { label: 'completeness critic', phase: 'Critic', schema: CRITIC, effort: 'high', model: JUDGE_MODEL })

return {
  contract: 'see 05-CONTRACTS-night.md beside this script',
  counts: { fm_units: FM_UNITS.length, sb_units: SB_UNITS.length, fm_ok: fmOut.length, sb_ok: sbOut.length,
    claims: claimPool.length, corrections: correctionPool.length, merged: mergedRows.length, orphaned: orphaned.length,
    ranked: ranked.length, verified: results.length, survivors: survivors.length, failed_merge_groups: failedGroups.length,
    unprocessed_corrections: unprocessedCorrections.length },
  readers: allReaders,
  ranked,
  ranked_but_unverified: rankedButUnverified,
  verified: results,
  orphaned_corrections: orphaned,
  unprocessed_corrections: unprocessedCorrections,
  critic,
}
