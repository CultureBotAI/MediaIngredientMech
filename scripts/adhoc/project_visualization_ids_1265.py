#!/usr/bin/env python3
"""#1265, 2026-11-08: project frozen layout IDs without recomputing coordinates.

Inputs: Git-baseline visualization arrays and the verified full migration receipt.
Outputs: current visualization arrays with only each node's id changed, plus hashes.
No embeddings, graph layout or scientific metadata is recomputed.
"""
from __future__ import annotations
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))
from mediaingredientmech.identity_projection import git_files, prove_identity_migration  # noqa: E402


def project(nodes: list[dict], aliases: dict[str, str]) -> list[dict]:
    result = deepcopy(nodes)
    seen = set()
    for node in result:
        identifier = aliases[node['id']]
        if identifier in seen:
            raise ValueError('Duplicate projected visualization identity')
        seen.add(identifier)
        node['id'] = identifier
    return result


def main():
    proof = prove_identity_migration(ROOT)
    names = ['docs/data/ingredient_umap.json', 'docs/data/ingredient_graph.json']
    before = git_files(ROOT, names)
    receipt = {'issue': 1265, 'purpose': 'address-only projection of existing layouts', 'artifacts': []}
    for name, raw in before.items():
        current = ROOT / name
        if current.read_bytes() != raw:
            raise ValueError(f'Refusing modified visualization: {name}')
        projected = (json.dumps(project(json.loads(raw), proof.transition['aliases']), indent=2) + '\n').encode()
        receipt['artifacts'].append({'path': name, 'before_sha256': hashlib.sha256(raw).hexdigest(),
            'after_sha256': hashlib.sha256(projected).hexdigest(), 'coordinates_changed': False})
        current.write_bytes(projected)
    path = ROOT / 'reports/stable_ids_1265_20261108/visualization-projection.json'
    path.write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
