"""Read-only confirmation of already published route-A origins; no producer changes."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess, yaml

W=Path.cwd(); C=W.parents[2]; B=W/'reports/all_unmatched_20261107/worker-05'
P=B/'buffer-parts-v1'; S=W/'.temp/w05-dependency-route-a-confirmation-v1'; V=S/'validation'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
j=lambda p:json.loads(p.read_text())
def put(p,d):
    assert not p.exists(),p
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(d,indent=2,ensure_ascii=False,default=str)+'\n')
def bind(p): return {'path':str(p.relative_to(W)) if p.is_relative_to(W) else str(p),'sha256':sha(p)}
def manifest(p):
    d=j(p)
    for f in d['files']: assert sha(p.parent/f['path'])==f['sha256'],p.parent/f['path']
    return dict(**bind(p),members=len(d['files']),status='PASS')
base='108e213e96f7d423ee345ce265d692e79063127c'
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==base
plans=[manifest(C/f'preflight/final-component-dependency-plan-v{v}/MANIFEST.json') for v in [1,2]]
protected=[manifest(P/'MANIFEST.json'),manifest(W/'.temp/final-preparation-comparison-v1/MANIFEST.json'),manifest(W/'.temp/w05-late-chem-coordination-v1/MANIFEST.json')]
ps=j(P/'core/proposals.json')['proposals']; ds=j(P/'core/decisions.json')['decisions']; es=j(P/'core/evidence.json')['evidence']
byowner={p['owner_path']:p for p in ps}; assert len(byowner)==len(ps)
deps=j(P/'dependencies-direct-v1/proposals.json')['proposals']; selected={p['proposal_id']:p for p in ps}
opts=j(C/'preflight/final-component-dependency-plan-v2/missing-origin-options-12.json')
generic=[]; withdrawn=[]; rows=[]
for opt in opts:
    p=byowner[opt['owner_path']]; cap=B/p['after_capture']['path']; before=W/p['owner_path']
    assert p['kind']=='edit_existing_owner' and sha(before)==p['before_sha256']==opt['before_sha256']
    assert sha(cap)==p['after_capture']['sha256']
    r=yaml.safe_load(cap.read_text()); old=yaml.safe_load(before.read_text())
    ix=int(opt['claim_keys'][0].split('[')[-1].rstrip(']')); part=r['components'][ix]
    assert r['curation_history'][:len(old['curation_history'])]==old['curation_history']
    assert p['dependency_reassessment']['causal_parent_case_id']=='KG_CASE:ba039f9e4a33baf69eb111ceb979cf6c9ad8fe788c13488f256336508ce94151'
    assert p['dependency_reassessment']['case_input_sha256']=='d42806e437d2e4c72f3e148314c5ef72e8c21f08c78b7b70eebe3d32c83b67d6'
    assert p['dependency_reassessment']['causal_case_is_not_child_recipe_observation'] is True
    if opt['source_disposition']=='GENERIC_REFERENCE_MIGRATION_CANDIDATE':
        assert part['component_id']=='mesh:D010461' and part['reference_scope']=='MIM_CATALOG';generic.append(p['proposal_id'])
    else:
        assert 'component_id' not in part and part['reference_scope']=='UNMAPPED';withdrawn.append(p['proposal_id'])
    rows.append(dict(proposal_id=p['proposal_id'],owner_path=p['owner_path'],before_sha256=p['before_sha256'],after_capture=p['after_capture'],claim_key=opt['claim_keys'][0],source_disposition=opt['source_disposition'],selected_component=part,source_case_ids=p['case_ids'],causal_case_is_not_child_recipe_observation=True))
assert len(generic)==5 and len(withdrawn)==7
composed=[]
for p0 in deps:
    p=selected[p0['proposal_id']]; assert p['after_capture']==p0['after_capture']
    cap=B/p['after_capture']['path']; assert sha(cap)==p['after_capture']['sha256']
    if p['proposal_id'] not in generic+withdrawn:
        r=yaml.safe_load(cap.read_text()); ix=int(p['dependency_reassessment']['claim_key'].split('[')[-1].rstrip(']'))
        assert r['components'][ix]['reference_scope']=='UNMAPPED' and 'component_id' not in r['components'][ix]
        composed.append(dict(proposal_id=p['proposal_id'],owner_path=p['owner_path'],before_sha256=p['before_sha256'],after_capture=p['after_capture'],claim_key=p['dependency_reassessment']['claim_key'],predecessor=p['dependency_reassessment']['selected_predecessor']))
assert len(composed)==3
parent=selected['W05-FINAL-MAT-039']; pr=yaml.safe_load((B/parent['after_capture']['path']).read_text())
assert parent['after_capture']['sha256']=='c083794668a362203de6430eaa2609c34cd8ef78574a1230aa25b4a64fb55fd7'
assert pr['identifier']=='mesh:D010461'
gy=W/'data/ingredients/mapped/GYPS.yaml'; gr=yaml.safe_load(gy.read_text())
assert gr['components'][2]['component_id']=='MICRO:0000178'
assert 'data/ingredients/mapped/GYPS.yaml' not in byowner
marine=byowner['data/ingredients/mapped/Marine_Broth_2216.yaml']; mr=yaml.safe_load((B/marine['after_capture']['path']).read_text())
assert mr['components'][0]['reference_scope']=='UNMAPPED' and 'component_id' not in mr['components'][0]
assert len(ps)==155 and len(ds)==188 and j(P/'core/proposal-lineage.json')['original_count']==138
put(V/'route-a-negative-controls.json',dict(at=datetime.now(timezone.utc).isoformat(),author='/root',base_head=base,status='PASS',plans=plans,selected_parent=parent['after_capture'],generic_ids=generic,withdrawn_new_origin_ids=withdrawn,authentic_missing_origins=rows,composed_existing_origins=composed,GYPS=dict(**bind(gy),component=gr['components'][2],unchanged_no_proposal=True),Marine_Broth_2216=dict(proposal_id=marine['proposal_id'],after_capture=marine['after_capture'],component=mr['components'][0]),other_worker_generic_dependencies=['data/ingredients/mapped/Marine_agar_2216.yaml#components[0]','data/ingredients/mapped/PYGS.yaml#components[0]','data/ingredients/mapped/togo_m2491_mrssi_base.yaml#components[8]'],scope='12 true child proposals and 3 existing composed origins already published; five generic targets conditional on exact accepted mesh:D010461 parent. No duplicated origins, no child recipes claimed in parent source case. Other three generic routes remain coordinator/other-origin composition obligations.'))
put(V/'preservation.json',dict(at=datetime.now(timezone.utc).isoformat(),status='PASS',protected=protected,original_source_head='43f7cf6e8681fa617b5d6d3529d94d537ca01f0d',published_predecessor=base,canonical_core=[bind(P/'core'/f) for f in ['decisions.json','proposals.json','evidence.json','proposal-lineage.json']],counts=dict(cases=len(ds),proposals=len(ps),original_proposals=138,evidence=len(es),occurrence_memberships=sum(len(d['occurrence_ids']) for d in ds)),new_cases=0,new_proposals=0,payload_changes=0))
py=str(W/'.temp/all-unmatched-worker-05/venv/bin/python');env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONPATH='src')
def run(n,cmd):
    r=subprocess.run(cmd,text=True,capture_output=True,env=env);put(V/(n+'.receipt.json'),dict(at=datetime.now(timezone.utc).isoformat(),command=cmd,exit_code=r.returncode));(V/(n+'.stdout.log')).write_text(r.stdout);(V/(n+'.stderr.log')).write_text(r.stderr);assert r.returncode==0,(n,r.stdout,r.stderr);print(n,'PASS')
(V/'strict-dependencies').mkdir()
run('strict-dependencies',[py,'scripts/validate_strict.py']+[str(B/p['after_capture']['path']) for p in deps]+['--workers','1','--out',str(V/'strict-dependencies/failures.tsv')])
contract=j(B/'contracts/frozen-baseline.json');shard=contract['queue']['shards']['5']['path']
run('exact-accounting',[py,str(C/'scripts/audit_worker_outcomes_v1.py'),'--shard',shard,'--decisions',str(P/'core/decisions.json'),'--evidence',str(P/'core/evidence.json'),'--proposals',str(P/'core/proposals.json'),'--artifact-root',str(B),'--source-root',str(Path(shard).parent.parent),'--mim-root',str(W),'--output',str(V/'exact-accounting.json')])
run('lineage',[py,str(B/'final-correction-v1/control/audit_lineage.py'),'--core',str(P/'core'),'--out',str(V/'original-lineage-audit.json')])
print(json.dumps(dict(status='PASS',route_a_missing_origins=len(rows),composed_existing=len(composed),unchanged_all_cases=len(ds),unchanged_all_proposals=len(ps))))
