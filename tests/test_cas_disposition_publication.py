"""Native diagnostic CAS history remains withheld through publication (#1383)."""

import json
import subprocess
from pathlib import Path
from types import SimpleNamespace

import pytest

from mediaingredientmech.curate import stable_sssom_publication as pub
from mediaingredientmech.export import reviewed_sssom as reviewed
from tests import stable_publication_fixture as fixtures
from tests.test_stable_id_adoption import api, commit, write
from tests.test_stable_sssom_publication import PublicationFixture, digest, ref, restore

OVERLAY = Path(__file__).parent / "fixtures/claw_cas_dispositions1193"


def patch_producer(root):
    """Reconstruct exact test-only changed source on the preserved native c1 fixture."""
    origin = json.loads((OVERLAY / "ORIGIN.json").read_bytes())
    patch = (OVERLAY / "producer.patch").read_bytes()
    assert api.sha(patch) == origin["patch_sha256"]
    assert origin["upstream_base"] == fixtures.CLAW_REVISION
    for name, pins in origin["files"].items():
        assert digest(root / name) == pins["before_sha256"]
    subprocess.run(
        ["git", "apply", "--check", "-"], input=patch, cwd=root, check=True, capture_output=True
    )
    subprocess.run(["git", "apply", "-"], input=patch, cwd=root, check=True, capture_output=True)
    for name, pins in origin["files"].items():
        assert digest(root / name) == pins["after_sha256"]
    commit(root)


def cas_request(f, row, owner):
    """Create genuine native synthetic primary/skeptic pairs for one held annotation."""
    claims_path = f.root / "cas-claims.json"
    entry = {
        "entry_id": "held-annotation",
        "row_position": 1,
        "row": row,
        "invalid_tokens": [{"field": "other", "token": "CAS:138-86-7"}],
        "owner": {**ref(f.root, owner), "mim_id": api.load_yaml(owner.read_bytes())["mim_id"]},
        "action": "RETAIN_INVALID_CAS_WITHHOLD",
        "reason": "Synthetic unresolved annotation remains historical.",
        "hold": {
            "issue": "https://github.com/CultureBotAI/MediaIngredientMech/issues/887",
            "reason": "No chemical identity approval.",
        },
        "evidence": ["primary.txt"],
    }
    claims = {
        "schema_version": 1,
        "capability": "reviewed-invalid-cas-dispositions-v1",
        "scope": "diagnostic_candidate_only",
        "scientific_approval": False,
        "author": "synthetic-fixture",
        "head": api.git(f.root, "rev-parse", "HEAD").decode().strip(),
        "canonical": ref(f.root, f.root / pub.CANONICAL),
        "source_correction": None,
        "evidence_inputs": {"primary.txt": digest(f.root / "primary.txt")},
        "entries": [entry],
    }
    write(claims_path, claims)
    target = {
        "target_id": entry["entry_id"],
        "kind": "snapshot_row",
        "label": "Synthetic invalid annotation",
        "path": claims_path.name,
        "selector": entry["entry_id"],
        "owner_paths": [
            {"repository": api.REPOSITORY, "path": entry["owner"]["path"], "role": "Current owner"}
        ],
        "semantic_digest": {
            "algorithm": "sha256-canonical-json-v1",
            "sha256": api.digest(entry),
            "description": "Complete diagnostic CAS disposition",
        },
    }
    inputs = [
        claims_path.name,
        pub.CANONICAL,
        entry["owner"]["path"],
        "primary.txt",
        "MAPPING_SEMANTICS.md",
        "schema/record_review.yaml",
        "scripts/record_review.py",
    ]
    request = {
        "schema_version": 1,
        "capability": claims["capability"],
        "claims": ref(f.root, claims_path),
        "reviews": [],
        "review_inputs": {},
    }
    for role in ("primary", "skeptic"):
        report = f.adoption.report("cas-" + role, [target], inputs)
        report["verdict"] = "pass_with_limitations"
        report["limitations"] = [
            "Synthetic diagnostic retention only; invalid CAS and release hold remain unresolved."
        ]
        report["assessments"] = [
            {
                "assessment_id": "cas",
                "area": "identity",
                "topic": "Diagnostic scope",
                "outcome": "supported",
                "summary": "Synthetic retained invalid assertion, no release approval.",
                "target_ids": [target["target_id"]],
                "evidence_ids": ["primary"],
                "dimensions": [
                    {
                        "name": k,
                        "value": v,
                        "definition": "Exact diagnostic scope",
                        "evidence_ids": ["primary"],
                    }
                    for k, v in {
                        "cas_disposition": entry["action"],
                        "diagnostic_scope": "diagnostic_candidate_only",
                        "hold_disposition": "WITHHOLD",
                    }.items()
                ],
            }
        ]
        pair = f.adoption.save_report(report)
        assert f.adoption.native.read_review(f.root, str(pair.relative_to(f.root))) == report
        request["reviews"].append(ref(f.root, pair))
        request["review_inputs"].update(
            {item["path"]: item["sha256"] for item in report["source"]["inputs"]}
        )
        request["review_inputs"][str(pair.with_name("review.md").relative_to(f.root))] = digest(
            pair.with_name("review.md")
        )
    path = f.root / "cas-request.json"
    write(path, request)
    return path


