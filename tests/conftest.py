"""Shared fixtures.

The kg-microbe dictionary writes a parsed index to a user cache directory
(#589). Tests must never touch the real one: they would leave indexes behind
on the developer's machine, and a cache built by one test could answer another
test's question. Every test gets its own.
"""

from __future__ import annotations

from contextlib import ExitStack
from pathlib import Path

import pytest

from mediaingredientmech.validation.kg_microbe_dict import CACHE_DIR_ENV
from tests.historical_correction_prestate import MODULE, ROOT, correction_context
from tests.historical_owner_context import (  # noqa: F401
    historical_identity_case,
    historical_owner_membership,
    historical_owner_records,
    historical_owner_sssom,
    historical_split_case,
    historical_wolfe_records,
    sulfate_case_records,
)
from tests.historical_partonomy_context import bind_context, requested_case
from tests.historical_source_anchors import restore_requested_case, use_historical_schema
from tests.pre_mint_schema import pre_mint_schema, pre_mint_schema_case  # noqa: F401


@pytest.fixture(autouse=True)
def _isolated_dictionary_cache(tmp_path_factory, monkeypatch):
    monkeypatch.setenv(CACHE_DIR_ENV, str(tmp_path_factory.mktemp("kgm-cache")))


@pytest.fixture(autouse=True)
def _historical_partonomy_context(request, tmp_path_factory):
    """#467: preserve dated assertions and test current corpus separately."""
    case = request.node.originalname
    if requested_case(request.path, case) is None:
        yield
        return
    parent = tmp_path_factory.mktemp("historical-partonomy-467")
    with bind_context(request.module, case, parent / "inputs"):
        yield


@pytest.fixture(autouse=True)
def _historical_step7c_source_anchors(request):
    """Keep the original evidence-bound source tests portable after publication."""
    use_historical_schema(request)
    if Path(request.path) == ROOT / MODULE:
        request.getfixturevalue("historical_correction_evidence")(request.module)
    restore_requested_case(request)


@pytest.fixture
def historical_correction_evidence(tmp_path_factory):
    """#1441: scope original correction tests to their exact evidence prestate."""
    with ExitStack() as stack:

        def bind(module):
            # Unrelated modules never allocate a context or read its archive.
            if Path(module.__file__) != ROOT / MODULE:
                return False
            parent = tmp_path_factory.mktemp("historical-correction-1441")
            return stack.enter_context(correction_context(module, parent / "evidence"))

        yield bind
