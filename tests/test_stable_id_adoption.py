"""Actual native synthetic adoption fixtures; no campaign scientific approvals (#1303)."""

import copy
import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.curate import stable_id_adoption as api

ROOT = Path(__file__).resolve().parents[1]
CLAW = (
    Path(os.environ.get("CLAW_SRC", str(ROOT.parent / "culturebotai-claw" / "src")))
    .resolve()
    .parent
)


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(api.encoded(value))


def command(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, stderr=subprocess.PIPE)


def initialize(root):
    root.mkdir(exist_ok=True)
    for args in [
        ("init",),
        ("config", "user.name", "Synthetic reviewer"),
        ("config", "user.email", "fixture@example.invalid"),
        ("remote", "add", "origin", "https://github.com/CultureBotAI/MediaIngredientMech.git"),
    ]:
        command(root, *args)


def commit(root):
    command(root, "add", ".")
    command(root, "commit", "-m", "Synthetic native fixture")
    return command(root, "rev-parse", "HEAD").decode().strip()


class Fixture:
    def __init__(self, tmp, monkeypatch):
        self.root, self.legacy, self.claw = (tmp / name for name in ("target", "legacy", "claw"))
        for root in (self.root, self.legacy, self.claw):
            initialize(root)
        for name in api._CAPTURE.files:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, path)
        for name in (*api.Claw.PATHS.values(), "uv.lock", "pyproject.toml"):
            path = self.claw / name
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(CLAW / name, path)
        commit(self.claw)
        monkeypatch.setenv("OPENCLAW_WORKSPACE", str(tmp / "workspace"))
        self.paths = ["data/ingredients/mapped/Exact.yaml", "data/ingredients/unmapped/Move.yaml"]
        self.original = [
            {
                "identifier": "CHEBI:1",
                "preferred_term": "Exact",
                "mapping_status": "MAPPED",
                "curation_history": [],
            },
            {
                "identifier": "UNMAPPED_1",
                "preferred_term": "Move",
                "mapping_status": "UNMAPPED",
                "curation_history": [],
            },
        ]
        for path, record in zip(self.paths, self.original, strict=True):
            for root in (self.root, self.legacy):
                p = root / path
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(yaml.safe_dump(record, sort_keys=False))
        source_commit = commit(self.root)
        before = {path: api.sha((self.root / path).read_bytes()) for path in self.paths}
        self.mints = []
        for number, (path, original) in enumerate(zip(self.paths, self.original, strict=True), 1):
            record = copy.deepcopy(original)
            identifier = f"MIM:{number:07d}"
            record.update(
                mim_id=identifier,
                legacy_identifiers=[
                    api.mim_curie_for_stem(Path(path).stem),
                    original["identifier"],
                ],
            )
            api.record_curation_event(
                record,
                curator="fixture",
                action="ASSIGNED_MIM_ID",
                timestamp="2026-01-01T00:00:00Z",
                changes=f"Assigned {identifier}; synthetic original mint",
            )
            api.write_validated_ingredient(
                record, self.root / path, schema_path=self.root / api.SCHEMA
            )
            self.mints.append(
                {
                    "path": path,
                    "mim_id": identifier,
                    "before_sha256": before[path],
                    "after_sha256": api.sha((self.root / path).read_bytes()),
                }
            )
        (self.root / "data/ids").mkdir()
        (self.root / api.REGISTRY_PATH).write_text(
            "mim_id\tlabel_at_minting\tminted_on\tstatus\treplaced_by\nMIM:0000001\tExact\t2026-01-01\tactive\t\nMIM:0000002\tMove\t2026-01-01\tactive\t\n"
        )
        (self.root / api.LIFECYCLE_PATH).write_text(
            "mim_id\tstatus\treplaced_by\tchanged_at\treason\n"
        )
        write(self.root / api.MIGRATION, {"source_commit": source_commit, "records": self.mints})
        for category, name in zip(("mapped", "unmapped"), api.AGGREGATES, strict=True):
            collection, errors = api._CAPTURE.script(
                "scripts/aggregate_records.py"
            ).aggregate_individual_files(self.root / "data/ingredients", category, validate=True)
            assert not errors
            api.write_validated_ingredient(
                collection,
                self.root / name,
                target_class="IngredientCollection",
                schema_path=self.root / api.SCHEMA,
            )
        self.head = commit(self.root)
        move = "data/ingredients/mapped/Move.yaml"
        new = "data/ingredients/unmapped/New.yaml"
        held = "data/ingredients/unmapped/Held.yaml"
        self.move, self.new, self.held = move, new, held
        legacy_base = commit(self.legacy)
        old = (self.legacy / self.paths[1]).read_bytes()
        (self.legacy / "archive").mkdir()
        (self.legacy / "archive/move.yaml").write_bytes(old)
        (self.legacy / self.paths[1]).rename(self.legacy / move)
        for path, label in [(new, "New"), (held, "Held")]:
            (self.legacy / path).write_text(
                yaml.safe_dump(
                    {
                        "identifier": "UNMAPPED_" + label,
                        "preferred_term": label,
                        "mapping_status": "UNMAPPED",
                        "curation_history": [],
                    },
                    sort_keys=False,
                )
            )
        cases = [
            {
                "case_id": str(i),
                "source_label": f"synthetic-{i}",
                "occurrences": [{"context": str(i), "alternative": False}],
            }
            for i in range(4)
        ]
        operations = []
        for index, (kind, previous, path) in enumerate(
            [("promote", self.paths[1], move), ("create", None, new), ("create", None, held)], 1
        ):
            operations.append(
                {
                    "operation_id": f"OP{index}",
                    "kind": kind,
                    "before_source_record": previous,
                    "source_record": path,
                    "after_capture": {
                        "path": path,
                        "sha256": api.sha((self.legacy / path).read_bytes()),
                    },
                    "origins": [
                        {
                            "worker_slot": "worker-01",
                            "proposal_id": f"P{index}",
                            "case_hashes": {str(index): api.digest(cases[index])},
                        }
                    ],
                }
            )
        after = api.hashes(api.inventory(self.legacy))
        write(self.legacy / "before.json", {"schema_version": 1, "owners": before})
        write(self.legacy / "after.json", {"schema_version": 1, "owners": after})
        ref = lambda path: {"path": path, "sha256": api.sha((self.legacy / path).read_bytes())}
        write(self.legacy / "cases.json", cases)
        write(
            self.legacy / "proposals.json",
            {
                "proposals": [
                    {"proposal_id": f"P{i}", "case_ids": [str(i if i < 4 else 0)]}
                    for i in range(1, 6)
                ]
            },
        )
        write(self.legacy / "decisions.json", {"decisions": cases})
        plan = {
            "baseline_commit": legacy_base,
            "intake_heads": {"worker-01": legacy_base},
            "bindings": [
                {"binding_id": "full-case-ledger", "role": "case_ledger", **ref("cases.json")},
                {"binding_id": "w01-proposals", "role": "proposal", **ref("proposals.json")},
                {"binding_id": "w01-decisions", "role": "decision", **ref("decisions.json")},
            ],
            "records": operations,
            "before_inventory": ref("before.json"),
            "after_inventory": ref("after.json"),
        }
        write(self.legacy / "plan.json", plan)
        acceptance = {
            "schema_version": 1,
            "scope": "source_application_only",
            "plan_sha256": ref("plan.json")["sha256"],
            "baseline_commit": legacy_base,
            "intake_heads": plan["intake_heads"],
            "binding_sha256": {b["binding_id"]: b["sha256"] for b in plan["bindings"]},
            "accepted_operations": {
                o["operation_id"]: o["after_capture"]["sha256"] for o in operations
            },
        }
        write(self.legacy / "acceptance.json", acceptance)
        receipt = {
            "baseline_commit": legacy_base,
            "acceptance": ref("acceptance.json"),
            "state": "complete",
            "recovery_required": False,
            "plan": ref("plan.json"),
            "before_inventory": before,
            "after_inventory": after,
            "completed_operations": [r["operation_id"] for r in operations],
            "records": [
                {
                    **op,
                    "before_capture": ref("archive/move.yaml") if op["kind"] == "promote" else None,
                }
                for op in operations
            ],
        }
        write(self.legacy / "application.json", receipt)
        write(self.legacy / "cases.json", cases)
        legacy_head = commit(self.legacy)
        self.request = {
            "schema_version": 1,
            "capability": api.CAPABILITY,
            "baseline_commit": self.head,
            "history_base": self.head,
            "timestamp": "2026-01-02T00:00:00Z",
            "claw_root": str(self.claw),
            "legacy": {
                "root": str(self.legacy),
                "head": legacy_head,
                "plan": ref("plan.json"),
                "application": ref("application.json"),
                "cases": ref("cases.json"),
            },
            "target_inventory": api.hashes(api.inventory(self.root)),
            "target_inputs": {
                name: api.sha((self.root / name).read_bytes())
                for name in (
                    *api.AGGREGATES,
                    str(api.REGISTRY_PATH),
                    str(api.LIFECYCLE_PATH),
                    api.MIGRATION,
                )
            },
            "existing": [
                {
                    "mim_id": f"MIM:{i:07d}",
                    "stable_path": path,
                    "legacy_path": move if i == 2 else path,
                }
                for i, path in enumerate(self.paths, 1)
            ],
            "decisions": [
                {
                    "operation_id": "OP2",
                    "disposition": "CREATE_DISTINCT_CONCEPT",
                    "concept_key": "new",
                    "owner_operation": "OP2",
                    "existing_mim_id": None,
                    "identity_holds": [],
                    "other_holds": ["role provisional"],
                    "primary": None,
                    "skeptic": None,
                },
                {
                    "operation_id": "OP3",
                    "disposition": "WITHHOLD_IDENTITY",
                    "concept_key": None,
                    "owner_operation": None,
                    "existing_mim_id": None,
                    "identity_holds": ["ambiguous supplied form"],
                    "other_holds": [],
                    "primary": None,
                    "skeptic": None,
                },
            ],
            "context": {"path": "evidence/context.json", "sha256": "0" * 64},
            "payloads": {"path": "evidence/payloads.json", "sha256": "0" * 64},
            "review_inputs": {},
        }
        crosswalk = [
            {
                "origin_id": f"w01::P{i}",
                "status": "apply" if i < 4 else "deferred" if i == 4 else "retired",
                "evidence_refs": [ref("proposals.json")],
                **(
                    {
                        "operation_id": f"OP{i}",
                        "payload_sha256": operations[i - 1]["after_capture"]["sha256"],
                    }
                    if i < 4
                    else {}
                ),
            }
            for i in range(1, 6)
        ]
        proof = {
            "structurally_complete": True,
            "scientific_approval": False,
            "application_authorized": False,
            "origin_count": 5,
            "applied_origin_count": 3,
            "native_operation_count": 3,
            "native_prepare_proof": {
                "plan_sha256": ref("plan.json")["sha256"],
                "acceptance_sha256": ref("acceptance.json")["sha256"],
                "before_owner_sha256": before,
                "after_owner_sha256": after,
                "native_input_sha256": {"plan.json": ref("plan.json")["sha256"]},
            },
            "evidence_sha256": {"acceptance.json": ref("acceptance.json")["sha256"]},
        }
        for key, value in [("origin_accounting", crosswalk), ("origin_proof", proof)]:
            path = f"evidence/{key}.json"
            write(self.root / path, value)
            self.request[key] = {"path": path, "sha256": api.sha((self.root / path).read_bytes())}
        intake = {
            "scope": "Synthetic original unclassified eligibility context",
            "candidates": [
                {
                    "candidate_key": op["operation_id"],
                    "owner_path": op["source_record"],
                    "owner_sha256": op["after_capture"]["sha256"],
                    "known_conditions_and_holds": [
                        {
                            "request_id": "original",
                            "origin": op["origins"][0]["proposal_id"],
                            "field": "remaining_holds",
                            "literal_value": (
                                "role provisional"
                                if op["operation_id"] == "OP2"
                                else "ambiguous supplied form"
                            ),
                        }
                    ],
                    "source_case_scope": op["origins"],
                    "existing_owner_comparison_context": [],
                    "existing_scientific_context": [],
                    "eligibility": None,
                }
                for op in operations
                if op["kind"] == "create"
            ],
        }
        path = "evidence/eligibility-intake.json"
        write(self.root / path, intake)
        self.request["eligibility_intake"] = {
            "path": path,
            "sha256": api.sha((self.root / path).read_bytes()),
        }
        self.request_path = self.root / "request.json"
        self.stage = self.root / ".temp/prepare"
        self.receipt = self.root / ".temp/application"
        self.native = api._CAPTURE.script("scripts/record_review.py")
        (self.root / "primary.txt").write_text("Synthetic primary scientific evidence only.\n")
        self.seal()

    def save(self):
        write(self.request_path, self.request)

    def report(self, role, targets, inputs, scientific=True):
        source = self.native.inspect_source(
            self.root,
            targets,
            ["MAPPING_SEMANTICS.md", self.request["eligibility_intake"]["path"], *inputs],
        )["source"]
        return {
            "schema_version": "1.0.0",
            "review_id": "20260102T000000Z-adoption-" + role,
            "kind": "batch",
            "repository": api.REPOSITORY,
            "title": "Synthetic adoption contract",
            "started_at": "2026-01-02T00:00:00Z",
            "finished_at": "2026-01-02T00:00:00Z",
            "reviewer": {
                "identity": role,
                "kind": "human",
                "independence": "independent" if role != "primary" else "self_review",
                "independence_basis": "Separate synthetic reviewer",
            },
            "skill": "review-yaml-category",
            "completion": "completed",
            "verdict": "needs_curation" if scientific else "pass",
            "scientific_review": scientific,
            "summary": "Synthetic fixture; not campaign approval",
            "source": source,
            "targets": targets,
            "scope": {
                "description": "Complete synthetic source/owner context",
                "selection": "Complete fixture",
                "coverage": "full",
                "population_size": len(targets),
                "reviewed_target_ids": [t["target_id"] for t in targets],
            },
            "checks": [
                {
                    "check_id": "identity",
                    "name": "Complete context",
                    "required": True,
                    "status": "passed",
                    "summary": "Actual fixture review scope",
                    "target_ids": [t["target_id"] for t in targets],
                    "evidence_ids": ["primary"],
                }
            ],
            "evidence": [
                {
                    "evidence_id": "primary",
                    "kind": "primary_source",
                    "reference": "primary.txt",
                    "snapshot_sha256": api.sha((self.root / "primary.txt").read_bytes()),
                    "accessed_at": "2026-01-02T00:00:00Z",
                    "support": "supports",
                    "summary": "Synthetic evidence",
                }
            ],
            "assessments": [],
            "findings": [],
            "actions": [],
            "limitations": [],
        }

    def save_report(self, report):
        path = self.root / f"reviews/structured/{report['review_id']}/review.yaml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(report, sort_keys=False))
        path.with_name("review.md").write_text(self.native.render_markdown(report))
        return path

    def seal(self, alter=None):
        self.save()
        view = api.inspect(self.root, self.request_path)
        for key in ("context", "payloads"):
            path = self.root / self.request[key]["path"]
            write(path, view[key])
            self.request[key]["sha256"] = api.sha(path.read_bytes())
        self.request["review_inputs"] = {}
        for role in ("primary", "skeptic"):
            report = self.report(
                role,
                view["targets"],
                [self.request["context"]["path"], self.request["payloads"]["path"], "primary.txt"],
            )
            for row, target in zip(self.request["decisions"], view["targets"], strict=True):
                report["assessments"].append(
                    {
                        "assessment_id": row["operation_id"],
                        "area": "identity",
                        "topic": "Complete source and duplicate boundary",
                        "outcome": (
                            "unknown" if row["disposition"] == "WITHHOLD_IDENTITY" else "supported"
                        ),
                        "summary": "Explicit synthetic concept decision",
                        "target_ids": [target["target_id"]],
                        "evidence_ids": ["primary"],
                        "dimensions": [
                            {
                                "name": "concept_disposition",
                                "value": row["disposition"],
                                "definition": "Explicit reviewed disposition",
                                "evidence_ids": ["primary"],
                            },
                            {
                                "name": "concept_scope",
                                "value": "complete_source_and_duplicate_boundary",
                                "definition": "All source contexts and duplicates",
                                "evidence_ids": ["primary"],
                            },
                        ],
                    }
                )
                report["assessments"][-1]["dimensions"].extend(
                    [
                        {
                            "name": "residual_" + name,
                            "value": json.dumps(
                                row[name], ensure_ascii=False, separators=(",", ":")
                            ),
                            "definition": "Explicit residual classification of original literal evidence; null remains unassessed",
                            "evidence_ids": ["primary"],
                        }
                        for name in ("identity_holds", "other_holds")
                    ]
                )
                if row["disposition"] == "CREATE_DISTINCT_CONCEPT":
                    report["assessments"][-1]["dimensions"].extend(
                        [
                            {
                                "name": key,
                                "value": value,
                                "definition": "Explicit scientific grouping outcome",
                                "evidence_ids": ["primary"],
                            }
                            for key, value in [
                                ("concept_key", row["concept_key"]),
                                ("concept_owner_operation", row["owner_operation"]),
                            ]
                        ]
                    )
                elif row["disposition"] == "BIND_EXISTING_CONCEPT_ONLY":
                    report["assessments"][-1]["dimensions"].append(
                        {
                            "name": "concept_existing_mim_id",
                            "value": row["existing_mim_id"],
                            "definition": "Explicit existing-owner identity outcome",
                            "evidence_ids": ["primary"],
                        }
                    )
                row[role] = {
                    "path": f"reviews/structured/{report['review_id']}/review.yaml",
                    "target_id": target["target_id"],
                    "assessment_id": row["operation_id"],
                }
            if alter:
                alter(role, report)
            path = self.save_report(report)
            for p in (path, path.with_name("review.md")):
                self.request["review_inputs"][str(p.relative_to(self.root))] = api.sha(
                    p.read_bytes()
                )
        self.save()

    def prepare(self):
        return api.prepare(self.root, self.request_path, self.stage)

    def accept(self):
        path = self.stage / "manifest.json"
        relative = str(path.relative_to(self.root))
        target = {
            "target_id": "prepared",
            "label": "Prepared administrative set",
            "kind": "snapshot_row",
            "path": relative,
            "selector": "prepared",
            "semantic_digest": {
                "algorithm": "sha256",
                "sha256": api.sha(path.read_bytes()),
                "description": "Exact prepared manifest bytes",
            },
            "owner_paths": [
                {"repository": api.REPOSITORY, "path": relative, "role": "prepared candidate"}
            ],
        }
        report = self.report("technical", [target], [relative, "primary.txt"], scientific=False)
        report["assessments"] = [
            {
                "assessment_id": "apply",
                "area": "completeness",
                "topic": "Exact administrative prepared set",
                "outcome": "supported",
                "summary": "All native synthetic invariants preserved",
                "target_ids": ["prepared"],
                "evidence_ids": ["primary"],
                "dimensions": [
                    {
                        "name": "adoption_action",
                        "value": "apply_exact_prepared_set",
                        "definition": "Administrative candidate only",
                        "evidence_ids": ["primary"],
                    }
                ],
            }
        ]
        rp = self.save_report(report)
        self.acceptance = self.root / "acceptance.json"
        write(
            self.acceptance,
            {
                "manifest_sha256": api.sha(path.read_bytes()),
                "review": {
                    "path": str(rp.relative_to(self.root)),
                    "sha256": api.sha(rp.read_bytes()),
                },
                "markdown_sha256": api.sha(rp.with_name("review.md").read_bytes()),
            },
        )


