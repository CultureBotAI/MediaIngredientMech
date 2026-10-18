# `data/ingredients/mapped/Methylcobalamin.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:28115` methylcobalamin identity,
CultureMech residual occurrence, restored SSSOM evidence, and final SSSOM row
pass, but the record is missing the local chemistry/type backfill present on
older active CHEBI records.

Severity: minor.

## Identity

- Reviewed record: `data/ingredients/mapped/Methylcobalamin.yaml`.
- Identifier and grounding: `identifier: CHEBI:28115` with
  `ontology_mapping.ontology_id: CHEBI:28115`, label `methylcobalamin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Occurrences: one CultureMech recipe occurrence.
- The record has not yet been classified with `ingredient_type` and has no
  local `chemical_properties` block.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl_Methanesulfonate` through `Methylcobalamin`: exited 0 and wrote zero
  ERROR rows.
- `uv run linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:28115` as active `methylcobalamin` with formula
  `C63H91CoN13O14P`, CAS `13422-55-4`, SMILES, InChI, and the same canonical
  label used by the YAML.
- The residual triage rows map the missing CultureMech ingredient
  `methylcobalamin` to `CHEBI:28115`, and the record's restored
  `ontology_mapping.evidence` now carries
  `culturemech:output/ingredient_occurrences.tsv` so the final SSSOM row
  publishes that provenance.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Methylcobalamin` to `CHEBI:28115` with empty `other`.

## Completeness

- `reports/yaml_record_review_batch/validation_data.json` reports the missing
  local `molecular_formula`, `smiles`, and `inchi` fields for this record.
- `find` found no local `ingredient_occurrences.tsv`, and an
  `rg --no-ignore --hidden --glob '!.git'` search for `methylcobalamin` and
  `CHEBI:28115` under this checkout found only the residual-triage row, the
  curated record, generated products, backups, the ChEBI cache, and the unified
  mapping snapshot; ignored files were included.

## Recommended Edits

- Minor: backfill `ingredient_type: SINGLE_INGREDIENT` and
  `chemical_properties` from the active `CHEBI:28115` term in
  `data/ingredients/mapped/Methylcobalamin.yaml`, then sync
  `data/curated/mapped_ingredients.yaml` and regenerate affected docs.
