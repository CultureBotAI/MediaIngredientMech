# `data/ingredients/mapped/Sugar.yaml`

## Verdict

Pass. The source label exact-matches active `NCIT:C71939`, the external-prefix
triage already records that NCIT-specific OLS resolves the row, and the final
SSSOM row has no unsafe `other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Sugar.yaml`.
- Identifier and grounding: `identifier: NCIT:C71939` with
  `ontology_mapping.ontology_id: NCIT:C71939`, label `Sugar`, source `NCIT`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 2 occurrences across 2 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sucrose` through `Sugars`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this NCIT record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh prefix-specific OLS4 lookup resolves active `NCIT:C71939` with label
  `Sugar` and exact synonym `Sugar`, matching the stored target and the
  existing external-prefix OLS triage row.
- `mappings/culturemech_recipe_membership.tsv` has the 2 expected
  `NCIT:C71939` recipe rows, agreeing with `total_occurrences: 2` and
  `media_count: 2`.
- The final SSSOM row exact-matches `NCIT:C71939` and leaves `other` empty.

## Completeness

- The NCIT identity, aggregate row, occurrence count, and final SSSOM row
  agree.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
