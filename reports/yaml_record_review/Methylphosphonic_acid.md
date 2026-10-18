# `data/ingredients/mapped/Methylphosphonic_acid.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:45129` methylphosphonic-acid identity,
CultureMech residual occurrence, restored SSSOM evidence, and final SSSOM row
pass, but the record is missing the local chemistry/type backfill present on
older active CHEBI records.

Severity: minor.

## Identity

- Reviewed record: `data/ingredients/mapped/Methylphosphonic_acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:45129` with
  `ontology_mapping.ontology_id: CHEBI:45129`, label
  `methylphosphonic acid`, source `CHEBI`, `mapping_quality: EXACT_MATCH`, and
  `mapping_status: MAPPED`.
- Occurrences: one CultureMech recipe occurrence.
- The record has not yet been classified with `ingredient_type` and has no
  local `chemical_properties` block.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methylene_Blue` through `Methylxanthoxylin`: exited 0 and wrote zero ERROR
  rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:45129` as active `methylphosphonic acid` with
  formula `CH5O3P`, CAS `993-13-5`, SMILES, InChI, and the same canonical label
  used by the YAML.
- The residual triage rows map the missing CultureMech ingredient
  `Methylphosphonic acid` to `CHEBI:45129`, and the record's restored
  `ontology_mapping.evidence` now carries
  `culturemech:output/ingredient_occurrences.tsv` so the final SSSOM row
  publishes that provenance.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Methylphosphonic_acid` to `CHEBI:45129` with empty `other`.

## Completeness

- `reports/yaml_record_review_batch/validation_data.json` reports the missing
  local `molecular_formula`, `smiles`, and `inchi` fields for this record.
- `find` found no local `ingredient_occurrences.tsv`, and an
  `rg --no-ignore --hidden --glob '!.git'` search for `Methylphosphonic acid`
  and `CHEBI:45129` under this checkout found only the residual-triage row, the
  curated record, generated products, backups, the ChEBI cache, and the unified
  mapping snapshot; ignored files were included.

## Recommended Edits

- Minor: backfill `ingredient_type: SINGLE_INGREDIENT` and
  `chemical_properties` from the active `CHEBI:45129` term in
  `data/ingredients/mapped/Methylphosphonic_acid.yaml`, then sync
  `data/curated/mapped_ingredients.yaml` and regenerate affected docs.
