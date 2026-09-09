"""Shared fixtures.

The kg-microbe dictionary writes a parsed index to a user cache directory
(#589). Tests must never touch the real one: they would leave indexes behind
on the developer's machine, and a cache built by one test could answer another
test's question. Every test gets its own.
"""

from __future__ import annotations

import pytest

from mediaingredientmech.validation.kg_microbe_dict import CACHE_DIR_ENV


@pytest.fixture(autouse=True)
def _isolated_dictionary_cache(tmp_path_factory, monkeypatch):
    monkeypatch.setenv(CACHE_DIR_ENV, str(tmp_path_factory.mktemp("kgm-cache")))
