"""Compile assessed campaign outcomes into the native owner-review contract.

Run only after final independent review and worker validation. Source-only cases
remain in the campaign contract; this helper creates no fictional MIM owner.
The generated review is an explicit compilation, not a release-status writer.
"""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import yaml

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'MAPPING_SEMANTICS.md').is_file())
OUT = ROOT / 'reports/all_unmatched_20261107/worker-03'
PRIVATE = ROOT / '.temp/all-unmatched-worker-03'
PREFIX = str(OUT.relative_to(ROOT))
now = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')
read = lambda p: json.loads(p.read_text())
write = lambda p, x: p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')


def main():
    decisions = read(OUT / 'decisions.json')['decisions']
    evidence = read(OUT / 'evidence.json')['evidence']
    proposals = read(OUT / 'proposals.json')['proposals']
    assert all(d['independent_review']['status'] == 'complete' for d in decisions)
    assert read(OUT / 'validation/structural-audit-final-v2.json')['structural_accounting'] == 'PASS'
    proposal_validation = read(OUT / 'validation/proposal-validation-final.json')
    assert proposal_validation['status'] == 'PASS'
    assert proposal_validation['input_proposals_sha256'] == hashlib.sha256((OUT / 'proposals.json').read_bytes()).hexdigest()
    assert read(OUT / 'validation/maintained-surface-final.json')['status'] == 'PASS'
    owners = sorted({o['path'] for d in decisions for o in d['owner_records']})
    target_by_path = {p: 'OWNER-' + Path(p).stem for p in owners}
    targets = [{'target_id': target_by_path[p], 'path': p,
                'label': yaml.safe_load((ROOT / p).read_text())['preferred_term'],
                'selector': 'identifier; preferred_term; ontology_mapping; source-linked synonyms and supplied form; applicable inherited holds',
                'record_class': 'IngredientRecord', 'kind': 'maintained',
                'owner_paths': [{'repository': 'CultureBotAI/MediaIngredientMech', 'path': p, 'role': 'Maintained ingredient owner; integration not applied'}]}
               for p in owners]
    selected = [d for d in decisions if d['owner_records']]
    ids = {e for d in selected for e in d['evidence_ids'] + d['independent_review']['evidence_ids']}
    inputs = {f'{PREFIX}/{name}.json' for name in ('decisions', 'evidence', 'proposals', 'agent-scopes')}
    inputs |= {'MAPPING_SEMANTICS.md', 'src/mediaingredientmech/schema/mediaingredientmech.yaml', 'docs/record-reviews.md', 'docs/record-review-profile.md', 'conf/record_review.yaml'}
    for e in evidence:
        if e['evidence_id'] in ids and e['capture']['root'] == 'artifact':
            inputs.add(f"{PREFIX}/{e['capture']['path']}")
    for p in proposals:
        inputs.add(f"{PREFIX}/{p['after_capture']['path']}")
    write(PRIVATE / 'native-targets.json', {'targets': targets})
    command = [sys.executable, 'scripts/record_review.py', 'inspect', '--targets', str(PRIVATE / 'native-targets.json')]
    for path in sorted(inputs):
        command += ['--input', path]
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    (OUT / 'validation/native-inspect.log').write_text(result.stdout + result.stderr)
    assert result.returncode == 0, result.stderr
    inspection = json.loads(result.stdout)
    write(OUT / 'validation/native-inspection.json', inspection)
    selected_targets = list(target_by_path.values())
    native_evidence = []
    mapping = {}
    kinds = {'primary_source': 'primary_source', 'ontology': 'database', 'source_snapshot': 'record_content',
             'native_record_review': 'prior_review', 'independent_review': 'prior_review',
             'unsuccessful_search': 'search', 'local_validation': 'validation'}
    for e in evidence:
        if e['evidence_id'] not in ids:
            continue
        eid = f'EV{len(native_evidence) + 1:04}'
        mapping[e['evidence_id']] = eid
        accessed = e.get('accessed_at') or now()
        accessed = datetime.datetime.fromisoformat(accessed.replace(' UTC', '+00:00')).astimezone(datetime.timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')
        reference = e.get('url') or (f"{PREFIX}/{e['capture']['path']}" if e['capture']['root'] == 'artifact' else 'frozen queue: ' + e['capture']['path'])
        native_evidence.append({'evidence_id': eid, 'kind': kinds[e['kind']], 'reference': reference,
                                'locator': e['locator'], 'accessed_at': accessed,
                                'support': 'context_only' if e['kind'] in {'source_snapshot', 'unsuccessful_search'} else 'partial',
                                'summary': e['supports_or_contradicts'], 'snapshot_sha256': e['capture']['sha256']})
        if e['kind'] == 'unsuccessful_search':
            native_evidence[-1]['search_scope'] = (
                'Bounded captured attempt only: ' + (e.get('url') or 'local capture') +
                '; locator: ' + e['locator'] + '; capture: ' + e['capture']['path'] +
                '. Attempt limitations: ' + e['supports_or_contradicts'] +
                ' This does not establish global absence or extend the actual captured search scope.')
    assessments = []
    for index, d in enumerate(selected, 1):
        assessments.append({'assessment_id': f'CASE{index:03}', 'area': 'identity',
                            'topic': 'Exact source-case applicability and retained owner boundaries',
                            'outcome': 'supported' if d['disposition'] == 'existing_identity_or_alias' and not d['missing_requirement'] else 'concern',
                            'summary': d['reasoning'], 'details': d['applicability'] + '\nNext requirement: ' + str(d['missing_requirement']) + '\nProposal IDs: ' + ', '.join(d['proposal_ids']),
                            'target_ids': [target_by_path[o['path']] for o in d['owner_records']],
                            'evidence_ids': list(dict.fromkeys(mapping[e] for e in d['evidence_ids'] + d['independent_review']['evidence_ids'])),
                            'dimensions': [{'name': 'source_case', 'value': d['case_id'],
                                            'definition': 'One exact frozen assigned source case, not a complete owner or role approval.',
                                            'evidence_ids': [mapping[d['evidence_ids'][0]]]}]})
    findings = []
    actions = []
    issue_owners = {
        'bd211065': 'data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml',
        'molasses': 'data/ingredients/mapped/Sugar_Beet_Molasses.yaml',
        'phb': 'data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml',
        'citrate': 'data/ingredients/mapped/Citric_Acid_X_H2o.yaml',
        'nh4-s4': 'data/ingredients/mapped/Nh42so4.yaml',
    }
    for issue in read(OUT / 'findings-issues.json')['findings']:
        owner = issue_owners.get(issue['finding_id'])
        if not owner:
            continue  # The upstream source-only defect has no invented MIM target.
        assert owner in target_by_path, owner
        related = [d for d in selected if any(o['path'] == owner for o in d['owner_records'])]
        fid = 'F-' + issue['finding_id']
        owned = [{'repository': 'CultureBotAI/MediaIngredientMech', 'path': owner, 'role': 'Maintained owner requiring guarded coordinator integration and full changed-byte review'}]
        findings.append({'finding_id': fid, 'issue_key': 'worker03-' + issue['finding_id'],
                         'category': 'identity', 'severity': 'major', 'status': 'open',
                         'certainty': 'confirmed', 'title': issue['title'],
                         'description': ' '.join(dict.fromkeys(d['reasoning'] for d in related)),
                         'target_ids': [target_by_path[owner]],
                         'evidence_ids': list(dict.fromkeys(mapping[e] for d in related for e in d['evidence_ids'] + d['independent_review']['evidence_ids'])),
                         'rule_id': 'MAPPING_SEMANTICS.md distinct supplied substance and nonresolving incompatible aliases',
                         'owner_paths': owned, 'external_issues': [issue['url']]})
        actions.append({'action_id': 'A-' + issue['finding_id'],
                        'description': 'Integrate the independently reviewed isolated proposal after coordinator conflict reconciliation; retain original before hashes and native holds. See ' + issue['url'],
                        'finding_ids': [fid], 'target_ids': [target_by_path[owner]], 'owner_paths': owned,
                        'acceptance_checks': ['Verify the baseline before hash and all coordinated proposal dependencies before applying guarded writes.',
                                              'Synchronize maintained individual/aggregate/SSSOM surfaces and pass applicable repository data gates.',
                                              'Withdraw inherited support for changed bytes and obtain complete native owner/payload review; satisfy source-specific holds and new-owner admission before exports.']})
    stamp = now()
    review_id = stamp.replace('-', '').replace(':', '') + '-worker03-source-owner-assessment'
    report = {'schema_version': '1.0.0', 'review_id': review_id, 'kind': 'batch',
              'repository': 'CultureBotAI/MediaIngredientMech', 'title': 'Worker03 frozen source applicability to existing MIM owners',
              'started_at': read(OUT / 'acceptance.json')['accepted_at'].replace('+00:00', 'Z'), 'finished_at': stamp,
              'reviewer': {'identity': 'Codex /root; compilation of /root/broths, /root/chemicals and /root/materials primary assessments and separate rotated skeptical reviews',
                           'kind': 'agent', 'independence': 'self_review',
                           'independence_basis': 'This native document is the coordinator compilation. Independent scientific review was performed by a different agent for each complete research batch; exact authors, case scopes, findings, re-review and inspected hashes are in agent-scopes.json and the cited independent captures.'},
              'skill': '.claude/skills/review-sssom-output/SKILL.md', 'completion': 'completed',
              'verdict': 'needs_curation', 'scientific_review': True,
              'summary': f'Assesses source-specific mapping applicability for {len(selected)} assigned cases referring to {len(owners)} actual frozen owner files. Proposals remain isolated and all inherited publication obligations remain explicit. No whole-record, role, mechanism or export approval.',
              'source': inspection['source'],
              'scope': {'description': 'Only source applicability, supplied form, candidate aliases and mapping boundaries of identified existing owners.',
                        'selection': 'All actual owner_records references in the final 188-case worker03 decisions; no sample.',
                        'coverage': 'full', 'population_size': len(owners), 'reviewed_target_ids': selected_targets,
                        'exclusions': [{'target': 'Source-only cases and proposed new owners', 'reason': 'No maintained MIM owner exists for these targets. Exact frozen-case science and independent reviews are retained in the campaign contract; no owner is fabricated for this native profile.'},
                                       {'target': 'Roles, mechanisms and publication admission', 'reason': 'Outside source mapping scope; existing negative obligations and fresh changed-byte review remain in force.'}]},
              'targets': targets,
              'checks': [{'check_id': 'SOURCE_INSPECT', 'name': 'Native owner and context byte inspection', 'status': 'passed', 'required': True,
                          'summary': f'Native inspect captured {len(inspection["source"]["inputs"])} actual inputs at the unchanged assigned base; see retained native-inspection.json.',
                          'target_ids': selected_targets, 'command': 'scripts/record_review.py inspect --targets .temp/all-unmatched-worker-03/native-targets.json with exact context inputs retained in native-inspection.json', 'exit_code': 0},
                         {'check_id': 'CAMPAIGN_GATES', 'name': 'Whole-shard accounting and isolated proposal checks', 'status': 'passed', 'required': True,
                          'summary': 'Actual whole-shard structural audit, closed-schema/partonomy/collision validation, and preserved-surface verification passed; logs are retained in the worker validation directory. These checks do not confer scientific release approval.',
                          'target_ids': selected_targets, 'exit_code': 0}],
              'evidence': native_evidence, 'assessments': assessments, 'findings': findings, 'actions': actions,
              'limitations': ['This is a compilation of source mapping assessments and their independent reviews, not an independent final owner release assessment.',
                              'needs_curation records proposed changes and unresolved source-specific evidence requirements; no inherited WITHHOLD or REJECTED obligation is cleared.',
                              'Frozen source-root captures remain referenced by exact hash in the campaign evidence contract and validated by its whole-shard auditor. Native source inspection additionally binds actual owner bytes and local campaign/primary captures.',
                              'No maintained ingredient, aggregate, SSSOM, unified mapping, semantic selector or downstream KG product was changed. Integration and full native exports belong to the coordinator.'],
              'links': ['https://github.com/CultureBotAI/MediaIngredientMech/pull/1158', 'https://github.com/CultureBotAI/MediaIngredientMech/issues/1165']}
    write(PRIVATE / 'native-review.json', report)
    write(OUT / 'native-review-scope.json', {'owner_paths': owners, 'case_ids_with_owners': [d['case_id'] for d in selected],
                                          'source_only_case_ids': [d['case_id'] for d in decisions if not d['owner_records']],
                                          'source_only_reason': report['scope']['exclusions'][0]['reason'], 'review_id': review_id})
    print(json.dumps({'review_id': review_id, 'owners': len(owners), 'case_assessments': len(selected)}))


if __name__ == '__main__':
    main()
