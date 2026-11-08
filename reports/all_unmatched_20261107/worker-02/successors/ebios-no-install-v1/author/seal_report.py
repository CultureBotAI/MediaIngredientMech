"""Seal only the new additive EBIOS report packet before ordinary publication."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import sys

O = Path(__file__).resolve().parent
W = O.parents[1]
R = W / 'reports/all_unmatched_20261107/worker-02/successors/ebios-no-install-v1'
BASE = '0c659aa4c121a5b1832bff699c28e30da577ca08'
sys.path.insert(0, str(W / 'src'))
from mediaingredientmech.curate.publication_guard import FrozenFile
from mediaingredientmech.ingredient_bundle_refresh import publish_new_files

def sha(raw):
    return hashlib.sha256(raw).hexdigest()
def encode(obj):
    return (json.dumps(obj, indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode()
def ref(p):
    return {'path': str(p.relative_to(R)), 'sha256': sha(p.read_bytes())}

assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=W).decode().strip() == BASE
author = json.loads((O / 'author-write-receipt.json').read_text())
for row in author['outputs']:
    assert sha((W / row['path']).read_bytes()) == row['sha256']

copies = {
    'skeptic/native-pair-review-v1.json': 'reviews/skeptic/native-pair-review-v1.json',
    'report-support-copy-receipt-v1.json': 'author/report-support-copy-receipt-v1.json',
    'report-technical-copy-receipt-v1.json': 'author/report-technical-copy-receipt-v1.json',
    'report-native-copy-receipt-v1.json': 'author/report-native-copy-receipt-v1.json',
    'stage_support.py': 'author/stage_support.py',
    'seal_report.py': 'author/seal_report.py',
}
held = [FrozenFile.capture(O / p) for p in copies]
assert sha(held[0].content) == 'e2cedbe979e5a4204aadffea864215402e056cf480cce0df5c3295e4e5caee3b'
outputs = [(R / name, f.content) for name, f in zip(copies.values(), held)]
for p, raw in outputs:
    p.parent.mkdir(parents=True, exist_ok=True)
def check():
    for f in held:
        f.verify()
publish_new_files(outputs, check)

selector = json.loads((R / 'selector.json').read_text())
native = json.loads((R / 'native/native-pair-receipt-v1.json').read_text())
handoff = {
    'schema_version': 1,
    'sealed_at': datetime.now(timezone.utc).isoformat(),
    'author': 'Codex worker02 /root',
    'status': 'REVIEWED_ADDITIVE_REPORT_READY_FOR_ORDINARY_PUBLICATION',
    'publication_base_head': BASE,
    'branch': 'review/all-unmatched-w02-source-review-20261107',
    'change': 'One genuine source_origin_retirement with empty successors; withdraw standalone new-owner installation only.',
    'filed_before_authoring': 'https://github.com/CultureBotAI/MediaIngredientMech/issues/1237#issuecomment-6720520960',
    'retirement': ref(R / 'source-origin-retirement.json'),
    'selector': ref(R / 'selector.json'),
    'source_case_reconciliation': ref(R / 'source-case-reconciliation.json'),
    'origin_id': 'w02::a2-proposal-nbrc1132-asahi-ebios-tablets',
    'origin_proposal_sha256': '47b497f7e9b2f764683bddb7479a891be28fa772716d84dd127238033fb34587',
    'origin_payload_sha256': '3275012aad49e7d7e353507d106a3a26c8b2313fad80e5e587ade3bec857bc3c',
    'original_kind': 'new_owner',
    'original_before_sha256': None,
    'successors': {},
    'full_original_counts_retained': selector['original_counts_retained'],
    'original_full_core_selection': selector['original_full_core_selection'],
    'family_candidate_sha256': 'a5b147248539b039caa788e4d208afdebd24c59b218082a1b5b06f266184f09a',
    'family_review_handoff_sha256': '76a4ba5d9cfcfa93c5150406daecc8b21d05cbd9838fbb50ebe626e65debfe5b',
    'technical_review': ref(R / 'reviews/technical/technical-review-v1.json'),
    'lineage_review': ref(R / 'reviews/lineage/review.json'),
    'skeptical_metadata_review': ref(R / 'reviews/skeptic/metadata-review-v1.json'),
    'skeptical_native_pair_review': ref(R / 'reviews/skeptic/native-pair-review-v1.json'),
    'native_pair': {'yaml': ref(R / 'native/review.yaml'), 'markdown': ref(R / 'native/review.md'),
                    'receipt': ref(R / 'native/native-pair-receipt-v1.json'),
                    'targets': native['targets'], 'inputs': native['inputs'], 'scientific_review': False},
    'validation': {'focused_technical_tests_passed': 31, 'lineage_intake_assertions': 1000,
                   'lineage_final_assertions': 197, 'lineage_negative_controls': 6,
                   'family_native_mismatch_controls': 2,
                   'actual_native_inspect_validate_render_parse_read_current_source': 'PASS',
                   'published_retirement_at_new_head': 'PENDING_ACTUAL_ORDINARY_COMMIT'},
    'frozen_native_proof_runtime': {
        'operator_path': str(O / 'technical/native-repo/src/mediaingredientmech/curate/campaign_owner_apply.py'),
        'operator_sha256': '4fb9bf0339d4621e56ee4278ae1b68eeadd371d6a7991a4c99ec7ee832670dca',
        'crosswalk_path': str(O / 'technical/native/crosswalk.py'),
        'crosswalk_sha256': '6b247656ec34a5280a7b10ba1dea6a67edfc12fa0aab004cbb2ec9575a650753',
        'newer_changing_integration_runtime_attested': False,
        'command': 'PYTHONDONTWRITEBYTECODE=1 <W>/.temp/all-unmatched-worker-02/venv/bin/python -B <O>/technical/verify_published_retirement.py --repo <W> --head <actual-new-head> --native-root <O>/technical/native-repo --crosswalk <O>/technical/native/crosswalk.py',
        'scope': 'One actual published retired origin; zero successors, applications or native owner operations; native_plan=None.'},
    'filed_comparator_observation': {
        'url': 'https://github.com/CultureBotAI/MediaIngredientMech/issues/1247#issuecomment-6720721669',
        'capture': ref(R / 'context/issue1247-comment6720721669.json'),
        'scope': 'Comparator-only bool/float equality limitation, not a demonstrated full crosswalk bypass. Actual statement integer1 valid. No gate fix here.'},
    'held_limits': selector['source_family_lot_role_export_holds'],
    'scientific_review': False,
    'owner_source_role_export_application_approval': False,
    'full_campaign_prepare': False,
    'prior_packets_preserved': ref(R / 'author/prior-packets-before-publication.json'),
    'publication_receipt_location': str(O / 'HANDOFF.json'),
    'publication_note': 'Actual resulting head, ordinary push and remote readback necessarily follow this immutable prepublication packet. They will be recorded in the separate private handoff; no future commit SHA or final published-head approval is fabricated.',
    'final_review_boundary': 'Independent metadata and final native-byte review complete. Separate final staged-file review and coordinator distinct publication review are not relabelled as source-science approval.',
    'copy_provenance': 'Review/native copies keep exact bytes and original private execution paths. Copied nested private manifests are provenance references; complete private members are retained under .temp/ebios-no-install-v1. Only this outer MANIFEST closes the public packet.',
    'scripts': 'Report script snapshots preserve private-root path assumptions. Run their original private counterparts at documented paths. No maintained workflow, code, gate or pin is edited.'
}
publish_new_files([(R / 'HANDOFF.json', encode(handoff))], check)
members = []
for p in sorted(R.rglob('*')):
    if p.is_dir():
        continue
    assert p.is_file() and not p.is_symlink()
    members.append({'path': str(p.relative_to(R)), 'sha256': sha(p.read_bytes()), 'bytes': p.stat().st_size})
manifest = {'schema_version': 1, 'sealed_at': datetime.now(timezone.utc).isoformat(),
            'author': 'Codex worker02 /root', 'immutable_after_seal': True,
            'members': members, 'excluded_self_receipts': ['MANIFEST.json', 'SHA256SUMS'],
            'scope': 'Complete closed report-only packet. All source cores and old reports remain unchanged.'}
manifest_raw = encode(manifest)
checksums = ''.join(f"{row['sha256']}  {row['path']}\n" for row in members)
checksums += f"{sha(manifest_raw)}  MANIFEST.json\n"
publish_new_files([(R / 'MANIFEST.json', manifest_raw), (R / 'SHA256SUMS', checksums.encode())], check)
print(json.dumps({'members': len(members), 'handoff': ref(R / 'HANDOFF.json'),
                  'manifest': ref(R / 'MANIFEST.json'), 'checksums': ref(R / 'SHA256SUMS')}, indent=2))
