"""Independent read-only verification of root type planning and review routing."""
from pathlib import Path
from copy import deepcopy
from collections import Counter
from datetime import datetime,timezone
import json,hashlib,sys,yaml
W=Path(__file__).resolve().parents[3];A=W/'reports/all_unmatched_20261107/worker-02';R=A/'final-corrections-v1';T=R/'chemistry/technical-review'
sys.path.insert(0,str(W/'src'))
from mediaingredientmech.curate.publication_guard import FrozenFile
held={}
def readbytes(p):
    p=p.absolute()
    if p not in held:held[p]=FrozenFile.capture(p)
    return held[p].content
def sha(p):return hashlib.sha256(readbytes(p)).hexdigest()
def J(p):return json.loads(readbytes(p))
def Y(p):return yaml.safe_load(readbytes(p))
def canonical(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode()).hexdigest()
def unique(rows,key):
    assert len({x[key] for x in rows})==len(rows),(key,'duplicates')
    return {x[key]:x for x in rows}
def payload(c):
    assert c['root']=='artifact';p=A/c['path'];assert sha(p)==c['sha256'],str(p);return Y(p)
def pointer(d,p):
    for x in p.lstrip('/').split('/'):
        x=x.replace('~1','/').replace('~0','~');d=d[int(x)] if isinstance(d,list) else d[x]
    return d
def save(name,v):
    p=T/name;assert not p.exists();p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n');return {'path':str(p.relative_to(W)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
intake=unique(J(C/'preflight/final-intake-candidate-v1/all-active-proposal-entries-v1.json')['entries'],'entry_id')
matrix=J(R/'original-58-claim-type-matrix.json');plan=J(R/'type-plan-v1.json');receipt=J(R/'typed-v1/type-correction-receipt.json');routing=J(R/'review-selection-v1/review-routing.json')
oldD=unique(J(A/'continuation-1201-v1/decisions.json')['decisions'],'case_id');oldP=unique(J(A/'continuation-1201-v1/proposals.json')['proposals'],'proposal_id')
preD=unique(J(R/'pretype-v2/decisions.json')['decisions'],'case_id');preP=unique(J(R/'pretype-v2/proposals.json')['proposals'],'proposal_id');preE=J(R/'pretype-v2/evidence.json')['evidence']
typedP=unique(J(R/'typed-v1/proposals.json')['proposals'],'proposal_id');revD=unique(J(R/'review-selection-v1/decisions.json')['decisions'],'case_id');revP=unique(J(R/'review-selection-v1/proposals.json')['proposals'],'proposal_id');revE=J(R/'review-selection-v1/evidence.json')['evidence']
frozen=unique(J(A/'context/frozen-shard-02.json')['cases'],'case_id');com=J(R/'pretype-v2/composition.json');chem=J(R/'chemistry/mapping-evidence-lineage.json')['entries'];prep=J(R/'preparations/mapping-evidence-lineage.json')
assert plan['pretype_proposals_sha256']==sha(R/'pretype-v2/proposals.json')==receipt['pretype_proposals_sha256']
assert plan['original_matrix_sha256']==sha(R/'original-58-claim-type-matrix.json')
assert receipt['plan_sha256']==sha(R/'type-plan-v1.json')
assert receipt['original_flag_dispositions']==plan['original_flag_dispositions']
flags=[i for d in plan['original_flag_dispositions'] for i in d['original_flag_indices']];assert sorted(flags)==list(range(58))
M={e['original_flag_index']:e for e in matrix['entries']};assert set(M)==set(range(58))
edit_map={};claim_rows=[]
for d in plan['original_flag_dispositions']:
    assert len(d['original_flag_indices'])==1;i=d['original_flag_indices'][0];m=M[i];flag=m['exact_original_flag'];original=payload(flag['after_capture']);entry=pointer(original,flag['pointer'])
    assert entry==flag['entry']==d['original_complete_entry'];assert canonical(entry)==d['original_entry_sha256']==m['provenance_audit_row']['full_value_sha256']
    assert m['provenance_audit_row']['classification']=='new_agent_record' and m['provenance_audit_row']['scientific_mapping_approval'] is False
    oldp=oldP[flag['proposal_id']];assert oldp['after_capture']==flag['after_capture'];assert canonical(intake['w02::'+flag['proposal_id']])==m['provenance_audit_row']['proposal_entry_sha256'];assert intake['w02::'+flag['proposal_id']]['proposal_ledger_sha256']==sha(A/'continuation-1201-v1/proposals.json')
    if oldp['kind']=='edit_existing_owner':
        baseline_path=W/oldp['owner_path'];assert sha(baseline_path)==oldp['before_sha256'];baseline=Y(baseline_path)
        assert entry not in baseline.get('ontology_mapping',{}).get('evidence',[]),'historical exact human value was flagged'
    else:baseline=None
    pid=d['successor_proposal_id'];p=preP[pid];before=payload(p['after_capture']);expected=pointer(before,d['successor_pointer']);assert expected==d['successor_complete_entry'];assert canonical(expected)==d['successor_entry_sha256'];assert expected['evidence_type']=='MANUAL_CURATION'
    lineage=d['authored_lineage']
    if lineage is None:assert expected==entry
    elif 'old_proposal_id' in lineage:
        assert lineage in prep and lineage['old_proposal_id']==flag['proposal_id'] and lineage['old_fullvalue']==entry and lineage['successor_fullvalue']==expected and lineage['successor_proposal_id']==pid
    else:
        assert lineage in chem and lineage['proposal_id']==pid and lineage['predecessor_full_value']==entry and lineage['successor_full_value']==expected
    key=(pid,int(d['successor_pointer'].rsplit('/',1)[1]));assert key not in edit_map;edit_map[key]=i
    claim_rows.append({'original_flag_index':i,'original_proposal_id':flag['proposal_id'],'original_payload':flag['after_capture'],'original_pointer':flag['pointer'],'original_full_value':entry,'canonical_sha256':canonical(entry),'successor_proposal_id':pid,'successor_pretype_capture':p['after_capture'],'successor_pointer':d['successor_pointer'],'successor_full_value':expected,'baseline_exact_human_object_excluded':True,'explicit_lineage_verified':lineage is not None,'classification_scope':'Technical binding to prior independently audited provenance row; not new scientific/source approval.'})
