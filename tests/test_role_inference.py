"""Tests for the three role-inference pipelines.

Covers the pure decision functions (no network / no CHEBI db needed) plus the
idempotency / compound-text behavior of the synonym extractor.
"""

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))


def _load(module_name: str):
    """Load a scripts/*.py module by path (scripts/ is not a package)."""
    spec = importlib.util.spec_from_file_location(
        module_name, ROOT / "scripts" / f"{module_name}.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


syn = _load("extract_roles_from_synonyms")
chebi = _load("infer_roles_from_chebi")
namelist = _load("infer_roles_from_name_lists")


# --- extract_roles_from_synonyms.extract_role_from_synonym -------------------

def test_synonym_single_role():
    roles, props = syn.extract_role_from_synonym(
        "Role: Buffer; Properties: Defined component, Inorganic compound"
    )
    assert roles == ["BUFFER"]
    assert "Defined component" in props


def test_synonym_compound_roles_split_on_comma():
    roles, _ = syn.extract_role_from_synonym(
        "Role: Buffer, Mineral source; Properties: Defined component"
    )
    assert roles == ["BUFFER", "MINERAL"]


def test_synonym_added_enum_values_map():
    # values added when REDUCING_AGENT/CHELATOR/indicators were introduced
    assert syn.extract_role_from_synonym("Role: Vitamin; Properties: x")[0] == ["VITAMIN_SOURCE"]
    assert syn.extract_role_from_synonym("Role: Reducing agent; Properties: x")[0] == ["REDUCING_AGENT"]
    assert syn.extract_role_from_synonym("Role: Antimicrobial agent; Properties: x")[0] == ["SELECTIVE_AGENT"]


def test_synonym_no_match_returns_empty():
    assert syn.extract_role_from_synonym("just some text") == ([], [])
    # unmapped role text yields no enum
    assert syn.extract_role_from_synonym("Role: Growth factor; Properties: x")[0] == []


def test_synonym_extraction_is_idempotent():
    from mediaingredientmech.curation.ingredient_curator import IngredientCurator

    curator = IngredientCurator(curator_name="test")
    record = {
        "identifier": "CHEBI:TEST",
        "preferred_term": "test salt",
        "mapping_status": "MAPPED",
        "synonyms": [
            {"synonym_text": "Role: Mineral source; Properties: Defined component",
             "synonym_type": "RAW_TEXT"},
        ],
    }
    first = syn.extract_roles_for_ingredient(curator, record)
    second = syn.extract_roles_for_ingredient(curator, record)
    assert first == 1
    assert second == 0  # re-run adds nothing
    assert [r["role"] for r in record["media_roles"]] == ["MINERAL"]


# --- infer_roles_from_chebi.infer_role ---------------------------------------

def test_chebi_clean_structural_rules():
    assert chebi.infer_role({"CHEBI:16646"}, "glucose")[0] == "CARBON_SOURCE"
    assert chebi.infer_role({"CHEBI:33709"}, "alanine")[0] == "AMINO_ACID_SOURCE"
    assert chebi.infer_role({"CHEBI:33229"}, "thiamine")[0] == "VITAMIN_SOURCE"


def test_chebi_ammonium_salt_is_nitrogen_not_mineral():
    role, _ = chebi.infer_role({"CHEBI:24839"}, "Ammonium chloride")
    assert role == "NITROGEN_SOURCE"


def test_chebi_skips_ambiguous_classes():
    # plain inorganic salt without ammonium -> not assigned (MINERAL deliberately dropped)
    assert chebi.infer_role({"CHEBI:24839"}, "sodium azide") == (None, None)
    # antimicrobial-agent role class is NOT used here
    assert chebi.infer_role({"CHEBI:33281"}, "1-octen-3-ol") == (None, None)
    # cofactor class is NOT used here
    assert chebi.infer_role({"CHEBI:23357"}, "hydrogen peroxide") == (None, None)


def test_chebi_precedence_vitamin_over_nothing():
    # vitamin + cofactor both present -> vitamin wins (cofactor not a rule)
    assert chebi.infer_role({"CHEBI:33229", "CHEBI:23357"}, "biotin")[0] == "VITAMIN_SOURCE"


# --- infer_roles_from_name_lists.infer_role ----------------------------------

@pytest.mark.parametrize("name,expected", [
    ("Ampicillin sodium salt", "SELECTIVE_AGENT"),
    ("Kanamycin sulfate", "SELECTIVE_AGENT"),
    ("Chloramphenicol", "SELECTIVE_AGENT"),
    ("EDTA", "CHELATOR"),
    ("Na2-EDTA x 2 H2O", "CHELATOR"),
    ("Nitrilotriacetic acid disodium salt", "CHELATOR"),
    ("Sodium dithionite", "REDUCING_AGENT"),
    ("DL-Dithiothreitol", "REDUCING_AGENT"),
    ("MgSO4 x 7 H2O", "MINERAL"),
    ("CuSO4 x 4 H2O", "MINERAL"),
    # extended categories
    ("HEPES", "BUFFER"),
    ("Phosphate buffer", "BUFFER"),
    ("Tris Acetate Stock Solution", "BUFFER"),
    ("Agar", "SOLIDIFYING_AGENT"),
    ("Peptone", "PROTEIN_SOURCE"),
    ("Yeast extract", "PROTEIN_SOURCE"),
    ("Tryptose", "PROTEIN_SOURCE"),        # peptone, not a sugar despite -ose
    ("Liver extract", "PROTEIN_SOURCE"),
    ("L-Asparagine monohydrate", "AMINO_ACID_SOURCE"),
    ("myo-Inositol", "VITAMIN_SOURCE"),
    ("Calcium D-Pantothenate", "VITAMIN_SOURCE"),
    ("D-Trehalose dihydrate", "CARBON_SOURCE"),
    ("Carboxymethyl cellulose", "CARBON_SOURCE"),
    ("Glycogen from bovine liver", "CARBON_SOURCE"),  # source organ != liver ingredient
    ("Malt extract", "CARBON_SOURCE"),
])
def test_namelist_positive(name, expected):
    assert namelist.infer_role(name) == expected


@pytest.mark.parametrize("name", [
    "Fe(III)-EDTA",            # metal-chelate complex -> iron source, not chelator
    "Sodium ferric EDTA",
    "Ferric citrate monohydrate",
    "Citrate",                 # ambiguous -> excluded
    "Dimethyl sulfide",        # volatile organosulfide, not a reductant additive
    # extended-category exclusions (matched a token but guarded out)
    "Brucella agar",           # agar-containing complete medium, not pure gelling agent
    "Malt Extract Agar",       # complete medium
    "Bacto Tryptic Soy Broth", # complete medium
    "Serine hydroxamate",      # serine analog/inhibitor, not an amino-acid source
    "L-alpha-Phosphatidylinositol from soybean",  # phospholipid, not a vitamin
    "4-Deoxypyridoxine",       # antivitamin
    "Lipopolysaccharide",      # endotoxin, not a carbon source
    "Glycerol monostearate",   # emulsifier ester, not a carbon source
])
def test_namelist_excluded(name):
    assert namelist.infer_role(name) is None