@pytest.fixture
def f(tmp_path, monkeypatch):
    return Fixture(tmp_path, monkeypatch)


def test_native_prepare_apply_and_verify(f):
    original = {p: (f.legacy / p).read_bytes() for p in api.inventory(f.legacy)}
    result = f.prepare()
    assert len(result["after_inventory"]) == 3
    f.accept()
    applied = api.apply(f.root, f.stage, f.acceptance, f.receipt, enabled=True)
    assert applied["state"] == "COMPLETE"
    assert not (f.root / f.paths[1]).exists() and (f.root / f.move).exists()
    assert not (f.root / f.held).exists()
    assert yaml.safe_load((f.root / f.new).read_bytes())["mapping_status"] == "UNMAPPED"
    assert yaml.safe_load((f.root / f.new).read_bytes())["mim_id"] == "MIM:0000003"
    assert (
        api.verify_completed(f.root, f.stage, f.receipt / "application.json")["status"]
        == "COMPLETE_CURRENT_CANDIDATE"
    )
    assert all((f.legacy / p).read_bytes() == raw for p, raw in original.items())


def managed(f):
    return {
        str(path.relative_to(f.root)): path.read_bytes()
        for parent in ("data/ingredients", "data/curated", "data/ids")
        for path in (f.root / parent).rglob("*")
        if path.is_file()
    }


