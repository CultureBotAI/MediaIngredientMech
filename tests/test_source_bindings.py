"""Candidate source identities require native independent evidence (#1299)."""

import copy
import importlib.util
import json
import shutil
import subprocess
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.export import reviewed_sssom as external
from mediaingredientmech.export import source_bindings as binding
from mediaingredientmech.stable_ids import MIM_PREFIX

ROOT = Path(__file__).resolve().parents[1]


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


class Fixture:
    def __init__(self, root):
        self.root = root
        self.review_path = root / "source-review.json"
        self.output = root / "candidate"
        for relative in (
            binding.HELPER,
            binding.SCHEMA,
            *binding.PRODUCER_PATHS,
            *binding.PRODUCER_AUXILIARY,
        ):
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)
        spec = importlib.util.spec_from_file_location(
            "source_binding_test_native", root / binding.HELPER
        )
        self.native = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.native)
        for args in (
            ("init",),
            ("config", "user.name", "Synthetic fixture"),
            ("config", "user.email", "fixture@example.invalid"),
            ("remote", "add", "origin", "https://github.com/CultureBotAI/MediaIngredientMech.git"),
            ("add", "."),
            ("commit", "-m", "Synthetic native review contract fixture"),
        ):
            subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)
        self.records = {}
        for i, name in enumerate(("Exact", "Hydrate", "Close", "Ungrounded", "Shared"), 1):
            category = "unmapped" if i == 4 else "mapped"
            path = f"data/ingredients/{category}/{name}.yaml"
            record = {
                "mim_id": f"MIM:{i:07d}",
                "identifier": (
                    "kgmicrobe.compound:hydrate"
                    if i == 2
                    else ("UNMAPPED_4" if i == 4 else "CHEBI:1" if i in {1, 5} else "CHEBI:3")
                ),
                "preferred_term": name,
                "mapping_status": "UNMAPPED" if i == 4 else "MAPPED",
                "legacy_identifiers": [
                    "MIM:" + name,
                    "CHEBI:1" if i in {1, 5} else "legacy:" + name,
                ],
                "synonyms": [],
            }
            self.records[path] = record
            target = root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(yaml.safe_dump(record))
        (root / "data/ids").mkdir()
        (root / binding.REGISTRY_PATH).write_text(
            "mim_id\tlabel_at_minting\tminted_on\tstatus\treplaced_by\n"
            + "".join(
                f"MIM:{i:07d}\t{name}\t2026-01-01\tactive\t\n"
                for i, name in enumerate(("Exact", "Hydrate", "Close", "Ungrounded", "Shared"), 1)
            )
        )
        (root / binding.LIFECYCLE_PATH).write_text(
            "mim_id\tstatus\treplaced_by\tchanged_at\treason\n"
        )
        (root / "nodes.tsv").write_text(
            "id\tname\tform\n"
            + "".join(
                f"SOURCE:{i}\t{name}\t{form}\n"
                for i, (name, form) in enumerate(
                    (
                        ("raw exact", "anhydrous"),
                        ("raw hydrate", "monohydrate"),
                        ("raw close", "specified"),
                        ("raw unresolved", "mixture"),
                    ),
                    1,
                )
            )
        )
        (root / "occurrences.tsv").write_text(
            "source_id\trecipe\tquantity\nSOURCE:1\tA\t2 mg\nSOURCE:2\tB\t1 g\nSOURCE:2\tC\t2 g\nSOURCE:3\tD\t1 g\nSOURCE:4\tE\t1 ml\n"
        )
        (root / "primary-source.txt").write_text(
            "Synthetic primary evidence fixture; not a real scientific approval.\n"
        )
        self.make_external()
        self.review = {
            "schema_version": 1,
            "capability": binding.CAPABILITY,
            "source": {
                "nodes": "nodes.tsv",
                "nodes_sha256": external.digest(root / "nodes.tsv"),
                "occurrences": "occurrences.tsv",
                "occurrences_sha256": external.digest(root / "occurrences.tsv"),
                "id_column": "id",
                "label_column": "name",
                "occurrence_id_column": "source_id",
                "curie_map": {"SOURCE": "https://example.invalid/source/"},
            },
            "record_inputs": {path: external.digest(root / path) for path in self.records},
            "ledger_inputs": {
                str(path): external.digest(root / path)
                for path in (binding.REGISTRY_PATH, binding.LIFECYCLE_PATH)
            },
            "inputs": {},
            "external_review": {
                "path": "external-review.json",
                "sha256": external.digest(root / "external-review.json"),
            },
            "cases": [
                {
                    "source_position": i,
                    "owner_record": path,
                    "holds": [],
                    "primary": None,
                    "skeptic": None,
                }
                for i, path in enumerate(list(self.records)[:4], 1)
            ],
        }
        self.seal()

    def make_external(self):
        (self.root / binding.EXTERNAL_SOURCE).parent.mkdir(parents=True, exist_ok=True)
        rows, decisions, owners, entries = [], [], {}, {}
        for index, (owner, predicate, obj) in enumerate(
            (
                (list(self.records)[0], "skos:exactMatch", "CHEBI:1"),
                (list(self.records)[1], "skos:broadMatch", "CHEBI:2"),
                (list(self.records)[1], "skos:exactMatch", "kgmicrobe.compound:hydrate"),
                (list(self.records)[2], "skos:closeMatch", "CHEBI:3"),
            ),
            1,
        ):
            record = self.records[owner]
            row = {
                "subject_id": record["mim_id"],
                "subject_label": record["preferred_term"],
                "predicate_id": predicate,
                "mapping_justification": "semapv:ManualMappingCuration",
                "object_id": obj,
                "object_label": "external label",
                "comment": "Preserve exact historical commentary",
                "source": "curator:original",
                "mapping_date": "2026-01-01",
                "other": "",
            }
            rows.append(row)
            owners[owner] = external.digest(self.root / owner)
            decision = {
                "source_position": index,
                "owner_record": owner,
                "row_sha256": external.row_sha256(row),
                "disposition": "SUPPORTED",
                "review_reason": "Synthetic original external review",
                "review_evidence": "external-evidence.json",
                "evidence_key": str(index),
            }
            decisions.append(decision)
            entries[str(index)] = {
                key: decision[key] for key in ("row_sha256", "disposition", "review_reason")
            }
            entries[str(index)]["owner_record_sha256"] = owners[owner]
        (self.root / binding.EXTERNAL_SOURCE).write_bytes(
            (
                "# mapping_set_id: https://example.invalid/fixture\n# predicate_semantics: skos\n# license: https://creativecommons.org/publicdomain/zero/1.0/\n# curie_map:\n#   MIM: "
                + MIM_PREFIX
                + "\n#   CHEBI: http://purl.obolibrary.org/obo/CHEBI_\n#   kgmicrobe.compound: https://w3id.org/kg-microbe/compound/\n#   skos: http://www.w3.org/2004/02/skos/core#\n#   semapv: https://w3id.org/semapv/vocab/\n"
            ).encode()
            + external._tsv(list(rows[0]), rows)
        )
        write_json(self.root / "external-evidence.json", {"entries": entries})
        write_json(
            self.root / "external-review.json",
            {
                "schema_version": 1,
                "source_sssom": binding.EXTERNAL_SOURCE,
                "source_sha256": external.digest(self.root / binding.EXTERNAL_SOURCE),
                "inputs": {
                    "external-evidence.json": external.digest(self.root / "external-evidence.json")
                },
                "record_inputs": owners,
                "decisions": decisions,
            },
        )

    def save(self):
        write_json(self.review_path, self.review)

    def seal(self, *, withheld=(), alter=None):
        self.review["inputs"] = {}
        self.save()
        inspection = binding.inspect_candidates(self.root, self.review_path)
        self.reports = []
        for role in ("primary", "skeptic"):
            targets = inspection["targets"]
            source = self.native.inspect_source(
                self.root, targets, [*inspection["inputs"], "primary-source.txt"]
            )["source"]
            report = {
                "schema_version": "1.0.0",
                "review_id": "20260101T000000Z-source-" + role,
                "kind": "batch",
                "repository": binding.REPOSITORY,
                "title": "Synthetic source identity contract",
                "started_at": "2026-01-01T00:00:00Z",
                "finished_at": "2026-01-01T00:00:00Z",
                "reviewer": {
                    "identity": role,
                    "kind": "human",
                    "independence": "independent" if role == "skeptic" else "self_review",
                    "independence_basis": "Separate synthetic test reviewer",
                },
                "skill": "review-sssom-output",
                "completion": "completed",
                "verdict": "needs_curation" if withheld else "pass",
                "scientific_review": True,
                "summary": "Synthetic fixture only",
                "source": source,
                "targets": targets,
                "scope": {
                    "description": "Every source entity and occurrence",
                    "selection": "Complete fixture",
                    "coverage": "full",
                    "population_size": len(targets),
                    "reviewed_target_ids": [target["target_id"] for target in targets],
                },
                "checks": [
                    {
                        "check_id": "identity",
                        "name": "Complete source identity",
                        "required": True,
                        "status": "passed",
                        "summary": "Inspected complete fixture payloads",
                        "target_ids": [target["target_id"] for target in targets],
                        "evidence_ids": ["primary"],
                    }
                ],
                "evidence": [
                    {
                        "evidence_id": "primary",
                        "kind": "primary_source",
                        "reference": "primary-source.txt",
                        "snapshot_sha256": external.digest(self.root / "primary-source.txt"),
                        "accessed_at": "2026-01-01T00:00:00Z",
                        "support": "supports",
                        "summary": "Synthetic primary evidence",
                    }
                ],
                "assessments": [],
                "findings": [],
                "actions": [],
                "limitations": [],
            }
            for i, target in enumerate(targets, 1):
                held = i in withheld
                report["assessments"].append(
                    {
                        "assessment_id": "identity-" + str(i),
                        "area": "identity",
                        "topic": "Complete source/material identity",
                        "outcome": "unknown" if held else "supported",
                        "summary": (
                            "Source identity unresolved"
                            if held
                            else "Same material over every captured occurrence"
                        ),
                        "target_ids": [target["target_id"]],
                        "evidence_ids": ["primary"],
                        "dimensions": [
                            {
                                "name": "source_identity_scope",
                                "value": "all_source_occurrences",
                                "definition": "All original occurrences, including preparation and alternative qualifiers",
                                "evidence_ids": ["primary"],
                            },
                            {
                                "name": "source_identity_disposition",
                                "value": "withhold" if held else "same_material",
                                "definition": "Explicit scientific identity conclusion",
                                "evidence_ids": ["primary"],
                            },
                        ],
                    }
                )
            # A withheld claim does not invalidate other positively reviewed targets.
            if withheld:
                report["verdict"] = "needs_curation"
            if alter:
                alter(role, report)
            relative = f"reviews/structured/{report['review_id']}/review.yaml"
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(yaml.safe_dump(report, sort_keys=False))
            destination.with_name("review.md").write_text(self.native.render_markdown(report))
            self.reports.append(report)
            for file in (destination, destination.with_name("review.md")):
                self.review["inputs"][file.relative_to(self.root).as_posix()] = external.digest(
                    file
                )
            for i, case in enumerate(self.review["cases"], 1):
                case[role] = {
                    "path": relative,
                    "target_id": "source-" + str(i),
                    "assessment_id": "identity-" + str(i),
                }
        self.save()


