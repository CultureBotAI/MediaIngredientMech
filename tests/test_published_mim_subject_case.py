"""The 62+ published `MIM:` subjects that #299 caught being silently case-mangled.

`988029fa` realigned SSSOM subjects to their per-record filename stems. The stems
were written by an older sanitiser that title-cases every token, so acronyms came
out wrong -- `MIM:EDTA_Stock` became `MIM:Edta_Stock`, `MIM:P-IV_Metal_Solution`
became `MIM:P-iv_Metal_Solution`. 64 already-published CURIEs moved.

Nothing caught it. `validate_sssom_invariants` Rule B1 lowercases the subject
before comparing it to the registry mint, so it is blind to subject case by
construction (`test_registry_mint_is_invariant_to_subject_case` pins exactly that
property). Rules A/B2/B3, `reconcile_sssom`, `qc-duplicate-ids` and
`check_flat_export_coverage` never look at the subject slug at all.

And the rename produced no alias trail: `build_curie_alias_map` derives
`mappings/mim_curie_aliases.tsv` from *git file renames* under `data/ingredients/`,
so renaming a subject without renaming its file emits nothing.
`docs/CURIE_STANDARD.md` section 5 tells consumers to persist `MIM:<name>` and
resolve through that map, which would have left all 64 dangling.

The renames were reverted (#299 option 1): the published spellings stand, and the
subject/file drift stays at the 73 cases `main` already carries until #236 decides
whether `MIM:` slugs are paths or opaque identifiers.

This test pins the published spelling of each of the 64. It is deliberately a
literal table rather than a derived rule -- the whole failure was a rule that
looked equivalent to the corpus and was not.
"""

from __future__ import annotations

from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"

