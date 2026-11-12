"""Real native adoption/generation/publication and refusal regressions (#1335)."""

from __future__ import annotations

import gzip
import json
import os
import shutil
import subprocess
from contextlib import contextmanager
from pathlib import Path
from types import SimpleNamespace

import pytest

from mediaingredientmech.curate import stable_sssom_publication as pub
from tests.stable_publication_fixture import (
    CLAW_REVISION,
    PACKAGED_PRODUCER,
    completed_adoption,
    materialize_producer,
)
from tests.test_stable_id_adoption import ROOT, api, commit, initialize, write


def digest(path):
    return api.sha(path.read_bytes())


def ref(root, path):
    return {"path": str(path.relative_to(root)), "sha256": digest(path)}


def current_outputs(root):
    return {
        name: (root / name).read_bytes() if (root / name).exists() else None for name in pub.OUTPUTS
    }


@contextmanager
def restore(paths):
    originals = {path: path.read_bytes() if path.exists() else None for path in paths}
    try:
        yield
    finally:
        for path, raw in originals.items():
            if raw is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(raw)


class PublicationFixture:
    def __init__(self, tmp, monkeypatch, producer):
        extra = {name: ROOT / name for name in pub._CAPTURE.files}
        self.adoption = completed_adoption(tmp / "adoption", monkeypatch, additional_sources=extra)
        self.root = self.adoption.root
        self.counter = 0
        self.producer = tmp / "producer"
        if producer is None:
            materialize_producer(self.producer)
            assert api.git(self.producer, "rev-parse", "HEAD").decode().strip() != CLAW_REVISION
        else:
            subprocess.run(
                ["git", "clone", "--no-hardlinks", "--no-local", str(producer), str(self.producer)],
                check=True,
                capture_output=True,
                timeout=120,
            )
            assert api.git(self.producer, "rev-parse", "HEAD").decode().strip() == CLAW_REVISION
        self.kg = tmp / "kg-microbe"
        initialize(self.kg)
        mapping = self.kg / "mappings/kgmicrobe_unified_entity_mappings.sssom.tsv.gz"
        mapping.parent.mkdir()
        mapping.write_bytes(
            gzip.compress(
                b"subject_id\tsubject_label\tpredicate_id\tobject_id\tobject_label\tsource\n",
                mtime=0,
            )
        )
        commit(self.kg)
        # Preserve a genuine historical suppression independently of the New
        # token that the actual producer will suppress from the current owner.
        before = {
            "subject_id": "MIM:Exact",
            "token_key": "historical blocked alias",
            "token": "historical blocked alias",
            "owner_subject_ids": json.dumps(["MIM:New"]),
            "disposition": "SUPPRESS",
            "input_surfaces": json.dumps(["historical.fixture"]),
            "source_refs": json.dumps(["synthetic historical source"]),
            "evidence_refs": json.dumps(["synthetic historical evidence"]),
        }
        (self.root / pub.SUPPRESSIONS).write_bytes(pub._tsv(pub.SIDECAR_FIELDS, [before]))
        self.history_root = tmp / "historical-review"
        initialize(self.history_root)
        for name in ("MAPPING_SEMANTICS.md", "primary.txt"):
            shutil.copyfile(self.root / name, self.history_root / name)
        historical_head = commit(self.history_root)
        historical_target = {
            "target_id": "original-obligation",
            "kind": "snapshot_row",
            "label": "Synthetic original provenance obligation",
            "path": "primary.txt",
            "selector": "original-obligation",
            "semantic_digest": {
                "algorithm": "sha256",
                "sha256": digest(self.history_root / "primary.txt"),
                "description": "Original synthetic evidence bytes",
            },
            "owner_paths": [
                {"repository": api.REPOSITORY, "path": "primary.txt", "role": "original evidence"}
            ],
        }
        historical = self.adoption.report(
            "historical-publication", [historical_target], ["primary.txt"], scientific=False
        )
        historical["source"] = self.adoption.native.inspect_source(
            self.history_root,
            [historical_target],
            ["primary.txt", "MAPPING_SEMANTICS.md"],
        )["source"]
        historical["assessments"] = [
            {
                "assessment_id": "retention",
                "area": "completeness",
                "topic": "Original provenance retention",
                "outcome": "supported",
                "summary": "Retain original source tokens and commentary; no current mapping approval",
                "target_ids": ["original-obligation"],
                "evidence_ids": ["primary"],
            }
        ]
        old_review = self.adoption.native.save_review(
            self.history_root,
            historical,
            schema_path=self.root / "schema/record_review.yaml",
        )
        self.history = {
            "root": str(self.history_root),
            "head": historical_head,
            "review": ref(self.history_root, old_review),
            "markdown_sha256": digest(old_review.with_name("review.md")),
        }
        self.generation_dir = self.root / ".temp/publication-generation"
        self.generated = pub.generate(
            self.root,
            self.producer,
            self.kg,
            self.adoption.stage,
            self.adoption.receipt / "application.json",
            self.generation_dir,
        )
        self.generation_receipt = self.generation_dir / "receipt.json"

    def request(
        self,
        *,
        disposition="INSTALL_WITHHOLD",
        alter=None,
        assessed=True,
        policy=None,
        omit_review_inputs=(),
    ):
        self.counter += 1
        prefix = f"publication-{self.counter:03d}"
        directory = self.root / "publication" / prefix
        directory.mkdir(parents=True)
        request_path = directory / "request.json"
        selection_path = directory / "selection.json"
        policy_path = directory / "operational-policy.json"
        write(policy_path, policy or json.loads(self.adoption.policy.read_bytes()))
        request = {
            "schema_version": 1,
            "capability": pub.CAPABILITY,
            "head": api.git(self.root, "rev-parse", "HEAD").decode().strip(),
            "generation": ref(self.root, self.generation_receipt),
            "selection": None,
            "reviews": [],
            "review_inputs": {},
            "operational_policy": ref(self.root, policy_path),
            "historical_reviews": getattr(self, "histories", [self.history]),
        }
        write(request_path, request)
        selection = pub.inspect(self.root, request_path)
        if not assessed:
            return SimpleNamespace(
                path=request_path,
                request=request,
                selection=selection,
                directory=directory,
                prefix=prefix,
            )
        for entry in selection["rows"]:
            entry["disposition"] = (
                disposition if entry["candidate_position"] else "REMOVE_WITH_HISTORY"
            )
            entry["reason"] = (
                "Synthetic installation decision; ordinary export review remains separate"
            )
        if alter:
            alter(selection)
        write(selection_path, selection)
        request["selection"] = ref(self.root, selection_path)
        claims = {entry["entry_id"]: entry for entry in selection["rows"]}
        claims.update({entry["entry_id"]: entry for entry in selection["history"]})
        claims["suppressions"] = selection["suppression"]
        targets = [
            {
                "target_id": key,
                "kind": "snapshot_row",
                "label": key,
                "path": str(selection_path.relative_to(self.root)),
                "selector": key,
                "semantic_digest": {
                    "algorithm": "sha256-canonical-json-v1",
                    "sha256": api.digest(claim),
                    "description": "Complete stable publication selection",
                },
                "owner_paths": [
                    {
                        "repository": api.REPOSITORY,
                        "path": str(selection_path.relative_to(self.root)),
                        "role": "complete stable publication selection",
                    }
                ],
            }
            for key, claim in claims.items()
        ]
        extra_inputs = [
            str(selection_path.relative_to(self.root)),
            "MAPPING_SEMANTICS.md",
            "primary.txt",
            *api.inventory(self.root),
            str(api.REGISTRY_PATH),
            str(api.LIFECYCLE_PATH),
            pub.CONTRACT,
            request["generation"]["path"],
            request["operational_policy"]["path"],
            *(name for name in pub.OUTPUTS if (self.root / name).exists()),
        ]
        if self.generated["adoption"] is not None:
            extra_inputs.append(self.generated["adoption"]["receipt"]["path"])
        else:
            selected = pub.Loaded(self.root, request_path).successor
            extra_inputs.extend(selected.local_inputs())
            extra_inputs.append(self.generated["curation_successor"]["path"])
        extra_inputs = [name for name in extra_inputs if name not in omit_review_inputs]
        for role in ("primary", "skeptic"):
            report = self.adoption.report(f"{prefix}-{role}", targets, extra_inputs)
            report["skill"] = "review-sssom-output"
            report["assessments"] = [
                {
                    "assessment_id": key,
                    "area": "identity",
                    "topic": "Canonical installation",
                    "outcome": "supported",
                    "summary": "Reviewed synthetic installation only",
                    "target_ids": [key],
                    "evidence_ids": ["primary"],
                    "dimensions": [
                        {
                            "name": "publication_action",
                            "value": (
                                "PRESERVE_SUPPRESSION_HISTORY"
                                if key == "suppressions"
                                else (
                                    "PRESERVE_HISTORICAL_OBLIGATIONS"
                                    if key.startswith("history-")
                                    else claim["disposition"]
                                )
                            ),
                            "definition": "Explicit installation disposition",
                            "evidence_ids": ["primary"],
                        },
                        {
                            "name": "publication_scope",
                            "value": "canonical_installation_not_release_approval",
                            "definition": "Installation is distinct from export approval",
                            "evidence_ids": ["primary"],
                        },
                    ],
                }
                for key, claim in claims.items()
            ]
            saved = self.adoption.save_report(report)
            request["reviews"].append(ref(self.root, saved))
            for path in (saved, saved.with_name("review.md")):
                request["review_inputs"][str(path.relative_to(self.root))] = digest(path)
        write(request_path, request)
        return SimpleNamespace(
            path=request_path,
            request=request,
            selection=selection,
            directory=directory,
            prefix=prefix,
        )

    def prepare(self, request=None):
        request = request or self.request()
        stage = self.root / ".temp" / (request.prefix + "-prepared")
        result = pub.prepare(self.root, request.path, stage)
        return request, stage, result

    def destination(self, request, suffix):
        return self.root / ".temp" / (request.prefix + "-" + suffix)

    def accept(self, request, stage, *, alter=None):
        manifest = stage / "manifest.json"
        document = json.loads(manifest.read_bytes())
        relative = str(manifest.relative_to(self.root))
        target = {
            "target_id": "prepared",
            "label": "Prepared publication set",
            "kind": "snapshot_row",
            "path": relative,
            "selector": "prepared",
            "semantic_digest": {
                "algorithm": "sha256",
                "sha256": digest(manifest),
                "description": "Exact prepared manifest bytes",
            },
            "owner_paths": [
                {"repository": api.REPOSITORY, "path": relative, "role": "prepared candidate"}
            ],
        }
        report = self.adoption.report(
            request.prefix + "-technical",
            [target],
            [relative, "primary.txt"],
            scientific=False,
        )
        budget = document["operational_budget"]
        dimensions = {
            "publication_action": "apply_exact_prepared_set",
            "operational_budget_sha256": api.digest(budget),
            "lease_seconds": str(budget["policy_value"]["lease_seconds"]),
            "lease_namespace_sha256": api.digest(budget["lease_namespace"]),
            "lease_scheduling": "mediaingredientmech_and_global_conflict_reviewed",
        }
        report["assessments"] = [
            {
                "assessment_id": "apply",
                "area": "completeness",
                "topic": "Exact publication set",
                "outcome": "supported",
                "summary": "Synthetic independent exact-set acceptance",
                "target_ids": ["prepared"],
                "evidence_ids": ["primary"],
                "dimensions": [
                    {
                        "name": key,
                        "value": value,
                        "definition": "Explicit administrative acceptance",
                        "evidence_ids": ["primary"],
                    }
                    for key, value in dimensions.items()
                ],
            }
        ]
        if alter:
            alter(report)
        saved = self.adoption.save_report(report)
        acceptance = request.directory / "acceptance.json"
        write(
            acceptance,
            {
                "manifest_sha256": digest(manifest),
                "review": ref(self.root, saved),
                "markdown_sha256": digest(saved.with_name("review.md")),
            },
        )
        return acceptance


