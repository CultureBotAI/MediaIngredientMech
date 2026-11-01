"""Audit every row/field changed by whole-candidate replacement, without editing it."""
from pathlib import Path
import collections, csv, hashlib, importlib.util, json, sys
import yaml

RUN = Path(__file__).resolve().parent
MIM = RUN / 'mim'
phase = sys.argv[1]
candidate = MIM / f'output/sssom-scientific-audit/{phase}.sssom.tsv'
canonical = (RUN / 'provenance/baseline-canonical.sssom.tsv') if phase == 'baseline' else MIM / 'mappings/ingredient_mappings.sssom.tsv'
review_path = (RUN / 'provenance/baseline-review.json') if phase == 'baseline' else MIM / 'reports/sssom_completion_20260921/review.json'

def read(path):
    return list(csv.DictReader((s for s in path.open() if not s.startswith('#')), delimiter='\t'))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def key(row):
    return row['subject_id'], row['object_id']

left_rows, right_rows = read(canonical), read(candidate)
left, right = {key(r): r for r in left_rows}, {key(r): r for r in right_rows}
assert len(left) == len(left_rows) and len(right) == len(right_rows)
changes, fields, classes = [], collections.Counter(), collections.Counter()
equal = 0
for k in sorted(left.keys() | right.keys()):
    if k not in left:
        changes.append(dict(kind='added', after=right[k])); classes['added'] += 1
    elif k not in right:
        changes.append(dict(kind='removed', before=left[k])); classes['removed'] += 1
    elif left[k] == right[k]:
        equal += 1
    else:
        diff = {f: dict(before=left[k][f], after=right[k][f]) for f in left[k] if left[k][f] != right[k][f]}
        fields.update(diff.keys())
        classes['changed'] += 1
        changes.append(dict(kind='changed', subject_id=k[0], object_id=k[1], fields=diff))

review = json.loads(review_path.read_text())
assert review['source_sha256'] == sha(canonical)
support = collections.Counter()
for d in review['decisions']:
    # Each decision is bound to its source position, full payload and owner bytes.
    pos = int(d['source_position'])
    row = left_rows[pos - 1]
    status = 'byte_equal' if right.get(key(row)) == row else ('missing' if key(row) not in right else 'changed')
    support[d['disposition'] + ':' + status] += 1

spec = importlib.util.spec_from_file_location('native_reconcile', MIM / 'scripts/reconcile_sssom.py')
native = importlib.util.module_from_spec(spec); spec.loader.exec_module(native)
aggregate = yaml.load((MIM / 'data/curated/mapped_ingredients.yaml').read_text(), Loader=yaml.CSafeLoader)
drift = native.find_drift(aggregate, right_rows)
summary = dict(phase=phase, canonical=dict(path=str(canonical),sha256=sha(canonical),rows=len(left_rows)),
               candidate=dict(path=str(candidate),sha256=sha(candidate),rows=len(right_rows)),
               counts=dict(classes), unchanged_rows=equal, changed_fields=dict(fields),
               native_drift={k:len(v) for k,v in drift.items()},
               canonical_review_payload_relation=dict(support),
               promotion_decision='DO_NOT_REPLACE_WHOLE_CANONICAL',
               reason='Native validity does not approve changed row payloads, missing curated rows, or unresolved scientific identity/synonym questions. Only independently evidenced scoped corrections are proposed; content-bound release holds remain.')
out = RUN / 'provenance'
(out / f'{phase}-promotion-summary.json').write_text(json.dumps(summary, indent=2)+'\n')
(out / f'{phase}-promotion-row-delta.json').write_text(json.dumps(changes, indent=2, ensure_ascii=False)+'\n')
(out / f'{phase}-candidate-drift.json').write_text(json.dumps(drift, indent=2, ensure_ascii=False)+'\n')
print(json.dumps(summary, indent=2))
