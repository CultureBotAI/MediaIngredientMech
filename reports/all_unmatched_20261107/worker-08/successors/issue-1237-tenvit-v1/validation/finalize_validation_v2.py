"""Finalize actual retained technical stages; repeat only bounded projection checks.

No source edits, export, admission waiver, or independent scientific approval.
The earlier exact-row assertion remains an honestly failed assertion.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import importlib.util
import json
import sys
import yaml

W=Path.cwd(); P=Path(__file__).absolute().parent
A=W/'reports/all_unmatched_20261107/worker-08'; O=A/'successors/issue-1237-tenvit-v1'
S=P/'full-attempt-v2'; V=P/'payload-attempt-v2'; OLD=A/'successors/issue-1227-v1'
sys.dont_write_bytecode=True;sys.path.insert(0,str(W/'src'));sys.path.insert(0,str(OLD/'scripts'))
import check_identity_obligations as identity

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def rel(p):
    p=Path(p);return str(p.relative_to(W)) if p.is_relative_to(W) else str(p)
def ref(p):return {'path':rel(p),'sha256':sha(p)}
def dump(name,v):
    with (P/name).open('x') as f:json.dump(v,f,indent=2,ensure_ascii=False,default=str);f.write('\n')

def main():
    select=O/'selection.json'
    assert sha(select)=='fb16bf5c29b981dc7dd60cf8d963a9aea25c12a65d6a0e55e29d84dfb2a26699'
    selection=read(select)
    for r in selection['authoritative_inputs'].values():assert r['root']=='artifact' and sha(A/r['path'])==r['sha256']
    proposals=read(O/'proposals.json')['proposals'];assert len(proposals)==114
    for p in proposals:assert sha(A/p['after_capture']['path'])==p['after_capture']['sha256']
    failed=read(S/'failure.json')
    assert failed['message']=='Wolfe SSSOM projection changed or empty'
    strict=[c for c in failed['commands'] if 'scripts/validate_strict.py' in c['argv']]
    assert len(strict)==1 and strict[0]['returncode']==0
    assert strict[0]['argv'][6:]==[str(A/p['after_capture']['path']) for p in proposals]
    assert list(csv.DictReader((S/'strict.tsv').open(),delimiter='\t'))==[]
    accounting=read(S/'selection-accounting.json')
    assert accounting['status']=='PASS' and accounting['selected_count']==114 and accounting['unchanged_original_proposal_objects']==113
    assert accounting['cases']==188 and accounting['occurrence_ids']==320 and accounting['original_evidence_prefix']==1082 and accounting['final_evidence_count']==1101
    baseline=read(S/'baseline-inputs.json')
    assert baseline['count']==len(baseline['sha256_by_path'])==2956
    assert {rel(p) for p in (W/'data/ingredients').rglob('*.yaml')}==set(baseline['sha256_by_path'])
    assert all(sha(W/p)==v for p,v in baseline['sha256_by_path'].items())
    overlay=read(S/'full-overlay.json')
    assert overlay['selected_payload_count']==114 and overlay['overlay_record_count']==3037
    assert overlay['baseline_partonomy_violations']==overlay['overlay_partonomy_violations']==[]
    alias=read(S/'alias-guards.json');assert alias['status']=='PASS' and len(alias['checked'])==10
    admit=read(S/'owner-admission-failed-held.json')
    assert admit['status']=='FAILED/HELD' and len(admit['failures'])==1
    assert admit['failures'][0]['proposal_id']=='op1201-trypticase-soy-broth' and admit['failures'][0]['gate_status']=='failed'
    ident=read(S/'identity-obligations.json')
    assert ident['status']=='PASS' and ident['selected_count']==114 and not any(ident['native_failures'].values())
    assert len(ident['actual_rule_d_negative_inputs'])==len(ident['actual_rule_d_rejections'])==ident['negative_rule_d_count']>0
    for e in ident['entries']:assert sha(W/e['fixture'])==e['sha256']
    checks=read(V/'payload-checks.json')
    assert checks['status']=='PASS' and len(checks['controls'])==12 and all(c['rejected'] for c in checks['controls'])
    for c in checks['controls']:assert sha(W/c['input']['path'])==c['input']['sha256']
    for p,h in checks['input_hashes'].items():assert sha(W/p)==h

    # Reload the unchanged real producer, not a mock or rewritten helper.
    producers=read(S/'claw-producer-source-hashes.json')
    assert all(sha(p)==h for p,h in producers['source_sha256_by_path'].items())
    entrypoint=Path(producers['entrypoint']);raw=entrypoint.read_bytes()
    spec=importlib.util.spec_from_file_location('tenvit_finalize_actual_claw',entrypoint)
    builder=importlib.util.module_from_spec(spec);sys.modules[spec.name]=builder
    exec(compile(raw,str(entrypoint),'exec',dont_inherit=True),builder.__dict__)
    builder._check_producer_bindings()
    assert str(Path(builder.__file__))==str(entrypoint)
    projections=read(S/'claw-actual-projections.json')
    b=projections['previous']['rows'];a=projections['current']['rows']
    assert len(a)==len(b)==1
    delta={k:{'before':b[0].get(k),'after':a[0].get(k)} for k in set(a[0])|set(b[0]) if a[0].get(k)!=b[0].get(k)}
    assert set(delta)=={'source','mapping_date'}
    beforepath=O/'beforeimages/Wolfes_Vitamin_Mix.yaml';afterpath=O/'payloads/Wolfes_Vitamin_Mix.yaml'
    before=yaml.safe_load(beforepath.read_text());after=yaml.safe_load(afterpath.read_text())
    for row,record,path in [(b[0],before,beforepath),(a[0],after,afterpath)]:
        assert row['mapping_date']==builder._mapping_date(path,record['curation_history'])
        assert row['source']=='MIM:MIM curation (#114)|MIM:curator='+builder._last_curator(record['curation_history'])
    assert a[0]['subject_id']=='MIM:Wolfes_Vitamin_Mix'
    assert a[0]['object_id']==after['identifier']=='kgmicrobe.ingredient:wolfes_vitamin_mix'
    assert a[0]['predicate_id']=='skos:exactMatch'
    assert projections['previous']['suppressions']==projections['current']['suppressions']==[]
    native=identity.load_rules();native.INGREDIENTS_DIR=S/'identity-obligation-fixture';native._subject_to_path.cache_clear()
    assert native.record_identifier(a[0]['subject_id'])==after['identifier']
    assert list(native.evaluate_rule_d(a))==[]
    bad=[dict(a[0],predicate_id='skos:closeMatch')];reject=list(native.evaluate_rule_d(bad));assert len(reject)==1
    builder._check_producer_bindings()
    dump('projection-qualification.json',dict(status='PASS',actual_projection_receipt=ref(S/'claw-actual-projections.json'),
        original_failed_assertion=ref(S/'failure.json'),identity_label_predicate_justification_confidence_aliases_unchanged=True,
        full_rows_byte_equal=False,exact_expected_history_provenance_delta=delta,
        metadata_verified_by_actual_native_helpers=['_mapping_date','_last_curator'],
        actual_rule_d_failures=[],actual_rule_d_degraded_control=bad,rejections=reject,
        native_sources=producers,limits='Two real in-memory YAML projections retained. No SSSOM export or downstream publication performed.'))
    failures=[dict(receipt=ref(P/'payload-checks-failure.json'),classification='harness defect',
        disposition='Invented-water mutant lacked quantity keys; version2 used a complete extra-water row and the same invariant path rejected it.'),
        dict(receipt=ref(P/'full-attempt-v1/failure.json'),classification='over-strict accounting assertion',
        disposition='Changed case legitimately appends authentic Wolfe owner preimage; version2 requires exact original prefix plus that one exact beforeimage.'),
        dict(receipt=ref(S/'failure.json'),classification='over-strict full projection equality',
        disposition='Actual new history changes only curator source and mapping date. This successor verifies those exact deltas and unchanged identity/predicate/aliases. Prior completed native stages reused unchanged.')]
    failures.append(dict(receipt=ref(P/'finalizer-attempt1-failure.json'),classification='finalizer argument index error',disposition='Corrected slice to actual payload start at argv index6; native command and full successful114-payload execution unchanged.'))
    native_paths=[W/'MAPPING_SEMANTICS.md',W/'.claude/skills/add-media/SKILL.md',W/'scripts/validate_strict.py',
        W/'scripts/validate_sssom_invariants.py',W/'src/mediaingredientmech/schema/mediaingredientmech.yaml',
        W/'src/mediaingredientmech/validation/write_validated.py',W/'src/mediaingredientmech/validation/component_partonomy.py',
        W/'src/mediaingredientmech/synonym_policy.py',W/'src/mediaingredientmech/sssom_grading.py',
        OLD/'scripts/validate_selection.py',OLD/'scripts/check_identity_obligations.py',OLD/'scripts/assemble.py']
    dump('receipt.json',dict(status='PASS',completed_at=datetime.now(timezone.utc).isoformat(),executor='worker08:/root/vitamins',
        role='Technical executor and prior source author; no independent scientific approval.',
        selection=ref(select),authoritative_inputs=selection['authoritative_inputs'],new_payload=ref(afterpath),
        cases=188,occurrence_ids=320,selected_payloads=114,original_proposal_objects_and_payloads_exact=113,
        unchanged_cases=187,evidence_entries=1101,original_evidence_prefix=1082,
        guarded_new_payloads=1,native_guard_negative_controls=2,exact_invariant_negative_controls=10,
        strict=dict(exit_code=0,payloads=114,violations=0,report=ref(S/'strict.tsv'),command=strict[0]),
        catalog=dict(baseline=2956,overlay=3037,partonomy_violations=0,receipt=ref(S/'full-overlay.json')),
        rejected_alias_guards=10,identity_obligations=dict(payloads=114,native_failures=ident['native_failures'],
        actual_rule_d_degraded_identity_rejections=ident['negative_rule_d_count'],receipt=ref(S/'identity-obligations.json')),
        wolfe_sssom_identity_predicate_alias_projection_unchanged=True,wolfe_full_sssom_row_equal=False,
        wolfe_expected_provenance_delta=delta,projection_receipt=ref(P/'projection-qualification.json'),
        owner_admission_status='FAILED/HELD',owner_admission_failures=admit['failures'],
        stages_reused_without_rerun=['114 strict schemas','2956 baseline and3037 overlay partonomy','all114 identity obligations','retained10 alias guards','2 native and10 invariant negatives'],
        final_rechecks=['All114 payload pins','all2956 baseline file bytes and ignored-inclusive membership','all selector input pins',
            'all exact identity fixture bytes','real Claw producer bindings and history metadata functions','actual Wolfe Rule D positive and degraded negative'],
        retained_attempts=failures,native_input_hashes={rel(p):sha(p) for p in native_paths},
        exact_sources_and_payloads_unchanged=True,maintained_writes=False,maintained_SSSOM_export=False,
        independent_scientific_review=False,scientific_approval=False,owner_admission_approval=False,release_approval=False,
        limits='Technical validation only. Source equivalence, CB-versus-nominal recipe association, W06/W08 duplicate reconciliation, role and downstream approvals remain separate and held where previously held. No blanket approval of 113 inherited proposals.'))
    members=[ref(p) for p in sorted(P.rglob('*')) if p.is_file() and p.name!='MANIFEST.json']
    dump('MANIFEST.json',dict(created_at=datetime.now(timezone.utc).isoformat(),status='complete',files=members,
        scope='Entire private technical packet including failed attempts, actual native fixtures, commands, reports and final qualification. No independent science approval.'))
    print('PASS receipt',sha(P/'receipt.json'),'MANIFEST',sha(P/'MANIFEST.json'),'files',len(members))

if __name__=='__main__':main()
