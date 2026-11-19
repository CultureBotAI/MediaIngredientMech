"""Read-only native invariant checks for namespace-preserving B1 aliases."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
import tempfile

RUN = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RUN/'claw/scripts'))

def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result

builder = module('followup684_builder', RUN/'claw/scripts/build_mim_ingredient_sssom.py')
validator = module('followup684_invariants', RUN/'mim/scripts/validate_sssom_invariants.py')
fixture_helpers = module('followup684_test_helpers', RUN/'claw/tests/test_sssom_identity_row.py')
actual = RUN/'mim/data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml'
cases = [('actual_sodium_stock', actual, hashlib.sha256(actual.read_bytes()).hexdigest())]
with tempfile.TemporaryDirectory(prefix='b1-b5-', dir=Path(__file__).parent) as tmp:
    for identifier, ontology, tag in [
        ('kgmicrobe.ingredient:MES_Buffer', 'CHEBI:39010', 'mixed_case_ingredient'),
        ('kgmicrobe.compound:MES_Buffer', 'FOODON:00001234', 'mixed_case_compound'),
    ]:
        folder = Path(tmp)/tag
        folder.mkdir()
        path = fixture_helpers.write_record(folder, 'MES_Buffer', identifier, ontology, 'NARROW_MATCH')
        cases.append((tag, path, hashlib.sha256(path.read_bytes()).hexdigest()))
    result = []
    for tag, path, digest in cases:
        rows = builder._row_from_yaml(path, {}, {}, {}, {})
        b1 = list(validator.evaluate_rule_b1(rows))
        b5 = list(validator.evaluate_rule_b5(rows))
        result.append({'case':tag,'input_sha256':digest,
                       'rows':[{k:r[k] for k in ['subject_id','predicate_id','object_id','object_source']} for r in rows],
                       'B1_findings':len(b1),'B5_findings':len(b5)})
        assert not b1 and not b5, (tag,b1,b5)
    print(json.dumps(result, indent=2))
