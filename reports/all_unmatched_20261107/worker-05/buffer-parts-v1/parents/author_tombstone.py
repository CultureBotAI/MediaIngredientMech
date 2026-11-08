from pathlib import Path
from datetime import datetime, timezone
import copy, hashlib, json, shutil
import yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient, validate_ingredient
from mediaingredientmech.synonym_policy import preferred_term_owners

W=Path.cwd();C=W.parents[2];S=W/'.temp/w05-buffer-parts-v1/parents';B=W/'reports/all_unmatched_20261107/worker-05';T=S/'tombstone';T.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
objsha=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
AT=datetime.now(timezone.utc).isoformat();CID='KG_CASE:c32b77bb4cf6ac08f95e5ee9c40834693b98899db178b6451c581aabf6cccb25';PID='W05-PARENTS-BACTO-SOYTONE-CONTINUITY';PUBLIC='buffer-parts-v1/parents/'
def write(p,x):
    assert not p.exists(),p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def cp(a,b):
    assert not b.exists();b.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a,b);assert sha(a)==sha(b)
owner='data/ingredients/mapped/Bacto_Soytone.yaml';src=W/owner
assert sha(src)=='b9c7e1b675da46d8733749a16b9c56f07618bb63ab5ecd71bdef1bf1cc2d2535'
before=T/'before/Bacto_Soytone.yaml';cp(src,before);r=yaml.safe_load(before.read_text());base=copy.deepcopy(r)
assert r['mapping_status']=='REJECTED' and r['representative']=='FOODON:03315720'
assert r['occurrence_statistics']=={'total_occurrences':0,'media_count':0}

# Bounded complete selected-proposal inventory supplied by the coordinator, plus current W05 core.
audit=C/'preflight/soy-identifier-dependency-preflight-v1';inv= json.loads((audit/'committed-selection-inventory.json').read_text())
payloads=inv['payloads']; assert isinstance(payloads,list)
duplicates=[x for x in payloads if x.get('owner_path')==owner or x.get('path')==owner or x.get('destination_owner_path')==owner]
core=json.loads((B/'tellurium-polypeptone-v1/core/proposals.json').read_text())['proposals'];local_duplicates=[p for p in core if p['owner_path']==owner or p.get('destination_owner_path')==owner]
assert not duplicates and not local_duplicates,(duplicates,local_duplicates)
cp(audit/'committed-selection-inventory.json',T/'input/committed-selection-inventory.json')
cp(audit/'soy-and-shared-identifier-proposals.json',T/'input/soy-and-shared-identifier-proposals.json')
cp(audit/'HANDOFF.json',T/'input/coordinator-HANDOFF.json')
scan=dict(at=AT,author='/root/buffer_hepes',ignored_files_included=True,source_inventory=dict(path=str(audit/'committed-selection-inventory.json'),sha256=sha(audit/'committed-selection-inventory.json')),selected_payloads_examined=len(payloads),selected_target_owner_matches=duplicates,current_W05_proposals_examined=len(core),current_W05_owner_matches=local_duplicates,limit='Exact coordinator committed selector cutoff; other live-head advances remain root integration checks. No inferred duplicate-owner absence beyond these inventories.')
write(T/'duplicate-check.json',scan)