@pytest.fixture(scope="module")
def publication(tmp_path_factory):
    selected = os.environ.get("STABLE_SSSOM_CLAW_ROOT")
    monkeypatch = pytest.MonkeyPatch()
    try:
        yield PublicationFixture(
            tmp_path_factory.mktemp("native-stable-publication"),
            monkeypatch,
            Path(selected) if selected else None,
        )
    finally:
        monkeypatch.undo()


@pytest.mark.parametrize("kind", ["source", "manifest", "membership"])
def test_1335_packaged_producer_drift_refuses_before_reconstruction(tmp_path, kind):
    source = tmp_path / "source"
    shutil.copytree(PACKAGED_PRODUCER, source)
    if kind == "source":
        target = source / "files/scripts/build_mim_ingredient_sssom.py.txt"
        target.write_bytes(target.read_bytes() + b"\n# changed source\n")
    elif kind == "manifest":
        target = source / "ORIGIN.json"
        target.write_bytes(target.read_bytes() + b"\n")
    else:
        (source / "extra.txt").write_text("not part of the reviewed snapshot")
    destination = tmp_path / "reconstructed"
    with pytest.raises(ValueError, match="changed|membership"):
        materialize_producer(destination, source=source)
    assert not destination.exists()


def test_1335_real_generation_and_unassessed_inspection(publication):
    f = publication
    before = current_outputs(f.root)
    request = f.request(assessed=False)
    assert all(
        row["disposition"] is None and row["reason"] is None for row in request.selection["rows"]
    )
    generated = json.loads((f.generation_dir / "generation.json").read_bytes())
    assert (
        generated["identity_mode"] == "stable"
        and generated["external_sssom_validation"] == "passed"
    )
    assert generated["emitted_rows"] == 1 and len(generated["owner_candidate_accounting"]) == 3
    assert generated["source_binding_candidate"] is None
    assert (
        generated["source_revisions"]["claw"]
        == api.git(f.producer, "rev-parse", "HEAD").decode().strip()
    )
    assert all(
        row["scientific_approval_added"] is False for row in generated["owner_candidate_accounting"]
    )
    assert not (f.root / f.adoption.held).exists()
    assert {row["token_key"] for row in request.selection["suppression"]["proposed"]} == {
        "new",
        "historical blocked alias",
    }
    assert current_outputs(f.root) == before


