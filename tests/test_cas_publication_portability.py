"""#1411: preserve original native CAS acquisitions across physical relocation."""

import copy
import json
import shutil
from pathlib import Path

import pytest

from mediaingredientmech.export import reviewed_sssom as reviewed
from mediaingredientmech.validation import semantic_transition as transition
from tests.test_cas_disposition_publication import cas_native, ordinary_request  # noqa: F401
from tests.test_stable_id_adoption import commit, initialize, write
from tests.test_stable_sssom_publication import digest, pub, ref, restore


@pytest.fixture(scope="module")
def relocated(cas_native, tmp_path_factory):  # noqa: F811
    f = cas_native
    request, stage, _ = f.prepare()
    acceptance = f.accept(request, stage)
    destination = f.destination(request, "portable-cas-application")
    application = pub.apply(f.root, stage, acceptance, destination, enabled=True)
    assert application["state"] == "COMPLETE"
    transition.capture(f.root, stage, destination / "application.json", "capsule")
    ordinary = ordinary_request(f)
    review = json.loads(ordinary.read_bytes())
    packet = json.loads((f.root / "capsule/transition.json").read_bytes())
    review["cas_disposition_transition"] = ref(f.root, f.root / "capsule/transition.json")
    review["inputs"]["capsule/transition.json"] = digest(f.root / "capsule/transition.json")
    for item in packet["files"]:
        review["inputs"][item["member"]] = item["sha256"]
    for name in application["outputs"]:
        review["inputs"][name] = digest(f.root / name)
    write(ordinary, review)
    target = tmp_path_factory.mktemp("relocated-cas") / "consumer"
    shutil.copytree(f.root, target)
    # The consumer cannot accidentally rely on the old original filesystem path.
    f.root.rename(f.root.with_name(f.root.name + "-unavailable"))
    return target, target / ordinary.name


def test_actual_native_relocation_exports_withheld_history_without_restamping(relocated):
    root, review = relocated
    source = root / pub.CANONICAL
    original = {name: (root / name).read_bytes() for name in pub.OUTPUTS}
    loaded = reviewed.load_review(root, review)
    proof = loaded["cas_dispositions"]
    assert proof["path"] != str(root / proof["relative_path"])
    assert not Path(proof["path"]).exists()
    assert len(proof["held_rows"]) == 1
    result = reviewed.export_reviewed(root, review, root / "portable-output")
    assert result["counts"] == {"source": 1, "supported": 0, "withhold": 1}
    assert reviewed.validate_reviewed(root, review, root / "portable-output") == result
    assert (
        reviewed.read_sssom(root / "portable-output/withheld_mappings.sssom.tsv")[2]
        == reviewed.read_sssom(source)[2]
    )
    assert {name: (root / name).read_bytes() for name in pub.OUTPUTS} == original


@pytest.mark.parametrize("missing", ["selector", "packet", "member", "current_output"])
def test_relocation_requires_explicit_complete_acquisition_inputs(relocated, missing):
    root, review_path = relocated
    with restore([review_path]):
        review = json.loads(review_path.read_bytes())
        packet = json.loads((root / review["cas_disposition_transition"]["path"]).read_bytes())
        if missing == "selector":
            del review["cas_disposition_transition"]
        elif missing == "packet":
            del review["inputs"][review["cas_disposition_transition"]["path"]]
        elif missing == "member":
            del review["inputs"][packet["files"][0]["member"]]
        else:
            del review["inputs"]["mappings/suppressed_aliases.tsv"]
        write(review_path, review)
        with pytest.raises(ValueError, match="CAS relocation"):
            reviewed.load_review(root, review_path)


@pytest.mark.parametrize(
    "attack", ["root", "request_path", "request_hash", "duplicate", "wrong_member", "selector_hash"]
)
def test_rehashed_capsule_cannot_substitute_acquisition_identity(relocated, attack):
    root, review_path = relocated
    packet_path = root / "capsule/transition.json"
    with restore([review_path, packet_path]):
        review = json.loads(review_path.read_bytes())
        packet = json.loads(packet_path.read_bytes())
        original = packet["publication"]["root"]
        manifest = json.loads((root / pub.DIAGNOSTIC_MANIFEST).read_bytes())
        wanted = manifest["cas_dispositions"]
        item = next(
            i
            for i in packet["files"]
            if i["root"] == original
            and i["path"] == wanted["relative_path"]
            and i["sha256"] == wanted["sha256"]
        )
        if attack == "root":
            packet["publication"]["root"] = original + "-wrong"
        elif attack == "request_path":
            item["path"] = "wrong-cas-request.json"
        elif attack == "request_hash":
            item["sha256"] = "0" * 64
        elif attack == "duplicate":
            packet["files"].append(copy.deepcopy(item))
        elif attack == "wrong_member":
            item["member"] = packet["files"][0]["member"]
        write(packet_path, packet)
        pin = digest(packet_path)
        review["inputs"]["capsule/transition.json"] = pin
        review["cas_disposition_transition"]["sha256"] = (
            "0" * 64 if attack == "selector_hash" else pin
        )
        write(review_path, review)
        with pytest.raises(ValueError, match="CAS relocation|Semantic transition"):
            reviewed.load_review(root, review_path)


