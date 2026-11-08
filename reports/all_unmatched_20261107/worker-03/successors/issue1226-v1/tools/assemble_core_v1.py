"""Build a new complete report selection from exact reviewed payloads, no owner writes."""
from pathlib import Path
import sys, json, copy, hashlib, csv, datetime

R = next(p for p in Path(__file__).resolve().parents if (p / 'MAPPING_SEMANTICS.md').is_file())
P = R / 'reports/all_unmatched_20261107/worker-03'
OLD = P / 'successors/issue1224-v1/publication-v1'
O = P / 'successors/issue1226-v1'
A = R / '.temp/w03-provenance-successor-v1'
sha = lambda b: hashlib.sha256(b).hexdigest()
canon = lambda x: json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()

def put(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x') as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write('\n')

def cap(path):
    return {'root': 'artifact', 'path': str(path.relative_to(P)), 'sha256': sha(path.read_bytes())}

def cp(src, dst):
    assert src.is_file() and not src.is_symlink()
    dst.parent.mkdir(parents=True, exist_ok=True)
    with dst.open('xb') as f:
        f.write(src.read_bytes())
    assert src.read_bytes() == dst.read_bytes()

if __name__ == '__main__':
    # Arguments are exact completed independent handoffs, archived byte-for-byte first.
    review = Path(sys.argv[1]).resolve(strict=True)
    technical = Path(sys.argv[2]).resolve(strict=True)
    assert review.is_relative_to(O) and technical.is_relative_to(O)
    old_props = json.loads((OLD / 'proposals.json').read_text())
    old_evidence = json.loads((OLD / 'evidence.json').read_text())
    decisions = json.loads((OLD / 'decisions.json').read_text())
    bridge = json.loads((O / 'payload-bridge.json').read_text())
    changes = {r['proposal_id']: r for r in bridge['entries']}
    assert len(changes) == 49 and len(old_props['proposals']) == 74
    cases = sorted({c for r in changes.values() for c in r['original_proposal']['case_ids']})
    assert len(cases) == 68 and len(decisions['decisions']) == 188
    new_props = copy.deepcopy(old_props)
    for p in new_props['proposals']:
        if p['proposal_id'] not in changes:
            continue
        row = changes[p['proposal_id']]
        assert p == row['original_proposal']
        assert sha((P / p['after_capture']['path']).read_bytes()) == row['before_payload_sha256']
        assert sha((R / row['new_payload_path']).read_bytes()) == row['after_payload_sha256']
        p['after_capture'] = row['after_capture']
        p['evidence_ids'] += ['w03-prov-1226-payload-bridge', 'w03-prov-1226-independent-review', 'w03-prov-1246-controls']
        p['independent_review'] = {
            'status': 'complete',
            'evidence_ids': ['w03-prov-1226-independent-review', 'w03-prov-1246-controls'],
            'reviewer': '/root/provenance_review',
            'technical_reviewer': '/root/provenance_controls',
            'primary_author': '/root (codex-worker03)',
            'reviewed_after_sha256': row['after_payload_sha256'],
            'scientific_review': False,
            'review_scope': 'Exact provenance-only successor: full object/parent/beforeimage/authorship binding; one evidence enum replacement and one appended history event; all scientific fields and holds retained. No new science, whole-owner, role or export approval.',
            'historical_review_locator': 'payload-bridge.json entries[proposal_id=' + p['proposal_id'] + '].original_proposal.independent_review',
        }
    new_evidence = copy.deepcopy(old_evidence)
    additions = [
        ('w03-prov-1226-payload-bridge', O/'payload-bridge.json', 'local_validation', 'entries: all 49 exact old/new payload and complete evidence object bindings, parent contexts, authentic beforeimages and original review objects', 'Binds 49 metadata-only successors to their actual prior authorship and payloads; scientific assertions are unchanged.', cases),
        ('w03-prov-1226-independent-review', review, 'independent_review', 'Completed independent provenance review and its exact per-payload/native review bindings', 'Independent review of all 49 enum/history corrections and exclusions, full-value preservation, all 74 selected payloads and source-scope inheritance. No scientific reapproval.', cases),
        ('w03-prov-1246-controls', technical, 'independent_review', 'Independent helper-v2 controls and exact batch/maintained-input review', 'All 36 original controls plus explicit no-native-write/no-output mismatch proof, issue1246 disposition, 49/74 retention and native checks; no science approval.', cases),
        ('w03-prov-1226-retention', O/'scientific-field-retention.json', 'local_validation', 'All 74 proposal rows and three inherited manual evidence objects', '49 exact enum changes plus 49 appended history objects; 25 payloads byte-identical. All other values and prior history objects retained, including Oxoid and all holds.', cases),
        ('w03-prov-1246-repair', O/'context/helper-repair-disposition.json', 'local_validation', 'Issue-first original helper/finding, bounded repair and preserved controls', 'The private helper rejects prepared/source beforeimage mismatch before writing and derives the bridge before hash from the validated source bytes.', cases),
    ]
    for key, path, kind, locator, support, refs in additions:
        new_evidence['evidence'].append({'evidence_id':key,'capture':cap(path),'kind':kind,'locator':locator,'supports_or_contradicts':support,'url':None,'case_ids':refs})
    assert new_evidence['evidence'][:len(old_evidence['evidence'])] == old_evidence['evidence']
    assert len(old_evidence['evidence']) == 863 and len(new_evidence['evidence']) == 868
    cp(OLD/'decisions.json', O/'decisions.json')
    put(O/'proposals.json', new_props)
    put(O/'evidence.json', new_evidence)
    assert (O/'decisions.json').read_bytes() == (OLD/'decisions.json').read_bytes()
    per_proposal = []
    for old, new in zip(old_props['proposals'], new_props['proposals']):
        changed_fields = [k for k in sorted(set(old)|set(new)) if old.get(k) != new.get(k)]
        expected = ['after_capture','evidence_ids','independent_review'] if old['proposal_id'] in changes else []
        assert changed_fields == expected
        per_proposal.append({'proposal_id':old['proposal_id'],'original_proposal_sha256':sha(canon(old)),'successor_proposal_sha256':sha(canon(new)),'changed_fields':changed_fields,'old_payload':old['after_capture'],'new_payload':new['after_capture'],'origin_unchanged':True,'kind':new['kind'],'owner_path':new['owner_path'],'before_sha256':new['before_sha256'],'case_ids':new['case_ids']})
    per_case = [{'case_id':x['case_id'],'case_input_sha256':x['case_input_sha256'],'unchanged_decision_object_sha256':sha(canon(x)),'disposition':x['disposition'],'proposal_ids':x['proposal_ids'],'historical_source_review_retained':True,'all_holds_retained':True} for x in decisions['decisions']]
    put(O/'machine-ledger.json', {'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'predecessor_head':'f6bfbf3c185f705484aa106405f813209146c766','case_count':188,'proposal_count':74,'changed_payload_count':49,'unchanged_payload_count':25,'prior_evidence_count':863,'evidence_count':868,'case_rows':per_case,'proposal_rows':per_proposal,'scope':'Report-only metadata correction. No scientific, role, whole-owner or supported-export reapproval; all historical source decisions, source-specific and native holds retained.'})
    put(O/'validation/complete-preservation.json', {'status':'PASS','all_188_decision_objects_unchanged':True,'entire_decisions_file_byte_identical':True,'decisions_sha256':sha((O/'decisions.json').read_bytes()),'all_863_predecessor_evidence_objects_unchanged':True,'all_25_unmodified_proposal_objects_unchanged':True,'changed_proposal_fields_only':['after_capture','evidence_ids','independent_review'],'49_changed_payload_semantic_differences_only':['ontology_mapping.evidence[0].evidence_type','one curation_history append'],'historical_review_objects_preserved_in_bridge':True,'retired_mixed_rcm_absent_from_active_proposals':not any(x['proposal_id']=='b-proposal-cm0149-form' for x in new_props['proposals']),'scientific_approval':False})
    with (O/'proposal-inventory.tsv').open('x',newline='') as f:
        writer=csv.writer(f,delimiter='\t',lineterminator='\n');writer.writerow(['proposal_id','kind','owner_path','before_sha256','prior_payload_sha256','selected_payload_sha256','metadata_changed'])
        for x in per_proposal:writer.writerow([x['proposal_id'],x['kind'],x['owner_path'],x['before_sha256'] or '',x['old_payload']['sha256'],x['new_payload']['sha256'],bool(x['changed_fields'])])
    cp(Path(__file__), O/'tools'/Path(__file__).name)
    print(json.dumps({'cases':188,'proposals':74,'evidence':868,'changed':49,'unchanged':25,'decision_sha256':sha((O/'decisions.json').read_bytes())},indent=2))
