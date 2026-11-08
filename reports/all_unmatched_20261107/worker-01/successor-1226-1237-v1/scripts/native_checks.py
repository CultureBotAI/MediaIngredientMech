"""Read-only native schema, partonomy and SSSOM comparison of the 76 selection.

Run with the pinned worker Python and -B. Output must be an exclusive new file.
No maintained surface or producer output is written.
"""
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import datetime

import yaml

W = Path(__file__).resolve().parents[5]
D = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(W / "src"))
from mediaingredientmech.validation.write_validated import validate_ingredient
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.export.reviewed_sssom import _safe_synonyms

# W is an independent Git worktree; derive the shared campaign's parent explicitly.
PRODUCER = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py')


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert not args.output.exists(), args.output
    # A source hash is an input binding, not a scientific approval.
    assert sha(PRODUCER) == '38d59f42953305f6fc51e4fc24dfc59ee1919bfb961595b67a8afe9f8a46a1bc'
    sys.path.insert(0, str(PRODUCER.parent))
    spec = importlib.util.spec_from_file_location('worker01_pinned_sssom', PRODUCER)
    producer = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = producer
    spec.loader.exec_module(producer)
    proposals = json.loads((W / 'reports/all_unmatched_20261107/worker-01/shard/proposals.json').read_text())['proposals']
    base = {str(p.relative_to(W)): yaml.safe_load(p.read_text()) for p in sorted((W / 'data/ingredients').glob('*/*.yaml'))}
    old_overlay = copy.deepcopy(base)
    new_overlay = copy.deepcopy(base)
    traces = []
    failures = []
    for proposal in proposals:
        pid = proposal['proposal_id']
        op = W / 'reports/all_unmatched_20261107/worker-01' / proposal['after_capture']['path']
        np = D / 'payloads' / (pid + '.yaml')
        old = yaml.safe_load(op.read_text())
        new = yaml.safe_load(np.read_text())
        assert sha(op) == proposal['after_capture']['sha256']
        errs = validate_ingredient(new)
        if errs:
            failures.append({'proposal_id': pid, 'schema_errors': [str(x) for x in errs]})
        old_overlay[proposal['owner_path']] = old
        new_overlay[proposal['owner_path']] = new
        # Compare exact same native call context; ownership is assessed separately
        # by the scientific label review. Empty owner index does not grant export.
        path = Path(proposal['owner_path'])
        before = producer._row_from_yaml(path, {}, {}, {}, {}, record=old, owners={})
        after = producer._row_from_yaml(path, {}, {}, {}, {}, record=new, owners={})
        for row in after:
            _safe_synonyms(row, new)
        btrip = [(r['subject_id'], r['predicate_id'], r['object_id']) for r in before]
        atrip = [(r['subject_id'], r['predicate_id'], r['object_id']) for r in after]
        if btrip != atrip:
            failures.append({'proposal_id': pid, 'changed_mapping_triples': [btrip, atrip]})
        traces.append({'proposal_id': pid, 'old_sha256': sha(op), 'new_sha256': sha(np), 'schema_errors': len(errs), 'before_rows': before, 'after_rows': after, 'mapping_triples_unchanged': btrip == atrip})
    partonomy = {}
    for name, records in [('baseline', base), ('predecessor_projection', old_overlay), ('successor_projection', new_overlay)]:
        errors = validate_component_partonomy(records.values())
        partonomy[name] = {'records': len(records), 'violations': [str(e) for e in errors]}
    if partonomy['successor_projection']['violations'] != partonomy['predecessor_projection']['violations']:
        failures.append({'partonomy_changed': True})
    result = {'reviewer': 'Codex /root (worker01), author-independent native technical check of subagent-authored payloads', 'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'result': 'PASS' if not failures else 'FAIL', 'scope': '76 complete isolated proposals; no maintained or canonical writes', 'inputs': [{'path': str(p), 'sha256': sha(p)} for p in [PRODUCER, W/'src/mediaingredientmech/schema/mediaingredientmech.yaml', W/'src/mediaingredientmech/validation/write_validated.py', W/'src/mediaingredientmech/validation/component_partonomy.py', W/'src/mediaingredientmech/synonym_policy.py', W/'src/mediaingredientmech/export/reviewed_sssom.py']], 'partonomy': partonomy, 'proposals': traces, 'failures': failures, 'limitations': ['Partonomy projection tests structure and references, not whether unresolved Se/W preparations may be simultaneously installed.', 'Pinned producer receives empty external residual, label and ownership overrides: tests local predicates and rejected-label filtering, not a canonical build or release.', 'No full repository suite or final branch CI was run by this focused check.'], 'scientific_or_release_approval': False}
    with args.output.open('x') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(json.dumps({'result': result['result'], 'payloads': len(traces), 'partonomy': {k: {'records': v['records'], 'violations': len(v['violations'])} for k,v in partonomy.items()}, 'failures': failures}))
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
