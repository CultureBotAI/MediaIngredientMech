# `data/ingredients/mapped/Hydroxyacetophenone.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI import, active generic
`hydroxyacetophenone` class, source-occurrence count, empty synonym set, and
final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Hydroxyacetophenone.yaml`.
- Identifier and grounding: `identifier: CHEBI:24668` with
  `ontology_mapping.ontology_id: CHEBI:24668`, label
  `hydroxyacetophenone`, source `CHEBI`, `mapping_quality: EXACT_MATCH`, and
  `mapping_status: MAPPED`.
- Source occurrences: one MicrobeDecoder occurrence from
  `bergey:minor_end_products`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hydroxyacetophenone.yaml data/ingredients/mapped/Hydroxyethylcellulose.yaml data/ingredients/mapped/Hydroxylamine_Hydrochloride.yaml data/ingredients/mapped/Hydroxystreptomycin.yaml data/ingredients/mapped/Hydroxyurea.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Hydroxyacetophenone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1510`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1510`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:24668` as the active ChEBI class
  `hydroxyacetophenone`, an acetophenone with at least one hydroxy substituent.
- The MicrobeDecoder source label exact-matches the ChEBI class label and does
  not specify one positional isomer. The hidden search also found the distinct
  para-isomer record `data/ingredients/mapped/4-Hydroxyacetophenone.yaml`, but
  no duplicate of this generic subject.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Hydroxyacetophenone` to `CHEBI:24668` and exports no `other` synonym
  noise.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and MicrobeDecoder review
  row.

## Completeness

- The active ChEBI identifier, MicrobeDecoder occurrence count, aggregate copy,
  and final SSSOM row are present and consistent.
- No unsupported roles or noisy final synonyms are asserted.

## Recommended Edits

- None.
