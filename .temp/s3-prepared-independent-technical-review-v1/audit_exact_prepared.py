"""2026-11-12 independent read-only audit of the exact completed S3 preparation.

No native source replay/apply, scientific judgment, lease acquisition or policy
change. Writes only immutable evidence for the native technical review.
"""
from pathlib import Path
import datetime
import hashlib
import json
import math
import os
import stat
import subprocess
import yaml

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
C = ROOT.parents[1]
STAGE = ROOT / '.temp/cumulative-source-successor-stage-s3-v1'
MANIFEST_SHA = '1c459a680f479d93370d38739e97089bccf50ad1dcf758a90978b452513aa2f7'
BASE = '3b6a0b54edddac053cf7f7cf2d9c8f63fb11c015'
START = datetime.datetime.now(datetime.timezone.utc).isoformat()
sha = lambda b: hashlib.sha256(b).hexdigest()
encoded = lambda v: (json.dumps(v, indent=2, ensure_ascii=False, allow_nan=False)+'\n').encode()
digest = lambda v: sha(json.dumps(v, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode())
observed = {}

def read(path, expected=None):
    path = Path(path)
    assert path.is_absolute() and path.resolve() == path, str(path)
    if expected is None:
        raw = path.read_bytes()
    else:
        raw = path.read_bytes()
        assert sha(raw) == expected, str(path)
    assert str(path) not in observed or observed[str(path)] == sha(raw), 'input drift: '+str(path)
    observed[str(path)] = sha(raw)
    return raw

def js(path, expected=None): return json.loads(read(path, expected))
def ya(path, expected=None): return yaml.load(read(path, expected), Loader=yaml.CSafeLoader)
def pinned(root, refs):
    for name, pin in refs.items():
        if pin is None:
            assert not os.path.lexists(root/name), str(root/name)
        else:
            read(root/name, pin)

manifest = js(STAGE/'manifest.json', MANIFEST_SHA)
head = subprocess.check_output(['git','--no-optional-locks','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
assert head == manifest['identity']['head'] == BASE
assert manifest['state']=='PREPARED_CANDIDATE_ONLY' and manifest['release_approval_added'] is False
assert manifest['root']==str(ROOT)
request = js(ROOT/manifest['request']['path'], manifest['request']['sha256'])
inspected = js(ROOT/'.temp/cumulative-source-successor-inspected-s3-v2/INSPECTED-REQUEST.json','336140127434edbd22467b4a9e58ae5e18d7be3c082c0fd20fca929e7e14dfaa')
restored = json.loads(json.dumps(request)); restored['review_inputs']={}
for op in restored['operations']: op.update(primary=None,skeptic=None)
assert restored == inspected
assert len(request['operations'])==14 and len({op['mim_id'] for op in request['operations']})==14
context=js(ROOT/request['context']['path'],request['context']['sha256'])
payloads=js(ROOT/request['payloads']['path'],request['payloads']['sha256'])
source_context=js(ROOT/request['source_context']['path'],request['source_context']['sha256'])
pinned(ROOT,manifest['inputs'])
closure_counts={}
for root, refs in manifest['predecessor_closure'].items():
    pinned(Path(root),refs);closure_counts[root]=len(refs)
for name,pin in manifest['outputs'].items(): read(STAGE/'candidate'/name,pin)
pinned(ROOT,manifest['before_inventory']);pinned(ROOT,manifest['ledger_sha256']);pinned(ROOT,manifest['publication_beforeimages'])
assert len(manifest['before_inventory'])==len(manifest['after_inventory'])==2957
actual_paths={str(p.relative_to(ROOT)) for category in ['mapped','unmapped'] for p in (ROOT/'data/ingredients'/category).glob('*.yaml')}
assert actual_paths==set(manifest['before_inventory'])
owners={name:ya(ROOT/name,pin) for name,pin in manifest['before_inventory'].items()}
after=dict(owners); reports={}; union={}; scientists=set(); matrix=[]
for op in request['operations']:
    before=owners[op['before']['path']]
    proposed=ya(ROOT/op['proposal']['path'],op['proposal']['sha256'])
    candidate=ya(STAGE/'candidate'/op['after_path'],manifest['outputs'][op['after_path']])
    assert candidate==proposed and before['mim_id']==candidate['mim_id']==op['mim_id']
    changed={k for k in set(before)|set(candidate) if (k in before)!=(k in candidate) or before.get(k)!=candidate.get(k)}
    assert changed==set(op['delta'])
    for name, delta in op['delta'].items():
        assert delta['before_present']==(name in before) and delta['after_present']==(name in candidate)
        assert delta['before']==before.get(name) and delta['after']==candidate.get(name)
    assert candidate['curation_history'][:len(before['curation_history'])]==before['curation_history']
    assert len(candidate['curation_history'])>len(before['curation_history'])
    assert not changed & {'mim_id','roles','components','occurrence_count','occurrences','culturemech_references'}
    del after[op['before']['path']];after[op['after_path']]=candidate
    if op['before']['path']!=op['after_path']: assert manifest['moves'][op['before']['path']]==op['after_path']
    target_payload=next(x for x in payloads if x['mim_id']==op['mim_id'])
    identities=[]
    for role in ['primary','skeptic']:
        ref=op[role]
        if ref['path'] not in reports:
            report=ya(ROOT/ref['path'],ref['sha256']);read(ROOT/str(Path(ref['path']).with_name('review.md')),ref['markdown_sha256']);reports[ref['path']]=report
            assert report['completion']=='completed' and report['scientific_review'] is True and report['verdict'] in ['pass','pass_with_limitations']
            assert report['source']['git_revision']==BASE
            for item in report['source']['inputs']:
                assert union.get(item['path'],item['sha256'])==item['sha256'];union[item['path']]=item['sha256'];read(ROOT/item['path'],item['sha256'])
        report=reports[ref['path']];identities.append(report['reviewer']['identity']);scientists.add(report['reviewer']['identity'])
        target=next(t for t in report['targets'] if t['target_id']==ref['target_id'])
        assessment=next(a for a in report['assessments'] if a['assessment_id']==ref['assessment_id'])
        assert target['semantic_digest']['sha256']==digest(target_payload)
        assert assessment['outcome']=='supported' and assessment['target_ids']==[op['mim_id']]
        checks=[x for x in report['checks'] if x['required'] and op['mim_id'] in x['target_ids']]
        assert checks and all(x['status']=='passed' for x in checks)
        dims={x['name']:x['value'] for x in assessment['dimensions']}
        assert dims['curation_action']=='apply_exact_source_delta' and dims['delta_sha256']==digest(op['delta']) and dims['permanent_mim_id']==op['mim_id']
        assert dims['residual_holds_json']==encoded(op['residual_holds']).decode().strip()
        assert dims['rejected_identifiers_json']==encoded(op['rejected_identifiers']).decode().strip()
        assert dims['corrective_delta_findings']=='none'
        active=[x for x in report['findings'] if op['mim_id'] in x['target_ids'] and x['status'] in ['open','deferred']]
        assert dims['residual_findings_json']==encoded(active).decode().strip()
        if role=='skeptic':assert report['reviewer']['independence']=='independent' and report['reviewer']['independence_basis']
    assert len(set(identities))==2
    matrix.append({'mim_id':op['mim_id'],'before':op['before'],'after_path':op['after_path'],'after_sha256':manifest['outputs'][op['after_path']],'changed_fields':sorted(changed),'history_prefix_preserved':True,'inherited_holds':op['inherited_holds'],'residual_holds':op['residual_holds'],'rejected_identifiers':op['rejected_identifiers'],'primary':op['primary'],'skeptic':op['skeptic']})
assert 'Codex /root/canary_cache_compatibility' not in scientists and len(reports)==2
assert set(manifest['outputs'])=={op['after_path'] for op in request['operations']}|{'data/curated/mapped_ingredients.yaml','data/curated/unmapped_ingredients.yaml','data/curation_successor.json'}
assert set(after)==set(manifest['after_inventory'])
for name,value in after.items():
    expected=manifest['outputs'].get(name,manifest['before_inventory'].get(name));assert manifest['after_inventory'][name]==expected
for category in ['mapped','unmapped']:
    aggregate=ya(STAGE/'candidate/data/curated'/f'{category}_ingredients.yaml')
    actual={r['mim_id']:r for r in aggregate['ingredients']}
    expected={r['mim_id']:{k:v for k,v in r.items() if k!='discussions'} for p,r in after.items() if p.split('/')[2]==category}
    assert len(actual)==len(aggregate['ingredients']) and actual==expected
    assert aggregate['total_count']==len(actual)
assert manifest['native_validation']['roundtrip']=={'complete_owners':2957,'native_exporter':True,'maintained_writes':False}
assert manifest['native_validation']['native_write_dry_run']['applied'] is False
budget=manifest['operational_budget'];policy=js(ROOT/budget['policy']['path'],budget['policy']['sha256'])
assert policy==budget['policy_value']=={'lease_seconds':259200,'evidence_max_age_seconds':259200,'safety_factor':2,'additional_overhead_seconds':600}
fit=js(ROOT/budget['measurement']['path'],budget['measurement']['sha256'])
assert read(STAGE/'fit-context.json',fit['context']['sha256'])==encoded({k:v for k,v in manifest.items() if k!='operational_budget'})
assert fit['input_closure']['qualified_predecessor']==manifest['predecessor_closure']
for section in ['target','owner_states','publication_beforeimages','staged']:pinned(ROOT,fit['input_closure'][section])
assert fit['lease_namespace']==budget['lease_namespace'] and fit['measured_current_owner_count']==2957
assert fit['maintained_writes'] is fit['lease_acquired'] is False
states=fit['input_closure']['owner_states'];rawstates={n:read(ROOT/n,h) for n,h in states.items() if h is not None};outraw={n:read(STAGE/'candidate'/n,h) for n,h in manifest['outputs'].items()}
before_bytes=sum(map(len,rawstates.values()));peak_bytes=sum(max(len(b),len(outraw.get(n,b))) for n,b in rawstates.items())+sum(len(b) for n,b in outraw.items() if states.get(n) is None)
counts={'owner_outputs':14,'replacements':sum(states.get(n) is not None for n in outraw),'installations':sum(states.get(n) is None for n in outraw),'relocations':len(manifest['moves']),'rechecks':16+8*len(outraw)+6*len(manifest['moves']),'peak_growth_factor':max(1,peak_bytes/before_bytes,(len(states)+len(manifest['moves']))/len(states))}
assert counts==budget['counts']
assert len(fit['sample_seconds'])==2 and all(x>0 for x in fit['sample_seconds'])
forecast=(max(fit['sample_seconds'])*counts['peak_growth_factor']*counts['rechecks']+budget['startup_seconds']+fit['backup_seconds'])*2+600
assert forecast==budget['forecast_seconds'] and math.isfinite(forecast) and forecast<259200
assert budget['startup_seconds']>=budget['terminal_predecessor_replay_seconds']>0
age=(datetime.datetime.now(datetime.timezone.utc)-datetime.datetime.fromisoformat(fit['measured_at'])).total_seconds();assert 0<=age<=259200
ns=budget['lease_namespace'];lockdir=Path(ns['locks_dir']);workspace=Path(ns['workspace_root'])
assert lockdir.resolve()==lockdir and workspace.resolve()==workspace and lockdir==workspace/'locks'
assert workspace==Path(manifest['claw']['root'])/'workspace' and ns['resource']=='mediaingredientmech' and ns['conflicting_global_resource']=='global'
assert all(os.environ.get(k) is None for k in ['OPENCLAW_WORKSPACE','OPENCLAW_ORCHESTRATION_ROOT'])
entries=sorted(p.name for p in lockdir.iterdir())
for name in ['mediaingredientmech.lock','global.lock']:assert not os.path.lexists(lockdir/name), 'current conflicting lease: '+name
for name in entries:assert stat.S_ISREG((lockdir/name).lstat().st_mode)
logs=C/'preflight/cumulative-source-canary-s3-native-preparation-v1'
terminal=js(logs/'RESULT.json');assert terminal['exit_code']==0;assert js(logs/'stdout.json',terminal['stdout_sha256'])==manifest;read(logs/'stderr.txt',terminal['stderr_sha256'])
assert sha((STAGE/'manifest.json').read_bytes())==MANIFEST_SHA
assert subprocess.check_output(['git','--no-optional-locks','rev-parse','HEAD'],cwd=ROOT,text=True).strip()==BASE
result={'started_at':START,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS_EXACT_PREPARED_TECHNICAL_AUDIT_NOT_APPLIED','manifest_sha256':MANIFEST_SHA,'head':head,'manifest_inputs_checked':len(manifest['inputs']),'qualified_predecessor_input_counts':closure_counts,'total_distinct_files_read':len(observed),'owner_inventory':2957,'owner_outputs':14,'total_outputs':17,'moves':manifest['moves'],'scientific_reports':list(reports),'scientists':sorted(scientists),'scientific_input_union_count':len(union),'all_scientific_required_checks_passed':True,'all_scientific_delta_dimensions_exact':True,'complete_aggregates_equal_after_records':True,'unselected_records_unchanged':True,'mint_lifecycle_unchanged':True,'mapping_beforeimages_unchanged':True,'original_context_and_operation_holds_unchanged':True,'historical_obligations_sha256':digest(context['historical_obligations']),'historical_reviews':[x['review_id'] for x in context['historical_obligations']],'operational_budget_sha256':digest(budget),'lease_namespace_sha256':digest(ns),'budget':budget,'recomputed_forecast_seconds':forecast,'fit_age_seconds_at_audit':age,'namespace_readback':{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'namespace':ns,'entries_including_hidden':entries,'mediaingredientmech_and_global_leases_absent':True,'scheduling':'Only root-owned sequential apply is accepted for this exact namespace; actual native hierarchy lock acquisition and terminal expiry/ownership checks remain mandatory. No lease acquired or reserved by reviewer.'},'native_roundtrip_and_write_dry_run_receipt':manifest['native_validation'],'new_scientific_votes':0,'native_apply_or_replay':False,'policy_changes':False,'findings':[]}
for name,value in [('AUDIT.json',result),('DELTA-MATRIX.json',matrix),('OBSERVED-INPUT-PINS.json',observed),('SCIENTIFIC-INPUT-UNION.json',union)]:
    with (OUT/name).open('x') as stream:stream.write(encoded(value).decode())
print(json.dumps({'status':result['status'],'outputs':17,'scientific_union':len(union),'files_checked':len(observed),'forecast_seconds':forecast,'audit_sha256':sha((OUT/'AUDIT.json').read_bytes())}))
