"""#1387 semantic reconstruction from a real native publication in a new root."""

import copy
import json
import shutil
import subprocess
from pathlib import Path
from types import SimpleNamespace

import pytest
import yaml

from mediaingredientmech.curate import stable_sssom_publication as pub
from mediaingredientmech.validation import semantic_transition as transition
from mediaingredientmech.validation.current_semantic_release import Inputs
from tests.test_stable_sssom_publication import PublicationFixture, api


@pytest.fixture(scope="module")
def produced(tmp_path_factory):
    directory = tmp_path_factory.mktemp("native-semantic-publication")
    original = directory / "original"
    with pytest.MonkeyPatch.context() as patch:
        fixture = PublicationFixture(original, patch, None)
        request, stage, _ = fixture.prepare()
        acceptance = fixture.accept(request, stage)
        receipt = fixture.destination(request, "applied")
        pub.apply(fixture.root, stage, acceptance, receipt, enabled=True)
        reference = transition.capture(
            fixture.root, stage, receipt / "application.json", "semantic-evidence"
        )
    packet = json.loads((fixture.root / reference["path"]).read_bytes())
    source = packet["sources"][0]
    source_receipt = json.loads((Path(source["root"]) / source["receipt"]["path"]).read_bytes())
    baseline = {
        name: (Path(source["root"]) / ref["path"]).read_bytes()
        for name, ref in source_receipt["beforeimages"].items()
    }
    publication_receipt = json.loads((receipt / "application.json").read_bytes())
    canonical_ref = publication_receipt["beforeimages"][pub.CANONICAL]
    baseline[pub.CANONICAL] = (fixture.root / canonical_ref["path"]).read_bytes()
    copied = directory / "portable"
    shutil.copytree(fixture.root, copied)
    # All original fixture, producer and history paths become unavailable.
    original.rename(directory / "original-unavailable")
    return copied, reference, baseline


@pytest.fixture
def case(produced, tmp_path):
    source, reference, baseline = produced
    root = tmp_path / "current"
    shutil.copytree(source, root)
    return root, copy.deepcopy(reference), copy.deepcopy(baseline)


def run(case):
    root, reference, baseline = case
    owners = {
        str(path.relative_to(root)): path.read_bytes()
        for path in root.glob("data/ingredients/*/*.yaml")
    }
    ledgers = {name: (root / name).read_bytes() for name in transition.LEDGERS}
    return transition.verify(
        Inputs(root), reference, {"proof": SimpleNamespace(after=baseline)}, owners, ledgers
    )


def test_real_native_publication_reconstructs_after_original_roots_disappear(case):
    result = run(case)
    assert result["scope"] == "semantic_reconstruction_not_transaction_reexecution"
    assert result["provenance"]["ordinary_release_review_required"] is True
    assert result["provenance"]["scientific_approval_added"] is False
    assert all(
        row["disposition"] == "INSTALL_WITHHOLD"
        for row in result["provenance"]["selection"]["rows"]
        if row["candidate_position"]
    )
    assert result["source"]["scientific_approval_added"] is False


def test_current_installed_full_row_cannot_drift(case):
    root, _, _ = case
    path = root / pub.CANONICAL
    path.write_bytes(
        path.read_bytes().replace(
            b"Synthetic original provenance comment", b"Dropped original provenance comment"
        )
    )
    with pytest.raises(ValueError, match="staged/installed canonical output differs"):
        run(case)


def test_historical_stable_endpoint_is_an_exact_byte_link(case):
    case[2][pub.CANONICAL] += b"\n"
    with pytest.raises(ValueError, match="exact historical stable endpoint"):
        run(case)


