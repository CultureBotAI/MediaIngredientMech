"""Permanent identities survive resolver, browser and native CURIE lookup (#1265)."""

import importlib.util
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.curie import CurieNormalizer
from mediaingredientmech.stable_ids import (
    LIFECYCLE_PATH,
    REGISTRY_PATH,
    Lifecycle,
    Mint,
    Registry,
    dump_lifecycle,
    dump_registry,
)

ROOT = Path(__file__).resolve().parents[1]


def save_registry(root, registry):
    (root / REGISTRY_PATH).parent.mkdir(parents=True, exist_ok=True)
    (root / REGISTRY_PATH).write_bytes(dump_registry(registry))
    (root / LIFECYCLE_PATH).write_bytes(dump_lifecycle(registry))


@pytest.fixture
def corpus(tmp_path):
    registry = Registry(
        tuple(
            Mint(f"MIM:{number:07d}", f"Ingredient {number}", "2026-11-08") for number in (1, 2, 3)
        )
    )
    save_registry(tmp_path, registry)
    for number in (1, 2, 3):
        record = {
            "mim_id": f"MIM:{number:07d}",
            "identifier": f"CHEBI:{number}",
            "preferred_term": f"Ingredient {number}",
            "legacy_identifiers": [f"MIM:Old_{number}", f"kgmicrobe.compound:old_{number}"],
        }
        path = tmp_path / f"data/ingredients/unmapped/Old_{number}.yaml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(record))
    return tmp_path, registry


def test_numeric_and_legacy_ids_follow_current_record_after_rename(corpus):
    root, _ = corpus
    old = root / "data/ingredients/unmapped/Old_1.yaml"
    record = yaml.safe_load(old.read_text())
    record.update(preferred_term="New label", identifier="CHEBI:99")
    current = root / "data/ingredients/mapped/Corrected.yaml"
    current.parent.mkdir(parents=True)
    current.write_text(yaml.safe_dump(record))
    old.unlink()
    normalizer = CurieNormalizer(repo_root=root)
    for alias in ("MIM:0000001", "MIM:Old_1", "MIM:Corrected", "kgmicrobe.compound:old_1"):
        verdict = normalizer.resolve(alias)
        assert verdict and verdict.curie == "MIM:0000001"
    assert normalizer.resolve("MIM:9999999").problem == "UNKNOWN_SUBJECT"


def test_legacy_external_alias_ambiguity_never_selects_a_record(corpus):
    root, _ = corpus
    for number in (1, 2):
        path = root / f"data/ingredients/unmapped/Old_{number}.yaml"
        record = yaml.safe_load(path.read_text())
        record["legacy_identifiers"].append("kgmicrobe.compound:shared")
        path.write_text(yaml.safe_dump(record))
    normalizer = CurieNormalizer(repo_root=root)
    assert normalizer.resolve("kgmicrobe.compound:shared").problem == "AMBIGUOUS_ALIAS"
    assert normalizer.resolve("MIM:0000001").curie == "MIM:0000001"
    assert normalizer.resolve("MIM:0000002").curie == "MIM:0000002"


def test_retired_id_chain_resolves_without_filename_or_sssom_authority(corpus):
    root, registry = corpus
    events = (
        Lifecycle("MIM:0000001", "retired", "MIM:0000002", "2026-11-08T01:00:00Z", "Replacement"),
        Lifecycle("MIM:0000002", "merged", "MIM:0000003", "2026-11-08T02:00:00Z", "Duplicate"),
    )
    save_registry(root, Registry(registry.entries, events))
    for number in (1, 2):
        (root / f"data/ingredients/unmapped/Old_{number}.yaml").unlink()
    normalizer = CurieNormalizer(repo_root=root)
    assert normalizer.resolve("MIM:0000001").curie == "MIM:0000003"
    assert normalizer.resolve("MIM:0000002").curie == "MIM:0000003"


