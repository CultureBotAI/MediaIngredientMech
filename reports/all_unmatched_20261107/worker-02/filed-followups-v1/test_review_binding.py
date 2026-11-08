from copy import deepcopy
import json
import pytest
import bind_review as b

def inputs():
 return (json.loads((b.S/'decisions.json').read_text())['decisions'],json.loads((b.S/'proposals.json').read_text())['proposals'],json.loads((b.R/'independent/scientific-review-v2.json').read_text()))
def test_exact_proof_binds_only_qualified_scope():
 ds,ps,p=inputs();cr,pr=b.validate(ds,ps,p);assert len(cr)==4 and len(pr)==2
 assert pr[b.b.ACID]['status']=='preserved_unchanged_context'
@pytest.mark.parametrize('mutation',[
 lambda d,p,v:v['case_reviews'].pop(),
 lambda d,p,v:v['case_reviews'].append(deepcopy(v['case_reviews'][0])),
 lambda d,p,v:d[114].update(reasoning='Changed after review'),
 lambda d,p,v:p[0].update(case_ids=[]),
 lambda d,p,v:next(x for x in p if x['proposal_id']==b.b.PID)['after_capture'].update(sha256='0'*64),
 lambda d,p,v:v['case_reviews'][0].update(reviewer='/root'),
 lambda d,p,v:v['case_reviews'][0].update(full_owner_or_release_approval=True),
 lambda d,p,v:v['proposal_reviews'][1].update(status='approve_bounded_correction'),
])
def test_stale_incomplete_or_inflated_proof_refused(mutation):
 ds,ps,v=inputs();mutation(ds,ps,v)
 if not next(x for x in ps if x['proposal_id']==ps[0]['proposal_id'])['case_ids']:
  # Unreviewed proposal metadata is preserved by the selection writer, not approved by this four-case proof.
  ps.pop()
 with pytest.raises(ValueError):b.validate(ds,ps,v)
def test_predecessor_fullproof_is_not_current_approval():
 ds,ps,v=inputs();v=json.loads((b.b.OLD/'independent/scientific-review-v1.json').read_text())
 with pytest.raises(ValueError):b.validate(ds,ps,v)