def assert_refused_without_writes(f, message):
    before = managed(f)
    with pytest.raises((ValueError, RuntimeError), match=message):
        f.prepare()
    assert managed(f) == before and not f.stage.exists()


def test_unassessed_inspection_preserves_digest_and_does_not_allocate(f):
    before = managed(f)
    original = api.inspect(f.root, f.request_path)
    for row in f.request["decisions"]:
        row.update(
            disposition=None,
            concept_key=None,
            owner_operation=None,
            existing_mim_id=None,
            primary=None,
            skeptic=None,
        )
    f.save()
    pending = api.inspect(f.root, f.request_path)
    assert pending["payloads"] == original["payloads"] and pending["context"] == original["context"]
    assert all(
        t["semantic_digest"] == old["semantic_digest"]
        for t, old in zip(pending["targets"], original["targets"], strict=True)
    )
    assert (
        pending["payloads"][0]["original_eligibility_context"]["known_conditions_and_holds"][0][
            "literal_value"
        ]
        == "role provisional"
    )
    assert (
        pending["payloads"][1]["original_eligibility_context"]["known_conditions_and_holds"][0][
            "literal_value"
        ]
        == "ambiguous supplied form"
    )
    assert_refused_without_writes(f, "unassessed")
    assert managed(f) == before


