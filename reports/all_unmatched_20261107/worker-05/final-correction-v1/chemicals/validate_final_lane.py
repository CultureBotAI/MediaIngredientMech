from pathlib import Path
from datetime import datetime, timezone
import json, yaml, hashlib, collections, dataclasses, subprocess, sys, copy
sys.path.insert(0,str(Path('src').resolve()))
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
O=Path(__file__).resolve().parent; R=Path('reports/all_unmatched_20261107/worker-05').resolve()
P=json.loads((O/'proposals-v2.json').read_text()); D=json.loads((O/'decisions-v2.json').read_text()); E=json.loads((O/'evidence-v1.json').read_text()); D0=json.loads((O/'input-decisions.json').read_text()); E0=json.loads((O/'input-evidence.json').read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(n,x):
 p=O/n;assert not p.exists();p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert len(P)==len({p['proposal_id'] for p in P})==len({p['owner_path'] for p in P})==57
assert len(D)==len({d['case_id'] for d in D})==67
assert E[:len(E0)]==E0
assert len({e['evidence_id'] for e in E})==len(E)
eids={e['evidence_id'] for e in E};pids={p['proposal_id'] for p in P};records={str(p):yaml.safe_load(p.read_text()) for f in ['mapped','unmapped'] for p in Path('data/ingredients',f).glob('*.yaml')}
baseline_violations=validate_component_partonomy(records.values())
def dups(rs):return {k:v for k,v in collections.Counter(r['identifier'] for r in rs.values() if r['mapping_status']!='REJECTED').items() if v>1}
before_duplicates=dups(records);checks=[];targets=[]
for d,old in zip(D,D0):
 assert d['case_id']==old['case_id'];assert d['case_input_sha256']==old['case_input_sha256'];assert d['occurrence_ids']==old['occurrence_ids'];assert d.get('preserved_source_holds')==old.get('preserved_source_holds')
 assert set(d['evidence_ids'])<=eids;assert set(d['proposal_ids'])<=pids
 for r in d['owner_records']:assert sha(Path(r['path']).read_bytes())==r['sha256']
for p in P:
 fp=O/Path(p['after_capture']['path']).relative_to('final-correction-v1/chemicals');assert sha(fp.read_bytes())==p['after_capture']['sha256'];new=yaml.safe_load(fp.read_text());targets.append(str(fp))
 dst=p.get('destination_owner_path',p['owner_path']);assert dst.split('/')[2]==new['mapping_status'].lower()
 if p['before_sha256']:
  oldpath=Path(p['owner_path']);assert sha(oldpath.read_bytes())==p['before_sha256'];old=records.pop(str(oldpath));assert new['curation_history'][:len(old['curation_history'])]==old['curation_history']
  negatives={s['synonym_text'] for s in old.get('synonyms',[]) if s['synonym_type']=='REJECTED_LABEL'}
  assert negatives<={s['synonym_text'] for s in new.get('synonyms',[]) if s['synonym_type']=='REJECTED_LABEL'}
 else:assert not Path(p['owner_path']).exists();assert new.get('curation_history')
 assert dst not in records;records[dst]=new
 linked=[d for d in D if d['case_id'] in p['case_ids']];assert len(linked)==len(p['case_ids']);assert set(p.get('applies_to_occurrence_ids',[]))<={o for d in linked for o in d['occurrence_ids']}
 assert all(p['proposal_id'] in d['proposal_ids'] for d in linked);assert set(p['evidence_ids'])<=eids
 checks.append({'proposal_id':p['proposal_id'],'after_capture':p['after_capture'],'original_owner_path':p['owner_path'],'destination_owner_path':dst,'before_sha256':p['before_sha256'],'history_and_inherited_negative_labels_preserved':True,'case_backlinks_and_occurrence_routes_valid':True})
after=validate_component_partonomy(records.values());after_duplicates=dups(records);introduced={k:v for k,v in after_duplicates.items() if v>before_duplicates.get(k,1)}
cmd=[sys.executable,'scripts/validate_strict.py',*targets,'--workers','1','--out',str(O/'strict-errors-v2.tsv')];r=subprocess.run(cmd,capture_output=True,text=True);(O/'strict-validation-v2.log').write_text(r.stdout+r.stderr)
dump('integrity-validation-v2.json',{'author':'/root/chemicals_research','at':datetime.now(timezone.utc).isoformat(),'case_count':len(D),'proposal_count':len(P),'evidence_count':len(E),'strict_exit_code':r.returncode,'baseline_partonomy_violations':[dataclasses.asdict(x) for x in baseline_violations],'substituted_partonomy_violations':[dataclasses.asdict(x) for x in after],'introduced_identifier_collisions':introduced,'all_original_evidence_objects_preserved':True,'all_case_input_hashes_occurrences_and_holds_preserved':True,'payload_checks':checks,'files':{n:sha((O/n).read_bytes()) for n in ['decisions-v2.json','proposals-v2.json','evidence-v1.json','payload-seal-v2.json']},'limits':'Private in-memory substitution of this lane only, including conditional candidates as structural fixtures. No family installation or whole-owner/export approval. Root validates the complete integrated successor independently.'})
print(json.dumps({'schema_exit':r.returncode,'partonomy':len(after),'introduced_collisions':introduced,'cases':len(D),'proposals':len(P),'evidence':len(E)}))
sys.exit(bool(r.returncode or after or introduced))
