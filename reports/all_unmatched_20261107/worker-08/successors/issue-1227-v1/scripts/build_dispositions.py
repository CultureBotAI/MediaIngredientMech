"""Bind the original twelve finding dispositions to the final reviewed selection.

This is an issue-lineage report, not GitHub mutation or maintained acceptance.
"""
from datetime import datetime, timezone
from pathlib import Path
import copy
import json
import yaml
from assemble import read, sha, checked_capture, SELECTION, SELECTION_CONFIG

ROOT = Path.cwd()
ART = ROOT / 'reports/all_unmatched_20261107/worker-08'
OUT = ART / 'successors/issue-1227-v1'

DISPOSITIONS = {
    'W08-IR-001': 'Individually reclassified all95 newly authored mapping evidence entries in88 payloads, preserving their original source URLs, acquisition times, LLM disclosure and history. Genuine inherited mapping evidence remains unchanged. ComponentEvidenceTypeEnum has a separate meaning and was not blanket-transformed.',
    'W08-IR-002': 'Qualified both JCM403 preparation preferred names and retained all six original raw pointer labels as non-resolving REJECTED_LABEL provenance. All original cases and occurrence routing remain. Neither generic pointer is a global identity alias.',
    'W08-IR-003': 'Completed source-specific component assessments for all32 originally named follow-up payloads. Form-compatible active catalog references and explicitly conditional joint-overlay references are proposed. The exact remaining B12-vitamer, pantothenate-stereochemistry, hydration, nested-stock and source-token facts remain recorded. The new explicit-DL reference finding is separately routed and corrected through exact ontology/registry form scope; no role/export hold or duplicate physical row is treated as a scientific obstacle to representation.',
    'W08-IR-004': 'Proposed promotions of the original JCM403 B12-stock and DuchefaL0230 placeholders, preserving stable filenames, frozen beforeimages and full histories. Compared existing catalog and selected proposals before choosing identities. JCM403 unknown B12 molecular form is not equated to the closest explicitly cyanocobalamin stock. L0230 represents the manufacturer dry product and its listed15 inputs at the stated nominal basis; no unlisted finished-medium ingredients or procurement facts are invented.',
    'W08-IR-005': 'Retained grounded water as a bounded CURATED_INTERPRETATION of NBRC1356 supernatant preparation. The original charged-salt recipe remains provenance; retained salts and their concentrations are unknown. No charged amount becomes a retained-solute concentration.',
    'W08-IR-006': 'Applied the exact34-row source-relative refinement:24 UNKNOWN lists, five COMPLETE literal two-input declarations, and five separately reasoned PARTIAL exclusions. The latter distinguish an omitted pH-adjusting input, YPS receiving preparations and Top-layer treatments. Missing quantities or exact molecular forms alone do not mean missing constituents, and literal COMPLETE does not claim finished molecular composition.',
    'W08-IR-007': 'Preserved supported NBRC1301 nalidixic-acid identity. Actual attempts did not yield readable NBRC1314/TOGO M2023 primary content; the exact occurrence is explicitly source-held and unverified. Every original occurrence remains, and an unread source is not represented as inspected.',
    'W08-IR-008': 'Retained the four literal phosphate strings and their provenance as REJECTED_LABEL: KH2HPO4 and K2HPO on dipotassium phosphate; KH PO and Potassium Phosphate on monopotassium phosphate. Valid anhydrous spelling and1215/1216 repairs remain. No source membership is remapped by typo inference; W03 shared-owner reconciliation remains separate.',
    'W08-IR-009': 'Changed Trypticase-soy-broth lookup grade to SYNONYM_MATCH while preserving its supported identity, canonical label, mixture boundaries and existing holds.',
    'W08-IR-010': 'Bound tetrahydrate properties to the already archived complete Thermo batch7 table and its original acquisition time; all three case backlinks and the proposal point to that claim-specific evidence. Batch6 is retained as historical incomplete support.',
    'W08-IR-011': 'Narrowed Allen case63 remaining requirement to the actual seven-water supplied-form uncertainty or primary correction. The established6g per1L stock recipe and separate5ml receiving dose remain distinguished and are not deferred for repeat research.',
    'W08-IR-012': 'Used exact NCIT:C87433 with CAS_RN_LOOKUP after primary CAS5794-13-8/exact L-hydrate synonym and native term-resolution review. Preserved distinct DL hydrate, original CAS/history and an explicit non-isomeric SMILES limitation; no structure or racemate is inferred. Dependent surfaces are inventoried without maintained edits or implied whole-owner admission.'
}