def test_substituted_nonselected_case_subset_is_rejected(f):
    cases = json.loads((f.legacy / "cases.json").read_bytes())
    write(f.legacy / "subset.json", cases[1:])
    f.request["legacy"]["cases"] = {
        "path": "subset.json",
        "sha256": api.sha((f.legacy / "subset.json").read_bytes()),
    }
    f.save()
    assert_refused_without_writes(f, "full original case ledger")


@pytest.mark.parametrize(
    "change,message",
    [
        ("missing_decision", "every create"),
        ("missing_existing", "complete existing ID"),
        ("missing_owner", "complete target inventory"),
        ("identity_hold", "unresolved identity hold"),
        ("group_disagreement", "inconsistent concept group"),
        ("unknown_disposition", "unknown concept"),
    ],
)
def test_request_scope_refusals(f, change, message):
    if change == "missing_decision":
        f.request["decisions"].pop()
    elif change == "missing_existing":
        f.request["existing"].pop()
    elif change == "missing_owner":
        f.request["target_inventory"].pop(f.paths[0])
    elif change == "identity_hold":
        f.request["decisions"][0]["identity_holds"] = ["unsettled supplied form"]
    elif change == "group_disagreement":
        f.request["decisions"][0]["owner_operation"] = "OP3"
    else:
        f.request["decisions"][0]["disposition"] = "MAPPED_THEREFORE_ELIGIBLE"
    f.save()
    assert_refused_without_writes(f, message)


@pytest.mark.parametrize("status", ["failed", "skipped", "unavailable", "not_applicable"])
def test_required_native_checks_must_pass(f, status):
    row = f.request["decisions"][0]
    path = f.root / row["skeptic"]["path"]
    report = yaml.safe_load(path.read_bytes())
    report["checks"][0]["status"] = status
    path.write_text(yaml.safe_dump(report, sort_keys=False))
    try:
        path.with_name("review.md").write_text(f.native.render_markdown(report))
    except f.native.ReviewError:
        # Invalid native status/completion combinations must be refused by the
        # real producer too; do not count the author-side failure as the test.
        pass
    for p in (path, path.with_name("review.md")):
        f.request["review_inputs"][str(p.relative_to(f.root))] = api.sha(p.read_bytes())
    f.save()
    assert_refused_without_writes(f, "required|completed|status")


@pytest.mark.parametrize(
    "change,message",
    [
        ("self_skeptic", "separate skeptical"),
        ("unsupported", "unsupported concept"),
        ("group", "exact concept group"),
        ("target_digest", "review target differs"),
        ("owner_path", "review owner target differs"),
        ("no_primary", "captured primary"),
    ],
)
def test_native_review_cannot_be_replaced_by_free_approval(f, change, message):
    def alter(role, r):
        if role != "skeptic":
            return
        if change == "self_skeptic":
            r["reviewer"]["identity"] = "primary"
        elif change == "unsupported":
            r["assessments"][0]["outcome"] = "unknown"
        elif change == "group":
            r["assessments"][0]["dimensions"][-1]["value"] = "OP3"
        elif change == "target_digest":
            r["targets"][0]["semantic_digest"]["sha256"] = "0" * 64
        elif change == "owner_path":
            r["targets"][0]["owner_paths"][0]["role"] = "arbitrary metadata"
        elif change == "no_primary":
            r["evidence"][0]["kind"] = "prior_review"

    f.seal(alter)
    assert_refused_without_writes(f, message)


def test_shared_concept_requires_explicit_both_row_group_decisions(f):
    row = f.request["decisions"][1]
    row.update(
        disposition="CREATE_DISTINCT_CONCEPT",
        concept_key="new",
        owner_operation="OP2",
        identity_holds=[],
    )
    f.seal()
    m = f.prepare()
    assert len(m["assignments"]) == 3 and m["assignments"][f.new] == "MIM:0000003"
    assert f.held not in m["outputs"] and len(m["decisions"]) == 2 and len(m["source_cases"]) == 4
    f.accept()
    api.apply(f.root, f.stage, f.acceptance, f.receipt, enabled=True)
    assert not (f.root / f.held).exists()


