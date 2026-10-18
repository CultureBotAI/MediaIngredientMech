# `data/ingredients/mapped/Bacitracin.yaml`

## Verdict

Pass. The CultureBotHT import exact-maps to non-obsolete `CHEBI:28669`
`bacitracin`, ChEBI carries the same CAS and peptide-mixture formula, and the
SSSOM row plus aggregate copy are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Bacitracin.yaml`.
- Identifier and grounding: `identifier: CHEBI:28669` with
  `ontology_mapping.ontology_id: CHEBI:28669`,
  `ontology_label: bacitracin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:28669` to non-obsolete `bacitracin`, defined as a mixture
  of closely related cyclic peptides, with CAS `1405-87-4` and formula
  `C63H98N14O14S`, matching the local chemical-property values.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bacitracin.yaml data/ingredients/mapped/Bacl2.yaml data/ingredients/mapped/Bacl2_X_2_H2o.yaml data/ingredients/mapped/Bacteriochlorophyll_A.yaml data/ingredients/mapped/Bacteriocin_Isk_1.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Bacitracin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookup for `CHEBI:28669` confirmed the active bacitracin identity, CAS,
  and mixture formula.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 521 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` confirm the
  `CHEBI:28669` OAK/OLS mapping.
- The record preserves the CultureBotHT CAS `1405-87-4` in
  `chemical_properties` and in the SSSOM `other` field.
- The 2026-08-27 occurrence refresh corrected the older importer count to 1/1
  from the distinct CultureMech recipe IDs in the refreshed occurrence table.

## Completeness

- The exact identifier, CAS, peptide-mixture formula, provisional
  `SELECTIVE_AGENT` role, occurrence count, SSSOM row, and aggregate copy are
  populated.
- No fixed InChI, SMILES, or molecular weight is required for this ChEBI
  mixture term.

## Recommended Edits

- None.
