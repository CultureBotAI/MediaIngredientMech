"""Guards for the aggregator's failure and counting behaviour (issue #172).

Aggregation is load-bearing in two places that can destroy data: `just
sync-curated` writes its output over `data/curated/`, and `just qc-roundtrip`
compares against it. A record it silently drops therefore disappears from the
collection, the next `just export-individual` deletes the per-record file too,
and the round-trip gate — now comparing two sources that agree the record does
not exist — passes. These tests pin the loud-failure behaviour that prevents it.
"""

import importlib.util
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))


def _load():
    spec = importlib.util.spec_from_file_location(
        "aggregate_records", ROOT / "scripts" / "aggregate_records.py"
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def _tree(tmp_path: Path, mapped: dict[str, str], unmapped: dict[str, str] | None = None) -> Path:
    root = tmp_path / "ingredients"
    for category, files in (("mapped", mapped), ("unmapped", unmapped or {})):
        d = root / category
        d.mkdir(parents=True)
        for name, text in files.items():
            (d / f"{name}.yaml").write_text(text)
    return root


def _record(identifier: str, term: str, status: str = "MAPPED") -> str:
    return yaml.safe_dump(
        {"identifier": identifier, "preferred_term": term, "mapping_status": status}
    )


def _reference_collection(path: Path, records: list[tuple[str, str]]) -> Path:
    """Write a collection file to be used as an order reference."""
    path.write_text(
        yaml.safe_dump({
            "generation_date": "2026-08-03T00:00:00+00:00",
            "total_count": len(records),
            "ingredients": [
                {"identifier": i, "preferred_term": term, "mapping_status": "MAPPED"}
                for i, term in records
            ],
        }, sort_keys=False)
    )
    return path


# --- a dropped record must never be silent ----------------------------------


def test_unparseable_record_is_reported_as_an_error(tmp_path):
    agg = _load()
    root = _tree(
        tmp_path,
        {"Good": _record("CHEBI:1", "Good"), "Corrupt": "identifier: CHEBI:2\nsynonyms: [unclosed\n"},
    )

    collection, errors = agg.aggregate_individual_files(root, "mapped")

    assert len(errors) == 1
    assert "Corrupt.yaml" in errors[0]
    # The dropped record really is absent — that is why it must not be silent.
    assert collection["total_count"] == 1


def test_cli_exits_nonzero_when_a_record_is_dropped(tmp_path):
    """The whole point: `sync-curated` writes over data/curated/, so a run that
    lost a record must not report success."""
    root = _tree(
        tmp_path,
        {"Good": _record("CHEBI:1", "Good"), "Corrupt": "identifier: CHEBI:2\nsynonyms: [unclosed\n"},
    )
    out = tmp_path / "out"

    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "aggregate_records.py"),
         "--ingredients-dir", str(root), "--output-dir", str(out)],
        capture_output=True, text=True, cwd=ROOT,
    )

    assert proc.returncode == 1, proc.stdout
    assert "could not be aggregated" in proc.stdout
    assert "Corrupt.yaml" in proc.stdout  # names the offending file


def test_empty_or_comment_only_file_is_an_error_not_an_empty_record(tmp_path):
    """load_yaml returns {} for an empty document. Appending that as a record
    loses the file's content while the collection still 'has' a record — the same
    silent loss, wearing a different hat. Must be an error even without
    --validate, which is how every caller runs it."""
    agg = _load()
    root = _tree(
        tmp_path,
        {"Good": _record("CHEBI:1", "Good"), "Truncated": "", "CommentOnly": "# nothing here\n"},
    )

    collection, errors = agg.aggregate_individual_files(root, "mapped")

    assert len(errors) == 2
    assert collection["total_count"] == 1
    assert {} not in collection["ingredients"]


def test_record_without_mapping_status_is_an_error(tmp_path):
    """Without it the status counts silently under-report."""
    agg = _load()
    root = _tree(tmp_path, {"NoStatus": yaml.safe_dump({"identifier": "CHEBI:1", "preferred_term": "A"})})

    _, errors = agg.aggregate_individual_files(root, "mapped")

    assert len(errors) == 1
    assert "mapping_status" in errors[0]


