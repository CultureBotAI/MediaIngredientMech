"""Source reconciliation must retain ambiguity, rejected names and review holds."""

import copy
import csv
import importlib.util
import io
import json
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "kgm_reconcile", ROOT / "scripts/reconcile_kgm_chemical_queue.py"
)
reconciler = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(reconciler)


def candidate(label="Sugar", source_id="source:1", **updates):
    item = {
        "source": "microbedecoder",
        "source_id": source_id,
        "category": "biolink:ChemicalEntity",
        "source_label": label,
        "raw_source_label": label,
        "occurrences": 1,
        "occurrences_definition": "native placeholder occurrence",
        **updates,
    }
    item["candidate_id"] = reconciler.candidate_id(item)
    return item


def owner(status="MAPPED", disposition="WITHHOLD"):
    return {
        "mapping_status": status,
        "native_review_rows": [{"decision": {"disposition": disposition}}],
    }


def hit(name="owner", resolving=True, kind="preferred_term"):
    return {"owner": name, "resolving": resolving, "kind": kind}


def test_identical_labels_preserve_distinct_source_owned_sugar_ids():
    candidates = [candidate(source_id="opaque:one"), candidate(source_id="opaque:two")]
    ledger, summary = reconciler.reconcile(candidates, {}, {}, {}, {})
    assert len(ledger) == 2
    assert {row["source_id"] for row in ledger} == {"opaque:one", "opaque:two"}
    assert len({row["candidate_id"] for row in ledger}) == 2
    assert len(summary["exact_casefold_label_groups"]) == 1
    assert len(summary["exact_casefold_label_groups"][0]["members"]) == 2
    assert summary["grouping_is_not_identity_merging"] is True
    assert not any(row["scientific_identity_approved_by_reconciliation"] for row in ledger)


def test_casefold_duplicate_owners_are_ambiguous_not_arbitrarily_selected():
    ledger, _ = reconciler.reconcile(
        [candidate("sUgAr")], {"a": owner(), "b": owner()}, {"sugar": [hit("a"), hit("b")]}, {}, {}
    )
    assert ledger[0]["resolving_owner_paths"] == ["a", "b"]
    assert "AMBIGUOUS_MULTIPLE_OWNERS" in ledger[0]["triage_flags"]


def test_supported_name_does_not_override_withheld_owner_or_downstream_hold():
    material = {
        ("microbedecoder", "source:1"): [
            {"row": {"identity_approved": "false", "predicate": "biolink:produces"}}
        ]
    }
    coverage = {"sugar": [{"disposition": "SUPPORTED", "row": {"predicate_id": "skos:broadMatch"}}]}
    ledger, _ = reconciler.reconcile(
        [candidate()], {"owner": owner()}, {"sugar": [hit()]}, coverage, material
    )
    assert set(ledger[0]["triage_flags"]) == {
        "DOWNSTREAM_MATERIAL_HOLD",
        "MATCHED_OWNER_HAS_WITHHELD_MAPPINGS",
        "CONSUMED_SUPPORTED_LEXICAL_COVERAGE",
    }
    assert ledger[0]["consumed_name_hits"][0]["row"]["predicate_id"] == "skos:broadMatch"
    assert ledger[0]["downstream_holds"] == material[("microbedecoder", "source:1")]
    assert ledger[0]["scientific_identity_approved_by_reconciliation"] is False


def test_withheld_export_token_never_counts_as_consumed_supported_coverage():
    ledger, _ = reconciler.reconcile(
        [candidate()],
        {"owner": owner()},
        {"sugar": [hit()]},
        {"sugar": [{"disposition": "WITHHOLD"}]},
        {},
    )
    assert "CONSUMED_SUPPORTED_LEXICAL_COVERAGE" not in ledger[0]["triage_flags"]
    assert "MIM_NAME_NOT_IN_CONSUMED_SUPPORTED_EXPORT" in ledger[0]["triage_flags"]
    assert ledger[0]["consumed_name_hits"][0]["disposition"] == "WITHHOLD"


def test_single_owner_ambiguous_record_is_not_presented_as_curated_identity():
    ledger, _ = reconciler.reconcile(
        [candidate()], {"owner": owner(status="AMBIGUOUS")}, {"sugar": [hit()]}, {}, {}
    )
    assert "MATCHED_AMBIGUOUS_OWNER" in ledger[0]["triage_flags"]
    assert ledger[0]["scientific_identity_approved_by_reconciliation"] is False


