# `data/ingredients/mapped/Astromicin.yaml`

## Verdict

Pass. The MicrobeDecoder `astromicin` production label exact-maps to
`CHEBI:37923`, and the local formula, stereospecific InChI, SMILES, SSSOM row,
and aggregate copy match the current CHEBI term.

## Identity

- Reviewed record: `data/ingredients/mapped/Astromicin.yaml`.
- Identifier and grounding: `identifier: CHEBI:37923` with
  `ontology_mapping.ontology_id: CHEBI:37923`,
  `ontology_label: astromicin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:37923` to non-obsolete `astromicin` with CAS xref
  `55779-06-1`, formula `C17H35N5O6`, and the same stereospecific InChI and
  SMILES stored on the record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Asparagine.yaml data/ingredients/mapped/Aspartate.yaml data/ingredients/mapped/Astaxanthin.yaml data/ingredients/mapped/Astromicin.yaml data/ingredients/mapped/Atorvastatin_Calcium_Salt_Trihydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Astromicin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookup for `CHEBI:37923` resolved the expected non-obsolete term and
  confirmed the formula, InChI, and SMILES.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 492 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `data/custom/microbedecoder/unmapped_labels.tsv` preserves the raw
  `kgmicrobe.trait:astromicin` import label with count 1 in
  `BacDive_Metabolite_production`.
- `mappings/microbedecoder_auto_mapped_review.tsv` records the local
  post-import approval that promoted this exact CHEBI import from
  `PENDING_REVIEW` to `MAPPED`.

## Completeness

- The exact identifier, label, mapping quality, chemistry fields, source
  occurrence, aggregate copy, and SSSOM row are populated.
- The 0/0 CultureMech occurrence count is correct for a MicrobeDecoder-only
  record that has not appeared in CultureMech recipe memberships.
- No synonyms, roles, components, or literature references are required for the
  current record.

## Recommended Edits

- None.
