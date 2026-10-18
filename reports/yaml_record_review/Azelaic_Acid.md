# `data/ingredients/mapped/Azelaic_Acid.yaml`

## Verdict

Pass. The CultureBotHT CAS lookup exact-maps to non-obsolete `CHEBI:48131`
`nonanedioic acid`, the CAS, formula, InChI, and SMILES all describe azelaic
acid, and the SSSOM row plus aggregate copy are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Azelaic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:48131` with
  `ontology_mapping.ontology_id: CHEBI:48131`,
  `ontology_label: nonanedioic acid`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:48131` to non-obsolete `nonanedioic acid`; its
  annotations include CAS `123-99-9`, formula `C9H16O4`, the same standard
  InChI and SMILES stored locally, and `Azelaic acid` as a synonym.
- PubChem lookup for CAS `123-99-9` resolves to title `Azelaic Acid`, formula
  `C9H16O4`, and the same standard InChI recorded locally.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Azacolutin.yaml data/ingredients/mapped/Azadirachtin.yaml data/ingredients/mapped/Azaserine.yaml data/ingredients/mapped/Azelaate.yaml data/ingredients/mapped/Azelaic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Azelaic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookup for `CHEBI:48131` and PubChem lookup for CAS `123-99-9`
  confirmed the exact acid identity and structure.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 510 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` confirm the
  `CHEBI:48131` OAK/OLS mapping.
- The record's CAS lookup provenance is consistent: the YAML curation history
  records CultureBotHT CAS `123-99-9`, `CHEBI:48131` resolution by OAK CHEBI
  CAS xref, and the later regrade to `CAS_RN_LOOKUP` because that lookup was
  the method that established the mapping.
- The ChEBI and PubChem structural values agree with the local chemical
  properties.

## Completeness

- The exact identifier, CAS, formula, InChI, SMILES, SSSOM row, and aggregate
  copy are populated.
- The 0/0 occurrence count is correct for a CultureBotHT-only compound not
  present in CultureMech recipe memberships.
- No supplied form, component list, roles, or environmental context is required
  for this exact acid record.

## Recommended Edits

- None.
