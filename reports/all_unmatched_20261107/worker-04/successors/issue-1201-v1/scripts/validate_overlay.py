"""Read-only checks of prospective owner bytes against the frozen MIM catalog."""
import json, hashlib, subprocess, collections, datetime, sys
from pathlib import Path
import yaml
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from oaklib import get_adapter
ROOT=Path(__file__).resolve().parents[6]
SUCCESSOR=Path(__file__).resolve().parents[1]
ART=ROOT/'reports/all_unmatched_20261107/worker-04'
BASE='e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'
proposals=json.loads((SUCCESSOR/'proposals.json').read_text())['proposals']
sha=lambda b:hashlib.sha256(b).hexdigest()
maintained_diff=subprocess.check_output(['git','diff',BASE,'--name-only','--','data/ingredients','data/curated','mappings','UNIFIED_INGREDIENT_MAPPING.tsv'],cwd=ROOT).decode().splitlines()
untracked=subprocess.check_output(['git','ls-files','--others','--','data/ingredients','data/curated','mappings'],cwd=ROOT).decode().splitlines()
assert not maintained_diff and not untracked,('maintained inputs differ from frozen baseline',maintained_diff,untracked)
baseline={str(p.relative_to(ROOT)):yaml.safe_load(p.read_text()) for category in ['mapped','unmapped'] for p in sorted((ROOT/'data/ingredients'/category).glob('*.yaml'))}
overlay=dict(baseline); errors=[]; rows=[]; seen_owner_paths=set(); seen_destinations=set()
for p in proposals:
    path=p['owner_path']
    destination=p.get('destination_owner_path',p.get('integration_target_path',path))
    if p.get('destination_owner_path') and p.get('integration_target_path') and p['destination_owner_path']!=p['integration_target_path']:errors.append('conflicting integration destinations '+path)
    if destination in seen_destinations:errors.append('duplicate integration destination '+destination)
    seen_destinations.add(destination)
    if destination!=path and (destination in baseline or (ROOT/destination).exists()):errors.append('integration destination already exists '+destination)
    if not destination.startswith(('data/ingredients/mapped/','data/ingredients/unmapped/')) or '..' in Path(destination).parts or Path(destination).suffix!='.yaml':errors.append('unsafe integration destination '+destination)
    if path in seen_owner_paths:errors.append('duplicate proposed owner '+path)
    seen_owner_paths.add(path)
    payload=(ART/p['after_capture']['path']).read_bytes()
    if sha(payload)!=p['after_capture']['sha256']:errors.append('after hash mismatch '+path)
    if path in overlay and path not in baseline:errors.append('duplicate proposed owner '+path)
    if p['kind']=='edit_existing_owner':
        original=subprocess.check_output(['git','show',f'{BASE}:{path}'],cwd=ROOT)
        current=(ROOT/path).read_bytes()
        if sha(original)!=p['before_sha256'] or current!=original:errors.append('before hash/current/frozen mismatch '+path)
    elif path in baseline:errors.append('new owner already exists '+path)
    record=yaml.safe_load(payload); overlay[path]=record
    collisions=[x for x,r in baseline.items() if r.get('identifier')==record.get('identifier') and r.get('mapping_status')!='REJECTED' and x!=path]
    other_proposals=[x['owner_path'] for x in proposals if x['proposal_id']!=p['proposal_id'] and yaml.safe_load((ART/x['after_capture']['path']).read_text()).get('identifier')==record.get('identifier')]
    before_identifier=(baseline.get(path) or {}).get('identifier')
    roles=['nutritional_roles','physicochemical_roles','cellular_metabolic_roles']
    for role in roles:
        if ((baseline.get(path) or {}).get(role) or [])!=(record.get(role) or []):errors.append('unrequested role change '+path+' '+role)
    if (p['kind']=='new_owner' or before_identifier!=record.get('identifier')) and (collisions or other_proposals):errors.append('introduced identifier collision '+path)
    rows.append({'proposal_id':p['proposal_id'],'owner_path':path,'integration_destination':destination,'identifier':record.get('identifier'),'existing_identifier_peers':collisions,'proposed_identifier_peers':other_proposals})
