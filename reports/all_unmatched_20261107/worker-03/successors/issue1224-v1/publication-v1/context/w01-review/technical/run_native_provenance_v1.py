import collections
import copy
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

P = Path(__file__).resolve().parent
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
I = C/'preflight/final-intake-candidate-v1'
M = C/'integration/worktree'
D = C/'integration/final-same-target-reconciliation-v2'
A = C/'assignments/w01-nine-scope-candidates-independent-v1.json'
sys.path.insert(0,str(M/'src'))
from mediaingredientmech.validation.write_validated import validate_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.synonym_policy import is_resolving_synonym
from mediaingredientmech.curate.publication_guard import FrozenFile
from mediaingredientmech.ingredient_bundle_refresh import publish_new_files

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):return json.loads(Path(p).read_text())
def record(p):return yaml.safe_load(Path(p).read_bytes())
def bind(p):return {'path':str(Path(p).resolve()),'sha256':sha(p)}
def save(name,value):
    with (P/name).open('x') as f:json.dump(value,f,indent=2,ensure_ascii=False);f.write('\n')
def hist_subset(small,large):
    # Every exact event retained with multiplicity, without requiring different
    # authors' parallel histories to be a linear chronological prefix.
    enc=lambda v:json.dumps(v,sort_keys=True,ensure_ascii=False)
    return not (collections.Counter(map(enc,small))-collections.Counter(map(enc,large)))

a=load(A);s=load(Path(a['final_candidate_summary']));old=load(D/'candidate-summary-v2.json')
before_hashes={x['path']:x['sha256'] for x in load(I/'baseline-owner-inventory.json')}
baseline={}
for name,digest in before_hashes.items():
    assert sha(M/name)==digest,name
    baseline[name]=record(M/name)
input_checks=[]
for name,digest in s['input_sha256'].items():
    p=Path(name)
    input_checks.append({'path':name,'expected':digest,'actual':sha(p),'equal':sha(p)==digest})
save('pinned-input-hash-check-v1.json',input_checks)
assert all(x['equal'] for x in input_checks)
inventory=lambda:{str(p.relative_to(M)):sha(p) for sub in ['mapped','unmapped'] for p in (M/'data/ingredients'/sub).glob('*.yaml')}
assert inventory()==before_hashes
old_by_id={x['candidate_id']:x for x in old['groups']}
correction_ids={'TARGET-006','TARGET-017','TARGET-032','NEW-OXOID-CM0149'}
metadata=[];overlay=copy.deepcopy(baseline);new_mapping_count=0
for t in s['groups']:
    cid=t['candidate_id'];f=D/t['candidate']['path'];assert sha(f)==t['candidate']['sha256']
    r=record(f);o=old_by_id[cid];of=D/o['candidate']['path'];prior=record(of)
    assert sha(of)==o['candidate']['sha256']
    same=f.read_bytes()==of.read_bytes()
    diffs=[k for k in prior.keys()|r.keys() if prior.get(k)!=r.get(k)]
    item={'candidate_id':cid,'current':bind(f),'first_publication':bind(of),'byte_identical':same,'changed_fields':sorted(diffs)}
    if cid in correction_ids:
        assert set(diffs)=={'ontology_mapping','curation_history'},(cid,diffs)
        assert r['curation_history'][:-1]==prior['curation_history']
        assert r['curation_history'][-1]['action']=='CORRECTED_EVIDENCE_PROVENANCE'
        assert r['curation_history'][-1]['llm_assisted'] is True
        old_ev=prior['ontology_mapping']['evidence'];new_ev=r['ontology_mapping']['evidence']
        assert len(old_ev)==len(new_ev)
        for x,y in zip(old_ev,new_ev):
            assert x['evidence_type']=='MANUAL_CURATION' and y['evidence_type']=='LLM_SUGGESTION'
            assert set(x)==set(y)
            assert all(x[k]==y[k] for k in x if k not in ['evidence_type','notes'])
            assert y['notes'].endswith(x['notes'])
            assert 'Agent-authored interpretation' in y['notes'] and 'not human-supplied evidence' in y['notes']
            assert 'issues/1226' in y['notes']
        om=copy.deepcopy(prior['ontology_mapping']);om['evidence']=new_ev;assert r['ontology_mapping']==om
        new_mapping_count+=len(new_ev)
        item.update(corrected_mapping_entries=len(new_ev),complete_first_publication_history_prefix=True,new_event=r['curation_history'][-1])
    else:assert same,cid
    metadata.append(item);overlay[t['owner_path']]=r
