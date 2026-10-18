# `data/ingredients/mapped/Auraptene.yaml`

## Verdict

Pass. The CultureBotHT record exact-maps to `CHEBI:134355` `auraptene`, and the
CAS, formula, InChI, SMILES, IUPAC synonym, SSSOM row, and aggregate copy agree
with the current CHEBI term.

## Identity

- Reviewed record: `data/ingredients/mapped/Auraptene.yaml`.
- Identifier and grounding: `identifier: CHEBI:134355` with
  `ontology_mapping.ontology_id: CHEBI:134355`,
  `ontology_label: auraptene`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:134355` to non-obsolete `auraptene` with CAS xref
  `495-02-3`, formula `C19H22O3`, and the same InChI and SMILES stored on the
  record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Atrazin.yaml data/ingredients/mapped/Atrop_Abyssomicin_C.yaml data/ingredients/mapped/Auraptene.yaml data/ingredients/mapped/Aureothricin.yaml data/ingredients/mapped/Avermectin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Auraptene.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookup for `CHEBI:134355` resolved the expected non-obsolete term and
  confirmed its CAS, formula, InChI, SMILES, and exact IUPAC synonym.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 496 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` already record
  `CHEBI:134355` as confirmed with no curation action.
- The single exact synonym in YAML and SSSOM is the CHEBI exact IUPAC synonym.

## Completeness

- The exact identifier, CAS RN, formula, InChI, SMILES, IUPAC synonym,
  aggregate copy, and SSSOM row are populated.
- The 0/0 occurrence count is correct for a CultureBotHT-only compound not
  present in CultureMech recipe memberships.
- No roles, components, or literature references are required for this
  single-ingredient CultureBotHT import.

## Recommended Edits

- None.
