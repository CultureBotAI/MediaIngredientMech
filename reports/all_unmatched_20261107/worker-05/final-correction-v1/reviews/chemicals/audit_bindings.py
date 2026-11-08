from pathlib import Path
import json, hashlib, datetime, yaml

W=Path.cwd(); N=W/'.temp/w05-final-correction-v1'; A=N/'chemicals'; L=N/'review-chemicals'
C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
R=W/'reports/all_unmatched_20261107/worker-05'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def obj(x): return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def read(p): return json.loads(p.read_text())
def cap_path(c):
    if c['root']=='source': return C/c['path']
    if c['path'].startswith('final-correction-v1/'): return N/Path(c['path']).relative_to('final-correction-v1')
    return R/c['path']
def changes(a,b,path=''):
    if type(a)!=type(b):return [path]
    if isinstance(a,dict):
        out=[]
        for k in sorted(a.keys()|b.keys()):
            if k not in a or k not in b:out.append(path+'/'+k)
            else:out+=changes(a[k],b[k],path+'/'+k)
        return out
    if isinstance(a,list):
        if len(a)!=len(b):return [path+'/length']
        return [p for i,(x,y) in enumerate(zip(a,b)) for p in changes(x,y,path+'/'+str(i))]
    return [] if a==b else [path]

dp=N/'remediation/chemical-report-v2/decisions-v3.json'
ep=N/'remediation/chemical-report-v1/evidence-v2.json'
pp=A/'proposals-v3.json';sp=N/'remediation/chemical-report-v3/primary-case-conclusions-v3.json'
D,E,P,S=map(read,[dp,ep,pp,sp]);assignment=read(N/'control/chemicals-assignment.json')
errors=[]; capture_checks=[]; payload_checks=[]
for e in E:
    c=e['capture'];p=cap_path(c);actual=sha(p) if p.exists() else None
    if actual!=c['sha256']:errors.append(['capture',e['evidence_id'],str(p),actual,c['sha256']])
    capture_checks.append({'evidence_id':e['evidence_id'],'capture':c,'resolved_path':str(p),'actual_sha256':actual,'scope':'Byte integrity only; scientific read scope is separately declared.'})
for p in P:
    q=cap_path(p['after_capture']);b=yaml.safe_load(q.read_text());assert sha(q)==p['after_capture']['sha256']
    pre=p.get('predecessor_after_capture');before=W/p['owner_path']
    if pre:
        z=cap_path(pre);assert sha(z)==pre['sha256'];old=yaml.safe_load(z.read_text())
    else:old=yaml.safe_load(before.read_text())
    oldhist=old.get('curation_history',[]);newhist=b.get('curation_history',[])
    assert newhist[:len(oldhist)]==oldhist,(p['proposal_id'],'history')
    if p.get('before_sha256') and before.exists():assert sha(before)==p['before_sha256'],(p['proposal_id'],'before')
    elif p.get('before_sha256'):errors.append(['missing baseline',p['proposal_id'],str(before)])
    payload_checks.append({'proposal_id':p['proposal_id'],'after_capture':p['after_capture'],'predecessor_after_capture':pre,'owner_path':p['owner_path'],'before_sha256':p.get('before_sha256'),'prior_history_preserved':True,'field_changes_from_predecessor':changes(old,b)})
assert len(D)==67 and len(P)==57
assert {d['case_id'] for d in D}==set(assignment['case_ids'])
assert set(assignment['proposal_ids']).issubset({p['proposal_id'] for p in P})
frozen=read(C/'shards/shard-05.json')['cases'];raw={x['case_id']:x for x in frozen}
case_checks=[]
for d in D:
    c=raw[d['case_id']]
    # The contract hash is for the complete frozen case without its digest field.
    candidates=[obj(c),obj({k:v for k,v in c.items() if k!='case_input_sha256'})]
    declared=c.get('case_input_sha256')
    if d['case_input_sha256'] not in candidates and d['case_input_sha256']!=declared:errors.append(['casehash',d['case_id'],c.keys()])
    case_checks.append({'case_id':d['case_id'],'selected_decision_object_sha256':obj(d),'case_input_sha256':d['case_input_sha256'],'occurrence_ids':d['occurrence_ids'],'preserved_holds_sha256':obj(d.get('preserved_source_holds'))})
amendments={
 'decisions':changes(read(A/'decisions-v2.json'),D),
 'evidence':changes(read(A/'evidence-v1.json'),E),
 'source_conclusions':changes(read(A/'primary-case-conclusions-v1.json'),S),
}
assert len(amendments['decisions'])==3 and all(x.endswith('/disposition') for x in amendments['decisions'])
assert len(amendments['evidence'])==14 and all(x.endswith('/supports_or_contradicts') for x in amendments['evidence'])
for x,y in zip(read(A/'evidence-v1.json'),E):
    if 'supports_or_contradicts' not in x:assert y['supports_or_contradicts']==x['observation']
assert set(x for x in amendments['source_conclusions'] if x.startswith('/case_reviews/'))=={'/case_reviews/0/assessment','/case_reviews/5/assessment'}
recipes=read(A/'evidence-read-ledger-v1.json')['frozen_recipes']
for r in recipes:assert sha(C/r['path'])==r['sha256']
typing=read(A/'mapping-evidence-corrections-v1.json');by={p['proposal_id']:yaml.safe_load(cap_path(p['after_capture']).read_text()) for p in P}
for x in typing:
    field=x['field'];idx=int(field.split('[')[1].split(']')[0]);assert by[x['proposal_id']]['ontology_mapping']['evidence'][idx]['evidence_type']==x['after_type']
receipt={'reviewer':'/root/materials_research','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS' if not errors else 'FAIL','errors':errors,'inputs':[{'path':str(p),'sha256':sha(p)} for p in [dp,ep,pp,sp,A/'FINAL-MANIFEST-v1.json',A/'finding-dispositions-v3.json',A/'native-projections-v3.json',A/'conditional-family-matrix-v1.json']], 'counts':{'cases':len(D),'payloads':len(P),'evidence_entries':len(E),'frozen_recipes':len(recipes),'exact_w02_typing_corrections':len(typing)},'case_checks':case_checks,'payload_checks':payload_checks,'capture_checks':capture_checks,'amendment_field_differences':amendments,'limits':['Mechanical hashes, preserved history and declared amendment boundaries are not scientific approval.','No maintained output, export, merge or source-hold release is authorized.','Native full-overlay checks are coordinator artifacts; this receipt does not claim their authorship.']}
out=L/'binding-audit-v1.json';assert not out.exists();out.write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'status':receipt['status'],'errors':errors,'counts':receipt['counts'],'sha256':sha(out),'amendments':amendments},ensure_ascii=False))
