from pathlib import Path
from datetime import datetime, timezone
import ast, copy, difflib, hashlib, json

O=Path(__file__).resolve().parent
A=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/scripts/audit_worker_outcomes_v1.py')
F=O.parent/'review-chemicals/finding-006-initial.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def objsha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
def binding(p):return {'path':str(p),'sha256':sha(p)}
def dump(n,x):
 p=O/n;assert not p.exists();p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
D0=json.loads((O/'decisions-v1.json').read_text());K0=json.loads((O/'primary-case-conclusions-v1.json').read_text());D=copy.deepcopy(D0);K=copy.deepcopy(K0)
tree=ast.parse(A.read_text());allowed=next(ast.literal_eval(n.value) for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='dispositions' for t in n.targets))
assert 'new_distinct_ingredient_proposal' in allowed and 'curation_proposal' not in allowed
changes=[]
for i in [10,48]:
 assert D[i]['disposition']=='curation_proposal'
 D[i]['disposition']='new_distinct_ingredient_proposal'
 K['case_reviews'][i]['decision_object_sha256']=objsha(D[i])
 changes.append({'lane_index':i,'case_id':D[i]['case_id'],'field':'disposition','before':'curation_proposal','after':'new_distinct_ingredient_proposal','before_object_sha256':objsha(D0[i]),'after_object_sha256':objsha(D[i])})
assert all(d['disposition'] in allowed for d in D)
assert [i for i,(a,b) in enumerate(zip(D,D0)) if a!=b]==[10,48]
for i in [10,48]:
 x=copy.deepcopy(D[i]);x['disposition']='curation_proposal';assert x==D0[i]
K['supplement']['native_disposition_remediation']={'finding_id':'W05-FINAL-SKEPTIC-CHEM-006','prior_conclusions':binding(O/'primary-case-conclusions-v1.json'),'updated_fields':'Only the two decision_object_sha256 bindings; all scientific assessment prose is unchanged.'}
dump('decisions-v2.json',D);dump('primary-case-conclusions-v2.json',K)
for old,new in [('decisions-v1.json','decisions-v2.json'),('primary-case-conclusions-v1.json','primary-case-conclusions-v2.json')]:
 p=O/'diffs-v2'/(Path(new).stem+'.diff');p.parent.mkdir(exist_ok=True);assert not p.exists();p.write_text(''.join(difflib.unified_diff((O/old).read_text().splitlines(True),(O/new).read_text().splitlines(True),fromfile=old,tofile=new)))
dump('disposition-remediation-v2.json',{'author':'/root/chemicals_research','at':datetime.now(timezone.utc).isoformat(),'finding':binding(F),'reported_before_fix':True,'auditor':binding(A),'allowed_dispositions':sorted(allowed),'all_67_dispositions_native_enum_valid':True,'changes':changes,'scientific_text_payload_proposals_evidence_raw_sources_routes_holds_unchanged':True,'selected_files':[binding(O/n) for n in ['decisions-v2.json','primary-case-conclusions-v2.json','proposals-v1.json','evidence-v1.json']],'prior_payload_validation':binding(O/'integrity-validation-v1.json'),'prior_native_projection':binding(O/'native-projection-v1.json'),'projection_attribution_limit':'The unchanged native builder emits semapv:ManualMappingCuration as its generic projection justification; this does not authenticate human curation. The actual new MappingEvidence entries remain LLM_SUGGESTION and the curation event explicitly records LLM authorship. No gate or projection code is changed.','validation_scope':'Native enum membership and exact two-field successor equality checks; the complete campaign auditor remains the coordinator task.'})
print(json.dumps({n:sha(O/n) for n in ['decisions-v2.json','primary-case-conclusions-v2.json','disposition-remediation-v2.json']}))
