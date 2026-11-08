from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, os, subprocess, sys, types
import yaml
from mediaingredientmech.validation.write_validated import validate_ingredient, write_validated_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy

W=Path.cwd(); S4=W/'.temp/w05-buffer-parts-v1'; S=S4/'parents-direct-v1'; OLD=S4/'parents'; B=W/'reports/all_unmatched_20261107/worker-05'; V=S/'validation'; V.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
objsha=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
load=lambda p:json.loads(p.read_text())
resolve=lambda c:S4/c['path'].removeprefix('buffer-parts-v1/') if c['path'].startswith('buffer-parts-v1/') else B/c['path']
ps=load(S/'proposals.json')['proposals']; oldps=load(OLD/'final/proposals.json')['proposals']; oldpi={p['proposal_id']:p for p in oldps}
checks=[]; paths=[]; selected={}; previous={}
for p in ps:
    pid=p['proposal_id']; f=resolve(p['after_capture']); assert sha(f)==p['after_capture']['sha256']; paths.append(f)
    r=yaml.safe_load(f.read_text()); before=yaml.safe_load(resolve(oldpi[pid]['after_capture']).read_text()); selected[pid]=r; previous[pid]=before
    assert not validate_ingredient(r)
    out=V/'guarded-readback'/f.name; write_validated_ingredient(r,out); assert yaml.safe_load(out.read_text())==r
    changed=sorted(k for k in set(before)|set(r) if before.get(k)!=r.get(k))
    if pid=='W05-FINAL-MAT-032':
        assert r==before and p==oldpi[pid]
        assert sha(f)==oldpi[pid]['after_capture']['sha256']
    else:
        assert pid=='W05-FINAL-MAT-039'; assert set(changed)=={'identifier','ontology_mapping','curation_history','notes'}
        assert r['curation_history'][:-1]==before['curation_history']
        assert r['ontology_mapping']['evidence'][:-3]==before['ontology_mapping']['evidence']
        assert all(x['evidence_type']=='LLM_SUGGESTION' for x in r['ontology_mapping']['evidence'][-3:])
        assert r['identifier']=='mesh:D010461'
        assert r['ontology_mapping']['ontology_id']=='mesh:D010461'
        assert r['ontology_mapping']['ontology_label']=='Peptones'
        assert r['ontology_mapping']['mapping_quality']=='EXACT_MATCH'
    checks.append(dict(proposal_id=pid,predecessor_capture=oldpi[pid]['after_capture'],after_capture=p['after_capture'],guarded_readback_sha256=sha(out),strict_closed_schema='PASS',changed_fields=changed,prior_history_events_preserved=len(before['curation_history']),prior_evidence_objects_preserved=len(before['ontology_mapping']['evidence'])))
assert not validate_component_partonomy(list(selected.values()))
cmd=[str(W/'.temp/all-unmatched-worker-05/venv/bin/python'),'scripts/validate_strict.py']+[str(f) for f in paths]+['--workers','1','--out',str(V/'strict-failures.tsv')]
proc=subprocess.run(cmd,capture_output=True,text=True,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONPATH='src')); (V/'strict.stdout.log').write_text(proc.stdout); (V/'strict.stderr.log').write_text(proc.stderr); assert proc.returncode==0
builder=W.parents[4]/'.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py'; assert sha(builder)=='38d59f42953305f6fc51e4fc24dfc59ee1919bfb961595b67a8afe9f8a46a1bc'
sys.path[:0]=[str(builder.parent),str(builder.parent.parent/'src')]; mod=types.ModuleType('parents_direct_projection'); mod.__file__=str(builder); sys.modules[mod.__name__]=mod; exec(compile(builder.read_bytes(),str(builder),'exec'),mod.__dict__)
records={str(q.relative_to(W)):yaml.safe_load(q.read_text()) for q in (W/'data/ingredients').rglob('*.yaml')}
coreps=load(B/'tellurium-polypeptone-v1/core/proposals.json')['proposals']
for q in coreps:
    f=B/q['after_capture']['path']; assert sha(f)==q['after_capture']['sha256']; records.pop(q['owner_path'],None); records[q.get('destination_owner_path',q['owner_path'])]=yaml.safe_load(f.read_text())