@pytest.fixture(scope="module")
def cas_native(tmp_path_factory):
    """Real completed adoption, native CAS pairs, native CLI and captured replay."""
    patcher = pytest.MonkeyPatch()
    original = fixtures.NativeReviewAdoptionFixture.__init__

    def constructor(self, *args, **kwargs):
        kwargs["original_records"][0]["chemical_properties"] = {"cas_rn": "138-86-7"}
        original(self, *args, **kwargs)

    patcher.setattr(fixtures.NativeReviewAdoptionFixture, "__init__", constructor)
    try:
        f = PublicationFixture(tmp_path_factory.mktemp("cas-native"), patcher, None)
        patch_producer(f.producer)
        canonical = f.root / pub.CANONICAL
        _, fields, rows = pub.read_sssom(canonical)
        rows[0]["other"] += "|CAS:138-86-7"
        canonical.write_bytes(pub._render_candidate(canonical.read_bytes(), fields, rows))
        f.cas_before = canonical.read_bytes()
        f.cas_request = cas_request(f, rows[0], f.root / "data/ingredients/mapped/Exact.yaml")
        f.generation_dir = f.root / ".temp/cas-generation"
        f.generated = pub.generate(
            f.root,
            f.producer,
            f.kg,
            f.adoption.stage,
            f.adoption.receipt / "application.json",
            f.generation_dir,
            cas_dispositions=f.cas_request,
            cas_dispositions_sha256=digest(f.cas_request),
        )
        f.generation_receipt = f.generation_dir / "receipt.json"
        yield f
    finally:
        patcher.undo()


def test_native_cas_generation_replay_and_forced_unassessed_hold(cas_native):
    f = cas_native
    view = f.request(assessed=False).selection
    held = [r for r in view["rows"] if "mandatory_disposition" in r]
    assert len(held) == 1 and held[0]["mandatory_disposition"] == "INSTALL_WITHHOLD"
    assert held[0]["disposition"] is None
    assert (
        held[0]["cas_disposition"]["historical_row"]
        == pub.read_sssom(Path("old"), content=f.cas_before)[2][0]
    )
    assert "CAS:138-86-7" in held[0]["candidate_row"]["other"]
    assert (f.root / pub.CANONICAL).read_bytes() == f.cas_before


@pytest.mark.parametrize("attack", ["promote", "strip", "change_history"])
def test_native_rewritten_paired_votes_cannot_clear_mandatory_hold(cas_native, attack):
    def mutate(selection):
        item = next(row for row in selection["rows"] if "mandatory_disposition" in row)
        if attack == "promote":
            item["disposition"] = "INSTALL_SUPPORTED"
        elif attack == "strip":
            del item["mandatory_disposition"]
            del item["cas_disposition"]
        else:
            item["cas_disposition"]["historical_row"]["comment"] = "Erased original history"

    # The fixture really authors new native pairs over the altered selection.
    request = cas_native.request(alter=mutate)
    with pytest.raises(ValueError, match="INSTALL_WITHHOLD|derived selection"):
        pub.prepare(cas_native.root, request.path, cas_native.root / (".temp/attack-" + attack))
    assert (cas_native.root / pub.CANONICAL).read_bytes() == cas_native.cas_before


