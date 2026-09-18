# `data/ingredients/mapped/Cytidine_5-Monophosphate.yaml`

## Verdict

Pass. The CultureBotHT row maps exactly to active `CHEBI:17361`, keeps
matching cytidine 5'-monophosphate structure fields, has the expected 0/0
CultureMech count, and exports a clean final SSSOM row with only a real exact
synonym and its own CAS alias in `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Cytidine_5-Monophosphate.yaml`.
- Current identifier and grounding: `identifier: CHEBI:17361`,
  `ontology_mapping.ontology_id: CHEBI:17361`,
  `ontology_label: cytidine 5'-monophosphate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:17361` returns active `CHEBI:17361` labelled
  `cytidine 5'-monophosphate` with formula `C9H14N3O8P` and matching
  InChI/SMILES strings.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:17361` as its primary
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

- The record's formula, InChI, SMILES, and CAS RN agree with live
  `CHEBI:17361`.
- `mappings/culturemech_recipe_membership.tsv` contains no `CHEBI:17361` rows,
  matching the record's 0/0 `occurrence_statistics`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirms the OAK/OLS
  review row with no curation action required.
- The final SSSOM row publishes
  `MIM:Cytidine_5-Monophosphate skos:exactMatch CHEBI:17361` and carries only
  `5'-cytidylic acid` plus `CAS:63-37-6` in `other`.

## Completeness

- No roles, parent mappings, supplied-form assertions, or mixture components
  are asserted, so there are no unsupported secondary claims to adjudicate.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found the expected row-review confirmations and no
  conflicting primary record for `CHEBI:17361`.

## Recommended Edits

- None for this record.
