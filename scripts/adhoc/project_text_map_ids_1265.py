#!/usr/bin/env python3
"""#1265, 2026-11-08: change existing text-map addresses, never re-embed text.

Input: frozen published HTML and exact current record paths in migration proof.
Output: identical layout/scientific metadata with numeric IDs and stable URLs,
plus before/after artifact hashes. Legacy slugs are encoded forwards from paths.
"""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))
from mediaingredientmech.identity_projection import git_files, prove_identity_migration  # noqa: E402


def project_html(html: str, records: dict) -> tuple[str, int]:
    index = {}
    for name, record in records.items():
        path = Path(name)
        stem = re.sub(r'[^A-Za-z0-9._-]+', '_', path.stem).strip('_') or 'ingredient'
        url = f'records/ingredient/{path.parent.name}/{stem}.html'
        if url in index:
            raise ValueError('Ambiguous legacy text-map URL')
        index[url] = record['mim_id']
    matches = list(re.finditer(r'const MAP_DATA = (.*);', html))
    if len(matches) != 1:
        raise ValueError('Expected exactly one embedded text-map payload')
    match = matches[0]
    payload = json.loads(match.group(1))
    seen = set()
    for point in payload['points']:
        identifier = index[point['url']]
        if identifier in seen:
            raise ValueError('Duplicate text-map record')
        seen.add(identifier)
        point['id'] = identifier
        point['url'] = 'ingredient/' + identifier.replace(':', '_')
    encoded = json.dumps(payload).replace('</', '<\\/')
    return html[:match.start(1)] + encoded + html[match.end(1):], len(seen)


def main():
    proof = prove_identity_migration(ROOT)
    name = 'docs/text_map.html'
    original = git_files(ROOT, [name])[name]
    path = ROOT / name
    if path.read_bytes() != original:
        raise ValueError('Refusing modified text map')
    updated, count = project_html(original.decode(), proof.transition['new_records'])
    path.write_text(updated)
    receipt = {'issue': 1265, 'path': name, 'points': count,
               'before_sha256': hashlib.sha256(original).hexdigest(),
               'after_sha256': hashlib.sha256(updated.encode()).hexdigest(),
               'coordinates_changed': False, 'scientific_metadata_changed': False}
    (ROOT / 'reports/stable_ids_1265_20261108/text-map-projection.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
