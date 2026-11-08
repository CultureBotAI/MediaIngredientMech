from pathlib import Path
import datetime, hashlib, json, subprocess

L = Path(__file__).resolve().parent
W = Path.cwd()
R = W / 'reports/all_unmatched_20261107/worker-05'
P = R / 'final-correction-v1'
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def obj(x): return hashlib.sha256(json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
def save(name, x):
    p = L / name; assert not p.exists(); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
def copy(name, p):
    dest = L / name; assert not dest.exists(); dest.parent.mkdir(parents=True, exist_ok=True); dest.write_bytes(p.read_bytes())
    return {'path': str(dest.relative_to(W)), 'sha256': sha(dest), 'original_path': str(p.relative_to(W)) if p.is_relative_to(W) else str(p)}
head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
assert head == '5156d92bec6bd885ca8bae3c5e18bfdce0069176'
allD = json.loads((P / 'core/decisions.json').read_text())['decisions']
allE = json.loads((P / 'core/evidence.json').read_text())['evidence']
allP = json.loads((P / 'core/proposals.json').read_text())['proposals']
proposal = next(p for p in allP if p['proposal_id'] == 'W05-FINAL-MAT-007')
ds = [d for d in allD if d['case_id'] in proposal['case_ids']]
assert [d['case_index'] for d in ds] == [11, 20, 70, 118, 120]
assert ds[2]['case_id'] == 'CM_NAME:8ba1df295abb60b7fb8cd7e12f80b861e3d2e7634dd64e3bfb7e88df0db0fd08'
raw = json.loads((C / 'shards/shard-05.json').read_text())['cases']
cases = [x for x in raw if x['case_id'] in proposal['case_ids']]
save('inputs/decisions.json', ds); save('inputs/proposal.json', proposal); save('inputs/raw-cases.json', cases)
eids = set(proposal['evidence_ids']) | {eid for d in ds for eid in d['evidence_ids']}
es = [e for e in allE if e['evidence_id'] in eids]
save('inputs/evidence-reused.json', es)
capture_index = []
for e in es:
    c = e['capture']; p = (C if c['root'] == 'source' else R) / c['path']
    assert sha(p) == c['sha256'], e['evidence_id']
    capture_index.append({'evidence_id': e['evidence_id'], 'original_capture': c, 'resolved_path': str(p), 'original_url': e.get('url'), 'original_accessed_at': e.get('accessed_at'), 'hash_verified': True, 'read_scope': 'Capture integrity only here; actual reading and applicability are recorded in the primary assessment.'})
before = W / proposal['owner_path']; predecessor = R / proposal['after_capture']['path']
assert sha(before) == proposal['before_sha256']
assert sha(predecessor) == proposal['after_capture']['sha256']
copies = [copy('inputs/maintained-before.yaml', before), copy('inputs/predecessor.yaml', predecessor)]
copies.append(copy('inputs/bsa-comment.json', L.parent / 'issues/bsa-comment.json'))
bsk = next(e for e in es if e['evidence_id'] == 'MATERIALS-CAP-776733f8ca9ff0a9')
copies.append(copy('captures/TOGO_M194-original.json', R / bsk['capture']['path']))
save('inputs/capture-index.json', capture_index)
contracts = ['MAPPING_SEMANTICS.md', '.claude/skills/curate-yaml-record/SKILL.md', '.claude/skills/add-media/SKILL.md', 'docs/record-reviews.md', 'docs/record-review-profile.md', 'src/mediaingredientmech/schema/mediaingredientmech.yaml', 'src/mediaingredientmech/validation/write_validated.py', 'src/mediaingredientmech/curate/curation_event.py']
save('preflight.json', {'author': '/root/materials_research', 'started_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'head': head, 'scope': {'proposal_id': proposal['proposal_id'], 'case_ids': proposal['case_ids'], 'case_indices': [d['case_index'] for d in ds], 'changed_scientific_case_index': 70, 'finding_id': 'W06-TU-004'}, 'read_contracts': [{'path': p, 'sha256': sha(W / p)} for p in contracts], 'source_inputs': [{'path': str(p.relative_to(W)), 'sha256': sha(p)} for p in [P / 'core/decisions.json', P / 'core/proposals.json', P / 'core/evidence.json']], 'copies': copies, 'limits': ['All five linked decisions and the whole selected BSA payload are in review scope; only the BSK supplied-form context is authorized for scientific correction.', 'The original 1537 evidence objects and complete sealed publication remain unchanged.', 'No coordinator union, JCM220/MediaDive3888 quantity, A7030 inherited claim, role or export is approved.']})
save('native-targets-before.json', {'targets': [{'target_id': 'W05-POSTSEAL-BSA', 'path': str(predecessor.relative_to(W)), 'kind': 'source', 'record_class': 'Ingredient', 'label': 'bovine serum albumin', 'selector': 'Complete selected proposal W05-FINAL-MAT-007; bounded supplied_form[5].notes correction', 'ownership_note': 'Maintained owner data/ingredients/mapped/Bovine_Serum_Albumin.yaml; isolated report-only successor, no maintained application.'}]})
print(json.dumps({'head': head, 'cases': len(ds), 'evidence_reused': len(es), 'original_total_evidence': len(allE), 'predecessor_sha256': sha(predecessor), 'before_sha256': sha(before)}))
