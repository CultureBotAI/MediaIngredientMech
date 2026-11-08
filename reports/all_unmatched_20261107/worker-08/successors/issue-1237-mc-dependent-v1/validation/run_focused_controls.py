"""Independent bounded technical checks; all output stays in this private lane.

The native validators are called without mocks. Supplemental history, source and
origin comparisons are explicitly distinct from those native gates. This module
does not run author main(), publish an export, or grant scientific approval.
"""
from __future__ import annotations

import copy
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import traceback

import yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import write_validated_ingredient, ValidationFailedError
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy

R = Path.cwd()
A = R / 'reports/all_unmatched_20261107/worker-08'
O = A / 'successors/issue-1237-mc-dependent-v1'
OLD = A / 'successors/issue-1237-tenvit-v1'
P = R / '.temp/mc-dependent-successor-v1/final-review'
RUN = P / 'native-attempt-v1'
BASE = 'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'
HEAD = 'a0190fed72b8f5119432003d1f9c84b8c1de7a48'
OWNER = 'data/ingredients/mapped/Mc_vitamins.yaml'
BEFORE = '59c53dfe4e273ebfc7c3fe86fd4244978868ff1879dcde97af64bbeb61c07123'
AFTER = '996fc2bfc69284abcbbe75fba6b069bc41fabb3e35c73d5a493de30ab153bcf3'
CID = 'CM_NAME:d57e91ffaea6f0ab6ff0f3d6f0b04c26356c832e85dd83e9e2319874fda43506'
TRIGGER = 'CM_OCC:a181b24b7eb91c50c771bd1c1fc3012fd0cf28f45b49f2750c3d43bda9cdd531'
PID = 'mc1237-prop-mc-vitamins-dependent'
CLAW = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw')
COMMANDS, CONTROLS, CHECKS = [], [], []


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    return json.loads(Path(p).read_text())


def save(name, data):
    path = RUN / name
    with path.open('x') as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        f.write('\n')


def check(condition, label):
    if not condition:
        raise AssertionError(label)
    CHECKS.append(label)


