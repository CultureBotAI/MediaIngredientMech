from pathlib import Path
import datetime, hashlib, json, re, subprocess, yaml

L = Path(__file__).resolve().parent
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def names(record):
    return [record.get('identifier', ''), record.get('preferred_term', ''), record.get('ontology_mapping', {}).get('ontology_label', '')] + [s.get('synonym_text', '') if isinstance(s, dict) else s for s in record.get('synonyms', [])]
def thiamine(text):
    return bool(re.search(r'thiamin|aneurin', text, re.I))
def monohydrate(text):
    text = re.sub(r'\s+', '', text.lower().replace('₂', '2'))
    return thiamine(text) and ('monohydrat' in text or bool(re.search(r'hcl[·⋅・.x-]*h2o', text)))
checked = []
comparators = []
def check(path, scope, expected=None):
    digest = sha(path)
    if expected:
        assert digest == expected
    record = yaml.safe_load(path.read_text())
    if not isinstance(record, dict):
        return
    checks = {'path': str(path), 'sha256': digest, 'scope': scope}
    checked.append(checks)
    ns = names(record)
    if any(thiamine(n) for n in ns):
        comparators.append({**checks, 'identifier': record.get('identifier'), 'preferred_term': record.get('preferred_term'), 'names': ns, 'monohydrate_name_hits': [n for n in ns if monohydrate(n)]})

for p in sorted(Path('data/ingredients').rglob('*.yaml')):
    check(p, 'maintained owner')
frozen = C / 'preflight/final-intake-candidate-v1/all-active-proposal-entries-v1.json'
for e in json.loads(frozen.read_text())['entries']:
    check(frozen.parent / e['payload_path'], 'frozen active proposal', e['payload_sha256'])
coordinator = C / 'integration/final-same-target-reconciliation-v2/publication-v4/candidate-summary-v4.json'
for e in json.loads(coordinator.read_text())['groups']:
    check(coordinator.parent.parent / e['candidate']['path'], 'pending coordinator union', e['candidate']['sha256'])
# This search includes ignored and hidden YAML files. It is a name-level duplicate
# lead search, not a scientific review of every unrelated record or recipe.
search = subprocess.run(['rg', '--no-ignore', '--hidden', '-l', '-i', '--glob', '*.yaml', 'thiamin|aneurin', '.'], capture_output=True, text=True, check=True)
ignored_paths = sorted(set(search.stdout.splitlines()))
ignored_hits = []
for s in ignored_paths:
    p = Path(s)
    try:
        r = yaml.safe_load(p.read_text())
    except (ValueError, yaml.YAMLError, UnicodeDecodeError):
        continue
    if isinstance(r, dict):
        hits = [n for n in names(r) if monohydrate(n)]
        if hits:
            ignored_hits.append({'path': str(p), 'sha256': sha(p), 'names': hits})
out = {'reviewer': '/root/materials_research', 'at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'inputs': [{'path': str(p), 'sha256': sha(p)} for p in (frozen, coordinator)], 'scope_counts': {s: sum(x['scope'] == s for x in checked) for s in ('maintained owner', 'frozen active proposal', 'pending coordinator union')}, 'checked_payloads': checked, 'thiamine_comparators': comparators, 'selected_monohydrate_name_hits': [x for x in comparators if x['monohydrate_name_hits']], 'ignored_inclusive_search': {'command': 'rg --no-ignore --hidden -l -i --glob *.yaml thiamin|aneurin .', 'matching_paths': ignored_paths, 'monohydrate_owner_name_hits': ignored_hits}, 'limit': 'Name and current owner-scope duplicate check only; no approval of unrelated inherited mappings, chemistry, histories, or pending coordinator unions. A newly authored review supplement may appear among ignored paths and is not a pre-existing owner.'}
p = L / 'monohydrate-owner-check-v1.json'
assert not p.exists()
p.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'path': str(p), 'sha256': sha(p), 'scope_counts': out['scope_counts'], 'selected_monohydrate_name_hits': out['selected_monohydrate_name_hits'], 'ignored_monohydrate_hits': ignored_hits}))
