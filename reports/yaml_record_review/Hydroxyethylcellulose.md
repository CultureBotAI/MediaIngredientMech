# `data/ingredients/mapped/Hydroxyethylcellulose.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI import, active
`hydroxyethylcellulose` class, source-occurrence count, empty synonym set, and
final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Hydroxyethylcellulose.yaml`.
- Identifier and grounding: `identifier: CHEBI:85249` with
  `ontology_mapping.ontology_id: CHEBI:85249`, label
  `hydroxyethylcellulose`, source `CHEBI`, `mapping_quality: EXACT_MATCH`, and
  `mapping_status: MAPPED`.
- Source occurrences: two MicrobeDecoder occurrences from
  `BacDive_Metabolite_utilization`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hydroxyacetophenone.yaml data/ingredients/mapped/Hydroxyethylcellulose.yaml data/ingredients/mapped/Hydroxylamine_Hydrochloride.yaml data/ingredients/mapped/Hydroxystreptomycin.yaml data/ingredients/mapped/Hydroxyurea.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Hydroxyethylcellulose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1510`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1510`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:85249` as the active ChEBI class
  `hydroxyethylcellulose`, a hydroxyethylated cellulose derivative.
- The MicrobeDecoder source label exact-matches the ChEBI label after
  case-normalization and does not introduce an unsupported hydrate, salt,
  stereochemical, mixture, catalog, or process boundary.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Hydroxyethylcellulose` to `CHEBI:85249` and exports no `other` synonym
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
