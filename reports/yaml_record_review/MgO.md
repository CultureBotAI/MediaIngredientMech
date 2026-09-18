# `data/ingredients/mapped/MgO.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:31794` magnesium oxide identity,
CultureMech residual occurrence count, restored SSSOM evidence, and final row
pass, but the record is missing the local chemistry/type backfill present on
older active CHEBI records.

Severity: minor.

## Identity

- Reviewed record: `data/ingredients/mapped/MgO.yaml`.
- Identifier and grounding: `identifier: CHEBI:31794` with
  `ontology_mapping.ontology_id: CHEBI:31794`, label `magnesium oxide`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- Occurrences: three CultureMech recipe occurrences.
- The record has not yet been classified with `ingredient_type` and has no
  local `chemical_properties` block.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Metronidazole` through `MgO`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:31794` as active `magnesium oxide` with `MgO` as a
  synonym.
- PubChem resolves `magnesium oxide` to CID 14792 with formula `MgO`, SMILES,
  and InChI.
- The residual triage row maps the missing CultureMech ingredient `MgO` to
  `CHEBI:31794`, and the record's restored `ontology_mapping.evidence` now
  carries `culturemech:output/ingredient_occurrences.tsv` so the final SSSOM
  row publishes that provenance.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:MgO` to
  `CHEBI:31794` with empty `other`.

## Completeness

- `reports/yaml_record_review_batch/validation_data.json` reports the missing
  local `molecular_formula`, `smiles`, and `inchi` fields for this record.
- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- Minor: backfill `ingredient_type: SINGLE_INGREDIENT` and
  `chemical_properties` from the active `CHEBI:31794` term in
  `data/ingredients/mapped/MgO.yaml`, then sync
  `data/curated/mapped_ingredients.yaml` and regenerate affected docs.