@pytest.mark.parametrize("status", ["retired", "merged"])
@pytest.mark.parametrize("subject", ["MIM:0000001", "mim:0000001", "MIM:Historical"])
@pytest.mark.parametrize("reverse", [False, True])
def test_lifecycle_redirect_never_transfers_old_mapping_evidence(corpus, status, subject, reverse):
    root, registry = corpus
    event = Lifecycle(
        "MIM:0000001", status, "MIM:0000002", "2026-11-08T01:00:00Z", "Reviewed replacement"
    )
    save_registry(root, Registry(registry.entries, (event,)))
    (root / "data/ingredients/unmapped/Old_1.yaml").unlink()
    mappings = root / "mappings"
    mappings.mkdir()
    (mappings / "mim_curie_aliases.tsv").write_text(
        "old_curie\tcurrent_curie\nMIM:Historical\tMIM:0000001\n"
    )
    rows = [f"{subject}\tCHEBI:1\tskos:exactMatch\n", "MIM:0000002\tCHEBI:2\tskos:exactMatch\n"]
    if reverse:
        rows.reverse()
    (mappings / "ingredient_mappings.sssom.tsv").write_text(
        "subject_id\tobject_id\tpredicate_id\n" + "".join(rows)
    )
    normalizer = CurieNormalizer(repo_root=root)
    assert normalizer.resolve(subject).curie == "MIM:0000002"
    assert normalizer.equivalent_term("MIM:0000002").curie == "CHEBI:2"
    assert normalizer.equivalent_term(subject).problem == "RETIRED_SUBJECT"
    assert normalizer._mappings["MIM:0000002"] == [("CHEBI:2", "skos:exactMatch")]


def test_replacement_without_own_mapping_does_not_inherit_old_equivalence(corpus):
    root, registry = corpus
    event = Lifecycle(
        "MIM:0000001", "retired", "MIM:0000002", "2026-11-08T01:00:00Z", "Reviewed replacement"
    )
    save_registry(root, Registry(registry.entries, (event,)))
    (root / "data/ingredients/unmapped/Old_1.yaml").unlink()
    mappings = root / "mappings"
    mappings.mkdir()
    (mappings / "ingredient_mappings.sssom.tsv").write_text(
        "subject_id\tobject_id\tpredicate_id\nMIM:0000001\tCHEBI:1\tskos:exactMatch\n"
    )
    normalizer = CurieNormalizer(repo_root=root)
    assert normalizer.resolve("MIM:0000001").curie == "MIM:0000002"
    assert normalizer.equivalent_term("MIM:0000002").problem == "NO_MAPPING"
    assert normalizer.equivalent_term("MIM:0000001").problem == "RETIRED_SUBJECT"


def test_duplicate_current_ids_fail_before_normalizer_can_choose(corpus):
    root, _ = corpus
    path = root / "data/ingredients/unmapped/Old_2.yaml"
    record = yaml.safe_load(path.read_text())
    record["mim_id"] = "MIM:0000001"
    path.write_text(yaml.safe_dump(record))
    with pytest.raises(ValueError, match="Duplicate MIM ID"):
        CurieNormalizer(repo_root=root)


def test_historical_alias_cycles_are_refused(corpus):
    root, _ = corpus
    aliases = root / "mappings/mim_curie_aliases.tsv"
    aliases.parent.mkdir()
    aliases.write_text("old_curie\tcurrent_curie\nMIM:a\tMIM:b\nMIM:b\tMIM:a\n")
    assert CurieNormalizer(repo_root=root).resolve("MIM:a").problem == "ALIAS_CYCLE"


def test_legacy_non_curie_placeholder_remains_explicitly_resolvable(corpus):
    root, _ = corpus
    path = root / "data/ingredients/unmapped/Old_1.yaml"
    record = yaml.safe_load(path.read_text())
    record["legacy_identifiers"].append("UNMAPPED_0196")
    path.write_text(yaml.safe_dump(record))
    assert CurieNormalizer(repo_root=root).resolve("UNMAPPED_0196").curie == "MIM:0000001"


