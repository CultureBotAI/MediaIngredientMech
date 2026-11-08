from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys,types,yaml
W=Path.cwd();B=W/'reports/all_unmatched_20261107/worker-05';P=B/'buffer-parts-v1';O=B/'tellurium-polypeptone-v1';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();j=lambda p:json.loads(p.read_text())
builder=W.parents[4]/'.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py'
assert sha(builder)=='38d59f42953305f6fc51e4fc24dfc59ee1919bfb961595b67a8afe9f8a46a1bc'
sys.path[:0]=[str(builder.parent),str(builder.parent.parent/'src')];mod=types.ModuleType('w05_buffer_parts_native');mod.__file__=str(builder);sys.modules[mod.__name__]=mod;exec(compile(builder.read_bytes(),str(builder),'exec'),mod.__dict__)
old=j(O/'core/proposals.json')['proposals'];new=j(P/'validation/input-proposals.json')['proposals'];assert old==new
oi={p['proposal_id']:p for p in old};baseline={str(p.relative_to(W)):yaml.safe_load(p.read_text()) for p in (W/'data/ingredients').rglob('*.yaml')};over=dict(baseline)
for p in new:
    f=B/p['after_capture']['path'];assert sha(f)==p['after_capture']['sha256'];over.pop(p['owner_path'],None);over[p.get('destination_owner_path',p['owner_path'])]=yaml.safe_load(f.read_text())
owners=mod.build_owner_index({mod._mim_curie(Path(p).name):r for p,r in over.items()})
oldcaps=j(P/'inputs/buffer-source-parts-triage-v1/verified-payloads.json');results=[]
for cap in oldcaps:
    p=oi[cap['proposal_id']];f=B/p['after_capture']['path'];r=yaml.safe_load(f.read_text());before=Path(cap['payload_path']);assert sha(before)==cap['payload_sha256'];br=yaml.safe_load(before.read_text())
    assert 'components' in br and 'component_assertion' in br and 'components' not in r and 'component_assertion' not in r
    rows=mod._row_from_yaml(W/p.get('destination_owner_path',p['owner_path']),{},{},{},{},record=r,owners=owners,suppressions=[])
    historical=mod._row_from_yaml(W/p.get('destination_owner_path',p['owner_path']),{},{},{},{},record=br,owners=owners,suppressions=[])
    assert len(rows)==1 and rows[0]['predicate_id']=='skos:exactMatch' and rows[0]['object_id']==r['identifier']
    results.append(dict(proposal_id=p['proposal_id'],current_capture=p['after_capture'],unchanged_from_predecessor=True,current_rows=rows,historical_before_capture=dict(path=str(before.relative_to(B)),sha256=sha(before)),historical_rows=historical,unsupported_original_components=br['components'],unsupported_original_assertion=br['component_assertion'],current_components_absent=True,current_component_assertion_absent=True,current_history=r['curation_history'],scope='SSSOM describes the whole named preparation. Current local registry is a conditional source handle, not a family-union decision or complete formulation proof.'))
mod._check_producer_bindings();out=P/'validation/native-row-projections.json';assert not out.exists();out.write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),status='PASS',builder=dict(path=str(builder),sha256=sha(builder)),baseline_records=len(baseline),overlay_records=len(over),projection_owner_index='Complete exact current142-proposal path-keyed overlay; optional external dictionaries empty.',reviewed_projections=results,all_selected_payloads_unchanged=True,scope='Four source-qualified stock origins; historical and current rows preserved separately. No maintained application, producer edit, export, identity merger, ingredient/input or dose inference.'),indent=2)+'\n');print(json.dumps({'status':'PASS','proposals':len(results),'current_rows':sum(len(r['current_rows']) for r in results),'overlay_records':len(over)}))