@pytest.mark.parametrize("attack", ["incomplete", "recovery", "output", "request_chain"])
def test_rehashed_application_still_needs_complete_native_chain(relocated, attack):
    root, review_path = relocated
    packet_path = root / "capsule/transition.json"
    packet = json.loads(packet_path.read_bytes())
    selected = packet["publication"]
    ref_kind = "manifest" if attack == "request_chain" else "receipt"
    item = next(
        i
        for i in packet["files"]
        if i["root"] == selected["root"]
        and i["path"] == selected[ref_kind]["path"]
        and i["sha256"] == selected[ref_kind]["sha256"]
    )
    member = root / item["member"]
    with restore([review_path, packet_path, member]):
        review = json.loads(review_path.read_bytes())
        value = json.loads(member.read_bytes())
        if attack == "incomplete":
            value["state"] = "FAILED"
        elif attack == "recovery":
            value["recovery_required"] = True
        elif attack == "output":
            value["outputs"][pub.CANONICAL] = "0" * 64
        else:
            value["request"]["sha256"] = "0" * 64
        write(member, value)
        item["sha256"] = selected[ref_kind]["sha256"] = digest(member)
        review["inputs"][item["member"]] = digest(member)
        write(packet_path, packet)
        review["inputs"]["capsule/transition.json"] = digest(packet_path)
        review["cas_disposition_transition"]["sha256"] = digest(packet_path)
        write(review_path, review)
        with pytest.raises(ValueError, match="CAS relocation"):
            reviewed.load_review(root, review_path)


def test_relocated_invalid_cas_cannot_be_supported(relocated):
    root, review_path = relocated
    evidence_path = root / "ordinary-cas-evidence.json"
    with restore([review_path, evidence_path]):
        review = json.loads(review_path.read_bytes())
        evidence = json.loads(evidence_path.read_bytes())
        review["decisions"][0]["disposition"] = "SUPPORTED"
        evidence["entries"]["1"]["disposition"] = "SUPPORTED"
        write(evidence_path, evidence)
        review["inputs"][evidence_path.name] = digest(evidence_path)
        write(review_path, review)
        with pytest.raises(ValueError, match="Invalid CAS check digit"):
            reviewed.load_review(root, review_path)


@pytest.mark.parametrize(
    "attack", ["restamp", "missing_root", "nonstring_root", "relative_root", "dot_root"]
)
def test_declared_origin_cannot_be_restamped_into_same_root_route(relocated, attack):
    root, review_path = relocated
    publication_path = root / pub.PROVENANCE
    publication = json.loads(publication_path.read_bytes())
    generation_path = root / publication["generation"]["path"]
    generation = json.loads(generation_path.read_bytes())
    generated_manifest = root / generation["outputs"]["manifest"]["path"]
    current_manifest = root / pub.DIAGNOSTIC_MANIFEST
    with restore(
        [review_path, publication_path, generation_path, generated_manifest, current_manifest]
    ):
        manifest = json.loads(generated_manifest.read_bytes())
        # Rehash the complete current chain, removing the explicit selector. A
        # forged physical proof path must not select the old same-root route.
        manifest["cas_dispositions"]["path"] = str(
            root / manifest["cas_dispositions"]["relative_path"]
        )
        if attack == "missing_root":
            del generation["root"]
        elif attack == "nonstring_root":
            generation["root"] = 123
        elif attack == "relative_root":
            generation["root"] = "relative/origin"
        elif attack == "dot_root":
            generation["root"] += "/../origin"
        write(generated_manifest, manifest)
        write(current_manifest, manifest)
        generation["outputs"]["manifest"]["sha256"] = digest(generated_manifest)
        write(generation_path, generation)
        publication["generation"]["sha256"] = digest(generation_path)
        write(publication_path, publication)
        review = json.loads(review_path.read_bytes())
        del review["cas_disposition_transition"]
        for path in (publication_path, generation_path, generated_manifest, current_manifest):
            review["inputs"][str(path.relative_to(root))] = digest(path)
        write(review_path, review)
        with pytest.raises(ValueError, match="original request/root binding"):
            reviewed.load_review(root, review_path)