def test_blank_source_id_is_retained_as_unresolved():
    ledger, _ = reconciler.reconcile(
        [candidate("", "mediadive.ingredient:1944", source="mediadive")], {}, {}, {}, {}
    )
    assert ledger[0]["source_id"] == "mediadive.ingredient:1944"
    assert "BLANK_SOURCE_LABEL" in ledger[0]["triage_flags"]


@pytest.mark.parametrize("label", ["CaCl2·2H2O", "(R)-lactate", "Na acetate x 3 H2O", " sugar "])
def test_punctuation_hydration_stereochemistry_and_whitespace_are_not_stripped(label):
    ledger, _ = reconciler.reconcile(
        [candidate(label)],
        {"owner": owner()},
        {"cacl2": [hit()], "lactate": [hit()], "na acetate": [hit()], "sugar": [hit()]},
        {},
        {},
    )
    assert ledger[0]["name_hits"] == []


def test_raw_label_match_remains_separate_from_transformed_label():
    item = candidate("Nickel chloride", raw_source_label="Nickel chloride (hexahydrate)")
    ledger, _ = reconciler.reconcile(
        [item],
        {"raw-owner": owner(), "transformed-owner": owner()},
        {
            "nickel chloride": [hit("transformed-owner")],
            "nickel chloride (hexahydrate)": [hit("raw-owner")],
        },
        {},
        {},
    )
    assert {(entry["candidate_field"], entry["owner"]) for entry in ledger[0]["name_hits"]} == {
        ("source_label", "transformed-owner"),
        ("raw_source_label", "raw-owner"),
    }
    assert "AMBIGUOUS_MULTIPLE_OWNERS" in ledger[0]["triage_flags"]


def test_same_id_in_different_source_does_not_inherit_material_hold():
    holds = {("mediadive", "source:1"): [{"row": {"identity_approved": "false"}}]}
    ledger, _ = reconciler.reconcile([candidate()], {}, {}, {}, holds)
    assert ledger[0]["downstream_holds"] == []


def test_rejected_and_note_synonyms_are_visible_but_not_resolving(tmp_path):
    folder = tmp_path / "data/ingredients/mapped"
    folder.mkdir(parents=True)
    (folder / "Owner.yaml").write_text(
        yaml.safe_dump(
            {
                "preferred_term": "Owner",
                "mapping_status": "MAPPED",
                "identifier": "CHEBI:1",
                "synonyms": [
                    {"synonym_text": "sugar", "synonym_type": "REJECTED_LABEL"},
                    {"synonym_text": "produces: sugar", "synonym_type": "EXACT"},
                    {"synonym_text": "another sugar", "synonym_type": "EXACT"},
                ],
            }
        )
    )
    (folder / "Rejected.yaml").write_text(
        yaml.safe_dump({"preferred_term": "3-methylacetate", "mapping_status": "REJECTED"})
    )
    owners, index, hashes = reconciler.load_owners(
        tmp_path, {"rows": [], "decisions": [], "input_snapshot": {}}
    )
    assert len(hashes) == 2
    assert index["sugar"][0]["resolving"] is False
    assert index["produces: sugar"][0]["resolving"] is False
    assert index["another sugar"][0]["resolving"] is True
    ledger, _ = reconciler.reconcile([candidate("3-methylacetate")], owners, index, {}, {})
    assert ledger[0]["resolving_owner_paths"] == []
    assert ledger[0]["owners"][0]["mapping_status"] == "REJECTED"
    assert "NON_RESOLVING_OR_REJECTED_LABEL_ONLY" in ledger[0]["triage_flags"]


@pytest.mark.parametrize("field", list(reconciler.OBSERVATION_FIELDS))
def test_hold_matches_entire_native_assertion_including_predicate(field):
    hold = {key: f"value-{key}" for key in reconciler.OBSERVATION_FIELDS}
    graph = {target: hold[key] for key, target in reconciler.OBSERVATION_FIELDS.items()}
    reconciler.verify_observation_holds([hold], [graph])
    altered = dict(graph)
    altered[reconciler.OBSERVATION_FIELDS[field]] += "-changed"
    with pytest.raises(ValueError, match="exactly match"):
        reconciler.verify_observation_holds([hold], [altered])


def test_hold_witness_count_is_not_collapsed():
    hold = dict.fromkeys(reconciler.OBSERVATION_FIELDS, "same")
    graph = dict.fromkeys(reconciler.OBSERVATION_FIELDS.values(), "same")
    with pytest.raises(ValueError, match="exactly match"):
        reconciler.verify_observation_holds([hold, hold], [graph])


