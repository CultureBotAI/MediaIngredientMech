from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, os, subprocess, sys, types
import yaml
from mediaingredientmech.validation.write_validated import validate_ingredient, write_validated_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy

W=Path.cwd();S=W/'.temp/w05-buffer-parts-v1/parents';B=W/'reports/all_unmatched_20261107/worker-05';V=S/'validation-final';V.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
objsha=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
ps=json.loads((S/'final/proposals.json').read_text())['proposals'];oldps=json.loads((S/'input/selected-proposals.json').read_text())['proposals'];oldpi={p['proposal_id']:p for p in oldps}
paths=[];checks=[];record_by_pid={}
for p in ps:
    f=S/p['after_capture']['path'].removeprefix('buffer-parts-v1/parents/');assert sha(f)==p['after_capture']['sha256'];paths.append(f)
    r=yaml.safe_load(f.read_text());record_by_pid[p['proposal_id']]=r;assert not validate_ingredient(r)
    out=V/'guarded-readback'/f.name;write_validated_ingredient(r,out);assert yaml.safe_load(out.read_text())==r
    before=yaml.safe_load((B/oldpi[p['proposal_id']]['after_capture']['path']).read_text())
    assert r['curation_history'][:-1]==before['curation_history']
    assert r['ontology_mapping']['evidence'][:len(before['ontology_mapping']['evidence'])]==before['ontology_mapping']['evidence']
    assert all(x['evidence_type']=='LLM_SUGGESTION' for x in r['ontology_mapping']['evidence'][len(before['ontology_mapping']['evidence']):])
    assert all(r.get(k)==before.get(k) for k in before if k not in ['identifier','ontology_mapping','curation_history','notes'])
    checks.append(dict(proposal_id=p['proposal_id'],after_capture=p['after_capture'],guarded_readback_sha256=sha(out),strict_closed_schema='PASS',all_other_fields_unchanged=True,prior_history_count=len(before['curation_history']),prior_evidence_count=len(before['ontology_mapping']['evidence'])))
assert not validate_component_partonomy(list(record_by_pid.values()))
cmd=[str(W/'.temp/all-unmatched-worker-05/venv/bin/python'),'scripts/validate_strict.py']+[str(f) for f in paths]+['--workers','1','--out',str(V/'strict-failures.tsv')]
proc=subprocess.run(cmd,capture_output=True,text=True,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONPATH='src'));(V/'strict.stdout.log').write_text(proc.stdout);(V/'strict.stderr.log').write_text(proc.stderr);assert proc.returncode==0
builder=W.parents[4]/'.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py';assert sha(builder)=='38d59f42953305f6fc51e4fc24dfc59ee1919bfb961595b67a8afe9f8a46a1bc'
sys.path[:0]=[str(builder.parent),str(builder.parent.parent/'src')];mod=types.ModuleType('parents_final_projection');mod.__file__=str(builder);sys.modules[mod.__name__]=mod;exec(compile(builder.read_bytes(),str(builder),'exec'),mod.__dict__)
records={str(q.relative_to(W)):yaml.safe_load(q.read_text()) for q in (W/'data/ingredients').rglob('*.yaml')}
coreps=json.loads((B/'tellurium-polypeptone-v1/core/proposals.json').read_text())['proposals']
for q in coreps:
    f=B/q['after_capture']['path'];assert sha(f)==q['after_capture']['sha256'];records.pop(q['owner_path'],None);records[q.get('destination_owner_path',q['owner_path'])]=yaml.safe_load(f.read_text())
before_records=dict(records)
for p in ps:records[p['owner_path']]=record_by_pid[p['proposal_id']]
owner=lambda rs:mod.build_owner_index({mod._mim_curie(Path(n).name):v for n,v in rs.items()})
bi=owner(before_records);ai=owner(records);results=[]
for p in ps:
    r=record_by_pid[p['proposal_id']];bef=before_records[p['owner_path']];bs=[];ass=[]
    br=mod._row_from_yaml(W/p['owner_path'],{}, {}, {}, {},record=bef,owners=bi,suppressions=bs)
    ar=mod._row_from_yaml(W/p['owner_path'],{}, {}, {}, {},record=r,owners=ai,suppressions=ass)
    expected=[('skos:exactMatch','MICRO:0000181')] if p['proposal_id']=='W05-FINAL-MAT-032' else [('skos:broadMatch','mesh:D011492'),('skos:exactMatch','kgmicrobe.ingredient:peptone')]
    assert [(x['predicate_id'],x['object_id']) for x in ar]==expected
    blocked=['Phytone peptone','Phytone peptone (BD-BBL)','Soytone (BD-Difco) or Phytone peptone (BD-BBL)','Soytone','Bacto Soytone','Properties: Undefined component'] if p['proposal_id']=='W05-FINAL-MAT-032' else ['Peptone (0.01 %']
    for row in ar:assert not set(blocked)&set(row['other'].split('|'))
    results.append(dict(proposal_id=p['proposal_id'],before_capture=oldpi[p['proposal_id']]['after_capture'],after_capture=p['after_capture'],before_rows=br,after_rows=ar,before_suppressions=[str(x) for x in bs],after_suppressions=[str(x) for x in ass],rejected_aliases_absent=blocked))
mod._check_producer_bindings()
old_ds={d['case_id']:d for d in json.loads((S/'input/selected-decisions.json').read_text())['decisions']};ds=json.loads((S/'final/decisions.json').read_text())['decisions'];case_checks=[]
for d in ds:
    b=old_ds[d['case_id']];changed=[k for k in set(d)|set(b) if d.get(k)!=b.get(k)];assert set(changed)=={'reasoning','parents_reassessment','evidence_ids','issue_refs'}
    for field in ['case_input_sha256','source','occurrence_ids','preserved_downstream_holds','preserved_source_holds','owner_records','missing_requirement','no_change_reason','disposition']:
        assert d.get(field)==b.get(field),field
    case_checks.append(dict(case_id=d['case_id'],base_decision_sha256=objsha(b),selected_decision_sha256=objsha(d),changed_fields=sorted(changed),all_inherited_scope_and_holds_unchanged=True))
receipt=dict(at=datetime.now(timezone.utc).isoformat(),author='/root/buffer_hepes',status='PASS',selected_payloads=checks,strict_command=cmd,strict_exit_code=proc.returncode,partonomy_check='PASS; neither selected parent creates components',current_full_W05_owner_index_records=len(records),selected_current_core_proposals=len(coreps),native_projections=results,case_checks=case_checks,builder=dict(path=str(builder),sha256=sha(builder)),scope='Two final parent payloads and complete source-case deltas. Native row projection uses the full current W05 overlay with only these two parent replacements. Root must separately compose dependency/source deltas and run full campaign accounting and native checks; no maintained changes or export approval.')
(V/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(dict(status='PASS',payloads=2,source_cases=2,soy_rows=len(results[0]['after_rows']),peptone_rows=len(results[1]['after_rows']))))