# (spelling introduced by 988029fa and reverted, published spelling that stands)
CASE_MANGLED = [
    ("MIM:84_GL_NaHCO3_Solution", "MIM:84_gL_NaHCO3_solution"),
    ("MIM:ATCC_Wolfes_Mineral_Mix", "MIM:ATCC_Wolfes_mineral_mix"),
    ("MIM:ATCC_Wolfes_Mineral_Mix_Minus_Iron", "MIM:ATCC_Wolfes_mineral_mix_minus_iron"),
    ("MIM:ATCC_Wolfes_Vitamin_Mix", "MIM:ATCC_Wolfes_vitamin_mix"),
    ("MIM:Bg-11_Trace_Metals_Solution", "MIM:BG-11_Trace_Metals_Solution"),
    ("MIM:Caso42h2osaturated_Solution", "MIM:CaSO42H2Osaturated_solution"),
    ("MIM:Carbon_Source_Solution", "MIM:Carbon_source_solution"),
    ("MIM:Cholesterol_Lipid_Concentrate", "MIM:Cholesterol_lipid_concentrate"),
    ("MIM:Das_Macro_Solution", "MIM:DAS_Macro_Solution"),
    ("MIM:Das_Vitamin_Cocktail", "MIM:DAS_Vitamin_Cocktail"),
    ("MIM:DL_Vitamins", "MIM:DL_vitamins"),
    ("MIM:Dyv_Metal_Solution", "MIM:DYV_Metal_Solution"),
    ("MIM:Edta_Stock", "MIM:EDTA_Stock"),
    ("MIM:Enrichment_Solution_For_Seawater_Medium", "MIM:Enrichment_Solution_for_Seawater_Medium"),
    ("MIM:Ferric_Malate_Solution", "MIM:Ferric_malate_solution"),
    ("MIM:G9_Trace_Metals_For_J_Medium", "MIM:G9_Trace_Metals_for_J_medium"),
    ("MIM:Glycine-NaOH_Buffer", "MIM:Glycine-NaOH_buffer"),
    ("MIM:Hans_1000x_Minerals", "MIM:Hans_1000x_minerals"),
    ("MIM:Hans_100x_Vitamins", "MIM:Hans_100x_vitamins"),
    ("MIM:K-phosphate_Buffer", "MIM:K-phosphate_buffer"),
    ("MIM:L-Cysteine_X_HCl_X_H2O_Solution", "MIM:L-Cysteine_x_HCl_x_H2O_solution"),
    ("MIM:LCFM_Carbon_Mix", "MIM:LCFM_Carbon_mix"),
    ("MIM:Legionella_Agar_Enrichment", "MIM:Legionella_agar_enrichment"),
    ("MIM:MES_Buffer", "MIM:MES_buffer"),
    ("MIM:Mwc_Metal_Solution", "MIM:MWC_Metal_Solution"),
    ("MIM:Macro_Component_1_For_J_Medium", "MIM:Macro_Component_1_for_J_Medium"),
    ("MIM:Macro_Component_2_For_J_Medium", "MIM:Macro_Component_2_for_J_medium"),
    ("MIM:Menadione_Solution", "MIM:Menadione_solution"),
    ("MIM:Metall_Salt_Sol_44", "MIM:Metall_salt_sol_44"),
    ("MIM:Micronutrient_Solution", "MIM:Micronutrient_solution"),
    ("MIM:Mineral_3B_Solution", "MIM:Mineral_3B_solution"),
    ("MIM:Mineral_3B_Solution_Minus_Nitrogen", "MIM:Mineral_3B_solution_minus_Nitrogen"),
    ("MIM:Mineral_3B_Solution_Minus_Phosphorus", "MIM:Mineral_3B_solution_minus_phosphorus"),
    ("MIM:Mineral_Salts_Base", "MIM:Mineral_salts_base"),
    ("MIM:Modified_P-iv_Chelated_Micronutrient_Solution", "MIM:Modified_P-IV_chelated_Micronutrient_Solution"),
    ("MIM:Modified_Trace_Vitamins", "MIM:Modified_trace_vitamins"),
    ("MIM:Murashige-Skoog_Basal_Salts", "MIM:Murashige-Skoog_basal_salts"),
    ("MIM:Na-phosphate_Buffer", "MIM:Na-phosphate_buffer"),
    ("MIM:Na2HPO4-KH2PO4_Buffer", "MIM:Na2HPO4-KH2PO4_buffer"),
    ("MIM:Na2HPO4-NaH2PO4_Buffer", "MIM:Na2HPO4-NaH2PO4_buffer"),
    ("MIM:P-ii_Metal_Solution", "MIM:P-II_Metal_Solution"),
    ("MIM:P-iv_Metal_Solution", "MIM:P-IV_Metal_Solution"),
    ("MIM:PIPES_Buffer", "MIM:PIPES_buffer"),
    ("MIM:Rumen_Fluid", "MIM:Rumen_fluid"),
    ("MIM:Salts_Solution", "MIM:Salts_solution"),
    ("MIM:Sea_Salts", "MIM:Sea_salts"),
    ("MIM:Skirrow_Supplement", "MIM:Skirrow_supplement"),
    ("MIM:Spir_Solution", "MIM:Spir_solution"),
    ("MIM:Steric_Solution", "MIM:Steric_solution"),
    ("MIM:Sulfur-free_DL_Minerals", "MIM:Sulfur-free_DL_minerals"),
    ("MIM:Sulfur_Free_Mineral_Mix", "MIM:Sulfur_free_mineral_mix"),
    ("MIM:TYG_Salts_Solution", "MIM:TYG_salts_solution"),
    ("MIM:Thauers_Vitamin_Mix", "MIM:Thauers_vitamin_mix"),
    ("MIM:Thauers_Vitamin_Mix_No_Biotin", "MIM:Thauers_vitamin_mix_no_Biotin"),
    ("MIM:Trace_Metal_Solution", "MIM:Trace_metal_solution"),
    ("MIM:Trace_Mineral_Solution", "MIM:Trace_mineral_solution"),
    ("MIM:Trace_Minerals", "MIM:Trace_minerals"),
    ("MIM:UW_Concentrated_Base", "MIM:UW_concentrated_base"),
    ("MIM:UW_Concentrated_Base_No_Mo", "MIM:UW_concentrated_base_no_Mo"),
    ("MIM:UW_Concentrated_Base_No_Sulfur", "MIM:UW_concentrated_base_no_sulfur"),
    ("MIM:Vitamins_Solution", "MIM:Vitamins_solution"),
    ("MIM:Wolfes_Mineral_Mix", "MIM:Wolfes_mineral_mix"),
    ("MIM:Wolfes_Mineral_Mix_minus_Nitrilotriacetic_acid", "MIM:Wolfes_mineral_mix_minus_Nitrilotriacetic_acid"),
    ("MIM:Wolfes_Vitamin_Mix", "MIM:Wolfes_vitamin_mix"),
]


@pytest.fixture(scope="module")
def subjects() -> set[str]:
    return {ln.split("\t", 1)[0] for ln in SSSOM.read_text(encoding="utf-8").splitlines()
            if ln.startswith("MIM:")}


@pytest.mark.parametrize("mangled,published", CASE_MANGLED,
                         ids=[p for _, p in CASE_MANGLED])
def test_published_subject_spelling_stands(mangled, published, subjects):
    assert published in subjects, (
        f"{published} has left the mapping set. It is a published CURIE; moving it "
        f"needs an alias row in mappings/mim_curie_aliases.tsv, not a silent rewrite.")
    assert mangled not in subjects, (
        f"{mangled} is back. It is the filename-stem spelling, which loses the "
        f"acronym case in {published}. See #299; #236 is still undecided.")


def test_the_table_is_the_full_set_299_measured():
    """64 subjects moved -- 62 in the diff #299 quotes plus 2 it folds into the two
    records promoted in the same commit. Pinning the count keeps a partial revert
    from passing."""
    assert len(CASE_MANGLED) == 64
    assert len({p for _, p in CASE_MANGLED}) == 64