def test_1336_generation_terminal_boundary_rejects_late_artifact_drift(publication, monkeypatch):
    """Real generation must recheck the triple after its final adoption replay."""
    f = publication
    native = pub.native()
    original = native.verify_completed
    directory = f.root / ".temp/terminal-generation-drift"
    candidate = directory / "candidate.sssom.tsv"
    calls = []

    def verify_then_mutate(*args, **kwargs):
        result = original(*args, **kwargs)
        calls.append(result["status"])
        if len(calls) == 2:
            candidate.write_bytes(candidate.read_bytes() + b"# actual late synthetic drift\n")
        return result

    monkeypatch.setattr(native, "verify_completed", verify_then_mutate)
    before = current_outputs(f.root)
    observed = {"scope": "Synthetic native generation terminal-boundary regression", "calls": calls}
    try:
        result = pub.generate(
            f.root,
            f.producer,
            f.kg,
            f.adoption.stage,
            f.adoption.receipt / "application.json",
            directory,
        )
    except ValueError as error:
        observed.update(status="REFUSED", error=str(error))
    else:
        observed.update(
            status="RETURNED_COMPLETE",
            returned_receipt=result,
            declared_candidate_sha256=result["outputs"]["sssom"]["sha256"],
        )
    observed["actual_candidate_sha256"] = digest(candidate)
    write(directory / "terminal-drift-observation.json", observed)
    assert calls == ["COMPLETE_CURRENT_CANDIDATE", "COMPLETE_CURRENT_CANDIDATE"]
    assert current_outputs(f.root) == before
    assert observed["status"] == "REFUSED", observed
    if (directory / "receipt.json").exists():
        assert json.loads((directory / "receipt.json").read_bytes())["state"] != "COMPLETE"