@pytest.fixture
def fixture(tmp_path):
    return Fixture(tmp_path)


def test_complete_candidate_preserves_external_predicates_and_mim_only(fixture):
    f = fixture
    manifest = binding.export_candidate(f.root, f.review_path, f.output)
    assert manifest["counts"] == {
        "source_entities": 4,
        "source_occurrences": 5,
        "supported": 4,
        "withheld": 0,
        "withheld_without_owner": 0,
    }
    assert manifest["production_authorized"] is False
    assert binding.validate_candidate(f.root, f.review_path, f.output) == manifest
    original = external.expected_products(f.root, f.root / "external-review.json")[0]
    for name, raw in original.items():
        assert (f.output / ("external-" + name)).read_bytes() == raw
    claims = binding.consumer_claims(
        f.root, f.review_path, f.output, capabilities={binding.CAPABILITY}
    )
    assert [claim["object_id"] for claim in claims] == [
        f"MIM.ingredient:{i:07d}" for i in range(1, 5)
    ]
    assert all(claim["predicate_id"] == "skos:exactMatch" for claim in claims)
    assert claims[-1]["original_subject_id"] == "SOURCE:4"
    cases = json.loads((f.output / "source-decisions.json").read_bytes())
    assert cases[-1]["payload"]["mapping_status"] == "UNMAPPED"
    assert cases[-1]["payload"]["mim_id"] == "MIM:0000004"
    assert len(cases[1]["payload"]["occurrences"]) == 2
    assert not any("subclass" in claim["predicate_id"] for claim in claims)
    assert manifest["curie_map"] == {"MIM": MIM_PREFIX, "MIM.ingredient": MIM_PREFIX}
    assert binding.expand_mim("MIM:0000004") == binding.expand_mim("MIM.ingredient:0000004")


