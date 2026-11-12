"""Permanent B1 identity is active ownership, never an invented mapping (#1371)."""

import copy
import importlib.util
import json
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.export import reviewed_sssom as reviewed
from mediaingredientmech.export.reviewed_sssom import capture_permanent_identity, permanent_subject
from mediaingredientmech.stable_ids import (
    LIFECYCLE_PATH,
    MIM_PREFIX,
    REGISTRY_PATH,
    Lifecycle,
    Mint,
    Registry,
    dump_lifecycle,
    dump_registry,
)

ROOT = Path(__file__).resolve().parents[1]


def invariant():
    spec = importlib.util.spec_from_file_location(
        "stable_b1_validator", ROOT / "scripts/validate_sssom_invariants.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n")


@pytest.fixture
def stable_fixture(tmp_path):
    root = tmp_path
    for kind in ("mapped", "unmapped"):
        (root / "data/ingredients" / kind).mkdir(parents=True)
    (root / "data/ids").mkdir()
    registry = Registry((Mint("MIM:0000001", "Original formula", "2026-11-10"),))
    (root / REGISTRY_PATH).write_bytes(dump_registry(registry))
    (root / LIFECYCLE_PATH).write_bytes(dump_lifecycle(registry))
    owner = "data/ingredients/mapped/CeNO33_X_6_H2O.yaml"
    record = {
        "mim_id": "MIM:0000001",
        "identifier": "cas:10294-41-4",
        "preferred_term": "cerium(III) nitrate hexahydrate",
        "mapping_status": "MAPPED",
        "legacy_identifiers": ["MIM:Original_formula", "MIM:Earlier_filename"],
        "synonyms": [{"synonym_text": "CeNO33 x 6 H2O", "synonym_type": "REJECTED_LABEL"}],
    }
    (root / owner).write_text(yaml.safe_dump(record))
    row = {
        "subject_id": "MIM:0000001",
        "subject_label": record["preferred_term"],
        "predicate_id": "skos:broadMatch",
        "object_id": "mesh:M0319657",
        "object_label": "cerium nitrate (Ce(+3))",
        "other": "Ce(NO3)3 x 6 H2O",
        "confidence": "0.8",
        "comment": "Parent mapping, not exact hydrate identity.",
    }
    metadata = {
        "mapping_set_id": "https://example.org/test",
        "predicate_semantics": "skos",
        "curie_map": {"MIM": MIM_PREFIX},
        "license": "https://creativecommons.org/publicdomain/zero/1.0/",
    }
    return root, registry, owner, record, row, metadata


def make_review(fixture, rows=None, dispositions=None, owner_paths=None):
    root, _, owner, _, row, metadata = fixture
    rows = [copy.deepcopy(row)] if rows is None else rows
    dispositions = dispositions or ["SUPPORTED"] * len(rows)
    source = root / "source.sssom.tsv"
    header = "".join("# " + line + "\n" for line in yaml.safe_dump(metadata).splitlines())
    source.write_bytes(header.encode() + reviewed._tsv(list(rows[0]), rows))
    entries, decisions, record_inputs = {}, [], {}
    owner_paths = owner_paths or [owner] * len(rows)
    for position, (claim, disposition) in enumerate(zip(rows, dispositions, strict=True), 1):
        owner = owner_paths[position - 1]
        record_inputs[owner] = reviewed.digest(root / owner)
        decision = {
            "source_position": position,
            "row_sha256": reviewed.row_sha256(claim),
            "owner_record": owner,
            "disposition": disposition,
            "review_reason": f"Explicit test review {position}: {disposition}",
            "review_evidence": "evidence.json",
            "evidence_key": str(position),
        }
        decisions.append(decision)
        entries[str(position)] = {
            key: decision[key] for key in ("row_sha256", "disposition", "review_reason")
        }
        entries[str(position)]["owner_record_sha256"] = reviewed.digest(root / owner)
    write_json(root / "evidence.json", {"entries": entries})
    pins = {
        str(path.relative_to(root)): reviewed.digest(path)
        for path in [
            root / REGISTRY_PATH,
            root / LIFECYCLE_PATH,
            *sorted((root / "data/ingredients").rglob("*.yaml")),
        ]
    }
    for owner in record_inputs:
        pins.pop(owner)
    pins["evidence.json"] = reviewed.digest(root / "evidence.json")
    document = {
        "schema_version": 1,
        "source_sssom": source.name,
        "source_sha256": reviewed.digest(source),
        "inputs": pins,
        "record_inputs": record_inputs,
        "decisions": decisions,
    }
    path = root / "review.json"
    write_json(path, document)
    return path


