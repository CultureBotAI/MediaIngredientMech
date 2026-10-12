"""`generate_index_files.py --output-dir` lets `just qc-roundtrip` check index
currency without rewriting tracked files (#810). Hermetic: it runs on a tiny
synthetic collection, not the committed corpus (#813)."""

from __future__ import annotations

from pathlib import Path

import yaml

from scripts.generate_index_files import main

INDEXES = (
    "mapped_ingredients_index.json", "unmapped_ingredients_index.json", "all_ingredients_index.json",
    "mapped_ingredients_index.csv", "unmapped_ingredients_index.csv", "all_ingredients_index.csv",
    "MAPPED_INGREDIENTS.md", "UNMAPPED_INGREDIENTS.md", "ALL_INGREDIENTS.md",
)


def _collection(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump({"ingredients": records}), encoding="utf-8")


def test_output_dir_receives_every_index_and_curated_is_untouched(tmp_path, monkeypatch):
    curated = tmp_path / "data" / "curated"
    _collection(curated / "mapped_ingredients.yaml", [{
        "identifier": "CHEBI:26710", "preferred_term": "NaCl", "mapping_status": "MAPPED",
        "ontology_mapping": {"ontology_id": "CHEBI:26710", "ontology_label": "sodium chloride",
                             "ontology_source": "CHEBI", "mapping_quality": "EXACT_MATCH"},
    }])
    _collection(curated / "unmapped_ingredients.yaml", [{
        "identifier": "UNMAPPED_0001", "preferred_term": "Calf brains", "mapping_status": "UNMAPPED",
    }])
    before = sorted(p.name for p in curated.iterdir())
    monkeypatch.chdir(tmp_path)

    out = tmp_path / "scratch"
    main(["--output-dir", str(out)])

    assert sorted(p.name for p in out.iterdir()) == sorted(INDEXES)
    assert sorted(p.name for p in curated.iterdir()) == before
    assert "NaCl" in (out / "ALL_INGREDIENTS.md").read_text(encoding="utf-8")
    assert "Calf brains" in (out / "UNMAPPED_INGREDIENTS.md").read_text(encoding="utf-8")
