"""Independent controls for whole-context evidence pin and true author conflict."""
from pathlib import Path
from copy import deepcopy
import json,sys
import pytest
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R))
import bind_review_v3 as m

def inputs():
    return (json.loads((m.S/'decisions.json').read_bytes()),json.loads((m.S/'proposals.json').read_bytes()),json.loads((m.R/'independent/scientific-review-v2.json').read_bytes()))

def test_true_case_author_conflict_refused():
    d,p,proof=inputs();proof['case_reviews'][0]['original_authors'].append('worker02 /root/final_reviewer')
    with pytest.raises(ValueError,match='Self review'):m.validate(d,p,proof)

def test_true_proposal_author_conflict_refused():
    d,p,proof=inputs();proof['proposal_reviews'][0]['original_authors'].append('/root/final_reviewer')
    with pytest.raises(ValueError,match='Self review'):m.validate(d,p,proof)

def test_unreviewed_case_context_change_refused():
    d,p,proof=inputs();d['decisions'][0]['missing_requirement']='removed historical hold'
    with pytest.raises(ValueError,match='Frozen predecessor bytes changed'):m.validate(d,p,proof)

def test_main_rejects_changed_full_evidence_before_output(monkeypatch,tmp_path):
    original_s=m.S;original_r=m.R
    root=tmp_path/'packet';selection=root/'review-input-v2';selection.mkdir(parents=True);(root/'independent').mkdir()
    for n in ['decisions','proposals','evidence']:(selection/(n+'.json')).write_bytes((original_s/(n+'.json')).read_bytes())
    # Only fixture-local paths are rebound; original exact full-file hashes remain.
    proof=json.loads((original_r/'independent/scientific-review-v2.json').read_bytes())
    for row in proof['input_hash_manifest']:
        for n in ['decisions','proposals','evidence']:
            if row['path']==str((original_s/(n+'.json')).absolute()):row['path']=str((selection/(n+'.json')).absolute())
    (root/'independent/scientific-review-v2.json').write_text(json.dumps(proof))
    evidence=selection/'evidence.json';evidence.write_bytes(evidence.read_bytes()+b'\n')
    original_require_output=m.b.require_output
    monkeypatch.setattr(m,'R',root);monkeypatch.setattr(m,'S',selection)
    monkeypatch.setattr(m.b,'require_output',lambda p:original_require_output(p,root=tmp_path))
    with pytest.raises(ValueError,match='Frozen predecessor bytes changed'):m.main()
    assert not (root/'selected-v3').exists()
