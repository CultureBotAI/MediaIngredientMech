"""Historical test restoration is scoped and never weakens writer validation."""

import base64
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
from types import SimpleNamespace

import pytest

from tests import historical_source_anchors as anchors

ROOT = anchors.ROOT
LABELS = "tests/test_curate_step7c_source_labels.py"
CORRECTION = "tests/test_correct_diketo_bacdive_evidence.py"


def request_for(module, root, *, case=None, repository=ROOT, names=("case",)):
    info = anchors.MODULES[module]
    before = {Path(name): (root / name).read_bytes() for name in info["anchors"]}
    if case is None:
        case = (
            (root, root / "evidence", root / "log", before)
            if module == LABELS
            else (root, root / "log")
        )
    values = {"case": case, "tmp_path": root}
    return SimpleNamespace(
        path=repository / module,
        fixturenames=names,
        getfixturevalue=values.__getitem__,
    )


@pytest.fixture
def anchor_case(tmp_path):
    for name in anchors.ANCHORS:
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"later publication bytes for " + name.encode())
    return tmp_path


def test_fixture_is_portable_and_matches_both_immutable_source_contracts():
    frozen = anchors.frozen_anchors()
    corrected = json.loads(
        (
            ROOT / "reports/diketo_bacdive_evidence_1111_20261102/source-evidence.json"
        ).read_bytes()
    )
    assert {name: anchors.digest(data) for name, data in frozen.items()} == corrected[
        "protected_anchors"
    ]
    labels = json.loads(
        (
            ROOT / "reports/step7c_source_labels_313_235_20261102/source-evidence.json"
        ).read_bytes()
    )
    for name in anchors.MODULES[LABELS]["anchors"]:
        assert anchors.digest(frozen[name]) == labels["before_sha256"][name]


@pytest.mark.parametrize("module", [LABELS, CORRECTION])
def test_only_declared_anchors_are_restored_and_before_assertions_remain_truthful(
    anchor_case, module
):
    sentinel = anchor_case / "owner.yaml"
    sentinel.write_bytes(b"original case owner")
    request = request_for(module, anchor_case)
    case = request.getfixturevalue("case")
    if module == LABELS:
        case[3][Path("owner.yaml")] = sentinel.read_bytes()
    assert anchors.restore_requested_case(request, repository_root=ROOT)
    frozen = anchors.frozen_anchors()
    for name in anchors.MODULES[module]["anchors"]:
        assert (anchor_case / name).read_bytes() == frozen[name]
    assert sentinel.read_bytes() == b"original case owner"
    if module == LABELS:
        assert all((anchor_case / path).read_bytes() == data for path, data in case[3].items())
        assert (
            (anchor_case / "UNIFIED_INGREDIENT_MAPPING.tsv")
            .read_bytes()
            .startswith(b"later publication")
        )


@pytest.mark.parametrize("kind", ["unrelated", "same_basename", "no_case"])
def test_unrelated_or_unrequested_fixtures_are_not_even_loaded(kind):
    def unexpected(name):
        pytest.fail(f"Unrelated fixture accessed: {name}")

    path = ROOT / LABELS
    if kind == "unrelated":
        path = ROOT / "tests/test_other.py"
    elif kind == "same_basename":
        path = ROOT / "tests/elsewhere" / Path(LABELS).name
    request = SimpleNamespace(
        path=path,
        fixturenames=() if kind == "no_case" else ("case",),
        getfixturevalue=unexpected,
    )
    assert anchors.restore_requested_case(request, repository_root=ROOT) is False


def test_wrong_archive_hash_refuses_before_constructing_case(tmp_path):
    archive = tmp_path / "wrong.gz"
    archive.write_bytes(anchors.ARCHIVE.read_bytes() + b"changed")
    request = SimpleNamespace(
        path=ROOT / LABELS,
        fixturenames=("case",),
        getfixturevalue=lambda _: pytest.fail("Case constructed before archive validation"),
    )
    with pytest.raises(ValueError, match="archive hash changed"):
        anchors.restore_requested_case(request, repository_root=ROOT, archive=archive)


@pytest.mark.parametrize("change", ["content", "members", "revision"])
def test_inner_contract_and_each_content_hash_are_checked(tmp_path, monkeypatch, change):
    doc = json.loads(gzip.decompress(anchors.ARCHIVE.read_bytes()))
    if change == "content":
        doc["anchors"][next(iter(doc["anchors"]))] = base64.b64encode(b"wrong").decode()
    elif change == "members":
        doc["anchors"]["../foreign"] = doc["anchors"].pop(next(iter(doc["anchors"])))
    else:
        doc["source_revision"] = "private checkpoint"
    raw = gzip.compress(json.dumps(doc).encode(), mtime=0)
    archive = tmp_path / "changed.gz"
    archive.write_bytes(raw)
    monkeypatch.setattr(anchors, "ARCHIVE_SHA256", hashlib.sha256(raw).hexdigest())
    with pytest.raises(ValueError, match="contract changed|content hash changed"):
        anchors.frozen_anchors(archive)


