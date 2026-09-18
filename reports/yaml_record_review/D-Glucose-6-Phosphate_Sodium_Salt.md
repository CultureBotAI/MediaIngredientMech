# `data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml`

## Verdict

Needs curation, with a major role-evidence issue. The CAS primary identifier,
`skos:narrowMatch` to `CHEBI:14314`, exact CAS/kg-microbe registry rows, 1/1
occurrence count, and clean final SSSOM synonym payload pass, but
`CARBON_SOURCE` is asserted only from a provisional name-pattern computation.

## Identity

- Reviewed record:
  `data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml`.
- Current identifier and grounding: `identifier: cas:54010-71-8`,
  `ontology_mapping.ontology_id: CHEBI:14314`,
  `ontology_label: D-glucose 6-phosphate`, `ontology_source: CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:14314` returns active `CHEBI:14314` labelled
  `D-glucose 6-phosphate`, the parent of the sodium salt.
- A live exact CHEBI label/synonym search for the full sodium-salt label
  returned no exact candidate.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `cas:54010-71-8` as its
  primary identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml data/ingredients/mapped/D-Glucuronic_Acid_Gamma_Lactone.yaml data/ingredients/mapped/D-Glucuronic_Acid_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/D-Glutamic_Acid.yaml data/ingredients/mapped/D-Leucine.yaml`:
  passed; 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-Glucuronic_Acid_Gamma_Lactone.yaml data/ingredients/mapped/D-Glutamic_Acid.yaml data/ingredients/mapped/D-Leucine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary exact records in this batch.
  This record and `D-Glucuronic_Acid_Sodium_Salt_Monohydrate` were
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

- The record's CAS RN, PubChem CID, formula, InChI, and SMILES describe the
  sodium salt supplied form rather than the neutral `CHEBI:14314` parent.
- The #322 evidence records the parent repair from generic `sodium salt` to the
  named-compound parent `D-glucose 6-phosphate`.
- The final SSSOM publishes a `skos:narrowMatch CHEBI:14314` parent row and
  exact CAS and kg-microbe registry rows; only `CAS:54010-71-8` appears in
  `other`.
- The `CARBON_SOURCE` facet is supported only by `COMPUTATIONAL_PREDICTION`
  from a curated name-pattern rule and its own `curator_note` calls it
  provisional.

## Completeness

- No exact CHEBI replacement for the sodium salt was found in live OLS, so the
  bounded fix is not a remapping.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found the expected parent, CAS-registry, and
  row-review surfaces and no curated exact CHEBI successor for this sodium
  salt.

## Recommended Edits

- In `data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml`, either
  replace the computational `CARBON_SOURCE` evidence with direct source-backed
  media-role evidence for this sodium salt, or remove the role facet; then
  rerun strict validation and the final SSSOM build.
