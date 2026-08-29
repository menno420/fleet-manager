import os, re, json, glob, hashlib
ROOT='corpus'
SEC_PAT = re.compile(r'^(#{2,4})\s+(.*)$')
# sections that carry agent-error evidence
WANT = re.compile(r'(previous[- ]session review|friction|self[- ]initiated|what went wrong|correction|disposition|review disposition|lesson|trap|regression|postmortem|post-mortem|missteps?|mistake|guard|drift|honest state|deviation)', re.I)
ERR_LEX = re.compile(r"""(\[conceded\]|\[survived\]|\[partial\]|conceded|retracted|was wrong|were wrong|got it wrong|incorrect(?:ly)?|should have|shouldn't have|failed to|forgot to|skipped the|never ran|did not run|didn't run|false (?:claim|positive|negative|wall)|overclaim|over-?stated|unverified claim|assumed|assumption was|misread|mis-?identified|violat\w+|breach\w*|guard fired|hook blocked|blocked by|caught by|the trap|regressi\w+|broke |broken by|flake|stale|drift\w*|not measured|inferred|hallucinat\w+|invented|fabricat\w+)""", re.I|re.X)
rows=[]
for repo in sorted(os.listdir(ROOT)):
    paths=[]
    for dp,dn,fn in os.walk(f'{ROOT}/{repo}'):
        for n in fn:
            if n.endswith('.md'): paths.append(os.path.join(dp,n))
    for path in paths:
        rel = os.path.relpath(path, f'{ROOT}/{repo}')
        try: txt=open(path, encoding='utf-8', errors='replace').read()
        except Exception: continue
        lines=txt.split('\n')
        # split into sections
        cur=None; buf=[]; start=0
        secs=[]
        for i,l in enumerate(lines):
            m=SEC_PAT.match(l)
            if m:
                if cur is not None: secs.append((cur,start,buf))
                cur=m.group(2).strip(); buf=[]; start=i+1
            elif cur is not None: buf.append(l)
        if cur is not None: secs.append((cur,start,buf))
        for title,ln,body in secs:
            b='\n'.join(body).strip()
            if not b: continue
            hit_sec = bool(WANT.search(title))
            hits = ERR_LEX.findall(b)
            if not hit_sec and len(hits)<2: continue
            if len(b) > 6000: b = b[:6000]+'\n…[truncated]'
            rows.append({'repo':repo,'file':rel,'line':ln,'section':title,
                         'err_hits':len(hits),'section_match':hit_sec,'text':b})
with open('evidence.jsonl','w') as f:
    for r in rows: f.write(json.dumps(r)+'\n')
print('sections extracted:', len(rows))
import collections
print('by repo:'); 
for k,v in collections.Counter(r['repo'] for r in rows).most_common(): print(f'  {k:24}{v}')
print('total chars:', sum(len(r['text']) for r in rows))
