"""#1395 CAS proof binds actual native generation policy and original decisions."""

import copy
import json
from pathlib import Path
from types import SimpleNamespace

import pytest
import yaml

from mediaingredientmech.validation import semantic_transition as transition
from tests.test_cas_disposition_publication import cas_native  # noqa: F401
from tests.test_stable_sssom_publication import api, pub


@pytest.fixture(scope="module")
def cas_evidence(cas_native):  # noqa: F811
    f = cas_native
    generation = json.loads(f.generation_receipt.read_bytes())
    manifest = json.loads((f.root / generation["outputs"]["manifest"]["path"]).read_bytes())
    # Capture once. All checks below use exact bytes even if original files move.
    captured = {}
    for item in manifest["source_inputs"]:
        if item["sha256"] is not None:
            raw = Path(item["path"]).read_bytes()
            assert api.sha(raw) == item["sha256"]
            captured[(item["path"], item["sha256"])] = raw

    class Captured:
        inputs = SimpleNamespace(root=f.root)

        def read(self, root, ref):
            return captured[(str(Path(root) / ref["path"]), ref["sha256"])]

        def document(self, root, ref):
            return json.loads(self.read(root, ref))

    source = json.loads((f.adoption.receipt / "application.json").read_bytes())
    predecessor = {
        name: (f.root / ref["path"]).read_bytes()
        for name, ref in source["beforeimages"].items()
        if name.startswith("data/ingredients/")
    }
    owners = {
        str(path.relative_to(f.root)): path.read_bytes()
        for path in f.root.glob("data/ingredients/*/*.yaml")
    }
    candidate = pub.read_sssom(f.root / generation["outputs"]["sssom"]["path"])[2]
    return (
        Captured(),
        str(f.root),
        generation,
        manifest,
        f.cas_before,
        candidate,
        owners,
        {"operations": [], "predecessor_owners": predecessor},
    )


def test_adoption_only_retained_cas_keeps_native_no_correction_contract(cas_evidence):
    assert cas_evidence[2].get("curation_successor") is None
    assert cas_evidence[3]["cas_dispositions"]["content"]["source_correction"] is None
    transition._cas(*cas_evidence)


def test_rehashed_held_rows_cannot_erase_native_cas_obligation(cas_evidence):
    args = list(cas_evidence)
    args[3] = copy.deepcopy(args[3])
    args[3]["cas_dispositions"]["held_rows"] = []
    with pytest.raises(ValueError, match="mandatory held/retired accounting"):
        transition._cas(*args)


def test_unclaimed_invalid_cas_position_is_not_hidden_by_claims(cas_evidence):
    args = list(cas_evidence)
    _, fields, rows = pub.read_sssom(Path("before"), content=args[4])
    rows.append(copy.deepcopy(rows[0]))
    args[4] = pub._render_candidate(args[4], fields, rows)
    # The independent exact canonical pin must reject this before row accounting.
    with pytest.raises(ValueError, match="CAS historical canonical differs"):
        transition._cas(*args)


def test_rehashed_captured_code_cannot_certify_a_missing_cas_hold(cas_evidence):
    """Benign replacement finalizer demonstrates why executable pins need authority."""
    args = list(cas_evidence)
    args[2], args[3] = copy.deepcopy(args[2]), copy.deepcopy(args[3])
    captured = args[0]
    claw = args[2]["claw"]["root"]
    name = "src/kg_microbe_utils/stable_mim.py"
    absolute = str(Path(claw) / name)
    raw = captured.read(claw, {"path": name, "sha256": args[2]["claw"]["files"][absolute]})
    changed = (
        raw
        + b"\ndef finalize_cas_dispositions(proof, rows):\n    return dict(proof, held_rows=[], retired_entries=[])\n"
    )
    new_pin = api.sha(changed)
    args[2]["claw"]["files"][absolute] = new_pin
    args[3]["producer_import_snapshot"][absolute] = new_pin
    args[3]["cas_dispositions"]["held_rows"] = []

    class RehashedCode:
        def read(self, root, ref):
            if root == claw and ref == {"path": name, "sha256": new_pin}:
                return changed
            return captured.read(root, ref)

        def document(self, root, ref):
            return json.loads(self.read(root, ref))

    args[0] = RehashedCode()
    with pytest.raises(ValueError, match="CAS producer implementation"):
        transition._cas(*args)