def test_packet_cannot_omit_a_native_beforeimage_even_when_rehashed(case):
    root, reference, _ = case
    path = root / reference["path"]
    packet = json.loads(path.read_bytes())
    selected = packet["publication"]
    item = next(
        x
        for x in packet["files"]
        if x["root"] == selected["root"] and x["path"] == selected["receipt"]["path"]
    )
    receipt = json.loads((root / item["member"]).read_bytes())
    before = receipt["beforeimages"][pub.CANONICAL]
    packet["files"] = [
        x
        for x in packet["files"]
        if not (
            x["root"] == selected["root"]
            and x["path"] == before["path"]
            and x["sha256"] == before["sha256"]
        )
    ]
    path.write_bytes(api.encoded(packet))
    reference["sha256"] = api.sha(path.read_bytes())
    with pytest.raises(ValueError, match="missing qualified native evidence"):
        run(case)


def test_ambiguous_duplicate_acquisition_cannot_be_hidden_in_a_rehash(case):
    root, reference, _ = case
    path = root / reference["path"]
    packet = json.loads(path.read_bytes())
    packet["files"].append(copy.deepcopy(packet["files"][0]))
    path.write_bytes(api.encoded(packet))
    reference["sha256"] = api.sha(path.read_bytes())
    with pytest.raises(ValueError, match="duplicate acquisition or member"):
        run(case)


def installation_pair(case, attack=None):
    """Use native-valid YAML/Markdown pairs; mutate actual scientific bindings."""
    root, reference, _ = case
    evidence = transition.Evidence(Inputs(root), reference)
    chosen = evidence.packet["publication"]
    original_root = chosen["root"]
    request = evidence.document(original_root, chosen["request"])
    selection = evidence.document(original_root, request["selection"])
    refs = copy.deepcopy(request["reviews"])
    review_inputs = copy.deepcopy(request["review_inputs"])
    parser = pub._CAPTURE.script("scripts/record_review.py")
    reports = [yaml.safe_load(evidence.read(original_root, ref)) for ref in refs]
    required = {entry["path"]: entry["sha256"] for entry in reports[0]["source"]["inputs"]}
    overlays = {}
    if attack:
        selected = 1 if attack == "duplicate_identity" else 0
        report = reports[selected]
        target = report["targets"][0]
        if attack == "wrong_path":
            target["path"] = "primary.txt"
        elif attack == "wrong_kind":
            target["kind"] = "generated"
        elif attack == "wrong_algorithm":
            target["semantic_digest"]["algorithm"] = "sha256"
        elif attack == "wrong_description":
            target["semantic_digest"]["description"] = "An unrelated object"
        elif attack == "missing_owner":
            report["source"]["inputs"] = [
                entry
                for entry in report["source"]["inputs"]
                if not entry["path"].startswith("data/ingredients/")
            ]
        elif attack == "missing_generation":
            report["source"]["inputs"] = [
                entry
                for entry in report["source"]["inputs"]
                if entry["path"] != request["generation"]["path"]
            ]
        elif attack == "wrong_evidence":
            for item in report["evidence"]:
                item["snapshot_sha256"] = "0" * 64
        elif attack == "duplicate_identity":
            report["reviewer"]["identity"] = reports[0]["reviewer"]["identity"]
        elif attack == "missing_git_revision":
            report["source"]["git_revision"] = "0" * 40
        elif attack == "false_committed_inputs":
            report["source"]["state"] = "git_commit"
        else:
            raise AssertionError(attack)
        # Native renderer validates schema and the full report/Markdown pair.
        markdown = parser.render_markdown(report, root / "schema/record_review.yaml").encode()
        raw = yaml.safe_dump(report, sort_keys=False).encode()
        ref = refs[selected]
        ref["sha256"] = api.sha(raw)
        md = str(Path(ref["path"]).with_name("review.md"))
        review_inputs[md] = api.sha(markdown)
        overlays[(original_root, ref["path"], ref["sha256"])] = raw
        overlays[(original_root, md, api.sha(markdown))] = markdown

    class Overlay:
        inputs = evidence.inputs

        def read(self, original, ref):
            key = (original, ref["path"], ref["sha256"])
            return overlays[key] if key in overlays else evidence.read(original, ref)

    return Overlay(), original_root, refs, review_inputs, selection, request["selection"], required


