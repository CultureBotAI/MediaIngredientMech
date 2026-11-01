"""Run all native invariants, including B4 against the actual read-only KG path."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
import sys

root = Path.cwd().resolve()
source, destination = map(lambda p: Path(p).resolve(), sys.argv[1:])
assert source.is_file()
destination.mkdir(parents=True, exist_ok=False)
path = root / "scripts/validate_sssom_invariants.py"
spec = importlib.util.spec_from_file_location("native_candidate_invariants", path)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
module.KGM_TRANSFORMS_DIR = Path(os.environ["KGMICROBE_ROOT"]) / "data/transformed/ontologies"
_, _, rows = module._read_sssom(source)
prefixes = sorted({row["object_id"].split(":")[0] for row in rows} & module.B4_PREFIXES)
transforms = [module.KGM_TRANSFORMS_DIR / f"{prefix.lower()}_nodes.tsv" for prefix in prefixes]
def sha(p):
    h = hashlib.sha256()
    with p.open("rb") as stream:
        while chunk := stream.read(8 * 1024 * 1024):
            h.update(chunk)
    return h.hexdigest()
inputs = [source, path, root / "data/curated/mapped_ingredients.yaml",
          root / "mappings/other_cross_record_baseline.tsv", *[p for p in transforms if p.is_file()]]
before = {str(p): sha(p) for p in inputs}
code = module.main([str(path), str(source), "--reject-tsv", str(destination / "rejects.tsv")])
assert before == {str(p): sha(p) for p in inputs}, "validator inputs changed"
receipt = {"timestamp": datetime.now(timezone.utc).isoformat(), "argv": [str(source)],
    "native_module_sha256": sha(path), "input_sha256": before, "exit_code": code,
    "rows": len(rows), "actual_kg_transform_path": str(module.KGM_TRANSFORMS_DIR),
    "missing_b4_transforms": [str(p) for p in transforms if not p.is_file()],
    "execution": "Unmodified native main; only KGM_TRANSFORMS_DIR points to the actual read-only checkout.",
    "scientific_approval_added": False}
with (destination / "receipt.json").open("x") as stream:
    json.dump(receipt, stream, indent=2); stream.write("\n")
print(json.dumps(receipt, indent=2))
raise SystemExit(code)
