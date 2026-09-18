# `data/ingredients/mapped/Hydroxyurea.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived ChEBI mapping, structure fields, ChEBI
synonym, CAS alias, and final SSSOM row all describe hydroxyurea.

## Identity

- Reviewed record: `data/ingredients/mapped/Hydroxyurea.yaml`.
- Identifier and grounding: `identifier: CHEBI:44423` with
  `ontology_mapping.ontology_id: CHEBI:44423`, label `hydroxyurea`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `127-07-1`, formula `CH4N2O2`, InChI
  `InChI=1S/CH4N2O2/c2-1(4)3-5/h5H,(H3,2,3,4)`, and SMILES `NC(=O)NO`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hydroxyacetophenone.yaml data/ingredients/mapped/Hydroxyethylcellulose.yaml data/ingredients/mapped/Hydroxylamine_Hydrochloride.yaml data/ingredients/mapped/Hydroxystreptomycin.yaml data/ingredients/mapped/Hydroxyurea.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Hydroxyurea.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1510`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1510`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:44423` as the active ChEBI class `hydroxyurea` and
  lists `N-HYDROXYUREA` as an exact synonym.
- PubChem resolves CAS RN `127-07-1` to `Hydroxyurea`, formula `CH4N2O2`, and
  the same InChI stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Hydroxyurea`
  to `CHEBI:44423` and exports only the inspected ChEBI synonym plus
  `CAS:127-07-1` in `other`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and OAK/OLS review row
  marking the mapping `CONFIRMED`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