def command(argv):
    result = subprocess.run(argv, cwd=R, capture_output=True, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'})
    COMMANDS.append({'argv': argv, 'returncode': result.returncode,
                     'stdout_sha256': hashlib.sha256(result.stdout).hexdigest(),
                     'stderr': result.stderr.decode(errors='replace')})
    check(result.returncode == 0, 'command succeeds: ' + ' '.join(argv))
    return result.stdout


def capture(ref):
    check(ref['root'] == 'artifact', 'artifact root')
    p = A / ref['path']
    check(p.is_file() and not p.is_symlink() and p.resolve().is_relative_to(A.resolve()), 'regular artifact capture')
    check(sha(p) == ref['sha256'], 'capture digest: ' + ref['path'])
    return p


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def payload_constraints(before, after):
    for key in set(before) | set(after):
        if key not in {'components', 'component_assertion', 'notes', 'curation_history'}:
            assert before.get(key) == after.get(key), ('unchanged field', key)
    assert after['curation_history'][:-1] == before['curation_history'], 'original history prefix'
    assert len(after['curation_history']) == len(before['curation_history']) + 1 == 5, 'one event'
    event = after['curation_history'][-1]
    assert event['llm_assisted'] is True, 'actual LLM attribution'
    assert event['curator'] == 'worker08:/root SCI-TENVIT-003 dependent source proposal', 'actual author'
    assert event['previous_status'] == event['new_status'] == 'MAPPED', 'no status promotion'
    assert len(after['components']) == len(before['components']) == 10, 'ten input parts'
    for i, (b, a) in enumerate(zip(before['components'], after['components'], strict=True)):
        for field in ['component_name', 'concentration_value', 'concentration_unit']:
            assert b[field] == a[field], ('literal input', i, field)
        if i != 6:
            assert a == b, ('unchanged other part', i)
    assert after['components'][6]['reference_scope'] == 'UNMAPPED', 'withdraw unsupported resolver'
    assert 'component_id' not in after['components'][6], 'unmapped omits id'
    assert after['component_assertion']['method'] == before['component_assertion']['method'] == 'RECIPE_TRANSCRIPTION'
    assert after['component_assertion']['completeness'] == before['component_assertion']['completeness'] == 'COMPLETE'
    assert after['component_assertion']['evidence'][0] == before['component_assertion']['evidence'][0], 'original recipe evidence'
    for field in ['evidence_type', 'source', 'source_record']:
        assert after['component_assertion']['evidence'][1][field] == before['component_assertion']['evidence'][1][field]
    assert before['component_assertion']['evidence'][1]['notes'] in event['changes'], 'old note retained exactly'
    assert after['notes'].startswith(before['notes']), 'original notes preserved'


def origin_constraints(proposal, case, dependency, old_case, old_proposals, routing):
    assert proposal['kind'] == 'edit_existing_owner', 'authentic existing origin'
    assert proposal['owner_path'] == OWNER, 'exact owner'
    assert proposal['before_sha256'] == BEFORE, 'exact nonnull preimage'
    assert proposal['proposal_id'] == PID and proposal['case_ids'] == [CID]
    assert proposal['source_occurrence_ids'] == [TRIGGER], 'only actual trigger'
    assert proposal['mc_campaign_occurrence_count'] == 0, 'no invented Mc occurrence'
    for key in ['case_id', 'case_input_sha256', 'source', 'occurrence_ids', 'disposition']:
        assert case[key] == old_case[key], ('frozen source', key)
    assert len(case['occurrence_ids']) == 6
    assert case['proposal_ids'] == old_case['proposal_ids'] + [PID], 'prior origins remain'
    assert case['owner_records'] == old_case['owner_records'] + [{'path': OWNER, 'sha256': BEFORE}]
    assert dependency['prior_proposal_ids'] == old_case['proposal_ids']
    assert dependency['all_six_occurrence_ids'] == old_case['occurrence_ids']
    assert dependency['trigger_occurrence'] == TRIGGER
    assert dependency['routing_status'] == 'PENDING_W04_CROSS_OWNER_DECISION', 'routing not approved'
    assert dependency['source_envelope_counts'] == routing['counts'], 'source envelope counts'
    assert dependency['no_role_export_or_owner_approval'] is True
    assert dependency['zero_new_case_or_mc_campaign_occurrence'] is True
    old = {p['proposal_id']: p for p in old_proposals}
    assert old['vm1201-prop-nbrc903-vitamin']['kind'] == 'new_owner'
    assert old['vm1201-prop-nbrc903-vitamin']['before_sha256'] is None
    assert old['vm1237-prop-wolfe-cb-dependent']['before_sha256'] == '709749bd7c83c38a09400fc1893885ead753847ff9d1cbbe4ec76b431d349738'


def negative(name, category, fn):
    try:
        fn()
    except AssertionError as e:
        CONTROLS.append({'name': name, 'category': category, 'rejected': True, 'reason': str(e)})
    else:
        raise AssertionError('negative escaped: ' + name)


def main():
    RUN.mkdir(exist_ok=False)
    started = datetime.now(timezone.utc).isoformat()
    check(command(['git', 'rev-parse', 'HEAD']).decode().strip() == HEAD, 'entry head')
    before_path, candidate_path = O/'beforeimages/Mc_vitamins.yaml', O/'payloads/Mc_vitamins.yaml'
    check(sha(before_path) == sha(R/OWNER) == BEFORE, 'authentic maintained beforeimage')
    check(sha(candidate_path) == AFTER, 'exact selected candidate')
    check(sha(OLD/'selection.json') == 'fb16bf5c29b981dc7dd60cf8d963a9aea25c12a65d6a0e55e29d84dfb2a26699', 'prior selection')
    for ref in read(OLD/'selection.json')['authoritative_inputs'].values():
        capture(ref)
    before, candidate = [yaml.safe_load(p.read_text()) for p in [before_path, candidate_path]]
    payload_constraints(before, candidate)
    proposals = read(OLD/'proposals.json')['proposals']
    check(len(proposals) == len({p['proposal_id'] for p in proposals}) == 114, '114 unique prior proposal objects')
    payload_paths = {p['proposal_id']: capture(p['after_capture']) for p in proposals}
    check(sha(payload_paths['vm1237-prop-wolfe-cb-dependent']) == 'b64eccf46c271520c27c73bc0a5863e2bc56447d1acf7461a90e3d72f9f4384f', 'CB candidate unchanged')
    proposal, case, dep = [read(O/'author'/f'{name}.json') for name in ['proposal','decision','dependency']]
    old_case = next(c for c in read(OLD/'decisions.json')['decisions'] if c['case_id'] == CID)
    routing = read(capture(dep['source_envelope']))
    check(routing['counts'] == {'cases':8,'CM_occurrences':71,'separate_KG_holds':84,'excluded_contexts':6,'nominal_context_upper_bound':65}, 'exact eight-case source envelope')
    check(len(routing['cases']) == 8, 'eight retained case objects')
    cm = [x for x in routing['cases'] if x['case_id'].startswith('CM_NAME:')]
    kg = [x for x in routing['cases'] if x['case_id'].startswith('KG_CASE:')]
    check(sum(len(x['complete_current_decision']['occurrence_ids']) for x in cm) == 71, '71 CM occurrences')
    check(sum(len(x['complete_current_decision']['occurrence_ids']) for x in kg) == 84, '84 separate KG holds')
    origin_constraints(proposal, case, dep, old_case, proposals, routing)
    # Actual full catalog input, including ignored paths, bound to frozen Git tree.
    entries = command(['git','ls-tree','-r','-z',BASE,'--','data/ingredients'])
    tree = {}
    for entry in entries.split(b'\0'):
        if not entry:
            continue
        meta, name = entry.split(b'\t',1)
        mode, kind, oid = meta.decode().split()
        if name.endswith(b'.yaml'):
            assert mode == '100644' and kind == 'blob'
            tree[name.decode()] = oid
    paths = sorted((R/'data/ingredients').rglob('*.yaml'))
    check({str(p.relative_to(R)) for p in paths} == set(tree), 'ignored-inclusive full catalog membership')
    catalog, catalog_hashes = {}, {}
    for path in paths:
        raw = path.read_bytes(); rel = str(path.relative_to(R))
        assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest() == tree[rel], rel
        catalog[rel] = yaml.safe_load(raw); catalog_hashes[rel] = sha(path)
    check(len(catalog) == 2956, '2956 baseline records')
    old_overlay = dict(catalog)
    for p in proposals:
        old_overlay[p['owner_path']] = yaml.safe_load(payload_paths[p['proposal_id']].read_text())
    check(OWNER not in {p['owner_path'] for p in proposals}, 'new dependent owner not already selected')
    overlay = dict(old_overlay); overlay[OWNER] = candidate
    save('catalog-inputs.json', {'baseline':BASE,'sha256_by_path':catalog_hashes,'prior_payloads':{p['proposal_id']:p['after_capture'] for p in proposals},'new_payload':proposal['after_capture']})
    for label, rows in [('baseline',catalog),('prior114',old_overlay),('candidate115',overlay)]:
        errors = [str(x) for x in validate_component_partonomy(rows.values())]
        check(not errors, label+' full-context native partonomy')
    save('overlay.json', {'baseline_records':len(catalog),'previous_selected_payloads':114,'current_selected_payloads':115,'overlay_records':len(overlay),'violations':[], 'owner_admission':'Existing TSB/Bacto FAILED/HELD retained; partonomy is not admission.'})
    print('Full 2956 baseline and prior114/new115 overlay partonomy PASS.',flush=True)
    # Real author function replay, real helper and writer, no monkeypatches.
    author = load_module('mc_author_read_only_replay', O/'provenance/author.py')
    calls = []
    def profiler(frame, event, arg):
        if event == 'call' and frame.f_code is record_curation_event.__code__:
            calls.append({'native':'record_curation_event','curator':frame.f_locals['curator'],'llm_assisted':frame.f_locals['llm_assisted'],'timestamp':frame.f_locals['timestamp']})
        if event == 'call' and frame.f_code is write_validated_ingredient.__code__:
            calls.append({'native':'write_validated_ingredient','path':str(frame.f_locals['path'])})
    sys.setprofile(profiler)
    try:
        rebuilt = author.make_candidate(copy.deepcopy(before),candidate['curation_history'][-1]['timestamp'])
        write_validated_ingredient(rebuilt,RUN/'replayed-candidate.yaml')
    finally:
        sys.setprofile(None)
    check(rebuilt == candidate and sha(RUN/'replayed-candidate.yaml') == AFTER, 'real helper/writer reproduce whole candidate exactly')
    check([c['native'] for c in calls] == ['record_curation_event','write_validated_ingredient'], 'one real helper then one real writer')
    check(calls[0]['llm_assisted'] is True, 'runtime true assistance')
    save('actual-native-call-replay.json',{'calls':calls,'whole_payload_sha256':AFTER,'author_main_executed':False})
    # Positive native writer controls and its scientifically limited baseline.
    write_validated_ingredient(before,RUN/'baseline-native-valid.yaml')
    check(yaml.safe_load((RUN/'baseline-native-valid.yaml').read_text()) == before, 'known stereo-defect baseline passes native schema')
    for name, mutate in [('unknown-component-field', lambda r:r['components'][6].update(unknown_native_field=True)),('bad-scope-enum',lambda r:r['components'][6].update(reference_scope='MIM_CATALOGUE')),('unmapped-retains-id',lambda r:r['components'][6].update(component_id='CHEBI:31345'))]:
        value=copy.deepcopy(candidate);mutate(value);dest=RUN/(name+'.yaml')
        try:
            write_validated_ingredient(value,dest)
        except ValidationFailedError as e:
            check(not dest.exists(), name+' refuses without write')
            CONTROLS.append({'name':name,'category':'ACTUAL_NATIVE_GUARDED_WRITER','rejected':True,'reason':e.summary(),'output_exists':False})
        else:
            raise AssertionError('native guard escaped: '+name)
    for name, code, mutate in [
        ('unmapped-retains-id','UNMAPPED_WITH_ID',lambda r:r['components'][6].update(component_id='CHEBI:31345')),
        ('mapped-without-id','MISSING_COMPONENT_ID',lambda r:r['components'][6].update(reference_scope='MIM_CATALOG')),
        ('missing-quantity-unit','INCOMPLETE_CONCENTRATION',lambda r:r['components'][6].pop('concentration_unit')),
        ('whole-self-reference','SELF_REFERENCE',lambda r:r['components'][6].update(component_id=r['identifier'],reference_scope='MIM_CATALOG',component_name=r['preferred_term']))]:
        changed=copy.deepcopy(candidate);mutate(changed);mutated=dict(overlay);mutated[OWNER]=changed
        errors=validate_component_partonomy(mutated.values())
        check(any(e.code==code and e.record_id==candidate['identifier'] for e in errors), name+' actual native partonomy rejects')
        CONTROLS.append({'name':name,'category':'ACTUAL_NATIVE_PARTONOMY_FULL_OVERLAY','rejected':True,'expected_code':code,'violations':[asdict(e) for e in errors]})
    # Supplemental invariants do not claim to be part of native validation.
    for name, mutate in [
        ('old-history-mutated',lambda r:r['curation_history'][0].update(curator='wrong-author')),
        ('missing-original-history',lambda r:r['curation_history'].pop(0)),
        ('false-new-llm-attribution',lambda r:r['curation_history'][-1].update(llm_assisted=False)),
        ('changed-literal-DL-name',lambda r:r['components'][6].update(component_name='calcium D-pantothenate')),
        ('changed-literal-quantity',lambda r:r['components'][6].update(concentration_value='0.05')),
        ('changed-literal-unit',lambda r:r['components'][6].update(concentration_unit='MG_PER_L')),
        ('added-unsupported-water',lambda r:r['components'].append({'component_name':'water','reference_scope':'UNMAPPED'}))]:
        changed=copy.deepcopy(candidate);mutate(changed)
        negative(name,'SUPPLEMENTAL_REVIEWED_PAYLOAD_INVARIANT',lambda changed=changed:payload_constraints(before,changed))
    for name, target, mutate in [
        ('null-before',0,lambda x:x.update(before_sha256=None)),
        ('stale-before',0,lambda x:x.update(before_sha256='0'*64)),
        ('wrong-owner',0,lambda x:x.update(owner_path='data/ingredients/mapped/Wolfes_Vitamin_Mix.yaml')),
        ('invented-Mc-occurrence',0,lambda x:x.update(mc_campaign_occurrence_count=1)),
        ('wrong-trigger',0,lambda x:x.update(source_occurrence_ids=[old_case['occurrence_ids'][0]])),
        ('changed-case-source',1,lambda x:x['source'].update(raw_source_label='Mc_vitamins')),
        ('lost-case-occurrence',1,lambda x:x['occurrence_ids'].pop()),
        ('changed-frozen-case-digest',1,lambda x:x.update(case_input_sha256='0'*64)),
        ('lost-prior-origin',1,lambda x:x['proposal_ids'].pop(0)),
        ('premature-W04-routing',2,lambda x:x.update(routing_status='APPROVED')),
        ('lost-exclusion',2,lambda x:x['source_envelope_counts'].update(excluded_contexts=5)),
        ('released-role-export-hold',2,lambda x:x.update(no_role_export_or_owner_approval=False))]:
        changed=copy.deepcopy([proposal,case,dep]);mutate(changed[target])
        negative(name,'SUPPLEMENTAL_ORIGIN_SOURCE_INVARIANT',lambda changed=changed:origin_constraints(*changed,old_case,proposals,routing))
    save('controls.json',{'controls':CONTROLS,'count':len(CONTROLS),'native_semantic_limit':'Known literal DL/D mismatch passes native schema and catalog name resolution; separate scientific review is mandatory.'})
    print('Actual native controls and supplemental negative controls PASS.',flush=True)
    # In-memory actual Claw producer projection using complete owner indices.
    entrypoint=CLAW/'scripts/build_mim_ingredient_sssom.py'
    builder=load_module('mc_actual_claw_producer',entrypoint)
    builder._check_producer_bindings()
    producer_bytes={str(p):hashlib.sha256(raw).hexdigest() for p,raw in builder._IMPORTED_PRODUCER_BYTES.items()}
    check(producer_bytes[str(entrypoint)]==sha(entrypoint),'actual producer source binding')
    check(command(['git','-C',str(CLAW),'rev-parse','HEAD']).decode().strip()=='76c1ebeea3fc7f80bf1abe044688f298f390cfac','actual Claw snapshot head')
    projections={}
    for label, rows, rec, path in [('before',old_overlay,before,before_path),('after',overlay,candidate,candidate_path)]:
        subjects={builder._mim_curie(Path(owner).name):record for owner,record in rows.items()}
        check(len(subjects)==len(rows),'all overlay subjects distinct '+label)
        owners=builder.build_owner_index(subjects);suppressions=[]
        projection=builder._row_from_yaml(path,{},{},{},{},record=rec,owners=owners,suppressions=suppressions)
        projections[label]={'rows':projection,'suppressions':[asdict(s) for s in suppressions]}
    check(projections['before']==projections['after'],'actual old/new Mc SSSOM rows and suppressions unchanged')
    check(bool(projections['after']['rows']),'nonempty actual Mc producer rows')
    builder._check_producer_bindings()
    native=load_module('mc_actual_sssom_invariants',R/'scripts/validate_sssom_invariants.py')
    fixture=RUN/'identity-fixture';fixture.mkdir();(fixture/'Mc_vitamins.yaml').write_bytes(candidate_path.read_bytes())
    native.INGREDIENTS_DIR=fixture;native._subject_to_path.cache_clear()
    projected=projections['after']['rows']
    failures={name:list(getattr(native,'evaluate_rule_'+name)(projected)) for name in ['b1','b2','b3','b5','d']}
    check(not any(failures.values()),'actual Mc projection native identity obligations')
    wrong=[dict(row,predicate_id='skos:closeMatch') for row in projected if row['object_id']==candidate['identifier']]
    rejections=list(native.evaluate_rule_d(wrong))
    check(len(wrong)==len(rejections)>0,'actual Rule D rejects degraded Mc own-identity row')
    save('actual-SSSOM-projection.json',{'projections':projections,'native_failures':failures,'Rule_D_negative_inputs':wrong,'Rule_D_negative_rejections':rejections,'producer_input_hashes':producer_bytes,'scope':'Actual in-memory YAML producer projection only, empty optional enrichments, full owner context. No maintained SSSOM file emitted or full published SSSOM suite run.'})
    check(command(['git','rev-parse','HEAD']).decode().strip()==HEAD,'exit head unchanged')
    check(sha(before_path)==sha(R/OWNER)==BEFORE and sha(candidate_path)==AFTER,'before/candidate preserved')
    check(all(sha(R/path)==digest for path,digest in catalog_hashes.items()),'whole maintained catalog exact after controls')
    check(all(sha(payload_paths[p['proposal_id']])==p['after_capture']['sha256'] for p in proposals),'all prior 114 candidate bytes preserved')
    save('receipt.json',{'status':'PASS_TECHNICAL_ONLY','started_at':started,'completed_at':datetime.now(timezone.utc).isoformat(),'reviewer':'worker08:/root/inorganics','author':'worker08:/root','payload_sha256':AFTER,'before_sha256':BEFORE,'baseline_records':len(catalog),'selected_prior_payloads':114,'selected_overlay_payloads':115,'full_overlay_records':len(overlay),'checks':CHECKS,'controls_count':len(CONTROLS),'commands':COMMANDS,'actual_native_helper_writer_replay':True,'known_D_vs_DL_defect_passes_native_checks':True,'actual_Mc_SSSOM_projection_unchanged':True,'all_maintained_and_prior_payload_bytes_preserved':True,'owner_admission':'TSB/Bacto FAILED/HELD retained; not re-admitted','scientific_approval':False,'final_selection_review':'Pending actual final selection and science/lineage receipts.','inputs':{str(p.relative_to(R)):sha(p) for p in [Path(__file__),candidate_path,before_path,O/'provenance/author.py',O/'author/proposal.json',O/'author/decision.json',O/'author/dependency.json',OLD/'selection.json',OLD/'proposals.json',OLD/'decisions.json',R/'MAPPING_SEMANTICS.md',R/'src/mediaingredientmech/validation/write_validated.py',R/'src/mediaingredientmech/validation/component_partonomy.py',R/'src/mediaingredientmech/curate/curation_event.py',R/'scripts/validate_sssom_invariants.py']}})
    print('PASS technical controls, whole Mc replay, original 114 preserved, old/new projection identical.',flush=True)


if __name__=='__main__':
    try:
        main()
    except BaseException as e:
        if RUN.exists():
            save('failure.json',{'type':type(e).__name__,'message':str(e),'traceback':traceback.format_exc(),'commands':COMMANDS,'completed_checks':CHECKS,'completed_controls':CONTROLS})
        raise
