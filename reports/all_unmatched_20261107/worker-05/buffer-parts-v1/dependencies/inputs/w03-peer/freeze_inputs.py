from pathlib import Path
import json,hashlib,subprocess,datetime,sys
import yaml
R=Path.cwd();C=R.parents[2];O=R/'.temp/peptone-consumer-independent-v1';P=C/'preflight/final-component-dependency-plan-v1';V=C/'preflight/final-component-dependency-plan-v2'
sha=lambda b:hashlib.sha256(b).hexdigest()
def dump(p,x):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(x,f,indent=2);f.write('\n')
def copy(src,dst):
 assert src.is_file() and not src.is_symlink();dst.parent.mkdir(parents=True,exist_ok=True)
 with dst.open('xb') as f:f.write(src.read_bytes())
 assert src.read_bytes()==dst.read_bytes()
 return {'source_path':str(src),'captured_path':str(dst.relative_to(R)),'sha256':sha(src.read_bytes())}
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip();assert head=='fe31a02850932a7bdf2fe65c93cb636a86f82a2c'
manifest=json.loads((P/'MANIFEST.json').read_text());seal=json.loads((P/'SEAL.json').read_text());assert sha((P/'MANIFEST.json').read_bytes())==seal['manifest_sha256']
for e in manifest['files']:assert sha((P/e['path']).read_bytes())==e['sha256']
captures=[]
for n in ['HANDOFF.json','MANIFEST.json','SEAL.json','minimal-couplings-28.json','source-evidence-refcheck-32.json','source-bindings.json','combined-candidate-bindings.json','plan-input-pins.json','composed-consumer-obligations.json','native-review-v2.yaml','native-review-v2.md','native-review-validation-v2.json']:
 captures.append(copy(P/n,O/'context/plan-v1'/n))
captures.append(copy(V/'ROUTES.md',O/'context/ROUTES.md'))
vmanifest=json.loads((V/'MANIFEST.json').read_text())
for e in vmanifest['files']:assert sha((V/e['path']).read_bytes())==e['sha256']
captures.append(copy(V/'MANIFEST.json',O/'context/route-MANIFEST.json'))
for n in ['MAPPING_SEMANTICS.md','docs/record-reviews.md','docs/record-review-profile.md','docs/stock_components.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','schema/record_review.yaml','.claude/skills/review-yaml-category/SKILL.md']:
 captures.append(copy(R/n,O/'context/contracts'/n))
claims=[x for x in json.loads((P/'minimal-couplings-28.json').read_text()) if (x.get('before_component') or x.get('component') or {}).get('component_id')=='MICRO:0000178'];assert len(claims)==20
bindings=json.loads((P/'source-bindings.json').read_text());binding={x['origin_id']:x for x in bindings}
targets=[];owner_rows=[]
for i,row in enumerate(claims,1):
 key=row['claim_key'];owner=key.split('#')[0];idx=int(key.split('components[')[1].split(']')[0]);new=row['before_owner_path'] is None
 if not new:
  src=R/owner;assert sha(src.read_bytes())==row['before_owner_sha256'];snap=C/'preflight/final-intake-candidate-v1/snapshot/baseline'/owner;assert src.read_bytes()==snap.read_bytes()
 else:
  b=binding[row['source_published_origin']];assert b['payload_sha256']==row['source_payload_sha256'];src=C/'preflight/final-intake-candidate-v1/snapshot/workers/w02'/b['git_path'];assert sha(src.read_bytes())==row['source_payload_sha256']
 dst=O/'context/owners'/Path(owner).name;ref=copy(src,dst);rec=yaml.safe_load(src.read_text());assert rec['components'][idx]==(row.get('before_component') or row['component'])
 target='PC%02d'%i;row['review_target_id']=target;row['captured_owner']=ref;row['owner_kind']='new_owner_proposal' if new else 'existing_maintained_owner';owner_rows.append({'target_id':target,'claim_key':key,'owner_path':owner,'component_index':idx,'owner_sha256':ref['sha256'],'before_sha256':row['before_owner_sha256'],'new_owner':new,'complete_component':rec['components'][idx],'component_assertion':rec.get('component_assertion'),'capture':ref})
 targets.append({'target_id':target,'path':str(dst.relative_to(R)),'label':key,'kind':'record','selector':'components[%d]'%idx,'owner_paths':[{'repository':'MediaIngredientMech','path':owner,'role':'proposed_owner' if new else 'maintained_record'}],'ownership_note':'Exact source-supported component identity only; no whole-owner approval. '+('Unapplied W02 new-owner proposal with genuine null beforeimage.' if new else 'Complete current maintained owner byte-identical to frozen baseline.')})
for e in json.loads((P/'source-evidence-refcheck-32.json').read_text()):assert sha(Path(e['path']).read_bytes())==e['sha256']
preserved=[]
for name in ['.temp/w03-provenance-successor-v1/MANIFEST.json','.temp/w03-provenance-successor-v1/HANDOFF.json','.temp/w03-provenance-successor-v1/PUBLICATION-RECEIPT.json','.temp/complete-identifier-dependencies-v1/MANIFEST.json','reports/all_unmatched_20261107/worker-03/successors/issue1226-v1/MANIFEST.json']:
 p=R/name;preserved.append({'path':name,'sha256':sha(p.read_bytes())})
dump(O/'context/claims-20.json',claims);dump(O/'context/owner-bindings-20.json',owner_rows);dump(O/'targets.json',{'targets':targets})
dump(O/'context/input-receipt.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':head,'plan_manifest_members_verified':len(manifest['files']),'route_manifest_members_verified':len(vmanifest['files']),'evidence_refcheck_files_verified':32,'existing_owner_beforeimages':19,'new_owner_proposals':1,'claims':20,'copies':captures,'prior_seals_to_preserve':preserved,'scope':'20 claims only, 19 baseline refs plus1newMRSSI. No source or candidate scientific approval inferred from hashes. All output confined to new review directory.'})
print(json.dumps({'claims':20,'native_targets':len(targets),'plan_members':len(manifest['files']),'route_members':len(vmanifest['files'])}))
