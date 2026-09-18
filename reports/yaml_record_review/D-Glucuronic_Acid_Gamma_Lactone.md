# `data/ingredients/mapped/D-Glucuronic_Acid_Gamma_Lactone.yaml`

## Verdict

Pass. The CAS-backed identity maps exactly to active `CHEBI:18268`, keeps
matching D-glucurono-6,3-lactone structure fields, has the expected 0/0
CultureMech count, and exports a clean final SSSOM row with only its own CAS
alias in `other`.

## Identity

- Reviewed record:
  `data/ingredients/mapped/D-Glucuronic_Acid_Gamma_Lactone.yaml`.
- Current identifier and grounding: `identifier: CHEBI:18268`,
  `ontology_mapping.ontology_id: CHEBI:18268`,
  `ontology_label: D-glucurono-6,3-lactone`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:18268` returns active `CHEBI:18268` labelled
  `D-glucurono-6,3-lactone` with formula `C6H8O6` and matching InChI/SMILES
  strings.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:18268` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml data/ingredients/mapped/D-Glucuronic_Acid_Gamma_Lactone.yaml data/ingredients/mapped/D-Glucuronic_Acid_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/D-Glutamic_Acid.yaml data/ingredients/mapped/D-Leucine.yaml`:
  passed; 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-Glucuronic_Acid_Gamma_Lactone.yaml data/ingredients/mapped/D-Glutamic_Acid.yaml data/ingredients/mapped/D-Leucine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary exact records in this batch.
  `D-Glucose-6-Phosphate_Sodium_Salt` and
  `D-Glucuronic_Acid_Sodium_Salt_Monohydrate` were intentionally skipped
  because their primary identifiers are CAS registry CURIEs.
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

- The record's formula, InChI, SMILES, and CAS RN agree with active
  `CHEBI:18268`.
- `mappings/culturemech_recipe_membership.tsv` contains no `CHEBI:18268` rows,
  matching the record's 0/0 `occurrence_statistics`.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` records that the
  historical `D-Glucuronic acid gamma lactone` synonym-enrichment candidate is
  already represented by the preferred term.
- The final SSSOM row publishes
  `MIM:D-Glucuronic_Acid_Gamma_Lactone skos:exactMatch CHEBI:18268` under the
  CAS lookup grade allowed by `MAPPING_SEMANTICS.md` and carries only
  `CAS:32449-92-6` in `other`.

## Completeness

- No roles, active synonyms, parent mappings, supplied-form assertions, or
  mixture components are asserted, so there are no unsupported secondary claims
  to adjudicate.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found the expected row-review confirmations and no
  conflicting primary record for `CHEBI:18268`.

## Recommended Edits

- None for this record.
