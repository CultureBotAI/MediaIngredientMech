# `data/ingredients/mapped/Hydrogen_Peroxide.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived ChEBI mapping, structure fields, ChEBI
synonyms, CAS alias, and final SSSOM row all describe hydrogen peroxide.

## Identity

- Reviewed record: `data/ingredients/mapped/Hydrogen_Peroxide.yaml`.
- Identifier and grounding: `identifier: CHEBI:16240` with
  `ontology_mapping.ontology_id: CHEBI:16240`, label `hydrogen peroxide`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `7722-84-1`, formula `H2O2`, InChI
  `InChI=1S/H2O2/c1-2/h1-2H`, and SMILES `[H]OO[H]`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hydrastine_1r_9s.yaml data/ingredients/mapped/Hydro_Methylpteroylglutamylglutamic_Acid.yaml data/ingredients/mapped/Hydrocarbon.yaml data/ingredients/mapped/Hydrogen_Peroxide.yaml data/ingredients/mapped/Hydrogen_Sulfide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Hydrogen_Peroxide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1454`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1454`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:16240` as the active ChEBI class `hydrogen peroxide`
  and lists all four stored synonyms as exact synonyms.
- PubChem resolves CAS RN `7722-84-1` to `Hydrogen Peroxide`, formula `H2O2`,
  and the same InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Hydrogen_Peroxide` to `CHEBI:16240` and exports only the inspected
  ChEBI synonyms plus `CAS:7722-84-1` in `other`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and OAK/OLS review row
  marking the mapping `CONFIRMED`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonyms,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
