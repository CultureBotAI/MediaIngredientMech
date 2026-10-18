# `data/ingredients/mapped/Benzoate.yaml`

## Verdict

Pass. The exact `CHEBI:16150` conjugate-base identity, reviewed microbedecoder
import, refreshed 2/2 occurrence count, ChEBI/PubChem structure fields, SSSOM
row, and aggregate copy all describe benzoate rather than neutral benzoic acid.

## Identity

- Reviewed record: `data/ingredients/mapped/Benzoate.yaml`.
- Identifier and grounding: `identifier: CHEBI:16150` with
  `ontology_mapping.ontology_id: CHEBI:16150`,
  `ontology_label: benzoate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search in `chebi` resolves `CHEBI:16150` to `benzoate` and defines
  it as the conjugate base of benzoic acid with charge -1.
- The record denotes benzoate, not the neutral `CHEBI:30746` benzoic acid
  record reviewed separately.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Benzbromarone.yaml data/ingredients/mapped/Benzene.yaml data/ingredients/mapped/Benzethonium_Chloride.yaml data/ingredients/mapped/Benzoate.yaml data/ingredients/mapped/Benzoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Benzoate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 556 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/microbedecoder_auto_mapped_review.tsv` records the
  review-ingredients approval that promoted this exact-label CHEBI mapping out
  of `PENDING_REVIEW`.
- Hidden/ignored-inclusive search found two `CHEBI:16150` rows in
  `mappings/culturemech_recipe_membership.tsv`, matching
  `occurrence_statistics: 2/2`.
- The `source_occurrences` entry is narrow and traceable: 31
  `microbedecoder` occurrences from `BacDive_Metabolite_utilization`.

## Completeness

- The exact CHEBI identifier, formula, InChI, SMILES, molecular weight,
  recipe occurrence count, source-occurrence provenance, SSSOM row, and
  aggregate copy are populated.
- No CAS, role, component list, or supplied-form split is required for this
  single-compound microbedecoder import.

## Recommended Edits

- None.