text=(
    'Mark the historical Bacto Soytone merge representative explicitly unresolved with an empty representative string. '
    'The old FOODON:03315720 identifier is shared by active owners and cannot establish a unique current generic-Soy representative after the source-qualified Soy identity correction. '
    'A direct redirect to MICRO:0000181 would assert unsupported equality of a named Bacto product and generic soy digest. '
    'Native preferred-term ownership treats an explicit unresolved representative as retaining the rejected tombstone name; removing the field would instead fall back to the old shared identifier. '
    'Preserve the original identifier, ontology mapping and historical evidence, rejected status, all source names, zero statistics and complete merge history as historical provenance. '
    'No active Bacto owner is minted, no prior occurrence is reassigned, no branded/generic equality is inferred, and no role/source/export admission follows. '
    'Root must reconcile a scientifically supported branded representative and historical source membership before any later identity redirect.'
)
r['representative']=''
r['ontology_mapping']['evidence'].append(dict(evidence_type='LLM_SUGGESTION',source='https://assets.thermofisher.com/TFS-Assets/BPD/brochures/peptones-supplements-feeds-technical-reference-guide.pdf',notes='Printed page33 distinguishes named Bacto Soytone and other soy peptone products and processing. Combined with the authentic historical merge and current shared-identifier inventory, generic soy-digest identity does not establish a unique branded Bacto representative. This supports withholding the active representative redirect, not a new ontology identity or a revision of historical human evidence.'))
r['curation_history'].append(dict(timestamp=AT,curator='Codex /root/buffer_hepes; W05 Soy continuity dependent proposal',action='MARKED_TOMBSTONE_REPRESENTATIVE_UNRESOLVED',changes=text,previous_status='REJECTED',new_status='REJECTED',llm_assisted=True,llm_model='gpt-6'))
r['notes']=(r.get('notes','')+'\n\n' if r.get('notes') else '')+'Report-only Soy continuity disposition: '+text+' The earlier mapping/evidence and identity strings are retained solely as authentic tombstone history, not newly approved live material identity. Empty representative is deliberate and must remain explicit; no replacement target is asserted.'
assert not validate_ingredient(r)
out=T/'proposed/Bacto_Soytone.yaml';write_validated_ingredient(r,out);assert yaml.safe_load(out.read_text())['representative']==''
assert r['curation_history'][:-1]==base['curation_history'] and r['ontology_mapping']['evidence'][:-1]==base['ontology_mapping']['evidence']
changed=[k for k in set(base)|set(r) if base.get(k)!=r.get(k)];assert set(changed)=={'representative','ontology_mapping','curation_history','notes'}
assert all(r.get(k)==base.get(k) for k in base if k not in changed)

records={str(p.relative_to(W)):yaml.safe_load(p.read_text()) for p in (W/'data/ingredients').rglob('*.yaml')}
for p in core:
    f=B/p['after_capture']['path'];assert sha(f)==p['after_capture']['sha256'];records.pop(p['owner_path'],None);records[p.get('destination_owner_path',p['owner_path'])]=yaml.safe_load(f.read_text())
for p in json.loads((S/'final/proposals.json').read_text())['proposals']:
    f=S/p['after_capture']['path'].removeprefix(PUBLIC);assert sha(f)==p['after_capture']['sha256'];records[p['owner_path']]=yaml.safe_load(f.read_text())
subject=lambda path:'MIM:'+Path(path).stem
own=lambda rs:preferred_term_owners({subject(k):v for k,v in rs.items()})
bo=own(records);removed=copy.deepcopy(records);removed[owner].pop('representative');ro=own(removed);after=copy.deepcopy(records);after[owner]=r;ao=own(after)
assert ao['bacto soytone']==frozenset({'MIM:Bacto_Soytone'})
assert ro['bacto soytone']==bo['bacto soytone'] and 'MIM:Soy_Peptone' not in bo['bacto soytone']
assert not set(ao['bacto soytone']) & set(bo['bacto soytone'])
write(T/'native-alias-reproduction.json',dict(author='/root/buffer_hepes',at=AT,policy=dict(path='src/mediaingredientmech/synonym_policy.py',sha256=sha(W/'src/mediaingredientmech/synonym_policy.py')),existing_regression_test=dict(path='tests/test_sssom_other_cross_record.py',sha256=sha(W/'tests/test_sssom_other_cross_record.py'),test='test_missing_explicit_target_never_credits_former_identifier_owner; explicit empty target case'),current_W05_plus_selected_parent_records=len(records),preferred_name='Bacto Soytone',before_with_old_explicit_target=sorted(bo['bacto soytone']),counterfactual_field_removed=sorted(ro['bacto soytone']),after_explicit_empty_target=sorted(ao['bacto soytone']),result='PASS',interpretation='Explicit unresolved pointer retains the tombstone name and does not credit unrelated shared-ID owners; absence would retain unsafe legacy fallback. This is continuity preservation, not a branded identity decision.'))

