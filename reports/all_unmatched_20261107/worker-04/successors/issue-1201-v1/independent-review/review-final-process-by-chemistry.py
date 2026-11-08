"""Independent final byte binding after full code and native-content review."""
import datetime,hashlib,json,sys
from pathlib import Path
import yaml
R=Path.cwd();W=R/'reports/all_unmatched_20261107/worker-04';S=W/'successors/issue-1201-v1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
binding=load(S/'validation/input-bindings.json')
for row in binding['files']+binding['gate_outputs']:
    assert sha(Path(row['path']))==row['sha256'],row['path']
commands=load(S/'validation/command-receipts.json')
assert set(commands)=={'predecessor','structural','schema','overlay','guarded_writer','auditor_controls'}
for name,row in commands.items():
    assert row['exit_code']==0 and row['input_binding_sha256']==sha(S/'validation/input-bindings.json'),name
    assert sha(S/row['log'])==row['log_sha256']
control_path=S/'independent-review/process-negative-controls-results.json'
controls=load(control_path)
assert controls['status']=='PASS' and len(controls['controls'])==23
for x in controls['controls']:assert x['status']=='PASS'
for path,h in controls['production_script_hashes'].items():assert sha(S/path)==h,path
native_commands=load(S/'validation/native-command-receipts.json')
assert len(native_commands)>=3,'Native inspect, save and validation receipts required'
for name,row in native_commands.items():
    assert row['exit_code']==0,name
    for stream in ['stdout','stderr']:
        assert sha(S/row[stream])==row[stream+'_sha256'],(name,stream)
saved=load(S/'validation/native-save.json');review_path=Path(saved['review'])
if not review_path.is_absolute():review_path=R/review_path
native=yaml.safe_load(review_path.read_text());content=load(S/'native-review-content.json')
assert native==content,'Saved native payload differs from inspected source content'
assert native['completion']=='completed' and native['verdict']=='needs_curation' and native['scientific_review'] is True
assert native['findings']==[] and any('not retired' in text for text in native['limitations'])
assert 'does not retire' in json.dumps(native['related_reviews']).lower()
inspection=load(S/'validation/native-inspection.json')
assert native['targets']==inspection['targets'] and native['source']==inspection['source']
for x in native['source']['inputs']:assert sha(R/x['path'])==x['sha256'],x['path']
prior=load(W/'decisions.json')['decisions'];decisions=load(S/'decisions.json')['decisions']
old={x['case_id']:x for x in prior};current={x['case_id']:x for x in decisions}
assert len(decisions)==188 and list(old)==list(current)
assembly=load(S/'validation/assembly-bindings.json');reassess=load(S/'reassessments.json')['reassessments'];reby={x['case_id']:x for x in reassess}
assert len(reassess)==len(reby)==108
assert set(reby)=={x['case_id'] for x in prior if not x['proposal_ids']}
selected=set(reby)|set(assembly['changed_cases']);assert len(selected)==112
assert set(native['scope']['reviewed_target_ids'])==selected=={t['target_id'] for t in native['targets']}
assert native['scope']['population_size']==112
assert {a['target_ids'][0] for a in native['assessments']}==selected and len(native['assessments'])==112
for d in decisions:
    for k in ['case_id','case_input_sha256','source','occurrence_ids']:
        assert d[k]==old[d['case_id']][k],(d['case_id'],k)
    for k,v in old[d['case_id']].items():
        if 'hold' in k:assert d.get(k)==v,(d['case_id'],k)
    if d['case_id'] not in assembly['changed_cases']:assert d==old[d['case_id']]
    if not d['proposal_ids']:assert d.get('no_change_reason')
for a in native['assessments']:
    cid=a['target_ids'][0]
    if cid in reby:assert json.dumps(reby[cid],ensure_ascii=False) in a['details']
    else:assert 'not a new claim to rerun the entire original scientific review' in a['details']
proposals=load(S/'proposals.json')['proposals'];assert len(proposals)==115 and len({p['owner_path'] for p in proposals})==115
for p in proposals:assert sha(W/p['after_capture']['path'])==p['after_capture']['sha256']
overlay=load(S/'validation/proposal-overlay.json')
assert overlay['status']=='PASS' and not overlay['errors'] and not overlay['partonomy']['introduced_violations']
assert not overlay['maintained_writes'] and not overlay['maintained_diff_from_frozen_base'] and not overlay['untracked_maintained_inputs']
assert len(overlay['identity_checks'])==115
assert any(x.get('inherited_mapping_quality_preserved_not_approved') for x in overlay['ontology_labels'] if x['owner_path'].endswith('/Actinomycetin.yaml'))
audit_path=S/commands['structural']['result_path']
assert sha(audit_path)==commands['structural']['result_sha256']
assert str(audit_path)==commands['structural']['command'][commands['structural']['command'].index('--output')+1]
audit=load(audit_path)
assert audit['structural_accounting']=='PASS' and audit['accounted_case_count']==188 and audit['scientific_adequacy_or_approval_established'] is False
for e in native['evidence']:
    if 'NOT a new remote retrieval' in e['locator']:assert e['reference'].startswith(('reports/','frozen-queue:'))
    if e['kind']=='search':assert e['support']=='context_only'
