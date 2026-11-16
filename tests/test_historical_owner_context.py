"""#1447 context integrity, exact scope and restoration controls."""

import base64
import copy
import gzip
import json
import types

import pytest

from tests import historical_owner_context as context


def packed(doc):
    return gzip.compress(json.dumps(doc).encode(), mtime=0)


def original_document():
    return json.loads(gzip.decompress(context.ARCHIVE.read_bytes()))


def module():
    return types.SimpleNamespace(
        __file__=str(context.ROOT / "tests/test_reviewed_ingredient_identities.py"),
        ROOT=context.ROOT,
        EVIDENCE=context.ROOT / context.EVIDENCE,
    )


CASE = "test_bsa_recipe_membership_and_supplier_preparations_stay_separate"


def test_complete_git_context_has_exact_fifteen_members():
    inputs = context.context_bytes()
    source = context.source_document()
    assert len(inputs) == 15
    assert set(inputs) == set(source["files"])
    assert sum(map(len, inputs.values())) == 18517173
    assert all(context.digest(b) == source["files"][n]["sha256"] for n, b in inputs.items())


@pytest.mark.parametrize(
    "kind", ["revision", "tree", "extra", "missing", "bytes", "size", "mode", "blob"]
)
def test_archive_refuses_identity_membership_and_member_drift(kind):
    doc = original_document()
    key = next(iter(doc["files"]))
    if kind == "revision":
        doc["source_revision"] = "0" * 40
    elif kind == "tree":
        doc["source_tree"] = "0" * 40
    elif kind == "extra":
        doc["files"]["extra"] = copy.deepcopy(doc["files"][key])
    elif kind == "missing":
        del doc["files"][key]
    elif kind == "bytes":
        doc["files"][key]["base64"] = base64.b64encode(b"changed").decode()
    elif kind == "size":
        doc["files"][key]["bytes"] += 1
    elif kind == "mode":
        doc["files"][key]["mode"] = "100755"
    else:
        doc["files"][key]["git_blob"] = "0" * 40
    with pytest.raises(ValueError):
        context.decode_context(packed(doc), context.source_document())


@pytest.mark.parametrize("kind", ["archive", "source", "symlink", "hardlink"])
def test_live_container_and_manifest_guards(kind, tmp_path):
    archive = tmp_path / "context.gz"
    source = tmp_path / "source.json"
    archive.write_bytes(context.ARCHIVE.read_bytes())
    source.write_bytes(context.SOURCE.read_bytes())
    if kind == "archive":
        archive.write_bytes(archive.read_bytes() + b"bad")
    elif kind == "source":
        source.write_bytes(source.read_bytes() + b" ")
    elif kind == "symlink":
        other = tmp_path / "symlink.gz"
        other.symlink_to(archive)
        archive = other
    else:
        (tmp_path / "hardlink.gz").hardlink_to(archive)
    with pytest.raises(ValueError):
        context.context_bytes(archive, source)


@pytest.mark.parametrize(
    "case,params,selected",
    [
        ("test_formula_supported_sulfates_have_local_identities", {"term": "MgSO4 x 6 H2O"}, True),
        ("test_formula_supported_sulfates_have_local_identities", {"term": "FeSO4 x 5 H2O"}, False),
        ("test_formula_supported_sulfates_have_local_identities", {"term": "FeSO4 x 6 H2O"}, False),
        ("test_formula_supported_sulfates_have_local_identities", {"term": "MnSO4 x 7 H2O"}, False),
        ("test_variable_ferric_sulfate_hydrate_is_not_moved_to_the_monohydrate", {}, False),
    ],
)
def test_only_the_selected_hydrate_cases_receive_history(case, params, selected):
    path = context.ROOT / "tests/test_hydrate_family_identity.py"
    assert context.requested_case(path, case, params) is selected


def test_unrelated_sulfate_fixture_returns_original_cached_current_object():
    records = [{"current": True}]
    request = types.SimpleNamespace(
        module=types.SimpleNamespace(
            __file__=str(context.ROOT / "tests/test_hydrate_family_identity.py")
        ),
        node=types.SimpleNamespace(
            originalname="test_formula_supported_sulfates_have_local_identities",
            callspec=types.SimpleNamespace(params={"term": "FeSO4 x 5 H2O"}),
        ),
    )
    assert context.sulfate_case_records.__wrapped__(request, records) is records
    assert records == [{"current": True}]


def test_foreign_module_is_refused_before_destination_creation(tmp_path):
    m = module()
    m.__file__ = str(tmp_path / "test_reviewed_ingredient_identities.py")
    dest = tmp_path / "input"
    with pytest.raises(ValueError, match="unselected"):
        with context.bind_root(m, CASE, {}, dest):
            pass
    assert not dest.exists()
    assert m.ROOT == context.ROOT


@pytest.mark.parametrize("exception", [False, True])
def test_complete_root_binding_restores_globals_on_success_and_exception(tmp_path, exception):
    m = module()
    try:
        with context.bind_root(m, CASE, {}, tmp_path / "input") as inputs:
            assert m.ROOT == tmp_path / "input"
            assert m.EVIDENCE == m.ROOT / context.EVIDENCE
            assert all((m.ROOT / n).read_bytes() == b for n, b in inputs.items())
            if exception:
                raise RuntimeError("deliberate original test error")
    except RuntimeError:
        assert exception
    assert m.ROOT == context.ROOT and m.EVIDENCE == context.ROOT / context.EVIDENCE


@pytest.mark.parametrize("kind", ["extra", "missing", "changed", "alias"])
def test_late_fixture_drift_refuses_and_restores_module(tmp_path, kind):
    m = module()
    with pytest.raises(ValueError):
        with context.bind_root(m, CASE, {}, tmp_path / "input") as inputs:
            target = m.ROOT / next(iter(inputs))
            if kind == "extra":
                (m.ROOT / "extra").write_text("extra")
            elif kind == "missing":
                target.unlink()
            elif kind == "changed":
                target.write_text("changed")
            else:
                payload = target.read_bytes()
                target.unlink()
                elsewhere = tmp_path / "elsewhere"
                elsewhere.write_bytes(payload)
                target.symlink_to(elsewhere)
    assert m.ROOT == context.ROOT and m.EVIDENCE == context.ROOT / context.EVIDENCE


def test_existing_destination_is_not_reused(tmp_path):
    dest = tmp_path / "input"
    dest.mkdir()
    with pytest.raises(ValueError, match="fresh"):
        with context.bind_root(module(), CASE, {}, dest):
            pass


def test_already_rebound_evidence_refuses_without_changing_root(tmp_path):
    m = module()
    m.EVIDENCE = tmp_path
    with pytest.raises(ValueError, match="evidence already"):
        with context.bind_root(m, CASE, {}, tmp_path / "input"):
            pass
    assert m.ROOT == context.ROOT
    assert not (tmp_path / "input").exists()