assert len(edit_map)==58
candidate_rows=unique(plan['candidate_edits'],'proposal_id');type_rows=unique(receipt['changed_candidates'],'proposal_id');assert candidate_rows.keys()==type_rows.keys() and len(type_rows)==51
typed_flags=[];type_proofs=[]
assert preP.keys()==typedP.keys()==revP.keys() and len(revP)==117
for pid,p in preP.items():
    before=payload(p['after_capture']);after=payload(typedP[pid]['after_capture'])
    meta=deepcopy(p);meta['after_capture']=typedP[pid]['after_capture'];assert meta==typedP[pid]
    if pid not in type_rows:assert before==after and p==typedP[pid];continue
    c=candidate_rows[pid];t=type_rows[pid];assert c['pretype_capture']==p['after_capture']==t['before_scientific_capture'];assert t['after_capture']==typedP[pid]['after_capture']
    expected=deepcopy(before);seen=set()
    for edit in c['edits']:
        idx=edit['evidence_index'];assert type(idx) is int and idx not in seen;seen.add(idx);assert edit['expected_complete_entry']==before['ontology_mapping']['evidence'][idx]
        assert edit['classification']=='new_agent_record' and edit['new_type']=='LLM_SUGGESTION'
        flag=edit_map[(pid,idx)];assert edit['original_flag_indices']==[flag];typed_flags.append(flag)
        if p['kind']=='edit_existing_owner':
            assert sha(W/p['owner_path'])==p['before_sha256'];assert edit['expected_complete_entry'] not in Y(W/p['owner_path']).get('ontology_mapping',{}).get('evidence',[])
        expected['ontology_mapping']['evidence'][idx]['evidence_type']='LLM_SUGGESTION'
        proof=next(x for x in t['entries'] if x['evidence_index']==idx)
        assert proof['before']==before['ontology_mapping']['evidence'][idx] and proof['after']==expected['ontology_mapping']['evidence'][idx] and proof['original_flag_indices']==[flag]
    assert len(after['curation_history'])==len(before.get('curation_history',[]))+1
    assert after['curation_history'][:-1]==before.get('curation_history',[])
    event=after['curation_history'][-1];assert event['curator']=='worker02 /root' and event['llm_assisted'] is True and event['action']=='CORRECTED'
    expected['curation_history'].append(event);assert expected==after,'Non-type field changed'
    for field in ['components','component_assertion','nutritional_roles','biological_roles','physical_roles']:assert before.get(field)==after.get(field)
    type_proofs.append({'proposal_id':pid,'before_capture':p['after_capture'],'after_capture':typedP[pid]['after_capture'],'type_indices':sorted(seen),'type_edit_count':len(seen),'other_content_exactly_equal_except_one_truthful_history_event':True,'new_event':event})