@pytest.mark.parametrize("disposition", ["INSTALL_WITHHOLD", "INSTALL_SUPPORTED"])
def test_1335_native_prepare_apply_verify_preserves_provenance(publication, disposition):
    f = publication
    with restore([f.root / name for name in pub.OUTPUTS]):
        request, stage, _ = f.prepare(f.request(disposition=disposition))
        acceptance = f.accept(request, stage)
        receipt = f.destination(request, "applied")
        result = pub.apply(f.root, stage, acceptance, receipt, enabled=True)
        assert result["state"] == "COMPLETE" and result["scientific_approval_added"] is False
        verified = pub.verify_completed(f.root, stage, receipt / "application.json")
        assert verified["scientific_approval_added"] is False
        _, _, rows = pub.read_sssom(f.root / pub.CANONICAL)
        assert len(rows) == 1 and rows[0]["subject_id"] == "MIM:0000001"
        assert "Synthetic original provenance comment" in rows[0]["comment"]
        assert "MIM:synthetic-original-source" in rows[0]["source"].split("|")
        assert rows[0]["validation_method"] == ""
        provenance = json.loads((f.root / pub.PROVENANCE).read_bytes())
        assert provenance["ordinary_release_review_required"] is True
        assert provenance["selection"]["rows"][0]["disposition"] == disposition
        assert (
            provenance["selection"]["rows"][0]["before_rows"][0]["row"]["validation_method"]
            == "synthetic-prior-stamp"
        )
        assert {
            row["token_key"] for row in pub._sidecar((f.root / pub.SUPPRESSIONS).read_bytes())
        } == {
            "new",
            "historical blocked alias",
        }


@pytest.mark.parametrize(
    "kind", ["owner", "registry", "lifecycle", "producer", "adoption", "review", "history"]
)
def test_1335_stale_native_input_refuses_before_installation(publication, kind):
    f = publication
    request = f.request()
    path = {
        "owner": f.root / "data/ingredients/mapped/Exact.yaml",
        "registry": f.root / api.REGISTRY_PATH,
        "lifecycle": f.root / api.LIFECYCLE_PATH,
        "producer": f.producer / "scripts/build_mim_ingredient_sssom.py",
        "adoption": f.adoption.receipt / "application.json",
        "review": f.root / request.request["reviews"][0]["path"],
        "history": f.history_root / "primary.txt",
    }[kind]
    before = current_outputs(f.root)
    with restore([path]):
        path.write_bytes(path.read_bytes() + b"\n")
        with pytest.raises(
            (ValueError, FileNotFoundError), match="changed|differs|mismatch|different|input"
        ):
            f.prepare(request)
        assert current_outputs(f.root) == before


def test_1335_missing_diagnostic_sidecar_is_not_a_tsv_only_route(publication):
    f = publication
    request = f.request()
    sidecar = f.root / f.generated["outputs"]["suppressions"]["path"]
    before = current_outputs(f.root)
    with restore([sidecar]):
        sidecar.unlink()
        with pytest.raises((ValueError, FileNotFoundError)):
            f.prepare(request)
        assert current_outputs(f.root) == before


@pytest.mark.parametrize("name", [pub.CANONICAL, pub.SUPPRESSIONS])
def test_1335_current_reviews_must_bind_exact_maintained_beforeimages(publication, name):
    f = publication
    request = f.request(omit_review_inputs=[name])
    before = current_outputs(f.root)
    with pytest.raises(ValueError, match="review omits"):
        f.prepare(request)
    assert current_outputs(f.root) == before