def write_tsv(path, rows, fields=None, prefix=""):
    stream = io.StringIO(newline="")
    stream.write(prefix)
    writer = csv.DictWriter(
        stream, fieldnames=fields or list(rows[0]), delimiter="\t", lineterminator="\n"
    )
    writer.writeheader()
    writer.writerows(rows)
    path.write_text(stream.getvalue())


def consumed_fixture(tmp_path):
    rows = [
        {
            "subject_id": "MIM:Sugar",
            "subject_label": "Sugar",
            "predicate_id": "skos:exactMatch",
            "object_id": "CHEBI:1",
            "object_label": "Sugar",
            "other": "sugar alias",
        },
        {
            "subject_id": "MIM:Hydrate",
            "subject_label": "Hydrate",
            "predicate_id": "skos:broadMatch",
            "object_id": "CHEBI:2",
            "object_label": "Parent",
            "other": "hydrated material",
        },
    ]
    prefix = "# mapping_set_id: https://example.org/reviewed\n# predicate_semantics: skos\n"
    write_tsv(tmp_path / reconciler.PRODUCTS[0], rows[:1], prefix=prefix)
    write_tsv(tmp_path / reconciler.PRODUCTS[1], rows[1:], prefix=prefix)
    dispositions = [
        {
            "source_position": str(i + 1),
            "row_sha256": reconciler.row_sha256(row),
            "subject_id": row["subject_id"],
            "predicate_id": row["predicate_id"],
            "object_id": row["object_id"],
            "owner_record": f"data/ingredients/mapped/{i}.yaml",
            "disposition": state,
        }
        for i, (row, state) in enumerate(zip(rows, ["SUPPORTED", "WITHHOLD"], strict=True))
    ]
    write_tsv(tmp_path / reconciler.PRODUCTS[2], dispositions)
    return refresh_consumed_manifest(tmp_path), rows, dispositions


def refresh_consumed_manifest(root):
    manifest = {
        "schema_version": 1,
        "semantic_status": "PASS_SUPPORTED_SUBSET",
        "source_sha256": "a" * 64,
        "counts": {"source": 2, "supported": 1, "withhold": 1},
        "files": {name: reconciler.digest(root / name) for name in reconciler.PRODUCTS},
    }
    (root / "manifest.json").write_bytes(reconciler.json_bytes(manifest))
    return {
        "files": {
            name: reconciler.digest(root / name) for name in (*reconciler.PRODUCTS, "manifest.json")
        }
    }


def test_consumed_partition_keeps_supported_and_withheld_name_channels(tmp_path):
    expected, _, _ = consumed_fixture(tmp_path)
    _, indexed, _ = reconciler.load_consumed(tmp_path, expected)
    assert indexed["sugar alias"][0]["matched_field"] == "other"
    assert indexed["sugar alias"][0]["disposition"] == "SUPPORTED"
    assert indexed["hydrated material"][0]["disposition"] == "WITHHOLD"
    assert indexed["hydrate"][0]["row"]["predicate_id"] == "skos:broadMatch"


def test_updated_checksums_cannot_move_withheld_row_into_supported_partition(tmp_path):
    _, rows, _ = consumed_fixture(tmp_path)
    prefix = "# mapping_set_id: https://example.org/reviewed\n# predicate_semantics: skos\n"
    write_tsv(tmp_path / reconciler.PRODUCTS[0], rows[1:], prefix=prefix)
    write_tsv(tmp_path / reconciler.PRODUCTS[1], rows[:1], prefix=prefix)
    expected = refresh_consumed_manifest(tmp_path)
    with pytest.raises(ValueError, match="partition rows differ"):
        reconciler.load_consumed(tmp_path, expected)


def test_consumed_input_changed_after_capture_is_refused(tmp_path):
    expected, _, _ = consumed_fixture(tmp_path)
    (tmp_path / reconciler.PRODUCTS[0]).write_text("unrelated replacement")
    with pytest.raises(ValueError, match="differs from captured source"):
        reconciler.load_consumed(tmp_path, expected)


def test_disposition_predicate_cannot_differ_even_with_recomputed_product_hash(tmp_path):
    _, _, dispositions = consumed_fixture(tmp_path)
    dispositions[0]["predicate_id"] = "skos:broadMatch"
    write_tsv(tmp_path / reconciler.PRODUCTS[2], dispositions)
    expected = refresh_consumed_manifest(tmp_path)
    with pytest.raises(ValueError, match="row identity differs"):
        reconciler.load_consumed(tmp_path, expected)