predecessor_review=R/'reviews/structured/20261108T053803Z-worker04-all-unmatched-source-review/review.yaml'
assert len(yaml.safe_load(predecessor_review.read_text())['findings'])==4
bind=[S/x for x in ['decisions.json','evidence.json','proposals.json','reassessments.json','validation/assembly-bindings.json','validation/input-bindings.json','validation/command-receipts.json','validation/proposal-overlay.json','cross-shard-dependencies.json','independent-review/review-selection.json','validation/native-command-receipts.json','validation/native-inspection.json','validation/native-save.json','native-review-content.json']]
bind += [review_path,review_path.with_name('review.md'),predecessor_review,audit_path,control_path]
receipt={'status':'complete','scientific_disposition':'accepted_narrow_scope','process_disposition':'accepted_final_bound_source_proposal_bundle','reviewer':'worker04/chemistry; independent of root assembly and native-process author','reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Code review of all root combination/native helper scripts and final exact assembled source/proposal outputs; this is not an independent re-review of all predecessor substance science or an authorization for maintained integration/export.','reviewed_scripts':{str(p.relative_to(S)):sha(p) for p in sorted((S/'scripts').glob('*.py'))},'reviewed_outputs':{str(p.relative_to(R)):sha(p) for p in bind},'actual_checks':{'bound_input_and_output_files_verified':len(binding['files'])+len(binding['gate_outputs']),'actual_gate_commands_passed':list(commands),'independent_synthetic_controls':23,'whole_shard_mechanically_accounted':188,'successor_reassessments':108,'additional_shared_payload_binding_cases':4,'native_scientific_target_count':112,'active_payloads':115,'source_occurrence_and_hold_fields_preserved':True,'unmodified_predecessor_decisions_byte_equivalent_as_json':True,'prior_native_findings_preserved':4,'native_saved_content_matches_reviewed_json':True},'review_notes':['All exact accepted reviewer bindings and new payloads are enforced before assembly; 108 originally unproposed cases and four shared-payload bindings delimit the successor scientific scope. Other predecessor assessments remain unchanged.','Destination guards reject duplicate, already occupied and unsafe paths; semantic overlay deliberately retains original owner keys and does not perform filesystem moves. Independent negative controls cover these cases.','Inherited Actinomycetin PLACEHOLDER mapping is accepted only as an unchanged tuple and explicitly remains outside approval; new or modified non-FALLBACK_REGISTRY registry mappings fail.','Actual full-catalog overlay has zero introduced partonomy/identity/destination/label errors and no maintained-input changes. Corrected FeNaEDTA alias and hydrate label fields have separate skeptical receipts.','Native review is needs_curation and preserves the four predecessor findings. No complete-owner, role, source-selector, export or other-shard approval is implied.','Native evidence retains original remote timestamps where recorded; otherwise it explicitly identifies local artifact inspection. Failed retrievals remain context-only search evidence.','All six final gate receipts, source/target inspection, saved native content, validation receipts and input/output/log hashes were checked; synthetic controls are separately identified and are not substitutes for those actual gate executions.'],'findings':[{'finding_id':'PROCESS-CHEM-01','status':'resolved','resolution':'Final overlay validates integration destinations and explicit semantic-overlay limits; destination positive/negative controls pass.'},{'finding_id':'PROCESS-CHEM-02','status':'resolved','resolution':'Media final v4 receipt provides exact full-payload review bindings and corrected evidence classification.'}],'remaining_limitations':['Coordinator must reconcile nine same-owner dependencies and eighteen candidate source-context overlaps against actual other-worker proposals; this review does not select a winner.','Isolated payload acceptance does not certify inherited owner fields, unresolved source-form facts or future publication.','No merge, downstream build, maintained data write, commit or push was performed by this reviewer.']}
if '--check-only' in sys.argv:
    print(json.dumps({'status':'PASS','acceptance_receipt_written':False,'native_review':str(review_path.relative_to(R)),'checks':receipt['actual_checks']},indent=2));sys.exit(0)
out=S/'independent-review/process-reviewed-by-chemistry-v2.json';assert not out.exists();out.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'path':str(out.relative_to(S)),'sha256':sha(out),'native_review':str(review_path.relative_to(R)),'status':'complete'},indent=2))
