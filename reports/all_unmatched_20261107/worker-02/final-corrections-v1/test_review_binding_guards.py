from copy import deepcopy
import importlib.util
from pathlib import Path
import pytest
p=Path(__file__).with_name('bind_independent_review.py');s=importlib.util.spec_from_file_location('binder',p);b=importlib.util.module_from_spec(s);s.loader.exec_module(b)
def inputs():
 d={'case_id':'case1','case_input_sha256':'f'*64};p={'proposal_id':'p1','after_capture':{'root':'artifact','path':'x.yaml','sha256':'a'*64}}
 row={'reviewer':'/root/final_reviewer','original_authors':['worker02 /root'],'authorship_conflict':False,'status':'approve','reasoning':'Specific inspected claim','review_mode':'fresh_complete_candidate'}
 c=dict(row,case_id='case1',case_input_sha256='f'*64,decision_canonical_sha256=b.digest(d));pr=dict(row,proposal_id='p1',proposal_canonical_sha256=b.digest(p),after_capture=p['after_capture'])
 routing={'cases':[{'case_id':'case1','authors':['worker02 /root']}],'payloads':[{'proposal_id':'p1','authors':['worker02 /root']}]}
 return [d],[p],routing,{'case_reviews':[c],'proposal_reviews':[pr]}
def test_valid_review_and_open_findings_are_distinct():
 d,p,r,v=inputs();assert b.validate_reviews(d,p,r,v)[0]['case1']['status']=='approve'
 v['case_reviews'][0]['status']='findings_open';assert b.validate_reviews(d,p,r,v)[0]['case1']['status']=='findings_open'
@pytest.mark.parametrize('mutation',[
 lambda d,p,r,v:v['case_reviews'].clear(),
 lambda d,p,r,v:v['proposal_reviews'].append(deepcopy(v['proposal_reviews'][0])),
 lambda d,p,r,v:d[0].update(reasoning='scientific change after review'),
 lambda d,p,r,v:p[0]['after_capture'].update(sha256='b'*64),
 lambda d,p,r,v:v['case_reviews'][0].update(reviewer='/root'),
 lambda d,p,r,v:r['cases'][0]['authors'].append('worker02 /root/final_reviewer'),
 lambda d,p,r,v:v['proposal_reviews'][0].update(authorship_conflict=True),
 lambda d,p,r,v:v['proposal_reviews'][0].update(reasoning=''),
 lambda d,p,r,v:v['case_reviews'][0].update(status='pending'),
 lambda d,p,r,v:r['payloads'].clear(),
])
def test_refuses_stale_incomplete_or_self_review(mutation):
 d,p,r,v=inputs();mutation(d,p,r,v)
 with pytest.raises(ValueError):b.validate_reviews(d,p,r,v)