def main():
    config = read(SELECTION_CONFIG)
    selection = {p['proposal_id']: p for p in read(SELECTION / 'proposals.json')['proposals']}
    decisions = {d['case_id']: d for d in read(SELECTION / 'decisions.json')['decisions']}
    native = yaml.safe_load((OUT / 'inputs/external-review/review.yaml').read_text())
    originals = {f['finding_id']: f for f in native['findings']}
    triage = read(OUT / 'inputs/coordinator-triage/actionable-findings-matrix.json')
    routing = read(OUT / 'acceptance.json')['issue_routing']
    rows = []
    for f in triage['findings']:
        fid = f['finding_id']
        assert f['severity'] == originals[fid]['severity']
        peers = []
        for g in config['groups']:
            if set(f['proposal_ids']) & set(g['proposal_ids']) or set(f['related_case_ids']) & set(g['case_ids']):
                receipt = read(checked_capture(g['peer_capture'], ART))
                assert receipt['open_blocking_findings'] == [] and receipt['full_payload_review'] is True
                peers.append(g['peer_capture'])
        assert peers
        rows.append(dict(finding_id=fid, title=f['title'], severity=f['severity'],
            issue=routing[fid], original_review_id=native['review_id'], original_reviewer=native['reviewer'],
            original_finding=copy.deepcopy(originals[fid]), historical_observations=copy.deepcopy(f['observations']),
            original_triage=copy.deepcopy(f), status='addressed_in_isolated_successor_with_explicit_holds',
            bounded_disposition=DISPOSITIONS[fid], peer_receipts=peers,
            successor_payload_bindings=[selection[p] for p in f['proposal_ids']],
            successor_case_bindings=[dict(case_id=c, source=decisions[c]['source'],
                case_input_sha256=decisions[c]['case_input_sha256'], occurrence_ids=decisions[c]['occurrence_ids'],
                missing_requirement=decisions[c].get('missing_requirement')) for c in f['related_case_ids']],
            maintained_or_release_approval=False, github_issue_closed=False))
    assert len(rows) == 12 and {r['finding_id'] for r in rows} == set(DISPOSITIONS)
    doc = dict(at=datetime.now(timezone.utc).isoformat(), findings=rows,
        original_head='b90a2fd4681d20e2586481b7b9b1114a78281b94',
        original_findings_sha256=sha(OUT / 'inputs/external-review/findings.json'),
        routing_recorded_before_changes=read(OUT / 'acceptance.json'),
        new_finding_referrals=[dict(path=str(p.relative_to(ART)), sha256=sha(p))
            for p in sorted([*OUT.glob('COORDINATOR-NEW-FINDINGS-v*.json'), OUT / 'COORDINATOR-ASSEMBLY-FINDING-v1.json'])],
        limitations='Only isolated proposal correction is resolved. Coordinator issue filing/disposition and final-head review, scientific source holds, whole-owner admission, roles and cross-shard/release gates remain separate. Issue1173 stays Worker01-specific.')
    path = OUT / 'issue-dispositions.json'
    with path.open('x') as out:
        json.dump(doc, out, indent=2, ensure_ascii=False); out.write('\n')
    print(json.dumps(dict(findings=len(rows), sha256=sha(path))))


if __name__ == '__main__': main()