def test_bind_existing_does_not_mint_or_rewrite_scientific_identity(f):
    row = f.request["decisions"][0]
    row.update(
        disposition="BIND_EXISTING_CONCEPT_ONLY",
        concept_key=None,
        owner_operation=None,
        existing_mim_id="MIM:0000001",
    )
    f.seal()
    m = f.prepare()
    assert (
        set(m["assignments"].values()) == {"MIM:0000001", "MIM:0000002"}
        and f.new not in m["outputs"]
        and f.held not in m["outputs"]
    )
    assert m["outputs"][str(api.REGISTRY_PATH)] == api.sha(
        (f.root / api.REGISTRY_PATH).read_bytes()
    )
    assert len(m["decisions"]) == 2 and len(m["source_cases"]) == 4


def test_all_withheld_mints_no_ids_but_preserves_full_accounting(f):
    f.request["decisions"][0].update(
        disposition="WITHHOLD_IDENTITY", concept_key=None, owner_operation=None
    )
    f.seal()
    m = f.prepare()
    assert (
        set(m["assignments"].values()) == {"MIM:0000001", "MIM:0000002"}
        and len(m["after_inventory"]) == 2
    )
    assert len(m["decisions"]) == 2 and len(m["source_cases"]) == 4


@pytest.mark.parametrize(
    "target", ["owner", "evidence", "legacy_owner", "head", "index", "unexpected_owner"]
)
def test_drift_between_prepare_and_apply_refuses_before_managed_writes(f, target):
    f.prepare()
    f.accept()
    if target == "owner":
        (f.root / f.paths[0]).write_bytes((f.root / f.paths[0]).read_bytes() + b"\n")
    elif target == "evidence":
        (f.root / "primary.txt").write_text("changed evidence")
    elif target == "legacy_owner":
        (f.legacy / f.held).write_bytes((f.legacy / f.held).read_bytes() + b"\n")
    elif target == "head":
        command(f.root, "commit", "--allow-empty", "-m", "Concurrent change")
    elif target == "index":
        (f.root / "new.txt").write_text("pending")
        command(f.root, "add", "new.txt")
    else:
        (f.root / "data/ingredients/unmapped/Extra.yaml").write_bytes(
            (f.root / f.paths[1]).read_bytes()
        )
    before = managed(f)
    with pytest.raises((ValueError, RuntimeError)):
        api.apply(f.root, f.stage, f.acceptance, f.receipt, enabled=True)
    assert managed(f) == before and not f.receipt.exists()


@pytest.mark.parametrize("mutation", ["record", "aggregate_count", "ledger", "manifest_scope"])
def test_prepared_output_substitution_even_with_updated_local_hash_is_rejected(f, mutation):
    m = f.prepare()
    if mutation == "manifest_scope":
        m["source_cases"] = m["source_cases"][1:]
    else:
        if mutation == "record":
            name = f.new
            v = yaml.safe_load((f.stage / "candidate" / name).read_bytes())
            v["preferred_term"] = "Substituted"
        elif mutation == "aggregate_count":
            name = api.AGGREGATES[1]
            v = yaml.safe_load((f.stage / "candidate" / name).read_bytes())
            v["mapped_count"] = 99
        else:
            name = str(api.REGISTRY_PATH)
            v = None
        path = f.stage / "candidate" / name
        path.write_bytes(
            yaml.safe_dump(v, sort_keys=False).encode()
            if v
            else path.read_bytes().replace(b"New", b"Imposter")
        )
        m["outputs"][name] = api.sha(path.read_bytes())
        if name in m["after_inventory"]:
            m["after_inventory"][name] = m["outputs"][name]
    write(f.stage / "manifest.json", m)
    f.accept()
    before = managed(f)
    with pytest.raises(ValueError):
        api.apply(f.root, f.stage, f.acceptance, f.receipt, enabled=True)
    assert managed(f) == before and not f.receipt.exists()


def test_apply_is_dry_run_without_explicit_apply(f):
    f.prepare()
    f.accept()
    before = managed(f)
    result = api.apply(f.root, f.stage, f.acceptance, f.receipt)
    assert (
        not result["applied"]
        and result["approval"] == "NONE"
        and managed(f) == before
        and not f.receipt.exists()
    )


def test_partial_failure_reports_actual_observation_and_preserves_recovery(f, monkeypatch):
    f.prepare()
    f.accept()
    before = managed(f)
    native = api.apply.__globals__["_new_owner"]
    calls = []

    def fail_after_first(*args, **kwargs):
        value = native(*args, **kwargs)
        calls.append(value)
        raise OSError("synthetic failure after actual guarded creation")

    monkeypatch.setitem(api.apply.__globals__, "_new_owner", fail_after_first)
    with pytest.raises(OSError, match="after actual"):
        api.apply(f.root, f.stage, f.acceptance, f.receipt, enabled=True)
    receipt = json.loads((f.receipt / "application.json").read_bytes())
    assert calls and receipt["state"] == "FAILED" and receipt["recovery_required"]
    assert receipt["observed_outputs"][f.move]["sha256"] == api.sha((f.root / f.move).read_bytes())
    assert (f.root / f.paths[1]).read_bytes() == before[f.paths[1]]
    assert all(
        (f.root / ref["path"]).read_bytes() == before[name]
        for name, ref in receipt["beforeimages"].items()
    )
    with pytest.raises(ValueError):
        api.verify_completed(f.root, f.stage, f.receipt / "application.json")
    snapshot = managed(f)
    with pytest.raises(ValueError):
        api.apply(f.root, f.stage, f.acceptance, f.receipt, enabled=True)
    assert managed(f) == snapshot


def test_completed_receipt_verifies_after_ordinary_commit_and_rejects_tampering(f):
    f.prepare()
    f.accept()
    api.apply(f.root, f.stage, f.acceptance, f.receipt, enabled=True)
    commit(f.root)
    assert (
        api.verify_completed(f.root, f.stage, f.receipt / "application.json")["status"]
        == "COMPLETE_CURRENT_CANDIDATE"
    )
    p = f.receipt / "application.json"
    v = json.loads(p.read_bytes())
    v["completed_operations"].pop()
    write(p, v)
    with pytest.raises(ValueError, match="prepared input closure is incomplete"):
        api.verify_completed(f.root, f.stage, p)


def test_duplicate_yaml_keys_cannot_replace_an_owner(f):
    path = f.root / f.paths[0]
    path.write_bytes(path.read_bytes() + b"preferred_term: Duplicate\n")
    f.request["target_inventory"][f.paths[0]] = api.sha(path.read_bytes())
    f.save()
    assert_refused_without_writes(f, "Duplicate")


def test_receipt_alias_refuses_without_writes(f):
    f.prepare()
    f.accept()
    f.receipt.symlink_to(f.stage, target_is_directory=True)
    before = managed(f)
    with pytest.raises(ValueError, match="alias|symlink"):
        api.apply(f.root, f.stage, f.acceptance, f.receipt, enabled=True)
    assert managed(f) == before


