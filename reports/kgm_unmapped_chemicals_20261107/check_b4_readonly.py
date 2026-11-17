"""Run native canonical-label Rule B4 against explicit read-only KG transforms."""

import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
KGM = Path("/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe-mim-1788-20261107")
SPEC = importlib.util.spec_from_file_location("invariants", ROOT / "scripts/validate_sssom_invariants.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)
module.KGM_TRANSFORMS_DIR = KGM / "data/transformed/ontologies"


def main():
    current = ROOT / "mappings/ingredient_mappings.sssom.tsv"
    before = HERE / "sodium-acetate/publication/canonical-before.tsv"
    outputs = {}
    for label, path in (("baseline", before), ("candidate", current)):
        _, _, rows = module._read_sssom(path)
        outputs[label] = list(module.evaluate_rule_b4(rows))
    assert outputs["baseline"] == outputs["candidate"], "new canonical label rejection"
    files = {str(p.relative_to(KGM)): hashlib.sha256(p.read_bytes()).hexdigest()
             for prefix in module.B4_PREFIXES
             if (p := module.KGM_TRANSFORMS_DIR / (prefix.lower() + "_nodes.tsv")).is_file()}
    document = {"kgm_head": subprocess.check_output(["git", "-C", str(KGM), "rev-parse", "HEAD"]).decode().strip(),
                "read_only": True, "source_files": files, "native_results": outputs,
                "native_validator_sha256": hashlib.sha256((ROOT / "scripts/validate_sssom_invariants.py").read_bytes()).hexdigest()}
    with (HERE / "b4-readonly-result.json").open("x") as stream:
        stream.write(json.dumps(document, indent=2, sort_keys=True) + "\n")
    print({key: len(value) for key, value in outputs.items()})


if __name__ == "__main__":
    main()
