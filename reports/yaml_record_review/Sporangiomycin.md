# `data/ingredients/mapped/Sporangiomycin.yaml`

## Verdict

Needs curation - major. The MeSH exact identity resolves, but the
`SELECTIVE_AGENT` role is still a provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Sporangiomycin.yaml`.
- Identifier and grounding: `identifier: mesh:C003339` with
  `ontology_mapping.ontology_id: mesh:C003339`, label `sporangiomycin`, source
  `MESH`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 source occurrences across 0 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sporangiomycin` through `Stachyose_Hydrate`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this MeSH record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup in the MeSH ontology resolves `mesh:C003339` with label
  `sporangiomycin`, matching the stored exact target.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` records
  the same prefix-specific MeSH resolution; the older `UNKNOWN_TERM` row came
  from prefix-dispatch coverage rather than a bad identifier.
- The final SSSOM row exact-matches `mesh:C003339` and has empty `other`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is supported only by
  `COMPUTATIONAL_PREDICTION` from `infer_roles_from_name_lists`, with the
  provisional name-pattern curator note.

## Completeness

- The MeSH identity, aggregate row, and final SSSOM row agree.
- No unsupported active synonym, component, or final SSSOM payload was found;
  the only unsupported claim is the provisional selective-agent role.

## Recommended Edits

- Major: either remove `physicochemical_roles.SELECTIVE_AGENT` from
  `data/ingredients/mapped/Sporangiomycin.yaml`, or replace the name-pattern
  evidence with a source that explicitly uses sporangiomycin as a selective
  agent in a culture context.