assert sorted(typed_flags)==list(range(58))
eid='w02-final-58-claim-specific-type-correction';erows=unique(revE,'evidence_id');assert revE[:-1]==preE and revE[-1]['evidence_id']==eid and revE[-1]['kind']=='local_validation';assert revE[-1]['capture']['sha256']==sha(R/'typed-v1/type-correction-receipt.json');assert routing['independent_approval_established'] is False and receipt['independent_scientific_or_provenance_approval'] is False
changed=set();payload_routes=unique(routing['payloads'],'proposal_id');assert payload_routes.keys()==revP.keys()
for pid,p in revP.items():
    expect=deepcopy(typedP[pid])
    if pid in type_rows:expect['evidence_ids'].append(eid)
    assert p==expect
    old=oldP.get(pid);byte_changed=old is None or old['after_capture']['sha256']!=p['after_capture']['sha256'];cap_changed=old is None or old['after_capture']!=p['after_capture'];assert byte_changed==cap_changed
    route=payload_routes[pid];assert route['complete_payload_changed']==byte_changed and route['after_capture']==p['after_capture'] and route['old_selected_proposal']==old
    if byte_changed:changed.add(pid);assert route['required_review']=='pending'
    else:assert route['required_review']=='exact_historical_binding'
assert len(changed)==74
case_routes=unique(routing['cases'],'case_id');assert frozen.keys()==oldD.keys()==preD.keys()==revD.keys()==case_routes.keys() and len(revD)==188
affected=[];caseproofs=[]
for cid,d in revD.items():
    old=oldD[cid];pre=preD[cid];case=frozen[cid];assert d['case_input_sha256']==old['case_input_sha256']==canonical(case)
    assert d['source']=={k:case[k] for k in ['source','source_case_id','source_label','raw_source_label']};assert d['occurrence_ids']==[x['occurrence_id'] for x in case.get('occurrences',[])]
    assert all(d[k]==old[k]==pre[k] for k in ['case_id','case_input_sha256','source','occurrence_ids'])
    expected=deepcopy(pre);need=bool(changed.intersection(pre['proposal_ids'])) or pre!=old
    if type_rows.keys() & set(pre['proposal_ids']):
        if eid not in expected['evidence_ids']:expected['evidence_ids'].append(eid)
    if need:expected['independent_review']={'status':'pending','evidence_ids':[]};affected.append(cid)
    assert d==expected
    route=case_routes[cid];assert route['affected']==need and route['original_decision']==old and route['old_decision_sha256']==canonical(old) and route['review_input_decision_sha256']==canonical(d)
    if not need:assert d==old
    caseproofs.append({'case_id':cid,'case_input_sha256':canonical(case),'old_decision_sha256':canonical(old),'review_input_decision_sha256':canonical(d),'affected':need,'changed_payload_dependencies':sorted(set(d['proposal_ids'])&changed),'source_and_occurrence_fields_exactly_frozen':True,'approval_status':d['independent_review']['status']})
assert len(affected)==105
assert routing['counts']=={'cases':188,'selected_proposals':117,'changed_complete_payloads':74,'affected_source_decisions':105}
# Freeze reviewed helper text without executing either helper or touching their outputs.
hd=T/'additional-final-helpers-v3';hd.mkdir(exist_ok=False)
for name in ['build_type_plan.py','prepare_review_selection.py']:
    p=R/name;raw=readbytes(p);(hd/name).write_bytes(raw)