@pytest.mark.parametrize("field", ["comment", "source", "suppression"])
def test_1335_rehashed_and_rereviewed_provenance_loss_is_refused(publication, field):
    f = publication

    def alter(selection):
        if field == "suppression":
            selection["suppression"]["proposed"] = selection["suppression"]["generated"]
        else:
            selection["rows"][0]["proposed_row"][field] = ""

    request = f.request(alter=alter)
    before = current_outputs(f.root)
    with pytest.raises(ValueError, match="complete derived selection differs"):
        f.prepare(request)
    assert current_outputs(f.root) == before


def test_1335_symlink_stage_refuses_without_writing_through_alias(publication):
    f = publication
    request = f.request()
    outside = request.directory / "outside"
    outside.mkdir()
    alias = request.directory / "alias"
    alias.symlink_to(outside, target_is_directory=True)
    before = current_outputs(f.root)
    with pytest.raises(ValueError, match="alias|Symlink|symlink"):
        pub.prepare(f.root, request.path, alias / "prepared")
    assert not list(outside.iterdir()) and current_outputs(f.root) == before


def test_1335_native_competing_lease_refuses_before_output_writes(publication):
    f = publication
    request, stage, _ = f.prepare()
    acceptance = f.accept(request, stage)
    manager = pub.native().Claw(f.producer).modules["locks"].LockManager()
    before = current_outputs(f.root)
    with manager.lock("mediaingredientmech", "synthetic competing publication"):
        with pytest.raises((RuntimeError, ValueError), match="lock|lease"):
            pub.apply(f.root, stage, acceptance, f.destination(request, "blocked"), enabled=True)
    assert current_outputs(f.root) == before


def test_1335_acceptance_cannot_omit_operational_budget(publication):
    f = publication
    request, stage, _ = f.prepare()

    def alter(report):
        report["assessments"][0]["dimensions"] = [
            dimension
            for dimension in report["assessments"][0]["dimensions"]
            if dimension["name"] != "operational_budget_sha256"
        ]

    acceptance = f.accept(request, stage, alter=alter)
    before = current_outputs(f.root)
    with pytest.raises(ValueError, match="budget|operational|acceptance"):
        pub.apply(f.root, stage, acceptance, f.destination(request, "unaccepted"), enabled=True)
    assert current_outputs(f.root) == before


def test_1335_apply_is_dry_run_without_explicit_enable(publication):
    f = publication
    request, stage, _ = f.prepare()
    acceptance = f.accept(request, stage)
    before = current_outputs(f.root)
    receipt = f.destination(request, "dry-run")
    result = pub.apply(f.root, stage, acceptance, receipt, enabled=False)
    assert result["applied"] is False
    assert current_outputs(f.root) == before and not receipt.exists()


def test_1335_insufficient_native_lease_budget_refuses_before_installation(publication):
    f = publication
    policy = json.loads(f.adoption.policy.read_bytes())
    policy["lease_seconds"] = 1
    request = f.request(policy=policy)
    before = current_outputs(f.root)
    with pytest.raises(ValueError, match="lease|budget|forecast|seconds"):
        f.prepare(request)
    assert current_outputs(f.root) == before


def test_1335_lost_native_lease_cannot_leave_a_success_receipt(publication, monkeypatch):
    f = publication
    request, stage, _ = f.prepare()
    acceptance = f.accept(request, stage)
    original = pub.native().Claw.__init__
    seen = []

    def wrapped(instance, root):
        original(instance, root)
        manager = instance.modules["locks"].LockManager
        check = manager.check_lock

        def lost(self, resource):
            value = check(self, resource)
            if value and resource == "mediaingredientmech" and resource in self._leases:
                seen.append(resource)
                if len(seen) > 1:
                    return {**value, "lease_token": "synthetic-other-writer"}
            return value

        manager.check_lock = lost

    before = current_outputs(f.root)
    monkeypatch.setattr(pub.native().Claw, "__init__", wrapped)
    receipt = f.destination(request, "lost-lease")
    with pytest.raises(ValueError, match="lease"):
        pub.apply(f.root, stage, acceptance, receipt, enabled=True)
    assert seen and current_outputs(f.root) == before
    if (receipt / "application.json").exists():
        report = json.loads((receipt / "application.json").read_bytes())
        assert report["state"] != "COMPLETE"


def test_1335_aliased_receipt_never_writes_through_existing_link(publication):
    f = publication
    request, stage, _ = f.prepare()
    acceptance = f.accept(request, stage)
    outside = request.directory / "receipt-outside"
    outside.mkdir()
    alias = request.directory / "receipt-alias"
    alias.symlink_to(outside, target_is_directory=True)
    before = current_outputs(f.root)
    with pytest.raises(ValueError, match="alias|Symlink|symlink"):
        pub.apply(f.root, stage, acceptance, alias, enabled=True)
    assert current_outputs(f.root) == before and not list(outside.iterdir())


