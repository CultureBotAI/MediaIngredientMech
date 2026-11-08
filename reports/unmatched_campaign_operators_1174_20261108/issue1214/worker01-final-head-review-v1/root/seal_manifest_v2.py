"""Seal private regular files and the retained refused-harness symlink without following it."""
from pathlib import Path
import datetime, hashlib, json, os

OUT = Path.cwd() / '.temp/infrastructure-pr1205-final-head-review-v1'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest_path = OUT / 'MANIFEST.json'
assert not manifest_path.exists()
alias = OUT / 'skeptical/exact-head-package-alias-refused'
assert alias.is_symlink()
failure = OUT / 'root/manifest-sealing-failure-v1.json'
assert not failure.exists()
failure.write_text(json.dumps({
    'at': datetime.datetime.now(datetime.UTC).isoformat(),
    'attempt': 'root/seal_review_v1.py',
    'result': 'Stopped before manifest creation on a retained private harness symlink.',
    'reason': 'The first bundler assumed every private artifact was a regular file. The independent reviewer intentionally retained the refused symlink-package setup as failed-probe evidence.',
    'scope': 'Private packaging assumption only; no target PR/archive defect, source edit, lost evidence or change to REVIEW.json/REVIEW.md.',
    'successor': 'root/seal_manifest_v2.py records the link target bytes separately and does not traverse it.',
    'alias': str(alias.relative_to(OUT)), 'target': os.readlink(alias),
}, indent=2) + '\n')
files=[]
symlinks=[]
for p in sorted(OUT.rglob('*')):
    if p.is_symlink():
        target=os.readlink(p)
        symlinks.append({'path':str(p.relative_to(OUT)), 'target':target,
                         'target_sha256':hashlib.sha256(os.fsencode(target)).hexdigest(),
                         'interpretation':'Retained private refused-harness alias; not an archived PR evidence file and not traversed.'})
    elif p.is_file():
        files.append({'path':str(p.relative_to(OUT)), 'sha256':sha(p), 'bytes':p.stat().st_size})
assert len(symlinks)==1
m={'schema_version':1,'sealed_at':datetime.datetime.now(datetime.UTC).isoformat(),
   'head':'4c8a987da40d48cceeb4390550f1ff7545927a0b',
   'base':'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99',
   'review_sha256':sha(OUT/'REVIEW.json'),
   'scope':'All private review regular files plus the exact target string of the retained refused-harness symlink. Hidden/ignored files included. Symlink targets are not traversed. This manifest excludes itself. No private review files were published to Git or GitHub.',
   'file_count':len(files),'files':files,'symlinks':symlinks}
manifest_path.write_text(json.dumps(m,indent=2)+'\n')
for e in files: assert sha(OUT/e['path'])==e['sha256']
print(json.dumps({'review':str(OUT/'REVIEW.json'), 'review_sha256':sha(OUT/'REVIEW.json'),
                  'manifest_sha256':sha(manifest_path),'regular_files':len(files),
                  'retained_private_harness_symlinks':len(symlinks)},indent=2))
