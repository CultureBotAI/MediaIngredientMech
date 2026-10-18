# `data/ingredients/mapped/Lipopolysaccharide.yaml`

## Verdict

Pass. The CultureBotHT exact CHEBI:16412 class identity, updated occurrence
count, empty final synonym payload, and final SSSOM row are internally
consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lipopolysaccharide.yaml`.
- Identifier and grounding: `identifier: CHEBI:16412` with
  `ontology_mapping.ontology_id: CHEBI:16412`, label `lipopolysaccharide`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The record has no curated formula, structure, CAS RN, or role facets.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lincomycin_Hydrochloride` through `Lithocholic_Acid`: exited 0 and wrote
  zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for all five
  CHEBI-grounded records in the batch.

## Evidence

- EBI OLS4 resolves `CHEBI:16412` as active `lipopolysaccharide`.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:16412` and has
  an empty `other` field.
- The aggregate `data/curated/mapped_ingredients.yaml` copy matches the
  per-record identity, refreshed three-recipe occurrence count, status, and
  mapping.

## Completeness

- The active CHEBI identity, aggregate copy, occurrence count, and final SSSOM
  row are present and consistent.
- No nutritional, physicochemical, cellular, environmental, structure, or CAS
  assertion is present.

## Recommended Edits

- None.