def test_1335_postwrite_owner_drift_never_claims_complete(publication, monkeypatch):
    f = publication
    request, stage, _ = f.prepare()
    acceptance = f.accept(request, stage)
    owner = f.root / "data/ingredients/mapped/Exact.yaml"
    globals_ = pub.apply.__globals__
    original = globals_["publish_validated"]
    touched = []

    def drift(*args, **kwargs):
        result = original(*args, **kwargs)
        touched.append(result.path)
        if len(touched) == 1:
            owner.write_bytes(owner.read_bytes() + b"\n# actual late owner change\n")
        return result

    with restore([owner, *[f.root / name for name in pub.OUTPUTS]]):
        monkeypatch.setitem(globals_, "publish_validated", drift)
        receipt = f.destination(request, "postwrite")
        with pytest.raises(ValueError, match="changed|differs"):
            pub.apply(f.root, stage, acceptance, receipt, enabled=True)
        assert touched
        report = json.loads((receipt / "application.json").read_bytes())
        assert report["state"] != "COMPLETE" and report["recovery_required"] is True


def test_1337_historical_root_requires_physical_independence(publication, monkeypatch):
    """Use a real Mac case alias; simulate only physical equivalence elsewhere."""
    f = publication
    request = f.request(assessed=False)
    alias = f.root.with_name(f.root.name.upper())
    samefile = Path.samefile
    actual_alias = alias.exists() and samefile(alias, f.root)
    if actual_alias:
        assert alias != f.root
        review = f.root / f.adoption.request["decisions"][0]["primary"]["path"]
        request.request["historical_reviews"] = [
            {
                "root": str(alias),
                "head": api.git(f.root, "rev-parse", "HEAD").decode().strip(),
                "review": ref(f.root, review),
                "markdown_sha256": digest(review.with_name("review.md")),
            }
        ]
        mode = "actual case-alias directory on this filesystem"
    else:
        # Linux generally has no case-equivalent directory spelling. Keep the
        # already-valid separate historical review and simulate just the
        # physical-equivalence answer, without a skip or privileged mount.
        assert not samefile(f.history_root, f.root)
        pair = {f.history_root, f.root}

        def equivalent(left, right):
            if {Path(left), Path(right)} == pair:
                return True
            return samefile(left, right)

        monkeypatch.setattr(Path, "samefile", equivalent)
        mode = "scoped Path.samefile equivalence simulation on valid distinct roots"
    write(request.path, request.request)
    write(
        request.directory / "physical-root-control.json",
        {
            "issue": 1337,
            "mode": mode,
            "actual_case_alias": actual_alias,
            "target_root": str(f.root),
            "history_root": request.request["historical_reviews"][0]["root"],
        },
    )
    before = current_outputs(f.root)
    with pytest.raises(ValueError, match="physical|independent|same.*root|alias"):
        pub.inspect(f.root, request.path)
    assert current_outputs(f.root) == before


def test_1338_late_kg_head_change_retains_honest_partial_failure(tmp_path, monkeypatch):
    """Advance only a fresh owned KG fixture after the first actual write."""
    f = PublicationFixture(tmp_path / "late-kg-head-fixture", monkeypatch, None)
    request, stage, _ = f.prepare()
    acceptance = f.accept(request, stage)
    receipt = f.destination(request, "late-kg-head")
    before = current_outputs(f.root)
    source = f.kg / "mappings/kgmicrobe_unified_entity_mappings.sssom.tsv.gz"
    source_before = digest(source)
    head_before = api.git(f.kg, "rev-parse", "HEAD").decode().strip()
    globals_ = pub.apply.__globals__
    original = globals_["publish_validated"]
    writes = []

    def advance_after_write(*args, **kwargs):
        result = original(*args, **kwargs)
        writes.append(result.path)
        if len(writes) == 1:
            subprocess.run(
                [
                    "git",
                    "commit",
                    "--allow-empty",
                    "-m",
                    "Synthetic late KG HEAD control for #1338",
                ],
                cwd=f.kg,
                check=True,
                capture_output=True,
                timeout=30,
            )
        return result

    monkeypatch.setitem(globals_, "publish_validated", advance_after_write)
    with pytest.raises(ValueError, match="KG.*(revision|HEAD)"):
        pub.apply(f.root, stage, acceptance, receipt, enabled=True)
    report = json.loads((receipt / "application.json").read_bytes())
    assert report["state"] == "FAILED" and report["recovery_required"] is True
    assert report["completed_operations"] == [
        {
            "path": pub.CANONICAL,
            "sha256": digest(f.root / pub.CANONICAL),
        }
    ]
    after = current_outputs(f.root)
    assert writes == [f.root / pub.CANONICAL] and after[pub.CANONICAL] != before[pub.CANONICAL]
    assert all(after[name] == before[name] for name in pub.OUTPUTS if name != pub.CANONICAL)
    assert digest(source) == source_before
    assert api.git(f.kg, "rev-parse", "HEAD").decode().strip() != head_before
    assert api.git(f.kg, "rev-parse", "HEAD^").decode().strip() == head_before
    with pytest.raises(ValueError, match="completed|complete|COMPLETE"):
        pub.verify_completed(f.root, stage, receipt / "application.json")


