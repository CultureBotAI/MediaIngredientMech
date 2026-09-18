# `data/ingredients/mapped/Cryptotanshinone.yaml`

## Verdict

Pass. The CultureBotHT record maps exactly to active `CHEBI:149838`
Cryptotanshinone, keeps the CultureBotHT CAS RN and ChEBI-derived structure
metadata in sync, and exports a final SSSOM row with only the structured CAS
alias.

## Identity

- Reviewed record: `data/ingredients/mapped/Cryptotanshinone.yaml`.
- Identifier and grounding: `identifier: CHEBI:149838`,
  `ontology_mapping.ontology_id: CHEBI:149838`,
  `ontology_label: Cryptotanshinone`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `match_level: EXACT` by equality of the record and ontology identifiers.
- Live OLS lookup by `CHEBI:149838` returns active `CHEBI:149838` labelled
  `Cryptotanshinone`.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this active record using `CHEBI:149838` as a
  primary identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cresol_Red.yaml data/ingredients/mapped/Crinamine.yaml data/ingredients/mapped/Crotonic_Acid.yaml data/ingredients/mapped/Crude_Oil.yaml data/ingredients/mapped/Cryptotanshinone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cresol_Red.yaml data/ingredients/mapped/Crinamine.yaml data/ingredients/mapped/Crotonic_Acid.yaml data/ingredients/mapped/Cryptotanshinone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-exact records in this batch. `Crude_Oil` was
  intentionally skipped because its ENVO primary identifier is outside this
  CHEBI-focused exact-label validation pass.
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

- Hidden/ignored-inclusive searches over `data`, `mappings`, `docs/data`,
  `scripts`, `tests`, and `reports` found the active `MIM:Cryptotanshinone`
  final SSSOM row, generated docs rows, and the OAK/OLS row-review
  confirmation for `CHEBI:149838`.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:149838` rows,
  which agrees with the CultureBotHT-only `0/0` `occurrence_statistics`.
- The final SSSOM `other` value is only `CAS:35825-57-1`, the structured CAS
  RN from `chemical_properties.cas_rn`.
- The record asserts no roles, components, supplied forms, or environment
  claims that require narrower supporting evidence.

## Completeness

- The ChEBI identifier, CAS RN, formula, InChI, SMILES, final SSSOM row,
  aggregate copy, and generated docs rows are populated and agree.
- `synonyms: []` is acceptable because no additional same-subject labels have
  been curated locally for this CultureBotHT import.

## Recommended Edits

- None.
