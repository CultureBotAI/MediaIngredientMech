"""Bounded technical replay; no scientific, admission or release approval.

All outputs are private. Published helper functions and Claw source are loaded
unchanged; their CLI main routines and publication functions are never called.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import asdict
from datetime import datetime, timezone
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import traceback

ROOT = Path.cwd()
P = ROOT / '.temp/all-unmatched-worker-08/tenvit-dependent-v1/validation/full-attempt-v1'
P.mkdir(exist_ok=False)
ART = ROOT / 'reports/all_unmatched_20261107/worker-08'
OLD = ART / 'successors/issue-1227-v1'
PREVIOUS = ART / 'successors/issue-1227-plain-flour-v1'
OUT = ART / 'successors/issue-1237-tenvit-v1'
CLAW = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw')
BASE = 'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'
PID = 'vm1237-prop-wolfe-cb-dependent'
CID = 'CM_NAME:d57e91ffaea6f0ab6ff0f3d6f0b04c26356c832e85dd83e9e2319874fda43506'
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / 'src'))
sys.path.insert(0, str(OLD / 'scripts'))
import yaml
import validate_selection as helpers
import check_identity_obligations as identity
from mediaingredientmech.validation.write_validated import write_validated_ingredient, ValidationFailedError
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.utils.ontology_client import OntologyClient
from mediaingredientmech.curie import mim_curie_for_stem


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def rel(path):
    path = Path(path)
    return str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)


def dump(name, value):
    path = P / name
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x') as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False, default=str)
        handle.write('\n')
    return dict(path=rel(path), sha256=sha(path))


COMMANDS = []


def command(argv, name):
    run = subprocess.run(argv, cwd=ROOT, capture_output=True, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'})
    (P / (name + '.stdout')).write_bytes(run.stdout)
    (P / (name + '.stderr')).write_bytes(run.stderr)
    COMMANDS.append(dict(argv=argv, cwd=str(ROOT), returncode=run.returncode,
                         stdout=rel(P / (name + '.stdout')), stderr=rel(P / (name + '.stderr'))))
    assert run.returncode == 0, (name, run.returncode, run.stderr.decode(errors='replace'))
    return run.stdout


def capture(ref):
    assert ref['root'] == 'artifact'
    path = ART / ref['path']
    assert path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(ART.resolve())
    assert sha(path) == ref['sha256'], ('capture hash', ref)
    return path


def main():
    started = datetime.now(timezone.utc).isoformat()
    dump('scope.json', dict(started_at=started, executor='worker08:/root/vitamins',
        independence='Technical executor and prior vitamin-source author; not independent scientific approval.',
        writes='Only this private validation directory', scientific_approval=False,
        maintained_application=False, release_approval=False))
    selected_path = OUT / 'proposals.json'
    assert sha(OUT / 'selection.json') == 'fb16bf5c29b981dc7dd60cf8d963a9aea25c12a65d6a0e55e29d84dfb2a26699'
    selection = read(OUT / 'selection.json')
    for ref in selection['authoritative_inputs'].values():
        capture(ref)
    assert sha(PREVIOUS / 'selection.json') == '335806d22ce278eaf628930b521d7164f0dee2493a19fbc790ae3c273d179f92'
    old_proposals = read(PREVIOUS / 'proposals.json')['proposals']
    proposals = read(selected_path)['proposals']
    assert len(proposals) == 114 and len(old_proposals) == 113
    old = {p['proposal_id']: p for p in old_proposals}
    current = {p['proposal_id']: p for p in proposals}
    assert len(current) == 114 and set(current) == set(old) | {PID}
    assert proposals[:113] == old_proposals, 'original 113 ordered proposal objects changed'
    author = read(OUT / 'author/proposal.json')
    assert {k:v for k,v in current[PID].items() if k != 'evidence_ids'} == {k:v for k,v in author.items() if k != 'evidence_ids'}
    assert current[PID]['evidence_ids'][:len(author['evidence_ids'])] == author['evidence_ids']
    files = {pid: capture(p['after_capture']) for pid, p in current.items()}
    records = {pid: yaml.safe_load(path.read_text()) for pid, path in files.items()}
    new = records[PID]
    before_path = OUT / 'beforeimages/Wolfes_Vitamin_Mix.yaml'
    prior = yaml.safe_load(before_path.read_text())
    assert sha(files[PID]) == 'b64eccf46c271520c27c73bc0a5863e2bc56447d1acf7461a90e3d72f9f4384f'
    assert sha(before_path) == current[PID]['before_sha256'] == '709749bd7c83c38a09400fc1893885ead753847ff9d1cbbe4ec76b431d349738'
    unchanged = [dict(proposal_id=pid,payload=current[pid]['after_capture']) for pid in old]
    assert all(current[pid] == old[pid] and sha(files[pid]) == old[pid]['after_capture']['sha256'] for pid in old)
    changed_fields = [k for k in sorted(set(prior) | set(new)) if prior.get(k) != new.get(k)]
    assert set(changed_fields) == {'components', 'component_assertion', 'notes', 'curation_history'}
    helpers.preserved_history(prior, new, True)
    assert new['curation_history'][-1]['llm_assisted'] is True
    old_decisions = read(PREVIOUS / 'decisions.json')['decisions']
    decisions = read(OUT / 'decisions.json')['decisions']
    assert len(decisions) == len(old_decisions) == 188
    od = {x['case_id']:x for x in old_decisions}; nd = {x['case_id']:x for x in decisions}
    assert len(nd) == 188 and set(od) == set(nd)
    assert [x['case_id'] for x in decisions] == [x['case_id'] for x in old_decisions]
    assert all(nd[c] == od[c] for c in od if c != CID)
    ac = read(OUT / 'author/decision.json')
    assert {k:v for k,v in nd[CID].items() if k not in ['evidence_ids','independent_review']} == {k:v for k,v in ac.items() if k not in ['evidence_ids','independent_review']}
    assert nd[CID]['evidence_ids'][:len(ac['evidence_ids'])] == ac['evidence_ids']
    assert nd[CID]['proposal_ids'] == od[CID]['proposal_ids'] + [PID]
    for c in od:
        for field in ['case_input_sha256','source','occurrence_ids','owner_records']:
            assert nd[c].get(field) == od[c].get(field), (c, field)
    occurrences = [o for x in decisions for o in x['occurrence_ids']]
    assert len(occurrences) == len(set(occurrences)) == 320
    assert len(nd[CID]['occurrence_ids']) == 6
    old_evidence = read(PREVIOUS / 'evidence.json')['evidence']
    evidence = read(OUT / 'evidence.json')['evidence']
    assert len(old_evidence) == 1082 and evidence[:1082] == old_evidence
    eids = [e['evidence_id'] for e in evidence]
    assert len(eids) == len(set(eids))
    assert all(set(d['evidence_ids']) <= set(eids) and set(d['proposal_ids']) <= set(current) for d in decisions)
    assert all(set(p['evidence_ids']) <= set(eids) and set(p['case_ids']) <= set(nd) for p in proposals)
    dump('selection-accounting.json', dict(status='PASS', selection_sha256=sha(OUT/'selection.json'),
        selected_count=114, unchanged_original_proposal_objects=113, unchanged_proposals=unchanged,
        cases=188, unchanged_decisions=187, occurrence_ids=320, dependent_case_occurrences=6,
        original_evidence_prefix=1082, final_evidence_count=len(evidence),
        changed_top_level_owner_fields=changed_fields, new_dependent_proposal_id=PID,
        author_final_appended_proposal_evidence=current[PID]['evidence_ids'][len(author['evidence_ids']):],
        author_final_appended_case_evidence=nd[CID]['evidence_ids'][len(ac['evidence_ids']):],
        final_independent_review=nd[CID]['independent_review'],
        independent_review_scope='Receipt bookkeeping checked only; no technical self-approval of science.'))
    print('Accounting passed: 188 cases, 320 occurrences, 114 proposals, original 113 exact.',flush=True)
    # Read the full maintained catalog, including ignored paths, and bind it to
    # the frozen Git tree without writing another checkout.
    listing = command(['git', 'ls-tree', '-r', '-z', BASE, '--', 'data/ingredients'], 'baseline-tree')
    tree = {}
    for entry in listing.split(b'\0'):
        if not entry:
            continue
        meta, name = entry.split(b'\t', 1)
        mode, kind, oid = meta.decode().split()
        if name.endswith(b'.yaml'):
            assert kind == 'blob' and mode == '100644'
            tree[name.decode()] = oid
    paths = sorted((ROOT / 'data/ingredients').rglob('*.yaml'))
    assert {rel(p) for p in paths} == set(tree)
    baseline_hashes, catalog = {}, {}
    for path in paths:
        raw = path.read_bytes()
        assert hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() == tree[rel(path)]
        baseline_hashes[rel(path)] = hashlib.sha256(raw).hexdigest()
        catalog[rel(path)] = yaml.safe_load(raw)
    assert len(catalog) == 2956
    dump('baseline-inputs.json', dict(baseline_commit=BASE, count=len(catalog), sha256_by_path=baseline_hashes,
        enumeration='Path.rglob includes ignored files; exact membership and Git blob bytes checked against frozen baseline.'))
    baseline_errors = list(map(str, validate_component_partonomy(catalog.values())))
    assert not baseline_errors, baseline_errors
    selected_owners = set()
    new_ids = set()
    held = []
    admission_path = OLD / 'independent-review/final_assembly/trypticase-admission-review-v1.json'
    assert sha(admission_path) == '97ba31cd26106faa23642b07692396a972e0147035bb9ab0ea90de479af463cf'
    admission = read(admission_path)
    predecessor1201 = {p['proposal_id']: p for p in read(ART / 'successors/issue-1201-v1/proposals.json')['proposals']}
    for p in proposals:
        pid, owner = p['proposal_id'], p['owner_path']
        rec = records[pid]
        assert owner not in selected_owners
        selected_owners.add(owner)
        if p['kind'] == 'edit_existing_owner':
            assert baseline_hashes[owner] == p['before_sha256']
            if rec['identifier'] != catalog[owner]['identifier']:
                try:
                    helpers.disallow_active_collision(catalog, owner, rec['identifier'])
                except AssertionError as failure:
                    hashes = {path: baseline_hashes[path] for path in admission['baseline_owner_checks']}
                    held.append(helpers.record_reviewed_admission_failure(p, predecessor1201[pid], hashes, admission, failure.args[0]))
        else:
            assert p['before_sha256'] is None and owner not in catalog and not (ROOT / owner).exists()
            assert rec['identifier'] not in {r['identifier'] for r in catalog.values()} | new_ids
            new_ids.add(rec['identifier'])
    assert len(held) == 1
    dump('owner-admission-failed-held.json', dict(status='FAILED/HELD', failures=held,
        exact_prior_review=dict(path=rel(admission_path), sha256=sha(admission_path)),
        qualification='The unchanged native collision gate still fails. This is a narrowly pinned recorded hold, not an exemption or owner admission.'))
    overlay = dict(catalog)
    overlay.update({p['owner_path']: records[p['proposal_id']] for p in proposals})
    overlay_errors = list(map(str, validate_component_partonomy(overlay.values())))
    dump('full-overlay.json', dict(baseline_record_count=len(catalog), selected_payload_count=114,
        overlay_record_count=len(overlay), baseline_partonomy_violations=baseline_errors,
        overlay_partonomy_violations=overlay_errors, owner_admission_status='HELD',
        scope='Native complete catalog partonomy, not identity admission or scientific acceptance.'))
    assert not overlay_errors, overlay_errors
    print('Full baseline/overlay partonomy passed; exact TSB/Bacto failed admission preserved.', flush=True)

    # Native guard/invariant controls already executed with exact same new bytes.
    payload_receipt = Path(__file__).parent / 'payload-attempt-v2/payload-checks.json'
    payload_checks = read(payload_receipt)
    assert payload_checks['status'] == 'PASS' and payload_checks['payload_sha256'] == sha(files[PID])
    assert len(payload_checks['controls']) == 12 and all(c['rejected'] for c in payload_checks['controls'])
    strict_command = [sys.executable, 'scripts/validate_strict.py', '--workers', '2', '--out', str(P / 'strict.tsv'), *map(str, files.values())]
    command(strict_command, 'strict')
    triage_path = OLD / 'inputs/coordinator-triage/target-verification-v1.json'
    alias_results = []
    for row in read(triage_path)['alias_checks']:
        text = row['synonym']['synonym_text']
        helpers.literal_nonresolving(records[row['proposal_id']],text)
        alias_results.append(dict(proposal_id=row['proposal_id'],literal=text,nonresolving=True))
    assert new.get('synonyms') == prior.get('synonyms')
    dump('alias-guards.json',dict(status='PASS',checked=alias_results,wolfe_synonyms_unchanged=True,
        native_policy_sha256=sha(ROOT/'src/mediaingredientmech/synonym_policy.py'),
        scope='Native rejected-label policy checks plus exact existing Wolfe synonym preservation; no universal synonym-equivalence claim.'))
    print('114 strict schemas and retained alias guards passed.',flush=True)
    fixture = P / 'identity-obligation-fixture'
    fixture.mkdir(exist_ok=False)
    native = identity.load_rules()
    native.INGREDIENTS_DIR = fixture
    native._subject_to_path.cache_clear()
    controls = identity.controls(native)
    rows, entries = [], []
    for p in proposals:
        pid = p['proposal_id']
        dest = fixture / Path(p['owner_path']).name
        assert not dest.exists()
        dest.write_bytes(files[pid].read_bytes())
        native._subject_to_path.cache_clear()
        subject = mim_curie_for_stem(dest.stem)
        assert native.record_identifier(subject) == records[pid]['identifier']
        projected = identity.projected_obligations(subject, records[pid])
        rows.extend(projected)
        entries.append(dict(proposal_id=pid, fixture=rel(dest), sha256=sha(dest), subject_id=subject,
            identifier=records[pid]['identifier'], projected_identity_obligations=projected))
    failures = {name: list(getattr(native, 'evaluate_rule_' + name)(rows)) for name in ['b1', 'b2', 'b3', 'b5', 'd']}
    wrong = [dict(row, predicate_id='skos:closeMatch') for row in rows
             if row['object_id'] == native.record_identifier(row['subject_id'])]
    rejected = list(native.evaluate_rule_d(wrong))
    dump('identity-obligations.json', dict(status='PASS' if not any(failures.values()) and len(wrong) == len(rejected) > 0 else 'FAIL',
        selected_count=len(entries), projected_rows=len(rows), predicate_counts=dict(Counter(r['predicate_id'] for r in rows)),
        native_failures=failures, native_controls=controls, actual_rule_d_negative_inputs=wrong,
        actual_rule_d_rejections=rejected, negative_rule_d_count=len(rejected), entries=entries,
        scope='Native B1/B2/B3/B5/D on unapplied identity obligations and exact private fixtures; no emitted whole SSSOM product.'))
    assert not any(failures.values()) and len(wrong) == len(rejected) > 0
    print('Native identity obligations and actual Rule D negatives passed.', flush=True)

    # Compile actual captured Claw source with its true __file__. Do not call
    # main(), any publication function, or a fixture substitute producer.
    entrypoint = CLAW / 'scripts/build_mim_ingredient_sssom.py'
    raw = entrypoint.read_bytes()
    spec = importlib.util.spec_from_file_location('tenvit_claw_source_snapshot', entrypoint)
    builder = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = builder
    exec(compile(raw, str(entrypoint), 'exec', dont_inherit=True), builder.__dict__)
    builder._check_producer_bindings()
    assert Path(builder.__file__).resolve() == entrypoint.resolve()
    producer_inputs = {str(path): hashlib.sha256(content).hexdigest() for path, content in builder._IMPORTED_PRODUCER_BYTES.items()}
    assert producer_inputs[str(entrypoint)] == hashlib.sha256(raw).hexdigest()
    claw_head = command(['git', '-C', str(CLAW), 'rev-parse', 'HEAD'], 'claw-head').decode().strip()
    assert claw_head == '76c1ebeea3fc7f80bf1abe044688f298f390cfac'
    old_overlay = dict(overlay)
    old_overlay[current[PID]['owner_path']] = prior
    projection_results = {}
    for version, snapshot, record, source_path in [('previous', old_overlay, prior, before_path),
                                                  ('current', overlay, new, files[PID])]:
        subjects = {}
        for owner, value in snapshot.items():
            subject = builder._mim_curie(Path(owner).name)
            assert subject not in subjects, ('duplicate Claw subject', owner, subject)
            subjects[subject] = value
        owners = builder.build_owner_index(subjects)
        suppressed = []
        projected = builder._row_from_yaml(source_path, {}, {}, {}, {},
            record=record, owners=owners, suppressions=suppressed)
        projection_results[version] = dict(payload_sha256=sha(source_path), full_overlay_count=len(snapshot),
            owner_index_count=len(owners), rows=projected, suppressions=[asdict(s) for s in suppressed],
            omitted_optional_inputs='No residual override, KG-Microbe label, or source enrichment. Real YAML producer and complete overlay name ownership index; no main or publisher invocation.')
    builder._check_producer_bindings()
    dump('claw-producer-source-hashes.json',dict(entrypoint=str(entrypoint),head=claw_head,true_file=builder.__file__,
        captured_compile=True,binding_guard_before_and_after='PASS',source_sha256_by_path=producer_inputs))
    dump('claw-actual-projections.json',projection_results)
    now_rows=projection_results['current']['rows'];before_rows=projection_results['previous']['rows']
    assert now_rows == before_rows and len(now_rows)>0, 'Wolfe SSSOM projection changed or empty'
    assert projection_results['current']['suppressions'] == projection_results['previous']['suppressions']
    assert all(row['subject_id']=='MIM:Wolfes_Vitamin_Mix' for row in now_rows)
    assert not list(native.evaluate_rule_d(now_rows))
    degraded=[dict(row,predicate_id='skos:closeMatch') for row in now_rows if row['object_id']==new['identifier']]
    rejected_wolfe=list(native.evaluate_rule_d(degraded))
    assert len(rejected_wolfe)==len(degraded)>0
    dump('claw-projection-assertions.json',dict(status='PASS',actual_projection_rows=len(now_rows),
        old_new_rows_exact_equal=True,old_new_suppressions_exact_equal=True,
        actual_rule_d_failures=[],degraded_identity_rejections=rejected_wolfe,
        held_admission_unchanged=True,maintained_publication=False))
    print('Actual Claw old/new Wolfe projections exactly equal.',flush=True)
    inputs = [OUT/'selection.json',selected_path,OUT/'decisions.json',OUT/'evidence.json',OUT/'lineage.json',
        OUT/'author/proposal.json',OUT/'author/decision.json',before_path,payload_receipt,
        PREVIOUS/'selection.json',PREVIOUS/'proposals.json',PREVIOUS/'decisions.json',PREVIOUS/'evidence.json',
        admission_path,triage_path,ROOT/'MAPPING_SEMANTICS.md',ROOT/'.claude/skills/add-media/SKILL.md',
        OLD/'scripts/assemble.py',OLD/'scripts/validate_selection.py',OLD/'scripts/check_identity_obligations.py',
        ROOT/'scripts/validate_strict.py',ROOT/'scripts/validate_sssom_invariants.py',
        ROOT/'src/mediaingredientmech/validation/write_validated.py',ROOT/'src/mediaingredientmech/validation/component_partonomy.py',
        ROOT/'src/mediaingredientmech/schema/mediaingredientmech.yaml',ROOT/'src/mediaingredientmech/sssom_grading.py',Path(__file__)]
    input_hashes={rel(p):sha(p) for p in inputs}
    assert all(sha(files[pid])==current[pid]['after_capture']['sha256'] for pid in current)
    assert all(sha(ROOT/path)==digest for path,digest in baseline_hashes.items())
    for ref in selection['authoritative_inputs'].values():capture(ref)
    dump('commands.json',COMMANDS)
    dump('completion.json',dict(status='PASS',started_at=started,completed_at=datetime.now(timezone.utc).isoformat(),
        executor='worker08:/root/vitamins',selected_payloads=114,new_dependent_payloads=1,exact_unchanged_payloads=113,
        cases=188,occurrence_ids=320,guarded_new_payloads=1,native_guard_negative_controls=2,invariant_negative_controls=10,
        strict_exit_code=0,baseline_records=len(catalog),overlay_records=len(overlay),baseline_partonomy_violations=0,
        overlay_partonomy_violations=0,native_rule_failures=failures,rule_d_degraded_identity_rejections=len(rejected),
        claw_actual_projected_payloads=2,wolfe_projection_unchanged=True,owner_admission_status='FAILED/HELD',
        owner_admission_failure_count=len(held),exact_selected_payloads_and_baseline_preserved=True,input_hashes=input_hashes,
        scientific_approval=False,independent_scientific_review=False,maintained_writes=False,maintained_SSSOM_export=False,
        release_approval=False,limits='Native shape, exact input/accounting preservation, complete catalog overlay partonomy, retained alias guards, native identity obligations, and actual old/new Wolfe row projection only. Does not grant source identity, scientific approval, owner admission, merge, roles, or release.'))
    print('COMPLETE technical PASS; owner admission FAILED/HELD; no scientific approval.',flush=True)

if __name__=='__main__':
    try:main()
    except BaseException as error:
        dump('failure.json',dict(at=datetime.now(timezone.utc).isoformat(),error_type=type(error).__name__,message=str(error),
            traceback=traceback.format_exc(),commands=COMMANDS,preservation='Exact failed runner and all completed stage outputs retained. No source mutation.'))
        raise
