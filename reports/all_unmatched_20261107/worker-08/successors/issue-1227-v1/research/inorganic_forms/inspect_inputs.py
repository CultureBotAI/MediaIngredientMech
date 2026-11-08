import sys, json, pathlib, hashlib, subprocess, re, html, yaml
ROOT=pathlib.Path('reports/all_unmatched_20261107/worker-08')
OUT=ROOT/'successors/issue-1227-v1/research/inorganic_forms'
A=json.loads((OUT/'assignment.json').read_text())
E0=json.loads((ROOT/'successors/issue-1201-v1/evidence.json').read_text())
E={x['evidence_id']:x for x in (E0['evidence'] if isinstance(E0,dict) else E0)}
CASES=json.loads((ROOT/'provenance/shard-08.json').read_text())['cases']
C={x['case_id']:x for x in CASES}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def compact(obj):
    strings={};defs={}
    def rec(x):
        if isinstance(x,str) and len(x)>150:
            if x not in strings:
                k='S'+str(len(strings)+1);strings[x]=k;defs[k]=x
            return {'$text':strings[x]}
        if isinstance(x,dict):return {k:rec(v) for k,v in x.items()}
        if isinstance(x,list):return [rec(v) for v in x]
        return x
    out=rec(obj);return json.dumps({'strings':defs,'document':out},ensure_ascii=False,separators=(',',':'))
def log(kind,path,scope):
    with (OUT/'inspection-log.jsonl').open('a') as f:f.write(json.dumps({'kind':kind,'path':str(path),'sha256':sha(path),'scope_rendered':scope})+'\n')
def source(eid):
    e=E[eid];cap=e['capture'];p=ROOT/cap['path']
    if cap['root']!='artifact':print('NON_ARTIFACT',json.dumps(e));return
    print('SOURCE',eid,e.get('url'),e.get('accessed_at'),cap)
    b=p.read_bytes()
    if b.startswith(b'%PDF'):s=subprocess.check_output(['pdftotext','-layout',str(p),'-']).decode()
    else:s=b.decode(errors='replace')
    if '<html' in s.lower() or '<!doctype' in s.lower():
        s=re.sub(r'<(script|style)\b[^>]*>.*?</\1>','',s,flags=re.S|re.I);s=html.unescape(re.sub('<[^>]*>',' ',s));s=re.sub(r'[ \t]+',' ',s);s=re.sub(r'\n\s*\n+','\n',s)
    try:
        d=json.loads(s)
        def trim(x):
            if isinstance(x,dict):return {k:trim(v) for k,v in x.items() if k not in ['roles','properties','_links','gmo']}
            if isinstance(x,list):return [trim(v) for v in x]
            return x
        print(compact(trim(d)))
    except ValueError:print(s)
    log('primary:'+eid,p,'Actual source scientific fields; automatic roles/properties omitted from display, not treated as chemical authority.')
mode=sys.argv[1]
if mode=='payloads':
    for i in map(int,sys.argv[2:]):
        p=A['proposals'][i];fp=ROOT/p['after_capture']['path'];d=yaml.safe_load(fp.read_text())
        print('PROPOSAL',i,p['proposal_id'],p['before_sha256'],p['after_capture']);print(compact(d));log('whole_selected_payload',fp,'Complete semantic YAML; repeated long strings interned losslessly.')
elif mode=='cases':
    for i in map(int,sys.argv[2:]):
        d=A['decisions'][i];c=C[d['case_id']]
        print('CASE',i,c.get('source_label'),compact(c));print('DECISION',compact({k:v for k,v in d.items() if k not in ['occurrence_context','owner_records']}));print('OWNER_CONTEXT',compact(d.get('owner_records',[])))
elif mode=='sources':
    for eid in sys.argv[2:]:source(eid)
