"""Run the unmodified native B4 rule with the actual read-only KG input directory."""
from pathlib import Path
import datetime
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
MIM = RUN / 'mim'
KG = (RUN.parent.parent / '../../KG-Hub/KG-Microbe/kg-microbe').resolve()
spec = importlib.util.spec_from_file_location('mim_invariants', MIM / 'scripts/validate_sssom_invariants.py')
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
module.KGM_TRANSFORMS_DIR = KG / 'data/transformed/ontologies'
source = MIM / 'mappings/ingredient_mappings.sssom.tsv'
if len(sys.argv) > 1:
    source = Path(sys.argv[1]).resolve()
name = sys.argv[2] if len(sys.argv) > 2 else 'baseline'
prelude, fields, rows = module._read_sssom(source)
prefixes = sorted({row['object_id'].split(':')[0] for row in rows} & module.B4_PREFIXES)
inputs = []
missing = []
for prefix in prefixes:
    p = module.KGM_TRANSFORMS_DIR / f'{prefix.lower()}_nodes.tsv'
    if not p.is_file():
        missing.append(prefix)
        continue
    inputs.append({'path': str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'bytes': p.stat().st_size})
findings = [{'row_number': n, 'row': row, 'reason': reason} for n, row, reason in module.evaluate_rule_b4(rows)]
result = {
    'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'source': {'path': str(source), 'sha256': hashlib.sha256(source.read_bytes()).hexdigest()},
    'native_rule_source': {'path': str(MIM/'scripts/validate_sssom_invariants.py'), 'sha256': hashlib.sha256((MIM/'scripts/validate_sssom_invariants.py').read_bytes()).hexdigest()},
    'execution': 'Imported native module; changed only KGM_TRANSFORMS_DIR to actual read-only KG path; called native _read_sssom and evaluate_rule_b4 without changing semantics.',
    'row_count': len(rows),
    'input_transforms': inputs,
    'skipped_prefixes_missing_transforms': missing,
    'findings': findings,
    'finding_count': len(findings),
    'limitations': ['Native B4 skips IDs absent from available transforms and non-B4 prefixes. No missing transform was substituted or synthesized.'],
}
path = HERE / f'{name}-b4-actual.json'
path.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'report': str(path), 'row_count':len(rows), 'finding_count':len(findings), 'skipped_prefixes':missing}, indent=2))
raise SystemExit(2 if findings else 0)