@pytest.mark.parametrize("with_cas", [False, True])
def test_native_cerium_shape_uses_mim_identity_without_slug(stable_fixture, monkeypatch, with_cas):
    root, _, owner, _, row, metadata = stable_fixture
    rows = [row]
    if with_cas:
        rows.append(
            dict(
                row,
                predicate_id="skos:exactMatch",
                object_id="cas:10294-41-4",
                object_label="cerium(III) nitrate hexahydrate",
            )
        )
    module = invariant()
    monkeypatch.setattr(module, "INGREDIENTS_DIR", (root / owner).parent)
    assert list(module.evaluate_rule_b1(rows, metadata=metadata)) == []
    path = make_review(stable_fixture, rows)
    output = root / "output"
    result = reviewed.export_reviewed(root, path, output)
    assert result["counts"] == {"source": len(rows), "supported": len(rows), "withhold": 0}
    _, _, actual = reviewed.read_sssom(output / reviewed.PRODUCTS[0])
    assert actual == rows
    assert not any(
        r["object_id"].startswith("kgmicrobe.") or r["subject_id"] == r["object_id"] for r in actual
    )
    assert reviewed.validate_reviewed(root, path, output) == result


@pytest.mark.parametrize(
    "subject", ["MIM:0000000", "MIM:0000002", "MIM:1", "mim:0000001", "MIM:００００００１"]
)
def test_numeric_spelling_or_unknown_id_never_uses_registry_fallback(
    stable_fixture, monkeypatch, subject
):
    root, _, owner, _, row, metadata = stable_fixture
    module = invariant()
    monkeypatch.setattr(module, "INGREDIENTS_DIR", (root / owner).parent)
    rows = [
        dict(row, subject_id=subject),
        dict(
            row,
            subject_id=subject,
            predicate_id="skos:exactMatch",
            object_id="kgmicrobe.ingredient:original_formula",
        ),
    ]
    assert permanent_subject(subject)
    rejects = list(module.evaluate_rule_b1(rows, metadata=metadata))
    assert len(rejects) == 1 and "invalid permanent identity" in rejects[0][2]


@pytest.mark.parametrize(
    "defect",
    [
        "missing_mint",
        "missing_lifecycle",
        "duplicate_owner",
        "missing_active",
        "retired",
        "duplicate_yaml",
        "unmapped",
        "wrong_prefix",
        "stale_label",
    ],
)
def test_invalid_current_identity_refuses_without_output(stable_fixture, defect):
    root, registry, owner, record, row, metadata = stable_fixture
    if defect == "missing_mint":
        (root / REGISTRY_PATH).unlink()
    elif defect == "missing_lifecycle":
        (root / LIFECYCLE_PATH).unlink()
    elif defect == "duplicate_owner":
        (root / owner).with_name("Duplicate.yaml").write_bytes((root / owner).read_bytes())
    elif defect == "missing_active":
        (root / owner).unlink()
    elif defect == "retired":
        retired = Registry(
            (*registry.entries, Mint("MIM:0000002", "Successor", "2026-11-10")),
            (
                Lifecycle(
                    "MIM:0000001", "retired", "MIM:0000002", "2026-11-11T00:00:00Z", "Retired"
                ),
            ),
        )
        (root / REGISTRY_PATH).write_bytes(dump_registry(retired))
        (root / LIFECYCLE_PATH).write_bytes(dump_lifecycle(retired))
    elif defect == "duplicate_yaml":
        with (root / owner).open("a") as stream:
            stream.write("mim_id: MIM:0000001\n")
    elif defect == "unmapped":
        record["mapping_status"] = "UNMAPPED"
        (root / owner).write_text(yaml.safe_dump(record))
    elif defect == "wrong_prefix":
        metadata["curie_map"]["MIM"] = "https://omim.org/entry/"
    elif defect == "stale_label":
        row["subject_label"] = "Original formula"
    with pytest.raises((ValueError, OSError)):
        identity = capture_permanent_identity(root, metadata)
        identity.require(row["subject_id"], row["subject_label"])
    assert not (root / "output").exists()


