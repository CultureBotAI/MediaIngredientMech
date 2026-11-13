"""2026-11-12: read-only capture of actual candidate ChEBI target facts.

Purpose: preserve reproducible database evidence for scientific reassessment.
Inputs: frozen ROWS.json and existing local OAK ChEBI SQLite database (mode=ro).
Outputs: selected targets, direct statements, annotation statements, prefixes,
ontology version metadata, database/selection/script hashes, exact query receipt.
This does not validate, curate, approve, or modify native products or the database.
Database facts alone do not establish source-material identity or approve a row.
"""
import datetime as dt
import hashlib
import json
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parent
DEST = ROOT / 'chebi-database-capture-v1'
DB = Path('/Users/marcin/.data/oaklib/chebi.db')
ROWS = ROOT / 'ROWS.json'

def digest(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda: f.read(8 * 1024 * 1024), b''):
            h.update(b)
    return h.hexdigest()

def save(name, value):
    p = DEST / name
    with p.open('x') as f:
        json.dump(value, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write('\n')
    return {'path': str(p), 'sha256': digest(p), 'bytes': p.stat().st_size}

started = dt.datetime.now(dt.timezone.utc).isoformat()
DEST.mkdir(exist_ok=False)
before = DB.stat()
wal = Path(str(DB) + '-wal')
if wal.exists():
    raise RuntimeError('Database has WAL; this bounded immutable capture stops.')
db_hash = digest(DB)
rows = json.loads(ROWS.read_text())
targets = sorted({r['proposed_row']['object_id'] for r in rows
                  if r.get('proposed_row') and r['proposed_row']['object_id'].startswith('CHEBI:')})
connection = sqlite3.connect(DB.as_uri() + '?mode=ro', uri=True)
connection.row_factory = sqlite3.Row
statement_query = 'SELECT * FROM statements WHERE subject = ? ORDER BY predicate, object, value, datatype, language, graph, stanza'
annotation_subject_query = "SELECT DISTINCT subject FROM statements WHERE predicate='owl:annotatedSource' AND object=? ORDER BY subject"
facts = {}
for target in targets:
    direct = [dict(x) for x in connection.execute(statement_query, (target,))]
    annotation_ids = [x[0] for x in connection.execute(annotation_subject_query, (target,))]
    annotations = {annotation_id: [dict(x) for x in connection.execute(statement_query, (annotation_id,))]
                   for annotation_id in annotation_ids}
    facts[target] = {'statements': direct, 'annotations': annotations}
metadata_query = "SELECT * FROM statements WHERE subject='obo:chebi.owl' ORDER BY predicate, object, value"
metadata = [dict(x) for x in connection.execute(metadata_query)]
prefixes = [dict(x) for x in connection.execute('SELECT * FROM prefix')]
connection.close()
after_hash = digest(DB)
after = DB.stat()
if (before.st_size, before.st_mtime_ns, db_hash) != (after.st_size, after.st_mtime_ns, after_hash) or wal.exists():
    raise RuntimeError('Database changed during read-only capture; no receipt issued.')
products = {name: save(name, value) for name, value in (
    ('selected-targets.json', targets), ('facts.json', facts),
    ('ontology-metadata.json', metadata), ('prefixes.json', prefixes))}
receipt = {'kind': 'read-only-official-ontology-database-capture/v1',
           'started_utc': started, 'finished_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
           'source': {'path': str(DB), 'sha256': db_hash, 'bytes': before.st_size,
                      'mtime_ns': before.st_mtime_ns, 'read_only_uri': DB.as_uri() + '?mode=ro',
                      'wal_present_before_or_after': False, 'hash_identical_before_after': True},
           'input': {'path': str(ROWS), 'sha256': digest(ROWS)},
           'script': {'path': str(Path(__file__).resolve()), 'sha256': digest(Path(__file__))},
           'queries': {'direct_statements': statement_query, 'annotation_subjects': annotation_subject_query,
                       'annotation_statements': statement_query, 'metadata': metadata_query,
                       'prefixes': 'SELECT * FROM prefix'},
           'products': products, 'target_count': len(targets),
           'empty_targets': [t for t, v in facts.items() if not v['statements']],
           'limits': ['Local official ChEBI database version is recorded, not claimed current upstream.',
                      'Database statements do not prove the source material has target identity.',
                      'No native approval, generation, or product/owner edits.']}
result = save('RECEIPT.json', receipt)
print(json.dumps({'receipt': result, 'target_count': len(targets), 'empty_targets': receipt['empty_targets'],
                  'database_sha256': db_hash, 'ontology_metadata': metadata}, ensure_ascii=False))