assert len(metadata)==37 and sum(x['byte_identical'] for x in metadata)==33 and new_mapping_count==13
save('mapping-evidence-and-reuse-v1.json',metadata)

rows=[];native_errors=[]
for t in a['candidates']:
    cid=t['candidate_id'];f=D/t['candidate']['path'];r=record(f)
    assert next(x for x in s['groups'] if x['candidate_id']==cid)==t
    tp=f.parent/'trace.json';assert load(tp)==t
    current=FrozenFile.capture(f);current.verify()
    b=record(D/t['before_capture']) if t['before_capture'] else None
    if b is not None:
        assert sha(D/t['before_capture'])==t['before_sha256']==before_hashes[t['owner_path']]
        assert (D/t['before_capture']).read_bytes()==(M/t['owner_path']).read_bytes()
        assert r['curation_history'][:len(b.get('curation_history',[]))]==b.get('curation_history',[])
    else:
        assert cid=='NEW-OXOID-CM0149' and t['owner_path'] not in baseline
        assert t['before_sha256'] is None and t['operation']=='new'
        assert r['curation_history'][0]['action']=='CREATED'
        assert r['curation_history'][0]['llm_assisted'] is True
    origins=[]
    for o in t['origins']:
        op=I/o['payload_path'];ov=record(op);assert sha(op)==o['payload_sha256']
        preserved=hist_subset(ov.get('curation_history',[]),r.get('curation_history',[]))
        if cid!='NEW-OXOID-CM0149':assert preserved,(cid,o['entry_id'])
        else:assert not preserved
        capture_checks=[]
        for ev in o.get('evidence',[]):
            target=Path(ev['guarded_capture_path']);digest=ev['capture']['sha256']
            capture_checks.append({'evidence_id':ev['evidence_id'],'path':str(target),'sha256':sha(target),'expected':digest,'equal':sha(target)==digest,'kind':ev['kind'],'url':ev.get('url'),'locator':ev.get('locator')})
        assert all(v['equal'] for v in capture_checks)
        origins.append({'entry_id':o['entry_id'],'payload':bind(op),'origin_history_event_count':len(ov.get('curation_history',[])),'events_preserved_as_owner_history':preserved,'new_oxoid_origin_is_historical_source_only':cid=='NEW-OXOID-CM0149','case_bindings':o['case_bindings'],'evidence':capture_checks})
    assert sorted(set(x for o in t['origins'] for x in o['case_ids']))==sorted(set(t['case_ids']))
    assert sorted(set(x for o in t['origins'] for cs in o['case_bindings'] for x in cs['occurrence_ids']))==sorted(set(t['occurrence_ids']))
    err=[x.message for x in validate_ingredient(r)];native_errors+=err
    alias=[{'text':x['synonym_text'],'type':x.get('synonym_type'),'source':x.get('source'),'resolves':is_resolving_synonym(x)} for x in r.get('synonyms',[])]
    before_alias=[{'text':x['synonym_text'],'type':x.get('synonym_type'),'source':x.get('source'),'resolves':is_resolving_synonym(x)} for x in (b or {}).get('synonyms',[])]
    rows.append({'candidate_id':cid,'owner_path':t['owner_path'],'candidate':bind(f),'trace':bind(tp),'authentic_before':bind(D/t['before_capture']) if b else None,'schema_errors':err,'origins':origins,'aliases':alias,'before_aliases':before_alias,'baseline_history_prefix_preserved':True if b else 'not_applicable_new_creation','full_candidate_history':r.get('curation_history'),'changed_fields_from_before':[k for k in (b or {}).keys()|r.keys() if (b or {}).get(k)!=r.get(k)]})
