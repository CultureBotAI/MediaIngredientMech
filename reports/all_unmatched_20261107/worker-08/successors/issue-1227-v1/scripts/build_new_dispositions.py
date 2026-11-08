"""Bind new routed findings to independently reviewed immutable corrections."""
from datetime import datetime, timezone
from pathlib import Path
import json
import yaml
from assemble import read, sha, checked_capture, SELECTION, SELECTION_CONFIG

ROOT = Path.cwd()
ART = ROOT / 'reports/all_unmatched_20261107/worker-08'
OUT = ART / 'successors/issue-1227-v1'


def main():
    config = read(SELECTION_CONFIG)
    selected = {p['proposal_id']: p for p in read(SELECTION / 'proposals.json')['proposals']}
    for pid, index, expected in [('vm-prop-new-29', 9, 'CHEBI:748116'), ('vm-prop-new-98', 5, 'cas:116-53-0')]:
        record = yaml.safe_load(checked_capture(selected[pid]['after_capture'], ART).read_text())
        part = record['components'][index]
        assert part['component_id'] == expected and part['reference_scope'] == 'EXTERNAL_TERM'
    evidence_id = 'vm1227-v2-dl-ontology'
    old_entry = next(e for e in read(OUT / 'evidence.json')['evidence'] if e['evidence_id'] == evidence_id)
    new_entry = next(e for e in read(SELECTION / 'evidence.json')['evidence'] if e['evidence_id'] == evidence_id)
    assert old_entry['kind'] == 'ontology' and new_entry == dict(old_entry, kind='local_validation')
    specs = [
        ('OP1227-REF-001', 'minor', 'minor', 1227, 'Soy-flour lookup grade exceeded the actual synonym method', ['op-soy-flour-alias'], 'COORDINATOR-NEW-FINDINGS-v1.json',
         'The exact primary and native synonym lookup supports SYNONYM_MATCH, retaining identity, source aliases and historical holds.'),
        ('OP1227-REF-002', 'minor', 'minor', 1201, 'Definition-level R2A pyruvate reference was left as pending work', ['op1201-r2a-medium'], 'COORDINATOR-NEW-FINDINGS-v1.json',
         'The named definition-level anion is linked to active CHEBI:15361. No sodium counterion, supplied salt, amount or closed complete recipe is inferred.'),
        ('OP1227-REF-003', 'minor', 'minor', 1227, 'Plain-flour applicability misstated the frozen amount', ['op1201-plain-flour'], 'COORDINATOR-NEW-FINDINGS-v1.json',
         'Applicability now states the exact frozen4g and derived g_l4, retaining the original source row and material scope.'),
        ('IF-OP1227-F1', 'P2', 'minor', 1227, 'R2A definition-derived parts used a label-enumeration method', ['op1201-r2a-medium'], 'COORDINATOR-NEW-FINDINGS-v2.json',
         'The complete v3 payload was re-reviewed with CURATED_INTERPRETATION and explicit agent rationale. Six components, amounts, identifiers and UNKNOWN closure remain. RawP2 is retained; normalized minor reflects provenance-method mismatch rather than a refuted constituent.'),
        ('VM1227-PEER-001', 'P2', 'major', 1201, 'Two explicit-DL component references used broader ontology identities', ['vm-prop-new-29','vm-prop-new-98'], 'COORDINATOR-NEW-FINDINGS-v3.json',
         'Immutable successor replaces the two overly broad component bindings with EXTERNAL_TERM scope: exact racemate CHEBI:748116 takes section3 priority for DL-alpha-lipoic acid, while cas:116-53-0 preserves supported DL-2-methylbutyric acid. Positive ontology racemate classification, literal DL synonyms and primary chemical-name/CAS evidence support these distinct choices; an unspecified structure is not treated as proof of racemate. Source names, quantities and preparation scope remain; no supplier procurement or duplicate owner is invented. Both complete changed payloads and outcomes are independently re-reviewed. RawP2 is retained; normalized major reflects stereochemical identity scope.'),
        ('W08-1227-ASSEMBLY-001', 'minor', 'minor', 1227, 'Local ontology-query receipt used a web-evidence category without a URL', ['vm-prop-new-29','vm-prop-new-98'], 'COORDINATOR-ASSEMBLY-FINDING-v1.json',
         'Only the local-query evidence entry kind changes from ontology to local_validation; the real null URL, original query time and captured bytes remain exact. Separately inspected official OLS evidence retains its real URL/time. All57 author cases and47 payloads are unchanged, and the metadata successor is independently reviewed. The failed first root assembly and all earlier receipts remain preserved; the auditor is unchanged.')]
    rows = []
    for fid, raw, severity, issue, title, pids, referral_name, disposition in specs:
        group = next(g for g in config['groups'] if set(pids) <= set(g['proposal_ids']))
        peer = read(checked_capture(group['peer_capture'], ART))
        assert peer['full_payload_review'] is True and not peer['open_blocking_findings']
        for pid in pids: assert peer['payload_hashes'][pid] == selected[pid]['after_capture']['sha256']
        referral = OUT / referral_name
        rows.append(dict(finding_id=fid, original_severity=raw, normalized_severity=severity, issue=issue,
            title=title, proposal_ids=pids, status='resolved_in_isolated_exact_successor_after_routing',
            route_before_fix=dict(path=str(referral.relative_to(ART)), sha256=sha(referral)),
            final_payload_bindings=[selected[p] for p in pids], final_peer_receipt=group['peer_capture'],
            bounded_disposition=disposition, github_mutation=False, release_approval=False))
    with (OUT / 'new-finding-dispositions.json').open('x') as out:
        json.dump(dict(at=datetime.now(timezone.utc).isoformat(), findings=rows,
            deduplication='Existing1201/1227 routed classes; coordinator retains GitHub issue disposition. IF-OP1227-F1 and W08-1227-PEER-OP-001 are one finding, not two. Earlier Thauer/pentanoate holds are not new findings.'), out, indent=2)
        out.write('\n')
    print('6 routed new findings bound to exact final payloads and separate peer receipts')


if __name__ == '__main__': main()
