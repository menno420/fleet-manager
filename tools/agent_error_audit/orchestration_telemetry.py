import json, os, glob, re, datetime, collections
BASE='/root/.claude/projects/-home-user-fleet-manager/5c635c91-40a8-50d4-a884-7c6e9a2b0388/subagents/workflows'
def parse(ts): return datetime.datetime.fromisoformat(ts.replace('Z','+00:00'))
def classify(prompt):
    p=prompt[:400].lower()
    if 'read the whole file' in p and 'shard-' in p: return 'harvest:cards'
    if 'rshards/owner' in p: return 'harvest:owner'
    if 'rshards/codex' in p: return 'harvest:codex'
    if 'census the agent-instruction surface' in p: return 'census'
    if 'synthesis lane' in p: return 'synthesize'
    if 'adversarially verify' in p: return 'verify'
    if 'completeness critic' in p or 'critic' in p: return 'critic'
    if 'prescription' in p or 'improvement prescription' in p: return 'prescribe'
    return 'other'
agents=[]
for wf in ('wf_9781a5e1-7af','wf_b8da4e25-5a3'):
    for f in glob.glob(f'{BASE}/{wf}/agent-*.jsonl'):
        try: rows=[json.loads(l) for l in open(f) if l.strip()]
        except Exception: continue
        if not rows: continue
        ts=[parse(r['timestamp']) for r in rows if r.get('timestamp')]
        if not ts: continue
        out=sum((r.get('message') or {}).get('usage',{}).get('output_tokens',0) for r in rows if r.get('type')=='assistant')
        cr =sum((r.get('message') or {}).get('usage',{}).get('cache_read_input_tokens',0) for r in rows if r.get('type')=='assistant')
        first=next((r for r in rows if r.get('type')=='user'), None)
        c=(first or {}).get('message',{}).get('content','')
        if isinstance(c,list): c=' '.join(str(x.get('text','')) for x in c if isinstance(x,dict))
        agents.append({'wf':wf,'start':min(ts),'end':max(ts),'out':out,'cache_read':cr,
                       'lane':classify(str(c)), 'msgs':len(rows),
                       'tools':sum(1 for r in rows if r.get('type')=='user' and 'tool_result' in str(r.get('message',{}))[:200])})
print(f"agents with transcripts: {len(agents)}")
t0=min(a['start'] for a in agents); t1=max(a['end'] for a in agents)
print(f"span: {t0:%H:%M:%S} → {t1:%H:%M:%S}  ({(t1-t0).total_seconds()/3600:.1f} h wall clock)\n")

# --- real concurrency, sampled every 15s ---
step=15; conc=[]
cur=t0
while cur<=t1:
    conc.append(sum(1 for a in agents if a['start']<=cur<=a['end']))
    cur+=datetime.timedelta(seconds=step)
import statistics
nz=[c for c in conc if c>0]
print("=== ACTUAL CONCURRENCY (15s samples) ===")
print(f"  peak={max(conc)}  mean(active)={statistics.mean(nz):.1f}  median(active)={statistics.median(nz):.0f}")
hist=collections.Counter(conc)
print("  distribution:", ", ".join(f"{k}:{v}" for k,v in sorted(hist.items()) if k>0))
print(f"  samples at 0 agents (idle): {hist[0]} of {len(conc)} ({100*hist[0]//len(conc)}%)")

# --- per-lane cost ---
print("\n=== COST BY LANE TYPE ===")
print(f"{'lane':18}{'n':>5}{'out tok':>12}{'% out':>7}{'mean dur':>10}{'median dur':>12}")
tot=sum(a['out'] for a in agents)
for lane,items in sorted(collections.Counter(a['lane'] for a in agents).most_common(), key=lambda x:-x[1]):
    g=[a for a in agents if a['lane']==lane]
    o=sum(a['out'] for a in g)
    durs=sorted((a['end']-a['start']).total_seconds() for a in g)
    print(f"{lane:18}{len(g):>5}{o:>12,}{100*o//max(tot,1):>6}%{statistics.mean(durs):>9.0f}s{statistics.median(durs):>11.0f}s")
print(f"{'TOTAL':18}{len(agents):>5}{tot:>12,}")
json.dump({'peak':max(conc),'mean_active':statistics.mean(nz),'agents':len(agents),'out':tot}, open('orch.json','w'))
