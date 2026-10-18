"""Reproduce the correction-batch unified export using a reviewed claw producer.

Load only direct live ingredient files into an isolated temporary input tree.
Merge tombstones are excluded; their names are retained on their representatives.
The current upstream producer otherwise lets alphabetically earlier tombstones
win its name index. No upstream checkout or CultureMech recipe is mutated.
"""

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile

import yaml


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--builder", type=Path, required=True)
    ap.add_argument("--culturemech", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[3]
    spec = importlib.util.spec_from_file_location("reviewed_unified_builder", args.builder)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert hasattr(
        module, "load_mapping_rejections"
    ), "Producer lacks reviewed source-ID rejection handling"
    recipe_hashes = {
        str(p.relative_to(args.culturemech)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in (args.culturemech / "data/normalized_yaml").rglob("*.yaml")
    }
    sources = {}
    excluded = []
    with tempfile.TemporaryDirectory(prefix="mim-unified-input-") as directory:
        staged = Path(directory)
        for group in ("mapped", "unmapped"):
            for path in sorted((root / "data/ingredients" / group).glob("*.yaml")):
                sources[str(path.relative_to(root))] = hashlib.sha256(path.read_bytes()).hexdigest()
                if yaml.safe_load(path.read_text())["mapping_status"] == "REJECTED":
                    excluded.append(str(path.relative_to(root)))
                    continue
                dest = staged / path.relative_to(root)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path, dest)
        ledger = Path("mappings/unified_mapping_rejections.tsv")
        (staged / ledger).parent.mkdir(parents=True)
        shutil.copyfile(root / ledger, staged / ledger)
        indexes = module.load_mim_index(staged)
        rejections = module.load_mapping_rejections(staged, indexes[0])
        occurrences = module.scan_culturemech(args.culturemech)
        rows = module.build_unified_rows(occurrences, *indexes, rejections)
        for path, expected in sources.items():
            assert hashlib.sha256((root / path).read_bytes()).hexdigest() == expected
        for path, expected in recipe_hashes.items():
            assert hashlib.sha256((args.culturemech / path).read_bytes()).hexdigest() == expected
        module.write_tsv(rows, args.output)
    evidence = dict(
        producer_sha256=hashlib.sha256(args.builder.read_bytes()).hexdigest(),
        wrapper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        ingredient_inputs=sources,
        culturemech_recipe_inputs=recipe_hashes,
        excluded_merge_tombstones=excluded,
        rejection_ledger_sha256=hashlib.sha256((root / ledger).read_bytes()).hexdigest(),
        output_sha256=hashlib.sha256(args.output.read_bytes()).hexdigest(),
        rows=len(rows),
        scope="MIM correction batch; current local CultureMech recipes read only; not proof that downstream media were regenerated",
    )
    (Path(__file__).parent / "unified-build.json").write_text(json.dumps(evidence, indent=2) + "\n")


if __name__ == "__main__":
    main()
