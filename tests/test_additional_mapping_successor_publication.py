"""Real correction-chain publication with independent extra assertions (#1373/#1418).

Use the existing CLAW_SRC test selector with a producer supporting additional
assertions. Every owner, evidence document and review judgment is synthetic.
The native review, producer, validation, lease and publication gates run intact.
"""

from __future__ import annotations

import copy
import gzip
import json
import os
from datetime import datetime
from pathlib import Path

import pytest
import yaml

from mediaingredientmech import additional_mappings
from mediaingredientmech.curate import curation_successor as successor
from mediaingredientmech.curate import stable_sssom_publication as publication
from tests.test_curation_successor import ref
from tests.test_curation_successor_chain import ChainFixture
from tests.test_curation_successor_history import (
    assert_exact_evidence,
    commit_paths,
    receipt_evidence,
)
from tests.test_curation_successor_transition import maintained, prepared
from tests.test_stable_id_adoption import ROOT, api, commit, initialize, write
from tests.test_stable_sssom_publication import PublicationFixture, current_outputs

CONTRACT = "src/mediaingredientmech/additional_mappings.py"


class AdditionalAssertionChainFixture(ChainFixture):
    """Bind each new evidence document into both genuine native review bundles."""

    def seal(self):
        view = super().seal()
        evidence = getattr(self, "assertion_evidence", ())
        if not evidence:
            return view  # The first completed correction uses the unchanged fixture.
        operation = self.request["operations"][0]
        for role in ("primary", "skeptic"):
            report = api.load_yaml((self.target / operation[role]["path"]).read_bytes())
            report["started_at"] = report["finished_at"] = self.stamp
            report["review_id"] = (
                datetime.fromisoformat(self.stamp.replace("Z", "+00:00")).strftime("%Y%m%dT%H%M%SZ")
                + "-"
                + report["review_id"].split("-", 1)[1]
                + "-assertions"
            )
            inputs = [item["path"] for item in report["source"]["inputs"]]
            report["source"] = self.original.native.inspect_source(
                self.target, report["targets"], [*inputs, *evidence]
            )["source"]
            for position, name in enumerate(evidence, 1):
                eid = "assertion-evidence-" + str(position)
                report["evidence"].append(
                    {
                        "evidence_id": eid,
                        "kind": "primary_source",
                        "reference": name,
                        "snapshot_sha256": api.sha((self.target / name).read_bytes()),
                        "accessed_at": self.stamp,
                        "support": "supports",
                        "summary": "Synthetic evidence for the scoped assertion or its withholding",
                    }
                )
                for assessment in report["assessments"]:
                    assessment["evidence_ids"].append(eid)
            saved = self.original.native.save_review(
                self.target, report, schema_path=self.target / "schema/record_review.yaml"
            )
            operation[role].update(
                **ref(self.target, saved),
                markdown_sha256=api.sha(saved.with_name("review.md").read_bytes()),
            )
            self.request["review_inputs"].update(
                {
                    str(p.relative_to(self.target)): api.sha(p.read_bytes())
                    for p in (saved, saved.with_name("review.md"))
                }
            )
        write(self.path, self.request)
        return view


def assertion(owner, target, predicate, status, evidence, stamp):
    return {
        "subject_id": owner,
        "ontology_id": target,
        "ontology_label": "Synthetic external assertion " + target,
        "ontology_source": "NCIT",
        "predicate_id": predicate,
        "review_status": status,
        "reviewed_by": "synthetic-assertion-reviewer-" + target,
        "reviewed_at": stamp,
        "review_note": "Contract fixture only; no real scientific or release approval",
        "llm_assisted": True,
        "mapping_justification": "semapv:LexicalMatching",
        "evidence": [
            {
                "evidence_type": "DATABASE_MATCH",
                "source": evidence,
                "supports": "SUPPORT" if status == "SUPPORTED" else "REFUTE",
                "explanation": "This synthetic document supports exactly the recorded disposition",
            }
        ],
    }