before={str(x) for x in validate_component_partonomy(baseline.values())}; after={str(x) for x in validate_component_partonomy(overlay.values())}
new=sorted(after-before)
errors.extend('introduced partonomy: '+x for x in new)
# Native OAK adapters against existing local ontology stores, with no fetch or rebuild.
adapters={}; labels=[]
for p in proposals:
    rec=overlay[p['owner_path']]; om=rec.get('ontology_mapping') or {}; curie=om.get('ontology_id')
    if not curie:continue
    if curie.startswith(('kgmicrobe.ingredient:','kgmicrobe.compound:')):
        if curie!=rec.get('identifier'):errors.append('registry self mapping differs from identifier '+p['owner_path'])
        inherited_om=(baseline.get(p['owner_path']) or {}).get('ontology_mapping') or {}
        inherited_registry_mapping=all(om.get(k)==inherited_om.get(k) for k in ['ontology_id','ontology_label','ontology_source','mapping_quality'])
        if om.get('mapping_quality')!='FALLBACK_REGISTRY' and not inherited_registry_mapping:errors.append('new registry mapping quality is not FALLBACK_REGISTRY '+p['owner_path'])
        if om.get('ontology_label')!=rec.get('preferred_term'):errors.append('registry label differs from preferred term '+p['owner_path'])
        labels.append({'owner_path':p['owner_path'],'id':curie,'declared_label':om.get('ontology_label'),'status':'local registry identity; not an external ontology lookup','exact_self_identity':curie==rec.get('identifier'),'mapping_quality':om.get('mapping_quality'),'inherited_mapping_quality_preserved_not_approved':inherited_registry_mapping and om.get('mapping_quality')!='FALLBACK_REGISTRY'})
        continue
    prefix=curie.split(':')[0].lower(); db=Path.home()/'.data/oaklib'/f'{prefix}.db'
    row={'owner_path':p['owner_path'],'id':curie,'declared_label':om.get('ontology_label'),'database':str(db)}
    if db.is_file():
        if prefix not in adapters: adapters[prefix]=get_adapter('sqlite:'+str(db))
        actual=adapters[prefix].label(curie); row['canonical_label']=actual; row['exact_canonical_match']=actual==om.get('ontology_label')
        if actual!=om.get('ontology_label'):errors.append('ontology label mismatch '+p['owner_path'])
    elif curie in {'MICRO:0001773','MICRO:0000591'}:
        if curie=='MICRO:0001773':
            capture=ART/'captures/biological/e985257a8f05541b.json';expected='529489a6244363f6ba16a56ce640883d856a893e78a6ca022bb842044f92b911';accessed_at='2026-11-08T05:13:02.966193+00:00'
        else:
            capture=SUCCESSOR/'captures/media/micro-chocolate.json';expected='b91f0b939835e4528cb4c1b50adad0c8d0da1180689c26f78d8ce022dc6b1b33';accessed_at='2026-11-08T05:52:53.603724+00:00'
        assert sha(capture.read_bytes())==expected
        terms=json.loads(capture.read_text())['_embedded']['terms'];matching=[t for t in terms if t['obo_id']==curie and t['is_obsolete'] is False and t['is_defining_ontology'] is True]
        assert len(matching)==1
        actual=matching[0]['label'];row.update({'canonical_label':actual,'exact_canonical_match':actual==om.get('ontology_label'),'status':'Verified original OLS capture; local MICRO adapter absent','capture':str(capture.relative_to(ART)),'capture_sha256':expected,'accessed_at':accessed_at})
        if actual!=om.get('ontology_label'):errors.append('ontology label mismatch '+p['owner_path'])
    elif curie=='mesh:D002374':
        capture=SUCCESSOR/'captures/biological/mesh-catalase-v2.json'
        receipt=json.loads((SUCCESSOR/'captures/biological/mesh-catalase-v2.json.receipt.json').read_text())
        expected='a3a08112b6c6f275dea91240062de6dbc0c112ea0d3180f3bb3f38a165476b51'
        assert sha(capture.read_bytes())==expected==receipt['sha256']
        term=json.loads(capture.read_text())
        assert term['@id']=='http://id.nlm.nih.gov/mesh/D002374' and term['http://id.nlm.nih.gov/mesh/vocab#active'] is True
        actual=term['label']['@value'];row.update({'canonical_label':actual,'exact_canonical_match':actual==om.get('ontology_label'),'status':'Official NLM MeSH capture; inherited Catalase mapping label only, not supplied product identity approval','capture':str(capture.relative_to(ART)),'capture_sha256':expected,'accessed_at':receipt['accessed_at']})
        if actual!=om.get('ontology_label'):errors.append('ontology label mismatch '+p['owner_path'])
    else:row['status']='local adapter unavailable';errors.append('ontology unavailable '+curie)
    labels.append(row)
result={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'baseline':BASE,'proposal_count':len(proposals),'baseline_record_count':len(baseline),'overlay_record_count':len(overlay),'overlay_path_semantics':'Payload semantics replace original owner keys; proposed integration destinations separately checked for uniqueness, safety and pre-existing files. No filesystem move is performed.','maintained_writes':False,'maintained_diff_from_frozen_base':maintained_diff,'untracked_maintained_inputs':untracked,'identity_checks':rows,'partonomy':{'baseline_violations':sorted(before),'overlay_violations':sorted(after),'introduced_violations':new},'ontology_labels':labels,'errors':errors,'status':'FAIL' if errors else 'PASS'}
(SUCCESSOR/'validation/proposal-overlay.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['proposal_count','baseline_record_count','overlay_record_count','errors','status']},indent=2))
sys.exit(bool(errors))
