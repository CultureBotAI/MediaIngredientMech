from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_checked_in_mapping_tsvs_use_lf_line_endings():
    offenders = [
        path.relative_to(ROOT).as_posix()
        for path in sorted((ROOT / "mappings").glob("*.tsv"))
        if b"\r\n" in path.read_bytes()
    ]

    assert offenders == []