def test_1391_native_report_inputs_need_not_duplicate_request_extras(case):
    args = installation_pair(case)
    assert not set(args[-1]) <= set(args[3])
    transition._reports(*args)


@pytest.mark.parametrize(
    "attack,reason",
    [
        ("wrong_path", "row/history coverage incomplete"),
        ("wrong_kind", "installation payload changed"),
        ("wrong_algorithm", "installation payload changed"),
        ("wrong_description", "installation payload changed"),
        ("missing_owner", "required input inventory differs"),
        ("missing_generation", "required input inventory differs"),
        ("wrong_evidence", "captured evidence omitted"),
        ("duplicate_identity", "independent installation pair omitted"),
        ("missing_git_revision", "Git provenance invalid"),
        ("false_committed_inputs", "Git provenance invalid"),
    ],
)
def test_1391_rehashed_native_pair_cannot_change_its_binding(case, attack, reason):
    args = installation_pair(case, attack)
    with pytest.raises(ValueError, match=reason):
        transition._reports(*args)


@pytest.mark.parametrize(
    "origin",
    [
        "https://github.com/CultureBotAI/MediaIngredientMech",
        "git@github.com:CultureBotAI/MediaIngredientMech",
        "git@github.com:CultureBotAI/MediaIngredientMech.git",
    ],
)
def test_1392_native_equivalent_origin_spelling_preserves_exact_git_proof(case, origin):
    subprocess.run(["git", "remote", "set-url", "origin", origin], cwd=case[0], check=True)
    assert run(case)["source"]["scientific_approval_added"] is False


def test_1392_equivalent_spelling_does_not_authorize_a_different_repository(case):
    subprocess.run(
        ["git", "remote", "set-url", "origin", "https://github.com/CultureBotAI/OtherRepository"],
        cwd=case[0],
        check=True,
    )
    with pytest.raises(ValueError, match="review Git authority is not MIM"):
        run(case)


def test_1392_actual_corrective_pair_and_history_survive_native_publication_relocation(tmp_path):
    """Exercise capture plus semantic reconstruction of the genuine two-step route."""
    from tests.test_curation_successor_publication import corrected, publication

    original = tmp_path / "original"
    original.mkdir()
    with pytest.MonkeyPatch.context() as patch:
        fixture, endpoint = corrected(original, patch)
        publisher = publication(fixture, endpoint, original)
        request, stage, _ = publisher.prepare()
        acceptance = publisher.accept(request, stage)
        receipt = publisher.destination(request, "semantic-applied")
        pub.apply(publisher.root, stage, acceptance, receipt, enabled=True)
        reference = transition.capture(
            publisher.root, stage, receipt / "application.json", "semantic-evidence"
        )
    evidence = transition.Evidence(Inputs(publisher.root), reference)
    first = evidence.packet["sources"][0]
    adoption_receipt = evidence.document(first["root"], first["receipt"])
    baseline = {
        name: evidence.read(first["root"], ref)
        for name, ref in adoption_receipt["beforeimages"].items()
    }
    application = json.loads((receipt / "application.json").read_bytes())
    baseline[pub.CANONICAL] = evidence.read(
        str(publisher.root), application["beforeimages"][pub.CANONICAL]
    )
    copied = tmp_path / "portable"
    shutil.copytree(publisher.root, copied)
    original.rename(tmp_path / "original-unavailable")
    result = run((copied, reference, baseline))
    assert len(result["source"]["operations"]) == 1
    retained = result["source"]["retained_contexts"][-1]["original_native_reviews"]
    assert retained["references"][0]["primary"]
    assert retained["references"][0]["skeptic"]
    assert len(retained["context"]["historical_obligations"]) == 2
    assert result["provenance"]["scientific_approval_added"] is False
