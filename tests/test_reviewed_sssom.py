"""Review-bound SSSOM partitions resist stale evidence and coherent tampering (#729)."""

import copy
import csv
import io
import json
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.export import reviewed_sssom as reviewed


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


@pytest.fixture
def reviewed_fixture(tmp_path):
    root = tmp_path
    records = root / "data/ingredients/mapped"
    records.mkdir(parents=True)
    rows, decisions, entries, record_inputs = [], [], {}, {}
    for i, name in enumerate(("Alpha", "Beta"), 1):
        owner = f"data/ingredients/mapped/{name}.yaml"
        (root / owner).write_text(
            yaml.safe_dump(
                {
                    "identifier": f"CHEBI:{i}",
                    "preferred_term": name,
                    "mapping_status": "MAPPED",
                    "synonyms": [],
                }
            )
        )
        record_inputs[owner] = reviewed.digest(root / owner)
        row = {
            "subject_id": f"MIM:{name}",
            "subject_label": name,
            "predicate_id": "skos:exactMatch",
            "object_id": f"CHEBI:{i}",
            "object_label": name.lower(),
            "other": f"{name} alias",
            "confidence": "0.8",
            "comment": "Historical annotation; unnormalized.",
        }
        rows.append(row)
        decision = {
            "source_position": i,
            "row_sha256": reviewed.row_sha256(row),
            "owner_record": owner,
            "disposition": "SUPPORTED" if i == 1 else "WITHHOLD",
            "review_reason": f"Inspected claim {i}: " + ("supported" if i == 1 else "unresolved"),
            "review_evidence": "evidence.json",
            "evidence_key": str(i),
        }
        decisions.append(decision)
        entries[str(i)] = {k: decision[k] for k in ("row_sha256", "disposition", "review_reason")}
        entries[str(i)]["owner_record_sha256"] = record_inputs[owner]
    source = root / "source.sssom.tsv"
    source.write_bytes(
        b"# mapping_set_id: https://example.org/canonical\n"
        b"# mapping_set_description: Canonical full mapping set\n"
        b"# predicate_semantics: skos\n"
        b"# license: https://creativecommons.org/publicdomain/zero/1.0/\n"
        b"# curie_map:\n#   CHEBI: http://purl.obolibrary.org/obo/CHEBI_\n"
        + reviewed._tsv(list(rows[0]), rows)
    )
    write_json(root / "evidence.json", {"entries": entries})
    review = {
        "schema_version": 1,
        "source_sssom": "source.sssom.tsv",
        "source_sha256": reviewed.digest(source),
        "inputs": {"evidence.json": reviewed.digest(root / "evidence.json")},
        "record_inputs": record_inputs,
        "decisions": decisions,
    }
    path = root / "review.json"
    write_json(path, review)
    return root, path, root / "output"


def mutate_review(fixture, mutate):
    _, path, _ = fixture
    review = json.loads(path.read_text())
    mutate(review)
    write_json(path, review)


def change_source_row(fixture, changes):
    root, path, _ = fixture
    source = root / "source.sssom.tsv"
    metadata, fields, rows = reviewed.read_sssom(source)
    rows[0].update(changes)
    header = "".join("# " + line + "\n" for line in yaml.safe_dump(metadata).splitlines())
    source.write_bytes(header.encode() + reviewed._tsv(fields, rows))
    review = json.loads(path.read_text())
    review["source_sha256"] = reviewed.digest(source)
    review["decisions"][0]["row_sha256"] = reviewed.row_sha256(rows[0])
    proof = json.loads((root / "evidence.json").read_text())
    proof["entries"]["1"]["row_sha256"] = reviewed.row_sha256(rows[0])
    write_json(root / "evidence.json", proof)
    review["inputs"]["evidence.json"] = reviewed.digest(root / "evidence.json")
    write_json(path, review)


def test_exact_partition_preserves_fields_and_changes_only_scope_metadata(reviewed_fixture):
    root, path, output = reviewed_fixture
    manifest = reviewed.export_reviewed(root, path, output)
    assert manifest["counts"] == {"source": 2, "supported": 1, "withhold": 1}
    original_meta, fields, rows = reviewed.read_sssom(root / "source.sssom.tsv")
    for index, name in enumerate(reviewed.PRODUCTS[:2]):
        metadata, actual_fields, actual = reviewed.read_sssom(output / name)
        assert actual == [rows[index]] and actual_fields == fields
        assert metadata["mapping_set_id"] != original_meta["mapping_set_id"]
        assert metadata["mapping_set_description"] != original_meta["mapping_set_description"]
        for key in original_meta.keys() - {"mapping_set_id", "mapping_set_description"}:
            assert metadata[key] == original_meta[key]
    assert reviewed.validate_reviewed(root, path, output) == manifest


