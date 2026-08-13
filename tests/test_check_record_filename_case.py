"""Tests for the per-record filename case guard (#352).

The bug this guards against is undetectable on the platform most contributors
use, so the tests drive the pure functions with the real path spellings that
caused each failure rather than relying on filesystem behaviour.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


def _load():
    spec = importlib.util.spec_from_file_location(
        "check_record_filename_case", ROOT / "scripts" / "check_record_filename_case.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


mod = _load()
P = "data/ingredients/mapped"


class TestFindDrift:
    def test_detects_the_thiamine_case_that_broke_ci(self):
        """git tracked Thiamine_Pyrophosphate.yaml; the exporter wrote
        Thiamine_pyrophosphate.yaml. macOS folded them; Linux made two files."""
        tracked = {f"{P}/Thiamine_Pyrophosphate.yaml", f"{P}/Glucose.yaml"}
        disk = {f"{P}/Thiamine_pyrophosphate.yaml", f"{P}/Glucose.yaml"}
        assert mod.find_drift(tracked, disk) == [
            (f"{P}/Thiamine_Pyrophosphate.yaml", f"{P}/Thiamine_pyrophosphate.yaml")]

    def test_detects_the_earlier_sodium_tartrate_case(self):
        """The same class, previously misdiagnosed as a lost record."""
        tracked = {f"{P}/Sodium_Tartrate.yaml"}
        disk = {f"{P}/Sodium_tartrate.yaml"}
        assert len(mod.find_drift(tracked, disk)) == 1

    def test_clean_corpus_reports_nothing(self):
        paths = {f"{P}/Glucose.yaml", f"{P}/Maltose.yaml"}
        assert mod.find_drift(paths, paths) == []

    def test_a_genuinely_absent_file_is_not_drift(self):
        """Absent is a different defect and must not be reported as a rename."""
        tracked = {f"{P}/Glucose.yaml", f"{P}/Deleted.yaml"}
        disk = {f"{P}/Glucose.yaml"}
        assert mod.find_drift(tracked, disk) == []

    def test_differences_beyond_case_are_not_drift(self):
        tracked = {f"{P}/Sodium_Citrate.yaml"}
        disk = {f"{P}/Sodium_Citrate_2.yaml"}
        assert mod.find_drift(tracked, disk) == []


class TestFindCollisions:
    def test_detects_two_tracked_paths_differing_only_by_case(self):
        """On Linux both exist and one record shadows the other."""
        tracked = {f"{P}/Glucose.yaml", f"{P}/glucose.yaml", f"{P}/Maltose.yaml"}
        assert mod.find_collisions(tracked) == [
            [f"{P}/Glucose.yaml", f"{P}/glucose.yaml"]]

    def test_no_collisions_in_a_clean_set(self):
        assert mod.find_collisions({f"{P}/Glucose.yaml", f"{P}/Maltose.yaml"}) == []

    def test_paths_in_different_directories_are_not_a_collision(self):
        tracked = {f"{P}/Glucose.yaml", "data/ingredients/unmapped/Glucose.yaml"}
        assert mod.find_collisions(tracked) == []


class TestUnicodeNormalisation:
    @pytest.mark.parametrize("name", ["Α-lipoic_Acid", "Poly-ß-hydroxybutyric_Acid"])
    def test_nfd_and_nfc_spellings_are_not_reported_as_drift(self, name):
        """macOS returns NFD from listdir while git stores NFC. Without
        normalisation these look like five renames that do not exist."""
        import unicodedata
        tracked = {f"{P}/{unicodedata.normalize('NFC', name)}.yaml"}
        disk = {f"{P}/{unicodedata.normalize('NFD', name)}.yaml"}
        assert mod.find_drift({mod._nfc(p) for p in tracked},
                              {mod._nfc(p) for p in disk}) == []


class TestAgainstTheRealRepo:
    def test_tracked_paths_are_unquoted(self):
        """`git ls-files` without -z backslash-quotes non-ASCII paths, which
        produced five spurious 'missing file' hits during the #352 diagnosis."""
        assert not [p for p in mod.tracked_paths() if "\\" in p]

    def test_the_committed_corpus_is_currently_clean(self):
        tracked, disk = mod.tracked_paths(), mod.disk_paths()
        assert mod.find_drift(tracked, disk) == []
        assert mod.find_collisions(tracked) == []
