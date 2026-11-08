"""Validate the additive two-case observation and carry-forward structural view."""
import copy, datetime, hashlib, json, subprocess, sys
from pathlib import Path

HERE=Path(__file__).resolve().parents[1]
WORKER=HERE.parents[1]
REPO=next(p for p in HERE.parents if (p/'MAPPING_SEMANTICS.md').is_file())
BASE='d74ab6d48f6345260087cf973cadbe7b6269109f'
CAMPAIGN=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
canon=lambda o:json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()
def read(p):return json.loads(p.read_text())
def write(p,o):p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
cases=read(HERE/'cases.json')['cases'];ds=read(HERE/'decisions.json')['decisions']
assert len(cases)==len(ds)==2
frozen=read(WORKER/'common/frozen-shard-09.json')['cases'];byid={c['case_id']:c for c in frozen}
assert {c['case_id'] for c in cases}=={d['case_id'] for d in ds}
payloads=read(HERE/'scientific-payload-hashes.json')
for c,d in zip(cases,ds):
    assert c==byid[c['case_id']]
    assert d['case_input_sha256']==hashlib.sha256(canon(c)).hexdigest()
    assert hashlib.sha256(canon({k:v for k,v in d.items() if k!='independent_review'})).hexdigest()==payloads['case_hashes'][d['case_id']]
    assert d['disposition']=='existing_identity_or_alias' and d['independent_review']['status']=='complete'
    assert d['retained_holds']['whole_owner_export_disposition']=='WITHHOLD'
    for owner in d['owner_records']:assert sha(REPO/owner['path'])==owner['sha256']
assert sha(HERE/'existing-owner-associations.json')==payloads['association_file_sha256']
assert read(HERE/'proposals.json')['proposals']==[]
associations=read(HERE/'existing-owner-associations.json')['associations']
for c,a in zip(cases,associations):
    assert a['case_id']==c['case_id'] and a['source_record']==c['original_kg_entry']['source_record']
    assert a['source_locator']['medium_id']==14 and a['source_locator']['solution_id']==20
    assert a['maintained_mutation'] is False and a['global_alias_activation'] is False and a['export_approval'] is False
    assert sha(REPO/a['owner_path'])==a['before_sha256']
evidence=read(HERE/'evidence.json')['evidence'];eids={e['evidence_id'] for e in evidence};assert len(eids)==len(evidence)
for e in evidence:
    p=WORKER/e['capture']['path'];assert e['capture']['root']=='artifact' and p.resolve().is_relative_to(WORKER.resolve())
    assert sha(p)==e['capture']['sha256']
for d in ds:
    assert set(d['evidence_ids']+d['independent_review']['evidence_ids'])<=eids
    assert all(d['case_id'] in e.get('case_ids',[d['case_id']]) for e in evidence if e['evidence_id'] in d['evidence_ids'])
protected=read(WORKER/'common/protected-input-hashes.json')['files']
for p,h in protected.items():assert sha(REPO/p)==h, p
prior_manifest=read(WORKER/'MANIFEST.json')
for entry in prior_manifest['files']:
    p=(WORKER if entry['root']=='artifact' else REPO)/entry['path']
    assert sha(p)==entry['sha256'],str(p)
assert not subprocess.check_output(['git','diff','--name-only','--diff-filter=CDMRTUXB',BASE,'--','.']).strip(), 'Previously tracked bytes changed'
subprocess.run(['git','merge-base','--is-ancestor',BASE,'HEAD'],check=True)
assert sha(HERE/'captures/rest-medium-14.capture')==sha(HERE/'provenance/captures/original-medium-14.body')
for meta_path in (HERE/'captures').glob('*.metadata.json'):
    m=read(meta_path)
    if 'sha256' in m:
        assert sha(REPO/m['capture_path'])==m['sha256']

# Build a validation-only full-shard view, preserving all185 untouched decisions.
# It does not claim a new scientific review of those185 historical decisions.
old=read(WORKER/'decisions.json');new_byid={d['case_id']:d for d in ds};integrated=copy.deepcopy(old)
integrated['decisions']=[new_byid.get(d['case_id'],d) for d in old['decisions']]
integrated['followup_scope_note']='Only2 source decisions newly assessed;185 decisions and all32 YAML proposals carried byte-equivalently as JSON values from published parent.'
out=HERE/'validation';write(out/'integrated-decisions.json',integrated)
ev=read(WORKER/'evidence.json');ev['evidence']+=evidence;write(out/'integrated-evidence.json',ev)
cmd=[sys.executable,str(CAMPAIGN/'scripts/audit_worker_outcomes_v1.py'),'--shard',str(CAMPAIGN/'queue/preliminary-v5/shards/shard-09.json'),'--decisions',str(out/'integrated-decisions.json'),'--evidence',str(out/'integrated-evidence.json'),'--proposals',str(WORKER/'proposals.json'),'--artifact-root',str(WORKER),'--source-root',str(CAMPAIGN/'queue/preliminary-v5'),'--mim-root',str(REPO),'--output',str(out/'structural-overlay-audit.json')]
r=subprocess.run(cmd,cwd=REPO,capture_output=True,text=True)
write(out/'structural-command.json',{'command':cmd,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
assert r.returncode==0,(r.stdout,r.stderr)
result={'status':'PASS','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'parent':BASE,'newly_reviewed_cases':2,'new_source_associations':2,'new_owner_payload_proposals':0,'carried_forward_cases':185,'protected_baseline_files_unchanged':len(protected),'prior_manifest_entries_unchanged':len(prior_manifest['files']),'old_tracked_files_changed':[],'whole_shard_structural_overlay':'PASS; not185 new scientific reviews','scientific_approval_from_validator':False,'decision_file_sha256':sha(HERE/'decisions.json'),'evidence_file_sha256':sha(HERE/'evidence.json'),'association_file_sha256':sha(HERE/'existing-owner-associations.json')}
write(out/'followup-validation.json',result);print(json.dumps(result,indent=2))