def test_nothing_is_written_when_any_record_fails(tmp_path):
    """Fail BEFORE writing: `sync-curated` points --output-dir at data/curated/,
    so writing a short collection and then exiting 1 would still destroy the
    record in the working tree."""
    root = _tree(
        tmp_path,
        {"Good": _record("CHEBI:1", "Good"), "Corrupt": "identifier: CHEBI:2\nsynonyms: [unclosed\n"},
    )
    out = tmp_path / "out"
    out.mkdir()
    sentinel = out / "mapped_ingredients.yaml"
    sentinel.write_text("total_count: 999\ningredients: []\n")

    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "aggregate_records.py"),
         "--ingredients-dir", str(root), "--output-dir", str(out)],
        capture_output=True, text=True, cwd=ROOT,
    )

    assert proc.returncode == 1
    # The pre-existing collection must be untouched.
    assert sentinel.read_text() == "total_count: 999\ningredients: []\n"


def test_cli_exits_zero_on_a_clean_tree(tmp_path):
    root = _tree(tmp_path, {"Good": _record("CHEBI:1", "Good")})
    out = tmp_path / "out"

    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "aggregate_records.py"),
         "--ingredients-dir", str(root), "--output-dir", str(out)],
        capture_output=True, text=True, cwd=ROOT,
    )

    assert proc.returncode == 0, proc.stdout


# --- status counting must not relabel ---------------------------------------


def test_rejected_records_are_not_counted_as_unmapped(tmp_path):
    """`unmapped_count` used to be `total - mapped`, silently relabelling every
    other status as UNMAPPED in a header consumers read."""
    agg = _load()
    root = _tree(
        tmp_path,
        {
            "A": _record("CHEBI:1", "A", "MAPPED"),
            "B": _record("CHEBI:2", "B", "REJECTED"),
            "C": _record("CHEBI:3", "C", "REJECTED"),
        },
    )

    collection, _ = agg.aggregate_individual_files(root, "mapped")

    assert collection["total_count"] == 3
    assert collection["mapped_count"] == 1
    assert collection["unmapped_count"] == 0  # not 2


def test_unmapped_records_are_counted(tmp_path):
    agg = _load()
    root = _tree(tmp_path, {}, {"U": _record("UNMAPPED_0001", "U", "UNMAPPED")})

    collection, _ = agg.aggregate_individual_files(root, "unmapped")

    assert collection["unmapped_count"] == 1
    assert collection["mapped_count"] == 0


# --- collection shape --------------------------------------------------------


def test_per_record_only_fields_are_dropped(tmp_path):
    """The collection does not carry `discussions`; aggregating must not inject it."""
    agg = _load()
    rec = yaml.safe_dump(
        {
            "identifier": "CHEBI:1",
            "preferred_term": "A",
            "mapping_status": "MAPPED",
            "discussions": [{"discussion_id": "kgscan-1"}],
        }
    )
    root = _tree(tmp_path, {"A": rec})

    collection, _ = agg.aggregate_individual_files(root, "mapped")

    assert "discussions" not in collection["ingredients"][0]


def test_exclude_fields_tracks_the_exporter():
    agg = _load()
    spec = importlib.util.spec_from_file_location(
        "export_individual_records", ROOT / "scripts" / "export_individual_records.py"
    )
    exp = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = exp
    spec.loader.exec_module(exp)

    assert agg.PER_RECORD_ONLY_FIELDS == tuple(exp.PER_RECORD_AUTHORED_FIELDS)


def test_missing_category_directory_returns_no_collection(tmp_path):
    agg = _load()
    collection, errors = agg.aggregate_individual_files(tmp_path / "nope", "mapped")

    assert collection is None
    assert errors == []


# --- no silent default output directory (#169) -------------------------------


def test_output_dir_is_required(tmp_path):
    """It used to default to data/collections/, which nothing reads, so a bare
    invocation looked successful while changing nothing that mattered (#169)."""
    root = _tree(tmp_path, {"Good": _record("CHEBI:1", "Good")})

    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "aggregate_records.py"),
         "--ingredients-dir", str(root)],
        capture_output=True, text=True, cwd=ROOT,
    )

    assert proc.returncode != 0
    assert "--output-dir" in (proc.stderr + proc.stdout)


def test_verify_roundtrip_aggregated_dir_is_required():
    """Same reasoning: its default was a COMMITTED artifact, so the check
    compared against a March-2026 copy and passed for months (#148/#169)."""
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "verify_roundtrip.py"),
         "--original-dir", str(ROOT / "data" / "curated")],
        capture_output=True, text=True, cwd=ROOT,
    )

    assert proc.returncode != 0
    assert "--aggregated-dir" in (proc.stderr + proc.stdout)


# --- order preservation keeps the diff proportional -------------------------


