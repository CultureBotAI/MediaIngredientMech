from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,importlib.util,yaml
D=Path(__file__).resolve().parent;C=D.parent.parent;P=C/'workers/w03/worktree/.temp/w08-published-head-independent-review-v1';W=C/'workers/w08/worktree';I=C/'integration/worktree';R='reports/all_unmatched_20261107/worker-08';H='b90a2fd4681d20e2586481b7b9b1114a78281b94';A=json.loads((D/'snapshot/assessment.json').read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
def git(p):return subprocess.check_output(['git','-C',str(W),'show',H+':'+p])
errors=[];checks=[];payloads={};human=[]
for e in A['proposal_accounting']:
 r=e['after_capture'];raw=git(R+'/'+r['path']);v=yaml.safe_load(raw);payloads[e['proposal_id']]=v
 ok=sha(raw)==r['sha256'] and raw==(P/'input-snapshot'/R/r['path']).read_bytes()
 checks.append({'proposal_id':e['proposal_id'],'path':R+'/'+r['path'],'sha256':sha(raw),'matches_committed_and_snapshot':ok})
 if not ok:errors.append(checks[-1])
 before={}
 if e['before_sha256']:
  b=git(e['owner_path']);before=yaml.safe_load(b)
  if sha(b)!=e['before_sha256']:errors.append({'before':e['proposal_id']})
 pre=before.get('ontology_mapping',{}).get('evidence',[]) or []
 for i,z in enumerate(v.get('ontology_mapping',{}).get('evidence',[]) or []):
  if z.get('evidence_type')=='MANUAL_CURATION' and z not in pre:human.append({'proposal_id':e['proposal_id'],'json_pointer':f'/ontology_mapping/evidence/{i}','assertion':z,'after_sha256':r['sha256'],'history_last':v.get('curation_history',[])[-1:]})
spec=importlib.util.spec_from_file_location('synonym_policy',I/'src/mediaingredientmech/synonym_policy.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
alias=[]
for pid in ['vm-prop-jcm403-vitamin','vm-prop-jcm403-b12','if-add-anhydrous-k2hpo4','if1201-edit-kh2po4-alias-scope']:
 for i,s in enumerate(payloads[pid].get('synonyms',[])):
  if pid.startswith('vm-') or s['synonym_text'] in ['KH2HPO4','K2HPO','KH PO','Potassium Phosphate']:
   alias.append({'proposal_id':pid,'json_pointer':f'/synonyms/{i}','synonym':s,'native_resolves':m.is_resolving_synonym(s)})
comp=[]
for e in json.loads((P/'b/feasible-component-candidates.json').read_text()):
 p=Path(e['candidate_path']);b=p.read_bytes();v=yaml.safe_load(b);c=payloads[e['proposal_id']]['components'][e['component_index']]
 ok=sha(b)==e['candidate_sha256'] and v['identifier']==e['candidate_identifier'] and c==e['component']
 comp.append({**e,'exact_candidate_and_component_binding_verified':ok,'baseline_status':v.get('mapping_status')})
 if not ok:errors.append({'component':e['proposal_id'],'index':e['component_index']})
# Recompute actual reviewer accounting without adding the finding axes together.
caseids={e['case_id'] for e in A['case_accounting']};pids={e['proposal_id'] for e in A['proposal_accounting']}
f=json.loads((D/'snapshot/findings.json').read_text())['finding_groups'];fu=set().union(*(set(x['proposal_ids']) for x in f));cu=set().union(*(set(x['direct_source_case_ids']) for x in f))
assert len(caseids)==188 and len(pids)==113 and len(fu)==94 and len(cu)==9
assert len(human)==95 and len({x['proposal_id'] for x in human})==88
out={'at':datetime.now(timezone.utc).isoformat(),'head':H,'status':'PASS' if not errors else 'FAIL','errors':errors,'selected_payload_checks':checks,'human_evidence_entries':human,'alias_checks':alias,'component_binding_checks':comp,'counts':{'cases':len(caseids),'payloads':len(pids),'affected_payload_union':len(fu),'affected_source_case_union':len(cu),'new_human_only_evidence_entries':len(human),'new_human_only_evidence_payloads':len({x['proposal_id'] for x in human}),'catalog_component_pairs_checked':len(comp)},'limits':'Component pair binding checks verify exact declared record/entity and payload fields; they are not blanket scientific approval for every source form. Independent scientific author must supply claim-specific provenance and retain explicit unresolved forms.'}
(D/'target-verification-v1.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print(json.dumps({'status':out['status'],'counts':out['counts'],'errors':errors},indent=2))