@pytest.mark.parametrize("kind", ["other_root", "root_alias", "malformed", "missing_before"])
def test_wrong_case_shape_or_root_is_rejected_before_replacement(anchor_case, tmp_path, kind):
    request = request_for(LABELS, anchor_case)
    original = request.getfixturevalue("case")
    bad = original
    if kind == "other_root":
        bad = (anchor_case.parent, *original[1:])
    elif kind == "root_alias":
        link = tmp_path / "root-alias"
        link.symlink_to(anchor_case, target_is_directory=True)
        bad = (link, *original[1:])
    elif kind == "malformed":
        bad = list(original)
    else:
        bad = (*original[:3], {})
    request.getfixturevalue = {"case": bad, "tmp_path": anchor_case}.__getitem__
    before = {name: (anchor_case / name).read_bytes() for name in anchors.ANCHORS}
    with pytest.raises(ValueError, match="shape|tmp_path|before dictionary"):
        anchors.restore_requested_case(request, repository_root=ROOT)
    assert before == {name: (anchor_case / name).read_bytes() for name in anchors.ANCHORS}


@pytest.mark.parametrize("kind", ["file_symlink", "parent_symlink", "hardlink"])
def test_aliased_anchor_refused_before_any_write(anchor_case, tmp_path, kind):
    request = request_for(CORRECTION, anchor_case)
    name = "mappings/suppressed_aliases.tsv"
    target = anchor_case / name
    foreign = tmp_path / "foreign"
    if kind == "parent_symlink":
        (anchor_case / "mappings").rename(foreign)
        (anchor_case / "mappings").symlink_to(foreign, target_is_directory=True)
        foreign_leaf = foreign / "suppressed_aliases.tsv"
    else:
        target.rename(foreign)
        foreign_leaf = foreign
        if kind == "file_symlink":
            target.symlink_to(foreign)
        else:
            os.link(foreign, target)
    before = {name: (anchor_case / name).read_bytes() for name in anchors.ANCHORS}
    foreign_bytes = foreign_leaf.read_bytes()
    with pytest.raises(ValueError, match="aliased|unaliased"):
        anchors.restore_requested_case(request, repository_root=ROOT)
    assert foreign_leaf.read_bytes() == foreign_bytes
    assert before == {name: (anchor_case / name).read_bytes() for name in anchors.ANCHORS}


def load_original(module):
    spec = importlib.util.spec_from_file_location(
        "historical_original_" + Path(module).stem, ROOT / module
    )
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


@pytest.mark.parametrize("module", [LABELS, CORRECTION])
def test_restored_fixture_still_rejects_subsequent_anchor_corruption(tmp_path, module, pre_mint_schema_case):
    original = load_original(module)
    if module == LABELS:
        case = original.case.__wrapped__(tmp_path, original.writer.frozen_owners())
    else:
        case = original.case.__wrapped__(tmp_path)
    request = request_for(module, tmp_path, case=case)
    assert anchors.restore_requested_case(request, repository_root=ROOT)
    canonical = tmp_path / "mappings/ingredient_mappings.sssom.tsv"
    canonical.write_bytes(canonical.read_bytes() + b"# deliberate later corruption\n")
    with pytest.raises(ValueError, match="anchor changed"):
        if module == LABELS:
            original.apply(case, enabled=False)
        else:
            original.writer.apply_sources(case[0], case[1])
    assert not (case[2] if module == LABELS else case[1]).exists()


@pytest.mark.parametrize("kind", ["modified", "aliased"])
def test_original_test_module_identity_is_required_before_fixture_access(tmp_path, kind):
    repository = tmp_path / "repository"
    module = repository / LABELS
    module.parent.mkdir(parents=True)
    if kind == "modified":
        module.write_bytes((ROOT / LABELS).read_bytes() + b"# changed test\n")
    else:
        module.symlink_to(ROOT / LABELS)
    request = SimpleNamespace(
        path=module,
        fixturenames=("case",),
        getfixturevalue=lambda _: pytest.fail("Changed module loaded a fixture"),
    )
    with pytest.raises(ValueError, match="Historical test.*changed|module is aliased"):
        anchors.restore_requested_case(request, repository_root=repository)


@pytest.mark.parametrize("module", [LABELS, CORRECTION])
def test_historical_schema_is_only_requested_for_exact_hash_bound_modules(module):
    called = []
    request = SimpleNamespace(path=ROOT / module, getfixturevalue=called.append)
    assert anchors.use_historical_schema(request)
    assert called == ["pre_mint_schema"]


def test_current_modules_never_request_historical_schema():
    request = SimpleNamespace(
        path=ROOT / "tests/test_stable_ids.py",
        getfixturevalue=lambda _: pytest.fail("Current schema was redirected"),
    )
    assert not anchors.use_historical_schema(request)


def test_modified_historical_module_cannot_select_old_schema(tmp_path):
    path = tmp_path / CORRECTION
    path.parent.mkdir(parents=True)
    path.write_bytes((ROOT / CORRECTION).read_bytes() + b"\n# changed test\n")
    request = SimpleNamespace(
        path=path,
        getfixturevalue=lambda _: pytest.fail("Schema selected before content check"),
    )
    with pytest.raises(ValueError, match="Historical test changed"):
        anchors.use_historical_schema(request, repository_root=tmp_path)


def test_frozen_schema_context_does_not_relax_current_required_identity():
    from mediaingredientmech.validation.write_validated import validate_ingredient
    from tests.pre_mint_schema import historical_schema

    old_record = {"identifier": "CHEBI:15377", "preferred_term": "Water", "mapping_status": "MAPPED"}
    assert any("mim_id" in error.message for error in validate_ingredient(old_record))
    with historical_schema():
        assert validate_ingredient(old_record) == []
    assert any("mim_id" in error.message for error in validate_ingredient(old_record))