@pytest.mark.parametrize("spelling", [".temp/../escaped", ".temp/../../escaped"])
@pytest.mark.parametrize("operation", ["prepare", "receipt"])
def test_1315_traversal_never_creates_an_escaped_output(f, spelling, operation):
    path = f.root / spelling
    resolved = path.resolve()
    assert not resolved.exists()
    before = managed(f)
    if operation == "prepare":
        with pytest.raises(ValueError, match="traversal"):
            api.prepare(f.root, f.request_path, path)
    else:
        f.prepare()
        f.accept()
        with pytest.raises(ValueError, match="traversal"):
            api.apply(f.root, f.stage, f.acceptance, path, enabled=True)
    assert not resolved.exists() and managed(f) == before


@pytest.mark.parametrize(
    "mutation", ["drop_deferred", "drop_retired", "upgrade_deferred", "replace_payload"]
)
def test_complete_original_crosswalk_cannot_shrink_or_reclassify(f, mutation):
    path = f.root / f.request["origin_accounting"]["path"]
    rows = json.loads(path.read_bytes())
    if mutation == "drop_deferred":
        rows = [r for r in rows if r["status"] != "deferred"]
    elif mutation == "drop_retired":
        rows = [r for r in rows if r["status"] != "retired"]
    elif mutation == "upgrade_deferred":
        rows[-2].update(
            status="apply", operation_id="OP2", payload_sha256=rows[1]["payload_sha256"]
        )
    else:
        rows[0]["payload_sha256"] = "0" * 64
    write(path, rows)
    f.request["origin_accounting"]["sha256"] = api.sha(path.read_bytes())
    f.save()
    assert_refused_without_writes(f, "crosswalk|origin")


def test_before_inventory_requires_actual_original_git_bytes(f):
    original = json.loads((f.legacy / "before.json").read_bytes())
    original["owners"][f.paths[0]] = "0" * 64
    write(f.legacy / "before.json", original)
    plan = json.loads((f.legacy / "plan.json").read_bytes())
    plan["before_inventory"]["sha256"] = api.sha((f.legacy / "before.json").read_bytes())
    write(f.legacy / "plan.json", plan)
    receipt = json.loads((f.legacy / "application.json").read_bytes())
    receipt["plan"]["sha256"] = api.sha((f.legacy / "plan.json").read_bytes())
    receipt["before_inventory"] = original["owners"]
    write(f.legacy / "application.json", receipt)
    for key, name in [("plan", "plan.json"), ("application", "application.json")]:
        f.request["legacy"][key]["sha256"] = api.sha((f.legacy / name).read_bytes())
    f.save()
    assert_refused_without_writes(f, "actual Git baseline")


@pytest.mark.parametrize("boundary", ["parent", "leaf"])
def test_late_preparation_alias_refuses_without_writing_through_it(f, monkeypatch, boundary):
    destination = f.root / "outside-owned-stage"
    destination.mkdir()
    sentinel = destination / "Exact.yaml"
    sentinel.write_text("unrelated sentinel")
    native = api.PreparationTree.put
    attacked = []

    def swapped(self, name, raw):
        if not attacked and name.endswith("mapped/Exact.yaml"):
            attacked.append(name)
            path = self.stage / name
            if boundary == "parent":
                path.parent.rename(path.parent.with_name("original-mapped"))
                path.parent.symlink_to(destination, target_is_directory=True)
            else:
                path.symlink_to(sentinel)
        return native(self, name, raw)

    monkeypatch.setattr(api.PreparationTree, "put", swapped)
    before = managed(f)
    with pytest.raises((ValueError, OSError), match="alias|symlink|changed|exists"):
        f.prepare()
    assert (
        attacked
        and sentinel.read_text() == "unrelated sentinel"
        and set(destination.iterdir()) == {sentinel}
    )
    assert managed(f) == before and not (f.stage / "manifest.json").exists()


def test_in_memory_writer_refuses_closed_schema_error_without_any_path_write(f):
    bad = copy.deepcopy(f.original[0])
    bad["mim_id"] = "MIM:0000001"
    bad["invented_scientific_field"] = True
    with pytest.raises(Exception, match="validation failed"):
        api.serialized(bad, f.root / api.SCHEMA)
    assert not f.stage.exists()


def test_native_sink_matches_default_records_names_and_stats(tmp_path):
    native = api._CAPTURE.script("scripts/export_individual_records.py")
    records = [
        {
            "identifier": "UNMAPPED_1",
            "preferred_term": "Alpha",
            "mapping_status": "UNMAPPED",
            "mim_id": "MIM:0000001",
        },
        {
            "identifier": "UNMAPPED_2",
            "preferred_term": "alpha",
            "mapping_status": "UNMAPPED",
            "mim_id": "MIM:0000002",
        },
    ]
    source = tmp_path / "collection.yaml"
    source.write_text(yaml.safe_dump({"ingredients": records}))
    default = tmp_path / "default"
    sink_directory = tmp_path / "untouched"
    sink_directory.mkdir()
    sentinel = sink_directory / "keep.yaml"
    sentinel.write_text("existing unrelated bytes")
    preserved = native.PreservedFields()
    preserved.by_mim_id["MIM:0000001"] = {"discussions": [{"topic": "Synthetic authored field"}]}
    expected = native.export_collection_to_individual_files(source, default, preserved=preserved)
    received = {}
    actual = native.export_collection_to_individual_files(
        source,
        sink_directory,
        preserved=preserved,
        record_sink=lambda p, r: received.update({p.name: copy.deepcopy(r)}),
    )
    assert actual == expected and actual["collisions"] == 1
    assert received == {p.name: yaml.safe_load(p.read_bytes()) for p in default.iterdir()}
    assert (
        set(sink_directory.iterdir()) == {sentinel}
        and sentinel.read_text() == "existing unrelated bytes"
    )
    assert received["Alpha.yaml"]["discussions"] == [{"topic": "Synthetic authored field"}]
    with pytest.raises(ValueError, match="mutually exclusive"):
        native.export_collection_to_individual_files(
            source, sink_directory, dry_run=True, record_sink=lambda *_: None
        )


@pytest.mark.parametrize("empty", [False, True])
def test_native_sink_retains_empty_and_duplicate_id_guards(tmp_path, empty):
    native = api._CAPTURE.script("scripts/export_individual_records.py")
    record = {
        "identifier": "UNMAPPED_1",
        "preferred_term": "Same",
        "mapping_status": "UNMAPPED",
        "mim_id": "MIM:0000001",
    }
    source = tmp_path / "collection.yaml"
    source.write_text(
        yaml.safe_dump({"ingredients": [] if empty else [record, copy.deepcopy(record)]})
    )
    sink_directory = tmp_path / "untouched"
    seen = []
    if empty:
        stats = native.export_collection_to_individual_files(
            source, sink_directory, record_sink=lambda *x: seen.append(x)
        )
        assert stats["total"] == 0 and stats["created"] == 0
    else:
        with pytest.raises(Exception, match="[Dd]uplicate"):
            native.export_collection_to_individual_files(
                source, sink_directory, record_sink=lambda *x: seen.append(x)
            )
    assert not sink_directory.exists() and not seen


