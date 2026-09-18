# `data/ingredients/mapped/Balhimycin.yaml`

## Verdict

Pass. The exact `CHEBI:47250` identity, reviewed microbedecoder import,
source-occurrence trace, ChEBI structure fields, SSSOM row, and aggregate copy
all describe balhimycin.

## Identity

- Reviewed record: `data/ingredients/mapped/Balhimycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:47250` with
  `ontology_mapping.ontology_id: CHEBI:47250`,
  `ontology_label: balhimycin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search in `chebi` resolves `CHEBI:47250` to `balhimycin`.
- PubChem resolves the `Balhimycin` name to formula `C66H73Cl2N9O24`, matching
  the ChEBI-backed formula stored on the record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Baicalein.yaml data/ingredients/mapped/Bakers_Yeast.yaml data/ingredients/mapped/Balhimycin.yaml data/ingredients/mapped/Bandamycin.yaml data/ingredients/mapped/Bathocuproine_Disulfonic_Acid_Disodium_Salt.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Balhimycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 535 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/microbedecoder_auto_mapped_review.tsv` records the
  review-ingredients approval that promoted this exact-label CHEBI mapping out
  of `PENDING_REVIEW`.
- The `source_occurrences` entry is narrow and traceable: one
  `microbedecoder` occurrence from `BacDive_Metabolite_production`; recipe
  `total_occurrences` and `media_count` correctly remain zero.

## Completeness

- The exact CHEBI identifier, formula, InChI, SMILES, molecular weight,
  source-occurrence provenance, SSSOM row, and aggregate copy are populated.
- No CAS, role, component list, or supplied-form split is required for this
  single-compound microbedecoder import.

## Recommended Edits

- None.