@pytest.mark.parametrize(
    "target", ["source.sssom.tsv", "evidence.json", "data/ingredients/mapped/Alpha.yaml"]
)
def test_stale_inputs_fail(reviewed_fixture, target):
    root, path, output = reviewed_fixture
    with (root / target).open("a") as stream:
        stream.write("\n")
    with pytest.raises(ValueError, match="Stale"):
        reviewed.export_reviewed(root, path, output)


@pytest.mark.parametrize(
    "attack",
    [
        "missing",
        "duplicate",
        "wrong_owner",
        "wrong_payload",
        "unsupported_status",
        "blank_reason",
        "blank_key",
        "missing_evidence",
        "record_inventory",
    ],
)
def test_malformed_or_misbound_decisions_fail(reviewed_fixture, attack):
    def mutate(review):
        decision = review["decisions"][0]
        if attack == "missing":
            review["decisions"].pop()
        elif attack == "duplicate":
            review["decisions"][1] = copy.deepcopy(decision)
        elif attack == "wrong_owner":
            decision["owner_record"] = review["decisions"][1]["owner_record"]
        elif attack == "wrong_payload":
            decision["row_sha256"] = "0" * 64
        elif attack == "unsupported_status":
            decision["disposition"] = "APPROVED"
        elif attack == "blank_reason":
            decision["review_reason"] = " "
        elif attack == "blank_key":
            decision["evidence_key"] = ""
        elif attack == "missing_evidence":
            review["inputs"].clear()
        elif attack == "record_inventory":
            review["record_inputs"].clear()

    mutate_review(reviewed_fixture, mutate)
    with pytest.raises(ValueError):
        reviewed.export_reviewed(*reviewed_fixture)


def test_scientific_override_must_agree_with_evidence(reviewed_fixture):
    mutate_review(reviewed_fixture, lambda r: r["decisions"][1].update(disposition="SUPPORTED"))
    with pytest.raises(ValueError, match="disagrees"):
        reviewed.export_reviewed(*reviewed_fixture)


def test_rehashed_wrong_scientific_reason_is_rejected(reviewed_fixture):
    mutate_review(
        reviewed_fixture, lambda r: r["decisions"][0].update(review_reason="Different claim")
    )
    with pytest.raises(ValueError, match="disagrees"):
        reviewed.export_reviewed(*reviewed_fixture)


@pytest.mark.parametrize("token", ["produces: alpha", "hydrolysis: alpha", "Role: carbon source"])
def test_supported_non_name_phrase_refused_even_with_positive_evidence(reviewed_fixture, token):
    change_source_row(reviewed_fixture, {"other": token})
    with pytest.raises(ValueError, match="Non-resolving"):
        reviewed.export_reviewed(*reviewed_fixture)


@pytest.mark.parametrize("curie", ["cas:2650-88-3", "cas:480-14-4", "CAS:89471-28-0", "cas:12-3-4"])
def test_invalid_cas_cannot_be_published_even_with_rehashed_approval(reviewed_fixture, curie):
    change_source_row(reviewed_fixture, {"object_id": curie})
    with pytest.raises(ValueError, match="Invalid CAS"):
        reviewed.export_reviewed(*reviewed_fixture)


def test_valid_cas_is_accepted_with_the_existing_explicit_review(reviewed_fixture):
    change_source_row(reviewed_fixture, {"object_id": "cas:7732-18-5"})
    assert reviewed.export_reviewed(*reviewed_fixture)["counts"]["supported"] == 1


def test_invalid_cas_payload_is_preserved_in_withheld_backlog(reviewed_fixture):
    change_source_row(reviewed_fixture, {"object_id": "cas:2650-88-3"})
    root, path, output = reviewed_fixture
    review = json.loads(path.read_text())
    proof = json.loads((root / "evidence.json").read_text())
    review["decisions"][0]["disposition"] = "WITHHOLD"
    proof["entries"]["1"]["disposition"] = "WITHHOLD"
    write_json(root / "evidence.json", proof)
    review["inputs"]["evidence.json"] = reviewed.digest(root / "evidence.json")
    write_json(path, review)
    assert reviewed.export_reviewed(*reviewed_fixture)["counts"]["withhold"] == 2
    assert "cas:2650-88-3" in (output / "withheld_mappings.sssom.tsv").read_text()