def test_browser_uses_stable_identity_and_preserves_mapping_and_alias_search():
    spec = importlib.util.spec_from_file_location(
        "stable_browser", ROOT / "scripts/browser_export.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    record = {
        "mim_id": "MIM:0000001",
        "identifier": "CHEBI:123",
        "preferred_term": "Current label",
        "legacy_identifiers": ["kgmicrobe.compound:old_label", "MIM:Old_filename"],
    }
    first = module.extract_ingredient_for_browser(record, "unmapped/Old_filename.yaml")
    second = module.extract_ingredient_for_browser(record, "mapped/Corrected.yaml")
    assert first["record_id"] == second["record_id"] == "MIM:0000001"
    assert first["stable_url"] == second["stable_url"]
    assert first["id"] == second["id"] == "CHEBI:123"
    assert "kgmicrobe.compound:old_label" in second["searchable"]
    assert "mim:old_filename" in second["searchable"]
    assert first["detail_page"] != second["detail_page"]
    with pytest.raises(ValueError, match="seven-digit"):
        module.extract_ingredient_for_browser({"identifier": "CHEBI:123"}, "mapped/Corrected.yaml")


@pytest.mark.parametrize(
    "reference",
    [
        " MIM:12 ",
        "MIM:12",
        "mim:12",
        "MIM:0000000",
        "MIM:9999999",
        "MIM:٠٠٠٠٠٠١",
        "mim:٠٠٠٠٠٠١",
        "MIM:００００００１",
    ],
)
@pytest.mark.parametrize("chained", [False, True])
def test_numeric_mim_spellings_never_fall_through_to_aliases(corpus, reference, chained):
    root, _ = corpus
    path = root / "data/ingredients/unmapped/Old_1.yaml"
    record = yaml.safe_load(path.read_text())
    record["legacy_identifiers"].extend([reference, reference.replace("mim:", "MIM:")])
    path.write_text(yaml.safe_dump(record))
    mappings = root / "mappings"
    mappings.mkdir()
    # Both alias mechanisms offer the bad spelling a real owner. Neither is
    # allowed to override the authoritative numeric namespace.
    (mappings / "mim_curie_aliases.tsv").write_text(
        f"old_curie\tcurrent_curie\nMIM:Historical\t{reference}\n{reference}\tMIM:0000001\n"
    )
    queried = "MIM:Historical" if chained else reference
    (mappings / "ingredient_mappings.sssom.tsv").write_text(
        "subject_id\tobject_id\tpredicate_id\n"
        f"{queried}\tCHEBI:0\tskos:exactMatch\n"
        "MIM:0000001\tCHEBI:1\tskos:exactMatch\n"
    )
    normalizer = CurieNormalizer(repo_root=root)
    assert not normalizer.resolve(queried)
    assert not normalizer.equivalent_term(queried)
    assert normalizer.equivalent_term("MIM:0000001").curie == "CHEBI:1"
    assert normalizer._mappings["MIM:0000001"] == [("CHEBI:1", "skos:exactMatch")]
    assert normalizer.resolve("MIM:Old_1").curie == "MIM:0000001"


def test_alias_chain_normalizes_numeric_prefix_and_preserves_registry_authority(corpus):
    root, registry = corpus
    mappings = root / "mappings"
    mappings.mkdir()
    (mappings / "mim_curie_aliases.tsv").write_text(
        "old_curie\tcurrent_curie\nMIM:Historical\tmim:0000001\n"
        "mim:0000001\tMIM:0000002\nMIM:0000001\tMIM:0000002\n"
    )
    normalizer = CurieNormalizer(repo_root=root)
    assert normalizer.resolve("MIM:Historical").curie == "MIM:0000001"
    event = Lifecycle(
        "MIM:0000001", "merged", "MIM:0000002", "2026-11-08T01:00:00Z", "Reviewed replacement"
    )
    save_registry(root, Registry(registry.entries, (event,)))
    (root / "data/ingredients/unmapped/Old_1.yaml").unlink()
    normalizer = CurieNormalizer(repo_root=root)
    assert normalizer.resolve("MIM:Historical").curie == "MIM:0000002"
    assert normalizer.equivalent_term("MIM:Historical").problem == "RETIRED_SUBJECT"
