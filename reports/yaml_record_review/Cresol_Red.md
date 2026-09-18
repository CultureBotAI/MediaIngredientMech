# `data/ingredients/mapped/Cresol_Red.yaml`

## Verdict

Pass. The record is grounded to active `CHEBI:86218` cresol red, has
matching structure metadata and exact/related ChEBI synonyms, publishes a clean
final SSSOM row, and its 2/2 CultureMech occurrence count matches the current
recipe-membership table.

## Identity

- Reviewed record: `data/ingredients/mapped/Cresol_Red.yaml`.
- Identifier and grounding: `identifier: CHEBI:86218`,
  `ontology_mapping.ontology_id: CHEBI:86218`, `ontology_label: cresol red`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `match_level: EXACT` by equality of the
  record and ontology identifiers.
- Live OLS lookup by `CHEBI:86218` returns active `CHEBI:86218` labelled
  `cresol red` with the same related synonyms curated on the record.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this active record using `CHEBI:86218` as a
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
  `scripts`, `tests`, and `reports` found the active `MIM:Cresol_Red` final
  SSSOM row, generated docs rows, and the OAK/OLS row-review confirmation for
  `CHEBI:86218`.
- `mappings/culturemech_recipe_membership.tsv` contains two `CHEBI:86218`
  rows and a total occurrence sum of 2, matching `occurrence_statistics`
  `2/2`.
- The final SSSOM `other` tokens are ChEBI related/exact synonyms for
  `CHEBI:86218` or the structured `CAS:1733-12-6` value from
  `chemical_properties.cas_rn`.
- The record asserts no roles, components, supplied forms, or environment
  claims that require narrower supporting evidence.

## Completeness

- The ChEBI identifier, CAS RN, formula, InChI, SMILES, final SSSOM row,
  aggregate copy, occurrence count, and generated docs rows are populated and
  agree.
- No consequential gaps were found for this exact chemical record.

## Recommended Edits

- None.