save('nine-candidate-lineage-schema-alias-v1.json',rows)
assert not native_errors
base_errors=[str(v) for v in validate_component_partonomy(baseline.values())]
full_errors=[str(v) for v in validate_component_partonomy(overlay.values())]
introduced=list((collections.Counter(full_errors)-collections.Counter(base_errors)).elements())
assert len(baseline)==2956 and len(overlay)==2957

# Meaningful controls execute the same native validators/guards, only against
# disposable private objects. No candidate, source, or maintained byte is changed.
negative={}
test=copy.deepcopy(record(D/a['candidates'][0]['candidate']['path']));test['technical_unknown_field_control']=True
negative['closed_schema_unknown_field']=[x.message for x in validate_ingredient(test)];assert negative['closed_schema_unknown_field']
bad=copy.deepcopy(overlay);parent=next(k for k,v in bad.items() if v.get('components'))
bad[parent]['components'][0].update(component_id='kgmicrobe.ingredient:technical_review_nonexistent_part',mapping_status='MAPPED',reference_scope='MIM_CATALOG')
negative['partonomy_missing_target']=[str(v) for v in validate_component_partonomy(bad.values()) if 'technical_review_nonexistent_part' in str(v)];assert negative['partonomy_missing_target']
fixtures=P/'guard-controls';fixtures.mkdir()
drift=fixtures/'input-drift.txt';drift.write_text('original private control\n');frozen=FrozenFile.capture(drift);drift.write_text('changed private control\n')
try:frozen.verify();raise AssertionError('drift not refused')
except ValueError as e:negative['frozen_input_change_refused']=str(e)
occupied=fixtures/'occupied-output.txt';occupied.write_text('original private sentinel\n');initial=occupied.read_bytes()
try:publish_new_files([(occupied,b'wrong replacement')],lambda:None);raise AssertionError('existing output not refused')
except FileExistsError as e:negative['existing_output_refused']=str(e)
assert occupied.read_bytes()==initial
assert inventory()==before_hashes
for x in input_checks:assert sha(x['path'])==x['expected']
sources=[M/q for q in ['src/mediaingredientmech/validation/write_validated.py','src/mediaingredientmech/validation/component_partonomy.py','src/mediaingredientmech/schema/mediaingredientmech.yaml','src/mediaingredientmech/synonym_policy.py','src/mediaingredientmech/curate/publication_guard.py','src/mediaingredientmech/ingredient_bundle_refresh.py','MAPPING_SEMANTICS.md']]
save('native-full-projection-v1.json',{'at':datetime.now(timezone.utc).isoformat(),'reviewer':'OpenAI Codex /root/issue_context independent technical review','assignment':bind(A),'summary':bind(Path(a['final_candidate_summary'])),'native_sources':[bind(q) for q in sources],'baseline_count':len(baseline),'overlay_count':len(overlay),'overlay_scope':'All 37 active author candidates over complete authentic 2956-owner baseline; schema/lineage review is the assigned nine only.','baseline_partonomy_errors':base_errors,'full_overlay_partonomy_errors':full_errors,'introduced_errors':introduced,'negative_controls':negative,'maintained_owner_hashes_unchanged':len(before_hashes),'pinned_inputs_rechecked':len(input_checks),'new_mapping_evidence_entries':new_mapping_count,'byte_reused_other_candidates':33,'scientific_approval':False})
print(json.dumps({'native_schema_errors':native_errors,'baseline':len(baseline),'overlay':len(overlay),'baseline_errors':len(base_errors),'overlay_errors':len(full_errors),'introduced_errors':introduced,'input_checks':len(input_checks),'negative_controls':list(negative),'receipt':bind(P/'native-full-projection-v1.json')}))
