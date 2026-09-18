# `data/ingredients/mapped/D-Glucuronic_Acid_Sodium_Salt_Monohydrate.yaml`

## Verdict

Pass. The CAS primary identifier and PubChem chemistry preserve the sodium
monohydrate identity, `CHEBI:4178` is only a close anhydrous parent, and final
SSSOM exports clean close and CAS-registry rows without leaking the raw
`(sodium salt)` note into `other`.

## Identity

- Reviewed record:
  `data/ingredients/mapped/D-Glucuronic_Acid_Sodium_Salt_Monohydrate.yaml`.
- Current identifier and grounding: `identifier: cas:207300-70-7`,
  `ontology_mapping.ontology_id: CHEBI:4178`,
  `ontology_label: D-glucuronic acid`, `ontology_source: CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:4178` returns active `CHEBI:4178` labelled
  `D-glucuronic acid`, the anhydrous close-match parent, with an anhydrous
  formula `C6H10O7`.
- A live exact CHEBI label/synonym search for the full sodium-monohydrate label
  returned no exact candidate.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `cas:207300-70-7` as its
  primary identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml data/ingredients/mapped/D-Glucuronic_Acid_Gamma_Lactone.yaml data/ingredients/mapped/D-Glucuronic_Acid_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/D-Glutamic_Acid.yaml data/ingredients/mapped/D-Leucine.yaml`:
  passed; 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-Glucuronic_Acid_Gamma_Lactone.yaml data/ingredients/mapped/D-Glutamic_Acid.yaml data/ingredients/mapped/D-Leucine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary exact records in this batch.
  This record and `D-Glucose-6-Phosphate_Sodium_Salt` were intentionally
  skipped because their primary identifiers are CAS registry CURIEs.
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
  sodium monohydrate supplied form rather than the anhydrous `CHEBI:4178`
  parent.
- The `CLOSE_MATCH` regrade is appropriate because live `CHEBI:4178` is the
  anhydrous D-glucuronic acid parent, not this sodium monohydrate.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` records that the CAS
  and kg-microbe residual rows are expected registry identifiers rather than
  OAK/OLS ontology terms.
- The final SSSOM publishes
  `MIM:D-Glucuronic_Acid_Sodium_Salt_Monohydrate skos:closeMatch CHEBI:4178`
  and an exact `cas:207300-70-7` registry row; only `CAS:207300-70-7` appears
  in `other`.

## Completeness

- The raw `(sodium salt)` provenance in YAML is correctly filtered out of the
  published `other` synonym payload.
- No exact CHEBI replacement for the sodium monohydrate was found in live OLS,
  so the bounded fix is not a remapping.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found the expected parent, CAS-registry, and
  row-review surfaces and no curated exact CHEBI successor for this sodium
  monohydrate.

## Recommended Edits

- None for this record.