@pytest.mark.parametrize(
    "change", ["candidate_comment", "suppression_evidence", "omit_residual", "omit_kg_input"]
)
def test_1339_rehashed_generation_requires_actual_native_output(publication, change):
    """Self-consistent hashes and fresh reviews cannot prove native generation."""
    f = publication
    # This is a genuine completed adoption and native generation. Prove the
    # unchanged invocation is inspectable before altering its claimed outputs.
    request = f.request(assessed=False)
    before = current_outputs(f.root)
    paths = {
        key: f.root / f.generated["outputs"][key]["path"]
        for key in ("sssom", "suppressions", "manifest")
    }
    paths["receipt"] = f.generation_receipt
    observation = {
        "issue": 1339,
        "change": change,
        "scope": "Synthetic native generation proof; no scientific approval",
        "untampered_inspection_passed": True,
        "producer_rerun_after_mutation": False,
        "original_hashes": {name: digest(path) for name, path in paths.items()},
    }
    with restore(list(paths.values())):
        for name, path in paths.items():
            (request.directory / ("original-" + name + ".bin")).write_bytes(path.read_bytes())
        manifest = json.loads(paths["manifest"].read_bytes())
        original_inputs = list(manifest["source_inputs"])
        if change == "candidate_comment":
            raw = paths["sssom"].read_bytes()
            _, fields, rows = pub.read_sssom(paths["sssom"], content=raw)
            assert len(rows) == 1
            rows[0]["comment"] += " | Synthetic addition never emitted by the native producer."
            paths["sssom"].write_bytes(pub._render_candidate(raw, fields, rows))
        elif change == "suppression_evidence":
            rows = pub._sidecar(paths["suppressions"].read_bytes())
            assert len(rows) == 1 and rows[0]["token_key"] == "new"
            rows[0]["evidence_refs"] = json.dumps(
                [
                    *json.loads(rows[0]["evidence_refs"]),
                    "synthetic evidence never emitted by the native producer",
                ]
            )
            paths["suppressions"].write_bytes(pub._tsv(pub.SIDECAR_FIELDS, rows))
        else:
            omitted = (
                f.producer / "workspace/reports/kg_microbe_residual_p25_categorized.json"
                if change == "omit_residual"
                else f.kg / "mappings/kgmicrobe_unified_entity_mappings.sssom.tsv.gz"
            )
            matches = [item for item in original_inputs if item["path"] == str(omitted)]
            assert len(matches) == 1
            if change == "omit_residual":
                assert matches[0]["sha256"] is None and not omitted.exists()
            else:
                assert matches[0]["sha256"] == digest(omitted)
            observation["omitted_input"] = matches[0]
            manifest["source_inputs"] = [
                item for item in original_inputs if item["path"] != str(omitted)
            ]
        # Rehash the full artifact pair, then the manifest, then every receipt
        # output. An ordinary stale-hash guard must not be why this is refused.
        for artifact in manifest["artifacts"]:
            key = "sssom" if artifact["role"] == "sssom" else "suppressions"
            artifact["sha256"] = digest(paths[key])
        write(paths["manifest"], manifest)
        receipt = json.loads(paths["receipt"].read_bytes())
        for key in ("sssom", "suppressions", "manifest"):
            receipt["outputs"][key]["sha256"] = digest(paths[key])
        write(paths["receipt"], receipt)
        request.request["generation"] = ref(f.root, paths["receipt"])
        write(request.path, request.request)
        observation["fresh_generation_ref"] = request.request["generation"]
        observation["modified_hashes"] = {name: digest(path) for name, path in paths.items()}
        for name, path in paths.items():
            (request.directory / ("modified-" + name + ".bin")).write_bytes(path.read_bytes())
        for item in original_inputs:
            path = Path(item["path"])
            assert (digest(path) if path.exists() else None) == item["sha256"]
        observation["original_source_inputs_unchanged"] = True
        try:
            pub.inspect(f.root, request.path)
        except ValueError as error:
            observation["inspect"] = {"status": "REFUSED", "error": str(error)}
        else:
            observation["inspect"] = {"status": "ACCEPTED_MODIFIED_GENERATION"}
        try:
            # On the vulnerable implementation this makes fresh actual native
            # primary/skeptical reviews and prepares the altered triple. The
            # repaired implementation must stop at its genuine inspection;
            # do not bypass that gate to manufacture review acceptance.
            reviewed, stage, prepared = f.prepare()
        except ValueError as error:
            observation["prepare_route"] = {"status": "REFUSED", "error": str(error)}
        else:
            observation["prepare_route"] = {
                "status": "PREPARED_MODIFIED_GENERATION",
                "stage": str(stage),
                "prepared_state": prepared["state"],
                "current_native_reviews": reviewed.request["reviews"],
                "generation_ref": reviewed.request["generation"],
            }
        observation["canonical_before_equals_after"] = current_outputs(f.root) == before
        write(request.directory / "generation-proof-observation.json", observation)
        assert current_outputs(f.root) == before
        for operation in ("inspect", "prepare_route"):
            result = observation[operation]
            assert result["status"] == "REFUSED", observation
            assert any(
                text in result["error"]
                for text in (
                    "native generation replay",
                    "complete native generation input membership differs",
                )
            ), result


