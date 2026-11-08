"""Check proposed identity/predicate obligations with native rules, not an export.

No TSV is emitted or maintained row changed. Minimal in-memory rows state the
obligations that integration must implement; private exact-payload fixtures let
native Rule D inspect the real selected identifier, including CAS_RN_LOOKUP.
"""
from collections import Counter
from datetime import datetime, timezone
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import yaml
from mediaingredientmech.curie import mim_curie_for_stem
from mediaingredientmech.sssom_grading import predicate_for
from assemble import read, sha, checked_capture, SELECTION

ROOT = Path.cwd()
ART = ROOT / 'reports/all_unmatched_20261107/worker-08'
OUT = ART / 'successors/issue-1227-v1'
PRIVATE = ROOT / '.temp/all-unmatched-worker-08/issue-1227-v1'


def load_rules():
    spec = importlib.util.spec_from_file_location('isolated_native_sssom_rules', ROOT / 'scripts/validate_sssom_invariants.py')
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


def projected_obligations(subject, record):
    primary = record['identifier']; mapping = record.get('ontology_mapping') or {}
    target, grade = mapping.get('ontology_id'), mapping.get('mapping_quality')
    if record.get('mapping_status') != 'MAPPED':
        return []
    rows = [dict(subject_id=subject, object_id=primary, predicate_id='skos:exactMatch')]
    if target and target != primary:
        rows.append(dict(subject_id=subject, object_id=target, predicate_id=predicate_for(grade)))
    if grade == 'NARROW_MATCH':
        assert primary != target, 'specific identity collapsed to parent'
    if any(r['predicate_id'] in ['skos:broadMatch', 'skos:narrowMatch'] for r in rows):
        handle = 'kgmicrobe.ingredient:' + subject[4:].lower()
        if primary.startswith(('kgmicrobe.ingredient:', 'kgmicrobe.compound:')):
            handle = primary
        if not any(r['object_id'] == handle for r in rows):
            rows.append(dict(subject_id=subject, object_id=handle, predicate_id='skos:exactMatch'))
    return rows


def controls(native):
    checks = []
    r = dict(identifier='cas:10039-56-2', mapping_status='MAPPED',
             ontology_mapping=dict(ontology_id='CHEBI:34696', mapping_quality='NARROW_MATCH'))
    positive = projected_obligations('MIM:Native_Control', r)
    assert not list(native.evaluate_rule_b1(positive))
    checks.append('positive asymmetric identity retains distinct primary and mandatory registry sibling')
    missing = [x for x in positive if not x['object_id'].startswith('kgmicrobe.')]
    assert list(native.evaluate_rule_b1(missing))
    checks.append('native B1 rejects missing registry sibling even when CAS identity exists')
    duplicate = positive + [positive[0]]
    assert list(native.evaluate_rule_b2(duplicate))
    checks.append('native B2 rejects duplicate subject/object identity')
    contradiction = positive + [dict(subject_id='MIM:Native_Control', object_id='CHEBI:34696', predicate_id='skos:exactMatch')]
    assert list(native.evaluate_rule_b3(contradiction))
    checks.append('native B3 rejects exact and asymmetric mapping to same parent')
    collided = copy.deepcopy(r); collided['identifier'] = 'CHEBI:34696'
    try:
        projected_obligations('MIM:Native_Control', collided)
    except AssertionError:
        checks.append('specific parent-collapse rejected before projecting obligations')
    else:
        raise AssertionError('specific parent-collapse control escaped')
    return checks


def main():
    fixture = PRIVATE / 'identity-obligation-fixture'
    fixture.mkdir(exist_ok=False)
    native = load_rules(); native.INGREDIENTS_DIR = fixture
    checks = controls(native)
    rows, entries = [], []
    for p in read(SELECTION / 'proposals.json')['proposals']:
        path = checked_capture(p['after_capture'], ART); record = yaml.safe_load(path.read_text())
        filename = Path(p['owner_path']).name
        destination = fixture / filename
        assert not destination.exists(), ('duplicate filename', filename)
        shutil.copyfile(path, destination)
        subject = mim_curie_for_stem(destination.stem)
        assert native.record_identifier(subject) == record['identifier'], ('native fixture unresolved', subject)
        projected = projected_obligations(subject, record)
        rows.extend(projected)
        entries.append(dict(proposal_id=p['proposal_id'], payload=p['after_capture'], subject_id=subject,
            identifier=record['identifier'], ontology_mapping=record.get('ontology_mapping'),
            projected_identity_obligations=projected,
            applicability='Unapplied contract obligations only, not emitted/reviewed SSSOM rows or release approval.'))
        native._subject_to_path.cache_clear()
    failures = {}
    for name in ['b1', 'b2', 'b3', 'b5', 'd']:
        failures[name] = list(getattr(native, 'evaluate_rule_' + name)(rows))
    # Rule D must actually read the exact fixture, rather than skip all rows.
    wrong_identity = [dict(r, predicate_id='skos:closeMatch') for r in rows
                      if r['object_id'] == native.record_identifier(r['subject_id'])]
    rejected = list(native.evaluate_rule_d(wrong_identity))
    assert len(wrong_identity) > 0 and len(rejected) == len(wrong_identity)
    checks.append('native D rejects every deliberately degraded own-identifier row against exact selected payload bytes')
    assert not any(failures.values()), failures
    result = dict(at=datetime.now(timezone.utc).isoformat(), input_sha256=sha(SELECTION / 'proposals.json'),
        native_rule_sha256=sha(ROOT / 'scripts/validate_sssom_invariants.py'),
        native_grading_sha256=sha(ROOT / 'src/mediaingredientmech/sssom_grading.py'),
        selected_payload_count=len(entries), projected_obligation_rows=len(rows),
        predicate_counts=dict(Counter(r['predicate_id'] for r in rows)), native_failures=failures,
        controls=checks, negative_rule_d_targets=len(rejected), entries=entries,
        scope='Native B1/B2/B3/B5/D tested on explicit proposed identity obligations and exact private payload fixtures. No maintained SSSOM or downstream export was built or validated; complete source scientific and release reviews remain separate.')
    with (OUT / 'validation/identity-obligations.json').open('x') as out:
        json.dump(result, out, indent=2, ensure_ascii=False); out.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'entries'}))


if __name__ == '__main__': main()
