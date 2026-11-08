"""Read-only exact-head archive audit; write proof only beside this script."""
import collections
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

OUT = Path(__file__).resolve().parent
ROOT = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/integration/worktree')
REL = Path('reports/unmatched_campaign_operators_1174_20261108/independent-review')
ARC = ROOT / REL
HEAD = '4c8a987da40d48cceeb4390550f1ff7545927a0b'
BASE = 'e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'

def sha(b):
    return hashlib.sha256(b).hexdigest()

def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, check=True).stdout

def save(name, value):
    dest = OUT / name
    with dest.open('x') as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write('\n')
    return {'path': str(dest), 'sha256': sha(dest.read_bytes())}

now = datetime.datetime.now(datetime.timezone.utc).isoformat()
selection_bytes = (ARC / 'SELECTION.json').read_bytes()
selection = json.loads(selection_bytes)
entries = selection['original_to_archive']
groups = collections.defaultdict(list)
mapping_results = []
errors = []
for idx, ent in enumerate(entries):
    rel = ent['archive_relative_path']
    pp = Path(rel)
    if pp.is_absolute() or '..' in pp.parts:
        errors.append({'kind': 'unsafe_archive_path', 'index': idx, 'path': rel})
        continue
    groups[rel].append((idx, ent))
    p = ARC / rel
    observed = p.read_bytes() if p.is_file() else None
    source = Path(ent['source_path'])
    original = source.read_bytes() if source.is_file() else None
    result = {
        'index': idx, **ent, 'archive_exists': observed is not None,
        'archive_sha256': sha(observed) if observed is not None else None,
        'archive_bytes': len(observed) if observed is not None else None,
        'archive_hash_matches': observed is not None and sha(observed) == ent['source_sha256'],
        'archive_size_matches': observed is not None and len(observed) == ent['bytes'],
        'original_exists': original is not None,
        'original_sha256': sha(original) if original is not None else None,
        'original_bytes': len(original) if original is not None else None,
        'original_hash_matches': None if original is None else sha(original) == ent['source_sha256'],
        'original_size_matches': None if original is None else len(original) == ent['bytes'],
    }
    mapping_results.append(result)
    for field in ['archive_hash_matches', 'archive_size_matches', 'original_hash_matches', 'original_size_matches']:
        if result[field] is False:
            errors.append({'kind': field, 'index': idx, 'path': rel})

duplicate_results = []
for rel, members in sorted(groups.items()):
    false_members = [i for i,e in members if e['deduplicated'] is False]
    true_members = [i for i,e in members if e['deduplicated'] is True]
    result = {
        'archive_relative_path': rel, 'mapping_indices': [i for i,e in members],
        'source_paths': [e['source_path'] for i,e in members],
        'member_count': len(members), 'original_flags_false': false_members,
        'deduplicated_flags_true': true_members,
        'consistent_sha256': len({e['source_sha256'] for i,e in members}) == 1,
        'consistent_bytes': len({e['bytes'] for i,e in members}) == 1,
        'one_original_rest_explicit_duplicates': len(false_members) == 1 and len(true_members) == len(members)-1,
    }
    duplicate_results.append(result)
    for field in ['consistent_sha256','consistent_bytes','one_original_rest_explicit_duplicates']:
        if not result[field]: errors.append({'kind': field, 'path': rel})

# os.walk includes hidden and ignored files. Do not follow symlinks.
inventory = []
symlinks = []
for directory, dirs, files in os.walk(ARC, followlinks=False):
    for name in dirs+files:
        p = Path(directory)/name
        if p.is_symlink(): symlinks.append(str(p.relative_to(ARC)))
    for name in files:
        p = Path(directory)/name
        rel = p.relative_to(ARC).as_posix()
        b = p.read_bytes()
        committed = git('show', f'{HEAD}:{(REL/rel).as_posix()}')
        inventory.append({'path': rel, 'bytes': len(b), 'sha256': sha(b),
                          'committed_sha256': sha(committed), 'working_matches_exact_head': b == committed,
                          'selected': rel in groups})
        if b != committed: errors.append({'kind':'working_differs_head','path':rel})

path_suspects = []
private_components = {'.git','.venv','venv','__pycache__','.aws','.codex','.claude','accounts','account','sessions','transcripts'}
credential_patterns = {
    'github_token': r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,})\b',
    'openai_like_token': r'\bsk-[A-Za-z0-9_-]{24,}\b',
    'aws_access_id': r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b',
    'private_key_header': r'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----',
    'chat_runtime_jsonl': r'"(?:session_meta|response_item|event_msg)"\s*[:,]',
}
content_suspects = []
logs = []
for row in inventory:
    rel = row['path']
    parts = set(Path(rel).parts)
    if parts & private_components or Path(rel).suffix.lower() in {'.jsonl','.sqlite','.db','.pyc'}:
        path_suspects.append({'path':rel,'reason':'runtime/account/fixture-git path component or binary database/transcript extension'})
    b=(ARC/rel).read_bytes()
    s=b.decode('utf-8',errors='replace')
    for name,pattern in credential_patterns.items():
        matches=list(re.finditer(pattern,s))
        if matches: content_suspects.append({'path':rel,'rule':name,'match_count':len(matches), 'lines':[s[:m.start()].count('\n')+1 for m in matches]})
    if Path(rel).suffix=='.log':
        logs.append({'path':rel,'bytes':row['bytes'],'sha256':row['sha256'],'text':s})

