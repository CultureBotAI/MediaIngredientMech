"""Independent complete-proof pin and publication-time source-drift controls."""
from pathlib import Path
from copy import deepcopy
import importlib.util,json,sys,hashlib
import pytest
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R))
s=importlib.util.spec_from_file_location('seven_independent_binder',R/'bind_review_v2.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def test_duplicate_full_context_pin_refused():
    proof=json.loads((R/'independent/scientific-review-v1.json').read_bytes());proof['input_hash_manifest'].append(deepcopy(proof['input_hash_manifest'][0]))
    raw=[(m.S/(n+'.json')).read_bytes() for n in ['decisions','proposals','evidence']]
    with pytest.raises(ValueError,match='Duplicate'):m.validate_raw_context(raw,proof)

@pytest.mark.parametrize('stage',['before_main','during_publication'])
def test_actual_proof_input_drift_refused_without_published_files(stage,tmp_path,monkeypatch):
    original_s=m.S;original_r=m.R;fixture_root=R/'technical/runtime-binding-fixtures-v3';root=fixture_root/tmp_path.name/'packet';selection=root/'review-input-v1';selection.mkdir(parents=True);(root/'independent').mkdir()
    for name in ['decisions','proposals','evidence']:(selection/(name+'.json')).write_bytes((original_s/(name+'.json')).read_bytes())
    proof=json.loads((original_r/'independent/scientific-review-v1.json').read_bytes())
    for row in proof['input_hash_manifest']:
        for name in ['decisions','proposals','evidence']:
            if row['path']==str((original_s/(name+'.json')).absolute()):row['path']=str((selection/(name+'.json')).absolute())
    aux=tmp_path/'auxiliary-source';aux.write_bytes(b'captured')
    proof['input_hash_manifest'].append({'path':str(aux),'sha256':hashlib.sha256(aux.read_bytes()).hexdigest()})
    (root/'independent/scientific-review-v1.json').write_text(json.dumps(proof))
    original_output=m.b.require_output;native_publish=m.b.publish_new_files
    monkeypatch.setattr(m,'R',root);monkeypatch.setattr(m,'S',selection)
    monkeypatch.setattr(m.b,'require_output',lambda p:original_output(p,root=fixture_root))
    if stage=='before_main':aux.write_bytes(b'changed')
    else:
        def publication(outputs,verify):
            aux.write_bytes(b'changed')
            return native_publish(outputs,verify)
        monkeypatch.setattr(m.b,'publish_new_files',publication)
    with pytest.raises(ValueError,match='Frozen input bytes changed'):m.main()
    out=root/'selected-v2'
    assert not out.exists() or list(out.iterdir())==[]
