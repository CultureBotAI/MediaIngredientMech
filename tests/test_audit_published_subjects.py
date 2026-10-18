"""Tests for scripts/audit_published_subjects.py (#300)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "audit_published_subjects.py"


@pytest.fixture(scope="module")
def mod():
    spec = importlib.util.spec_from_file_location("audit_published_subjects", SCRIPT)
    m = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = m
    spec.loader.exec_module(m)
    return m


def test_live_published_subjects_match_baseline(mod):
    """#300: the committed baseline and SSSOM pass --check."""
    assert mod.main(["--check"]) == 0


def test_vanished_subject_without_alias_fails_check_and_write_baseline(mod, tmp_path, monkeypatch):
    """#300: a subject removed from SSSOM without an alias row fails both --check
    and --write-baseline so the omission cannot be laundered."""
    baseline = tmp_path / "baseline.tsv"
    sssom = tmp_path / "sssom.tsv"
    aliases = tmp_path / "aliases.tsv"

    baseline.write_text(
        "subject_id\tsubject_label\n"
        "MIM:Kept\tKept\n"
        "MIM:Vanished\tVanished\n",
        encoding="utf-8",
    )
    sssom.write_text(
        "# curie_map:\n"
        "subject_id\tsubject_label\tpredicate_id\tobject_id\n"
        "MIM:Kept\tKept\tskos:exactMatch\tCHEBI:1\n",
        encoding="utf-8",
    )
    aliases.write_text(
        "old_curie\tcurrent_curie\tfirst_seen\tretired_at\tchain_length\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(mod, "BASELINE", baseline)
    monkeypatch.setattr(mod, "SSSOM", sssom)
    monkeypatch.setattr(mod, "ALIASES", aliases)

    assert mod.main(["--check"]) == 2
    assert mod.main(["--write-baseline"]) == 2


def test_vanished_subject_with_live_alias_passes_and_refreshes_baseline(mod, tmp_path, monkeypatch):
    """#300: a vanished subject covered by mim_curie_aliases.tsv passes --check
    and allows --write-baseline to advance the baseline."""
    baseline = tmp_path / "baseline.tsv"
    sssom = tmp_path / "sssom.tsv"
    aliases = tmp_path / "aliases.tsv"

    baseline.write_text(
        "subject_id\tsubject_label\n"
        "MIM:Kept\tKept\n"
        "MIM:Old_Name\tOld Name\n",
        encoding="utf-8",
    )
    sssom.write_text(
        "# curie_map:\n"
        "subject_id\tsubject_label\tpredicate_id\tobject_id\n"
        "MIM:Kept\tKept\tskos:exactMatch\tCHEBI:1\n"
        "MIM:New_Name\tNew Name\tskos:exactMatch\tCHEBI:2\n",
        encoding="utf-8",
    )
    aliases.write_text(
        "old_curie\tcurrent_curie\tfirst_seen\tretired_at\tchain_length\n"
        "MIM:Old_Name\tMIM:New_Name\t2026-08-01\t2026-08-02\t2\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(mod, "BASELINE", baseline)
    monkeypatch.setattr(mod, "SSSOM", sssom)
    monkeypatch.setattr(mod, "ALIASES", aliases)

    assert mod.main(["--check"]) == 0
    assert mod.main(["--write-baseline"]) == 0
    refreshed = mod.load_baseline(baseline)
    assert set(refreshed) == {"MIM:Kept", "MIM:New_Name"}


def test_dangling_alias_target_fails_check(mod, tmp_path, monkeypatch):
    """#300: an alias pointing to a target absent from the SSSOM is caught."""
    baseline = tmp_path / "baseline.tsv"
    sssom = tmp_path / "sssom.tsv"
    aliases = tmp_path / "aliases.tsv"

    baseline.write_text(
        "subject_id\tsubject_label\n"
        "MIM:Old_Name\tOld Name\n",
        encoding="utf-8",
    )
    sssom.write_text(
        "# curie_map:\n"
        "subject_id\tsubject_label\tpredicate_id\tobject_id\n"
        "MIM:Kept\tKept\tskos:exactMatch\tCHEBI:1\n",
        encoding="utf-8",
    )
    aliases.write_text(
        "old_curie\tcurrent_curie\tfirst_seen\tretired_at\tchain_length\n"
        "MIM:Old_Name\tMIM:Ghost_Target\t2026-08-01\t2026-08-02\t2\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(mod, "BASELINE", baseline)
    monkeypatch.setattr(mod, "SSSOM", sssom)
    monkeypatch.setattr(mod, "ALIASES", aliases)

    assert mod.main(["--check"]) == 2
