"""Copy exact stable reviewer/author support into the additive report packet."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys

O = Path(__file__).resolve().parent
W = O.parents[1]
R = W / 'reports/all_unmatched_20261107/worker-02/successors/ebios-no-install-v1'
sys.path.insert(0, str(W / 'src'))
from mediaingredientmech.curate.publication_guard import FrozenFile
from mediaingredientmech.ingredient_bundle_refresh import publish_new_files

sources = {
    'build_metadata.py': 'author/build_metadata.py',
    'author-write-receipt.json': 'author/write-receipt.json',
    'verify_prior_packets.py': 'author/verify_prior_packets.py',
    'prior-packets-before-publication.json': 'author/prior-packets-before-publication.json',
    'root-prepublication-readback.json': 'author/root-prepublication-readback.json',
    'inputs/issue-comment-read-receipt.json': 'author/issue-comment-read-receipt.json',
    'inputs/issue-comment-read-receipt-retry-v1.json': 'author/issue-comment-read-receipt-retry-v1.json',
    'skeptic/context-review-v1.json': 'reviews/skeptic/context-review-v1.json',
    'skeptic/metadata-review-v1.json': 'reviews/skeptic/metadata-review-v1.json',
}
for p in sorted((O / 'lineage').iterdir()):
    assert p.is_file() and not p.is_symlink()
    sources[str(p.relative_to(O))] = 'reviews/lineage/' + p.name

held = [FrozenFile.capture(O / p) for p in sources]
outputs = [(R / target, f.content) for target, f in zip(sources.values(), held)]
for p, raw in outputs:
    p.parent.mkdir(parents=True, exist_ok=True)

def recheck():
    for f in held:
        f.verify()

publish_new_files(outputs, recheck)
receipt = {'at': datetime.now(timezone.utc).isoformat(), 'author': 'Codex worker02 /root',
           'purpose': 'Exact copies only; private original paths in reviews remain their real execution paths.',
           'script_copy_notice': 'Copied scripts preserve original private-root assumptions; execute originals at their documented paths.',
           'copies': [{'source': str(f.path), 'destination': str(p.relative_to(W)),
                       'sha256': hashlib.sha256(raw).hexdigest()}
                      for f, (p, raw) in zip(held, outputs)]}
with (O / 'report-support-copy-receipt-v1.json').open('x') as f:
    json.dump(receipt, f, indent=2); f.write('\n')
print(json.dumps({'copied': len(outputs)}))
