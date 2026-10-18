# `data/ingredients/mapped/Na-ascorbate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:113451` sodium ascorbate identity, CAS
provenance, occurrence count, accepted synonyms, structure, and final exact row
pass, but `VITAMIN_SOURCE` is only a provisional ChEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-ascorbate.yaml`.
- Identifier and grounding: `identifier: CHEBI:113451` with
  `ontology_mapping.ontology_id: CHEBI:113451`, label `sodium ascorbate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 38 CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-3-hydroxybutyrate` through `Na-ascorbate`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:113451` as active
  `sodium ascorbate`, with `cas:134-03-2`, formula `C6H7O6.Na`, the stored
  InChI/SMILES, and the curated sodium ascorbate synonyms.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Na-ascorbate` to `CHEBI:113451` with same-substance synonyms and
  `CAS:134-03-2` in `other`.
- Major: `nutritional_roles.VITAMIN_SOURCE` is supported only by
  `COMPUTATIONAL_PREDICTION` from ChEBI is-a/has-role closure and has a
  provisional curator note. The record needs inspected media-specific evidence
  before making the vitamin-source assertion.

## Completeness

- The active ChEBI target, CAS RN, structure, 38/38 occurrence count, accepted
  synonyms, and final row agree.
- Raw `Properties: ...` import strings remain only in YAML and are correctly
  filtered from final SSSOM `other`.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na-ascorbate.yaml`, replace the
  provisional `VITAMIN_SOURCE` inference with source-backed role evidence or
  remove the role. Re-run strict validation and final SSSOM validation after
  the repair.
