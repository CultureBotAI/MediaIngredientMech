# `data/ingredients/mapped/Benzothiazole.yaml`

## Verdict

Needs curation, minor. The exact `CHEBI:45993` benzothiazole identity,
CultureMech residual provenance, restored SSSOM source, occurrence count, and
aggregate copy pass, but the record is missing `ingredient_type:
SINGLE_INGREDIENT`.

## Identity

- Reviewed record: `data/ingredients/mapped/Benzothiazole.yaml`.
- Identifier and grounding: `identifier: CHEBI:45993` with
  `ontology_mapping.ontology_id: CHEBI:45993`,
  `ontology_label: benzothiazole`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- OLS search in `chebi` returns `CHEBI:45993` as the `benzothiazole` class.
- PubChem resolves benzothiazole to formula `C7H5NS`; there is no salt,
  hydrate, stereochemical, or parent-term mismatch in the current mapping.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Benzoin.yaml data/ingredients/mapped/Benzothiazole.yaml data/ingredients/mapped/Benzyl_Alcohol.yaml data/ingredients/mapped/Benzyl_Isothiocyanate.yaml data/ingredients/mapped/Benzylcyanide.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Benzoin.yaml data/ingredients/mapped/Benzothiazole.yaml data/ingredients/mapped/Benzyl_Alcohol.yaml data/ingredients/mapped/Benzyl_Isothiocyanate.yaml data/ingredients/mapped/Benzylcyanide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five records.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 559 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/culturemech_residual_groundings.tsv` row 85 records the same single
  CultureMech residual mention and the same exact grounding to `CHEBI:45993`.
- The 2026-09-06 curation event restored the occurrence-table evidence into
  `ontology_mapping.evidence`, and the current SSSOM row includes
  `MIM:culturemech:output/ingredient_occurrences.tsv` in `source`.

## Completeness

- The exact CHEBI identifier, CultureMech occurrence evidence, 1/1 occurrence
  count, SSSOM row, and aggregate copy are populated.
- Minor gap: unlike older classified exact-CHEBI records with structural
  definitions, this residual-grounding record lacks `ingredient_type:
  SINGLE_INGREDIENT`.

## Recommended Edits

- Minor: set `ingredient_type: SINGLE_INGREDIENT` in
  `data/ingredients/mapped/Benzothiazole.yaml` through the normal classifier or
  a narrow single-record curation, then run `just sync-curated`.