@pytest.mark.parametrize("name", ["cas-claims.json", "cas-request.json", "primary.txt"])
def test_native_replay_refuses_changed_cas_input(cas_native, name):
    f = cas_native
    request = f.request(assessed=False)
    path = f.root / name
    with restore([path]):
        path.write_bytes(path.read_bytes() + b" ")
        with pytest.raises(ValueError, match="changed|digest|hash|replay"):
            pub.inspect(f.root, request.path)
    assert (f.root / pub.CANONICAL).read_bytes() == f.cas_before


def test_retirement_requires_actual_source_endpoint_and_reviewed_rejection():
    entry = {
        "action": "RETIRE_INVALID_CAS",
        "row": {"object_id": "cas:138-86-7"},
        "owner": {
            "mim_id": "MIM:0000001",
            "path": "data/ingredients/mapped/a.yaml",
            "sha256": "a" * 64,
        },
    }
    endpoint_ref = {"path": "endpoint.json", "sha256": "b" * 64}
    manifest = {
        "cas_dispositions": {"content": {"source_correction": endpoint_ref, "entries": [entry]}}
    }
    with pytest.raises(ValueError, match="genuinely selected"):
        pub._cas_source_correction(manifest, None, endpoint_ref)
    operation = {
        "mim_id": "MIM:0000001",
        "after_path": entry["owner"]["path"],
        "proposal": {"sha256": "a" * 64},
        "rejected_identifiers": [],
    }
    endpoint = SimpleNamespace(loaded=SimpleNamespace(request={"operations": [operation]}))
    with pytest.raises(ValueError, match="reviewed corrective"):
        pub._cas_source_correction(manifest, endpoint, endpoint_ref)
    operation["rejected_identifiers"] = ["cas:138-86-7"]
    pub._cas_source_correction(manifest, endpoint, endpoint_ref)


@pytest.mark.parametrize("field", ["object_id", "other", "xref"])
def test_positive_cas_gate_stays_strict(field):
    with pytest.raises(ValueError, match="Invalid CAS check digit"):
        reviewed._safe_identifiers({field: "CAS:89471-28-0"})


def ordinary_request(f):
    """Bind actual installed native provenance and all historical CAS review inputs."""
    root = f.root
    manifest = json.loads((root / pub.DIAGNOSTIC_MANIFEST).read_bytes())
    proof = manifest["cas_dispositions"]
    request, claims = proof["request"], proof["content"]
    refs = [
        request["claims"],
        *request["reviews"],
        ref(root, f.cas_request),
        ref(root, f.generation_receipt),
        f.generated["outputs"]["manifest"],
    ]
    inputs = {r["path"]: r["sha256"] for r in refs}
    inputs.update(claims["evidence_inputs"])
    inputs.update(request["review_inputs"])
    inputs.pop(pub.CANONICAL, None)
    historical = root / "cas-canonical-before.tsv"
    historical.write_bytes(f.cas_before)
    inputs[historical.name] = digest(historical)
    for name in (pub.PROVENANCE, pub.DIAGNOSTIC_MANIFEST):
        inputs[name] = digest(root / name)
    rows = reviewed.read_sssom(root / pub.CANONICAL)[2]
    owners = {
        api.load_yaml(p.read_bytes())["mim_id"]: p for p in root.glob("data/ingredients/*/*.yaml")
    }
    decisions, entries, records = [], {}, {}
    for i, row in enumerate(rows, 1):
        owner = owners[row["subject_id"]]
        name = str(owner.relative_to(root))
        records[name] = digest(owner)
        decision = {
            "source_position": i,
            "row_sha256": reviewed.row_sha256(row),
            "owner_record": name,
            "disposition": "WITHHOLD",
            "review_reason": "Synthetic unresolved historical invalid CAS.",
            "review_evidence": "ordinary-cas-evidence.json",
            "evidence_key": str(i),
        }
        decisions.append(decision)
        entries[str(i)] = {k: decision[k] for k in ("row_sha256", "disposition", "review_reason")}
        entries[str(i)]["owner_record_sha256"] = records[name]
    evidence = root / "ordinary-cas-evidence.json"
    write(evidence, {"entries": entries})
    inputs[evidence.name] = digest(evidence)
    review = {
        "schema_version": 1,
        "source_sssom": pub.CANONICAL,
        "source_sha256": digest(root / pub.CANONICAL),
        "inputs": inputs,
        "record_inputs": records,
        "decisions": decisions,
    }
    path = root / "ordinary-cas-review.json"
    write(path, review)
    return path


