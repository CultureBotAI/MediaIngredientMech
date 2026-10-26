"""Bulk download of every complete ingredient record, written into the Pages artifact.

The browser catalog (data/ingredients.json) and the CSV lists are summaries:
evidence, roles, components, chemical properties and curation history exist
only in the per-record YAML. This export carries all of it as JSON Lines, one
record per line in source-path order, gzipped, beside a manifest that gives the
record count and SHA-256. scripts/build_pages_site.py writes it at deploy
time, so it is never committed and the build receipt covers its bytes.

Each line is ``{"source_file", "record_id", "record"}``: the YAML mapping
unchanged, the file it came from (identifiers are shared between records), and
the record's stable ``MIM:`` id, the same one the browser catalog uses.
"""

from __future__ import annotations

import argparse
import datetime
import gzip
import hashlib
import json
import os
from pathlib import Path

import yaml  # type: ignore[import-untyped]

from mediaingredientmech.curie import mim_curie_for_stem

DOWNLOADS_DIR = "downloads"
EXPORT_NAME = "mediaingredientmech-records.jsonl.gz"
MANIFEST_NAME = "manifest.json"
REPOSITORY = "https://github.com/CultureBotAI/MediaIngredientMech"


def _json_value(value: object) -> str:
    # YAML reads an unquoted timestamp or date as a datetime or date; JSON has
    # neither, so it is written in ISO 8601, which is deterministic.
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()
    raise TypeError(f"{type(value).__name__} has no JSON form")


def export_lines(ingredient_root: Path, sources: list[Path]) -> bytes:
    """Serialize every source record, sorted by its path under ingredient_root.

    Dates and times are written in ISO 8601; any other value with no JSON form
    raises rather than being stringified, since the file claims to hold each
    record as written.
    """
    lines = []
    for source in sorted(sources, key=lambda p: p.relative_to(ingredient_root).as_posix()):
        record = yaml.safe_load(source.read_text(encoding="utf-8"))
        if not isinstance(record, dict):
            raise ValueError(f"Not a record mapping: {source}")
        line = {
            "source_file": source.relative_to(ingredient_root).as_posix(),
            "record_id": mim_curie_for_stem(source.stem),
            "record": record,
        }
        lines.append(
            json.dumps(
                line,
                ensure_ascii=False,
                allow_nan=False,
                separators=(",", ":"),
                default=_json_value,
            )
        )
    return ("\n".join(lines) + "\n").encode("utf-8")


def write_records_export(ingredient_root: Path, sources: list[Path], output: Path) -> list[str]:
    """Write the export and its manifest under output/downloads; return their site paths."""
    if not sources:
        raise ValueError("No ingredient sources to export")
    payload = export_lines(ingredient_root, sources)
    # mtime=0 keeps the gzip header free of the build time, so unchanged
    # records compress to identical bytes.
    compressed = gzip.compress(payload, compresslevel=9, mtime=0)
    folder = output / DOWNLOADS_DIR
    folder.mkdir(parents=True, exist_ok=True)
    (folder / EXPORT_NAME).write_bytes(compressed)
    manifest = {
        "file": EXPORT_NAME,
        "format": "JSON Lines, gzip; one object per line: source_file, record_id, record",
        "record_count": len(sources),
        "sorted_by": "source_file",
        "bytes": len(compressed),
        "sha256": hashlib.sha256(compressed).hexdigest(),
        "uncompressed_sha256": hashlib.sha256(payload).hexdigest(),
        "source": "data/ingredients/{mapped,unmapped}/*.yaml",
        "schema": f"{REPOSITORY}/blob/main/src/mediaingredientmech/schema/mediaingredientmech.yaml",
        "license": "Project data: CC BY 4.0 (LICENSE-DATA). Third-party source material "
        "keeps its own terms (LICENSE).",
    }
    commit = os.environ.get("GITHUB_SHA")
    if commit:
        manifest["source_commit"] = commit
    (folder / MANIFEST_NAME).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return [f"{DOWNLOADS_DIR}/{EXPORT_NAME}", f"{DOWNLOADS_DIR}/{MANIFEST_NAME}"]


def check_records_export(output: Path, expected_sources: set[str]) -> None:
    """Refuse an export whose manifest, bytes or record set do not match the sources."""
    folder = output / DOWNLOADS_DIR
    manifest = json.loads((folder / MANIFEST_NAME).read_text(encoding="utf-8"))
    compressed = (folder / EXPORT_NAME).read_bytes()
    if manifest.get("sha256") != hashlib.sha256(compressed).hexdigest():
        raise ValueError("Records export does not match its manifest checksum")
    rows = [json.loads(line) for line in gzip.decompress(compressed).decode("utf-8").splitlines()]
    files = [row["source_file"] for row in rows]
    if manifest.get("record_count") != len(rows) or files != sorted(expected_sources):
        raise ValueError("Records export does not hold every ingredient source exactly once")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    root = Path(__file__).resolve().parents[2]
    parser.add_argument("--ingredients", type=Path, default=root / "data" / "ingredients")
    parser.add_argument(
        "--out", type=Path, required=True, help="site directory to write downloads/ into"
    )
    args = parser.parse_args()
    sources = sorted(
        p for status in ("mapped", "unmapped") for p in (args.ingredients / status).glob("*.yaml")
    )
    for name in write_records_export(args.ingredients, sources, args.out):
        print(args.out / name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