def test_source_rejected_alias_cannot_be_published(reviewed_fixture):
    root, path, _ = reviewed_fixture
    owner = root / "data/ingredients/mapped/Alpha.yaml"
    record = yaml.safe_load(owner.read_text())
    record["synonyms"] = [{"synonym_text": "ALPHA ALIAS", "synonym_type": "REJECTED_LABEL"}]
    owner.write_text(yaml.safe_dump(record))
    proof = json.loads((root / "evidence.json").read_text())
    proof["entries"]["1"]["owner_record_sha256"] = reviewed.digest(owner)
    write_json(root / "evidence.json", proof)
    mutate_review(
        reviewed_fixture,
        lambda r: r.update(
            record_inputs={
                **r["record_inputs"],
                "data/ingredients/mapped/Alpha.yaml": reviewed.digest(owner),
            },
            inputs={"evidence.json": reviewed.digest(root / "evidence.json")},
        ),
    )
    with pytest.raises(ValueError, match="rejected synonym"):
        reviewed.export_reviewed(*reviewed_fixture)


@pytest.mark.parametrize(
    "attack",
    [
        "supported_row",
        "withheld_row",
        "partition",
        "disposition",
        "manifest_counts",
        "missing_file",
        "extra_file",
    ],
)
def test_coherently_rehashed_outputs_do_not_bypass_expected_partition(reviewed_fixture, attack):
    root, path, output = reviewed_fixture
    reviewed.export_reviewed(root, path, output)
    manifest = json.loads((output / "manifest.json").read_text())
    if attack == "supported_row":
        target = output / reviewed.PRODUCTS[0]
        target.write_text(target.read_text().replace("CHEBI:1", "CHEBI:999"))
    elif attack == "withheld_row":
        target = output / reviewed.PRODUCTS[1]
        target.write_text(target.read_text().replace("CHEBI:2", "CHEBI:999"))
    elif attack == "partition":
        first, second = (output / name for name in reviewed.PRODUCTS[:2])
        first_bytes, second_bytes = first.read_bytes(), second.read_bytes()
        first.write_bytes(second_bytes)
        second.write_bytes(first_bytes)
    elif attack == "disposition":
        target = output / reviewed.PRODUCTS[2]
        target.write_text(target.read_text().replace("WITHHOLD", "SUPPORTED"))
    elif attack == "manifest_counts":
        manifest["counts"]["supported"] = 2
    elif attack == "missing_file":
        (output / reviewed.PRODUCTS[1]).unlink()
    elif attack == "extra_file":
        (output / "rogue.tsv").write_text("unreviewed")
    for name in reviewed.PRODUCTS:
        if (output / name).exists():
            manifest["files"][name] = reviewed.digest(output / name)
    write_json(output / "manifest.json", manifest)
    with pytest.raises(ValueError):
        reviewed.validate_reviewed(root, path, output)


def test_conflicting_source_label_and_subject_owner_refused(reviewed_fixture):
    change_source_row(reviewed_fixture, {"subject_label": "Beta"})
    with pytest.raises(ValueError, match="owner"):
        reviewed.export_reviewed(*reviewed_fixture)


@pytest.mark.parametrize(
    "changes",
    [
        {"subject_id": "MIM:missing"},
        {"subject_id": "MIM:Beta"},
        {"subject_label": "Invented identity label"},
    ],
)
def test_subject_and_preferred_label_must_both_resolve(reviewed_fixture, changes):
    change_source_row(reviewed_fixture, changes)
    with pytest.raises(ValueError, match="owner"):
        reviewed.export_reviewed(*reviewed_fixture)


@pytest.mark.parametrize("status", ["UNMAPPED", "AMBIGUOUS", "REJECTED", "PENDING_REVIEW"])
def test_nonmapped_owner_cannot_support_mapping(reviewed_fixture, status):
    root, _, _ = reviewed_fixture
    owner = root / "data/ingredients/mapped/Alpha.yaml"
    record = yaml.safe_load(owner.read_text())
    record["mapping_status"] = status
    owner.write_text(yaml.safe_dump(record))
    mutate_review(
        reviewed_fixture,
        lambda r: r["record_inputs"].update(
            {
                "data/ingredients/mapped/Alpha.yaml": reviewed.digest(owner),
            }
        ),
    )
    with pytest.raises(ValueError, match="owner"):
        reviewed.export_reviewed(*reviewed_fixture)


