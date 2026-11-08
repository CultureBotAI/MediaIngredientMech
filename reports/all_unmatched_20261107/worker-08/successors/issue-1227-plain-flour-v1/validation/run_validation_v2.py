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
P = ROOT / '.temp/all-unmatched-worker-08/plain-flour-method-v1/validation/attempt-v2'
P.mkdir(exist_ok=False)
ART = ROOT / 'reports/all_unmatched_20261107/worker-08'
OLD = ART / 'successors/issue-1227-v1'
OUT = ART / 'successors/issue-1227-plain-flour-v1'
CLAW = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw')
BASE = 'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'
PID = 'op1201-plain-flour'
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
    dump('scope.json', dict(started_at=started, executor='worker08:/root/organics',
        independence='Technical executor authored predecessor organic proposal; no independent scientific approval.',
        writes='Only this private validation directory', scientific_approval=False,
        maintained_application=False, release_approval=False))
    selected_path = OUT / 'proposals.json'
    assert sha(OUT / 'selection.json') == '335806d22ce278eaf628930b521d7164f0dee2493a19fbc790ae3c273d179f92'
    selection = read(OUT / 'selection.json')
    for ref in selection['authoritative_inputs'].values():
        capture(ref)
    old_proposals = read(OLD / 'final-v2/proposals.json')['proposals']
    proposals = read(selected_path)['proposals']
    assert len(proposals) == len(old_proposals) == 113
    old = {p['proposal_id']: p for p in old_proposals}
    current = {p['proposal_id']: p for p in proposals}
    assert len(current) == 113 and set(old) == set(current)
    author = read(OUT / 'author/proposal.json')
    assert {k:v for k,v in current[PID].items() if k != 'evidence_ids'} == {k:v for k,v in author.items() if k != 'evidence_ids'}
    assert current[PID]['evidence_ids'] == author['evidence_ids'] + ['w08-final001-science', 'w08-final001-skeptical', 'w08-final001-historical-review-referral']
    dump('author-final-metadata-boundary.json', dict(status='PASS', exact_delta='Only the three explicitly bound final peer/referral evidence IDs are appended.', appended_ids=current[PID]['evidence_ids'][len(author['evidence_ids']):]))
    files = {pid: capture(p['after_capture']) for pid, p in current.items()}
    records = {pid: yaml.safe_load(path.read_text()) for pid, path in files.items()}
    new = records[PID]
    prior = yaml.safe_load(capture(old[PID]['after_capture']).read_text())
    assert sha(files[PID]) == '884fee1ea6a5082a51b8769f2a827199b1703972ad80fa48e1bb8d2d09ab3873'
    unchanged = []
    for pid in current:
        if pid == PID:
            continue
        assert current[pid] == old[pid], ('unexpected proposal metadata delta', pid)
        assert sha(files[pid]) == old[pid]['after_capture']['sha256']
        unchanged.append(dict(proposal_id=pid, payload=current[pid]['after_capture']))
    assert len(unchanged) == 112
    for field in ['proposal_id', 'case_ids', 'owner_path', 'kind', 'before_sha256']:
        assert current[PID][field] == old[PID][field], field
    changed_fields = [k for k in sorted(set(prior) | set(new)) if prior.get(k) != new.get(k)]
    assert set(changed_fields) == {'preferred_term', 'ontology_mapping', 'notes', 'curation_history'}
    helpers.preserved_history(prior, new, True)
    assert len(new['curation_history']) == len(prior['curation_history']) + 1
    assert new['curation_history'][-1]['llm_assisted'] is True
    assert new['preferred_term'] == 'flour'
    for field in ['identifier', 'synonyms', 'ingredient_type', 'mapping_status']:
        assert new[field] == prior[field], field
    for field in ['ontology_id', 'ontology_label', 'ontology', 'mapping_quality']:
        assert new['ontology_mapping'].get(field) == prior['ontology_mapping'].get(field), field
    assert new['ontology_mapping']['mapping_quality'] == 'EXACT_MATCH'
    dump('selection-and-112-unchanged.json', dict(selection_sha256=sha(OUT / 'selection.json'),
        final_proposals_sha256=sha(selected_path), predecessor_proposals_sha256=sha(OLD / 'final-v2/proposals.json'),
        selected_count=113, changed_proposal=PID, changed_payload_sha256=sha(files[PID]),
        changed_top_level_fields=changed_fields, exact_other_proposals_and_payloads=unchanged))
    print('Selection verified: 113, exactly 112 unchanged.', flush=True)

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
    dump('full-overlay.json', dict(baseline_record_count=len(catalog), selected_payload_count=113,
        overlay_record_count=len(overlay), baseline_partonomy_violations=baseline_errors,
        overlay_partonomy_violations=overlay_errors, owner_admission_status='HELD',
        scope='Native complete catalog partonomy, not identity admission or scientific acceptance.'))
    assert not overlay_errors, overlay_errors
    print('Full baseline/overlay partonomy passed; exact TSB/Bacto failed admission preserved.', flush=True)

    # Guard only the newly changed full payload; full113 strict check follows.
    replay = P / 'guarded-replay/Plain_Flour.yaml'
    write_validated_ingredient(copy.deepcopy(new), replay)
    assert yaml.safe_load(replay.read_text()) == new
    guard_controls = []
    for name in ['unknown-field', 'invalid-enum']:
        malformed = copy.deepcopy(new)
        if name == 'unknown-field':
            malformed['plain_flour_native_unknown_field_control'] = True
        else:
            malformed['ontology_mapping']['mapping_quality'] = 'INVALID_NATIVE_ENUM_CONTROL'
        fixture = P / 'controls' / (name + '.json')
        dump('controls/' + name + '.json', malformed)
        target = P / 'controls' / (name + '-must-not-be-written.yaml')
        try:
            write_validated_ingredient(malformed, target)
        except ValidationFailedError as error:
            guard_controls.append(dict(control=name, rejected=True, error_type=type(error).__name__,
                diagnostic=str(error), input_sha256=sha(fixture), target_absent=not target.exists()))
            assert not target.exists()
        else:
            raise AssertionError(('guard control escaped', name))
    dump('guarded-replay.json', dict(status='PASS', input_sha256=sha(files[PID]), replay_sha256=sha(replay),
        parsed_equal=True, controls=guard_controls, replay_path=rel(replay)))
    strict_command = [sys.executable, 'scripts/validate_strict.py', '--workers', '2', '--out', str(P / 'strict.tsv'), *map(str, files.values())]
    command(strict_command, 'strict')
    print('Guarded replay and 113-payload strict validator passed.', flush=True)

    primary_path = OUT / 'research/primary-label-resolution.json'
    primary = read(primary_path)
    adapter = OntologyClient()._get_adapter('FOODON')
    assert adapter is not None
    actual = adapter.label('FOODON:00004510')
    assert actual == new['preferred_term'] == new['ontology_mapping']['ontology_label'] == 'flour'
    # Exact matching is intentionally not synonym matching: the negative uses
    # the actual predecessor label and a fresh native canonical label lookup.
    control_label = prior['preferred_term']
    native_control_label = adapter.label(new['ontology_mapping']['ontology_id'])
    assert control_label != native_control_label
    dump('canonical-label-and-control.json', dict(primary_receipt=dict(path=rel(primary_path), sha256=sha(primary_path)),
        native_lookup=dict(curie='FOODON:00004510', adapter_class=type(adapter).__name__, label=actual),
        current_preferred_label=new['preferred_term'], current_grade=new['ontology_mapping']['mapping_quality'],
        positive_exact_equality=True, negative_exact_label_control=dict(input_label=control_label,
        actual_native_label=native_control_label, rejected_as_exact_primary_label=control_label != native_control_label),
        scope='Technical primary-label equality only. No inference of generic material applicability, unique ontology synonym or CAS lookup.'))

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
    spec = importlib.util.spec_from_file_location('plain_flour_claw_source_snapshot', entrypoint)
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
    for version, snapshot, record, source_path in [('previous', old_overlay, prior, capture(old[PID]['after_capture'])),
                                                  ('current', overlay, new, files[PID])]:
        subjects = {}
        for owner, value in snapshot.items():
            subject = builder._mim_curie(Path(owner).name)
            assert subject not in subjects, ('duplicate Claw subject', owner, subject)
            subjects[subject] = value
        owners = builder.build_owner_index(subjects)
        suppressed = []
        projected = builder._row_from_yaml(source_path, {}, {}, {}, {'FOODON:00004510': actual},
            record=record, owners=owners, suppressions=suppressed)
        projection_results[version] = dict(payload_sha256=sha(source_path), full_overlay_count=len(snapshot),
            owner_index_count=len(owners), rows=projected, suppressions=[asdict(s) for s in suppressed],
            omitted_optional_inputs='No residual override or KG-Microbe labels/source enrichment; the actual YAML producer is invoked with the full overlay owned-name index and verified native canonical label.')
    builder._check_producer_bindings()
    dump('claw-producer-source-hashes.json', dict(entrypoint=str(entrypoint), head=claw_head, true_file=builder.__file__,
        captured_compile=True, binding_guard_before_and_after='PASS', source_sha256_by_path=producer_inputs))
    dump('claw-actual-projections.json', projection_results)
    now_rows = projection_results['current']['rows']
    before_rows = projection_results['previous']['rows']
    assert len(now_rows) == len(before_rows) == 1
    row = now_rows[0]
    assert row['subject_id'] == before_rows[0]['subject_id'] == 'MIM:Plain_Flour'
    assert row['subject_label'] == 'flour' and before_rows[0]['subject_label'] == 'Plain flour'
    assert row['object_id'] == 'FOODON:00004510' and row['object_label'] == 'flour'
    assert row['predicate_id'] == 'skos:exactMatch' and row['mapping_justification'] == 'semapv:LexicalMatching'
    assert 'Plain flour' in row['other'].split('|')
    assert not builder._cas_token(new) and not any(t.casefold().startswith('cas:') for t in row['other'].split('|'))
    assert len(list(native.evaluate_rule_d(now_rows))) == 0
    degraded_flour = [dict(row, predicate_id='skos:closeMatch')]
    flour_reject = list(native.evaluate_rule_d(degraded_flour))
    assert len(flour_reject) == 1
    dump('claw-projection-assertions.json', dict(status='PASS', projected_payloads=2,
        stable_subject='MIM:Plain_Flour', current_subject_label='flour', object_id='FOODON:00004510',
        predicate='skos:exactMatch', justification='semapv:LexicalMatching', raw_alias_retained=True,
        invented_CAS=False, actual_new_row_rule_d_failures=[], degraded_new_row_rule_d_rejection=flour_reject,
        maintained_publication=False, held_owners_release=False))
    print('Actual Claw old/new in-memory projections passed.', flush=True)

    inputs = [OUT / 'selection.json', selected_path, OUT / 'author/proposal.json', primary_path,
        OLD / 'final-v2/proposals.json', admission_path, ROOT / 'MAPPING_SEMANTICS.md',
        ROOT / '.claude/skills/curate-yaml-record/SKILL.md',
        OLD / 'scripts/assemble.py', OLD / 'scripts/validate_selection.py', OLD / 'scripts/check_identity_obligations.py',
        ROOT / 'scripts/validate_strict.py', ROOT / 'scripts/validate_sssom_invariants.py',
        ROOT / 'src/mediaingredientmech/validation/write_validated.py',
        ROOT / 'src/mediaingredientmech/validation/component_partonomy.py',
        ROOT / 'src/mediaingredientmech/utils/ontology_client.py',
        ROOT / 'src/mediaingredientmech/sssom_grading.py', Path(__file__)]
    input_hashes = {rel(p): sha(p) for p in inputs}
    for pid in current:
        assert sha(files[pid]) == current[pid]['after_capture']['sha256']
    assert all(sha(ROOT / path) == digest for path, digest in baseline_hashes.items())
    dump('commands.json', COMMANDS)
    dump('completion.json', dict(status='PASS', started_at=started, completed_at=datetime.now(timezone.utc).isoformat(),
        executor='worker08:/root/organics', selected_payloads=113, changed_payloads=1, exact_unchanged_payloads=112,
        guarded_changed_payloads=1, native_guard_negative_controls=2, strict_exit_code=0,
        baseline_records=len(catalog), overlay_records=len(overlay), baseline_partonomy_violations=0,
        overlay_partonomy_violations=0, native_rule_failures=failures,
        rule_d_deliberately_degraded_identity_rejections=len(rejected), claw_actual_projected_payloads=2,
        canonical_label_mismatch_control_rejected=True, owner_admission_status='FAILED/HELD',
        owner_admission_failure_count=len(held), exact_selected_payloads_and_baseline_preserved=True,
        input_hashes=input_hashes, scientific_approval=False, independent_scientific_review=False,
        maintained_writes=False, maintained_SSSOM_export=False, release_approval=False,
        limits='This technical receipt checks native shape, exact input preservation, full-overlay partonomy, explicit identity obligations and the actual old/new single-owner Claw row projection. It does not attest source material equivalence, certify inherited whole-owner claims, admit TSB/Bacto, or authorize release.'))
    print('COMPLETE: bounded technical validation PASS; owner admission FAILED/HELD; no scientific approval.', flush=True)


if __name__ == '__main__':
    try:
        main()
    except BaseException as error:
        dump('failure-attempt-v2.json', dict(at=datetime.now(timezone.utc).isoformat(), error_type=type(error).__name__,
             message=str(error), traceback=traceback.format_exc(), commands=COMMANDS,
             preservation='All completed stage artifacts and this exact runner are retained; no automatic fix or retry.'))
        raise