def snapshot_fixture(root):
    rows = [candidate(), candidate(source_id="source:2")]
    (root / "candidates.json").write_bytes(reconciler.json_bytes(rows))
    manifest = {
        "schema_version": 1,
        "files": {
            "candidates.json": {
                "sha256": reconciler.digest(root / "candidates.json"),
                "bytes": (root / "candidates.json").stat().st_size,
            }
        },
        "candidates": {
            "path": "candidates.json",
            "sha256": reconciler.digest(root / "candidates.json"),
            "rows": 2,
            "counts_by_source": {"microbedecoder": 2},
        },
        "hold_tables": [],
    }
    (root / "source-manifest.json").write_bytes(reconciler.json_bytes(manifest))
    return manifest, rows


def test_snapshot_binds_exact_candidate_bytes(tmp_path):
    snapshot_fixture(tmp_path)
    _, rows, _, _ = reconciler.load_snapshot(tmp_path)
    assert len(rows) == 2
    (tmp_path / "candidates.json").write_text("[]")
    with pytest.raises(ValueError, match="Changed source snapshot"):
        reconciler.load_snapshot(tmp_path)


def test_duplicate_source_identity_is_refused_even_with_new_snapshot_hash(tmp_path):
    manifest, rows = snapshot_fixture(tmp_path)
    rows[1] = copy.deepcopy(rows[0])
    path = tmp_path / "candidates.json"
    path.write_bytes(reconciler.json_bytes(rows))
    manifest["files"][path.name] = {"sha256": reconciler.digest(path), "bytes": path.stat().st_size}
    manifest["candidates"]["sha256"] = reconciler.digest(path)
    (tmp_path / "source-manifest.json").write_bytes(reconciler.json_bytes(manifest))
    with pytest.raises(ValueError, match="duplicate source candidate"):
        reconciler.load_snapshot(tmp_path)


@pytest.mark.parametrize("name", ["../outside.json", "/absolute/path"])
def test_snapshot_relative_paths_cannot_escape_root(tmp_path, name):
    with pytest.raises(ValueError, match="escapes root"):
        reconciler.relative_file(tmp_path, name)


def test_native_review_source_hash_gate_remains_mandatory(tmp_path):
    source = tmp_path / "mapping.tsv"
    source.write_text("current bytes")
    report = tmp_path / "review.json"
    report.write_text(
        json.dumps({"schema_version": 1, "source_sssom": source.name, "source_sha256": "0" * 64})
    )
    with pytest.raises(ValueError, match="Stale source SSSOM hash"):
        reconciler.load_review(tmp_path, report)


def test_whole_material_inventory_is_preserved_but_witness_scope_uses_exact_queue_ids(tmp_path):
    manifest, _ = snapshot_fixture(tmp_path)
    selected = dict.fromkeys(reconciler.OBSERVATION_FIELDS, "value")
    selected["object_curie"] = "source:1"
    unrelated = dict(selected, object_curie="not-in-current-queue")
    write_tsv(tmp_path / "holds.tsv", [selected, unrelated])
    graph = {target: selected[key] for key, target in reconciler.OBSERVATION_FIELDS.items()}
    write_tsv(tmp_path / "witness.tsv", [graph])
    for name in ("holds.tsv", "witness.tsv"):
        path = tmp_path / name
        manifest["files"][name] = {"sha256": reconciler.digest(path), "bytes": path.stat().st_size}
    manifest["hold_tables"] = [
        {
            "source": "microbedecoder",
            "path": "holds.tsv",
            "source_id_field": "object_curie",
            "exact_observation_witness": "witness.tsv",
        }
    ]
    (tmp_path / "source-manifest.json").write_bytes(reconciler.json_bytes(manifest))
    _, _, holds, hashes = reconciler.load_snapshot(tmp_path)
    assert list(holds) == [("microbedecoder", "source:1")]
    assert len(reconciler.tsv_rows(tmp_path / "holds.tsv")) == 2
    assert tmp_path / "holds.tsv" in hashes
    graph["predicate"] = "wrong-predicate"
    write_tsv(tmp_path / "witness.tsv", [graph])
    manifest["files"]["witness.tsv"] = {
        "sha256": reconciler.digest(tmp_path / "witness.tsv"),
        "bytes": (tmp_path / "witness.tsv").stat().st_size,
    }
    (tmp_path / "source-manifest.json").write_bytes(reconciler.json_bytes(manifest))
    with pytest.raises(ValueError, match="exactly match"):
        reconciler.load_snapshot(tmp_path)