@pytest.mark.parametrize(
    "attack,reason",
    [
        ("hold", "diagnostic action/hold scope"),
        ("same_identity", "distinct independent skeptical review"),
        ("missing_git", "native Git provenance invalid"),
        ("wrong_target", "native reviewed claim differs"),
        ("uncaptured_evidence", "captured per-entry evidence"),
    ],
)
def test_rehashed_original_cas_pair_cannot_clear_its_own_hold(cas_evidence, attack, reason):
    """Keep claim, owner and all original science bytes; change only pair intent."""
    args = list(cas_evidence)
    args[2], args[3] = copy.deepcopy(args[2]), copy.deepcopy(args[3])
    captured, root = args[:2]
    request = captured.document(root, args[2]["cas_dispositions"])
    report_ref = request["reviews"][0]
    report = yaml.safe_load(captured.read(root, report_ref))
    if attack == "hold":
        for dimension in report["assessments"][0]["dimensions"]:
            if dimension["name"] == "hold_disposition":
                dimension["value"] = "RELEASED"
    elif attack == "same_identity":
        other = yaml.safe_load(captured.read(root, request["reviews"][1]))
        report["reviewer"]["identity"] = other["reviewer"]["identity"]
    elif attack == "missing_git":
        report["source"]["git_revision"] = "0" * 40
    elif attack == "wrong_target":
        report["targets"][0]["semantic_digest"]["sha256"] = "0" * 64
    elif attack == "uncaptured_evidence":
        report["evidence"][0]["snapshot_sha256"] = "0" * 64
    else:
        raise AssertionError(attack)
    parser = pub._CAPTURE.script("scripts/record_review.py")
    markdown = parser.render_markdown(
        report, captured.inputs.root / "schema/record_review.yaml"
    ).encode()
    raw = yaml.safe_dump(report, sort_keys=False).encode()
    report_ref["sha256"] = api.sha(raw)
    md_path = str(Path(report_ref["path"]).with_name("review.md"))
    request["review_inputs"][md_path] = api.sha(markdown)
    request_raw = api.encoded(request)
    args[2]["cas_dispositions"]["sha256"] = api.sha(request_raw)
    args[3]["cas_dispositions"]["sha256"] = api.sha(request_raw)
    args[3]["cas_dispositions"]["request"] = request
    replacements = {
        (report_ref["path"], report_ref["sha256"]): raw,
        (md_path, api.sha(markdown)): markdown,
        (args[2]["cas_dispositions"]["path"], api.sha(request_raw)): request_raw,
    }

    class RehashedReview:
        inputs = captured.inputs

        def read(self, original, ref):
            key = (ref["path"], ref["sha256"])
            return (
                replacements[key]
                if original == root and key in replacements
                else captured.read(original, ref)
            )

        def document(self, original, ref):
            return json.loads(self.read(original, ref))

    args[0] = RehashedReview()
    with pytest.raises(ValueError, match=reason):
        transition._cas(*args)


def without_proof(cas_evidence, historical_token, candidate_token):
    args = list(cas_evidence)
    args[2], args[3], args[5] = (copy.deepcopy(args[index]) for index in (2, 3, 5))
    args[2]["cas_dispositions"] = None
    args[3]["cas_dispositions"] = None
    _, fields, rows = pub.read_sssom(Path("before"), content=args[4])
    for row in rows:
        row["other"] = row["other"].replace("CAS:138-86-7", historical_token)
    args[4] = pub._render_candidate(args[4], fields, rows)
    for row in args[5]:
        row["other"] = row["other"].replace("CAS:138-86-7", candidate_token)
    return args


@pytest.mark.parametrize("where", ["historical", "candidate"])
@pytest.mark.parametrize("invalid", ["CAS:138-86-7", "CAS:malformed"])
def test_1395_absence_cannot_erase_historical_or_current_cas_obligation(
    cas_evidence, where, invalid
):
    historical, candidate = (
        (invalid, "CAS:7732-18-5") if where == "historical" else ("CAS:7732-18-5", invalid)
    )
    with pytest.raises(ValueError, match="requires explicit disposition proof"):
        transition._cas(*without_proof(cas_evidence, historical, candidate))


@pytest.mark.parametrize("token", ["CAS:7732-18-5", "12-34-5", "unrelated numeric source 12345"])
def test_1395_valid_no_proof_and_native_non_cas_scope_remain_supported(cas_evidence, token):
    assert transition._cas(*without_proof(cas_evidence, token, token)) is None
