# `data/ingredients/mapped/Phoslactomycin.yaml`

## Verdict

Needs curation; major. The local `kgmicrobe.compound:phoslactomycin`
placeholder is intentionally retained for the phoslactomycin family label, but
`SELECTIVE_AGENT` is still supported only by a provisional name-list inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Phoslactomycin.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.compound:phoslactomycin` with matching
  `ontology_mapping.ontology_id`, label `Phoslactomycin`, source
  `kgmicrobe.compound`, `mapping_quality: PLACEHOLDER`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from
  `kg-microbe` metatraits unmapped placeholders.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- The row-review and unknown-term triage tables were inspected directly; they
  record `kgmicrobe.compound:phoslactomycin` as an expected local registry
  identifier pending curator promotion.
- A fresh OLS4 search for `phoslactomycin` across CHEBI, NCIT, MICRO, BTO,
  FOODON, and MeSH returned only specific phoslactomycin variants, not an
  unqualified phoslactomycin family class.
- The final SSSOM row was inspected directly and preserves the exact local
  `kgmicrobe.compound:phoslactomycin` registry identity.

## Evidence

- `mappings/ingredient_mappings_unknown_term_manual_candidate_review.tsv`
  already rejected promotion to variant-specific CHEBI candidates such as
  `CHEBI:207967`, `CHEBI:218976`, and `CHEBI:219060` because the source label
  is family-level.
- The record notes the same manual candidate review, and the final SSSOM row
  exports no `other` tokens.
- Major: the `SELECTIVE_AGENT` role is supported only by
  `COMPUTATIONAL_PREDICTION` evidence from a provisional curated name-pattern
  rule.

## Completeness

- The local placeholder identity is complete enough while no exact external
  phoslactomycin family term exists in the searched ontologies.
- Physicochemical-role evidence remains incomplete while the selective-agent
  role is provisional.

## Recommended Edits

- Major: in `data/ingredients/mapped/Phoslactomycin.yaml`, replace
  `physicochemical_roles.SELECTIVE_AGENT` with source-backed evidence or remove
  the provisional role facet until it is curated.