def test_rename_keeps_identity_and_rejected_alias_is_not_a_subject(stable_fixture):
    root, _, owner, record, row, metadata = stable_fixture
    identity = capture_permanent_identity(root, metadata)
    assert identity.require(row["subject_id"], row["subject_label"]) == owner
    renamed = (root / owner).with_name("Completely_renamed.yaml")
    (root / owner).rename(renamed)
    record["preferred_term"] = "Reviewed renamed label"
    renamed.write_text(yaml.safe_dump(record))
    successor = capture_permanent_identity(root, metadata)
    assert successor.require("MIM:0000001", "Reviewed renamed label") == str(
        renamed.relative_to(root)
    )
    with pytest.raises(ValueError):
        successor.require("MIM:Original_formula", "Reviewed renamed label")
    with pytest.raises(ValueError):
        successor.require("MIM:0000001", "CeNO33 x 6 H2O")
    with pytest.raises((ValueError, OSError)):
        identity.verify()


@pytest.mark.parametrize(
    "missing",
    [str(REGISTRY_PATH), str(LIFECYCLE_PATH), "data/ingredients/unmapped/Unresolved.yaml"],
)
def test_ordinary_review_must_pin_entire_identity_closure(stable_fixture, missing):
    root, registry, _, _, _, _ = stable_fixture
    extra = root / "data/ingredients/unmapped/Unresolved.yaml"
    extra.write_text(
        yaml.safe_dump(
            {"mim_id": "MIM:0000002", "preferred_term": "Unresolved", "mapping_status": "UNMAPPED"}
        )
    )
    (root / REGISTRY_PATH).write_bytes(
        dump_registry(
            Registry((*registry.entries, Mint("MIM:0000002", "Unresolved", "2026-11-10")))
        )
    )
    path = make_review(stable_fixture)
    review = json.loads(path.read_text())
    del review["inputs"][missing]
    write_json(path, review)
    with pytest.raises(ValueError, match="Permanent identity input missing"):
        reviewed.export_reviewed(root, path, root / "output")
    assert not (root / "output").exists()


@pytest.mark.parametrize("drift", ["owner", "mint", "lifecycle", "add_owner", "inode"])
def test_late_identity_drift_refuses_and_preserves_output(stable_fixture, monkeypatch, drift):
    root, _, owner, _, _, _ = stable_fixture
    path = make_review(stable_fixture)
    output = root / "output"
    reviewed.export_reviewed(root, path, output)
    before = {p.name: p.read_bytes() for p in output.iterdir()}
    original = reviewed._products

    def mutate(loaded):
        products = original(loaded)
        target = {
            "owner": root / owner,
            "mint": root / REGISTRY_PATH,
            "lifecycle": root / LIFECYCLE_PATH,
        }.get(drift)
        if target is not None:
            target.write_bytes(target.read_bytes() + b"\n")
        elif drift == "add_owner":
            (root / owner).with_name("Late.yaml").write_bytes((root / owner).read_bytes())
        else:
            target = root / owner
            replacement = target.with_suffix(".replacement")
            replacement.write_bytes(target.read_bytes())
            assert replacement.stat().st_ino != target.stat().st_ino
            replacement.replace(target)
        return products

    monkeypatch.setattr(reviewed, "_products", mutate)
    with pytest.raises((ValueError, OSError)):
        reviewed.export_reviewed(root, path, output)
    assert {p.name: p.read_bytes() for p in output.iterdir()} == before


def test_permanent_identity_does_not_promote_withheld_registry_or_external(stable_fixture):
    root, _, _, _, row, _ = stable_fixture
    registry = dict(
        row,
        predicate_id="skos:exactMatch",
        object_id="kgmicrobe.ingredient:unproved",
        object_label="Unproved registry claim",
    )
    close = dict(
        row,
        predicate_id="skos:closeMatch",
        object_id="CHEBI:1",
        object_label="Unproved ontology claim",
    )
    path = make_review(
        stable_fixture, [row, registry, close], ["SUPPORTED", "WITHHOLD", "WITHHOLD"]
    )
    products, manifest = reviewed.expected_products(root, path)
    _, _, supported = reviewed.read_sssom(Path("supported"), content=products[reviewed.PRODUCTS[0]])
    _, _, withheld = reviewed.read_sssom(Path("withheld"), content=products[reviewed.PRODUCTS[1]])
    assert supported == [row] and withheld == [registry, close]
    assert manifest["counts"] == {"source": 3, "supported": 1, "withhold": 2}


def test_permanent_identity_does_not_clear_b5(stable_fixture, monkeypatch):
    root, _, owner, _, row, metadata = stable_fixture
    module = invariant()
    monkeypatch.setattr(module, "INGREDIENTS_DIR", (root / owner).parent)
    rows = [
        row,
        *(
            dict(
                row, predicate_id="skos:exactMatch", object_id=f"kgmicrobe.{kind}:original_formula"
            )
            for kind in ("ingredient", "compound")
        ),
    ]
    assert list(module.evaluate_rule_b1(rows, metadata=metadata)) == []
    assert list(module.evaluate_rule_b5(rows))