def test_duplicate_json_key_refused(reviewed_fixture):
    _, path, _ = reviewed_fixture
    path.write_text(
        path.read_text().replace('"schema_version": 1', '"schema_version": 1, "schema_version": 1')
    )
    with pytest.raises(ValueError, match="Duplicate JSON key"):
        reviewed.export_reviewed(*reviewed_fixture)


def test_disposition_output_retains_exact_evidence_trace(reviewed_fixture):
    root, path, output = reviewed_fixture
    reviewed.export_reviewed(root, path, output)
    rows = list(
        csv.DictReader(io.StringIO((output / reviewed.PRODUCTS[2]).read_text()), delimiter="\t")
    )
    assert [row["source_position"] for row in rows] == ["1", "2"]
    assert rows[1]["review_evidence"] == "evidence.json" and rows[1]["evidence_key"] == "2"
    assert rows[1]["disposition"] == "WITHHOLD"


def test_refreshed_source_checksum_does_not_approve_changed_mapping(reviewed_fixture):
    root, _, _ = reviewed_fixture
    source = root / "source.sssom.tsv"
    source.write_text(source.read_text().replace("CHEBI:1", "CHEBI:999"))
    mutate_review(reviewed_fixture, lambda r: r.update(source_sha256=reviewed.digest(source)))
    with pytest.raises(ValueError, match="payload"):
        reviewed.export_reviewed(*reviewed_fixture)


def test_refreshed_evidence_checksum_does_not_hide_changed_evidence(reviewed_fixture):
    root, _, _ = reviewed_fixture
    evidence = root / "evidence.json"
    proof = json.loads(evidence.read_text())
    proof["entries"]["1"]["disposition"] = "WITHHOLD"
    write_json(evidence, proof)
    mutate_review(
        reviewed_fixture, lambda r: r["inputs"].update({"evidence.json": reviewed.digest(evidence)})
    )
    with pytest.raises(ValueError, match="disagrees"):
        reviewed.export_reviewed(*reviewed_fixture)


def test_refreshed_owner_checksum_needs_fresh_exact_evidence(reviewed_fixture):
    root, _, _ = reviewed_fixture
    owner = root / "data/ingredients/mapped/Alpha.yaml"
    record = yaml.safe_load(owner.read_text())
    record["notes"] = "Source record changed after the evidence review."
    owner.write_text(yaml.safe_dump(record))
    mutate_review(
        reviewed_fixture,
        lambda r: r["record_inputs"].update(
            {
                "data/ingredients/mapped/Alpha.yaml": reviewed.digest(owner),
            }
        ),
    )
    with pytest.raises(ValueError, match="disagrees"):
        reviewed.export_reviewed(*reviewed_fixture)


def test_encoded_filename_subject_resolves_exactly(reviewed_fixture):
    root, _, _ = reviewed_fixture
    old = "data/ingredients/mapped/Alpha.yaml"
    new = "data/ingredients/mapped/(Alpha).yaml"
    (root / old).rename(root / new)
    change_source_row(reviewed_fixture, {"subject_id": "MIM:~28Alpha~29"})

    def move_owner(review):
        review["record_inputs"][new] = review["record_inputs"].pop(old)
        review["decisions"][0]["owner_record"] = new

    mutate_review(reviewed_fixture, move_owner)
    assert reviewed.export_reviewed(*reviewed_fixture)["counts"]["supported"] == 1


def test_validate_only_cli_is_read_only_and_detects_tampering(
    reviewed_fixture, monkeypatch, capsys
):
    root, path, output = reviewed_fixture
    reviewed.export_reviewed(root, path, output)
    monkeypatch.setattr(
        "sys.argv",
        [
            "reviewed_sssom",
            "--root",
            str(root),
            "--review",
            str(path),
            "--output",
            str(output),
            "--validate-only",
        ],
    )
    reviewed.main()
    assert json.loads(capsys.readouterr().out)["counts"]["source"] == 2
    target = output / "ingredient_mappings.sssom.tsv"
    target.write_text(target.read_text().replace("CHEBI:1", "CHEBI:999"))
    changed = target.read_bytes()
    with pytest.raises(ValueError):
        reviewed.main()
    assert target.read_bytes() == changed


