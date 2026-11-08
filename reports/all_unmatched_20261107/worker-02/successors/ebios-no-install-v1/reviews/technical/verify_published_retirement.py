"""Read-only, one-origin published retirement proof; never prepare/apply owners.

Run only AFTER publication with --repo W02 --head ACTUAL_NEW_HEAD. Native source
paths may be supplied explicitly; their exact reviewed bytes are pinned below.
The current root/head and original source bytes are checked, not simulated.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import sys
from datetime import datetime, timezone

BASE = '0c659aa4c121a5b1832bff699c28e30da577ca08'
OID = 'w02::a2-proposal-nbrc1132-asahi-ebios-tablets'
PID = OID.split('::', 1)[1]
PROPOSAL_SHA = '47b497f7e9b2f764683bddb7479a891be28fa772716d84dd127238033fb34587'
PAYLOAD_SHA = '3275012aad49e7d7e353507d106a3a26c8b2313fad80e5e587ade3bec857bc3c'
STATEMENT_SHA = '8ab8cb596290c6ff6657c51daf1a0def7e19e2d3e17f67ca0471b7650901c91c'
CROSSWALK_SHA = '6b247656ec34a5280a7b10ba1dea6a67edfc12fa0aab004cbb2ec9575a650753'
PREFIX = 'reports/all_unmatched_20261107/worker-02/'
LEDGER = PREFIX + 'seven-preparation-types-v1/selected-v3/proposals.json'
LEDGER_SHA = '062a71f90bd78a2161853ea8448e69bcc21b656f212f01747c6d4b81e27f7ae9'
PAYLOAD = PREFIX + 'continuation-1201-v1/a/after/nbrc1132_asahi_ebios_tablets.yaml'
STATEMENT = PREFIX + 'successors/ebios-no-install-v1/source-origin-retirement.json'
CASE = 'CM_NAME:22e6006ce3bb10066c3c593c4736919fa6cd47f8f2d2a5347ffe92535e5237ff'
CASE_SHA = 'f7fc89c056b723c1291bfeb8e1f3b03325086518cef6edede78158b69fe5cd7d'

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def load_runtime(native_root, crosswalk_path, producer_pins):
    native_root = Path(native_root).resolve()
    for name, expected in producer_pins.items():
        if digest((native_root / name).read_bytes()) != expected:
            raise ValueError('reviewed native producer differs: ' + name)
    raw = Path(crosswalk_path).read_bytes()
    if digest(raw) != CROSSWALK_SHA:
        raise ValueError('reviewed crosswalk differs')
    sys.path.insert(0, str(native_root / 'src'))
    from mediaingredientmech.curate import campaign_owner_apply as native
    if Path(native.__file__).resolve() != (native_root / 'src/mediaingredientmech/curate/campaign_owner_apply.py'):
        raise ValueError('unexpected already-loaded native module')
    native._check_loaded_producers()
    spec = importlib.util.spec_from_file_location('ebios_exact_crosswalk', crosswalk_path)
    crosswalk = importlib.util.module_from_spec(spec)
    exec(compile(raw, str(crosswalk_path), 'exec'), crosswalk.__dict__)
    return native, crosswalk

def source_context(repo, head, native, crosswalk):
    """Real full original proposal/payload, with selected publication head explicit."""
    repo = Path(repo).absolute()
    raw = native.FrozenFile.capture(repo / LEDGER).content
    crosswalk.require(digest(raw) == LEDGER_SHA, 'original full proposal ledger drift')
    members = crosswalk.read_json(raw)['proposals']
    proposal, = [p for p in members if p['proposal_id'] == PID]
    crosswalk.require(crosswalk.object_hash(proposal) == PROPOSAL_SHA, 'original proposal drift')
    crosswalk.require(proposal['kind'] == 'new_owner' and proposal['before_sha256'] is None,
                      'original kind/preimage was relabelled')
    origin = {'origin_id': OID, 'worker_slot': 2, 'published_head': head,
              'proposal': proposal, 'proposal_object_sha256': PROPOSAL_SHA,
              'payload_sha256': PAYLOAD_SHA, 'case_hashes': {CASE: CASE_SHA}}
    def ref(path, sha):
        return {'path': path, 'sha256': sha, 'published_path': path}
    binding = {'origin_id': OID, 'proposal_ledger': ref(LEDGER, LEDGER_SHA),
               'payload': ref(PAYLOAD, PAYLOAD_SHA)}
    return origin, binding

def resolution_context(repo, head, crosswalk):
    statement = crosswalk.read_json((Path(repo) / STATEMENT).read_bytes())
    crosswalk.require(digest((Path(repo) / STATEMENT).read_bytes()) == STATEMENT_SHA,
                      'reviewed statement drift')
    # Additional explicit author-level check: native dictionary equality alone
    # admits JSON true/1.0 as version 1. This does not modify the native operator.
    crosswalk.require(type(statement['schema_version']) is int and statement['schema_version'] == 1,
                      'actual statement version is not integer 1')
    capture = {'path': STATEMENT, 'sha256': STATEMENT_SHA, 'published_path': STATEMENT}
    return {'origin_id': OID, 'status': 'retired',
            'evidence_refs': [{'path': STATEMENT, 'sha256': STATEMENT_SHA}],
            'successor_origin_ids': [], 'retirement_reason': statement['reason'],
            'retirement_bridge': {'capture': capture, 'published_head': head}}

def verify(repo, head, native, crosswalk):
    repo = Path(repo).absolute()
    native.commit(head)
    crosswalk.require(head != BASE, 'new retirement metadata cannot be published at original source head')
    crosswalk.require(native.git(repo, 'rev-parse', 'HEAD').decode().strip() == head,
                      'requested publication head is not actual local HEAD')
    native.git(repo, 'merge-base', '--is-ancestor', BASE, head)
    for path, expected in [(LEDGER, LEDGER_SHA), (PAYLOAD, PAYLOAD_SHA)]:
        old = native.git(repo, 'show', BASE + ':' + path)
        new = native.git(repo, 'show', head + ':' + path)
        crosswalk.require(old == new and digest(new) == expected, 'old/new original source bytes differ')
    origin, binding = source_context(repo, head, native, crosswalk)
    resolution = resolution_context(repo, head, crosswalk)
    result = crosswalk.validate_resolution_crosswalk(
        [origin], [resolution], root=repo, origin_bindings=[binding], native_plan=None)
    crosswalk.require(result['origin_count'] == 1 and result['additional_successor_count'] == 0,
                      'unexpected proof universe')
    crosswalk.require(result['applied_origin_count'] == result['native_operation_count'] == 0
                      and result['native_prepare_proof'] is None
                      and result['scientific_approval'] is False
                      and result['application_authorized'] is False, 'proof scope inflated')
    native._check_loaded_producers()
    return {'checked_at': datetime.now(timezone.utc).isoformat(),
            'reviewer_script': 'worker02 /root/research_b; executed_by caller',
            'metadata_publication_head': head, 'original_scientific_source_head': BASE,
            'crosswalk_sha256': CROSSWALK_SHA, 'statement_sha256': STATEMENT_SHA,
            'original_proposal_object_sha256': PROPOSAL_SHA, 'original_payload_sha256': PAYLOAD_SHA,
            'native_result': result, 'full_campaign_prepare': False,
            'scope': 'Actual published single-origin empty-successor retirement only; no owner install, science, routing, or export approval.'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--head', required=True)
    parser.add_argument('--native-root', type=Path)
    parser.add_argument('--crosswalk', type=Path)
    args = parser.parse_args()
    campaign = args.repo.resolve().parents[2]
    native_root = args.native_root or campaign / 'integration/worktree'
    crosswalk_path = args.crosswalk or campaign / 'integration/final-application-accounting-v3/crosswalk.py'
    native, crosswalk = load_runtime(native_root, crosswalk_path, PRODUCER_PINS)
    print(json.dumps(verify(args.repo, args.head, native, crosswalk), indent=2, ensure_ascii=False))

# Exact reviewed producer and ordinary import pins; populated once from the
# independently verified runtime binding receipt, not accepted from caller input.
PRODUCER_PINS = {'src/mediaingredientmech/curate/campaign_owner_apply.py': '4fb9bf0339d4621e56ee4278ae1b68eeadd371d6a7991a4c99ec7ee832670dca', 'scripts/apply_unmatched_campaign_owners.py': 'd68fff3b69e6502bb8adad828019b91e9b664687cdaaf4453159dfb81f16cbdb', 'src/mediaingredientmech/curate/publication_guard.py': 'f6d1e625b3bd2c7e01cd938cb00e77c57bdfc7ffda350b8925ef690c0e4b464b', 'src/mediaingredientmech/curate/apply_receipt.py': '6c7c613a1a9c2211c68b20a2483e99009c34fd908c9bf3b3acbac63eedb72a3f', 'src/mediaingredientmech/validation/write_validated.py': '6763083be385b38dceb911f13dbd9575aea0dc42425204ccc43360f93c0dcbc9', 'src/mediaingredientmech/validation/mapping_change_receipts.py': 'f9f8f4dfa7ca9ea37b8a39da1d22b6173fe63429212735150e4607c99f35407d', 'src/mediaingredientmech/export/reviewed_sssom.py': '2aa3a795d0bd63c99d97883a492bd2654ecd94dd2aa2c000736b76d64b7099f2', 'src/mediaingredientmech/schema/mediaingredientmech.yaml': 'bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012', 'src/mediaingredientmech/schema/mech_shared.yaml': 'c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895', 'MAPPING_SEMANTICS.md': '6b52f2ac48109ddd5d81996a136b19776cab55efa69a5ec832cf716d6885a062', 'uv.lock': 'f5ce4325376797ada321c0ffba1e6050355e3185c0a079d2c731d17480aeca1a', 'src/mediaingredientmech/__init__.py': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', 'src/mediaingredientmech/curate/__init__.py': '92cd8cc6811a0032c32f4d2fab13b0cb500d618d8cf3bc5b477521f99be7248b', 'src/mediaingredientmech/export/__init__.py': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', 'src/mediaingredientmech/validation/__init__.py': '64fb7c891e465775172b9dec11aa6cedef51f4c71c0bc81e3fa72e93daf50caf', 'src/mediaingredientmech/curie.py': '65349560f9f946446e5c81d90b4c42669805459bb814db508b90aeb41610e923', 'src/mediaingredientmech/review_claims.py': 'bf214f5791223ed318b017db7206bc4ba8cf48bc9ce30d80fba5728cc5ca62fd', 'src/mediaingredientmech/sssom_metadata.py': '0c5e08a55ff6845959ec84b1f530f9891e361f1a1b16b9f81b42beafb8a20d66', 'src/mediaingredientmech/synonym_policy.py': 'f57df13c28f2c2dd2abd3bfcb139094410dd0db4be7fdaffa533ba827c8ca069'}

if __name__ == '__main__':
    main()