def test_1342_native_rule_f_warning_preserves_replay_and_publication_hold(
    tmp_path, monkeypatch, capsys
):
    """Accept genuine diagnostic bytes without approving a dateless publication."""
    from tests import stable_publication_fixture as fixture_source

    original = fixture_source.NativeReviewAdoptionFixture
    native_event = api.record_curation_event

    class WithDatelessExistingOwner(original):
        def __init__(self, *args, **kwargs):
            kwargs["original_records"][1].update(
                identifier="NCIT:C17189",
                mapping_status="MAPPED",
                ontology_mapping={
                    "ontology_id": "NCIT:C17189",
                    "ontology_label": "Synthetic second dated owner",
                    "ontology_source": "NCIT",
                    "mapping_quality": "EXACT_MATCH",
                },
            )

            def date_other_existing_owner(record, **event):
                if record.get("preferred_term") != "Exact":
                    return native_event(record, **event)

            # Only synthetic fixture construction omits this existing owner's
            # date. Native adoption, generation, replay and validation execute
            # with the original event writer restored; no invalid dates or
            # mocked warning output stand in for the real native case.
            with monkeypatch.context() as construction:
                construction.setattr(api, "record_curation_event", date_other_existing_owner)
                super().__init__(*args, **kwargs)
            assert api.record_curation_event is native_event

    monkeypatch.setattr(fixture_source, "NativeReviewAdoptionFixture", WithDatelessExistingOwner)
    f = PublicationFixture(tmp_path / "native-rule-f-diagnostic", monkeypatch, None)
    assert api.record_curation_event is native_event
    assert f.generated["state"] == "COMPLETE"
    assert f.generated["returncode"] == 0
    assert json.loads((f.adoption.receipt / "application.json").read_bytes())["state"] == "COMPLETE"
    warning = "keeping an empty mapping_date for native Rule F review"
    replay_output = capsys.readouterr()
    assert warning in replay_output.err and warning not in replay_output.out
    invocation_stdout = f.root / f.generated["stdout"]["path"]
    assert warning in invocation_stdout.read_text()
    assert digest(invocation_stdout) == f.generated["stdout"]["sha256"]
    original_artifacts = {
        name: digest(f.root / item["path"]) for name, item in f.generated["outputs"].items()
    }
    assert original_artifacts == {
        name: item["sha256"] for name, item in f.generated["outputs"].items()
    }
    candidate = f.root / f.generated["outputs"]["sssom"]["path"]
    _, _, rows = pub.read_sssom(candidate)
    assert len(rows) == 2
    by_subject = {row["subject_id"]: row for row in rows}
    assert by_subject["MIM:0000001"]["mapping_date"] == ""
    assert by_subject["MIM:0000001"]["object_id"] == "NCIT:C80300"
    assert by_subject["MIM:0000002"]["object_id"] == "NCIT:C17189"
    exact = api.load_yaml((f.root / "data/ingredients/mapped/Exact.yaml").read_bytes())
    dated = api.load_yaml((f.root / f.adoption.move).read_bytes())
    assert exact["curation_history"] == []
    assert by_subject["MIM:0000002"]["mapping_date"] == max(
        event["timestamp"][:10] for event in dated["curation_history"]
    )
    assert all(row["predicate_id"] == "skos:exactMatch" for row in rows)
    before = current_outputs(f.root)
    request = f.request()
    stage = f.root / ".temp" / (request.prefix + "-prepared")
    with pytest.raises(ValueError, match="native qc-sssom failed.*Rule F"):
        pub.prepare(f.root, request.path, stage)
    failed = json.loads((stage / "FAILED.json").read_bytes())
    assert failed["state"] == "FAILED_PREPARATION" and failed["canonical_writes"] is False
    _, _, rejects = pub.read_sssom(stage / "rejected.tsv")
    assert len(rejects) == 1 and rejects[0]["subject_id"] == "MIM:0000001"
    assert "mapping_date is empty" in rejects[0]["reject_reason"]
    assert "Rule F: 1" in (stage / "validation.stderr.txt").read_text()
    assert current_outputs(f.root) == before
    assert original_artifacts == {
        name: digest(f.root / item["path"]) for name, item in f.generated["outputs"].items()
    }
    write(
        request.directory / "rule-f-replay-observation.json",
        {
            "issue": 1342,
            "native_adoption": "COMPLETE",
            "native_generation": "COMPLETE",
            "native_event_restored_before_adoption": True,
            "replay_warning_on_stderr": True,
            "original_invocation_stdout": ref(f.root, invocation_stdout),
            "unchanged_native_artifacts": original_artifacts,
            "native_prepare": failed,
            "canonical_before_equals_after": True,
        },
    )