@pytest.mark.parametrize("position", [0, 3, True, "1"])
def test_invalid_source_positions_fail(reviewed_fixture, position):
    mutate_review(reviewed_fixture, lambda r: r["decisions"][0].update(source_position=position))
    with pytest.raises(ValueError, match="position"):
        reviewed.export_reviewed(*reviewed_fixture)


@pytest.mark.parametrize("predicate", ["skos:broadMatch", "skos:narrowMatch"])
def test_supported_asymmetric_row_requires_supported_registry_sibling(reviewed_fixture, predicate):
    change_source_row(reviewed_fixture, {"predicate_id": predicate, "object_id": "CHEBI:999"})
    with pytest.raises(ValueError, match="Rule B1"):
        reviewed.export_reviewed(*reviewed_fixture)


@pytest.mark.parametrize("registry_supported", [True, False])
def test_registry_sibling_must_survive_supported_partition(reviewed_fixture, registry_supported):
    root, path, output = reviewed_fixture
    owner = root / "data/ingredients/mapped/Alpha.yaml"
    record = yaml.safe_load(owner.read_text())
    record["identifier"] = "kgmicrobe.compound:alpha"
    owner.write_text(yaml.safe_dump(record))
    change_source_row(
        reviewed_fixture, {"predicate_id": "skos:broadMatch", "object_id": "CHEBI:999"}
    )
    source = root / "source.sssom.tsv"
    metadata, fields, rows = reviewed.read_sssom(source)
    sibling = {
        **rows[0],
        "predicate_id": "skos:exactMatch",
        "object_id": "kgmicrobe.compound:alpha",
    }
    rows.append(sibling)
    source.write_bytes(
        "".join("# " + line + "\n" for line in yaml.safe_dump(metadata).splitlines()).encode()
        + reviewed._tsv(fields, rows)
    )
    review = json.loads(path.read_text())
    proof = json.loads((root / "evidence.json").read_text())
    review["source_sha256"] = reviewed.digest(source)
    review["record_inputs"]["data/ingredients/mapped/Alpha.yaml"] = reviewed.digest(owner)
    proof["entries"]["1"]["owner_record_sha256"] = reviewed.digest(owner)
    decision = {
        **review["decisions"][0],
        "source_position": 3,
        "row_sha256": reviewed.row_sha256(sibling),
        "evidence_key": "3",
        "disposition": "SUPPORTED" if registry_supported else "WITHHOLD",
    }
    review["decisions"].append(decision)
    proof["entries"]["3"] = {
        key: decision[key] for key in ("row_sha256", "disposition", "review_reason")
    }
    proof["entries"]["3"]["owner_record_sha256"] = reviewed.digest(owner)
    write_json(root / "evidence.json", proof)
    review["inputs"]["evidence.json"] = reviewed.digest(root / "evidence.json")
    write_json(path, review)
    if registry_supported:
        assert reviewed.export_reviewed(root, path, output)["counts"]["supported"] == 2
    else:
        with pytest.raises(ValueError, match="Rule B1"):
            reviewed.export_reviewed(root, path, output)
        assert json.loads(path.read_text())["decisions"][2]["disposition"] == "WITHHOLD"


def test_evidence_mutation_between_hash_and_parse_cannot_approve(reviewed_fixture, monkeypatch):
    root, path, _ = reviewed_fixture
    evidence = root / "evidence.json"
    proof = json.loads(evidence.read_text())
    proof["entries"]["1"]["disposition"] = "WITHHOLD"
    write_json(evidence, proof)
    mutate_review(
        reviewed_fixture, lambda r: r["inputs"].update({"evidence.json": reviewed.digest(evidence)})
    )
    read_bytes, fired = Path.read_bytes, []

    def mutate_after_read(target):
        data = read_bytes(target)
        if target.resolve() == evidence.resolve() and not fired:
            fired.append(True)
            proof["entries"]["1"]["disposition"] = "SUPPORTED"
            write_json(evidence, proof)
        return data

    monkeypatch.setattr(Path, "read_bytes", mutate_after_read)
    with pytest.raises(ValueError, match="disagrees"):
        reviewed.load_review(root, path)
    assert fired


