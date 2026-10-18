# `data/ingredients/mapped/Naphthalene_Sulfonic_Acid.yaml`

## Verdict

Pass. The curated exact `CHEBI:36336` naphthalenesulfonic acid mapping, 3/3
occurrence count, aggregate copy, and final exact SSSOM row agree after the
prior broad-parent repair.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Naphthalene_Sulfonic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:36336` with
  `ontology_mapping.ontology_id: CHEBI:36336`, label
  `naphthalenesulfonic acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 3 CultureMech recipe occurrences across 3 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Naphthalene_Sulfonic_Acid` through `Natamycin`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:36336` as active
  `naphthalenesulfonic acid` with the related synonym
  `naphthalenesulfonic acids`.
- The curation history records the important identity repair: the record was
  moved from broad sulfonic-acid parent `CHEBI:29214` and inherited
  sulfonic-acid chemistry to exact `CHEBI:36336`.
- The final SSSOM row maps `MIM:Naphthalene_Sulfonic_Acid` exactly to
  `CHEBI:36336`, uses the canonical object label, and emits an empty `other`
  column.

## Completeness

- The active CHEBI term, 3/3 occurrence count, aggregate copy, and final exact
  row agree.
- The record has no role, component, environment, or chemical-property
  assertions; those optional slots are appropriately empty for the current
  curated content.

## Recommended Edits

- None.
