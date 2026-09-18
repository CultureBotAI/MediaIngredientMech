# `data/ingredients/mapped/Benzaldehyde.yaml`

## Verdict

Needs curation, minor. The exact `CHEBI:17169` benzaldehyde identity,
CultureMech residual provenance, restored SSSOM source, and aggregate copy pass,
but the record is missing `ingredient_type: SINGLE_INGREDIENT`.

## Identity

- Reviewed record: `data/ingredients/mapped/Benzaldehyde.yaml`.
- Identifier and grounding: `identifier: CHEBI:17169` with
  `ontology_mapping.ontology_id: CHEBI:17169`,
  `ontology_label: benzaldehyde`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- OLS exact search in `chebi` resolves `CHEBI:17169` to `benzaldehyde`.
- The record denotes benzaldehyde, matching the exact CultureMech residual
  label that produced the record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Beef_Heart.yaml data/ingredients/mapped/Beef_Heart_Infusion.yaml data/ingredients/mapped/Beijerincks_Solution.yaml data/ingredients/mapped/Benzaldehyde.yaml data/ingredients/mapped/Benzalkonium_Chloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Benzaldehyde.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 551 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/culturemech_residual_groundings.tsv` records the same two
  CultureMech mentions and the same new-record grounding to `CHEBI:17169`.
- The 2026-09-06 curation event restored the occurrence-table evidence into
  `ontology_mapping.evidence`, and the current SSSOM row includes
  `MIM:culturemech:output/ingredient_occurrences.tsv` in `source`.

## Completeness

- The exact CHEBI identifier, CultureMech occurrence evidence, SSSOM row, and
  aggregate copy are populated.
- Minor gap: unlike the older classified CHEBI records around it, this newer
  residual-grounding record lacks `ingredient_type: SINGLE_INGREDIENT`.

## Recommended Edits

- Minor: set `ingredient_type: SINGLE_INGREDIENT` in
  `data/ingredients/mapped/Benzaldehyde.yaml` through the normal classifier or
  a narrow single-record curation, then run `just sync-curated`.