for p in oldps: records[p['owner_path']]=previous[p['proposal_id']]
before_records=dict(records)
for p in ps: records[p['owner_path']]=selected[p['proposal_id']]
owner=lambda rs:mod.build_owner_index({mod._mim_curie(Path(n).name):v for n,v in rs.items()})
bi=owner(before_records); ai=owner(records); projections=[]
for p in ps:
    pid=p['proposal_id']; bs=[]; ass=[]
    br=mod._row_from_yaml(W/p['owner_path'],{}, {}, {}, {},record=previous[pid],owners=bi,suppressions=bs)
    ar=mod._row_from_yaml(W/p['owner_path'],{}, {}, {}, {},record=selected[pid],owners=ai,suppressions=ass)
    expected=[('skos:exactMatch','MICRO:0000181')] if pid=='W05-FINAL-MAT-032' else [('skos:exactMatch','mesh:D010461')]
    assert [(x['predicate_id'],x['object_id']) for x in ar]==expected
    if pid=='W05-FINAL-MAT-039': assert [(x['predicate_id'],x['object_id']) for x in br]==[('skos:broadMatch','mesh:D011492'),('skos:exactMatch','kgmicrobe.ingredient:peptone')]
    blocked=['Phytone peptone','Phytone peptone (BD-BBL)','Soytone (BD-Difco) or Phytone peptone (BD-BBL)','Soytone','Bacto Soytone','Properties: Undefined component'] if pid=='W05-FINAL-MAT-032' else ['Peptone (0.01 %']
    for row in ar: assert not set(blocked)&set(row['other'].split('|'))
    projections.append(dict(proposal_id=pid,before_capture=oldpi[pid]['after_capture'],after_capture=p['after_capture'],before_rows=br,after_rows=ar,before_suppressions=[str(x) for x in bs],after_suppressions=[str(x) for x in ass],rejected_aliases_absent=blocked))
mod._check_producer_bindings()
old_ds={d['case_id']:d for d in load(OLD/'final/decisions.json')['decisions']}; ds=load(S/'decisions.json')['decisions']; case_checks=[]
for d in ds:
    b=old_ds[d['case_id']]; changed=sorted(k for k in set(d)|set(b) if d.get(k)!=b.get(k))
    if 'W05-FINAL-MAT-039' in d['proposal_ids']: assert set(changed)=={'reasoning','parents_direct_reassessment','evidence_ids'}
    else: assert not changed
    for field in ['case_input_sha256','source','occurrence_ids','preserved_downstream_holds','preserved_source_holds','owner_records','missing_requirement','no_change_reason','disposition','applicability','proposal_ids']:
        assert d.get(field)==b.get(field),field
    case_checks.append(dict(case_id=d['case_id'],base_decision_sha256=objsha(b),selected_decision_sha256=objsha(d),changed_fields=changed,all_inherited_scope_and_holds_unchanged=True))
old_manifest=load(OLD/'MANIFEST.json'); members=old_manifest.get('files',old_manifest.get('members',[])); prior_checks=[]
for row in members:
    path=row.get('path',row.get('relative_path')); assert sha(OLD/path)==row['sha256']; prior_checks.append(path)
receipt=dict(at=datetime.now(timezone.utc).isoformat(),author='/root/buffer_hepes',status='PASS',selected_payloads=checks,strict_command=cmd,strict_exit_code=proc.returncode,partonomy_check='PASS; no component assertions created',current_full_W05_owner_index_records=len(records),selected_current_core_proposals=len(coreps),native_projections=projections,case_checks=case_checks,sealed_parents_members_rehashed=len(prior_checks),builder=dict(path=str(builder),sha256=sha(builder)),scope='Two complete selected parent payloads, one substantive Peptone successor and unchanged Soy. Full current W05 overlay plus sealed parent state is the native comparison baseline. Root must compose independently authored five generic child/RCM and source deltas and rerun complete native campaign checks. No maintained-data or export approval.')
(V/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n'); print(json.dumps(dict(status='PASS',payloads=2,changed_payloads=1,source_cases=2,peptone_before_rows=2,peptone_after_rows=1,old_sealed_files=len(prior_checks))))
