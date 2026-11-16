"""Executable annotations must survive type-only proof normalization (#1432/#1433/#1434)."""

import importlib.util
from pathlib import Path

import pytest

SPEC = importlib.util.spec_from_file_location(
    "type_only_source_comparison",
    Path(__file__).resolve().parents[1] / "scripts/adhoc/compare_type_only_sources.py",
)
assert SPEC is not None and SPEC.loader is not None
helper = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(helper)


def test_postponed_simple_name_annotation_is_permitted():
    before = "from __future__ import annotations\ndef record(events):\n    return len(events)\n"
    after = before.replace("    return", "    value: int\n    return")
    assert helper.compare(before, after)["normalized_type_only_equivalent"] is True


@pytest.mark.parametrize("future", ["", "from __future__ import annotations\n"])
def test_executable_attribute_annotation_is_refused(future):
    before = future + "def record(events):\n    return len(events)\n"
    after = before.replace("    return", '    events.append("executed").ignored: int\n    return')
    original, proposed = {}, {}
    exec(before, original)
    exec(after, proposed)
    left, right = [], []
    assert original["record"](left) == 0 and left == []
    assert proposed["record"](right) == 1 and right == ["executed"]
    assert helper.compare(before, after)["normalized_type_only_equivalent"] is False


def test_evaluated_annotation_expression_is_refused():
    before = 'events = []\ndef mark():\n    events.append("executed")\n    return int\n'
    after = before + "value: mark()\n"
    original, proposed = {}, {}
    exec(before, original)
    exec(after, proposed)
    assert original["events"] == [] and proposed["events"] == ["executed"]
    assert helper.compare(before, after)["normalized_type_only_equivalent"] is False


@pytest.mark.parametrize("prefix, indent", [("", ""), ("class Example:\n", "    ")])
def test_ordinary_firstlineno_assignment_is_compared(prefix, indent):
    before = prefix + indent + "__firstlineno__ = 11\n"
    after = prefix + indent + "__firstlineno__ = 12\n"
    result = helper.compare(before, after)
    assert result["raw_code_equivalent"] is False
    assert result["normalized_type_only_equivalent"] is False


@pytest.mark.parametrize(
    "left, right", [("True", "1"), ("1", "1.0"), ("0.0", "-0.0"), ("1+0j", "1"), ("0j", "-0j")]
)
def test_scalar_types_and_floating_point_bits_are_compared(left, right):
    before = "def value():\n    return " + left + "\n"
    after = "def value():\n    return " + right + "\n"
    result = helper.compare(before, after)
    assert result["raw_code_equivalent"] is False
    assert result["normalized_type_only_equivalent"] is False


def test_postponed_local_annotation_cannot_hide_changed_binding():
    before = "from __future__ import annotations\nx = 1\ndef value():\n    return x\n"
    after = before.replace("    return x", "    x: int\n    return x")
    original, proposed = {}, {}
    exec(before, original)
    exec(after, proposed)
    assert original["value"]() == 1
    with pytest.raises(UnboundLocalError):
        proposed["value"]()
    result = helper.compare(before, after)
    assert result["normalized_structure_equivalent"] is True
    assert "value" in result["function_code_changes"]
    assert result["normalized_type_only_equivalent"] is False
