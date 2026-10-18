# `data/ingredients/mapped/Bacl2_X_2_H2o.yaml`

## Verdict

Pass. The CultureMech hydrate label is exact-mapped to non-obsolete
`CHEBI:86153` `barium chloride dihydrate`, the hydrate-specific CAS, formula,
synonyms, SSSOM row, and aggregate copy all agree, and the record is distinct
from anhydrous `BaCl2`.

## Identity

- Reviewed record: `data/ingredients/mapped/Bacl2_X_2_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:86153` with
  `ontology_mapping.ontology_id: CHEBI:86153`,
  `ontology_label: barium chloride dihydrate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search resolves `barium chloride dihydrate` to `CHEBI:86153` with a
  definition identifying it as the dihydrate form of barium chloride.
- The local hydrate CAS `10326-27-9`, formula `Ba.2Cl.2H2O`, InChI, and SMILES
  are hydrate-specific and do not collapse to anhydrous `CHEBI:63317`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bacitracin.yaml data/ingredients/mapped/Bacl2.yaml data/ingredients/mapped/Bacl2_X_2_H2o.yaml data/ingredients/mapped/Bacteriochlorophyll_A.yaml data/ingredients/mapped/Bacteriocin_Isk_1.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Bacl2_X_2_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 exact lookup for `barium chloride dihydrate` confirmed the
  hydrate-specific `CHEBI:86153` target.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 523 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` confirm the
  `CHEBI:86153` OAK/OLS mapping.
- `mappings/hydrate_review.tsv` explicitly marks this as an established
  dihydrate whose CAS and ChEBI identity/formula agree.
- The SSSOM row preserves hydrate text aliases and `CAS:10326-27-9`.

## Completeness

- The exact hydrate identifier, CAS, formula, InChI, SMILES, hydrate synonyms,
  11/11 occurrence count, SSSOM row, and aggregate copy are populated.
- No additional parent component is required because the record denotes a
  single isolated hydrate form, not a mixture of free barium chloride and water.

## Recommended Edits

- None.
