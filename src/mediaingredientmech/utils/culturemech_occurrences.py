"""Helpers for CultureMech occurrence-table rows."""

from __future__ import annotations

import re
from collections.abc import Mapping

AIR_DRIED_GARDEN_SOIL_ID = "kgmicrobe.ingredient:air-dried_garden_soil"
BETAINE_HYDRATE_ID = "CHEBI:91242"
CALCIUM_2_ID = "CHEBI:29108"
CALCIUM_SULFATE_HEPTAHYDRATE_ID = "kgmicrobe.compound:caso4_x_7_h2o"
COPPER_ID = "kgmicrobe.compound:copper"
DISODIUM_2_OXOGLUTARATE_ID = "kgmicrobe.compound:na2_alpha-ketoglutarate"
ELEMENTAL_SULFUR_ID = "CHEBI:33403"
EMIM_LYSINE_ID = "kgmicrobe.compound:1-ethyl-3-methylimidazolium_lysine"
IRON_0_ID = "CHEBI:82664"
LIPOIC_ACID_ID = "CHEBI:16494"
MAGNESIUM_2_ID = "CHEBI:18420"
MOLYBDENUM_ID = "kgmicrobe.compound:molybdenum"
POTASSIUM_SULFATE_HEPTAHYDRATE_ID = "kgmicrobe.compound:k2so4_x_7_h2o"
SODIUM_CROTONATE_ID = "kgmicrobe.compound:na-crotonate"
TETRAMETHYL_AMMONIUM_ID = "kgmicrobe.compound:tetramethyl_ammonium"
TRACE_ELEMENT_SOLUTION_ID = "kgmicrobe.ingredient:trace_element_solution"
TRACE_ELEMENT_SOLUTION_SL_10_ID = "kgmicrobe.ingredient:trace_element_solution_sl-10"
ZEIKUS_TRACE_ELEMENT_SOLUTION_ID = "kgmicrobe.ingredient:zeikus_trace_element_solution"


def _source_label_key(value: str) -> str:
    """Normalize exact source labels without making broad lexical guesses."""
    value = re.sub(r"\s*-\s*", "-", value.strip().casefold())
    value = re.sub(r"-+", "-", value)
    return re.sub(r"\s+", " ", value)


# CultureMech's vendored MIM label index can lag local MIM identity curation.
# These are source labels that CultureMech still resolves to a broader parent
# or retired local mint, but MIM now publishes as narrower records.
SOURCE_LABEL_IDENTIFIER_OVERRIDES = {
    _source_label_key("air-dried garden soil"): AIR_DRIED_GARDEN_SOIL_ID,
    _source_label_key("Betaine x H2O"): BETAINE_HYDRATE_ID,
    _source_label_key("1-ethyl-3-methylimidazolium lysine"): EMIM_LYSINE_ID,
    _source_label_key("Na-crotonate"): SODIUM_CROTONATE_ID,
    _source_label_key("Sodium crotonate"): SODIUM_CROTONATE_ID,
    _source_label_key("Elemental sulfur"): ELEMENTAL_SULFUR_ID,
    _source_label_key("Elemental sulphur"): ELEMENTAL_SULFUR_ID,
    _source_label_key("Na2 alpha-ketoglutarate"): DISODIUM_2_OXOGLUTARATE_ID,
    _source_label_key("Na2 α-ketoglutarate"): DISODIUM_2_OXOGLUTARATE_ID,
    _source_label_key("D,L-6,8-Thioctic Acid"): LIPOIC_ACID_ID,
    _source_label_key("Thioctic acid"): LIPOIC_ACID_ID,
    _source_label_key("α-lipoic acid"): LIPOIC_ACID_ID,
    _source_label_key("α--Lipoic acid"): LIPOIC_ACID_ID,
    _source_label_key("Sulfur"): ELEMENTAL_SULFUR_ID,
    _source_label_key("Sulfur (powder)"): ELEMENTAL_SULFUR_ID,
    _source_label_key("Sulfur, powder"): ELEMENTAL_SULFUR_ID,
    _source_label_key("Sulfur, powdered"): ELEMENTAL_SULFUR_ID,
    _source_label_key("Sulfur powder"): ELEMENTAL_SULFUR_ID,
    _source_label_key("Sulphur"): ELEMENTAL_SULFUR_ID,
    _source_label_key("Tetramethyl ammonium"): TETRAMETHYL_AMMONIUM_ID,
    _source_label_key("Trace element solution"): TRACE_ELEMENT_SOLUTION_ID,
    _source_label_key("Trace element solution SL-10"): TRACE_ELEMENT_SOLUTION_SL_10_ID,
    _source_label_key("Zeikus trace element solution"): ZEIKUS_TRACE_ELEMENT_SOLUTION_ID,
    _source_label_key("Calcium"): CALCIUM_2_ID,
    _source_label_key("CaSO4 x 7 H2O"): CALCIUM_SULFATE_HEPTAHYDRATE_ID,
    _source_label_key("Copper"): COPPER_ID,
    _source_label_key("Iron"): IRON_0_ID,
    _source_label_key("Magnesium"): MAGNESIUM_2_ID,
    _source_label_key("Molybdenum"): MOLYBDENUM_ID,
    _source_label_key("K2SO4 x 7 H2O"): POTASSIUM_SULFATE_HEPTAHYDRATE_ID,
    _source_label_key("K2SO4·7H2O"): POTASSIUM_SULFATE_HEPTAHYDRATE_ID,
    _source_label_key("K2SO4・7H2O"): POTASSIUM_SULFATE_HEPTAHYDRATE_ID,
}


def mim_identifier_for_occurrence(row: Mapping[str, str]) -> str:
    """Return the MIM identifier that should own one CultureMech occurrence row."""
    source_label = _source_label_key(row.get("preferred_term") or "")
    return SOURCE_LABEL_IDENTIFIER_OVERRIDES.get(
        source_label,
        (row.get("resolved_identifier") or "").strip(),
    )
