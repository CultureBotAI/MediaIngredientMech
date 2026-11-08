from copy import deepcopy
import json
import pytest
import bind_review_v3 as b

def inputs():
 return (json.loads((b.S/'decisions.json').read_text()),json.loads((b.S/'proposals.json').read_text()),json.loads((b.R/'independent/scientific-review-v2.json').read_text()))
def test_exact_proof_binds_only_qualified_scope():
 ds,ps,p=inputs();cr,pr=b.validate(ds,ps,p);assert len(cr)==4 and len(pr)==2
 assert pr[b.b.ACID]['status']=='preserved_unchanged_context'
@pytest.mark.parametrize('mutation',[
 lambda d,p,v:v['case_reviews'].pop(),
 lambda d,p,v:v['case_reviews'].append(deepcopy(v['case_reviews'][0])),
 lambda d,p,v:d['decisions'][114].update(reasoning='Changed after review'),
 lambda d,p,v:p['proposals'][0].update(description='Changed unrelated context'),
 lambda d,p,v:next(x for x in p['proposals'] if x['proposal_id']==b.b.PID)['after_capture'].update(sha256='0'*64),
 lambda d,p,v:v['case_reviews'][0].update(reviewer='/root'),
 lambda d,p,v:v['case_reviews'][0].update(full_owner_or_release_approval=True),
 lambda d,p,v:v['proposal_reviews'][1].update(status='approve_bounded_correction'),
])
def test_stale_incomplete_or_inflated_proof_refused(mutation):
 ds,ps,v=inputs();mutation(ds,ps,v)
 with pytest.raises(ValueError):b.validate(ds,ps,v)
def test_predecessor_fullproof_is_not_current_approval():
 ds,ps,v=inputs();v=json.loads((b.b.OLD/'independent/scientific-review-v1.json').read_text())
 with pytest.raises(ValueError):b.validate(ds,ps,v)

def test_exact_raw_context_positive():
 ds,ps,v=inputs();b.validate_raw_context([(b.S/(n+'.json')).read_bytes() for n in ['decisions','proposals','evidence']],v)
@pytest.mark.parametrize('idx',[0,1,2])
def test_raw_whitespace_drift_refused(idx):
 ds,ps,v=inputs();raw=[(b.S/(n+'.json')).read_bytes() for n in ['decisions','proposals','evidence']];raw[idx]+=b' '
 with pytest.raises(ValueError):b.validate_raw_context(raw,v)
