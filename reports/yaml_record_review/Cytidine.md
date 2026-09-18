# `data/ingredients/mapped/Cytidine.yaml`

## Verdict

Pass. The FEBA/PubChem CAS-backed record maps to active `CHEBI:17562`, keeps
matching cytidine structure fields, has a refreshed 15/15 CultureMech
occurrence count, and exports only curated cytidine synonyms plus
`CAS:65-46-3` in the final SSSOM `other` column.

## Identity

- Reviewed record: `data/ingredients/mapped/Cytidine.yaml`.
- Current identifier and grounding: `identifier: CHEBI:17562`,
  `ontology_mapping.ontology_id: CHEBI:17562`,
  `ontology_label: cytidine`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:17562` returns active `CHEBI:17562` labelled
  `cytidine` with formula `C9H13N3O5` and matching InChI/SMILES strings.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:17562` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cycloviracin_B2.yaml data/ingredients/mapped/Cystargin.yaml data/ingredients/mapped/Cysteine.yaml data/ingredients/mapped/Cystine.yaml data/ingredients/mapped/Cytidine.yaml`:
  passed; 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cycloviracin_B2.yaml data/ingredients/mapped/Cysteine.yaml data/ingredients/mapped/Cystine.yaml data/ingredients/mapped/Cytidine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI exact records in this batch.
  `Cystargin` was intentionally skipped because its primary identifier is
  `mesh:C058276`, outside this CHEBI/OBO validation scope.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- The record's formula, InChI, SMILES, and CAS RN agree with the active
  `CHEBI:17562` cytidine identity selected by the recorded PubChem
  CAS-RN cross-reference.
- `mappings/culturemech_recipe_membership.tsv` contains 15 rows for
  `CHEBI:17562`, matching the record's refreshed 15/15
  `occurrence_statistics`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirms the OAK/OLS
  review row with no curation action required.
- The final SSSOM row publishes `MIM:Cytidine skos:exactMatch CHEBI:17562`
  under the CAS lookup grade allowed by `MAPPING_SEMANTICS.md` and carries only
  same-substance cytidine labels plus `CAS:65-46-3` in `other`.

## Completeness

- No roles, parent mappings, supplied-form assertions, or mixture components
  are asserted, so there are no unsupported secondary claims to adjudicate.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found the expected `NLDM_metabolites` component
  reference and no primary-record conflict for `CHEBI:17562`.

## Recommended Edits

- None for this record.
