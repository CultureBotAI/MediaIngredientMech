"""Independent read-only corpus probe; writes evidence only next to this script."""
import contextlib
import csv
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
from datetime import datetime, timezone

run = Path(__file__).resolve().parent.parent
new_root = run / 'claw-source'
old_root = run / 'claw'
mim = run / 'step1-mim'
cm = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/CultureMech')

def module(root, name):
    spec = importlib.util.spec_from_file_location(name, root / 'scripts/build_unified_ingredient_mapping.py')
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value

new = module(new_root, 'independent_new_builder')
old = module(old_root, 'independent_old_builder')
proposals = json.loads((run / 'step1-independent/proposed-source-holds.json').read_text())['rows']
with contextlib.redirect_stdout(io.StringIO()) as log:
    indexes = new.load_mim_index(mim)
    labels = new.load_mim_label_index(mim)
    live = new.live_records(*indexes)
    old_indexes = old.load_mim_index(mim)
    old_live = old.live_records(*old_indexes)
    occurrences = new.scan_culturemech(cm)
    (run/'step1-independent/claw-source-hold-occurrences.json').write_text(json.dumps(occurrences,indent=2)+'\n')
    old_rejections = old.load_mapping_rejections(mim, old_indexes[0], label_index=labels, live=old_live)
    old_rows = old.build_unified_rows(occurrences, *old_indexes, old_rejections, labels)
    new_without_holds = new.build_unified_rows(occurrences, *indexes, new.load_mapping_rejections(mim, indexes[0], label_index=labels, live=live), labels)
    assert old_rows == new_without_holds, 'Existing ledger behavior changed'
    with tempfile.TemporaryDirectory() as temp:
        temp_root = Path(temp)
        path = temp_root / new.REJECTIONS_PATH
        path.parent.mkdir(parents=True)
        path.write_bytes((mim / new.REJECTIONS_PATH).read_bytes())
        with path.open('a', newline='') as stream:
            writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
            for row in proposals:
                writer.writerow([row['ingredient_name'], row['rejected_id'], '', row['reason']])
        rejections = new.load_mapping_rejections(temp_root, indexes[0], label_index=labels, live=live)
        held_rows = new.build_unified_rows(occurrences, *indexes, rejections, labels)
    old_by_name = {r['ingredient_name']: r for r in old_rows}
    held_by_name = {r['ingredient_name']: r for r in held_rows}
    changed = {name for name in old_by_name if old_by_name[name] != held_by_name[name]}
    assert changed == {r['ingredient_name'] for r in proposals}, changed
    checks = []
    for row in proposals:
        name = row['ingredient_name']
        assert occurrences[name]['term_id'] == row['rejected_id'], (name, occurrences[name])
        anchor = new._anchor_record(name, indexes[0], labels, live)
        assert anchor is None, (name, anchor)
        held = held_by_name[name]
        fields = ('mim_id', 'chebi_id', 'culturemech_term_id', 'cas_rn', 'kg_microbe_node_id', 'synonyms')
        assert not any(held[field] for field in fields), held
        assert held['mapping_status'] == 'UNMAPPED', held
        for field in ('ingredient_name', 'occurrence_count', 'example_media'):
            assert held[field] == old_by_name[name][field], (field, name)
        checks.append({'label': name, 'rejected_id': row['rejected_id'], 'anchor': anchor, 'before': old_by_name[name], 'after': held})
    summary = {
        'checked_at': datetime.now(timezone.utc).isoformat(),
        'source_head': subprocess.check_output(['git','rev-parse','HEAD'],cwd=new_root,text=True).strip(),
        'source_dirty': subprocess.check_output(['git','status','--short'],cwd=new_root,text=True),
        'builder_sha256': hashlib.sha256((new_root/'scripts/build_unified_ingredient_mapping.py').read_bytes()).hexdigest(),
        'old_builder_head': subprocess.check_output(['git','rev-parse','HEAD'],cwd=old_root,text=True).strip(),
        'culturemech_head': subprocess.check_output(['git','rev-parse','HEAD'],cwd=cm,text=True).strip(),
        'legacy_rows_identical': len(old_rows),
        'exact_held_labels_changed': len(changed),
        'held_labels_without_independent_owner': len(checks),
        'held_labels_without_identity_or_borrowed_metadata': len(checks),
        'unrelated_rows_identical': len(old_rows)-len(changed),
        'rows': checks,
    }
(run/'step1-independent/claw-source-hold-corpus.log').write_text(log.getvalue())
(run/'step1-independent/claw-source-hold-corpus.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='rows'},indent=2))