@pytest.mark.parametrize(
    "name",
    [
        "nodes.tsv",
        "occurrences.tsv",
        "primary-source.txt",
        "data/ingredients/unmapped/Ungrounded.yaml",
        "data/ids/mim_id_registry.tsv",
    ],
)
def test_changed_source_occurrence_owner_or_evidence_cannot_inherit_review(fixture, name):
    with (fixture.root / name).open("a") as stream:
        stream.write("\n")
    with pytest.raises(ValueError):
        binding.expected_products(fixture.root, fixture.review_path)


@pytest.mark.parametrize(
    "attack",
    [
        "missing",
        "same_reviewer",
        "scope",
        "digest",
        "label_evidence",
        "source_hash",
        "different_owner",
        "no_source_identity",
    ],
)
def test_native_identity_proof_attacks_fail(fixture, attack):
    def alter(role, report):
        if role != "skeptic":
            return
        if attack == "missing":
            report["assessments"][0]["dimensions"].pop()
        elif attack == "same_reviewer":
            report["reviewer"]["identity"] = "primary"
        elif attack == "scope":
            report["assessments"][0]["dimensions"][0]["value"] = "label_only"
        elif attack == "digest":
            report["targets"][0]["semantic_digest"]["sha256"] = "0" * 64
        elif attack == "label_evidence":
            report["evidence"][0]["kind"] = "record_content"
        elif attack == "source_hash":
            report["source"]["inputs"][0]["sha256"] = "0" * 64
        elif attack == "different_owner":
            report["targets"][0]["owner_paths"][0]["path"] = list(fixture.records)[4]
        elif attack == "no_source_identity":
            report["assessments"][0]["area"] = "grounding"

    fixture.seal(alter=alter)
    with pytest.raises(ValueError):
        binding.expected_products(fixture.root, fixture.review_path)