def runnable_fixture(tmp_path):
    snapshot, mim, consumed = [tmp_path / name for name in ("snapshot", "mim", "consumed")]
    for folder in (snapshot, mim, consumed):
        folder.mkdir()
    manifest, _ = snapshot_fixture(snapshot)
    expected, _, _ = consumed_fixture(consumed)
    manifest["consumed_reviewed"] = expected
    manifest["upstream_root"] = str(tmp_path / "upstream-read-only")
    (snapshot / "source-manifest.json").write_bytes(reconciler.json_bytes(manifest))
    (mim / "data/ingredients/mapped").mkdir(parents=True)
    fields = ["subject_id", "subject_label", "predicate_id", "object_id", "object_label", "other"]
    source = mim / "source.tsv"
    write_tsv(
        source,
        [],
        fields=fields,
        prefix="# mapping_set_id: https://example.org/empty\n# predicate_semantics: skos\n",
    )
    (mim / "review.json").write_bytes(
        reconciler.json_bytes(
            {
                "schema_version": 1,
                "source_sssom": "source.tsv",
                "source_sha256": reconciler.digest(source),
                "inputs": {},
                "record_inputs": {},
                "decisions": [],
            }
        )
    )
    return snapshot, mim, consumed


def test_complete_read_only_run_keeps_consumed_generation_separate(tmp_path):
    snapshot, mim, consumed = runnable_fixture(tmp_path)
    before = {path: path.read_bytes() for path in tmp_path.rglob("*") if path.is_file()}
    output = tmp_path / "output"
    summary = reconciler.run(snapshot, mim, Path("review.json"), consumed, output)
    assert summary["candidate_count"] == 2
    assert summary["current_source_equals_consumed_source"] is False
    assert summary["consumed_partition_counts"] == {"source": 2, "supported": 1, "withhold": 1}
    assert all(path.read_bytes() == content for path, content in before.items())
    assert {path.name for path in output.iterdir()} == {
        "ledger.json",
        "ledger.tsv",
        "summary.json",
        "receipt.json",
    }
    receipt = json.loads((output / "receipt.json").read_bytes())
    assert receipt["scientific_review"] is False
    assert all(reconciler.digest(output / name) == sha for name, sha in receipt["outputs"].items())


def test_run_refuses_output_under_upstream_checkout(tmp_path):
    snapshot, mim, consumed = runnable_fixture(tmp_path)
    output = tmp_path / "upstream-read-only/report"
    with pytest.raises(ValueError, match="must not write to the upstream"):
        reconciler.run(snapshot, mim, Path("review.json"), consumed, output)
    assert not output.exists()


def test_run_refuses_existing_output_without_overwriting(tmp_path):
    snapshot, mim, consumed = runnable_fixture(tmp_path)
    output = tmp_path / "output"
    output.mkdir()
    (output / "ledger.json").write_text("existing annotation")
    with pytest.raises(ValueError, match="new directory"):
        reconciler.run(snapshot, mim, Path("review.json"), consumed, output)
    assert (output / "ledger.json").read_text() == "existing annotation"


def test_run_refuses_stale_native_review_before_creating_output(tmp_path):
    snapshot, mim, consumed = runnable_fixture(tmp_path)
    (mim / "source.tsv").write_text("changed bytes")
    output = tmp_path / "output"
    with pytest.raises(ValueError, match="Stale source SSSOM hash"):
        reconciler.run(snapshot, mim, Path("review.json"), consumed, output)
    assert not output.exists()


def test_1152_nested_backups_are_excluded_but_ignored_direct_children_are_included(tmp_path):
    mapped = tmp_path / "data/ingredients/mapped"
    backups = mapped / "backups"
    backups.mkdir(parents=True)
    old = backups / "Old.yaml"
    old.write_text(
        yaml.safe_dump(
            {
                "preferred_term": "Historical name",
                "mapping_status": "MAPPED",
                "synonyms": [{"synonym_text": "historical alias", "synonym_type": "EXACT"}],
            }
        )
    )
    current = mapped / "Current.yaml"
    current.write_text(
        yaml.safe_dump(
            {
                "preferred_term": "Current",
                "mapping_status": "MAPPED",
                "synonyms": [{"synonym_text": "current alias", "synonym_type": "EXACT"}],
            }
        )
    )
    (tmp_path / ".gitignore").write_text("data/ingredients/mapped/Current.yaml\n")
    owners, index, hashes = reconciler.load_owners(
        tmp_path, {"rows": [], "decisions": [], "input_snapshot": {}}
    )
    assert list(owners) == ["data/ingredients/mapped/Current.yaml"]
    assert set(index) == {"current", "current alias"}
    assert list(hashes) == [current]
    assert reconciler.record_paths(tmp_path) == [current]
    assert old.read_text().find("Historical name") >= 0