declared_checks = {
    'source_entries': len(entries) == selection['source_entries'],
    'unique_files': len(groups) == selection['unique_files'],
    'unique_bytes': sum((ARC/r).stat().st_size for r in groups) == selection['unique_bytes'],
    'combined_review_sha256': sha((ARC/'independent-v3/COMBINED-REVIEW-v1.json').read_bytes()) == selection['combined_review_sha256'],
}
for key,ok in declared_checks.items():
    if not ok: errors.append({'kind':'declared_count_or_hash_mismatch','field':key})

receipt_paths = [
    'independent-v1/PROVISIONAL-REVIEW-v1.json',
    'independent-v2/source-first-fix-review-v1.json',
    'independent-v3/source-v2-independent-review.json',
    'independent-v3/COMBINED-REVIEW-v1.json',
]
receipt_results = []
for rel in receipt_paths:
    value=json.loads((ARC/rel).read_text())
    references=[]
    if rel.endswith('PROVISIONAL-REVIEW-v1.json'):
        references=value['findings']
    elif rel.endswith('source-v2-independent-review.json'):
        references=[{'path':p,'sha256':v['sha256']} for p,v in value['results'].items()]
    elif rel.endswith('COMBINED-REVIEW-v1.json'):
        references=value['evidence']
    verified=[]
    for ref in references:
        p=ARC/Path(rel).parent/ref['path']
        # Deduplication can relocate an unchanged probe. Resolve via same source directory mapping.
        candidate = p if p.is_file() else None
        resolution='same_archive_directory'
        if candidate is None:
            receipt_entry=next(e for e in entries if e['archive_relative_path']==rel)
            original_ref=(Path(receipt_entry['source_path']).parent/ref['path']).as_posix()
            match=[e for e in entries if e['source_path']==original_ref and e['source_sha256']==ref['sha256']]
            if len(match)==1:
                candidate=ARC/match[0]['archive_relative_path'];resolution='SELECTION_original_to_archive'
        actual=sha(candidate.read_bytes()) if candidate and candidate.is_file() else None
        item={'path':ref['path'],'expected_sha256':ref['sha256'],'resolved_archive_path':str(candidate.relative_to(ARC)) if candidate else None,'resolution':resolution,'actual_sha256':actual,'matches':actual==ref['sha256']}
        verified.append(item)
        if not item['matches']: errors.append({'kind':'receipt_evidence_binding','receipt':rel,'reference':item})
    receipt_results.append({'path':rel,'sha256':sha((ARC/rel).read_bytes()),'references':verified,'receipt':value})

proofs={}
for name,value in [('entry-verification-v1.json',mapping_results),('duplicate-mapping-verification-v1.json',duplicate_results),('ignored-inclusive-inventory-v1.json',inventory),('bounded-log-contents-v1.json',logs),('review-receipts-binding-v1.json',receipt_results)]:
    proofs[name]=save(name,value)
summary={
    'created_at':now,'reviewer':'/root/issue_context','scope':'Read-only archive integrity, provenance, privacy and historical review scope; no scientific or integration approval.',
    'integration_root':str(ROOT),'requested_head':HEAD,'observed_head':git('rev-parse','HEAD').decode().strip(),'base':BASE,
    'git_status_short':git('status','--short').decode(),'selection_sha256':sha(selection_bytes),
    'declared':{k:selection[k] for k in ['source_entries','unique_files','unique_bytes','combined_review_sha256']},
    'observed':{'source_entries':len(entries),'unique_files':len(groups),'archive_files_with_metadata':len(inventory),'selected_bytes':sum((ARC/r).stat().st_size for r in groups),'duplicate_mapping_count':sum(len(v)-1 for v in groups.values()),'duplicate_target_groups':sum(len(v)>1 for v in groups.values()),'original_available':sum(x['original_exists'] for x in mapping_results),'original_unavailable':sum(not x['original_exists'] for x in mapping_results)},
    'declared_checks':declared_checks,'symlinks':symlinks,'unselected_files':[r['path'] for r in inventory if not r['selected']],
    'privacy_scan':{'scope':'Every file from os.walk, including hidden and ignored files; path and credential/runtime-signature scan, plus separately reviewed bounded log contents. Historical absolute provenance paths are not rewritten.','path_suspects':path_suspects,'content_suspects':content_suspects},
    'errors':errors,'proofs':proofs,
    'audit_harness_notes':['Initial README lookup used report root instead of independent-review root and raised FileNotFoundError; corrected read succeeded without integration changes.','An accidental nonexistent shell command after creating the output directory returned127; no integration reads/writes or proof claims depended on it.','The preliminary filename search output was truncated; this audit uses complete os.walk inventory and no exclusion rules.'],
    'limits':['No independent rerun of archived probe programs or full test suite.','Credential/signature scan is bounded and cannot prove absence of every possible secret; file roles and bounded logs require reviewer inspection.','Historical source paths and manifests can reference intentionally excluded private fixtures; reference text is distinguished from copied fixture trees.'],
}
proofs['audit-summary-v1.json']=save('audit-summary-v1.json',summary)
print(json.dumps({k:summary[k] for k in ['observed','declared_checks','errors','privacy_scan','unselected_files']},indent=2))
print(json.dumps({'summary':proofs['audit-summary-v1.json']},indent=2))