def test_duplicate_source_key_cannot_gain_two_owners_through_labels(fixture):
    source = fixture.root / "nodes.tsv"
    source.write_text(source.read_text().replace("SOURCE:2", "SOURCE:1"))
    fixture.review["source"]["nodes_sha256"] = external.digest(source)
    fixture.save()
    with pytest.raises(ValueError, match="unique CURIEs"):
        binding.inspect_candidates(fixture.root, fixture.review_path)


def test_shared_external_alias_does_not_select_an_owner(fixture):
    # Exact and Shared both retain CHEBI:1. No external-ID lookup is attempted.
    fixture.review["cases"][0]["owner_record"] = "CHEBI:1"
    fixture.save()
    with pytest.raises(ValueError, match="unknown proposed owner"):
        binding.expected_products(fixture.root, fixture.review_path)


def test_changed_owner_cannot_reuse_native_report_even_after_manifest_rehash(fixture):
    owner = list(fixture.records)[0]
    (fixture.root / owner).write_text(
        (fixture.root / owner).read_text().replace("Exact", "Renamed")
    )
    fixture.review["record_inputs"][owner] = external.digest(fixture.root / owner)
    fixture.save()
    with pytest.raises(ValueError):
        binding.expected_products(fixture.root, fixture.review_path)


def test_held_case_cannot_be_supported(fixture):
    fixture.review["cases"][0]["holds"] = ["Alternative preparation has unresolved supplied form"]
    fixture.seal()
    with pytest.raises(ValueError, match="held/ambiguous"):
        binding.expected_products(fixture.root, fixture.review_path)


def test_consumer_refuses_unknown_capability_and_tampered_payload(fixture):
    binding.export_candidate(fixture.root, fixture.review_path, fixture.output)
    with pytest.raises(ValueError, match="capability"):
        binding.consumer_claims(
            fixture.root, fixture.review_path, fixture.output, capabilities=set()
        )
    decisions = fixture.output / "source-decisions.json"
    raw = json.loads(decisions.read_bytes())
    raw[0]["binding"]["object_id"] = "MIM:0000005"
    write_json(decisions, raw)
    manifest = json.loads((fixture.output / "manifest.json").read_bytes())
    manifest["files"][decisions.name] = external.digest(decisions)
    write_json(fixture.output / "manifest.json", manifest)
    with pytest.raises(ValueError, match="candidate bytes differ"):
        binding.validate_candidate(fixture.root, fixture.review_path, fixture.output)


def test_output_reservation_and_symlink_refusal(fixture):
    fixture.output.mkdir()
    (fixture.output / "keep").write_text("unrelated")
    with pytest.raises(ValueError, match="already exists"):
        binding.export_candidate(fixture.root, fixture.review_path, fixture.output)
    assert (fixture.output / "keep").read_text() == "unrelated"
    alias = fixture.root / "alias"
    alias.symlink_to(fixture.output, target_is_directory=True)
    with pytest.raises(ValueError, match="symlink"):
        binding.export_candidate(fixture.root, fixture.review_path, alias)