evidence=[]
for eid,f,kind,locator,support in [
    ('W05-PARENTS-TOMBSTONE-BEFORE',before,'owner_record','Authentic complete rejected Bacto_Soytone beforeimage; every history event and existing evidence retained.','The original representative points to shared FOODON03315720 and historical merge selected generic Soy.'),
    ('W05-PARENTS-TOMBSTONE-INVENTORY',T/'duplicate-check.json','source_snapshot','Complete coordinator selected proposal inventory and current W05 proposal owner-path check.','No duplicate Bacto_Soytone dependent proposal in this bounded committed selector; no new source case.'),
    ('W05-PARENTS-TOMBSTONE-POLICY',T/'native-alias-reproduction.json','source_snapshot','Actual native preferred_term_owners behavior with complete W05+selected-parent index.','Explicit unresolved target avoids fallback; no schema or gate change.'),
    ('W05-PARENTS-TOMBSTONE-AUDIT',T/'input/coordinator-HANDOFF.json','source_snapshot','Coordinator conditional source dependency audit, attributed to /root/step7d_science_c.','Shared-ID occurrence associations and representative continuity remain distinct from source identity; original audit is not reauthored.')
]:evidence.append(dict(evidence_id=eid,capture=dict(root='artifact',path=PUBLIC+str(f.relative_to(S)),sha256=sha(f)),kind=kind,locator=locator,supports_or_contradicts=support,case_ids=[CID],url=None))
eids=[e['evidence_id'] for e in evidence]+['W05-PARENTS-THERMO','W05-PARENTS-COMMENT6719869465']
p=dict(proposal_id=PID,case_ids=[CID],description=text,owner_path=owner,kind='edit_existing_owner',before_sha256=sha(before),before_capture=dict(root='artifact',path=PUBLIC+'tombstone/before/Bacto_Soytone.yaml',sha256=sha(before)),after_capture=dict(root='artifact',path=PUBLIC+'tombstone/proposed/Bacto_Soytone.yaml',sha256=sha(out)),evidence_ids=eids,primary_author='/root/buffer_hepes',source_trigger_proposal_id='W05-FINAL-MAT-032',source_trigger_case_id=CID,dependency_kind='historical merge representative continuity',identity_consequence='No replacement material identity or active owner. Historical rejected identifier/mapping remain; explicit empty representative withholds unsafe live identity credit.',predicate_consequence='REJECTED tombstone emits no mapping row; native preferred-name ownership remains on its own tombstone subject, not shared live FOODON owners.',publication_obligations='Root composes the full Soy source decision and requires exact independent review, authentic-before verification, complete native alias/guarded/full-overlay checks. All source membership, sibling and export holds persist.',cross_shard_conflict='Coordinator exact committed inventory checked before adding this dependent owner proposal; root must check any later selector deltas.',independent_review=dict(status='pending exact full payload and composed source decision',evidence_ids=[]))
write(S/'final/tombstone-proposals.json',dict(schema_version=1,proposals=[p]))
write(S/'final/tombstone-evidence.json',dict(schema_version=1,evidence=evidence))
base_d=next(x for x in json.loads((S/'input/selected-decisions.json').read_text())['decisions'] if x['case_id']==CID)
owner_binding=dict(path=owner,sha256=sha(before));assert owner_binding in base_d['owner_records']
delta=dict(case_id=CID,base_decision_sha256=objsha(base_d),additions=dict(proposal_ids=[PID],evidence_ids=eids,owner_records=[owner_binding]),owner_before_binding_already_present=True,soy_continuity_reassessment=dict(author='/root/buffer_hepes',at=AT,status='bounded authentic dependent proposal prepared; exact independent review pending',proposal_id=PID,source_trigger_proposal_id='W05-FINAL-MAT-032',source_case_ownership_unchanged=True,new_source_cases=0,before_representative='FOODON:03315720',proposed_representative='',rationale=text,shared_membership_not_partitioned=True,whole_owner_or_release_approval=False),composition='Add unique arrays and the distinct soy_continuity_reassessment field only. Preserve the full parent decision, all original owner bindings, holds and source occurrences; root reviews full final composed decision.')
write(S/'final/tombstone-case-deltas.json',dict(schema_version=1,author='/root/buffer_hepes',deltas=[delta]))
write(T/'author-receipt.json',dict(at=AT,author='/root/buffer_hepes',proposal_id=PID,before_sha256=sha(before),after_sha256=sha(out),changed_fields=sorted(changed),prior_history_events_preserved=len(base['curation_history']),prior_mapping_evidence_objects_preserved=len(base['ontology_mapping']['evidence']),new_history_events=1,new_mapping_evidence_type='LLM_SUGGESTION',all_remaining_fields_unchanged=True,original_source_case_owner_binding_already_present=True,source_case=CID))
print(json.dumps(dict(proposal_id=PID,before=sha(before),after=sha(out),native_alias_before=sorted(bo['bacto soytone']),native_alias_after=sorted(ao['bacto soytone']))))