details=save('additional-helper-checks-v3.json',{'reviewer':'/root/research_b','scope':'Independent mechanical/provenance checks; no scientific approval of own chemistry or others sources.','claims':claim_rows,'type_changes':type_proofs,'cases':caseproofs,'changed_payload_ids':sorted(changed),'affected_case_ids':affected,'counts':routing['counts'],'type_change_count':len(typed_flags),'typed_candidate_count':len(type_rows),'full_value_claim_coverage':58,'historical_human_and_component_type_changes':0,'evidence_receipt_only_appended':True})
for frozenfile in held.values():frozenfile.verify()
manifest=[{'path':(str(p.relative_to(W)) if p.is_relative_to(W) else str(p)),'sha256':hashlib.sha256(s.content).hexdigest(),'bytes':len(s.content)} for p,s in sorted(held.items())]
result={'reviewer':'/root/research_b','reviewed_at':datetime.now(timezone.utc).isoformat(),'verdict':'approve_exact_technical_plan_and_routing','task_scope':'Two root-authored report helpers and exact output ledgers. This reviewer authored some chemistry candidates and therefore explicitly does not approve chemical/source claims; D independently reviews those.','input_hash_manifest':manifest,'independent_check_script':{'path':str(Path(__file__).relative_to(W)),'sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},'detailed_checks':details,'verified_counts':{'original_flags':58,'exact_type_only_changes':58,'changed_type_candidates':51,'source_cases':188,'selected_payloads':117,'changed_complete_payloads':74,'affected_cases_requiring_review':105,'exact_unchanged_case_decisions':83,'exact_unchanged_payload_bytes':43},'findings':[],'retained_initial_audit_attempt':{'script':'.temp/w02-final-corrections-v1/chemistry/audit_additional_helpers_v3.py','log':'.temp/w02-final-corrections-v1/chemistry/audit-additional-helpers-v3.log','reason':'Reviewer initial assertion treated proposal_entry_sha256 as native proposal-object digest. It actually binds the complete frozen coordinator intake wrapper. The second audit verifies that exact wrapper and its original ledger hash; this was a reviewer scope assumption, not an input defect. A second preserved attempt used mandatory occurrences instead of the contract-defined empty KG fallback; v3c uses case.get(occurrences,[]) and preserves both failed logs.'},'assessment':['Every old58 full-value object and pointer binds the authentic oldselected payload and its prior audit row; explicit authored full-value lineage binds revised scientific entries before typing.','Every changed final YAML equals its pretype YAML with only the declared MappingEvidence.evidence_type edits plus one truthful appended curation event. All other chemical/source/role/component fields and historical events are exact. Historical unchanged human entries and component-evidence enums are not retyped.','The review routing is reconstructed independently from payload byte hashes and full original/pretype decisions. All188 rawsourcefields,caseobjectdigests and occurrenceIDs are exact;105 affectedcases and74changedpayloads are marked pending, not fabricated approved. The83unaffected decisions remain exactly historical.','Root labels D as the assigned actual reviewer but independent_approval_established remains false. This routing is an invitation/input record for fresh review, not proof D already approved.'], 'technical_limits':['The helpers use hardcoded isolated report locations and exclusive create, but ordinary multi-file reads/writes are not an atomic transaction or a general hostile-concurrency filesystem boundary. This audit captured and reverified every inspected input unchanged.','No helper was re-executed into its immutable output directory. The read-only independent audit reconstructed the exact outputs instead; it did not rerun root117native validators or replace D science review.','The all58 matrix supplies prior audited authorship classifications. This review verifies their exact bindings and actual type-only effect, not reclassification of every source truth claim or new approval by an original author.','The previous37-control suite and its resolved containment receipt remain separately sealed; the two new hardcoded helper workflows are bound here to their actual exact immutable outputs.']}
bound=save('additional-technical-review-v3.json',result);print(json.dumps(bound));print(json.dumps(result['verified_counts']))
