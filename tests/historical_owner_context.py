"""Finite dated inputs for ten unchanged assertion bodies (#1447).

Only explicitly requested fixtures use these bytes. Live corpus fixtures,
stable-ID lookup, validators and publication gates remain current.
"""

from __future__ import annotations

import base64
import csv
import gzip
import hashlib
import io
import json
import os
from contextlib import contextmanager
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / "tests/fixtures/historical_owners_1447"
ARCHIVE = DIRECTORY / "context.json.gz"
SOURCE = DIRECTORY / "source.json"
ARCHIVE_SHA256 = "3c8dbb1584e40a537be123f64bee4ec30c40671db2cea10fa586eae9e83c3f7b"
SOURCE_SHA256 = "bebdec0775b84b1d6b5a95aa8fdf2b973c020257a75a5e4caf8623b3a8099f77"
REVISION = "0dac278466699129a083343a921c2e0ca18a9ab4"
MAPPED = "data/curated/mapped_ingredients.yaml"
SSSOM = "mappings/ingredient_mappings.sssom.tsv"
MEMBERSHIP = "mappings/culturemech_recipe_membership.tsv"
EVIDENCE = "reports/sssom_completion_20260921/mapping_review/identity-review-20260924"
CASES = {
    "test_hydrate_family_identity.py": {
        "test_l_cysteine_solution_keeps_local_identity_on_the_hydrate_parent": None,
        "test_variable_sulfate_hydrates_are_locally_identified": None,
        "test_variable_sulfate_membership_rows_move_to_local_identity": None,
        "test_formula_supported_sulfates_have_local_identities": ("term", "MgSO4 x 6 H2O"),
    },
    "test_lipoic_stereochemistry.py": {
        "test_wolfe_vitamin_components_use_generic_lipoic_acid": None,
    },
    "test_reviewed_ingredient_identities.py": {
        "test_ncit_current_cas_evidence_agrees_with_promoted_records": None,
        "test_bsa_recipe_membership_and_supplier_preparations_stay_separate": None,
    },
    "test_fix_merge_tombstone_resolution.py": {
        "test_persisted_split_preserves_history_and_avoids_retired_id": (
            "slug",
            "Trisodium_Citrate_X_3_H2o",
        ),
    },
}


def require(condition, message):
    if not condition:
        raise ValueError("Historical owner context: " + message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def regular(path):
    path = Path(path).absolute()
    require(path == path.resolve() and path.is_file(), "aliased or missing input")
    require(path.stat().st_nlink == 1, "hardlinked input")
    return path.read_bytes()


def source_document(path=SOURCE):
    raw = regular(path)
    require(digest(raw) == SOURCE_SHA256, "source manifest changed")
    doc = json.loads(raw)
    require(doc["source_revision"] == REVISION, "source revision differs")
    return doc


def decode_context(raw, source):
    """Each member must match the independently pinned Git inventory."""
    doc = json.loads(gzip.decompress(raw))
    require(
        set(doc) == {"schema_version", "source_revision", "source_tree", "files"}
        and type(doc["schema_version"]) is int
        and doc["schema_version"] == 1
        and doc["source_revision"] == REVISION == source["source_revision"]
        and doc["source_tree"] == source["source_tree"]
        and set(doc["files"]) == set(source["files"]),
        "archive identity or membership differs",
    )
    result = {}
    for name, expected in source["files"].items():
        item = doc["files"][name]
        require(set(item) == {*expected, "base64"}, "member metadata differs")
        require({k: item[k] for k in expected} == expected, "member metadata differs")
        require(expected["mode"] == "100644", "unexpected Git mode")
        content = base64.b64decode(item["base64"], validate=True)
        require(
            digest(content) == expected["sha256"]
            and type(item["bytes"]) is int
            and len(content) == item["bytes"],
            "member bytes differ: " + name,
        )
        result[name] = content
    return result


def context_bytes(archive=ARCHIVE, source_path=SOURCE):
    source = source_document(source_path)
    raw = regular(archive)
    require(digest(raw) == ARCHIVE_SHA256, "archive hash differs")
    return decode_context(raw, source)


def requested_case(module_path, name, params, repository_root=ROOT):
    path = Path(module_path)
    for module, cases in CASES.items():
        if path != repository_root / "tests" / module or name not in cases:
            continue
        condition = cases[name]
        return condition is None or params.get(condition[0]) == condition[1]
    return False


def selected(request):
    params = getattr(getattr(request.node, "callspec", None), "params", {})
    return requested_case(request.module.__file__, request.node.originalname, params)


def rows(raw):
    # These authenticated historical files have only a leading metadata block.
    lines = raw.decode("utf-8").splitlines(keepends=True)
    while lines and lines[0].startswith("#"):
        lines.pop(0)
    return list(csv.DictReader(io.StringIO("".join(lines)), delimiter="\t"))


@contextmanager
def bind_root(module, name, params, destination, *, repository_root=ROOT):
    require(requested_case(module.__file__, name, params, repository_root), "unselected case")
    require(module.ROOT == repository_root, "module already rebound")
    original_evidence = getattr(module, "EVIDENCE", None)
    if original_evidence is not None:
        require(original_evidence == repository_root / EVIDENCE, "evidence already rebound")
    inputs = context_bytes()
    destination = Path(destination).absolute()
    require(
        destination == destination.resolve() and not os.path.lexists(destination),
        "fresh unaliased destination required",
    )
    destination.mkdir()
    for relative, raw in inputs.items():
        path = destination / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("xb") as stream:
            stream.write(raw)
    original_root = module.ROOT
    module.ROOT = destination
    if original_evidence is not None:
        module.EVIDENCE = destination / EVIDENCE
    try:
        yield inputs
    finally:
        module.ROOT = original_root
        if original_evidence is not None:
            module.EVIDENCE = original_evidence
        require(
            {
                p.relative_to(destination).as_posix()
                for p in destination.rglob("*")
                if p.is_file() or p.is_symlink()
            }
            == set(inputs),
            "fixture membership changed",
        )
        require(
            all(regular(destination / n) == b for n, b in inputs.items()), "fixture content changed"
        )
        require(context_bytes() == inputs, "historical source changed")


@pytest.fixture
def historical_owner_records(request):
    require(selected(request), "unselected record fixture")
    inputs = context_bytes()
    yield yaml.safe_load(inputs[MAPPED])["ingredients"]
    require(context_bytes() == inputs, "historical source changed")


@pytest.fixture
def historical_owner_sssom(request):
    require(selected(request), "unselected SSSOM fixture")
    return rows(context_bytes()[SSSOM])


@pytest.fixture
def historical_owner_membership(request):
    require(selected(request), "unselected membership fixture")
    return rows(context_bytes()[MEMBERSHIP])


@pytest.fixture
def historical_wolfe_records(historical_owner_records):
    return {r["preferred_term"]: r for r in historical_owner_records}


@pytest.fixture
def sulfate_case_records(request, records):
    # Original three other parameter instances continue using current records.
    if selected(request):
        return yaml.safe_load(context_bytes()[MAPPED])["ingredients"]
    return records


@pytest.fixture
def historical_identity_case(request, tmp_path):
    require(selected(request), "unselected identity fixture")
    with bind_root(request.module, request.node.originalname, {}, tmp_path / "historical-inputs"):
        yield


@pytest.fixture
def historical_split_case(request, tmp_path):
    if not selected(request):
        yield
        return
    with bind_root(
        request.module,
        request.node.originalname,
        request.node.callspec.params,
        tmp_path / "historical-inputs",
    ):
        yield