def test_completed_exact_rerun_is_read_only(f):
    f.prepare()
    f.accept()
    api.apply(f.root, f.stage, f.acceptance, f.receipt, enabled=True)
    before = managed(f)
    receipt = (f.receipt / "application.json").read_bytes()
    result = api.apply(f.root, f.stage, f.acceptance, f.receipt, enabled=True)
    assert result["unchanged"] and not result["applied"]
    assert managed(f) == before and (f.receipt / "application.json").read_bytes() == receipt


def test_native_busy_lease_refuses_without_writes(f):
    f.prepare()
    f.accept()
    before = managed(f)
    locks = api.Claw(f.claw).modules["locks"].LockManager()
    with locks.lock("mediaingredientmech", "synthetic competing writer"):
        with pytest.raises(RuntimeError, match="acquire lock"):
            api.apply(f.root, f.stage, f.acceptance, f.receipt, enabled=True)
    assert managed(f) == before and not f.receipt.exists()


def test_lost_native_lease_refuses_complete_and_preserves_diagnostic(f, monkeypatch):
    f.prepare()
    f.accept()
    before = managed(f)
    original = api.Claw.__init__
    seen = []

    def wrapped(self, root):
        original(self, root)
        klass = self.modules["locks"].LockManager
        check = klass.check_lock

        def lost(instance, resource):
            value = check(instance, resource)
            if value and resource == "mediaingredientmech" and resource in instance._leases:
                seen.append(resource)
                if len(seen) > 1:
                    return {**value, "lease_token": "another-writer"}
            return value

        klass.check_lock = lost

    monkeypatch.setattr(api.Claw, "__init__", wrapped)
    with pytest.raises(ValueError, match="lease lost"):
        api.apply(f.root, f.stage, f.acceptance, f.receipt, enabled=True)
    receipt = json.loads((f.receipt / "application.json").read_bytes())
    assert (
        seen
        and receipt["state"] == "FAILED"
        and receipt["recovery_required"]
        and not receipt["completed_operations"]
    )
    assert managed(f) == before


@pytest.mark.parametrize("phase", ["relocation", "aggregate", "ledger", "completion"])
def test_partial_phase_failures_never_claim_complete(f, monkeypatch, phase):
    f.prepare()
    f.accept()
    globals_ = api.apply.__globals__
    if phase == "relocation":
        old = globals_["_retire"]

        def changed(*args, **kwargs):
            old(*args, **kwargs)
            raise OSError("synthetic post-relocation failure")

        monkeypatch.setitem(globals_, "_retire", changed)
    elif phase in {"aggregate", "ledger"}:
        old = globals_["publish_validated"]

        def changed(target, *args, **kwargs):
            value = old(target, *args, **kwargs)
            if (phase == "aggregate" and str(target.path).endswith(api.AGGREGATES[0])) or (
                phase == "ledger" and target.path == f.root / api.REGISTRY_PATH
            ):
                raise OSError("synthetic post-" + phase + " failure")
            return value

        monkeypatch.setitem(globals_, "publish_validated", changed)
    else:

        def changed(*args, **kwargs):
            raise OSError("synthetic completion receipt failure")

        monkeypatch.setitem(globals_, "finish_receipt", changed)
    with pytest.raises(OSError, match="synthetic"):
        api.apply(f.root, f.stage, f.acceptance, f.receipt, enabled=True)
    receipt = json.loads((f.receipt / "application.json").read_bytes())
    assert (
        receipt["state"] == "FAILED"
        and receipt["recovery_required"]
        and receipt["observed_outputs"]
    )
    assert receipt["beforeimages"] and receipt["completed_operations"]
    with pytest.raises(ValueError, match="completed adoption"):
        api.verify_completed(f.root, f.stage, f.receipt / "application.json")


def test_administrative_inverse_preserves_science_and_both_history_lineages(f):
    m = f.prepare()
    for stable, legacy in ((f.paths[0], f.paths[0]), (f.paths[1], f.move)):
        current = yaml.safe_load((f.stage / "candidate" / legacy).read_bytes())
        scientific = yaml.safe_load((f.legacy / legacy).read_bytes())
        original_stable = yaml.safe_load((f.root / stable).read_bytes())
        assert current["mim_id"] == original_stable["mim_id"]
        assert (
            current["curation_history"][: len(scientific["curation_history"])]
            == scientific["curation_history"]
        )
        for event in original_stable["curation_history"]:
            assert event in current["curation_history"]
        restored = {
            k: v
            for k, v in current.items()
            if k not in {"mim_id", "legacy_identifiers", "curation_history"}
        }
        assert restored == {
            k: v
            for k, v in scientific.items()
            if k not in {"mim_id", "legacy_identifiers", "curation_history"}
        }
    assert m["scientific_approval_added"] is False
    assert not any("sssom" in p or "UNIFIED" in p for p in m["outputs"])


def test_mutated_selected_producer_is_refused(f):
    path = f.root / "scripts/export_individual_records.py"
    path.write_bytes(path.read_bytes() + b"\n# changed selected producer\n")
    assert_refused_without_writes(f, "producer|source|compiled")


def mutated_api(f, old, new):
    import types

    source = f.root / "src/mediaingredientmech/curate/stable_id_adoption.py"
    text = source.read_text()
    assert text.count(old) == 1
    source.write_text(text.replace(old, new))
    loader_path = f.root / "src/mediaingredientmech/curate/adoption_producer.py"
    raw = loader_path.read_bytes()
    module = types.ModuleType("_synthetic_adoption_mutation_loader")
    module.__file__ = str(loader_path)
    exec(compile(raw, str(loader_path), "exec"), module.__dict__)
    capture, implementation = module.load(f.root, raw)
    capture.verify()
    return implementation


