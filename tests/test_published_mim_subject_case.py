"""Every published `MIM:` subject must resolve to a live record (#299, #236).

## What #299 was actually protecting

`988029fa` realigned SSSOM subjects to their per-record filename stems. 64
already-published CURIEs moved -- `MIM:EDTA_Stock` became `MIM:Edta_Stock`,
`MIM:P-IV_Metal_Solution` became `MIM:P-iv_Metal_Solution`.

Nothing caught it. `validate_sssom_invariants` Rule B1 lowercases the subject
before comparing it to the registry mint, so it is blind to subject case by
construction (`test_registry_mint_is_invariant_to_subject_case` pins exactly that
property). Rules A/B2/B3, `reconcile_sssom`, `qc-duplicate-ids` and
`check_flat_export_coverage` never look at the subject slug at all.

The concrete harm was never the spelling. It was that the rename produced **no
alias trail**: `build_curie_alias_map` derived `mim_curie_aliases.tsv` from *git
file renames*, so renaming a subject without renaming its file emitted nothing,
and `docs/CURIE_STANDARD.md` section 5 -- which tells consumers to persist
`MIM:<name>` and resolve through that map -- would have left all 64 dangling.

So #299 reverted, and this file used to pin the 64 published spellings as a
literal table, holding the line until #236 decided whether `MIM:` slugs are
paths or opaque identifiers.

## What changed

**#236 is decided: subjects are derived from the filename stem.** That is what
`CURIE_STANDARD.md` section 1 always said -- *"The SSSOM subject is derived from
the ingredient YAML's filename stem ... Filenames move ... 113 changed a CURIE
and are published as aliases."* Subjects are expected to move; the alias map is
the designated mechanism, and `mim_curie_alias_seeds.tsv` now supplies the
retirements git cannot derive (escaping, case-only renames on a case-insensitive
filesystem, subjects recomputed from `preferred_term`).

With the trail supplied, #299's objection is answered, so this file no longer
pins spellings. It pins the property the spellings were standing in for: **no
published CURIE dangles.** That is strictly stronger -- the old table only
covered 64 known subjects, this covers all of them -- and it does not have to be
rewritten every time a filename legitimately changes.

The 64 are kept below as a regression cohort: they are the ones known to have
moved, so they are the ones most likely to lose their alias.
"""

from __future__ import annotations

import csv
from pathlib import Path

import pytest

from mediaingredientmech.curie import mim_curie_for_stem

ROOT = Path(__file__).resolve().parent.parent
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
ALIASES = ROOT / "mappings" / "mim_curie_aliases.tsv"

# (filename-stem spelling, spelling published before #236 was decided).
# Both must remain resolvable; which one the SSSOM currently carries depends on
# whether the rebuild has been promoted yet, so no test below asserts either.
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


@pytest.fixture(scope="module")
def aliases() -> dict[str, str]:
    with ALIASES.open(newline="", encoding="utf-8") as f:
        return {r["old_curie"]: r["current_curie"]
                for r in csv.DictReader(f, delimiter="\t")}


@pytest.fixture(scope="module")
def live() -> set[str]:
    return {mim_curie_for_stem(p.stem)
            for d in ("mapped", "unmapped")
            for p in (ROOT / "data" / "ingredients" / d).glob("*.yaml")}


def resolve(curie: str, aliases: dict[str, str], live: set[str]) -> str | None:
    """Follow the alias chain to a live record, or None. Cycle-safe."""
    seen: set[str] = set()
    cur = curie
    while cur not in live:
        if cur in seen or cur not in aliases:
            return None
        seen.add(cur)
        cur = aliases[cur]
    return cur


def test_every_published_subject_resolves_to_a_live_record(subjects, aliases, live):
    """The invariant the 64-row table was standing in for.

    A subject either names a record file directly or reaches one through the
    alias map. Anything else is a CURIE a consumer persisted that now resolves
    to nothing -- the failure #299 reverted a rename to avoid.
    """
    dangling = sorted(s for s in subjects if resolve(s, aliases, live) is None)

    assert not dangling, (
        f"{len(dangling)} published MIM: subject(s) resolve to no record and have "
        f"no alias: {dangling[:10]}. Add them to mappings/mim_curie_alias_seeds.tsv "
        f"and re-run scripts/build_curie_alias_map.py.")


@pytest.mark.parametrize("stem_spelling,published_spelling", CASE_MANGLED,
                         ids=[p for _, p in CASE_MANGLED])
def test_both_spellings_of_a_known_mover_still_resolve(
    stem_spelling, published_spelling, aliases, live
):
    """Whichever spelling a consumer holds, it must still reach the record.

    These 64 are the cohort known to have moved, so they are the ones whose
    alias is most likely to be dropped by a regeneration.
    """
    for spelling in (stem_spelling, published_spelling):
        assert resolve(spelling, aliases, live) is not None, (
            f"{spelling} resolves to nothing. Both spellings of a subject that has "
            f"moved must stay resolvable -- consumers persisted one of them.")


def test_the_cohort_is_the_full_set_299_measured():
    """64 subjects moved -- 62 in the diff #299 quotes plus 2 it folds into the two
    records promoted in the same commit. Pinning the count keeps a partial
    migration from passing."""
    assert len(CASE_MANGLED) == 64
    assert len({p for _, p in CASE_MANGLED}) == 64


def test_no_alias_points_at_a_dead_target(aliases, live):
    """`build_curie_alias_map` withholds dangling aliases; this pins that the
    published map stayed that way."""
    dead = sorted(old for old, new in aliases.items()
                  if resolve(new, aliases, live) is None)

    assert not dead, f"{len(dead)} alias target(s) resolve to no record: {dead[:10]}"
