from copy import deepcopy
import importlib.util,json,sys
from pathlib import Path
import pytest
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R));s=importlib.util.spec_from_file_location('seven_binder',R/'bind_review_v3.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
D=json.loads((m.S/'decisions.json').read_text());P=json.loads((m.S/'proposals.json').read_text());PROOF=json.loads((R/'independent/scientific-review-v2.json').read_text());RAW=[(m.S/(n+'.json')).read_bytes() for n in ['decisions','proposals','evidence']]
def test_exact_complete_proof_positive():
 m.validate_raw_context(RAW,PROOF);cr,pr=m.validate(D,P,PROOF);assert len(cr)==2 and len(pr)==7
@pytest.mark.parametrize('kind',['wrong_reviewer','self_author','false_independence','release_approval','omitted_case','duplicate_case','omitted_proposal','duplicate_proposal','eighth_target','stale_case','stale_payload','wrong_status','old_proof'])
def test_incomplete_stale_or_overbroad_review_refused(kind):
 proof=deepcopy(PROOF)
 if kind=='wrong_reviewer':proof['case_reviews'][0]['reviewer']='/root'
 elif kind=='self_author':proof['proposal_reviews'][0]['original_authors']=['worker02 /root/final_reviewer']
 elif kind=='false_independence':proof['case_reviews'][0]['authorship_conflict']=True
 elif kind=='release_approval':proof['proposal_reviews'][0]['full_owner_or_release_approval']=True
 elif kind=='omitted_case':proof['case_reviews']=[]
 elif kind=='duplicate_case':proof['case_reviews'].append(deepcopy(proof['case_reviews'][0]))
 elif kind=='omitted_proposal':proof['proposal_reviews'].pop()
 elif kind=='duplicate_proposal':proof['proposal_reviews'].append(deepcopy(proof['proposal_reviews'][0]))
 elif kind=='eighth_target':proof['proposal_reviews'][0]['proposal_id']='dsmz40'
 elif kind=='stale_case':proof['case_reviews'][0]['decision_canonical_sha256']='0'*64
 elif kind=='stale_payload':proof['proposal_reviews'][0]['after_capture']['sha256']='0'*64
 elif kind=='wrong_status':proof['proposal_reviews'][0]['status']='approve_whole_owner'
 else:proof=json.loads((R.parent/'filed-followups-v1/independent/scientific-review-v2.json').read_text())
 with pytest.raises((ValueError,KeyError)):m.validate(D,P,proof)
@pytest.mark.parametrize('index',[0,1,2])
def test_whitespace_only_raw_context_drift_refused(index):
 changed=list(RAW);changed[index]+=b'\n'
 with pytest.raises(ValueError):m.validate_raw_context(changed,PROOF)
def test_unreviewed_context_change_refused():
 changed=deepcopy(D);changed['decisions'][0]['reasoning']+=' invented'
 with pytest.raises(ValueError):m.validate(changed,P,PROOF)
def test_case58_omitted_occurrence_refused():
 changed=deepcopy(D);changed['decisions'][58]['occurrence_ids'].pop()
 with pytest.raises(ValueError):m.validate(changed,P,PROOF)
def test_missing_raw_input_pin_refused():
 changed=deepcopy(PROOF);changed['input_hash_manifest']=[r for r in changed['input_hash_manifest'] if r['path']!=str((m.S/'evidence.json').absolute())]
 with pytest.raises(ValueError):m.validate_raw_context(RAW,changed)

@pytest.mark.parametrize('collection',['case_reviews','proposal_reviews'])
@pytest.mark.parametrize('author',['/root/final_reviewer','human reviewer',None])
def test_actual_current_author_field_refused(collection,author):
 changed=deepcopy(PROOF)
 if author is None:changed[collection][0].pop('current_correction_author')
 else:changed[collection][0]['current_correction_author']=author
 with pytest.raises(ValueError):m.validate(D,P,changed)
