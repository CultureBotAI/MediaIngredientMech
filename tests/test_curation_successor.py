"""Actual native adoption followed by a separately reviewed source correction."""

from __future__ import annotations

import copy
import json
import shutil

import yaml

from mediaingredientmech.curate import curation_successor as successor
from mediaingredientmech.curate import stable_sssom_publication as pub
from tests.stable_publication_fixture import completed_adoption
from tests.test_stable_id_adoption import ROOT, api, commit, initialize, write


def ref(root, path):
    return {"path": str(path.relative_to(root)), "sha256": api.sha(path.read_bytes())}


class SuccessorFixture:
    def __init__(self, tmp, monkeypatch, *, publication_baseline=False):
        extra = {name: ROOT / name for name in {*successor._CAPTURE.files, *pub._CAPTURE.files}}
        self.original = completed_adoption(tmp / "original", monkeypatch, additional_sources=extra)
        original = self.original.root
        if publication_baseline:
            (original / pub.SUPPRESSIONS).write_bytes(pub._tsv(pub.SIDECAR_FIELDS, []))
        self.predecessor = original
        self.target = tmp / "successor"
        shutil.copytree(original, self.target)
        self.history = tmp / "history"
        initialize(self.history)
        for name in (
            "MAPPING_SEMANTICS.md",
            "schema/record_review.yaml",
            "primary.txt",
            self.original.request["eligibility_intake"]["path"],
        ):
            dest = self.history / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(original / name, dest)
        commit(self.history)
        f = self.original
        original_root = f.root
        f.root = self.history
        historical = []
        for role in ("primary-history", "skeptic-history"):
            target = {
                "target_id": "old",
                "kind": "snapshot_row",
                "path": "primary.txt",
                "selector": "old",
                "label": "Synthetic original obligation",
                "semantic_digest": {
                    "algorithm": "sha256",
                    "sha256": api.sha((self.history / "primary.txt").read_bytes()),
                    "description": "Original synthetic evidence bytes",
                },
                "owner_paths": [
                    {
                        "repository": api.REPOSITORY,
                        "path": "primary.txt",
                        "role": "historical evidence",
                    }
                ],
            }
            report = f.report(role, [target], ["primary.txt"], scientific=False)
            report["assessments"] = [
                {
                    "assessment_id": "retention",
                    "area": "completeness",
                    "topic": "Retain historical source holds",
                    "outcome": "supported",
                    "summary": "Synthetic evidence, no current approval",
                    "target_ids": ["old"],
                    "evidence_ids": ["primary"],
                }
            ]
            path = f.save_report(report)
            historical.append(
                {
                    "identity": successor._identity(self.history),
                    "review": ref(self.history, path),
                    "markdown_sha256": api.sha(path.with_name("review.md").read_bytes()),
                }
            )
        f.root = original_root
        manifest = json.loads((f.stage / "manifest.json").read_bytes())
        self.endpoint = {
            "kind": "adoption",
            "identity": successor._identity(original),
            "stage": str(f.stage.relative_to(original)),
            "manifest": ref(original, f.stage / "manifest.json"),
            "receipt": ref(original, f.receipt / "application.json"),
            "producer": manifest["producer"],
            "publication_beforeimages": successor._optional_hashes(
                successor._optional(original, successor.PUBLICATION)
            ),
            "publication_proof": None,
            "historical_reviews": historical,
        }
        self.before = {
            n: x.read_bytes()
            for n, x in (
                (str(p.relative_to(self.target)), p)
                for p in self.target.glob("data/ingredients/*/*.yaml")
            )
        }
        owner = "data/ingredients/mapped/Exact.yaml"
        before = api.load_yaml(self.before[owner])
        after = copy.deepcopy(before)
        after["ontology_mapping"]["mapping_quality"] = "MANUAL_CURATION"
        self.stamp = "2026-11-12T00:00:00Z"
        api.record_curation_event(
            after,
            curator="synthetic-primary",
            timestamp=self.stamp,
            action="MANUAL_CURATION",
            changes="Reviewed exact method-only correction; retain identity and all original evidence.",
            previous_status="MAPPED",
            new_status="MAPPED",
            llm_assisted=True,
            llm_model="synthetic-fixture",
        )
        self.proposal = self.target / "correction/proposal.yaml"
        self.proposal.parent.mkdir()
        self.proposal.write_text(yaml.safe_dump(after, sort_keys=False))
        self.context_path = self.target / "correction/context.json"
        self.payloads_path = self.target / "correction/payloads.json"
        source = f.request["context"]
        self.request = {
            "schema_version": 1,
            "capability": successor.CAPABILITY,
            "identity": successor._identity(self.target),
            "predecessor": self.endpoint,
            "timestamp": self.stamp,
            "curator": "synthetic-primary",
            "claw_root": str(f.claw),
            "operational_policy": ref(self.target, self.target / "operational-policy.json"),
            "target_inventory": {n: api.sha(raw) for n, raw in self.before.items()},
            "target_inputs": {
                n: api.sha((self.target / n).read_bytes())
                for n in (*api.AGGREGATES, *successor.LEDGERS)
            },
            "source_context": source,
            "operations": [
                {
                    "mim_id": before["mim_id"],
                    "before": ref(self.target, self.target / owner),
                    "after_path": owner,
                    "proposal": ref(self.target, self.proposal),
                    "delta": successor._delta(before, after),
                    "issues": ["https://github.com/CultureBotAI/MediaIngredientMech/issues/1373"],
                    "evidence": [ref(self.target, self.target / "primary.txt")],
                    "inherited_holds": [],
                    "residual_holds": [],
                    "rejected_identifiers": [],
                    "rejected_labels": [],
                    "primary": None,
                    "skeptic": None,
                }
            ],
            "context": None,
            "payloads": None,
            "review_inputs": {},
        }
        self.path = self.target / "correction/request.json"
        write(self.path, self.request)

    def seal(self):
        view = successor.inspect(self.target, self.path)
        for key, path in (("context", self.context_path), ("payloads", self.payloads_path)):
            write(path, view[key])
            self.request[key] = ref(self.target, path)
        f = self.original
        f.root = self.target
        op = self.request["operations"][0]
        target = view["targets"][0]
        target["path"] = self.request["payloads"]["path"]
        target["label"] = "Synthetic exact correction"
        target["owner_paths"] = [
            {
                "repository": api.REPOSITORY,
                "path": target["path"],
                "role": "proposed source correction",
            }
        ]
        for role in ("primary", "skeptic"):
            inputs = [
                self.request[k]["path"]
                for k in ("context", "payloads", "source_context", "operational_policy")
            ]
            inputs += [op["before"]["path"], op["proposal"]["path"], "primary.txt"]
            report = f.report("correction-" + role, [target], inputs)
            report["verdict"] = "pass"
            dims = {
                "curation_action": "apply_exact_source_delta",
                "delta_sha256": api.digest(op["delta"]),
                "permanent_mim_id": op["mim_id"],
                "residual_holds_json": api.encoded(op["residual_holds"]).decode().strip(),
                "rejected_identifiers_json": api.encoded(op["rejected_identifiers"])
                .decode()
                .strip(),
                "corrective_delta_findings": "none",
                "residual_findings_json": api.encoded([]).decode().strip(),
            }
            report["assessments"] = [
                {
                    "assessment_id": "correct",
                    "area": "grounding",
                    "topic": "Exact synthetic correction",
                    "outcome": "supported",
                    "summary": "No identity or release approval beyond this correction",
                    "target_ids": [target["target_id"]],
                    "evidence_ids": ["primary"],
                    "dimensions": [
                        {
                            "name": k,
                            "value": v,
                            "definition": "Exact synthetic contract",
                            "evidence_ids": ["primary"],
                        }
                        for k, v in dims.items()
                    ],
                }
            ]
            path = f.save_report(report)
            op[role] = {
                **ref(self.target, path),
                "markdown_sha256": api.sha(path.with_name("review.md").read_bytes()),
                "target_id": target["target_id"],
                "assessment_id": "correct",
            }
            self.request["review_inputs"].update(
                {
                    str(p.relative_to(self.target)): api.sha(p.read_bytes())
                    for p in (path, path.with_name("review.md"))
                }
            )
        f.root = self.predecessor
        write(self.path, self.request)
        return view


def test_real_predecessor_inspect_and_paired_review(tmp_path, monkeypatch):
    f = SuccessorFixture(tmp_path, monkeypatch)
    f.seal()
    loaded = successor.Loaded(f.target, f.path)
    successor._admitted(loaded)
    assert len(loaded.operations) == 1
    assert loaded.predecessor.verify_native()["status"] == "COMPLETE_CURRENT_CANDIDATE"
    assert {n: (f.target / n).read_bytes() for n in f.before} == f.before

    manifest = successor.prepare(f.target, f.path, f.target / ".temp/correct")
    assert len(manifest["outputs"]) == 4
    assert manifest["before_inventory"] == manifest["after_inventory"] | {
        "data/ingredients/mapped/Exact.yaml": manifest["before_inventory"][
            "data/ingredients/mapped/Exact.yaml"
        ]
    }
