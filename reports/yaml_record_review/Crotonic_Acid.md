# `data/ingredients/mapped/Crotonic_Acid.yaml`

## Verdict

Pass. The merged record is grounded to active `CHEBI:41131` crotonic acid, its
CAS conflict was resolved to the current CHEBI xref, its 42/42 CultureMech
count matches the recipe-membership table, and the final SSSOM row contains
only true same-subject aliases.

## Identity

- Reviewed record: `data/ingredients/mapped/Crotonic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:41131`,
  `ontology_mapping.ontology_id: CHEBI:41131`, `ontology_label: crotonic acid`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `match_level: EXACT` by equality of the
  record and ontology identifiers.
- Live OLS lookup by `CHEBI:41131` returns active `CHEBI:41131` labelled
  `crotonic acid` with the trans-crotonic-acid synonyms curated on the record.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this active record using `CHEBI:41131` as a
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
  `scripts`, `tests`, and `reports` found the active `MIM:Crotonic_Acid` final
  SSSOM row, generated docs rows, and the OAK/OLS row-review confirmation for
  `CHEBI:41131`.
- The same searches also found `Na-crotonate` using `CHEBI:41131` as a
  `NARROW_MATCH` parent with a sibling local registry identity row, not as a
  second active exact crotonic-acid record.
- `mappings/culturemech_recipe_membership.tsv` contains 42 `CHEBI:41131`
  rows and a total occurrence sum of 42, matching `occurrence_statistics`
  `42/42`.
- The final SSSOM `other` tokens are ChEBI synonyms, the curated
  `CATALOG_VARIANT` surface `Crotonic acid (ALDRICH 113018)`, or the
  structured `CAS:107-93-7` value from `chemical_properties.cas_rn`. The raw
  `Role:` and `Properties:` import payloads remain filtered from the final
  SSSOM.
- The `CARBON_SOURCE` role is backed by the imported CultureMech role text
  rather than inferred from the compound name or ChEBI class.

## Completeness

- The ChEBI identifier, CAS RN, formula, InChI, SMILES, final SSSOM row,
  aggregate copy, occurrence count, and generated docs rows are populated and
  agree.
- The old duplicate `Crotonic_Acid_2.yaml` was absorbed by curation history and
  hidden/ignored-inclusive active-record search found no remaining duplicate
  primary identifier.

## Recommended Edits

- None.