@pytest.mark.parametrize("predicate", ["skos:narrowMatch", "skos:closeMatch", "skos:exactMatch"])
def test_reviewed_predicates_are_preserved_without_identity_or_subclass_inference(
    stable_fixture, predicate
):
    root, _, _, _, row, _ = stable_fixture
    row = dict(row, predicate_id=predicate, object_id="CHEBI:1")
    path = make_review(stable_fixture, [row])
    products, _ = reviewed.expected_products(root, path)
    _, _, actual = reviewed.read_sssom(Path("output"), content=products[reviewed.PRODUCTS[0]])
    assert actual == [row]


def test_shared_external_parent_does_not_collapse_distinct_permanent_owners(stable_fixture):
    root, registry, owner, record, row, _ = stable_fixture
    second_owner = "data/ingredients/mapped/Distinct.yaml"
    second = dict(
        record,
        mim_id="MIM:0000002",
        preferred_term="Distinct reviewed supplied form",
        identifier="UNMAPPED_2",
        legacy_identifiers=["MIM:Distinct"],
    )
    (root / second_owner).write_text(yaml.safe_dump(second))
    (root / REGISTRY_PATH).write_bytes(
        dump_registry(
            Registry(
                (*registry.entries, Mint("MIM:0000002", second["preferred_term"], "2026-11-10"))
            )
        )
    )
    rows = [row, dict(row, subject_id=second["mim_id"], subject_label=second["preferred_term"])]
    path = make_review(stable_fixture, rows, owner_paths=[owner, second_owner])
    products, _ = reviewed.expected_products(root, path)
    _, _, actual = reviewed.read_sssom(Path("output"), content=products[reviewed.PRODUCTS[0]])
    assert actual == rows
    assert {r["subject_id"] for r in actual} == {"MIM:0000001", "MIM:0000002"}
    assert len({r["object_id"] for r in actual}) == 1


@pytest.mark.parametrize("alias", ["symlink", "hardlink", "parent_symlink"])
def test_identity_filesystem_aliases_refused(stable_fixture, alias):
    import os

    root, _, owner, _, _, metadata = stable_fixture
    path = root / owner
    if alias == "symlink":
        original = path.with_suffix(".original")
        path.rename(original)
        path.symlink_to(original.name)
    elif alias == "hardlink":
        os.link(path, path.with_suffix(".link"))
    else:
        original = path.parent.with_name("original-mapped")
        path.parent.rename(original)
        path.parent.symlink_to(original.name)
    with pytest.raises(ValueError, match="symlink|hardlinked"):
        capture_permanent_identity(root, metadata)


def test_cli_reads_permanent_namespace_metadata_without_synthesizing_rows(
    stable_fixture, monkeypatch
):
    root, _, owner, _, row, _ = stable_fixture
    make_review(stable_fixture)
    module = invariant()
    monkeypatch.setattr(module, "INGREDIENTS_DIR", (root / owner).parent)
    prelude, _, rows = module._read_sssom(root / "source.sssom.tsv")
    metadata = yaml.safe_load("\n".join(line[1:].removeprefix(" ") for line in prelude))
    assert list(module.evaluate_rule_b1(rows, metadata=metadata)) == []
    assert rows == [row]


@pytest.mark.parametrize("drift", ["inventory", "same_bytes_inode"])
def test_terminal_identity_drift_rolls_back_publication(stable_fixture, monkeypatch, drift):
    root, _, owner, _, _, _ = stable_fixture
    path = make_review(stable_fixture)
    output = root / "output"
    reviewed.export_reviewed(root, path, output)
    before = {p.name: p.read_bytes() for p in output.iterdir()}
    rename = Path.rename
    fired = False

    def late_change(source, destination):
        nonlocal fired
        result = rename(source, destination)
        if Path(destination) == output and not fired:
            fired = True
            current = root / owner
            if drift == "inventory":
                current.with_name("Late.yaml").write_bytes(current.read_bytes())
            else:
                replacement = current.with_suffix(".replacement")
                replacement.write_bytes(current.read_bytes())
                assert replacement.stat().st_ino != current.stat().st_ino
                replacement.replace(current)
        return result

    monkeypatch.setattr(Path, "rename", late_change)
    with pytest.raises((ValueError, OSError), match="inventory changed|input changed"):
        reviewed.export_reviewed(root, path, output)
    assert fired
    assert {p.name: p.read_bytes() for p in output.iterdir()} == before