def test_held_and_ownerless_cases_remain_in_complete_accounting(fixture):
    fixture.review["cases"][0]["holds"] = ["Conflicting preparation identities remain unresolved"]
    fixture.review["cases"][3]["owner_record"] = None
    fixture.seal(withheld={1, 4})
    manifest = binding.export_candidate(fixture.root, fixture.review_path, fixture.output)
    assert manifest["counts"] == {
        "source_entities": 4,
        "source_occurrences": 5,
        "supported": 2,
        "withheld": 2,
        "withheld_without_owner": 1,
    }
    cases = json.loads((fixture.output / "source-decisions.json").read_bytes())
    assert cases[0]["payload"]["holds"] == ["Conflicting preparation identities remain unresolved"]
    assert cases[3]["payload"]["owner_record"] is None
    assert sum(len(case["payload"]["occurrences"]) for case in cases) == 5


def test_rename_and_alias_change_retains_id_after_fresh_review(fixture):
    old = list(fixture.records)[3]
    new = "data/ingredients/unmapped/Renamed_material.yaml"
    record = copy.deepcopy(fixture.records.pop(old))
    record["preferred_term"] = "Renamed material"
    record["legacy_identifiers"].append("MIM:Another_old_name")
    (fixture.root / old).unlink()
    (fixture.root / new).write_text(yaml.safe_dump(record))
    fixture.records[new] = record
    fixture.review["record_inputs"].pop(old)
    fixture.review["record_inputs"][new] = external.digest(fixture.root / new)
    fixture.review["cases"][3]["owner_record"] = new
    fixture.seal()
    binding.export_candidate(fixture.root, fixture.review_path, fixture.output)
    claims = binding.consumer_claims(
        fixture.root, fixture.review_path, fixture.output, capabilities={binding.CAPABILITY}
    )
    assert claims[-1]["object_id"] == "MIM.ingredient:0000004"
    assert claims[-1]["object_label"] == "Renamed material"


def test_no_external_mapping_is_required_for_reviewed_mim_only(fixture):
    source = fixture.root / binding.EXTERNAL_SOURCE
    metadata, fields, _ = external.read_sssom(source)
    source.write_bytes(
        "".join("# " + line + "\n" for line in yaml.safe_dump(metadata).splitlines()).encode()
        + external._tsv(fields, [])
    )
    review = json.loads((fixture.root / "external-review.json").read_bytes())
    review.update(source_sha256=external.digest(source), record_inputs={}, decisions=[])
    write_json(fixture.root / "external-review.json", review)
    fixture.review["external_review"]["sha256"] = external.digest(
        fixture.root / "external-review.json"
    )
    fixture.save()
    manifest = binding.export_candidate(fixture.root, fixture.review_path, fixture.output)
    assert manifest["external_counts"] == {"source": 0, "supported": 0, "withhold": 0}
    assert manifest["counts"]["supported"] == 4
    assert "MIM:0000004" in (fixture.output / "source-bindings.sssom.tsv").read_text()


def test_external_withhold_does_not_withhold_reviewed_source(fixture):
    path = fixture.root / "external-review.json"
    review = json.loads(path.read_bytes())
    review["decisions"][0]["disposition"] = "WITHHOLD"
    proof_path = fixture.root / "external-evidence.json"
    proof = json.loads(proof_path.read_bytes())
    proof["entries"]["1"]["disposition"] = "WITHHOLD"
    write_json(proof_path, proof)
    review["inputs"]["external-evidence.json"] = external.digest(proof_path)
    write_json(path, review)
    fixture.review["external_review"]["sha256"] = external.digest(path)
    fixture.save()
    manifest = binding.export_candidate(fixture.root, fixture.review_path, fixture.output)
    assert manifest["external_counts"]["withhold"] == 1
    assert manifest["counts"]["supported"] == 4


def test_namespace_change_cannot_inherit_source_review(fixture):
    fixture.review["source"]["curie_map"]["SOURCE"] = "https://different.example.invalid/"
    fixture.save()
    with pytest.raises(ValueError, match="complete identity payload"):
        binding.expected_products(fixture.root, fixture.review_path)


def test_source_drift_at_final_validation_leaves_explicit_failed_candidate(fixture, monkeypatch):
    original = binding.validate_candidate

    def change_after_reservation(root, review, output):
        if Path(output) == fixture.output:
            with (fixture.root / "occurrences.tsv").open("a") as stream:
                stream.write("SOURCE:1\tnew-context\t3 mg\n")
        return original(root, review, output)

    # #1305 executes the private captured implementation, not public cache state.
    monkeypatch.setitem(
        binding.export_candidate.__globals__, "validate_candidate", change_after_reservation
    )
    with pytest.raises(ValueError, match="stale input"):
        binding.export_candidate(fixture.root, fixture.review_path, fixture.output)
    failure = json.loads((fixture.output / "FAILED.json").read_bytes())
    assert failure["status"] == "FAILED_INCOMPLETE_CANDIDATE"
    assert (fixture.output / "source-decisions.json").is_file()


