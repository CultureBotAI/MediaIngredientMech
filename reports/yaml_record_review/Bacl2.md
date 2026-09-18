# `data/ingredients/mapped/Bacl2.yaml`

## Verdict

Pass. The CultureMech `BaCl2` label is exact-mapped to non-obsolete
`CHEBI:63317` `barium chloride`, the CAS was corrected from an EC number to
ChEBI's CAS xref, and the structure, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Bacl2.yaml`.
- Identifier and grounding: `identifier: CHEBI:63317` with
  `ontology_mapping.ontology_id: CHEBI:63317`,
  `ontology_label: barium chloride`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:63317` to non-obsolete `barium chloride` with synonym
  `BaCl2`, CAS `10361-37-2`, formula `Ba.2Cl`, and the same InChI and SMILES
  stored locally.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bacitracin.yaml data/ingredients/mapped/Bacl2.yaml data/ingredients/mapped/Bacl2_X_2_H2o.yaml data/ingredients/mapped/Bacteriochlorophyll_A.yaml data/ingredients/mapped/Bacteriocin_Isk_1.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Bacl2.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookup for `CHEBI:63317` confirmed the exact anhydrous barium chloride
  identity, CAS, and structure.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 522 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` confirm the
  `CHEBI:63317` OAK/OLS mapping.
- The 2026-08-06 CAS audit replaced the invalid `233-788-1` EC/EINECS number
  with ChEBI's `10361-37-2` CAS xref, matching the active local CAS field and
  SSSOM `other` value.
- The exact synonyms `barium chloride` and `barium dichloride` are ChEBI or
  kg-microbe-supported labels for the same anhydrous salt.

## Completeness

- The exact identifier, CAS, formula, InChI, SMILES, trace-element role, 7/7
  occurrence count, SSSOM row, and aggregate copy are populated.
- The hydrate-specific `BaCl2 x 2 H2O` material is represented separately by
  `data/ingredients/mapped/Bacl2_X_2_H2o.yaml`.

## Recommended Edits

- None.