def test_source_metadata_mutation_during_review_rejected(reviewed_fixture, monkeypatch):
    root, path, _ = reviewed_fixture
    source = root / "source.sssom.tsv"
    read_bytes, fired = Path.read_bytes, []

    def mutate_after_read(target):
        data = read_bytes(target)
        if target.resolve() == source.resolve() and not fired:
            fired.append(True)
            source.write_bytes(data.replace(b"Canonical full mapping set", b"Modified after hash"))
        return data

    monkeypatch.setattr(Path, "read_bytes", mutate_after_read)
    with pytest.raises(ValueError, match="changed during"):
        reviewed.load_review(root, path)
    assert fired


def prepare_new_generation(fixture):
    root, path, output = fixture
    reviewed.export_reviewed(root, path, output)
    previous = {p.name: p.read_bytes() for p in output.iterdir()}
    proof = json.loads((root / "evidence.json").read_text())
    proof["entries"]["1"]["disposition"] = "WITHHOLD"
    write_json(root / "evidence.json", proof)

    def new_disposition(review):
        review["decisions"][0]["disposition"] = "WITHHOLD"
        review["inputs"]["evidence.json"] = reviewed.digest(root / "evidence.json")

    mutate_review(fixture, new_disposition)
    return previous


def test_failed_staged_write_preserves_complete_previous_publication(reviewed_fixture, monkeypatch):
    previous = prepare_new_generation(reviewed_fixture)
    _, _, output = reviewed_fixture
    write_bytes = Path.write_bytes

    def fail_second_file(path, data):
        if path.name == "withheld_mappings.sssom.tsv":
            raise OSError("simulated disk write failure")
        return write_bytes(path, data)

    monkeypatch.setattr(Path, "write_bytes", fail_second_file)
    with pytest.raises(OSError, match="disk write"):
        reviewed.export_reviewed(*reviewed_fixture)
    assert {p.name: p.read_bytes() for p in output.iterdir()} == previous


def test_failed_directory_install_restores_previous_publication(reviewed_fixture, monkeypatch):
    previous = prepare_new_generation(reviewed_fixture)
    _, _, output = reviewed_fixture
    rename = Path.rename

    def fail_install(path, target):
        if path.name == "new":
            raise OSError("simulated directory install failure")
        return rename(path, target)

    monkeypatch.setattr(Path, "rename", fail_install)
    with pytest.raises(OSError, match="directory install"):
        reviewed.export_reviewed(*reviewed_fixture)
    assert {p.name: p.read_bytes() for p in output.iterdir()} == previous


def test_input_change_during_install_rolls_back_previous_publication(reviewed_fixture, monkeypatch):
    previous = prepare_new_generation(reviewed_fixture)
    root, _, output = reviewed_fixture
    rename = Path.rename

    def mutate_after_install(path, target):
        result = rename(path, target)
        if path.name == "new":
            with (root / "evidence.json").open("a") as stream:
                stream.write("\n")
        return result

    monkeypatch.setattr(Path, "rename", mutate_after_install)
    with pytest.raises(ValueError, match="changed during"):
        reviewed.export_reviewed(*reviewed_fixture)
    assert {p.name: p.read_bytes() for p in output.iterdir()} == previous


def test_validate_only_rechecks_inputs_after_artifact_reads(reviewed_fixture, monkeypatch):
    root, path, output = reviewed_fixture
    reviewed.export_reviewed(root, path, output)
    read_bytes, fired = Path.read_bytes, []

    def mutate_after_output_read(target):
        data = read_bytes(target)
        if target == output / "ingredient_mappings.sssom.tsv" and not fired:
            fired.append(True)
            with (root / "evidence.json").open("a") as stream:
                stream.write("\n")
        return data

    monkeypatch.setattr(Path, "read_bytes", mutate_after_output_read)
    with pytest.raises(ValueError, match="changed during"):
        reviewed.validate_reviewed(root, path, output)


@pytest.mark.parametrize("confidence", ["not-a-number", "NaN", "Infinity", "-Infinity"])
def test_confidence_must_be_numeric_and_finite_without_normalization(reviewed_fixture, confidence):
    change_source_row(reviewed_fixture, {"confidence": confidence})
    with pytest.raises(ValueError, match="confidence"):
        reviewed.export_reviewed(*reviewed_fixture)
