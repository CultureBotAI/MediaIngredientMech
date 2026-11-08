"""Read-only native validation of all selected proposal bytes, 2026-11-08.

Writes replay fixtures only beneath this task's private directory. A schema or
partonomy result is never scientific acceptance. Maintained data is read-only.
"""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.synonym_policy import is_resolving_synonym
from mediaingredientmech.utils.ontology_client import OntologyClient
from assemble import sha, read, checked_capture, SELECTION

ROOT = Path.cwd()
ART = ROOT / 'reports/all_unmatched_20261107/worker-08'
OUT = ART / 'successors/issue-1227-v1'
PRIVATE = ROOT / '.temp/all-unmatched-worker-08/issue-1227-v1'
BASE = 'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'


def preserved_history(prior, rec, changed):
    history = prior.get('curation_history', [])
    assert rec.get('curation_history', [])[:len(history)] == history, 'lost history'
    if changed:
        assert len(rec.get('curation_history', [])) > len(history), 'missing correction history'
    for field in ['roles', 'community_organism_roles', 'nutritional_roles',
                  'physicochemical_roles', 'cellular_metabolic_roles',
                  'causal_graphs', 'occurrence_statistics']:
        assert rec.get(field) == prior.get(field), ('role/occurrence/graph mutation', field)


def truthful_mapping_evidence(prior, updated):
    assert updated['evidence_type'] != 'MANUAL_CURATION', 'unrepaired human evidence'
    assert updated.get('source') == prior.get('source'), 'lost mapping source'


def literal_nonresolving(rec, text):
    candidates = [s for s in rec.get('synonyms', []) if s['synonym_text'] == text]
    assert candidates, ('lost literal alias', text)
    assert all(not is_resolving_synonym(s) for s in candidates), ('alias still resolving', text)


def disallow_active_collision(catalog, owner_path, identifier):
    collisions = [path for path, r in catalog.items() if path != owner_path
                  and r.get('mapping_status') != 'REJECTED' and r['identifier'] == identifier]
    assert not collisions, ('changed identity collides', identifier, collisions)


def record_reviewed_admission_failure(proposal, predecessor, hashes, review, failure):
    """Record this exact failed admission; never turn it into a passing gate."""
    assert proposal['proposal_id'] == 'op1201-trypticase-soy-broth'
    assert proposal == review['exact_selected_proposal']
    assert predecessor == review['predecessor_proposal']
    assert proposal['after_capture']['sha256'] == '8a3c82b77cf1d335e2aa67f396cfcbe4c2d68ec6985376951326d6b640847879'
    assert predecessor['after_capture']['sha256'] == 'cbc788c1a9ce7cea22a92b4360bad7c113f0e99c2cf5a1ecbbd3a0e79f99aa6c'
    assert review['maintained_admission'] == 'HELD' and review['reviewer'] == '/root/inorganics'
    assert failure == ('changed identity collides', 'MICRO:0000113', ['data/ingredients/mapped/Bacto_Tryptic_Soy_Broth.yaml'])
    assert set(hashes) == set(review['baseline_owner_checks']) == {'data/ingredients/unmapped/Trypticase_Soy_Broth.yaml', 'data/ingredients/mapped/Bacto_Tryptic_Soy_Broth.yaml'}
    for path, bound in review['baseline_owner_checks'].items():
        assert hashes[path] == bound['current_sha256'] == bound['baseline_sha256']
    return dict(proposal_id=proposal['proposal_id'], gate_status='failed', maintained_admission='HELD',
        failure=list(failure), dependency_id='W08-1227-TSB-OWNER-RECONCILIATION',
        selected_sha256=proposal['after_capture']['sha256'], predecessor_sha256=predecessor['after_capture']['sha256'],
        owner_hashes=hashes, scope='Only bounded grade/evidence correction proceeds to validation. This owner is not admitted; no duplicate winner or general collision exemption is selected.')


