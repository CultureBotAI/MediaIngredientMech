"""#467: historical fixture integrity and separate full current-corpus gates."""

import base64
import gzip
import hashlib
import importlib.util
import json
import os
import sys
from copy import deepcopy
from types import SimpleNamespace

import pytest

from mediaingredientmech.validation.component_partonomy import (
    load_curated_records,
    validate_component_partonomy,
)
from tests import historical_partonomy_context as context


def producer():
    spec = importlib.util.spec_from_file_location(
        "partonomy_467_current_gate", context.ROOT / context.WRITER
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def current_records():
    return load_curated_records(context.ROOT / "data/curated")


def test_complete_current_corpus_keeps_native_semantic_validation(current_records):
    """The live corpus never receives the historical ROOT binding."""
    assert validate_component_partonomy(current_records) == []
    assert {"mapped_ingredients.yaml", "unmapped_ingredients.yaml"} == {
        name.rsplit("/", 1)[-1] for name in context.INPUTS if name.startswith("data/curated/")
    }


def test_current_corpus_refuses_historical_migration_without_changes(current_records):
    records = deepcopy(current_records)
    before = deepcopy(records)
    with pytest.raises(ValueError, match="neither the reviewed pre-migration"):
        producer().migrate(records)
    assert records == before
    assert current_records == before


@pytest.mark.parametrize("mutation", ["revision", "missing_catalog", "extra_member", "payload"])
def test_coherently_rewritten_historical_container_cannot_change_context(mutation):
    doc = json.loads(gzip.decompress(context.ARCHIVE.read_bytes()))
    if mutation == "revision":
        doc["source_revision"] = "0" * 40
    elif mutation == "missing_catalog":
        del doc["files"]["data/curated/unmapped_ingredients.yaml"]
    elif mutation == "extra_member":
        doc["files"]["../current-record.yaml"] = {}
    else:
        entry = doc["files"]["data/curated/mapped_ingredients.yaml"]
        raw = base64.b64decode(entry["base64"]) + b"\n# altered identity catalog\n"
        entry.update(
            base64=base64.b64encode(raw).decode(),
            bytes=len(raw),
            sha256=hashlib.sha256(raw).hexdigest(),
        )
    encoded = gzip.compress(json.dumps(doc).encode(), mtime=0)
    with pytest.raises(ValueError, match="identity or membership differs|input bytes differ"):
        context.decode_context(encoded)


def test_wrong_archive_bytes_are_rejected(tmp_path):
    archive = tmp_path / "context.json.gz"
    archive.write_bytes(context.ARCHIVE.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="archive hash differs"):
        context.context_bytes(archive)


@pytest.mark.parametrize("kind", ["symlink", "hardlink"])
def test_archive_aliases_are_rejected(tmp_path, kind):
    source = tmp_path / "original.gz"
    source.write_bytes(context.ARCHIVE.read_bytes())
    alias = tmp_path / "alias.gz"
    if kind == "symlink":
        alias.symlink_to(source)
    else:
        os.link(source, alias)
    with pytest.raises(ValueError, match="aliased|hardlinked"):
        context.context_bytes(alias)


def test_only_named_original_cases_get_historical_context(tmp_path):
    original = "tests/test_component_partonomy.py"
    assert (
        context.requested_case(
            context.ROOT / original, "test_real_curated_corpus_has_no_partonomy_violations"
        )
        == original
    )
    module = SimpleNamespace(__file__=str(context.ROOT / original), ROOT=context.ROOT)
    with context.bind_context(module, "unrelated_new_current_case", tmp_path / "unused") as bound:
        assert bound is False
        assert module.ROOT == context.ROOT
    assert not (tmp_path / "unused").exists()


def test_context_tamper_is_rejected_and_original_root_restored(tmp_path):
    module = SimpleNamespace(
        __file__=str(context.ROOT / "tests/test_component_partonomy.py"), ROOT=context.ROOT
    )
    destination = tmp_path / "context"
    with pytest.raises(ValueError, match="fixture content changed"):
        with context.bind_context(
            module, "test_real_curated_corpus_has_no_partonomy_violations", destination
        ) as bound:
            assert bound is True and module.ROOT == destination
            (destination / "data/curated/mapped_ingredients.yaml").write_bytes(b"ingredients: []\n")
    assert module.ROOT == context.ROOT


def test_historical_context_cannot_overwrite_an_existing_destination(tmp_path):
    module = SimpleNamespace(
        __file__=str(context.ROOT / "tests/test_component_partonomy.py"), ROOT=context.ROOT
    )
    destination = tmp_path / "existing"
    destination.mkdir()
    marker = destination / "retained.txt"
    marker.write_bytes(b"preserve")
    with pytest.raises(ValueError, match="new unaliased destination"):
        with context.bind_context(
            module, "test_real_curated_corpus_has_no_partonomy_violations", destination
        ):
            pytest.fail("an occupied destination must not be bound")
    assert marker.read_bytes() == b"preserve"
    assert module.ROOT == context.ROOT