def test_aggregation_matches_the_existing_collection_order(tmp_path):
    """Without this, aggregating an unchanged tree rewrote ~9,500 lines of pure
    reordering, so a one-record change arrived as an unreviewable diff — the
    exact condition under which 55 curation events went unnoticed (#148)."""
    agg = _load()
    root = _tree(tmp_path, {
        "Zulu": _record("CHEBI:3", "Zulu"),
        "Alpha": _record("CHEBI:1", "Alpha"),
        "Mike": _record("CHEBI:2", "Mike"),
    })
    # Existing collection is in a deliberately non-alphabetical order.
    reference = _reference_collection(tmp_path / "mapped_ingredients.yaml", [
        ("CHEBI:2", "Mike"), ("CHEBI:3", "Zulu"), ("CHEBI:1", "Alpha"),
    ])

    collection, _ = agg.aggregate_individual_files(root, "mapped", order_reference=reference)

    assert [r["preferred_term"] for r in collection["ingredients"]] == ["Mike", "Zulu", "Alpha"]


def test_new_records_go_last_in_filename_order(tmp_path):
    agg = _load()
    root = _tree(tmp_path, {
        "Alpha": _record("CHEBI:1", "Alpha"),
        "Brand": _record("CHEBI:9", "Brand New"),
        "Mike": _record("CHEBI:2", "Mike"),
    })
    reference = _reference_collection(tmp_path / "mapped_ingredients.yaml", [
        ("CHEBI:2", "Mike"), ("CHEBI:1", "Alpha"),
    ])

    collection, _ = agg.aggregate_individual_files(root, "mapped", order_reference=reference)

    terms = [r["preferred_term"] for r in collection["ingredients"]]
    assert terms == ["Mike", "Alpha", "Brand New"]


def test_missing_order_reference_falls_back_to_filename_order(tmp_path):
    """An absent reference must not be fatal — first aggregation into a temp dir
    has nothing to match."""
    agg = _load()
    root = _tree(tmp_path, {"Bravo": _record("CHEBI:2", "Bravo"), "Alpha": _record("CHEBI:1", "Alpha")})

    collection, _ = agg.aggregate_individual_files(
        root, "mapped", order_reference=tmp_path / "nope.yaml"
    )

    assert [r["preferred_term"] for r in collection["ingredients"]] == ["Alpha", "Bravo"]


def test_main_passes_the_output_collection_as_the_order_reference(tmp_path):
    """Covers the WIRING, not just the function.

    All the other ordering tests call aggregate_individual_files with an explicit
    order_reference. A review mutated the sole real call site to
    `order_reference=None` and every test still passed — the feature could be
    silently disabled and the ~9,500-line reorder would return with CI green.
    This drives main() end to end against a seeded output directory.
    """
    root = _tree(tmp_path, {
        "Zulu": _record("CHEBI:3", "Zulu"),
        "Alpha": _record("CHEBI:1", "Alpha"),
        "Mike": _record("CHEBI:2", "Mike"),
    })
    out = tmp_path / "out"
    out.mkdir()
    # Seed the destination in a deliberately non-alphabetical order.
    _reference_collection(out / "mapped_ingredients.yaml", [
        ("CHEBI:2", "Mike"), ("CHEBI:3", "Zulu"), ("CHEBI:1", "Alpha"),
    ])

    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "aggregate_records.py"),
         "--ingredients-dir", str(root), "--output-dir", str(out)],
        capture_output=True, text=True, cwd=ROOT,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr

    written = yaml.safe_load((out / "mapped_ingredients.yaml").read_text())
    assert [r["preferred_term"] for r in written["ingredients"]] == ["Mike", "Zulu", "Alpha"]


def test_unhashable_identifier_does_not_crash_ordering(tmp_path):
    """A list-valued identifier would make an unhashable pair key. Ordering is a
    presentation concern; it must not take down the whole aggregation with a
    bare TypeError and lose the per-record diagnostics."""
    agg = _load()
    root = _tree(tmp_path, {
        "Weird": yaml.safe_dump({"identifier": ["a", "b"], "preferred_term": "W",
                                 "mapping_status": "MAPPED"}),
        "Fine": _record("CHEBI:1", "Fine"),
    })
    reference = _reference_collection(tmp_path / "ref.yaml", [("CHEBI:1", "Fine")])

    collection, errors = agg.aggregate_individual_files(root, "mapped", order_reference=reference)

    assert errors == []
    assert len(collection["ingredients"]) == 2