def official_exact_term(terms, curie, expected):
    exact = [t for t in terms if t.get('obo_id') == curie]
    assert len(exact) == 1 and exact[0]['label'] == expected and not exact[0].get('is_obsolete'), 'official exact-term mismatch'
    return exact[0]


def complete_preservation_scope(before, receipt):
    assert receipt['status'] == 'PASS' and receipt['failure_count'] == 0
    groups = receipt['groups']
    original = groups['initial_hashed_working_files']
    supplemental = groups['supplemental_ten_baseline_entries']
    assert original['passed'] == original['checks'] == len(before['files'])
    assert supplemental['passed'] == supplemental['checks'] == before['tracked_count'] - len(before['files'])
    for group in groups.values():
        if 'checks' in group:
            assert group['failed'] == 0 and group['passed'] == group['checks'], 'incomplete preservation subgroup'
    assert groups['w05_all_manifest_members']['checks'] > 0


def main():
    validation_root = OUT / 'validation'; validation_root.mkdir(exist_ok=True)
    run_name = sys.argv[1] if len(sys.argv) > 1 else 'attempt-v1'
    assert '/' not in run_name and run_name.startswith('attempt-')
    val = validation_root / run_name
    val.mkdir(exist_ok=False)
    proposals = read(SELECTION / 'proposals.json')['proposals']
    old = {p['proposal_id']: p for p in read(ART / 'successors/issue-1201-v1/proposals.json')['proposals']}
    catalog = {str(p.relative_to(ROOT)): yaml.safe_load(p.read_text()) for p in sorted((ROOT / 'data/ingredients').rglob('*.yaml'))}
    baseline_size = len(catalog)
    baseline_errors = list(map(str, validate_component_partonomy(catalog.values())))
    new_ids, selected, records, receipts, paths = set(), set(), {}, [], []
    inherited_human_evidence, admission_failures = [], []
    admission_review_path = OUT / 'independent-review/final_assembly/trypticase-admission-review-v1.json'
    assert sha(admission_review_path) == '97ba31cd26106faa23642b07692396a972e0147035bb9ab0ea90de479af463cf'
    admission_review = read(admission_review_path)
    client = OntologyClient(); labels = []
    for p in proposals:
        pid = p['proposal_id']; path = checked_capture(p['after_capture'], ART)
        rec = yaml.safe_load(path.read_text()); prior = yaml.safe_load(checked_capture(old[pid]['after_capture'], ART).read_text())
        replay = PRIVATE / 'guarded-replays' / run_name / (pid + '.yaml')
        write_validated_ingredient(rec, replay)
        assert yaml.safe_load(replay.read_text()) == rec
        assert p['owner_path'] not in selected, 'duplicate selected owner'
        selected.add(p['owner_path'])
        if p['kind'] == 'edit_existing_owner':
            assert sha(ROOT / p['owner_path']) == p['before_sha256']
            raw = subprocess.check_output(['git', 'show', BASE + ':' + p['owner_path']])
            assert hashlib.sha256(raw).hexdigest() == p['before_sha256']
            before_record = yaml.safe_load(raw)
            if rec['identifier'] != before_record['identifier']:
                try:
                    disallow_active_collision(catalog, p['owner_path'], rec['identifier'])
                except AssertionError as error:
                    hashes = {path: sha(ROOT / path) for path in admission_review['baseline_owner_checks']}
                    assert prior['identifier'] == rec['identifier'] == 'MICRO:0000113'
                    admission_failures.append(record_reviewed_admission_failure(p, old[pid], hashes, admission_review, error.args[0]))
        else:
            assert p['before_sha256'] is None and not (ROOT / p['owner_path']).exists()
            assert rec['identifier'] not in {r['identifier'] for r in catalog.values()} | new_ids, ('duplicate new identity', pid)
            new_ids.add(rec['identifier'])
            before_record = {}
        for index, evidence in enumerate((rec.get('ontology_mapping') or {}).get('evidence', [])):
            if evidence.get('evidence_type') == 'MANUAL_CURATION':
                assert evidence in (before_record.get('ontology_mapping') or {}).get('evidence', []), ('new human-only evidence remains', pid, index)
                inherited_human_evidence.append(dict(proposal_id=pid, index=index, evidence=evidence,
                    scope='Byte-equivalent inherited mapping evidence; retained, not a fresh human authorship attestation.'))
        # Immutable history is a prefix of a corrected payload's history.
        preserved_history(prior, rec, p['after_capture']['sha256'] != old[pid]['after_capture']['sha256'])
        catalog[p['owner_path']] = rec; records[pid] = rec
        mapping = rec.get('ontology_mapping') or {}
        curie, expected = mapping.get('ontology_id'), mapping.get('ontology_label')
        entry = dict(proposal_id=pid, ontology_id=curie, declared_label=expected)
        if curie and curie.split(':')[0] in ['CHEBI', 'FOODON', 'NCIT', 'ENVO']:
            adapter = client._get_adapter(curie.split(':')[0]); actual = adapter.label(curie) if adapter else None
            entry.update(actual_label=actual, status='canonical' if actual == expected else 'unresolved_or_mismatch')
        elif curie and curie.startswith('kgmicrobe.'):
            entry.update(status='registry_self_consistency', identity_matches=curie == rec['identifier'], label_matches=expected == rec['preferred_term'])
            assert entry['identity_matches'] and entry['label_matches'], ('registry label mismatch', pid)
        elif curie and curie.startswith('MICRO:'):
            captures = read(OUT / 'root-primary/retrievals.json')
            capture = next(x for x in captures if x['id'] == curie)
            assert sha(ROOT / capture['path']) == capture['sha256'] and capture['http_status'] == 200
            terms = read(ROOT / capture['path'])['_embedded']['terms']
            exact = official_exact_term(terms, curie, expected)
            entry.update(status='official_OLS_canonical_native_adapter_unavailable', actual_label=exact['label'],
                capture=capture, limitation='Native safe-prefix policy skips the unavailable MICRO adapter. Primary official exact-term bytes validate label only, not source applicability or whole-owner approval.')
        else:
            entry.update(status='native_engine_A_not_applicable', reason='Native safe-prefix policy excludes this namespace; primary capture remains scientific evidence, no invented local adapter.')
        labels.append(entry)
        paths.append(str(path.relative_to(ROOT)))
        receipts.append(dict(proposal_id=pid, owner_path=p['owner_path'], kind=p['kind'], before_sha256=p['before_sha256'], after_sha256=p['after_capture']['sha256'], identifier=rec['identifier']))
    overlay_errors = list(map(str, validate_component_partonomy(catalog.values())))
    triage = read(OUT / 'inputs/coordinator-triage/target-verification-v1.json')
    mapping_corrections = []
    for x in triage['human_evidence_entries']:
        idx = int(x['json_pointer'].split('/')[-1]); rec = records[x['proposal_id']]
        updated = rec['ontology_mapping']['evidence'][idx]
        truthful_mapping_evidence(x['assertion'], updated)
        mapping_corrections.append(dict(proposal_id=x['proposal_id'], pointer=x['json_pointer'], before=x['assertion'], after=updated))
    aliases = []
    for x in triage['alias_checks']:
        text = x['synonym']['synonym_text']; literal_nonresolving(records[x['proposal_id']], text)
        aliases.append(dict(proposal_id=x['proposal_id'], literal=text, status='preserved_nonresolving'))
    completeness = []
    for x in read(OUT / 'inputs/coordinator-triage/completeness-adjudication-refinement.json')['rows']:
        rec = records[x['proposal_id']]; actual = rec['component_assertion']['completeness']; recommendation = x['root_triage_recommendation']
        if recommendation == 'UNKNOWN': assert actual == 'UNKNOWN', x['proposal_id']
        if recommendation == 'COMPLETE_FOR_LITERAL_PRINTED_INPUT_LIST': assert actual == 'COMPLETE', x['proposal_id']
        completeness.append(dict(proposal_id=x['proposal_id'], actual=actual, recommendation=recommendation, scope='Literal source constituent list, not finished molecular composition. Exclusions require separate scientific assessment.'))
    cmd = [sys.executable, 'scripts/validate_strict.py', '--workers', '2', '--out', str(val / 'strict.tsv'), *paths]
    run = subprocess.run(cmd, capture_output=True, text=True)
    (val / 'strict.log').write_text(run.stdout + run.stderr)
    before = read(OUT / 'provenance/predecessor-working-bytes.json')
    mismatches = [r['path'] for r in before['files'] if not (ROOT / r['path']).is_file() or sha(ROOT / r['path']) != r['sha256']]
    preservation_path = OUT / 'independent-review/preservation-final/receipt.json'
    independent_preservation = read(preservation_path)
    complete_preservation_scope(before, independent_preservation)
    assert independent_preservation['predecessor_input']['sha256'] == sha(OUT / 'provenance/predecessor-working-bytes.json')
    for ref in independent_preservation['receipt_files'].values():
        assert sha(ART / ref['path']) == ref['sha256']
    supplemental = independent_preservation['groups']['supplemental_ten_baseline_entries']
    assert supplemental['passed'] == supplemental['checks'] == before['tracked_count'] - len(before['files']) == 10
    assert independent_preservation['groups']['w05_all_manifest_members']['failed'] == 0
    preserved = dict(prior_captured_working_files=len(before['files']), declared_tracked_entries=before['tracked_count'],
        supplemental_git_tree_entries=supplemental['checks'], mismatches=mismatches,
        independent_complete_preservation_receipt=dict(path=str(preservation_path.relative_to(ART)), sha256=sha(preservation_path)),
        qualification='Original15,633 working-byte rows plus ten separately checked b90 tree entries, including exact directory-symlink target bytes. No missing original file is inferred from an omitted capture row.')
    ws = before['w05_sealed_review']; wp = ROOT / ws['root']
    assert sha(wp / 'SEAL.json') == ws['seal_sha256'] and sha(wp / 'MANIFEST.sha256') == ws['manifest_sha256']
    errors = [r for r in labels if r['status'] == 'unresolved_or_mismatch']
    report = dict(at=datetime.now(timezone.utc).isoformat(), validation_command=[sys.executable, str(Path(__file__).resolve()), run_name], proposal_count=len(proposals), guarded_replays=len(receipts), proposals=receipts,
        baseline_record_count=baseline_size, overlay_record_count=len(catalog), baseline_partonomy_violations=baseline_errors,
        overlay_partonomy_violations=overlay_errors, strict_command=cmd, strict_exit_code=run.returncode, labels=labels,
        label_status_counts=dict(Counter(x['status'] for x in labels)), label_errors=errors,
        mapping_evidence_corrections=mapping_corrections, inherited_human_evidence=inherited_human_evidence, aliases=aliases, completeness=completeness,
        owner_admission_status='HELD' if admission_failures else 'not_approved', owner_admission_failures=admission_failures,
        bounded_correction_validation_status='PASS' if not baseline_errors and not overlay_errors and not errors and not mismatches and run.returncode == 0 else 'FAIL',
        preservation=preserved, w05_seals_preserved=True,
        input_hashes={str((SELECTION / n).relative_to(ROOT)): sha(SELECTION / n) for n in ['decisions.json', 'proposals.json', 'evidence.json', 'assembly-provenance.json']},
        scientific_approval=False, release_approval=False)
    (val / 'combined-validation.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['proposals','labels','mapping_evidence_corrections','aliases','completeness','strict_command']}, indent=2))
    assert len(proposals) == 113 and len(mapping_corrections) == 95 and len(admission_failures) == 1
    assert not baseline_errors and not overlay_errors and not errors and not mismatches and run.returncode == 0
    final_receipt = validation_root / 'combined-validation.json'
    assert not final_receipt.exists(), 'immutable successful validation receipt already exists'
    final_receipt.write_bytes((val / 'combined-validation.json').read_bytes())


if __name__ == '__main__':
    main()
