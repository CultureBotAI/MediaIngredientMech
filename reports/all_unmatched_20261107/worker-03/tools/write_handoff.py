"""Write review-only inventories and the coordinator handoff from final artifacts."""
import collections
import csv
import datetime
import hashlib
import json
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'MAPPING_SEMANTICS.md').is_file())
OUT = ROOT / 'reports/all_unmatched_20261107/worker-03'
read = lambda p: json.loads(p.read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
write = lambda p, v: p.write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')


def main():
    decisions = read(OUT / 'decisions.json')['decisions']
    proposals = read(OUT / 'proposals.json')['proposals']
    evidence = read(OUT / 'evidence.json')['evidence']
    scopes = read(OUT / 'agent-scopes.json')
    native = read(OUT / 'native-review-scope.json')
    issues = read(OUT / 'findings-issues.json')
    counts = dict(collections.Counter(d['disposition'] for d in decisions))
    assert all(d['independent_review']['status'] == 'complete' for d in decisions)
    assert read(OUT / 'validation/proposal-validation-final.json')['status'] == 'PASS'
    assert read(OUT / 'validation/maintained-surface-final.json')['status'] == 'PASS'
    with (OUT / 'unresolved-requirements.tsv').open('w') as f:
        writer = csv.writer(f, delimiter='\t', lineterminator='\n')
        writer.writerow(['case_id', 'source', 'raw_source_label', 'missing_requirement', 'evidence_ids', 'issue_refs'])
        for d in decisions:
            if d['disposition'] == 'unresolved':
                writer.writerow([d['case_id'], d['source']['source'], d['source']['raw_source_label'], d['missing_requirement'], '|'.join(d['evidence_ids']), '|'.join(d['issue_refs'])])
    with (OUT / 'proposal-inventory.tsv').open('w') as f:
        writer = csv.writer(f, delimiter='\t', lineterminator='\n')
        writer.writerow(['proposal_id', 'kind', 'owner_path', 'before_sha256', 'after_path', 'after_sha256', 'case_ids', 'independent_reviewer'])
        for p in proposals:
            writer.writerow([p['proposal_id'], p['kind'], p['owner_path'], p['before_sha256'], p['after_capture']['path'], p['after_capture']['sha256'], '|'.join(p['case_ids']), p['independent_review']['reviewer']])
    review_paths = [a['independent_review_capture'] for a in scopes['assignments']]
    hashes = {str(p.relative_to(OUT)): sha(p) for p in [OUT / n for n in ['decisions.json', 'evidence.json', 'proposals.json', 'agent-scopes.json', 'cross-shard-owner-references.json', 'findings-issues.json'] + review_paths]}
    handoff = {
        'schema_version': 1, 'worker_slot': 3,
        'created_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'branch': 'review/all-unmatched-w03-source-review-20261107',
        'assigned_base': 'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99',
        'shard_sha256': '90d5d5df1ae9609c08593c93216d78449f6ac2781f1d5e7e95695751fdd0c228',
        'case_count': len(decisions), 'independently_reviewed_cases': len(decisions),
        'unreviewed_case_ids': [], 'source_case_counts': dict(collections.Counter(d['source']['source'] for d in decisions)),
        'disposition_counts': counts, 'evidence_count': len(evidence), 'proposal_count': len(proposals),
        'proposal_kinds': dict(collections.Counter(p['kind'] for p in proposals)),
        'existing_native_owner_count': len(native['owner_paths']),
        'native_owner_case_count': len(native['case_ids_with_owners']),
        'source_only_case_count': len(native['source_only_case_ids']),
        'native_review_id': native['review_id'], 'native_review_verdict': 'needs_curation',
        'artifact_sha256': hashes,
        'independent_scopes': scopes['assignments'],
        'new_issue_urls': [i['url'] for i in issues['findings']],
        'review_correction_tracker': read(OUT / 'review-correction-tracker.json')['url'],
        'cross_shard': read(OUT / 'cross-shard-owner-references.json'),
        'remaining_requirements': 'Every unresolved case has its own source-specific missing requirement in decisions.json and unresolved-requirements.tsv. Other dispositions can also retain integration, source or native holds.',
        'integration_limits': [
            'No maintained data, canonical SSSOM, unified snapshot, semantic/companion selector, qc-evidence.yaml or lockfile changes.',
            'Do not apply overlapping owner proposals independently; reconcile all exact before hashes, source-case sets, aliases, components and coordinated tombstones.',
            'JCM431 worker01 overlap is explicitly recorded; both complete payloads remain for coordinator reconciliation and neither is selected as winner.',
            'All inherited native/source/downstream holds remain explicit. Mapping evidence does not approve roles, mechanisms or complete owner payloads.',
            'New owners remain subject to native admission issue1165. Guarded integration, synchronized surfaces, fresh whole-payload review and coherent exports belong to coordinator.',
            'No worker PR, merge, downstream rebuild, paid provider or external session was used.'
        ],
        'final_git_receipt': 'The final response and private publication-receipt.json identify the pushed commit and remote readback. This committed handoff cannot contain its own commit SHA.',
    }
    write(OUT / 'HANDOFF.json', handoff)
    rows = '\n'.join(f'| {k} | {v} |' for k, v in sorted(counts.items()))
    agent_rows = '\n'.join(f"| {a['primary_research_agent']} | {a['case_count']} | {a['proposal_count']} | {a['actual_independent_reviewer']} |" for a in scopes['assignments'])
    issue_lines = '\n'.join(f"- [{i['finding_id']}]({i['url']}): {i['title']}" for i in issues['findings'])
    content = f'''# Worker03 frozen source-review handoff

All {len(decisions)} assigned cases received source-context assessment, primary-source research and separate skeptical review. The final bundle contains {len(proposals)} isolated proposals ({handoff['proposal_kinds'].get('new_owner', 0)} new owners and {handoff['proposal_kinds'].get('edit_existing_owner', 0)} existing-owner edits), {len(evidence)} evidence entries, and {counts.get('unresolved', 0)} precisely unresolved outcomes. Reviewed does not mean resolved or approved for release.

Branch: `{handoff['branch']}`. Frozen base: `{handoff['assigned_base']}`. Shard SHA256: `{handoff['shard_sha256']}`. Dependency PR1158 was still open and unmerged at the final live read in `context/pr1158-final.json`; the assignment was not rebased. The final push receipt supplies the exact branch commit without a self-referential commit hash here.

## Case accounting and actual review scopes

| Disposition | Cases |
| --- | ---: |
{rows}

| Primary author | Cases | Proposals | Separate skeptical reviewer |
| --- | ---: | ---: | --- |
{agent_rows}

The three independent captures bind exact case lists, complete author/core hashes, every proposed payload and retained findings/re-review. `agent-scopes.json` records actual scopes. `decisions.json` retains every frozen occurrence and explicit per-case evidence applicability. `unresolved-requirements.tsv` lists the exact remaining scientific requirements. All {len(decisions)} cases are accounted for; no source cases from another shard are claimed.

Primary retrieval was not uniformly successful. The two microbedecoder `sugar` cases (`KG_CASE:33c13b23fafbf9588be9c5570e87b1ec40a840bd1da2c1616a3cd9f3913d1478` and `KG_CASE:4fb6d439270ed94097d3ade71c3f52468c7b915b2bcff39b0fadcbc4b223aa19`) retain their frozen provenance and failed-access evidence. Final publisher retries retrieved the Gardnerella chapter abstract, whose several carbohydrate examples do not identify the extracted generic substrate; its full-text link returned the abstract. Alkaliflexus publisher attempts failed. Neither original full substrate passage was retrieved in this review; both identities remain unresolved. `validation/bergey-supplement-review.json` independently assesses the exact added captures. These bounded failures do not establish global unavailability. Other unsuccessful searches and source-version limitations remain explicit per case; no failed retrieval is used as identity evidence.

## Artifacts and checks

- `decisions.json`, `evidence.json`, `proposals.json`: the structural campaign contract; exact hashes in `HANDOFF.json` and `manifest.sha256`.
- `proposal-inventory.tsv`: intended owner paths, unchanged before hashes and exact after payloads. These are proposals only.
- `validation/structural-audit-final-v2.json`: whole-shard audit including the bounded final Bergey followup; structural validity is not scientific approval.
- `validation/proposal-validation-final.json`: all {len(proposals)} exact payloads pass closed-schema, full-catalog component overlay, new active-identifier collision and history checks. Biological role/causal-graph fields on existing owners are unchanged.
- `validation/final-id-label-coverage.json`: all 28 proposed ontology targets have verified canonical/synonym labels. MICRO uses primary OLS term objects because the local adapter/table is unavailable; NCIT is verified in local semsql. No ontology refresh was run.
- `validation/maintained-surface-final.json`: all 3,060 baseline maintained files and original owner-file membership unchanged; 187 full source recipes and 52 frozen KG owner hashes verified.
- Auditor failure controls: 22 tests passed (`validation/structural-auditor-controls-final.log`). Proposal-wrapper controls: 6 tests passed (`validation/proposal-wrapper-controls-final-v2.log`); only retained dependency deprecation warnings.
- Native formal review: `reviews/structured/{native['review_id']}/review.yaml` and generated `review.md`, created through native inspect/validate/save. It assesses {len(native['case_ids_with_owners'])} cases against {len(native['owner_paths'])} actual existing owners and has verdict `needs_curation`. The {len(native['source_only_case_ids'])} source-only cases stay in the campaign contract; no MIM target was invented.
- Final independent branch review and native check logs are retained in `validation/`; they are separate from the scientific reviewer captures.

The unrestricted `git diff --check` reports whitespace in retained source captures and native-generated Markdown. Those bytes are preserved for provenance and canonical rendering; the authored-artifact check is reported separately. No whitespace rule or repository gate was disabled.

No full maintained-data rebuild gates were invoked because no maintained data were changed. No exports or downstream products were regenerated. The original shared primary-cache manifest was verified as `0a8c6b1d8fd3a60de0b5c269613cf25e30ee94f4ae20aa987679639d603e27d5`; exact reused capture bytes and original timestamps remain with their per-case applicability. Cache integrity grants no case or owner approval.

## Findings and remaining integration

{issue_lines}

Five corrected proposal/review findings are recorded in [{handoff['review_correction_tracker']}]({handoff['review_correction_tracker']}). The JCM431 inherited numbered-pointer miss is tracked under #1173's IR-SHARD-ARTIFACT-9 and #718 with an exact re-review comment, preserving the earlier missed review and proposal bytes. The named Metals44 stock was independently distinguished from the providerless numbered pointer using its source formula and ontology definition.

`cross-shard-owner-references.json` records nine frozen other-shard case references sharing five proposed existing-owner paths, plus the separately observed actual worker01 JCM431 proposal overlap. The JCM431 before hash remains `ad02ea5d31f05ad4f5a71af9718cab059c17a983d01fb0aa101d6b61b8a94549`; the corrected worker03 after hash is `83ffd40a40010e3b5c997565750e523539ebe3bfc9bc5332d42f2f7aef16db1f`. Its bare numbered aliases are provenance-only REJECTED_LABEL. The two workers' full payloads, component grounding and source-case sets still need coordinator reconciliation. This inventory is not a complete cross-shard conflict detector, especially for new-owner or lexical overlaps.

Coordinator next steps: reconcile all overlapping proposals and coordinated PHB tombstones before guarded application; preserve source identities, native/source/downstream holds and the explicit requirements; withdraw inherited support for changed owner bytes; perform complete changed-payload review and the maintained synchronization/export gates. New-owner admission remains constrained by #1165. No mapping review here clears roles, mechanisms, whole-record or publication obligations. No worker PR, merge, downstream rebuild or external session was opened.
'''
    (OUT / 'HANDOFF.md').write_text(content)
    (OUT / 'README.md').write_text('Worker03 completed the assigned 188-case frozen source-review shard. Start with [HANDOFF.md](HANDOFF.md) for counts, actual review scopes, validation, findings and coordinator integration limits. Exact machine-readable state and hashes are in [HANDOFF.json](HANDOFF.json).\n\nThe final root decisions/evidence/proposals are authoritative for this worker handoff. Per-agent author cores intentionally retain their pre-assembly review metadata; their separate hash-bound skeptical reviews are attached in the root artifacts. Superseded drafts and unsuccessful captures are retained as provenance, not active proposals or scientific support. The manifest excludes only itself to avoid self-reference.\n')
    print(json.dumps({k: handoff[k] for k in ['case_count', 'proposal_count', 'evidence_count', 'existing_native_owner_count', 'source_only_case_count']}))


if __name__ == '__main__':
    main()
