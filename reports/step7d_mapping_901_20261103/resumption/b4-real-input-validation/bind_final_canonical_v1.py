"""Read-only dependency-equivalence binding of the completed native B4 run."""
from __future__ import annotations
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
from datetime import datetime, timezone

D=Path(__file__).resolve().parent.parent
W=D.parent/'step7d'
OLD=D/'b4-real-input-validation/rerun-v2'
OUT=D/'b4-real-input-validation/final-canonical-binding-v1.json'
KG=Path('/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe')
CANONICAL=W/'mappings/ingredient_mappings.sssom.tsv'
VALIDATOR=W/'scripts/validate_sssom_invariants.py'

def sha(raw): return hashlib.sha256(raw).hexdigest()
def digest(path): return sha(path.read_bytes())
def canonical(value): return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()
def load(path): return json.loads(path.read_text())
def git(root,*args): return subprocess.check_output(['git','-C',str(root),*args],text=True)
def kg_context():
    return {'revision':git(KG,'rev-parse','HEAD').strip(), 'branch':git(KG,'branch','--show-current').strip(), 'status_porcelain_v1':git(KG,'status','--porcelain=v1','--untracked-files=all')}
def mim_context(): return {'revision':git(W,'rev-parse','HEAD').strip(), 'status_porcelain_v1':git(W,'status','--porcelain=v1','--untracked-files=all')}
def transform_snapshot(expected):
    out={}
    for prefix, item in expected.items():
        path=Path(item['path'])
        value={'path':str(path),'present':path.is_file()}
        if path.is_file():
            st=path.stat(); value.update(sha256=digest(path),bytes=st.st_size,mtime_ns=st.st_mtime_ns)
        out[prefix]=value
    return out

