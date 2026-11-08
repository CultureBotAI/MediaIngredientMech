"""Bounded read-only lookup of proposed ontology IDs in existing KG tables.

This does not regenerate or adopt downstream products and does not replace
primary ontology identity review. Missing tables/IDs remain explicit limitations.
"""
import csv
import datetime
import hashlib
import json
from pathlib import Path
import yaml

root = Path('reports/all_unmatched_20261107/worker-03')
tables = Path('/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe-mim-1788-20261107/data/transformed/ontologies')
requests = {}
for group in ('broths', 'chemicals', 'materials'):
    for proposal in json.loads((root / group / 'proposals.json').read_text())['proposals']:
        record = yaml.safe_load((root / proposal['after_capture']['path']).read_text())
        mapping = record.get('ontology_mapping') or {}
        identifier = mapping.get('ontology_id', '')
        if identifier.split(':')[0] not in {'CHEBI', 'FOODON', 'MICRO', 'NCIT', 'ENVO'}:
            continue
        requests.setdefault(identifier, []).append({'proposal_id': proposal['proposal_id'], 'label': mapping.get('ontology_label')})
results = []
inputs = {}
for prefix in sorted({identifier.split(':')[0] for identifier in requests}):
    path = tables / (prefix.lower() + '_nodes.tsv')
    targets = {identifier for identifier in requests if identifier.startswith(prefix + ':')}
    if not path.is_file():
        results += [{'identifier': identifier, 'status': 'table_unavailable', 'proposals': requests[identifier]} for identifier in sorted(targets)]
        continue
    before = hashlib.sha256(path.read_bytes()).hexdigest()
    found = {}
    with path.open() as stream:
        for line, row in enumerate(csv.DictReader(stream, delimiter='\t'), start=2):
            if row.get('id') in targets:
                found[row['id']] = {'line': line, 'row': row}
    assert hashlib.sha256(path.read_bytes()).hexdigest() == before, path
    inputs[str(path)] = before
    for identifier in sorted(targets):
        result = {'identifier': identifier, 'proposals': requests[identifier], 'table': str(path)}
        if identifier not in found:
            result['status'] = 'not_found_in_this_table'
        else:
            result.update(found[identifier])
            names = {result['row'].get('name', '').casefold()} | {s.casefold() for s in result['row'].get('synonym', '').split('|')}
            result['status'] = 'found'
            result['label_checks'] = [{'proposal_id': request['proposal_id'], 'canonical_or_synonym': str(request['label']).casefold() in names} for request in requests[identifier]]
        results.append(result)
output = {'accessed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'scope': 'Named existing local KG transformed ontology tables only. Additional observational evidence, not a change to frozen queue or downstream products; no general absence claim.',
          'input_sha256': inputs, 'results': results, 'scientific_approval': False}
(root / 'validation/local-ontology-lookup-final.json').write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps({'requested_ids': len(requests), 'limitations_or_label_mismatch': [r for r in results if r['status'] != 'found' or not all(c['canonical_or_synonym'] for c in r['label_checks'])]}, indent=2))
