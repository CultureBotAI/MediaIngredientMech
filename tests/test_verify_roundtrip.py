"""Guards for the curated <-> per-record round-trip gate.

The gate exists because `just export-individual` projects data/curated/ over the
per-record tree, so anything written directly into data/ingredients/ is reverted
on the next export. That silently destroyed 55 curation events from PR #116
(issue #148). These tests pin the behaviour the gate depends on — above all that
it *fails* when it should, since a gate that can only pass is worthless.
"""

import importlib.util
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def _write_collection(path: Path, records: list[dict]) -> None:
    mapped = sum(1 for r in records if r.get("mapping_status") == "MAPPED")
    path.write_text(
        yaml.safe_dump(
            {
                "generation_date": "2026-08-02T00:00:00+00:00",
                "total_count": len(records),
                "mapped_count": mapped,
                "unmapped_count": len(records) - mapped,
                "ingredients": records,
            },
            sort_keys=False,
        )
    )


def _record(identifier: str, term: str, **extra) -> dict:
    return {
        "identifier": identifier,
        "preferred_term": term,
        "mapping_status": "MAPPED",
        **extra,
    }


def _pair(tmp_path: Path, original: list[dict], aggregated: list[dict]):
    orig_dir, agg_dir = tmp_path / "curated", tmp_path / "agg"
    orig_dir.mkdir()
    agg_dir.mkdir()
    for d, recs in ((orig_dir, original), (agg_dir, aggregated)):
        _write_collection(d / "mapped_ingredients.yaml", recs)
        _write_collection(d / "unmapped_ingredients.yaml", [])
    return orig_dir, agg_dir


# --- the constant must not drift from the exporter's -------------------------


def test_per_record_only_fields_tracks_the_exporter():
    """Drift here is silent in the unsafe direction: a field listed only in the
    verifier is wiped on every export while the gate stays green."""
    vr = _load("verify_roundtrip")
    exp = _load("export_individual_records")
    assert vr.PER_RECORD_ONLY_FIELDS == tuple(exp.PER_RECORD_AUTHORED_FIELDS)


# --- the gate must pass when it should ---------------------------------------


def test_identical_collections_pass(tmp_path):
    vr = _load("verify_roundtrip")
    recs = [_record("CHEBI:1", "Glucose"), _record("CHEBI:2", "NaCl")]
    orig, agg = _pair(tmp_path, recs, [dict(r) for r in recs])

    results = vr.verify_round_trip(orig, agg)
    assert results["data_diffs"] == 0
    assert results["errors"] == []


def test_per_record_only_field_is_ignored(tmp_path):
    """`discussions` lives only on per-record files by design; comparing it
    would report a permanent expected difference and make the gate useless."""
    vr = _load("verify_roundtrip")
    orig = [_record("CHEBI:1", "Glucose")]
    agg = [_record("CHEBI:1", "Glucose", discussions=[{"discussion_id": "kgscan-1"}])]
    o, a = _pair(tmp_path, orig, agg)

    assert vr.verify_round_trip(o, a)["errors"] == []


# --- the gate must FAIL when it should ---------------------------------------


def test_single_field_drift_is_caught_with_counts_unchanged(tmp_path):
    """The subtle case: record counts match, one field differs. This is the
    shape of the #148 drift (ingredient_type flipped on 53 records)."""
    vr = _load("verify_roundtrip")
    orig = [_record("UNMAPPED_0113", "BCYE agar", ingredient_type="UNDEFINED_MIXTURE")]
    agg = [_record("UNMAPPED_0113", "BCYE agar", ingredient_type="DEFINED_MEDIUM")]
    o, a = _pair(tmp_path, orig, agg)

    results = vr.verify_round_trip(o, a)
    assert results["data_diffs"] == 1
    assert any("UNMAPPED_0113" in e for e in results["errors"])


def test_record_count_mismatch_is_caught(tmp_path):
    vr = _load("verify_roundtrip")
    o, a = _pair(tmp_path, [_record("CHEBI:1", "A"), _record("CHEBI:2", "B")], [_record("CHEBI:1", "A")])

    assert vr.verify_round_trip(o, a)["errors"]


def test_a_field_present_only_in_the_collection_is_caught(tmp_path):
    """Direction matters: the exporter would wipe this on the next run."""
    vr = _load("verify_roundtrip")
    orig = [_record("CHEBI:1", "Glucose", notes="curated note")]
    agg = [_record("CHEBI:1", "Glucose")]
    o, a = _pair(tmp_path, orig, agg)

    assert vr.verify_round_trip(o, a)["data_diffs"] == 1


def test_many_mismatches_still_fail_despite_the_error_cap(tmp_path):
    """The cap bounds *reporting*, not the verdict — data_diffs is set before it."""
    vr = _load("verify_roundtrip")
    orig = [_record(f"CHEBI:{i}", f"T{i}", ingredient_type="UNDEFINED_MIXTURE") for i in range(60)]
    agg = [_record(f"CHEBI:{i}", f"T{i}", ingredient_type="DEFINED_MEDIUM") for i in range(60)]
    o, a = _pair(tmp_path, orig, agg)

    results = vr.verify_round_trip(o, a)
    assert results["data_diffs"] > 0
    assert len(results["errors"]) <= 30  # capped, but non-empty
    assert results["errors"]


def test_more_than_one_mismatch_is_reported_per_file(tmp_path):
    """It used to stop after the first, turning one fix into many CI rounds."""
    vr = _load("verify_roundtrip")
    orig = [_record(f"CHEBI:{i}", f"T{i}", notes="a") for i in range(5)]
    agg = [_record(f"CHEBI:{i}", f"T{i}", notes="b") for i in range(5)]
    o, a = _pair(tmp_path, orig, agg)

    assert len(vr.verify_round_trip(o, a)["errors"]) > 1