def test_actual_publication_withheld_export_and_immutable_history(cas_native):
    """Install only after native paired/technical reviews; ordinary export stays held."""
    f = cas_native
    request, stage, _ = f.prepare()
    acceptance = f.accept(request, stage)
    destination = f.destination(request, "cas-application")
    result = pub.apply(f.root, stage, acceptance, destination, enabled=True)
    assert result["state"] == "COMPLETE" and result["scientific_approval_added"] is False
    assert (
        pub.verify_completed(f.root, stage, destination / "application.json")["status"]
        == "COMPLETE_CURRENT_CANONICAL_CANDIDATE"
    )
    review_path = ordinary_request(f)
    loaded = reviewed.load_review(f.root, review_path)
    assert len(loaded["cas_dispositions"]["held_rows"]) == 1
    output = f.root / "ordinary-cas-output"
    manifest = reviewed.export_reviewed(f.root, review_path, output)
    assert manifest["counts"] == {"source": 1, "supported": 0, "withhold": 1}
    assert reviewed.validate_reviewed(f.root, review_path, output) == manifest
    held = reviewed.read_sssom(output / "withheld_mappings.sssom.tsv")[2]
    assert "CAS:138-86-7" in held[0]["other"]
    # A coherent rewritten ordinary vote still reaches the unchanged positive CAS gate.
    evidence_path = f.root / "ordinary-cas-evidence.json"
    with restore([review_path, evidence_path]):
        review = json.loads(review_path.read_bytes())
        evidence = json.loads(evidence_path.read_bytes())
        review["decisions"][0]["disposition"] = "SUPPORTED"
        evidence["entries"]["1"]["disposition"] = "SUPPORTED"
        write(evidence_path, evidence)
        review["inputs"][evidence_path.name] = digest(evidence_path)
        write(review_path, review)
        with pytest.raises(ValueError, match="Invalid CAS check digit"):
            reviewed.load_review(f.root, review_path)
    # A caller cannot erase history while retaining a purported current native manifest.
    for name in (
        pub.PROVENANCE,
        pub.DIAGNOSTIC_MANIFEST,
        "cas-canonical-before.tsv",
        "cas-claims.json",
    ):
        with restore([review_path]):
            review = json.loads(review_path.read_bytes())
            del review["inputs"][name]
            write(review_path, review)
            with pytest.raises(ValueError, match="CAS"):
                reviewed.load_review(f.root, review_path)
    # Strip both independent visible markers and edit row/history coherently;
    # current native publication/original generation still prevents legacy fallback.
    canonical = f.root / pub.CANONICAL
    native_manifest = f.root / pub.DIAGNOSTIC_MANIFEST
    with restore([canonical, native_manifest, review_path, evidence_path]):
        metadata, fields, rows = reviewed.read_sssom(canonical)
        del metadata["cas_disposition_capability"]
        del metadata["cas_disposition_request"]
        rows[0]["other"] = ""  # Attempt to hide the bad historical annotation.
        rows[0]["comment"] = "Erased negative history"
        import yaml

        header = "".join("# " + line + "\n" for line in yaml.safe_dump(metadata).splitlines())
        canonical.write_bytes(header.encode() + reviewed._tsv(fields, rows))
        native_manifest.unlink()
        review = json.loads(review_path.read_bytes())
        review["inputs"].pop(pub.DIAGNOSTIC_MANIFEST)
        review["source_sha256"] = digest(canonical)
        review["decisions"][0]["row_sha256"] = reviewed.row_sha256(rows[0])
        evidence = json.loads(evidence_path.read_bytes())
        evidence["entries"]["1"]["row_sha256"] = reviewed.row_sha256(rows[0])
        write(evidence_path, evidence)
        review["inputs"][evidence_path.name] = digest(evidence_path)
        write(review_path, review)
        with pytest.raises(ValueError, match="CAS disposition capability/provenance"):
            reviewed.load_review(f.root, review_path)
    # Terminal ordinary-product validation rechecks immutable review bytes too.
    with restore([f.cas_request]):
        f.cas_request.write_bytes(f.cas_request.read_bytes() + b" ")
        with pytest.raises(ValueError, match="changed|Stale"):
            reviewed.validate_reviewed(f.root, review_path, output)
