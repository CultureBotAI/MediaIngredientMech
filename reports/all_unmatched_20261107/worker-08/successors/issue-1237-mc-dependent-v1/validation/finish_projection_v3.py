"""Finish bounded projection checks, retaining the completed v2 native checks.

The actual producer derives source/date from the new history event. Their exact
change is reported; identity/alias/predicate equivalence remains required.
"""
from dataclasses import asdict
from datetime import datetime, timezone
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import traceback
import yaml

R=Path.cwd(); P=R/'.temp/mc-dependent-successor-v1/final-review'
A=R/'reports/all_unmatched_20261107/worker-08'; O=A/'successors/issue-1237-mc-dependent-v1'
OLD=A/'successors/issue-1237-tenvit-v1'; RUN=P/'projection-attempt-v3'
OWNER='data/ingredients/mapped/Mc_vitamins.yaml'
HEAD='a0190fed72b8f5119432003d1f9c84b8c1de7a48'
BEFORE='59c53dfe4e273ebfc7c3fe86fd4244978868ff1879dcde97af64bbeb61c07123'
AFTER='996fc2bfc69284abcbbe75fba6b069bc41fabb3e35c73d5a493de30ab153bcf3'
CLAW=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw')
CHECKS=[]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def save(n,d):
    with (RUN/n).open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False,default=str);f.write('\n')
