# `data/ingredients/mapped/B-Glucan_From_Oat.yaml`

## Verdict

Pass. The CultureBotHT CAS lookup maps to non-obsolete `CHEBI:28793`
`beta-D-glucan`, ChEBI carries the same CAS and polymer formula, and the SSSOM
row plus aggregate copy are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/B-Glucan_From_Oat.yaml`.
- Identifier and grounding: `identifier: CHEBI:28793` with
  `ontology_mapping.ontology_id: CHEBI:28793`,
  `ontology_label: beta-D-glucan`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:28793` to non-obsolete `beta-D-glucan` with CAS
  `9041-22-9` and formula `C12H22O11(C6H10O5)n`, matching the local
  chemical-property values.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Azureomycin.yaml data/ingredients/mapped/B-Glucan_From_Oat.yaml data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml data/ingredients/mapped/BHI.yaml data/ingredients/mapped/Bacillomycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/B-Glucan_From_Oat.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookup for `CHEBI:28793` confirmed the CAS-backed beta-D-glucan
  identity and polymer formula.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 517 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv`,
  `mappings/ingredient_mappings_synonym_enrich_review.tsv`, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` confirm the
  `CHEBI:28793` mapping and report no additional synonym action.
- The 2026-08-24 regrade records why `CAS_RN_LOOKUP` is the right mapping grade:
  the record was created by explicit CAS-to-ChEBI lookup rather than a lexical
  lookup against the label `b-Glucan from Oat`.

## Completeness

- The exact identifier, CAS, polymer formula, provisional `CARBON_SOURCE` role,
  SSSOM row, and aggregate copy are populated.
- No fixed InChI, SMILES, or molecular weight is required for this polymeric
  class.
- The 0/0 occurrence count is correct for a CultureBotHT-only compound not
  present in CultureMech recipe memberships.

## Recommended Edits

- None.
