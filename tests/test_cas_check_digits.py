"""Tests for CAS Registry Number check-digit validation (#753)."""

from __future__ import annotations

import importlib.util
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO / "scripts" / "validate_cas_check_digits.py"


def _load_validator():
    spec = importlib.util.spec_from_file_location("validate_cas_check_digits", SCRIPT_PATH)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_is_valid_cas_rn():
    mod = _load_validator()
    # Valid CAS-RNs
    assert mod.is_valid_cas_rn("7732-18-5") == (True, 5, 5)
    assert mod.is_valid_cas_rn("cas:10031-43-3") == (True, 3, 3)
    assert mod.is_valid_cas_rn("CAS:5786-71-0") == (True, 0, 0)
    assert mod.is_valid_cas_rn("cas:16695-21-9") == (True, 9, 9)
    # Upstream ChEBI typos documented in #753
    assert mod.is_valid_cas_rn("480-43-4") == (False, 4, 3)
    assert mod.is_valid_cas_rn("cas:138-86-7") == (False, 7, 3)
    # Non-CAS string
    assert mod.is_valid_cas_rn("not-a-cas") == (False, None, None)


def test_supported_sssom_has_zero_invalid_cas_check_digits():
    mod = _load_validator()
    assert mod.scan_sssom_file(mod.SUPPORTED_SSSOM) == []
    yaml_findings = mod.scan_yaml_records()
    published = [f for f in yaml_findings if f["release_state"] == "PUBLISHED"]
    assert published == []
