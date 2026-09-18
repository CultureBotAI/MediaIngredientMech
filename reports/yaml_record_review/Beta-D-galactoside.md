# `data/ingredients/mapped/Beta-D-galactoside.yaml`

## Verdict

Pass. The exact `CHEBI:28034` beta-D-galactoside class identity, reviewed
microbedecoder provenance, class formula, SSSOM row, and aggregate copy all
agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Beta-D-galactoside.yaml`.
- Identifier and grounding: `identifier: CHEBI:28034` with
  `ontology_mapping.ontology_id: CHEBI:28034`,
  `ontology_label: beta-D-galactoside`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS search in `chebi` returns `CHEBI:28034` for the generic
  beta-D-galactoside class.
- The stored variable formula `C6H11O6R` is consistent with the class-level
  CHEBI identity rather than with one concrete PubChem compound.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Beta-Amyrin.yaml data/ingredients/mapped/Beta-D-fucose.yaml data/ingredients/mapped/Beta-D-galacto-pyranosyl-D-arabinose.yaml data/ingredients/mapped/Beta-D-galactoside.yaml data/ingredients/mapped/Beta-D-glucuronic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Beta-Amyrin.yaml data/ingredients/mapped/Beta-D-fucose.yaml data/ingredients/mapped/Beta-D-galactoside.yaml data/ingredients/mapped/Beta-D-glucuronic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-backed records.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 571 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/microbedecoder_auto_mapped_review.tsv` row 81 approved the
  `CHEBI:28034` mapping after local OAK resolution and case-insensitive
  canonical-label agreement.
- The current Engine A and OLS checks agree with the exact CHEBI class
  grounding.

## Completeness

- The exact CHEBI identifier, class formula, single-ingredient classification,
  SSSOM row, and aggregate copy are populated.
- `occurrence_statistics` correctly preserves a zero medium count with two
  microbedecoder source occurrences.
- No role, component list, or supplied-form split is required for this
  class-level carbohydrate record.

## Recommended Edits

- None.
