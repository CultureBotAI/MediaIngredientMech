"""Independent controls specific to new case98 proof scope; no science approval."""
from pathlib import Path
from copy import deepcopy
import importlib.util,json,sys
import pytest
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R))
s=importlib.util.spec_from_file_location('case98_binder_independent',R/'bind_review_v3.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
CID='CM_NAME:b2842dee958925abda8f2e56af9eb9a5fd009b8306848c04ae6782597864506c'
def inputs():return json.loads((m.S/'decisions.json').read_bytes()),json.loads((m.S/'proposals.json').read_bytes()),json.loads((R/'independent/scientific-review-v2.json').read_bytes())
def test_omitting_only_new_case98_proof_refused():
 d,p,v=inputs();v['case_reviews']=[x for x in v['case_reviews'] if x['case_id']!=CID]
 with pytest.raises(ValueError):m.validate(d,p,v)
def test_new_case98_actual_self_author_refused():
 d,p,v=inputs();next(x for x in v['case_reviews'] if x['case_id']==CID)['current_correction_author']='/root/final_reviewer'
 with pytest.raises(ValueError):m.validate(d,p,v)
def test_new_case98_occurrence_drift_after_review_refused():
 d,p,v=inputs();d['decisions'][98]['occurrence_ids'].pop()
 with pytest.raises(ValueError):m.validate(d,p,v)
def test_immediate_seven_only_proof_cannot_approve_new_case98():
 d,p,_=inputs();old=json.loads((R/'independent/scientific-review-v1.json').read_bytes())
 with pytest.raises((ValueError,KeyError)):m.validate(d,p,old)