def main():
    if OUT.exists(): raise RuntimeError('Refuse replacing existing evidence')
    started=datetime.now(timezone.utc).isoformat()
    prior=load(OLD/'summary.json')
    expected_inputs=load(OLD/'inputs-before.json')
    assert expected_inputs==load(OLD/'inputs-after.json')
    expected_kg=load(OLD/'kg-before.json')
    assert expected_kg==load(OLD/'kg-after.json')
    context_before=mim_context()
    kg_before=kg_context()
    validator_bytes=VALIDATOR.read_bytes()
    assert sha(validator_bytes)==prior['native_validator_sha256']
    tree=ast.parse(validator_bytes)
    evaluator=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='evaluate_rule_b4')
    consumed=sorted({n.args[0].value for n in ast.walk(evaluator) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and isinstance(n.func.value,ast.Name) and n.func.value.id=='row' and n.func.attr=='get' and n.args and isinstance(n.args[0],ast.Constant)})
    assert consumed==['object_id','object_label'], consumed
    loader=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='_load_ontology_labels')
    transform_fields=sorted({n.args[0].value for n in ast.walk(loader) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and isinstance(n.func.value,ast.Name) and n.func.value.id=='row' and n.func.attr=='get' and n.args and isinstance(n.args[0],ast.Constant)})
    assert transform_fields==['id','name','synonym']
    spec=importlib.util.spec_from_file_location('native_sssom_b4_binding', VALIDATOR)
    native=importlib.util.module_from_spec(spec); spec.loader.exec_module(native)
    assert set(expected_inputs)==set(native.B4_PREFIXES)
    inputs_before=transform_snapshot(expected_inputs)
    assert inputs_before==expected_inputs, 'Transform dependency drift'
    assert kg_before==expected_kg, 'KG revision/status drift'
    prior_path=OLD/'current-canonical.sssom.tsv'
    prior_bytes=prior_path.read_bytes(); current_bytes=CANONICAL.read_bytes()
    assert sha(prior_bytes)==prior['current_canonical_sha256']
    p0,c0,r0=native._read_sssom(prior_path)
    p1,c1,r1=native._read_sssom(CANONICAL)
    assert p0==p1 and c0==c1 and len(r0)==len(r1)==prior['current_rows']
    diff=[]
    for position,(before,after) in enumerate(zip(r0,r1),start=1):
        assert set(before)==set(after)==set(c0)
        for field in c0:
            if before[field]!=after[field]:
                diff.append({'subject_id':before['subject_id'],'object_id':before['object_id'],'output_position':position,'column':field,'before':before[field],'after':after[field]})
    corrections_path=D/'comment-remediation-v2/comment-corrections.json'
    corrections=load(corrections_path)
    expected_diff=[{k:item[k] for k in ['subject_id','object_id','output_position','column','before','after']} for item in corrections]
    assert diff==expected_diff and len(diff)==4 and all(x['column']=='comment' for x in diff)
    # This is byte-level equivalence apart from exactly the approved comment cells.
    expected_after=prior_bytes
    for item in corrections:
        before=item['before'].encode(); after=item['after'].encode()
        assert expected_after.count(before)==1
        expected_after=expected_after.replace(before,after,1)
    assert expected_after==current_bytes
    consumed_before=[[r[k] for k in consumed] for r in r0]
    consumed_after=[[r[k] for k in consumed] for r in r1]
    assert consumed_before==consumed_after
    owner_coverage=load(OLD/'selected-38-owner-coverage.json')
    assert len(owner_coverage)==38
    owners={}
    for owner in owner_coverage:
        p=owner['owner_path']; current_sha=digest(W/p)
        assert current_sha==owner['owner_sha256'], p
        owners[p]=current_sha
    assert len(owners)==38
    owner_vector=sorted(owners.items())
    inputs_after=transform_snapshot(expected_inputs)
    kg_after=kg_context()
    context_after=mim_context()
    assert inputs_after==inputs_before==expected_inputs
    assert kg_after==kg_before==expected_kg
    assert context_after==context_before
    assert VALIDATOR.read_bytes()==validator_bytes and CANONICAL.read_bytes()==current_bytes
    assert all(digest(W/path)==value for path,value in owners.items())
    result={
      'schema':'mim-native-b4-canonical-equivalence-binding/v1','result':'PASS_WITH_PRIOR_SKIPS_PRESERVED',
      'started_at':started,'finished_at':datetime.now(timezone.utc).isoformat(),
      'method':'Dependency-equivalence proof; no new B4 evaluation and no waiver. Native evaluator/loader read and imported unchanged; every consumed ordered value and exact transform dependency is identical to rerun-v2.',
      'mim_context_before':context_before,'mim_context_after':context_after,
      'prior_native_run':{'summary_path':str(OLD/'summary.json'),'summary_sha256':digest(OLD/'summary.json'),'canonical_sha256':sha(prior_bytes),'rejects':prior['current_rejects']},
      'current_canonical':{'path':str(CANONICAL),'sha256':sha(current_bytes),'rows':len(r1)},
      'native_validator':{'path':str(VALIDATOR),'sha256':sha(validator_bytes),'evaluator':'evaluate_rule_b4','evaluator_lines':[evaluator.lineno,evaluator.end_lineno],'row_columns':consumed,'transform_loader':'_load_ontology_labels','transform_columns':transform_fields,'prefixes':sorted(native.B4_PREFIXES)},
      'consumed_values':{'every_ordered_row_equal':True,'before_sha256':sha(canonical(consumed_before)),'after_sha256':sha(canonical(consumed_after)),'rows':len(r1)},
      'canonical_diff':{'columns_and_header_identical':True,'exact_raw_bytes_except_reviewed_comment_cells':True,'cell_count':len(diff),'corrections_path':str(corrections_path),'corrections_sha256':digest(corrections_path),'cells':diff},
      'transforms':{'before':inputs_before,'after':inputs_after,'equal_to_prior_run':True,'absent_exact_native_paths_checked_ignores_do_not_apply':True},
      'kg_context':{'before':kg_before,'after':kg_after,'equal_to_prior_run':True},
      'selected_owners':{'count':len(owners),'all_equal_to_prior_run':True,'coverage_path':str(OLD/'selected-38-owner-coverage.json'),'coverage_sha256':digest(OLD/'selected-38-owner-coverage.json'),'owner_sha256':owners,'vector_sha256':sha(canonical(owner_vector))},
      'preserved_coverage':{'current':prior['current_coverage'],'selected':prior['selected_current_coverage'],'missing_transform_prefixes':prior['missing_transform_prefixes'],'new_or_existing_rejects':0},
      'limitations':prior['limitations']+' This proof binds the new canonical hash through exact dependency equality; it does not extend B4 to its excluded prefixes or missing transforms.',
      'maintained_writes':False,'kg_writes':False,'downloads':False,'paid_provider_calls':False,
      'binder_sha256':digest(Path(__file__))
    }
    with OUT.open('x') as f: json.dump(result,f,indent=2,ensure_ascii=False); f.write('\n')
    print(json.dumps({'result':result['result'],'output':str(OUT),'sha256':digest(OUT),'canonical_sha256':sha(current_bytes),'rows':len(r1),'owners':len(owners),'comment_cells':len(diff)}))

if __name__=='__main__': main()
