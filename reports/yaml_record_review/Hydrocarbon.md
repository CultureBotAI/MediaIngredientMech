# `data/ingredients/mapped/Hydrocarbon.yaml`

## Verdict

Needs curation. The exact ChEBI `hydrocarbon` identity passes, but
`degradation: hydrocarbon` is a process-qualified raw label and is currently
published as an SSSOM `other` synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Hydrocarbon.yaml`.
- Identifier and grounding: `identifier: CHEBI:24632` with
  `ontology_mapping.ontology_id: CHEBI:24632`, label `hydrocarbon`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hydrastine_1r_9s.yaml data/ingredients/mapped/Hydro_Methylpteroylglutamylglutamic_Acid.yaml data/ingredients/mapped/Hydrocarbon.yaml data/ingredients/mapped/Hydrogen_Peroxide.yaml data/ingredients/mapped/Hydrogen_Sulfide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Hydrocarbon.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1454`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1454`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:24632` as the active ChEBI class `hydrocarbon` and lists
  both `hydrocarbon` and `hydrocarbons` as exact synonyms.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Hydrocarbon`
  to `CHEBI:24632`.
- Major: `degradation: hydrocarbon` is a process-qualified trait/source label,
  not an exact synonym of the hydrocarbon chemical class, but it is stored as
  `RAW_TEXT` and exported beside the legitimate `hydrocarbons` synonym in the
  SSSOM `other` column.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and OAK/OLS review row
  marking the CHEBI mapping `CONFIRMED`.

## Completeness

- The active ChEBI identifier, exact plural synonym, aggregate copy, and final
  exact-match row are present and consistent.
- The record is incomplete until the process-qualified raw label is removed
  from the exported exact-synonym surface.

## Recommended Edits

- Major: remove `degradation: hydrocarbon` from active exported synonyms or
  keep it only as non-exported source provenance, regenerate the SSSOM, and
  rerun strict, term, round-trip, id-label, component, and SSSOM validation.
