# `data/ingredients/mapped/D-Leucrose.yaml`

## Verdict

Needs curation, with a major role-evidence issue. The local CAS fallback
identity, PubChem structure fields, 0/0 count, and exact CAS SSSOM row pass,
but `CARBON_SOURCE` is asserted only from a provisional name-pattern
computation and needs direct media-use evidence or removal.

## Identity

- Reviewed record: `data/ingredients/mapped/D-Leucrose.yaml`.
- Current identifier and grounding: `identifier: cas:7158-70-5`,
  `ontology_mapping.ontology_id: cas:7158-70-5`,
  `ontology_label: D-Leucrose`, `ontology_source: CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- A fresh exact OLS label/synonym search across CHEBI and NCIT found no exact
  D-Leucrose candidate.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `cas:7158-70-5` as its
  primary identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-Leucrose.yaml data/ingredients/mapped/D-Lysine.yaml data/ingredients/mapped/D-Maltose_Monohydrate.yaml data/ingredients/mapped/D-Mannose_6-phosphate_Sodium_Salt.yaml data/ingredients/mapped/D-Methionine.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-Lysine.yaml data/ingredients/mapped/D-Methionine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the two CHEBI-primary exact records in this batch. This record,
  `D-Maltose_Monohydrate`, and `D-Mannose_6-phosphate_Sodium_Salt` were
  intentionally skipped because their primary identifiers are CAS registry
  CURIEs.
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

- The record's CAS RN, PubChem CID, formula, InChI, and SMILES consistently
  describe the local D-Leucrose fallback identity.
- `mappings/culturemech_recipe_membership.tsv` contains no `cas:7158-70-5`
  rows, matching the record's 0/0 `occurrence_statistics`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` classifies the
  residual CAS `UNKNOWN_TERM` as an expected registry identifier.
- The final SSSOM row publishes
  `MIM:D-Leucrose skos:exactMatch cas:7158-70-5` with `CAS:7158-70-5` as the
  only `other` token.
- The `CARBON_SOURCE` facet is supported only by `COMPUTATIONAL_PREDICTION`
  from a curated name-pattern rule and its own `curator_note` calls it
  provisional.

## Completeness

- No exact CHEBI or NCIT replacement for D-Leucrose was found in live OLS, so
  the bounded fix is not a remapping.
- No parent mappings, synonyms, supplied-form assertions, or mixture
  components are asserted, so there are no unsupported secondary claims beyond
  the provisional nutritional role.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found the expected CAS-registry row and no curated
  exact ontology replacement for `cas:7158-70-5`.

## Recommended Edits

- In `data/ingredients/mapped/D-Leucrose.yaml`, either replace the
  computational `CARBON_SOURCE` evidence with direct CultureBotHT or
  source-backed media-role evidence for this ingredient, or remove the role
  facet; then rerun strict validation and the final SSSOM build.