@pytest.mark.parametrize("mutation", ["unsupported_science", "same_reviewer"])
def test_real_mutations_demonstrate_native_admission_guards(f, mutation):
    if mutation == "unsupported_science":
        f.seal(
            lambda role, r: (
                r["assessments"][0].update(outcome="unknown") if role == "skeptic" else None
            )
        )
        message = "unsupported concept"
        old = 'assessment["outcome"] == "supported"'
        new = 'True or assessment["outcome"] == "supported"'
    else:
        f.seal(
            lambda role, r: r["reviewer"].update(identity="primary") if role == "skeptic" else None
        )
        message = "separate skeptical"
        old = 'and results[0]["reviewer"]["identity"] != results[1]["reviewer"]["identity"]'
        new = "and True  # synthetic mutation removes reviewer separation"
    assert_refused_without_writes(f, message)
    mutant = mutated_api(f, old, new)
    result = mutant.prepare(f.root, f.request_path, f.stage)
    # Actual unsafe candidate admission, not an import/setup exception, is the
    # positive mutation control. Synthetic outputs are never applied.
    assert result["status"] == "PREPARED_CANDIDATE_ONLY"
    assert result["assignments"][f.new] == "MIM:0000003" and (f.stage / "manifest.json").exists()
    assert not (f.root / f.new).exists()


def test_uncommitted_completed_phase_log_tampering_is_refused(f):
    f.prepare()
    f.accept()
    api.apply(f.root, f.stage, f.acceptance, f.receipt, enabled=True)
    path = f.receipt / "application.json"
    value = json.loads(path.read_bytes())
    value["completed_operations"].pop()
    write(path, value)
    with pytest.raises(ValueError, match="completed phase log"):
        api.verify_completed(f.root, f.stage, path)


def test_1317_unknown_hold_partition_is_an_unassessed_question_not_empty_approval(f):
    original = api.inspect(f.root, f.request_path)
    before = managed(f)
    for row in f.request["decisions"]:
        row.update(
            disposition=None,
            identity_holds=None,
            other_holds=None,
            concept_key=None,
            owner_operation=None,
            existing_mim_id=None,
            primary=None,
            skeptic=None,
        )
    f.save()
    pending = api.inspect(f.root, f.request_path)
    assert pending["payloads"] == original["payloads"] and pending["context"] == original["context"]
    assert (
        pending["payloads"][1]["original_eligibility_context"]["known_conditions_and_holds"][0][
            "literal_value"
        ]
        == "ambiguous supplied form"
    )
    assert managed(f) == before
    assert_refused_without_writes(f, "unassessed concept")


def test_1317_positive_disposition_cannot_treat_null_identity_classification_as_clear(f):
    f.request["decisions"][0]["identity_holds"] = None
    f.save()
    assert_refused_without_writes(f, "unassessed residual identity")


def test_1317_unclassified_other_scope_does_not_force_role_review(f):
    f.request["decisions"][0]["other_holds"] = None
    f.seal()
    view = api.inspect(f.root, f.request_path)
    assert (
        view["payloads"][0]["original_eligibility_context"]["known_conditions_and_holds"][0][
            "literal_value"
        ]
        == "role provisional"
    )
    manifest = f.prepare()
    assert manifest["decisions"][0]["other_holds"] is None
    record = yaml.safe_load((f.stage / "candidate" / f.new).read_bytes())
    assert record["mapping_status"] == "UNMAPPED" and "roles" not in record


@pytest.mark.parametrize(
    "change",
    [
        "missing_classification",
        "conflicting_classification",
        "wrong_intake_owner",
        "missing_intake_candidate",
    ],
)
def test_1317_native_current_hold_binding_refuses_missing_or_conflicting_evidence(f, change):
    if change in {"missing_classification", "conflicting_classification"}:

        def alter(role, report):
            if role != "skeptic":
                return
            dimensions = report["assessments"][0]["dimensions"]
            if change == "missing_classification":
                report["assessments"][0]["dimensions"] = [
                    v for v in dimensions if v["name"] != "residual_identity_holds"
                ]
            else:
                next(v for v in dimensions if v["name"] == "residual_identity_holds")[
                    "value"
                ] = '["unresolved supplied form"]'

        f.seal(alter)
        message = "residual hold classification"
    else:
        ref = f.request["eligibility_intake"]
        path = f.root / ref["path"]
        value = json.loads(path.read_bytes())
        if change == "wrong_intake_owner":
            value["candidates"][0]["owner_sha256"] = "0" * 64
        else:
            value["candidates"].pop()
        write(path, value)
        ref["sha256"] = api.sha(path.read_bytes())
        f.save()
        message = "intake"
    assert_refused_without_writes(f, message)


def test_current_policy_drift_invalidates_inspected_context(f):
    path = f.root / "MAPPING_SEMANTICS.md"
    path.write_bytes(path.read_bytes() + b"\nchanged current policy\n")
    assert_refused_without_writes(f, "producer|source|compiled")


@pytest.mark.parametrize("operation", ["inspect", "prepare", "apply", "verify"])
def test_1315_target_root_traversal_is_refused_before_native_input_reads(f, monkeypatch, operation):
    (f.root / ".temp").mkdir(exist_ok=True)
    alias = f.root / ".temp/.."
    before = managed(f)

    def forbidden(*_args, **_kwargs):
        raise AssertionError("target read ran before root rejection")

    monkeypatch.setattr(api.FrozenFile, "capture", forbidden)
    with pytest.raises(ValueError, match="target root traversal"):
        if operation == "inspect":
            api.inspect(alias, f.request_path)
        elif operation == "prepare":
            api.prepare(alias, f.request_path, f.stage)
        elif operation == "apply":
            api.apply(alias, f.stage, f.root / "absent-acceptance.json", f.receipt, enabled=True)
        else:
            api.verify_completed(alias, f.stage, f.receipt / "application.json")
    assert managed(f) == before and not f.stage.exists() and not f.receipt.exists()


@pytest.mark.parametrize("role", ["legacy", "Claw"])
def test_1315_input_root_traversal_refuses_before_reading_that_root(f, monkeypatch, role):
    actual = f.legacy if role == "legacy" else f.claw
    (actual / ".temp").mkdir()
    alias = actual / ".temp/.."
    if role == "legacy":
        f.request["legacy"]["root"] = str(alias)
    else:
        f.request["claw_root"] = str(alias)
    f.save()
    native = api.FrozenFile.capture
    reads = []

    def captured(path):
        if Path(path).is_relative_to(actual):
            reads.append(str(path))
            raise AssertionError("aliased source read before root rejection")
        return native(path)

    monkeypatch.setattr(api.FrozenFile, "capture", captured)
    assert_refused_without_writes(f, role + " root traversal")
    assert not reads


@pytest.mark.parametrize("relation", ["same", "legacy_nested", "target_nested"])
def test_native_root_disjointness_still_refuses_both_directions(f, relation):
    if relation == "same":
        path = f.root
    elif relation == "legacy_nested":
        path = f.root / "nested-legacy"
        path.mkdir()
    else:
        path = f.root.parent
    f.request["legacy"]["root"] = str(path)
    f.save()
    assert_refused_without_writes(f, "roots overlap")
