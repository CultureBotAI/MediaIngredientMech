# `data/ingredients/mapped/D-Mannose_6-phosphate_Sodium_Salt.yaml`

## Verdict

Needs curation, with major role and final-SSSOM synonym issues. The CAS primary
identifier, PubChem chemistry, parent `CHEBI:17369`, 0/0 count, and CAS
registry rows pass, but final SSSOM publishes parent-level mannose
6-phosphate synonyms for the sodium salt, and `CARBON_SOURCE` is only
computationally supported.

## Identity

- Reviewed record:
  `data/ingredients/mapped/D-Mannose_6-phosphate_Sodium_Salt.yaml`.
- Current identifier and grounding: `identifier: cas:70442-25-0`,
  `ontology_mapping.ontology_id: CHEBI:17369`,
  `ontology_label: D-mannose 6-phosphate`, `ontology_source: CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:17369` returns active `CHEBI:17369` labelled
  `D-mannose 6-phosphate`, the parent without the sodium counterion.
- A live exact CHEBI/NCIT label/synonym search for the full sodium-salt label
  returned no exact candidate.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `cas:70442-25-0` as its
  primary identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-Leucrose.yaml data/ingredients/mapped/D-Lysine.yaml data/ingredients/mapped/D-Maltose_Monohydrate.yaml data/ingredients/mapped/D-Mannose_6-phosphate_Sodium_Salt.yaml data/ingredients/mapped/D-Methionine.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-Lysine.yaml data/ingredients/mapped/D-Methionine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the two CHEBI-primary exact records in this batch.
  This record, `D-Leucrose`, and `D-Maltose_Monohydrate` were intentionally
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
  sodium-salt supplied form rather than the `CHEBI:17369` parent.
- `mappings/culturemech_recipe_membership.tsv` contains no
  `cas:70442-25-0` rows, matching the record's 0/0 `occurrence_statistics`.
- The final SSSOM publishes a parent `CHEBI:17369` narrow row and exact CAS and
  kg-microbe registry rows.
- `Mannose-6-Phosphate` and `D-mannose 6-(dihydrogen phosphate)` are parent
  synonyms that omit the sodium counterion; publishing them in `other` for the
  sodium-salt subject erases the specificity preserved by the local CAS
  identity.
- The `CARBON_SOURCE` facet is supported only by `COMPUTATIONAL_PREDICTION`
  from a curated name-pattern rule and its own `curator_note` calls it
  provisional.

## Completeness

- No exact CHEBI or NCIT replacement for D-mannose 6-phosphate sodium salt was
  found in live OLS, so the bounded identity fix is not a remapping.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found the expected parent, CAS-registry, and
  row-review surfaces and no curated exact ontology successor for this sodium
  salt.

## Recommended Edits

- In `data/ingredients/mapped/D-Mannose_6-phosphate_Sodium_Salt.yaml`, remove
  or demote active parent synonyms that omit the sodium counterion so the final
  SSSOM no longer publishes them in `other`, then regenerate the final SSSOM.
- In the same record, either replace the computational `CARBON_SOURCE` evidence
  with direct source-backed media-role evidence, or remove the role facet; then
  rerun strict validation and the final SSSOM build.
