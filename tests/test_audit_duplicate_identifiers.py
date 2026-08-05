"""Guards for the duplicate-identifier gate (#218).

This gate exists because a record's `identifier` IS its ontology CURIE, so two
records sharing one both claim to be that term and an `{identifier: record}`
lookup silently keeps whichever came last. The gate is only worth having if it
actually fails, and "a check that looks healthiest when it has stopped working"
is a failure this repo has shipped three times (#148, #180, #181). So each test
below pins a way the gate could go quietly green.
"""

import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "audit_duplicate_identifiers.py"

BASELINE_HEADER = (
    "identifier\tcollection\trecord_count\tmembers_fingerprint\tdisposition\t"
    "same_after_folding\thydrate_markers\tpreferred_terms\n"
)


def rec(identifier, term, status="MAPPED"):
    return {"identifier": identifier, "preferred_term": term, "mapping_status": status}


def build(tmp_path, mapped, unmapped=()):
    """A minimal repo tree the script can run against."""
    for name, recs in (("mapped", mapped), ("unmapped", unmapped)):
        d = tmp_path / "data" / "curated"
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{name}_ingredients.yaml").write_text(
            yaml.safe_dump({"total_count": len(recs), "ingredients": list(recs)})
        )
    (tmp_path / "scripts").mkdir(exist_ok=True)
    (tmp_path / "scripts" / SCRIPT.name).write_text(SCRIPT.read_text())
    (tmp_path / "mappings").mkdir(exist_ok=True)
    return tmp_path


def run(tmp_path, *args):
    return subprocess.run(
        [sys.executable, str(tmp_path / "scripts" / SCRIPT.name), *args],
        capture_output=True, text=True,
    )


@pytest.fixture
def repo(tmp_path):
    return build(tmp_path, [rec("CHEBI:1", "Glycerol"), rec("CHEBI:1", "glycerol"),
                            rec("CHEBI:2", "Water")])


def test_baseline_then_check_passes(repo):
    assert run(repo, "--write-baseline").returncode == 0
    assert run(repo, "--check").returncode == 0


def test_new_duplicate_fails(repo):
    run(repo, "--write-baseline")
    path = repo / "data" / "curated" / "mapped_ingredients.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["ingredients"].append(rec("CHEBI:2", "Water, again"))
    path.write_text(yaml.safe_dump(doc))
    out = run(repo, "--check")
    assert out.returncode == 2
    assert "NEW" in out.stdout and "CHEBI:2" in out.stdout


def test_group_growing_fails(repo):
    run(repo, "--write-baseline")
    path = repo / "data" / "curated" / "mapped_ingredients.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["ingredients"].append(rec("CHEBI:1", "GLYCEROL "))
    path.write_text(yaml.safe_dump(doc))
    out = run(repo, "--check")
    assert out.returncode == 2
    assert "GREW" in out.stdout


def test_member_swap_at_constant_size_fails(repo):
    """The hole that lets a curator's verdict be transplanted onto other records."""
    run(repo, "--write-baseline")
    path = repo / "data" / "curated" / "mapped_ingredients.yaml"
    path.write_text(yaml.safe_dump({"ingredients": [
        rec("CHEBI:1", "Chloroform"), rec("CHEBI:1", "Benzene"), rec("CHEBI:2", "Water")]}))
    out = run(repo, "--check")
    assert out.returncode == 2, "swapping both members at the same count must not pass"
    assert "SWAPPED" in out.stdout


def test_losing_all_records_fails(repo):
    """Wholesale data loss makes every group vanish; that must not read as success."""
    run(repo, "--write-baseline")
    path = repo / "data" / "curated" / "mapped_ingredients.yaml"
    path.write_text(yaml.safe_dump({"ingredients": []}))
    out = run(repo, "--check")
    assert out.returncode == 2
    assert "GONE" in out.stdout


