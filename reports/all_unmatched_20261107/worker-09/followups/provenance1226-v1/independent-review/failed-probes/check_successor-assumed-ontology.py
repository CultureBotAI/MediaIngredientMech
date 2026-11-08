"""Independent successor assessment; never imports the author's mutation helper."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json,hashlib,copy,re,datetime,difflib
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
R=ROOT/'reports/all_unmatched_20261107/worker-09/followups/provenance1226-v1'
sys.path.insert(0,str(ROOT/'src'))
import yaml
from mediaingredientmech.validation.write_validated import validate_ingredient
from mediaingredientmech.synonym_policy import is_resolving_synonym
from mediaingredientmech.sssom_grading import predicate_for,confidence_for,justification_for
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
canon=lambda v:hashlib.sha256(json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
read=lambda p:json.loads(p.read_text())
def save(n,v):
    with (OUT/n).open('x') as f:json.dump(v,f,ensure_ascii=False,indent=2);f.write('\n')

base=read(OUT/'baseline-inspection.json');before_by={r['proposal_id']:r for r in base['records']}
notes=read(OUT/'claim-context-notes.json')['notes']
allow={r['proposal_id']:r for r in read(R/'inputs/w09-eight-entry-allowlist.json')['rows']}
selection=read(R/'selection.json');selected=selection['selected']
originals=read(R/'predecessor-cores/proposals.json')['proposals']
proposals=read(R/'proposals.json')['proposals']
assert len(selected)==len(proposals)==len(originals)==32
assert len({r['proposal_id'] for r in selected})==32
assert {r['proposal_id'] for r in selected}=={r['entry_id'].split('::',1)[1] for r in base['selection']}
assert len({r['proposal_id'] for r in proposals})==32
old_proposals={r['proposal_id']:r for r in originals};new_proposals={r['proposal_id']:r for r in proposals}
old_selection={r['entry_id'].split('::',1)[1]:r for r in base['selection']}
payload_checks=[];diffs=[];schema_checks=[];component_changes=[]
for selected_row in selected:
    pid=selected_row['proposal_id'];path=ROOT/selected_row['selected_path'];before_path=R/'predecessors'/f'{pid}.yaml'
    assert sha(before_path)==selected_row['before_sha256']==old_selection[pid]['sha256']
    assert sha(path)==selected_row['selected_sha256']
    before=yaml.safe_load(before_path.read_text());after=yaml.safe_load(path.read_text())
    changed=pid in allow
    assert selected_row['changed']==changed
    assert selected_row['release_approval'] is False
    oldp=old_proposals[pid];newp=new_proposals[pid]
    assert canon(oldp)==selected_row['original_proposal_sha256'] and canon(newp)==selected_row['selected_proposal_sha256']
    restored_proposal=copy.deepcopy(newp);restored_proposal['after_capture']=oldp['after_capture']
    assert restored_proposal==oldp
    cap=newp['after_capture'];assert cap['root']=='artifact'
    captured=ROOT/'reports/all_unmatched_20261107/worker-09'/cap['path']
    assert captured.resolve()==path.resolve() and sha(captured)==cap['sha256']
    if changed:
        row=allow[pid];previous=before_by[pid]
        assert before==previous['full_record'] and sha(before_path)==row['payload_sha256']
        idx=int(re.fullmatch(r'ontology_mapping\.evidence\[(\d+)\]',row['field']).group(1))
        original_object=before['ontology_mapping']['evidence'][idx]
        assert original_object==row['full_value'] and canon(original_object)==row['full_value_sha256']
        changed_object=after['ontology_mapping']['evidence'][idx]
        expected_object=copy.deepcopy(original_object);expected_object['evidence_type']='LLM_SUGGESTION'
        assert changed_object==expected_object
        assert after['curation_history'][:-1]==before['curation_history']
        assert len(after['curation_history'])==len(before['curation_history'])+1
        event=after['curation_history'][-1]
        assert event['llm_assisted'] is True and event['curator']=='Codex worker09'
        assert event['action']=='CORRECTED_MAPPING_EVIDENCE_ATTRIBUTION'
        assert event['previous_status']==event['new_status']==before['mapping_status']
        assert datetime.datetime.fromisoformat(event['timestamp']).tzinfo is not None
        for literal in ['#1226',pid,row['field']+'.evidence_type','MANUAL_CURATION','LLM_SUGGESTION',row['full_value_sha256'],'No identity, source applicability, outcome, role, coalescence or export approval change']:
            assert literal in event['changes'],(pid,literal)
        restored=copy.deepcopy(after);restored['ontology_mapping']['evidence'][idx]=original_object;restored['curation_history'].pop()
        assert restored==before, 'Non-allowlisted complete-record difference'
        # Exact top-level and complete nested mapping checks do not rely on author's proof.
        fieldproof={k:{'before_sha256':canon(v),'after_sha256':canon(after[k]),'equal':v==after[k]} for k,v in before.items()}
        assert set(after)==set(before)
        assert {k for k,v in fieldproof.items() if not v['equal']}=={'ontology_mapping','curation_history'}
        if pid=='ma-casamino-distinct':
            assert canon(after['ontology_mapping']['evidence'][1])=='172fc3c050e5737dfc774001fa18e3263d7c33242119f5a00aec64fc2fd915c9'
            assert after['ontology_mapping']['evidence'][1]==base['exception']['full_value']
        errors=validate_ingredient(after);assert not errors, str(errors)
        schema_checks.append({'proposal_id':pid,'errors':[]})
        reason=notes[pid]
        details={'field':row['field']+'.evidence_type','before_full_object_sha256':canon(original_object),
                 'after_full_object_sha256':canon(changed_object),'old_mapping_sha256':canon(before['ontology_mapping']),
                 'new_mapping_sha256':canon(after['ontology_mapping']),'history_prefix_sha256':canon(before['curation_history']),
                 'event':event,'all_top_level_field_checks':fieldproof,'full_candidate':after,
                 'reconstructed_predecessor_equal':True,'assessment':reason}
        diffs.append(''.join(difflib.unified_diff(before_path.read_text().splitlines(True),path.read_text().splitlines(True),fromfile=str(before_path),tofile=str(path))))
    else:
        assert before_path.read_bytes()==path.read_bytes() and oldp==newp
        details={'assessment':{'typing_reason':'This selected payload is outside the eight-entry repair allowlist. Exact raw-byte equality and unchanged proposal object are independently verified; no inherited approval is renewed.','full_record_context':'No candidate change; original source assessment and owner context remain as published.','approval_limit':'Preservation review only. Chemistry, aliases, roles and export approval are not reassessed.'},'byte_identical':True}
    assert before.get('components')==after.get('components') and before.get('component_assertion')==after.get('component_assertion')
    # Directly replay the native synonym and mapping-grade functions, independently of author wrapper.
    for record in [before,after]:
        m=record['ontology_mapping'];q=m['mapping_quality']
        projection={'identity':record['identifier'],'preferred':record['preferred_term'],'mapping':{k:v for k,v in m.items() if k!='evidence'},
                    'quality_predicate':predicate_for(q),'quality_confidence':confidence_for(q),'quality_justification':justification_for(q),
                    'resolving_synonyms':[(s,is_resolving_synonym(s)) for s in record.get('synonyms',[])]}
        if record is before:first_projection=projection
        else:assert projection==first_projection
    payload_checks.append({'proposal_id':pid,'reviewer':'Codex /root/provenance1226_reviewer','changed':changed,
                           'before_path':str(before_path.relative_to(ROOT)),'selected_path':str(path.relative_to(ROOT)),
                           'before_sha256':sha(before_path),'after_sha256':sha(path),'verdict':'supported_provenance_correction_with_limits' if changed else 'byte_identical_retention_only',
                           'details':details,'native_projection_unchanged':True,'scientific_review':False})
assert sum(r['changed'] for r in payload_checks)==8
assert len(list((R/'candidates').glob('*.yaml')))==8
decisions=read(R/'effective-decisions.json')['decisions']
assert sha(R/'effective-decisions.json')==base['effective_decisions_sha256']
assert [{'case_id':r['case_id'],'full_row_sha256':canon(r)} for r in decisions]==base['case_bindings']
frozen=read(R/'inputs/frozen-shard-09.json')['cases'];frozen_by={r['case_id']:r for r in frozen}
assert len(frozen)==len(frozen_by)==len(decisions)==187
case_checks=[]
for i,r in enumerate(decisions):
    assert canon(frozen_by[r['case_id']])==r['case_input_sha256']
    assert set(r['proposal_ids']) <= set(old_proposals)
    case_checks.append({'case_id':r['case_id'],'index':i,'reviewer':'Codex /root/provenance1226_reviewer',
                        'full_effective_row_sha256':canon(r),'case_input_sha256':r['case_input_sha256'],
                        'verdict':'exact_effective_outcome_retained','source':r['source'],'disposition':r['disposition'],
                        'occurrence_ids':r['occurrence_ids'],'proposal_ids':r['proposal_ids'],
                        'reason':'Complete current effective outcome object equals its independently bound77d6beae predecessor. Raw names, source kinds, occurrences, evidence references, holds and outcome are unchanged. This review does not reassess scientific support or release a hold.',
                        'scientific_review':False})
assert len({r['case_id'] for r in case_checks})==187
controls=read(R/'validation/controls.json')
assert controls['status']=='PASS' and controls['test_count']==27 and all(r['status']=='PASS' for r in controls['tests'])
save('successor-assessments.json',{'reviewer':'Codex /root/provenance1226_reviewer','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'status':'PASS','verdict':'pass_with_limitations','scientific_review':False,'source_head':base['head'],
 'changed_payloads':8,'retained_payloads':24,'case_count':187,'payloads':payload_checks,'cases':case_checks,
 'schema_checks':schema_checks,'author_controls_independently_read':{'script_sha256':sha(R/'tools/test_controls.py'),'result_sha256':sha(R/'validation/controls.json'),'tests':[{'name':r['name'],'status':r['status']} for r in controls['tests']],
 'assessment':'All requested positive and negative classes have meaningful assertions; exact exception and component/science mutation refusals are exercised. Path reservation refuses pre-existing/symlink/hardlink/outside/.. outputs and preserves sentinels. No hostile-concurrency or atomic eight-file transaction is claimed.'},
 'writer_assessment':{'path':str((R/'tools/correct_provenance.py').relative_to(ROOT)),'sha256':sha(R/'tools/correct_provenance.py'),
 'reason':'Native schema gate and native event helper are used. Complete pinned allowlist+raw payload hashes bind full object and mapping context. Restoring the single enum and removing the appended event must reproduce the complete predecessor. Reserved descriptor wrapper adds exclusive/no-follow/no-alias checks to the native writer; native writer alone is not claimed exclusive.'},
 'new_findings':[],'limits':['Provenance-only review: no literature/chemical identity/source applicability reassessment or whole-owner/role/export approval.',
 'Historical Casamino evidence[1] remains ambiguous and unchanged. ComponentEvidenceTypeEnum fields are untouched.',
 'Two exact hexahydrate source-assessment supersessions remain preserved; no reversion to original earlier decisions and no new routing/hold release.']})
with (OUT/'full-candidate-diffs.txt').open('x') as f:f.write('\n'.join(diffs))
print(json.dumps({'status':'PASS','changed_payloads':8,'retained_payloads':24,'cases':len(case_checks),'new_findings':0}))
