# `data/ingredients/mapped/Oatmeal.yaml`

## Verdict

Pass with minor issues. `Oatmeal` exact-maps to active `NCIT:C29298`
`Oatmeal Powder`, but the final SSSOM row still carries a stale
`UNKNOWN_TERM` validation stamp for a now-resolving NCIT term.

## Identity

- Reviewed record: `data/ingredients/mapped/Oatmeal.yaml`.
- Identifier and grounding: `identifier: NCIT:C29298` with
  `ontology_mapping.ontology_id: NCIT:C29298`, label `Oatmeal Powder`, source
  `NCIT`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: NCIT:C29298`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Synonyms: original `Oatmeal` plus CultureMech surface
  `Oatmeal (Quaker White Oats)`.
- Occurrences: 18 CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this NCIT-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `NCIT:C29298` as active `Oatmeal Powder`
  and lists `OATMEAL` as an exact synonym.
- The final SSSOM row maps `MIM:Oatmeal` exactly to `NCIT:C29298` and keeps
  `Oatmeal (Quaker White Oats)` as the only `other` token.
- The final SSSOM row's `validation_method` is still
  `none|UNKNOWN_TERM|2026-07-07`, and the hidden and ignored-inclusive search
  over `data/ingredients`, `data/curated`, `mappings`, `reports`, `docs`, and
  `UNIFIED_INGREDIENT_MAPPING.tsv` found historical invalid-CURIE reports for
  `NCIT:C29298` but no active missing-prefix triage row documenting the stamp.
- No unsupported roles, components, supplied forms, or environmental contexts
  are asserted.

## Completeness

- The active NCIT term, exact synonym, occurrence count, YAML synonym, and
  final SSSOM synonym agree.
- The live `Oatmeal agar` records remain separate unmapped media-formulation
  records, so they do not conflict with this oatmeal powder record.

## Recommended Edits

- Refresh the final SSSOM validation stamp for `MIM:Oatmeal` now that
  `NCIT:C29298` resolves under the active term validator, or add the NCIT row
  to `mappings/ingredient_mappings_unknown_term_triage.tsv` if the SSSOM
  synonym-review dispatcher still intentionally skips NCIT.