def test_run_refuses_output_in_mim_scientific_data_surface(tmp_path):
    snapshot, mim, consumed = runnable_fixture(tmp_path)
    output = mim / "data/ingredients/mapped/report"
    with pytest.raises(ValueError, match="maintained MIM data"):
        reconciler.run(snapshot, mim, Path("review.json"), consumed, output)
    assert not output.exists()


def test_1155_late_output_parent_swap_cannot_write_upstream(tmp_path, monkeypatch):
    snapshot, mim, consumed = runnable_fixture(tmp_path)
    upstream = tmp_path / "upstream-read-only"
    upstream.mkdir()
    parent = tmp_path / "safe-parent"
    parent.mkdir()
    original_load = reconciler.load_review

    def swapped_load(*args, **kwargs):
        parent.rmdir()
        parent.symlink_to(upstream, target_is_directory=True)
        return original_load(*args, **kwargs)

    monkeypatch.setattr(reconciler, "load_review", swapped_load)
    with pytest.raises(ValueError, match="directory component"):
        reconciler.run(snapshot, mim, Path("review.json"), consumed, parent / "report")
    assert list(upstream.iterdir()) == []


@pytest.mark.parametrize("replace", ["parent", "leaf"])
def test_1155_swap_after_directory_reservation_is_refused(tmp_path, monkeypatch, replace):
    snapshot, mim, consumed = runnable_fixture(tmp_path)
    upstream = tmp_path / "upstream-read-only"
    upstream.mkdir()
    parent = tmp_path / "safe-parent"
    parent.mkdir()
    output = parent / "report"
    original_publish = reconciler.ingredient_bundle_refresh.publish_new_files
    parked = tmp_path / "retained-directory"

    def swapped_publish(outputs, verify):
        target = parent if replace == "parent" else output
        target.rename(parked)
        target.symlink_to(upstream, target_is_directory=True)
        return original_publish(outputs, verify)

    monkeypatch.setattr(reconciler.ingredient_bundle_refresh, "publish_new_files", swapped_publish)
    with pytest.raises(ValueError, match="parent is aliased"):
        reconciler.run(snapshot, mim, Path("review.json"), consumed, output)
    assert list(upstream.iterdir()) == []
    assert not any(path.is_file() for path in parked.rglob("*"))


def test_1155_swap_after_file_reservation_removes_only_owned_files(tmp_path, monkeypatch):
    snapshot, mim, consumed = runnable_fixture(tmp_path)
    upstream = tmp_path / "upstream-read-only"
    upstream.mkdir()
    sentinel = upstream / "ledger.json"
    sentinel.write_text("unrelated upstream evidence")
    parent = tmp_path / "safe-parent"
    parent.mkdir()
    output = parent / "report"
    original_publish = reconciler.ingredient_bundle_refresh.publish_new_files
    parked = tmp_path / "retained-directory"

    def swapped_publish(outputs, verify):
        def swapped_verify():
            output.rename(parked)
            output.symlink_to(upstream, target_is_directory=True)
            verify()

        return original_publish(outputs, swapped_verify)

    monkeypatch.setattr(reconciler.ingredient_bundle_refresh, "publish_new_files", swapped_publish)
    with pytest.raises(ValueError, match="directory binding changed"):
        reconciler.run(snapshot, mim, Path("review.json"), consumed, output)
    assert list(upstream.iterdir()) == [sentinel]
    assert sentinel.read_text() == "unrelated upstream evidence"
    assert list(parked.iterdir()) == []


def test_1155_unaliased_nested_output_is_supported(tmp_path):
    snapshot, mim, consumed = runnable_fixture(tmp_path)
    output = tmp_path / "new-parent/nested/report"
    reconciler.run(snapshot, mim, Path("review.json"), consumed, output)
    assert {path.name for path in output.iterdir()} == {
        "ledger.json",
        "ledger.tsv",
        "summary.json",
        "receipt.json",
    }
