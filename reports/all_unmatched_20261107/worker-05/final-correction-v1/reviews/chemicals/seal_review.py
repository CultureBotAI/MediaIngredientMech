from pathlib import Path
import datetime, hashlib, json

N = Path('.temp/w05-final-correction-v1')
L, B = N / 'review-chemicals', N / 'chemical-supplement-v1'
def read(p): return json.loads(p.read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def obj(x): return hashlib.sha256(json.dumps(x, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()
def dump(p, x):
    assert not p.exists(), p
    p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')

reviewp = L / 'main-review-v2.json'
r = read(reviewp)
assert r['status'] == 'complete' and r['open_findings'] == 0
assert sha(L / 'main-review-v1.json') == '9c46f53b9d4cc8eae9439e381c4b4f94a005c0852ace18331e4d6e1afa13a2a6'
assert sha(L / 'binding-audit-v1.json') == 'eab50c24311edd01461d6728230365ff2b8bcdc4fc9a2695a249e9f5345c0f66'
assert sha(L / 'source-crosscheck/review-v1.json') == 'a5308688c41554fbd781fcf0063de8fdc64ef4efcc5f2e4221881ab0d71e494e'
for p, expected in r['reviewed_inputs'].items(): assert sha(Path(p)) == expected
selected = r['selected_cumulative_inputs']
D, E, P, S = [read(Path(selected[k]['path'])) for k in ['decisions', 'evidence', 'proposals', 'source_conclusions']]
assert len(r['case_reviews']) == len(D) == 67
assert len(r['payload_reviews']) == len(P) == 58
assert len({x['case_id'] for x in r['case_reviews']}) == 67
assert len({x['proposal_id'] for x in r['payload_reviews']}) == 58
for i, (case, d) in enumerate(zip(r['case_reviews'], D)):
    assert case['case_id'] == d['case_id']
    assert case['selected_decision_object_sha256'] == obj(d)
    assert case['selected_source_conclusion_object_sha256'] == obj(S['case_reviews'][i])
    assert case['source_holds_sha256'] == obj(d['preserved_source_holds'])
    assert case['proposal_ids'] == d['proposal_ids']
    assert case['holds_released'] is False and case['whole_owner_or_export_approval'] is False
for payload, p in zip(r['payload_reviews'], P):
    assert payload['proposal_id'] == p['proposal_id']
    assert payload['selected_proposal_object_sha256'] == obj(p)
    assert payload['after_capture'] == p['after_capture']
    assert payload['whole_payload_read'] is True and payload['holds_released'] is False
inspection = read(L / 'native-inspect-v2.json')
assert len(inspection['targets']) == 58
seal = read(B / 'FINAL-MANIFEST-v2.json')
for row in seal['selected']:
    assert sha(B / row['path']) == row['sha256']
members = seal.get('all_lane_files', [])
for row in members: assert sha(B / row['path']) == row['sha256']
lineage = read(B / 'binding-lineage-disposition-v1.json')
index = read(B / 'current-conclusion-bindings-v1.json')
assert lineage['finding_id'] == 'W05-FINAL-ASSEMBLY-002-BINDINGS'
assert lineage['binding_index']['sha256'] == sha(B / 'current-conclusion-bindings-v1.json')
assert len(index['bindings']) == 67
for i, x in enumerate(index['bindings']): assert x['current_decision_object_sha256'] == obj(D[i])
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
receipt = {'reviewer': '/root/materials_research', 'at': now, 'status': 'PASS', 'scope': 'Final readback of the completed chemical scientific review and exact successor input bindings. This is not a second scientific authorship claim or whole-owner approval.', 'review': {'path': str(reviewp), 'sha256': sha(reviewp)}, 'selected_cumulative_inputs': selected, 'counts': {'cases': 67, 'payloads': 58, 'evidence_entries': len(E), 'native_inspected_targets': 58}, 'all_case_and_payload_object_hashes_recomputed': True, 'all_holds_preserved': True, 'immutable_v1_review_audit_and_child_receipt_verified': True, 'final_author_seal': {'path': str(B / 'FINAL-MANIFEST-v2.json'), 'sha256': sha(B / 'FINAL-MANIFEST-v2.json'), 'manifest_member_hashes_verified': len(members)}, 'binding_lineage_finding': {'finding_id': lineage['finding_id'], 'path': str(B / 'binding-lineage-disposition-v1.json'), 'sha256': sha(B / 'binding-lineage-disposition-v1.json'), 'disposition': 'Additive binding index independently verified. All 67 current canonical hashes match the final selected decisions. The three historical hashes and two alternate serialization hashes remain explicitly historical; no scientific prose was rewritten.'}, 'reviewer_prose_remediation': {'CHEM-004': 'Payload review 53 now correctly states twelve DSMZ routes, eleven flat plus DSMZ 212a.', 'CHEM-005': 'Payload review 44 and FILED-1238 now correctly distinguish stored NARROW_MATCH from native skos:broadMatch.', 'independent_assembly_check': 'Assigned separately by root; this receipt does not claim its completion.'}, 'limits': r['limits']}
dump(L / 'final-readback-v1.json', receipt)
handoff = L / 'HANDOFF.md'
assert not handoff.exists()
handoff.write_text('Independent chemical review is complete for all 67 assigned chemical/prior-root cases and 58 exact candidate payloads. The selected review is `main-review-v2.json`; `binding-audit-v2.json` and `final-readback-v1.json` bind the current cumulative decisions, proposals, evidence and source conclusions.\n\nThe monohydrate completeness finding now has one bounded source-defined material for six NBRC occurrences. No CAS, structure, chloride stoichiometry, supplier or parent relationship was invented. Six initial skeptical findings remain immutable, including two corrected reviewer prose defects and the supplement enum defect. Root metadata amendments and the explicit historical/serialization hash index were rechecked.\n\nThe reviewer is `/root/materials_research`, independent of the chemical primary author. The child `/root/materials_research/chemical_primary_crosscheck` checked 28 cases, 16 payload field sets and 48 source captures; its exact receipt and actual scope are retained. The parent read all complete candidate payloads and made the final adjudications. The separate materials lane authored by the parent receives no approval here.\n\nCompletion releases no source, export, role, legacy mapping, cross-shard or owner-installation hold. HEPES, Wolfe and nominal ethanol candidates remain conditional family choices. Full integrated native publication and the independent final assembly check belong to the coordinator. No maintained data, Git, GitHub or export write was performed by this reviewer.\n')
manifest = L / 'FINAL-MANIFEST-v1.json'
files = [{'path': str(p.relative_to(L)), 'sha256': sha(p), 'bytes': p.stat().st_size} for p in sorted(L.rglob('*')) if p.is_file() and p != manifest]
dump(manifest, {'reviewer': '/root/materials_research', 'sealed_at': now, 'selected_review': {'path': 'main-review-v2.json', 'sha256': sha(reviewp)}, 'selected_readback': {'path': 'final-readback-v1.json', 'sha256': sha(L / 'final-readback-v1.json')}, 'scope': {'cases': 67, 'payloads': 58, 'evidence_entries': 528}, 'actual_delegated_scope': r['scope']['delegation'], 'preservation': 'Entire private review tree, including immutable predecessors, six initial findings, actual child scope, scripts, images and failed binding preflight. Manifest excludes only itself.', 'files': files, 'no_source_owner_export_approval': True})
print(json.dumps({'review_sha256': sha(reviewp), 'audit_sha256': sha(L / 'binding-audit-v2.json'), 'readback_sha256': sha(L / 'final-readback-v1.json'), 'manifest_sha256': sha(manifest), 'manifest_members': len(files), 'selected_cumulative_inputs': selected}, indent=2))
