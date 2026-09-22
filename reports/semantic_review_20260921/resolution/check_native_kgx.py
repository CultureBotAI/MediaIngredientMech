import csv
import hashlib
import importlib.metadata
import importlib.util
import json
import sys
from pathlib import Path

# Load just the two offline context helpers, not KG-Microbe's transform package.
# These are read-only validation dependencies; no KG-Microbe graph is imported.
kg_root = Path(sys.argv[2]).resolve()
def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, kg_root / relative)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

model = load('kg_microbe.utils.biolink_model', 'kg_microbe/utils/biolink_model.py')
model.prepare_kgx()
context = load('mim_local_context', 'kg_microbe/merge_utils/local_context.py')
from kgx.source.tsv_source import TsvSource

bundle = Path(sys.argv[1])
manifest = json.loads((bundle / 'manifest.json').read_text())
class Owner:
    def log_error(self, **kwargs):
        raise AssertionError(kwargs)
with context.local_prefix_context():
    source = TsvSource(Owner())
    source.set_prefix_map(manifest['curie_map'])
    parsed = list(source.parse(str(bundle / 'mim-kgx.tar.gz'), format='tsv', compression='tar.gz'))
assert all(row is not None for row in parsed)
nodes = {row[0]:row[-1] for row in parsed if len(row) == 2}
edges = {row[-1]['id']:row[-1] for row in parsed if len(row) == 4}
assert len(nodes) == manifest['counts']['nodes']
assert len(edges) == manifest['counts']['edges']
json_cells = 0
for filename, actual in [('mim_nodes.tsv', nodes), ('mim_edges.tsv', edges)]:
    with (bundle / filename).open() as stream:
        for row in csv.DictReader(stream, delimiter='\t', quoting=csv.QUOTE_NONE):
            parsed_row = actual[row['id']]
            for key, value in row.items():
                if key.endswith('_json') and value:
                    assert json.loads(parsed_row[key]) == json.loads(value), (row['id'], key)
                    json_cells += 1
            for key in ('subject', 'predicate', 'object'):
                if key in row:
                    assert row[key] == parsed_row[key]
report = {'result':'passed', 'kgx_version':importlib.metadata.version('kgx'), 'reader':'kgx.source.tsv_source.TsvSource', 'archive_sha256':hashlib.sha256((bundle / 'mim-kgx.tar.gz').read_bytes()).hexdigest(), 'nodes':len(nodes), 'edges':len(edges), 'json_annotations_preserved':json_cells, 'configuration':'Pinned local Biolink model and prefix context; manifest prefix overrides; no remote ontology import', 'limits':'Reader compatibility, endpoints, predicates, and JSON preservation; not strict Biolink schema validation.'}
(bundle / 'native-kgx-reader.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