def publication_fixture(f, endpoint, tmp_path):
    """Use the actual selected Claw CLI, retaining native generation/review APIs."""
    p = PublicationFixture.__new__(PublicationFixture)
    p.root, p.adoption, p.counter = f.target, f.original, 0
    p.adoption.root = f.target
    p.adoption.policy = f.target / "operational-policy.json"
    p.histories = [
        {
            "root": item["identity"]["root"],
            "head": item["identity"]["head"],
            "review": item["review"],
            "markdown_sha256": item["markdown_sha256"],
        }
        for item in f.endpoint["historical_reviews"]
    ]
    p.history = p.histories[0]
    p.producer = Path(os.environ["MIM_ADDITIONAL_ASSERTION_CLAW_SRC"]).resolve().parent
    p.kg = tmp_path / "synthetic-kg-input"
    initialize(p.kg)
    mapping = p.kg / "mappings/kgmicrobe_unified_entity_mappings.sssom.tsv.gz"
    mapping.parent.mkdir()
    mapping.write_bytes(
        gzip.compress(
            b"subject_id\tsubject_label\tpredicate_id\tobject_id\tobject_label\tsource\n", mtime=0
        )
    )
    commit(p.kg)
    p.generation_dir = f.target / ".temp/additional-assertion-generation"
    # The maintained NCIT fixture route consumes stored labels, never OAK/OLS.
    # Check the selected owner inputs before invoking the real CLI.
    for path in api.inventory(f.target):
        record = api.load_yaml((f.target / path).read_bytes())
        target = (record.get("ontology_mapping") or {}).get("ontology_id")
        assert target is None or target.startswith("NCIT:")
    p.generated = publication.generate(
        f.target,
        p.producer,
        p.kg,
        None,
        None,
        p.generation_dir,
        curation_successor=endpoint,
        curation_successor_sha256=api.sha(endpoint.read_bytes()),
    )
    p.generation_receipt = p.generation_dir / "receipt.json"
    return p


