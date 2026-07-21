"""Tests for the Step 7b role-research template + template_vars extension + Edison shim."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml


_REPO_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _REPO_ROOT / "scripts"

# Ensure scripts/ is on sys.path so `research_ingredient_edison` imports resolve
# inside the shim's `_upstream_main` call.
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))


def _load(script: str):
    spec = importlib.util.spec_from_file_location(f"_test_{script}", _SCRIPTS_DIR / f"{script}.py")
    module = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    sys.modules[f"_test_{script}"] = module
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    return module


ri = _load("research_ingredient")


# ---------------- template_vars extensions ----------------


def _minimal_doc() -> dict:
    return {
        "identifier": "MediaIngredientMech:000042",
        "preferred_term": "Test ingredient",
        "ingredient_type": "SINGLE",
        "mapping_status": "MAPPED",
    }


def test_template_vars_carries_role_placeholders():
    tv = ri.template_vars(_minimal_doc(), "mapped", "test-ingredient")
    for key in (
        "candidate_nutritional_roles",
        "candidate_physicochemical_roles",
        "candidate_cellular_metabolic_roles",
        "existing_role_assignments",
        "chebi_role_axioms",
    ):
        assert key in tv, f"template_vars missing {key!r}"


def test_candidate_menus_are_the_full_facet_enum_values():
    tv = ri.template_vars(_minimal_doc(), "mapped", "t")
    # NutritionalRoleEnum currently has 12 values; check a few representatives.
    for tok in ("CARBON_SOURCE", "NITROGEN_SOURCE", "SULFUR_SOURCE", "VITAMIN_SOURCE"):
        assert tok in tv["candidate_nutritional_roles"], f"{tok} missing from nutritional menu"
    # PhysicochemicalRoleEnum
    for tok in ("BUFFER", "CHELATOR", "SURFACTANT", "REDUCING_AGENT"):
        assert tok in tv["candidate_physicochemical_roles"], f"{tok} missing from physicochem menu"
    # CellularMetabolicRoleEnum
    for tok in ("SUBSTRATE", "ELECTRON_DONOR", "COFACTOR", "INHIBITOR"):
        assert tok in tv["candidate_cellular_metabolic_roles"], f"{tok} missing from cellular menu"


def test_existing_role_assignments_flags_gaps():
    """A record with zero facet slots populated should be described as all-GAP."""
    tv = ri.template_vars(_minimal_doc(), "mapped", "t")
    assert "Nutritional: (none — GAP)" in tv["existing_role_assignments"]
    assert "Physicochemical: (none — GAP)" in tv["existing_role_assignments"]
    assert "Cellular-metabolic: (none — GAP)" in tv["existing_role_assignments"]


def test_existing_role_assignments_reports_populated_facets():
    doc = _minimal_doc()
    doc["nutritional_roles"] = [
        {"role": "CARBON_SOURCE", "confidence": 1.0},
        {"role": "ENERGY_SOURCE", "confidence": 0.7},
    ]
    doc["physicochemical_roles"] = [{"role": "BUFFER", "confidence": 0.9}]
    # cellular_metabolic_roles left empty
    tv = ri.template_vars(doc, "mapped", "t")
    summary = tv["existing_role_assignments"]
    assert "CARBON_SOURCE@1.00" in summary
    assert "ENERGY_SOURCE@0.70" in summary
    assert "BUFFER@0.90" in summary
    assert "Cellular-metabolic: (none — GAP)" in summary


def test_existing_role_assignments_handles_plain_string_roles():
    """The MIM schema stores rich assignments, but scalar-list callers must still render."""
    doc = _minimal_doc()
    doc["nutritional_roles"] = ["CARBON_SOURCE", "ENERGY_SOURCE"]
    tv = ri.template_vars(doc, "mapped", "t")
    summary = tv["existing_role_assignments"]
    assert "CARBON_SOURCE" in summary and "ENERGY_SOURCE" in summary


def test_chebi_role_axioms_no_grounding_returns_placeholder():
    doc = _minimal_doc()  # identifier is `MediaIngredientMech:000042` — not CHEBI:*
    tv = ri.template_vars(doc, "mapped", "t")
    assert "no chebi grounding" in tv["chebi_role_axioms"].lower()


def test_chebi_role_axioms_reads_from_ontology_mapping():
    doc = _minimal_doc()
    doc["ontology_mapping"] = {"ontology_id": "CHEBI:99999", "ontology_label": "notarealchebi"}
    # Live OAK call — either returns empty (unknown id) or "OAK adapter unavailable"
    # depending on whether sqlite:obo:chebi is warmed. Both are acceptable; the test
    # asserts the code path runs without raising and returns a string.
    tv = ri.template_vars(doc, "mapped", "t")
    assert isinstance(tv["chebi_role_axioms"], str)


def test_ingredient_chebi_id_extraction_prefers_identifier_when_chebi():
    doc = {"identifier": "CHEBI:17234"}
    assert ri._ingredient_chebi_id(doc) == "CHEBI:17234"


def test_ingredient_chebi_id_falls_back_to_ontology_mapping():
    doc = {"identifier": "MIM:00042", "ontology_mapping": {"ontology_id": "CHEBI:17234"}}
    assert ri._ingredient_chebi_id(doc) == "CHEBI:17234"


def test_ingredient_chebi_id_returns_none_when_no_chebi():
    assert ri._ingredient_chebi_id({}) is None
    assert ri._ingredient_chebi_id({"identifier": "MIM:00042"}) is None


# ---------------- template file itself ----------------


def test_role_template_references_all_new_placeholders():
    """The template must reference every new placeholder template_vars() emits, so
    that a template drift can be caught by test rather than silent empty renders.
    """
    template = (_REPO_ROOT / "templates" / "ingredient_role_research.md").read_text()
    for placeholder in (
        "{candidate_nutritional_roles}",
        "{candidate_physicochemical_roles}",
        "{candidate_cellular_metabolic_roles}",
        "{existing_role_assignments}",
        "{chebi_role_axioms}",
    ):
        assert placeholder in template, f"role template missing {placeholder!r}"


def test_role_template_names_the_three_facet_enums():
    """Guard that the enum names in the template stay aligned with mim_roles.yaml
    class names — a rename upstream would be caught here.
    """
    template = (_REPO_ROOT / "templates" / "ingredient_role_research.md").read_text()
    for enum_name in ("NutritionalRoleEnum", "PhysicochemicalRoleEnum", "CellularMetabolicRoleEnum"):
        assert enum_name in template, f"role template missing enum name {enum_name}"


def test_role_template_shows_worked_yaml_example():
    """The fenced YAML block must appear so PaperQA has a shape to fill."""
    template = (_REPO_ROOT / "templates" / "ingredient_role_research.md").read_text()
    assert "```yaml" in template
    assert "role_research:" in template
    assert "nutritional_roles:" in template
    assert "reference_type: PEER_REVIEWED_PUBLICATION" in template


# ---------------- Edison shim ----------------


roles_shim = _load("research_ingredient_roles_edison")


def test_shim_injects_template_when_missing():
    args = roles_shim._inject_defaults(["--target", "data/ingredients/mapped/foo.yaml"])
    assert "--template" in args
    template_idx = args.index("--template")
    assert args[template_idx + 1].endswith("templates/ingredient_role_research.md")


def test_shim_injects_out_dir_when_missing():
    args = roles_shim._inject_defaults(["--target", "x.yaml"])
    assert "--out-dir" in args
    out_idx = args.index("--out-dir")
    assert args[out_idx + 1].endswith("research/ingredients/roles")


def test_shim_preserves_user_template_override():
    args = roles_shim._inject_defaults([
        "--target", "x.yaml",
        "--template", "/custom/path/tpl.md",
    ])
    # Only ONE --template flag present, and it's the user's.
    assert args.count("--template") == 1
    assert "/custom/path/tpl.md" in args


def test_shim_preserves_user_out_dir_override():
    args = roles_shim._inject_defaults([
        "--target", "x.yaml",
        "--out-dir", "/tmp/scratch",
    ])
    assert args.count("--out-dir") == 1
    assert "/tmp/scratch" in args


def test_shim_dry_run_flag_passthrough():
    args = roles_shim._inject_defaults(["--target", "x.yaml", "--dry-run"])
    assert "--dry-run" in args


# ---------------- End-to-end template render (dry, no OAK, no API) ----------------


def test_template_renders_with_all_placeholders_filled(tmp_path):
    """Load the real roles template and .format_map it with real template_vars output.

    Fails LOUDLY if any placeholder in the template is missing from template_vars —
    even though _DefaultEmpty would silently swallow it in production, we want the
    test to catch this. Compare rendered length to a baseline; a missing placeholder
    would leave a `{name}` literal in the output.
    """
    doc = _minimal_doc()
    tv = ri.template_vars(doc, "mapped", "t")
    template = (_REPO_ROOT / "templates" / "ingredient_role_research.md").read_text()

    # Substitute — use plain format_map with a real dict (no _DefaultEmpty fallback),
    # so a missing placeholder would raise KeyError.
    rendered = template.format_map(tv)

    # No leftover `{placeholder}` literals from the top-level facets/existing/chebi keys.
    for leftover in (
        "{candidate_nutritional_roles}",
        "{candidate_physicochemical_roles}",
        "{candidate_cellular_metabolic_roles}",
        "{existing_role_assignments}",
        "{chebi_role_axioms}",
    ):
        assert leftover not in rendered, f"unrendered placeholder in output: {leftover}"

    # Rendered content should have the enum candidate values substituted in.
    assert "CARBON_SOURCE" in rendered
    assert "BUFFER" in rendered
    assert "SUBSTRATE" in rendered
