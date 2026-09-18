# `data/ingredients/mapped/Cytosine.yaml`

## Verdict

Pass. The FEBA/PubChem CAS-backed record maps to active `CHEBI:16040`, keeps
matching cytosine structure fields, has the expected 20/20 CultureMech
occurrence count, and exports only curated cytosine synonyms plus `CAS:71-30-7`
in the final SSSOM `other` column.

## Identity

- Reviewed record: `data/ingredients/mapped/Cytosine.yaml`.
- Current identifier and grounding: `identifier: CHEBI:16040`,
  `ontology_mapping.ontology_id: CHEBI:16040`,
  `ontology_label: cytosine`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:16040` returns active `CHEBI:16040` labelled
  `cytosine` with formula `C4H5N3O` and matching InChI/SMILES strings.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:16040` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cytidine_5-Monophosphate.yaml data/ingredients/mapped/Cytisine.yaml data/ingredients/mapped/Cytochrome.yaml data/ingredients/mapped/Cytosine.yaml data/ingredients/mapped/Cytovirin.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cytidine_5-Monophosphate.yaml data/ingredients/mapped/Cytisine.yaml data/ingredients/mapped/Cytochrome.yaml data/ingredients/mapped/Cytosine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI exact records in this batch.
  `Cytovirin` was intentionally skipped because its primary identifier is a
  local `kgmicrobe.compound` placeholder.
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
  `CHEBI:16040` cytosine identity selected by the recorded PubChem
  CAS-RN cross-reference.
- `mappings/culturemech_recipe_membership.tsv` contains 20 rows for
  `CHEBI:16040`, matching the record's 20/20 `occurrence_statistics`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirms the OAK/OLS
  review row with no curation action required.
- The final SSSOM row publishes `MIM:Cytosine skos:exactMatch CHEBI:16040`
  under the CAS lookup grade allowed by `MAPPING_SEMANTICS.md` and carries only
  same-substance cytosine labels plus `CAS:71-30-7` in `other`.

## Completeness

- No roles, parent mappings, supplied-form assertions, or mixture components
  are asserted, so there are no unsupported secondary claims to adjudicate.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found the expected `NLDM_metabolites` component
  reference and no primary-record conflict for `CHEBI:16040`.

## Recommended Edits

- None for this record.