def test_native_markdown_mismatch_and_input_symlink_refused(fixture):
    report = fixture.root / fixture.review["cases"][0]["primary"]["path"]
    report.with_name("review.md").write_text("Misleading independent result")
    relative = report.with_name("review.md").relative_to(fixture.root).as_posix()
    fixture.review["inputs"][relative] = external.digest(report.with_name("review.md"))
    fixture.save()
    with pytest.raises(ValueError, match="Markdown"):
        binding.expected_products(fixture.root, fixture.review_path)
    nodes = fixture.root / "nodes.tsv"
    nodes.rename(fixture.root / "real-nodes.tsv")
    nodes.symlink_to(fixture.root / "real-nodes.tsv")
    with pytest.raises(ValueError, match="symlink"):
        binding.inspect_candidates(fixture.root, fixture.review_path)


def test_smaller_external_table_is_not_current_canonical_partition(fixture):
    original = fixture.root / binding.EXTERNAL_SOURCE
    smaller = fixture.root / "smaller.tsv"
    smaller.write_bytes(original.read_bytes())
    review_path = fixture.root / "external-review.json"
    review = json.loads(review_path.read_bytes())
    review["source_sssom"] = "smaller.tsv"
    write_json(review_path, review)
    fixture.review["external_review"]["sha256"] = external.digest(review_path)
    fixture.save()
    with pytest.raises(ValueError, match="current root canonical"):
        binding.expected_products(fixture.root, fixture.review_path)


def test_ownerless_empty_sssom_partitions_validate_without_inventing_objects(fixture):
    for case in fixture.review["cases"]:
        case["owner_record"] = None
    fixture.seal(withheld={1, 2, 3, 4})
    manifest = binding.export_candidate(fixture.root, fixture.review_path, fixture.output)
    assert manifest["counts"]["supported"] == 0
    assert manifest["counts"]["withheld"] == manifest["counts"]["withheld_without_owner"] == 4
    cases = json.loads((fixture.output / "source-decisions.json").read_bytes())
    assert len(cases) == 4 and all(case["payload"]["owner_record"] is None for case in cases)
    assert (
        binding.consumer_claims(
            fixture.root, fixture.review_path, fixture.output, capabilities={binding.CAPABILITY}
        )
        == []
    )


def test_cli_inspection_and_validation_use_actual_native_candidate(fixture):
    binding.export_candidate(fixture.root, fixture.review_path, fixture.output)
    import sys

    for extra in (("--inspect",), ("--output", str(fixture.output), "--validate-only")):
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "mediaingredientmech.export.source_bindings",
                "--root",
                str(fixture.root),
                "--review",
                str(fixture.review_path),
                *extra,
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        actual = json.loads(result.stdout)
        assert actual.get("status", actual.get("semantic_status")) in {
            "inspection_only",
            "REVIEWED_CANDIDATE_ONLY",
        }


def test_distinct_reviewed_owners_sharing_external_id_are_not_collapsed(fixture):
    nodes = fixture.root / "nodes.tsv"
    nodes.write_text(nodes.read_text() + "SOURCE:5\traw shared\tanhydrous\n")
    occurrences = fixture.root / "occurrences.tsv"
    occurrences.write_text(occurrences.read_text() + "SOURCE:5\tF\t1 g\n")
    fixture.review["source"].update(
        nodes_sha256=external.digest(nodes), occurrences_sha256=external.digest(occurrences)
    )
    fixture.review["cases"].append(
        {
            "source_position": 5,
            "owner_record": list(fixture.records)[4],
            "holds": [],
            "primary": None,
            "skeptic": None,
        }
    )
    fixture.seal()
    binding.export_candidate(fixture.root, fixture.review_path, fixture.output)
    claims = binding.consumer_claims(
        fixture.root, fixture.review_path, fixture.output, capabilities={binding.CAPABILITY}
    )
    assert claims[0]["object_id"] == "MIM.ingredient:0000001"
    assert claims[-1]["object_id"] == "MIM.ingredient:0000005"
    assert (
        fixture.records[list(fixture.records)[0]]["identifier"]
        == fixture.records[list(fixture.records)[4]]["identifier"]
        == "CHEBI:1"
    )


