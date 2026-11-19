"""Explicit pre-#1265 schema for checksum-bound historical migration replay.

Opt in only in tests whose subject is a dated historical writer. This fixture
never changes the current schema, injects IDs, rewrites historical source bytes,
or bypasses the historical writer's content/review provenance checks.
"""
from __future__ import annotations

import hashlib
import json
from contextlib import contextmanager
from pathlib import Path

import pytest

from mediaingredientmech.validation import write_validated

ROOT = Path(__file__).parents[1]
SOURCE = Path(__file__).parent / "fixtures/pre_mint_schema_1265"
SOURCE_COMMIT = "0dac278466699129a083343a921c2e0ca18a9ab4"


@contextmanager
def historical_schema():
    manifest = json.loads((SOURCE / "manifest.json").read_text())
    assert manifest["source_commit"] == SOURCE_COMMIT
    for description in manifest["files"].values():
        raw = (ROOT / description["snapshot_path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == description["sha256"]
    snapshot = ROOT / manifest["files"]["mediaingredientmech.yaml"]["snapshot_path"]
    current = write_validated.DEFAULT_SCHEMA_PATH.resolve()
    original = write_validated._get_validator

    def historical_validator(schema_path):
        selected = snapshot if Path(schema_path).resolve() == current else schema_path
        return original(selected)

    with pytest.MonkeyPatch.context() as patch:
        patch.setattr(write_validated, "_get_validator", historical_validator)
        yield snapshot


@pytest.fixture(scope="module")
def pre_mint_schema():
    """Opt in an entire dated historical test module."""
    with historical_schema() as snapshot:
        yield snapshot


@pytest.fixture
def pre_mint_schema_case():
    """Opt in one archived replay without affecting current tests in its module."""
    with historical_schema() as snapshot:
        yield snapshot