@pytest.mark.parametrize("kind", ["source", "retained_companion"])
def test_real_captured_consumers_use_only_captured_acquisition_code(
    relocated, kind, monkeypatch, tmp_path
):
    from mediaingredientmech import native_acquisition
    from mediaingredientmech.export import companion_producer, source_bindings, source_producer

    def forbidden_public(*args, **kwargs):
        raise AssertionError("Ambient public acquisition implementation was reused")

    monkeypatch.setattr(native_acquisition, "Evidence", forbidden_public)
    maintained = Path(__file__).resolve().parents[1]
    code_root = tmp_path / "declared-producer-package"
    initialize(code_root)
    # Package exactly the public contract: an undeclared dependency cannot be
    # supplied accidentally by the author's complete checkout (#1411).
    names = (
        (
            source_bindings.HELPER,
            source_bindings.SCHEMA,
            *source_bindings.PRODUCER_PATHS,
            *source_bindings.PRODUCER_AUXILIARY,
        )
        if kind == "source"
        else companion_producer.PATHS
    )
    for name in names:
        destination = code_root / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(maintained / name, destination)
    commit(code_root)
    if kind == "source":
        capture, _ = source_producer.captured_native_modules(
            code_root, (code_root / source_producer.LOADER).read_bytes()
        )
    else:
        capture = companion_producer.load(
            code_root, (code_root / companion_producer.LOADER).read_bytes()
        )
    assert "src/mediaingredientmech/native_acquisition.py" in capture.files
    exporter = capture.load("mediaingredientmech.export.reviewed_sssom")
    assert exporter is not reviewed
    root, review_path = relocated
    loaded = exporter.load_review(root, review_path)
    assert len(loaded["cas_dispositions"]["held_rows"]) == 1
    output = root / (kind + "-captured-output")
    manifest = exporter.export_reviewed(root, review_path, output)
    assert manifest["counts"] == {"source": 1, "supported": 0, "withhold": 1}
    assert exporter.validate_reviewed(root, review_path, output) == manifest
    assert capture.load("mediaingredientmech.native_acquisition").Evidence is not forbidden_public
    capture.verify()


@pytest.mark.parametrize("missing", [False, True])
def test_current_semantic_inputs_bind_executing_acquisition_code(tmp_path, monkeypatch, missing):
    """Exercise the real implementation-capture boundary, not a full release vote."""
    from mediaingredientmech.validation import current_semantic_release as current

    root = tmp_path / "current-semantic-inputs"
    initialize(root)
    maintained = Path(__file__).resolve().parents[1]
    # Supply the maintained package, without deriving membership from the
    # implementation set under test. Native publication capture is also exact.
    for source in (maintained / "src/mediaingredientmech").rglob("*.py"):
        destination = root / source.relative_to(maintained)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    for name, (raw, _) in current.publication._CAPTURE.files.items():
        destination = root / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(raw)
    request = dict.fromkeys(current.REQUEST_KEYS, {})
    request.update(schema_version=1, capability=current.CAPABILITY, historical_root=str(root))
    write(root / "request.json", request)
    commit(root)
    dependency = root / "src/mediaingredientmech/native_acquisition.py"
    observed = []
    native_inputs = current.Inputs

    def observe_inputs(path):
        result = native_inputs(path)
        observed.append(result)
        return result

    monkeypatch.setattr(current, "Inputs", observe_inputs)
    if missing:
        dependency.unlink()
        with pytest.raises(FileNotFoundError, match="native_acquisition.py"):
            current.evaluate(root, "request.json")
    else:
        # Deliberately stop at the next real boundary after code capture. This
        # does not stub or waive historical reconstruction, or claim a release.
        with pytest.raises(ValueError, match="historical/current roots must be disjoint"):
            current.evaluate(root, "request.json")
        name = "src/mediaingredientmech/native_acquisition.py"
        assert observed[0].hashes()[name] == digest(dependency)
        observed[0].recheck()
        dependency.write_bytes(dependency.read_bytes() + b"\n# changed after capture\n")
        with pytest.raises(ValueError, match="late input drift: " + name):
            observed[0].recheck()