def test_source_identity_self_loop_and_reserved_namespace_refused(fixture):
    nodes = fixture.root / "nodes.tsv"
    nodes.write_text(nodes.read_text().replace("SOURCE:1", "MIM:0000001"))
    occurrences = fixture.root / "occurrences.tsv"
    occurrences.write_text(occurrences.read_text().replace("SOURCE:1", "MIM:0000001"))
    fixture.review["source"].update(
        nodes_sha256=external.digest(nodes), occurrences_sha256=external.digest(occurrences)
    )
    fixture.review["source"]["curie_map"]["MIM"] = MIM_PREFIX
    fixture.seal()
    with pytest.raises(ValueError, match="self-loop"):
        binding.expected_products(fixture.root, fixture.review_path)
    fixture.review["source"]["curie_map"]["MIM"] = "https://omim.org/entry/"
    fixture.save()
    with pytest.raises(ValueError, match="conflicting reserved namespace"):
        binding.inspect_candidates(fixture.root, fixture.review_path)


def test_cached_native_reports_still_recheck_changed_inputs(fixture, monkeypatch):
    original = binding._native
    calls = []

    def native_with_count(inputs):
        native = original(inputs)
        parse = native.parse_review_bundle

        def counted(*args, **kwargs):
            calls.append(args[0])
            result = parse(*args, **kwargs)
            if len(calls) == 2:
                with (fixture.root / "nodes.tsv").open("a") as stream:
                    stream.write("SOURCE:9\tconcurrent addition\tunknown\n")
            return result

        native.parse_review_bundle = counted
        return native

    # #1305 preserves this negative injection at the actual executing namespace.
    monkeypatch.setitem(binding.expected_products.__globals__, "_native", native_with_count)
    with pytest.raises(ValueError, match="stale input"):
        binding.expected_products(fixture.root, fixture.review_path)
    assert len(calls) == 2


def test_producer_receipt_binds_exact_code_lock_git_and_runtime(fixture):
    """#1305 keeps producer provenance distinct from scientific review."""
    manifest = binding.export_candidate(fixture.root, fixture.review_path, fixture.output)
    producer = json.loads((fixture.output / "producer.json").read_bytes())
    for path in (
        *binding.PRODUCER_PATHS,
        *binding.PRODUCER_AUXILIARY,
        binding.HELPER,
        binding.SCHEMA,
    ):
        assert producer["files"][path] == external.digest(fixture.root / path)
        assert manifest["inputs"][path] == producer["files"][path]
    assert (
        producer["selected_context"]["git_revision"]
        == subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=fixture.root, text=True
        ).strip()
    )
    assert producer["selected_context"]["state"] == "working_tree"
    assert producer["runtime"]["python"].startswith("3.13.")
    assert producer["generation_origin"]["root"] == str(ROOT)
    assert producer["status"] == "GENERATION_CONTEXT_ATTESTATION"


@pytest.mark.parametrize(
    "path",
    [
        "src/mediaingredientmech/export/source_bindings.py",
        "src/mediaingredientmech/review_claims.py",
        "src/mediaingredientmech/identity_projection.py",
        "uv.lock",
        "pyproject.toml",
        ".python-version",
    ],
)
def test_selected_producer_or_dependency_mismatch_is_refused(fixture, path):
    """#1305: the selected producer cannot advertise bytes that did not execute."""
    with (fixture.root / path).open("a") as stream:
        stream.write("\n# Changed private selected-root bytes\n")
    with pytest.raises(ValueError, match="executing and selected producer bytes differ"):
        binding.expected_products(fixture.root, fixture.review_path)
    assert not fixture.output.exists()


def test_candidate_revalidation_refuses_later_producer_drift(fixture):
    """#1305: an old candidate cannot acquire a fresh producer hash silently."""
    binding.export_candidate(fixture.root, fixture.review_path, fixture.output)
    with (fixture.root / "uv.lock").open("a") as stream:
        stream.write("\n# Later dependency epoch\n")
    with pytest.raises(ValueError, match="executing and selected producer bytes differ"):
        binding.validate_candidate(fixture.root, fixture.review_path, fixture.output)