def test_rejected_records_are_not_a_claim(tmp_path):
    repo = build(tmp_path, [rec("CHEBI:1", "Glycerol"),
                            rec("CHEBI:1", "Old glycerol", status="REJECTED")])
    repo_baseline = repo / "mappings" / "duplicate_identifier_baseline.tsv"
    repo_baseline.write_text(BASELINE_HEADER + "x\tmapped\t2\tdead\tUNREVIEWED\tfalse\t0\tx\n")
    out = run(repo, "--check")
    # the REJECTED tombstone does not make CHEBI:1 a duplicate, so the only
    # complaint is the stale baseline row — not a CHEBI:1 finding
    assert "CHEBI:1" not in out.stdout


def test_duplicates_in_the_unmapped_collection_are_caught(tmp_path):
    repo = build(tmp_path, [rec("CHEBI:1", "Water")],
                 [rec("UNMAPPED_0001", "Thing", status="UNMAPPED"),
                  rec("UNMAPPED_0001", "Other thing", status="UNMAPPED")])
    # a non-empty baseline covering something else, so the unmapped duplicate
    # surfaces as NEW rather than tripping the empty-baseline guard first
    repo_baseline = repo / "mappings" / "duplicate_identifier_baseline.tsv"
    repo_baseline.write_text(
        BASELINE_HEADER + "CHEBI:99\tmapped\t2\tdead\tUNREVIEWED\tfalse\t0\tx | y\n")
    out = run(repo, "--check")
    assert out.returncode == 2
    assert "UNMAPPED_0001" in out.stdout


def test_missing_or_corrupt_baseline_exits_2_not_traceback(repo):
    out = run(repo, "--check")
    assert out.returncode == 2 and "Traceback" not in out.stderr

    b = repo / "mappings" / "duplicate_identifier_baseline.tsv"
    b.write_text(BASELINE_HEADER + "CHEBI:1\tmapped\tnot-a-number\tf\tUNREVIEWED\tfalse\t0\tx\n")
    out = run(repo, "--check")
    assert out.returncode == 2 and "Traceback" not in out.stderr

    b.write_text("wrong\tcolumns\n1\t2\n")
    out = run(repo, "--check")
    assert out.returncode == 2 and "Traceback" not in out.stderr


def test_unparseable_collection_exits_2_not_traceback(repo):
    (repo / "data" / "curated" / "mapped_ingredients.yaml").write_text("{[not yaml")
    out = run(repo, "--check")
    assert out.returncode == 2 and "Traceback" not in out.stderr


def test_check_and_write_baseline_are_mutually_exclusive(repo):
    out = run(repo, "--check", "--write-baseline")
    assert out.returncode != 0
    assert "not allowed with" in out.stderr


def test_refresh_resets_a_disposition_whose_members_changed(repo):
    run(repo, "--write-baseline")
    b = repo / "mappings" / "duplicate_identifier_baseline.tsv"
    b.write_text(b.read_text().replace("UNREVIEWED", "SAFE_MERGE"))

    path = repo / "data" / "curated" / "mapped_ingredients.yaml"
    path.write_text(yaml.safe_dump({"ingredients": [
        rec("CHEBI:1", "Chloroform"), rec("CHEBI:1", "Benzene")]}))
    run(repo, "--write-baseline")
    rows = [r.split("\t") for r in b.read_text().splitlines()[1:]]
    assert rows and rows[0][4] == "UNREVIEWED", (
        "a verdict about glycerol must not survive onto chloroform/benzene")


def test_hydrate_signal_has_no_false_positives_on_known_traps():
    sys.path.insert(0, str(ROOT / "scripts"))
    import importlib.util
    spec = importlib.util.spec_from_file_location("audit_dup", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    for trap in ("b-Mannan borohydrate reduced carob seed", "Sodium hydroxide",
                 "Carbohydrate mix", "Tetrahydrofuran", "Dihydrogen phosphate"):
        assert not mod.HYDRATE.search(trap), trap
    for real in ("CoCl2 x 6 H2O", "MgSO4·7H2O", "Cr2(SO4)3 x n H2O",
                 "Cadmium chloride hemipentahydrate", "Sodium Thiosulfate Pentahydrate",
                 "Potassium tellurite hydrate"):
        assert mod.HYDRATE.search(real), real
