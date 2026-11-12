"""Shared fixtures.

The kg-microbe dictionary writes a parsed index to a user cache directory
(#589). Tests must never touch the real one: they would leave indexes behind
on the developer's machine, and a cache built by one test could answer another
test's question. Every test gets its own.
"""

from __future__ import annotations

import pytest

from mediaingredientmech.validation.kg_microbe_dict import CACHE_DIR_ENV
from tests.historical_source_anchors import restore_requested_case, use_historical_schema
from tests.pre_mint_schema import pre_mint_schema, pre_mint_schema_case  # noqa: F401


@pytest.fixture(autouse=True)
def _isolated_dictionary_cache(tmp_path_factory, monkeypatch):
    monkeypatch.setenv(CACHE_DIR_ENV, str(tmp_path_factory.mktemp("kgm-cache")))


@pytest.fixture(autouse=True)
def _historical_step7c_source_anchors(request):
    """Keep the original evidence-bound source tests portable after publication."""
    use_historical_schema(request)
    restore_requested_case(request)
