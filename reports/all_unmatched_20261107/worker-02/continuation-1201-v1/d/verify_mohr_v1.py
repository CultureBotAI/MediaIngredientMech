"""Independent exact-byte composition/accounting and binding probes; no maintained writes."""
from pathlib import Path
from copy import deepcopy
from datetime import datetime,timezone
import hashlib,json,sys,subprocess
import yaml
R=Path('reports/all_unmatched_20261107/worker-02');S=R/'continuation-1201-v1';D=S/'d';Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(v):return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def read(p):return json.loads(p.read_text())
assembled=S/'integration/assembled-v3';decisions=read(assembled/'decisions.json')['decisions'];proposals=read(assembled/'proposals.json')['proposals'];evidence=read(assembled/'evidence.json')['evidence'];p=next(p for p in proposals if p['proposal_id']=='w02-v2-mohr-hexahydrate-composed');selected=[d for d in decisions if d['case_id'] in p['case_ids']];cases=read(Q/'shards/shard-02.json')['cases'];byid={x['case_id']:x for x in cases}
assert len(cases)==len(decisions)==len({d['case_id'] for d in decisions})==188
assert set(byid)=={d['case_id'] for d in decisions}
for d in decisions:
 c=byid[d['case_id']];assert digest(c)==d['case_input_sha256'];assert d['source']=={k:c[k] for k in ['source','source_case_id','source_label','raw_source_label']};assert d['occurrence_ids']==[o['occurrence_id'] for o in c.get('occurrences',[])]
assert len(selected)==7
ids=set(p['evidence_ids'])|{i for d in selected for i in d['evidence_ids']};checked=[]
for e in evidence:
 if e['evidence_id'] not in ids:continue
 c=e['capture'];f={'artifact':R,'source':Q}[c['root']]/c['path'];assert sha(f)==c['sha256'];checked.append(e['evidence_id'])
assert set(checked)==ids
owner=Path(p['owner_path']);assert sha(owner)==p['before_sha256'];assert hashlib.sha256(subprocess.check_output(['git','show','e000d66dd26ab053e9b17ce7bf8d3c873c3dde99:'+str(owner)])).hexdigest()==p['before_sha256']
base=yaml.safe_load(owner.read_text());old=yaml.safe_load((R/'integration/after/Fe_Nh42_So42_X_6_H2o.yaml').read_text());rev=yaml.safe_load((S/'c/proposed-owners/c2-proposal-mohr-stock-aliases.yaml').read_text());final=yaml.safe_load((R/p['after_capture']['path']).read_text())
expected=deepcopy(old);changed=[]
for i,(b,r) in enumerate(zip(base['synonyms'],rev['synonyms'])):
 if b!=r:
  assert r=={**b,'synonym_type':'REJECTED_LABEL'};expected['synonyms'][i]=r;changed.append(b['synonym_text'])
assert len(changed)==3
expected['ontology_mapping']['evidence']+=rev['ontology_mapping']['evidence'][len(base['ontology_mapping']['evidence']):]
expected['curation_history']+=rev['curation_history'][len(base['curation_history']):]
assert final['curation_history'][-1]['action']=='PROPOSED_CURATION';expected['curation_history'].append(final['curation_history'][-1]);assert final==expected
assert final['curation_history'][:len(old['curation_history'])]==old['curation_history']
assert final['synonyms'][len(base['synonyms']):]==old['synonyms'][len(base['synonyms']):]
sys.path.insert(0,str(D/'review-v1-inputs'));import bind_successor_reviews as bind
# Snapshot module retains ROOT-relative default; point to the actual declared artifact root for exact captures.
bind.ARTIFACT=R
row={'proposal_id':p['proposal_id'],'after_capture':p['after_capture'],'status':'approve','reasoning':'Exact after bytes checked independently.'}
bind.verify_proposal(p,row,'/root/final_reviewer',['/root','/root/research_a','/root/research_b','/root/research_c']);negatives=[]
for name,bad,reviewer in [('self_review',row,'/root'),('open_finding',{**row,'status':'findings_open'},'/root/final_reviewer'),('payload_swapped',{**row,'after_capture':{**p['after_capture'],'sha256':'0'*64}},'/root/final_reviewer'),('blank_reason',{**row,'reasoning':''},'/root/final_reviewer')]:
 try:bind.verify_proposal(p,bad,reviewer,['/root'])
 except ValueError:negatives.append(name)
 else:raise AssertionError(name+' accepted')
try:bind.verify_ref({**p['after_capture'],'sha256':'0'*64})
except ValueError:negatives.append('capture_hash_changed')
else:raise AssertionError('Changed capture accepted')
out={'checked_at':datetime.now(timezone.utc).isoformat(),'full_shard_mechanical_accounting':188,'scientifically_reviewed_cases':7,'scoped_evidence_capture_hashes_verified':len(checked),'preserved_original_baseline_sha256':p['before_sha256'],'exact_after_capture':p['after_capture'],'composition_matches_independent_expected_object':True,'prior_additions_and_history_preserved':True,'changed_synonym_types':changed,'binding_negative_probes_rejected':negatives,'limits':'Full-shard accounting is mechanical only; unrelated source science is not independently reviewed here. Guard tests are not release approval.'}
path=D/'verification-v1.json'
if path.exists():raise FileExistsError(path)
path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