def test_two_corrections_publish_independent_assertions_and_keep_holds(tmp_path, monkeypatch):
    """Actual source deltas and canonical install preserve scoped evidence and holds."""
    if not os.environ.get("MIM_ADDITIONAL_ASSERTION_CLAW_SRC"):
        pytest.skip(
            "Dedicated additional-assertion producer required; CI runs this with its explicit pin"
        )
    progress = []

    def completed(phase):
        progress.append(phase)
        write(tmp_path / "combined-progress.json", {"completed": progress})

    f = AdditionalAssertionChainFixture(tmp_path, monkeypatch)
    completed("adoption_and_first_correction_verified")
    operation = f.request["operations"][0]
    selected = operation["after_path"]
    before_owner = api.load_yaml(f.before[selected])
    after_owner = api.load_yaml(f.proposal.read_bytes())
    after_owner["ontology_mapping"]["mapping_quality"] = "EXACT_MATCH"
    after_owner["ontology_mapping"]["evidence"] = [
        {"evidence_type": "DATABASE_MATCH", "source": "primary.txt"}
    ]
    f.assertion_evidence = ["synthetic-broad-evidence.txt", "synthetic-held-evidence.txt"]
    for name, status in zip(f.assertion_evidence, ("SUPPORTED", "WITHHOLD"), strict=True):
        (f.target / name).write_text(
            f"Synthetic contract-only evidence for the {status} extra relation; no real claim.\n"
        )
        operation["evidence"].append(ref(f.target, f.target / name))
    owner = after_owner["mim_id"]
    after_owner[additional_mappings.FIELD] = [
        assertion(
            owner, "NCIT:C990001", "skos:broadMatch", "SUPPORTED", f.assertion_evidence[0], f.stamp
        ),
        assertion(
            owner, "NCIT:C990002", "skos:closeMatch", "WITHHOLD", f.assertion_evidence[1], f.stamp
        ),
    ]
    after_owner["curation_history"][-1][
        "changes"
    ] = "Synthetic exact primary with independently evidenced broad assertion and held close proposal."
    f.proposal.write_text(yaml.safe_dump(after_owner, sort_keys=False))
    operation.update(
        proposal=ref(f.target, f.proposal), delta=successor._delta(before_owner, after_owner)
    )
    write(f.path, f.request)
    holds = copy.deepcopy(operation["inherited_holds"])
    assert holds and operation["residual_holds"] == holds
    source_before = maintained(f.target)
    stage, acceptance, manifest = prepared(f)
    assert manifest["producer"]["files"][CONTRACT] == api.sha((ROOT / CONTRACT).read_bytes())
    destination = f.target / ".temp/additional-source-application"
    dry = successor.apply(f.target, stage, acceptance, destination, enabled=False)
    assert dry["applied"] is False and not destination.exists()
    assert maintained(f.target) == source_before
    result = successor.apply(f.target, stage, acceptance, destination, enabled=True)
    assert result["state"] == "COMPLETE" and result["release_approval_added"] is False
    source_receipt = destination / "application.json"
    second_evidence = receipt_evidence(f.target, stage, source_receipt)
    commit_paths(
        f.target, manifest["outputs"], "Commit synthetic independently reviewed extra assertions"
    )
    assert (
        successor.verify_completed(f.target, stage, source_receipt)["status"]
        == "COMPLETE_CURRENT_SOURCE_SUCCESSOR"
    )
    assert api.load_yaml((f.target / selected).read_bytes()) == after_owner
    assert after_owner["curation_history"][:-1] == before_owner["curation_history"]
    completed("second_correction_dry_run_apply_commit_verify")
    endpoint = f.path.with_name("endpoint.json")
    write(
        endpoint,
        {
            "schema_version": 1,
            "capability": successor.CAPABILITY,
            "root": str(f.target),
            "stage": str(stage.relative_to(f.target)),
            "manifest": ref(f.target, stage / "manifest.json"),
            "receipt": ref(f.target, source_receipt),
            "producer": manifest["producer"],
        },
    )
    p = publication_fixture(f, endpoint, tmp_path)
    generated = json.loads((p.generation_dir / "generation.json").read_bytes())
    assert generated["external_sssom_validation"] == "passed"
    assert generated["canonical_label_resolution"] == {}
    assert generated["emitted_rows"] == 3
    assert any(
        item["path"] == str(f.target / CONTRACT)
        and item["sha256"] == api.sha((ROOT / CONTRACT).read_bytes())
        for item in generated["source_inputs"]
    )
    _, _, candidate = publication.read_sssom(p.generation_dir / "candidate.sssom.tsv")
    expected_triples = {
        (owner, "skos:exactMatch", "NCIT:C80300"),
        (owner, "skos:broadMatch", "NCIT:C990001"),
        (owner, "skos:closeMatch", "NCIT:C990002"),
    }
    assert {
        (row["subject_id"], row["predicate_id"], row["object_id"]) for row in candidate
    } == expected_triples
    for row in candidate:
        additional_mappings.row_assertion(after_owner, row)
    completed("captured_claw_generation_and_native_sssom_validation")

    def retain_assertion_holds(selection):
        for entry in selection["rows"]:
            if entry.get("mandatory_disposition"):
                entry["disposition"] = entry["mandatory_disposition"]

    request = p.request(disposition="INSTALL_SUPPORTED", alter=retain_assertion_holds)
    selected_rows = [entry for entry in request.selection["rows"] if entry["candidate_position"]]
    assert {
        entry["proposed_row"]["object_id"]: entry["disposition"] for entry in selected_rows
    } == {
        "NCIT:C80300": "INSTALL_SUPPORTED",
        "NCIT:C990001": "INSTALL_SUPPORTED",
        "NCIT:C990002": "INSTALL_WITHHOLD",
    }
    request, publication_stage, _ = p.prepare(request)
    technical = p.accept(request, publication_stage)
    canonical_before = current_outputs(f.target)
    output = p.destination(request, "additional-applied")
    dry = publication.apply(f.target, publication_stage, technical, output, enabled=False)
    assert dry["applied"] is False and not output.exists()
    assert current_outputs(f.target) == canonical_before
    applied = publication.apply(f.target, publication_stage, technical, output, enabled=True)
    assert applied["state"] == "COMPLETE" and applied["scientific_approval_added"] is False
    proof = publication.verify_completed(f.target, publication_stage, output / "application.json")
    assert proof["status"] == "COMPLETE_CURRENT_CANONICAL_CANDIDATE"
    assert proof["ordinary_release_review_required"] is True
    _, _, installed = publication.read_sssom(f.target / publication.CANONICAL)
    assert len(installed) == 3
    assert {
        (row["subject_id"], row["predicate_id"], row["object_id"]) for row in installed
    } == expected_triples
    for row in installed:
        additional_mappings.row_assertion(after_owner, row)
        assert row["validation_method"] == ""
    provenance = json.loads((f.target / publication.PROVENANCE).read_bytes())
    assert provenance["selection"] == request.selection
    primary_selection = next(
        entry
        for entry in provenance["selection"]["rows"]
        if entry["proposed_row"] and entry["proposed_row"]["object_id"] == "NCIT:C80300"
    )
    assert (
        primary_selection["before_rows"][0]["row"]["validation_method"] == "synthetic-prior-stamp"
    )
    assert api.load_yaml((f.target / selected).read_bytes()) == after_owner
    persisted_operation = json.loads(f.path.read_bytes())["operations"][0]
    assert persisted_operation["inherited_holds"] == persisted_operation["residual_holds"] == holds
    assert not (f.target / f.original.held).exists()
    assert maintained(f.first) == f.first_maintained
    assert maintained(f.adoption) == f.adoption_maintained
    assert_exact_evidence(f.first_evidence)
    assert_exact_evidence(second_evidence)
    completed("canonical_prepare_dry_run_apply_verify_with_history_and_holds")