@pytest.mark.parametrize("change", ["head", "lock", "producer"])
def test_mid_execution_context_drift_refused(fixture, monkeypatch, change):
    """#1305 late boundary retains original source and producer observations."""
    original = binding._native

    def changed(inputs):
        native = original(inputs)
        if change == "head":
            subprocess.run(
                ["git", "commit", "--allow-empty", "-m", "Synthetic context change"],
                cwd=fixture.root,
                capture_output=True,
                check=True,
            )
        else:
            path = "uv.lock" if change == "lock" else "src/mediaingredientmech/review_claims.py"
            with (fixture.root / path).open("a") as stream:
                stream.write("\n# Concurrent private context change\n")
        return native

    monkeypatch.setitem(binding.expected_products.__globals__, "_native", changed)
    with pytest.raises(ValueError, match="stale input|Git HEAD changed"):
        binding.expected_products(fixture.root, fixture.review_path)


def _private_python(fixture, code):
    import sys

    return subprocess.run(
        [sys.executable, "-c", code, str(fixture.root)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )


def test_equal_byte_isolated_validator_preserves_original_generation_origin(fixture):
    """#1305 allows identical compiled code at another honest consumer root."""
    binding.export_candidate(fixture.root, fixture.review_path, fixture.output)
    before = (fixture.output / "producer.json").read_bytes()
    result = _private_python(
        fixture,
        """
import importlib.util,json,sys
from pathlib import Path
root=Path(sys.argv[1])
spec=importlib.util.spec_from_file_location("isolated_source_api",root/"src/mediaingredientmech/export/source_bindings.py")
api=importlib.util.module_from_spec(spec);spec.loader.exec_module(api)
result=api.validate_candidate(root,root/"source-review.json",root/"candidate")
assert api._PRODUCER_CAPTURE.root == root
print(json.dumps({"status":result["semantic_status"],"actual_validator_root":str(api._PRODUCER_CAPTURE.root)}))
""",
    )
    assert json.loads(result.stdout)["actual_validator_root"] == str(fixture.root)
    assert (fixture.output / "producer.json").read_bytes() == before
    assert json.loads(before)["generation_origin"]["root"] == str(ROOT)


def test_preloaded_stale_dependency_is_not_reused_or_reloaded(fixture):
    """#1305/#1195: compile new captured bytes; leave the public old cache alone."""
    result = _private_python(
        fixture,
        """
import importlib.util,json,sys,hashlib
from pathlib import Path
root=Path(sys.argv[1]);path=root/"src/mediaingredientmech/review_claims.py"
path.write_bytes(path.read_bytes()+b"\\nCAPTURE_VERSION = 'old'\\n")
spec=importlib.util.spec_from_file_location("mediaingredientmech.review_claims",path)
old=importlib.util.module_from_spec(spec);sys.modules[spec.name]=old;spec.loader.exec_module(old)
old_function=old.payload_sha256
path.write_bytes(path.read_bytes()+b"\\nCAPTURE_VERSION = 'new'\\n")
spec=importlib.util.spec_from_file_location("isolated_source_api",root/"src/mediaingredientmech/export/source_bindings.py")
api=importlib.util.module_from_spec(spec);spec.loader.exec_module(api)
private=api._PRODUCER_CAPTURE.modules["mediaingredientmech.review_claims"]
assert private.CAPTURE_VERSION == 'new'
assert private.payload_sha256 is not old_function
assert sys.modules['mediaingredientmech.review_claims'] is old
assert old.CAPTURE_VERSION == 'old' and old.payload_sha256 is old_function
manifest=api.export_candidate(root,root/'source-review.json',root/'candidate')
assert manifest['inputs']['src/mediaingredientmech/review_claims.py'] == hashlib.sha256(path.read_bytes()).hexdigest()
print(json.dumps({'private':'new','public':'old','candidate':manifest['semantic_status']}))
""",
    )
    assert json.loads(result.stdout) == {
        "private": "new",
        "public": "old",
        "candidate": "REVIEWED_CANDIDATE_ONLY",
    }


def test_loaded_capture_refuses_origin_disk_change(fixture):
    """#1305: later disk bytes cannot masquerade as the already compiled source."""
    result = _private_python(
        fixture,
        """
import importlib.util,json,sys
from pathlib import Path
root=Path(sys.argv[1]);source=root/'src/mediaingredientmech/export/source_bindings.py'
spec=importlib.util.spec_from_file_location('isolated_source_api',source)
api=importlib.util.module_from_spec(spec);spec.loader.exec_module(api)
source.write_bytes(source.read_bytes()+b'\\n# Drift after captured compilation\\n')
try: api.expected_products(root,root/'source-review.json')
except ValueError as exc:
 assert 'executed producer/dependency changed' in str(exc)
 print(json.dumps({'refused':str(exc)}))
else: raise AssertionError('stale compiled producer accepted')
""",
    )
    assert "executed producer/dependency changed" in json.loads(result.stdout)["refused"]
