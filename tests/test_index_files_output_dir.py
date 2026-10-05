"""`generate_index_files.py --output-dir` lets `just qc-roundtrip` check index
currency without rewriting tracked files (#810)."""

from __future__ import annotations

from pathlib import Path

from scripts.generate_index_files import main

ROOT = Path(__file__).resolve().parents[1]
INDEXES = (
    "mapped_ingredients_index.json", "unmapped_ingredients_index.json", "all_ingredients_index.json",
    "mapped_ingredients_index.csv", "unmapped_ingredients_index.csv", "all_ingredients_index.csv",
    "MAPPED_INGREDIENTS.md", "UNMAPPED_INGREDIENTS.md", "ALL_INGREDIENTS.md",
)


def test_output_dir_receives_every_index_and_matches_the_committed_files(tmp_path, monkeypatch):
    monkeypatch.chdir(ROOT)
    before = {name: (ROOT / "data/curated" / name).read_bytes() for name in INDEXES}
    main(["--output-dir", str(tmp_path)])
    assert sorted(p.name for p in tmp_path.iterdir()) == sorted(INDEXES)
    for name in INDEXES:
        assert (tmp_path / name).read_bytes() == before[name], f"stale committed index: {name}"
        assert (ROOT / "data/curated" / name).read_bytes() == before[name]
