from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import json,hashlib
W=Path(__file__).resolve().parents[3];R=W/'reports/all_unmatched_20261107/worker-02';S=R/'final-corrections-v1/chemistry'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def cap(p):return {'root':'artifact','path':str(p.relative_to(R)),'sha256':sha(p)}
def save(p,x):assert not p.exists();p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
ids=['fc-chem-ferric-wako-europe-n-hydrate','fc-chem-ferric-wako-us-99point5-n-hydrate']
def refs(row):
    if isinstance(row,dict):
        for k,v in row.items():
            if k=='evidence_ids' and isinstance(v,list):row[k]=list(dict.fromkeys(y for x in v for y in (ids if x=='fc-chem-ferric-wako' else [x])))
            else:refs(v)
    elif isinstance(row,list):
        for v in row:refs(v)
E=read(S/'evidence-v3.json');bindings=[]
for e in E['evidence']:
    if e['evidence_id']=='fc-chem-ferric-wako':
        before=json.loads(json.dumps(e));e['evidence_id']=ids[0] if '/europe/' in e['url'] else ids[1]
        e['locator']='Manufacturer product identity table: CAS15244-10-7 and Fe2(SO4)3·nH2O; exact retained URL/time identifies this page/version separately.'
        e['supports_or_contradicts']='This '+('Europe JIS reagent' if '/europe/' in e['url'] else 'US99.5% product')+' page explicitly identifies ferric sulfate n-hydrate andCAS15244-10-7. Supports chemical variable-hydrate CAS scope only; no fixedn, historicallot, grade equivalence or assay transfer. The displayed399.88 is explicitly the anhydrous Fe2(SO4)3 reference and is not imported as hydrate molecular mass.'
        bindings.append({'old_full_object':before,'successor_full_object':e})
assert len(bindings)==2 and len({e['evidence_id'] for e in E['evidence']})==len(E['evidence'])
E['predecessor_metadata_capture']=cap(S/'evidence-v3.json');save(S/'evidence-v4.json',E)
for kind in ['proposals','decisions']:
    x=read(S/(kind+'-v3.json'));refs(x);x['predecessor_metadata_capture']=cap(S/(kind+'-v3.json'))
    if kind=='decisions':
        old=read(R/'continuation-1201-v1/decisions.json')['decisions']
        for n in [82,89]:
            d=next(d for d in x['decisions'] if d['case_id']==old[n]['case_id']);d['missing_requirement']=d['missing_requirement'].replace('The remaining bare unhydrated alias still requires exact-form assessment and complete owner/coordinator release review.','The complete successor also concretely rejects the underqualified bare formula and generic hydrate aliases; complete owner/coordinator release review remains.')
        d=next(d for d in x['decisions'] if d['case_id']==old[96]['case_id']);d['missing_requirement']=d['missing_requirement'].replace('the unresolved bare unhydrated alias,','the now-concrete rejection of the underqualified bare formula and generic hydrate aliases,')
        d=next(d for d in x['decisions'] if d['case_id']==old[149]['case_id'])
        for key in ['reasoning','applicability']:d[key]=d[key].replace('the isolated correction preserves them as REJECTED_LABEL and must be composed with the earlier shared Mohr proposal.','the complete selected successor preserves those stock tokens as REJECTED_LABEL and also retires the two underqualified global aliases. Supported occurrence-specific CAS/form reasoning remains distinct from global resolver scope.')
    save(S/(kind+'-v4.json'),x)
f=read(S/'finding-dispositions.json');refs(f);f['predecessor_metadata_capture']=cap(S/'finding-dispositions.json');save(S/'finding-dispositions-v2.json',f)
save(S/'metadata-revision-v4.json',{'author':'/root/research_b','created_at':datetime.now(timezone.utc).isoformat(),'findings':[cap(S/'finding-evidence-id-collision-v1.json'),cap(S/'finding-stale-mohr-requirement-v1.json')],'evidence_id_lineage':bindings,'decision_changes':'Only active stale Mohr requirements/composition phrases in cases82,89,96,149 changed; original exact fields remain in finding receipt and v3. Source quantities and every frozen source field preserved.','candidate_yaml_changes':0,'previous_primary_manifest':cap(S/'PRIMARY-MANIFEST-v1.json'),'status':'corrected_pending_independent_rebind'})
D=read(S/'decisions-v4.json')['decisions'];P=read(S/'proposals-v4.json')['proposals'];oldD=read(R/'continuation-1201-v1/decisions.json')['decisions'];oldE=read(R/'continuation-1201-v1/evidence.json')['evidence'];cE=read(R/'final-corrections-v1/preparations/evidence.json')['evidence'];allE=oldE+E['evidence']+cE
counts=Counter(e['evidence_id'] for e in allE);assert all(n==1 for n in counts.values()),[k for k,v in counts.items() if v>1]
for d in D:
    od=next(x for x in oldD if x['case_id']==d['case_id']);assert all(d[k]==od[k] for k in ['case_id','case_input_sha256','source','occurrence_ids']);assert all(id in counts for id in d['evidence_ids']);assert 'fc-chem-ferric-wako' not in d['evidence_ids']
for p in P:
    assert sha(W/p['owner_path'])==p['before_sha256'];assert sha(R/p['after_capture']['path'])==p['after_capture']['sha256'];assert all(id in counts for id in p['evidence_ids'])
for e in E['evidence']:assert sha(R/e['capture']['path'])==e['capture']['sha256']
save(S/'integrity-v4.json',{'status':'PASS','author':'/root/research_b','active_fragments':[cap(S/(k+'-v4.json')) for k in ['decisions','proposals','evidence']],'active_finding_dispositions':cap(S/'finding-dispositions-v2.json'),'proposal_count':len(P),'decision_count':len(D),'new_evidence_rows':len(E['evidence']),'new_evidence_unique_ids':len({e['evidence_id'] for e in E['evidence']}),'cross_original_new_and_preparation_ID_uniqueness':True,'candidate_yaml_count_unchanged':15,'native_write_status':'15 guarded writes previouslypassed; no scientific YAML change in v4','independent_review':'pending final D rebind','prior_error_preserved':True,'no_maintained_mutation':True})
print(json.dumps(read(S/'integrity-v4.json')))