def check(ok,description):
    if not ok:raise AssertionError(description)
    CHECKS.append(description)
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m;spec.loader.exec_module(m);return m
def main():
    RUN.mkdir(exist_ok=False)
    start=datetime.now(timezone.utc).isoformat()
    controls=read(P/'native-attempt-v2/controls.json')
    failure=read(P/'native-attempt-v2/failure.json')
    check(len(controls['controls'])==26 and all(x['rejected'] for x in controls['controls']),'26 actual prior native and supplemental negatives retained')
    check(failure['message']=='actual old/new Mc SSSOM rows and suppressions unchanged','precise previous overly broad equality assertion retained')
    previous_inputs=read(P/'native-attempt-v2/catalog-inputs.json')
    check(all(sha(R/path)==h for path,h in previous_inputs['sha256_by_path'].items()),'same full catalog inputs as successful native checks')
    catalog={path:yaml.safe_load((R/path).read_text()) for path in previous_inputs['sha256_by_path']}
    proposals=read(OLD/'proposals.json')['proposals']
    old_overlay=dict(catalog)
    for p in proposals:
        ref=p['after_capture']; path=A/ref['path']
        check(sha(path)==ref['sha256']==previous_inputs['prior_payloads'][p['proposal_id']]['sha256'],'prior payload exact '+p['proposal_id'])
        old_overlay[p['owner_path']]=yaml.safe_load(path.read_text())
    before_path=O/'beforeimages/Mc_vitamins.yaml';after_path=O/'payloads/Mc_vitamins.yaml'
    check(sha(before_path)==sha(R/OWNER)==BEFORE and sha(after_path)==AFTER,'exact maintained before and candidate')
    before=yaml.safe_load(before_path.read_text());after=yaml.safe_load(after_path.read_text())
    new_overlay=dict(old_overlay);new_overlay[OWNER]=after
    entry=CLAW/'scripts/build_mim_ingredient_sssom.py';builder=module('mc_actual_claw_projection_v3',entry)
    builder._check_producer_bindings()
    producer_hashes={str(p):hashlib.sha256(raw).hexdigest() for p,raw in builder._IMPORTED_PRODUCER_BYTES.items()}
    check(producer_hashes[str(entry)]==sha(entry),'actual producer source binding')
    check(subprocess.check_output(['git','-C',str(CLAW),'rev-parse','HEAD'],text=True).strip()=='76c1ebeea3fc7f80bf1abe044688f298f390cfac','actual Claw head')
    projections={}
    for label,overlay,record,path in [('before',old_overlay,before,before_path),('after',new_overlay,after,after_path)]:
        subjects={builder._mim_curie(Path(owner).name):rec for owner,rec in overlay.items()}
        check(len(subjects)==len(overlay),'full overlay distinct subjects '+label)
        owners=builder.build_owner_index(subjects);supp=[]
        rows=builder._row_from_yaml(path,{},{},{},{},record=record,owners=owners,suppressions=supp)
        projections[label]={'rows':rows,'suppressions':[asdict(s) for s in supp]}
    save('actual-projections.json',projections)
    check(len(projections['before']['rows'])==len(projections['after']['rows'])>0,'nonempty equal row counts')
    changes=[]
    for old,new in zip(projections['before']['rows'],projections['after']['rows'],strict=True):
        fields={key:{'before':old.get(key),'after':new.get(key)} for key in old.keys()|new.keys() if old.get(key)!=new.get(key)}
        changes.append(fields)
        check(set(fields)=={'mapping_date','source'},'only actual history date and curator provenance change')
        check(old['mapping_date']=='2026-09-07' and new['mapping_date']=='2026-11-08','exact old/new event dates')
        check('mediaingredientmech-agentic-curation' in old['source'] and after['curation_history'][-1]['curator'] in new['source'],'actual historical/new curators')
        check(old['subject_id']==new['subject_id']=='MIM:Mc_vitamins','same subject')
        check(old['object_id']==new['object_id']==after['identifier'],'same own identifier')
        check(old['predicate_id']==new['predicate_id']=='skos:exactMatch','same Rule D identity predicate')
        check(old['other']==new['other'],'same alias surface')
    check(projections['before']['suppressions']==projections['after']['suppressions'],'same suppressed token assertions')
    builder._check_producer_bindings()
    native=module('mc_actual_sssom_rules_v3',R/'scripts/validate_sssom_invariants.py')
    fixture=RUN/'identity-fixture';fixture.mkdir();(fixture/'Mc_vitamins.yaml').write_bytes(after_path.read_bytes())
    native.INGREDIENTS_DIR=fixture;native._subject_to_path.cache_clear()
    rows=projections['after']['rows']
    failures={n:list(getattr(native,'evaluate_rule_'+n)(rows)) for n in ['b1','b2','b3','b5','d']}
    check(not any(failures.values()),'actual Mc rows pass native identity obligations')
    wrong=[dict(row,predicate_id='skos:closeMatch') for row in rows if row['object_id']==after['identifier']]
    rejections=list(native.evaluate_rule_d(wrong))
    check(len(wrong)==len(rejections)>0,'actual Rule D rejects each degraded own-identity row')
    save('projection-assessment.json',{'status':'PASS_IDENTITY_ALIAS_PREDICATE_PRESERVATION_WITH_EXACT_PROVENANCE_DELTA','changes':changes,'native_rules':failures,'actual_rule_D_negative_inputs':wrong,'actual_rule_D_rejections':rejections,'producer_sha256_by_path':producer_hashes,'scope':'Actual in-memory YAML producer and native B1/B2/B3/B5/D on exact Mc fixture. Full before/after overlay owner indices; optional enrichment dictionaries empty. No full emitted SSSOM product, no publication or scientific approval.'})
    check(subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==HEAD,'W08 head unchanged')
    check(sha(before_path)==sha(R/OWNER)==BEFORE and sha(after_path)==AFTER,'before/candidate preserved after final technical checks')
    check(all(sha(R/path)==h for path,h in previous_inputs['sha256_by_path'].items()),'full maintained catalog preserved after checks')
    input_paths=[Path(__file__),P/'native-attempt-v2/controls.json',P/'native-attempt-v2/failure.json',P/'native-attempt-v2/overlay.json',P/'native-attempt-v2/actual-native-call-replay.json',P/'native-attempt-v2/catalog-inputs.json',P/'run_focused_controls_v2.py',before_path,after_path,O/'author/proposal.json',O/'author/decision.json',O/'author/dependency.json',O/'provenance/author.py',OLD/'selection.json',OLD/'proposals.json',R/'src/mediaingredientmech/validation/write_validated.py',R/'src/mediaingredientmech/validation/component_partonomy.py',R/'src/mediaingredientmech/curate/curation_event.py',R/'scripts/validate_sssom_invariants.py']
    result={'status':'PASS_TECHNICAL_ONLY_WITH_PRESERVED_HARNESS_ATTEMPTS','reviewer':'worker08:/root/inorganics','author':'worker08:/root','started_at':start,'completed_at':datetime.now(timezone.utc).isoformat(),'checks':CHECKS,'before_sha256':BEFORE,'payload_sha256':AFTER,'guarded_exact_replay':True,'actual_helper_llm_assisted':True,'baseline_records':len(catalog),'prior_selected_payloads':114,'selected_overlay_payloads':115,'overlay_records':len(new_overlay),'full_context_partonomy':'PASS baseline, prior114 and candidate115; exact v2 receipt retained','negative_controls':{'native_guarded_writer':3,'native_full_overlay_partonomy':4,'supplemental_payload_invariants':7,'supplemental_origin_source_invariants':12,'native_Rule_D':len(rejections)},'known_stereo_defect_passes_native_schema_and_partonomy':True,'identity_alias_predicate_obligations_unchanged':True,'producer_provenance_delta':changes,'owner_admission':'Prior TSB/Bacto failure remains HELD; no new admission claim.','science_approval':False,'final_assembly_review':'Pending exact final selected indices and independent science/lineage receipts.','maintained_or_author_changes':False,'historical_failures':[{'attempt':'native-attempt-v1','reason':'Reviewer incorrectly counted KG downstream holds as CM occurrence IDs; corrected to nested downstream_holds, with zero KG CM occurrence IDs.'},{'attempt':'native-attempt-v2','reason':'Reviewer over-required full SSSOM row equality. Actual source/date must change with appended event; all identity/alias/predicate obligations unchanged. Completed actual native controls are reused with exact input hashes.'}],'input_hashes':{str(p.relative_to(R)):sha(p) for p in input_paths}}
    save('receipt.json',result)
    print(json.dumps({'status':result['status'],'receipt_sha256':sha(RUN/'receipt.json'),'projection_changes':changes,'native_controls':result['negative_controls']},indent=2))
if __name__=='__main__':
    try:main()
    except BaseException as e:
        if RUN.exists():save('failure.json',{'type':type(e).__name__,'message':str(e),'traceback':traceback.format_exc(),'checks':CHECKS})
        raise
