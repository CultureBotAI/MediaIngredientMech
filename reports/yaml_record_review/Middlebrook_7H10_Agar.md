# `data/ingredients/mapped/Middlebrook_7H10_Agar.yaml`

## Verdict

Pass. The exact `NCIT:C85509` named Middlebrook 7H10 medium identity,
occurrence count, CultureMech catalog variant, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Middlebrook_7H10_Agar.yaml`.
- Identifier and grounding: `identifier: NCIT:C85509` with
  `ontology_mapping.ontology_id: NCIT:C85509`, label
  `Middlebrook 7H10 Growth Medium`, source `NCIT`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: NCIT:C85509`, and `ingredient_type: NAMED_MEDIUM`.
- Occurrences: five CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mgso4_X_7_H2o` through `Middlebrook_7H10_Agar`: exited 0 and wrote zero
  ERROR rows.
- Direct Engine A term validation was skipped for this NCIT record because
  NCIT is outside the CHEBI-focused LinkML term-validation pass used for this
  mixed batch.

## Evidence

- EBI OLS4 NCIT exact search resolves `NCIT:C85509` as active
  `Middlebrook 7H10 Growth Medium` with exact synonym
  `MIDDLEBROOK 7H10 AGAR`, distinct from `NCIT:C127518` Middlebrook 7H10S
  selective agar.
- The 2026-05-11 curation mapped the over-conflated agar source to the
  specific named NCIT medium rather than generic agar.
- The residual triage row maps `Middlebrook 7H10 Agar (Difco)` to the active
  `NCIT:C85509` Middlebrook 7H10 agar record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Middlebrook_7H10_Agar` to `NCIT:C85509` with the Difco catalog variant
  in `other`.

## Completeness

- The NCIT identity, named-medium ingredient type, occurrence count, catalog
  variant, and final SSSOM row are populated and agree.

## Recommended Edits

- None.
